#!/usr/bin/env python3
"""Vaultrum - Area de Metricas - el instrumento.

Mide dos cosas distintas, y no las mezcla:

  EL PLAN      lo que el area ESCRIBE: un MET-XXX.n (plan de medicion) o un
               MET-XXX (lectura de la entrega). Se mide contra las leyes 1 a 6.
  EL DATO      lo que el juego DEVUELVE: un CSV de eventos. Se mide su calidad
               ANTES de leerlo, y despues se calcula solo lo que el dato permite
               afirmar. Todo lo que sale de aca es HECHO; interpretar es de 03.

  python3 metricas.py plan    <MET-XXX.n.md> [--verificar]
  python3 metricas.py lectura <MET-XXX.md>   [--verificar]
  python3 metricas.py datos   <eventos.csv>  [--plan MET.md] [--funnel a,b,c]
                                             [--dias 1,7,30] [--verificar]

Las seis leyes de la medicion (Area_metricas.md):
  1  objetivo antes que metrica
  2  un KPI se define entero, y no cambia despues de ver el dato
  3  todo KPI viaja con sus guardrails
  4  cada evento justifica su existencia
  5  la fase decide que se mide
  6  el dato dice que, no por que: se valida antes de leerse y se lee rotulado

CSV esperado (encabezado obligatorio, columnas extra = parametros):
  timestamp, player_id, event     obligatorias. timestamp ISO 8601 o epoch s
  session_id, version, environment  opcionales pero su falta se declara
  flow, currency, amount          eventos de recurso (flow = source | sink)

Sin dependencias: corre con el python del owner, en Windows o donde sea.
La prueba del instrumento es probar_metricas.py, en esta misma carpeta.
"""
import csv, datetime, os, re, sys, unicodedata
from collections import defaultdict, Counter
from statistics import median

# --------------------------------------------------------------- vocabulario
FASES = {
    'planning': 'Planning', 'planificacion': 'Planning',
    'pre-production': 'Pre-Production', 'preproduction': 'Pre-Production',
    'preproduccion': 'Pre-Production', 'pre-produccion': 'Pre-Production',
    'production': 'Production', 'produccion': 'Production',
    'testing': 'Testing',
    'pre-launch': 'Pre-Launch', 'prelaunch': 'Pre-Launch', 'soft launch': 'Pre-Launch',
    'soft-launch': 'Pre-Launch', 'prelanzamiento': 'Pre-Launch',
    'launch': 'Launch', 'lanzamiento': 'Launch',
    'post-launch': 'Post-Launch', 'postlaunch': 'Post-Launch',
    'postlanzamiento': 'Post-Launch', 'post-lanzamiento': 'Post-Launch',
    'live ops': 'Live Ops', 'liveops': 'Live Ops', 'live-ops': 'Live Ops',
}
# Donde rige el playtest, rige su tope: 13_Playtesting_y_validacion (Biblioteca).
FASES_PLAYTEST = {'Pre-Production', 'Production', 'Testing'}
TOPE_PLAYTEST = 10

# Ley 5 -- "ignorar la fase": KPIs que en esa fase no tienen poblacion que los sostenga.
_ESCALA = {'arpu', 'arpau', 'arppu', 'arpdau', 'ltv', 'dau', 'wau', 'mau', 'mrr',
           'roas', 'cpi', 'cac', 'cpa', 'ecpm', 'd30', 'stickiness'}
PREMATURO = {
    'Planning': _ESCALA | {'d1', 'd7', 'conversion', 'revenue'},
    'Pre-Production': _ESCALA,
    'Production': _ESCALA,
    'Testing': {'ltv', 'mrr', 'roas', 'cpi', 'cac', 'cpa', 'ecpm', 'arpdau'},
}
MODELOS = ('premium', 'free-to-play', 'f2p', 'freemium', 'hibrido', 'suscripcion',
           'subscription', 'ads', 'anuncios', 'ad-supported', 'no aplica')

KPI_CLAVES = ('nombre', 'formula', 'poblacion', 'ventana', 'fuente', 'baseline')
PII = re.compile(r'(^|_)(email|mail|nombre_real|real_name|full_name|telefono|phone|'
                 r'direccion|address|dni|documento|ip|ip_address|password|tarjeta|card|username|user_name|'
                 r'player_name|nombre_jugador)($|_)')
NOMBRE_EVENTO = re.compile(r'^[a-z][a-z0-9_]*$')
DINAMICO = re.compile(r'\d{2,}|\d{4}[_-]\d{2}|user\d|uid\d')
ROTULOS_LECTURA = ('hechos', 'interpretaciones', 'hipotesis', 'recomendacion', 'proxima medicion')
ESTADOS = ('cerrado', 'ajustar', 'pausado')


def plano(s):
    """minusculas, sin acentos, sin lo que va entre parentesis."""
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r'\(.*?\)', '', s.lower())
    return re.sub(r'\s+', ' ', s).strip()


# --------------------------------------------------------------- lectura del md
def secciones(txt):
    """{titulo_plano: cuerpo} de los ## del documento, ignorando bloques de codigo."""
    out, actual, buf, fence = {}, None, [], False
    for linea in txt.splitlines():
        if linea.strip().startswith('```'):
            fence = not fence
        if not fence and linea.startswith('## '):
            if actual is not None:
                out[actual] = '\n'.join(buf).strip()
            actual, buf = plano(linea[3:]), []
        elif actual is not None:
            buf.append(linea)
    if actual is not None:
        out[actual] = '\n'.join(buf).strip()
    return out


def buscar(secs, *claves):
    """cuerpo de la primera seccion cuyo titulo empiece por alguna clave."""
    for k in claves:
        for titulo, cuerpo in secs.items():
            if titulo.startswith(k):
                return cuerpo
    return None


def pares(cuerpo):
    """lineas 'clave: valor' -> {clave_plana: valor}."""
    d = {}
    for linea in (cuerpo or '').splitlines():
        m = re.match(r'^\s*[-*]?\s*([A-Za-zÁÉÍÓÚáéíóúñÑ ]+?)\s*:\s*(.+)$', linea)
        if m:
            d[plano(m.group(1))] = m.group(2).strip()
    return d


def items(cuerpo):
    return [l.strip()[1:].strip() for l in (cuerpo or '').splitlines()
            if l.strip()[:1] in '-*' and len(l.strip()) > 2]


def tabla(cuerpo):
    """filas de la primera tabla markdown: lista de dicts por encabezado plano."""
    filas = [l for l in (cuerpo or '').splitlines() if l.strip().startswith('|')]
    if len(filas) < 2:
        return []
    cab = [plano(c) for c in filas[0].strip().strip('|').split('|')]
    out = []
    for f in filas[2:]:
        celdas = [c.strip().strip('`') for c in f.strip().strip('|').split('|')]
        out.append(dict(zip(cab, celdas + [''] * (len(cab) - len(celdas)))))
    return out


def con_texto(cuerpo, minimo=4):
    return cuerpo is not None and len(re.findall(r'\w+', cuerpo)) >= minimo


VACIAS = {'del', 'las', 'los', 'por', 'que', 'con', 'sin', 'una', 'uno', 'para', 'the', 'and',
          'per', 'sobre', 'entre', 'cada', 'total', 'rate', 'tasa'}


def tokens_kpi(texto):
    """palabras que identifican una metrica: sin vacias, y las siglas cortas (d1, d7) se quedan."""
    return {t for t in re.findall(r'[a-z0-9]+', plano(texto))
            if t not in VACIAS and (len(t) >= 3 or re.match(r'^d\d+$', t))}


# --------------------------------------------------------------- el PLAN
def medir_plan(txt):
    """-> (fase, fallas). Cada falla: (ley, detalle)."""
    s = secciones(txt)
    f = []

    # Ley 1 -- objetivo antes que metrica
    if not con_texto(buscar(s, 'objetivo')):
        f.append(('Ley 1', 'no declara el Objetivo: sin objetivo, el KPI no mide nada'))
    if not con_texto(buscar(s, 'comportamiento esperado', 'comportamiento')):
        f.append(('Ley 1', 'no declara el Comportamiento esperado: que deberia cambiar en el jugador'))

    # Ley 2 -- el KPI entero
    kpi_txt = buscar(s, 'kpi primario', 'kpi')
    kpi = pares(kpi_txt)
    if kpi_txt is None:
        f.append(('Ley 2', 'no hay seccion KPI primario'))
    else:
        for c in KPI_CLAVES:
            if not kpi.get(c):
                f.append(('Ley 2', 'el KPI primario no declara "%s"%s' % (
                    c, ' (si no hay, se escribe "sin baseline" y por que)' if c == 'baseline' else '')))
        n = len(re.findall(r'^\s*[-*]?\s*nombre\s*:', kpi_txt or '', re.I | re.M))
        if n > 1:
            f.append(('Ley 2', 'declara %d KPI primarios: uno solo decide, los demas son secundarios' % n))

    # Ley 3 -- guardrails
    if not items(buscar(s, 'guardrail')) and not con_texto(buscar(s, 'guardrail'), 2):
        f.append(('Ley 3', 'sin guardrails: una mejora local puede romper el producto sin que nadie lo vea'))

    # Ley 5 -- la fase decide (se lee antes que la 4 porque la 4 depende de la fase)
    fase_txt = buscar(s, 'fase')
    fp = pares(fase_txt)
    fase = FASES.get(plano(fp.get('fase', '')).split(' ')[0] if fp.get('fase') else '', None)
    if fp.get('fase') and fase is None:
        fase = FASES.get(plano(fp['fase']))
    if fase is None:
        f.append(('Ley 5', 'fase no declarada o desconocida: se lee del cuaderno/TL, no se adivina'))
    modelo = plano(fp.get('modelo', ''))
    if not modelo or not any(modelo.startswith(m) for m in MODELOS):
        f.append(('Ley 5', 'modelo de negocio no declarado (o "no aplica — <por que>")'))
    if fase in PREMATURO:
        medidos = ' '.join(x or '' for x in (kpi_txt, buscar(s, 'metricas diagnosticas', 'diagnostic'),
                                           buscar(s, 'guardrail')))
        malos = sorted(tokens_kpi(medidos) & PREMATURO[fase])
        if malos:
            f.append(('Ley 5', 'ignorar la fase: %s en %s. No hay poblacion que lo sostenga todavia'
                      % (', '.join(m.upper() for m in malos), fase)))

    # Ley 4 -- cada evento justifica su existencia
    tp = buscar(s, 'tracking plan', 'plan de eventos', 'eventos')
    filas = tabla(tp)
    metricas_declaradas = tokens_kpi(' '.join(x or '' for x in (
        kpi.get('nombre', ''), buscar(s, 'metricas diagnosticas', 'diagnostic'), buscar(s, 'guardrail'))))
    if tp is None or not filas:
        f.append(('Ley 4', 'sin tracking plan en tabla: Evento | Disparo | Parametros | Pregunta | KPI'))
    for fila in filas:
        ev = fila.get('evento', '')
        if not ev:
            continue
        if not NOMBRE_EVENTO.match(ev):
            f.append(('Ley 4', '"%s": el nombre va en snake_case, sin espacios ni mayusculas' % ev))
        if DINAMICO.search(ev):
            f.append(('Ley 4', '"%s": valor dinamico dentro del nombre. Va como parametro' % ev))
        if not fila.get('pregunta'):
            f.append(('Ley 4', '"%s": no dice que pregunta responde' % ev))
        kp = fila.get('kpi', '')
        if not kp:
            f.append(('Ley 4', '"%s": no alimenta ninguna metrica' % ev))
        elif metricas_declaradas and not (tokens_kpi(kp) & metricas_declaradas):
            f.append(('Ley 4', '"%s": alimenta "%s", que no es ni el KPI, ni una diagnostica, ni un guardrail'
                      % (ev, kp)))
        for p in re.split(r'[,;·/ ]+', plano(fila.get('parametros', ''))):
            if p and PII.search(p):
                f.append(('Ley 4', '"%s": el parametro "%s" es dato personal. Minimizacion: afuera' % (ev, p)))
    eventos = [x.get('evento') for x in filas if x.get('evento')]
    if len(eventos) != len(set(eventos)):
        rep = [e for e, c in Counter(eventos).items() if c > 1]
        f.append(('Ley 4', 'eventos repetidos en el tracking plan: %s' % ', '.join(rep)))
    if fase in FASES_PLAYTEST and len(eventos) > TOPE_PLAYTEST:
        tope = re.search(r'tope\s*:\s*(\d+)\s*[—-]+\s*\S', fase_txt or '', re.I)
        if not tope or int(tope.group(1)) < len(eventos):
            f.append(('Ley 4', '%d eventos en %s: el tope de 13_Playtesting_y_validacion es %d. '
                      'Se baja, o se declara "tope: N — <razon>" en la seccion Fase'
                      % (len(eventos), fase, TOPE_PLAYTEST)))

    # Corolario -- el artefacto declara su estado
    est = buscar(s, 'estado')
    if not est or not any(e in plano(est) for e in ESTADOS):
        f.append(('Estado', 'no declara Cerrado / Ajustar / Pausado'))
    return fase, f, kpi.get('nombre', '')


# --------------------------------------------------------------- la LECTURA
def kpi_de_plan(ruta_lectura, txt_lectura):
    """Busca el/los MET-XXX.n que la lectura cita en su Insumo y devuelve sus KPI."""
    insumo = buscar(secciones(txt_lectura), 'insumo') or ''
    citados = set(re.findall(r'MET-\d+\.\d+', insumo))
    kpis, carpeta = {}, os.path.dirname(os.path.abspath(ruta_lectura))
    for nombre in sorted(os.listdir(carpeta)):
        m = re.match(r'(MET-\d+\.\d+)', nombre)
        if m and m.group(1) in citados and nombre.endswith('.md'):
            _, _, k = medir_plan(open(os.path.join(carpeta, nombre), encoding='utf-8').read())
            kpis[m.group(1)] = k
    return citados, kpis


def medir_lectura(ruta, txt):
    s = secciones(txt)
    f = []
    if not con_texto(buscar(s, 'insumo'), 1):
        f.append(('Ley 1', 'no declara su Insumo: que plan de medicion lee'))
    for r in ROTULOS_LECTURA:
        if not con_texto(buscar(s, r), 2):
            f.append(('Ley 6', 'falta la seccion "%s": hecho, interpretacion, hipotesis y recomendacion '
                      'van separados' % r))
    if not con_texto(buscar(s, 'calidad del dato', 'validacion del dato'), 2):
        f.append(('Ley 6', 'no declara la Calidad del dato: se valida antes de leerse'))
    citados, kpis = kpi_de_plan(ruta, txt)
    leido = pares(buscar(s, 'kpi primario', 'kpi')).get('nombre', '')
    if citados and not kpis:
        f.append(('Ley 2', 'cita %s y no esta en la carpeta: no se puede comprobar que el KPI no cambio'
                  % ', '.join(sorted(citados))))
    for met, k in kpis.items():
        if k and leido and plano(k) != plano(leido):
            f.append(('Ley 2', 'metric shopping: %s congelo "%s" y la lectura decide con "%s"'
                      % (met, k, leido)))
    est = buscar(s, 'estado')
    if not est or not any(e in plano(est) for e in ESTADOS):
        f.append(('Estado', 'no declara Cerrado / Ajustar / Pausado'))
    return f


# --------------------------------------------------------------- el DATO
def a_fecha(v):
    v = (v or '').strip()
    if not v:
        return None
    try:
        return datetime.datetime.fromtimestamp(float(v), tz=datetime.timezone.utc)
    except ValueError:
        pass
    try:
        d = datetime.datetime.fromisoformat(v.replace('Z', '+00:00'))
        return d if d.tzinfo else d.replace(tzinfo=datetime.timezone.utc)
    except ValueError:
        return None


def cargar_eventos(ruta):
    with open(ruta, encoding='utf-8-sig', newline='') as fh:
        lector = csv.DictReader(fh)
        cols = [c.strip() for c in (lector.fieldnames or [])]
        filas = [{(k or '').strip(): (v or '').strip() for k, v in r.items()} for r in lector]
    return cols, filas


def calidad(cols, filas, eventos_plan=None):
    """Ley 6, primera mitad: el dato se valida ANTES de leerse. -> (validas, hallazgos)"""
    h = []
    for c in ('timestamp', 'player_id', 'event'):
        if c not in cols:
            h.append(('bloqueante', 'falta la columna "%s"' % c))
    if any(x[0] == 'bloqueante' for x in h):
        return [], h
    for c in ('session_id', 'version', 'environment'):
        if c not in cols:
            h.append(('declarar', 'sin columna "%s": lo que depende de ella no se puede afirmar' % c))
    validas, invalidas, vistos, dup = [], 0, set(), 0
    for r in filas:
        t = a_fecha(r.get('timestamp'))
        if t is None or not r.get('player_id') or not r.get('event'):
            invalidas += 1
            continue
        clave = (r['player_id'], r.get('session_id', ''), r['event'], r['timestamp'])
        if clave in vistos:
            dup += 1
            continue
        vistos.add(clave)
        r = dict(r)
        r['_t'] = t
        validas.append(r)
    if invalidas:
        h.append(('invalido', '%d fila(s) sin timestamp legible, jugador o evento' % invalidas))
    if dup:
        h.append(('duplicado', '%d evento(s) duplicado(s) (mismo jugador, sesion, evento y instante). '
                  'Se descartan para medir; su causa es un defecto de telemetria' % dup))
    if 'environment' in cols:
        ents = Counter(r.get('environment') for r in validas)
        if len(ents) > 1:
            h.append(('contaminacion', 'mas de un entorno mezclado: %s' % dict(ents)))
    if 'version' in cols:
        vers = Counter(r.get('version') for r in validas)
        if len(vers) > 1:
            h.append(('declarar', 'mas de una version: %s. Comparar por version, no sumar' % dict(vers)))
    if eventos_plan:
        fuera = Counter(r['event'] for r in validas if r['event'] not in eventos_plan)
        if fuera:
            h.append(('fuera de plan', 'eventos que el tracking plan no declara: %s' % dict(fuera)))
        nunca = sorted(set(eventos_plan) - {r['event'] for r in validas})
        if nunca:
            h.append(('faltante', 'eventos del plan que nunca dispararon: %s' % ', '.join(nunca)))
    for r in validas:
        if r.get('flow') in ('source', 'sink'):
            try:
                if float(r.get('amount') or 0) < 0:
                    h.append(('signo', 'amount negativo en un evento de recurso: el signo lo da "flow", '
                              'no el numero. Con los dos, el neto se cuenta dos veces'))
                    break
            except ValueError:
                h.append(('invalido', 'amount no numerico en un evento de recurso'))
                break
    return validas, h


def pct(a, b):
    return None if not b else 100.0 * a / b


def retencion(validas, dias):
    """Dn clasica y rolling por cohorte de primer dia (UTC)."""
    dias_de = defaultdict(set)
    for r in validas:
        dias_de[r['player_id']].add(r['_t'].date())
    cohortes = defaultdict(list)
    for p, ds in dias_de.items():
        cohortes[min(ds)].append(p)
    ultimo = max((max(ds) for ds in dias_de.values()), default=None)
    out = []
    for dia0 in sorted(cohortes):
        jugadores = cohortes[dia0]
        fila = {'cohorte': dia0.isoformat(), 'n': len(jugadores)}
        for n in dias:
            objetivo = dia0 + datetime.timedelta(days=n)
            if ultimo is None or objetivo > ultimo:
                fila['D%d' % n] = None           # la ventana todavia no cerro: no es un cero
                continue
            clas = sum(1 for p in jugadores if objetivo in dias_de[p])
            roll = sum(1 for p in jugadores if any(d >= objetivo for d in dias_de[p]))
            fila['D%d' % n] = (pct(clas, len(jugadores)), pct(roll, len(jugadores)))
        out.append(fila)
    return out


def funnel(validas, pasos):
    """conversion paso a paso: jugadores que hicieron el paso i HABIENDO hecho el i-1 antes."""
    primero = defaultdict(dict)
    for r in sorted(validas, key=lambda x: x['_t']):
        primero[r['player_id']].setdefault(r['event'], r['_t'])
    out, prev = [], None
    for i, ev in enumerate(pasos):
        if i == 0:
            actuales = {p for p, e in primero.items() if ev in e}
        else:
            actuales = {p for p in prev if ev in primero[p] and primero[p][ev] >= primero[p][pasos[i - 1]]}
        out.append((ev, len(actuales), pct(len(actuales), len(prev)) if prev is not None else None))
        prev = actuales
    return out


def progresion(validas, cols):
    """triadas <x>_started / <x>_completed / <x>_failed, por id si hay una columna *_id."""
    col_id = next((c for c in cols if c.endswith('_id') and c not in ('player_id', 'session_id')), None)
    cuenta = defaultdict(Counter)
    for r in validas:
        m = re.match(r'^(.*)_(started|completed|failed)$', r['event'])
        if m:
            clave = (m.group(1), r.get(col_id, '') if col_id else '')
            cuenta[clave][m.group(2)] += 1
    # Una base es progresion solo si alguna vez TERMINA: wave_started sin wave_completed
    # es un marcador de tiempo, no un intento. Contarla daria "0% de completion" a algo
    # que nunca tuvo como completarse -- un numero correcto sobre el objeto equivocado.
    terminan = {b for (b, _), c in cuenta.items() if c['completed'] + c['failed'] > 0}
    out = []
    for (base, ident), c in sorted(cuenta.items()):
        if base not in terminan:
            continue
        terminados = c['completed'] + c['failed']
        out.append({'sistema': base, 'id': ident, 'starts': c['started'], 'completes': c['completed'],
                    'fails': c['failed'], 'completion': pct(c['completed'], c['started']),
                    'fail_sobre_terminados': pct(c['failed'], terminados),
                    'fail_sobre_starts': pct(c['failed'], c['started'])})
    return out


def economia(validas):
    flujo = defaultdict(lambda: [0.0, 0.0])
    for r in validas:
        if r.get('flow') in ('source', 'sink'):
            try:
                a = abs(float(r.get('amount') or 0))
            except ValueError:
                continue
            flujo[r.get('currency') or '?'][0 if r['flow'] == 'source' else 1] += a
    return {m: (s, k, s - k, (s / k) if k else None) for m, (s, k) in flujo.items()}


def sesiones(validas):
    por = defaultdict(list)
    for r in validas:
        if r.get('session_id'):
            por[(r['player_id'], r['session_id'])].append(r['_t'])
    dur = [(max(ts) - min(ts)).total_seconds() for ts in por.values() if len(ts) > 1]
    jugadores = Counter(p for p, _ in por)
    return len(por), (median(jugadores.values()) if jugadores else None), (median(dur) if dur else None)


def eventos_del_plan(ruta_plan):
    s = secciones(open(ruta_plan, encoding='utf-8').read())
    return [x.get('evento') for x in tabla(buscar(s, 'tracking plan', 'plan de eventos', 'eventos'))
            if x.get('evento')]


# --------------------------------------------------------------- salida
def fmt(v, suf='%'):
    return '—' if v is None else ('%.1f%s' % (v, suf))


def informe_datos(ruta, args):
    cols, filas = cargar_eventos(ruta)
    plan = args.get('--plan')
    validas, h = calidad(cols, filas, eventos_del_plan(plan) if plan else None)
    print('\n  METRICAS - lectura del dato: %s' % os.path.basename(ruta))
    print('  %d filas leidas, %d validas para medir\n' % (len(filas), len(validas)))
    print('  CALIDAD DEL DATO (Ley 6: se valida antes de leerse)')
    if not h:
        print('    [ok] sin hallazgos')
    for tipo, d in h:
        print('    [%s] %s' % (tipo, d))
    bloquea = [x for x in h if x[0] in ('bloqueante', 'duplicado', 'contaminacion', 'signo')]
    if not validas:
        print('\n  No hay dato medible.')
        return 1
    jugadores = len({r['player_id'] for r in validas})
    n_ses, ses_mediana, dur_mediana = sesiones(validas)
    print('\n  HECHOS (medidos sobre las filas validas, UTC)')
    print('    jugadores unicos        %d' % jugadores)
    if n_ses:
        print('    sesiones                %d  · mediana por jugador %s · duracion mediana %s'
              % (n_ses, ses_mediana, fmt(dur_mediana, ' s')))
    dias = [int(x) for x in args.get('--dias', '1,7,30').split(',') if x.strip()]
    ret = retencion(validas, dias)
    if ret:
        print('\n    retencion por cohorte   (clasica / rolling; — = la ventana no cerro)')
        for fila in ret:
            partes = []
            for n in dias:
                v = fila['D%d' % n]
                partes.append('D%d %s' % (n, '—' if v is None else '%s / %s' % (fmt(v[0]), fmt(v[1]))))
            print('      %s  n=%-4d %s' % (fila['cohorte'], fila['n'], '   '.join(partes)))
    if args.get('--funnel'):
        print('\n    funnel (conversion desde el paso anterior)')
        for ev, n, c in funnel(validas, [x.strip() for x in args['--funnel'].split(',')]):
            print('      %-28s %5d   %s' % (ev, n, fmt(c) if c is not None else 'inicio'))
    prog = progresion(validas, cols)
    if prog:
        print('\n    progresion              completion · fail/terminados · fail/starts')
        for p in prog:
            print('      %-18s %-10s starts %-4d %s · %s · %s' % (
                p['sistema'], p['id'] or '', p['starts'], fmt(p['completion']),
                fmt(p['fail_sobre_terminados']), fmt(p['fail_sobre_starts'])))
    eco = economia(validas)
    if eco:
        print('\n    economia                generado · hundido · neto · ratio source/sink')
        for m, (s, k, neto, ratio) in sorted(eco.items()):
            print('      %-10s %10.1f %10.1f %10.1f   %s' % (m, s, k, neto, fmt(ratio, '')))
    print('\n  LO QUE ESTE DATO NO PUEDE AFIRMAR')
    print('    por que paso lo medido: eso es interpretacion (03_Lector_Datos) y se rotula.')
    print('    causalidad: un antes/despues no la prueba sin control o sin descontar confounders.')
    if 'version' not in cols:
        print('    diferencias entre versiones: no hay columna version.')
    print()
    return 1 if bloquea else 0


def informe_md(modo, ruta):
    txt = open(ruta, encoding='utf-8').read()
    if modo == 'plan':
        fase, fallas, kpi = medir_plan(txt)
        print('\n  METRICAS - plan de medicion: %s' % os.path.basename(ruta))
        print('  fase %s · KPI primario "%s"' % (fase or '?', kpi or '?'))
    else:
        fallas = medir_lectura(ruta, txt)
        print('\n  METRICAS - lectura: %s' % os.path.basename(ruta))
    if not fallas:
        print('  EN LEY\n')
        return 0
    for ley, d in fallas:
        print('    [%s] %s' % (ley, d))
    print('\n  FUERA DE LEY: %d falla(s)\n' % len(fallas))
    return 1


def main(argv):
    if len(argv) < 3 or argv[1] not in ('plan', 'lectura', 'datos'):
        print(__doc__)
        return 2
    modo, ruta = argv[1], argv[2]
    args, i = {}, 3
    while i < len(argv):
        if argv[i] in ('--plan', '--funnel', '--dias') and i + 1 < len(argv):
            args[argv[i]] = argv[i + 1]
            i += 2
        else:
            args[argv[i]] = True
            i += 1
    rc = informe_datos(ruta, args) if modo == 'datos' else informe_md(modo, ruta)
    return rc if '--verificar' in args else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

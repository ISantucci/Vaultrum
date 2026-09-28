#!/usr/bin/env python3
"""Vaultrum - Area de Produccion - revision de fase y senales de parada (v1).

Un estudio no deja que una fase se cierre por inercia, ni que el trabajo nuevo se
apile sobre deuda que nadie mira. Hasta hoy Vaultrum hacia las dos cosas: la fase
era una etiqueta sin criterio de salida, y cuatro entregas seguidas de un mismo
proyecto cerraron en CONDITIONAL GO sin que nadie abriera el juego.

Este instrumento lee un proyecto de 06_Proyectos/ y contesta dos preguntas:

  SENALES DE PARADA   se puede abrir trabajo nuevo, o hay algo que frenar primero?
  SALIDA DE FASE      la fase declarada respondio su pregunta, y con que evidencia?

Las senales son de este archivo (S1..S9). El criterio de salida de cada fase NO:
vive en Flujos/05_Flujo_Revision_De_Fase.md y este instrumento lo LEE de ahi. Un
criterio escrito en dos lugares empieza a diferir en cuanto uno se edita, asi que
probar_fase.py verifica que la nota y el instrumento digan lo mismo.

  python3 fase.py <proyecto>                informe completo
  python3 fase.py <proyecto> --senales      solo las senales de parada
  python3 fase.py <proyecto> --salida       el caso de salida de la fase declarada
  python3 fase.py <proyecto> --verificar    exit 1 si hay una parada activa sin aceptar
  python3 fase.py 06_Proyectos --todos      un renglon por proyecto (revision periodica)

El instrumento NO decide. Arma el caso. Avanzar, seguir, volver o cortar lo decide
el owner, y la decision se escribe en el registro del cuaderno (seccion 5).

Lee la evidencia de otras dos areas sin repetir sus reglas:
  Control de Calidad  los bloques qa-* de cada QA de entrega (parser de calidad.py)
  Metricas            la existencia de una lectura MET-XXX (la del playtest)
"""
import os, re, sys, unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
FLUJO = os.path.normpath(os.path.join(AQUI, '..', 'Flujos', '05_Flujo_Revision_De_Fase.md'))
CALIDAD = os.path.normpath(os.path.join(AQUI, '..', '..', 'Area control de calidad', 'Herramientas'))
sys.path.insert(0, CALIDAD)
import calidad as Q  # noqa: E402  -- el parser de los bloques qa-* es de Calidad

RUIDO = {'.git', '.obsidian', '__pycache__', '.claude', '.agents', '.vaultrum', 'node_modules'}
ART = re.compile(r'^((TL|RQ|VE|QA|MET|GDS|LDS|UXS|SOL|EJ|ART)-(\d+))(?:\.(\d+[a-z]?))?_')
SUPERADO = re.compile(r'Superad[oa] por\s+`?TL-(\d+)', re.I)
NO_JUGABLE = re.compile(r'no\s+es\s+jugable|no\s+jugable|gds\s+no\s+aplica|no\s+pasa\s+por\s+game\s+design', re.I)
ARRANQUE_OK = re.compile(r'\barranque\s+(ok|si)\b', re.I)

FASES = ['Planning', 'Pre-Production', 'Production', 'Testing',
         'Pre-Launch', 'Launch', 'Post-Launch', 'Live Ops']
PREGUNTA = {
    'Planning':       'vale la pena construirlo?',
    'Pre-Production': 'funciona el nucleo?',
    'Production':     'los sistemas funcionan como deberian?',
    'Testing':        'el jugador real se comporta como esperaba el diseno?',
    'Pre-Launch':     'funciona como producto completo antes de escalar?',
    'Launch':         'que pasa con el mercado real, a escala?',
    'Post-Launch':    'como evoluciona?',
    'Live Ops':       'como se mantiene y mejora un producto vivo?',
}
ALIAS = {
    'planning': 'Planning', 'planificacion': 'Planning',
    'pre-production': 'Pre-Production', 'preproduction': 'Pre-Production',
    'pre production': 'Pre-Production', 'pre-produccion': 'Pre-Production',
    'preproduccion': 'Pre-Production', 'pre produccion': 'Pre-Production',
    'production': 'Production', 'produccion': 'Production',
    'testing': 'Testing',
    'pre-launch': 'Pre-Launch', 'prelaunch': 'Pre-Launch', 'pre launch': 'Pre-Launch',
    'soft launch': 'Pre-Launch', 'soft-launch': 'Pre-Launch',
    'launch': 'Launch', 'lanzamiento': 'Launch',
    'post-launch': 'Post-Launch', 'postlaunch': 'Post-Launch', 'post launch': 'Post-Launch',
    'live ops': 'Live Ops', 'liveops': 'Live Ops', 'live-ops': 'Live Ops',
}
CON_JUGADORES = {'Testing', 'Pre-Launch', 'Launch', 'Post-Launch', 'Live Ops'}
GRAVES = ('bloqueante', 'critico', 'mayor')
ABIERTOS = ('abierto', 'diferido')

# Las nueve senales. El codigo no cambia nunca: el registro del cuaderno lo cita.
SENALES = {
    'S1': 'fase sin declarar',
    'S2': 'cuaderno atrasado',
    'S3': 'entrega abierta debajo de otra',
    'S4': 'deuda arrastrada',
    'S5': 'defecto desaparecido',
    'S6': 'el juego no arranco',
    'S7': 'fase con jugadores sin playtest leido',
    'S8': 'codigo sin diseno',
    'S9': 'fase sin revisar',
}


# ------------------------------------------------------------------ lectura
def plano(s):
    """minusculas y sin acentos: 'Preproducción' -> 'preproduccion'."""
    s = unicodedata.normalize('NFKD', s.lower())
    return ''.join(c for c in s if not unicodedata.combining(c))


def leer(ruta):
    try:
        return open(ruta, encoding='utf-8', errors='replace').read()
    except OSError:
        return ''


def valor_de(txt, clave):
    """El valor de 'clave: valor' o '| clave | valor |', sin plantillas '<...>'."""
    for linea in txt.split('\n'):
        if '<' in linea:
            continue
        low = plano(linea)
        m = re.search(r'\b' + clave + r'\b\s*(?:\*\*)?\s*[:|]\s*(.+)', low)
        if m:
            v = re.sub(r'[*`_]', '', m.group(1)).strip(' |\t')
            if v:
                return v, linea.strip()
    return None, None


def fase_de(txt):
    """La fase declarada en el cuaderno. Solo cuenta si el valor ES una fase."""
    for linea in txt.split('\n'):
        if '<' in linea:
            continue
        low = plano(linea)
        m = re.search(r'\bfase(?:\s+del\s+producto)?\b\s*(?:\*\*)?\s*[:|]\s*(.+)', low)
        if not m:
            continue
        resto = re.sub(r'[*`_]', '', m.group(1)).strip(' |\t')
        for alias in sorted(ALIAS, key=len, reverse=True):
            if resto.startswith(alias) and not resto[len(alias):len(alias) + 1].isalnum():
                return ALIAS[alias]
    return None


def modelo_de(txt):
    v, _ = valor_de(txt, r'modelo(?:\s+de\s+negocio)?')
    return v


def filas_registro(txt):
    """Las filas de tabla del cuaderno que empiezan con un ID (PRJ-001, D-12...)."""
    out = []
    for linea in txt.split('\n'):
        s = linea.strip()
        if s.startswith('|') and re.match(r'^\|\s*[A-Za-z]+-\d+\s*\|', s):
            out.append(s)
    return out


class Proyecto:
    def __init__(self, carpeta):
        self.carpeta = os.path.abspath(carpeta)
        self.nombre = os.path.basename(self.carpeta.rstrip('/\\'))
        self.ruta_cuaderno = os.path.join(self.carpeta, self.nombre + '.md')
        self.cuaderno = leer(self.ruta_cuaderno)
        self.arts = []                     # (tipo, id, num, sub, rel, texto)
        for dp, dn, fn in os.walk(self.carpeta):
            dn[:] = sorted(d for d in dn if d not in RUIDO)
            for f in sorted(fn):
                if not f.endswith('.md'):
                    continue
                m = ART.match(f)
                if not m:
                    continue
                ruta = os.path.join(dp, f)
                rel = os.path.relpath(ruta, self.carpeta).replace('\\', '/')
                self.arts.append((m.group(2), m.group(1), int(m.group(3)), m.group(4), rel, leer(ruta)))
        self.fase = fase_de(self.cuaderno)
        self.modelo = modelo_de(self.cuaderno)
        self.registro = filas_registro(self.cuaderno)

    def de(self, tipo, sub=False):
        """Artefactos de un tipo. sub=False: solo los que no llevan .n."""
        out = [a for a in self.arts if a[0] == tipo and (sub is None or bool(a[3]) == sub)]
        return sorted(out, key=lambda a: (a[2], a[3] or ''))

    def tls(self):
        return self.de('TL')

    def superado(self, tl):
        return bool(SUPERADO.search(tl[5]))

    def tiene_ve(self, num):
        return any(v[2] == num for v in self.de('VE'))

    def qas_entrega(self):
        return self.de('QA')

    def ultimo(self, tipo):
        xs = self.de(tipo)
        return xs[-1] if xs else None


def defectos(qa):
    """{id: (severidad, estado)} de qa-defectos."""
    out = {}
    for f in Q.filas(Q.bloques(qa[5]).get('qa-defectos', [])):
        if len(f) >= 3 and f[0]:
            out[f[0]] = (plano(f[1]).strip(), plano(f[2]).strip())
    return out


def arranco(qa):
    return bool(ARRANQUE_OK.search(' '.join(Q.bloques(qa[5]).get('qa-humo', []))))


def veredicto(qa):
    d = Q.bloques(qa[5]).get('qa-decision', [])
    return d[0].strip() if d else 'sin veredicto'


# ------------------------------------------------------------------ senales
def senales(p):
    """[(codigo, nivel, detalle, como se levanta)]  nivel: parada | aviso"""
    out = []
    tls = p.tls()
    ve = p.ultimo('VE')
    qas = p.qas_entrega()

    # S1 -- sin fase, cualquier area que mida contesta la pregunta de otra fase
    if not p.fase:
        out.append(('S1', 'parada', 'el cuaderno no declara la fase del producto',
                    'Produccion la escribe en la seccion 3: "fase del producto: <una de las ocho>"'))

    # S2 -- el cuaderno es memoria; si no nombra lo ultimo, no es memoria de nada
    for ult in (tls[-1] if tls else None, ve):
        if ult and ult[1] not in p.cuaderno:
            out.append(('S2', 'parada', 'el cuaderno no nombra %s (%s)' % (ult[1], ult[4]),
                        'Produccion pone al dia las secciones 3 y 4 del cuaderno antes de responder'))

    # S3 -- una entrega sin cerrar debajo de otra abierta es trabajo que nadie valido
    for tl in tls:
        if hay_posterior(tls, tl) and not p.tiene_ve(tl[2]) and not p.superado(tl):
            out.append(('S3', 'parada', '%s no tiene VE y ya se abrio un timeline posterior' % tl[1],
                        'se cierra con su VE, o se declara "Superado por TL-XXX" en el timeline'))

    # S4 y S5 -- la deuda de Calidad, a traves de las entregas
    if qas:
        ultimo_qa = qas[-1]
        d_ult = defectos(ultimo_qa)
        previo = defectos(qas[-2]) if len(qas) > 1 else {}
        for bid, (sev, est) in sorted(d_ult.items()):
            if sev in GRAVES and est in ABIERTOS and previo.get(bid, ('', ''))[1] in ABIERTOS:
                racha = 0
                for q in reversed(qas):
                    s_e = defectos(q).get(bid)
                    if s_e and s_e[1] in ABIERTOS:
                        racha += 1
                    else:
                        break
                out.append(('S4', 'parada', '%s (%s, %s) lleva %d entregas seguidas abierto'
                            % (bid, sev, est, racha),
                            'se cierra con reverificacion, o el owner lo acepta por escrito para esta entrega'))
        ultima_vez = {}
        for q in qas:
            for bid, s_e in defectos(q).items():
                ultima_vez[bid] = (q, s_e)
        for bid, (q, (sev, est)) in sorted(ultima_vez.items()):
            if q is not ultimo_qa and est in ABIERTOS:
                nivel = 'parada' if sev in GRAVES else 'aviso'
                out.append(('S5', nivel, '%s (%s, %s en %s) no aparece en ningun QA posterior'
                            % (bid, sev, est, q[1]),
                            'el proximo QA de entrega lo lista: cerrado con reverificacion, o todavia abierto'))

        # S6 -- ninguna revision de fase vale sin el juego corriendo
        if p.fase != 'Planning':
            ultimos = qas[-2:]
            sin = [q for q in ultimos if not arranco(q)]
            if len(ultimos) == 2 and len(sin) == 2:
                out.append(('S6', 'parada', 'las dos ultimas entregas cerraron sin que el juego arrancara (%s)'
                            % ', '.join(q[1] for q in sin),
                            'el proximo QA de entrega arranca la build: "arranque ok" en qa-humo'))
            elif sin and sin[-1] is ultimo_qa:
                out.append(('S6', 'aviso', 'la ultima entrega (%s) cerro sin que el juego arrancara' % ultimo_qa[1],
                            'el proximo QA de entrega arranca la build'))

    # S7 -- de Testing en adelante, la evidencia sale de gente jugando
    if p.fase in CON_JUGADORES and not p.de('MET'):
        out.append(('S7', 'parada', 'la fase es %s y no hay ninguna lectura de playtest (MET-XXX)' % p.fase,
                    'Metricas escribe el plan (MET-XXX.n) y lee el playtest (MET-XXX)'))

    # S8 -- codigo que avanza sobre un requerimiento jugable sin diseno
    for tl in tls:
        if p.tiene_ve(tl[2]) or p.superado(tl):
            continue
        n = tl[2]
        hay_codigo = any(a[0] in ('SOL', 'EJ') and a[2] == n for a in p.arts)
        if not hay_codigo:
            continue
        for rq in [a for a in p.arts if a[0] == 'RQ' and a[2] == n and a[3]]:
            con_gds = any(a[0] == 'GDS' and a[2] == n and a[3] == rq[3] for a in p.arts)
            if not con_gds and not NO_JUGABLE.search(rq[5]):
                out.append(('S8', 'parada', '%s.%s ya tiene codigo y no tiene GDS ni declara que no es jugable'
                            % (rq[1], rq[3]),
                            'Game Design cierra su GDS, o Produccion declara en el RQ que no es jugable'))

    # S9 -- una entrega cerrada deja una pregunta: la fase sigue?
    if ve and not any('fase' in plano(f) and ve[1] in f for f in p.registro):
        out.append(('S9', 'parada', '%s cerro la entrega y nadie decidio si la fase sigue' % ve[1],
                    'revision de fase (fase.py --salida) y una fila en el registro: "fase: revision tras %s"'
                    % ve[1]))
    return aceptar(p, out)


def hay_posterior(tls, tl):
    return any(t[2] > tl[2] for t in tls)


def aceptadas(p):
    """{codigo: fila} -- paradas que el owner acepto por escrito para ESTA entrega.

    La fila nombra la senal y la ultima entrega (el VE, o el TL si todavia no hay VE)
    y esta Confirmada. Una aceptacion vale hasta la entrega siguiente: con un VE
    nuevo, se vuelve a decidir.
    """
    ve = p.ultimo('VE')
    tls = p.tls()
    ancla = ve[1] if ve else (tls[-1][1] if tls else None)
    out = {}
    if not ancla:
        return out
    for f in p.registro:
        low = plano(f)
        if ancla in f and 'confirmado' in low and 'parada' in low:
            for c in re.findall(r'\bs(\d)\b', low):
                out.setdefault('S' + c, f.split('|')[1].strip())
    return out


def aceptar(p, out):
    acc = aceptadas(p)
    return [(c, ('aceptada' if nivel == 'parada' and c in acc else nivel), det,
             ('aceptada por %s' % acc[c]) if nivel == 'parada' and c in acc else como)
            for (c, nivel, det, como) in out]


def activas(sen, excluir=()):
    return [s for s in sen if s[1] == 'parada' and s[0] not in excluir]


# ------------------------------------------------------------------ salida de fase
def criterios(ruta=FLUJO):
    """{fase: [(tipo, clave, texto)]} leido del flujo. tipo: medido | juicio."""
    txt = leer(ruta)
    if not txt:
        raise SystemExit('fase.py: no encuentro el criterio de salida en %s' % ruta)
    out, actual, dentro = {}, None, False
    nombres = {f.upper(): f for f in FASES}
    for linea in txt.split('\n'):
        if linea.strip().startswith('```'):
            dentro, actual = not dentro, None
            continue
        if not dentro or not linea.strip():
            continue
        if not linea.startswith(' '):
            cab = re.split(r'\s{2,}', linea.strip())[0]
            actual = nombres.get(cab)
            if actual:
                out.setdefault(actual, [])
            continue
        if actual:
            p = linea.split()
            if p[0] == 'medido' and len(p) >= 2:
                out[actual].append(('medido', p[1], ' '.join(p[2:])))
            elif p[0] == 'juicio':
                out[actual].append(('juicio', None, ' '.join(p[1:])))
    return out


def chequeos(p, sen):
    """clave -> (ok, evidencia). Las claves que el flujo puede pedir."""
    qas = p.qas_entrega()
    q = qas[-1] if qas else None
    d = defectos(q) if q else {}
    graves = sorted(b for b, (s, e) in d.items() if s in GRAVES and e in ABIERTOS)
    bloq = sorted(b for b, (s, e) in d.items() if s in ('bloqueante', 'critico') and e in ABIERTOS)
    abiertos_tl = [t[1] for t in p.tls() if not p.tiene_ve(t[2]) and not p.superado(t)]
    lecturas = [m[1] for m in p.de('MET')]
    act = activas(sen, excluir=('S9',))
    return {
        'senales':     (not act, 'sin paradas activas' if not act else
                        'paradas activas: ' + ' '.join(sorted({s[0] for s in act}))),
        'build':       (bool(q and arranco(q)), ('%s: arranque ok' % q[1]) if q and arranco(q) else
                        ('%s: el juego no arranco en el gate' % q[1]) if q else 'no hay QA de entrega'),
        'deuda':       (bool(q) and not graves, ('%s: sin mayores abiertos' % q[1]) if q and not graves else
                        ('%s: %s' % (q[1], ' '.join(graves))) if q else 'no hay QA de entrega'),
        'bloqueantes': (bool(q) and not bloq, ('%s: sin bloqueantes ni criticos' % q[1]) if q and not bloq else
                        ('%s: %s' % (q[1], ' '.join(bloq))) if q else 'no hay QA de entrega'),
        'met':         (bool(lecturas), ' '.join(lecturas) if lecturas else 'no hay lectura MET-XXX'),
        'entregas':    (not abiertos_tl, 'todos los timelines tienen VE' if not abiertos_tl else
                        'sin VE: ' + ' '.join(abiertos_tl)),
        'modelo':      (bool(p.modelo), p.modelo or 'modelo de negocio sin declarar'),
    }


def salida(p, sen, ruta=FLUJO):
    """(lineas, rc). rc 2 si el flujo pide una medicion que este instrumento no tiene."""
    crit = criterios(ruta)
    ch = chequeos(p, sen)
    L = []
    if not p.fase:
        return (['no hay fase declarada: no hay contra que revisar (S1)'], 1)
    items = crit.get(p.fase)
    if items is None:
        return (['el flujo no tiene criterio de salida para %s' % p.fase], 2)
    faltan, juicios, rc = [], 0, 0
    L.append('fase declarada: %s -- %s' % (p.fase, PREGUNTA[p.fase]))
    idx = FASES.index(p.fase)
    if idx + 1 < len(FASES):
        L.append('si avanza:      %s -- %s' % (FASES[idx + 1], PREGUNTA[FASES[idx + 1]]))
    L.append('')
    for tipo, clave, texto in items:
        if tipo == 'medido':
            if clave not in ch:
                L.append('  [ERROR]  %-11s el flujo pide una medicion que fase.py no tiene' % clave)
                rc = 2
                continue
            ok, ev = ch[clave]
            L.append('  [%s]  %-11s %s' % ('ok    ' if ok else 'FALTA ', clave, texto))
            L.append('           %-11s %s' % ('', ev))
            if not ok:
                faltan.append(clave)
        else:
            juicios += 1
            L.append('  [juicio] %s' % texto)
    L.append('')
    if faltan:
        L.append('lo que el instrumento dice: NO SE PUEDE AVANZAR -- %d medido(s) en falta: %s'
                 % (len(faltan), ', '.join(faltan)))
    else:
        L.append('lo que el instrumento dice: los medidos estan en verde; avanzar depende de %d juicio(s),'
                 % juicios)
        L.append('                            que firma el owner, no este instrumento')
    L.append('')
    L.append('las cuatro salidas -- decide el owner, y se registra en el cuaderno (seccion 5):')
    L.append('  AVANZAR  la fase respondio su pregunta: el cuaderno pasa a la siguiente')
    L.append('  SEGUIR   todavia no: el proximo timeline ataca lo que falta, y solo eso')
    L.append('  VOLVER   la evidencia contradice la fase: se baja una (Production que descubre que el nucleo no anda)')
    L.append('  CORTAR   la respuesta es no: se recorta alcance en el orden del libro 17, o se cierra el proyecto')
    ve = p.ultimo('VE')
    ancla = ve[1] if ve else 'VE-XXX'
    L.append('')
    L.append('  | PRJ-0NN | AAAA-MM-DD | fase: revision tras %s | Confirmado | SEGUIR en %s -- <por que> | -- |'
             % (ancla, p.fase))
    return (L, rc)


# ------------------------------------------------------------------ informe
def informe_senales(p, sen):
    L = []
    if not sen:
        L.append('  sin senales: se puede abrir trabajo nuevo')
        return L
    for c, nivel, det, como in sen:
        etiqueta = {'parada': 'PARADA  ', 'aceptada': 'aceptada', 'aviso': 'aviso   '}[nivel]
        L.append('  %s %s %-38s %s' % (etiqueta, c, SENALES[c], det))
        L.append('  %s    %-38s -> %s' % (' ' * 8, '', como))
    return L


def cabecera(p):
    tls = p.tls()
    ve = p.ultimo('VE')
    qas = p.qas_entrega()
    L = ['FASE -- %s' % p.nombre,
         '  fase:      %s' % (p.fase or 'SIN DECLARAR'),
         '  modelo:    %s' % (p.modelo or 'sin declarar'),
         '  timelines: %s' % (' '.join(t[1] for t in tls) or 'ninguno'),
         '  ultimo VE: %s' % (ve[1] if ve else 'ninguno')]
    if qas:
        L.append('  ultimo QA de entrega: %s (%s)' % (qas[-1][1], veredicto(qas[-1])))
    return L


def es_proyecto(carpeta):
    nombre = os.path.basename(os.path.abspath(carpeta).rstrip('/\\'))
    return os.path.isfile(os.path.join(carpeta, nombre + '.md'))


def todos(raiz):
    L, rc = [], 0
    for d in sorted(os.listdir(raiz)):
        c = os.path.join(raiz, d)
        if not os.path.isdir(c) or d in RUIDO:
            continue
        if not es_proyecto(c):
            L.append('%-18s sin cuaderno: no es un proyecto de la cadena' % d)
            continue
        p = Proyecto(c)
        sen = senales(p)
        par = sorted({s[0] for s in sen if s[1] == 'parada'})
        acc = sorted({s[0] for s in sen if s[1] == 'aceptada'})
        av = sorted({s[0] for s in sen if s[1] == 'aviso'})
        if par:
            rc = 1
        L.append('%-18s fase: %-15s paradas: %-18s aceptadas: %-8s avisos: %s'
                 % (d, p.fase or 'SIN DECLARAR', ' '.join(par) or '-', ' '.join(acc) or '-', ' '.join(av) or '-'))
    return L, rc


def main(argv):
    try:
        sys.stdout.reconfigure(errors='replace')
    except AttributeError:
        pass
    args = [a for a in argv[1:] if not a.startswith('--')]
    flags = {a for a in argv[1:] if a.startswith('--')}
    if not args:
        print(__doc__)
        return 2
    ruta = args[0]
    if '--todos' in flags:
        L, rc = todos(ruta)
        print('\n'.join(L))
        return rc if '--verificar' in flags else 0
    if not es_proyecto(ruta):
        print('fase.py: %s no tiene cuaderno (<carpeta>/<carpeta>.md): no es un proyecto' % ruta)
        return 2
    p = Proyecto(ruta)
    sen = senales(p)
    act = activas(sen)
    if '--verificar' in flags:
        if act:
            print('PARADA: %s' % ' '.join(sorted({s[0] for s in act})))
            return 1
        print('SIN PARADAS ACTIVAS')
        return 0
    L = cabecera(p)
    rc = 0
    if '--salida' not in flags:
        L += ['', 'SENALES DE PARADA'] + informe_senales(p, sen)
    if '--senales' not in flags:
        s, rc = salida(p, sen)
        L += ['', 'REVISION DE FASE'] + ['  ' + x if x else '' for x in s]
    print('\n'.join(L))
    return 2 if rc == 2 else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

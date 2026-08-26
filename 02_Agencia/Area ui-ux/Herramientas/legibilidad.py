#!/usr/bin/env python3
"""Vaultrum - Area de UI/UX - medicion de legibilidad de un UXS (v1).

Prueba las seis leyes de la comunicacion sobre los bloques declarativos del UXS:

  Ley 1  las tres preguntas tienen respuesta   uxs-preguntas
  Ley 2  ninguna senal viaja sola en el color  uxs-paleta + uxs-contraste + uxs-distincion
  Ley 3  el mapping no se rompe entre pantallas uxs-mapping vs uxs-navegacion
  Ley 4  ninguna accion sin respuesta          uxs-feedback
  Ley 5  nada se descubre por prueba y error   uxs-acciones vs uxs-visible
  Ley 6  sin estados muertos                   uxs-navegacion (alcanzabilidad + salida)
  Corol. el presupuesto de pantalla es finito  uxs-pantalla vs uxs-densidad

Tres fases:
  presupuesto  la mitad A del UXS: cuanto entra y por que canal
  interfaz     la mitad B completa: se exigen los ocho bloques
  complemento  un UXS que extiende a otro y solo trae sus propios bloques

Los bloques viven dentro de bloques de codigo cercados, con la etiqueta en el
info-string. Eso es deliberado: grafo.py ignora los bloques de codigo, asi que
instrumentar un UXS no agrega ni una arista al grafo del vault.

  python3 legibilidad.py [ruta]              informe completo
  python3 legibilidad.py [ruta] --verificar  solo el veredicto (exit 1 si falla)
  python3 legibilidad.py [ruta] --leyes      que ley cubre cada falla
"""
import os, re, sys, collections

# ---------------------------------------------------------------- lexico
FENCE  = re.compile(r'^(```|~~~)\s*(\S+)?\s*(.*)$')
ARISTA = re.compile(r'^(.+?)\s*--\s*([^\->]+?)\s*-->\s*(.+?)$')
HEX    = re.compile(r'^#?([0-9a-fA-F]{6})$')
JUSTIF = re.compile(r'\(.+\)')
VACIA  = re.compile(r'^[-—–∅\s]*$')

LEY = {
    'preguntas'   : 'Ley 1 - las tres preguntas tienen respuesta en pantalla',
    'preguntas-falta': 'Ley 1 - hay un estado sin fila de preguntas',
    'contraste'   : 'Ley 2 - ninguna senal viaja sola en el color (contraste WCAG)',
    'distincion'  : 'Ley 2 - dos senales que colapsan en daltonismo o en grises',
    'color-suelto': 'Ley 2 - color usado sin declarar en la paleta',
    'mapping'     : 'Ley 3 - el mapping es una promesa: no se rompe entre pantallas',
    'tecla-suelta': 'Ley 3 - tecla usada sin declarar en el mapping',
    'feedback'    : 'Ley 4 - ninguna accion sin respuesta en el mismo frame',
    'visible'     : 'Ley 5 - nada se descubre por prueba y error',
    'muerto'      : 'Ley 6 - estado sin salida',
    'inalcanzable': 'Ley 6 - estado al que no se llega desde la raiz',
    'densidad'    : 'Corolario - el presupuesto de pantalla es finito',
    'sin-medir'   : 'Corolario - pantalla declarada y no medida',
    'sin-instrumentar': 'Contrato - el UXS no declara su fase ni sus bloques',
    'falta-bloque': 'Contrato - falta un bloque obligatorio de la fase',
}

FASES = {
    'presupuesto': ['uxs-paleta', 'uxs-densidad'],
    'complemento': ['uxs-paleta', 'uxs-densidad', 'uxs-preguntas'],
    'interfaz'   : ['uxs-paleta', 'uxs-densidad', 'uxs-preguntas', 'uxs-mapping',
                    'uxs-navegacion', 'uxs-acciones', 'uxs-visible', 'uxs-feedback'],
}

# umbrales
WCAG = {'texto': 4.5, 'grande': 3.0, 'ui': 3.0}
DIST_SIM  = 40.0    # distancia euclidea minima en sRGB simulado (max 441)
DIST_GRIS = 1.40    # razon de contraste minima entre dos senales en escala de grises

# matrices de simulacion de dicromacia (Vienot-Brettel-Mollon, severidad 1.0),
# aplicadas sobre RGB lineal.
SIM = {
    'protanopia' : ((0.152286, 1.052583, -0.204868),
                    (0.114503, 0.786281,  0.099216),
                    (-0.003882, -0.048116, 1.051998)),
    'deuteranopia': ((0.367322, 0.860646, -0.227968),
                     (0.280085, 0.672501,  0.047413),
                     (-0.011820, 0.042940, 0.968881)),
    'tritanopia' : ((1.255528, -0.076749, -0.178779),
                    (-0.078411, 0.930809,  0.147602),
                    (0.004733,  0.691367,  0.303900)),
}

# ---------------------------------------------------------------- color
def a_rgb(s):
    m = HEX.match(s.strip())
    if not m: return None
    h = m.group(1)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def lineal(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def luminancia(rgb):
    r, g, b = (lineal(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contraste(a, b):
    la, lb = luminancia(a), luminancia(b)
    if la < lb: la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)

def simular(rgb, tipo):
    m = SIM[tipo]
    lin = [lineal(x) for x in rgb]
    out = []
    for fila in m:
        v = sum(f * l for f, l in zip(fila, lin))
        v = max(0.0, min(1.0, v))
        v = v * 12.92 if v <= 0.0031308 else 1.055 * (v ** (1 / 2.4)) - 0.055
        out.append(max(0, min(255, round(v * 255))))
    return tuple(out)

def distancia(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

# ---------------------------------------------------------------- parseo
def bloques(txt):
    """rinde (etiqueta, argumento, [lineas]) por cada bloque cercado uxs-*."""
    lines = txt.split('\n')
    i, n = 0, len(lines)
    while i < n:
        m = FENCE.match(lines[i].rstrip())
        if m and m.group(2) and m.group(2).lower().startswith('uxs-'):
            cerca, etq, arg = m.group(1), m.group(2).lower(), (m.group(3) or '').strip()
            cuerpo, i = [], i + 1
            while i < n and not lines[i].rstrip().startswith(cerca):
                cuerpo.append(lines[i]); i += 1
            yield etq, arg, cuerpo
        i += 1

def filas(cuerpo, sep=None):
    """El comentario es '#' al principio de la linea o ' # ' al final: un hex no es comentario."""
    for l in cuerpo:
        if l.lstrip().startswith('#'): continue
        l = re.sub(r'\s#\s.*$', '', l).rstrip()
        if not l.strip(): continue
        yield [c.strip() for c in (l.split(sep) if sep else l.split())] , l.strip()

def leer_uxs(path, txt):
    d = collections.defaultdict(list)
    pantallas = {}
    for etq, arg, cuerpo in bloques(txt):
        if etq == 'uxs-pantalla':
            pantallas[arg or '(sin nombre)'] = [l for l in cuerpo if l.strip()]
        else:
            d[etq].append((arg, cuerpo))
    return d, pantallas

def cargar_excepciones(raiz):
    ruta = os.path.join(raiz, '02_Agencia', 'Area ui-ux', 'Herramientas', 'excepciones.txt')
    exc = collections.defaultdict(dict)
    if not os.path.exists(ruta): return exc
    for linea in open(ruta, encoding='utf-8', errors='replace'):
        linea = linea.split('#')[0].strip()
        if not linea or '|' not in linea: continue
        p = [x.strip() for x in linea.split('|')]
        if len(p) < 3: continue
        exc[p[0].replace('\\', '/')][p[1]] = p[2]
    return exc

# ---------------------------------------------------------------- medicion
def medir(path, txt):
    """Devuelve (metricas, [(tipo, detalle)])."""
    d, pantallas = leer_uxs(path, txt)
    f = []
    met = dict(estados=0, teclas=0, pares=0, pantallas=len(pantallas),
               peor_contraste=None, peor_par=None, fase=None, bloques=len(d) + len(pantallas))

    if not d and not pantallas:
        return met, [('sin-instrumentar', 'el UXS no declara un solo bloque uxs-*')]

    fase = (d['uxs-fase'][0][1][0].strip().lower() if d.get('uxs-fase') and d['uxs-fase'][0][1] else None)
    if fase not in FASES:
        return met, [('sin-instrumentar', f'fase declarada: {fase!r} (esperado: presupuesto | complemento | interfaz)')]
    met['fase'] = fase
    for b in FASES[fase]:
        if b not in d: f.append(('falta-bloque', f'{b} (fase {fase})'))

    # ---- paleta
    paleta = {}
    for cols, cruda in filas(d['uxs-paleta'][0][1] if d.get('uxs-paleta') else []):
        if len(cols) >= 2:
            rgb = a_rgb(cols[1])
            if rgb: paleta[cols[0]] = rgb
            else:   f.append(('color-suelto', f'{cols[0]} = {cols[1]} no es un hex de 6 digitos'))

    def color(nombre):
        if nombre in paleta: return paleta[nombre]
        rgb = a_rgb(nombre)
        if rgb is None: f.append(('color-suelto', nombre))
        return rgb

    # ---- Ley 2a: contraste WCAG
    for cols, cruda in filas(d['uxs-contraste'][0][1] if d.get('uxs-contraste') else []):
        if len(cols) < 2: continue
        clase = cols[2].lower() if len(cols) > 2 else 'texto'
        umbral = WCAG.get(clase, 4.5)
        a, b = color(cols[0]), color(cols[1])
        if not a or not b: continue
        r = contraste(a, b)
        met['pares'] += 1
        if met['peor_contraste'] is None or r < met['peor_contraste']:
            met['peor_contraste'], met['peor_par'] = r, f'{cols[0]}/{cols[1]}'
        if r < umbral:
            f.append(('contraste', f'{cols[0]} sobre {cols[1]}: {r:.2f}:1 (minimo {umbral} para {clase})'))

    # ---- Ley 2b: la senal no colapsa en daltonismo ni en grises
    for cols, cruda in filas(d['uxs-distincion'][0][1] if d.get('uxs-distincion') else []):
        if len(cols) < 2: continue
        a, b = color(cols[0]), color(cols[1])
        if not a or not b: continue
        gris = contraste((round(luminancia(a) * 255),) * 3, (round(luminancia(b) * 255),) * 3)
        if gris < DIST_GRIS:
            f.append(('distincion', f'{cols[0]} vs {cols[1]}: en escala de grises quedan a {gris:.2f}:1'))
        for tipo in SIM:
            dd = distancia(simular(a, tipo), simular(b, tipo))
            if dd < DIST_SIM:
                f.append(('distincion', f'{cols[0]} vs {cols[1]}: bajo {tipo} quedan a {dd:.0f} (minimo {DIST_SIM:.0f})'))

    # ---- navegacion
    aristas, estados, salidas = [], set(), collections.defaultdict(int)
    for cols, cruda in filas(d['uxs-navegacion'][0][1] if d.get('uxs-navegacion') else [], sep=None):
        m = ARISTA.match(cruda)
        if not m: continue
        o, k, t = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
        aristas.append((o, k, t)); estados.add(o); salidas[o] += 1
        if not t.startswith('['): estados.add(t)
    met['estados'] = len(estados)

    # ---- Ley 3: mapping
    mapping = {}
    for cols, cruda in filas(d['uxs-mapping'][0][1] if d.get('uxs-mapping') else [], sep=None):
        if len(cols) < 2: continue
        k, verbo = cols[0], ' '.join(cols[1:])
        if k in mapping and mapping[k] != verbo:
            f.append(('mapping', f'{k} significa "{mapping[k]}" y tambien "{verbo}"'))
        mapping[k] = verbo
    met['teclas'] = len(mapping)
    sueltas = set()
    for o, k, t in aristas:
        if k.isupper() and k not in mapping: sueltas.add((k, f'{o} -> {t}'))

    # ---- Ley 4: feedback
    fb = {c[0][0] for c in filas(d['uxs-feedback'][0][1] if d.get('uxs-feedback') else [], sep=None) if c[0]}
    for k in sorted(mapping):
        if k not in fb: f.append(('feedback', f'{k} no declara respuesta inmediata'))

    # ---- Ley 5: nada por prueba y error
    visible, acciones = {}, {}
    for cols, cruda in filas(d['uxs-visible'][0][1] if d.get('uxs-visible') else [], sep=None):
        if cols: visible[cols[0]] = set(cols[1:])
    for cols, cruda in filas(d['uxs-acciones'][0][1] if d.get('uxs-acciones') else [], sep=None):
        if cols: acciones[cols[0]] = set(cols[1:])
    for o, k, t in aristas:                   # minuscula = transicion automatica, no es input
        if k.isupper(): acciones.setdefault(o, set()).add(k)
    for e in sorted(acciones):
        for k in sorted(acciones[e] - visible.get(e, set())):
            f.append(('visible', f'{e}: {k} hace algo y no esta escrita en pantalla'))
    for mapa, etq in ((acciones, 'accion'), (visible, 'escrita en pantalla')):
        for e in mapa:
            for k in mapa[e]:
                if k.isupper() and k not in mapping: sueltas.add((k, f'{e} ({etq})'))
    for k, donde in sorted(sueltas):
        f.append(('tecla-suelta', f'{k} (usada en {donde})'))

    # ---- Ley 6: sin estados muertos, todo se alcanza
    raiz = None
    if d.get('uxs-raiz') and d['uxs-raiz'][0][1]:
        for cols, cruda in filas(d['uxs-raiz'][0][1]):
            raiz = cols[0]; break
    if raiz is None and aristas: raiz = aristas[0][0]
    for e in sorted(estados):
        if salidas[e] == 0: f.append(('muerto', e))
    if raiz:
        vistos, cola = {raiz}, [raiz]
        while cola:
            cur = cola.pop()
            for o, k, t in aristas:
                if o == cur and not t.startswith('[') and t not in vistos:
                    vistos.add(t); cola.append(t)
        for e in sorted(estados - vistos):
            f.append(('inalcanzable', f'{e} (raiz declarada: {raiz})'))

    # ---- Ley 1: las tres preguntas tienen respuesta
    con_fila = set()
    for cols, cruda in filas(d['uxs-preguntas'][0][1] if d.get('uxs-preguntas') else [], sep='|'):
        if not cols or not cols[0]: continue
        e = cols[0]; con_fila.add(e)
        celdas = cols[1:4]
        if len(celdas) < 3:
            f.append(('preguntas', f'{e}: declara {len(celdas)} de 3 respuestas')); continue
        for etq, c in zip(('que pasa', 'que puedo hacer', 'como voy'), celdas):
            if VACIA.match(c) or (c.startswith(('-', '\u2014', '\u2013')) and not JUSTIF.search(c)):
                f.append(('preguntas', f'{e}: "{etq}" sin respuesta y sin justificacion'))
    if d.get('uxs-preguntas'):
        for e in sorted(estados - con_fila):
            f.append(('preguntas-falta', e))

    # ---- Corolario: densidad
    techo = None
    for cols, cruda in filas(d['uxs-densidad'][0][1] if d.get('uxs-densidad') else []):
        if len(cols) >= 2 and cols[0].lower() == 'techo':
            try: techo = int(cols[1])
            except ValueError: pass
    if techo:
        for nombre, lineas in sorted(pantallas.items()):
            if len(lineas) > techo:
                f.append(('densidad', f'{nombre}: {len(lineas)} lineas (techo {techo})'))
    if fase == 'interfaz':
        for e in sorted(estados):
            if e not in pantallas: f.append(('sin-medir', e))
    return met, f

# ---------------------------------------------------------------- recorrido
def recolectar(ruta):
    if os.path.isfile(ruta): return {ruta: open(ruta, encoding='utf-8', errors='replace').read()}
    out = {}
    for dp, dn, fn in os.walk(ruta):
        dn[:] = [x for x in dn if not x.startswith('.') and x != '_to_delete']
        for f in sorted(fn):
            if f.startswith('UXS-') and f.endswith('.md'):
                p = os.path.join(dp, f)
                out[os.path.relpath(p, ruta).replace('\\', '/')] = \
                    open(p, encoding='utf-8', errors='replace').read()
    return out

def auditar(ruta):
    exc = cargar_excepciones(ruta if os.path.isdir(ruta) else '.')
    res = {}
    for p, txt in recolectar(ruta).items():
        met, f = medir(p, txt)
        fallas = [(t, det) for t, det in f if t not in exc.get(p, {})]
        okey   = [(t, det, exc[p][t]) for t, det in f if t in exc.get(p, {})]
        res[p] = (met, fallas, okey)
    return res

# ---------------------------------------------------------------- informe
def informe(res):
    if not res:
        print('sin UXS medibles en la ruta dada'); return
    print(f"{'UXS':<40}{'fase':>12}{'estados':>9}{'teclas':>8}{'pantallas':>11}   {'peor contraste':<28}")
    for p, (met, f, ok) in sorted(res.items()):
        pc = f"{met['peor_contraste']:.2f}:1 {met['peor_par']}" if met['peor_contraste'] else '-'
        print(f"{os.path.basename(p)[:40]:<40}{str(met['fase']):>12}{met['estados']:>9}"
              f"{met['teclas']:>8}{met['pantallas']:>11}   {pc:<28}")
    tot = sum(len(f) for _, f, _ in res.values())
    if tot:
        print(f"\nFuera de ley ({tot}):")
        for p, (met, f, ok) in sorted(res.items()):
            if not f: continue
            print(f"\n  {p}")
            agr = collections.defaultdict(list)
            for t, det in f: agr[t].append(det)
            for t in sorted(agr, key=lambda x: -len(agr[x])):
                print(f"    {LEY.get(t, t)}  ({len(agr[t])})")
                for det in agr[t][:8]: print(f"        {det}")
    exs = [(p, t, det, r) for p, (m, f, ok) in res.items() for t, det, r in ok]
    if exs:
        print(f"\nExcepciones declaradas ({len(exs)}) - estan en excepciones.txt, no fallan:")
        for p, t, det, r in exs[:12]: print(f"    {t:<14} {os.path.basename(p)}  {det}  ({r})")

def veredicto(res):
    agr = collections.Counter()
    for p, (met, f, ok) in res.items():
        for t, det in f: agr[LEY.get(t, t)] += 1
    if not agr:
        n = sum(1 for _ in res)
        print(f"LEGIBILIDAD EN LEY: {n} UXS medidos, las seis leyes en verde.")
        return 0
    print('LEGIBILIDAD FUERA DE LEY: ' + ' | '.join(f'{n} {k}' for k, n in agr.most_common()))
    return 1

if __name__ == '__main__':
    if '--leyes' in sys.argv:
        for k, v in LEY.items(): print(f'  {k:<18} {v}')
        sys.exit(0)
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    r = auditar(args[0] if args else '.')
    if '--verificar' in sys.argv: sys.exit(veredicto(r))
    informe(r); print(); sys.exit(veredicto(r))

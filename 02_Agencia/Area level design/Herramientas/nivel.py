#!/usr/bin/env python3
"""Vaultrum - Area de Level Design - medicion del espacio jugable (v1).

Un area que declara un numero sin instrumento esta estimando. Level Design
declara que un nivel es superable con el salto que el GDS definio: esto lo
prueba, simulando el mismo salto en vez de opinando.

Cuatro leyes del espacio, todas derivadas del GDS y ninguna inventada aca:

  Ley 1  ningun hueco supera el techo derivado del largo de salto
  Ley 2  ningun escalon supera el techo derivado de la altura de salto
  Ley 3  toda plataforma es alcanzable desde la anterior, simulando el salto
  Ley 4  hay techo suficiente para saltar donde hay que saltar

  python3 nivel.py <nivel.txt> <parametros.json>
  python3 nivel.py <nivel.txt> <parametros.json> --verificar
"""
import sys, json, math

SOLIDOS = set('#=')   # '#' es piso; '=' es techo: solido, nunca superficie
PISO    = set('#')
PELIGRO = set('^')
PASABLE = set('.CM')

def cargar(p):
    filas = [l.rstrip('\n') for l in open(p, encoding='utf-8') if l.strip('\n') != '' or True]
    filas = [f for f in filas if f]
    w = max(len(f) for f in filas)
    return [f.ljust(w, '.') for f in filas]

def solido(g, x, y):
    if y < 0 or y >= len(g) or x < 0 or x >= len(g[0]): return False
    return g[y][x] in SOLIDOS

def superficies(g):
    """Por columna, la y de la superficie mas alta PISABLE (o None).

    Un techo es solido y no es superficie. Distinguirlo por geometria es
    ambiguo -- una plataforma flotante y un techo se ven igual desde arriba --
    asi que el nivel lo declara: '=' es techo. Salio de correr esta misma
    herramienta sobre LDS-001.5 y rebotar a Game Design."""
    W, H = len(g[0]), len(g)
    out = []
    for x in range(W):
        y = None
        for yy in range(H):
            if g[yy][x] in PISO:
                y = yy; break
        out.append(y)
    return out

def huecos(sup):
    """Tramos contiguos sin superficie -> (x_ini, x_fin, ancho)."""
    res, ini = [], None
    for x, y in enumerate(sup):
        if y is None and ini is None: ini = x
        elif y is not None and ini is not None:
            res.append((ini, x-1, x-ini)); ini = None
    if ini is not None: res.append((ini, len(sup)-1, len(sup)-ini))
    return res

def escalones(sup):
    """Cambios de altura entre columnas contiguas con superficie."""
    res = []
    prev_x, prev_y = None, None
    for x, y in enumerate(sup):
        if y is None: continue
        if prev_y is not None and x == prev_x + 1 and y != prev_y:
            res.append((x, prev_y - y))   # positivo = sube
        prev_x, prev_y = x, y
    return res

def simular_salto(P):
    """Devuelve la trayectoria (dx, dy) del salto maximo, en tiles.
    dy positivo = mas arriba. Usa exactamente los parametros del GDS."""
    T = P['tile_px']
    vx = P['velocidad_max_px_s'] / 60.0
    vy = -P['impulso_salto_px_frame']
    gs, gc = P['gravedad_subida'], P['gravedad_caida']
    x = y = 0.0
    tray = []
    for _ in range(240):
        vy += gs if vy < 0 else gc
        if abs(vy) < P['umbral_apex']: vy -= (gs if vy < 0 else gc) * (1 - P['factor_apex'])
        vy = min(vy, P['velocidad_terminal_px_s'] / 60.0)
        x += vx; y += vy
        tray.append((x / T, -y / T))
        if y > T * 8: break
    return tray

def alcance(P, dy_tiles):
    """Distancia horizontal maxima util para llegar a una plataforma dy tiles
    mas ALTA (dy>0) o mas baja (dy<0) que la de salida."""
    tray = simular_salto(P)
    mejor = 0.0
    for dx, dyy in tray:
        if dyy >= dy_tiles - 0.05:
            mejor = max(mejor, dx)
    return mejor

def auditar(g, P):
    sup = superficies(g)
    fallas, datos = [], {}
    hs = huecos(sup)
    es = escalones(sup)
    datos['huecos'] = hs
    datos['escalones'] = es

    tope_hueco = P['hueco_max_tiles']
    tope_escalon = P['escalon_max_tiles']

    for (a, b, w) in hs:
        if a == 0 or b == len(sup) - 1: continue   # bordes del nivel
        if w > tope_hueco:
            fallas.append(('Ley 1', 'hueco de %d tiles en x=%d..%d (tope %d)' % (w, a, b, tope_hueco)))
    for (x, d) in es:
        if d > tope_escalon:
            fallas.append(('Ley 2', 'escalon de %d tiles subiendo en x=%d (tope %d)' % (d, x, tope_escalon)))

    # Ley 3 - alcanzabilidad simulada, hueco por hueco
    for (a, b, w) in hs:
        if a == 0 or b == len(sup) - 1: continue
        y_sal, y_lle = sup[a-1], sup[b+1]
        if y_sal is None or y_lle is None: continue
        dy = y_sal - y_lle                      # positivo = hay que subir
        necesario = w + 1                       # tiles de vuelo
        posible = alcance(P, dy)
        datos.setdefault('saltos', []).append((a, b, w, dy, round(posible, 2)))
        if posible < necesario:
            fallas.append(('Ley 3', 'hueco x=%d..%d (%d tiles, dy=%+d) necesita %d y el salto llega a %.2f'
                           % (a, b, w, dy, necesario, posible)))

    # Ley 4 - techo sobre el punto de despegue de cada salto
    alto_salto = P['altura_salto_tiles']
    for (a, b, w) in hs:
        if a == 0: continue
        y_sal = sup[a-1]
        if y_sal is None: continue
        libre = 0
        for k in range(1, 12):
            if solido(g, a-1, y_sal - k): break
            libre += 1
        datos.setdefault('techos', []).append((a-1, libre))
        if libre < alto_salto + 1:
            fallas.append(('Ley 4', 'techo de %d tiles en x=%d: hace falta %d' % (libre, a-1, int(alto_salto)+1)))
    return sup, datos, fallas

def informe(g, P):
    sup, d, f = auditar(g, P)
    W, H = len(g[0]), len(g)
    print('nivel %dx%d tiles | superficie en %d columnas | huecos %d | escalones %d'
          % (W, H, sum(1 for s in sup if s is not None), len(d['huecos']), len(d['escalones'])))
    print()
    print('%-6s %-14s %-6s %-8s %s' % ('HUECO', 'x', 'ancho', 'desnivel', 'alcance del salto (tiles)'))
    for (a, b, w, dy, pos) in d.get('saltos', []):
        marca = 'OK ' if pos >= w + 1 else 'NO '
        print('%-6s %-14s %-6d %-8s %s%.2f  (necesita %d)' % (marca, '%d..%d' % (a, b), w, '%+d' % dy, '', pos, w + 1))
    print()
    tray = simular_salto(P)
    alto = max(dy for _, dy in tray)
    largo = max(dx for dx, _ in tray if _ >= -0.05) if tray else 0
    print('salto medido:  altura maxima %.2f tiles | alcance en llano %.2f tiles' % (alto, alcance(P, 0)))
    print('techos declarados: hueco <= %d | escalon <= %d | altura util %.1f'
          % (P['hueco_max_tiles'], P['escalon_max_tiles'], P['altura_salto_tiles']))
    print()
    if f:
        print('FUERA DE LEY (%d):' % len(f))
        for ley, msg in f: print('  %-6s %s' % (ley, msg))
    return 0 if not f else 1

def veredicto(g, P):
    _, _, f = auditar(g, P)
    if not f:
        print('NIVEL EN LEY: todo hueco se cruza, todo escalon se sube, todo salto entra.')
        return 0
    agr = {}
    for ley, _ in f: agr[ley] = agr.get(ley, 0) + 1
    print('NIVEL FUERA DE LEY: ' + ' | '.join('%d %s' % (v, k) for k, v in sorted(agr.items())))
    return 1

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    g = cargar(args[0]); P = json.load(open(args[1], encoding='utf-8'))
    sys.exit(veredicto(g, P) if '--verificar' in sys.argv else informe(g, P))

#!/usr/bin/env python3
"""Vaultrum - Area de Arte - el instrumento de las SECUENCIAS 2D.

arte.py mide mallas. Esto mide lo que vuelve de un encargo de animacion: una
carpeta de cuadros PNG (y, si hay, el GIF de revision). Existe por la misma
razon que el resto del area: lo que se ve bien en una vista previa no prueba que
la secuencia este bien. En Miles, una caminata que "se veia fluida" repetia la
misma pierna, y un personaje "desaparecia" en un cuadro sin que nadie supiera si
era dibujo, alfa, recorte u orden.

Que mide (RA-010, RA-011, RA-012):

  cuadros    existen, se leen, y TODOS comparten lienzo            ley 3 (la medida)
  alfa       hay canal alfa real, hay transparencia, y no es un      ley 6 (la entrega)
             damero dibujado encima de un fondo opaco
  vacio      ningun cuadro sin pixeles opacos (la "desaparicion")     ley 6
  recorte    ningun pixel opaco tocando el borde del lienzo           ley 6
  suelo      en un ciclo IN-PLACE, la linea de apoyo no deriva        ley 3
  escala     el alto de la silueta no cambia mas de lo tolerado      ley 3 / identidad
  paleta     ningun cuadro trae una familia de colores nueva          ley 5
  loop       el ultimo cuadro no duplica al primero (pausa) y el      RA-011
             enlace ultimo -> primero no salta mas que el ciclo
  gif        mismos cuadros que los PNG, y duracion total             RA-012

Lo que NO mide, y se declara: si la pierna que apoya es la izquierda o la
derecha, si la pose comunica la accion, si el personaje "es el mismo". Eso lo
juzga una persona contra la referencia maestra -- y lo juzga con los cuadros
numerados y el GIF, no con una impresion.

  python3 animacion.py <carpeta_de_cuadros> [--gif ruta.gif] [--in-place]
                       [--sin-loop] [--tol-escala 0.10] [--verificar]

  --in-place   para caminata o idle: la linea de apoyo no deriva. Una carrera
               tiene fase aerea y NO se mide asi.
  --tol-escala una pose que cambia la silueta a proposito (salto, brazo arriba)
               sube la tolerancia, y el ART lo declara.

Sin dependencias: usa Pillow si esta instalado y, si no, un lector de PNG
propio (8 y 16 bits, gris, RGB, paleta con tRNS, gris+alfa, RGBA; sin
entrelazado). La prueba es probar_animacion.py.
"""
import os, re, struct, sys, zlib

# ------------------------------------------------------------------ lectura
def _paeth(a, b, c):
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    return a if pa <= pb and pa <= pc else (b if pb <= pc else c)


def leer_png_puro(ruta):
    """-> (ancho, alto, pixeles RGBA como lista de tuplas, tiene_alfa)."""
    datos = open(ruta, 'rb').read()
    if datos[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError('no es PNG')
    pos, idat, pal, trns = 8, b'', None, None
    w = h = prof = tipo = entrel = None
    while pos < len(datos):
        n, t = struct.unpack('>I4s', datos[pos:pos + 8])
        cuerpo = datos[pos + 8:pos + 8 + n]
        pos += 12 + n
        if t == b'IHDR':
            w, h, prof, tipo, _, _, entrel = struct.unpack('>IIBBBBB', cuerpo)
        elif t == b'PLTE':
            pal = [tuple(cuerpo[i:i + 3]) for i in range(0, len(cuerpo), 3)]
        elif t == b'tRNS':
            trns = cuerpo
        elif t == b'IDAT':
            idat += cuerpo
        elif t == b'IEND':
            break
    if entrel:
        raise ValueError('PNG entrelazado: no soportado por el lector propio (instalar Pillow)')
    canales = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[tipo]
    bpp_bits = canales * prof
    stride = (w * bpp_bits + 7) // 8
    paso = max(1, bpp_bits // 8)
    crudo = zlib.decompress(idat)
    filas, prev, i = [], bytearray(stride), 0
    for _ in range(h):
        filtro = crudo[i]
        linea = bytearray(crudo[i + 1:i + 1 + stride])
        i += 1 + stride
        for x in range(stride):
            a = linea[x - paso] if x >= paso else 0
            b = prev[x]
            c = prev[x - paso] if x >= paso else 0
            if filtro == 1:
                linea[x] = (linea[x] + a) & 255
            elif filtro == 2:
                linea[x] = (linea[x] + b) & 255
            elif filtro == 3:
                linea[x] = (linea[x] + ((a + b) >> 1)) & 255
            elif filtro == 4:
                linea[x] = (linea[x] + _paeth(a, b, c)) & 255
        filas.append(linea)
        prev = linea
    px = []
    for linea in filas:
        if prof < 8:                       # paleta o gris de 1/2/4 bits
            vals, mask = [], (1 << prof) - 1
            for byte in linea:
                for s in range(8 - prof, -1, -prof):
                    vals.append((byte >> s) & mask)
            vals = vals[:w]
        elif prof == 16:
            vals = list(linea[0::2])       # el byte alto alcanza para medir
        else:
            vals = list(linea)
        for x in range(w):
            if tipo == 3:
                idx = vals[x]
                r, g, b = pal[idx]
                al = trns[idx] if trns and idx < len(trns) else 255
                px.append((r, g, b, al))
            elif tipo == 0:
                v = vals[x]
                px.append((v, v, v, 255))
            elif tipo == 4:
                v, al = vals[2 * x], vals[2 * x + 1]
                px.append((v, v, v, al))
            elif tipo == 2:
                px.append((vals[3 * x], vals[3 * x + 1], vals[3 * x + 2], 255))
            else:
                px.append(tuple(vals[4 * x:4 * x + 4]))
    tiene_alfa = tipo in (4, 6) or (tipo == 3 and trns is not None)
    return w, h, px, tiene_alfa


def leer_png(ruta):
    if os.environ.get('VAULTRUM_SIN_PIL'):          # la prueba corre las dos lecturas
        return leer_png_puro(ruta)
    try:
        from PIL import Image
        im = Image.open(ruta)
        tiene_alfa = im.mode in ('RGBA', 'LA', 'PA') or (im.mode == 'P' and 'transparency' in im.info)
        im = im.convert('RGBA')
        plano = im.get_flattened_data() if hasattr(im, 'get_flattened_data') else im.getdata()
        return im.width, im.height, [tuple(x) for x in plano], tiene_alfa
    except ImportError:
        return leer_png_puro(ruta)


def leer_gif(ruta):
    """-> (cuadros, duracion_ms). Recorre los bloques sin decodificar el LZW."""
    d = open(ruta, 'rb').read()
    if d[:6] not in (b'GIF87a', b'GIF89a'):
        raise ValueError('no es GIF')
    flags = d[10]
    pos = 13 + (3 * (2 ** ((flags & 7) + 1)) if flags & 0x80 else 0)
    cuadros, dur, demora = 0, 0, 0
    while pos < len(d):
        b = d[pos]
        if b == 0x3B:
            break
        if b == 0x21:                                   # extension
            etiqueta = d[pos + 1]
            pos += 2
            if etiqueta == 0xF9 and d[pos] == 4:
                demora = struct.unpack('<H', d[pos + 2:pos + 4])[0] * 10
            while d[pos]:
                pos += d[pos] + 1
            pos += 1
        elif b == 0x2C:                                 # imagen
            cuadros += 1
            dur += demora
            demora = 0
            lflags = d[pos + 9]
            pos += 10 + (3 * (2 ** ((lflags & 7) + 1)) if lflags & 0x80 else 0)
            pos += 1                                    # LZW min code size
            while d[pos]:
                pos += d[pos] + 1
            pos += 1
        else:
            raise ValueError('GIF con un bloque desconocido en %d' % pos)
    return cuadros, dur


# ------------------------------------------------------------------ medidas
def opacos(w, h, px, umbral=16):
    return [(i % w, i // w) for i, p in enumerate(px) if p[3] > umbral]


def caja(pts):
    if not pts:
        return None
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def damero(w, h, px):
    """Un damero DIBUJADO: el cuadro es opaco y su borde alterna dos grises claros."""
    if any(p[3] < 250 for p in px):
        return False
    borde = [px[x] for x in range(w)] + [px[(h - 1) * w + x] for x in range(w)]
    colores = {p[:3] for p in borde}
    if len(colores) != 2:
        return False
    return all(min(c) > 150 and max(c) - min(c) < 12 for c in colores)


def familia(p):
    return (p[0] >> 3, p[1] >> 3, p[2] >> 3)


def colores(px):
    """familias de color (RGB a 5 bits por canal) de los pixeles PLENOS. Los bordes
    semitransparentes se excluyen: el antialias inventa mezclas en cada cuadro, y
    contarlas daria 'colores nuevos' en una secuencia perfectamente coherente."""
    return {familia(p) for p in px if p[3] >= 250}


def diferencia(a, b):
    n = len(a)
    if not n:
        return 0.0
    return sum(abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2]) + abs(x[3] - y[3])
               for x, y in zip(a, b)) / (4.0 * n)


def mediana(v):
    s = sorted(v)
    return None if not s else (s[len(s) // 2] if len(s) % 2 else (s[len(s) // 2 - 1] + s[len(s) // 2]) / 2)


def orden_natural(nombre):
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', nombre)]


# ------------------------------------------------------------------ la medicion
def medir(carpeta, gif=None, in_place=False, loop=True, tol_escala=0.10, tol_suelo=2,
          tol_paleta=0.10):
    """-> (cuadros_leidos, hallazgos). Hallazgo: (chequeo, detalle)."""
    h = []
    nombres = sorted((f for f in os.listdir(carpeta) if f.lower().endswith('.png')), key=orden_natural)
    if not nombres:
        return 0, [('cuadros', 'no hay PNG en %s' % carpeta)]
    cuadros = []
    for n in nombres:
        try:
            cuadros.append((n,) + tuple(leer_png(os.path.join(carpeta, n))))
        except Exception as e:  # un cuadro ilegible es un hallazgo, no un traceback
            h.append(('cuadros', '%s no se puede leer: %s' % (n, e)))
    if not cuadros:
        return 0, h
    tam = {(c[1], c[2]) for c in cuadros}
    if len(tam) > 1:
        h.append(('cuadros', 'lienzos distintos %s: el pivot y la escala dejan de ser comparables. '
                  'Mismo lienzo para todos, sin recentrar por caja visible' % sorted(tam)))
        return len(cuadros), h

    base_colores, alturas, suelos, cajas = None, [], [], []
    for n, w, hh, px, alfa in cuadros:
        if damero(w, hh, px):
            h.append(('alfa', '%s: damero DIBUJADO sobre fondo opaco. No es transparencia' % n))
        elif not alfa:
            h.append(('alfa', '%s: sin canal alfa' % n))
        elif not any(p[3] < 250 for p in px):
            h.append(('alfa', '%s: tiene canal alfa y ningun pixel transparente' % n))
        pts = opacos(w, hh, px)
        if not pts:
            h.append(('vacio', '%s: ningun pixel opaco. Es la "desaparicion": revisar alfa, recorte e '
                      'indice antes de redibujar' % n))
            cajas.append(None)
            continue
        c = caja(pts)
        cajas.append(c)
        if alfa and (c[0] == 0 or c[1] == 0 or c[2] == w - 1 or c[3] == hh - 1):
            h.append(('recorte', '%s: la silueta toca el borde del lienzo. Falta margen para manos, pies '
                      'o pelo, o algo quedo cortado' % n))
        alturas.append(c[3] - c[1] + 1)
        suelos.append(c[3])
        if base_colores is None:
            base_colores = colores(px)
        else:
            plenos = [p for p in px if p[3] >= 250]
            if plenos:
                nuevos = sum(1 for p in plenos if familia(p) not in base_colores) / float(len(plenos))
                if nuevos > tol_paleta:
                    h.append(('paleta', '%s: %.0f%% de sus pixeles son de colores que el primer cuadro '
                              'no tiene. Paleta distinta, o otro personaje' % (n, 100 * nuevos)))

    if alturas:
        med = mediana(alturas)
        for (n, *_), c in zip(cuadros, cajas):
            if c is None:
                continue
            alto = c[3] - c[1] + 1
            if med and abs(alto - med) / float(med) > tol_escala:
                h.append(('escala', '%s: la silueta mide %d px de alto contra %d de mediana (%+.0f%%). '
                          'Si no es una pose deliberada, cambio la escala del personaje'
                          % (n, alto, med, 100.0 * (alto - med) / med)))
    if in_place and suelos:
        ms = mediana(suelos)
        fuera = [(cuadros[i][0], s) for i, s in enumerate(suelos) if abs(s - ms) > tol_suelo]
        for n, s in fuera:
            h.append(('suelo', '%s: la linea de apoyo esta en y=%d contra %d. En un ciclo in-place el '
                      'personaje flota o se hunde' % (n, s, ms)))

    if loop and len(cuadros) >= 3:
        px = [c[3] for c in cuadros]
        pasos = [diferencia(px[i], px[i + 1]) for i in range(len(px) - 1)]
        cierre = diferencia(px[-1], px[0])
        tipico = mediana(pasos) or 0.0
        if cierre < 0.25 and tipico > 0.25:
            h.append(('loop', 'el ultimo cuadro (%s) repite al primero: en bucle, ese cuadro es una '
                      'pausa involuntaria' % cuadros[-1][0]))
        elif tipico and cierre > 2.5 * tipico:
            h.append(('loop', 'el enlace %s -> %s cambia %.1f contra %.1f tipico entre cuadros: el ciclo '
                      'salta al volver a empezar' % (cuadros[-1][0], cuadros[0][0], cierre, tipico)))
    elif loop:
        h.append(('declarado', 'menos de 3 cuadros: el enlace del loop no se mide'))

    if gif:
        try:
            n_gif, dur = leer_gif(gif)
            if n_gif != len(cuadros):
                h.append(('gif', 'el GIF tiene %d cuadros y la carpeta %d: el GIF no sale de estos PNG'
                          % (n_gif, len(cuadros))))
            else:
                h.append(('declarado', 'GIF: %d cuadros, %d ms de ciclo' % (n_gif, dur)))
        except Exception as e:
            h.append(('gif', 'el GIF no se puede leer: %s' % e))
    return len(cuadros), h


def main(argv):
    args = [a for a in argv[1:] if not a.startswith('--')]
    if not args:
        print(__doc__)
        return 2
    opt = {}
    i = 1
    while i < len(argv):
        if argv[i] in ('--gif', '--tol-escala') and i + 1 < len(argv):
            opt[argv[i]] = argv[i + 1]
            if argv[i + 1] in args:
                args.remove(argv[i + 1])
            i += 2
        else:
            i += 1
    n, h = medir(args[0], gif=opt.get('--gif'), in_place='--in-place' in argv,
                 loop='--sin-loop' not in argv, tol_escala=float(opt.get('--tol-escala', 0.10)))
    print('\n  ARTE - secuencia: %s  (%d cuadros)' % (args[0], n))
    fallas = [x for x in h if x[0] != 'declarado']
    for tipo, d in h:
        print('    [%s] %s' % (tipo, d))
    print('\n  %s\n' % ('SECUENCIA EN LEY' if not fallas else 'FUERA DE LEY: %d hallazgo(s)' % len(fallas)))
    print('  No mide: que pierna apoya, si la pose comunica la accion, si es el mismo personaje.')
    print('  Eso se juzga contra la referencia maestra, con los cuadros numerados.\n')
    return 1 if (fallas and '--verificar' in argv) else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

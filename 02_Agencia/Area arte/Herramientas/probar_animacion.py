#!/usr/bin/env python3
"""Vaultrum - Area de Arte - la prueba del instrumento de secuencias.

Cada caso fabrica cuadros PNG a mano, con el defecto conocido adentro, y
comprueba que animacion.py lo encuentre -- o que NO encuentre nada en la
secuencia sana. Los casos de lectura corren dos veces: con Pillow y con el lector
propio, porque el owner puede no tener Pillow y un instrumento que solo anda con
una dependencia instalada no es el instrumento de todos (RA-008: el instrumento
se verifica en el extremo de su rango, y la maquina del owner es un extremo).

    python3 probar_animacion.py        exit 0 si pasan todos
"""
import math, os, shutil, struct, sys, tempfile, zlib

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import animacion as A  # noqa: E402

W = H = 64
TRANSP = (0, 0, 0, 0)


# ------------------------------------------------------------------ fabricar
def png_rgba(ruta, w, h, px, alfa=True):
    """escritor minimo: RGBA (o RGB), 8 bits, filtro 0."""
    tipo, n = (6, 4) if alfa else (2, 3)
    filas = b''.join(b'\x00' + bytes(v for p in px[y * w:(y + 1) * w] for v in p[:n]) for y in range(h))
    def trozo(t, c):
        return struct.pack('>I', len(c)) + t + c + struct.pack('>I', zlib.crc32(t + c) & 0xffffffff)
    datos = (b'\x89PNG\r\n\x1a\n' + trozo(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, tipo, 0, 0, 0))
             + trozo(b'IDAT', zlib.compress(filas)) + trozo(b'IEND', b''))
    open(ruta, 'wb').write(datos)


def gif(ruta, cuadros, demora_cs=10):
    """GIF de 1x1 con N cuadros: el instrumento cuenta bloques, no decodifica."""
    d = b'GIF89a' + struct.pack('<HHBBB', 1, 1, 0x80, 0, 0) + b'\x00\x00\x00\xff\xff\xff'
    for _ in range(cuadros):
        d += b'\x21\xF9\x04\x00' + struct.pack('<H', demora_cs) + b'\x00\x00'
        d += b'\x2C' + struct.pack('<HHHHB', 0, 0, 1, 1, 0) + b'\x02\x02\x44\x01\x00'
    open(ruta, 'wb').write(d + b'\x3B')


def rect(px, x0, y0, x1, y1, color):
    for y in range(y0, y1):
        for x in range(x0, x1):
            px[y * W + x] = color


def cuadro(fase, alto_cuerpo=28, suelo=58, color_cuerpo=(40, 40, 40, 255), dx=0):
    """un personaje minimo: torso + dos piernas que alternan. fase en [0, 1)."""
    px = [TRANSP] * (W * H)
    top = suelo - 12 - alto_cuerpo
    rect(px, 24 + dx, top, 40 + dx, suelo - 12, color_cuerpo)
    paso = int(round(6 * math.sin(2 * math.pi * fase)))
    rect(px, 26 + paso + dx, suelo - 12, 30 + paso + dx, suelo, (200, 50, 50, 255))   # pierna I
    rect(px, 34 - paso + dx, suelo - 12, 38 - paso + dx, suelo, (50, 50, 200, 255))   # pierna D
    return px


def carpeta(cuadros_px, alfa=True, tam=None):
    d = tempfile.mkdtemp()
    for i, px in enumerate(cuadros_px):
        w, h = tam[i] if tam else (W, H)
        png_rgba(os.path.join(d, 'caminata_%02d.png' % (i + 1)), w, h, px, alfa)
    return d


def ciclo(n=8, **kw):
    return [cuadro(i / float(n), **kw) for i in range(n)]


def tipos(d, **kw):
    try:
        _, h = A.medir(d, **kw)
        return [t for t, _ in h if t != 'declarado'], h
    finally:
        pass


casos, fallos = [], []


def caso(nombre, lectores=('pil', 'puro')):
    def deco(fn):
        for l in lectores:
            casos.append(('%s  [%s]' % (nombre, l), fn, l))
        return fn
    return deco


def con(d, fn):
    try:
        return fn(d)
    finally:
        shutil.rmtree(d, ignore_errors=True)


# ------------------------------------------------------------------ casos
@caso('ciclo sano de 8 cuadros: en ley, tambien in-place')
def _():
    t, h = con(carpeta(ciclo()), lambda d: tipos(d, in_place=True))
    assert t == [], h


@caso('lienzos distintos')
def _():
    cs = ciclo()
    cs[3] = [TRANSP] * (70 * 64)
    tam = [(W, H)] * 8
    tam[3] = (70, 64)
    t, h = con(carpeta(cs, tam=tam), tipos)
    assert t == ['cuadros'], h


@caso('sin canal alfa')
def _():
    cs = [[p if p[3] else (255, 255, 255, 255) for p in c] for c in ciclo()]
    t, h = con(carpeta(cs, alfa=False), tipos)
    assert 'alfa' in t, h


@caso('damero dibujado sobre fondo opaco (no es transparencia)')
def _():
    cs = []
    for c in ciclo():
        cs.append([p if p[3] else ((204, 204, 204, 255) if ((i % W) // 8 + (i // W) // 8) % 2
                                   else (255, 255, 255, 255)) for i, p in enumerate(c)])
    # 204 y 255 no son "dos grises parecidos": se ajusta al damero tipico de 2 grises claros
    cs = [[(q if q[:3] not in ((204, 204, 204), (255, 255, 255)) else
            ((200, 200, 200, 255) if q[0] == 204 else (238, 238, 238, 255))) for q in c] for c in cs]
    t, h = con(carpeta(cs), tipos)
    assert any('damero' in x for _, x in h), h


@caso('cuadro vacio: la desaparicion')
def _():
    cs = ciclo()
    cs[5] = [TRANSP] * (W * H)
    t, h = con(carpeta(cs), tipos)
    assert 'vacio' in t, h


@caso('silueta que toca el borde: recorte')
def _():
    cs = ciclo()
    rect(cs[2], 0, 30, 6, 34, (40, 40, 40, 255))
    t, h = con(carpeta(cs), tipos)
    assert 'recorte' in t, h


@caso('in-place: un cuadro flota 6 px')
def _():
    cs = ciclo()
    cs[4] = cuadro(4 / 8.0, suelo=52)
    t, h = con(carpeta(cs), lambda d: tipos(d, in_place=True))
    assert 'suelo' in t, h


@caso('el personaje cambia de escala en un cuadro')
def _():
    cs = ciclo()
    cs[5] = cuadro(5 / 8.0, alto_cuerpo=40)
    t, h = con(carpeta(cs), tipos)
    assert 'escala' in t, h


@caso('la misma escala, con la tolerancia declarada para una pose deliberada')
def _():
    cs = ciclo()
    cs[5] = cuadro(5 / 8.0, alto_cuerpo=40)
    t, h = con(carpeta(cs), lambda d: tipos(d, tol_escala=0.5))
    assert 'escala' not in t, h


@caso('el ultimo cuadro repite al primero: pausa involuntaria')
def _():
    cs = ciclo() + [cuadro(0.0)]
    t, h = con(carpeta(cs), tipos)
    assert 'loop' in t and any('pausa' in x for _, x in h), h


@caso('el ciclo salta al volver a empezar')
def _():
    cs = [cuadro(0.0, dx=i) for i in range(8)]     # avanza sin volver: el enlace 8 -> 1 salta
    t, h = con(carpeta(cs), tipos)
    assert 'loop' in t and any('salta' in x for _, x in h), h


@caso('un cuadro con otra paleta')
def _():
    cs = ciclo()
    cs[3] = cuadro(3 / 8.0, color_cuerpo=(20, 180, 60, 255))
    t, h = con(carpeta(cs), tipos)
    assert 'paleta' in t, h


@caso('GIF con un cuadro menos que los PNG', lectores=('pil',))
def _():
    def f(d):
        g = os.path.join(d, 'preview.gif.bin')
        gif(g, 7)
        return tipos(d, gif=g)
    t, h = con(carpeta(ciclo()), f)
    assert 'gif' in t, h


@caso('GIF con los mismos cuadros: declara duracion', lectores=('pil',))
def _():
    def f(d):
        g = os.path.join(d, 'preview.gif.bin')
        gif(g, 8, demora_cs=10)
        return tipos(d, gif=g)
    t, h = con(carpeta(ciclo()), f)
    assert t == [] and any('800 ms' in x for _, x in h), h


@caso('extremo: dos cuadros, el loop no se mide y se declara')
def _():
    t, h = con(carpeta(ciclo(2)), tipos)
    assert t == [] and any(k == 'declarado' for k, _ in h), h


@caso('extremo: un .png que no es PNG es un hallazgo, no un traceback')
def _():
    d = carpeta(ciclo())
    open(os.path.join(d, 'caminata_99.png'), 'wb').write(b'esto no es un png')
    t, h = con(d, tipos)
    assert 'cuadros' in t, h


@caso('extremo: el lector propio lee lo mismo que Pillow en PNG con filtros reales', lectores=('pil',))
def _():
    try:
        from PIL import Image
    except ImportError:
        return  # sin Pillow no hay contra que comparar: se declara en la salida
    d = tempfile.mkdtemp()
    try:
        im = Image.new('RGBA', (37, 23))
        im.putdata([((x * 7) % 256, (y * 11) % 256, (x * y) % 256, (x + y) * 5 % 256)
                    for y in range(23) for x in range(37)])
        for modo, nombre in (('RGBA', 'a.png'), ('P', 'p.png'), ('LA', 'la.png'), ('RGB', 'rgb.png')):
            r = os.path.join(d, nombre)
            (im.convert(modo) if modo != 'P' else im.convert('RGBA').quantize(16)).save(r, optimize=True)
            w, hh, px, _ = A.leer_png_puro(r)
            im2 = Image.open(r).convert('RGBA')
            ref = [tuple(x) for x in (im2.get_flattened_data() if hasattr(im2, 'get_flattened_data')
                                      else im2.getdata())]
            assert (w, hh) == (37, 23) and px == ref, 'difiere en modo %s' % modo
        r = os.path.join(d, 'a16.png')
        Image.new('I;16', (5, 3), 40000).save(r)
        w, hh, px, _ = A.leer_png_puro(r)
        assert (w, hh) == (5, 3) and px[0][3] == 255
    finally:
        shutil.rmtree(d)


# ------------------------------------------------------------------ correr
if __name__ == '__main__':
    for nombre, fn, lector in casos:
        if lector == 'puro':
            os.environ['VAULTRUM_SIN_PIL'] = '1'
        else:
            os.environ.pop('VAULTRUM_SIN_PIL', None)
        try:
            fn()
            print('  [ok]    %s' % nombre)
        except AssertionError as e:
            fallos.append(nombre)
            print('  [FALLA] %s  %s' % (nombre, e))
        except Exception as e:
            fallos.append(nombre)
            print('  [ERROR] %s  %r' % (nombre, e))
    try:
        import PIL  # noqa: F401
    except ImportError:
        print('\n  (sin Pillow: los casos [pil] corrieron con el lector propio)')
    print('\n  %d casos, %d fallas' % (len(casos), len(fallos)))
    sys.exit(1 if fallos else 0)

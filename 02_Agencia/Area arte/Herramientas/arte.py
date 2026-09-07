# -*- coding: utf-8 -*-
"""Vaultrum - Area de Arte - el instrumento de las seis leyes (v1).

    malla(piezas)                    leyes 1, 2 y 3
    presupuesto(piezas, familias)    ley 4
    paleta(materiales, familias)     ley 5
    entrega(ruta, contrato)          ley 6

POR QUE ESTE ARCHIVO ESTA PARTIDO EN DOS MITADES

La mitad de abajo son LAS LEYES y no importa `bpy`. La mitad de arriba es lo
unico que sabe de Blender: lee la escena y devuelve piezas como diccionarios.

    lectura del DCC   ->  piezas (dict)  ->  las leyes  ->  veredicto

Es la D de SOLID escrita en un archivo: el instrumento IMPLEMENTA las leyes y
las leyes no dependen del DCC. Si manana el area trabaja en otra herramienta se
reescribe `leer_coleccion` y **las seis leyes no se mueven**.

Y tiene una consecuencia que no es teorica: **las leyes se pueden correr y
probar fuera de Blender**, con piezas escritas a mano. El area tiene una regla
sobre eso -- *el instrumento tambien se verifica, y se verifica en el extremo
de su rango* (RA-008)-- y un instrumento que solo corre adentro del DCC no se
puede verificar en ningun extremo. El anterior no se podia: importaba `bpy` en
la primera linea.

INSTALAR (adentro de Blender, una vez por sesion; ver AiCare_Blender)
    exec(open(r"<ruta>/arte.py").read())
USAR
    malla(leer_coleccion("Goblin"))
    presupuesto(leer_coleccion("Goblin"), {"enemigo": {"caras": 900, "max_simultaneos": 20}})
"""
import json
import math
import os
import struct

# ---------------------------------------------------------------- umbrales
# Cada uno con su procedencia. Un umbral sin origen es una opinion con decimales.
RELLENO_MACIZO      = 0.28   # RA-006: 2V/A sobre la dimension minima. Cubo = 1/3.
RELLENO_INTERMEDIO  = 0.12   # RA-006: pared gruesa. Debajo, cascara.
Z_MIN_TOLERANCIA_MM = 0.5    # RA-003: "apoya en z=0" con medio milimetro de gracia
CONTRASTE_MINIMO    = 1.8    # ley 5: dos familias que se distinguen en gris
DISTANCIA_MINIMA    = 25.0   # ley 5: distancia de color entre familias, en Lab dE76


# ============================================================================
#  MITAD 1 — LA LECTURA DEL DCC.  Es lo unico que sabe de Blender.
# ============================================================================

def leer_coleccion(nombres):
    """Devuelve las piezas de una o varias collections, como diccionarios.

    Es la unica funcion de este archivo que importa `bpy`, y esta a proposito:
    para portar el area a otro DCC se reescribe esta y nada mas.
    """
    import bpy, bmesh
    from mathutils.bvhtree import BVHTree

    if isinstance(nombres, str):
        nombres = [nombres]
    objs = [o for c in nombres for o in bpy.data.collections[c].all_objects
            if o.type == 'MESH']

    def bvh(obj):
        bm = bmesh.new(); bm.from_mesh(obj.data)
        bmesh.ops.triangulate(bm, faces=bm.faces)
        bm.transform(obj.matrix_world)
        v = [x.co.copy() for x in bm.verts]
        t = [[x.index for x in f.verts] for f in bm.faces]
        bm.free()
        return BVHTree.FromPolygons(v, t, all_triangles=True, epsilon=0.0)

    arboles = {o.name: bvh(o) for o in objs}
    cruces = [(objs[i].name, objs[j].name)
              for i in range(len(objs)) for j in range(i + 1, len(objs))
              if arboles[objs[i].name].overlap(arboles[objs[j].name])]

    piezas = []
    for o in objs:
        bm = bmesh.new(); bm.from_mesh(o.data); bm.normal_update()
        mundo = [o.matrix_world @ v.co for v in bm.verts]
        piezas.append(dict(
            nombre       = o.name,
            caras        = len(bm.faces),
            verts        = len(bm.verts),
            ngons        = sum(1 for f in bm.faces if len(f.verts) > 4),
            no_manifold  = sum(1 for e in bm.edges if not e.is_manifold),
            interiores   = sum(1 for f in bm.faces
                               if all(len(e.link_faces) > 2 for e in f.edges)),
            # SIN redondear: el signo es lo que se lee, y redondear antes de
            # mirarlo es el defecto que la flecha destapo (RA-008).
            volumen      = bm.calc_volume(signed=True),
            area         = sum(f.calc_area() for f in bm.faces),
            dim_min      = min(o.dimensions),
            bbox         = [round(x, 6) for x in o.dimensions],
            z_min        = min(v.z for v in mundo) if mundo else 0.0,
            escala       = [round(x, 6) for x in o.scale],
            rotacion     = [round(x, 6) for x in o.rotation_euler],
            emparentado  = o.parent is not None,
            materiales   = [m.name for m in o.data.materials if m],
        ))
        bm.free()
    return dict(piezas=piezas, cruces=cruces)


def leer_materiales():
    """Censo de materiales de la escena, como diccionarios. Tambien usa bpy."""
    import bpy
    out = []
    for m in bpy.data.materials:
        rgba = (1.0, 1.0, 1.0, 1.0)
        try:
            rgba = tuple(m.diffuse_color)
        except Exception:
            pass
        out.append(dict(nombre=m.name, rgb=tuple(rgba[:3]), usuarios=m.users))
    return out


# ============================================================================
#  MITAD 2 — LAS LEYES.  No importan bpy. Se pueden correr y probar afuera.
# ============================================================================

def _veredicto(fallas):
    return "EN LEY" if not fallas else "FUERA DE LEY: " + ", ".join(fallas)


def relleno(pieza):
    """RA-006 — macizo o cascara, medido y no supuesto.

    Espesor equivalente = 2V/A. Para una chapa de espesor t da t; para un cubo
    de lado L da L/3. Se divide por la dimension mas chica de la pieza.

    TRAMPA DECLARADA: la clase es una razon contra el bbox, y el bbox miente en
    tres casos -- pieza casi plana, pieza inclinada, objeto con varias islas.
    Se lee `espesor_eq_mm`, NO la clase.
    """
    V = abs(pieza["volumen"])
    A = pieza["area"]
    esp = (2.0 * V / A) if A > 1e-12 else 0.0
    minima = max(pieza["dim_min"], 1e-6)
    r = esp / minima
    return dict(espesor_eq_mm=round(esp * 1000, 1),
                dim_min_mm=round(minima * 1000, 1),
                razon=round(r, 3),
                clase=("macizo" if r >= RELLENO_MACIZO else
                       "intermedio" if r >= RELLENO_INTERMEDIO else "cascara"))


def malla(escena, apoya=True):
    """Leyes 1, 2 y 3 sobre las piezas de un asset ya emparentado.

    Ley 1  nada se atraviesa, todo mira afuera, todo cierra
    Ley 2  el relleno y el espesor se declaran
    Ley 3  la medida es real, y la colocacion se verifica DESPUES de emparentar

    `apoya=False` para lo que vuela: no se le exige z_min = 0.
    """
    piezas = escena["piezas"]
    cruces = ["%s x %s" % (a, b) for a, b in escena.get("cruces", [])]
    invertidas = [p["nombre"] for p in piezas if p["volumen"] <= 0.0]
    no_manifold = sum(p["no_manifold"] for p in piezas)
    interiores = sum(p["interiores"] for p in piezas)

    rell = {p["nombre"]: relleno(p) for p in piezas}
    clases = {}
    for v in rell.values():
        clases[v["clase"]] = clases.get(v["clase"], 0) + 1

    # --- Ley 3: la colocacion, que solo significa algo DESPUES de emparentar
    sucias = [p["nombre"] for p in piezas
              if any(abs(s - 1.0) > 1e-4 for s in p["escala"])
              or any(abs(r) > 1e-4 for r in p["rotacion"])]
    z = min((p["z_min"] for p in piezas), default=0.0)
    apoyo_ok = (not apoya) or abs(z) * 1000 <= Z_MIN_TOLERANCIA_MM
    sin_emparentar = [p["nombre"] for p in piezas if not p["emparentado"]]
    # Una sola pieza suelta es un asset de una pieza, no un asset sin armar.
    sin_armar = len(piezas) > 1 and len(sin_emparentar) == len(piezas)

    fallas = []
    if cruces:            fallas.append("interpenetracion")
    if invertidas:        fallas.append("normales invertidas")
    if no_manifold:       fallas.append("no manifold")
    if interiores:        fallas.append("caras interiores")
    if sucias:            fallas.append("transform sin aplicar")
    if not apoyo_ok:      fallas.append("no apoya en z=0")
    if sin_armar:         fallas.append("sin emparentar: la colocacion no se midio")

    return dict(
        ley="1-3", objetos=len(piezas),
        caras=sum(p["caras"] for p in piezas),
        verts=sum(p["verts"] for p in piezas),
        ngons=sum(p["ngons"] for p in piezas),
        pares_que_se_cruzan=cruces,
        normales_invertidas=invertidas,
        no_manifold=no_manifold, caras_interiores=interiores,
        relleno=clases,
        cascaras=[k for k, v in rell.items() if v["clase"] == "cascara"],
        espesores_mm={k: v["espesor_eq_mm"] for k, v in rell.items()},
        transform_sucio=sucias,
        z_min_mm=round(z * 1000, 2),
        sin_emparentar=sin_emparentar,
        veredicto=_veredicto(fallas))


def presupuesto(escena, familia):
    """Ley 4 — el costo se mide EN PANTALLA, no en el archivo.

    `familia` = {"nombre": str, "caras": int, "max_simultaneos": int}

    817 caras no significa nada. 817 x 20 goblins simultaneos = 16.340 caras en
    pantalla es el numero que decide, y es el que esta ley existe para que
    alguien mire.
    """
    caras = sum(p["caras"] for p in escena["piezas"])
    n = max(int(familia.get("max_simultaneos", 1)), 1)
    en_pantalla = caras * n
    techo_pieza = familia.get("caras")
    techo_pantalla = familia.get("caras_en_pantalla")

    fallas = []
    if techo_pieza is not None and caras > techo_pieza:
        fallas.append("el asset excede su familia: %d > %d" % (caras, techo_pieza))
    if techo_pantalla is not None and en_pantalla > techo_pantalla:
        fallas.append("el set excede en pantalla: %d > %d" % (en_pantalla, techo_pantalla))
    if techo_pieza is None and techo_pantalla is None:
        fallas.append("sin presupuesto declarado: no hay contra que medir")

    return dict(ley="4", familia=familia.get("nombre", "?"),
                caras_asset=caras, max_simultaneos=n,
                caras_en_pantalla=en_pantalla,
                techo_pieza=techo_pieza, techo_pantalla=techo_pantalla,
                veredicto=_veredicto(fallas))


# ---- ley 5: el color, medido y no mirado ----------------------------------
def _lineal(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminancia(rgb):
    """Luminancia relativa WCAG. Es el 'gris' contra el que se mide."""
    r, g, b = (_lineal(max(0.0, min(1.0, x))) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a, b):
    """Razon de contraste WCAG entre dos colores. 1.0 = identicos."""
    la, lb = luminancia(a), luminancia(b)
    hi, lo = max(la, lb), min(la, lb)
    return round((hi + 0.05) / (lo + 0.05), 2)


def dicromacia(rgb, tipo="deuteranopia"):
    """Simulacion de dicromacia (Vienot 1999, sobre LMS de Hunt-Pointer-Estevez).

    No es un filtro decorativo: es como ve una de cada doce personas. Una senal
    que solo existe en el canal rojo-verde no existe para ellas.
    """
    r, g, b = (_lineal(max(0.0, min(1.0, x))) for x in rgb)
    L = 17.8824 * r + 43.5161 * g + 4.11935 * b
    M = 3.45565 * r + 27.1554 * g + 3.86714 * b
    S = 0.0299566 * r + 0.184309 * g + 1.46709 * b
    if tipo == "protanopia":
        L = 2.02344 * M - 2.52581 * S
    elif tipo == "deuteranopia":
        M = 0.494207 * L + 1.24827 * S
    else:                                  # tritanopia
        S = -0.395913 * L + 0.801109 * M
    rr = 0.080944 * L - 0.130504 * M + 0.116721 * S
    gg = -0.0102485 * L + 0.0540194 * M - 0.113615 * S
    bb = -0.000365294 * L + -0.00412163 * M + 0.693513 * S
    def gamma(x):
        x = max(0.0, min(1.0, x))
        return 12.92 * x if x <= 0.0031308 else 1.055 * (x ** (1 / 2.4)) - 0.055
    return (gamma(rr), gamma(gg), gamma(bb))


def _lab(rgb):
    r, g, b = (_lineal(max(0.0, min(1.0, x))) for x in rgb)
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = (0.2126 * r + 0.7152 * g + 0.0722 * b)
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883
    f = lambda t: t ** (1 / 3) if t > 0.008856 else (7.787 * t + 16 / 116)
    fx, fy, fz = f(x), f(y), f(z)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def distancia_color(a, b):
    """dE76 en Lab. Barato, y suficiente para separar familias."""
    la, lb = _lab(a), _lab(b)
    return round(math.sqrt(sum((x - y) ** 2 for x, y in zip(la, lb))), 1)


def paleta(materiales, familias=None, terreno=None):
    """Ley 5 — paleta cerrada, y las familias que hay que distinguir se distinguen.

    `materiales` = [{"nombre", "rgb", "usuarios"}]
    `familias`   = {"nombre de familia": "nombre del material"}   (opcional)
    `terreno`    = rgb del suelo donde el asset va a estar         (opcional)

    Mide en color, en GRIS y en DICROMACIA. Una familia que solo se distingue
    en color no se distingue: se distingue para quien la diseño.
    """
    fallas = []
    usados = [m for m in materiales if m.get("usuarios", 1) > 0]
    huerfanos = [m["nombre"] for m in materiales if m.get("usuarios", 1) == 0]

    # duplicados: dos materiales distintos con el mismo color
    dup = []
    for i in range(len(usados)):
        for j in range(i + 1, len(usados)):
            if distancia_color(usados[i]["rgb"], usados[j]["rgb"]) < 2.0:
                dup.append("%s = %s" % (usados[i]["nombre"], usados[j]["nombre"]))

    pares = []
    if familias:
        color = {f: next((m["rgb"] for m in materiales if m["nombre"] == n), None)
                 for f, n in familias.items()}
        sin_material = [f for f, c in color.items() if c is None]
        if sin_material:
            fallas.append("familia sin material: " + ", ".join(sin_material))
        nombres = [f for f, c in color.items() if c is not None]
        for i in range(len(nombres)):
            for j in range(i + 1, len(nombres)):
                a, b = color[nombres[i]], color[nombres[j]]
                d = dict(par="%s / %s" % (nombres[i], nombres[j]),
                         distancia=distancia_color(a, b),
                         gris=contraste(a, b),
                         deuteranopia=distancia_color(dicromacia(a), dicromacia(b)),
                         protanopia=distancia_color(dicromacia(a, "protanopia"),
                                                    dicromacia(b, "protanopia")))
                d["se_distingue"] = (d["distancia"] >= DISTANCIA_MINIMA
                                     and d["gris"] >= CONTRASTE_MINIMO
                                     and d["deuteranopia"] >= DISTANCIA_MINIMA)
                pares.append(d)
        colapsan = [d["par"] for d in pares if not d["se_distingue"]]
        if colapsan:
            fallas.append("familias que colapsan: " + ", ".join(colapsan))

    contra_terreno = []
    if terreno and familias:
        for f, n in familias.items():
            c = next((m["rgb"] for m in materiales if m["nombre"] == n), None)
            if c is None:
                continue
            r = contraste(c, terreno)
            contra_terreno.append(dict(familia=f, contraste=r))
            if r < CONTRASTE_MINIMO:
                fallas.append("%s se pierde contra el terreno (%.2f)" % (f, r))

    if dup:
        fallas.append("materiales duplicados: " + ", ".join(dup))

    return dict(ley="5", materiales=len(materiales), usados=len(usados),
                huerfanos=huerfanos, duplicados=dup,
                pares=pares, contra_terreno=contra_terreno,
                veredicto=_veredicto(fallas))


def entrega(ruta, contrato=None):
    """Ley 6 — se verifica leyendo el archivo ENTREGADO, no el fuente.

    Parsea el .glb (glTF binario) sin dependencias: cabecera, chunk JSON, y de
    ahi nombres, unidades, ejes y basura colada.

    `contrato` = {"nombres": [...], "prefijo": str, "max_mb": float,
                  "sin": ["Cube", ...]}
    El contrato del cliente le gana a la convencion interna, y por eso se pasa
    de afuera en vez de estar escrito aca adentro.
    """
    contrato = contrato or {}
    fallas = []
    if not os.path.isfile(ruta):
        return dict(ley="6", archivo=ruta,
                    veredicto="FUERA DE LEY: el archivo entregado no existe")

    tam_mb = os.path.getsize(ruta) / (1024 * 1024)
    with open(ruta, "rb") as fh:
        cab = fh.read(12)
        if len(cab) < 12 or cab[:4] != b"glTF":
            return dict(ley="6", archivo=ruta,
                        veredicto="FUERA DE LEY: no es un .glb (falta la marca glTF)")
        version = struct.unpack("<I", cab[4:8])[0]
        js = None
        while True:
            enc = fh.read(8)
            if len(enc) < 8:
                break
            largo, tipo = struct.unpack("<II", enc)
            datos = fh.read(largo)
            if tipo == 0x4E4F534A:          # 'JSON'
                js = json.loads(datos.decode("utf-8"))
                break
    if js is None:
        return dict(ley="6", archivo=ruta,
                    veredicto="FUERA DE LEY: el .glb no trae chunk JSON")

    nodos  = [n.get("name", "") for n in js.get("nodes", [])]
    mallas = [m.get("name", "") for m in js.get("meshes", [])]
    mats   = [m.get("name", "") for m in js.get("materials", [])]
    sin_nombre = [i for i, n in enumerate(mallas) if not n]

    if sin_nombre:
        fallas.append("%d malla(s) sin nombre" % len(sin_nombre))
    esperados = contrato.get("nombres")
    if esperados:
        faltan = [n for n in esperados if n not in nodos and n not in mallas]
        if faltan:
            fallas.append("faltan en la entrega: " + ", ".join(faltan))
    pref = contrato.get("prefijo")
    if pref:
        fuera = [n for n in mallas if n and not n.startswith(pref)]
        if fuera:
            fallas.append("fuera del prefijo '%s': %s" % (pref, ", ".join(fuera)))
    basura = [n for n in contrato.get("sin", []) if n in nodos or n in mallas]
    if basura:
        fallas.append("basura colada: " + ", ".join(basura))
    tope = contrato.get("max_mb")
    if tope is not None and tam_mb > tope:
        fallas.append("pesa %.2f MB, el contrato pide %.2f" % (tam_mb, tope))

    return dict(ley="6", archivo=os.path.basename(ruta), version=version,
                mb=round(tam_mb, 3), nodos=len(nodos), mallas=mallas,
                materiales=mats, mallas_sin_nombre=len(sin_nombre),
                generador=js.get("asset", {}).get("generator", ""),
                veredicto=_veredicto(fallas))

"""Verificacion de malla low poly — Vaultrum / registro Arte_Blender (RA-002).

Se instala UNA vez por sesion de Blender y despues se llama en una linea,
en vez de reenviar las funciones en cada llamada MCP (ver AiCare_Blender.md).

Instalar:
    exec(open(r"<ruta>/verificar_malla.py").read())
Usar:
    result = verificar("Fogata")            # una collection
    result = verificar(["Arbol", "Fogata"]) # varias
    result = verificar("Voyage")            # recorre las subcollections (all_objects)
    result = relleno(bpy.data.objects["Bomba_Cimiento"])   # macizo o cascara, medido
"""
import bpy, bmesh
from mathutils.bvhtree import BVHTree


def _bvh(obj):
    bm = bmesh.new(); bm.from_mesh(obj.data)
    bmesh.ops.triangulate(bm, faces=bm.faces)
    bm.transform(obj.matrix_world)
    v = [x.co.copy() for x in bm.verts]
    t = [[x.index for x in f.verts] for f in bm.faces]
    bm.free()
    return BVHTree.FromPolygons(v, t, all_triangles=True, epsilon=0.0)


def relleno(o):
    """RA-006 -- mide si una pieza es MACIZA o una CASCARA, sin abrirla.

    espesor equivalente = 2V/A. Para una chapa de espesor t da t; para un cubo
    de lado L da L/3. Dividido por la dimension mas chica de la pieza:

        >= 0.28  macizo      (el volumen ES la masa)
        >= 0.12  intermedio  (pared gruesa)
        <  0.12  cascara     (hueco con pared fina)
    """
    bm = bmesh.new(); bm.from_mesh(o.data); bm.normal_update()
    V = abs(bm.calc_volume(signed=True))
    A = sum(f.calc_area() for f in bm.faces)
    bm.free()
    esp = (2.0 * V / A) if A > 1e-12 else 0.0
    minima = max(min(o.dimensions), 1e-6)
    r = esp / minima
    return {"espesor_eq_mm": round(esp * 1000, 1),
            "dim_min_mm": round(minima * 1000, 1),
            "razon": round(r, 3),
            "clase": "macizo" if r >= 0.28 else ("intermedio" if r >= 0.12 else "cascara")}


def _stats(o):
    bm = bmesh.new(); bm.from_mesh(o.data); bm.normal_update()
    s = {"caras": len(bm.faces), "verts": len(bm.verts),
         "ngons": sum(1 for f in bm.faces if len(f.verts) > 4),
         "no_manifold": sum(1 for e in bm.edges if not e.is_manifold),
         "interiores": sum(1 for f in bm.faces
                           if all(len(e.link_faces) > 2 for e in f.edges)),
         "vol": round(bm.calc_volume(signed=True), 9),
         "vol_signo": bm.calc_volume(signed=True)}
    bm.free()
    return s


def verificar(colecciones):
    """Devuelve el veredicto RA-002 de las collections dadas."""
    if isinstance(colecciones, str):
        colecciones = [colecciones]
    objs = [o for c in colecciones for o in bpy.data.collections[c].all_objects
            if o.type == 'MESH']
    bv = {o.name: _bvh(o) for o in objs}
    cruces = [f"{objs[i].name} x {objs[j].name}"
              for i in range(len(objs)) for j in range(i + 1, len(objs))
              if bv[objs[i].name].overlap(bv[objs[j].name])]
    st = {o.name: _stats(o) for o in objs}
    invertidas = [k for k, v in st.items() if v["vol_signo"] <= 0.0]
    rell = {o.name: relleno(o) for o in objs}
    clases = {}
    for v in rell.values():
        clases[v["clase"]] = clases.get(v["clase"], 0) + 1
    fallas = []
    if cruces:      fallas.append("interpenetracion")
    if invertidas:  fallas.append("normales invertidas")
    if sum(v["no_manifold"] for v in st.values()): fallas.append("no manifold")
    if sum(v["interiores"] for v in st.values()):  fallas.append("caras interiores")
    return {
        "objetos": len(objs),
        "caras": sum(v["caras"] for v in st.values()),
        "verts": sum(v["verts"] for v in st.values()),
        "ngons": sum(v["ngons"] for v in st.values()),
        "pares_que_se_cruzan": cruces,
        "normales_invertidas": invertidas,
        "no_manifold": sum(v["no_manifold"] for v in st.values()),
        "caras_interiores": sum(v["interiores"] for v in st.values()),
        "relleno": clases,
        "cascaras": [k for k, v in rell.items() if v["clase"] == "cascara"],
        "veredicto": "EN LEY" if not fallas else "FUERA DE LEY: " + ", ".join(fallas),
    }

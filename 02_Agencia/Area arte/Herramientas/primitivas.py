"""Primitivas de modelado low poly — Vaultrum / registro Arte_Blender.

Se instala UNA vez por sesion de Blender; despues cada llamada MCP manda datos,
no funciones (ver AiCare_Blender.md, regla 6).

    exec(open(r"<ruta>/primitivas.py").read())

Todo se construye con bmesh, con las normales recalculadas hacia afuera y el
resultado en la collection que se le pase (o en la escena si no se pasa ninguna).
"""
import bpy, bmesh, math
from mathutils import Vector, Matrix


def material(nombre, color, rugosidad=0.8, metal=0.0):
    m = bpy.data.materials.get(nombre) or bpy.data.materials.new(nombre)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*color, 1.0)
    b.inputs["Roughness"].default_value = rugosidad
    b.inputs["Metallic"].default_value = metal
    m.diffuse_color = (*color, 1.0)          # para el viewport solid y Workbench
    return m


def _crear(nombre, bm, mat, col):
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(nombre)
    bm.to_mesh(me)
    bm.free()
    o = bpy.data.objects.new(nombre, me)
    (col or bpy.context.scene.collection).objects.link(o)
    if mat:
        o.data.materials.append(mat)
    return o


def caja(nombre, x0, x1, y0, y1, z0, z1, mat=None, col=None):
    """Caja por extremos. Acepta los limites en cualquier orden (no invierte normales)."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector(((x0 + x1) / 2 + v.co.x * abs(x1 - x0),
                       (y0 + y1) / 2 + v.co.y * abs(y1 - y0),
                       (z0 + z1) / 2 + v.co.z * abs(z1 - z0)))
    return _crear(nombre, bm, mat, col)


def loft(nombre, secciones, mat=None, col=None):
    """secciones = [(x, semiancho, z0, z1)] -> prisma cerrado lofteado sobre X."""
    bm = bmesh.new()
    anillos = [[bm.verts.new(p) for p in ((x, w, z0), (x, w, z1), (x, -w, z1), (x, -w, z0))]
               for x, w, z0, z1 in secciones]
    for a, b in zip(anillos, anillos[1:]):
        for i in range(4):
            bm.faces.new((a[i], a[(i + 1) % 4], b[(i + 1) % 4], b[i]))
    bm.faces.new(tuple(reversed(anillos[0])))
    bm.faces.new(tuple(anillos[-1]))
    return _crear(nombre, bm, mat, col)


def loft_anillos(nombre, anillos_pts, tapar=True, mat=None, col=None):
    """anillos_pts = [[Vector,...], ...] con el MISMO N por anillo -> cascara cerrada.
    Es la base de una carroceria: un anillo por estacion, N puntos por anillo."""
    bm = bmesh.new()
    anillos = [[bm.verts.new(p) for p in ring] for ring in anillos_pts]
    n = len(anillos_pts[0])
    for a, b in zip(anillos, anillos[1:]):
        for i in range(n):
            j = (i + 1) % n
            bm.faces.new((a[i], a[j], b[j], b[i]))
    if tapar:
        bm.faces.new(tuple(reversed(anillos[0])))
        bm.faces.new(tuple(anillos[-1]))
    return _crear(nombre, bm, mat, col)


def prisma(nombre, perfil, a, b, eje='Y', triangular_tapas=True, mat=None, col=None):
    """perfil = [(u, v)] cerrado, extruido de `a` a `b` sobre `eje`.
    Las tapas se triangulan: un ngon concavo se tesela mal y los picos desaparecen."""
    def punto(u, v, w):
        return {'Y': (u, w, v), 'X': (w, u, v), 'Z': (u, v, w)}[eje]
    bm = bmesh.new()
    va = [bm.verts.new(punto(u, v, a)) for u, v in perfil]
    vb = [bm.verts.new(punto(u, v, b)) for u, v in perfil]
    k = len(perfil)
    for i in range(k):
        j = (i + 1) % k
        bm.faces.new((va[i], va[j], vb[j], vb[i]))
    t = [bm.faces.new(tuple(reversed(va))), bm.faces.new(tuple(vb))]
    if triangular_tapas:
        bmesh.ops.triangulate(bm, faces=t)
    return _crear(nombre, bm, mat, col)


def anillo_rect(nombre, ext, ins, z0, z1, mat=None, col=None):
    """Marco rectangular cerrado (parapeto, marco, borde)."""
    bm = bmesh.new()
    E = [(ext, ext), (-ext, ext), (-ext, -ext), (ext, -ext)]
    I = [(ins, ins), (-ins, ins), (-ins, -ins), (ins, -ins)]
    eb = [bm.verts.new((x, y, z0)) for x, y in E]
    et = [bm.verts.new((x, y, z1)) for x, y in E]
    ib = [bm.verts.new((x, y, z0)) for x, y in I]
    it = [bm.verts.new((x, y, z1)) for x, y in I]
    for i in range(4):
        j = (i + 1) % 4
        bm.faces.new((eb[i], eb[j], et[j], et[i]))
        bm.faces.new((it[i], it[j], ib[j], ib[i]))
        bm.faces.new((et[i], et[j], it[j], it[i]))
        bm.faces.new((ib[i], ib[j], eb[j], eb[i]))
    return _crear(nombre, bm, mat, col)


def tubo(nombre, centro, r_ext, r_int, ancho, n=16, eje='Y', mat=None, col=None):
    """Tubo cerrado (neumatico, aro). Hueco de verdad: la llanta entra sin cruzarlo."""
    cx, cy, cz = centro
    def punto(ang, r, off):
        c, s = math.cos(ang), math.sin(ang)
        return {'Y': (cx + r * c, off, cz + r * s),
                'X': (off, cy + r * c, cz + r * s),
                'Z': (cx + r * c, cy + r * s, off)}[eje]
    base = {'Y': cy, 'X': cx, 'Z': cz}[eje]
    bm = bmesh.new()
    def aro(r, off):
        return [bm.verts.new(punto(2 * math.pi * i / n, r, off)) for i in range(n)]
    a = aro(r_ext, base - ancho / 2); b = aro(r_ext, base + ancho / 2)
    c = aro(r_int, base + ancho / 2); d = aro(r_int, base - ancho / 2)
    for u, v in ((a, b), (b, c), (c, d), (d, a)):
        for i in range(n):
            j = (i + 1) % n
            bm.faces.new((u[i], u[j], v[j], v[i]))
    return _crear(nombre, bm, mat, col)


def separar_panel(nombre, malla, indices, luz=0.004, espesor=0.003, mat=None, col=None):
    """Corta un panel de una cascara cerrada y lo vuelve solido.

    RA-004, ley de la junta: la retraccion tiene que ser MAYOR que el espesor
    (luz > espesor), y tiene que ser un inset real -- una escala uniforme retrae
    distinto en los bordes largos que en los cortos."""
    bs = bmesh.new(); bs.from_mesh(malla); bs.faces.ensure_lookup_table()
    ids = set(indices)
    bmesh.ops.delete(bs, geom=[f for f in bs.faces if f.index not in ids], context='FACES')
    r = bmesh.ops.inset_region(bs, faces=list(bs.faces), thickness=luz, depth=0.0,
                               use_boundary=True, use_even_offset=True)
    bmesh.ops.delete(bs, geom=r['faces'], context='FACES')
    o = _crear(nombre, bs, mat, col)
    md = o.modifiers.new("s", 'SOLIDIFY')
    md.thickness, md.offset, md.use_rim = espesor, -1.0, True
    bpy.context.view_layer.objects.active = o
    bpy.ops.object.modifier_apply(modifier=md.name)
    return o


def poner_origen(o, punto):
    """Lleva el origen del objeto a `punto` SIN mover la geometria en el mundo.
    (RA-005: hacerlo al reves corre el asset entero y RA-002 igual da EN LEY.)"""
    p = Vector(punto)
    o.data.transform(Matrix.Translation(o.matrix_world.translation - p))
    o.data.update()
    o.location = p
    bpy.context.view_layer.update()
    return o


def emparentar(objetos, ancla):
    """RA-001. Usa identidad como parent inverse: los hijos ya estan en
    coordenadas del asset, y matrix_world del ancla puede estar sin actualizar."""
    for o in objetos:
        if o is not ancla:
            o.parent = ancla
            o.matrix_parent_inverse = Matrix.Identity(4)
    bpy.context.view_layer.update()


def girar_malla(o, grados, eje='Z'):
    o.data.transform(Matrix.Rotation(math.radians(grados), 4, eje))
    o.data.update()
    return o


def _afuera(o):
    """Normales hacia afuera, decidido por el SIGNO DEL VOLUMEN, no por heuristica."""
    bm = bmesh.new(); bm.from_mesh(o.data)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.normal_update()
    if bm.calc_volume(signed=True) < 0:
        bmesh.ops.reverse_faces(bm, faces=bm.faces)
    bm.to_mesh(o.data); bm.free(); o.data.update()
    return o


def limpiar(objetos):
    """shade flat + reporta que objeto quedo con transform sucio para exportar."""
    for o in objetos:
        _afuera(o)
        o.select_set(False)
        bpy.context.view_layer.objects.active = o
        bpy.ops.object.shade_flat()
    return [o.name for o in objetos
            if tuple(round(v, 4) for v in o.scale) != (1.0, 1.0, 1.0)
            or any(abs(a) > 1e-4 for a in o.rotation_euler)]


def relajar(moviles, fijos=(), paso=0.006, iteraciones=600, plano=False):
    """RA-002 -- separa piezas hasta el PRIMER instante sin interpenetracion.

    Se colocan cruzadas a proposito y se empujan de a `paso` en la direccion que
    las separa; se corta cuando BVHTree.overlap() devuelve vacio. Ese primer paso
    es el contacto exacto: se tocan y no se atraviesan.

    `plano=True` empuja solo en XY (util para un anillo apoyado en el piso).
    Devuelve (iteraciones, convergio).
    """
    from mathutils.bvhtree import BVHTree

    def bvh(o):
        bm = bmesh.new(); bm.from_mesh(o.data)
        bmesh.ops.triangulate(bm, faces=bm.faces)
        bm.transform(o.matrix_world)
        v = [x.co.copy() for x in bm.verts]
        t = [[x.index for x in f.verts] for f in bm.faces]
        bm.free()
        return BVHTree.FromPolygons(v, t, all_triangles=True, epsilon=0.0)

    piezas = list(moviles) + list(fijos)
    n_mov = len(moviles)
    it, movido = 0, True
    while movido and it < iteraciones:
        movido = False; it += 1
        bv = [bvh(p) for p in piezas]
        for i in range(len(piezas)):
            for j in range(i + 1, len(piezas)):
                if not bv[i].overlap(bv[j]):
                    continue
                d = piezas[j].matrix_world.translation - piezas[i].matrix_world.translation
                if plano:
                    d.z = 0.0
                d = d.normalized() if d.length > 1e-6 else Vector((1, 0, 0))
                a_mov, b_mov = i < n_mov, j < n_mov
                if a_mov and b_mov:
                    piezas[i].location -= d * (paso / 2); piezas[j].location += d * (paso / 2)
                elif a_mov:
                    piezas[i].location -= d * paso
                elif b_mov:
                    piezas[j].location += d * paso
                else:
                    continue
                movido = True
        if movido:
            bpy.context.view_layer.update()
    return it, not movido


def esquirla(nombre, centro, direccion, alto, radio, lados=5, semilla=0, mat=None, col=None):
    """Lasca de roca: prisma conico apoyado sobre una cara, apuntando afuera y arriba."""
    import random as _r
    rnd = _r.Random(semilla)
    d = Vector(direccion).normalized()
    lat = d.cross(Vector((0, 0, 1)))
    if lat.length < 1e-4:
        lat = Vector((1, 0, 0))
    lat.normalize()
    up = d.cross(lat).normalized()

    def aro(r, t, giro):
        pts = []
        for i in range(lados):
            a = 2 * math.pi * i / lados + giro
            rr = r * (1.0 + rnd.uniform(-0.22, 0.22))
            pts.append(Vector(centro) + d * t + lat * (rr * math.cos(a)) + up * (rr * math.sin(a)))
        return pts

    return loft_anillos(nombre, [aro(radio, 0.0, 0.0),
                                 aro(radio * 0.78, alto * 0.55, 0.35),
                                 aro(radio * 0.42, alto, 0.7)],
                        True, mat, col)


def torno(nombre, perfil, n=16, origen=(0, 0, 0), eje=(0, 0, 1), mat=None, col=None):
    """Superficie de revolucion (torno). perfil = [(radio, s)] recorrido de punta a
    punta sobre el eje; un radio 0 se resuelve como POLO (abanico de triangulos),
    asi que un perfil que arranca y termina en el eje da un solido cerrado -- y si
    baja por adentro antes de cerrar, da un solido HUECO de verdad (un anima, un
    vaso, un cano). Sin esto un cilindro con agujero hay que sacarlo con boolean.
    """
    d = Vector(eje).normalized()
    u = d.cross(Vector((0, 1, 0)))
    if u.length < 1e-5:
        u = d.cross(Vector((1, 0, 0)))
    u.normalize()
    v = d.cross(u).normalized()
    o = Vector(origen)

    bm = bmesh.new()
    aros = []
    for r, s in perfil:
        c = o + d * s
        if abs(r) < 1e-6:
            aros.append([bm.verts.new(c)])
        else:
            aros.append([bm.verts.new(c + u * (r * math.cos(2 * math.pi * i / n))
                                        + v * (r * math.sin(2 * math.pi * i / n)))
                         for i in range(n)])
    for a, b in zip(aros, aros[1:]):
        if len(a) == 1 and len(b) == 1:
            continue
        if len(a) == 1:
            for i in range(n):
                bm.faces.new((a[0], b[i], b[(i + 1) % n]))
        elif len(b) == 1:
            for i in range(n):
                bm.faces.new((a[i], a[(i + 1) % n], b[0]))
        else:
            for i in range(n):
                j = (i + 1) % n
                bm.faces.new((a[i], a[j], b[j], b[i]))
    if len(aros[0]) > 1:
        bm.faces.new(tuple(reversed(aros[0])))
    if len(aros[-1]) > 1:
        bm.faces.new(tuple(aros[-1]))
    return _crear(nombre, bm, mat, col)


def sillares(nombre, n, r_int, r_ext, z0, z1, luz_ang=0.030, fase=0.0, mat=None, col=None):
    """Anillo de mamposteria: n bloques trapezoidales, cada uno una isla cerrada
    dentro de la MISMA malla (RA-001: un curso de sillares es UNA pieza)."""
    bm = bmesh.new()
    paso = 2 * math.pi / n
    for k in range(n):
        a0 = fase + k * paso + luz_ang / 2
        a1 = fase + (k + 1) * paso - luz_ang / 2
        pts = [(r_int, a0), (r_ext, a0), (r_ext, a1), (r_int, a1)]
        base = [bm.verts.new((r * math.cos(a), r * math.sin(a), z0)) for r, a in pts]
        alto = [bm.verts.new((r * math.cos(a), r * math.sin(a), z1)) for r, a in pts]
        for i in range(4):
            j = (i + 1) % 4
            bm.faces.new((base[i], base[j], alto[j], alto[i]))
        bm.faces.new(tuple(reversed(base)))
        bm.faces.new(tuple(alto))
    return _crear(nombre, bm, mat, col)


def centro_masa(objetos, densidad, por_defecto=1000.0):
    """Centro de masa REAL y masa en kg, por volumen x densidad de cada material.

    densidad: {nombre_de_material: kg/m3}. Usa el teorema de la divergencia sobre
    los triangulos, asi que vale para cualquier solido cerrado, hueco incluido.

    RA-008: lo que se APOYA lleva el origen en el piso; lo que VUELA lo lleva en
    su centro de masa, porque es el punto sobre el que gira en el aire.
    """
    total_m = 0.0
    acumulado = Vector((0.0, 0.0, 0.0))
    for o in objetos:
        nombre_mat = o.data.materials[0].name if o.data.materials else ""
        rho = densidad.get(nombre_mat, por_defecto)
        bm = bmesh.new(); bm.from_mesh(o.data)
        bmesh.ops.triangulate(bm, faces=bm.faces)
        bm.transform(o.matrix_world)
        V = 0.0
        C = Vector((0.0, 0.0, 0.0))
        for f in bm.faces:
            a, b, c = (v.co for v in f.verts)
            dv = a.dot(b.cross(c)) / 6.0
            V += dv
            C += (a + b + c) * (dv / 4.0)
        bm.free()
        if abs(V) > 1e-12:
            acumulado += C * rho
            total_m += V * rho
    return (acumulado / total_m if abs(total_m) > 1e-12 else Vector()), total_m

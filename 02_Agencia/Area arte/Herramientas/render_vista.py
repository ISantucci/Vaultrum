"""Render de asset a archivo — Vaultrum / registro Arte_Blender.

AiCare, regla 5: no se captura la pantalla, se renderiza el asset.
Workbench sale igual al viewport en solid, no necesita luces, no compila shaders
y NO depende de que la UI de Blender este viva.

    exec(open(r"<ruta>/render_vista.py").read())
    vista("Voyage_lateral.png", (0,-14,0.74), (0,0,0.74), res=(940,400), orto=4.62,
          solo="Voyage")
"""
import bpy, os
from mathutils import Vector

DIR_VISTAS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(
    globals().get("__file__", "x")))), "Vistas") if globals().get("__file__") else None


def vista(nombre, pos, hacia, lens=50, res=(800, 600), orto=None, solo=None,
          carpeta=None):
    """Renderiza a <carpeta>/<nombre>. `solo` = nombre de collection a aislar."""
    sc = bpy.context.scene
    cam_prev, motor_prev = sc.camera, sc.render.engine
    ocultas = []
    if solo:
        for c in sc.collection.children:
            if c.name != solo:
                ocultas.append((c, c.hide_render)); c.hide_render = True
        for o in sc.collection.objects:
            o.hide_render = True

    cd = bpy.data.cameras.new("_vista"); cd.lens = lens
    if orto:
        cd.type, cd.ortho_scale = 'ORTHO', orto
    cam = bpy.data.objects.new("_vista", cd)
    sc.collection.objects.link(cam)
    cam.location = Vector(pos)
    cam.rotation_euler = (Vector(hacia) - cam.location).to_track_quat('-Z', 'Y').to_euler()
    sc.camera = cam

    sc.render.engine = 'BLENDER_WORKBENCH'
    sh = sc.display.shading
    sh.light, sh.color_type = 'STUDIO', 'MATERIAL'
    sh.show_shadows, sh.show_cavity = True, True
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.resolution_percentage = 100
    sc.render.image_settings.file_format = 'PNG'
    destino = carpeta or DIR_VISTAS or bpy.app.tempdir
    os.makedirs(destino, exist_ok=True)
    sc.render.filepath = os.path.join(destino, nombre)
    bpy.ops.render.render(write_still=True)

    sc.camera, sc.render.engine = cam_prev, motor_prev
    bpy.data.objects.remove(cam, do_unlink=True)
    bpy.data.cameras.remove(cd)
    for c, h in ocultas:
        c.hide_render = h
    if solo:
        for o in sc.collection.objects:
            o.hide_render = False
    return sc.render.filepath

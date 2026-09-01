#!/usr/bin/env python3
"""Vaultrum - generador de los graficos del sistema.

Un grafico por area de la Agencia, uno por torre, y uno del sistema entero.
De cada uno salen DOS archivos con el mismo contenido y las mismas coordenadas:

    <nombre>.drawio    editable en draw.io / diagrams.net (mxGraph XML)
    <nombre>.svg       mirable en cualquier lado, sin instalar nada

POR QUE UN GENERADOR Y NO DOCE ARCHIVOS A MANO
Doce diagramas dibujados a mano divergen igual que doce textos que dicen lo mismo:
uno se edita, los otros no, y a los dos meses ninguno describe el sistema. Aca la
FUENTE es la especificacion de abajo -- una lista de nodos y aristas por diagrama --
y el dibujo es una copia generada. Si el sistema cambia, se corrige la spec y se
regenera todo con la misma forma.

    python3 generar_graficos.py

El lenguaje visual es el mismo en los doce, para que se puedan leer en serie:

    insumo       lo que entra al area, y lo produjo otro
    rol          un agente o sub-agente: alguien con responsabilidad
    artefacto    una salida registrable y numerada
    gate         una decision que puede frenar
    instrumento  un script: su salida es la evidencia
    externo      algo que vive fuera de esta area
    nota         una aclaracion, sin caja
"""
import os, xml.sax.saxutils as sx

COL, FILA = 250, 125          # paso de la grilla
ANCHO, ALTO = 200, 62         # caja por defecto
MARGEN = 75                   # deja lugar para las flechas que vuelven por afuera

ESTILOS = {
    #            relleno    borde      texto      forma
    'insumo':    ('#EAF2FB', '#4A7EBB', '#1B3A5C', 'round'),
    'rol':       ('#FFFFFF', '#3D3D3D', '#1A1A1A', 'rect'),
    'artefacto': ('#FFF4E0', '#C98A2B', '#5C3B08', 'rect'),
    'gate':      ('#FDE9E9', '#C0504D', '#5C1A18', 'round'),
    'instrumento':('#EAF6EC', '#3F8A4E', '#14401E', 'hex'),
    'externo':   ('#F2F2F2', '#9A9A9A', '#4A4A4A', 'dash'),
    'nota':      ('none',    'none',    '#6A6A6A', 'plain'),
    'capa':      ('#EDE7F6', '#6A4FA3', '#2E1A5C', 'round'),
}
ANCHO_CHAR = 6.35             # ancho medio de un char a 12px en la fuente base


def envolver(texto, ancho_px, tam=12):
    """Parte el texto en lineas que entran en la caja. El SVG no envuelve solo."""
    cupo = max(8, int((ancho_px - 16) / (ANCHO_CHAR * tam / 12.0)))
    lineas, actual = [], ''
    for palabra in texto.split():
        prueba = (actual + ' ' + palabra).strip()
        if len(prueba) <= cupo:
            actual = prueba
        else:
            if actual:
                lineas.append(actual)
            actual = palabra
    if actual:
        lineas.append(actual)
    return lineas or ['']


class Diagrama:
    def __init__(self, clave, titulo, subtitulo):
        self.clave, self.titulo, self.subtitulo = clave, titulo, subtitulo
        self.nodos, self.aristas = {}, []
        self.orden = []

    def n(self, ident, etiqueta, tipo, col, fila, ancho=ANCHO, alto=ALTO):
        self.nodos[ident] = dict(id=ident, txt=etiqueta, tipo=tipo,
                                 x=MARGEN + col * COL, y=100 + fila * FILA,
                                 w=ancho, h=alto)
        self.orden.append(ident)
        return self

    def a(self, desde, hasta, etiqueta='', tipo='solida'):
        self.aristas.append(dict(a=desde, b=hasta, txt=etiqueta, tipo=tipo))
        return self

    # ---------- geometria compartida por los dos formatos ----------
    def puertos(self, na, nb):
        """De donde sale y a donde entra la flecha, segun posicion relativa."""
        ax, ay, aw, ah = na['x'], na['y'], na['w'], na['h']
        bx, by, bw, bh = nb['x'], nb['y'], nb['w'], nb['h']
        if abs((ay + ah / 2) - (by + bh / 2)) < 30:               # misma fila
            if bx > ax:
                return (ax + aw, ay + ah / 2), (bx, by + bh / 2)
            return (ax, ay + ah / 2), (bx + bw, by + bh / 2)
        if abs((ax + aw / 2) - (bx + bw / 2)) < 30:               # misma columna
            if by > ay:
                return (ax + aw / 2, ay + ah), (bx + bw / 2, by)
            return (ax + aw / 2, ay), (bx + bw / 2, by + bh)
        if by > ay:
            return (ax + aw / 2, ay + ah), (bx + bw / 2, by)
        return (ax + aw / 2, ay), (bx + bw / 2, by + bh)

    def camino(self, ar, i):
        """Los puntos de la arista. Devuelve (lista de puntos, punto de etiqueta).

        Tres casos, y el tercero es el que importa. Una arista que VUELVE --el
        rebote del Revisor al Disenador, la Escuela al Core-- tiene su destino
        arriba, y si se dibuja recta atraviesa todas las cajas del medio. Esas
        salen por el costado y rodean. Un diagrama en el que una flecha pasa por
        encima de una caja dice algo que no es cierto: que la toca.
        """
        na, nb = self.nodos[ar['a']], self.nodos[ar['b']]
        ax, ay, aw, ah = na['x'], na['y'], na['w'], na['h']
        bx, by, bw, bh = nb['x'], nb['y'], nb['w'], nb['h']
        cya, cyb = ay + ah / 2, by + bh / 2

        if by + bh < ay - 5:                      # vuelve hacia arriba: rodea
            lado = min(ax, bx) - 30 - (i % 3) * 14
            pts = [(ax, cya), (lado, cya), (lado, cyb), (bx, cyb)]
            return pts, (lado, (cya + cyb) / 2)

        if abs(cya - cyb) < 30:                   # misma fila
            if bx > ax:
                pts = [(ax + aw, cya), (bx, cyb)]
            else:
                pts = [(ax, cya), (bx + bw, cyb)]
            return pts, ((pts[0][0] + pts[1][0]) / 2, cya)

        if abs((ax + aw / 2) - (bx + bw / 2)) < 30:   # misma columna
            pts = [(ax + aw / 2, ay + ah), (bx + bw / 2, by)]
            return pts, (ax + aw / 2, (ay + ah + by) / 2)

        # baja y se corre: escalon, con la horizontal escalonada por arista para
        # que dos aristas largas no se pisen la linea ni la etiqueta
        frac = 0.42 + (i % 3) * 0.12
        corte = (ay + ah) + ((by) - (ay + ah)) * frac
        pts = [(ax + aw / 2, ay + ah), (ax + aw / 2, corte), (bx + bw / 2, corte), (bx + bw / 2, by)]
        return pts, ((ax + aw / 2 + bx + bw / 2) / 2, corte)

    def lienzo(self):
        an = max(n['x'] + n['w'] for n in self.nodos.values()) + MARGEN
        al = max(n['y'] + n['h'] for n in self.nodos.values()) + MARGEN + 20
        return int(an), int(al)

    def puertos(self, na, nb):   # compatibilidad: el ruteo real esta en camino()
        return (na['x'] + na['w'], na['y'] + na['h'] / 2), (nb['x'], nb['y'] + nb['h'] / 2)


def svg_forma(n):
    relleno, borde, color, forma = ESTILOS[n['tipo']]
    x, y, w, h = n['x'], n['y'], n['w'], n['h']
    if forma == 'plain':
        return ''
    if forma == 'hex':
        c = 14
        pts = f"{x+c},{y} {x+w-c},{y} {x+w},{y+h/2} {x+w-c},{y+h} {x+c},{y+h} {x},{y+h/2}"
        return f'<polygon points="{pts}" fill="{relleno}" stroke="{borde}" stroke-width="1.6"/>'
    rx = 14 if forma == 'round' else 3
    guion = ' stroke-dasharray="6 4"' if forma == 'dash' else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{relleno}" stroke="{borde}" stroke-width="1.6"{guion}/>')


def a_svg(d):
    an, al = d.lienzo()
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{an}" height="{al}" '
         f'viewBox="0 0 {an} {al}" font-family="Segoe UI, Helvetica, Arial, sans-serif">',
         f'<rect width="{an}" height="{al}" fill="#FFFFFF"/>',
         '<defs><marker id="f" markerWidth="9" markerHeight="9" refX="8" refY="4.5" '
         'orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#5A5A5A"/></marker>'
         '<marker id="fr" markerWidth="9" markerHeight="9" refX="8" refY="4.5" '
         'orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#C0504D"/></marker></defs>',
         f'<text x="{MARGEN}" y="42" font-size="21" font-weight="600" fill="#1A1A1A">'
         f'{sx.escape(d.titulo)}</text>',
         f'<text x="{MARGEN}" y="66" font-size="12.5" fill="#6A6A6A">'
         f'{sx.escape(d.subtitulo)}</text>']

    for i, ar in enumerate(d.aristas):
        pts, (mx, my) = d.camino(ar, i)
        col = '#C0504D' if ar['tipo'] == 'rebote' else '#5A5A5A'
        mk = 'fr' if ar['tipo'] == 'rebote' else 'f'
        guion = ' stroke-dasharray="7 5"' if ar['tipo'] in ('rebote', 'punteada') else ''
        camino = 'M ' + ' L '.join('%.0f,%.0f' % q for q in pts)
        p.append(f'<path d="{camino}" fill="none" stroke="{col}" stroke-width="1.5"'
                 f'{guion} marker-end="url(#{mk})"/>')
        if ar['txt']:
            ancho_txt = len(ar['txt']) * 5.6 + 12
            mx = min(max(mx, ancho_txt / 2 + 4), an - ancho_txt / 2 - 4)
            p.append(f'<rect x="{mx-ancho_txt/2:.0f}" y="{my-9:.0f}" width="{ancho_txt:.0f}" '
                     f'height="16" rx="3" fill="#FFFFFF" opacity="0.94"/>')
            p.append(f'<text x="{mx:.0f}" y="{my+3:.0f}" font-size="10.5" fill="{col}" '
                     f'text-anchor="middle">{sx.escape(ar["txt"])}</text>')

    for ident in d.orden:
        n = d.nodos[ident]
        p.append(svg_forma(n))
        _, _, color, forma = ESTILOS[n['tipo']]
        tam = 11.5 if forma != 'plain' else 11
        lineas = envolver(n['txt'], n['w'], tam)
        y0 = n['y'] + n['h'] / 2 - (len(lineas) - 1) * (tam + 2) / 2 + tam / 3
        peso = '600' if n['tipo'] in ('rol', 'gate', 'capa') else '400'
        anclaje = 'start' if forma == 'plain' else 'middle'
        cx = n['x'] if forma == 'plain' else n['x'] + n['w'] / 2
        for i, ln in enumerate(lineas):
            p.append(f'<text x="{cx:.0f}" y="{y0 + i*(tam+2):.0f}" font-size="{tam}" '
                     f'fill="{color}" font-weight="{peso}" text-anchor="{anclaje}">'
                     f'{sx.escape(ln)}</text>')
    p.append('</svg>')
    return '\n'.join(p)


ESTILO_DRAWIO = {
    'insumo':     'rounded=1;whiteSpace=wrap;html=1;fillColor=#EAF2FB;strokeColor=#4A7EBB;fontColor=#1B3A5C;',
    'rol':        'rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#3D3D3D;fontColor=#1A1A1A;fontStyle=1;',
    'artefacto':  'rounded=0;whiteSpace=wrap;html=1;fillColor=#FFF4E0;strokeColor=#C98A2B;fontColor=#5C3B08;',
    'gate':       'rounded=1;whiteSpace=wrap;html=1;fillColor=#FDE9E9;strokeColor=#C0504D;fontColor=#5C1A18;fontStyle=1;',
    'instrumento':'shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fillColor=#EAF6EC;strokeColor=#3F8A4E;fontColor=#14401E;',
    'externo':    'rounded=0;whiteSpace=wrap;html=1;dashed=1;fillColor=#F2F2F2;strokeColor=#9A9A9A;fontColor=#4A4A4A;',
    'nota':       'text;html=1;align=left;verticalAlign=middle;fontColor=#6A6A6A;',
    'capa':       'rounded=1;whiteSpace=wrap;html=1;fillColor=#EDE7F6;strokeColor=#6A4FA3;fontColor=#2E1A5C;fontStyle=1;',
}


def a_drawio(d):
    an, al = d.lienzo()
    c = [f'<mxfile host="Vaultrum" type="device"><diagram name="{sx.escape(d.titulo)}">',
         f'<mxGraphModel dx="{an}" dy="{al}" grid="1" gridSize="10" page="1" '
         f'pageWidth="{an}" pageHeight="{al} " math="0" shadow="0"><root>',
         '<mxCell id="0"/><mxCell id="1" parent="0"/>',
         f'<mxCell id="titulo" value="{sx.escape(d.titulo)}" '
         'style="text;html=1;align=left;fontSize=21;fontStyle=1;" vertex="1" parent="1">'
         f'<mxGeometry x="{MARGEN}" y="20" width="700" height="30" as="geometry"/></mxCell>',
         f'<mxCell id="subtitulo" value="{sx.escape(d.subtitulo)}" '
         'style="text;html=1;align=left;fontSize=12;fontColor=#6A6A6A;" vertex="1" parent="1">'
         f'<mxGeometry x="{MARGEN}" y="52" width="900" height="20" as="geometry"/></mxCell>']
    for ident in d.orden:
        n = d.nodos[ident]
        c.append(f'<mxCell id="{sx.quoteattr(ident)[1:-1]}" value="{sx.escape(n["txt"])}" '
                 f'style="{ESTILO_DRAWIO[n["tipo"]]}" vertex="1" parent="1">'
                 f'<mxGeometry x="{n["x"]}" y="{n["y"]}" width="{n["w"]}" height="{n["h"]}" '
                 'as="geometry"/></mxCell>')
    for i, ar in enumerate(d.aristas):
        est = ('edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;jettySize=auto;'
               + ('dashed=1;strokeColor=#C0504D;fontColor=#C0504D;'
                  if ar['tipo'] == 'rebote' else
                  'dashed=1;strokeColor=#5A5A5A;' if ar['tipo'] == 'punteada'
                  else 'strokeColor=#5A5A5A;'))
        na, nb = d.nodos[ar['a']], d.nodos[ar['b']]
        if nb['y'] + nb['h'] < na['y'] - 5:     # vuelve: sale y entra por izquierda
            est += 'exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;'
        c.append(f'<mxCell id="e{i}" value="{sx.escape(ar["txt"])}" style="{est}" '
                 f'edge="1" parent="1" source="{sx.quoteattr(ar["a"])[1:-1]}" '
                 f'target="{sx.quoteattr(ar["b"])[1:-1]}">'
                 '<mxGeometry relative="1" as="geometry"/></mxCell>')
    c.append('</root></mxGraphModel></diagram></mxfile>')
    return '\n'.join(c)


def escribir(diagramas, destino='.'):
    for d in diagramas:
        for ext, texto in (('drawio', a_drawio(d)), ('svg', a_svg(d))):
            ruta = os.path.join(destino, '%s.%s' % (d.clave, ext))
            with open(ruta, 'w', encoding='utf-8', newline='\n') as f:
                f.write(texto)
        an, al = d.lienzo()
        print('  [ok] %-34s %d nodos, %d aristas  (%dx%d)'
              % (d.clave, len(d.nodos), len(d.aristas), an, al))


# =============================================================================
#  LA ESPECIFICACION. Esto es la fuente; los .drawio y .svg son copias.
# =============================================================================
def specs_a():
    """Produccion, Game Design, Level Design."""
    D = []

    d = Diagrama('agencia-01-produccion', 'Área de Producción',
                 'Dueña de la entrega: la abre con la intención y la cierra validándola. Puerta de entrada del Modo Vaultrum.')
    d.n('intencion', 'Intención abierta del owner · idea · problema · objetivo', 'insumo', 0, 0)
    d.n('consultor', '01 Consultor Estratégico — ¿tiene sentido?', 'rol', 1, 0)
    d.n('traductor', '02 Traductor Operativo — baja a tierra', 'rol', 2, 0)
    d.n('planificador', '03 Planificador — formaliza', 'rol', 3, 0)
    d.n('tl', 'TL-XXX  Timeline', 'artefacto', 4, 0)
    d.n('rq', 'RQ-XXX.n  Requerimiento', 'artefacto', 4, 1)
    d.n('areas', 'Pivoteo entre áreas: Game Design · Level Design · UI/UX · Programación · Calidad', 'externo', 4, 2, 220, 88)
    d.n('despachante', '05 Despachante — quién ejecuta y dónde', 'rol', 2, 2)
    d.n('qa', 'QA-XXX gate de entrega (Calidad)', 'externo', 3, 3)
    d.n('validador', '04 Validador de Entrega', 'rol', 2, 3)
    d.n('ve', 'VE-XXX  Validación', 'artefacto', 1, 3)
    d.n('estado', 'Cerrado · Ajustar · Pausado', 'gate', 0, 3)
    d.n('nota', 'El Despachante no es un paso del loop: corre de costado y sirve a los cuatro.', 'nota', 0, 4, 700, 20)
    d.a('intencion', 'consultor').a('consultor', 'traductor', 'idea validada')
    d.a('traductor', 'planificador', 'alcance').a('planificador', 'tl')
    d.a('tl', 'rq', 'cuelga').a('rq', 'areas', 'insumo de cada area')
    d.a('areas', 'qa', 'hilos cerrados').a('qa', 'validador', 'GO / CONDITIONAL GO')
    d.a('validador', 've').a('ve', 'estado')
    d.a('despachante', 'areas', 'rutea la ejecucion', 'punteada')
    d.a('validador', 'consultor', 'Ajustar', 'rebote')
    D.append(d)

    d = Diagrama('agencia-02-game-design', 'Área de Game Design (Technical)',
                 'Convierte un requerimiento jugable en reglas implementables y validables. No escribe código ni define alcance.')
    d.n('rq', 'RQ-XXX.n jugable (Producción)', 'insumo', 0, 0)
    d.n('uxsa', 'UXS mitad A — presupuesto de comunicación (UI/UX, ANTES del GDS)', 'insumo', 0, 1, 200, 88)
    d.n('core', 'VaultrumCore — criterio base', 'externo', 0, 2)
    d.n('gd', 'Área de Game Design: mecánicas · reglas · feedback · estados · balance', 'rol', 1, 1, 210, 88)
    d.n('gds', 'GDS-XXX.n Game Design Spec', 'artefacto', 2, 0)
    d.n('marco', 'GDS-XXX.0 marco común — solo si 3+ GDS comparten definiciones', 'artefacto', 2, 2, 200, 88)
    d.n('gate', 'Declara qué NO aplica y qué dimensión falta', 'gate', 2, 1)
    d.n('lds', 'Level Design → LDS', 'externo', 3, 0)
    d.n('uxsb', 'UI/UX mitad B → UXS', 'externo', 3, 1)
    d.n('prog', 'Programación → SOL', 'externo', 3, 2)
    d.a('rq', 'gd').a('uxsa', 'gd', 'condiciona').a('core', 'gd', 'principio 1', 'punteada')
    d.a('gd', 'gds').a('gd', 'gate').a('gd', 'marco', 'si aplica')
    d.a('gds', 'lds', 'si hay espacio').a('gate', 'uxsb', 'si alguien lo lee')
    d.a('gds', 'prog', 'GDS cerrado')
    D.append(d)

    d = Diagrama('agencia-03-level-design', 'Área de Level Design',
                 'Acomoda en el espacio y el tiempo un sistema ya diseñado. Opcional: existe solo si el hilo tiene dimensión espacial.')
    d.n('gds', 'GDS-XXX.n cerrado (Game Design)', 'insumo', 0, 0)
    d.n('ld', 'Área de Level Design: niveles · encuentros · checkpoints · pacing', 'rol', 1, 0, 215, 88)
    d.n('lds', 'LDS-XXX.n Level Design Spec', 'artefacto', 2, 0)
    d.n('nivel', 'nivel.py — leyes del espacio', 'instrumento', 2, 1)
    d.n('prog', 'Programación → SOL', 'externo', 3, 0)
    d.n('deuda', 'DEUDA: LDS no tiene contrato en contratos.txt. El Gate lo reporta "sin contrato": ni lo aprueba ni lo falla. Se destraba con 4 LDS reales.', 'externo', 1, 2, 300, 88)
    d.a('gds', 'ld').a('ld', 'lds').a('lds', 'nivel', 'se mide').a('lds', 'prog')
    d.a('deuda', 'lds', '', 'punteada')
    D.append(d)
    return D


def specs_b():
    """UI/UX, Programacion, Control de Calidad."""
    D = []

    d = Diagrama('agencia-04-ui-ux', 'Área de UI/UX',
                 'Tres modos. Dicta el presupuesto de comunicación ANTES de que un sistema cierre, y después diseña y mide la interfaz.')
    d.n('rq', 'RQ-XXX.n', 'insumo', 0, 0)
    d.n('m1', 'Modo Presupuesto: cuánto se puede comunicar y por qué canal', 'rol', 1, 0, 200, 88)
    d.n('uxsa', 'UXS mitad A', 'artefacto', 2, 0)
    d.n('gds0', 'Game Design cierra el GDS contra ella', 'externo', 3, 0)
    d.n('gdsc', 'GDS-XXX.n cerrado', 'insumo', 0, 1)
    d.n('m2', 'Modo Interfaz: pantallas · HUD · jerarquía · feedback', 'rol', 1, 1, 200, 88)
    d.n('uxsb', 'UXS mitad B', 'artefacto', 2, 1)
    d.n('prog', 'Programación → SOL', 'externo', 3, 1)
    d.n('int', 'Interfaz que ya existe (juego o herramienta)', 'insumo', 0, 2)
    d.n('m3', 'Modo Pasada: medir lo que ya está', 'rol', 1, 2)
    d.n('leg', 'legibilidad.py — contraste WCAG · daltonismo · mapping · densidad', 'instrumento', 2, 2, 220, 88)
    d.n('nota', 'Es el único artefacto que abre ANTES que su insumo principal: por eso declara dos insumos y no uno.', 'nota', 0, 3, 780, 20)
    d.a('rq', 'm1').a('m1', 'uxsa').a('uxsa', 'gds0')
    d.a('gdsc', 'm2').a('m2', 'uxsb').a('uxsb', 'prog')
    d.a('int', 'm3').a('m3', 'leg')
    d.a('uxsb', 'leg', 'se mide', 'punteada')
    D.append(d)

    d = Diagrama('agencia-05-programacion', 'Área de Programación',
                 'Cuatro sub-agentes en loop. El loop no cierra hasta que el Revisor da OK. Consume el paquete de diseño y produce SOL + EJ.')
    d.n('paquete', 'RQ + GDS (+ LDS / UXS si existen)', 'insumo', 0, 0)
    d.n('analista', '1 · Analista Técnico — lee el proyecto real', 'rol', 1, 0)
    d.n('disenador', '2 · Diseñador de Solución — acá se decide', 'rol', 1, 1)
    d.n('sol', 'SOL-XXX.n + Contrato de ejecución', 'artefacto', 2, 1)
    d.n('gate1', 'GATE: aprobación del alcance', 'gate', 3, 1)
    d.n('ejecutor', '3 · Ejecutor Técnico — solo tras el OK', 'rol', 1, 2)
    d.n('ej', 'EJ-XXX.n', 'artefacto', 2, 2)
    d.n('gate2', 'GATE: existencia en disco', 'gate', 3, 2)
    d.n('revisor', '4 · Revisor Técnico', 'rol', 1, 3)
    d.n('despacho', 'Despacho: SOL con contrato → ejecutor barato. Donde se decide → modelo fuerte', 'externo', 0, 2, 220, 88)
    d.n('qa', 'Calidad → QA', 'externo', 3, 3)
    d.a('paquete', 'analista').a('analista', 'disenador', 'diagnostico')
    d.a('disenador', 'sol').a('sol', 'gate1').a('gate1', 'ejecutor', 'OK del owner')
    d.a('ejecutor', 'ej').a('ej', 'gate2').a('gate2', 'revisor')
    d.a('revisor', 'qa', 'hilo cerrado')
    d.a('despacho', 'ejecutor', 'rutea', 'punteada')
    d.a('revisor', 'disenador', 'hallazgo de diseno: reabre el SOL', 'rebote')
    D.append(d)

    d = Diagrama('agencia-06-control-de-calidad', 'Área de Control de Calidad',
                 'El gate que corre al terminar, antes del VE. No arregla lo que encuentra ni decide la entrega.')
    d.n('ej', 'EJ-XXX.n con revisión OK', 'insumo', 0, 0)
    d.n('qh', 'Gate de HILO — pase por riesgo', 'rol', 1, 0)
    d.n('qan', 'QA-XXX.n', 'artefacto', 2, 0)
    d.n('tl', 'TL con sus hilos cerrados', 'insumo', 0, 1)
    d.n('qe', 'Gate de ENTREGA — regresión + cobertura', 'rol', 1, 1)
    d.n('qa', 'QA-XXX', 'artefacto', 2, 1)
    d.n('ver', 'GO · CONDITIONAL GO · NO-GO', 'gate', 3, 1)
    d.n('cal', 'calidad.py — las leyes del QA', 'instrumento', 2, 2)
    d.n('ve', 'Producción → VE', 'externo', 4, 1)
    d.n('prog', 'Programación: defecto reproducible', 'externo', 4, 2)
    d.n('hallazgo', 'HALLAZGO: el QA-XXX.n existe en papel. 0 archivos QA-*.n en disco; todo cierra por gate de entrega.', 'externo', 0, 2, 300, 88)
    d.a('ej', 'qh').a('qh', 'qan').a('tl', 'qe').a('qan', 'qe', 'insumo')
    d.a('qe', 'qa').a('qa', 'ver').a('ver', 've', 'GO / CONDITIONAL GO')
    d.a('qa', 'cal', 'se mide').a('ver', 'prog', 'NO-GO: rebota', 'rebote')
    d.a('hallazgo', 'qh', '', 'punteada')
    D.append(d)
    return D


def specs_c():
    """Conocimiento, Arquitectura, Comunidad."""
    D = []

    d = Diagrama('agencia-07-conocimiento', 'Área de Conocimiento',
                 'La memoria de la Agencia. Tres modos. No produce trabajo de proyecto y no opera git.')
    d.n('vivo', 'Artefacto en curso (cualquier área)', 'insumo', 0, 0)
    d.n('copiloto', 'Modo Copiloto — asiste y NO firma', 'rol', 1, 0)
    d.n('cerrar', 'Artefacto por cerrar', 'insumo', 0, 1)
    d.n('gate', 'Modo Gate — mide y cierra o rebota', 'rol', 1, 1)
    d.n('doc', 'documentacion.py — la forma del texto', 'instrumento', 2, 1)
    d.n('dec', 'Cierra · Rebota', 'gate', 3, 1)
    d.n('entrega', 'Entrega cerrada (VE)', 'insumo', 0, 2)
    d.n('cosecha', 'Modo Cosecha — qué aprendizaje se absorbe', 'rol', 1, 2)
    d.n('commit', 'COMMIT-XXX propuesta al Core', 'artefacto', 2, 2)
    d.n('owner', 'Aprobación del owner', 'gate', 3, 2)
    d.n('core', '01_VaultrumCore', 'externo', 4, 2)
    d.n('arq', 'Arquitectura emplaza dónde vive', 'externo', 4, 1)
    d.a('vivo', 'copiloto').a('cerrar', 'gate').a('gate', 'doc').a('doc', 'dec')
    d.a('entrega', 'cosecha').a('cosecha', 'commit').a('commit', 'owner').a('owner', 'core', 'merge')
    d.a('dec', 'arq', 'donde vive', 'punteada')
    d.a('dec', 'cerrar', 'rebota con hallazgo', 'rebote')
    D.append(d)

    d = Diagrama('agencia-08-arquitectura', 'Área de Arquitectura',
                 'Dicta la forma del vault antes de que se construya, y ubica lo que entra. No escribe contenido ni mergea al Core.')
    d.n('preg', '¿Cómo se hace sin romper la arquitectura?', 'insumo', 0, 0)
    d.n('plano', 'Modo Plano — explica en cascada', 'rol', 1, 0)
    d.n('resp', 'Explicación (no escribe archivos)', 'artefacto', 2, 0)
    d.n('mat', 'Material nuevo: papers · libros · notas', 'insumo', 0, 1)
    d.n('empl', 'Modo Emplazamiento — decide dónde vive', 'rol', 1, 1)
    d.n('arq', 'ARQ-XXX salida del área', 'artefacto', 2, 1)
    d.n('vault', 'El vault entero', 'insumo', 0, 2)
    d.n('pasada', 'Modo Pasada — mide, repara, verifica', 'rol', 1, 2)
    d.n('inst', 'grafo.py · grafo.py --paquete · gemelos.py — las seis leyes', 'instrumento', 2, 2, 220, 88)
    d.n('hook', 'Gate de cierre .git/hooks/pre-commit', 'gate', 3, 2)
    d.n('exc', 'excepciones.txt — lo no declarado, falla', 'externo', 3, 1)
    d.a('preg', 'plano').a('plano', 'resp')
    d.a('mat', 'empl').a('empl', 'arq').a('vault', 'pasada').a('pasada', 'inst')
    d.a('inst', 'hook', 'en cada commit').a('inst', 'exc', 'consulta', 'punteada')
    D.append(d)

    d = Diagrama('torre-01-comunidad', 'Capa de Comunidad',
                 'Prepara las publicaciones del sistema. No publica, no inventa avances y no genera imágenes.')
    d.n('disp', 'Disparadores: cierre de épica · VE · merge al Core · área nueva', 'insumo', 0, 0, 230, 88)
    d.n('piso', 'Archivo — el piso de lo ya publicado', 'insumo', 0, 1)
    d.n('cont', 'Área de Contenido — lee el avance real contra el piso', 'rol', 1, 0, 200, 88)
    d.n('dec', '¿Hay avance real? Si no, no hay post', 'gate', 2, 0)
    d.n('pub', 'PUB-XXX — es/en en un solo bloque, separado por cinco guiones', 'artefacto', 3, 0, 210, 88)
    d.n('tres', 'Los tres tiempos: qué problema había · qué se implementó · caso de uso con resultado', 'externo', 2, 1, 210, 100)
    d.n('post', 'post.py — formato del PUB', 'instrumento', 3, 1)
    d.n('cat', 'Archivo / Catálogo / Leaderboard', 'artefacto', 4, 1)
    d.n('ver', 'Cada afirmación se verifica contra el archivo que la prueba', 'externo', 4, 0)
    d.a('disp', 'cont').a('piso', 'cont', 'compara').a('cont', 'dec').a('dec', 'pub', 'si')
    d.a('tres', 'pub', 'forma obligatoria', 'punteada').a('pub', 'post', 'se mide')
    d.a('pub', 'ver', '', 'punteada').a('post', 'cat')
    D.append(d)
    return D


def specs_d():
    """IA Operativa, Escuela, y el sistema entero."""
    D = []

    d = Diagrama('torre-02-ia-operativa', 'Capa de IA Operativa — los dos presupuestos',
                 'No produce trabajo: gobierna cómo opera la IA. Dos presupuestos que bajan la misma factura por caminos que no se tocan.')
    d.n('cap1', 'Costo de ENTRADA — qué contexto se carga', 'capa', 0, 0)
    d.n('aicare', 'AiCare — Pass GC de contexto', 'rol', 1, 0)
    d.n('contar', 'contar_contexto.py — mapa · pesados · carga · diff', 'instrumento', 2, 0, 220, 76)
    d.n('poda', 'Podado + delta medido (antes → después)', 'artefacto', 3, 0)
    d.n('commit', 'Corre en cada commit', 'gate', 1, 1)
    d.n('cap2', 'Costo de EJECUCIÓN — dónde corre y qué cuesta', 'capa', 0, 2)
    d.n('desp', '05 Despachante (agente de la Agencia)', 'rol', 1, 2)
    d.n('skill', 'vaultrum-despacho — el procedimiento', 'externo', 1, 3)
    d.n('bandeja', 'bandeja/ — ordenes → procesadas → resultados', 'instrumento', 2, 2, 220, 76)
    d.n('ejec', 'Ejecutores desde cmd: claude -p --permission-mode · codex exec - --sandbox', 'externo', 3, 2, 220, 88)
    d.n('desppy', 'despacho.py — cuántas · a quién · cuánto · fallos', 'instrumento', 2, 3, 220, 76)
    d.n('ley', 'Ley del subagente: escribe el archivo y devuelve un resumen corto. Corre sobre EJECUCIÓN, no sobre juicio.', 'nota', 0, 4, 820, 20)
    d.a('cap1', 'aicare').a('aicare', 'contar').a('contar', 'poda').a('commit', 'aicare', '', 'punteada')
    d.a('cap2', 'desp').a('desp', 'bandeja').a('bandeja', 'ejec').a('bandeja', 'desppy', 'log.txt')
    d.a('skill', 'desp', 'la usa', 'punteada')
    D.append(d)

    d = Diagrama('torre-03-escuela', 'Escuela Vaultrum',
                 'Aprendizaje proactivo con misión acotada. Escribe en la Biblioteca y NO mergea al Core.')
    d.n('gap', 'Misión acotada: gap declarado + presupuesto + barra', 'insumo', 0, 0, 230, 76)
    d.n('bib', '1 · Bibliotecario — qué hay y qué falta', 'rol', 1, 0)
    d.n('inv', '2 · Investigador — trae la fuente', 'rol', 1, 1)
    d.n('des', '3 · Destilador — escribe la ficha', 'rol', 1, 2)
    d.n('val', '4 · Validador — verifica invariantes', 'rol', 1, 3)
    d.n('bibl', 'Biblioteca: Fundamentos · Juegos por género · Construcción · Fuentes · Documentos', 'artefacto', 2, 1, 230, 88)
    d.n('bpy', 'biblioteca.py — catálogo derivado', 'instrumento', 2, 2)
    d.n('est', 'EST-XXX — la misión registrada', 'artefacto', 2, 3)
    d.n('aicare', 'AiCare cuida el presupuesto', 'externo', 0, 2)
    d.n('core', '01_VaultrumCore', 'externo', 3, 1)
    d.n('front', 'El Core tiene el PRECIO de todo y el MECANISMO de nada. La Biblioteca tiene lo otro.', 'externo', 3, 2, 220, 88)
    d.a('gap', 'bib').a('bib', 'inv').a('inv', 'des').a('des', 'val')
    d.a('des', 'bibl').a('bibl', 'bpy', 'se mide').a('val', 'est')
    d.a('aicare', 'des', '', 'punteada')
    d.a('bibl', 'core', 'NO mergea', 'rebote')
    d.a('front', 'bibl', '', 'punteada')
    D.append(d)

    d = Diagrama('sistema-completo', 'Vaultrum — el sistema entero',
                 'Cinco capas. El Core es fuente y retorno; la Agencia produce; las torres cuidan aprendizaje, publicación y operación de la IA.')
    d.n('core', '01_VaultrumCore — el criterio base: fuente y retorno', 'capa', 2, 0, 240, 62)
    d.n('arqui', 'Arquitectura — la forma del vault', 'rol', 0, 1)
    d.n('prod', 'Producción — TL + RQ, dueña de la entrega', 'rol', 2, 1, 220)
    d.n('cono', 'Conocimiento — qué vuelve al Core', 'rol', 4, 1)
    d.n('diseno', 'Game Design · Level Design · UI/UX → GDS · LDS · UXS', 'rol', 1, 2, 230, 62)
    d.n('prog', 'Programación — SOL + EJ', 'rol', 2, 2)
    d.n('cal', 'Calidad — QA', 'rol', 3, 2)
    d.n('proy', '06_Proyectos — el trabajo real: TL → RQ → GDS → SOL → EJ → QA → VE', 'artefacto', 2, 3, 300, 62)
    d.n('esc', '05_Escuela — Biblioteca + misiones EST', 'capa', 0, 3)
    d.n('com', '03_Comunidad — PUB + Archivo', 'capa', 4, 3)
    d.n('ia', '04_IA Operativa — AiCare + Despacho', 'capa', 0, 4)
    d.n('gate', 'Gate de cierre en cada commit: grafo · grafo --paquete · gemelos · documentacion', 'gate', 2, 4, 300, 62)
    d.n('puertas', 'CLAUDE.md · AGENTS.md — las dos puertas, idénticas', 'externo', 4, 4)
    d.a('core', 'prod', 'alimenta el arranque').a('prod', 'diseno').a('prod', 'prog')
    d.a('diseno', 'prog', 'paquete de diseno').a('prog', 'cal').a('cal', 'prod', 'QA → VE')
    d.a('prod', 'proy', 'aterriza en')
    d.a('cono', 'core', 'merge con aprobacion')
    d.a('cal', 'cono', 'aprendizaje', 'punteada')
    d.a('arqui', 'core', 'emplaza', 'punteada')
    d.a('esc', 'core', 'NO mergea', 'rebote')
    d.a('proy', 'com', 'lo publicable', 'punteada')
    d.a('ia', 'prog', 'rutea la ejecucion', 'punteada')
    d.a('gate', 'proy', 'mide antes de entrar', 'punteada')
    D.append(d)
    return D


def specs():
    return specs_a() + specs_b() + specs_c() + specs_d()


if __name__ == '__main__':
    aca = os.path.dirname(os.path.abspath(__file__))
    print('\n  Vaultrum - generando los graficos\n')
    escribir(specs(), aca)
    print('\n  Listo. Los .drawio se abren en draw.io; los .svg, en cualquier lado.\n')

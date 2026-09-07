# -*- coding: utf-8 -*-
"""El instrumento tambien se verifica, y se verifica en el EXTREMO de su rango.
Es RA-008, aplicada al propio arte.py."""
import sys, struct, json, os, tempfile
AQUI = os.path.dirname(os.path.abspath(__file__))
TMP  = tempfile.mkdtemp(prefix='arte_')
sys.path.insert(0, AQUI)
import arte

ok = fail = 0
def check(nombre, cond, detalle=''):
    global ok, fail
    if cond: ok += 1;  print('  ok   %s' % nombre)
    else:    fail += 1; print('  FALLA %s  %s' % (nombre, detalle))

def pieza(n, caras=10, verts=8, ngons=0, nm=0, inter=0, vol=1.0, area=6.0,
          dmin=1.0, zmin=0.0, esc=(1,1,1), rot=(0,0,0), padre=True, mats=None):
    return dict(nombre=n, caras=caras, verts=verts, ngons=ngons, no_manifold=nm,
                interiores=inter, volumen=vol, area=area, dim_min=dmin,
                bbox=[dmin]*3, z_min=zmin, escala=list(esc), rotacion=list(rot),
                emparentado=padre, materiales=mats or [])

print('\n--- LEY 1: normales invertidas, en el EXTREMO (escala de milimetros)')
# el defecto que rompio al verificador anterior: redondear el volumen a 9
# decimales antes de mirarle el signo. Una flecha de 0.688 m tiene piezas cuyo
# volumen cabe debajo de ese redondeo.
chica = pieza('Flecha_Punta', vol=-2.5e-10, area=1e-4, dmin=0.004)
r = arte.malla(dict(piezas=[chica], cruces=[]), apoya=False)
check('volumen negativo diminuto se detecta', 'Flecha_Punta' in r['normales_invertidas'],
      r['normales_invertidas'])
check('y el veredicto lo dice', 'normales invertidas' in r['veredicto'], r['veredicto'])

print('\n--- LEY 1: interpenetracion y manifold')
r = arte.malla(dict(piezas=[pieza('A'), pieza('B')], cruces=[('A','B')]))
check('cruce reportado', 'A x B' in r['pares_que_se_cruzan'])
r = arte.malla(dict(piezas=[pieza('A', nm=3)], cruces=[]))
check('no manifold reportado', r['no_manifold'] == 3)

print('\n--- LEY 2: relleno, y la trampa del bbox')
cubo  = arte.relleno(pieza('cubo', vol=1.0, area=6.0, dmin=1.0))
# caja hueca de 1 m con pared de 5 mm: V = 6*1*0.005, A = 12 (adentro y afuera)
hueca = arte.relleno(pieza('hueca', vol=0.03, area=12.0, dmin=1.0))
# LA TRAMPA DECLARADA: una pieza casi plana cuya dimension minima ES su espesor.
# El bbox miente y la clase dice "macizo". Por eso la regla dice leer el
# milimetro y no la clase -- y este test existe para que eso quede probado.
plana = arte.relleno(pieza('plana', vol=0.001, area=2.02, dmin=0.001))
check('cubo = macizo (razon 1/3)', cubo['clase']=='macizo' and abs(cubo['razon']-0.333)<0.01, cubo)
check('caja hueca de pared fina = cascara', hueca['clase']=='cascara', hueca)
check('5 mm de pared, medidos', abs(hueca['espesor_eq_mm']-5.0) < 0.1, hueca)
check('TRAMPA: pieza casi plana da macizo y el milimetro no miente',
      plana['clase']=='macizo' and plana['espesor_eq_mm']==1.0, plana)
check('el milimetro se reporta siempre', 'espesor_eq_mm' in cubo and 'espesor_eq_mm' in hueca)

print('\n--- LEY 3: la colocacion, que solo vale DESPUES de emparentar')
r = arte.malla(dict(piezas=[pieza('P', zmin=0.109)], cruces=[]))   # las agujas: 109 mm
check('109 mm hundidos se detectan', 'no apoya en z=0' in r['veredicto'], r['veredicto'])
r = arte.malla(dict(piezas=[pieza('P', esc=(1.05,1,1))], cruces=[]))
check('transform sin aplicar se detecta', 'transform sin aplicar' in r['veredicto'])
r = arte.malla(dict(piezas=[pieza('A',padre=False), pieza('B',padre=False)], cruces=[]))
check('varias piezas sin emparentar = no se midio', 'sin emparentar' in r['veredicto'], r['veredicto'])
r = arte.malla(dict(piezas=[pieza('Unica', padre=False)], cruces=[]))
check('UNA pieza suelta NO es un asset sin armar', 'sin emparentar' not in r['veredicto'], r['veredicto'])
r = arte.malla(dict(piezas=[pieza('Vuela', zmin=1.4)], cruces=[]), apoya=False)
check('lo que vuela no se le exige z=0', r['veredicto']=='EN LEY', r['veredicto'])

print('\n--- LEY 4: el numero que decide es el de PANTALLA')
r = arte.presupuesto(dict(piezas=[pieza('g', caras=817)]),
                     {"nombre":"enemigo","caras":900,"max_simultaneos":20,
                      "caras_en_pantalla":12000})
check('817 pasa como pieza', 'excede su familia' not in r['veredicto'])
check('16.340 en pantalla NO pasa', r['caras_en_pantalla']==16340 and 'en pantalla' in r['veredicto'], r)
r = arte.presupuesto(dict(piezas=[pieza('g', caras=817)]), {"nombre":"enemigo"})
check('sin presupuesto declarado = falla', 'sin presupuesto' in r['veredicto'], r['veredicto'])

print('\n--- LEY 5: el color medido en gris y en dicromacia')
rojo, verde = (0.8,0.1,0.1), (0.1,0.6,0.1)
check('rojo y verde se distinguen en color', arte.distancia_color(rojo,verde) >= 25,
      arte.distancia_color(rojo,verde))
d = arte.distancia_color(arte.dicromacia(rojo), arte.dicromacia(verde))
check('y COLAPSAN en deuteranopia (por eso la ley)', d < 25, 'dE=%s' % d)
mats = [dict(nombre='Rojo', rgb=rojo, usuarios=2), dict(nombre='Verde', rgb=verde, usuarios=2)]
r = arte.paleta(mats, {'single':'Rojo','splash':'Verde'})
check('paleta reporta el colapso', 'colapsan' in r['veredicto'], r['veredicto'])
mats2 = [dict(nombre='Claro', rgb=(0.95,0.9,0.8), usuarios=1),
         dict(nombre='Oscuro', rgb=(0.15,0.15,0.2), usuarios=1)]
r = arte.paleta(mats2, {'a':'Claro','b':'Oscuro'})
check('claro vs oscuro SI se distingue en las tres', r['veredicto']=='EN LEY', r['veredicto'])
r = arte.paleta([dict(nombre='A', rgb=(0.5,0.5,0.5), usuarios=1),
                 dict(nombre='B', rgb=(0.5,0.5,0.5), usuarios=1)])
check('dos materiales del mismo color = duplicado', 'duplicados' in r['veredicto'], r['veredicto'])
r = arte.paleta(mats2, {'a':'Claro'}, terreno=(0.93,0.9,0.82))
check('lo que se pierde contra el terreno se reporta', 'terreno' in r['veredicto'], r['veredicto'])

print('\n--- LEY 6: el .glb, leyendo el archivo ENTREGADO')
def glb(nodos, mallas, gen='Vaultrum'):
    j = json.dumps({"asset":{"version":"2.0","generator":gen},
                    "nodes":[{"name":n} for n in nodos],
                    "meshes":[{"name":m} for m in mallas],
                    "materials":[]}).encode()
    j += b' ' * ((4 - len(j) % 4) % 4)
    chunk = struct.pack('<II', len(j), 0x4E4F534A) + j
    return b'glTF' + struct.pack('<III', 2, 12 + len(chunk), 0)[:8] + struct.pack('<I', 12+len(chunk)) [:0] + chunk
def escribir(p, nodos, mallas):
    j = json.dumps({"asset":{"version":"2.0","generator":"Vaultrum"},
                    "nodes":[{"name":n} for n in nodos],
                    "meshes":[{"name":m} for m in mallas],"materials":[]}).encode()
    j += b' ' * ((4 - len(j) % 4) % 4)
    chunk = struct.pack('<II', len(j), 0x4E4F534A) + j
    with open(p,'wb') as f:
        f.write(b'glTF' + struct.pack('<II', 2, 12+len(chunk)) + chunk)
escribir(os.path.join(TMP, 'ok.glb'), ['Fig_Torso','Fig_Brazo'], ['Fig_Torso','Fig_Brazo'])
r = arte.entrega(os.path.join(TMP, 'ok.glb'), {"prefijo":"Fig_","sin":["Cube"],"max_mb":5})
check('glb sano pasa', r['veredicto']=='EN LEY', r['veredicto'])
escribir(os.path.join(TMP, 'sucio.glb'), ['Fig_Torso','Cube'], ['Fig_Torso','', 'Cube'])
r = arte.entrega(os.path.join(TMP, 'sucio.glb'), {"prefijo":"Fig_","sin":["Cube"]})
check('malla sin nombre se detecta', 'sin nombre' in r['veredicto'], r['veredicto'])
check('el Cube colado se detecta', 'basura colada' in r['veredicto'], r['veredicto'])
check('el prefijo del cliente manda', "prefijo" in r['veredicto'], r['veredicto'])
r = arte.entrega(os.path.join(TMP, 'no_existe.glb'))
check('archivo inexistente lo dice', 'no existe' in r['veredicto'], r['veredicto'])
with open(os.path.join(TMP, 'falso.glb'),'wb') as f: f.write(b'NOPE' + b'\0'*20)
r = arte.entrega(os.path.join(TMP, 'falso.glb'))
check('un archivo que no es glb lo dice', 'no es un .glb' in r['veredicto'], r['veredicto'])

print('\n%d ok, %d fallas' % (ok, fail))
sys.exit(1 if fail else 0)

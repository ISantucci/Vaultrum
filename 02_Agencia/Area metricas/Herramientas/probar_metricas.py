#!/usr/bin/env python3
"""Vaultrum - Area de Metricas - la prueba del instrumento.

metricas.py mide planes y datos. Este archivo lo mide a el: cada caso construye
un plan o un CSV a mano, con la respuesta correcta conocida, y comprueba que el
instrumento la de. Los casos de EXTREMO estan porque un instrumento que solo se
probo en el medio de su rango no esta probado (RA-008, Area de Arte).

    python3 probar_metricas.py        exit 0 si pasan todos
"""
import os, sys, tempfile, shutil, io, contextlib

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import metricas as M  # noqa: E402

PLAN_OK = """# MET-001.3 — Tutorial del constructor

## Insumo
`RQ-001.3` · `GDS-001.3`

## Fase y modelo
fase: Pre-Production
modelo: Premium

## Objetivo
Que un jugador nuevo entienda como construir una torre sin ayuda externa.

## Comportamiento esperado
Coloca su primera torre en un spot valido antes de que llegue la primera oleada.

## KPI primario
nombre: primera torre sin ayuda
formula: jugadores con tower_placed antes de wave_started(1) / jugadores con level_started
poblacion: testers de la build 0.3, primera sesion
ventana: primera sesion
fuente: level_started, tower_placed, wave_started
baseline: sin baseline — primera medicion del hilo
objetivo: 80% o mas (umbral de 13_Playtesting_y_validacion)

## Metricas diagnosticas
- tiempo hasta primera torre
- intentos de colocacion invalida

## Guardrails
- abandono en el primer minuto

## Tracking plan
| Evento | Disparo | Parametros | Pregunta | KPI |
|---|---|---|---|---|
| level_started | carga del nivel | level_id, build | cuantos empiezan? | primera torre sin ayuda |
| tower_placed | torre colocada | level_id, tower_type, seconds | coloca antes de la oleada? | primera torre sin ayuda |
| tower_place_failed | intento invalido | level_id, reason | donde se equivoca? | intentos de colocacion invalida |
| wave_started | arranca una oleada | level_id, wave | llego la oleada antes? | primera torre sin ayuda |
| session_quit | cierra el juego | seconds | abandona temprano? | abandono en el primer minuto |

## Estado
Cerrado
"""

LECTURA_OK = """# MET-001 — Lectura del playtest 0.3

## Insumo
`MET-001.3` · `TL-001` · `eventos_build03.csv`

## KPI primario
nombre: primera torre sin ayuda

## Calidad del dato
metricas.py datos: 0 duplicados, un solo entorno, version 0.3.

## Hechos
6 de 8 testers colocaron la primera torre antes de la oleada.

## Interpretaciones
El spot resaltado se entiende; el menu de torres no.

## Hipotesis
Los dos que fallaron no encontraron el menu de torres.

## Recomendacion
Probar el menu abierto por defecto en la proxima build.

## Proxima medicion
Mismo KPI, build 0.4.

## Estado
Cerrado
"""

casos, fallos = [], []


def caso(nombre):
    def deco(fn):
        casos.append((nombre, fn))
        return fn
    return deco


def leyes(txt):
    _, f, _ = M.medir_plan(txt)
    return [l for l, _ in f]


def detalle(txt):
    _, f, _ = M.medir_plan(txt)
    return ' | '.join(d for _, d in f)


# ------------------------------------------------------------------ plan
@caso('plan completo: en ley')
def _():
    assert leyes(PLAN_OK) == [], detalle(PLAN_OK)


@caso('Ley 1: sin objetivo')
def _():
    t = PLAN_OK.replace('Que un jugador nuevo entienda como construir una torre sin ayuda externa.', '')
    assert 'Ley 1' in leyes(t)


@caso('Ley 1: sin comportamiento esperado')
def _():
    t = PLAN_OK.replace('Coloca su primera torre en un spot valido antes de que llegue la primera oleada.', '')
    assert 'Ley 1' in leyes(t)


@caso('Ley 2: KPI sin poblacion (el denominador)')
def _():
    t = PLAN_OK.replace('poblacion: testers de la build 0.3, primera sesion\n', '')
    assert 'Ley 2' in leyes(t) and 'poblacion' in detalle(t)


@caso('Ley 2: sin baseline ni su declaracion')
def _():
    t = PLAN_OK.replace('baseline: sin baseline — primera medicion del hilo\n', '')
    assert 'baseline' in detalle(t)


@caso('Ley 2: dos KPI primarios')
def _():
    t = PLAN_OK.replace('nombre: primera torre sin ayuda\n', 'nombre: primera torre sin ayuda\nnombre: D1\n')
    assert 'KPI primarios' in detalle(t)


@caso('Ley 3: sin guardrails')
def _():
    t = PLAN_OK.replace('- abandono en el primer minuto\n', '')
    assert 'Ley 3' in leyes(t)


@caso('Ley 4: fecha dentro del nombre del evento')
def _():
    t = PLAN_OK.replace('| session_quit |', '| session_quit_2026_09_25 |')
    assert 'valor dinamico' in detalle(t)


@caso('Ley 4: nombre en CamelCase')
def _():
    t = PLAN_OK.replace('| session_quit |', '| SessionQuit |')
    assert 'snake_case' in detalle(t)


@caso('Ley 4: parametro con dato personal')
def _():
    t = PLAN_OK.replace('| seconds | abandona', '| seconds, email | abandona')
    assert 'dato personal' in detalle(t)


@caso('Ley 4: evento que no alimenta ninguna metrica declarada')
def _():
    t = PLAN_OK.replace('| abandono en el primer minuto |', '| fps promedio |')
    assert 'no es ni el KPI' in detalle(t)


@caso('Ley 4: evento sin pregunta')
def _():
    t = PLAN_OK.replace('| abandona temprano? |', '|  |')
    assert 'pregunta' in detalle(t)


@caso('Ley 4: 11 eventos en Pre-Production pasan el tope de la Biblioteca')
def _():
    extra = ''.join('| extra_%s | x | a | por que? | primera torre sin ayuda |\n' % c for c in 'abcdef')
    t = PLAN_OK.replace('\n## Estado', extra + '\n## Estado')
    assert 'tope de 13_Playtesting' in detalle(t)


@caso('Ley 4: el mismo exceso, con el tope declarado y su razon, pasa')
def _():
    extra = ''.join('| extra_%s | x | a | por que? | primera torre sin ayuda |\n' % c for c in 'abcdef')
    t = PLAN_OK.replace('\n## Estado', extra + '\n## Estado')
    t = t.replace('modelo: Premium', 'modelo: Premium\ntope: 12 — test de onboarding con 12 preguntas escritas')
    assert 'tope' not in detalle(t), detalle(t)


@caso('Ley 5: ARPPU y D30 en un prototipo = ignorar la fase')
def _():
    t = PLAN_OK.replace('- abandono en el primer minuto\n', '- abandono en el primer minuto\n- ARPPU\n- D30\n')
    d = detalle(t)
    assert 'ignorar la fase' in d and 'ARPPU' in d and 'D30' in d


@caso('Ley 5: el mismo ARPPU en Launch no es prematuro')
def _():
    t = PLAN_OK.replace('- abandono en el primer minuto\n', '- abandono en el primer minuto\n- ARPPU\n')
    t = t.replace('fase: Pre-Production', 'fase: Launch')
    assert 'ignorar la fase' not in detalle(t)


@caso('Ley 5: fase no declarada')
def _():
    t = PLAN_OK.replace('fase: Pre-Production\n', '')
    assert 'fase no declarada' in detalle(t)


@caso('Ley 5: fase en castellano y con aclaracion entre parentesis')
def _():
    t = PLAN_OK.replace('fase: Pre-Production', 'fase: Preproduccion (prototipo jugable)')
    fase, _, _ = M.medir_plan(t)
    assert fase == 'Pre-Production', fase


@caso('Estado: un plan que no declara su estado')
def _():
    t = PLAN_OK.replace('## Estado\nCerrado\n', '')
    assert 'Estado' in leyes(t)


# ------------------------------------------------------------------ lectura
def con_carpeta(archivos, fn):
    d = tempfile.mkdtemp()
    try:
        for nombre, txt in archivos.items():
            open(os.path.join(d, nombre), 'w', encoding='utf-8').write(txt)
        return fn(d)
    finally:
        shutil.rmtree(d)


@caso('Ley 6: lectura completa y con el mismo KPI que el plan: en ley')
def _():
    def f(d):
        r = os.path.join(d, 'MET-001_Lectura.md')
        return M.medir_lectura(r, LECTURA_OK)
    assert con_carpeta({'MET-001.3_Tutorial.md': PLAN_OK, 'MET-001_Lectura.md': LECTURA_OK}, f) == []


@caso('Ley 2: metric shopping — la lectura decide con otro KPI')
def _():
    otra = LECTURA_OK.replace('nombre: primera torre sin ayuda', 'nombre: tiempo hasta primera torre')
    def f(d):
        return M.medir_lectura(os.path.join(d, 'MET-001_Lectura.md'), otra)
    fallas = con_carpeta({'MET-001.3_Tutorial.md': PLAN_OK}, f)
    assert any('metric shopping' in x for _, x in fallas), fallas


@caso('Ley 6: hipotesis mezclada con los hechos (falta su seccion)')
def _():
    t = LECTURA_OK.replace('## Hipotesis\nLos dos que fallaron no encontraron el menu de torres.\n', '')
    def f(d):
        return M.medir_lectura(os.path.join(d, 'MET-001_Lectura.md'), t)
    fallas = con_carpeta({'MET-001.3_Tutorial.md': PLAN_OK}, f)
    assert any('hipotesis' in x for _, x in fallas), fallas


@caso('Ley 2: la lectura cita un plan que no esta en disco')
def _():
    def f(d):
        return M.medir_lectura(os.path.join(d, 'MET-001_Lectura.md'), LECTURA_OK)
    fallas = con_carpeta({}, f)
    assert any('no esta en la carpeta' in x for _, x in fallas), fallas


# ------------------------------------------------------------------ dato
def csv_(filas, cab='timestamp,player_id,session_id,version,environment,event'):
    d = tempfile.mkdtemp()
    r = os.path.join(d, 'e.csv')
    open(r, 'w', encoding='utf-8').write(cab + '\n' + '\n'.join(filas) + '\n')
    return d, r


def cargar(filas, cab=None, plan=None):
    d, r = csv_(filas, cab) if cab else csv_(filas)
    try:
        cols, crudas = M.cargar_eventos(r)
        return cols, M.calidad(cols, crudas, plan)
    finally:
        shutil.rmtree(d)


@caso('Dato: retencion D1 clasica contra rolling, con respuesta conocida')
def _():
    # cohorte 09-01: a, b, c. a vuelve el 02 (D1). b vuelve recien el 03 (rolling si, clasica no).
    # c no vuelve. Ultimo dia observado: 03, asi que D1 cerro y D7 no.
    filas = ['2026-09-01T10:00:00Z,a,s1,0.3,test,session_start',
             '2026-09-01T11:00:00Z,b,s2,0.3,test,session_start',
             '2026-09-01T12:00:00Z,c,s3,0.3,test,session_start',
             '2026-09-02T10:00:00Z,a,s4,0.3,test,session_start',
             '2026-09-03T10:00:00Z,b,s5,0.3,test,session_start']
    _, (validas, _) = cargar(filas)
    ret = M.retencion(validas, [1, 7])
    c = ret[0]
    assert c['n'] == 3
    clas, roll = c['D1']
    assert abs(clas - 100 / 3) < 1e-6 and abs(roll - 200 / 3) < 1e-6, c
    assert c['D7'] is None, 'una ventana que no cerro no es un cero'


@caso('Dato: los duplicados se detectan y no se cuentan')
def _():
    filas = ['2026-09-01T10:00:00Z,a,s1,0.3,test,tower_placed'] * 3
    _, (validas, h) = cargar(filas)
    assert len(validas) == 1 and any(t == 'duplicado' for t, _ in h), h


@caso('Dato: dos entornos mezclados = contaminacion')
def _():
    filas = ['2026-09-01T10:00:00Z,a,s1,0.3,test,x', '2026-09-01T10:00:01Z,b,s2,0.3,prod,x']
    _, (_, h) = cargar(filas)
    assert any(t == 'contaminacion' for t, _ in h), h


@caso('Dato: eventos fuera del plan y eventos del plan que nunca dispararon')
def _():
    filas = ['2026-09-01T10:00:00Z,a,s1,0.3,test,tower_placed',
             '2026-09-01T10:00:01Z,a,s1,0.3,test,debug_click']
    _, (_, h) = cargar(filas, plan=['tower_placed', 'wave_started'])
    tipos = [t for t, _ in h]
    assert 'fuera de plan' in tipos and 'faltante' in tipos, h


@caso('Dato: funnel paso a paso, respetando el orden temporal')
def _():
    filas = ['2026-09-01T10:00:00Z,a,s1,0.3,test,level_started',
             '2026-09-01T10:00:05Z,a,s1,0.3,test,tower_placed',
             '2026-09-01T10:00:00Z,b,s2,0.3,test,level_started',
             # c coloca una torre ANTES de empezar el nivel: no cuenta como conversion
             '2026-09-01T09:59:00Z,c,s3,0.3,test,tower_placed',
             '2026-09-01T10:00:00Z,c,s3,0.3,test,level_started']
    _, (validas, _) = cargar(filas)
    f = M.funnel(validas, ['level_started', 'tower_placed'])
    assert f[0][1] == 3 and f[1][1] == 1 and abs(f[1][2] - 100 / 3) < 1e-6, f


@caso('Dato: progresion con las dos tasas de fallo, que no son intercambiables')
def _():
    cab = 'timestamp,player_id,session_id,version,environment,event,level_id'
    filas = ['2026-09-01T10:00:0%dZ,a,s1,0.3,test,level_started,L1' % i for i in range(4)] + \
            ['2026-09-01T10:01:00Z,a,s1,0.3,test,level_completed,L1',
             '2026-09-01T10:02:00Z,a,s1,0.3,test,level_failed,L1']
    cols, (validas, _) = cargar(filas, cab)
    p = M.progresion(validas, cols)[0]
    assert p['starts'] == 4 and p['completion'] == 25.0
    assert p['fail_sobre_terminados'] == 50.0 and p['fail_sobre_starts'] == 25.0, p


@caso('Dato: un <x>_started que nunca termina no es progresion (no inventa 0% de completion)')
def _():
    filas = ['2026-09-01T10:00:00Z,a,s1,0.3,test,wave_started',
             '2026-09-01T10:00:01Z,a,s1,0.3,test,level_started',
             '2026-09-01T10:00:02Z,a,s1,0.3,test,level_completed']
    cols, (validas, _) = cargar(filas)
    bases = [p['sistema'] for p in M.progresion(validas, cols)]
    assert bases == ['level'], bases


@caso('Dato: economia +100/-90 contra +1000/-300 — el gasto sube y la acumulacion mas')
def _():
    cab = 'timestamp,player_id,session_id,version,environment,event,flow,currency,amount'
    filas = ['2026-09-01T10:00:00Z,a,s1,0.3,test,gold_earned,source,gold,1000',
             '2026-09-01T10:00:01Z,a,s1,0.3,test,gold_spent,sink,gold,300']
    _, (validas, h) = cargar(filas, cab)
    s, k, neto, ratio = M.economia(validas)['gold']
    assert (s, k, neto) == (1000, 300, 700) and abs(ratio - 1000 / 300) < 1e-9 and not h


@caso('Dato: un sink con amount negativo es un signo ambiguo')
def _():
    cab = 'timestamp,player_id,session_id,version,environment,event,flow,currency,amount'
    filas = ['2026-09-01T10:00:00Z,a,s1,0.3,test,gold_spent,sink,gold,-300']
    _, (_, h) = cargar(filas, cab)
    assert any(t == 'signo' for t, _ in h), h


@caso('Dato (extremo): timestamps epoch e ISO en el mismo archivo')
def _():
    filas = ['1788300000,a,s1,0.3,test,x', '2026-09-01T10:00:00+00:00,a,s1,0.3,test,y']
    _, (validas, h) = cargar(filas)
    assert len(validas) == 2 and not any(t == 'invalido' for t, _ in h), h


@caso('Dato (extremo): falta una columna obligatoria = bloqueante, no traceback')
def _():
    _, (validas, h) = cargar(['2026-09-01T10:00:00Z,a,x'], cab='timestamp,player_id,evento')
    assert validas == [] and any(t == 'bloqueante' for t, _ in h), h


@caso('Dato (extremo): un funnel sobre cero jugadores no divide por cero')
def _():
    f = M.funnel([], ['a', 'b'])
    assert f[0][1] == 0 and f[1][2] is None, f


@caso('Dato (extremo): el informe entero corre y --verificar devuelve 1 si hay duplicados')
def _():
    d, r = csv_(['2026-09-01T10:00:00Z,a,s1,0.3,test,x'] * 2)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            rc = M.main(['metricas.py', 'datos', r, '--verificar'])
        assert rc == 1
    finally:
        shutil.rmtree(d)


# ------------------------------------------------------------------ correr
if __name__ == '__main__':
    for nombre, fn in casos:
        try:
            fn()
            print('  [ok]    %s' % nombre)
        except AssertionError as e:
            fallos.append(nombre)
            print('  [FALLA] %s  %s' % (nombre, e))
        except Exception as e:  # un traceback tambien es una falla del instrumento
            fallos.append(nombre)
            print('  [ERROR] %s  %r' % (nombre, e))
    print('\n  %d casos, %d fallas' % (len(casos), len(fallos)))
    sys.exit(1 if fallos else 0)

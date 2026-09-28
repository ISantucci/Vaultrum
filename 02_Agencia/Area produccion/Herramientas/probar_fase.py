#!/usr/bin/env python3
"""Vaultrum - Area de Produccion - la prueba de fase.py.

fase.py lee proyectos y dice si hay que frenar y si una fase puede cerrarse. Este
archivo lo mide a el: cada caso arma un proyecto a mano, con la respuesta correcta
conocida, y comprueba que el instrumento la de. Los casos de EXTREMO estan porque
un instrumento que solo se probo en el medio de su rango no esta probado (RA-008).

Y dos casos de SINCRONIA, que son los que sostienen la regla de no decir dos veces
lo mismo: el flujo 05 y fase.py nombran las mismas nueve senales, y todo criterio
medido que el flujo pide es uno que el instrumento sabe medir.

    python3 probar_fase.py        exit 0 si pasan todos
"""
import os, re, sys, tempfile, shutil, io, contextlib

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import fase as F  # noqa: E402

CASOS = []


def caso(f):
    CASOS.append(f)
    return f


# ------------------------------------------------------------------ armado
def cuaderno(nombre, fase='Pre-Production', modelo='Premium', nombra=(), filas=()):
    L = ['# %s -- cuaderno de proyecto' % nombre, '', '## 3. Estado', '']
    if fase is not None:
        L.append('fase del producto: %s' % fase)
    if modelo is not None:
        L.append('modelo de negocio: %s' % modelo)
    L += ['', 'Cadena: ' + ' '.join(nombra), '', '## 5. Decisiones', '',
          '| ID | Fecha | Tema | Estado | Decision | Reemplaza a |',
          '|----|-------|------|--------|----------|-------------|']
    L += list(filas)
    return '\n'.join(L) + '\n'


def qa(num, defectos=(), arranque='ok', decision='CONDITIONAL GO'):
    humo = 'instalacion ok | arranque %s | pantalla principal ok' % arranque if arranque else 'documentacion ok'
    L = ['# QA-%s' % num, '', '```qa-alcance', 'tipo entrega', 'insumo TL-%s' % num, 'perfil estandar', '```',
         '```qa-humo', humo, 'resultado   aceptada        (aceptada | condicional | rechazada)', '```']
    if defectos:
        L += ['```qa-defectos'] + ['%s | %s | %s | nota' % d for d in defectos] + ['```']
    L += ['```qa-decision', decision, '```']
    return '\n'.join(L) + '\n'


class Proy:
    def __init__(self, nombre='Juego', **kw):
        self.base = tempfile.mkdtemp(prefix='fase_')
        self.dir = os.path.join(self.base, nombre)
        os.makedirs(self.dir)
        self.nombre = nombre
        self.kw = kw
        self.files = {}

    def art(self, rel, texto='# x\n'):
        self.files[rel] = texto
        return self

    def construir(self, texto_cuaderno=None):
        for rel, t in self.files.items():
            ruta = os.path.join(self.dir, rel)
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            open(ruta, 'w', encoding='utf-8').write(t)
        c = texto_cuaderno if texto_cuaderno is not None else cuaderno(self.nombre, **self.kw)
        open(os.path.join(self.dir, self.nombre + '.md'), 'w', encoding='utf-8').write(c)
        return F.Proyecto(self.dir)

    def fin(self):
        shutil.rmtree(self.base, ignore_errors=True)


def codigos(sen, nivel=None):
    return sorted({s[0] for s in sen if nivel is None or s[1] == nivel})


def correr(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = F.main(['fase.py'] + argv)
    return rc, buf.getvalue()


def entrega(p, n, defectos=(), arranque='ok', ve=True):
    """Un TL con su QA de entrega y, si ve, su VE."""
    p.art('01_Produccion/TL-%s_T.md' % n)
    p.art('06_Calidad/QA-%s_Gate.md' % n, qa(n, defectos, arranque))
    if ve:
        p.art('01_Produccion/VE-%s_J.md' % n)
    return p


def revisada(*ves):
    return ['| PRJ-%03d | 2026-09-28 | fase: revision tras %s | Confirmado | SEGUIR | -- |' % (i + 1, v)
            for i, v in enumerate(ves)]


# ------------------------------------------------------------------ fase declarada
@caso
def fase_en_la_linea_del_estado():
    assert F.fase_de('fase del producto: Pre-Production') == 'Pre-Production'


@caso
def la_plantilla_no_cuenta_como_fase():
    assert F.fase_de('fase del producto: <Planning · Pre-Production · Production>') is None


@caso
def alias_con_acento():
    assert F.fase_de('Fase: **Preproducción**') == 'Pre-Production'


@caso
def production_no_se_confunde_con_pre_production():
    assert F.fase_de('fase del producto: Production') == 'Production'
    assert F.fase_de('fase del producto: Post-Launch') == 'Post-Launch'
    assert F.fase_de('fase: launch') == 'Launch'


@caso
def fase_en_tabla():
    assert F.fase_de('| fase del producto | Testing |') == 'Testing'


@caso
def una_fila_de_revision_no_es_la_fase():
    assert F.fase_de('| PRJ-001 | 2026-09-28 | fase: revision tras VE-001 | Confirmado | SEGUIR en Testing |') is None


@caso
def una_palabra_que_empieza_como_fase_no_es_fase():
    assert F.fase_de('fase: testingrig para el editor') is None


@caso
def modelo_declarado():
    assert F.modelo_de('modelo de negocio: Premium') == 'premium'
    assert F.modelo_de('modelo de negocio: <premium · free-to-play>') is None


# ------------------------------------------------------------------ S1 S2 S3
@caso
def s1_sin_fase():
    p = Proy(fase=None, nombra=('TL-001', 'VE-001'), filas=revisada('VE-001'))
    entrega(p, '001')
    try:
        assert 'S1' in codigos(F.senales(p.construir()), 'parada')
    finally:
        p.fin()


@caso
def proyecto_sano_no_tiene_senales():
    p = Proy(nombra=('TL-001', 'VE-001'), filas=revisada('VE-001'))
    entrega(p, '001')
    try:
        assert F.senales(p.construir()) == []
    finally:
        p.fin()


@caso
def s2_cuaderno_que_no_nombra_el_ultimo_timeline():
    p = Proy(nombra=('TL-001', 'VE-001'), filas=revisada('VE-001'))
    entrega(p, '001')
    entrega(p, '002')
    try:
        det = [s[2] for s in F.senales(p.construir()) if s[0] == 'S2']
        assert any('TL-002' in d for d in det) and any('VE-002' in d for d in det), det
    finally:
        p.fin()


@caso
def s3_entrega_sin_ve_debajo_de_otra():
    p = Proy(nombra=('TL-001', 'TL-002'))
    p.art('01_Produccion/TL-001_T.md').art('01_Produccion/TL-002_T.md')
    try:
        det = [s[2] for s in F.senales(p.construir()) if s[0] == 'S3']
        assert det and 'TL-001' in det[0], det
    finally:
        p.fin()


@caso
def s3_no_salta_si_el_timeline_esta_superado():
    p = Proy(nombra=('TL-001', 'TL-002'))
    p.art('01_Produccion/TL-001_T.md', '# TL-001\n\nSuperado por `TL-002`\n').art('01_Produccion/TL-002_T.md')
    try:
        assert 'S3' not in codigos(F.senales(p.construir()))
    finally:
        p.fin()


@caso
def s3_el_ultimo_timeline_abierto_es_trabajo_en_curso():
    p = Proy(nombra=('TL-001', 'TL-002', 'VE-001'), filas=revisada('VE-001'))
    entrega(p, '001')
    p.art('01_Produccion/TL-002_T.md')
    try:
        assert F.senales(p.construir()) == []
    finally:
        p.fin()


# ------------------------------------------------------------------ S4 S5 S6
@caso
def s4_mayor_abierto_dos_entregas():
    p = Proy(nombra=('TL-002', 'VE-002'), filas=revisada('VE-002'))
    entrega(p, '001', [('BUG-001', 'mayor', 'diferido')])
    entrega(p, '002', [('BUG-001', 'mayor', 'diferido')])
    try:
        det = [s[2] for s in F.senales(p.construir()) if s[0] == 'S4']
        assert det and '2 entregas' in det[0], det
    finally:
        p.fin()


@caso
def s4_cuenta_la_racha_entera():
    p = Proy(nombra=('TL-003', 'VE-003'), filas=revisada('VE-003'))
    for n in ('001', '002', '003'):
        entrega(p, n, [('BUG-001', 'critico', 'abierto')])
    try:
        det = [s[2] for s in F.senales(p.construir()) if s[0] == 'S4']
        assert det and '3 entregas' in det[0], det
    finally:
        p.fin()


@caso
def s4_no_salta_por_un_menor():
    p = Proy(nombra=('TL-002', 'VE-002'), filas=revisada('VE-002'))
    entrega(p, '001', [('BUG-001', 'menor', 'abierto')])
    entrega(p, '002', [('BUG-001', 'menor', 'abierto')])
    try:
        assert 'S4' not in codigos(F.senales(p.construir()))
    finally:
        p.fin()


@caso
def s5_mayor_que_desaparece_es_parada_y_menor_es_aviso():
    p = Proy(nombra=('TL-002', 'VE-002'), filas=revisada('VE-002'))
    entrega(p, '001', [('BUG-001', 'mayor', 'diferido'), ('BUG-002', 'menor', 'abierto')])
    entrega(p, '002', [('BUG-003', 'menor', 'cerrado')])
    try:
        sen = F.senales(p.construir())
        s5 = {s[2].split()[0]: s[1] for s in sen if s[0] == 'S5'}
        assert s5 == {'BUG-001': 'parada', 'BUG-002': 'aviso'}, s5
    finally:
        p.fin()


@caso
def s5_no_salta_si_reaparece_mas_tarde():
    p = Proy(nombra=('TL-003', 'VE-003'), filas=revisada('VE-003'))
    entrega(p, '001', [('BUG-001', 'mayor', 'diferido')])
    entrega(p, '002', [])
    entrega(p, '003', [('BUG-001', 'mayor', 'cerrado')])
    try:
        assert 'S5' not in codigos(F.senales(p.construir()))
    finally:
        p.fin()


@caso
def s5_un_cerrado_puede_no_volver_a_aparecer():
    p = Proy(nombra=('TL-002', 'VE-002'), filas=revisada('VE-002'))
    entrega(p, '001', [('BUG-001', 'mayor', 'cerrado')])
    entrega(p, '002', [])
    try:
        assert 'S5' not in codigos(F.senales(p.construir()))
    finally:
        p.fin()


@caso
def s6_dos_entregas_sin_arrancar_es_parada():
    p = Proy(nombra=('TL-002', 'VE-002'), filas=revisada('VE-002'))
    entrega(p, '001', arranque='no-verificado')
    entrega(p, '002', arranque=None)          # un gate de documentos, sin campo arranque
    try:
        sen = F.senales(p.construir())
        assert [s[1] for s in sen if s[0] == 'S6'] == ['parada'], sen
    finally:
        p.fin()


@caso
def s6_una_sola_entrega_sin_arrancar_es_aviso():
    p = Proy(nombra=('TL-001', 'VE-001'), filas=revisada('VE-001'))
    entrega(p, '001', arranque='no-verificado')
    try:
        assert [s[1] for s in F.senales(p.construir()) if s[0] == 'S6'] == ['aviso']
    finally:
        p.fin()


@caso
def s6_si_la_ultima_arranco_no_hay_senal():
    p = Proy(nombra=('TL-002', 'VE-002'), filas=revisada('VE-002'))
    entrega(p, '001', arranque='no-verificado')
    entrega(p, '002', arranque='ok')
    try:
        assert 'S6' not in codigos(F.senales(p.construir()))
    finally:
        p.fin()


@caso
def s6_no_corre_en_planning():
    p = Proy(fase='Planning', nombra=('TL-002', 'VE-002'), filas=revisada('VE-002'))
    entrega(p, '001', arranque=None)
    entrega(p, '002', arranque=None)
    try:
        assert 'S6' not in codigos(F.senales(p.construir()))
    finally:
        p.fin()


# ------------------------------------------------------------------ S7 S8 S9
@caso
def s7_testing_sin_lectura():
    p = Proy(fase='Testing', nombra=('TL-001', 'VE-001'), filas=revisada('VE-001'))
    entrega(p, '001')
    p.art('08_Metricas/MET-001.1_Plan.md')    # un plan no es una lectura
    try:
        assert 'S7' in codigos(F.senales(p.construir()), 'parada')
    finally:
        p.fin()


@caso
def s7_se_levanta_con_la_lectura():
    p = Proy(fase='Testing', nombra=('TL-001', 'VE-001'), filas=revisada('VE-001'))
    entrega(p, '001')
    p.art('08_Metricas/MET-001_Lectura.md')
    try:
        assert 'S7' not in codigos(F.senales(p.construir()))
    finally:
        p.fin()


@caso
def s8_codigo_sin_diseno():
    p = Proy(nombra=('TL-001',))
    p.art('01_Produccion/TL-001_T.md').art('01_Produccion/RQ-001.1_Torres.md', '# RQ\nArea: Game Design\n')
    p.art('01_Produccion/RQ-001.2_Menu.md', '# RQ\nNo pasa por Game Design: no es jugable y esta declarado.\n')
    p.art('05_Programacion/SOL-001_Arq.md')
    try:
        det = [s[2] for s in F.senales(p.construir()) if s[0] == 'S8']
        assert len(det) == 1 and 'RQ-001.1' in det[0], det
    finally:
        p.fin()


@caso
def s8_no_salta_con_gds_ni_en_timeline_cerrado():
    p = Proy(nombra=('TL-001', 'VE-001', 'TL-002'), filas=revisada('VE-001'))
    entrega(p, '001')
    p.art('01_Produccion/Archivo/RQ-001.1_X.md').art('05_Programacion/SOL-001_A.md')   # cerrado: historia
    p.art('01_Produccion/TL-002_T.md').art('01_Produccion/RQ-002.1_Y.md')
    p.art('02_GameDesign/GDS-002.1_Y.md').art('05_Programacion/EJ-002.1_Y.md')
    try:
        assert 'S8' not in codigos(F.senales(p.construir()))
    finally:
        p.fin()


@caso
def s9_entrega_cerrada_sin_revision():
    p = Proy(nombra=('TL-001', 'VE-001'))
    entrega(p, '001')
    try:
        assert codigos(F.senales(p.construir())) == ['S9']
    finally:
        p.fin()


@caso
def s9_una_revision_de_otra_entrega_no_alcanza():
    p = Proy(nombra=('TL-002', 'VE-002'), filas=revisada('VE-001'))
    entrega(p, '001')
    entrega(p, '002')
    try:
        assert codigos(F.senales(p.construir())) == ['S9']
    finally:
        p.fin()


# ------------------------------------------------------------------ aceptacion y verificar
@caso
def el_owner_acepta_una_parada_para_esta_entrega():
    filas = revisada('VE-002') + ['| PRJ-009 | 2026-09-28 | parada S6 tras VE-002 | Confirmado | se juega manana | -- |']
    p = Proy(nombra=('TL-002', 'VE-002'), filas=filas)
    entrega(p, '001', arranque=None)
    entrega(p, '002', arranque=None)
    try:
        sen = F.senales(p.construir())
        s6 = [s for s in sen if s[0] == 'S6']
        assert s6 and s6[0][1] == 'aceptada' and 'PRJ-009' in s6[0][3], s6
        rc, _ = correr([p.dir, '--verificar'])
        assert rc == 0
    finally:
        p.fin()


@caso
def una_aceptacion_vieja_no_vale_para_la_entrega_nueva():
    filas = revisada('VE-002') + ['| PRJ-009 | 2026-09-20 | parada S6 tras VE-001 | Confirmado | ... | -- |']
    p = Proy(nombra=('TL-002', 'VE-002'), filas=filas)
    entrega(p, '001', arranque=None)
    entrega(p, '002', arranque=None)
    try:
        assert [s[1] for s in F.senales(p.construir()) if s[0] == 'S6'] == ['parada']
    finally:
        p.fin()


@caso
def una_aceptacion_pendiente_no_acepta():
    filas = revisada('VE-002') + ['| PRJ-009 | 2026-09-28 | parada S6 tras VE-002 | Pendiente | ... | -- |']
    p = Proy(nombra=('TL-002', 'VE-002'), filas=filas)
    entrega(p, '001', arranque=None)
    entrega(p, '002', arranque=None)
    try:
        p.construir()
        rc, out = correr([p.dir, '--verificar'])
        assert rc == 1 and 'S6' in out, out
    finally:
        p.fin()


@caso
def verificar_sin_paradas_da_cero():
    p = Proy(nombra=('TL-001', 'VE-001'), filas=revisada('VE-001'))
    entrega(p, '001')
    try:
        p.construir()
        rc, out = correr([p.dir, '--verificar'])
        assert rc == 0 and 'SIN PARADAS' in out, out
    finally:
        p.fin()


@caso
def una_carpeta_sin_cuaderno_no_es_proyecto():
    base = tempfile.mkdtemp(prefix='fase_')
    try:
        rc, out = correr([base])
        assert rc == 2 and 'no tiene cuaderno' in out
    finally:
        shutil.rmtree(base, ignore_errors=True)


@caso
def todos_un_renglon_por_proyecto():
    a = Proy('Alfa', nombra=('TL-001', 'VE-001'), filas=revisada('VE-001'))
    entrega(a, '001')
    a.construir()
    b_dir = os.path.join(a.base, 'Beta')
    os.makedirs(b_dir)
    open(os.path.join(b_dir, 'Beta.md'), 'w', encoding='utf-8').write(cuaderno('Beta', fase=None))
    os.makedirs(os.path.join(a.base, 'Suelto'))
    try:
        rc, out = correr([a.base, '--todos', '--verificar'])
        L = out.strip().split('\n')
        assert len(L) == 3, out
        assert 'S1' in L[1] and 'sin cuaderno' in L[2] and rc == 1, out
    finally:
        a.fin()


# ------------------------------------------------------------------ salida de fase
@caso
def salida_con_un_medido_en_falta_no_deja_avanzar():
    p = Proy(nombra=('TL-001', 'VE-001'), filas=revisada('VE-001'))
    entrega(p, '001', [('BUG-001', 'mayor', 'abierto')], arranque='ok')
    try:
        pr = p.construir()
        L, rc = F.salida(pr, F.senales(pr))
        txt = '\n'.join(L)
        assert rc == 0 and 'NO SE PUEDE AVANZAR' in txt and 'deuda' in txt and 'met' in txt, txt
    finally:
        p.fin()


@caso
def salida_con_los_medidos_en_verde_deja_la_decision_a_los_juicios():
    p = Proy(nombra=('TL-001', 'VE-001'), filas=revisada('VE-001'))
    entrega(p, '001', [('BUG-001', 'menor', 'abierto')], arranque='ok')
    p.art('08_Metricas/MET-001_Lectura.md')
    try:
        pr = p.construir()
        L, rc = F.salida(pr, F.senales(pr))
        txt = '\n'.join(L)
        assert 'los medidos estan en verde' in txt and '[juicio]' in txt, txt
        assert 'si avanza:      Production' in txt, txt
    finally:
        p.fin()


@caso
def salida_ignora_la_s9_porque_la_revision_es_lo_que_la_levanta():
    p = Proy(nombra=('TL-001', 'VE-001'))
    entrega(p, '001', arranque='ok')
    p.art('08_Metricas/MET-001_Lectura.md')
    try:
        pr = p.construir()
        ok, ev = F.chequeos(pr, F.senales(pr))['senales']
        assert ok, ev
    finally:
        p.fin()


@caso
def salida_con_una_clave_que_el_instrumento_no_tiene_es_error():
    base = tempfile.mkdtemp(prefix='fase_')
    flujo = os.path.join(base, 'flujo.md')
    open(flujo, 'w', encoding='utf-8').write('```txt\nPRE-PRODUCTION    x\n  medido inventada   algo\n```\n')
    p = Proy(nombra=('TL-001', 'VE-001'), filas=revisada('VE-001'))
    entrega(p, '001')
    try:
        pr = p.construir()
        L, rc = F.salida(pr, F.senales(pr), ruta=flujo)
        assert rc == 2 and any('ERROR' in x for x in L), L
    finally:
        p.fin()
        shutil.rmtree(base, ignore_errors=True)


@caso
def la_ultima_fase_no_tiene_siguiente():
    p = Proy(fase='Live Ops', nombra=('TL-001', 'VE-001'), filas=revisada('VE-001'))
    entrega(p, '001')
    p.art('08_Metricas/MET-001_Salud.md')
    try:
        pr = p.construir()
        L, rc = F.salida(pr, F.senales(pr))
        assert rc == 0 and not any(x.startswith('si avanza') for x in L), L
    finally:
        p.fin()


@caso
def los_numeros_se_ordenan_como_numeros():
    p = Proy(nombra=('TL-010', 'VE-010'), filas=revisada('VE-010'))
    entrega(p, '009')
    entrega(p, '010')
    try:
        pr = p.construir()
        assert pr.ultimo('VE')[1] == 'VE-010' and pr.qas_entrega()[-1][1] == 'QA-010'
    finally:
        p.fin()


# ------------------------------------------------------------------ sincronia
@caso
def el_flujo_y_el_instrumento_nombran_las_mismas_senales():
    txt = open(F.FLUJO, encoding='utf-8').read()
    en_flujo = set(re.findall(r'^(S\d)\s', txt, re.M))
    assert en_flujo == set(F.SENALES), (sorted(en_flujo), sorted(F.SENALES))


@caso
def todo_medido_del_flujo_lo_sabe_medir_el_instrumento():
    p = Proy(nombra=('TL-001', 'VE-001'), filas=revisada('VE-001'))
    entrega(p, '001')
    try:
        pr = p.construir()
        claves = set(F.chequeos(pr, F.senales(pr)))
        crit = F.criterios()
        assert set(crit) == set(F.FASES), sorted(crit)
        pedidas = {c for items in crit.values() for (t, c, _) in items if t == 'medido'}
        assert pedidas <= claves, pedidas - claves
        assert all(any(t == 'juicio' for (t, _, _) in crit[f]) for f in F.FASES)
    finally:
        p.fin()


# ------------------------------------------------------------------ correr
def main():
    fallas = 0
    for f in CASOS:
        try:
            f()
            print('  ok     %s' % f.__name__)
        except AssertionError as e:
            fallas += 1
            print('  FALLA  %s  %s' % (f.__name__, e))
        except Exception as e:  # noqa: BLE001
            fallas += 1
            print('  ERROR  %s  %r' % (f.__name__, e))
    print('\n%d casos, %d fallas' % (len(CASOS), fallas))
    return 1 if fallas else 0


if __name__ == '__main__':
    sys.exit(main())

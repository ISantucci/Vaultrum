#!/usr/bin/env python3
"""Vaultrum - Area de Produccion - el inventario de requerimientos (v1).

Cuenta los RQ del vault, les deriva estado y verifica que cada uno este en la
carpeta que le corresponde. Es el instrumento que le faltaba al area que es
DUEÑA DE LA ENTREGA: hasta hoy, saber si un requerimiento estaba hecho era
memoria del owner, y la memoria no es un instrumento.

  El estado de un RQ NO se declara en el RQ: se DERIVA de su cadena.
  Un RQ no sabe si esta hecho -- lo sabe su timeline, y el timeline lo sabe
  porque tiene (o no tiene) su VE en disco. Es la misma regla que la Ley 1b de
  documentacion.py: un timeline esta cerrado cuando tiene su VE.

  entregado   su TL tiene VE, y el VE no lo declara Pausado      -> Archivo/
  pausado     su TL tiene VE, y el VE lo nombra en una linea      -> vive
              que dice Pausado
  superado    su TL declara "Superado por TL-XXX"                 -> Archivo/
  en curso    su TL todavia no tiene VE                           -> vive

  Los dos que se archivan son los que ya no admiten trabajo. Los dos que
  quedan vivos son los dos que si: uno porque falta hacerlo, el otro porque
  falta poder hacerlo. Un Pausado archivado seria un pendiente escondido.

Los dos ambitos se miden con la misma regla y se archivan por separado:

  Modo Owner   02_Agencia/Area produccion/Salidas/Requerimientos/Archivo/
  proyecto     06_Proyectos/<Proyecto>/01_Produccion/Archivo/

  python3 requerimientos.py [ruta]               informe
  python3 requerimientos.py [ruta] --verificar   solo el veredicto (exit 1 si falla)
  python3 requerimientos.py [ruta] --archivar    mueve lo entregado y lo superado
  python3 requerimientos.py [ruta] --pendientes  solo lo que queda por hacer

Las excepciones se declaran en Herramientas/excepciones.txt: ruta | estado | razon.
Lo que no esta declarado ahi, falla.
"""
import os, re, shutil, sys, collections

RUIDO   = {'.git', '.obsidian', '__pycache__', '.claude', '.agents', '.vaultrum', 'node_modules'}
ARCHIVO = 'Archivo'
ART     = re.compile(r'^(TL|RQ|VE)-(\d+)(?:\.(\d+[a-z]?))?_')
SUPERADO = re.compile(r'Superad[oa] por\s+`?TL-(\d+)', re.I)
ESTADOS_ARCHIVABLES = ('entregado', 'superado')


# ------------------------------------------------------------------ lectura
def raiz_vault(ruta):
    p = os.path.abspath(ruta)
    if os.path.isfile(p):
        p = os.path.dirname(p)
    while True:
        if os.path.exists(os.path.join(p, '00_START_HERE.md')):
            return p
        padre = os.path.dirname(p)
        if padre == p:
            return os.path.abspath(ruta)
        p = padre


def ambito_de(rel):
    """Modo Owner, o el nombre del proyecto. Un RQ pertenece a uno solo."""
    partes = rel.split('/')
    if partes[0] == '06_Proyectos' and len(partes) > 1:
        return partes[1]
    return 'MODO OWNER'


def recolectar(raiz):
    """{ambito: {tipo: {tl: [(n, rel, texto)]}}}"""
    inv = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(list)))
    for dp, dn, fn in os.walk(raiz):
        dn[:] = [d for d in dn if d not in RUIDO]
        for f in sorted(fn):
            if not f.endswith('.md'):
                continue
            m = ART.match(f)
            if not m:
                continue
            ruta = os.path.join(dp, f)
            rel = os.path.relpath(ruta, raiz).replace('\\', '/')
            txt = open(ruta, encoding='utf-8', errors='replace').read()
            inv[ambito_de(rel)][m.group(1)][m.group(2)].append((m.group(3), rel, txt))
    return inv


def cargar_excepciones(raiz_tool):
    """{<ambito>/RQ-<tl>.<n>: (estado declarado, razon)}

    Se declaran por IDENTIDAD del requerimiento y NO por ruta, a proposito.
    Este instrumento MUEVE archivos, y una excepcion escrita contra una ruta se
    rompe en silencio en cuanto el archivo se mueve -- exactamente el fallo que
    ARQ-025 midio cuando los EJ de Modo Owner cambiaron de carpeta y sus
    excepciones dejaron de aplicar sin que nada avisara. Un RQ no cambia de
    identidad cuando se archiva; cambia de lugar.

    Una excepcion PISA el estado derivado. No silencia una falla: declara, con
    razon escrita, cual es el estado real cuando la cadena no alcanza a decirlo.
    """
    ruta = os.path.join(raiz_tool, 'excepciones.txt')
    exc = {}
    if not os.path.exists(ruta):
        return exc
    for l in open(ruta, encoding='utf-8', errors='replace'):
        l = l.split('#')[0].strip()
        if not l or '|' not in l:
            continue
        p = [x.strip() for x in l.split('|')]
        if len(p) >= 3:
            exc[p[0]] = (p[1], p[2])
    return exc


def identidad(fila):
    return '%s/RQ-%s.%s' % (fila['ambito'], fila['tl'], fila['n'])


# ------------------------------------------------------------------ medicion
def _limpiar(celda):
    return re.sub(r'[*_`\s]+', '', celda).lower()


def pausados_en(ve_textos, tl):
    """(declarados, ambiguos): los RQ que un VE deja Pausado.

    DECLARADO es de forma y por eso se puede contar: una fila de la tabla
    "Contra los RQ" del VE, donde una celda EMPIEZA con "Pausado". Esa tabla ya
    es la forma que el VE tiene, asi que la regla no pide nada nuevo.

    AMBIGUO es todo lo demas: el VE nombra al RQ en una linea que dice Pausado
    pero no en esa forma. El instrumento NO decide -- lo reporta y el RQ se
    queda vivo. Es a proposito: la primera version de esto leia cualquier
    mencion y clasifico como Pausado un RQ-009.4 que el VE narraba asi:

        RQ-009.4 -> EJ-009.4   (estuvo Pausado; reabierto con opcion C)

    Esa linea cuenta una historia, no declara un estado. Un instrumento que
    confunde las dos cosas archiva mal en la direccion peor: deja afuera del
    Archivo algo terminado, o peor, esconde un pendiente. Ante la duda no
    adivina; pide que el VE lo declare, o que se declare la excepcion.
    """
    dec, amb = set(), set()
    for txt in ve_textos:
        for linea in txt.splitlines():
            if 'pausado' not in linea.lower():
                continue
            ns = {m.group(1) for m in re.finditer(r'RQ-' + tl + r'\.(\d+[a-z]?)', linea)}
            if not ns:
                continue
            celdas = linea.split('|')
            canonico = len(celdas) > 2 and any(_limpiar(c).startswith('pausado') for c in celdas)
            (dec if canonico else amb).update(ns)
    return dec, (amb - dec)


def medir(raiz, exc=None):
    exc = exc or {}
    inv = recolectar(raiz)
    filas = []
    for amb in sorted(inv, key=lambda x: (x != 'MODO OWNER', x)):
        c = inv[amb]
        for tl in sorted(c['RQ']):
            ves = [t for _, _, t in c['VE'].get(tl, [])]
            tls = [t for _, _, t in c['TL'].get(tl, [])]
            sup = next((SUPERADO.search(t).group(1) for t in tls if SUPERADO.search(t)), None)
            paus, ambig = pausados_en(ves, tl) if ves else (set(), set())
            for n, rel, _ in sorted(c['RQ'][tl], key=lambda x: (len(x[0] or ''), x[0] or '')):
                if sup:
                    est, nota = 'superado', 'TL-%s lo reemplaza' % sup
                elif not ves:
                    est, nota = 'en curso', 'TL-%s todavia no tiene VE' % tl
                elif n in paus:
                    est, nota = 'pausado', 'el VE-%s lo declara Pausado' % tl
                elif n in ambig:
                    est, nota = 'ambiguo', 'el VE-%s dice Pausado sin declararlo en su tabla' % tl
                else:
                    est, nota = 'entregado', 'VE-%s en disco' % tl
                fila = dict(ambito=amb, tl=tl, n=n, rel=rel, estado=est, nota=nota,
                            declarado=None, archivado=('/%s/' % ARCHIVO) in rel)
                d = exc.get(identidad(fila))
                if d:
                    fila['declarado'] = d[1]
                    fila['nota'] = 'declarado %s (medido %s): %s' % (d[0], est, d[1])
                    fila['estado'] = d[0]
                filas.append(fila)
    return filas


def destino(raiz, fila):
    """Donde tiene que vivir este RQ. Devuelve None si ya esta bien."""
    debe = fila['estado'] in ESTADOS_ARCHIVABLES
    if debe == fila['archivado']:
        return None
    partes = fila['rel'].split('/')
    if debe:
        nueva = '/'.join(partes[:-1] + [ARCHIVO, partes[-1]])
    else:
        nueva = '/'.join([p for p in partes[:-1] if p != ARCHIVO] + [partes[-1]])
    return nueva


# ------------------------------------------------------------------ informe
def informe(raiz, filas, exc, solo_pendientes=False):
    cuenta = collections.Counter(f['estado'] for f in filas)
    print()
    print('  INVENTARIO DE REQUERIMIENTOS')
    print('  ' + '=' * 60)
    print('  %d RQ en %d ambitos' % (len(filas), len({f['ambito'] for f in filas})))
    print()

    if not solo_pendientes:
        print('  %-14s %5s %5s %5s %5s %5s %5s' % ('AMBITO', 'total', 'entr', 'curso', 'paus', 'super', 'ambig'))
        print('  ' + '-' * 52)
        for amb in sorted({f['ambito'] for f in filas}, key=lambda x: (x != 'MODO OWNER', x)):
            g = [f for f in filas if f['ambito'] == amb]
            c = collections.Counter(f['estado'] for f in g)
            print('  %-14s %5d %5d %5d %5d %5d %5d' % (amb[:14], len(g), c['entregado'],
                                                         c['en curso'], c['pausado'], c['superado'], c['ambiguo']))
        print('  ' + '-' * 52)
        print('  %-14s %5d %5d %5d %5d %5d %5d' % ('TOTAL', len(filas), cuenta['entregado'],
                                                   cuenta['en curso'], cuenta['pausado'], cuenta['superado'],
                                                   cuenta['ambiguo']))
        print()

    vivos = [f for f in filas if f['estado'] in ('en curso', 'pausado', 'ambiguo')]
    print('  LO QUE QUEDA POR HACER (%d)' % len(vivos))
    print('  ' + '-' * 60)
    amb_ant = None
    for f in sorted(vivos, key=lambda f: (f['ambito'] != 'MODO OWNER', f['ambito'], f['tl'], len(f['n'] or ''), f['n'] or '')):
        if f['ambito'] != amb_ant:
            print('  %s' % f['ambito'])
            amb_ant = f['ambito']
        print('      %-9s RQ-%s.%-4s %-8s %s' % ('', f['tl'], f['n'], f['estado'], f['nota']))
    if not vivos:
        print('      nada: todo lo escrito esta entregado o superado')
    print()
    if solo_pendientes:
        return

    mal = [(f, destino(raiz, f)) for f in filas]
    mal = [(f, d) for f, d in mal if d]
    ok_exc = [f for f in filas if f['declarado']]
    if mal:
        print('  FUERA DE SU CARPETA (%d)' % len(mal))
        print('  ' + '-' * 60)
        for f, d in mal[:40]:
            print('      %-9s %s' % (f['estado'], f['rel']))
            print('      %-9s -> %s' % ('', d))
        if len(mal) > 40:
            print('      ... y %d mas' % (len(mal) - 40))
        print()
    if ok_exc:
        print('  Excepciones declaradas (%d) - estan en excepciones.txt, no fallan' % len(ok_exc))
        for f in ok_exc:
            print('      %-9s %-22s %s' % (f['estado'], identidad(f), f['declarado']))
        print()

    print('  Fuera del alcance de la herramienta (sigue siendo juicio):')
    print('      si el RQ estaba bien escrito  ·  si lo entregado era lo pedido')
    print('      eso lo dice el VE, y el VE lo firma una persona')
    print()
    return mal


def archivar(raiz, filas, exc):
    movidos = []
    for f in filas:
        d = destino(raiz, f)
        if not d:
            continue
        origen = os.path.join(raiz, f['rel'])
        final = os.path.join(raiz, d)
        os.makedirs(os.path.dirname(final), exist_ok=True)
        if os.path.exists(final):
            print('  NO se movio (ya existe destino): %s' % d)
            continue
        shutil.move(origen, final)
        movidos.append((f['rel'], d))
    return movidos


def main():
    args = sys.argv[1:]
    verificar   = '--verificar' in args
    hacer       = '--archivar' in args
    pendientes  = '--pendientes' in args
    destino_arg = next((a for a in args if not a.startswith('--')), '.')
    raiz = raiz_vault(destino_arg)
    exc = cargar_excepciones(os.path.dirname(os.path.abspath(__file__)))

    filas = medir(raiz, exc)

    if hacer:
        movidos = archivar(raiz, filas, exc)
        print()
        print('  ARCHIVADOS: %d' % len(movidos))
        for a, b in movidos:
            print('      %s' % b)
        print()
        filas = medir(raiz, exc)

    mal = [f for f in filas if destino(raiz, f)]

    if not verificar:
        informe(raiz, filas, exc, solo_pendientes=pendientes)

    if mal:
        print('INVENTARIO FUERA DE LEY: %d RQ fuera de su carpeta. '
              'Se ordena con --archivar.' % len(mal))
        return 1
    c = collections.Counter(f['estado'] for f in filas)
    print('INVENTARIO EN LEY: %d entregado(s) y %d superado(s) en su Archivo, '
          '%d en curso y %d pausado(s) a la vista.'
          % (c['entregado'], c['superado'], c['en curso'], c['pausado']))
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""Vaultrum - instrumento del Despacho de ejecucion (capa IA Operativa).

Cuenta lo que se delego de verdad. Lee el log de la bandeja -- una linea por
orden ejecutada -- y responde cuatro preguntas que hasta hoy se contestaban de
memoria: cuantas ejecuciones se delegaron, a que ejecutor, cuanto tardaron y
cuantas volvieron en fallo.

    python3 despacho.py resumen                    el total, por ejecutor y por estado
    python3 despacho.py resumen --desde 2026-09-01  solo desde una fecha
    python3 despacho.py ordenes --ultimas 20        una linea por orden, la ultima arriba

POR QUE EXISTE
`07_Despacho de ejecucion` cierra declarando su propia deuda, textual: "no mide
lo que cuesta una ejecucion delegada, ni cuantas veces se delego, ni si el
ahorro fue real. Hoy el despacho es criterio escrito y no medicion."

Es la misma deuda que esta capa ya tuvo una vez con los tokens, y se cierra por
la misma puerta: un contador. AiCare mide el costo de ENTRADA con
contar_contexto.py; esto mide el de EJECUCION. Son dos presupuestos distintos y
ninguno de los dos se estima.

QUE MIDE Y QUE NO -- el margen de error, declarado
  MIDE      cuantas ordenes corrieron, a que ejecutor fueron, cuanto tardo cada
            una en segundos de reloj, y como termino (OK o el exit code del que
            fallo). Todo sale del log que escribe observer.ps1 al cerrar cada
            orden: es un hecho, no una estimacion.
  NO MIDE   tokens, plata, ni si el ahorro fue real. Para eso haria falta que el
            ejecutor devuelva su consumo, y hoy no lo devuelve. Una ejecucion
            corta puede haber sido cara y una larga barata.
  NO VE     lo que se ruteo sin pasar por la bandeja. Un /codex:rescue disparado
            a mano dentro de una sesion no deja linea en el log y este contador
            no lo cuenta. Si el numero parece bajo, esa es la primera sospecha.

El log es runtime y no se versiona: en un clone recien bajado este script no
tiene nada que contar, y lo dice en vez de fallar.
"""
import os, re, sys
from collections import Counter, defaultdict

BANDEJA = os.path.join('04_IA Operativa', 'Herramientas', 'bandeja')

# observer.ps1 escribe:  <fecha>  <orden>  [<ejecutor>]  <seg>s  <estado>
# El ejecutor es opcional a proposito: las lineas escritas antes de que el
# observer lo registrara siguen siendo validas y se cuentan como 'desconocido'.
# Un instrumento que descarta su propio historial mide menos de lo que hay.
LINEA = re.compile(
    r'^(?P<fecha>\d{4}-\d{2}-\d{2})\s+(?P<hora>\d{2}:\d{2}:\d{2})\s+'
    r'(?P<orden>\S+)\s+'
    r'(?:(?P<ejecutor>[A-Za-z][\w.-]*)\s+)?'
    r'(?P<seg>\d+)s\s*'
    r'(?P<estado>.*)$'
)


def leer(raiz, desde=None):
    log = os.path.join(raiz, BANDEJA, 'log.txt')
    if not os.path.isfile(log):
        return None, log
    filas, rotas = [], 0
    with open(log, encoding='utf-8', errors='replace') as f:
        for cruda in f:
            cruda = cruda.strip()
            if not cruda:
                continue
            m = LINEA.match(cruda)
            if not m:
                rotas += 1
                continue
            d = m.groupdict()
            if desde and d['fecha'] < desde:
                continue
            d['ejecutor'] = d['ejecutor'] or 'desconocido'
            d['seg'] = int(d['seg'])
            d['estado'] = (d['estado'] or 'OK').strip() or 'OK'
            d['ok'] = d['estado'].upper().startswith('OK')
            filas.append(d)
    return (filas, rotas), log


def pendientes(raiz):
    cola = os.path.join(raiz, BANDEJA, 'ordenes')
    if not os.path.isdir(cola):
        return 0
    return len([x for x in os.listdir(cola) if x.endswith('.md')])


def mediana(valores):
    """Mediana de verdad, tambien con muestra par.

    La primera version hacia sorted(v)[len(v)//2], que con dos ejecuciones de 4s
    y 310s devolvia 310. Un instrumento cuya regla es "medir es contar, no
    estimar" no puede redondear a favor de la muestra mas grande.
    """
    v = sorted(valores)
    n = len(v)
    if not n:
        return 0
    if n % 2:
        return v[n // 2]
    return int(round((v[n // 2 - 1] + v[n // 2]) / 2.0))


def barra(parte, total, ancho=24):
    if not total:
        return ' ' * ancho
    lleno = int(round(ancho * parte / float(total)))
    return '#' * lleno + '.' * (ancho - lleno)


def resumen(raiz, desde):
    datos, log = leer(raiz, desde)
    if datos is None:
        print('\n  [--] no hay log todavia: %s' % log)
        print('       la bandeja no corrio ninguna orden en esta maquina, o es un clone recien bajado.')
        print('       El log es runtime y no se versiona. Nada que medir no es un error.\n')
        return 0
    filas, rotas = datos

    print('\n  DESPACHO DE EJECUCION - lo que se delego de verdad')
    print('  ' + '=' * 50)
    if desde:
        print('  desde %s' % desde)
    if not filas:
        print('\n  0 ejecuciones en el rango. Nada que medir.\n')
        return 0

    ok = sum(1 for f in filas if f['ok'])
    fallo = len(filas) - ok
    seg = [f['seg'] for f in filas]
    med = mediana(seg)

    print('\n  %d ejecucion(es)   %s .. %s' % (len(filas), filas[0]['fecha'], filas[-1]['fecha']))
    print('    OK     %4d  %s  %.0f%%' % (ok, barra(ok, len(filas)), 100.0 * ok / len(filas)))
    print('    FALLO  %4d  %s  %.0f%%' % (fallo, barra(fallo, len(filas)), 100.0 * fallo / len(filas)))

    print('\n  Por ejecutor:')
    por = defaultdict(list)
    for f in filas:
        por[f['ejecutor']].append(f)
    for nombre in sorted(por, key=lambda n: -len(por[n])):
        g = por[nombre]
        g_ok = sum(1 for x in g if x['ok'])
        print('    %-14s %4d ejecucion(es)   %d OK / %d fallo   mediana %ds'
              % (nombre, len(g), g_ok, len(g) - g_ok, mediana([x['seg'] for x in g])))

    print('\n  Duracion:  total %ds   mediana %ds   la mas larga %ds (%s)'
          % (sum(seg), med, max(seg), max(filas, key=lambda f: f['seg'])['orden']))

    if fallo:
        print('\n  Los fallos, por motivo:')
        for motivo, n in Counter(f['estado'] for f in filas if not f['ok']).most_common():
            print('    %-28s %d' % (motivo[:28], n))

    en_vuelo = pendientes(raiz)
    if en_vuelo:
        print('\n  %d orden(es) esperando al observer.' % en_vuelo)
    if rotas:
        print('\n  [!] %d linea(s) del log no matchearon el formato y no se contaron.' % rotas)

    print('\n  Lo que este numero NO dice: tokens, plata, ni si el ahorro fue real.')
    print('  Tampoco ve lo que se ruteo sin pasar por la bandeja.\n')
    return 0


def ordenes(raiz, desde, ultimas):
    datos, log = leer(raiz, desde)
    if datos is None:
        print('\n  [--] no hay log todavia: %s\n' % log)
        return 0
    filas, _ = datos
    if not filas:
        print('\n  0 ejecuciones en el rango.\n')
        return 0
    print('\n  %-19s  %-34s  %-12s %6s  %s' % ('CUANDO', 'ORDEN', 'EJECUTOR', 'DURA', 'ESTADO'))
    for f in list(reversed(filas))[:ultimas]:
        print('  %s %s  %-34s  %-12s %5ds  %s'
              % (f['fecha'], f['hora'], f['orden'][:34], f['ejecutor'][:12], f['seg'], f['estado']))
    print('')
    return 0


def main():
    args = sys.argv[1:]
    if not args or args[0] in ('-h', '--help'):
        print(__doc__)
        return 0
    modo = args[0]
    raiz = os.path.abspath('.')
    desde = None
    ultimas = 20
    for i, a in enumerate(args):
        if a == '--desde' and i + 1 < len(args):
            desde = args[i + 1]
        elif a == '--ultimas' and i + 1 < len(args):
            ultimas = int(args[i + 1])
        elif not a.startswith('--') and i > 0 and args[i - 1] not in ('--desde', '--ultimas'):
            raiz = os.path.abspath(a)
    if not os.path.isfile(os.path.join(raiz, '00_START_HERE.md')):
        print('\n  [X] %s no parece la raiz de Vaultrum (falta 00_START_HERE.md)\n' % raiz)
        return 1
    if modo == 'resumen':
        return resumen(raiz, desde)
    if modo == 'ordenes':
        return ordenes(raiz, desde, ultimas)
    print('\n  [X] modo desconocido: %s   (resumen | ordenes)\n' % modo)
    return 1


if __name__ == '__main__':
    sys.exit(main())

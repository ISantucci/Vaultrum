#!/usr/bin/env python3
"""Vaultrum - Area de Arquitectura - privacidad del paquete.

Tus proyectos son tuyos. `06_Proyectos/` no se versiona, pero eso no alcanza:
lo que pasa adentro de un proyecto se puede filtrar CONTADO en las notas del
sistema -- su nombre, sus artefactos, sus decisiones. Paso: antes de la v1.0
habia 85 lineas en 45 archivos versionados que nombraban proyectos privados, y
ningun instrumento lo media. El .gitignore cuida archivos; esto cuida texto.

Mide el PAQUETE (lo que `git ls-files` va a publicar) y falla si:
  1. un archivo versionado vive en 06_Proyectos/;
  2. un archivo versionado es un artefacto de la cadena (TL-, RQ-, GDS-, ...)
     o historial de uso (ARQ-, EST-, PUB-, COMMIT-, 00_Registro_*);
  3. un archivo versionado es local por nombre (*.local.*);
  4. el texto de un archivo versionado nombra un proyecto privado.

Los nombres privados salen del DISCO, nunca de un archivo versionado:
  - el nombre de cada carpeta y de cada nota suelta de 06_Proyectos/;
  - las lineas de 06_Proyectos/privado.txt, para lo que no es una carpeta
    (el nombre comercial de un juego, un cliente, un codigo interno).
En privado.txt tambien se declaran los falsos positivos -- una palabra comun
que coincide con el nombre de un proyecto -- una por linea:
    ruta | termino | razon          (ruta exacta, o carpeta/** para un subarbol)
Como la lista vive dentro de 06_Proyectos/, tampoco viaja.

La busqueda es por palabra entera y respeta mayusculas: `Rayo` no es `rayo`.
El guion bajo cuenta como borde, porque asi se nombran los artefactos: en
`SOL-001_Arquitectura_Rayo` el proyecto esta nombrado.

Lee lo que esta en el INDICE de git (lo que el proximo commit publica), no la
copia de trabajo: un archivo limpio en disco y sucio en stage se publicaria sucio.

  python3 privacidad.py [raiz]              informe
  python3 privacidad.py [raiz] --verificar  solo el veredicto (exit 1 si falla)
"""
import os, re, sys, subprocess

PROYECTOS = '06_Proyectos'
LISTA     = os.path.join(PROYECTOS, 'privado.txt')
ARTEFACTO = re.compile(r'^(TL|RQ|GDS|LDS|UXS|ART|MET|SOL|EJ|QA|VE|BUG|ARQ|EST|PUB|COMMIT)-\d{3}')
REGISTRO  = re.compile(r'^00_Registro_')
MINIMO    = 3            # un termino de menos letras no es un nombre: es ruido


def versionados(raiz):
    """[(ruta, sha)] de lo que el paquete publica, leido del indice. None si no es git."""
    try:
        r = subprocess.run(['git', '-C', raiz, 'ls-files', '-s', '-z'],
                           capture_output=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    if r.returncode != 0:
        return None
    out = []
    for reg in r.stdout.split(b'\0'):
        if not reg or b'\t' not in reg:
            continue
        meta, ruta = reg.split(b'\t', 1)
        modo, sha = meta.split()[:2]
        if modo == b'160000':
            continue                          # submodulo: no es texto de este repo
        out.append((ruta.decode('utf-8', 'replace'), sha.decode()))
    return out


def contenidos(raiz, entradas):
    """{sha: bytes} de cada blob del indice, en una sola llamada a git."""
    shas = sorted({s for _, s in entradas})
    if not shas:
        return {}
    r = subprocess.run(['git', '-C', raiz, 'cat-file', '--batch'],
                       input=('\n'.join(shas) + '\n').encode(), capture_output=True, timeout=300)
    datos, i, res = r.stdout, 0, {}
    while i < len(datos):
        fin = datos.index(b'\n', i)
        cab = datos[i:fin].split()
        i = fin + 1
        if len(cab) < 3 or cab[1] == b'missing':
            continue
        n = int(cab[2])
        res[cab[0].decode()] = datos[i:i + n]
        i += n + 1
    return res


def privados(raiz):
    """(terminos, excepciones). Todo sale de 06_Proyectos/, que no viaja."""
    base = os.path.join(raiz, PROYECTOS)
    terminos, exc = set(), []
    if not os.path.isdir(base):
        return terminos, exc
    for x in os.listdir(base):
        if x.startswith(('.', '_', '00_')):
            continue
        ruta = os.path.join(base, x)
        if os.path.isdir(ruta):
            terminos.add(x)
        elif x.endswith('.md'):
            terminos.add(x[:-3])
    lista = os.path.join(raiz, LISTA)
    if os.path.isfile(lista):
        for linea in open(lista, encoding='utf-8', errors='replace'):
            linea = linea.split('#')[0].strip()
            if not linea:
                continue
            if '|' in linea:
                p = [s.strip() for s in linea.split('|')]
                if len(p) >= 3 and p[2]:
                    exc.append((p[0].replace('\\', '/'), p[1]))
            else:
                terminos.add(linea)
    return {t for t in terminos if len(t) >= MINIMO}, exc


def exceptuado(exc, ruta, termino):
    for patron, t in exc:
        if t != termino:
            continue
        if patron == ruta or (patron.endswith('/**') and ruta.startswith(patron[:-2])):
            return True
    return False


def leer_texto(datos):
    if datos is None:
        return None
    if b'\0' in datos[:8192]:
        return None                       # binario: no hay texto que filtrar
    return datos.decode('utf-8', 'replace')


def medir(raiz):
    entradas = versionados(raiz)
    if entradas is None:
        return None
    archivos = [p for p, _ in entradas]
    terminos, exc = privados(raiz)
    fallas = []
    for p in archivos:
        nombre = os.path.basename(p)
        if p.startswith(PROYECTOS + '/'):
            fallas.append(('proyecto versionado', p, None, None))
        elif ARTEFACTO.match(nombre) or REGISTRO.match(nombre):
            fallas.append(('historial versionado', p, None, None))
        elif '.local.' in nombre:
            fallas.append(('archivo local versionado', p, None, None))
    if terminos:
        patron = re.compile(r'(?<![A-Za-z0-9])(%s)(?![A-Za-z0-9])'
                            % '|'.join(re.escape(t) for t in sorted(terminos, key=len, reverse=True)))
        blobs = contenidos(raiz, entradas)
        for p, sha in entradas:
            if p.startswith(PROYECTOS + '/'):
                continue
            txt = leer_texto(blobs.get(sha))
            if not txt:
                continue
            for n, linea in enumerate(txt.splitlines(), 1):
                for m in patron.finditer(linea):
                    if not exceptuado(exc, p, m.group(1)):
                        fallas.append(('nombra un proyecto privado', p, n, m.group(1)))
    return fallas, terminos, archivos


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    raiz = os.path.abspath(args[0] if args else '.')
    solo = '--verificar' in sys.argv
    r = medir(raiz)
    if r is None:
        print('PRIVACIDAD: no es un repo git, no hay paquete que medir.')
        return 0
    fallas, terminos, archivos = r
    if not fallas:
        if terminos:
            print('PRIVACIDAD EN LEY: los %d archivos del paquete no nombran ninguno de tus %d '
                  'termino(s) privado(s), y nada de 06_Proyectos viaja.' % (len(archivos), len(terminos)))
        else:
            print('PRIVACIDAD EN LEY: nada de 06_Proyectos viaja (no hay proyectos locales que nombrar).')
        return 0
    print('PRIVACIDAD FUERA DE LEY: %d hallazgo(s). Esto se publicaria con el proximo push:' % len(fallas))
    mostradas = fallas if not solo else fallas[:15]
    for tipo, p, n, t in mostradas:
        if n:
            print('  %s:%d  %s  «%s»' % (p, n, tipo, t))
        else:
            print('  %s  %s' % (p, tipo))
    if len(mostradas) < len(fallas):
        print('  ... y %d mas (correlo sin --verificar para verlos todos)' % (len(fallas) - len(mostradas)))
    print('')
    print('  Reescribi la linea sin el nombre: la leccion viaja, el proyecto no.')
    print('  Si es una palabra comun que coincide, declarala en %s:' % LISTA)
    print('    ruta | termino | razon')
    return 1


if __name__ == '__main__':
    sys.exit(main())

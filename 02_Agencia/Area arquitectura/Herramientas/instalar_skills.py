#!/usr/bin/env python3
"""Vaultrum - instalador del entorno de trabajo (RQ-007.7 . Portabilidad).

Se llama "instalador de skills" por historia y hace mas que eso: deja el entorno
armado para las dos superficies donde corre Vaultrum, y verifica que se pueda
trabajar de verdad antes de decir que termino.

Las skills VIVEN en su area. Esto las SINCRONIZA a los dos directorios donde
los asistentes las descubren solos. No es una mudanza: es una copia, y la
fuente sigue siendo el area.

    02_Agencia/Area X/Skills/vaultrum-X/SKILL.md      <-- la fuente
            |
            +--> .claude/skills/vaultrum-X/           Claude Code
            +--> .agents/skills/vaultrum-X/           Codex, Cursor, Zed, Copilot

  python3 instalar_skills.py [ruta_del_vault]        sincroniza, instala y verifica
  python3 instalar_skills.py [ruta] --verificar      solo mide, no escribe (exit 1 si difiere)

Cuatro cosas, en este orden:
  1. sincroniza las skills a los dos directorios de descubrimiento
  2. instala el gate de cierre en .git/hooks/pre-commit
  3. prepara la bandeja de ordenes (runtime de la capa IA Operativa)
  4. verifica el ENTORNO y da un veredicto: se puede trabajar, o que falta

POR QUE EXISTE ESTE ARCHIVO
Reemplaza la logica que vivia dentro de skills.bat y skills.sh. La version .bat
tenia un defecto de los que no avisan: borraba los dos destinos ANTES de copiar,
y su calculo del nombre de la skill se resolvia al nombre de una carpeta
ancestro en vez del de la skill. Resultado: borraba las once skills instaladas
y despues copiaba el repo entero dentro de .claude/skills/<carpeta>/, de forma
recursiva, hasta que el usuario cerraba la ventana. Desde afuera parecia que
"no hacia nada".

Dos reglas salieron de eso y estan implementadas aca:
  1. No se destruye el destino antes de saber que la fuente esta bien.
  2. El recorrido EXCLUYE los destinos. Un instalador que se lee a si mismo
     como fuente es una recursion esperando pasar.

Y una tercera, del 2026-08-28, que es de superficie y no de logica:
  3. Borrar es LIMPIEZA, no parte de la instalacion. Hay superficies donde el
     proceso no puede borrar -- un montaje remoto, un permiso restringido -- y
     ahi este script moria con traceback DESPUES de haber sincronizado bien,
     diciendo que fallo cuando habia terminado. Es la misma mentira que
     instalar_trace.py ya habia arreglado por otra puerta. Ahora lo que no se
     puede borrar se aparta a _to_delete/ y se avisa; la instalacion no depende
     de eso. Ver `La superficie del ejecutor` en el Core.
"""
import os, sys, shutil, re, hashlib, time, subprocess

DESTINOS = ['.claude/skills', '.agents/skills']
EXCLUIR  = {'.git', '.claude', '.agents', 'node_modules', '_to_delete'}
HOOK_SRC = os.path.join('02_Agencia', 'Area arquitectura', 'Herramientas', 'pre-commit')
TOPE_TOTAL, TOPE_UNA = 8000, 1536
MARCA = ('Generado por instalar_skills.py desde 02_Agencia/Area */Skills/ y las capas 03/04/05.\n'
         'Editar aca no cambia el sistema: se pisa en la proxima corrida.\n'
         'Para cambiar una skill, edita su fuente en el area y volve a correr el instalador.\n')
PAPELERA = '_to_delete'
# La marca se escribe DENTRO de cada carpeta generada, no solo en la raiz del
# destino. Es lo unico que distingue una copia nuestra de una skill que el
# usuario instalo por su cuenta, y sin ese dato el instalador no puede borrar
# nada sin arriesgarse a borrar lo ajeno.
SELLO = '_GENERADO_NO_EDITAR.txt'
_apartados = []

BANDEJA     = os.path.join('04_IA Operativa', 'Herramientas', 'bandeja')
BANDEJA_SUB = ('ordenes', 'resultados', 'procesadas')

# Las dos superficies donde corre Vaultrum, y que necesita cada una para
# descubrir las skills solo. Las rutas NO son una preferencia nuestra: son las
# que cada harness escanea. Codex escanea .agents/skills en el repo (y tambien
# en $HOME y /etc/codex/skills); Claude Code, .claude/skills.
# Fuente: developers.openai.com/codex -> Build skills, 2026-09-01.
HARNESS = (
    # nombre         binario   destino            puerta       config
    ('Claude Code',  'claude', '.claude/skills',  'CLAUDE.md', None),
    ('Codex',        'codex',  '.agents/skills',  'AGENTS.md', '.codex/config.toml'),
)


def huella_archivo(ruta):
    """sha1 de un archivo suelto. La `huella` que ya existe es de arboles."""
    h = hashlib.sha1()
    try:
        with open(ruta, 'rb') as f:
            for bloque in iter(lambda: f.read(65536), b''):
                h.update(bloque)
    except OSError:
        return None
    return h.hexdigest()


def descartar(ruta):
    """Saca `ruta` de en medio. Borrarla es lo ideal, no es lo obligatorio.

    Regla 3 del docstring: hay superficies donde el proceso no puede borrar. Un
    instalador que muere ahi reporta un fallo que no ocurrio. Cuando no se puede,
    se aparta a _to_delete/ (que esta en EXCLUIR y en el .gitignore) y se avisa
    al final, una vez, en vez de romper.
    """
    if not os.path.isdir(ruta):
        return
    try:
        shutil.rmtree(ruta)
        return
    except OSError:
        pass
    destino = os.path.join(PAPELERA, 'instalador',
                           os.path.basename(ruta) + '.' + str(int(time.time() * 1000)))
    try:
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        os.rename(ruta, destino)
        _apartados.append(destino)
    except OSError:
        _apartados.append(ruta + '  (no se pudo ni borrar ni mover)')


def fuentes(raiz):
    """{nombre_de_skill: ruta_de_su_carpeta}. Excluye los destinos: eso es lo que evita la recursion."""
    out = {}
    for base, dirs, files in os.walk(raiz):
        dirs[:] = [d for d in dirs if d not in EXCLUIR]
        if 'SKILL.md' in files:
            nombre = os.path.basename(base)
            if nombre in out:
                # F5: elegir una fuente por el orden de os.walk es elegir al azar, y despues
                # --verificar la compara contra la fuente equivocada y dice que esta todo bien.
                raise SystemExit(f'  [ERROR] dos fuentes se llaman «{nombre}»:\n'
                                 f'          {out[nombre]}\n          {base}\n'
                                 f'  No se toca ningun destino. Renombra una de las dos.')
            out[nombre] = base
    return out


def huella(ruta):
    """Hash del ARBOL entero, no solo de SKILL.md.

    F4: comparar solo SKILL.md deja pasar assets, scripts y referencias divergentes,
    y --verificar devuelve 0 sobre una copia que no es igual a su fuente.
    """
    h = hashlib.sha256()
    for base, dirs, files in os.walk(ruta):
        dirs.sort()
        for f in sorted(files):
            rel = os.path.relpath(os.path.join(base, f), ruta).replace('\\', '/')
            h.update(rel.encode())
            with open(os.path.join(base, f), 'rb') as fh:
                h.update(fh.read())
    return h.hexdigest()


def sincronizar(origen, destino):
    """Copia a un temporal, valida, y recien despues reemplaza.

    F3: la version anterior hacia rmtree(destino) y despues copytree. Un fallo por
    permisos, disco lleno o interrupcion dejaba la skill ausente o a medias --
    exactamente el modo de falla que este instalador existe para no repetir, y que
    su propio docstring declara prohibido. Escribirlo mal una vez es un error;
    escribirlo mal en el archivo que denuncia ese error es peor.
    """
    tmp    = destino + '.nuevo'
    previo = destino + '.previo'
    for x in (tmp, previo):
        descartar(x)
    shutil.copytree(origen, tmp)
    if huella(tmp) != huella(origen):
        descartar(tmp)
        raise SystemExit(f'  [ERROR] la copia de «{os.path.basename(origen)}» no coincide '
                         f'con su fuente. No se reemplaza nada.')
    if os.path.isdir(destino):
        os.rename(destino, previo)
    try:
        os.rename(tmp, destino)
    except OSError:
        if os.path.isdir(previo):
            os.rename(previo, destino)     # se restaura la copia que andaba
        raise
    descartar(previo)
    # El sello va DESPUES de validar la huella, no antes: si se escribiera en el
    # temporal, la copia no coincidiria con su fuente y la validacion de arriba
    # -- que es la que evita reemplazar con una copia rota -- fallaria siempre.
    try:
        with open(os.path.join(destino, SELLO), 'w', encoding='utf-8') as f:
            f.write(MARCA)
    except OSError:
        pass


def es_generada(ruta):
    """¿Esta carpeta la escribio este instalador?

    ARQ-024: hasta hoy, toda carpeta en .claude/skills/ o .agents/skills/ sin
    fuente en el vault se consideraba huerfana y se borraba. Quien tuviera skills
    propias ahi las perdia sin que nadie le preguntara. Un instalador puede pisar
    lo que genero; no puede borrar lo que no instalo.

    En una instalacion vieja no hay sellos por carpeta todavia: la primera corrida
    despues de este cambio no va a borrar nada y lo va a avisar. Es el lado
    correcto en el que equivocarse.
    """
    return os.path.isfile(os.path.join(ruta, SELLO))


def descripcion(ruta):
    txt = open(os.path.join(ruta, 'SKILL.md'), encoding='utf-8', errors='replace').read()
    m = re.search(r'^description:\s*"?(.*?)"?\s*$', txt.split('\n---', 1)[0], re.M | re.S)
    return len(m.group(1)) if m else 0


def preparar_bandeja(solo_medir):
    """Deja lista la bandeja de ordenes de la capa IA Operativa.

    La bandeja es el canal entre el productor -- la conversacion donde se decide --
    y los ejecutores que tienen manos: el productor deja una orden en ordenes/, el
    observer la ejecuta parado en el proyecto, y la salida vuelve a resultados/.

    Tres decisiones, para que no se lea como algo que no es:
      1. NO copia observer.ps1 ni observer.bat. La herramienta vive en su area,
         igual que cada skill vive en la suya. Aca solo se crea lo que es runtime.
      2. NO toca el contenido de ordenes/, resultados/ ni procesadas/. Correr el
         instalador cien veces no puede costar una orden en vuelo.
      3. NO cuenta como diferencia en --verificar. La bandeja no es una copia
         generada que pueda quedar fuera de sincronia con una fuente: es
         infraestructura de ejecucion. Si falta, se avisa; el gate no se rompe.
    """
    if not os.path.isdir(BANDEJA):
        print('\n  [--] bandeja: no instalada (falta %s)' % BANDEJA)
        return

    faltantes = [s for s in BANDEJA_SUB if not os.path.isdir(os.path.join(BANDEJA, s))]

    if solo_medir:
        print('\n  [%s] bandeja: %s' % ('ok' if not faltantes else '!!', BANDEJA))
        for s in faltantes:
            print('       falta %s/' % s)
    else:
        for s in BANDEJA_SUB:
            os.makedirs(os.path.join(BANDEJA, s), exist_ok=True)
        print('\n  [ok] bandeja lista: %s' % BANDEJA)

    cola = os.path.join(BANDEJA, 'ordenes')
    if os.path.isdir(cola):
        pendientes = len([x for x in os.listdir(cola) if x.endswith('.md')])
        if pendientes:
            print('       %d orden(es) esperando al observer' % pendientes)

    if shutil.which('claude') is None:
        print('       [aviso] "claude" no esta en el PATH: el observer arranca pero no ejecuta')
    else:
        print('       arrancalo con %s' % os.path.join(BANDEJA, 'observer.bat'))


def version_de(binario):
    """La version del ejecutor, o vacio. Nunca cuelga y nunca rompe.

    Un instalador que se traba preguntandole la version a un binario es peor que
    uno que no la sabe. Timeout corto y except ancho a proposito.
    """
    try:
        r = subprocess.run([binario, '--version'], capture_output=True, text=True, timeout=10)
        linea = (r.stdout or r.stderr or '').strip().splitlines()[0][:40]
        # Si no tiene un digito no es una version: es un mensaje de error del
        # binario. Imprimirlo igual seria informar ruido como si fuera un dato.
        return linea if any(c.isdigit() for c in linea) else ''
    except Exception:
        return ''


def hermanos_del_vault(raiz):
    """Carpetas vecinas del vault: los candidatos a proyecto, para no adivinar.

    El observer necesita saber contra que proyecto corre y eso es un dato de cada
    maquina. No se puede inventar, pero si se puede mostrar la lista para que el
    owner elija sin salir a buscarla.
    """
    padre = os.path.dirname(os.path.abspath(raiz))
    yo = os.path.basename(os.path.abspath(raiz))
    try:
        return sorted(x for x in os.listdir(padre)
                      if x != yo and not x.startswith('.')
                      and os.path.isdir(os.path.join(padre, x)))[:8]
    except OSError:
        return []


def verificar_entorno(raiz):
    """El chequeo de harness: despues de correr esto, se puede trabajar o no.

    POR QUE EXISTE
    El instalador sincronizaba las skills a los dos destinos y daba por hecho el
    resto. Pero una skill copiada a .agents/skills no sirve de nada si codex no
    esta instalado, y la bandeja no puede despachar nada si no sabe contra que
    proyecto corre. El resultado era un instalador que decia "Listo" sobre un
    entorno que no podia trabajar.

    Esto es `La superficie del ejecutor` aplicada al arranque: se comprueba que
    se PUEDE, antes de que alguien gaste una sesion descubriendo que no.

    NO FALLA NI CUENTA COMO DIFERENCIA. Misma regla que la bandeja: esto no es
    una copia generada que pueda quedar fuera de sincronia con una fuente, es
    infraestructura. Se informa; el gate no se rompe. Que falte codex en una
    maquina es un hecho de esa maquina, no un defecto del vault.
    """
    print('\n  ENTORNO - las dos superficies donde corre Vaultrum')
    print('  ' + '-' * 50)
    faltan = []

    for nombre, binario, destino, puerta, config in HARNESS:
        ruta = shutil.which(binario)
        n = len([x for x in os.listdir(destino)
                 if os.path.isdir(os.path.join(destino, x))]) if os.path.isdir(destino) else 0
        marca = 'ok' if ruta else '--'
        if not ruta:
            faltan.append("%s no esta en el PATH (%s no se puede usar aca)" % (binario, nombre))
        print('\n  [%s] %-12s %s' % (marca, nombre, ruta or 'no esta en el PATH'))
        v = version_de(binario) if ruta else ''
        if v:
            print('       version    %s' % v)
        print('       descubre   %s  (%d skills)' % (destino, n))
        if not os.path.isfile(puerta):
            faltan.append('falta la puerta %s' % puerta)
            print('       puerta     [!!] falta %s' % puerta)
        else:
            print('       puerta     %s' % puerta)
        if config:
            estado = 'ok' if os.path.isfile(config) else '[!!] falta'
            print('       config     %s  %s' % (config, estado))
            if not os.path.isfile(config):
                faltan.append('falta %s' % config)

    # el gate de cierre
    hook = os.path.join('.git', 'hooks', 'pre-commit')
    print('\n  [%s] gate       %s' % ('ok' if os.path.isfile(hook) else '--', hook))
    if not os.path.isfile(hook):
        faltan.append('el gate de cierre no esta instalado (corre el instalador sin --verificar)')

    # la bandeja necesita saber contra que proyecto corre
    cfg = os.path.join(BANDEJA, 'proyecto.local.txt')
    if os.path.isfile(cfg):
        try:
            destino_obs = [l.strip() for l in open(cfg, encoding='utf-8')
                           if l.strip() and not l.strip().startswith('#')][0]
        except (IndexError, OSError):
            destino_obs = '(vacio)'
        print('  [ok] bandeja    despacha a: %s' % destino_obs)
    else:
        print('  [!!] bandeja    falta %s' % cfg)
        print('       el observer no sabe contra que proyecto correr. Escribi la ruta ahi.')
        vecinos = hermanos_del_vault(raiz)
        if vecinos:
            print('       candidatos vecinos del vault: %s' % ', '.join(vecinos))
        faltan.append('falta %s' % cfg)

    print('')
    if faltan:
        print('  VEREDICTO: el entorno NO esta listo. %d cosa(s):' % len(faltan))
        for f in faltan:
            print('    - %s' % f)
        print('  Nada de esto rompe el vault: son datos de esta maquina.')
    else:
        print('  VEREDICTO: entorno listo. Los dos harnesses descubren las skills,')
        print('             el gate corre y la bandeja sabe a donde despachar.')
    return len(faltan)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    raiz = os.path.abspath(args[0] if args else '.')
    solo_medir = '--verificar' in sys.argv
    os.chdir(raiz)

    if not os.path.isfile('00_START_HERE.md'):
        print('  [ERROR] Esto no parece la raiz de Vaultrum.')
        return 2

    print('\n  VAULTRUM - instalador de skills')
    print('  ===============================\n')

    src = fuentes('.')
    if not src:
        print('  [ERROR] no se encontro ninguna SKILL.md. No se toca nada.')
        return 2

    difiere = []
    for nombre, ruta in sorted(src.items()):
        h_src = huella(ruta)
        estados = []
        for d in DESTINOS:
            dst = os.path.join(d, nombre)
            igual = os.path.isdir(dst) and huella(dst) == h_src
            if not igual:
                difiere.append(f'{d}/{nombre}')
                estados.append('difiere')
            if not solo_medir and not igual:
                sincronizar(ruta, dst)
            if not solo_medir and os.path.isdir(dst) and not os.path.isfile(os.path.join(dst, SELLO)):
                # Sellar tambien lo que ya estaba al dia: sin esto, una instalacion
                # existente nunca se sella (nunca pasa por sincronizar) y queda
                # indistinguible de una skill que el usuario puso a mano.
                try:
                    with open(os.path.join(dst, SELLO), 'w', encoding='utf-8') as f:
                        f.write(MARCA)
                except OSError:
                    pass
        print(f'  [{"==" if not estados else "ok" if not solo_medir else "!!"}] {nombre}')

    # destinos que ya no tienen fuente
    huerfanas = []
    for d in DESTINOS:
        if os.path.isdir(d):
            for x in os.listdir(d):
                if os.path.isdir(os.path.join(d, x)) and x not in src:
                    huerfanas.append(os.path.join(d, x))
    if huerfanas:
        mias   = [h for h in huerfanas if es_generada(h)]
        ajenas = [h for h in huerfanas if not es_generada(h)]
        if mias:
            print('\n  Sin fuente en el area (se borran: llevan el sello de este instalador):')
            for h in mias:
                print(f'    - {h}')
                difiere.append(h)      # F4: una huerfana ES una diferencia
                if not solo_medir:
                    descartar(h)
        if ajenas:
            print('\n  [!] Hay carpetas en los destinos que este instalador NO genero.')
            print('      No se tocan. Si son tuyas, quedan donde estan; si sobraron de una')
            print('      instalacion vieja, borralas a mano y la proxima corrida no las nombra:')
            for h in ajenas:
                print(f'    - {h}')

    if not solo_medir:
        for d in DESTINOS:
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, '_GENERADO_NO_EDITAR.txt'), 'w', encoding='utf-8').write(MARCA)
        if os.path.isdir('.git') and os.path.isfile(HOOK_SRC):
            os.makedirs(os.path.join('.git', 'hooks'), exist_ok=True)
            destino_hook = os.path.join('.git', 'hooks', 'pre-commit')
            # Un hook ajeno no se pisa en silencio: se respalda y se avisa. Perder
            # el gate de otro proyecto sin decirlo es la misma clase de fallo que
            # borrar sus skills.
            if os.path.isfile(destino_hook) and huella_archivo(destino_hook) != huella_archivo(HOOK_SRC):
                copia = destino_hook + '.previo-' + time.strftime('%Y%m%d-%H%M%S')
                try:
                    shutil.copyfile(destino_hook, copia)
                    print(f'\n  [!] Ya habia un pre-commit distinto. Se respaldo en {copia}')
                except OSError:
                    print('\n  [!] Ya habia un pre-commit distinto y no se pudo respaldar.')
                    print('      No se pisa. Movelo a mano si querias el gate de Vaultrum.')
                    raise SystemExit(3)
            shutil.copyfile(HOOK_SRC, destino_hook)
            try:
                os.chmod(os.path.join('.git', 'hooks', 'pre-commit'), 0o755)
            except OSError:
                pass
            print('\n  [ok] gate de cierre instalado en .git/hooks/pre-commit')

    preparar_bandeja(solo_medir)

    # presupuesto de contexto residente
    print(f'\n  {len(src)} skills · residente (suma de las descriptions):')
    total = 0
    for nombre, ruta in sorted(src.items()):
        n = descripcion(ruta)
        total += n
        if n > TOPE_UNA:
            print(f'    [AVISO] {nombre}: {n} chars, pasa el tope de {TOPE_UNA} por entrada')
    pct = total * 100 // TOPE_TOTAL
    estado = 'AVISO' if total > TOPE_TOTAL else 'ok'
    print(f'    [{estado}] {total} chars / {TOPE_TOTAL} tope de Codex = {pct}%')

    if _apartados:
        print('\n  [aviso] esta superficie no permite borrar. Se aparto a _to_delete/,')
        print('          la instalacion quedo completa igual. Borralos a mano:')
        for a in _apartados:
            print(f'    - {a}')

    pendientes_entorno = verificar_entorno(raiz)

    if solo_medir and difiere:
        print(f'\n  FUERA DE SINCRONIA: {len(difiere)} copia(s) difieren de su fuente.')
        return 1
    # El instalador no puede decir "Listo" sobre un entorno que no puede
    # trabajar: ese es el mismo fallo que se disfraza de exito que el vault
    # persigue en todos lados. Las skills quedaron sincronizadas igual -- eso es
    # lo que hace este script -- pero lo que falta se dice en el cierre, no
    # cincuenta lineas mas arriba donde nadie lo lee.
    if pendientes_entorno:
        print('\n  Skills sincronizadas. El entorno NO esta completo: resolve lo de arriba')
        print('  y volve a correr el instalador para confirmarlo.\n')
        return 0
    print('\n  Listo. Abri una sesion nueva para que el asistente las descubra.\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())

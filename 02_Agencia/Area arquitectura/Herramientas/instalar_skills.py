#!/usr/bin/env python3
"""Vaultrum - instalador de skills (RQ-007.7 . Portabilidad).

Las skills VIVEN en su area. Esto las SINCRONIZA a los dos directorios donde
los asistentes las descubren solos. No es una mudanza: es una copia, y la
fuente sigue siendo el area.

    02_Agencia/Area X/Skills/vaultrum-X/SKILL.md      <-- la fuente
            |
            +--> .claude/skills/vaultrum-X/           Claude Code
            +--> .agents/skills/vaultrum-X/           Codex, Cursor, Zed, Copilot

  python3 instalar_skills.py [ruta_del_vault]        sincroniza e instala el hook
  python3 instalar_skills.py [ruta] --verificar      solo mide, no escribe (exit 1 si difiere)

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
"""
import os, sys, shutil, re

DESTINOS = ['.claude/skills', '.agents/skills']
EXCLUIR  = {'.git', '.claude', '.agents', 'node_modules', '_to_delete'}
HOOK_SRC = os.path.join('02_Agencia', 'Area arquitectura', 'Herramientas', 'pre-commit')
TOPE_TOTAL, TOPE_UNA = 8000, 1536
MARCA = ('Generado por instalar_skills.py desde 02_Agencia/Area */Skills/ y las capas 03/04/05.\n'
         'Editar aca no cambia el sistema: se pisa en la proxima corrida.\n'
         'Para cambiar una skill, edita su fuente en el area y volve a correr el instalador.\n')


def fuentes(raiz):
    """{nombre_de_skill: ruta_de_su_carpeta}. Excluye los destinos: eso es lo que evita la recursion."""
    out = {}
    for base, dirs, files in os.walk(raiz):
        dirs[:] = [d for d in dirs if d not in EXCLUIR]
        if 'SKILL.md' in files:
            nombre = os.path.basename(base)
            if nombre in out:
                print(f'  [AVISO] dos fuentes se llaman «{nombre}»: {out[nombre]} y {base}')
            out[nombre] = base
    return out


def descripcion(ruta):
    txt = open(os.path.join(ruta, 'SKILL.md'), encoding='utf-8', errors='replace').read()
    m = re.search(r'^description:\s*"?(.*?)"?\s*$', txt.split('\n---', 1)[0], re.M | re.S)
    return len(m.group(1)) if m else 0


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
        estados = []
        for d in DESTINOS:
            dst = os.path.join(d, nombre)
            igual = (os.path.isfile(os.path.join(dst, 'SKILL.md')) and
                     open(os.path.join(dst, 'SKILL.md'), 'rb').read() ==
                     open(os.path.join(ruta, 'SKILL.md'), 'rb').read())
            if not igual:
                difiere.append(f'{d}/{nombre}')
                estados.append('difiere')
            if not solo_medir:
                if os.path.isdir(dst):
                    shutil.rmtree(dst)
                shutil.copytree(ruta, dst)
        print(f'  [{"==" if not estados else "ok" if not solo_medir else "!!"}] {nombre}')

    # destinos que ya no tienen fuente
    huerfanas = []
    for d in DESTINOS:
        if os.path.isdir(d):
            for x in os.listdir(d):
                if os.path.isdir(os.path.join(d, x)) and x not in src:
                    huerfanas.append(os.path.join(d, x))
    if huerfanas:
        print('\n  Sin fuente en el area (se borran, son copias generadas):')
        for h in huerfanas:
            print(f'    - {h}')
            if not solo_medir:
                shutil.rmtree(h)

    if not solo_medir:
        for d in DESTINOS:
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, '_GENERADO_NO_EDITAR.txt'), 'w', encoding='utf-8').write(MARCA)
        if os.path.isdir('.git') and os.path.isfile(HOOK_SRC):
            os.makedirs(os.path.join('.git', 'hooks'), exist_ok=True)
            shutil.copyfile(HOOK_SRC, os.path.join('.git', 'hooks', 'pre-commit'))
            try:
                os.chmod(os.path.join('.git', 'hooks', 'pre-commit'), 0o755)
            except OSError:
                pass
            print('\n  [ok] gate de cierre instalado en .git/hooks/pre-commit')

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

    if solo_medir and difiere:
        print(f'\n  FUERA DE SINCRONIA: {len(difiere)} copia(s) difieren de su fuente.')
        return 1
    print('\n  Listo. Abri una sesion nueva para que el asistente las descubra.\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())

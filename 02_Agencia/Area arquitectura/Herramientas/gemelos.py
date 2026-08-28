#!/usr/bin/env python3
"""Vaultrum - Arquitectura - los archivos que tienen que ser identicos, lo son.

El vault tiene copias deliberadas. CLAUDE.md y AGENTS.md son la MISMA puerta para
dos harnesses que leen nombres distintos (RQ-007.2). Las skills viven versionadas
en la carpeta de su area y se copian a .claude/skills y .agents/skills, que es lo
que el harness carga.

Ninguna de esas copias estaba verificada. Una copia que nadie compara **deriva**:
alguien edita CLAUDE.md y no AGENTS.md, y a partir de ahi Codex y Claude reciben
instrucciones distintas del mismo vault, sin un solo sintoma.

Dos relaciones distintas, y la diferencia importa:

  ESPEJO    ninguno es el original: los dos tienen que decir lo mismo
            CLAUDE.md == AGENTS.md
  COPIA     hay un original y hay derivados: el derivado sigue al original
            02_Agencia/.../Skills/X/SKILL.md  ->  .claude/skills/X/SKILL.md
                                              ->  .agents/skills/X/SKILL.md

Un espejo que difiere no dice cual esta bien: hay que decidirlo.
Una copia que difiere si lo dice: gana la fuente versionada.

  python3 gemelos.py <ruta_del_vault>              informe
  python3 gemelos.py <ruta> --verificar            exit 1 si algo derivo
  python3 gemelos.py <ruta> --sincronizar          reescribe las COPIAS desde su
                                                   fuente. Nunca toca un espejo.
"""
import os, sys, hashlib

ESPEJOS = [(('CLAUDE.md', 'AGENTS.md'),
            'misma puerta para dos harnesses que leen nombres distintos (RQ-007.2)')]
DESTINOS = ('.claude/skills', '.agents/skills')


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def fuentes_de_skills(raiz):
    """{nombre_de_skill: ruta de su fuente versionada}"""
    out = {}
    for dp, dn, fn in os.walk(raiz):
        if any(x in dp for x in ('.git', '.claude', '.agents')):
            continue
        if os.path.basename(os.path.dirname(dp)) == 'Skills' and 'SKILL.md' in fn:
            out[os.path.basename(dp)] = os.path.join(dp, 'SKILL.md')
    return out


def revisar(raiz):
    fallas, revisados = [], 0

    for grupo, razon in ESPEJOS:
        rutas = [os.path.join(raiz, g) for g in grupo]
        faltan = [g for g, r in zip(grupo, rutas) if not os.path.isfile(r)]
        if faltan:
            fallas.append(f"espejo: falta {', '.join(faltan)} — {razon}")
            continue
        revisados += 1
        if len({sha(r) for r in rutas}) > 1:
            fallas.append(f"ESPEJO DERIVADO: {' y '.join(grupo)} difieren, y tienen que "
                          f"decir lo mismo ({razon}). Ninguno es el original: decidí cuál vale.")

    for nombre, fuente in sorted(fuentes_de_skills(raiz).items()):
        h = sha(fuente)
        for d in DESTINOS:
            copia = os.path.join(raiz, d, nombre, 'SKILL.md')
            if not os.path.isfile(copia):
                fallas.append(f"copia ausente: {d}/{nombre}/SKILL.md — la fuente existe y "
                              f"el harness no la ve. Corré skills.sh / skills.bat.")
                continue
            revisados += 1
            if sha(copia) != h:
                fallas.append(f"COPIA DERIVADA: {d}/{nombre}/SKILL.md ≠ su fuente "
                              f"{os.path.relpath(fuente, raiz)} — gana la fuente.")
    return fallas, revisados


def sincronizar(raiz):
    """Reescribe las COPIAS desde su fuente. Los espejos NO se tocan."""
    n = 0
    for nombre, fuente in sorted(fuentes_de_skills(raiz).items()):
        datos = open(fuente, 'rb').read()
        for d in DESTINOS:
            copia = os.path.join(raiz, d, nombre, 'SKILL.md')
            if os.path.isfile(copia) and open(copia, 'rb').read() != datos:
                open(copia, 'wb').write(datos)
                print(f"  sincronizada  {d}/{nombre}/SKILL.md")
                n += 1
    print(f"{n} copia(s) sincronizada(s) desde su fuente versionada."
          if n else "Nada que sincronizar: todas las copias siguen a su fuente.")
    print("Los espejos (CLAUDE.md / AGENTS.md) no se tocan: no hay original que gane.")
    return 0


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    raiz = args[0] if args else '.'
    if '--sincronizar' in sys.argv:
        sys.exit(sincronizar(raiz))
    fallas, n = revisar(raiz)
    if fallas:
        print("GEMELOS FUERA DE NORMA:")
        for f in fallas:
            print(f"  {f}")
        print("\nUna copia que nadie compara deriva. `--sincronizar` arregla las copias;")
        print("un espejo derivado se decide a mano.")
        sys.exit(1)
    print(f"GEMELOS EN NORMA: {n} archivo(s) que deben ser identicos, lo son.")
    sys.exit(0)

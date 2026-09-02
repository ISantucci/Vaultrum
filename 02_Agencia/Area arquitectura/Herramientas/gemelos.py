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
  python3 gemelos.py <ruta> --parecidos            lo que NO deberia ser identico
                                                   y casi lo es. Reporta, no repara.

EL TERCER CASO: LA CASI-DUPLICACION
Espejos y copias son duplicacion DELIBERADA, y este script las cuida. Lo que
nadie medía es la otra: dos bloques que dicen lo mismo con distinta redaccion,
en archivos que la regla de capas separa a proposito. Ahi empieza la deriva --
un texto se edita, el otro no, y nadie se entera hasta que chocan.

ARQ-024 encontro seis solapamientos leyendo, y la conclusion incomoda es que el
sistema YA sabia que esto pasa: lo escribio dos veces el mismo mes y volvio a
pasar igual. Una regla que solo vive escrita se incumple; lo que se cumple es lo
que se mide.

Este modo REPORTA y no repara. Decidir cual de dos textos manda es juicio, y el
juicio no se automatiza.
"""
import os, sys, hashlib, re, difflib, unicodedata, collections

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


# ------------------------------------------------------- casi-duplicacion
# UMBRAL 0.85, y sale de medir, no de elegir a ojo.
#
# Se midio la similitud de los 1446 bloques comparables de 02_Agencia. La
# distribucion tiene masa arriba de 0.7 y se desploma abajo de 0.6: entre 0.6 y
# 0.85 hay parecido de familia -- mismo vocabulario, contenido distinto -- y de
# 0.85 para arriba los dos bloques dicen lo mismo con diferencias cosmeticas,
# que es exactamente el estado en el que una edicion los separa en silencio.
# El caso que ARQ-024 documento por nombre (el bloque de instrumento del QA,
# copiado en la skill y en 00_Indice_qa) mide 1.00.
UMBRAL = 0.85
MIN_BLOQUE = 160          # menos que esto es una frase, no un bloque
PREFILTRO = 0.35          # Jaccard de palabras largas: evita comparar todo con todo


def _norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[`*_#>|\-–—]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def _comparables(raiz):
    """Los archivos que la regla de capas separa: si dos de estos coinciden, importa."""
    out = []
    for dp, dn, fn in os.walk(raiz):
        dn[:] = [d for d in dn if not d.startswith('.') and d not in ('_to_delete', '06_Proyectos')]
        for f in fn:
            rel = os.path.relpath(os.path.join(dp, f), raiz).replace('\\', '/')
            if not rel.endswith('.md') or not rel.startswith('02_Agencia'):
                continue
            if '/Salidas/' in rel and not re.search(r'/00_(Indice|Salidas|Registro)', rel):
                continue          # los artefactos se parecen entre si por contrato
            txt = open(os.path.join(dp, f), encoding='utf-8', errors='replace').read()
            for par in re.split(r'\n\s*\n', txt):
                n = _norm(par)
                if len(n) >= MIN_BLOQUE:
                    # La etiqueta salta la linea de cerca: "```txt" no dice nada
                    # de que es el bloque, y un informe que no se puede leer no
                    # sirve para decidir.
                    lineas = [l for l in par.strip().split('\n')
                              if l.strip() and not l.strip().startswith('```')]
                    out.append((rel, n, frozenset(w for w in n.split() if len(w) > 4),
                                (lineas[0].strip() if lineas else par.strip())[:62]))
    return out


def parecidos(raiz):
    bloques = _comparables(raiz)
    hallazgos = []
    for i in range(len(bloques)):
        ra, na, sa, ma = bloques[i]
        for j in range(i + 1, len(bloques)):
            rb, nb, sb, mb = bloques[j]
            if ra == rb:
                continue
            if abs(len(na) - len(nb)) > max(len(na), len(nb)) * 0.4:
                continue
            inter = len(sa & sb)
            if not inter or inter / float(len(sa | sb)) < PREFILTRO:
                continue
            r = difflib.SequenceMatcher(None, na, nb).ratio()
            if r >= UMBRAL:
                hallazgos.append((r, ra, rb, ma))
    hallazgos.sort(reverse=True)

    print('\n  CASI-DUPLICACION - lo que no deberia ser identico y casi lo es')
    print('  ' + '=' * 62)
    print('  %d bloques comparables en %d archivos de la Agencia · umbral %.2f'
          % (len(bloques), len({b[0] for b in bloques}), UMBRAL))
    if not hallazgos:
        print('\n  Ningun par pasa el umbral. Nada que decidir.\n')
        return 0
    print('\n  %d par(es). Por archivo, los que mas aparecen:\n' % len(hallazgos))
    cuenta = collections.Counter()
    for _, a, b, _ in hallazgos:
        cuenta[a] += 1
        cuenta[b] += 1
    for arch, n in cuenta.most_common(10):
        print('    %3d  %s' % (n, arch))
    print('\n  Los diez mas parecidos:\n')
    for r, a, b, m in hallazgos[:10]:
        print('    %.2f  %s' % (r, m))
        print('          %s' % a)
        print('          %s' % b)
    print('\n  Esto REPORTA, no repara. Para cada par hay que decidir cual es la')
    print('  fuente y cual pasa a ser una cita: eso es juicio, y no se automatiza.\n')
    return len(hallazgos)


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    raiz = args[0] if args else '.'
    if '--parecidos' in sys.argv:
        sys.exit(0 if parecidos(args[0] if args else '.') >= 0 else 1)
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

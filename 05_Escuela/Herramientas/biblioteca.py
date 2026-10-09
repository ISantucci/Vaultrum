#!/usr/bin/env python3
"""Vaultrum - Escuela - la vista de la Biblioteca, calculada.

La Biblioteca tiene una sola fuente de verdad por libro: su propia ficha.
El estante lo enlaza y lo describe; todo lo demas -- cuantos hay, en que estado,
de que mision salio -- se calcula. Un dato calculado no puede derivar.

  python3 biblioteca.py <ruta_del_vault>              el catalogo, derivado del arbol
  python3 biblioteca.py <ruta> --verificar             ficha, estante y MISION coinciden (exit 1 si no)
  python3 biblioteca.py <ruta> --dedup <texto>         ¿ya hay algo que cubra esto?
  python3 biblioteca.py <ruta> --maduros               libros con forma de terminado y estado abierto
"""
import os, re, sys, collections

ESTANTES = [('Fundamentos', 'Fundamentos'), ('Juegos', 'Juegos'),
            ('Construccion', 'Construcción'),
            ('Fuentes', 'Fuentes'), ('Documentos', 'Documentación real')]
BASE = '05_Escuela/Biblioteca'
VOCABULARIO = ['En estudio', 'En destilación', 'En validación', 'En la Biblioteca', 'A actualizar',
               'Reservado', 'Catalogada', 'Catalogado', 'Estudiado', 'Inaccesible', 'Descartado']
CERRADOS = {'en la biblioteca', 'catalogada', 'catalogado', 'estudiado', 'descartado', 'inaccesible'}


def normalizar(e):
    """'Catalogada (pendiente de destilación)' y 'Catalogada' son el mismo estado."""
    return e.split('(')[0].strip() or '—'


def frontmatter(txt):
    if not txt.startswith('---'): return {}
    fin = txt.find('\n---', 3)
    if fin < 0: return {}
    d = {}
    for l in txt[3:fin].split('\n'):
        if ':' in l:
            k, v = l.split(':', 1)
            d[k.strip().lower()] = v.strip().strip('[]')
    return d


def cargar(raiz):
    """Devuelve {estante: [ficha, ...]} y {estante: [nombre listado en el indice, ...]}."""
    fichas, listados = {}, {}
    for carpeta, _ in ESTANTES:
        d = os.path.join(raiz, BASE, carpeta)
        if not os.path.isdir(d):
            fichas[carpeta], listados[carpeta] = [], []
            continue
        items = []
        for f in sorted(os.listdir(d)):
            if not f.endswith('.md') or f.startswith('00_'): continue
            txt = open(os.path.join(d, f), encoding='utf-8', errors='replace').read()
            fm = frontmatter(txt)
            items.append({'archivo': f[:-3], 'estado': normalizar(fm.get('estado', '—')),
                          'mision': re.sub(r'_Mision.*|_Catalogo.*', '', fm.get('mision', '—')).strip('[]'),
                          'tipo': fm.get('tipo', fm.get('familia', '—')),
                          'texto': txt})
        fichas[carpeta] = items
        idx = os.path.join(d, [x for x in os.listdir(d) if x.startswith('00_')][0]) \
            if any(x.startswith('00_') for x in os.listdir(d)) else None
        entradas = {}
        if idx:
            texto = open(idx, encoding='utf-8', errors='replace').read()
            bloques = re.split(r'^### \[\[', texto, flags=re.M)[1:]
            for b in bloques:
                nombre = b.split(']]')[0].split('|')[0].strip()
                # solo la descripcion de ESA entrada: hasta el proximo titulo, primer parrafo
                cuerpo = re.split(r'\n#{2,3} ', b.split(']]', 1)[1])[0]
                cuerpo = next((l for l in cuerpo.split('\n') if l.strip()), '')
                declarado = next((v for v in VOCABULARIO if v.lower() in cuerpo.lower()), None)
                entradas[nombre] = declarado
        listados[carpeta] = entradas
    return fichas, listados


def catalogo(fichas):
    total = sum(len(v) for v in fichas.values())
    print(f"BIBLIOTECA — {total} piezas en {len(ESTANTES)} estantes\n")
    print(f"{'ESTANTE':<18}{'piezas':>7}   estados")
    for carpeta, nombre in ESTANTES:
        items = fichas[carpeta]
        c = collections.Counter(i['estado'] for i in items)
        det = ', '.join(f"{n} {e}" for e, n in c.most_common())
        print(f"{nombre:<18}{len(items):>7}   {det}")

    print("\nPOR MISIÓN")
    mis = collections.defaultdict(list)
    for carpeta, _ in ESTANTES:
        for i in fichas[carpeta]:
            mis[i['mision']].append(f"{carpeta[:4]}/{i['archivo']}")
    for m in sorted(mis, key=lambda x: (x in ('—', ''), x)):
        v = mis[m]
        etiqueta = m if m not in ('—', '') else 'sin misión declarada'
        print(f"  {etiqueta:<28} {len(v):>3}   {', '.join(x.split('/')[1] for x in v[:4])}"
              + (' …' if len(v) > 4 else ''))

    curso = [(c, i) for c, _ in ESTANTES for i in fichas[c]
             if i['estado'].lower() not in CERRADOS and i['estado'] != '—']
    print(f"\nEN CURSO ({len(curso)}) — lo único que no se puede leer de un solo estante")
    for c, i in curso:
        print(f"  {i['estado']:<18} {c[:4]}/{i['archivo']}   ({i['mision']})")


SALIDAS = '05_Escuela/Salidas'
# Estados de MISION que dicen "esto todavia no termino".
MISION_ABIERTA = ('en estudio', 'en investigaci', 'en destilaci', 'en validaci', 'abierta')


def estado_de_mision(raiz, mision):
    """El estado que la propia mision declara en su frontmatter, o None."""
    d = os.path.join(raiz, SALIDAS)
    if not mision or mision in ('—', '') or not os.path.isdir(d):
        return None
    for f in sorted(os.listdir(d)):
        if f.startswith(mision) and f.endswith('.md'):
            fm = frontmatter(open(os.path.join(d, f), encoding='utf-8', errors='replace').read())
            return fm.get('estado')
    return None


def verificar(fichas, listados, raiz='.'):
    """Tres cruces, no dos.

    Los dos primeros comparan la ficha con su estante. El tercero pregunta algo
    que ninguno de los dos pregunta: si la MISION que produjo la ficha dice que
    todavia no termino. El lote EST-006 tuvo doce libros diciendo "En la
    Biblioteca" mientras su propia mision declaraba "En estudio -- sin AiCare,
    sin handoff", y esta herramienta contestaba EN NORMA. La ficha y el estante
    coincidian; nadie le preguntaba a la mision.
    """
    fallas = []
    for carpeta, nombre in ESTANTES:
        en_disco = {i['archivo'] for i in fichas[carpeta]}
        en_indice = set(listados[carpeta])
        declarados = listados[carpeta]
        for x in sorted(en_disco - en_indice):
            fallas.append(f"{nombre}: la ficha `{x}` existe y el estante no la enlaza")
        for x in sorted(en_indice - en_disco):
            fallas.append(f"{nombre}: el estante enlaza `{x}` y la ficha no existe")
        for i in fichas[carpeta]:
            if i['estado'] == '—':
                fallas.append(f"{nombre}: `{i['archivo']}` no declara estado en su frontmatter")
            elif i['estado'] not in VOCABULARIO:
                fallas.append(f"{nombre}: `{i['archivo']}` usa el estado «{i['estado']}», que no está en el vocabulario")
            d = declarados.get(i['archivo'])
            if d and d != i['estado']:
                fallas.append(f"{nombre}: `{i['archivo']}` — la ficha dice «{i['estado']}» y el estante dice «{d}»")
            if i['estado'].lower() in CERRADOS:
                em = estado_de_mision(raiz, i['mision'])
                if em and any(k in em.lower() for k in MISION_ABIERTA):
                    fallas.append(f"{nombre}: `{i['archivo']}` dice «{i['estado']}» y su misión "
                                  f"{i['mision']} declara «{em}» — la pieza está cerrada y la misión abierta")
    if fallas:
        print("BIBLIOTECA FUERA DE NORMA:")
        for f in fallas[:20]: print(f"  {f}")
        if len(fallas) > 20: print(f"  … y {len(fallas)-20} más")
        return 1
    total = sum(len(v) for v in fichas.values())
    print(f"BIBLIOTECA EN NORMA: {total} fichas, cada una enlazada por su estante, con estado declarado,")
    print("y ninguna cerrada por encima de una misión que se declara abierta.")
    return 0


def dedup(fichas, consulta):
    """Busca por TERMINO, no por frase entera.

    La version anterior hacia `consulta in texto`: una consulta de dos palabras
    --que es como se enuncia un gap real-- no encontraba nada aunque el libro
    existiera. `onboarding tutorial` devolvia "la mision es alta" con
    `09_Onboarding_y_tutorial` en el estante. Un guardrail que falla en la
    direccion de autorizar trabajo es peor que no tenerlo.
    """
    terminos = [x for x in re.split(r'[^0-9a-zA-ZáéíóúñüÁÉÍÓÚÑÜ]+', consulta.lower()) if len(x) > 2]
    if not terminos:
        terminos = [consulta.lower().strip()]
    hits = []
    for c, _ in ESTANTES:
        for i in fichas[c]:
            heno = (i['archivo'] + ' ' + i['texto'][:1500]).lower()
            tocados = [x for x in terminos if x in heno]
            if tocados:
                hits.append((len(tocados), c, i, tocados))
    hits.sort(key=lambda h: (-h[0], h[1], h[2]['archivo']))
    if not hits:
        print(f"nada cubre «{consulta}» todavía — la misión es alta, no actualización")
        print(f"  (se buscaron {len(terminos)} término(s): {', '.join(terminos)})")
        return 0
    plenos = [h for h in hits if h[0] == len(terminos)]
    print(f"{len(hits)} pieza(s) tocan «{consulta}»"
          + (f", {len(plenos)} con TODOS los términos" if len(terminos) > 1 else "")
          + " — evaluá si la misión es actualización:")
    for n, c, i, tocados in hits[:15]:
        marca = '**' if n == len(terminos) and len(terminos) > 1 else '  '
        print(f"{marca} {c[:4]:<5} {i['archivo']:<48} {i['estado']:<18} {n}/{len(terminos)} ({', '.join(tocados[:4])})")
    if len(hits) > 15:
        print(f"   … y {len(hits)-15} más")
    return 0


SECCIONES_DE_LIBRO = ['## CHECKLIST', '## Baseline numérico', '## Antipatrones']


def maduros(fichas):
    """Libros con forma de terminado y estado abierto.

    `--verificar` cruza la ficha contra el estante y ve el DESACUERDO. No ve el
    ACUERDO en un estado viejo: siete libros del lote EST-006 estuvieron meses
    completos --mismo esqueleto de nueve secciones que los promovidos-- diciendo
    "En estudio" en los dos lados. La ficha y el estante coincidian; el
    instrumento daba EN NORMA y los libros no se podian usar como insumo.
    """
    filas = []
    for carpeta in ('Fundamentos', 'Juegos'):
        for i in fichas.get(carpeta, []):
            if i['estado'].lower() in CERRADOS:
                continue
            faltan = [s for s in SECCIONES_DE_LIBRO if s not in i['texto']]
            filas.append((carpeta, i, faltan))
    if not filas:
        print("MADUREZ: ningún libro abierto. Nada esperando promoción.")
        return 0
    listos = [f for f in filas if not f[2]]
    print(f"MADUREZ — {len(filas)} libro(s) con estado abierto, {len(listos)} con forma de terminado\n")
    for carpeta, i, faltan in filas:
        if faltan:
            print(f"  en curso   {carpeta[:4]}/{i['archivo']:<44} {i['estado']:<14} falta: {', '.join(s[3:] for s in faltan)}")
        else:
            print(f"  FORMA OK   {carpeta[:4]}/{i['archivo']:<44} {i['estado']:<14} las {len(SECCIONES_DE_LIBRO)} secciones están")
    if listos:
        print(f"\n{len(listos)} libro(s) tienen FORMA de terminado y estado abierto.")
        print("FORMA NO ES CONTENIDO. Esta herramienta cuenta secciones; no lee lo que dicen.")
        print("Una auditoría del lote EST-006 encontró seis de siete libros con forma completa")
        print("y contradicciones internas: numeros que no cerraban ENTRE SI dentro del mismo libro.")
        print("Promover exige leer + handoff a Conocimiento + aprobación del owner.")
        print("Y son DOS escrituras: la ficha Y el índice del estante.")
    return 0


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    raiz = args[0] if args else '.'
    fichas, listados = cargar(raiz)
    if '--verificar' in sys.argv: sys.exit(verificar(fichas, listados, raiz))
    if '--maduros' in sys.argv: sys.exit(maduros(fichas))
    if '--dedup' in sys.argv:
        if len(args) < 2:
            print("uso: biblioteca.py <ruta> --dedup <texto>"); sys.exit(2)
        sys.exit(dedup(fichas, ' '.join(args[1:])))
    catalogo(fichas)

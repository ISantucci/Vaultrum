#!/usr/bin/env python3
"""Vaultrum - Escuela - la vista de la Biblioteca, calculada.

La Biblioteca tiene una sola fuente de verdad por libro: su propia ficha.
El estante lo enlaza y lo describe; todo lo demas -- cuantos hay, en que estado,
de que mision salio -- se calcula. Un dato calculado no puede derivar.

  python3 biblioteca.py <ruta_del_vault>              el catalogo, derivado del arbol
  python3 biblioteca.py <ruta> --verificar             estante y fichas coinciden (exit 1 si no)
  python3 biblioteca.py <ruta> --dedup <texto>         ¿ya hay algo que cubra esto?
"""
import os, re, sys, collections

ESTANTES = [('Fundamentos', 'Fundamentos'), ('Juegos', 'Juegos'),
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


def verificar(fichas, listados):
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
    if fallas:
        print("BIBLIOTECA FUERA DE NORMA:")
        for f in fallas[:20]: print(f"  {f}")
        if len(fallas) > 20: print(f"  … y {len(fallas)-20} más")
        return 1
    total = sum(len(v) for v in fichas.values())
    print(f"BIBLIOTECA EN NORMA: {total} fichas, cada una enlazada por su estante y con estado declarado.")
    return 0


def dedup(fichas, consulta):
    q = consulta.lower()
    hits = [(c, i) for c, _ in ESTANTES for i in fichas[c]
            if q in i['archivo'].lower() or q in i['texto'][:1200].lower()]
    if not hits:
        print(f"nada cubre «{consulta}» todavía — la misión es alta, no actualización")
        return 0
    print(f"{len(hits)} pieza(s) tocan «{consulta}» — evaluá si la misión es actualización:")
    for c, i in hits[:15]:
        print(f"  {c[:4]:<5} {i['archivo']:<48} {i['estado']}")
    return 0


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    raiz = args[0] if args else '.'
    fichas, listados = cargar(raiz)
    if '--verificar' in sys.argv: sys.exit(verificar(fichas, listados))
    if '--dedup' in sys.argv:
        if len(args) < 2:
            print("uso: biblioteca.py <ruta> --dedup <texto>"); sys.exit(2)
        sys.exit(dedup(fichas, ' '.join(args[1:])))
    catalogo(fichas)

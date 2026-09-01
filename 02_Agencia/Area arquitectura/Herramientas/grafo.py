#!/usr/bin/env python3
"""Vaultrum - Area de Arquitectura - auditoria del grafo (v2).

Mide tres ejes por cada link del vault:
  POSICION  donde vive el link dentro de la nota (titulo / linea / lista / tabla / mitad de frase / frontmatter)
  DIRECCION hacia donde apunta en el arbol de INDICES (cascada / salida / retorno / hermano / salto / sube / lateral / cruza)
  ALCANCE   si la nota se puede alcanzar caminando desde la puerta del vault

Ignora bloques de codigo y codigo en linea: Obsidian no crea aristas ahi.
Las excepciones se declaran en Herramientas/excepciones.txt, una por linea: ruta | ley | razon.
La ruta puede ser exacta o un prefijo de subarbol terminado en '/**'.

  python3 grafo.py [ruta_del_vault]              informe completo
  python3 grafo.py [ruta] --verificar            solo el veredicto (exit 1 si falla)
  python3 grafo.py [ruta] --paquete              mide el vault PUBLICADO (git ls-files)
  python3 grafo.py [ruta] --leyes                que ley cubre cada falla

El modo --paquete existe porque el gate medía la copia de trabajo y no el
paquete que se entrega: en disco todo resuelve, y en un clone se rompe lo que
apunta a un archivo gitignoreado. Ver COMMIT-005.
"""
import os,re,sys,collections

# ---------------------------------------------------------------- lexico
WL     = re.compile(r'(?<!!)\[\[([^\]\|#]+)((?:#[^\]\|]*)?)(?:\|([^\]]*))?\]\]')
MD     = re.compile(r'(?<!!)\[([^\]]*)\]\(([^)#]+\.md)(?:#[^)]*)?\)')
INLINE = re.compile(r'`[^`]*`')
FENCE  = re.compile(r'^(```|~~~)')
SALIDA = re.compile(r'hacia donde seguir|salida declarada', re.I)
PUENTE = re.compile(r'\bpuente\b', re.I)

POS = ['TITULO','titulo-mixto','LINEA','LISTA','TABLA','MEDIO','YAML']
DIR = ['cascada','salida','retorno','hermano','salto','sube','lateral','CRUZA']

POS_ILEGAL = ('TABLA','MEDIO','YAML','titulo-mixto')
DIR_ILEGAL = ('salto','sube','retorno')

LEY = {'TABLA':'Ley 6 — cero aristas invisibles',
       'YAML':'Ley 6 — cero aristas invisibles',
       'MEDIO':'Ley 4 — la prosa nombra con backticks',
       'titulo-mixto':'Ley 1 — el link es el titulo de la seccion',
       'salto':'Ley 2 — cascada de un solo escalon',
       'sube':'Ley 2 — no hay links de vuelta al padre',
       'retorno':'Ley 2 — no hay links de vuelta al indice padre (para volver esta la carpeta)',
       'puente':'Ley 5 — un puente por capa, y declarado',
       'no-viaja':'Ley 7 — el paquete no enlaza lo que no viaja',
       'flotando':'Corolario — nada flota',
       'inalcanzable':'Pregunta fundacional — se entra por un indice y se llega caminando',
       'roto':'link roto','ambiguo':'link ambiguo (nombre repetido)'}

PUERTA   = '00_START_HERE.md'
EXENTAS  = {'README.md','LICENSE.md','CONTRIBUTING.md'}
DENSIDAD = 0.40          # links por KB; el Core sano vive cerca de 0,15

# ---------------------------------------------------------------- carga
def es_indice(p):
    b = os.path.basename(p)[:-3]
    if re.match(r'^(00_|0\d_Indice|Area_)', b, re.I): return True
    if 'Indice' in b or 'Catalogo' in b: return True
    d = re.sub(r'^\d+[_\s-]+', '', os.path.basename(os.path.dirname(p)))
    return bool(d) and b.lower() == d.lower()

def cargar(root):
    files = {}
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if not d.startswith('.') and d != '_to_delete']
        for f in sorted(fn):
            if f.endswith('.md'):
                p = os.path.relpath(os.path.join(dp, f), root).replace('\\', '/')
                files[p] = open(os.path.join(dp, f), encoding='utf-8', errors='replace').read()
    return files

def cargar_paquete(root):
    """El paquete es lo que git entrega: `git ls-files`. Lo que no esta ahi no
    viaja, y un wikilink que lo apunta es un link roto para todo el que clone."""
    try:
        import subprocess
        out = subprocess.run(['git','-C',root,'ls-files','-z'],
                             capture_output=True, timeout=120)
        if out.returncode != 0: return None
        return {p.replace('\\','/') for p in out.stdout.decode('utf-8','replace').split('\0')
                if p.endswith('.md')}
    except Exception:
        return None

def cargar_excepciones(root):
    """ruta | ley | razon — una por linea. Lo que no esta aca, falla."""
    ruta = os.path.join(root, '02_Agencia', 'Area arquitectura', 'Herramientas', 'excepciones.txt')
    exc = collections.defaultdict(dict)
    if not os.path.exists(ruta): return exc
    for linea in open(ruta, encoding='utf-8', errors='replace'):
        linea = linea.split('#')[0].strip()
        if not linea or '|' not in linea: continue
        partes = [x.strip() for x in linea.split('|')]
        if len(partes) < 3: continue
        exc[partes[0].replace('\\', '/')][partes[1]] = partes[2]
    return exc

def razon_de(exc, ruta, tipo):
    """Excepcion declarada para (ruta, tipo). Acepta ruta exacta o prefijo 'carpeta/**'.

    El prefijo existe para un caso concreto: un subarbol que no se publica.
    Las leyes del grafo cuidan el vault publicado; medirlas sobre un workspace
    local es una categoria equivocada. Igual se declara, con su razon."""
    r = exc.get(ruta, {}).get(tipo)
    if r: return r
    for patron, tipos in exc.items():
        if patron.endswith('/**') and ruta.startswith(patron[:-2]):
            r = tipos.get(tipo)
            if r: return r
    return None

# ---------------------------------------------------------------- escaneo
def escanear(txt):
    """rinde (linea, posicion, destino, alias, seccion) por cada link fuera de bloques de codigo."""
    lines = txt.split('\n'); fence = None; fmend = -1; h = ''
    if lines and lines[0].strip() == '---':
        for i, l in enumerate(lines[1:], 1):
            if l.strip() == '---': fmend = i; break
    for i, l in enumerate(lines):
        s = l.strip()
        m = FENCE.match(s)
        if m:
            if fence is None: fence = m.group(1)
            elif s.startswith(fence): fence = None
            continue
        if fence is not None: continue
        if s.startswith('#'): h = re.sub(r'^#+\s*', '', s)
        l = INLINE.sub(lambda m: ' ' * len(m.group(0)), l)   # el codigo en linea no es arista
        s = l.strip()
        ms  = [(m.start(), m.group(1), m.group(3) or '') for m in WL.finditer(l)]
        ms += [(m.start(), m.group(2), m.group(1))       for m in MD.finditer(l)]
        if not ms: continue
        ms.sort()
        if 0 < i <= fmend: pos = 'YAML'
        elif s.startswith('#'):
            t = re.sub(r'^#+\s*', '', s)
            pos = 'TITULO' if re.fullmatch(r'\[\[[^\]]+\]\]', t) else 'titulo-mixto'
        elif s.startswith('|'): pos = 'TABLA'
        elif re.match(r'^([-*+]|\d+\.)\s', s): pos = 'LISTA'
        elif not l[:ms[0][0]].strip().strip('>-').strip('→»').strip(): pos = 'LINEA'
        else: pos = 'MEDIO'
        for _, t, al in ms: yield (i + 1, pos, t.strip().rstrip('\\'), al, h)

def resolver(files, stems, sufijos, t):
    """resuelve como Obsidian: ruta exacta, sufijo de ruta, o nombre unico."""
    t = t.strip().rstrip('\\').replace('\\', '/')
    if t.endswith('.md'): t = t[:-3]
    if t + '.md' in files: return t + '.md'
    if '/' in t:                                   # ruta parcial: Obsidian la resuelve por sufijo
        c = sufijos.get(t)
        if c: return c[0] if len(c) == 1 else 'AMBIGUO'
        return None
    c = stems.get(t)
    if not c: return None
    return c[0] if len(c) == 1 else 'AMBIGUO'

def capa(p): return p.split('/')[0] if '/' in p else 'RAIZ'

def direccion(a, b, dirs_con_indice):
    """La cascada se mide entre INDICES, no entre carpetas: una carpeta contenedora
    sin indice propio no agrega un escalon."""
    da, db = os.path.dirname(a), os.path.dirname(b)
    if da == db: return 'cascada' if es_indice(a) else 'hermano'
    if da == '' or db.startswith(da + '/'):
        resto = db[len(da) + 1:] if da else db
        acc = da
        for seg in resto.split('/'):
            acc = (acc + '/' + seg) if acc else seg
            idx = dirs_con_indice.get(acc, ())
            if idx and not (acc == db and b in idx):
                return 'salto'                     # habia un indice en el medio que debia enlazarlo
        return 'cascada'
    if da.startswith(db + '/'): return 'sube'
    if capa(a) != capa(b): return 'CRUZA'
    return 'lateral'

# ---------------------------------------------------------------- auditoria
def auditar(root, modo_paquete=False):
    files = cargar(root)
    exc   = cargar_excepciones(root)
    pkg   = cargar_paquete(root) if modo_paquete else None
    stems, sufijos, dirs_con_indice = {}, {}, {}
    for p in files:
        stems.setdefault(os.path.basename(p)[:-3], []).append(p)
        segs = p[:-3].split('/')
        for k in range(1, len(segs)):
            sufijos.setdefault('/'.join(segs[-k - 1:]), []).append(p)
        if es_indice(p): dirs_con_indice.setdefault(os.path.dirname(p), []).append(p)

    # QUE SE AUDITA vs CONTRA QUE SE RESUELVE -- son dos universos distintos y
    # confundirlos fue el defecto que ARQ-024 encontro en --paquete.
    #
    # Se AUDITAN las notas del paquete: son las que alguien va a clonar. Una nota
    # que no viaja no puede romper el gate del paquete, y hasta hoy lo rompia --
    # las 4 fallas que frenaban el commit estaban en 06_Proyectos/, que .gitignore
    # excluye entero. El gate del paquete frenaba por archivos que no estan en el
    # paquete: el defecto de COMMIT-005, invertido.
    #
    # Se RESUELVE contra el disco completo, a proposito. Si el universo de
    # resolucion tambien se recortara, un link a una nota que existe pero no viaja
    # resolveria a None y se reportaria como ROTO, y se perderia la distincion que
    # COMMIT-005 vino a crear: "roto" es que no existe en ningun lado; "no-viaja"
    # es que existe y no entra al paquete. Son dos defectos distintos y se arreglan
    # distinto.
    fuentes = files if pkg is None else {p: t for p, t in files.items() if p in pkg}

    r = dict(files=files, auditadas=fuentes, exc=exc, pkg=pkg, modo_paquete=modo_paquete,
             pos=collections.defaultdict(collections.Counter),
             dirn=collections.defaultdict(collections.Counter),
             kb=collections.Counter(), n=collections.Counter(),
             rotos=[], ambig=[], viol=collections.defaultdict(collections.Counter),
             detalle=collections.defaultdict(list), colgada=set(),
             cruces=collections.defaultdict(lambda: collections.defaultdict(list)),
             laterales=collections.Counter(), adj=collections.defaultdict(list))

    for p, txt in fuentes.items():
        c = capa(p); r['n'][c] += 1; r['kb'][c] += len(txt) / 1024
        for ln, ps, t, al, h in escanear(txt):
            r['pos'][c][ps] += 1
            d = resolver(files, stems, sufijos, t)
            if d is None:  r['rotos'].append((p, t, ln)); continue
            if d == 'AMBIGUO': r['ambig'].append((p, t, ln)); continue
            if pkg is not None and p in pkg and d not in pkg:
                r['viol'][p]['no-viaja'] += 1
                r['detalle'][p].append((ln, 'no-viaja', d))
            dr = direccion(p, d, dirs_con_indice)
            # Ley 2: una hoja que enlaza al indice de su propia carpeta vuelve al padre.
            # Se mide por el EFECTO (donde aterriza la arista), no por el rotulo de la
            # seccion: escribir 'Hacia donde seguir' arriba no convierte un retorno en salida.
            if (os.path.dirname(p) == os.path.dirname(d)
                    and es_indice(d) and not es_indice(p) and d != PUERTA):
                dr = 'retorno'
            elif dr != 'cascada' and SALIDA.search(h) and es_indice(d): dr = 'salida'
            r['dirn'][c][dr] += 1
            if ps in POS_ILEGAL:
                r['viol'][p][ps] += 1; r['detalle'][p].append((ln, ps, d))
            if dr in DIR_ILEGAL:
                r['viol'][p][dr] += 1; r['detalle'][p].append((ln, dr, d))
            if dr == 'CRUZA': r['cruces'][c][capa(d)].append((p, ln, d))
            if dr == 'lateral': r['laterales'][p] += 1
            if ps in ('TITULO', 'LISTA', 'LINEA', 'TABLA') and dr in ('cascada', 'hermano'):
                r['colgada'].add(d)
            if ps in ('TITULO', 'LISTA', 'LINEA') and dr != 'sube':
                r['adj'][p].append(d)

    # nada flota: toda nota cuelga de un indice
    universo = fuentes
    r['flotando'] = [p for p in universo if p not in r['colgada']
                     and not p.endswith('SKILL.md')
                     and os.path.basename(p) not in EXENTAS and p != PUERTA]

    # se llega caminando: alcanzabilidad real desde la puerta
    if PUERTA in files:
        vistas, cola = {PUERTA}, [PUERTA]
        while cola:
            for m in r['adj'].get(cola.pop(), []):
                if m not in vistas: vistas.add(m); cola.append(m)
        r['inalcanzables'] = [p for p in sorted(universo) if p not in vistas
                              and not p.endswith('SKILL.md')
                              and os.path.basename(p) not in EXENTAS]
    else:
        r['inalcanzables'] = None                  # no hay puerta: no se puede verificar

    # Ley 5: una capa enlaza a otra desde una sola nota, y esa nota lo declara
    r['puentes'] = {}
    for origen, destinos in r['cruces'].items():
        if origen == 'RAIZ': continue              # la raiz es la puerta, no un puente
        for destino, aristas in destinos.items():
            fuentes = sorted({a[0] for a in aristas})
            declara = [f for f in fuentes if PUENTE.search(files.get(f, ''))]
            r['puentes'][(origen, destino)] = (fuentes, declara, aristas)
    return r

def fallas(r):
    """Devuelve (lista_de_fallas, lista_de_excepciones_declaradas)."""
    f, ok = [], []
    exc = r['exc']
    for p, q in r['viol'].items():
        for tipo, n in q.items():
            razon = razon_de(exc, p, tipo)
            (ok if razon else f).append((p, tipo, n, razon))
    for p in r['flotando']:
        razon = razon_de(exc, p, 'flotando')
        (ok if razon else f).append((p, 'flotando', 1, razon))
    for p in (r['inalcanzables'] or []):
        razon = razon_de(exc, p, 'inalcanzable')
        (ok if razon else f).append((p, 'inalcanzable', 1, razon))
    for (o, d), (fuentes, declara, aristas) in r['puentes'].items():
        if len(fuentes) > 1 or not declara:
            f.append((f'{o} -> {d}', 'puente', len(fuentes), None))
    for p, t, ln in r['rotos']:  f.append((p, 'roto', 1, None))
    for p, t, ln in r['ambig']:  f.append((p, 'ambiguo', 1, None))
    return f, ok

# ---------------------------------------------------------------- informe
def informe(r):
    tot = sum(sum(c.values()) for c in r['pos'].values())
    inal = r['inalcanzables']
    if r.get('modo_paquete'):
        n = '?' if r.get('pkg') is None else len(r['pkg'])
        print(f"MODO PAQUETE — se AUDITAN las {n} notas que git entrega, de "
              f"{len(r['files'])} en disco. Se RESUELVE contra el disco completo, para "
              f"distinguir un link roto de uno que no viaja.")
        if r.get('pkg') is None:
            print("  (git no respondio: se midio la copia de trabajo)")
        print()
    print(f"notas {len(r.get('auditadas', r['files']))} | links {tot} | rotos {len(r['rotos'])} | "
          f"ambiguos {len(r['ambig'])} | flotando {len(r['flotando'])} | "
          f"inalcanzables {'?' if inal is None else len(inal)}")
    print()
    print(f"{'CAPA':<18}{'notas':>6}{'links':>7}" + "".join(f"{x:>12}" for x in POS))
    for c in sorted(r['pos']):
        q = r['pos'][c]; t = sum(q.values()) or 1
        print(f"{c:<18}{r['n'][c]:>6}{t:>7}" + "".join(f"{q[x]:>5}{100*q[x]/t:>6.0f}%" for x in POS))
    print()
    print(f"{'CAPA':<18}" + "".join(f"{x:>12}" for x in DIR) + f"{'l/nota':>9}{'l/KB':>7}")
    for c in sorted(r['dirn']):
        q = r['dirn'][c]; t = sum(q.values()) or 1
        dens = sum(r['pos'][c].values()) / max(r['kb'][c], 1)
        print(f"{c:<18}" + "".join(f"{q[x]:>5}{100*q[x]/t:>6.0f}%" for x in DIR)
              + f"{sum(r['pos'][c].values())/max(r['n'][c],1):>9.1f}"
              + f"{dens:>7.2f}" + ("  <-- densa" if dens > DENSIDAD else ""))

    f, ok = fallas(r)
    if f:
        print(f"\nFuera de ley ({len(f)}):")
        agr = collections.defaultdict(list)
        for p, tipo, n, _ in f: agr[tipo].append((p, n))
        for tipo in sorted(agr, key=lambda t: -sum(x[1] for x in agr[t])):
            print(f"\n  {LEY.get(tipo, tipo)}  ({sum(x[1] for x in agr[tipo])})")
            for p, n in sorted(agr[tipo], key=lambda x: -x[1])[:12]:
                extra = ""
                if tipo in ('salto', 'sube', 'retorno', 'TABLA', 'MEDIO', 'YAML',
                            'titulo-mixto', 'no-viaja'):
                    ej = [d for l, t2, d in r['detalle'].get(p, []) if t2 == tipo][:1]
                    if ej: extra = f"   ej: -> {ej[0]}"
                print(f"    {n:>3}  {p}{extra}")
    if ok:
        print(f"\nExcepciones declaradas ({len(ok)}) — estan en excepciones.txt, no fallan:")
        for p, tipo, n, razon in ok[:12]: print(f"    {n:>3}  {tipo:<14} {p}  ({razon})")

    print("\nPuentes entre capas (Ley 5):")
    for (o, d), (fuentes, declara, aristas) in sorted(r['puentes'].items()):
        estado = "OK" if len(fuentes) == 1 and declara else "FUERA DE LEY"
        print(f"  {o} -> {d}: {len(aristas)} aristas desde {len(fuentes)} nota(s)  [{estado}]")
        for x in fuentes: print(f"      {'declara puente' if x in declara else 'no declara  '}  {x}")

    lat = [(p, n) for p, n in r['laterales'].most_common() if n > 1]
    if lat:
        print(f"\nLaterales por documento (el corolario admite la cadena; >1 pide decision del owner):")
        for p, n in lat[:12]: print(f"    {n:>3}  {p}")

    for k, tit in (('rotos', 'Links rotos'), ('ambig', 'Links ambiguos (nombre repetido)')):
        if r[k]:
            print(f"\n{tit}:")
            for p, t, ln in r[k][:12]: print(f"    {p}:{ln} -> {t}")

def veredicto(r):
    f, ok = fallas(r)
    if not f:
        print(f"GRAFO EN LEY: nada flota, nada se esconde, nada se saltea, "
              f"todo se alcanza caminando. ({len(ok)} excepciones declaradas)")
        return 0
    agr = collections.Counter()
    for p, tipo, n, _ in f: agr[LEY.get(tipo, tipo)] += n
    print("GRAFO FUERA DE LEY: " + " | ".join(f"{n} {k}" for k, n in agr.most_common()))
    return 1

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    r = auditar(args[0] if args else '.', modo_paquete='--paquete' in sys.argv)
    if '--leyes' in sys.argv:
        for k, v in LEY.items(): print(f"  {k:<14} {v}")
        sys.exit(0)
    if '--verificar' in sys.argv: sys.exit(veredicto(r))
    informe(r); print(); veredicto(r)

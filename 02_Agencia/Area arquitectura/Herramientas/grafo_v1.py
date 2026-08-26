#!/usr/bin/env python3
"""Vaultrum - Area de Arquitectura - auditoria del grafo.

Mide dos ejes por cada link del vault:
  POSICION  donde vive el link dentro de la nota (titulo / linea / lista / tabla / mitad de frase / frontmatter)
  DIRECCION hacia donde apunta en el arbol (cascada / hermano / sube / lateral / cruza de capa)

Ignora bloques de codigo: Obsidian no crea aristas ahi.

  python3 grafo.py [ruta_del_vault]              informe completo
  python3 grafo.py [ruta] --verificar            solo el veredicto (exit 1 si falla)
"""
import os,re,sys,collections

WL=re.compile(r'\[\[([^\]\|#]+)((?:#[^\]\|]*)?)(?:\|([^\]]*))?\]\]')
INLINE=re.compile(r'`[^`]*`')
MD=re.compile(r'(?<!!)\[([^\]]*)\]\(([^)]+\.md)\)')
POS=['TITULO','titulo-mixto','LINEA','LISTA','TABLA','MEDIO','YAML']
DIR=['cascada','salida','hermano','sube','lateral','CRUZA']
SALIDA=re.compile(r'hacia donde seguir|salida declarada',re.I)
ILEGAL=('TABLA','MEDIO','YAML','titulo-mixto')

def es_indice(p):
    b=os.path.basename(p)[:-3]
    if re.match(r'^(00_|0\d_Indice|Area_)',b,re.I): return True
    if 'Indice' in b or 'Catalogo' in b: return True
    d=os.path.basename(os.path.dirname(p))
    d=re.sub(r'^\d+[_\s-]+','',d)          # 03_Optimizacion/Optimizacion.md tambien es indice
    return bool(d) and b.lower()==d.lower()

def cargar(root):
    files={}
    for dp,dn,fn in os.walk(root):
        dn[:]=[d for d in dn if not d.startswith('.')]
        for f in sorted(fn):
            if f.endswith('.md'):
                p=os.path.relpath(os.path.join(dp,f),root).replace('\\','/')
                files[p]=open(os.path.join(dp,f),encoding='utf-8',errors='replace').read()
    return files

def escanear(txt):
    """rinde (linea, posicion, destino, alias, seccion) por cada link fuera de bloques de codigo."""
    lines=txt.split('\n'); fence=False; fmend=-1; h=''
    if lines and lines[0].strip()=='---':
        for i,l in enumerate(lines[1:],1):
            if l.strip()=='---': fmend=i; break
    for i,l in enumerate(lines):
        s=l.strip()
        if s.startswith('```'): fence=not fence; continue
        if fence: continue
        if s.startswith('#'): h=re.sub(r'^#+\s*','',s)
        l=INLINE.sub(lambda m:' '*len(m.group(0)),l)   # el codigo en linea no es arista
        s=l.strip()
        ms=[(m.start(),m.group(1),m.group(3) or '') for m in WL.finditer(l)]
        ms+=[(m.start(),m.group(2),m.group(1)) for m in MD.finditer(l)]
        if not ms: continue
        ms.sort()
        if 0<i<=fmend: pos='YAML'
        elif s.startswith('#'):
            t=re.sub(r'^#+\s*','',s)
            pos='TITULO' if re.fullmatch(r'\[\[[^\]]+\]\]',t) else 'titulo-mixto'
        elif s.startswith('|'): pos='TABLA'
        elif re.match(r'^([-*+]|\d+\.)\s',s): pos='LISTA'
        elif not l[:ms[0][0]].strip().strip('>-').strip('\u2192\u00bb').strip(): pos='LINEA'
        else: pos='MEDIO'
        for _,t,al in ms: yield (i+1,pos,t.strip().rstrip('\\'),al,h)

def resolver(files,stems,t):
    t=t.strip().rstrip('\\').replace('\\','/')
    if t.endswith('.md'): t=t[:-3]
    if t+'.md' in files: return t+'.md'
    c=stems.get(t.split('/')[-1])
    if not c: return None
    return c[0] if len(c)==1 else 'AMBIGUO'

def capa(p): return p.split('/')[0] if '/' in p else 'RAIZ'

def direccion(a,b):
    da,db=os.path.dirname(a),os.path.dirname(b)
    if da==db: return 'cascada' if es_indice(a) else 'hermano'
    if db.startswith(da+'/') or da=='': return 'cascada'
    if da.startswith(db+'/'): return 'sube'
    if capa(a)!=capa(b): return 'CRUZA'
    return 'lateral'

def auditar(root):
    files=cargar(root); stems={}
    for p in files: stems.setdefault(os.path.basename(p)[:-3],[]).append(p)
    r=dict(files=files,stems=stems,pos=collections.defaultdict(collections.Counter),
           dirn=collections.defaultdict(collections.Counter),ind=collections.Counter(),
           rotos=[],ambig=[],viol=collections.defaultdict(collections.Counter),
           kb=collections.Counter(),n=collections.Counter(),colgada=set())
    for p,txt in files.items():
        c=capa(p); r['n'][c]+=1; r['kb'][c]+=len(txt)/1024
        for ln,ps,t,al,h in escanear(txt):
            r['pos'][c][ps]+=1
            if ps in ILEGAL: r['viol'][p][ps]+=1
            d=resolver(files,stems,t)
            if d is None: r['rotos'].append((p,t,ln)); continue
            if d=='AMBIGUO': r['ambig'].append((p,t,ln)); continue
            dr=direccion(p,d)
            if dr in ('lateral','hermano') and SALIDA.search(h) and es_indice(d): dr='salida'
            r['ind'][d]+=1; r['dirn'][c][dr]+=1
            if ps in ('TITULO','LISTA','LINEA','TABLA') and dr in ('cascada','hermano'):
                r['colgada'].add(d)
    puerta={'00_START_HERE.md','README.md','LICENSE.md'}
    r['flotando']=[p for p in files if p not in r['colgada']
                   and not p.endswith('SKILL.md') and os.path.basename(p) not in puerta]
    return r

def informe(r):
    tot=sum(sum(c.values()) for c in r['pos'].values())
    print(f"notas {len(r['files'])} | links {tot} | rotos {len(r['rotos'])} | "
          f"ambiguos {len(r['ambig'])} | flotando {len(r['flotando'])}")
    print()
    print(f"{'CAPA':<18}{'notas':>6}{'links':>7}"+"".join(f"{x:>12}" for x in POS))
    for c in sorted(r['pos']):
        q=r['pos'][c]; t=sum(q.values()) or 1
        print(f"{c:<18}{r['n'][c]:>6}{t:>7}"+"".join(f"{q[x]:>5}{100*q[x]/t:>6.0f}%" for x in POS))
    print()
    print(f"{'CAPA':<18}"+"".join(f"{x:>12}" for x in DIR)+f"{'l/nota':>9}{'l/KB':>7}")
    for c in sorted(r['dirn']):
        q=r['dirn'][c]; t=sum(q.values()) or 1
        print(f"{c:<18}"+"".join(f"{q[x]:>5}{100*q[x]/t:>6.0f}%" for x in DIR)
              +f"{sum(r['pos'][c].values())/max(r['n'][c],1):>9.1f}{sum(r['pos'][c].values())/max(r['kb'][c],1):>7.2f}")
    fuera={p:q for p,q in r['viol'].items() if capa(p)!='01_VaultrumCore'}
    core={p:q for p,q in r['viol'].items() if capa(p)=='01_VaultrumCore'}
    if fuera:
        print("\nEscritura fuera de ley (tabla / mitad de frase / frontmatter):")
        for p,q in sorted(fuera.items(),key=lambda x:-sum(x[1].values()))[:15]:
            print(f"  {sum(q.values()):>4}  {dict(q)}  {p}")
    if core:
        n=sum(sum(q.values()) for q in core.values())
        print(f"\nExcepciones del Core ({n} links en {len(core)} notas) — las decide el owner, el area no las toca:")
        for p,q in sorted(core.items(),key=lambda x:-sum(x[1].values()))[:6]:
            print(f"  {sum(q.values()):>4}  {dict(q)}  {os.path.basename(p)}")
    if r['flotando']:
        print("\nNotas flotando (ningun indice las enlaza):")
        for p in sorted(r['flotando'])[:30]: print("   ",p)
    for k,tit in (('rotos','Links rotos'),('ambig','Links ambiguos (nombre repetido)')):
        if r[k]:
            print(f"\n{tit}:")
            for p,t,ln in r[k][:12]: print(f"   {p}:{ln} -> {t}")

def veredicto(r):
    fallas=[]
    if r['flotando']: fallas.append(f"{len(r['flotando'])} notas flotando")
    _=None
    n=sum(sum(q.values()) for p,q in r['viol'].items() if capa(p)!='01_VaultrumCore')
    if n: fallas.append(f"{n} links fuera de ley")
    if r['rotos']: fallas.append(f"{len(r['rotos'])} links rotos")
    if r['ambig']: fallas.append(f"{len(r['ambig'])} links ambiguos")
    if fallas: print("GRAFO FUERA DE LEY: "+" | ".join(fallas)); return 1
    print("GRAFO EN LEY: nada flota, nada se esconde, nada esta roto."); return 0

if __name__=='__main__':
    args=[a for a in sys.argv[1:] if not a.startswith('--')]
    root=args[0] if args else '.'
    r=auditar(root)
    if '--verificar' in sys.argv: sys.exit(veredicto(r))
    informe(r); print(); veredicto(r)

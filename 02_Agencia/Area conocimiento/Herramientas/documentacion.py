#!/usr/bin/env python3
"""Vaultrum - Area de Conocimiento - medicion de la documentacion (v1).

El area afirma dos cosas sobre lo escrito: que esta completo y que se entiende.
Sin instrumento las dos son juicio. Esto las prueba donde se pueden probar, y
declara donde no.

Seis leyes de la documentacion. Ninguna se invento aca: las seis ya estaban
escritas en el vault, sueltas, sin nadie que las midiera.

  Ley 1  el artefacto declara su insumo        02_Indice Agencia (gates)
  Ley 2  la forma del contrato esta completa   RQ-008.1 (contrato de salida)
  Ley 3  una omision declarada es criterio     02_Indice Agencia (test del "no aplica")
  Ley 4  ningun numero sin fuente              Gates verificables + COMMIT-004
  Ley 5  lo terminado existe en disco          vaultrum-programador (borde de salida)
  Ley 6  no se dice dos veces                  principio 11 (no acumular) + principio 6
  Corol. el artefacto declara su estado        02_Indice Agencia (Cerrado/Ajustar/Pausado)

  python3 documentacion.py <ruta>              informe completo
  python3 documentacion.py <ruta> --verificar  solo el veredicto (exit 1 si falla)
  python3 documentacion.py <ruta> --cosecha    que se trabajo y que merece absorberse
  python3 documentacion.py --leyes             que ley cubre cada falla

Lo que NO prueba, y por eso el informe lo separa: si el texto se entiende, si el
criterio es correcto, si el aprendizaje vale. Eso sigue siendo juicio y se
declara como juicio. Un informe que presenta juicio como medicion vale menos que
uno que no mide nada.
"""
import os, re, sys, json, glob, hashlib, unicodedata, collections

TIPOS   = ('TL', 'RQ', 'GDS', 'LDS', 'UXS', 'SOL', 'EJ', 'QA', 'VE')
ART     = re.compile(r'^(' + '|'.join(TIPOS) + r')-(\d+)(?:\.(\d+))?')
FENCE   = re.compile(r'^(```|~~~)')
H2      = re.compile(r'^##\s+(.+?)\s*$')
RUIDO   = ('.git', '.obsidian', '.aicare', '.vaultrum', '__pycache__', '_to_delete', 'node_modules')

# de que artefacto cuelga cada uno (02_Indice Agencia, columna vertebral)
INSUMO  = {'RQ': ('TL',), 'GDS': ('RQ', 'TL'), 'LDS': ('GDS',), 'UXS': ('RQ', 'GDS'),
           'SOL': ('RQ', 'GDS', 'LDS', 'UXS'), 'EJ': ('SOL',), 'VE': ('TL',)}

LEY = {
    'insumo'       : 'Ley 1 - un artefacto downstream no existe sin su insumo upstream',
    'contrato'     : 'Ley 2 - falta una seccion obligatoria del contrato del tipo',
    'sin-contrato' : 'Ley 2 - el tipo no tiene forma estable medible (no falla: es el hallazgo)',
    'contrato-vacio': 'Ley 2 - una seccion del contrato existe y esta incompleta',
    'omision'      : 'Ley 3 - un "no aplica" sin decir que dimension queda ausente',
    'sin-evidencia': 'Ley 4 - afirmacion con numero y sin fuente ni instrumento',
    'fantasma'     : 'Ley 5 - se afirma un archivo del vault que no esta en disco',
    'duplicado'    : 'Ley 6 - el mismo parrafo vive en dos archivos',
    'sin-estado'   : 'Corolario - el artefacto no declara su estado de cierre',
}

# Vocabulario CANONICO de estados. Los contratos de salida de cada area lo citan;
# no lo redefinen. Antes vivia en tres lugares y los tres decian cosas distintas: el
# contrato del EJ admitia "Reportada" y "Rebotada", que aca no existian, asi que un EJ
# que cumplia su contrato podia fallar el gate. Hallazgo del adversarial review, 2026-08-28.
ESTADOS  = ('cerrado', 'cerrada', 'ajustar', 'pausado', 'descartado', 'en revision', 'abierto',
            'entregado',
            # ciclo de vida de SOL
            'propuesta', 'aprobada', 'ejecutada',
            # ciclo de vida de EJ
            'en ejecucion', 'reportada', 'rebotada')
# Secciones que ademas de existir tienen que traer sus bloques. Hoy solo el contrato
# de ejecucion, porque es el unico que habilita delegar trabajo a otro ejecutor.
SUBBLOQUES = {'contrato de ejecucion': ('archivos', 'interfaces', 'invariantes', 'prohibido')}
UNIDADES = r'(?:%|ms|fps|kb|mb|gb|px|hz|x|veces|segundos|minutos|horas|prompts|tokens|lineas|links|notas|archivos)'
NUMERO   = re.compile(r'(?<![\w.-])(\d+(?:[.,]\d+)?)\s*(' + UNIDADES + r')\b', re.I)
FUENTE   = re.compile(r'(`[^`]+`|\bmedid|\bmedic|\bsegun\b|\bfuente\b|\bconteo\b|\bestimacion\b|\ba ojo\b|'
                      r'\bdeclarad|\bTL-\d|\bEJ-\d|\bVE-\d|\bARQ-\d|\bEST-\d|\bSOL-\d|\bgrafo\b|\blegibilidad\b|'
                      r'\bdocumentacion\.py\b|\bcontar_contexto\b)', re.I)
NOAPLICA = re.compile(r'\b(no aplica|no corresponde|n/?a|sin (?:lds|uxs|nivel|interfaz))\b', re.I)
RUTA     = re.compile(r'`((?:0\d_|00_)[^`]*?\.(?:md|py|txt|json|csv))`')


def limpiar(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'[^a-z0-9 ]', ' ', s.lower())
    return re.sub(r'\s+', ' ', s).strip()


def raiz_vault(ruta):
    p = os.path.abspath(ruta)
    if os.path.isfile(p):
        p = os.path.dirname(p)
    while True:
        if os.path.exists(os.path.join(p, '00_START_HERE.md')):
            return p
        nuevo = os.path.dirname(p)
        if nuevo == p:
            return os.path.abspath(ruta if os.path.isdir(ruta) else os.path.dirname(ruta))
        p = nuevo


def cargar_contratos(raiz):
    ruta = os.path.join(raiz, '02_Agencia', 'Area conocimiento', 'Herramientas', 'contratos.txt')
    c = {}
    try:
        for linea in open(ruta, encoding='utf-8'):
            linea = linea.strip()
            if not linea or linea.startswith('#') or '|' not in linea:
                continue
            partes = [x.strip() for x in linea.split('|')]
            c[partes[0].upper()] = [limpiar(x) for x in partes[1:] if x]
    except OSError:
        pass
    return c


def cargar_excepciones(raiz):
    ruta = os.path.join(raiz, '02_Agencia', 'Area conocimiento', 'Herramientas', 'excepciones.txt')
    ex = set()
    try:
        for linea in open(ruta, encoding='utf-8'):
            linea = linea.strip()
            if not linea or linea.startswith('#') or '|' not in linea:
                continue
            partes = [x.strip() for x in linea.split('|')]
            if len(partes) >= 3 and partes[2]:
                ex.add((partes[0].replace('\\', '/'), partes[1]))
    except OSError:
        pass
    return ex


def prosa(txt):
    """Lineas de prosa: sin bloques de codigo, sin tablas, sin frontmatter."""
    fuera, dentro, yaml = [], False, False
    for i, l in enumerate(txt.splitlines(), 1):
        if i == 1 and l.strip() == '---':
            yaml = True
            continue
        if yaml:
            if l.strip() == '---':
                yaml = False
            continue
        if FENCE.match(l.strip()):
            dentro = not dentro
            continue
        if dentro or l.lstrip().startswith('|') or l.strip().startswith('>'):
            continue
        fuera.append((i, l))
    return fuera


def bases_de(rel, raiz):
    """Contra que raiz se resuelve una ruta que un artefacto afirma.

    ARQ-024 encontro que la Ley 5 acusaba fantasmas: resolvia SIEMPRE contra la
    raiz del vault, pero un RQ o un QA de proyecto escribe sus rutas relativas a
    LA CARPETA DE SU PROYECTO. Los seis "archivos que no estan en disco" existian
    todos:

        03_LevelDesign/instrumentos/sim.py        existe, dentro del proyecto
        06_Calidad/harness_mcs/ultimo_build.txt   existe, dentro del proyecto

    Un instrumento que acusa lo que si esta es peor que uno que no mide: enseña a
    ignorar su salida, y ahi se pierde tambien lo que acusaba bien.

    Se devuelven las dos bases posibles, de la mas especifica a la mas general, y
    la ruta es fantasma solo si no aparece en NINGUNA. Un artefacto de proyecto
    puede nombrar legitimamente una ruta del vault -- una herramienta, un indice --
    y eso tampoco es un fantasma.
    """
    bases = []
    segs = rel.split('/')
    if len(segs) >= 3 and segs[0] == '06_Proyectos':
        bases.append(os.path.join(raiz, segs[0], segs[1]))
    bases.append(raiz)
    return bases


def medir(rel, txt, contratos, raiz):
    m = ART.match(os.path.basename(rel))
    if not m:
        # No es un artefacto de la cadena (COMMIT, ARQ, indice, nota del Core).
        # No hay contrato que medir: se dice, no se rompe. Un instrumento que
        # revienta con un stack trace no da un veredicto: deja de contestar.
        cuerpo = '\n'.join(l for _, l in prosa(txt))
        return '-', [('sin-contrato', 0, 'no es un artefacto de la cadena: no hay contrato que medir')], cuerpo
    tipo = m.group(1)
    base = m.group(2)
    fallas = []
    lineas = prosa(txt)
    cuerpo = '\n'.join(l for _, l in lineas)
    todo   = txt

    # Ley 1 - insumo declarado
    if tipo in INSUMO:
        # el numero puede venir pegado al nombre del archivo en un wikilink
        # (TL-007_Apertura...), asi que el corte de la derecha es "no siga un digito".
        ok = any(re.search(r'\b' + p + r'-' + base + r'(?![\d])', todo) for p in INSUMO[tipo])
        if not ok:
            esperados = ' o '.join(p + '-' + base for p in INSUMO[tipo])
            fallas.append(('insumo', 0, 'no nombra su insumo (' + esperados + ')'))

    # Ley 2 - contrato de secciones
    #
    # Se mide la PRESENCIA y ademas el CUERPO. Un encabezado sin nada debajo satisface
    # "la seccion existe" y no satisface nada mas: es el mismo defecto que la Ley 1 de
    # UI/UX tenia --una declaracion que se lee como evidencia-- reproducido aca.
    # Hallazgo del adversarial review, 2026-08-28.
    cuerpos, actual = {}, None
    for l in txt.splitlines():
        m = H2.match(l)
        if m:
            actual = limpiar(m.group(1))
            cuerpos[actual] = []
        elif actual is not None:
            cuerpos[actual].append(l)

    presentes = list(cuerpos)
    if tipo not in contratos:
        fallas.append(('sin-contrato', 0, tipo + ' no tiene forma estable medida (ver contratos.txt)'))
    else:
        for sec in contratos[tipo]:
            match = [p for p in presentes if p and (sec in p or p in sec)]
            if not match:
                fallas.append(('contrato', 0, 'falta la seccion "' + sec + '"'))
                continue
            cuerpo = '\n'.join(cuerpos[match[0]]).strip()
            util = re.sub(r'[\s|`>*_#-]', '', cuerpo)
            if len(util) < 3:
                fallas.append(('contrato-vacio', 0, 'la seccion "' + sec + '" es un encabezado sin cuerpo'))
                continue
            # Secciones con estructura interna declarada: no alcanza con que existan.
            # El "Contrato de ejecucion" es el que habilita delegar un EJ a un ejecutor
            # barato; si le falta cualquiera de sus cuatro bloques, quien ejecuta tiene
            # que DECIDIR, que es justo lo que no se delega.
            for bloque in SUBBLOQUES.get(sec, ()):
                if bloque not in limpiar(cuerpo):
                    fallas.append(('contrato-vacio', 0,
                                   'la seccion "' + sec + '" no declara "' + bloque + '"'))

    # Ley 3 - omision declarada
    for n, l in lineas:
        # Un TITULO no declara nada: nombra la seccion donde se declara.
        # '## Test del "no aplica"' no es un "no aplica" sin dimension.
        if l.lstrip().startswith('#'):
            continue
        if NOAPLICA.search(l):
            resto = NOAPLICA.sub('', l).strip(' .:-—·*')
            if len(resto) < 25:
                fallas.append(('omision', n, l.strip()[:70]))

    # Ley 4 - numero sin fuente
    for n, l in lineas:
        if NUMERO.search(l) and not FUENTE.search(l):
            fallas.append(('sin-evidencia', n, l.strip()[:70]))

    # Ley 5 - rutas afirmadas que no existen, contra la raiz que corresponde
    bases = bases_de(rel, raiz)
    for n, l in lineas:
        for m in RUTA.finditer(l):
            r = m.group(1)
            if '*' in r or '?' in r:
                continue                      # un patron no es una ruta
            if not any(os.path.exists(os.path.join(b, r)) for b in bases):
                fallas.append(('fantasma', n, r))

    # Corolario - estado de cierre.
    # Solo a los artefactos que CIERRAN algo: el TL cierra la entrega planificada,
    # el EJ cierra el hilo, el VE cierra la iteracion. El estado de un GDS o un SOL
    # vive en el indice de su area, no en el artefacto: pedirselo seria inventar
    # una regla que el vault no tiene.
    if tipo in ('TL', 'EJ', 'VE'):
        bajo = limpiar(cuerpo)
        if not any(e in bajo for e in ESTADOS):
            fallas.append(('sin-estado', 0, 'no declara Cerrado / Ajustar / Pausado'))

    return tipo, fallas, cuerpo


def parrafos(cuerpo):
    for p in re.split(r'\n\s*\n', cuerpo):
        p = re.sub(r'\s+', ' ', p).strip()
        if len(p) >= 220:
            yield hashlib.sha1(limpiar(p).encode()).hexdigest()[:12], p[:60]


def recolectar(ruta):
    ruta = os.path.abspath(ruta)
    if os.path.isfile(ruta):
        return [ruta]
    out = []
    for r, d, fs in os.walk(ruta):
        d[:] = [x for x in d if x not in RUIDO and not x.startswith('.')]
        for f in sorted(fs):
            if f.endswith('.md') and ART.match(f):
                out.append(os.path.join(r, f))
    return out


def auditar(ruta):
    raiz = raiz_vault(ruta)
    contratos = cargar_contratos(raiz)
    excep = cargar_excepciones(raiz)
    res, huellas = [], collections.defaultdict(list)
    for path in recolectar(ruta):
        rel = os.path.relpath(path, raiz).replace('\\', '/')
        txt = open(path, encoding='utf-8', errors='replace').read()
        tipo, fallas, cuerpo = medir(rel, txt, contratos, raiz)
        fallas = [f for f in fallas if (rel, f[0]) not in excep]
        for h, muestra in parrafos(cuerpo):
            huellas[h].append((rel, muestra))
        res.append({'rel': rel, 'tipo': tipo, 'fallas': fallas})
    for h, donde in huellas.items():
        archivos = sorted(set(d[0] for d in donde))
        if len(archivos) > 1:
            for r in res:
                if r['rel'] == archivos[0]:
                    r['fallas'].append(('duplicado', 0, 'tambien en ' + archivos[1] + ' — "' + donde[0][1] + '..."'))
    return raiz, res, contratos, excep


# ------------------------------------------------------------------ cosecha
FRICCION = re.compile(r'remedial\s*:\s*(\d+)', re.I)


def cosecha(ruta):
    raiz = raiz_vault(ruta)
    print('COSECHA — que se trabajo y que podria absorberse\n')

    # 1. la traza: que toco Vaultrum mientras trabajaba (cuesta cero tokens)
    ev = collections.Counter()
    arts = collections.Counter()
    n = 0
    for f in glob.glob(os.path.join(raiz, '.vaultrum', 'trace', '*.jsonl')):
        for linea in open(f, encoding='utf-8', errors='replace'):
            try:
                d = json.loads(linea)
            except ValueError:
                continue
            n += 1
            ev[d.get('ev', '?')] += 1
            if d.get('art'):
                arts[d['art']] += 1
    print('Traza de operacion (.vaultrum/trace)')
    if not n:
        print('   vacia — el hook no corrio o la sesion no se abrio con `vaultrum_trace.py`')
        print('   sin traza, la cosecha depende de leer las salidas a mano: mas cara y menos honesta')
    else:
        print('   %d eventos · %s' % (n, ' · '.join('%s %d' % kv for kv in ev.most_common())))
        if arts:
            print('   artefactos tocados: ' + ', '.join('%s (%d)' % kv for kv in arts.most_common(8)))

    # 2. la friccion remedial declarada en los VE: lo que hubo que pedir dos veces
    print('\nFriccion remedial declarada en los VE')
    remediales, ves = [], 0
    for path in recolectar(raiz):
        if not os.path.basename(path).startswith('VE-'):
            continue
        ves += 1
        txt = open(path, encoding='utf-8', errors='replace').read()
        rel = os.path.relpath(path, raiz).replace('\\', '/')
        for l in txt.splitlines():
            if '→' in l and re.search(r'remedial', l, re.I):
                remediales.append((rel, l.split('→', 1)[1].strip()))
    if not ves:
        print('   no hay VE en esta ruta')
    elif not remediales:
        print('   %d VE leidos, ninguno declara remediales con detalle' % ves)
        print('   sin la lista, el numero no sirve para arreglar nada (06_Medicion de friccion)')
    else:
        for rel, t in remediales:
            print('   %-38s %s' % (rel.split('/')[-1], t[:70]))

    # 3. lo que ya esta en Staging: para no proponer dos veces lo mismo
    st = os.path.join(raiz, '02_Agencia', 'Area conocimiento', 'Staging')
    pendientes = sorted(f for f in os.listdir(st) if f.startswith('COMMIT-')) if os.path.isdir(st) else []
    print('\nYa en Staging (no se propone de nuevo)')
    print('   ' + (', '.join(pendientes) if pendientes else 'vacio — el ciclo cerro'))

    print('\nLo que esto NO decide')
    print('   si un aprendizaje vale, si es reutilizable y si entra al Core.')
    print('   Eso es criterio del Cosechador y aprobacion del owner. Esto junta la evidencia.')
    return 0


# ------------------------------------------------------------------ informe
def informe(raiz, res, contratos, excep):
    tot = collections.Counter()
    for r in res:
        for f in r['fallas']:
            tot[f[0]] += 1
    portipo = collections.Counter(r['tipo'] for r in res)
    print('artefactos %d | %s' % (len(res), ' '.join('%s %d' % kv for kv in sorted(portipo.items()))))
    print('contratos medidos: %s | sin forma estable: %s'
          % (', '.join(sorted(contratos)) or '—',
             ', '.join(t for t in TIPOS if t not in contratos) or '—'))
    duros = sum(v for k, v in tot.items() if k != 'sin-contrato')
    print('\nfallas %d (+%d artefactos de tipo sin contrato)\n' % (duros, tot['sin-contrato']))
    for clave in ('insumo', 'contrato', 'contrato-vacio', 'omision', 'sin-evidencia', 'fantasma', 'duplicado', 'sin-estado', 'sin-contrato'):
        filas = [(r['rel'], f) for r in res for f in r['fallas'] if f[0] == clave]
        if not filas:
            continue
        print('  %s  (%d)' % (LEY[clave], len(filas)))
        for rel, f in filas[:12]:
            loc = (':%d' % f[1]) if f[1] else ''
            print('      %-46s %s' % (rel.split('/')[-1] + loc, f[2]))
        if len(filas) > 12:
            print('      ... y %d mas' % (len(filas) - 12))
        print()
    if excep:
        print('  Excepciones declaradas (%d) — estan en excepciones.txt, no fallan' % len(excep))
    print('\n  Fuera del alcance de la herramienta (sigue siendo juicio):')
    print('      si el texto se entiende · si el criterio es correcto · si el aprendizaje vale')
    print('      rutas fuera del vault: las prueba el gate de existencia en disco de `vaultrum-programador`')


def veredicto(res):
    duras = [f for r in res for f in r['fallas'] if f[0] != 'sin-contrato']
    if not duras:
        print('DOCUMENTACION EN LEY')
        return 0
    c = collections.Counter(f[0] for f in duras)
    print('DOCUMENTACION FUERA DE LEY: ' + ' | '.join('%s %d' % (LEY[k].split(' - ')[1][:44], v)
                                                      for k, v in c.most_common()))
    return 1


if __name__ == '__main__':
    if '--leyes' in sys.argv:
        for k, v in LEY.items():
            print('%-14s %s' % (k, v))
        sys.exit(0)
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    ruta = args[0] if args else '.'
    if '--cosecha' in sys.argv:
        sys.exit(cosecha(ruta))
    raiz, res, contratos, excep = auditar(ruta)
    if '--verificar' in sys.argv:
        sys.exit(veredicto(res))
    informe(raiz, res, contratos, excep)
    print()
    sys.exit(veredicto(res))

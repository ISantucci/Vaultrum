#!/usr/bin/env python3
"""Vaultrum - Capa de Comunidad - formato y extraccion del post.

Una PUB publicable tiene el texto en UN SOLO bloque, los dos idiomas adentro,
separados por una linea de exactamente cinco guiones. Asi el post se copia de
una sola vez, y una maquina lo puede extraer sin interpretar nada.

  python3 post.py <PUB.md>              informe de formato
  python3 post.py <PUB.md> --texto      imprime el post listo para publicar
  python3 post.py <PUB.md> --corto      imprime la version corta
  python3 post.py <PUB.md> --verificar  solo el veredicto (exit 1 si falla)
  python3 post.py <carpeta> --todos     verifica todas las PUB de la carpeta
"""
import os, re, sys, glob

SEP_IDIOMA = '-----'      # exactamente cinco guiones, y nada mas en la linea
SEP_CIERRE = '---'        # antes del cierre de la red Vaultrumita
LIMITE_CORTO = 280

TITULO_POST   = 'Post'
TITULO_CORTO  = 'Versión corta'
TITULO_TIEMPOS = 'Los tres tiempos'
TIEMPOS = ['Problema', 'Implementacion', 'Caso de uso']   # se comparan sin acentos


def bloque(txt, titulo):
    """Devuelve el contenido del unico bloque cercado bajo '## <titulo>'."""
    secciones = re.findall(r'^##[ \t]+(.+?)[ \t]*$', txt, re.M)
    exactas = [s for s in secciones if s.strip() == titulo]
    parecidas = [s for s in secciones if s.strip() != titulo and s.strip().startswith(titulo)]
    if len(exactas) != 1:
        return None, f"esperaba un solo titulo '## {titulo}' y encontre {len(exactas)}" + (
            f" (hay {len(parecidas)} parecidos: {', '.join(parecidas)})" if parecidas else "")
    inicio = re.search(r'^##[ \t]+' + re.escape(titulo) + r'[ \t]*$', txt, re.M).end()
    resto = txt[inicio:]
    corte = re.search(r'^##[ \t]+', resto, re.M)
    seccion = resto[:corte.start()] if corte else resto
    bloques = re.findall(r'^```[^\n]*\n(.*?)^```', seccion, re.M | re.S)
    if len(bloques) != 1:
        return None, f"la seccion '{titulo}' tiene {len(bloques)} bloques cercados y debe tener exactamente 1"
    return bloques[0].rstrip('\n'), None


def sin_acentos(s):
    for a, b in zip('áéíóúÁÉÍÓÚ', 'aeiouAEIOU'): s = s.replace(a, b)
    return s


def partir(cuerpo):
    """Parte el bloque en español / ingles por la linea separadora exacta."""
    lineas = cuerpo.split('\n')
    marcas = [i for i, l in enumerate(lineas) if l.strip() == SEP_IDIOMA]
    casi = [i for i, l in enumerate(lineas)
            if l.strip() != SEP_IDIOMA and re.fullmatch(r'-{2,}', l.strip() or 'x')
            and l.strip() != SEP_CIERRE]
    if len(marcas) != 1:
        extra = f" (hay {len(casi)} lineas de guiones que no son exactamente cinco)" if casi else ""
        return None, None, f"esperaba una sola linea de exactamente cinco guiones y encontre {len(marcas)}" + extra
    es = '\n'.join(lineas[:marcas[0]]).strip()
    en = '\n'.join(lineas[marcas[0] + 1:]).strip()
    if not es: return None, None, "la mitad en español quedo vacia"
    if not en: return None, None, "la mitad en ingles quedo vacia"
    return es, en, None


def revisar(ruta):
    txt = open(ruta, encoding='utf-8', errors='replace').read()
    fallas, datos = [], {}

    cuerpo, err = bloque(txt, TITULO_POST)
    if err:
        fallas.append(f"post: {err}")
    else:
        es, en, err = partir(cuerpo)
        if err: fallas.append(f"post: {err}")
        else:
            datos['post'] = cuerpo; datos['post_es'] = es; datos['post_en'] = en
            if SEP_CIERRE not in [l.strip() for l in en.split('\n')]:
                fallas.append("post: falta la linea de cierre de tres guiones antes de la red Vaultrumita")

    cuerpo, err = bloque(txt, TITULO_CORTO)
    if err:
        fallas.append(f"corta: {err}")
    else:
        es, en, err = partir(cuerpo)
        if err: fallas.append(f"corta: {err}")
        else:
            datos['corto'] = cuerpo; datos['corto_es'] = es; datos['corto_en'] = en
            for lang, s in (('español', es), ('ingles', en)):
                n = len(' '.join(s.split()))
                datos[f'largo_{lang}'] = n
                if n > LIMITE_CORTO:
                    fallas.append(f"corta: la mitad en {lang} tiene {n} caracteres y el limite es {LIMITE_CORTO}")
    cuerpo, err = bloque(txt, TITULO_TIEMPOS)
    if err:
        fallas.append(f"tres tiempos: {err}")
    else:
        plano = sin_acentos(cuerpo).lower()
        faltan = [x for x in TIEMPOS if x.lower() not in plano]
        if faltan:
            fallas.append("tres tiempos: falta declarar " + ", ".join(faltan))
        else:
            datos['tiempos'] = cuerpo

    return fallas, datos


def informe(ruta, fallas, datos):
    print(f"{os.path.basename(ruta)}")
    if 'post_es' in datos:
        print(f"  post   español {len(datos['post_es']):>5} car | ingles {len(datos['post_en']):>5} car | separador exacto")
    if 'tiempos' in datos:
        print("  tiempos  problema, implementacion y caso de uso declarados")
    if 'corto_es' in datos:
        print(f"  corta  español {datos.get('largo_español', 0):>5} car | ingles {datos.get('largo_ingles', 0):>5} car | limite {LIMITE_CORTO}")
    for f in fallas:
        print(f"  FALLA  {f}")


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print(__doc__); sys.exit(2)
    destino = args[0]

    if '--todos' in sys.argv:
        rutas = sorted(glob.glob(os.path.join(destino, 'PUB-*.md')))
        if not rutas:
            print(f"no encontre ninguna PUB en {destino}"); sys.exit(2)
        malas = 0
        for r in rutas:
            fallas, datos = revisar(r)
            informe(r, fallas, datos)
            malas += bool(fallas)
        print()
        if malas:
            print(f"FORMATO FUERA DE NORMA: {malas} de {len(rutas)} publicaciones"); sys.exit(1)
        print(f"FORMATO EN NORMA: {len(rutas)} publicaciones, un bloque por idioma con el separador exacto"); sys.exit(0)

    fallas, datos = revisar(destino)

    if '--texto' in sys.argv or '--corto' in sys.argv:
        clave = 'post' if '--texto' in sys.argv else 'corto'
        if clave not in datos:
            print(f"no se pudo extraer el {clave}:", *fallas, sep='\n  ', file=sys.stderr); sys.exit(1)
        print(datos[clave]); sys.exit(0)

    if '--verificar' in sys.argv:
        if fallas:
            print("FORMATO FUERA DE NORMA: " + " | ".join(fallas)); sys.exit(1)
        print("FORMATO EN NORMA: un bloque, los dos idiomas, separador de cinco guiones exacto"); sys.exit(0)

    informe(destino, fallas, datos)
    print()
    sys.exit(1 if fallas else 0)

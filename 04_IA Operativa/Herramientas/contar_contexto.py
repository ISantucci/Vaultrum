#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
contar_contexto.py — Medicion real de contexto para AiCare (capa 04_IA Operativa).

Existe porque AiCare decia "medir" y en realidad estimaba a ojo. Este script
cuenta. No adivina cuanto pesa el vault: lo lee y lo suma.

Que mide, y con que precision:

  bytes / caracteres  -> EXACTO. Se leen los archivos.
  tokens              -> EXACTO si hay un tokenizador instalado (tiktoken).
                         APROXIMADO con heuristica calibrada si no lo hay.
                         El modo usado se declara en cada salida. Nunca se
                         presenta una estimacion como si fuera un conteo.

Que NO mide (declarado, no omitido):

  - El consumo real de la ventana del modelo en una conversacion. Eso lo sabe
    el runtime, no el vault. Este script mide el costo del MATERIAL que se
    carga, que es la parte que Vaultrum si controla.
  - El historial de conversacion, las instrucciones de sistema ni las salidas
    generadas. Solo mide archivos del vault.

Uso:

  # Radiografia del vault entero, por capa
  python contar_contexto.py mapa

  # Los archivos mas pesados (default 20)
  python contar_contexto.py pesados --top 30

  # Cuanto cuesta cargar un conjunto concreto (una carga real)
  python contar_contexto.py carga "01_VaultrumCore/01_Indice VaultrumCore.md" \\
                                  "05_Escuela/Biblioteca/Juegos/01_Pong.md"

  # Lo mismo, leyendo la lista de un manifiesto (un path por linea, # = comentario)
  python contar_contexto.py carga --manifiesto .aicare/carga-actual.txt

  # Comparar dos manifiestos (antes / despues de podar)
  python contar_contexto.py diff .aicare/antes.txt .aicare/despues.txt

  # Presupuesto: marca comodo / ajustado / excedido
  python contar_contexto.py carga --manifiesto .aicare/carga-actual.txt --presupuesto 40000

Salida: texto plano pensado para pegar en el bloque "Medicion" de AiCare.
Con --json devuelve el mismo dato como JSON.
"""

import argparse
import json
import os
import re
import sys

# ---------------------------------------------------------------- tokenizador

def _cargar_tokenizador():
    """Devuelve (funcion_contar, nombre_modo). Prefiere conteo exacto."""
    try:
        import tiktoken  # type: ignore
        enc = tiktoken.get_encoding("cl100k_base")
        return (lambda t: len(enc.encode(t)), "exacto (tiktoken/cl100k_base)")
    except Exception:
        pass
    return (_estimar_tokens, "aproximado (heuristica es-markdown, +-12%)")


_RE_PALABRA = re.compile(r"\w+", re.UNICODE)


def _estimar_tokens(texto: str) -> int:
    """
    Heuristica para markdown en espanol.

    Calibrada contra el vault: el espanol tokeniza peor que el ingles (acentos,
    palabras largas) y el markdown suma simbolos que casi siempre son 1 token.
    Se toma el maximo de dos estimadores para no subestimar, que es el error
    caro: subestimar hace creer que hay presupuesto donde no lo hay.
    """
    if not texto:
        return 0
    n_chars = len(texto)
    n_palabras = len(_RE_PALABRA.findall(texto))
    n_simbolos = n_chars - len(re.sub(r"[^\w\s]", "", texto))
    por_chars = n_chars / 3.6
    por_palabras = n_palabras * 1.35 + n_simbolos * 0.5
    return int(max(por_chars, por_palabras))


# ---------------------------------------------------------------- utilidades

IGNORAR_DIRS = {".git", ".obsidian", "__pycache__", ".aicare", "node_modules"}
EXTENSIONES = {".md"}


def raiz_vault(desde: str = None) -> str:
    """Sube desde este archivo hasta encontrar la raiz del vault."""
    if desde:
        return os.path.abspath(desde)
    p = os.path.abspath(os.path.dirname(__file__))
    for _ in range(6):
        if os.path.exists(os.path.join(p, "00_START_HERE.md")):
            return p
        p = os.path.dirname(p)
    return os.getcwd()


def recorrer(raiz: str):
    for dirpath, dirnames, filenames in os.walk(raiz):
        dirnames[:] = [d for d in dirnames if d not in IGNORAR_DIRS]
        for f in filenames:
            if os.path.splitext(f)[1].lower() in EXTENSIONES:
                yield os.path.join(dirpath, f)


def medir_archivo(path: str, contar):
    try:
        with open(path, encoding="utf-8") as fh:
            texto = fh.read()
    except (OSError, UnicodeDecodeError) as e:
        return {"path": path, "error": str(e), "bytes": 0, "chars": 0, "tokens": 0}
    return {
        "path": path,
        "bytes": os.path.getsize(path),
        "chars": len(texto),
        "tokens": contar(texto),
    }


def humano(n: int) -> str:
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}k"
    return str(n)


def barra(parte: int, total: int, ancho: int = 24) -> str:
    if total <= 0:
        return " " * ancho
    llenos = int(round(ancho * parte / total))
    return "#" * llenos + "." * (ancho - llenos)


# ---------------------------------------------------------------- comandos

def cmd_mapa(args, raiz, contar, modo):
    filas = [medir_archivo(p, contar) for p in recorrer(raiz)]
    por_capa = {}
    for f in filas:
        rel = os.path.relpath(f["path"], raiz)
        capa = rel.split(os.sep)[0]
        if capa.endswith(".md"):
            capa = "(raiz)"
        d = por_capa.setdefault(capa, {"archivos": 0, "tokens": 0, "bytes": 0})
        d["archivos"] += 1
        d["tokens"] += f["tokens"]
        d["bytes"] += f["bytes"]

    total_tok = sum(d["tokens"] for d in por_capa.values())
    total_arch = sum(d["archivos"] for d in por_capa.values())

    if args.json:
        print(json.dumps({"modo": modo, "total_tokens": total_tok,
                          "total_archivos": total_arch, "capas": por_capa},
                         ensure_ascii=False, indent=2))
        return

    print(f"MAPA DEL VAULT — {raiz}")
    print(f"Conteo de tokens: {modo}")
    print()
    print(f"{'capa':<28}{'archivos':>9}{'tokens':>10}{'%':>7}  reparto")
    print("-" * 84)
    for capa, d in sorted(por_capa.items(), key=lambda kv: -kv[1]["tokens"]):
        pct = 100 * d["tokens"] / total_tok if total_tok else 0
        print(f"{capa[:27]:<28}{d['archivos']:>9}{humano(d['tokens']):>10}"
              f"{pct:>6.1f}%  {barra(d['tokens'], total_tok)}")
    print("-" * 84)
    print(f"{'TOTAL':<28}{total_arch:>9}{humano(total_tok):>10}")
    print()
    print("Leer el vault entero cuesta ese total. Por eso se carga por indices.")


def cmd_pesados(args, raiz, contar, modo):
    filas = [medir_archivo(p, contar) for p in recorrer(raiz)]
    filas.sort(key=lambda f: -f["tokens"])
    top = filas[: args.top]

    if args.json:
        print(json.dumps({"modo": modo,
                          "top": [{**f, "path": os.path.relpath(f["path"], raiz)}
                                  for f in top]}, ensure_ascii=False, indent=2))
        return

    print(f"ARCHIVOS MAS PESADOS (top {args.top}) — conteo: {modo}")
    print()
    print(f"{'tokens':>8}  archivo")
    print("-" * 84)
    for f in top:
        print(f"{humano(f['tokens']):>8}  {os.path.relpath(f['path'], raiz)}")
    print()
    print("Un archivo pesado no es un problema hasta que se carga sin necesidad.")


def _leer_manifiesto(path: str):
    with open(path, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea and not linea.startswith("#"):
                yield linea


def _resolver(raiz: str, entradas):
    resueltos, faltantes = [], []
    for e in entradas:
        p = e if os.path.isabs(e) else os.path.join(raiz, e)
        if os.path.isfile(p):
            resueltos.append(p)
        else:
            faltantes.append(e)
    return resueltos, faltantes


def _medir_carga(raiz, entradas, contar):
    paths, faltantes = _resolver(raiz, entradas)
    filas = [medir_archivo(p, contar) for p in paths]
    filas.sort(key=lambda f: -f["tokens"])
    total = sum(f["tokens"] for f in filas)
    return filas, faltantes, total


def cmd_carga(args, raiz, contar, modo):
    entradas = list(args.archivos)
    if args.manifiesto:
        entradas += list(_leer_manifiesto(args.manifiesto))
    if not entradas:
        print("Nada que medir: pasa archivos o --manifiesto.", file=sys.stderr)
        return 2

    filas, faltantes, total = _medir_carga(raiz, entradas, contar)

    if args.json:
        print(json.dumps({"modo": modo, "total_tokens": total,
                          "archivos": [{"path": os.path.relpath(f["path"], raiz),
                                        "tokens": f["tokens"]} for f in filas],
                          "faltantes": faltantes,
                          "presupuesto": args.presupuesto},
                         ensure_ascii=False, indent=2))
        return 0

    print(f"CARGA MEDIDA — {len(filas)} archivos — conteo: {modo}")
    print()
    print(f"{'tokens':>8}{'%':>7}  archivo")
    print("-" * 84)
    for f in filas:
        pct = 100 * f["tokens"] / total if total else 0
        print(f"{humano(f['tokens']):>8}{pct:>6.1f}%  {os.path.relpath(f['path'], raiz)}")
    print("-" * 84)
    print(f"{humano(total):>8}         TOTAL")

    if faltantes:
        print()
        print("NO ENCONTRADOS (revisar el manifiesto):")
        for f in faltantes:
            print(f"  - {f}")

    if args.presupuesto:
        pct = 100 * total / args.presupuesto
        if pct <= 60:
            estado = "COMODO"
        elif pct <= 90:
            estado = "AJUSTADO"
        elif pct <= 100:
            estado = "AL LIMITE"
        else:
            estado = "EXCEDIDO"
        print()
        print(f"Presupuesto: {humano(args.presupuesto)} tokens")
        print(f"Usado:       {humano(total)} ({pct:.0f}%)  -> {estado}")
        if estado in ("AL LIMITE", "EXCEDIDO"):
            print()
            print("Candidatos a podar (los 3 mas pesados de esta carga):")
            for f in filas[:3]:
                print(f"  - {os.path.relpath(f['path'], raiz)} ({humano(f['tokens'])})")
            print("Antes de podar: confirmar que cada uno no sea insumo de un gate.")
    return 0


def cmd_diff(args, raiz, contar, modo):
    filas_a, falt_a, tot_a = _medir_carga(raiz, list(_leer_manifiesto(args.antes)), contar)
    filas_b, falt_b, tot_b = _medir_carga(raiz, list(_leer_manifiesto(args.despues)), contar)

    set_a = {os.path.relpath(f["path"], raiz) for f in filas_a}
    set_b = {os.path.relpath(f["path"], raiz) for f in filas_b}
    liberados = sorted(set_a - set_b)
    sumados = sorted(set_b - set_a)
    delta = tot_b - tot_a

    if args.json:
        print(json.dumps({"modo": modo, "antes": tot_a, "despues": tot_b,
                          "delta": delta, "liberados": liberados,
                          "sumados": sumados}, ensure_ascii=False, indent=2))
        return

    print(f"DIFF DE CARGA — conteo: {modo}")
    print()
    print(f"  antes:   {humano(tot_a):>8} tokens  ({len(filas_a)} archivos)")
    print(f"  despues: {humano(tot_b):>8} tokens  ({len(filas_b)} archivos)")
    signo = "+" if delta > 0 else ("-" if delta < 0 else " ")
    pct = (100 * delta / tot_a) if tot_a else 0
    print(f"  delta:   {signo}{humano(abs(delta)):>7} tokens  ({signo}{abs(pct):.0f}%)")
    if liberados:
        print()
        print("LIBERADOS:")
        for p in liberados:
            print(f"  - {p}")
    if sumados:
        print()
        print("SUMADOS:")
        for p in sumados:
            print(f"  + {p}")
    print()
    if delta < 0:
        print("Poda efectiva. Validar que ningun archivo liberado sea insumo de un gate.")
    elif delta > 0:
        print("La carga crecio. Si no fue deliberado, es acumulacion.")
    else:
        print("Sin cambio de peso.")


# ---------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Medicion real de contexto para AiCare (Vaultrum).")
    ap.add_argument("--vault", help="Raiz del vault (default: autodetecta)")
    ap.add_argument("--json", action="store_true", help="Salida en JSON")
    sub = ap.add_subparsers(dest="cmd", required=True)

    # --json y --vault se aceptan tambien despues del subcomando, porque es
    # donde la mano los escribe. Un flag que solo funciona en una posicion es
    # una trampa, no una interfaz.
    def comunes(p):
        p.add_argument("--vault", dest="vault_sub", help=argparse.SUPPRESS)
        p.add_argument("--json", dest="json_sub", action="store_true",
                       help="Salida en JSON")
        return p

    p_mapa = comunes(sub.add_parser("mapa", help="Peso del vault por capa"))

    p_pes = comunes(sub.add_parser("pesados", help="Archivos mas pesados"))
    p_pes.add_argument("--top", type=int, default=20)

    p_car = comunes(sub.add_parser("carga", help="Costo de una carga concreta"))
    p_car.add_argument("archivos", nargs="*", default=[])
    p_car.add_argument("--manifiesto", help="Archivo con un path por linea")
    p_car.add_argument("--presupuesto", type=int,
                       help="Token Budget contra el que comparar")

    p_dif = comunes(sub.add_parser("diff", help="Comparar dos manifiestos (antes/despues)"))
    p_dif.add_argument("antes")
    p_dif.add_argument("despues")

    args = ap.parse_args(argv)
    args.json = args.json or getattr(args, "json_sub", False)
    args.vault = args.vault or getattr(args, "vault_sub", None)
    raiz = raiz_vault(args.vault)
    contar, modo = _cargar_tokenizador()

    return {
        "mapa": cmd_mapa,
        "pesados": cmd_pesados,
        "carga": cmd_carga,
        "diff": cmd_diff,
    }[args.cmd](args, raiz, contar, modo) or 0


if __name__ == "__main__":
    sys.exit(main())

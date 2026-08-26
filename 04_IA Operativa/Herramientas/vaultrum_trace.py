#!/usr/bin/env python3
"""
vaultrum_trace.py — el grabador de Vaultrum.

Anota que hizo Vaultrum mientras trabaja, sin gastar contexto en anotarlo.

Lo invoca Claude Code como hook de tipo `command`: corre como proceso del CLI,
recibe el evento por stdin en JSON, y su salida NO se re-inyecta al contexto.
Por eso cuesta cero tokens.

    modo hook   python vaultrum_trace.py            (lee el evento por stdin)
    modo rol    python vaultrum_trace.py rol gd.balanceador
    modo cerrar python vaultrum_trace.py cerrar TL-004

REGLA DURA
    Si algo falla, sale con codigo 0 y no escribe nada.
    Un grabador roto no puede romper una sesion de trabajo.

Ver SOL-004.1 para el contrato completo.
"""

import json
import os
import sys
import time

MAX_BYTES = 8 * 1024 * 1024          # rota el archivo antes de que pese
RUIDO = (".vaultrum", ".git", ".obsidian", ".aicare", "node_modules", "__pycache__")

AREAS = {
    "area produccion": "produccion",
    "area game design": "gamedesign",
    "area level design": "leveldesign",
    "area ui-ux": "uiux",
    "area programacion": "programacion",
    "area conocimiento": "conocimiento",
}
PREFIJOS = ("TL-", "RQ-", "GDS-", "LDS-", "UXS-", "SOL-", "EJ-", "VE-", "EST-")

SKILLS = {
    "vaultrum-produccion": "produccion",
    "vaultrum-gamedesign": "gamedesign",
    "vaultrum-leveldesign": "leveldesign",
    "vaultrum-uiux": "uiux",
    "vaultrum-programador": "programacion",
    "vaultrum-conocimiento": "conocimiento",
    "vaultrum-escuela": "escuela",
    "vaultrum-gc": "aicare",
    "aicare": "aicare",
}


def raiz():
    """El vault es dos niveles arriba de Herramientas/."""
    aqui = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(aqui, "..", ".."))


def dir_trace():
    d = os.path.join(raiz(), ".vaultrum", "trace")
    os.makedirs(d, exist_ok=True)
    return d


def sesion_actual(nueva=None):
    p = os.path.join(raiz(), ".vaultrum", "current")
    if nueva:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(nueva)
        return nueva
    try:
        with open(p, encoding="utf-8") as f:
            return f.read().strip() or "suelta"
    except OSError:
        return "suelta"


def anotar(ev):
    """Una linea por evento. Append y nada mas."""
    sid = ev.pop("_sid", None) or sesion_actual()
    ruta = os.path.join(dir_trace(), sid + ".jsonl")
    if os.path.exists(ruta) and os.path.getsize(ruta) > MAX_BYTES:
        os.rename(ruta, ruta[:-6] + "." + str(int(time.time())) + ".jsonl")
    ev["t"] = round(time.time(), 1)
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(json.dumps(ev, ensure_ascii=False, separators=(",", ":")) + "\n")


def relativa(ruta):
    """Devuelve la ruta relativa al vault, o None si el archivo no es del vault."""
    if not ruta:
        return None
    try:
        rel = os.path.relpath(os.path.abspath(ruta), raiz())
    except (ValueError, OSError):
        return None
    if rel.startswith(".."):
        return None                                   # fuera del vault: no se registra
    rel = rel.replace("\\", "/")
    if any(part in RUIDO for part in rel.split("/")):
        return None
    return rel


def area_de(rel):
    bajo = rel.lower()
    for carpeta, clave in AREAS.items():
        if "/" + carpeta + "/" in "/" + bajo:
            return clave
    if bajo.startswith("01_vaultrumcore"):
        return "core"
    if bajo.startswith("05_escuela"):
        return "escuela"
    if bajo.startswith("03_comunidad"):
        return "comunidad"
    if bajo.startswith("04_ia operativa"):
        return "aicare"
    return None


def artefacto_de(rel):
    base = os.path.basename(rel)
    for p in PREFIJOS:
        if base.startswith(p):
            return base.split("_")[0]
    return None


def verbo(herramienta, rel):
    """Traduce una llamada a herramienta a uno de los verbos del contrato."""
    escribe = herramienta in ("Write", "Edit", "MultiEdit", "NotebookEdit")
    bajo = rel.lower()
    if escribe:
        if "/salidas/" in "/" + bajo:
            return "out"
        return "in"
    if bajo.startswith("01_vaultrumcore"):
        return "load"                                  # cargar criterio del Core
    if bajo.startswith("05_escuela/biblioteca"):
        return "study"                                 # ir a leer a la Biblioteca
    return "in"


def desde_hook():
    crudo = sys.stdin.read()
    if not crudo.strip():
        return
    ev = json.loads(crudo)
    nombre = ev.get("hook_event_name") or ""
    sid = str(ev.get("session_id") or "")[:16] or None

    if nombre == "SessionStart":
        anotar({"_sid": sesion_actual(sid or "suelta"), "ev": "wake"})
        return
    if nombre == "SessionEnd":
        anotar({"_sid": sid or sesion_actual(), "ev": "sleep"})
        return

    herramienta = ev.get("tool_name") or ""
    entrada = ev.get("tool_input") or ev.get("inputs") or {}
    if not isinstance(entrada, dict):
        return

    if herramienta == "Skill":
        nombre_skill = str(entrada.get("skill") or "").split(":")[-1].strip().lower()
        clave = SKILLS.get(nombre_skill)
        if clave:
            anotar({"_sid": sid, "ev": "in", "a": clave, "via": "skill"})
        return

    rel = relativa(entrada.get("file_path") or entrada.get("notebook_path") or entrada.get("path"))
    if not rel:
        return
    a = area_de(rel)
    if not a:
        return

    linea = {"_sid": sid, "ev": verbo(herramienta, rel), "a": a, "f": rel}
    art = artefacto_de(rel)
    if art:
        linea["art"] = art
    anotar(linea)


def main():
    try:
        if len(sys.argv) > 2 and sys.argv[1] == "rol":
            anotar({"ev": "rol", "ag": sys.argv[2]})
        elif len(sys.argv) > 2 and sys.argv[1] == "cerrar":
            anotar({"ev": "cerrar", "tl": sys.argv[2]})
        elif len(sys.argv) == 1:
            desde_hook()
    except Exception:
        pass                                           # nunca romper la sesion
    return 0


if __name__ == "__main__":
    sys.exit(main())

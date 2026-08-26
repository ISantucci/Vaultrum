#!/usr/bin/env python3
"""
instalar_trace.py — deja el grabador de Vaultrum andando.

Se corre UNA vez, desde la raiz del vault:

    python "04_IA Operativa/Herramientas/instalar_trace.py"

Que hace:
  1. crea o actualiza .claude/settings.json con los tres hooks del grabador
  2. respeta lo que ya hubiera configurado ahi (no pisa, agrega)
     y corrige el comando si quedo escrito con el interprete de otra maquina
  3. asegura que .vaultrum/ este en el .gitignore
  4. corre una prueba real y dice si el grabador quedo funcionando

Es idempotente: correrlo dos veces no duplica nada.
Ver SOL-004.1 y EJ-004.1.
"""

import json
import os
import subprocess
import sys

EVENTOS = ("SessionStart", "SessionEnd", "PostToolUse")
MATCHER = "Read|Write|Edit|MultiEdit|NotebookEdit|Skill"
MARCA = "vaultrum_trace.py"


def raiz():
    aqui = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(aqui, "..", ".."))


def comando():
    """El interprete con el que se corrio esto es el que va a andar."""
    interprete = os.path.basename(sys.executable) or "python"
    if interprete.lower().startswith("python"):
        interprete = interprete[:-4] if interprete.lower().endswith(".exe") else interprete
    else:
        interprete = "python"
    return '%s "$CLAUDE_PROJECT_DIR/04_IA Operativa/Herramientas/%s"' % (interprete, MARCA)


def hooks_del_grabador(entradas):
    """Los hooks que invocan al grabador, dentro de las entradas de un evento."""
    salida = []
    for grupo in entradas or []:
        for h in grupo.get("hooks", []):
            if MARCA in str(h.get("command", "")):
                salida.append((grupo, h))
    return salida


def instalar_hooks():
    d = os.path.join(raiz(), ".claude")
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, "settings.json")

    cfg = {}
    if os.path.exists(p):
        try:
            with open(p, encoding="utf-8") as f:
                cfg = json.load(f) or {}
        except (OSError, ValueError):
            resguardo = p + ".bak"
            os.replace(p, resguardo)
            print("  ! settings.json existia y no era JSON valido")
            print("    se guardo como settings.json.bak y se escribe uno nuevo")
            cfg = {}

    hooks = cfg.setdefault("hooks", {})
    cmd = comando()
    agregados = []
    actualizados = []
    viejo = None

    for ev in EVENTOS:
        entradas = hooks.setdefault(ev, [])
        mios = hooks_del_grabador(entradas)

        if mios:
            # Ya estaba, pero "estar" no alcanza: el comando pudo haberse
            # escrito desde otra maquina, con un interprete que en esta no
            # resuelve. Un hook mudo es peor que ningun hook, porque el mundo
            # se ve dormido con Vaultrum trabajando. Se actualiza al vuelo.
            for grupo, h in mios:
                if h.get("command") != cmd:
                    if viejo is None:
                        viejo = h.get("command")
                    h["command"] = cmd
                    if ev not in actualizados:
                        actualizados.append(ev)
                if ev == "PostToolUse" and grupo.get("matcher") != MATCHER:
                    grupo["matcher"] = MATCHER
                    if ev not in actualizados:
                        actualizados.append(ev)
            continue

        grupo = {"hooks": [{"type": "command", "command": cmd}]}
        if ev == "PostToolUse":
            grupo["matcher"] = MATCHER
        entradas.append(grupo)
        agregados.append(ev)

    with open(p, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return p, agregados, actualizados, viejo, cmd


def asegurar_gitignore():
    p = os.path.join(raiz(), ".gitignore")
    try:
        texto = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    except OSError:
        return False
    if ".vaultrum/" in texto:
        return False
    with open(p, "a", encoding="utf-8") as f:
        f.write("\n# Trace de operacion (RQ-004.1) — lo escribe el hook, no es contenido del vault\n.vaultrum/\n")
    return True


def probar():
    """Corre el grabador de verdad y confirma que dejo la linea."""
    script = os.path.join(raiz(), "04_IA Operativa", "Herramientas", MARCA)
    if not os.path.exists(script):
        return False, "no se encontro " + MARCA + " al lado de este instalador"
    destino = os.path.join(raiz(), ".vaultrum", "trace", "instalacion.jsonl")
    # No se borra el archivo previo. Hay montajes donde borrar no esta
    # permitido, y un instalador que se cae ahi miente sobre el grabador:
    # dice que fallo cuando el grabador anda. Se mide el tamano antes y
    # despues se lee solo lo que se agrego.
    antes = os.path.getsize(destino) if os.path.exists(destino) else 0
    try:
        subprocess.run(
            [sys.executable, script],
            input='{"hook_event_name":"SessionStart","session_id":"instalacion"}',
            text=True, timeout=20,
        )
    except Exception as e:
        return False, "no se pudo ejecutar el grabador: %s" % e
    if not os.path.exists(destino) or os.path.getsize(destino) <= antes:
        return False, "el grabador corrio pero no escribio el trace"
    with open(destino, "rb") as f:
        f.seek(antes)
        agregado = f.read().decode("utf-8", "replace").strip()
    if not agregado:
        return False, "el grabador corrio pero no escribio el trace"
    return True, agregado.splitlines()[-1]


def main():
    print()
    print("  Vaultrum — instalacion del grabador")
    print("  vault: " + raiz())
    print()

    p, agregados, actualizados, viejo, cmd = instalar_hooks()
    if agregados:
        print("  + hooks agregados: " + ", ".join(agregados))
    if actualizados:
        print("  ~ hooks actualizados: " + ", ".join(actualizados))
        if viejo:
            print("    antes:  " + viejo)
    if not agregados and not actualizados:
        print("  = los hooks ya estaban configurados, no se toco nada")
    print("    " + os.path.relpath(p, raiz()))
    print("    comando: " + cmd)
    print()

    if asegurar_gitignore():
        print("  + .vaultrum/ agregado al .gitignore")
    else:
        print("  = .vaultrum/ ya estaba en el .gitignore")
    print()

    ok, detalle = probar()
    if ok:
        print("  OK  el grabador funciona. Escribio:")
        print("      " + detalle)
        print()
        print("  Desde la proxima sesion de Claude Code sobre este vault,")
        print("  todo lo que haga Vaultrum queda registrado en .vaultrum/trace/")
        print("  Costo en tokens: cero. El hook corre fuera del modelo.")
    else:
        print("  FALLO  " + detalle)
        print()
        print("  El grabador no quedo andando. Nada se rompio: sin trace,")
        print("  Vaultrum funciona igual, solo que el visor no vera nada.")
    print()
    return 0 if ok else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        os._exit(0)

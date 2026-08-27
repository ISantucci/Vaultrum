#!/bin/sh
# ============================================================================
#  Vaultrum - instalador de skills            RQ-007.7 . Portabilidad
#  Equivalente de skills.bat para macOS y Linux.
#
#  Las skills VIVEN en su area. Este script las SINCRONIZA a los dos
#  directorios donde los asistentes las descubren solos. La fuente sigue
#  siendo el area; las copias NUNCA se editan a mano.
# ============================================================================
set -e
cd "$(dirname "$0")"

printf '\n  VAULTRUM - instalador de skills\n  ===============================\n\n'

if [ ! -f "00_START_HERE.md" ]; then
  echo "  [ERROR] Esto no parece la raiz de Vaultrum."
  echo "          Corre skills.sh desde la carpeta que contiene 00_START_HERE.md"
  exit 1
fi

for T in .claude/skills .agents/skills; do
  rm -rf "$T"; mkdir -p "$T"
done

N=0
find . -name SKILL.md -not -path "./.git/*" -not -path "./.claude/*" -not -path "./.agents/*" -print |
while IFS= read -r F; do
  SRC=$(dirname "$F"); NAME=$(basename "$SRC")
  for T in .claude/skills .agents/skills; do
    mkdir -p "$T/$NAME"; cp -R "$SRC/." "$T/$NAME/"
  done
  echo "  [ok] $NAME"
done
N=$(find .claude/skills -name SKILL.md | wc -l | tr -d ' ')

for T in .claude/skills .agents/skills; do
  cat > "$T/_GENERADO_NO_EDITAR.txt" <<'M'
Generado por skills.sh / skills.bat desde 02_Agencia/Area */Skills/ y las capas 03/04/05.
Editar aca no cambia el sistema: se pisa en la proxima corrida.
Para cambiar una skill, edita su fuente en el area y volve a correr el instalador.
M
done

printf '\n  %s skills sincronizadas a .claude/skills y .agents/skills\n\n' "$N"

# Presupuesto de contexto: solo name + description quedan residentes.
# Claude Code topea 1536 chars por description; Codex 8000 en total.
if command -v python3 >/dev/null 2>&1; then
  python3 - <<'PY'
import os,re,io
tot=0; mx=0; bad=[]
for root,d,f in os.walk(".claude/skills"):
    if "SKILL.md" in f:
        c=io.open(os.path.join(root,"SKILL.md"),encoding="utf-8").read()
        m=re.search(r'^description:\s*"(.*?)"\s*$',c,re.S|re.M)
        n=len(m.group(1)) if m else 0
        tot+=n; mx=max(mx,n)
        if n>1536: bad.append(os.path.basename(root))
print("  Presupuesto de contexto (solo name + description quedan residentes):")
print(f"     total residente : {tot} chars  (tope Codex 8000)")
print(f"     la mas larga    : {mx} chars  (tope Claude Code 1536)")
print("     [AVISO] pasan el tope: "+", ".join(bad) if bad else "     [ok] ninguna pasa el tope")
print("     [ok] el total entra" if tot<=8000 else "     [AVISO] el total pasa el tope de Codex")
PY
fi

printf '\n  Listo. Abri una sesion nueva para que el asistente las descubra.\n\n'

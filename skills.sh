#!/bin/sh
# ============================================================================
#  Vaultrum - instalador de skills            RQ-007.7 . Portabilidad
#  Envoltorio: la logica vive en instalar_skills.py, una sola vez, para las
#  tres plataformas. Ver el comentario de skills.bat para por que se movio.
# ============================================================================
set -e
cd "$(dirname "$0")"

SCRIPT="02_Agencia/Area arquitectura/Herramientas/instalar_skills.py"

if [ ! -f "00_START_HERE.md" ]; then
  echo "  [ERROR] Esto no parece la raiz de Vaultrum."
  exit 1
fi
if [ ! -f "$SCRIPT" ]; then
  echo "  [ERROR] No encuentro $SCRIPT"
  exit 1
fi

if command -v python3 >/dev/null 2>&1; then
  python3 "$SCRIPT" "$PWD" "$@"
elif command -v python >/dev/null 2>&1; then
  python "$SCRIPT" "$PWD" "$@"
else
  echo "  [ERROR] No encontre Python en el PATH."
  exit 1
fi

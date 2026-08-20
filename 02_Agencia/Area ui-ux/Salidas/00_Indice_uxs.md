## Índice de UI/UX Specs (UXS)

Registro de todas las specs de interfaz del Área de UI/UX.

Cada `UXS-XXX.n` es la capa de comunicación jugador↔juego diseñada y validada para un `GDS-XXX.n`.

---

## Registro

| UXS | Insumo (GDS) | Interfaz | Estado |
|-----|--------------|----------|--------|
| — | — | (sin salidas todavía) | — |

---

## Regla

- Un `UXS` cuelga siempre de un `GDS` (hereda número base y subnumeración).
- Estados posibles: En análisis / En diseño / En validación / Cerrada / Rebotada.
- Al registrar, linkear al `GDS` (y al `LDS` si aplica) y dejar el resultado de la validación.
- Un `UXS` cerrado es insumo del `SOL` del Área de Programación (junto al `GDS` y, si existe, el `LDS`).

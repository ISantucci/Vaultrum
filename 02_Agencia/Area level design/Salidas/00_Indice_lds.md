## Índice de Level Design Specs (LDS)

Registro de todas las specs de nivel del Área de Level Design.

Cada `LDS-XXX.n` es un nivel/escenario jugable diseñado y validado para un `GDS-XXX.n`.

---

## Registro

| LDS | Insumo (GDS) | Nivel | Estado |
|-----|--------------|-------|--------|
| — | — | (sin salidas todavía) | — |

---

## Regla

- Un `LDS` cuelga siempre de un `GDS` (hereda número base y subnumeración).
- Estados posibles: En análisis / En diseño / En validación / Cerrada / Rebotada.
- Al registrar, linkear al `GDS` y dejar el resultado de la validación.
- Un `LDS` cerrado es insumo del `SOL` del Área de Programación (junto al `GDS` y, si existe, el `UXS`).

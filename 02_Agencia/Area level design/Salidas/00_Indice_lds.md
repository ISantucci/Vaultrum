## Índice de Level Design Specs (LDS)

Registro de todas las specs de nivel del Área de Level Design.

Cada `LDS-XXX.n` es un nivel/escenario jugable diseñado y validado para un `GDS-XXX.n`.

---

## Registro

Todavía no hay ninguna. El primer `LDS` entra cuando un `GDS` cerrado declare que el nivel aplica.

---

## Regla

- Un `LDS` cuelga siempre de un `GDS` (hereda número base y subnumeración).
- Estados posibles: En análisis / En diseño / En validación / Cerrada / Rebotada.
- El `LDS` declara su `GDS` en su propia ficha, y el índice lo nombra. El resultado de la validación queda en el `LDS`.
- Un `LDS` cerrado es insumo del `SOL` del Área de Programación (junto al `GDS` y, si existe, el `UXS`).

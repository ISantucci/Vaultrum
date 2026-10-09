## Índice de Level Design Specs (LDS)

Registro de todas las specs de nivel del Área de Level Design.

Cada `LDS-XXX.n` es un nivel/escenario jugable diseñado y validado para un `GDS-XXX.n`.

---

## Registro

Los artefactos de un proyecto **no se registran acá**. Viven en la carpeta del proyecto, en `06_Proyectos/<Proyecto>/03_LevelDesign/`, y se listan en el cuaderno de ese proyecto.

Este índice es el **contrato de salida** del área: qué produce, qué forma tiene, cómo se numera y cuándo está cerrado. No es un archivo.

> Entrada a los proyectos: `00_Proyectos`. Por qué dejaron de vivir acá: `TL-008_La_Agencia_Es_La_Empresa`.

## Regla

- Un `LDS` cuelga siempre de un `GDS` (hereda número base y subnumeración).
- Estados posibles: En análisis / En diseño / En validación / Cerrada / Rebotada.
- El `LDS` declara su `GDS` en su propia ficha, y el índice lo nombra. El resultado de la validación queda en el `LDS`.
- Un `LDS` cerrado es insumo del `SOL` del Área de Programación (junto al `GDS` y, si existe, el `UXS`).

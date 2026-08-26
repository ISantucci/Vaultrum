## Índice de UI/UX Specs (UXS)

Registro de todas las specs de interfaz del Área de UI/UX.

Cada `UXS-XXX.n` es la capa de comunicación entre el sistema y quien lo opera, diseñada para un hilo de trabajo y **medida** antes de cerrarse.

---

## Los tres modos

| Modo | Qué registra | Cuándo |
|------|--------------|--------|
| Presupuesto | cuánto se puede comunicar, por qué canal, con qué techo | antes de que Game Design cierre el `GDS` |
| Interfaz | pantallas, jerarquía, mapping, feedback y accesibilidad, instrumentados | con el `GDS` cerrado |
| Pasada | una medición sobre una interfaz que ya existe | cuando hay que revisar lo que ya está |

---

## Las dos mitades de un UXS

Un `UXS` no empieza cuando el `GDS` termina. Tiene dos mitades y dos cierres:

```txt
Mitad A — Presupuesto   con el RQ en la mano, antes de que el GDS cierre
Mitad B — Interfaz      con el GDS cerrado, medida con la herramienta
```

Un `UXS` que arranca directo en la mitad B es válido y se declara: significa que el sistema se cerró sin presupuesto. Es deuda, no error, y queda escrita en la ficha.

---

## Registro

Los artefactos de un proyecto **no se registran acá**. Viven en la carpeta del proyecto, en `06_Proyectos/<Proyecto>/04_UI-UX/`, y se listan en el cuaderno de ese proyecto.

Este índice es el **contrato de salida** del área: qué produce, qué forma tiene, cómo se numera y cuándo está cerrado. No es un archivo.

> Entrada a los proyectos: `00_Proyectos`. Por qué dejaron de vivir acá: `TL-008_La_Agencia_Es_La_Empresa`.

## Primera medición del área

Las dos specs se escribieron antes de que existiera `legibilidad.py`. Medidas por primera vez, el resultado es **rojo**, y eso es la noticia: tres hallazgos que dos lecturas cuidadosas no habían visto.

| Dónde | Ley | Hallazgo |
|-------|-----|----------|
| `UXS-003.5`, `Options` | Ley 5 | `↑` y `↓` mueven el cursor y no están escritas en pantalla (dos fallas) |
| `UXS-003.5`, estructura | Ley 2 | `#2A3040` sobre `#10131C` da 1,41:1, por debajo del mínimo de 3:1 |

Y una afirmación que hasta ahora era solo una afirmación quedó probada: el par cian/naranja de `UXS-003.7` **sobrevive** a la simulación de protanopia, deuteranopia y tritanopia y a la escala de grises.

Ninguno de los tres hallazgos se corrigió: las dos specs ya bajaron a `EJ-003` y tocarlas ahora abriría una diferencia entre lo escrito y lo construido. Son decisión del owner.

---

## Regla

- Un `UXS` cuelga de su `RQ` en la mitad A y de su `GDS` en la mitad B, y declara cada insumo en su línea rotulada.
- La numeración se hereda del hilo: `RQ-004.5 → GDS-004.5 → UXS-004.5`.
- Estados posibles: En presupuesto / En análisis / En diseño / En validación / Cerrada / Rebotada.
- Un `UXS` no cierra sin estar instrumentado: una spec que no se puede medir no se puede validar.
- El veredicto de cierre lo da `legibilidad.py --verificar`, no una lectura.
- Toda excepción vive en `Herramientas/excepciones.txt` con su razón escrita.
- Un `UXS` cerrado es insumo del `SOL` del Área de Programación, junto al `GDS` y, si existe, el `LDS`.

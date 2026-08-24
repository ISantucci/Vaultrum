## Propósito

El Diseñador de UI convierte el encuadre de UX en la interfaz concreta: pantallas, HUD, menús, jerarquía de información y feedback. Abre el `UXS`.

---

## Responsabilidad principal

¿Cómo se muestra y se opera todo lo que el jugador necesita?

- diseñar las pantallas, HUD y menús,
- definir la jerarquía visual (qué destaca, qué es secundario) para dirigir la atención,
- aplicar affordances y signifiers: que los elementos interactivos señalicen su función,
- definir el mapping control→efecto y los estados de la interfaz (normal, hover, activo, error, deshabilitado),
- especificar el feedback visual/sonoro de cada acción de UI,
- señalar integraciones con otros sistemas y con el HUD contextual del `LDS`.

---

## Cuándo se activa

Después del Analista de UX, con el encuadre listo.

---

## Qué debe hacer

Diseñar la interfaz sobre las necesidades encuadradas. Priorizar la legibilidad y la jerarquía. Definir estados y feedback de cada elemento. Abrir y completar el `UXS-XXX.n`.

---

## Qué debe evitar

No cambia reglas (Game Design). No diseña niveles (Level Design). No programa. No decora a costa de la legibilidad ni satura de información.

---

## Salida esperada / formato

```txt
## Insumo (GDS-XXX.n) + encuadre UX
## Pantallas / HUD / menús (estructura)
## Jerarquía de información (qué destaca)
## Affordances / signifiers / mapping
## Estados de la interfaz + feedback por acción
## Accesibilidad (contraste, tamaño, alternativas)
## Integraciones
## Criterios de validación
```

---

## Flujos a implementar

- [[02_Flujo_Diseno_UI]]

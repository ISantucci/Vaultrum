## Propósito

Esta sección organiza los conceptos relacionados con cómo un NPC se desplaza dentro del espacio del juego.

Movimiento no es lo mismo que decisión.

La decisión define qué quiere hacer el NPC.

El comportamiento solicita una acción.

El movimiento ejecuta el desplazamiento.

```txt
Decisión
→ define intención.

Comportamiento
→ solicita acción.

Movimiento
→ ejecuta desplazamiento.
```

---

## Responsabilidad de esta sección

La responsabilidad de esta sección es ordenar las formas en que un NPC puede moverse, ajustar su trayectoria o consumir información de navegación.

Movimiento debe responder:

```txt
¿Cómo se desplaza el NPC?
¿Cómo sigue un objetivo?
¿Cómo evita obstáculos?
¿Cómo consume una ruta calculada?
¿Cómo ejecuta físicamente una intención?
```

Movimiento no debería decidir por qué el NPC se mueve.

Tampoco debería absorber percepción, toma de decisiones, combate o pathfinding completo.

---

## [[Steering Behaviours]]

Agrupa técnicas de movimiento que permiten dirigir un agente mediante fuerzas, direcciones o tendencias de desplazamiento.

Sirve cuando el NPC necesita moverse de forma más suave, reactiva u orgánica.

Esta nota responde principalmente:

```txt
¿Cómo transformo una intención de movimiento en una dirección o fuerza deseada?
```

---
## [[Flocking]]

Agrupa criterios y técnicas para coordinar movimiento grupal mediante reglas locales entre agentes.

Sirve cuando varios NPCs o entidades deben moverse de forma orgánica sin superponerse, amontonarse o dispersarse sin control.

Esta nota responde principalmente:

```
¿Cómo coordino movimiento grupal local entre varios agentes?
```

---

## [[Obstacle Avoidance]]

Agrupa criterios y técnicas para evitar obstáculos locales durante el desplazamiento.

Sirve cuando el NPC necesita ajustar su trayectoria para no chocar, trabarse o atravesar elementos cercanos.

Esta nota responde principalmente:

```txt
¿Cómo evito obstáculos locales mientras el NPC intenta moverse?
```

---

## [[Integracion con Pathfinding]]

Explica cómo un NPC puede consumir rutas calculadas por un sistema de pathfinding sin absorber la lógica del algoritmo.

Sirve cuando el NPC necesita seguir una ruta generada por otro sistema.

Esta nota responde principalmente:

```txt
¿Cómo usa el NPC una ruta sin convertirse en el sistema de pathfinding?
```

---

## Regla final

Movimiento ejecuta desplazamiento.

No decide por qué el NPC se mueve.

No calcula toda la navegación del mapa.

No reemplaza comportamiento.

Primero intención.

Después desplazamiento.
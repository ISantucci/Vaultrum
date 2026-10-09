## Propósito

Esta sección organiza los sistemas que permiten que un NPC elija qué hacer según la información disponible, su rol dentro del juego y el contexto actual.

Toma de decisiones no es percepción.

Toma de decisiones no es comportamiento.

Toma de decisiones no es movimiento.

La relación base es:

```txt
Percepción
→ entrega información.

Toma de decisiones
→ interpreta información y elige.

Comportamiento
→ ejecuta la acción elegida.
```

La toma de decisiones no debe absorber percepción, movimiento ni comportamiento completo.

---

## Responsabilidad de esta sección

La responsabilidad de esta sección es ordenar formas concretas de decidir.

Debe ayudar a responder:

```txt
¿Qué debería hacer el NPC ahora?
¿Qué información necesita para decidir?
¿Qué método de decisión conviene?
¿Cómo se evita mezclar decisión con ejecución?
```

Cada método de decisión debe tener una responsabilidad clara.

No todos los NPCs necesitan el mismo sistema.

Un NPC simple puede resolverse con una condición directa.

Un NPC con modos claros puede usar estados.

Un NPC con preguntas ordenadas puede usar árboles de decisión.

Un NPC con varias opciones válidas puede usar selección ponderada.

Un NPC que necesita planificar pasos para alcanzar un objetivo puede usar GOAP.

---

## [[Estados de NPC]]

Organizan el comportamiento de un NPC en modos claros, como patrullar, perseguir, atacar, investigar o huir.

Sirven cuando el NPC puede describirse mediante estados activos y transiciones entre esos estados.

Esta nota responde principalmente:

```txt
¿Qué modo está activo ahora y cuándo cambia?
```

---

## [[Arboles de decision]]

Permiten evaluar condiciones en forma ordenada para elegir una acción.

Sirven cuando la decisión puede expresarse como una secuencia clara de preguntas sobre el contexto.

Esta nota responde principalmente:

```txt
¿Qué acción conviene según estas condiciones?
```

---

## [[Seleccion ponderada]]

Permite elegir entre varias opciones usando pesos, probabilidades o prioridades relativas.

Sirve cuando hay varias opciones válidas y se busca variedad controlada o prioridad variable.

Esta nota responde principalmente:

```txt
¿Qué opción conviene elegir entre varias posibilidades válidas?
```

---

## [[GOAP]]

Permite planificar una secuencia de acciones para alcanzar un objetivo a partir de precondiciones, efectos y estado del mundo.

Sirve cuando el NPC no solo debe elegir una acción inmediata, sino construir un plan con varios pasos posibles.

Esta nota responde principalmente:

```txt
¿Qué secuencia de acciones permite alcanzar este objetivo?
```

---

## Regla final

Decidir no es ejecutar.

La decisión elige.

El comportamiento actúa.

El movimiento desplaza.

Primero se entiende qué debe decidir el NPC.

Después se elige el método más simple que resuelva esa decisión.
## Propósito

Esta sección organiza los conceptos relacionados con cómo un NPC recibe información del mundo.

La percepción permite que un NPC detecte estímulos, objetivos, amenazas o cambios del entorno.

```txt
Percepción
→ recibe información
→ expone datos
→ alimenta decisiones
```

La percepción no decide por sí sola.

---

## Responsabilidad de esta sección

La responsabilidad de esta sección es ordenar las formas en que un NPC puede obtener información útil del mundo.

Debe ayudar a responder:

```txt
¿Qué puede percibir el NPC?
¿Qué información recibe?
¿Qué estímulo detecta?
¿Qué dato expone a otros sistemas?
¿Cómo se evita mezclar percepción con decisión?
```

La percepción debe informar.

No debe decidir comportamiento.

No debe ejecutar acciones.

No debe mover al NPC.

---

## [[Field of View]]

Técnica de percepción visual que permite saber si un objetivo está dentro del rango, ángulo y línea de visión del NPC.

Sirve cuando la dirección visual del NPC importa para el gameplay.

Esta nota responde principalmente:

```txt
¿Qué puede ver el NPC?
```

---

## [[Deteccion del jugador]]

Aplicación concreta de percepción orientada a saber si el jugador fue detectado por distancia, visión, evento, daño, zona u otro estímulo.

Sirve cuando el jugador debe modificar el comportamiento posible del NPC.

Esta nota responde principalmente:

```txt
¿El NPC tiene información suficiente para considerar detectado al jugador?
```

---

## Regla final

La percepción informa.

La decisión interpreta.

El comportamiento actúa.

La percepción no debe convertirse en decisión ni en ejecución.
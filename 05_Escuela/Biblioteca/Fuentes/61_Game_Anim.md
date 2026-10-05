---
tipo: fuente
titulo: "Game Anim: Video Game Animation Explained"
autores: Jonathan Cooper
editorial: A K Peters / CRC Press
anio: 2019 (2.ª ed. CRC Press, 2021)
estado: Catalogada (pendiente de destilación)
mision: EST-020_Mision_Mapa_Territorio_Arte
temas: animación de juego, respuesta vs fidelidad, anticipación vs lag de input, ventanas de cancelación, in place vs root motion, máquinas de estado, rigs para juego
apunta_a: Principios de animacion · Claves por tipo de animacion · Huesos e influencias · Rigging y skinning
---

# Fuente 61 — Game Anim

> Libro-fuente externo, del propio campo. Es la traducción de los principios de cine a un medio donde el jugador puede interrumpir cualquier cuadro.
> **IP:** conceptos + cita, nunca texto verbatim con copyright.

## Cita

Cooper, J. (2019). *Game Anim: Video Game Animation Explained*. A K Peters / CRC Press. ISBN 978-1-138-09487-1. Segunda edición: CRC Press, 2021, ISBN 978-0-367-70765-1.

## Qué es (marco aprendido)

Un director de animación con carrera en producción de gran escala escribe el manual que le faltaba al oficio: qué cambia cuando la animación responde a un control. Cinco ideas transferibles:

1. **Respuesta contra fidelidad.** Cada cuadro de anticipación es un cuadro entre el botón y la acción. En juego la anticipación se acorta al mínimo y el peso se muda a la recuperación, después de que la acción ya ocurrió. El principio de cine sigue valiendo; cambia dónde se lo paga.
2. **Ventanas de cancelación.** Una animación de juego se divide en tramos donde el jugador puede o no interrumpirla. Dónde se abren esas ventanas define si un ataque se siente ágil o comprometido, y es una decisión de diseño tanto como de animación.
3. **In place o root motion.** La animación puede quedarse en el lugar y que el código mueva al personaje, o llevar el desplazamiento en el hueso raíz y que el motor lo lea. Lo primero le da el control al diseño; lo segundo da fidelidad (pies que no patinan). Es una decisión técnica con consecuencias de game feel.
4. **Nada se ve solo.** Una animación de juego se ve entrando y saliendo de otras: máquinas de estado, blends, ciclos que empalman. La transición es parte de la pieza.
5. **El rig está acotado por el motor.** Cantidad de huesos, influencias por vértice y jerarquía exportable los fija lo que el juego puede evaluar en tiempo real, no lo que permite la herramienta de modelado.

## Por qué le sirve a Vaultrum (a qué apunta)

- **`Principios de animacion`**: es la fuente de **la especificación de juego** que cada principio lleva junto a su versión de cine (`59_The_Illusion_of_Life`).
- **`Claves por tipo de animacion`**: reposo, locomoción, ataque, golpe recibido, muerte — cada tipo con su propio compromiso entre respuesta y fidelidad.
- **`Huesos e influencias`**: el presupuesto de rig como restricción del motor.
- **`Rigging y skinning`** (IA Operativa): qué tiene que salir de la herramienta de modelado para que el motor lo lea sin sorpresas.

## Límites declarados

Está escrito desde la producción 3D de gran escala: equipos, captura de movimiento, herramientas propias de cada estudio. Lo de sprites 2D aparece poco. Lo que dice de presupuestos técnicos depende de plataforma y motor: se toma como criterio, no como cifra. Las cifras de Vaultrum salen de medir, no de esta fuente.

## Estado y próximos pasos

- **Catalogada**, pendiente de destilación.
- Cierra el trío de animación de `EST-020`: `59_The_Illusion_of_Life` da el principio, `60_The_Animators_Survival_Kit` el oficio, y esta fuente la especificación de juego.

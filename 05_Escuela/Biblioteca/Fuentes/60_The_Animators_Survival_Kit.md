---
tipo: fuente
titulo: "The Animator's Survival Kit"
autores: Richard Williams
editorial: Faber and Faber
anio: 2009 (edición ampliada; orig. 2001)
estado: Catalogada (pendiente de destilación)
mision: EST-020_Mision_Mapa_Territorio_Arte
temas: timing y espaciado, claves, breakdowns e intermedios, cartas de timing, caminata y carrera, peso
apunta_a: 09 - Timing · 04 - Pose a pose y accion directa · 06 - Entradas y salidas suaves · Curvas e interpolacion · RA-011_Locomocion_por_apoyos
---

# Fuente 60 — The Animator's Survival Kit

> Libro-fuente externo: el manual de oficio de animación más usado. No explica qué es la animación; explica cómo se hace, cuadro por cuadro.
> **IP:** conceptos + cita, nunca texto verbatim con copyright.

## Cita

Williams, R. (2009). *The Animator's Survival Kit* (edición ampliada). Faber and Faber. ISBN 978-0-571-23834-7. Primera edición: Faber and Faber, 2001.

## Qué es (marco aprendido)

El director de animación de *Who Framed Roger Rabbit* reúne en un manual lo que aprendió de los animadores de la época dorada. Cuatro ideas transferibles:

1. **Timing y espaciado son dos variables, no una.** El timing es cuántos cuadros dura una acción; el espaciado es cómo se reparten las posiciones dentro de esos cuadros. Dos movimientos con el mismo timing se sienten distintos por su espaciado: posiciones juntas leen lento, separadas leen rápido. Animar con un dibujo por cuadro o con uno cada dos cambia además la textura del movimiento.
2. **Jerarquía de poses: claves, extremos, breakdowns, intermedios.** Las claves cuentan la historia; el breakdown decide *cómo* se pasa de una a otra (por qué arco, con qué peso); los intermedios solo rellenan. El breakdown es donde vive la personalidad del movimiento.
3. **La carta de timing.** Una pequeña escala anotada junto a la clave dice cuántos intermedios van y dónde se apiñan. Es una curva de aceleración escrita a mano.
4. **La caminata como caídas controladas.** Se descompone en contacto, recepción, paso y elevación: el cuerpo cae sobre el pie que apoya y se levanta sobre el que empuja. La carrera es la variante en la que hay cuadros sin ningún apoyo. El peso se lee en cuánto y cuándo baja la cadera.

## Por qué le sirve a Vaultrum (a qué apunta)

- **`09 - Timing`**: la distinción entre timing y espaciado es la base de la nota.
- **`04 - Pose a pose y accion directa`**: la jerarquía clave-breakdown-intermedio es el método de pose a pose hecho operativo.
- **`06 - Entradas y salidas suaves`**: lo que la carta de timing dibuja es exactamente una entrada y una salida.
- **`Curvas e interpolacion`**: en un motor o en una herramienta 3D el intermedio lo genera la interpolación. La carta de timing es la curva de animación antes de que existiera el editor de curvas; leer una ayuda a leer la otra.
- **`RA-011_Locomocion_por_apoyos`**: la regla del Área de Arte que construye la locomoción sobre los contactos con el piso tiene acá su análisis de origen.

## Límites declarados

Es animación dibujada, pensada para cine a 24 cuadros por segundo. En un juego el intermedio lo calcula el motor y la tasa de cuadros no es fija: la carta de timing se traduce en curvas y en duraciones, no en dibujos. No trata respuesta al input, ciclos que tienen que empalmar con la velocidad real del personaje, ni root motion; eso es de `61_Game_Anim`.

## Estado y próximos pasos

- **Catalogada**, pendiente de destilación.
- Pieza del medio del trío de animación de `EST-020`: entre el principio (`59_The_Illusion_of_Life`) y su especificación de juego (`61_Game_Anim`).

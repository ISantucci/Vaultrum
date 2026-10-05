## Definición

La **silueta** es la forma de algo rellena de un solo color. Una silueta es **legible** cuando, rellena de negro y a la escala de pantalla real, todavía dice qué es —y qué está haciendo—.

---

## Idea central

```txt
el jugador decide por la silueta antes que por el detalle
a la distancia de juego, el detalle no existe; la silueta, si
```

Es la prueba más barata y más dura de un diseño: si dos enemigos tienen casi la misma silueta, el jugador los confunde aunque tengan colores y texturas distintos.

---

## Especificación para videojuegos

```txt
cada familia, su silueta      lo que el jugador tiene que distinguir se distingue en negro
la accion tambien             una pose de ataque y una de espera del mismo enemigo tienen
                              siluetas distintas (Puesta en escena, Anticipacion)
a la escala real              se prueba al tamano que tiene en pantalla, no en el visor
                              del DCC a pantalla completa
desde la camara real          un juego cenital lee la silueta desde arriba
las caras van a la silueta    en un asset de pocas caras, el contorno es donde se gastan
                              (Low poly)
```

---

## Cómo se juzga

```txt
se mide     render de la silueta en negro sobre blanco a la escala de pantalla, y la
            superposicion entre las siluetas de dos familias: cuanto mas se superponen,
            mas se confunden. Como lo hace la IA esta en Legibilidad (IA Operativa)
se juzga    si la silueta dice que es, sin el color
```

No hay un umbral universal de superposición: se compara contra las demás familias del mismo juego.

---

## Errores comunes

```txt
Distinguir dos enemigos por el color de la ropa.
Disenar la silueta de frente para un juego lateral.
Llenar de detalle interno un asset cuya silueta no se lee.
Brazos dentro del contorno del torso en la pose que importa.
```

---

## Fuentes

- `64_Creating_Characters_with_Personality` — la silueta como prueba del diseño.
- `51_Understanding_Comics` — la lectura de una forma simple.
- Área de Arte: `RA-003_Medidas_y_proporcion` y el rol del `05_Guardian_Visual`.

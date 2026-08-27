---
tipo: fuente
titulo: "A Composer's Guide to Game Music"
autores: Winifred Phillips
editorial: MIT Press
anio: 2014
estado: Catalogada (pendiente de destilación)
mision: EST-009_Mision_Fuentes_Huerfanas
temas: música de juego en la práctica, música adaptativa por capas, loops, integración con el estado del juego
apunta_a: 16_Audio_como_gameplay · 12_Pacing_y_estructura
---

# Fuente 56 — A Composer's Guide to Game Music

> Libro-fuente externo. **Mitad práctica del par de audio**, junto con `39_Game_Sound`.
> **IP:** conceptos + cita, nunca texto verbatim con copyright.

## Cita

Phillips, W. (2014). *A Composer's Guide to Game Music*. MIT Press. ISBN 978-0-262-53449-9.

## Qué es (marco aprendido)

Escrito por una compositora en activo, es el manual práctico de cómo se hace música que **funciona dentro de un sistema interactivo**. Su tema central es la música adaptativa y sus dos técnicas dominantes:

```txt
por capas (vertical)      capas que entran y salen según el estado; siempre sonando, cambia la densidad
por secuencia (horizontal) segmentos que se encadenan en puntos de transición musicalmente válidos
```

Y el problema que ninguna partitura lineal tiene: **una pieza que se repite tiene que poder repetirse cien veces sin cansar**, lo que cambia cómo se compone, no solo cómo se implementa.

## Por qué le sirve a Vaultrum (a qué apunta)

`16_Audio_como_gameplay` (*En estudio*) ya propone en su sección de aplicación "música por capas con N `AudioSource` sincronizados por `PlayScheduled` y cross-fade" — es decir, **ya recomienda la técnica sin tener una sola fuente de audio que la respalde**. Esta la respalda, y `39_Game_Sound` da la teoría debajo.

Cruza con `12_Pacing_y_estructura`: la música adaptativa es la curva de intensidad hecha audible, y es la forma más barata de que un dev solo la comunique.

## Límites declarados

Está escrito para compositores. Se destila el **criterio de diseño** (cuándo por capas y cuándo por secuencia, qué hace que un loop no canse), no la técnica de composición ni de orquestación.

## Estado y próximos pasos

- **Catalogada**, pendiente de destilación.
- Va en par con `39_Game_Sound`: se destilan juntas o no se destilan.

---
tipo: fuente
titulo: "Game Feel: A Game Designer's Guide to Virtual Sensation"
autores: Steve Swink
editorial: CRC Press / Morgan Kaufmann
anio: 2008
estado: Estudiado (destilada — alimentó 02_Game_feel)
mision: EST-023_Mision_Swink_Game_Feel
temas: game feel, control en tiempo real, juice, respuesta percibida, umbrales de percepción, sobre ADSR, metáfora, reglas
---

# Fuente 05 — Game Feel: A Game Designer's Guide to Virtual Sensation

> Libro-fuente externo. Catalogado en `EST-003`, usado como marco por `EST-010` y **destilado recién en `EST-023`**.
> **IP:** conceptos + cita, nunca texto verbatim con copyright.

## Cita

Swink, S. (2008). *Game Feel: A Game Designer's Guide to Virtual Sensation*. Morgan Kaufmann / CRC Press. ISBN 978-0-12-374328-2.

Y dos artículos del mismo autor que adelantan partes del libro: *Game Feel: The Secret Ingredient* (Gamasutra, 2007) y *Principles of Virtual Sensation* (Gamasutra, 2006).

## Qué es (marco aprendido)

El tratado que le dio nombre al tema. Define el game feel como **control en tiempo real de objetos virtuales en un espacio simulado, con las interacciones enfatizadas por pulido**, y lo arma en cuatro pisos:

```txt
1  tres bloques        control en tiempo real · espacio simulado · pulido
2  percepcion          cuando existe el control en tiempo real (cap. 2 y 3, el procesador humano)
3  seis componentes    input · respuesta · contexto · pulido · metafora · reglas, cada uno
                       con sus metricas (cap. 5 a 11)
4  ocho principios     resultados predecibles · respuesta instantanea · facil pero profundo ·
                       novedad · respuesta atractiva · movimiento organico · armonia ·
                       pertenencia (cap. 17)
```

En el medio, cinco casos analizados componente por componente: *Asteroids*, *Super Mario Bros.*, *Bionic Commando*, *Super Mario 64* y *Raptor Safari*.

**Lo que más rinde para Vaultrum:**

- **Los umbrales.** Tres condiciones para que haya control en tiempo real: impresión de movimiento (más de 10 cuadros por segundo), respuesta percibida como instantánea (menos de 100 ms; entre 100 y 240 ms se siente pesada) y continuidad de la respuesta (más allá del lazo de corrección de ~240 ms deja de sentirse control). Los apoya en el procesador humano de Card, Moran y Newell: percepción ~100 ms, cognición ~70 ms, motor ~70 ms.
- **El sobre ADSR** (cap. 7). Ataque, decaimiento, sostenido y liberación —tomados de la síntesis de sonido— para describir la velocidad del avatar en el tiempo. Convierte *"se siente resbaloso"* en un número.
- **Métricas duras y blandas** (cap. 5). Las duras se leen del juego —cuadros, velocidades, duraciones—; las blandas son impresiones del jugador. El método es atar cada blanda a una dura.
- **Metáfora y reglas** (cap. 10 y 11). Lo que el objeto representa fija qué física espera el jugador —en tres grados: real, icónico, abstracto—, y lo que está en juego al moverse cambia cómo se siente el mismo movimiento —en tres alturas: reglas altas, medias y bajas—.

## Por qué le sirve a Vaultrum (a qué apunta)

Es la fuente primaria de `02_Game_feel` y, a través de él, de los principios de game feel del Core. Hasta `EST-023` el libro usaba sólo cuatro de los seis componentes y ninguno de los umbrales; los dos que faltaban —metáfora y reglas— son justamente los que un `GDS` deja implícitos.

## Qué se verificó contra qué

Verificación parcial declarada. El texto completo del libro no se leyó en esta misión.

```txt
estructura, capitulos y titulos de los 8 principios   indice del libro (Library of Congress)
definicion y los seis componentes                     articulo de Swink de 2007 · Wikipedia · 69
umbrales 10 fps / 100 ms / 240 ms                     70 (que los cita de Swink)
ciclos del procesador humano y fusion perceptual      notas de MIT 6.813 sobre Card, Moran y Newell (1983)
sobre ADSR y su lectura corto=ajustado / largo=suelto 70 · indice del libro (cap. 7)
metafora en 3 grados, reglas en 3 alturas, metricas   subtitulos del indice del libro (cap. 5, 10, 11);
duras y blandas                                       su lectura y los ejemplos, destilacion propia
lectura de 4 principios (predecibles, facil pero      articulo de Swink de 2006
profundo, novedad, respuesta atractiva)
lectura de movimiento organico, armonia, pertenencia  destilacion propia, SIN el capitulo a la vista
```

La última fila es la deuda: cuando el libro esté disponible para leer, esas tres lecturas se confrontan con el capítulo 17.

## Estado y próximos pasos

- **Estudiado**, destilada en `EST-023` → `02_Game_feel`.
- **Lo que se tomó:** los tres bloques, los seis componentes, los umbrales, el sobre ADSR, métricas duras y blandas, metáfora y reglas, los ocho principios.
- **Lo que sigue sin destilar:** los cinco casos de estudio componente por componente, y las métricas de input a nivel de dispositivo (cap. 6). Se destilan cuando un libro de género los necesite: el caso *Super Mario Bros.* es insumo natural de `02_Plataformero_2D`.

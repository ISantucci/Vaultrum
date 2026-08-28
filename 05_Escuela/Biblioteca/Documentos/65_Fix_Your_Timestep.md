---
tipo: documento
familia: Referencia técnica
autor: Glenn Fiedler
anio: 2004 (revisado 2006 y 2018)
formato: Artículo técnico con código de referencia
acceso: Libre
licencia: nivel B — publicado abiertamente por el autor en su propio sitio; sin licencia formal declarada
prioridad: alta
estado: Estudiado
mision: EST-012_Mision_Bucle_de_simulacion
url: https://gafferongames.com/post/fix_your_timestep/
---

# Documento 65 — Fix Your Timestep!

> Artículo técnico canónico. Entra al estante porque es la **referencia primaria del acumulador con interpolación**, el mecanismo que dos proyectos de Vaultrum implementaron sin poder citar de dónde salía.
> La Biblioteca no aloja el texto: ficha, referencia y URL.

## Referencia

Fiedler, G. (2004, rev. 2018). *Fix Your Timestep!*. gafferongames.com. https://gafferongames.com/post/fix_your_timestep/ (consultado 2026-08-28).

## Qué es

El artículo que fijó el vocabulario con el que hoy se discute el bucle. Recorre cuatro bucles en orden de menos a más correcto —paso variable, paso fijo puro, paso fijo con acumulador, y acumulador con interpolación de render— y en cada paso muestra qué defecto concreto resuelve el siguiente.

Su aporte de vocabulario es el que más se usa: **«la espiral de la muerte»**, el nombre de la realimentación positiva que aparece cuando un paso de simulación cuesta más de lo que dura, y que explica por qué un juego mal armado se cuelga en vez de bajar de fps.

## Por qué le sirve a Vaultrum

`SOL-001_Arquitectura_Salto` decidió paso fijo a 60 Hz con acumulador, render interpolado y techo de pasos —las cuatro piezas de este artículo— y las decidió correctamente sin una fuente que citar. Este documento es esa fuente.

## Nivel de licencia

**Nivel B.** Publicado abiertamente por el autor en su sitio, sin licencia formal. Se cita y se referencia; no se aloja ni se transcribe.

## Estado

**Estudiado.** Destilado en `01_Bucle_de_simulacion` (estante de Construcción), misión `EST-012`. Lo que se tomó: el modelo del acumulador y el nombre de la espiral. Lo que no: el código de referencia en C++, que Vaultrum no consume verbatim.

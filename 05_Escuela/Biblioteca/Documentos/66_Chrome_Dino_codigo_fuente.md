---
tipo: documento
familia: Código fuente liberado
autor: The Chromium Authors (Google)
anio: 2014 (versión TypeScript leída en el commit 9b4a14466a0e, 2026-10-02)
formato: Código fuente (TypeScript)
acceso: Libre
licencia: nivel A — licencia BSD de Chromium
prioridad: alta
estado: Estudiado
mision: EST-019_Mision_Endless_runner_y_contrarreloj
url: https://github.com/chromium/chromium/tree/main/components/neterror/resources/dino_game
---

# Documento 66 — Chrome Dino (T-Rex Runner), código fuente

> Artefacto real de la industria: el endless runner más jugado del mundo, con su configuración entera legible.
> **IP:** ficha + referencia. La Biblioteca no aloja el código; cita constantes y comportamientos.

---

- **Autor y año:** The Chromium Authors, 2014; reescrito en TypeScript. Extracción histórica de 2014: https://github.com/wayou/t-rex-runner (BSD)
- **Tipo:** código fuente del juego de la página sin conexión de Chrome. Fijar el commit al citar: `main` cambia.
- **URL:** https://github.com/chromium/chromium/tree/main/components/neterror/resources/dino_game — `offline.ts` (configuración y bucle), `horizon.ts` (generación), `obstacle.ts` (huecos), `trex.ts` (salto y cajas), `distance_meter.ts` (puntaje)
- **Estado de acceso:** **Libre.** Nivel A.
- **Qué se aprende:**
  - El runner completo en números: velocidad de 6 a 13 px/cuadro con aceleración lineal, 3 s limpios al arrancar, hueco mínimo que crece con la velocidad y el ancho del grupo y se sortea hasta 1.5 veces, desbloqueo de obstáculos por velocidad, nunca tres iguales seguidos.
  - Cajas de colisión compuestas y generosas: seis cajas para el T-Rex corriendo, una para agachado; el pterodáctilo solo cuenta la franja del cuerpo.
  - Tres alturas de volador pensadas para tres respuestas, y una de ellas es no hacer nada. En móvil, sin agacharse, la altura media desaparece. Medido, la lectura es binaria: agacharse pasa la media y la alta, y el salto completo le pasa por encima a la alta.
  - El game over con dos caminos: la tecla de salto queda bloqueada 1.2 s y Enter o el clic reinician ya.
  - Un modo accesible con avisos sonoros que reescribe velocidad, huecos y salto al mismo tiempo.
  - **Un defecto instructivo:** la aceleración se suma por cuadro, sin `deltaTime`, mientras el mundo se mueve por tiempo. La rampa depende de la frecuencia del monitor.
- **Medido corriendo (`EST-021`):** el código compilado tal cual, con tiempo virtual y un bot, en `05_Escuela/Herramientas/banco_dino/medir.mjs`. Lo que la lectura no mostraba:
  - **Dos bucles en la primera partida.** La tecla que arranca llama a `update()` con el rAF del parpadeo todavía pendiente: quedan dos cadenas, y una partida arrancada durante el parpadeo llega al tope en 57 s en vez de 117 (60 Hz). Visto también en `chrome://dino` de Chromium 141 sin modificar: 120 rAF/s en la primera partida, 60 en la segunda.
  - **El avance de cada cuadro se trunca** (`Math.floor`): a tope el mundo va a 780 px/s a 60 Hz (752 con ±0.5 ms de jitter), 720 a 120–144 y 660 a 165, mientras el puntaje cuenta la velocidad sin truncar. La frecuencia mueve la rampa y la velocidad del mundo en sentidos opuestos.
  - **La suelta del salto no se recuerda:** antes de los 30 px no hace nada, así que el toque más corto da el salto más alto.
  - **Al volver el foco retoma al instante**, con los obstáculos donde estaban.
  - **La física del salto lee el reloj de la animación:** si la caída rápida aterriza justo en el pixel del piso con abajo apretado, el T-Rex queda agachado sobre el piso con el salto activo, y no puede volver a saltar hasta 1.05 s después de despegar a 60 Hz y 2.15 s a 144 Hz.
  - La ventana de presión real es 1.4–1.9 veces la calculada (0.42–0.43 s sobre un cactus chico) y ninguno de 3.123 pares del generador es imposible.
- **Gap de Vaultrum que cubre:** el libro de endless runner no existía y `RQ-001.6` de Portfolio estaba pausado por eso.
- **Prioridad:** **Alta** — es la calibración del baseline de `05_Endless_runner`.

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
  - Tres alturas de volador que fuerzan tres respuestas distintas, y una de ellas es no hacer nada. En móvil, sin agacharse, la altura media desaparece.
  - El game over con dos caminos: la tecla de salto queda bloqueada 1.2 s y Enter o el clic reinician ya.
  - Un modo accesible con avisos sonoros que reescribe velocidad, huecos y salto al mismo tiempo.
  - **Un defecto instructivo:** la aceleración se suma por cuadro, sin `deltaTime`, mientras el mundo se mueve por tiempo. La rampa depende de la frecuencia del monitor.
- **Gap de Vaultrum que cubre:** el libro de endless runner no existía y `RQ-001.6` de Portfolio estaba pausado por eso.
- **Prioridad:** **Alta** — es la calibración del baseline de `05_Endless_runner`.

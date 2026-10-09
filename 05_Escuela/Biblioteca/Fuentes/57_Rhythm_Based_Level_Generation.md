---
tipo: fuente
titulo: "Rhythm-Based Level Generation for 2D Platformers"
autores: Gillian Smith, Mike Treanor, Jim Whitehead & Michael Mateas
editorial: Foundations of Digital Games (FDG '09), ACM
anio: 2009
licencia: nivel B — PDF publicado por el laboratorio de los autores
estado: Estudiado
mision: EST-019_Mision_Endless_runner_y_contrarreloj
temas: generación procedural, ritmo, grupos rítmicos, verificación física de jugabilidad
apunta_a: Level Design · Game Design
url: https://eis.ucsc.edu/papers/smith-fdg-09.pdf
---

# Fuente 57 — Rhythm-Based Level Generation for 2D Platformers

> Paper externo. **IP:** conceptos + cita, nunca texto verbatim con copyright.

## Cita

Smith, G., Treanor, M., Whitehead, J. & Mateas, M. (2009). Rhythm-Based Level Generation for 2D Platformers. *Proceedings of the 4th International Conference on Foundations of Digital Games*, ACM. PDF: https://eis.ucsc.edu/papers/smith-fdg-09.pdf (consultado 2026-10-02).

## Qué es (marco aprendido)

El nivel se arma con **grupos rítmicos** que no se superponen: cada uno tiene una duración, un tipo de ritmo y una densidad, y los verbos del jugador se traducen a geometría con una gramática. Un **modelo físico** del personaje garantiza que todo lo generado sea jugable —cada salto termina antes de que empiece el siguiente—, y unos críticos eligen entre muchos candidatos. Entre grupo y grupo hay un descanso.

## Por qué le sirve a Vaultrum (a qué apunta)

Es la forma de la regla de huecos de `05_Endless_runner`: **el generador no confía en números sueltos, verifica cada patrón contra el salto real.** Y es la puerta a la generación por bloques de autor, que ese libro declara sin destilar.

## Límites declarados

Es sobre plataformeros con niveles finitos, no sobre runners infinitos. La versión extendida (Launchpad, 2011) no se leyó.

## Estado y próximos pasos

- **Estudiado** para `05_Endless_runner`; queda pendiente destilar la generación por grupos rítmicos.

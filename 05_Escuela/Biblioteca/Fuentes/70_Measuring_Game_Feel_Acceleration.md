---
tipo: fuente
titulo: "Measuring How Game Feel Is Influenced by the Player Avatar's Acceleration and Deceleration"
autores: Gustav Dahl, Martin Kraus
editorial: ACM
anio: 2015
estado: Estudiado (destilada — alimentó 02_Game_feel)
mision: EST-023_Mision_Swink_Game_Feel
temas: game feel, aceleración, frenado, sobre ADSR, medición con jugadores
apunta_a: 02_Game_feel · 03_Matematica_del_movimiento · Área de Game Design
---

# Fuente 70 — Measuring How Game Feel Is Influenced by the Player Avatar's Acceleration and Deceleration

> Paper académico externo. Entra porque el baseline de `02_Game_feel` fija tiempos de aceleración y frenado **sin un solo dato medido con jugadores** detrás.
> **IP:** conceptos + cita, nunca texto verbatim.

## Cita

Dahl, G. y Kraus, M. (2015). *Measuring How Game Feel Is Influenced by the Player Avatar's Acceleration and Deceleration: Using a 2D Platformer to Describe Players' Perception of Loose and Tight Game Feel*. ACM. DOI 10.1145/2818187.2818275. Versión extendida: tesis de Medialogía, Universidad de Aalborg.

## Qué es (marco aprendido)

Toma el sobre ADSR de Swink —ataque, decaimiento, sostenido, liberación aplicados a la velocidad del avatar— y lo **mide con jugadores**. Un plataformero 2D con una pelota que rueda; entre rondas cambian el ataque (aceleración) y la liberación (frenado), cada uno rápido (1–240 ms) o lento (241–1500 ms), en orden contrabalanceado. 274 participantes, 701 rondas registradas, cada una calificada en escalas de siete puntos: nervioso, fluido, rígido, flotante, responsivo, disfrutable, difícil, frustrante.

Descartan el decaimiento por innecesario en un avatar y usan curvas lineales.

## Lo que encontró

```txt
flotante     lo produce sobre todo un ATAQUE largo (> 1 s)
rigido       lo produce sobre todo una LIBERACION larga (> 1 s)
responsivo   alto con valores bajos; se sostiene con un ataque mas largo
             mientras la liberacion ronde 0.25 s
disfrute     sin tendencia clara
dificultad   sube con valores altos, igual que la frustracion
```

Los propios autores advierten que los resultados son **menos nítidos que los umbrales de Swink**, y muchos jugadores describieron el feel con palabras básicas —pesado, lento, responsivo— o no notaron diferencia entre rondas.

## Por qué le sirve a Vaultrum (a qué apunta)

Es la evidencia de una asimetría que el baseline de `02_Game_feel` ya aplicaba sin poder citarla: **la liberación decide cuán responsivo se siente el control; el ataque, cuán flotante.** Por eso el frenado tiene ventana propia y más corta que la aceleración.

## Límites declarados

Un solo género (plataformero 2D), un solo avatar (una pelota), curvas lineales y escalas ordinales promediadas en franjas de 0.25 s. Los números se leen como dirección, no como valores a copiar.

## Estado y próximos pasos

- **Estudiado**, destilada en `EST-023` → `02_Game_feel` (la sección del sobre ADSR).
- **Lo que se tomó:** la asimetría ataque/liberación y la franja de 0.25 s.
- **Lo que sigue sin destilar:** nada relevante; el resto del paper es metodología.

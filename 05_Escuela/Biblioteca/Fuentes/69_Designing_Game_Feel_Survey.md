---
tipo: fuente
titulo: "Designing Game Feel. A Survey"
autores: Martin Pichlmair, Mads Johansen
editorial: IEEE Transactions on Games
anio: 2021
estado: Estudiado (destilada — alimentó 02_Game_feel)
mision: EST-023_Mision_Swink_Game_Feel
temas: game feel, tuning, juicing, streamlining, revisión de literatura
apunta_a: 02_Game_feel · 10_Input_y_respuesta · Área de Game Design
---

# Fuente 69 — Designing Game Feel. A Survey

> Paper académico externo. Entra porque `02_Game_feel` tenía un solo marco —el de Swink— y ninguna lectura de cómo lo usa la práctica que vino después.
> **IP:** conceptos + cita, nunca texto verbatim.

## Cita

Pichlmair, M. y Johansen, M. (2021). *Designing Game Feel. A Survey*. IEEE Transactions on Games, 14(2), 138–152. DOI 10.1109/TG.2021.3072241. Preprint: arXiv:2011.09201 (2020).

## Qué es (marco aprendido)

Una revisión de más de doscientas fuentes —libros, charlas, postmortems, código— sobre cómo se diseña el game feel. Toma la definición de Swink y ordena la práctica en **tres dominios de experiencia**, cada uno con su verbo de oficio:

```txt
dominio         verbo           que se hace
fisicalidad     tuning          fijar los parametros que definen como se comporta lo que se
                                maneja: da cohesion y prediccion
amplificacion   juicing         sumar feedback que enfatiza y agranda los eventos: da poder
                                y dice cuanto importa cada uno
soporte         streamlining    interpretar el input en el contexto de la jugada para que el
                                juego haga lo que el jugador quiso: coyote time, buffer, asistencia
```

Y cataloga los recursos concretos —coyote time, screenshake, hitstop, trails y muchos más— asignando cada uno a uno o más dominios.

## Por qué le sirve a Vaultrum (a qué apunta)

Le pone nombre al tercer dominio que `02_Game_feel` no tenía como tal: el **soporte**. El perdón de input vivía en `10_Input_y_respuesta` como técnica; acá aparece como uno de los tres dominios del game feel, al lado del juice. Un `GDS` que declara física y efectos pero no declara qué input perdona dejó uno de los tres dominios sin diseñar.

La correspondencia con las capas del libro:

```txt
fisicalidad   -> capa 2, simulacion
amplificacion -> capa 3, confirmacion
soporte       -> capa 1, respuesta, y el perdon de 10_Input_y_respuesta
```

## Límites declarados

Es un mapa de la práctica, no un estudio medido: no aporta umbrales numéricos. Los números del libro salen de Swink y de `70_Measuring_Game_Feel_Acceleration`.

## Estado y próximos pasos

- **Estudiado**, destilada en `EST-023` → `02_Game_feel` (la sección de los seis componentes y la correspondencia de dominios).
- **Lo que se tomó:** los tres dominios y su correspondencia con las capas.
- **Lo que sigue sin destilar:** las tablas completas de recursos por dominio. Se destilan cuando un libro de género necesite un recurso que el vocabulario de efectos no tenga.

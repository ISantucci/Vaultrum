## Definición

**Bloquear** (blockout) es construir primero con primitivas —cajas, cilindros, esferas— las masas grandes del objeto, a escala real, y recién después refinar la forma y el detalle.

```txt
1  bloqueo     masas, escala y silueta, a escala real y contra un vecino
2  forma       las curvas y los volumenes principales
3  detalle     lo que se ve de cerca: biseles, ornamento, costuras
```

---

## Idea central

**El detalle es lo más caro de rehacer, y lo primero que se tira cuando cambia la escala.**

```txt
detallar primero     una torre con todas sus tejas, que despues resulta 20% mas alta
                     de lo que pide la grilla: se rehace entera
bloquear primero     una caja de 3.00 m contra la grilla del nivel, aprobada; las tejas
                     se ponen una vez
```

Es la versión de modelado de lo que el Área de Arte aprendió al revés: la celda de 3.00 m se eligió midiendo cuántos de los ocho assets ya construidos entraban. La dimensión maestra se decide **antes del primer asset** (mitad A del `ART`), y el bloqueo es donde un asset se mide contra ella antes de costar algo.

---

## Lo que se decide en el bloqueo

```txt
escala           contra la dimension maestra del proyecto y contra un vecino con
                 razon funcional (RA-003): la puerta contra el personaje, no contra
                 otra puerta
silueta          se lee en negro sobre blanco a la distancia de juego (Silueta legible)
proporcion       la medida que el blueprint no trae se deriva, y se lee en dos vistas
                 (RA-004, RA-005)
presupuesto      cuantas caras va a poder gastar, sabiendo cuantas veces aparece
```

Lo que **no** se decide en el bloqueo: el detalle, la topología fina, los materiales.

---

## Modificadores no destructivos

Espejo, subdivisión, bisel, array: mientras sean modificadores, la forma se puede cambiar sin rehacer. Se aplican **tarde**, cuando la forma está aprobada, y se aplican antes de verificar: el instrumento mide la malla final, no la que el modificador promete.

---

## Cómo se juzga

```txt
se mide     bbox del bloqueo contra la dimension maestra y contra el vecino: es un
            numero, se mide antes de seguir
se juzga    si la silueta del bloqueo ya dice que objeto es
```

---

## Errores comunes

```txt
Modelar el detalle de una pieza antes de tener el conjunto bloqueado.
Bloquear sin escala real ("despues lo escalo"): la escala sin aplicar es un defecto.
Aprobar el bloqueo mirandolo de frente, en el DCC, y no a la distancia de juego.
Aplicar modificadores para "ver como queda" y perder la posibilidad de volver.
```

---

## Fuentes

- `65_Digital_Modeling` — el flujo de bloqueo a detalle.
- Área de Arte: Modo Escala, `RA-003_Medidas_y_proporcion`, `RA-004_De_blueprint_a_malla`, `RA-005_Blueprint_sin_cotas`.

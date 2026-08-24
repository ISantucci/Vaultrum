---
tipo: fundamento
estado: En la Biblioteca
mision: [[EST-001_Mision_Pong]] (síntesis) + uso en [[VE-003_Pong3D]]
---

# Fundamento 03 — Definición de Terminado

> La checklist que separa *compila* de *está hecho*. El baseline que todo entregable cumple antes de considerarse terminado.
> Estado: **En la Biblioteca** — sintetiza los Fundamentos 01, 02 y 05, y el uso real en `VE-003`.

## Índice del libro

- Qué es y qué no es
- La checklist transversal
- Cómo se corre
- Cómo la extiende un libro de género
- Los dos modos de cerrar
- Aplicación
- Límites
- Fuentes

## Qué es y qué no es

Una **definición de terminado** es una lista de condiciones verificables que un entregable cumple antes de declararse hecho.

```txt
NO es una lista de features         → eso es el alcance
NO es una lista de bugs             → eso es el reporte de QA
NO es "pasa los tests"              → los tests verifican el código, no la entrega
SÍ es: qué tiene que poder hacer
       una persona con esto en la mano
```

La distinción operativa es una sola:

> **Se corre sobre el entregable funcionando, no sobre el código.**

Tildar ítems leyendo la implementación es el cierre en falso que este instrumento existe para evitar. Un ítem verificado en el código dice que *debería* funcionar; solo el entregable corriendo dice que funciona.

**Por qué existe este fundamento.** En `VE-002` la implementación de un juego completo nunca llegó a estar en disco y aun así todos los pasos previos figuraban cerrados. En `VE-003` los 18 ítems estaban implementados en código y ninguno se recorrió sobre el juego corriendo. Los dos casos son el mismo error visto en dos profundidades.

## La checklist transversal

El mínimo que aplica a **cualquier entregable jugable**, independiente del género. Un libro de género la extiende; no la reemplaza.

```txt
LOOP
[ ] Cada input produce feedback perceptible, siempre
[ ] El objetivo se entiende sin que nadie lo explique
[ ] El loop principal se puede repetir sin romperse ni trabarse

PARTIDA
[ ] Hay condición de victoria y de derrota, ambas alcanzables
[ ] El fin de partida se percibe sin interpretar números
[ ] Se puede volver a jugar sin cerrar la aplicación

ESTADOS
[ ] Se puede pausar y despausar
[ ] Toda pantalla tiene salida: ninguna sin acción posible
[ ] No hay estados muertos ni transiciones sin retorno

CLARIDAD
[ ] Los controles se comunican sin manual externo
[ ] En todo momento se puede responder: qué pasa / qué puedo hacer / cómo voy
[ ] El estado del sistema es legible de un vistazo

FEEL
[ ] La acción principal se siente como un evento, no como un cambio de variable
[ ] Los eventos importantes se sienten distintos de los secundarios (jerarquía)
[ ] El control responde en el instante y frena con peso
[ ] El juice nunca impide leer el estado del juego
```

Dieciséis ítems, cinco bloques. Los cinco bloques son el orden de fallo típico: casi todo entregable apurado tilda **LOOP**, tilda a medias **PARTIDA**, y falla entero en **ESTADOS**, **CLARIDAD** y **FEEL**.

## Cómo se corre

```txt
1. El entregable corre en su entorno de destino.
2. Se recorre ítem por ítem, en orden, sobre el entregable.
3. Cada ítem queda: [x] tildado · [ ] con hallazgo concreto · N/A con justificación escrita
4. Un ítem sin marcar no es un ítem tildado. Es un ítem sin correr.
5. El resultado se registra en el VE.
```

**Reglas de marcado:**

- **N/A es válido y exige justificación en la misma línea.** Un sandbox sin condición de victoria formal puede marcar N/A el ítem correspondiente si dice por qué. Un N/A sin motivo es un ítem salteado.
- **Un hallazgo no es un ítem tildado.** Si el ítem falla, se anota qué falla y a qué área rebota.
- **No se tilda desde el código.** Nunca.

## Cómo la extiende un libro de género

La checklist transversal es el piso. El libro del género agrega los ítems específicos de ese tipo de entregable, que suelen ser los que más importan.

Ejemplo, comparando con [[01_Pong]]:

```txt
transversal:  "el loop principal se puede repetir sin romperse"
Pong añade:   "la pelota nunca atraviesa una paleta ni una pared, ni se traba"
              "dónde pego cambia hacia dónde sale: puedo apuntar"
              "tras un gol hay un saque legible, no un reinicio instantáneo"
```

El ítem transversal es cierto y no alcanza: el tunneling es *el* fallo característico de un Pong, y ninguna checklist genérica lo iba a nombrar.

**Regla de composición:** la checklist efectiva de una entrega es `transversal + género`. Si el género no tiene libro, la entrega corre solo la transversal **y lo declara** — no finge cobertura que no tiene.

## Los dos modos de cerrar

Una entrega puede darse por terminada de dos maneras, y el `VE` declara cuál usó:

| Modo | Qué es | Qué dice | Qué NO dice |
|------|--------|----------|-------------|
| **Checklist** | se recorren los ítems, uno por uno, sobre el entregable corriendo | cuál de los ítems falla | si el conjunto se sostiene como experiencia |
| **Veredicto** | el owner usa el entregable y emite un juicio global | si el conjunto funciona | cuál de los ítems falla |

Los dos son verificaciones parciales y ninguno reemplaza al otro. Un 8/10 del owner es información real y suficiente para cerrar una entrega; no dice cuál de los dieciséis ítems falla. La checklist dice cuál falla; no dice si el conjunto engancha.

Cuando se cierra por veredicto, **se declara la deuda**: qué ítems no se recorrieron. Criterio del Core: [[Verificacion parcial declarada]].

## Aplicación

```txt
Producción (RQ)  → cada ítem de la checklist tiene que estar cubierto por
                   algún RQ. Un ítem sin RQ es un hueco de planificación.
Game Design      → el CHECKLIST por-GDS de [[05_Fundamentos_de_experiencia_ludica]]
                   cubre el diseño; éste cubre la entrega. No se solapan:
                   uno pregunta "¿está bien diseñado?", el otro "¿está hecho?"
Producción (VE)  → se corre acá, sobre el entregable corriendo. Es el gate.
```

Es también la fuente canónica del checklist que la skill `vaultrum-produccion` corre en el paso 4.

## Límites

- **No mide calidad, mide completitud.** Un entregable puede tildar los dieciséis ítems y ser aburrido. Para "¿está bien?" el instrumento es el CHECKLIST por-GDS de los 9 pilares, y en última instancia el veredicto de alguien jugando.
- **No aplica sin cambios fuera de lo jugable.** Un entregable de software tiene una versión análoga —manejo de error legible, estado inicial y final claros, ninguna operación sin salida, feedback de progreso— pero los bloques PARTIDA y FEEL no se traducen directo. Cuando se aplique a software no-juego, se declara qué bloques se adaptaron.
- **No reemplaza al playtest.** La checklist detecta huecos; el playtest detecta que algo no gusta. Son dos cosas y hacen falta las dos.
- **No crece indefinidamente.** Si la lista transversal supera los ~20 ítems, algo que era específico de un género se coló acá. Se poda y se manda al libro que corresponde.

## Fuentes

Síntesis propia a partir de los Fundamentos [[01_Loop_de_experiencia]], [[02_Game_feel]] y [[05_Fundamentos_de_experiencia_ludica]], del libro de género [[01_Pong]], y del uso real en [[VE-002_Pong3D]] y [[VE-003_Pong3D]].

Canon de apoyo, sin verbatim: `19_Playful_Production_Process` (fases y criterios de cierre) · `03_Game_Design_Workshop` (playtesting como instrumento) · `09_Gamers_Brain` y `10_Game_Usability` (legibilidad, usabilidad, ausencia de estados muertos) · `05_Game_Feel` (respuesta y peso) · `08_Designing_Games` (elegancia y prototipo gris).

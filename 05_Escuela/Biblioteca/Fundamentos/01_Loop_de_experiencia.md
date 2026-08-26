---
tipo: fundamento
estado: En la Biblioteca
mision: EST-001_Mision_Pong
---

# Fundamento 01 — Loop de experiencia

> Qué convierte un conjunto de reglas en algo que se *juega*. Transversal a todo género.
> Estado: **En la Biblioteca** — primer aporte destilado desde el análisis de Pong (`EST-001_Mision_Pong`).

## Índice del libro

- Loop de experiencia
- Table-stakes
- Juice / game feel
- Definición de Terminado
- Aplicación
- Límites
- Fuentes

## Loop de experiencia

El núcleo es un ciclo de cuatro tiempos que se cierra sobre sí mismo:

```txt
input → feedback → objetivo → victoria/derrota
  ↑                                    │
  └────────────────────────────────────┘
```

Un entregable sin este ciclo cerrado todavía no es una experiencia: es una demo técnica. Y el corte no es gradual — falta **cualquiera** de los cuatro y el resultado cambia de categoría:

```txt
sin input          → una animación
sin feedback       → un sistema que no se puede aprender
sin objetivo       → un juguete
sin victoria/derrota → un juguete con marcador
```

### Los loops anidan

Un loop solo alcanza para un ejercicio, no para un juego. Lo que sostiene a alguien jugando son **loops de escalas distintas corriendo a la vez**, cada uno con su propio cierre.

El caso más limpio es Pong, porque no tiene contenido, narrativa ni progresión donde esconderse:

```txt
LOOP ATÓMICO (≈0.3–1 s)
  leer la trayectoria → mover la paleta → interceptar → ver salir el rebote
                              ↑                              │
                              └──────────────────────────────┘

LOOP DE PUNTO (≈5–20 s)      rally → alguien falla → gol → saque
LOOP DE PARTIDA (≈2–5 min)   puntos → puntaje objetivo → victoria/derrota → revancha
```

La regla que sale de ahí es general: **siempre tiene que haber algo que perseguir ahora, algo a mediano plazo, y algo por lo que volver.** Los tres, simultáneos.

El error clásico al implementar es construir solo el loop atómico —la pelota que rebota, el personaje que salta, el botón que responde— y llamarlo juego. Sin el loop superior no hay stakes: nada de lo que pasa en el loop chico acumula hacia ningún lado. `18_Art_of_Failure`, `21_The_Grasshopper`

### Qué separa un juego de un juguete

Dos cosas, y las dos son de diseño, no de implementación:

```txt
1. un objetivo impuesto
2. un obstáculo innecesario aceptado voluntariamente
```

En Pong: llegar al puntaje, y solo poder mover la paleta en un eje. Sacale cualquiera de los dos y queda un salvapantallas. `21_The_Grasshopper`, `06_Half_Real`

El obstáculo innecesario es el que más se subestima. Quitar restricciones para "hacerlo más cómodo" suele destruir el juego: la restricción **es** el juego.

### Dónde vive la tensión

En la incertidumbre del resultado. Si el resultado se conoce de antemano, el loop se ejecuta pero no tensa.

Las fuentes de incertidumbre son varias y no equivalentes: el desempeño propio, el del oponente, el azar, la información oculta, la complejidad del espacio de decisión. Pong es *agon* puro —habilidad contra habilidad, sin azar— y por eso toda su tensión sale de las dos primeras. `23_Man_Play_and_Games`, `17_Uncertainty_in_Games`

Consecuencia práctica: un juego de un jugador contra un sistema determinista y transparente **necesita** conseguir la incertidumbre de otro lado, o el loop se agota en dos partidas.

## Table-stakes

Lo mínimo para que el loop esté cerrado, en cualquier género:

| # | Table-stake | Qué se rompe sin ella |
|---|-------------|-----------------------|
| 1 | El input produce **feedback perceptible** en el mismo instante | El jugador no puede aprender el sistema: no sabe qué causó qué |
| 2 | Hay un **objetivo entendible sin explicación externa** | No hay nada que perseguir; el input se vuelve exploración sin dirección |
| 3 | Hay **condición de victoria y de derrota**, ambas alcanzables | No hay stakes: nada de lo que se hace tiene consecuencia acumulada |
| 4 | El **estado actual es legible** en todo momento (qué pasa / qué puedo hacer / cómo voy) | El jugador juega a ciegas y atribuye al azar lo que era su decisión |
| 5 | El fin de partida es **perceptible** y ofrece **reintento inmediato** | El fracaso expulsa en vez de retener; el loop de partida no cierra |
| 6 | **Ninguna pantalla sin salida** | Estados muertos: el loop se corta por un motivo que no es del juego |

Las seis se verifican jugando, no leyendo código.

## Juice / game feel

El loop define *qué pasa*; el juice define *cómo se siente que pase*. Son capas distintas y el orden importa:

```txt
primero el loop, después el juice.
el juice no tapa un loop roto — lo hace más ruidoso.
```

Dos reglas transversales que salieron del análisis de Pong y aplican a cualquier género:

**Jerarquía del feedback.** Los eventos no pueden sonar todos igual de fuerte. Si el rebote contra la pared se siente como el gol, el jugador no aprende qué importa. La intensidad del feedback **enseña la importancia relativa de los eventos** — es información, no decoración.

**La legibilidad gana.** Si el juice impide leer el estado del juego, el juice está mal. Un screenshake que tapa la pelota convierte una mejora de feel en un problema de claridad.

Desarrollo en `02_Game_feel`.

## Definición de Terminado

El loop cerrado es el piso, no el techo. La checklist completa está en `03_Definicion_de_terminado`; lo que este fundamento aporta ahí son los dos bloques que dependen del loop:

```txt
LOOP
[ ] El input produce feedback perceptible, siempre
[ ] Hay un objetivo que se entiende sin que nadie lo explique
[ ] El loop atómico se puede repetir indefinidamente sin romperse

PARTIDA
[ ] Hay condición de victoria y de derrota
[ ] El fin de partida se percibe sin interpretar números
[ ] Se puede volver a jugar sin cerrar la aplicación
```

## Aplicación

**Producción (RQ).** Los seis table-stakes entran como requerimiento explícito, siempre, en cualquier entregable jugable. No se asumen y no se dejan implícitos: una table-stake sin `RQ` es un hueco.

**Game Design (GDS).** Al diseñar un sistema, verificar que aporte a alguno de los loops anidados. Un sistema que no alimenta ningún loop es contenido, no mecánica.

**Validación de entrega (VE).** Si el entregable "funciona" y no engancha, el diagnóstico casi siempre es un loop superior faltante: existe el atómico y no hay razón para volver.

Criterio del Core relacionado: `Baseline de entregable`.

## Límites

- **No dice cuántos loops.** Tres es lo típico (atómico / sesión corta / retorno), pero un juego largo tiene más y uno de dos minutos puede tener dos. La regla es que haya más de uno, no que haya tres.
- **No aplica igual fuera de lo jugable.** En una herramienta el equivalente del loop atómico existe (acción → resultado visible) pero "victoria/derrota" no: se reemplaza por *tarea completada / error recuperable*.
- **No resuelve la duración.** Un loop bien cerrado y aburrido sigue siendo aburrido. Lo que hace interesante al loop es el espacio de decisión, y eso es Pilar 9 de `05_Fundamentos_de_experiencia_ludica`.

## Fuentes

Conceptos destilados, sin verbatim:

`21_The_Grasshopper` (objetivo impuesto + obstáculo innecesario) · `06_Half_Real` (reglas vs ficción, qué constituye un juego) · `17_Uncertainty_in_Games` (fuentes de incertidumbre) · `23_Man_Play_and_Games` (agon / alea / mimicry / ilinx) · `18_Art_of_Failure` (fracaso que retiene) · `04_Theory_of_Fun` (aprendizaje como fuente de diversión) · `16_Advanced_Game_Design` (loops anidados y pensamiento sistémico) · `05_Game_Feel` (feedback y respuesta) · `09_Gamers_Brain` (legibilidad y carga cognitiva).

Cruza con: `02_Game_feel` · `03_Definicion_de_terminado` · `04_Playbook_de_diseno` · `05_Fundamentos_de_experiencia_ludica` · `01_Pong`.

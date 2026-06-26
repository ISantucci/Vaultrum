## Proposito

Esta subcarpeta reune formas de convertir el espacio visual de un videojuego en informacion util para sistemas de IA, navegacion, pathfinding o gameplay.

No existe para elegir algoritmos.
No existe para resolver comportamientos de NPC.
No existe para hacer mapas mas complejos porque si.

Existe para responder:

```txt
¿Como represento el mapa para que un sistema pueda leerlo?
```

---

## Idea central

Antes de calcular caminos, tomar decisiones espaciales o mover agentes, el juego necesita una representacion logica del espacio.

```txt
Mapa visual
→ representacion logica
→ lectura por sistemas
→ navegacion o decision
```

Esa representacion puede ser simple o compleja segun la necesidad real del juego.

No todos los juegos necesitan la misma estructura.

---

## Responsabilidad de esta subcarpeta

Esta subcarpeta debe ayudar a decidir y documentar como se estructura el espacio.

Su responsabilidad es explicar conceptos como:

```txt
nodos
grillas
waypoints
grafos
GridMap
GridNode
conexiones
vecinos
puntos de interes
posiciones navegables
```

No es responsabilidad principal de esta subcarpeta explicar:

```txt
A*
Theta*
estados de NPC
percepcion
patrullaje
ataque
huida
steering behaviours
```

Esos temas pertenecen a otras subcarpetas.

---

## Cuando usar esta subcarpeta

Usar esta subcarpeta cuando el problema sea:

```txt
representar posiciones importantes del mapa
definir puntos navegables
elegir entre nodos, grillas o waypoints
conectar zonas del escenario
preparar informacion para pathfinding
preparar informacion para comportamiento de NPCs
decidir si el mapa necesita una estructura logica
```

Ejemplos:

```txt
Un enemigo debe moverse entre puntos fijos.
→ Waypoints pueden alcanzar.

Un agente debe elegir entre caminos alternativos.
→ Nodos y conexiones pueden servir.

Un mapa tactico trabaja por casilleros.
→ Grilla puede tener sentido.

Un sistema necesita calcular rutas flexibles.
→ Grafo o mapa de nodos puede ser necesario.
```

---

## Como usar esta subcarpeta

El flujo recomendado es:

```txt
1. Entender como se mueve el agente o sistema.
2. Identificar si el mapa necesita puntos, celdas o conexiones.
3. Elegir la representacion minima suficiente.
4. Definir que datos debe guardar cada unidad del mapa.
5. Definir como se conectan esas unidades.
6. Validar si la representacion permite resolver el problema.
7. Recién despues evaluar pathfinding o reglas de mapa.
```

La representacion debe elegirse antes del algoritmo.

---

## [[Nodos]]

Los nodos representan puntos logicos del mapa.

Sirven para marcar posiciones relevantes, posibles puntos de navegacion o unidades de una red de caminos.

Usar esta nota cuando el mapa necesita puntos conectables, pero no necesariamente una grilla completa.

Pregunta principal:

```txt
¿Que puntos del mapa necesita reconocer el sistema?
```

---

## [[Grillas]]

Las grillas representan el mapa dividido en celdas.

Sirven cuando el espacio puede analizarse por casilleros, tiles o unidades regulares.

Usar esta nota cuando el juego necesita lectura espacial por celdas.

Pregunta principal:

```txt
¿Conviene dividir el mapa en casilleros?
```

---

## [[Waypoints]]

Los waypoints representan puntos de recorrido definidos manualmente o por diseño.

Sirven para rutas simples, patrullajes, caminos guiados o recorridos predecibles.

Usar esta nota cuando no hace falta calcular caminos complejos.

Pregunta principal:

```txt
¿Alcanza con que el agente siga puntos predefinidos?
```

---

## [[GridMap y GridNode]]

GridMap y GridNode representan una estructura donde el mapa se organiza mediante nodos asociados a una grilla.

Sirven cuando se necesita trabajar con celdas, vecinos y navegacion basada en posiciones logicas.

Usar esta nota cuando la representacion del mapa necesita combinar grilla y nodos.

Pregunta principal:

```txt
¿Como organizo una grilla navegable en codigo?
```

---

## Relacion con otras subcarpetas

```txt
Representacion de mapa
→ define como se lee el espacio.

Navegacion y pathfinding
→ usa esa representacion para calcular caminos.

Reglas de mapa
→ agrega condiciones, costos o bloqueos.

Diseno y aplicacion
→ decide si esa representacion tiene sentido para el juego.
```

---

## Criterio para una IA

Cuando una IA trabaje con esta subcarpeta, no debe saltar directo a algoritmos.

Primero debe responder:

```txt
¿Que necesita saber el sistema sobre el mapa?
¿El espacio se representa por puntos, celdas o caminos?
¿La estructura debe ser manual, automatica o mixta?
¿Hace falta saber vecinos?
¿Hace falta guardar costos?
¿Hace falta representar bloqueos?
¿La solucion simple alcanza?
```

---

## Errores que esta subcarpeta ayuda a evitar

```txt
usar A* sin tener una representacion clara del mapa
crear una grilla cuando waypoints alcanzaban
crear un grafo cuando solo habia una ruta fija
meter datos de mapa dentro del NPC
mezclar representacion con decision
confundir mapa visual con mapa logico
```

---

## Regla final

La representacion del mapa no existe para demostrar tecnica.

Existe para que el juego pueda entender el espacio.

```txt
Primero representar.
Despues navegar.
Despues decidir.
```
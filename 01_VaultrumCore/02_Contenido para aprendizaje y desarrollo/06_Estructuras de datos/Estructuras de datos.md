## Proposito

Esta seccion organiza estructuras de datos aplicadas al desarrollo de videojuegos, sistemas de gameplay y arquitectura de software.

Una estructura de datos no se elige por parecer avanzada.

Se elige porque ordena informacion de una manera que ayuda a resolver un problema concreto.

```txt
Problema del sistema
→ tipo de informacion
→ forma de acceso necesaria
→ estructura adecuada
→ sistema mas claro
```

---

## Idea central

Las estructuras de datos son formas de organizar informacion.

En videojuegos pueden usarse para:

```txt
guardar historial
procesar elementos en orden
representar conexiones del mapa
ordenar entidades por prioridad
manejar turnos
administrar eventos
guardar rutas
gestionar acciones pendientes
```

La estructura no es el sistema completo.

La estructura sostiene datos para que otro sistema pueda operar mejor.

Ejemplo:

```txt
Stack
→ guarda historial.

Sistema de Undo
→ usa ese historial para revertir acciones.
```

Otro ejemplo:

```txt
Grafo
→ representa nodos y conexiones.

Pathfinding
→ usa el grafo para calcular rutas.
```

---

## Estructuras incluidas

```txt
Stack
Queue
Grafos
ABB
```

---

## [[Stack]]

Estructura LIFO.

```txt
Last In, First Out
→ ultimo en entrar, primero en salir
```

Sirve para historial, undo, redo, navegacion hacia atras y manejo de estados previos.

Ejemplo de uso:

```txt
Sistema de comandos
→ guarda acciones ejecutadas en Stack
→ permite deshacer la ultima accion
```

---

## [[Queue]]

Estructura FIFO.

```txt
First In, First Out
→ primero en entrar, primero en salir
```

Sirve para procesar elementos en orden de llegada.

Ejemplo de uso:

```txt
Oleada de enemigos
→ carga enemigos en Queue
→ spawner procesa uno por uno
```

---

## [[Grafos]]

Estructura formada por nodos y conexiones.

Sirve para representar mapas, rutas, zonas conectadas, caminos alternativos y relaciones entre puntos.

Ejemplo de uso:

```txt
Mapa navegable
→ se representa como grafo
→ pathfinding consume nodos y conexiones
```

---

## [[ABB]]

Arbol Binario de Busqueda.

Sirve para mantener datos ordenados por un criterio y consultar valores minimos, maximos o prioridades.

Ejemplo de uso:

```txt
Enemigos ordenados por progreso
→ torre consulta el enemigo mas avanzado
```

---

## Como elegir una estructura

```txt
Necesito historial
→ Stack

Necesito orden de llegada
→ Queue

Necesito conexiones
→ Grafos

Necesito orden por criterio
→ ABB
```

Regla:

```txt
La estructura se elige por el acceso que necesito,
no por la teoria que quiero demostrar.
```

---

## Cuando una lista alcanza

Una lista simple puede alcanzar cuando:

```txt
hay pocos elementos
el sistema es simple
no hay consultas frecuentes
no importa historial
no importa prioridad
no importa orden de llegada estricto
no hay conexiones complejas
```

Ejemplo:

```txt
lista de enemigos cercanos
→ puede alcanzar si son pocos y se recorre ocasionalmente
```

No conviene reemplazar todo por estructuras mas complejas sin necesidad.

---

## Cuando conviene una estructura mas especifica

Conviene usar una estructura especifica cuando el problema tiene una forma clara.

Ejemplos:

```txt
deshacer ultima accion
→ Stack

procesar eventos en orden
→ Queue

representar caminos conectados
→ Grafo

buscar prioridad maxima o minima
→ ABB
```

---

## Relacion con videojuegos

En videojuegos, las estructuras de datos suelen aparecer detras de sistemas concretos.

Ejemplos:

```txt
Undo / Redo
→ Stack

Oleadas de enemigos
→ Queue

Event Queue
→ Queue

Mapas conectados
→ Grafos

Pathfinding
→ Grafos

Targeting prioritario
→ ABB
```

La estructura existe para mejorar el sistema.

No debe reemplazar el criterio de gameplay.

---

## Relacion con otras secciones

Esta seccion puede ser consumida por otras areas del vault.

Ejemplos:

```txt
IA para NPC
→ puede usar grafos para representar navegacion.

IA para desarrollo de mapas
→ puede usar grafos para representar rutas y conexiones.

Patrones de diseño
→ puede combinar Command con Stack para Undo.

Optimizacion
→ puede evaluar costos de acceso, busqueda y memoria.

Algoritmos
→ pueden operar sobre estructuras como grafos.
```

Regla:

```txt
Estructura de datos
→ organiza informacion.

Algoritmo
→ procesa informacion.

Sistema de gameplay
→ usa ambos para resolver una necesidad del juego.
```

---

## Regla de navegacion

```txt
Estructuras de datos
→ linkea directo a las estructuras concretas.

La carpeta Estructuras
→ organiza archivos.

No hace falta un indice intermedio
si no aporta navegacion real.
```

---

## Criterio general

Antes de usar una estructura, preguntar:

```txt
¿Que problema real estoy resolviendo?
¿Que informacion necesito guardar?
¿Como necesito acceder a esa informacion?
¿Importa el orden?
¿Importa la prioridad?
¿Importan las conexiones?
¿Importa el historial?
¿Una lista simple alcanza?
¿La estructura mejora claridad o solo agrega complejidad?
```

---

## Errores comunes

Errores comunes al trabajar con estructuras de datos:

```txt
usar listas para todo
usar estructuras complejas sin necesidad
mezclar estructura con logica de gameplay
hacer que la estructura decida comportamiento
duplicar datos sin control
no entender el costo de busqueda o actualizacion
elegir por teoria y no por problema
crear indices intermedios que no agregan navegacion
```

---

## Criterio para una IA

Cuando una IA trabaje con estructuras de datos debe:

```txt
identificar primero el problema
elegir la estructura segun necesidad real
explicar por que esa estructura encaja
explicar cuando no conviene usarla
separar estructura, algoritmo y sistema consumidor
evitar sobrearquitectura
no crear indices innecesarios
usar ejemplos aplicados a videojuegos
respetar navegacion waterfall
```

---

## Regla final

```txt
Una estructura de datos no hace bueno a un sistema por si sola.

Lo mejora cuando organiza la informacion de la forma que el problema necesita.
```
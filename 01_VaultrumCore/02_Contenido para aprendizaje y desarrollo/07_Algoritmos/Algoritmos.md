## Proposito

Esta seccion reune algoritmos utiles para resolver problemas concretos dentro de videojuegos, software y sistemas interactivos.

No existe para juntar nombres de algoritmos.
No existe para aplicar tecnicas por costumbre.
No existe para mezclar algoritmos con estructuras de datos, IA, mapas o comportamiento de NPC.

Existe para entender que procedimiento conviene usar segun el problema, sobre que informacion trabaja y que resultado produce.

La pregunta central de esta seccion es:

```txt
¿Que procedimiento resuelve este problema?
```

---

## Idea central

Un algoritmo es una secuencia de pasos para transformar informacion disponible en un resultado util.

```txt
Datos de entrada
→ procedimiento
→ resultado
```

Ejemplo:

```txt
Grafo con costos
→ Dijkstra
→ camino de menor costo

Mapa con origen y objetivo
→ A Star
→ ruta dirigida hacia el destino

Lista desordenada
→ QuickSort
→ lista ordenada
```

Un algoritmo no crea por si mismo el sistema completo.

Consume informacion.

Procesa informacion.

Devuelve un resultado.

---

## Responsabilidad de esta seccion

Esta seccion debe explicar algoritmos como procedimientos reutilizables.

Su responsabilidad es documentar:

```txt
que problema resuelve cada algoritmo
que datos necesita
que estructura suele consumir
como funciona conceptualmente
cuando conviene usarlo
cuando no conviene usarlo
que errores evita
que riesgos tiene aplicarlo mal
```

No es responsabilidad principal de esta seccion explicar:

```txt
comportamiento completo de NPC
diseño completo de mapas
arquitectura de managers
implementacion completa de gameplay
documentacion de sistemas de juego
```

Esos temas viven en otras secciones de Vaultrum.

---

## Diferencia entre estructura y algoritmo

Una estructura organiza informacion.

Un algoritmo procesa informacion.

```txt
Estructura de datos
→ organiza.

Algoritmo
→ procesa.

Sistema consumidor
→ usa el resultado.
```

Ejemplo:

```txt
Grafo
→ estructura.

Dijkstra
→ algoritmo.

Sistema de navegacion
→ consume el resultado.
```

Esta diferencia evita mezclar responsabilidades.

---

## Como usar esta seccion

El flujo recomendado es:

```txt
1. Entender el problema.
2. Identificar que informacion existe.
3. Identificar que resultado se necesita.
4. Revisar si el algoritmo aplica.
5. Validar si la solucion simple alcanza.
6. Aplicar el algoritmo sin mezclarlo con el sistema consumidor.
7. Validar el resultado.
```

No se empieza por el nombre del algoritmo.

Se empieza por el problema.

---

## Algoritmos incluidos

### [[Dijkstra]]

Calcula caminos de menor costo sobre una estructura con conexiones y pesos no negativos.

Usar cuando el problema sea encontrar el camino mas barato o calcular costos acumulados sin necesidad de orientar la busqueda hacia un objetivo especifico.

Pregunta principal:

```txt
¿Cual es el camino de menor costo segun los pesos disponibles?
```

---

### [[A Star]]

Calcula caminos combinando costo acumulado y una heuristica hacia el objetivo.

Usar cuando existe un destino concreto y se quiere orientar la busqueda hacia ese destino.

Pregunta principal:

```txt
¿Como encuentro una ruta hacia este objetivo usando costo y estimacion?
```

---

### [[Theta Star]]

Variante de pathfinding any-angle basada en A Star que usa line of sight para intentar producir rutas mas directas.

Usar cuando se necesita una ruta menos angular y el costo tecnico de verificar visibilidad tiene sentido.

Pregunta principal:

```txt
¿Conviene calcular una ruta mas directa usando visibilidad entre puntos?
```

---

### [[QuickSort]]

Ordena una coleccion usando pivotes y particiones.

Usar cuando el problema sea ordenar datos segun un criterio.

Pregunta principal:

```txt
¿Como ordeno esta coleccion de datos?
```

---

## Relacion con otras secciones

Esta seccion puede ser consumida por otras partes de Vaultrum.

Ejemplos:

```txt
IA para desarrollo de mapas
→ puede usar algoritmos de pathfinding.

Estructuras de datos
→ provee grafos, listas, arrays u otras estructuras.

Optimizacion
→ puede evaluar costo, frecuencia y rendimiento del algoritmo.

IA para NPC
→ puede usar resultados de algoritmos, pero no deberia contenerlos mezclados.
```

La direccion correcta es:

```txt
Algoritmo
→ define procedimiento.

Sistema consumidor
→ decide cuando usarlo.
```

---

## Criterio para una IA

Cuando una IA proponga un algoritmo, debe justificar:

```txt
que problema resuelve
que datos recibe
que resultado devuelve
que estructura consume
por que conviene ese algoritmo
por que no alcanza una solucion mas simple
que costo tecnico tiene
como se valida el resultado
```

No alcanza con decir:

```txt
Usar A Star.
```

Debe explicar por que A Star aplica al problema.

---

## Errores que esta seccion ayuda a evitar

```txt
usar algoritmos por moda
usar A Star para cualquier movimiento
usar Dijkstra cuando no hay costos
usar QuickSort cuando no hace falta ordenar
mezclar algoritmo con comportamiento de NPC
meter pathfinding dentro de una clase de movimiento
confundir estructura de datos con algoritmo
duplicar explicaciones en secciones consumidoras
```

---

## Criterio de links

Los links deben guiar.

No deben decorar.

Regla:

```txt
Indice de Algoritmos
→ linkea algoritmos incluidos.

Notas de algoritmos
→ linkean solo dependencias operativas reales.

Secciones consumidoras
→ llaman al algoritmo cuando lo necesitan.
```

Una nota de algoritmo no debe convertirse en hub de mapas, NPC, optimizacion y estructuras.

---

## Regla final

Un algoritmo no es una solucion completa.

Es un procedimiento dentro de una solucion.

```txt
Problema claro
→ datos claros
→ algoritmo adecuado
→ resultado validado
```
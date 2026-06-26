## Proposito

Esta subcarpeta reune criterios para calcular, preparar, validar y usar rutas dentro de un mapa logico.

No existe para almacenar algoritmos puros.
No existe para explicar toda la IA del NPC.
No existe para decidir comportamientos.
No existe para resolver movimiento fisico completo.
No existe para aplicar A Star por costumbre.

Existe para responder:

```txt
¿Como usa un sistema de mapas una representacion navegable para obtener una ruta util?
```

---

## Idea central

Navegacion y pathfinding no son lo mismo que movimiento.

```txt
Mapa logico
→ ofrece estructura.

Algoritmo
→ calcula una ruta.

Sistema de navegacion
→ adapta esa ruta al caso concreto.

Movimiento
→ ejecuta desplazamiento.

NPC
→ decide por que quiere ir ahi.
```

Esta subcarpeta se enfoca en el puente entre mapa logico y ruta usable.

---

## Responsabilidad de esta subcarpeta

Esta subcarpeta debe explicar como preparar y usar rutas dentro de IA para desarrollo de mapas.

Su responsabilidad incluye:

```txt
entender que es pathfinding
adaptar algoritmos al mapa
suavizar rutas
desacoplar pathfinding de clases concretas
buscar nodos cercanos
conectar posiciones reales con nodos
validar rutas
separar calculo de ruta y movimiento
```

No es responsabilidad principal de esta subcarpeta explicar en profundidad:

```txt
A Star
Theta Star
Dijkstra
percepcion del jugador
estados de NPC
patrullaje
ataque
huida
movimiento fisico
```

Los algoritmos viven en `Algoritmos`.

Esta subcarpeta puede consumirlos, pero no duplicarlos.

---

## Diferencia entre algoritmo y aplicacion en mapas

Un algoritmo define un procedimiento general.

Una aplicacion en mapas define como ese procedimiento se usa sobre una representacion espacial concreta.

```txt
A Star
→ algoritmo.

Uso de A Star en un mapa de nodos
→ aplicacion dentro de mapas.

Theta Star
→ algoritmo.

Uso de Theta Star para rutas mas directas
→ aplicacion dentro de mapas.
```

Esta diferencia evita duplicar contenido y mezclar responsabilidades.

---

## Cuando usar esta subcarpeta

Usar esta subcarpeta cuando el problema sea:

```txt
un agente debe llegar a un destino variable
hay una representacion de mapa navegable
hay obstaculos o conexiones
hay multiples caminos posibles
hay que convertir posiciones reales en nodos
hay que suavizar una ruta
hay que desacoplar el algoritmo de una clase concreta
hay que validar visualmente un camino
```

Ejemplos:

```txt
Un enemigo debe llegar a cualquier punto del escenario.
→ revisar Pathfinding y Nodo mas cercano y target real.

Una ruta de A Star se ve demasiado angular.
→ revisar A Star suavizado.

El algoritmo depende directamente de PF_Node.
→ revisar Pathfinding generico.

El target no esta sobre un nodo.
→ revisar Nodo mas cercano y target real.
```

---

## Como usar esta subcarpeta

El flujo recomendado es:

```txt
1. Confirmar que existe una representacion de mapa.
2. Identificar origen real.
3. Identificar target real.
4. Buscar nodo cercano al origen si corresponde.
5. Buscar nodo cercano al target si corresponde.
6. Elegir algoritmo desde Algoritmos si hace falta.
7. Calcular ruta.
8. Adaptar o suavizar ruta si corresponde.
9. Entregar resultado al sistema consumidor.
10. Validar con debug visual.
```

La ruta calculada no debe confundirse con el movimiento final del agente.

---

## [[Pathfinding]]

Concepto general de calcular caminos dentro de una estructura navegable.

Usar esta nota para entender cuando hace falta pathfinding y que informacion minima necesita.

Pregunta principal:

```txt
¿Realmente necesito calcular una ruta?
```

---

## [[A Star suavizado]]

Aplicacion posterior a una ruta calculada con A Star para reducir puntos innecesarios o mejorar naturalidad del recorrido.

No reemplaza a A Star.

No reexplica A Star.

Pregunta principal:

```txt
¿La ruta calculada funciona, pero se ve demasiado angular?
```

---

## [[Pathfinding generico]]

Criterio para desacoplar el algoritmo de una clase concreta de nodo.

Sirve cuando el pathfinding no deberia depender directamente de `PF_Node`, `GridNode`, `MapNode` u otra implementacion especifica.

Pregunta principal:

```txt
¿Como hago que el algoritmo reciba funciones en vez de depender de una clase concreta?
```

---

## [[Nodo mas cercano y target real]]

Criterio para conectar posiciones reales del mundo con una estructura navegable basada en nodos.

Sirve cuando el origen o el destino no estan exactamente sobre un nodo.

Pregunta principal:

```txt
¿Como conecto una posicion real con una ruta por nodos?
```

---

## Algoritmos relacionados

Esta subcarpeta puede consumir algoritmos de la seccion `Algoritmos`.

Especialmente:

```txt
A Star
Theta Star
Dijkstra
```

Pero esos algoritmos no deben desarrollarse aca en profundidad.

La direccion correcta es:

```txt
Algoritmos
→ explica el procedimiento.

Navegacion y pathfinding
→ explica como ese procedimiento se aplica dentro del mapa.
```

---

## Sobre Line of Sight

Line of Sight es una validación de paso directo entre dos puntos.

Permite responder:

```txt
¿Existe una conexión directa válida entre este punto y este otro?
```

Dentro de navegación y pathfinding puede usarse para comprobar si una ruta puede simplificarse o si un algoritmo puede conectar puntos de forma más directa.

Puede alimentar:

```txt
A Star suavizado
Theta Star
validación de rutas
sistemas de cobertura
percepción de NPC
detección de jugador
```

Pero Line of Sight no queda encerrado como nota hija de esta carpeta.

Es una técnica transversal.

Por ahora se menciona dentro de las notas que la consumen.

Si más adelante aparece una necesidad real de reutilizarla en varios sistemas con mayor profundidad, puede convertirse en una nota propia dentro de VaultrumAi.

No se crea ahora solo por completismo.

---

## Relacion con la ultima clase de pathfinding avanzado

La ultima clase vuelve centrales estos problemas:

```txt
mapa de nodos propio
sin grilla obligatoria
nodo cercano al NPC
nodo cercano al target
ruta con A Star, A Star suavizado o Theta Star
llegada al target real
pathfinding generico
debug visual
costos dinamicos
```

La separacion correcta es:

```txt
Mapa de nodos propio
→ Representacion de mapa

A Star / Theta Star
→ Algoritmos

A Star suavizado
→ Navegacion y pathfinding

Nodo cercano y target real
→ Navegacion y pathfinding

Pathfinding generico
→ Navegacion y pathfinding

Costos dinamicos
→ Reglas de mapa

Debug visual
→ criterio de validacion de cada sistema
```

---

## Criterio para una IA

Antes de proponer una solución de pathfinding, una IA debe separar responsabilidades.

Debe poder responder:

```txt
¿Existe una representación navegable?
¿El destino es fijo o variable?
¿El origen y el target están sobre nodos?
¿Hace falta calcular una ruta o alcanzan waypoints?
¿Movimiento directo alcanza?
¿Qué algoritmo corresponde consultar?
¿A Star simple alcanza?
¿A Star suavizado alcanza?
¿Hace falta Theta Star?
¿La ruta necesita suavizado?
¿El algoritmo está acoplado a una clase concreta?
¿Cómo se entrega la ruta al sistema consumidor?
¿Cómo se valida visualmente?
```

No debe asumir que todo problema de movimiento requiere A Star.

No debe asumir que toda ruta angular necesita Theta Star.

No debe aplicar pathfinding complejo si una solución más simple cumple el rol.

Regla:

```txt
Primero problema de navegación.
Después estructura.
Después algoritmo.
Después adaptación.
Después sistema consumidor.
```

---

## Errores que esta subcarpeta ayuda a evitar

```txt
confundir pathfinding con movimiento
guardar algoritmos puros dentro de mapas
duplicar A Star en varias secciones
usar Theta Star sin justificarlo
meter pathfinding dentro del comportamiento del NPC
ignorar que el target puede no estar sobre un nodo
acoplar el algoritmo a una clase concreta sin necesidad
no validar rutas visualmente
```

---

## Criterio de links

Los links deben respetar direccion de dependencia.

```txt
Esta subcarpeta
→ puede linkear a algoritmos cuando los consume.

Algoritmos
→ no deben depender narrativamente de esta subcarpeta.

Notas base de representacion
→ no deben explicar esta subcarpeta.

Notas de pathfinding
→ pueden llamar a estructuras base cuando las necesitan.
```

Regla:

```txt
El consumidor llama al proveedor.
El proveedor no explica todos sus consumidores.
```

---

## Regla final

Navegacion y pathfinding no es una bolsa de algoritmos.

Es el puente entre una representacion del mapa y una ruta usable.

```txt
Mapa logico
→ algoritmo adecuado
→ ruta
→ sistema consumidor
```
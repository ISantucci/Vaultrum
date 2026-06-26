## Definicion

Pathfinding generico es una forma de diseñar el calculo de rutas para que no dependa directamente de una clase concreta de nodo.

En vez de escribir el algoritmo acoplado a `PF_Node`, `GridNode`, `MapNode` u otra clase especifica, el sistema recibe funciones para consultar vecinos, costos, heuristicas y condiciones.

No es un algoritmo nuevo.

No reemplaza a A Star, Dijkstra o Theta Star.

No decide comportamientos.

No mueve entidades.

Existe para desacoplar el calculo de caminos de la implementacion concreta del mapa.

```txt
Algoritmo
→ recibe funciones

Mapa concreto
→ provee datos

Resultado
→ ruta
```

---

## Responsabilidad de esta nota

Esta nota explica el criterio de hacer pathfinding desacoplado y reutilizable.

Su responsabilidad es definir:

```txt
que problema resuelve
que dependencias evita
que datos necesita
como se estructura
cuando conviene implementarlo
cuando no conviene implementarlo
que costo tiene
como validarlo
```

Esta nota no debe explicar en profundidad cada algoritmo.

Los algoritmos viven en la seccion `Algoritmos`.

---

## Problema que resuelve

El problema aparece cuando el algoritmo queda pegado a una clase concreta.

Ejemplo:

```txt
AStar
→ depende directamente de PF_Node
```

Esto hace que el algoritmo sea dificil de reutilizar si despues aparece:

```txt
GridNode
MapNode
WaypointNode
NavNode
otro tipo de nodo
```

Pregunta principal:

```txt
¿El algoritmo necesita conocer la clase concreta o solo necesita funciones?
```

---

## Idea central

Muchos algoritmos de pathfinding no necesitan saber que clase exacta representa el nodo.

Necesitan saber:

```txt
cuales son los vecinos
cuanto cuesta moverse
cuanto falta hasta el objetivo
si el nodo es valido
cuando se llego al objetivo
```

Entonces se puede pasar esa informacion mediante funciones.

```txt
getNeighbors
getCost
heuristic
isGoal
isValid
```

Esto permite que el algoritmo trabaje sobre tipos distintos.

---

## Datos que necesita

Un pathfinding generico puede necesitar:

```txt
nodo inicial
condicion de objetivo
funcion para obtener vecinos
funcion para calcular costo
funcion heuristica
funcion de validez
funcion de comparacion
```

Ejemplo:

```txt
start
goal
getNeighbors(node)
getCost(from, to)
heuristic(node, goal)
```

El algoritmo no necesita saber si el nodo viene de una grilla, un grafo o una lista manual.

---

## Que devuelve

El resultado puede ser:

```txt
lista de nodos genericos
lista de posiciones
ruta parcial
resultado fallido
```

Ejemplo:

```csharp
List<TNode>
```

La ruta devuelta debe ser interpretada por el sistema consumidor.

El algoritmo no debe mover entidades.

---

## Diferencia con pathfinding acoplado

Pathfinding acoplado:

```txt
AStar recibe PF_Node.
AStar llama directamente a PF_Node.Neighbors.
AStar depende de PF_Node.Cost.
```

Pathfinding generico:

```txt
AStar recibe TNode.
AStar llama a getNeighbors(TNode).
AStar llama a getCost(TNode, TNode).
AStar llama a heuristic(TNode, TNode).
```

La segunda opcion es mas flexible.

Pero tambien puede ser mas abstracta.

Debe usarse cuando esa flexibilidad tiene sentido.

---

## Ejemplo conceptual en codigo

```csharp
using System;
using System.Collections.Generic;

public static class GenericPathfinding
{
    public static List<TNode> FindPath<TNode>(
        TNode start,
        TNode goal,
        Func<TNode, IEnumerable<TNode>> getNeighbors,
        Func<TNode, TNode, float> getCost,
        Func<TNode, TNode, float> heuristic)
    {
        // Aca podria usarse A Star, Dijkstra u otro algoritmo.
        // Lo importante es que el algoritmo no depende de una clase concreta.

        return AStar.FindPath(
            start,
            goal,
            getNeighbors,
            getCost,
            heuristic
        );
    }
}
```

Ejemplo de uso con `GridNode`:

```csharp
List<GridNode> path = GenericPathfinding.FindPath(
    startNode,
    goalNode,
    node => gridMap.GetOrthogonalNeighbors(node),
    (from, to) => to.BaseCost,
    (from, to) => Vector2Int.Distance(from.Coordinates, to.Coordinates)
);
```

Ejemplo de uso con `MapNode`:

```csharp
List<MapNode> path = GenericPathfinding.FindPath(
    startNode,
    goalNode,
    node => node.Neighbors,
    (from, to) => Vector3.Distance(from.Position, to.Position) + to.BaseCost,
    (from, to) => Vector3.Distance(from.Position, to.Position)
);
```

El algoritmo es el mismo.

Los datos vienen de cada estructura.

---

## Contrato minimo

Un sistema de pathfinding generico debe definir un contrato.

Ejemplo:

```txt
Para cualquier TNode necesito poder saber:

vecinos
costo
heuristica
si es valido
si es objetivo
```

Ese contrato puede venir por funciones o interfaces.

Con funciones:

```csharp
Func<TNode, IEnumerable<TNode>> getNeighbors
Func<TNode, TNode, float> getCost
Func<TNode, TNode, float> heuristic
```

Con interfaz:

```csharp
public interface IPathNode<TNode>
{
    IEnumerable<TNode> GetNeighbors();
}
```

La opcion depende del proyecto.

---

## Cuando implementar pathfinding generico

Conviene implementar pathfinding generico cuando:

```txt
el algoritmo podria usarse con distintos tipos de nodo
hay varias representaciones de mapa
se quiere desacoplar algoritmo y datos
se quiere testear el algoritmo sin Unity
se quiere evitar dependencia directa de MonoBehaviour
se quiere reutilizar A Star, Dijkstra u otro algoritmo
el proyecto puede crecer en tipos de mapas
```

Ejemplo correcto:

```txt
El proyecto tiene GridNode para mapas tacticos
y MapNode para mapas libres.

Ambos necesitan rutas.

→ Pathfinding generico tiene sentido.
```

---

## Cuando NO implementar pathfinding generico

No conviene implementarlo cuando:

```txt
solo existe un tipo de nodo
el sistema es muy chico
la abstraccion agrega confusion
nadie va a reutilizar el algoritmo
el proyecto necesita una solucion rapida y simple
la flexibilidad no aporta valor real
```

Ejemplo:

```txt
Prototipo con una unica grilla simple para una entrega corta.

→ Un pathfinding concreto puede alcanzar.
```

No todo sistema necesita generics.

---

## Por que no implementarlo de mas

La abstraccion tambien tiene costo.

Puede generar:

```txt
mas dificultad de lectura
mas parametros
mas delegados
mas errores de configuracion
mas distancia entre algoritmo y datos
mas dificultad para debuggear
```

Regla:

```txt
Desacoplar tiene sentido cuando reduce dependencia real.
No cuando solo hace el codigo mas elegante.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
hacer generico un sistema que nunca se reutiliza
usar nombres genericos que nadie entiende
pasar demasiadas funciones sin documentar
ocultar reglas importantes dentro de lambdas
hacer dificil debuggear costos y vecinos
usar abstraccion para evitar decidir una estructura
mezclar generics con MonoBehaviours innecesariamente
```

Ejemplo de mala practica:

```txt
Crear un Pathfinding<TNode, TCost, TContext, TAgent>
cuando el juego solo tiene un tipo de mapa y un solo enemigo.
```

Eso es sobrearquitectura.

---

## Costos de implementacion

Implementar pathfinding generico requiere:

```txt
definir contrato de datos
pasar funciones correctamente
testear con mas de un tipo de nodo
documentar que significa cada funcion
manejar errores de configuracion
mantener debug legible
separar algoritmo de Unity si corresponde
```

No es solo cambiar una clase por `TNode`.

Hay que asegurar que la abstraccion se entienda.

---

## Costos de optimizacion

El costo depende de la implementacion.

Posibles costos:

```txt
overhead por delegados o funciones
allocations si se crean colecciones nuevas
costo por enumeradores
costo por lambdas mal usadas
dificultad para cachear vecinos
dificultad para perfilar si todo esta demasiado abstracto
```

En la mayoria de casos, el costo puede ser aceptable.

Pero en sistemas con muchos agentes y muchas busquedas, debe medirse.

---

## Criterio de optimizacion

Para reducir costo:

```txt
evitar crear listas nuevas en cada getNeighbors
reutilizar colecciones internas
cachear vecinos si el mapa no cambia
evitar LINQ en loops criticos
medir frecuencia de llamadas
testear con cantidad real de agentes
mantener debug activable/desactivable
```

Ejemplo:

```txt
Mala practica:
getNeighbors crea una nueva lista para cada nodo explorado.

Mejor:
usar colecciones reutilizables,
cachear vecinos,
o devolver una coleccion existente si es seguro.
```

---

## Preguntas antes de implementar

Antes de implementar pathfinding generico, una IA debe responder:

```txt
¿Hay mas de un tipo de nodo?
¿El algoritmo se va a reutilizar?
¿Que dependencia concreta se quiere eliminar?
¿La abstraccion mejora mantenibilidad?
¿La abstraccion complica demasiado?
¿Como se van a pasar vecinos?
¿Como se van a pasar costos?
¿Como se va a debuggear?
¿Como se va a testear?
¿Que costo puede tener?
```

Si no hay una dependencia real que resolver, no conviene generizar.

---

## Errores comunes

```txt
confundir generico con mejor
hacer generico sin necesidad
pasar funciones mal nombradas
ocultar reglas de mapa dentro del algoritmo
perder trazabilidad de costos
acoplar igual el algoritmo a Unity
hacer dificil leer el flujo
no testear con mas de una estructura
```

---

## Criterio para una IA

Cuando una IA proponga pathfinding generico, debe justificar:

```txt
que clase concreta se quiere desacoplar
que tipos de nodo podrian usarlo
que contrato minimo necesita
que funciones se pasan
que algoritmo queda reutilizable
que complejidad agrega
que beneficio real aporta
como se valida
```

No alcanza con decir:

```txt
Hacerlo generico.
```

Debe explicar que dependencia concreta se esta eliminando.

---

## Checklist

Antes de implementar pathfinding generico, revisar:

```txt
¿Existe una dependencia concreta que molesta?
¿Hay mas de una estructura que pueda consumirlo?
¿El algoritmo puede vivir separado del nodo?
¿Los vecinos pueden pasarse como funcion?
¿Los costos pueden pasarse como funcion?
¿La heuristica puede pasarse como funcion?
¿El resultado sigue siendo entendible?
¿El debug sigue siendo claro?
¿El costo de abstraccion esta justificado?
¿Se evito sobrearquitectura?
```

---

## Regla final

Pathfinding generico no existe para hacer codigo mas sofisticado.

Existe para evitar dependencias innecesarias cuando hay una razon real.

```txt
Dependencia concreta molesta
→ contrato generico
→ algoritmo reutilizable
→ sistema consumidor interpreta
```
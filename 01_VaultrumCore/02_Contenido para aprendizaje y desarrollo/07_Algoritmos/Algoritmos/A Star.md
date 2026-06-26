## Definicion

A Star, tambien escrito como A*, es un algoritmo de busqueda de caminos que combina costo acumulado y estimacion hacia un objetivo.

Sirve para encontrar una ruta desde un origen hasta un destino dentro de una estructura navegable.

No crea el mapa.

No decide que quiere hacer un NPC.

No mueve entidades.

No reemplaza al sistema de navegacion.

A Star calcula una ruta usando informacion disponible.

```txt
Costo acumulado
+
Estimacion hacia el objetivo
=
Prioridad de busqueda
```

---

## Responsabilidad de esta nota

Esta nota explica A Star como algoritmo.

Su responsabilidad es definir:

```txt
que problema resuelve
que datos necesita
como funciona
que resultado devuelve
cuando conviene usarlo
cuando no conviene usarlo
que errores evita
que riesgos tiene
```

Esta nota no debe explicar todo el sistema de mapas, NPCs o movimiento.

Los sistemas que usen A Star deben referenciar este algoritmo desde su propio contexto.

---

## Problema que resuelve

A Star resuelve el problema de buscar un camino hacia un objetivo concreto.

Se usa cuando existe:

```txt
un punto de origen
un punto de destino
una estructura navegable
vecinos o conexiones
costos
una forma de estimar distancia al objetivo
```

Pregunta principal:

```txt
¿Cual parece ser el mejor camino hacia este objetivo?
```

---

## Datos que necesita

A Star necesita informacion como:

```txt
nodo inicial
nodo objetivo
vecinos de cada nodo
costo para moverse entre nodos
heuristica hacia el objetivo
condicion de bloqueo o validez
```

No necesita conocer el comportamiento del NPC.

No necesita conocer la UI.

No necesita saber por que el objetivo fue elegido.

Solo necesita datos para calcular una ruta.

---

## Resultado que devuelve

A Star normalmente devuelve:

```txt
una lista de nodos
una lista de posiciones
una ruta parcial
ninguna ruta si el objetivo no es alcanzable
```

Ejemplo:

```txt
Inicio
→ Nodo A

Objetivo
→ Nodo F

Resultado
→ A → B → D → F
```

El resultado debe ser consumido por otro sistema.

El algoritmo no deberia ejecutar el movimiento.

---

## Como funciona

A Star usa una formula comun:

```txt
F = G + H
```

Donde:

```txt
G
→ costo acumulado desde el origen hasta el nodo actual.

H
→ estimacion desde el nodo actual hasta el objetivo.

F
→ prioridad total usada para elegir que nodo revisar.
```

El algoritmo prioriza nodos con menor `F`.

Flujo conceptual:

```txt
1. Agregar el nodo inicial a la lista abierta.
2. Calcular su G, H y F.
3. Tomar el nodo con menor F.
4. Revisar sus vecinos.
5. Ignorar vecinos invalidos o bloqueados.
6. Calcular nuevo costo G.
7. Actualizar el camino si el nuevo costo es mejor.
8. Repetir hasta llegar al objetivo.
9. Reconstruir la ruta final.
```

---

## Heuristica

La heuristica es una estimacion del costo hasta el objetivo.

Puede basarse en:

```txt
distancia Manhattan
distancia Euclidiana
distancia Chebyshev
distancia personalizada
```

La heuristica ayuda a orientar la busqueda.

Una mala heuristica puede hacer que el algoritmo explore de mas o elija caminos incorrectos segun el caso.

---

## Diferencia con Dijkstra

Dijkstra usa costo acumulado.

A Star usa costo acumulado mas heuristica.

```txt
Dijkstra
→ explora segun menor costo acumulado.

A Star
→ explora segun menor costo acumulado + estimacion al objetivo.
```

A Star suele ser mas dirigido cuando hay un destino concreto.

Dijkstra puede ser mas adecuado cuando se necesitan distancias desde un origen hacia muchos destinos o cuando no se quiere usar heuristica.

---

## Ejemplo conceptual en codigo

```csharp
using System;
using System.Collections.Generic;

public static class AStar
{
    public static List<TNode> FindPath<TNode>(
        TNode start,
        TNode goal,
        Func<TNode, IEnumerable<TNode>> getNeighbors,
        Func<TNode, TNode, float> getCost,
        Func<TNode, TNode, float> heuristic)
    {
        List<TNode> openSet = new() { start };
        HashSet<TNode> closedSet = new();

        Dictionary<TNode, TNode> cameFrom = new();
        Dictionary<TNode, float> gCost = new();
        Dictionary<TNode, float> fCost = new();

        gCost[start] = 0f;
        fCost[start] = heuristic(start, goal);

        while (openSet.Count > 0)
        {
            TNode current = GetLowest(openSet, fCost);

            if (EqualityComparer<TNode>.Default.Equals(current, goal))
            {
                return ReconstructPath(current, cameFrom);
            }

            openSet.Remove(current);
            closedSet.Add(current);

            foreach (TNode neighbor in getNeighbors(current))
            {
                if (closedSet.Contains(neighbor)) continue;

                float tentativeG = gCost[current] + getCost(current, neighbor);

                if (!openSet.Contains(neighbor))
                {
                    openSet.Add(neighbor);
                }
                else if (gCost.ContainsKey(neighbor) && tentativeG >= gCost[neighbor])
                {
                    continue;
                }

                cameFrom[neighbor] = current;
                gCost[neighbor] = tentativeG;
                fCost[neighbor] = tentativeG + heuristic(neighbor, goal);
            }
        }

        return new List<TNode>();
    }

    private static TNode GetLowest<TNode>(List<TNode> nodes, Dictionary<TNode, float> fCost)
    {
        TNode best = nodes[0];
        float bestCost = fCost.ContainsKey(best) ? fCost[best] : float.PositiveInfinity;

        foreach (TNode node in nodes)
        {
            float cost = fCost.ContainsKey(node) ? fCost[node] : float.PositiveInfinity;

            if (cost < bestCost)
            {
                best = node;
                bestCost = cost;
            }
        }

        return best;
    }

    private static List<TNode> ReconstructPath<TNode>(
        TNode current,
        Dictionary<TNode, TNode> cameFrom)
    {
        List<TNode> path = new() { current };

        while (cameFrom.ContainsKey(current))
        {
            current = cameFrom[current];
            path.Add(current);
        }

        path.Reverse();
        return path;
    }
}
```

Este ejemplo muestra A Star desacoplado de una clase concreta de nodo.

El algoritmo recibe funciones.

No depende directamente de `GridNode`, `MapNode` o `PF_Node`.

---

## Cuando conviene usarlo

Conviene usar A Star cuando:

```txt
hay un destino concreto
hay una estructura navegable
hay obstaculos o caminos posibles
hay costos
se quiere orientar la busqueda hacia el objetivo
la ruta debe calcularse en tiempo razonable
```

Ejemplos:

```txt
enemigo que busca llegar al jugador
unidad que navega por una grilla
agente que debe rodear obstaculos
sistema que calcula rutas en un mapa con nodos
```

---

## Cuando NO conviene usarlo

No conviene usar A Star cuando:

```txt
el recorrido es fijo
no hay caminos alternativos
no hay estructura navegable
una lista de waypoints alcanza
se necesitan distancias a muchos destinos
la heuristica no aporta valor
el mapa cambia tanto que recalcular siempre seria costoso
```

A Star no debe usarse solo porque suena avanzado.

---

## Errores comunes

```txt
usar A Star sin mapa logico
confundir ruta con movimiento
meter comportamiento de NPC dentro del algoritmo
usar una heuristica incorrecta
ignorar costos
ignorar nodos bloqueados
recalcular demasiado seguido
no validar visualmente la ruta
acoplar el algoritmo a una clase concreta sin necesidad
```

---

## Criterio para una IA

Cuando una IA proponga A Star, debe justificar:

```txt
por que hay un problema de busqueda de camino
cual es el origen
cual es el destino
que estructura consume
como obtiene vecinos
como calcula costos
que heuristica usa
que devuelve
que sistema consume la ruta
como se valida
```

---

## Checklist

Antes de usar A Star, revisar:

```txt
¿Existe un destino concreto?
¿Existe una estructura navegable?
¿Los vecinos estan definidos?
¿Los costos estan definidos?
¿La heuristica tiene sentido?
¿Hay nodos bloqueados?
¿El algoritmo esta separado del movimiento?
¿El comportamiento del NPC esta separado?
¿La ruta puede debuggearse?
```

---

## Regla final

A Star no mueve.

A Star no decide.

A Star calcula.

```txt
Datos navegables
→ A Star
→ ruta
→ sistema consumidor
```
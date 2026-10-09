## Definicion

Dijkstra es un algoritmo que calcula caminos de menor costo dentro de una estructura con conexiones y pesos no negativos.

Sirve para encontrar la ruta mas barata desde un origen hacia uno o varios destinos.

No crea la estructura.

No decide comportamientos.

No mueve entidades.

No reemplaza al sistema que consume la ruta.

Dijkstra procesa costos acumulados.

```txt
Origen
→ conexiones con costos
→ camino de menor costo
```

---

## Responsabilidad de esta nota

Esta nota explica Dijkstra como algoritmo.

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

Esta nota no debe explicar todo el sistema de mapas, NPCs o grafos.

Los sistemas que usen Dijkstra deben referenciar este algoritmo desde su propio contexto.

---

## Problema que resuelve

Dijkstra resuelve el problema de encontrar el camino de menor costo considerando pesos acumulados.

Pregunta principal:

```txt
¿Cual es el camino mas barato desde este origen?
```

Ejemplo:

```txt
A → B cuesta 2
B → C cuesta 3
A → C cuesta 10

Camino mas barato:
A → B → C

Costo total:
5
```

Dijkstra no elige por la conexion local mas barata.

Evalua costos acumulados.

---

## Datos que necesita

Dijkstra necesita informacion como:

```txt
nodo inicial
nodos disponibles
vecinos o conexiones
costo de cada conexion
estado valido o invalido
criterio de destino si corresponde
```

Los costos deben ser no negativos.

Si existen costos negativos, Dijkstra no es el algoritmo adecuado.

---

## Resultado que devuelve

Dijkstra puede devolver:

```txt
camino de menor costo hacia un destino
costos minimos desde un origen hacia muchos nodos
tabla de distancias
nodo previo para reconstruir caminos
ninguna ruta si el destino no es alcanzable
```

El resultado debe ser consumido por otro sistema.

El algoritmo no deberia ejecutar movimiento.

---

## Como funciona

Flujo conceptual:

```txt
1. Asignar costo 0 al nodo inicial.
2. Asignar infinito al resto.
3. Elegir el nodo no visitado con menor costo acumulado.
4. Revisar sus vecinos.
5. Calcular nuevo costo acumulado.
6. Actualizar si el nuevo costo es menor.
7. Marcar el nodo como visitado.
8. Repetir hasta terminar o llegar al destino.
9. Reconstruir camino si corresponde.
```

La idea central es:

```txt
Siempre expandir primero el costo acumulado mas bajo conocido.
```

---

## Diferencia con A Star

Dijkstra usa solo costo acumulado.

A Star usa costo acumulado mas heuristica.

```txt
Dijkstra
→ explora por menor costo acumulado.

A Star
→ explora por menor costo acumulado + estimacion al objetivo.
```

Dijkstra puede ser mejor cuando:

```txt
no hay un objetivo unico
se necesitan distancias a muchos nodos
no se quiere depender de una heuristica
se busca costo minimo general desde un origen
```

---

## Ejemplo conceptual en codigo

```csharp
using System;
using System.Collections.Generic;

public static class Dijkstra
{
    public static Dictionary<TNode, float> CalculateDistances<TNode>(
        TNode start,
        Func<TNode, IEnumerable<TNode>> getNeighbors,
        Func<TNode, TNode, float> getCost)
    {
        List<TNode> openSet = new() { start };
        HashSet<TNode> visited = new();
        Dictionary<TNode, float> distances = new();

        distances[start] = 0f;

        while (openSet.Count > 0)
        {
            TNode current = GetLowest(openSet, distances);

            openSet.Remove(current);
            visited.Add(current);

            foreach (TNode neighbor in getNeighbors(current))
            {
                if (visited.Contains(neighbor)) continue;

                float newDistance = distances[current] + getCost(current, neighbor);

                if (!distances.ContainsKey(neighbor) || newDistance < distances[neighbor])
                {
                    distances[neighbor] = newDistance;

                    if (!openSet.Contains(neighbor))
                    {
                        openSet.Add(neighbor);
                    }
                }
            }
        }

        return distances;
    }

    private static TNode GetLowest<TNode>(
        List<TNode> nodes,
        Dictionary<TNode, float> distances)
    {
        TNode best = nodes[0];
        float bestDistance = distances.ContainsKey(best)
            ? distances[best]
            : float.PositiveInfinity;

        foreach (TNode node in nodes)
        {
            float distance = distances.ContainsKey(node)
                ? distances[node]
                : float.PositiveInfinity;

            if (distance < bestDistance)
            {
                best = node;
                bestDistance = distance;
            }
        }

        return best;
    }
}
```

Este ejemplo muestra Dijkstra desacoplado de una clase concreta.

El algoritmo recibe funciones para obtener vecinos y costos.

---

## Cuando conviene usarlo

Conviene usar Dijkstra cuando:

```txt
hay costos no negativos
se busca camino de menor costo
no hay una buena heuristica
se necesitan distancias desde un origen
se quiere calcular costo hacia varios destinos
se trabaja sobre conexiones con pesos
```

Ejemplos:

```txt
calcular ruta mas barata
evaluar caminos disponibles
calcular distancias desde una base
analizar costos de un mapa
```

---

## Cuando NO conviene usarlo

No conviene usar Dijkstra cuando:

```txt
no hay costos
el recorrido es fijo
hay un destino concreto y una buena heuristica
A Star seria mas eficiente
hay costos negativos
una solucion simple alcanza
```

Dijkstra no debe usarse solo porque hay movimiento.

---

## Errores comunes

```txt
usar Dijkstra sin costos reales
usar Dijkstra con costos negativos
confundir camino mas corto con camino mas barato
mezclar el algoritmo con movimiento
meter comportamiento de NPC dentro del algoritmo
no reconstruir correctamente el camino
no validar rutas visualmente
usar Dijkstra cuando A Star seria mas adecuado
```

---

## Criterio para una IA

Cuando una IA proponga Dijkstra, debe justificar:

```txt
por que se necesita costo minimo
que estructura consume
que representan los costos
si los costos son no negativos
si hay un destino o muchos destinos
que resultado devuelve
que sistema consume el resultado
como se valida
```

---

## Checklist

Antes de usar Dijkstra, revisar:

```txt
¿Hay costos no negativos?
¿Existe estructura con conexiones?
¿Se busca menor costo acumulado?
¿Hace falta ruta a un destino o distancias a varios?
¿A Star seria mejor?
¿El algoritmo esta separado del movimiento?
¿El comportamiento esta separado?
¿Se puede validar el resultado?
```

---

## Regla final

Dijkstra no decide por donde ir porque si.

Calcula menor costo acumulado.

```txt
Estructura con costos
→ Dijkstra
→ distancias o ruta
→ sistema consumidor
```
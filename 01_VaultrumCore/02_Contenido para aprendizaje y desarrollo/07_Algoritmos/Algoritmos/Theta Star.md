## Definicion

Theta Star, tambien escrito como Theta*, es un algoritmo de pathfinding any-angle basado en A Star.

Su objetivo es encontrar rutas mas directas permitiendo conectar puntos que tienen linea de vision entre si.

No crea el mapa.

No decide comportamientos.

No reemplaza al movimiento.

No es simplemente A Star con otro nombre.

Theta Star modifica la forma de construir la ruta usando visibilidad directa entre puntos.

```txt
A Star
→ busca por vecinos.

Theta Star
→ busca por vecinos y aprovecha line of sight para reducir quiebres.
```

---

## Responsabilidad de esta nota

Esta nota explica Theta Star como algoritmo.

Su responsabilidad es definir:

```txt
que problema resuelve
que datos necesita
como se diferencia de A Star
como usa line of sight
cuando conviene usarlo
cuando no conviene usarlo
que riesgos tiene
```

Esta nota no debe convertirse en una guia completa de mapas, NPCs o percepcion.

Los sistemas que usen Theta Star deben referenciar este algoritmo desde su propio contexto.

---

## Problema que resuelve

Theta Star resuelve el problema de obtener rutas menos angulares en mapas donde A Star puede producir caminos demasiado quebrados.

Esto suele pasar cuando la ruta se calcula sobre:

```txt
grillas
nodos
conexiones discretas
mapas con vecinos limitados
```

Pregunta principal:

```txt
¿Puedo llegar de forma mas directa sin seguir cada quiebre de la estructura?
```

---

## Idea central

A Star suele construir rutas pasando de nodo en nodo.

Theta Star intenta mejorar eso preguntando:

```txt
¿El padre del nodo actual tiene linea directa hacia el vecino?
```

Si la respuesta es si, puede conectar el vecino con un nodo anterior y reducir puntos intermedios.

```txt
Ruta angular
→ A → B → C → D

Ruta mas directa
→ A → D
```

Siempre que exista visibilidad o paso directo valido.

---

## Datos que necesita

Theta Star necesita informacion como:

```txt
nodo inicial
nodo objetivo
vecinos
costos
heuristica
line of sight entre puntos
validacion de obstaculos
estructura navegable
```

La diferencia clave frente a A Star es que Theta Star necesita una funcion confiable de line of sight.

Sin esa validacion, puede generar rutas que atraviesan obstaculos.

---

## Resultado que devuelve

Theta Star normalmente devuelve:

```txt
una lista de nodos
una lista de puntos
una ruta mas directa
una ruta con menos cambios de direccion
ninguna ruta si el objetivo no es alcanzable
```

El resultado debe ser ejecutado por otro sistema.

Theta Star no mueve entidades.

---

## Como funciona

Theta Star parte de una logica similar a A Star.

Pero al evaluar un vecino, intenta mejorar la ruta usando el padre del nodo actual.

Flujo conceptual:

```txt
1. Iniciar busqueda como A Star.
2. Tomar el nodo con menor prioridad.
3. Revisar vecinos.
4. Preguntar si el padre del nodo actual tiene line of sight hacia el vecino.
5. Si tiene vision directa, intentar conectar el vecino con ese padre.
6. Si no tiene vision directa, conectar como A Star tradicional.
7. Repetir hasta llegar al objetivo.
8. Reconstruir ruta.
```

La diferencia importante esta en la actualizacion del padre.

---

## Line of sight

Line of sight significa verificar si hay una linea directa valida entre dos puntos.

Puede usarse para saber si entre esos puntos hay:

```txt
paredes
obstaculos
zonas bloqueadas
terreno invalido
interrupciones
```

Theta Star depende de esta verificacion.

Si line of sight esta mal implementado, la ruta puede parecer buena pero ser imposible.

---

## Diferencia con A Star suavizado

A Star suavizado y Theta Star buscan reducir rutas demasiado angulares, pero lo hacen en momentos distintos del proceso.

A Star suavizado funciona como post-proceso:

```txt
1. A Star calcula una ruta.
2. Después se intenta simplificar esa ruta.
3. Line of Sight valida si se pueden saltear puntos intermedios.
```

Theta Star integra esa lógica durante la búsqueda:

```txt
1. Busca camino.
2. Mientras explora vecinos, revisa si existe line of sight con nodos anteriores.
3. Si la conexión directa es válida, actualiza el padre para generar una ruta más directa.
```

Comparación:

```txt
A Star suavizado
→ mejora una ruta ya calculada.

Theta Star
→ construye una ruta más directa durante el cálculo.
```

A Star suavizado puede ser suficiente cuando la ruta de A Star ya es válida y solo necesita mejorar su forma.

Theta Star puede tener sentido cuando el problema de rutas angulares aparece de forma recurrente y existe una validación confiable de line of sight.

No conviene usar Theta Star solo porque parece más avanzado.

Si el suavizado posterior alcanza, puede ser una solución más simple y suficiente.

Para el criterio de suavizado como post-proceso, ver `A Star suavizado`.

---

## Ejemplo conceptual en pseudocodigo

```txt
Para cada vecino del nodo actual:

si parent[current] tiene line of sight hacia neighbor:
    evaluar costo desde parent[current] hasta neighbor
    si mejora:
        parent[neighbor] = parent[current]
        actualizar costos
si no:
    evaluar costo desde current hasta neighbor
    si mejora:
        parent[neighbor] = current
        actualizar costos
```

La idea central es que el vecino no siempre hereda como padre al nodo actual.

Puede heredar un nodo anterior si existe paso directo.

---

## Ejemplo conceptual en codigo

```csharp
public interface ILineOfSight<TNode>
{
    bool HasLineOfSight(TNode from, TNode to);
}
```

```csharp
public static class ThetaStarConcept
{
    public static void UpdateVertex<TNode>(
        TNode current,
        TNode neighbor,
        Dictionary<TNode, TNode> parent,
        Dictionary<TNode, float> gCost,
        Func<TNode, TNode, float> getCost,
        Func<TNode, TNode, bool> hasLineOfSight)
    {
        TNode currentParent = parent.ContainsKey(current) ? parent[current] : current;

        if (hasLineOfSight(currentParent, neighbor))
        {
            float newCost = gCost[currentParent] + getCost(currentParent, neighbor);

            if (!gCost.ContainsKey(neighbor) || newCost < gCost[neighbor])
            {
                parent[neighbor] = currentParent;
                gCost[neighbor] = newCost;
            }
        }
        else
        {
            float newCost = gCost[current] + getCost(current, neighbor);

            if (!gCost.ContainsKey(neighbor) || newCost < gCost[neighbor])
            {
                parent[neighbor] = current;
                gCost[neighbor] = newCost;
            }
        }
    }
}
```

Este ejemplo muestra solo la idea de actualizacion.

No es una implementacion completa.

---

## Cuando conviene usarlo

Conviene evaluar Theta Star cuando:

```txt
A Star genera rutas demasiado angulares
se necesita movimiento mas natural
existe una buena funcion de line of sight
el mapa permite rutas any-angle
el costo extra de visibilidad es aceptable
la calidad de la ruta justifica la complejidad
```

Ejemplos:

```txt
agentes que se mueven en espacios abiertos
mapas donde las rutas por grilla se ven artificiales
sistemas que necesitan menos puntos intermedios
```

---

## Cuando NO conviene usarlo

No conviene usar Theta Star cuando:

```txt
A Star simple alcanza
A Star suavizado alcanza
no hay line of sight confiable
el mapa es estrictamente por celdas
el movimiento debe respetar una grilla dura
el costo de verificar visibilidad es alto
la ruta directa puede romper reglas del diseño
```

Theta Star no debe aplicarse solo porque parece mas avanzado.

---

## Errores comunes

```txt
usar Theta Star sin line of sight confiable
generar rutas que atraviesan obstaculos
confundir any-angle con ignorar reglas del mapa
usar Theta Star cuando A Star suavizado alcanza
no validar visualmente las rutas
mezclar el algoritmo con movimiento
mezclar el algoritmo con percepcion del NPC
```

---

## Criterio para una IA

Cuando una IA proponga Theta Star, debe justificar:

```txt
por que A Star simple no alcanza
por que A Star suavizado no alcanza
como se calcula line of sight
que obstaculos se consideran
que estructura consume
que resultado devuelve
que costo extra tiene
como se valida visualmente
```

---

## Checklist

Antes de usar Theta Star, revisar:

```txt
¿El mapa permite movimiento any-angle?
¿Existe line of sight confiable?
¿A Star simple genera rutas malas?
¿A Star suavizado seria suficiente?
¿El costo extra esta justificado?
¿La ruta respeta obstaculos?
¿La ruta respeta reglas de gameplay?
¿El algoritmo esta separado del movimiento?
¿Se puede debuggear visualmente?
```

---

## Regla final

Theta Star no es “A Star mejor”.

Es una variante mas especifica.

```txt
Si la ruta angular es un problema real
y line of sight es confiable
→ Theta Star puede tener sentido.
```
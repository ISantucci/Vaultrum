## Definicion

Un grafo es una estructura de datos formada por nodos y conexiones.

```txt
Nodo
→ punto, entidad o estado.

Conexion
→ relacion entre nodos.
```

Un grafo permite representar informacion donde lo importante no es solo guardar elementos, sino tambien saber como se conectan.

Ejemplo conceptual:

```txt
A conectado con B
B conectado con C
A conectado con D
D conectado con C
```

Representacion:

```txt
A ─ B ─ C
│       │
D ──────┘
```

En videojuegos, los grafos son muy utiles para representar mapas, rutas, zonas, decisiones, relaciones y sistemas conectados.

---

## Responsabilidad

La responsabilidad de un grafo es representar relaciones entre elementos.

Debe responder:

```txt
¿Que nodos existen?
¿Que conexiones existen?
¿Desde este nodo a cuales puedo ir?
¿Que costo tiene una conexion?
¿Hay camino entre dos nodos?
```

Un grafo organiza conexiones.

No decide por si solo que camino conviene.

Ejemplo:

```txt
Grafo
→ representa nodos y conexiones.

Algoritmo de pathfinding
→ calcula ruta.

NPC o sistema consumidor
→ usa la ruta para moverse.
```

---

## Que NO debe hacer

Un grafo no debe absorber responsabilidades del sistema que lo usa.

No debe:

```txt
decidir comportamiento del NPC
mover personajes
calcular siempre la mejor ruta por si mismo
aplicar daño
actualizar UI
resolver reglas de gameplay
crear enemigos
decidir dificultad
```

Ejemplo incorrecto:

```txt
Grafo
→ detecta jugador
→ decide perseguir
→ calcula ruta
→ mueve enemigo
→ ataca
```

Ejemplo correcto:

```txt
PathGraph
→ guarda nodos y conexiones.

Pathfinding
→ calcula ruta sobre el grafo.

EnemyMovement
→ sigue la ruta.

NPCDecision
→ decide si necesita moverse.
```

Regla:

```txt
Grafo representa conexiones.
No decide gameplay.
```

---

## Que problema resuelve

Un grafo resuelve problemas donde los datos tienen relaciones o caminos posibles.

Casos que puede resolver:

```txt
mapas conectados
rutas alternativas
pathfinding
zonas navegables
arboles de dialogo no lineales
relaciones entre habitaciones
sistemas de nodos
conexiones entre objetivos
redes de transporte
mapas de decision
```

Ejemplo:

```txt
Un NPC esta en Nodo A.
Quiere llegar a Nodo C.

No alcanza con saber que existen A y C.
Tambien necesita saber:

A conecta con B.
B conecta con C.
A conecta con D.
D conecta con C.
```

Esto permite que un algoritmo decida por donde ir.

Idea central:

```txt
Si importan las conexiones entre elementos,
un grafo suele ser una buena opcion.
```

---

## Datos que necesita

Un grafo puede necesitar:

```txt
nodos
conexiones
costos
direccion de conexiones
estado de bloqueo
peso de cada conexion
posicion de cada nodo
datos extra por nodo
```

Ejemplo:

```txt
Nodo
→ posicion en mundo
→ si esta desbloqueado
→ tipo de zona

Conexion
→ nodo origen
→ nodo destino
→ costo
→ si esta habilitada
```

No todos los grafos necesitan costos.

Ejemplo simple:

```txt
Habitacion A conectada con Habitacion B
```

Ejemplo con costo:

```txt
Nodo A hacia Nodo B
→ costo 5

Nodo A hacia Nodo C
→ costo 12
```

---

## Que produce

Un grafo puede producir:

```txt
lista de nodos
vecinos de un nodo
conexiones de un nodo
costo entre nodos conectados
estado de una conexion
```

Operaciones comunes:

```txt
Agregar nodo
Agregar conexion
Obtener vecinos
Consultar costo
Bloquear conexion
Desbloquear conexion
```

La salida del grafo debe ser interpretada por algoritmos o sistemas consumidores.

Ejemplo:

```txt
GetNeighbors(A)
→ devuelve B y D.

Pathfinding
→ evalua esos vecinos.
```

---

## Como funciona

Un grafo puede representarse de varias formas.

Una forma comun es una lista de adyacencia.

```txt
A → B, D
B → A, C
C → B, D
D → A, C
```

Ejemplo conceptual en C#:

```csharp
using System.Collections.Generic;
using UnityEngine;

public class GraphNode
{
    public string Id { get; }
    public Vector3 Position { get; }

    public GraphNode(string id, Vector3 position)
    {
        Id = id;
        Position = position;
    }
}
```

```csharp
using System.Collections.Generic;

public class Graph
{
    private readonly Dictionary<GraphNode, List<GraphNode>> adjacency =
        new Dictionary<GraphNode, List<GraphNode>>();

    public void AddNode(GraphNode node)
    {
        if (!adjacency.ContainsKey(node))
        {
            adjacency[node] = new List<GraphNode>();
        }
    }

    public void AddConnection(GraphNode from, GraphNode to)
    {
        AddNode(from);
        AddNode(to);

        adjacency[from].Add(to);
    }

    public IReadOnlyList<GraphNode> GetNeighbors(GraphNode node)
    {
        if (!adjacency.ContainsKey(node))
        {
            return new List<GraphNode>();
        }

        return adjacency[node];
    }
}
```

Este ejemplo representa conexiones.

No calcula la mejor ruta por si solo.

---

## Grafos dirigidos y no dirigidos

Un grafo puede ser dirigido o no dirigido.

### Grafo no dirigido

La conexion funciona en ambos sentidos.

```txt
A conectado con B
→ A puede ir a B
→ B puede ir a A
```

Ejemplo:

```txt
camino entre dos habitaciones
```

---

### Grafo dirigido

La conexion funciona en un solo sentido.

```txt
A conectado hacia B
→ A puede ir a B
→ B no necesariamente puede ir a A
```

Ejemplo:

```txt
calle de una sola mano
salto hacia una plataforma inferior
flujo de dialogo
decision irreversible
```

---

## Grafos con costo

Las conexiones pueden tener costo.

```txt
A → B
costo 3

A → C
costo 10
```

El costo puede representar:

```txt
distancia
tiempo
dificultad
peligro
energia
recursos
peso tactico
```

Ejemplo en pathfinding:

```txt
camino corto pero peligroso
→ costo alto

camino largo pero seguro
→ costo medio

camino bloqueado
→ no disponible
```

El grafo guarda el costo.

El algoritmo decide como usarlo.

---

## Sistemas consumidores comunes

Un grafo suele aparecer como soporte de sistemas que necesitan relaciones o rutas.

Ejemplos:

```txt
Pathfinding
→ calcula caminos sobre nodos conectados.

IA de NPC
→ consume rutas o zonas conectadas.

Diseño de mapas
→ representa habitaciones, rutas o caminos alternativos.

Sistema de dialogo
→ conecta opciones y respuestas.

Sistema de quests
→ conecta objetivos dependientes.

Mapa de zonas
→ conecta areas desbloqueadas.
```

El grafo no implementa esos sistemas por si solo.

Solo ofrece la estructura de relaciones.

Regla:

```txt
Grafo sirve cuando el sistema consumidor necesita conocer conexiones.

Si el sistema solo necesita historial,
orden de llegada o prioridad simple,
Grafo no es la estructura correcta.
```

---

## Ejemplo aplicado: mapa de nodos para pathfinding

Un grafo puede representar puntos navegables del mapa.

Flujo:

```txt
Diseñador coloca nodos.
Se conectan nodos transitables.
Cada conexion puede tener costo.
Pathfinding consulta vecinos.
Pathfinding calcula ruta.
NPC sigue ruta.
```

Ejemplo conceptual:

```txt
Nodo A
→ conecta con B costo 5
→ conecta con D costo 2

Nodo B
→ conecta con C costo 4

Nodo D
→ conecta con C costo 10
```

Un algoritmo puede decidir:

```txt
A → B → C
costo total 9

A → D → C
costo total 12
```

El grafo no elige por si solo.

Solo ofrece nodos, conexiones y costos.

---

## Como aplicarlo en videojuegos

En videojuegos, un grafo puede usarse cuando hay elementos conectados.

Casos tipicos:

```txt
pathfinding
rutas alternativas
mapas de nodos
habitaciones conectadas
zonas desbloqueables
sistemas de dialogo
arboles de decisiones no estrictamente lineales
quests encadenadas
mapas tacticos
redes de caminos
```

Ejemplo en Tower Defense:

```txt
Nodos del camino
→ representan puntos del mapa.

Conexiones
→ representan caminos posibles.

Costos
→ indican dificultad o distancia.

Pathfinding
→ calcula ruta para enemigos.
```

Esto permite rutas alternativas, caminos desbloqueables o decisiones de recorrido.

---

## Cuando conviene usar Grafos

Conviene usar grafos cuando:

```txt
importan las conexiones entre elementos
hay caminos posibles
hay rutas alternativas
hay nodos y relaciones
hay estados conectados
hay zonas conectadas
hay dependencias no lineales
```

Preguntas utiles:

```txt
¿Hay puntos conectados?
¿Necesito saber vecinos?
¿Hay mas de un camino posible?
¿Las conexiones tienen costo?
¿Algunas conexiones pueden bloquearse?
¿Un algoritmo va a recorrer estas conexiones?
```

Si la respuesta es si, un grafo puede ser una buena opcion.

---

## Cuando NO conviene usar Grafos

No conviene usar grafos si:

```txt
solo necesitas una lista simple
solo necesitas historial
solo necesitas orden de llegada
solo necesitas prioridad simple
no hay conexiones reales
el mapa es completamente lineal
los datos no se relacionan entre si
```

Ejemplos:

```txt
deshacer ultima accion
→ Stack.

procesar eventos en orden
→ Queue.

lista de enemigos activos
→ List puede alcanzar.

ordenar enemigos por progreso
→ ABB o estructura ordenada.
```

Regla:

```txt
No usar Grafo si no hay relaciones que navegar.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
usar grafo para datos sin conexiones
meter pathfinding dentro del grafo
hacer que el grafo decida comportamiento
duplicar nodos sin control
no validar conexiones invalidas
no diferenciar dirigido y no dirigido
no controlar costos
actualizar conexiones sin criterio
hacer grafos enormes sin necesidad
```

Ejemplo de mala practica:

```txt
Graph calcula ruta, mueve NPC y decide ataque.
```

Problema:

```txt
Se mezclan estructura, algoritmo, movimiento y decision.
```

Mejor:

```txt
Graph
→ estructura.

Pathfinding
→ algoritmo.

Movement
→ ejecucion.

Decision
→ criterio de accion.
```

---

## Costos de implementacion

Implementar un grafo puede requerir:

```txt
definir nodos
definir conexiones
definir costos
definir direccion de conexiones
validar conexiones
debug visual
integracion con algoritmos
integracion con sistemas consumidores
```

El costo aumenta si:

```txt
hay muchos nodos
las conexiones cambian en runtime
hay costos dinamicos
hay zonas bloqueables
hay multiples agentes usando el grafo
```

---

## Costos de optimizacion

Un grafo puede ser barato o caro segun uso.

Riesgos posibles:

```txt
demasiados nodos
demasiadas conexiones
busquedas frecuentes
pathfinding constante
allocations al consultar vecinos
actualizacion dinamica de costos
debug visual siempre activo
```

Alternativas:

```txt
mantener grafos simples
cachear vecinos
limitar recalculos de ruta
actualizar costos solo cuando cambian
usar conexiones necesarias
desactivar debug en runtime
dividir grafos por zonas
```

Criterio:

```txt
Grafo chico y estatico
→ costo bajo.

Grafo grande con pathfinding constante
→ riesgo alto.
```

---

## Validacion

Validar un grafo implica revisar que sus conexiones representen correctamente el sistema.

Para mapas:

```txt
si todos los nodos necesarios existen
si las conexiones son correctas
si no hay conexiones imposibles
si los costos tienen sentido
si nodos bloqueados no se usan
si los vecinos devueltos son correctos
si el algoritmo consumidor puede recorrerlo
```

Debug util:

```txt
dibujar nodos
dibujar conexiones
mostrar costos
mostrar conexiones bloqueadas
logs de vecinos
ruta calculada por algoritmo
```

---

## Preguntas antes de implementarlo

Antes de usar Grafo, preguntar:

```txt
¿Hay elementos conectados?
¿Que representa cada nodo?
¿Que representa cada conexion?
¿Las conexiones son dirigidas o no dirigidas?
¿Tienen costo?
¿Pueden bloquearse?
¿Que sistema va a consumir el grafo?
¿Necesito pathfinding o solo relaciones?
¿Una lista simple alcanza?
```

---

## Errores comunes

Errores comunes:

```txt
usar grafos sin conexiones reales
meter algoritmo dentro de la estructura
hacer que el grafo decida gameplay
no validar conexiones
no representar costos correctamente
confundir grafo dirigido con no dirigido
crear nodos duplicados
no tener debug visual
hacer mas nodos de los necesarios
```

---

## Criterio para una IA

Cuando una IA trabaje con Grafos debe:

```txt
identificar si el problema es de conexiones
definir que representa un nodo
definir que representa una conexion
separar grafo, algoritmo y sistema consumidor
no convertir el grafo en pathfinding completo
explicar si es dirigido o no dirigido
explicar si tiene costos
proponer debug visual
comparar con List, Stack o Queue si hay duda
```

Regla operativa:

```txt
Si el problema tiene relaciones navegables,
Grafo tiene sentido.

Si solo hay elementos sueltos,
probablemente alcanza una estructura mas simple.
```

---

## Checklist

Antes de cerrar una implementacion con Grafo, revisar:

```txt
¿El problema realmente necesita conexiones?
¿Cada nodo tiene responsabilidad clara?
¿Cada conexion tiene sentido?
¿Las conexiones son dirigidas o no dirigidas?
¿Hay costos?
¿Los costos representan algo real?
¿El grafo esta separado del algoritmo?
¿El sistema consumidor esta separado del grafo?
¿Hay debug visual?
¿Una lista simple alcanzaba?
```

---

## Regla final

```txt
Un grafo no es pathfinding por si solo.

Es la estructura que permite representar caminos, relaciones y conexiones.
```
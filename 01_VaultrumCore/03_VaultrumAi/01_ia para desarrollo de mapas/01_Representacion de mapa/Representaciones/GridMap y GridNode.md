## Definicion

GridMap y GridNode forman una estructura para representar un mapa mediante una grilla compuesta por nodos.

`GridMap` representa la estructura general.

`GridNode` representa cada unidad individual dentro de esa estructura.

No son automaticamente un sistema de pathfinding.

No son automaticamente una IA.

No son automaticamente un manager global.

Existen para organizar el mapa como datos navegables o consultables.

```txt
GridMap
→ estructura general del mapa

GridNode
→ unidad individual de la grilla
```

---

## Responsabilidad de esta nota

Esta nota define la responsabilidad de `GridMap` y `GridNode` como estructura de representacion.

Su responsabilidad es explicar:

```txt
que representa GridMap
que representa GridNode
que informacion puede guardar cada parte
como se separan responsabilidades
que limites tiene esta estructura
como validarla visualmente
```

Esta nota no debe explicar en detalle todos los sistemas que consumen `GridMap` o `GridNode`.

Los sistemas consumidores deben referenciar esta estructura desde su propio contexto.

---

## Responsabilidad de GridMap

`GridMap` debe representar el conjunto organizado de nodos de una grilla.

Puede responder preguntas como:

```txt
¿Que nodos existen?
¿Cual es el ancho y alto del mapa?
¿Cual es el tamaño de cada celda?
¿Como obtengo un nodo por coordenada?
¿Como convierto una posicion real en coordenada?
¿Como convierto una coordenada en posicion real?
¿Que nodos estan dentro de los limites?
```

`GridMap` no deberia decidir comportamientos.

`GridMap` no deberia mover entidades.

`GridMap` no deberia resolver toda la IA.

`GridMap` no deberia conocer todos los sistemas que lo consumen.

---

## Responsabilidad de GridNode

`GridNode` debe representar una unidad individual dentro del `GridMap`.

Puede responder preguntas como:

```txt
¿Cual es mi coordenada?
¿Cual es mi posicion en mundo?
¿Estoy bloqueado?
¿Estoy disponible?
¿Que costo base tengo?
¿Que tipo de terreno represento?
```

`GridNode` no deberia decidir comportamientos.

`GridNode` no deberia mover entidades.

`GridNode` no deberia calcular rutas completas por si mismo.

`GridNode` no deberia conocer todos los sistemas que lo consumen.

---

## Separacion entre GridMap y GridNode

La separacion principal es:

```txt
GridMap
→ administra la estructura general.

GridNode
→ representa una unidad del mapa.
```

Ejemplo:

```txt
GridMap
→ ancho: 20
→ alto: 10
→ cellSize: 1
→ nodos: matriz de GridNode

GridNode
→ coordenada: (4, 7)
→ posicion: (4, 0, 7)
→ bloqueado: false
→ costo: 1
```

`GridMap` contiene o administra nodos.

`GridNode` no deberia administrar todo el mapa.

---

## Informacion que puede contener GridMap

`GridMap` puede contener informacion como:

```txt
ancho
alto
tamaño de celda
origen
matriz de nodos
metodos de consulta
conversion mundo-grilla
conversion grilla-mundo
validacion de limites
```

Ejemplo conceptual:

```txt
GridMap
→ Width: 10
→ Height: 10
→ CellSize: 1
→ Origin: (0, 0, 0)
```

La informacion debe mantenerse enfocada en la estructura del mapa.

---

## Informacion que puede contener GridNode

`GridNode` puede contener informacion como:

```txt
coordenada
posicion en mundo
estado bloqueado/disponible
costo base
tipo de terreno
ocupante actual
referencia visual para debug
```

Ejemplo conceptual:

```txt
GridNode (3, 2)
→ posicion mundo: (3, 0, 2)
→ bloqueado: false
→ costo base: 1
```

No todos los proyectos necesitan todos estos datos.

---

## Coordenada y posicion real

`GridNode` suele tener una coordenada logica y una posicion real.

```txt
Coordenada
→ ubicacion dentro de la grilla

Posicion real
→ ubicacion dentro del mundo
```

Ejemplo:

```txt
Coordenada: (5, 4)
Posicion real: (10, 0, 8)
```

Esta separacion evita confundir datos logicos con posiciones fisicas.

---

## Conversiones

`GridMap` puede ofrecer conversiones entre mundo y grilla.

Ejemplo:

```txt
WorldToGrid
→ posicion real a coordenada

GridToWorld
→ coordenada a posicion real
```

Estas conversiones son parte del contrato de la estructura.

Deben ser claras, estables y validables.

Una mala conversion puede hacer que sistemas consumidores interpreten mal el mapa.

---

## Limites

`GridMap` debe poder validar si una coordenada esta dentro del mapa.

Ejemplo:

```txt
(3, 2)
→ valida

(-1, 4)
→ invalida

(20, 5)
→ invalida si el ancho es 20
```

Validar limites evita errores al consultar nodos inexistentes.

---

## Vecinos

`GridMap` puede exponer nodos vecinos de un `GridNode`.

Los vecinos pueden calcularse segun reglas como:

```txt
4 direcciones
8 direcciones
solo ortogonales
ortogonales y diagonales
filtrados por estado
```

La estructura puede ofrecer vecinos.

Pero no deberia decidir por si misma que debe hacer cada sistema con esos vecinos.

---

## Estado de GridNode

Un `GridNode` puede tener estado.

Ejemplos:

```txt
disponible
bloqueado
ocupado
reservado
desactivado
```

El estado permite que otros sistemas interpreten si ese nodo puede ser usado.

El nodo expone informacion.

La decision pertenece al sistema consumidor.

---

## Costo de GridNode

Un `GridNode` puede tener un costo base.

Ese costo puede representar:

```txt
dificultad
penalizacion
terreno
riesgo
preferencia
```

El nodo puede guardar el costo.

Pero no deberia decidir como se usa ese costo.

El significado del costo pertenece al sistema que lo interpreta.

---

## Que NO debe hacer GridMap

`GridMap` no debe asumir responsabilidades globales innecesarias.

No debe:

```txt
mover NPCs
decidir comportamientos
controlar estados de IA
resolver combate
actualizar UI
crear reglas de juego completas
funcionar como GameManager
conocer todos los sistemas consumidores
```

`GridMap` debe mantenerse como estructura del mapa.

---

## Que NO debe hacer GridNode

`GridNode` no debe asumir responsabilidades que pertenecen a otros sistemas.

No debe:

```txt
mover entidades
decidir acciones
calcular rutas completas
resolver percepcion
resolver combate
controlar comportamiento de NPC
actualizar interfaces
administrar todo el mapa
```

`GridNode` debe mantenerse como unidad de informacion espacial.

---

## GridMap y GridNode como contrato de informacion

La estructura puede pensarse como un contrato.

```txt
GridMap dice:
Tengo una grilla.
Puedo darte nodos.
Puedo convertir posiciones.
Puedo validar limites.
Puedo exponer vecinos.

GridNode dice:
Tengo coordenada.
Tengo posicion.
Tengo estado.
Puedo tener costo.
Puedo ser consultado.
```

Ese contrato permite que otros sistemas usen el mapa sin mezclar responsabilidades.

---

## Ejemplo conceptual en codigo

```csharp
using System.Collections.Generic;
using UnityEngine;

public class GridNode
{
    public Vector2Int Coordinates { get; }
    public Vector3 WorldPosition { get; }
    public bool IsBlocked { get; private set; }
    public float BaseCost { get; private set; }

    public GridNode(Vector2Int coordinates, Vector3 worldPosition, float baseCost = 1f)
    {
        Coordinates = coordinates;
        WorldPosition = worldPosition;
        BaseCost = baseCost;
    }

    public void SetBlocked(bool isBlocked)
    {
        IsBlocked = isBlocked;
    }

    public void SetBaseCost(float baseCost)
    {
        BaseCost = baseCost;
    }
}
```

```csharp
public class GridMap
{
    private readonly GridNode[,] _nodes;
    private readonly int _width;
    private readonly int _height;
    private readonly float _cellSize;
    private readonly Vector3 _origin;

    public GridMap(int width, int height, float cellSize, Vector3 origin)
    {
        _width = width;
        _height = height;
        _cellSize = cellSize;
        _origin = origin;
        _nodes = new GridNode[_width, _height];

        BuildGrid();
    }

    private void BuildGrid()
    {
        for (int x = 0; x < _width; x++)
        {
            for (int y = 0; y < _height; y++)
            {
                Vector2Int coordinates = new Vector2Int(x, y);
                Vector3 worldPosition = GridToWorld(coordinates);

                _nodes[x, y] = new GridNode(coordinates, worldPosition);
            }
        }
    }

    public Vector3 GridToWorld(Vector2Int coordinates)
    {
        return _origin + new Vector3(
            coordinates.x * _cellSize,
            0f,
            coordinates.y * _cellSize
        );
    }

    public Vector2Int WorldToGrid(Vector3 worldPosition)
    {
        Vector3 localPosition = worldPosition - _origin;

        int x = Mathf.FloorToInt(localPosition.x / _cellSize);
        int y = Mathf.FloorToInt(localPosition.z / _cellSize);

        return new Vector2Int(x, y);
    }

    public bool TryGetNode(Vector2Int coordinates, out GridNode node)
    {
        node = null;

        if (!IsInsideBounds(coordinates)) return false;

        node = _nodes[coordinates.x, coordinates.y];
        return true;
    }

    public bool IsInsideBounds(Vector2Int coordinates)
    {
        if (coordinates.x < 0) return false;
        if (coordinates.y < 0) return false;
        if (coordinates.x >= _width) return false;
        if (coordinates.y >= _height) return false;

        return true;
    }

    public List<GridNode> GetOrthogonalNeighbors(GridNode node)
    {
        List<GridNode> neighbors = new();

        Vector2Int[] directions =
        {
            Vector2Int.up,
            Vector2Int.down,
            Vector2Int.left,
            Vector2Int.right
        };

        foreach (Vector2Int direction in directions)
        {
            Vector2Int neighborCoordinates = node.Coordinates + direction;

            if (TryGetNode(neighborCoordinates, out GridNode neighbor))
            {
                neighbors.Add(neighbor);
            }
        }

        return neighbors;
    }
}
```

Este ejemplo muestra una estructura de grilla.

No mueve entidades.

No decide comportamientos.

No calcula toda la IA.

---

## Ejemplo de uso correcto

Uso correcto:

```txt
GridMap construye y expone la grilla.
GridNode representa cada unidad.
Otro sistema consulta nodos.
Otro sistema interpreta estado, costo o vecinos.
```

Ejemplo:

```txt
GridMap
→ TryGetNode()
→ WorldToGrid()
→ GridToWorld()
→ GetNeighbors()

GridNode
→ Coordinates
→ WorldPosition
→ IsBlocked
→ BaseCost
```

---

## Ejemplo de uso incorrecto

Uso incorrecto:

```txt
GridNode
→ detecta jugador
→ decide perseguir
→ calcula camino completo
→ mueve enemigo
→ actualiza UI

GridMap
→ controla oleadas
→ controla combate
→ controla estados
→ funciona como GameManager
```

En ese caso, la estructura dejo de ser representacion de mapa y empezo a mezclar responsabilidades.

---

## Cuando conviene usar GridMap y GridNode

Conviene usar esta estructura cuando:

```txt
el mapa se organiza por celdas
se necesita consultar posiciones por coordenada
se necesita convertir mundo a grilla
se necesita validar limites
se necesita exponer nodos regulares
se necesita estado o costo por celda
se necesita una estructura navegable ordenada
```

Ejemplos:

```txt
juego tactico por casilleros
sistema de construccion por grilla
mapa tile-based
lectura de zonas navegables
representacion espacial regular
```

---

## Cuando NO conviene usar GridMap y GridNode

No conviene usar esta estructura cuando:

```txt
el mapa no necesita grilla
el movimiento no depende de celdas
hay pocos puntos importantes
waypoints simples alcanzan
nodos libres representan mejor el espacio
la grilla agrega complejidad innecesaria
```

No todo mapa necesita `GridMap`.

No todo nodo necesita pertenecer a una grilla.

---

## Ubicacion y escala

`GridMap` debe tener ubicacion y escala claras.

Debe definirse:

```txt
origen
ancho
alto
cellSize
orientacion
conversion mundo-grilla
conversion grilla-mundo
```

Una mala ubicacion o escala puede romper consultas.

Ejemplos de error:

```txt
el jugador esta visualmente sobre una celda pero el sistema lee otra
un obstaculo bloquea una celda incorrecta
el borde del mapa no coincide con la grilla
el cellSize no representa el espacio real
```

---

## Validacion visual

`GridMap` y `GridNode` deben poder validarse visualmente.

Una buena validacion puede mostrar:

```txt
bordes de la grilla
centro de cada nodo
coordenadas
nodos bloqueados
nodos disponibles
costos
vecinos
limites
origen
```

Esto permite detectar:

```txt
nodos mal ubicados
grilla desalineada
vecinos incorrectos
limites mal calculados
costos mal asignados
bloqueos equivocados
```

Sin debug visual, una grilla puede parecer correcta en codigo pero fallar en escena.

---

## Errores comunes

```txt
hacer que GridMap sea un GameManager
hacer que GridNode tenga logica de NPC
confundir coordenada con posicion real
no validar limites
no validar conversiones
usar grilla sin necesidad
no mostrar debug visual
guardar demasiada logica en cada nodo
duplicar datos que pertenecen a otro sistema
mezclar estructura de mapa con comportamiento
```

---

## Criterio para una IA

Cuando una IA proponga `GridMap` y `GridNode`, debe justificar:

```txt
por que la grilla es necesaria
que representa cada GridNode
que datos guarda GridNode
que datos NO debe guardar
que responsabilidades tiene GridMap
que responsabilidades NO debe asumir
como se convierten posiciones
como se validan limites
como se valida visualmente
que sistema consume esta estructura
```

La IA no debe convertir esta nota en una explicacion de todos los sistemas que usan grillas.

Debe mantener la responsabilidad clara.

---

## Checklist

Antes de usar `GridMap` y `GridNode`, revisar:

```txt
¿El mapa necesita grilla?
¿Cada GridNode representa una unidad clara?
¿GridMap tiene origen, ancho, alto y cellSize definidos?
¿La conversion mundo-grilla funciona?
¿La conversion grilla-mundo funciona?
¿Los limites estan validados?
¿Los nodos guardan solo informacion necesaria?
¿GridMap evita ser GameManager?
¿GridNode evita tener logica de NPC?
¿Se puede validar visualmente?
```

---

## Regla final

`GridMap` y `GridNode` no son el sistema completo.

Son una estructura de representacion.

```txt
GridMap
→ organiza

GridNode
→ representa

Sistema consumidor
→ interpreta
```
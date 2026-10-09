## Definicion

Una grilla es una forma de representar el espacio dividiendolo en celdas regulares.

Cada celda representa una unidad logica del mapa.

No es necesariamente visible para el jugador.

No es necesariamente el mapa completo.

No es necesariamente la mejor solucion para todo juego.

Una grilla existe para que el sistema pueda leer el espacio como una estructura ordenada.

```txt
Grilla
→ division regular del espacio
→ celdas
→ lectura sistematica del mapa
```

---

## Responsabilidad de esta nota

Esta nota define que es una grilla dentro de una representacion de mapa.

Su responsabilidad es explicar:

```txt
que representa una grilla
que representa una celda
que informacion puede guardar
que limites tiene
como validar que esta bien construida
```

Esta nota no debe explicar en detalle los sistemas que consumen grillas.

Los sistemas que necesiten grillas deben referenciar esta nota desde su propio contexto.

---

## Responsabilidad de una grilla

Una grilla debe representar el espacio como un conjunto de unidades regulares.

Puede responder preguntas como:

```txt
¿En que celda esta esta posicion?
¿Que celdas existen alrededor?
¿Que celdas estan disponibles?
¿Que celdas estan bloqueadas?
¿Que celdas pertenecen a una zona?
¿Como se divide logicamente el mapa?
```

Una grilla no deberia decidir comportamientos.

Una grilla no deberia mover entidades.

Una grilla no deberia resolver todo el pathfinding por si misma.

Una grilla no deberia conocer todos los sistemas que la consumen.

---

## Que puede representar una celda

Una celda puede representar:

```txt
un casillero del mapa
una posicion logica
una zona caminable
una zona bloqueada
un tile
una unidad tactica
un espacio ocupable
un espacio de consulta
```

Ejemplo conceptual:

```txt
Celda (0, 0)
Celda (0, 1)
Celda (1, 0)
Celda (1, 1)
```

La celda debe tener un significado claro dentro del sistema.

---

## Informacion que puede contener una celda

Una celda puede contener informacion como:

```txt
coordenada
posicion en mundo
estado disponible/bloqueado
costo base
tipo de terreno
ocupante actual
referencia visual para debug
```

Ejemplo conceptual:

```txt
Celda X: 3
Celda Y: 5
Posicion mundo: (6, 0, 10)
Disponible: true
Costo base: 1
Tipo: suelo
```

No todas las grillas necesitan todos estos datos.

La informacion debe responder a la necesidad real del proyecto.

---

## Coordenadas

Las coordenadas permiten identificar una celda dentro de la grilla.

Pueden ser:

```txt
x, y
fila, columna
row, column
Vector2Int
indice lineal
```

Ejemplo:

```txt
Celda (2, 4)
```

La coordenada no siempre es igual a la posicion real en mundo.

Puede existir una conversion:

```txt
coordenada de grilla
→ posicion en mundo

posicion en mundo
→ coordenada de grilla
```

---

## Tamaño de celda

El tamaño de celda define cuanto espacio real representa cada unidad de la grilla.

Ejemplo:

```txt
cellSize = 1
→ cada celda representa 1 unidad del mundo

cellSize = 2
→ cada celda representa 2 unidades del mundo
```

El tamaño debe elegirse con criterio.

Una celda demasiado grande puede perder precision.

Una celda demasiado chica puede generar demasiados datos.

---

## Vecinos

Los vecinos de una celda son las celdas cercanas que pueden consultarse desde ella.

Ejemplo en 4 direcciones:

```txt
arriba
abajo
izquierda
derecha
```

Ejemplo en 8 direcciones:

```txt
arriba
abajo
izquierda
derecha
diagonales
```

La grilla puede exponer vecinos.

Pero no deberia decidir por si misma que sistema debe hacer con esos vecinos.

---

## Estado

Una celda puede tener estado.

Ejemplos:

```txt
disponible
bloqueada
ocupada
reservada
desactivada
desconocida
```

El estado permite que otros sistemas interpreten si esa celda puede usarse.

La celda expone informacion.

La decision pertenece al sistema consumidor.

---

## Costo

Una celda puede tener un costo asociado.

El costo puede representar:

```txt
dificultad de atravesar
penalizacion
peso tactico
riesgo
preferencia
tipo de terreno
```

La grilla puede guardar costos.

Pero no deberia decidir por si misma como se usan esos costos.

El significado del costo debe definirse en el sistema que lo interpreta.

---

## Que NO debe hacer una grilla

Una grilla no debe asumir responsabilidades que no le corresponden.

No debe:

```txt
mover NPCs
decidir comportamientos
resolver combate
controlar estados de IA
actualizar UI innecesariamente
calcular toda la logica del juego
convertirse en un manager global
conocer todos los sistemas que la consumen
```

Una grilla debe mantenerse como estructura de informacion espacial.

---

## Grilla como contrato de informacion

Una grilla puede pensarse como un contrato simple.

```txt
Yo divido el espacio en celdas.
Cada celda tiene una coordenada.
Cada celda puede tener estado.
Cada celda puede tener costo.
Puedo convertir posicion de mundo a celda.
Puedo convertir celda a posicion de mundo.
Puedo exponer vecinos.
```

Ese contrato permite que otros sistemas trabajen con el mapa sin mezclar responsabilidades.

La nota de grillas debe documentar ese contrato.

No debe documentar todos los sistemas consumidores.

---

## Ejemplo conceptual en codigo

```csharp
using UnityEngine;

public class GridCell
{
    public Vector2Int Coordinates { get; }
    public Vector3 WorldPosition { get; }
    public bool IsBlocked { get; private set; }
    public float BaseCost { get; private set; }

    public GridCell(Vector2Int coordinates, Vector3 worldPosition, float baseCost = 1f)
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

Ejemplo de grilla simple:

```csharp
public class GridMap
{
    private readonly GridCell[,] _cells;
    private readonly float _cellSize;
    private readonly Vector3 _origin;

    public GridMap(int width, int height, float cellSize, Vector3 origin)
    {
        _cells = new GridCell[width, height];
        _cellSize = cellSize;
        _origin = origin;

        for (int x = 0; x < width; x++)
        {
            for (int y = 0; y < height; y++)
            {
                Vector3 worldPosition = _origin + new Vector3(x * _cellSize, 0f, y * _cellSize);
                _cells[x, y] = new GridCell(new Vector2Int(x, y), worldPosition);
            }
        }
    }

    public bool TryGetCell(Vector2Int coordinates, out GridCell cell)
    {
        cell = null;

        if (coordinates.x < 0 || coordinates.y < 0) return false;
        if (coordinates.x >= _cells.GetLength(0)) return false;
        if (coordinates.y >= _cells.GetLength(1)) return false;

        cell = _cells[coordinates.x, coordinates.y];
        return true;
    }
}
```

Este ejemplo muestra la grilla como estructura de informacion.

No mueve entidades.

No decide comportamientos.

No calcula toda la IA.

---

## Ejemplo de uso correcto

Uso correcto:

```txt
La grilla divide el mapa.
Cada celda tiene coordenada, posicion y estado.
Otro sistema consulta celdas.
Otro sistema decide que hacer con esa informacion.
```

Ejemplo:

```txt
Celda (4, 2)
→ posicion
→ estado
→ costo
```

Eso permite que la grilla sea reutilizable.

---

## Ejemplo de uso incorrecto

Uso incorrecto:

```txt
Celda (4, 2)
→ detecta jugador
→ decide perseguir
→ calcula ruta completa
→ mueve enemigo
→ actualiza UI
```

Esa celda dejo de ser celda.

Se convirtio en una clase mezclada.

---

## Cuando conviene usar grillas

Conviene usar grillas cuando el mapa funciona naturalmente por unidades regulares.

Ejemplos:

```txt
juegos tacticos
juegos por turnos
mapas tile-based
sistemas de construccion por casilleros
zonas de ocupacion
lectura espacial regular
mapas donde importa fila y columna
```

La grilla es util cuando la regularidad del espacio ayuda al sistema.

---

## Cuando NO conviene usar grillas

No conviene usar grillas cuando:

```txt
el mapa no se organiza por celdas
el movimiento es libre y no necesita division regular
la grilla agrega demasiada complejidad
waypoints simples alcanzan
nodos libres representan mejor el espacio
el nivel tiene pocas posiciones relevantes
```

No todo mapa necesita dividirse en casilleros.

---

## Ubicacion y tamaño de la grilla

La grilla debe tener una ubicacion y dimensiones claras.

Debe definirse:

```txt
origen
ancho
alto
tamaño de celda
orientacion
conversion mundo-grilla
conversion grilla-mundo
```

Una grilla mal alineada puede generar errores dificiles de ver.

Ejemplos:

```txt
celdas corridas respecto al escenario
objetos entre dos celdas
bloqueos mal detectados
posiciones reales convertidas a celdas incorrectas
```

---

## Validacion visual

Una grilla debe poder validarse visualmente.

Una buena validacion puede mostrar:

```txt
bordes de celdas
coordenadas
celdas bloqueadas
celdas disponibles
costos
origen de la grilla
tamaño de celda
```

Esto permite detectar:

```txt
grilla mal alineada
cell size incorrecto
celdas faltantes
bloqueos mal cargados
celdas inaccesibles
```

Sin debug visual, una grilla puede parecer correcta en codigo pero estar mal ubicada en el mundo.

---

## Errores comunes

```txt
usar grilla cuando no hace falta
hacer la celda demasiado grande
hacer la celda demasiado chica
confundir coordenada con posicion real
mezclar logica de NPC dentro de la celda
hacer que la grilla sea un manager global
no validar alineacion visual
no definir bien vecinos
no separar datos de decisiones
```

---

## Criterio para una IA

Cuando una IA proponga una grilla, debe justificar:

```txt
por que el mapa necesita division regular
que representa cada celda
que datos guarda cada celda
que datos NO debe guardar
como se convierte posicion real a celda
como se convierte celda a posicion real
como se validan visualmente las celdas
que sistema consume la grilla
```

La IA no debe convertir la nota de grillas en una explicacion de todos los sistemas que usan grillas.

Debe mantener la responsabilidad clara.

---

## Checklist

Antes de usar grillas, revisar:

```txt
¿El mapa necesita celdas?
¿La division regular aporta valor?
¿El tamaño de celda tiene sentido?
¿El origen de la grilla esta claro?
¿La conversion mundo-grilla esta definida?
¿Cada celda guarda solo informacion necesaria?
¿La grilla evita decidir comportamientos?
¿La grilla evita mover entidades?
¿La grilla evita conocer sistemas consumidores?
¿Se puede validar visualmente?
```

---

## Regla final

Una grilla no es la IA.

Una grilla no es el movimiento.

Una grilla es una estructura para leer el espacio.

```txt
Grilla
→ estructura regular

Celda
→ unidad de informacion

Sistema consumidor
→ interpreta esa informacion
```
## Definicion

Un nodo es un punto logico del mapa que representa una posicion reconocible para un sistema.

No es necesariamente un objeto visible para el jugador.

No es necesariamente un destino final.

No es necesariamente una celda.

Un nodo existe para que el juego pueda identificar, conectar y evaluar puntos importantes del espacio.

```txt
Nodo
→ punto logico del mapa
→ posicion reconocible por sistemas
```

---

## Responsabilidad de esta nota

Esta nota define que es un nodo dentro de una representacion de mapa.

Su responsabilidad es explicar:

```txt
que representa un nodo
que informacion puede guardar
como puede conectarse con otros nodos
que limites tiene
como validar que esta bien ubicado
```

Esta nota no debe explicar en detalle los sistemas que usan nodos.

Los sistemas que necesiten nodos deben referenciar esta nota desde su propio contexto.

---

## Responsabilidad de un nodo

Un nodo debe representar una unidad clara de informacion espacial.

Puede responder preguntas como:

```txt
¿Donde hay un punto navegable?
¿Donde hay una interseccion?
¿Donde empieza o termina una conexion?
¿Que puntos del mapa pueden conectarse?
¿Que posicion puede usar un sistema como referencia?
```

Un nodo no deberia decidir comportamientos.

Un nodo no deberia mover entidades.

Un nodo no deberia calcular una ruta completa por si mismo.

Un nodo no deberia conocer todos los sistemas que lo consumen.

---

## Que puede representar un nodo

Un nodo puede representar:

```txt
una posicion navegable
una interseccion
una entrada
una salida
una esquina
un punto de referencia
un punto de decision espacial
un punto cercano a un objetivo
un punto de control para debug
```

Ejemplo conceptual:

```txt
NodoEntrada
NodoCentro
NodoSalidaNorte
NodoSalidaSur
```

El nombre del nodo debe ayudar a entender su rol dentro del mapa.

---

## Informacion que puede contener

Un nodo puede contener informacion como:

```txt
identificador
posicion
lista de vecinos
estado disponible/bloqueado
costo base
tipo de zona
referencia visual para debug
```

Ejemplo conceptual:

```txt
Nodo A
→ posicion: (4, 0, 8)
→ vecinos: Nodo B, Nodo C
→ disponible: true
→ costo base: 1
```

No todos los nodos necesitan todos estos datos.

La informacion debe responder a la necesidad del sistema.

---

## Posicion

La posicion indica donde existe el nodo dentro del mundo o del mapa logico.

Puede venir de:

```txt
un Transform en Unity
una coordenada Vector3
una coordenada Vector2
una celda
una posicion definida manualmente
una posicion generada automaticamente
```

La posicion debe ser clara y validable.

Si un nodo representa un punto navegable, debe estar ubicado donde realmente tenga sentido para el agente o sistema que lo va a usar.

---

## Vecinos

Los vecinos son otros nodos a los que un nodo esta conectado directamente.

```txt
Nodo A
→ vecinos: Nodo B, Nodo C
```

Los vecinos no significan necesariamente que el sistema deba moverse hacia ellos.

Solo indican que existe una relacion directa posible entre nodos.

La interpretacion de esa relacion depende del sistema que consuma la estructura.

---

## Conexiones

Una conexion representa la relacion entre dos nodos.

Puede ser simple:

```txt
Nodo A ↔ Nodo B
```

O puede tener informacion adicional:

```txt
distancia
costo
bloqueo
condicion de uso
tipo de terreno
```

La conexion debe responder a una necesidad real.

Si solo hace falta saber que dos puntos estan conectados, no hace falta agregar mas datos.

---

## Estado

Un nodo puede tener un estado.

Ejemplos:

```txt
disponible
bloqueado
desbloqueado
activo
inactivo
reservado
```

El estado permite que otros sistemas sepan si ese punto puede usarse.

Pero el nodo no deberia decidir por si mismo que hacer con ese estado.

Debe exponer informacion.

La decision pertenece al sistema consumidor.

---

## Costo

Un nodo puede tener un costo asociado.

El costo puede representar:

```txt
distancia
dificultad
riesgo
peso tactico
penalizacion
preferencia
```

El nodo puede guardar el valor.

Pero no deberia decidir por si mismo como se usa ese valor.

El significado del costo debe estar definido por el sistema que lo interpreta.

---

## Que NO debe hacer un nodo

Un nodo no debe asumir responsabilidades que no le corresponden.

No debe:

```txt
mover al NPC
decidir comportamientos
calcular rutas completas por si mismo
elegir objetivos
resolver combate
controlar estados de IA
contener logica de gameplay innecesaria
conocer todos los sistemas que lo usan
convertirse en un manager
```

Un nodo debe mantenerse como una pieza de informacion espacial.

Mientras mas responsabilidades se le agregan, mas dificil se vuelve reutilizarlo.

---

## Nodos como contrato de informacion

Un nodo puede pensarse como un contrato simple.

```txt
Yo soy un punto del mapa.
Tengo una posicion.
Puedo tener vecinos.
Puedo tener estado.
Puedo tener costo.
Puedo ser consultado por otros sistemas.
```

Ese contrato permite que otros sistemas trabajen con el mapa sin mezclar responsabilidades.

La nota de nodos debe documentar ese contrato.

No debe documentar todos los sistemas consumidores.

---

## Ejemplo conceptual en codigo

```csharp
using System.Collections.Generic;
using UnityEngine;

public class MapNode
{
    public string Id { get; }
    public Vector3 Position { get; }
    public IReadOnlyList<MapNode> Neighbors => _neighbors;
    public bool IsBlocked { get; private set; }
    public float BaseCost { get; private set; }

    private readonly List<MapNode> _neighbors = new();

    public MapNode(string id, Vector3 position, float baseCost = 1f)
    {
        Id = id;
        Position = position;
        BaseCost = baseCost;
    }

    public void AddNeighbor(MapNode neighbor)
    {
        if (neighbor == null) return;
        if (neighbor == this) return;
        if (_neighbors.Contains(neighbor)) return;

        _neighbors.Add(neighbor);
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

Este ejemplo muestra un nodo como estructura de informacion.

No mueve entidades.

No calcula rutas.

No decide comportamientos.

Solo expone datos utiles para otros sistemas.

---

## Ejemplo de uso correcto

Uso correcto:

```txt
El mapa define nodos.
Cada nodo tiene posicion y vecinos.
Otro sistema consulta esos nodos.
Otro sistema decide que hacer con esa informacion.
```

Ejemplo:

```txt
Nodo A
→ posicion
→ vecinos
→ costo
→ estado
```

Eso permite que el nodo sea reutilizable.

---

## Ejemplo de uso incorrecto

Uso incorrecto:

```txt
Nodo A
→ detecta al jugador
→ decide perseguir
→ calcula camino
→ mueve al NPC
→ actualiza UI
```

Ese nodo dejo de ser nodo.

Se convirtio en una clase mezclada.

---

## Cuando conviene usar nodos

Conviene usar nodos cuando el mapa necesita puntos logicos reconocibles.

Ejemplos:

```txt
hay intersecciones
hay caminos conectados
hay posiciones importantes
hay zonas que pueden habilitarse o bloquearse
hay sistemas que necesitan consultar puntos del mapa
hay rutas que pueden representarse como secuencia de puntos
```

Los nodos son utiles cuando el mapa necesita estructura.

---

## Cuando NO conviene usar nodos

No conviene usar nodos cuando:

```txt
el recorrido es totalmente fijo
el sistema no necesita consultar posiciones
hay una unica ruta simple
el mapa no necesita estructura logica
una animacion o movimiento directo alcanza
```

No todo movimiento necesita nodos.

No todo mapa necesita nodos.

---

## Ubicacion y cantidad de nodos

La cantidad de nodos debe responder al diseño del mapa.

Pocos nodos pueden dejar caminos pobres o imprecisos.

Demasiados nodos pueden volver el sistema dificil de mantener.

Criterio:

```txt
Cada nodo debe tener una razon para existir.
```

Un nodo deberia estar donde aporta informacion:

```txt
intersecciones
cambios de direccion
entradas
salidas
zonas importantes
puntos de decision
puntos necesarios para conectar rutas
```

---

## Validacion visual

Los nodos deben poder validarse visualmente.

Una buena validacion puede mostrar:

```txt
posicion de cada nodo
nombre o identificador
lineas hacia vecinos
color segun estado
color segun costo
nodos bloqueados
nodos disponibles
```

Esto permite detectar errores como:

```txt
nodos mal ubicados
vecinos faltantes
conexiones incorrectas
nodos duplicados
nodos inaccesibles
```

Sin debug visual, la estructura puede parecer correcta en codigo pero fallar en el mapa real.

---

## Errores comunes

```txt
crear nodos sin necesidad real
usar nodos como managers
meter comportamiento de NPC dentro del nodo
hacer que el nodo calcule todo
poner demasiados nodos
poner muy pocos nodos
no validar vecinos
no mostrar debug visual
confundir nodo con destino final exacto
duplicar datos que pertenecen a otro sistema
```

---

## Criterio para una IA

Cuando una IA proponga nodos, debe justificar:

```txt
que representa cada nodo
por que el mapa necesita nodos
que datos guarda el nodo
que datos NO debe guardar
que sistema los consume
como se conectan
como se validan
```

La IA no debe convertir la nota de nodos en una explicacion de todos los sistemas que usan nodos.

Debe mantener la responsabilidad clara.

---

## Checklist

Antes de usar nodos, revisar:

```txt
¿El mapa necesita puntos logicos?
¿Cada nodo tiene una razon para existir?
¿La posicion del nodo es clara?
¿Los vecinos estan definidos?
¿El nodo guarda solo informacion necesaria?
¿El nodo evita decidir comportamientos?
¿El nodo evita mover entidades?
¿El nodo evita conocer sistemas consumidores?
¿Se puede validar visualmente?
```

---

## Regla final

Un nodo no es el sistema.

Un nodo alimenta sistemas.

```txt
Nodo
→ informacion espacial

Sistema consumidor
→ interpreta esa informacion
```
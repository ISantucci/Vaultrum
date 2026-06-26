## Definicion

Un waypoint es un punto de referencia usado para guiar un recorrido.

Puede representar una posicion por la que una entidad, camara, sistema o ruta debe pasar.

No es necesariamente un nodo de una red compleja.

No es necesariamente parte de un algoritmo de busqueda.

No es necesariamente visible para el jugador.

Un waypoint existe para marcar puntos utiles de recorrido o referencia.

```txt
Waypoint
→ punto de paso
→ referencia para recorrido
```

---

## Responsabilidad de esta nota

Esta nota define que es un waypoint dentro de una representacion de mapa.

Su responsabilidad es explicar:

```txt
que representa un waypoint
que informacion puede guardar
como puede organizarse en una ruta
que limites tiene
como validar que esta bien ubicado
```

Esta nota no debe explicar en detalle los sistemas que consumen waypoints.

Los sistemas que necesiten waypoints deben referenciar esta nota desde su propio contexto.

---

## Responsabilidad de un waypoint

Un waypoint debe representar un punto de paso claro.

Puede responder preguntas como:

```txt
¿Por donde debe pasar esta entidad?
¿Cual es el siguiente punto de una ruta?
¿Donde empieza un recorrido?
¿Donde termina un recorrido?
¿Que punto sirve como referencia manual?
```

Un waypoint no deberia decidir comportamientos.

Un waypoint no deberia calcular rutas complejas.

Un waypoint no deberia mover entidades por si mismo.

Un waypoint no deberia conocer todos los sistemas que lo consumen.

---

## Que puede representar un waypoint

Un waypoint puede representar:

```txt
inicio de ruta
punto intermedio
final de ruta
punto de patrulla
punto de curva
punto de espera
punto de referencia
punto de spawn
punto de camara
```

Ejemplo conceptual:

```txt
WaypointInicio
WaypointCurva
WaypointPuente
WaypointFinal
```

El nombre del waypoint debe ayudar a entender su uso.

---

## Informacion que puede contener

Un waypoint puede contener informacion como:

```txt
identificador
posicion
orden dentro de una ruta
tiempo de espera
siguiente waypoint
waypoint anterior
estado activo/inactivo
referencia visual para debug
```

Ejemplo conceptual:

```txt
Waypoint 03
→ posicion: (10, 0, 4)
→ orden: 3
→ espera: 0.5 segundos
→ activo: true
```

No todos los waypoints necesitan todos estos datos.

La informacion debe responder al uso real.

---

## Posicion

La posicion indica donde existe el waypoint en el mundo.

Puede venir de:

```txt
un Transform en Unity
una coordenada Vector3
una coordenada Vector2
una posicion definida manualmente
una posicion generada por herramienta
```

La posicion debe ser clara y validable.

Si una entidad debe pasar por ese punto, el waypoint debe estar ubicado en un lugar alcanzable y coherente.

---

## Orden

Los waypoints suelen organizarse en una secuencia.

Ejemplo:

```txt
Waypoint 01
→ Waypoint 02
→ Waypoint 03
→ Waypoint 04
```

El orden puede definirse por:

```txt
lista
array
indice
referencia al siguiente
orden manual en escena
nombre
```

El orden debe ser estable y facil de revisar.

Un error en el orden puede romper toda la ruta.

---

## Ruta

Una ruta de waypoints es una secuencia de puntos de paso.

```txt
Ruta
→ conjunto ordenado de waypoints
```

La ruta puede ser:

```txt
lineal
circular
de ida y vuelta
manual
predefinida
temporal
```

La ruta puede usar waypoints.

Pero el waypoint individual no deberia controlar toda la logica de la ruta.

---

## Estado

Un waypoint puede tener estado.

Ejemplos:

```txt
activo
inactivo
ocupado
disponible
deshabilitado
visitado
```

El estado permite que otros sistemas sepan si ese waypoint puede usarse.

Pero el waypoint no deberia decidir por si mismo que hacer con ese estado.

Debe exponer informacion.

La decision pertenece al sistema consumidor.

---

## Que NO debe hacer un waypoint

Un waypoint no debe asumir responsabilidades que no le corresponden.

No debe:

```txt
mover al NPC
decidir comportamiento
calcular pathfinding completo
resolver combate
controlar estados de IA
actualizar UI
conocer todos los sistemas que lo consumen
convertirse en manager de rutas
```

Un waypoint debe mantenerse como punto de referencia.

Mientras mas responsabilidades se le agregan, menos reutilizable se vuelve.

---

## Waypoint como contrato de informacion

Un waypoint puede pensarse como un contrato simple.

```txt
Yo soy un punto de paso.
Tengo una posicion.
Puedo tener orden.
Puedo tener estado.
Puedo tener datos simples de recorrido.
Puedo ser consultado por otros sistemas.
```

Ese contrato permite que otros sistemas usen rutas manuales sin mezclar responsabilidades.

La nota de waypoints debe documentar ese contrato.

No debe documentar todos los sistemas consumidores.

---

## Ejemplo conceptual en codigo

```csharp
using UnityEngine;

public class Waypoint
{
    public string Id { get; }
    public Vector3 Position { get; }
    public int Order { get; }
    public bool IsActive { get; private set; }
    public float WaitTime { get; private set; }

    public Waypoint(string id, Vector3 position, int order, float waitTime = 0f)
    {
        Id = id;
        Position = position;
        Order = order;
        WaitTime = waitTime;
        IsActive = true;
    }

    public void SetActive(bool isActive)
    {
        IsActive = isActive;
    }

    public void SetWaitTime(float waitTime)
    {
        WaitTime = waitTime;
    }
}
```

Ejemplo de ruta simple:

```csharp
using System.Collections.Generic;

public class WaypointRoute
{
    private readonly List<Waypoint> _waypoints;

    public IReadOnlyList<Waypoint> Waypoints => _waypoints;

    public WaypointRoute(List<Waypoint> waypoints)
    {
        _waypoints = waypoints;
    }

    public bool TryGetWaypoint(int index, out Waypoint waypoint)
    {
        waypoint = null;

        if (index < 0) return false;
        if (index >= _waypoints.Count) return false;

        waypoint = _waypoints[index];
        return true;
    }
}
```

Este ejemplo muestra waypoints como datos de ruta.

No mueve entidades.

No decide comportamiento.

No calcula caminos complejos.

---

## Ejemplo de uso correcto

Uso correcto:

```txt
Los waypoints definen puntos de paso.
Una ruta ordena esos puntos.
Otro sistema recorre esa ruta.
Otro sistema decide que hacer al llegar.
```

Ejemplo:

```txt
Waypoint 01
→ posicion
→ orden
→ espera
→ activo
```

Eso permite reutilizar los waypoints sin mezclar logica.

---

## Ejemplo de uso incorrecto

Uso incorrecto:

```txt
Waypoint 01
→ detecta jugador
→ decide atacar
→ mueve enemigo
→ calcula ruta alternativa
→ actualiza UI
```

Ese waypoint dejo de ser waypoint.

Se convirtio en una clase mezclada.

---

## Cuando conviene usar waypoints

Conviene usar waypoints cuando el recorrido esta controlado o predefinido.

Ejemplos:

```txt
patrullaje simple
camino fijo de enemigos
ruta de camara
puntos de spawn
recorrido guiado
movimiento entre puntos conocidos
tutoriales
secuencias controladas
```

Los waypoints son utiles cuando no hace falta una busqueda compleja.

---

## Cuando NO conviene usar waypoints

No conviene usar waypoints cuando:

```txt
el destino cambia constantemente
hay muchos caminos posibles
el mapa tiene obstaculos dinamicos complejos
el agente necesita elegir ruta
el espacio requiere analisis flexible
una red de nodos seria mas adecuada
una grilla seria mas adecuada
```

Un waypoint es una referencia.

No reemplaza siempre a una estructura navegable mas amplia.

---

## Cantidad y ubicacion de waypoints

La cantidad de waypoints debe responder al recorrido.

Pocos waypoints pueden generar rutas pobres o bruscas.

Demasiados waypoints pueden volver el recorrido dificil de mantener.

Criterio:

```txt
Cada waypoint debe tener una razon para existir.
```

Un waypoint deberia estar donde aporta control:

```txt
inicio
final
cambio de direccion
punto de espera
curva importante
zona de decision manual
punto que el diseñador quiere controlar
```

---

## Validacion visual

Los waypoints deben poder validarse visualmente.

Una buena validacion puede mostrar:

```txt
posicion de cada waypoint
nombre o identificador
orden de recorrido
lineas entre puntos
estado activo/inactivo
direccion de avance
```

Esto permite detectar:

```txt
waypoints mal ubicados
orden incorrecto
saltos raros
puntos inaccesibles
puntos duplicados
rutas cortadas
```

Sin debug visual, una ruta puede parecer correcta en datos pero fallar en escena.

---

## Errores comunes

```txt
usar waypoints para problemas que requieren pathfinding
poner waypoints sin orden claro
mezclar decision de NPC dentro del waypoint
hacer que el waypoint mueva entidades
poner demasiados waypoints
poner muy pocos waypoints
no validar ruta visualmente
confundir waypoint con nodo de red
confundir waypoint con objetivo final
```

---

## Criterio para una IA

Cuando una IA proponga waypoints, debe justificar:

```txt
por que alcanza con puntos predefinidos
que representa cada waypoint
como se ordenan
que datos guardan
que datos NO deben guardar
que sistema los consume
como se validan visualmente
```

La IA no debe convertir la nota de waypoints en una explicacion de todos los sistemas que los usan.

Debe mantener la responsabilidad clara.

---

## Checklist

Antes de usar waypoints, revisar:

```txt
¿El recorrido es predefinido?
¿Cada waypoint tiene una razon para existir?
¿La posicion de cada waypoint es clara?
¿El orden esta definido?
¿La ruta puede validarse visualmente?
¿El waypoint guarda solo informacion necesaria?
¿El waypoint evita decidir comportamientos?
¿El waypoint evita mover entidades?
¿El waypoint evita conocer sistemas consumidores?
¿Waypoints alcanzan o hace falta otra estructura?
```

---

## Regla final

Un waypoint no es una IA.

Un waypoint no es un algoritmo.

Un waypoint es un punto de paso.

```txt
Waypoint
→ referencia de recorrido

Ruta
→ secuencia de puntos

Sistema consumidor
→ interpreta y ejecuta
```
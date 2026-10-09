## Definición

La integración con pathfinding describe cómo un NPC puede consumir rutas calculadas por un sistema de navegación para moverse dentro del mapa.

```txt
NPC
→ necesita llegar a un objetivo.

Pathfinding
→ calcula una ruta.

Movimiento
→ sigue esa ruta.
```

Esta nota no explica completo cómo funciona pathfinding.

Explica cómo un NPC lo usa sin absorberlo.

---

## Responsabilidad

La responsabilidad de esta integración es definir el puente entre una intención de movimiento y una ruta navegable.

Debe responder:

```txt
¿Cuándo un NPC necesita pedir una ruta?
¿Qué información entrega al sistema de pathfinding?
¿Qué recibe como resultado?
¿Cómo usa esa ruta?
¿Cuándo recalcula?
¿Cuándo abandona la ruta?
```

La integración no debe contener todo el algoritmo.

Debe coordinar consumo.

---

## Qué NO debe hacer

La integración con pathfinding no debe:

```txt
reescribir A Star completo
reescribir Dijkstra completo
definir toda la representación del mapa
duplicar nodos, grillas o costos
decidir comportamiento del NPC
mover al NPC sin separación
resolver combate
```

Ejemplo incorrecto:

```txt
NPCPathfindingIntegration
→ detecta jugador
→ decide perseguir
→ implementa A Star
→ mueve
→ ataca
```

Ejemplo correcto:

```txt
Comportamiento
→ pide llegar a una posición.

PathfindingService
→ devuelve ruta.

Movimiento
→ sigue puntos de ruta.
```

Regla:

```txt
La integración consume pathfinding.

No lo reemplaza.
```

---

## Qué problema resuelve

La integración con pathfinding permite que un NPC use rutas calculadas por otro sistema sin mezclar responsabilidades.

Sin una integración clara, un NPC puede terminar absorbiendo:

```txt
representación del mapa
algoritmo de búsqueda
cálculo de costos
seguimiento de ruta
decisión de comportamiento
movimiento físico
```

Con una integración sana, el flujo queda separado:

```txt
objetivo definido
→ ruta calculada
→ ruta consumida
→ movimiento ejecutado
```

---

## Datos que necesita

La integración puede necesitar:

```txt
posición actual del NPC
posición objetivo
referencia al sistema de pathfinding
tipo de mapa navegable
radio del agente
restricciones de navegación
frecuencia de recálculo
distancia mínima para recalcular
ruta actual
índice del punto actual
```

También puede necesitar contexto:

```txt
si el objetivo se mueve
si hay caminos bloqueados
si hay costos
si hay rutas alternativas
si hay zonas prohibidas
si la ruta puede quedar inválida
```

---

## Qué produce

La integración puede producir:

```txt
ruta actual
lista de puntos
siguiente punto objetivo
estado de ruta válida
estado de ruta inválida
evento de llegada
solicitud de recálculo
```

Ejemplo:

```txt
CurrentRoute = [Punto1, Punto2, Punto3]
CurrentWaypointIndex = 0
```

Eso no significa que el NPC haya decidido perseguir.

Solo significa que existe una ruta para ejecutar una intención.

---

## Flujo general

El flujo sano es:

```txt
1. El comportamiento define un destino.
2. La integración solicita una ruta.
3. El sistema de pathfinding devuelve una lista de puntos.
4. El movimiento consume esos puntos.
5. La integración revisa si debe recalcular.
6. Al llegar, informa finalización.
```

Ejemplo conceptual:

```csharp
using System.Collections.Generic;
using UnityEngine;

public interface IPathfinder
{
    IReadOnlyList<Vector3> FindPath(Vector3 from, Vector3 to);
}

public class NPCPathRequest
{
    private readonly IPathfinder pathfinder;

    public NPCPathRequest(IPathfinder pathfinder)
    {
        this.pathfinder = pathfinder;
    }

    public IReadOnlyList<Vector3> RequestPath(Vector3 currentPosition, Vector3 targetPosition)
    {
        return pathfinder.FindPath(currentPosition, targetPosition);
    }
}
```

Este ejemplo solo pide una ruta.

No implementa el algoritmo.

No mueve.

No decide.

---

## Seguimiento de ruta

Una vez obtenida la ruta, el movimiento puede seguir puntos.

```csharp
using System.Collections.Generic;
using UnityEngine;

public class RouteFollower
{
    private readonly Transform owner;
    private readonly float speed;
    private readonly float arriveDistance;

    private IReadOnlyList<Vector3> route;
    private int currentIndex;

    public RouteFollower(Transform owner, float speed, float arriveDistance)
    {
        this.owner = owner;
        this.speed = speed;
        this.arriveDistance = arriveDistance;
    }

    public void SetRoute(IReadOnlyList<Vector3> newRoute)
    {
        route = newRoute;
        currentIndex = 0;
    }

    public void Tick(float deltaTime)
    {
        if (route == null || currentIndex >= route.Count)
        {
            return;
        }

        Vector3 target = route[currentIndex];
        Vector3 direction = target - owner.position;

        if (direction.magnitude <= arriveDistance)
        {
            currentIndex++;
            return;
        }

        owner.position += direction.normalized * speed * deltaTime;
    }
}
```

Este ejemplo sigue una ruta.

No calcula pathfinding.

No decide comportamiento.

---

## Relación con movimiento

La integración con pathfinding no reemplaza al movimiento.

Solo le entrega información para ejecutar desplazamiento.

```txt
Pathfinding
→ devuelve puntos de ruta.

Integración
→ administra consumo, recálculo y estado de ruta.

Movimiento
→ ejecuta desplazamiento hacia los puntos.
```

El seguimiento de ruta puede ser directo o puede combinarse con steering para suavizar el desplazamiento.

Ejemplo:

```txt
Ruta calculada
→ siguiente punto
→ steering hacia el punto
→ movimiento físico
```

La integración no debería decidir si el NPC persigue, huye, patrulla o ataca.

Solo ejecuta una intención ya definida.

---

## Cuándo conviene usarlo

Conviene integrar pathfinding cuando:

```txt
el mapa tiene obstáculos importantes
el NPC necesita rodear paredes
hay zonas bloqueadas
hay costos de movimiento
hay rutas alternativas
el objetivo no es alcanzable en línea recta
el movimiento directo falla
```

Pregunta clave:

```txt
¿El NPC necesita una ruta para llegar?
```

Si la respuesta es sí, pathfinding puede aportar valor.

---

## Cuándo NO conviene usarlo

No conviene integrar pathfinding si:

```txt
el NPC no se mueve
el movimiento directo alcanza
los recorridos son fijos
el mapa es abierto y simple
el costo no se justifica
solo se necesita una animación o desplazamiento básico
```

Ejemplos:

```txt
comerciante fijo
NPC de diálogo
torreta fija
enemigo en pasillo lineal
objeto interactivo
```

Regla:

```txt
No usar pathfinding si no hay problema real de navegación.
```

---

## Recalculo de ruta

La ruta no debería recalcularse por costumbre en cada frame.

Conviene recalcular cuando:

```txt
el objetivo se movió lo suficiente
la ruta quedó bloqueada
el NPC se desvió demasiado
cambió una regla del mapa
apareció una ruta inválida
pasó un intervalo definido
```

Riesgos de recalcular mal:

```txt
muchos NPCs pidiendo rutas al mismo tiempo
costos altos por frame
allocations innecesarias
comportamiento errático
rutas que cambian demasiado seguido
```

Regla:

```txt
Pathfinding debe pedirse cuando hace falta.

No por costumbre en cada frame.
```

---

## Riesgos comunes

Riesgos comunes al integrar pathfinding:

```txt
meter el algoritmo dentro del NPC
recalcular ruta cada frame
no separar cálculo de ruta y seguimiento
no manejar rutas inválidas
usar pathfinding donde alcanzaban waypoints
no visualizar la ruta
duplicar mapa lógico
hacer que pathfinding decida comportamiento
hacer que movimiento calcule rutas completas
```

Ejemplo de mala práctica:

```txt
Enemy.cs contiene detección, decisión, A Star, movimiento y ataque.
```

Problema:

```txt
Se mezclan responsabilidades.

El NPC absorbe mapa, algoritmo y comportamiento.
```

---

## Validación

La integración con pathfinding se valida revisando:

```txt
si se pide ruta cuando corresponde
si la ruta empieza cerca del NPC
si termina cerca del objetivo
si respeta obstáculos
si respeta zonas bloqueadas
si el NPC sigue la ruta
si recalcula con criterio
si maneja ruta inválida
```

Debug útil:

```txt
líneas de ruta
nodos visitados
punto actual de ruta
logs de solicitud
logs de recálculo
estado de ruta válida o inválida
```

---

## Regla final

Integrar pathfinding no es meter el algoritmo dentro del NPC.

Es consumir una ruta calculada por otro sistema.

El NPC define intención.

Pathfinding calcula ruta.

Movimiento ejecuta desplazamiento.
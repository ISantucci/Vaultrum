## Definicion

Pathfinding es el proceso de calcular una ruta entre un origen y un destino dentro de una estructura navegable.

No es un algoritmo especifico.

No es movimiento fisico.

No es comportamiento de NPC.

No es una representacion de mapa.

Pathfinding es el uso de una estructura del mapa y, si hace falta, un algoritmo para obtener un camino posible.

```txt
Origen
→ estructura navegable
→ calculo de ruta
→ destino
```

---

## Responsabilidad de esta nota

Esta nota explica que es pathfinding dentro de IA para desarrollo de mapas.

Su responsabilidad es definir:

```txt
que problema resuelve
que datos necesita
que devuelve
que sistemas suele consumir
que sistemas lo consumen a el
cuando conviene usarlo
cuando no conviene usarlo
```

Esta nota no debe explicar en profundidad algoritmos como A Star, Dijkstra o Theta Star.

Esos algoritmos pertenecen a la seccion `Algoritmos`.

---

## Problema que resuelve

Pathfinding resuelve el problema de encontrar por donde ir desde un punto hacia otro.

Se usa cuando no alcanza con moverse en linea recta o seguir una ruta fija.

Ejemplos:

```txt
hay obstaculos
hay multiples caminos
hay zonas bloqueadas
hay costos
hay rutas alternativas
el destino puede cambiar
el mapa tiene conexiones
```

Pregunta principal:

```txt
¿Como llego desde este origen hasta este destino respetando el mapa?
```

---

## Datos que necesita

Un sistema de pathfinding necesita datos claros.

Puede necesitar:

```txt
origen
destino
estructura navegable
vecinos
conexiones
costos
bloqueos
condiciones de validez
algoritmo de busqueda
criterio de llegada
```

Ejemplo:

```txt
Origen
→ nodo cercano al agente

Destino
→ nodo cercano al target

Estructura
→ nodos conectados

Algoritmo
→ A Star

Resultado
→ lista de nodos o posiciones
```

El pathfinding no deberia inventar esos datos.

Debe recibirlos o consultarlos desde sistemas responsables.

---

## Que devuelve

Pathfinding normalmente devuelve una ruta.

La ruta puede estar representada como:

```txt
lista de nodos
lista de posiciones
lista de waypoints
lista de celdas
ruta parcial
resultado fallido
```

Ejemplo:

```txt
Nodo A
→ Nodo C
→ Nodo F
→ Nodo H
```

El resultado no significa que el agente ya se movio.

Solo significa que existe una ruta calculada.

---

## Diferencia entre pathfinding y algoritmo

Pathfinding es el problema o proceso general.

El algoritmo es el procedimiento usado para resolverlo.

```txt
Pathfinding
→ necesito una ruta.

A Star
→ procedimiento posible para calcularla.

Dijkstra
→ procedimiento posible para calcular menor costo.

Theta Star
→ procedimiento posible para rutas any-angle.
```

No todos los casos de pathfinding usan el mismo algoritmo.

No todos los casos necesitan un algoritmo complejo.

---

## Diferencia entre pathfinding y movimiento

Pathfinding calcula una ruta.

Movimiento ejecuta esa ruta.

```txt
Pathfinding
→ devuelve puntos.

Movimiento
→ desplaza la entidad entre esos puntos.
```

Ejemplo:

```txt
Pathfinding devuelve:
A → B → C

Movimiento hace:
mover agente hacia A
luego hacia B
luego hacia C
```

Si una clase calcula ruta, mueve el NPC, decide comportamiento y actualiza animaciones, hay mezcla de responsabilidades.

---

## Diferencia entre pathfinding y decision

Pathfinding no decide por que un agente quiere ir a un lugar.

Eso pertenece a otro sistema.

Ejemplo:

```txt
Decision de NPC
→ quiero perseguir al jugador.

Pathfinding
→ calculo una ruta hacia el jugador.

Movimiento
→ ejecuto la ruta.
```

Pathfinding responde:

```txt
¿Por donde puedo ir?
```

No responde:

```txt
¿Por que quiero ir?
```

---

## Estructuras que puede consumir

Pathfinding puede trabajar sobre distintas estructuras.

Ejemplos:

```txt
nodos
grafos
grillas
GridMap y GridNode
waypoints conectados
mapas con costos
```

La estructura debe existir antes de calcular la ruta.

Si no hay estructura navegable, el pathfinding no tiene sobre que trabajar.

```txt
Primero estructura.
Despues ruta.
```

---

## Algoritmos que puede usar

Pathfinding puede usar distintos algoritmos segun el problema.

Ejemplos:

```txt
A Star
Dijkstra
Theta Star
BFS
DFS
```

Pero esta nota no debe desarrollar cada algoritmo.

Los algoritmos deben vivir en su seccion correspondiente.

Esta nota solo explica que el pathfinding puede consumirlos.

---

## Costos y bloqueos

Una ruta no siempre depende solo de distancia.

Puede depender de:

```txt
costo de nodo
costo de conexion
zonas bloqueadas
zonas peligrosas
terreno dificil
rutas desbloqueadas
condiciones dinamicas
```

El pathfinding puede usar esos datos para calcular una ruta valida o conveniente.

Pero los costos y bloqueos deben venir de la estructura o de reglas de mapa.

---

## Origen y destino

El origen y el destino pueden ser:

```txt
nodos
celdas
waypoints
posiciones reales
```

En muchos casos, el agente y el target no estan exactamente sobre nodos.

Entonces puede hacer falta convertir:

```txt
posicion real del agente
→ nodo cercano al origen

posicion real del target
→ nodo cercano al destino
```

Y despues:

```txt
ruta por nodos
→ llegada final al target real
```

Esta separacion evita confundir navegacion logica con posicion fisica exacta.

---

## Flujo general de pathfinding

Un flujo sano puede ser:

```txt
1. Recibir origen real.
2. Recibir destino real.
3. Consultar estructura navegable.
4. Buscar nodo o celda inicial si corresponde.
5. Buscar nodo o celda objetivo si corresponde.
6. Elegir algoritmo segun el problema.
7. Calcular ruta.
8. Validar si la ruta existe.
9. Devolver ruta al sistema consumidor.
10. Debuggear visualmente si corresponde.
```

La ruta debe devolverse.

No ejecutarse dentro del algoritmo.

---

## Ejemplo conceptual en codigo

```csharp
using System;
using System.Collections.Generic;

public class PathfindingService<TNode>
{
    private readonly Func<TNode, IEnumerable<TNode>> _getNeighbors;
    private readonly Func<TNode, TNode, float> _getCost;
    private readonly Func<TNode, TNode, float> _heuristic;

    public PathfindingService(
        Func<TNode, IEnumerable<TNode>> getNeighbors,
        Func<TNode, TNode, float> getCost,
        Func<TNode, TNode, float> heuristic)
    {
        _getNeighbors = getNeighbors;
        _getCost = getCost;
        _heuristic = heuristic;
    }

    public List<TNode> FindPath(TNode start, TNode goal)
    {
        return AStar.FindPath(
            start,
            goal,
            _getNeighbors,
            _getCost,
            _heuristic
        );
    }
}
```

Este ejemplo muestra un servicio que usa un algoritmo.

El servicio no sabe si el nodo es `GridNode`, `MapNode` o `PF_Node`.

Recibe funciones.

Devuelve una ruta.

No mueve entidades.

No decide comportamiento.

---

## Ejemplo de uso correcto

Uso correcto:

```txt
Mapa
→ expone nodos y vecinos.

Reglas de mapa
→ exponen costos o bloqueos.

Algoritmo
→ calcula ruta.

Pathfinding
→ coordina el calculo de ruta.

Movimiento
→ consume la ruta.
```

Ejemplo:

```txt
Origen real
→ nodo inicial

Target real
→ nodo objetivo

A Star
→ ruta por nodos

Movimiento
→ recorre ruta
```

---

## Ejemplo de uso incorrecto

Uso incorrecto:

```txt
Pathfinding
→ detecta jugador
→ decide perseguir
→ calcula ruta
→ mueve NPC
→ ataca
→ actualiza UI
```

Eso no es un sistema de pathfinding limpio.

Es una mezcla de percepcion, decision, navegacion, movimiento y gameplay.

---

## Cuando conviene usar pathfinding

Conviene usar pathfinding cuando:

```txt
el destino es variable
hay obstaculos
hay multiples rutas
hay costos
hay caminos bloqueados
el agente necesita elegir por donde ir
una ruta fija no alcanza
```

Ejemplos:

```txt
enemigo que persigue al jugador
unidad que se mueve por un mapa tactico
agente que debe rodear obstaculos
sistema que busca ruta entre zonas
```

---

## Cuando NO conviene usar pathfinding

No conviene usar pathfinding cuando:

```txt
el recorrido es fijo
no hay obstaculos relevantes
no hay rutas alternativas
el agente solo sigue una secuencia definida
una linea directa alcanza
waypoints simples alcanzan
```

Pathfinding agrega complejidad.

Debe usarse cuando resuelve un problema real.

---

## Cuando implementar pathfinding

Conviene implementar pathfinding cuando existe una necesidad real de calcular rutas variables.

No alcanza con que una entidad se mueva.

Debe existir un problema de navegacion.

Implementar pathfinding tiene sentido cuando:

```txt
el destino cambia durante la partida
el agente debe rodear obstaculos
existen multiples caminos posibles
hay zonas bloqueadas o desbloqueables
hay costos de movimiento
hay rutas alternativas
el mapa puede cambiar
el recorrido no puede resolverse con waypoints fijos
la ruta debe adaptarse al estado del mundo
```

Ejemplo correcto:

```txt
Un enemigo debe perseguir al jugador en un escenario con paredes.

El jugador cambia de posicion.
El camino directo puede estar bloqueado.
Hay varias rutas posibles.

→ Pathfinding tiene sentido.
```

Otro ejemplo correcto:

```txt
Una unidad tactica debe moverse a una celda elegida por el jugador.

El destino cambia.
El mapa tiene celdas bloqueadas.
El sistema debe encontrar una ruta valida.

→ Pathfinding tiene sentido.
```

---

## Cuando NO implementar pathfinding

No conviene implementar pathfinding si el problema puede resolverse con una solucion mas simple.

No implementar pathfinding cuando:

```txt
el recorrido es fijo
el agente siempre sigue el mismo camino
no hay obstaculos relevantes
no hay rutas alternativas
el destino no cambia
el movimiento puede ser directo
una secuencia de waypoints alcanza
una animacion o spline alcanza
el costo tecnico no se justifica
```

Ejemplo:

```txt
Un enemigo de tower defense siempre sigue una ruta fija desde entrada hasta base.

Si no elige caminos, no esquiva obstaculos y no recalcula ruta:

→ Waypoints alcanzan.
→ Pathfinding puede ser sobrearquitectura.
```

Otro ejemplo:

```txt
Una plataforma se mueve entre dos puntos.

→ No necesita pathfinding.
→ Necesita movimiento interpolado o ruta fija.
```

---

## Por que no implementar pathfinding de mas

Pathfinding agrega complejidad tecnica.

Implementarlo sin necesidad puede generar:

```txt
mas codigo
mas puntos de fallo
mas debug
mas costo de CPU
mas problemas de sincronizacion
mas dependencia entre sistemas
mas dificultad para balancear movimiento
mas dificultad para entender errores
```

Un sistema simple y mantenible suele ser mejor que un sistema avanzado innecesario.

Regla:

```txt
Si el camino ya esta decidido por diseño,
no hace falta calcularlo por algoritmo.
```

---

## Mala practica al implementar pathfinding

Pathfinding se vuelve mala practica cuando se usa para resolver problemas que no le corresponden.

Malas practicas comunes:

```txt
usar pathfinding para todo movimiento
calcular ruta cada frame sin necesidad
meter pathfinding dentro del script del NPC
hacer que el algoritmo mueva la entidad
hacer que el pathfinding decida comportamiento
usar A Star sin estructura navegable clara
ignorar costos de rendimiento
no manejar rutas fallidas
no tener debug visual
duplicar logica de mapa dentro del NPC
hacer que cada agente recalcule lo mismo por separado
```

Ejemplo de mala practica:

```txt
Enemy.cs
→ detecta jugador
→ decide perseguir
→ calcula A Star
→ mueve al enemigo
→ actualiza animacion
→ ataca
→ modifica UI
```

Problema:

```txt
percepcion
decision
pathfinding
movimiento
combate
UI
```

quedaron mezclados en una sola clase.

---
## Costos de implementacion

Pathfinding tiene costo de implementacion y mantenimiento.

Antes de implementarlo, considerar:

```txt
crear o adaptar estructura navegable
definir vecinos
definir costos
definir bloqueos
elegir algoritmo
manejar rutas fallidas
separar ruta de movimiento
hacer debug visual
optimizar frecuencia de recalculo
probar casos borde
```

No es solo “agregar A Star”.

Es construir el sistema alrededor para que el algoritmo tenga datos confiables.

---
## Costos de optimizacion

Pathfinding puede afectar rendimiento si se usa sin control.

Costos posibles:

```txt
CPU por busqueda de ruta
CPU por recorrer vecinos
CPU por calcular heuristicas
CPU por validar obstaculos
CPU por line of sight si aplica
memoria por listas abiertas y cerradas
allocations si se crean listas nuevas constantemente
picos si muchos agentes recalculan al mismo tiempo
costo de debug si se dibuja demasiado
```

Problemas frecuentes:

```txt
recalcular ruta cada frame
recalcular todos los agentes en el mismo frame
crear listas nuevas en cada busqueda
usar LINQ en loops criticos
buscar nodos con FindObjectsOfType
validar line of sight demasiadas veces
no cachear rutas cuando corresponde
```

---
## Criterio de optimizacion

Pathfinding debe calcularse con frecuencia controlada.

Opciones para reducir costo:

```txt
recalcular solo cuando cambia el destino
recalcular solo cuando cambia el mapa
recalcular cada cierto intervalo
distribuir calculos entre frames
cachear rutas si el mapa no cambia
reutilizar listas o estructuras internas
usar pooling si hay muchas consultas
limitar cantidad de agentes que recalculan por frame
usar rutas parciales
usar waypoints para casos simples
usar pathfinding solo para agentes que realmente lo necesitan
```

Ejemplo:

```txt
Mala practica:
100 enemigos recalculan A Star en Update.

Mejor:
los enemigos recalculan solo cuando el target cambia lo suficiente,
o cuando su ruta queda invalida,
o en intervalos escalonados.
```

---
## Preguntas antes de implementar

Antes de implementar pathfinding, una IA debe responder:

```txt
¿Que problema real de navegacion existe?
¿Una ruta fija alcanza?
¿Waypoints alcanzan?
¿Movimiento directo alcanza?
¿El destino cambia?
¿Hay obstaculos?
¿Hay rutas alternativas?
¿Hay estructura navegable?
¿Cuantos agentes van a usarlo?
¿Cada cuanto se recalcula?
¿Que pasa si no hay ruta?
¿Como se va a debuggear?
¿Que costo de CPU puede tener?
¿Que allocations puede generar?
¿Como se va a validar?
```

Si estas preguntas no tienen respuesta, todavia no conviene implementar.

---
## Regla de decision

```txt
Si el agente solo necesita seguir puntos fijos
→ usar waypoints.

Si el agente necesita elegir ruta en una estructura navegable
→ evaluar pathfinding.

Si hay un destino concreto y una heuristica util
→ evaluar A Star.

Si se necesitan costos desde un origen hacia varios destinos
→ evaluar Dijkstra.

Si la ruta es valida pero demasiado angular
→ evaluar suavizado.

Si la ruta necesita any-angle y line of sight confiable
→ evaluar Theta Star.
```

La tecnica debe responder al problema.

No al deseo de usar una tecnica avanzada.

---

## Validacion visual

El pathfinding debe poder validarse visualmente.

Una buena validacion puede mostrar:

```txt
origen
destino
nodo inicial
nodo objetivo
ruta calculada
conexiones exploradas
nodos bloqueados
costos
ruta fallida
```

Esto permite detectar errores como:

```txt
ruta atravesando obstaculos
nodo inicial incorrecto
nodo objetivo incorrecto
costos mal interpretados
conexiones faltantes
ruta demasiado angular
```

Sin debug visual, el pathfinding puede parecer correcto en codigo pero fallar en escena.

---

## Errores comunes

Errores comunes al trabajar con pathfinding:

```txt
usar pathfinding sin estructura navegable
confundir pathfinding con movimiento
confundir pathfinding con decisión de NPC
calcular rutas cada frame sin necesidad
ignorar costos y bloqueos
no manejar rutas fallidas
no separar target real de nodo objetivo
acoplar el algoritmo a una clase concreta
no validar visualmente
usar pathfinding cuando waypoints alcanzaban
usar pathfinding cuando movimiento directo alcanzaba
usar A Star por costumbre sin evaluar el problema
usar Theta Star cuando A Star suavizado alcanzaba
```

Muchos errores aparecen por aplicar una técnica avanzada antes de entender el problema real.

Pathfinding debe resolver una necesidad de navegación.

No debe agregarse solo porque una entidad se mueve.

Regla:

```txt
Si una ruta fija alcanza
→ usar waypoints.

Si el movimiento directo alcanza
→ no hace falta pathfinding.

Si hay que calcular una ruta variable sobre una estructura navegable
→ evaluar pathfinding.

Si la ruta existe pero se ve demasiado angular
→ evaluar suavizado.

Si el suavizado no alcanza y hay line of sight confiable
→ evaluar Theta Star.
```
```

---

## Criterio para una IA

Cuando una IA proponga pathfinding, debe justificar:

```txt
que problema de ruta existe
que estructura navegable se usa
que datos recibe
que algoritmo consume
que devuelve
quien consume la ruta
como se manejan costos y bloqueos
que pasa si no hay ruta
como se valida visualmente
```

No alcanza con decir:

```txt
Usar pathfinding.
```

Debe explicar que responsabilidad cumple dentro del sistema.

---

## Checklist

Antes de implementar pathfinding, revisar:

```txt
¿Existe una estructura navegable?
¿Hay origen?
¿Hay destino?
¿El destino puede cambiar?
¿Hay vecinos o conexiones?
¿Hay costos?
¿Hay bloqueos?
¿Hace falta algoritmo?
¿Que algoritmo corresponde?
¿La ruta se devuelve sin mover entidades?
¿Se maneja el caso sin ruta?
¿Se puede debuggear visualmente?
```

---

## Regla final

Pathfinding no es la IA completa.

Pathfinding calcula rutas.

```txt
Estructura navegable
→ algoritmo
→ ruta calculada
→ sistema consumidor
```
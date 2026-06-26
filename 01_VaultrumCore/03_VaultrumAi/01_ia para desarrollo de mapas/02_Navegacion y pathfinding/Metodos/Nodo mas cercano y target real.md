## Definicion

Nodo mas cercano y target real es un criterio de navegacion que separa la posicion exacta del mundo de la estructura logica usada para calcular rutas.

Un agente y un objetivo no siempre estan colocados exactamente sobre nodos.

Por eso, muchas veces hace falta:

```txt
posicion real del agente
→ nodo cercano de origen

posicion real del target
→ nodo cercano de destino

ruta por nodos
→ llegada final al target real
```

No es un algoritmo de pathfinding completo.

No reemplaza a A Star, Dijkstra o Theta Star.

No mueve entidades por si mismo.

Existe para conectar el mundo fisico con una representacion navegable.

---

## Responsabilidad de esta nota

Esta nota explica como conectar posiciones reales con una estructura de nodos.

Su responsabilidad es definir:

```txt
que problema resuelve
que datos necesita
como se elige nodo cercano
como se diferencia nodo objetivo de target real
cuando conviene aplicarlo
cuando no conviene aplicarlo
que costo tiene
como validarlo
```

Esta nota no debe explicar todo el pathfinding.

El pathfinding consume esta preparacion cuando necesita calcular una ruta sobre nodos.

---

## Problema que resuelve

El problema aparece cuando el sistema de rutas trabaja con nodos, pero el mundo real trabaja con posiciones libres.

Ejemplo:

```txt
NPC real:
(2.4, 0, 7.8)

Target real:
(15.2, 0, 3.1)

Nodos disponibles:
Nodo A, Nodo B, Nodo C, Nodo D
```

El pathfinding no sabe calcular desde cualquier coordenada libre si su estructura trabaja por nodos.

Entonces necesita conectar esas posiciones con nodos.

Pregunta principal:

```txt
¿Como conecto una posicion real con una ruta por nodos?
```

---

## Idea central

La idea central es separar tres cosas:

```txt
posicion real
nodo de navegacion
ruta logica
```

Ejemplo:

```txt
El jugador esta en una posicion real.

El sistema busca el nodo mas cercano al jugador.

Calcula ruta hasta el nodo mas cercano al destino.

Luego el agente se mueve desde el ultimo nodo hacia el target real.
```

Esto evita exigir que todos los objetivos esten perfectamente ubicados sobre nodos.

---

## Datos que necesita

Este criterio puede necesitar:

```txt
posicion real de origen
posicion real de destino
lista de nodos disponibles
distancia entre posicion y nodo
criterio de validez del nodo
line of sight opcional
radio maximo de busqueda opcional
estado bloqueado o disponible
```

No alcanza con buscar el nodo matematicamente mas cercano si ese nodo no es valido.

---

## Que devuelve

Puede devolver:

```txt
nodo cercano al origen
nodo cercano al destino
ruta por nodos
punto final real
resultado fallido si no hay nodo valido
```

Ejemplo:

```txt
Origen real
→ Nodo A

Target real
→ Nodo F

Ruta:
A → C → F

Final:
salir de F hacia target real
```

---

## Nodo cercano al origen

El nodo cercano al origen permite entrar a la estructura navegable.

Ejemplo:

```txt
NPC en posicion real
→ buscar nodo navegable mas cercano
```

Pero el nodo no debe elegirse solo por distancia si hay restricciones.

Tambien puede revisarse:

```txt
si esta bloqueado
si es alcanzable
si tiene line of sight
si pertenece a una zona valida
si esta dentro de un radio razonable
```

---

## Nodo cercano al target

El nodo cercano al target permite calcular la ruta hacia una zona cercana al objetivo.

Ejemplo:

```txt
Target real
→ buscar nodo navegable mas cercano
```

El nodo cercano al target no siempre es el destino final.

Es el punto donde termina la ruta logica.

Despues puede hacer falta un movimiento final hacia la posicion real.

---

## Target real

El target real es la posicion exacta a la que se quiere llegar.

Puede ser:

```txt
posicion del jugador
punto clickeado por el usuario
posicion de un item
zona de interaccion
objetivo dinamico
punto del mundo
```

El target real puede no coincidir con ningun nodo.

Por eso, la ruta por nodos y la llegada final deben separarse.

---

## Flujo recomendado

Flujo sano:

```txt
1. Recibir posicion real de origen.
2. Recibir posicion real del target.
3. Buscar nodo valido cercano al origen.
4. Buscar nodo valido cercano al target.
5. Calcular ruta entre nodos.
6. Entregar ruta al sistema consumidor.
7. Mover por la ruta.
8. Al llegar al ultimo nodo, moverse hacia target real si corresponde.
```

La llegada al target real pertenece al movimiento o al sistema consumidor.

No al algoritmo de busqueda.

---

## Ejemplo conceptual en codigo

```csharp
using System.Collections.Generic;
using UnityEngine;

public static class ClosestNodeFinder
{
    public static bool TryFindClosestNode<TNode>(
        Vector3 worldPosition,
        IEnumerable<TNode> nodes,
        System.Func<TNode, Vector3> getPosition,
        System.Func<TNode, bool> isValid,
        out TNode closestNode)
    {
        closestNode = default;

        float bestDistance = float.PositiveInfinity;
        bool found = false;

        foreach (TNode node in nodes)
        {
            if (!isValid(node)) continue;

            float distance = Vector3.Distance(worldPosition, getPosition(node));

            if (distance < bestDistance)
            {
                bestDistance = distance;
                closestNode = node;
                found = true;
            }
        }

        return found;
    }
}
```

Este ejemplo busca un nodo valido cercano.

No calcula ruta.

No mueve entidades.

No decide comportamiento.

Solo conecta posicion real con estructura logica.

---

## Ejemplo de uso correcto

Uso correcto:

```txt
NPC quiere ir a un target real.

Sistema:
1. busca nodo cercano al NPC,
2. busca nodo cercano al target,
3. calcula ruta por nodos,
4. devuelve ruta,
5. movimiento ejecuta ruta y llegada final.
```

Cada parte tiene una responsabilidad separada.

---

## Ejemplo de uso incorrecto

Uso incorrecto:

```txt
ClosestNodeFinder
→ busca nodo cercano
→ calcula A Star
→ mueve NPC
→ decide si atacar
→ actualiza animacion
```

Eso mezcla demasiadas responsabilidades.

Buscar nodo cercano debe ser una preparacion para pathfinding, no toda la IA.

---

## Cuando implementar este criterio

Conviene implementarlo cuando:

```txt
la estructura de navegacion usa nodos
el origen puede estar fuera de un nodo
el target puede estar fuera de un nodo
el jugador puede elegir posiciones libres
los objetivos se mueven en espacio libre
la ruta se calcula por nodos pero el movimiento ocurre en mundo real
```

Ejemplo correcto:

```txt
El jugador hace click en cualquier punto del escenario.

El sistema de pathfinding usa nodos.

→ Hay que conectar el click real con el nodo mas cercano valido.
```

---

## Cuando NO implementarlo

No conviene implementarlo cuando:

```txt
el origen y destino siempre son nodos
el juego funciona estrictamente por grilla
el movimiento solo sigue waypoints fijos
el target siempre esta preasignado a una posicion logica
la estructura ya resuelve posiciones reales de otra forma
```

Ejemplo:

```txt
Juego tactico por turnos donde el jugador siempre elige una celda.

→ No hace falta buscar nodo cercano libre.
→ La celda elegida ya es el destino logico.
```

---

## Por que no implementarlo de mas

Buscar nodo cercano agrega otra capa de decision espacial.

Si se implementa sin necesidad puede generar:

```txt
errores de seleccion
nodos incorrectos
rutas raras
agentes yendo a puntos no esperados
costos extra de busqueda
debug mas dificil
```

Regla:

```txt
Si el destino ya esta expresado en la estructura navegable,
no hace falta convertirlo.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
elegir siempre el nodo matematicamente mas cercano sin validar
ignorar bloqueos
ignorar si el nodo es alcanzable
ignorar line of sight cuando importa
buscar entre todos los nodos cada frame
repetir busquedas para muchos agentes sin cache
mezclar busqueda de nodo con movimiento
mezclar busqueda de nodo con decision de NPC
no manejar caso sin nodo valido
```

Ejemplo de mala practica:

```txt
El target esta detras de una pared.

El nodo mas cercano matematicamente esta del otro lado.

El sistema lo elige igual.

Resultado:
ruta incoherente o agente intentando atravesar pared.
```

---

## Costos de implementacion

Implementar este criterio requiere:

```txt
tener lista de nodos disponible
definir criterio de validez
definir como medir distancia
decidir si usar line of sight
manejar caso sin nodo valido
definir radio maximo si corresponde
debuggear nodo elegido
separar origen logico y target real
```

No es solo buscar el minimo por distancia.

---

## Costos de optimizacion

Buscar nodo cercano puede ser costoso si hay muchos nodos o muchas consultas.

Costos posibles:

```txt
CPU por recorrer nodos
CPU por calcular distancias
CPU por validar line of sight
CPU por filtros de validez
allocations si se crean listas temporales
picos si muchos agentes buscan nodo al mismo tiempo
```

Problemas frecuentes:

```txt
buscar entre todos los nodos cada frame
usar Vector3.Distance cuando alcanza con distancia cuadrada
validar raycasts demasiadas veces
no cachear resultados
no usar estructuras espaciales cuando el mapa es grande
```

---

## Criterio de optimizacion

Opciones para reducir costo:

```txt
buscar solo cuando cambia el target
usar distancia cuadrada para comparar
filtrar primero por estado valido
usar radio maximo
cachear nodo cercano si el target no cambia
actualizar en intervalos
dividir el mapa por sectores
usar grilla espacial o estructura de consulta si hay muchos nodos
evitar line of sight salvo que sea necesario
```

Ejemplo:

```txt
Mala practica:
cada enemigo busca el nodo mas cercano al jugador en cada Update.

Mejor:
recalcular cuando el jugador se movio suficiente,
o cachear el nodo cercano al jugador por un tiempo corto.
```

---

## Preguntas antes de implementar

Antes de implementar este criterio, una IA debe responder:

```txt
¿El sistema usa nodos?
¿El origen puede estar fuera de un nodo?
¿El target puede estar fuera de un nodo?
¿Que significa nodo valido?
¿La distancia alcanza como criterio?
¿Hace falta line of sight?
¿Que pasa si no hay nodo valido?
¿Cuantos nodos existen?
¿Cuantos agentes consultan esto?
¿Cada cuanto se busca?
¿Como se va a debuggear?
```

Si estas preguntas no tienen respuesta, la implementacion puede elegir nodos incorrectos.

---

## Validacion visual

Debe poder verse:

```txt
posicion real de origen
posicion real del target
nodo cercano al origen
nodo cercano al target
linea entre posicion real y nodo elegido
ruta por nodos
movimiento final hacia target real
nodos descartados si corresponde
```

Esto ayuda a detectar:

```txt
nodo cercano incorrecto
target real mal interpretado
nodo bloqueado elegido por error
ruta valida pero llegada final incorrecta
distancia mal calculada
```

---

## Errores comunes

```txt
confundir nodo objetivo con target real
elegir nodo mas cercano sin validar
no manejar caso sin nodo
buscar nodos cada frame sin necesidad
hacer que el buscador mueva al agente
hacer que el buscador decida comportamiento
ignorar bloqueos
ignorar obstaculos entre target y nodo
no debuggear visualmente
```

---

## Criterio para una IA

Cuando una IA proponga nodo cercano y target real, debe justificar:

```txt
por que origen o destino no estan sobre nodos
como se busca el nodo cercano
que hace que un nodo sea valido
que pasa si no hay nodo valido
como se conecta la ruta con el target real
quien ejecuta la llegada final
que costo tiene la busqueda
como se valida visualmente
```

No alcanza con decir:

```txt
Buscar el nodo mas cercano.
```

Debe explicar cercano segun que criterio y valido bajo que reglas.

---

## Checklist

Antes de implementar nodo cercano y target real, revisar:

```txt
¿Hay estructura por nodos?
¿Origen y target pueden estar fuera de nodos?
¿La lista de nodos esta disponible?
¿Existe criterio de nodo valido?
¿Se evita elegir nodos bloqueados?
¿Se maneja caso sin nodo valido?
¿Se diferencia nodo objetivo de target real?
¿La llegada final esta separada del pathfinding?
¿La busqueda tiene frecuencia controlada?
¿Se puede debuggear visualmente?
```

---

## Regla final

El nodo cercano no es el destino real.

Es un puente entre mundo fisico y mapa logico.

```txt
Posicion real
→ nodo cercano valido
→ ruta logica
→ llegada final
```
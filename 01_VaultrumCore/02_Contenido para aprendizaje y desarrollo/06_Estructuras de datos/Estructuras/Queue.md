## Definicion

Una Queue, o cola, es una estructura de datos en la que el primer elemento en entrar es el primero en salir.

Su regla principal es:

```txt
FIFO
→ First In, First Out
→ primero en entrar, primero en salir
```

Esto significa que la cola funciona como una fila.

El primer elemento agregado queda adelante.

Cuando se saca un elemento, se saca primero el que llevaba mas tiempo esperando.

Ejemplo conceptual:

```txt
Enqueue A
Enqueue B
Enqueue C

Queue:
A ← frente
B
C ← final

Dequeue
→ sale A
```

Una Queue es util cuando el sistema necesita procesar elementos en el mismo orden en que fueron agregados.

---

## Responsabilidad

La responsabilidad de una Queue es guardar elementos respetando orden FIFO.

Debe responder:

```txt
¿Cual fue el primer elemento agregado que todavia no fue procesado?
¿Puedo consultar el siguiente elemento sin sacarlo?
¿Puedo sacar el siguiente elemento?
¿Hay elementos pendientes?
```

Una Queue organiza pendientes.

No interpreta por si sola que significa cada pendiente.

Ejemplo:

```txt
Queue
→ guarda eventos pendientes.

EventQueue
→ decide cuando procesarlos.

Sistema consumidor
→ ejecuta la accion correspondiente.
```

---

## Que NO debe hacer

Una Queue no debe absorber responsabilidades del sistema que la usa.

No debe:

```txt
decidir gameplay
ejecutar eventos por si sola
saber que significa cada elemento
validar reglas del juego
actualizar UI
crear enemigos por si sola
resolver prioridad
ordenar por importancia
manejar conexiones entre datos
```

Ejemplo incorrecto:

```txt
Queue
→ guarda enemigo
→ decide cuando spawnear
→ instancia enemigo
→ actualiza UI
→ cambia dificultad
```

Ejemplo correcto:

```txt
SpawnQueue
→ usa Queue para guardar enemigos pendientes.

Spawner
→ procesa el siguiente enemigo.

WaveSystem
→ define reglas de oleada.

UI
→ muestra progreso.
```

Regla:

```txt
Queue guarda orden de llegada.
No decide comportamiento.
```

---

## Que problema resuelve

La Queue resuelve problemas donde importa procesar primero lo que llego primero.

Casos que puede resolver:

```txt
eventos pendientes
oleadas de enemigos
turnos
acciones en cola
mensajes
tareas asincronas
animaciones pendientes
ordenes de unidades
procesamiento por lotes
```

Ejemplo:

```txt
Llegan tres enemigos para spawnear.

Enemy A
Enemy B
Enemy C

El spawner debe procesarlos en ese orden.

Primero A.
Despues B.
Despues C.
```

Esto encaja naturalmente con una Queue.

Idea central:

```txt
Si el sistema necesita respetar orden de llegada,
una Queue suele ser una buena opcion.
```

---

## Datos que necesita

Una Queue necesita elementos del mismo tipo conceptual.

Ejemplos:

```txt
eventos
enemigos pendientes
acciones
mensajes
turnos
tareas
comandos pendientes
solicitudes de pathfinding
```

No necesita saber que significan internamente.

Ejemplo:

```txt
Queue<GameEvent>
→ guarda eventos pendientes.

Queue<EnemySpawnData>
→ guarda enemigos por aparecer.

Queue<TurnAction>
→ guarda acciones de turno.
```

La Queue solo necesita:

```txt
elemento a encolar
regla de procesamiento
capacidad si se quiere limitar
frecuencia de consumo si aplica
```

---

## Que produce

Una Queue puede producir:

```txt
siguiente elemento pendiente
elemento removido
cantidad de elementos
estado vacio/no vacio
```

Operaciones comunes:

```txt
Enqueue
→ agrega elemento al final.

Dequeue
→ saca y devuelve el elemento del frente.

Peek
→ consulta el elemento del frente sin sacarlo.

Count
→ indica cantidad de elementos.
```

La salida de una Queue debe ser interpretada por el sistema consumidor.

Ejemplo:

```txt
Dequeue
→ devuelve siguiente enemigo.

Spawner
→ instancia ese enemigo.
```

---

## Como funciona

Una Queue tiene tres operaciones principales.

```txt
Enqueue
→ agrega un elemento al final de la cola.

Dequeue
→ saca y devuelve el elemento del frente.

Peek
→ consulta el elemento del frente sin sacarlo.
```

Ejemplo basico en C#:

```csharp
using System.Collections.Generic;
using UnityEngine;

public class QueueExample : MonoBehaviour
{
    private Queue<string> spawnQueue = new Queue<string>();

    private void Start()
    {
        spawnQueue.Enqueue("Enemy A");
        spawnQueue.Enqueue("Enemy B");
        spawnQueue.Enqueue("Enemy C");

        Debug.Log(spawnQueue.Peek());
        // Muestra: Enemy A

        Debug.Log(spawnQueue.Dequeue());
        // Saca: Enemy A

        Debug.Log(spawnQueue.Dequeue());
        // Saca: Enemy B
    }
}
```

El orden de salida es igual al orden de entrada.

```txt
Entraron:
Enemy A
Enemy B
Enemy C

Salen:
Enemy A
Enemy B
Enemy C
```

Esto vuelve a la Queue ideal para pendientes ordenados.

---

## Sistemas consumidores comunes

Una Queue suele aparecer como soporte de sistemas que necesitan procesar elementos en orden de llegada.

Ejemplos:

```txt
Event Queue
→ procesa eventos pendientes en orden.

Spawner de oleadas
→ instancia enemigos en secuencia.

Sistema de turnos
→ resuelve acciones o participantes en orden.

Cola de tareas
→ procesa trabajos pendientes.

Mensajes de gameplay
→ despacha notificaciones en orden.
```

La Queue no implementa esos sistemas por si sola.

Solo ofrece la forma de acceso correcta:

```txt
primero en entrar
→ primero en salir
```

Ejemplo:

```txt
Sistema de oleadas
→ usa Queue porque necesita spawnear enemigos en orden.

Sistema de eventos
→ usa Queue porque necesita procesar eventos pendientes.

Sistema de turnos
→ usa Queue porque necesita respetar orden.
```

Regla:

```txt
Queue sirve cuando el sistema consumidor necesita orden de llegada.

Si el sistema necesita historial inverso,
prioridad o conexiones,
Queue no es la estructura correcta.
```

---

## Ejemplo aplicado: spawner de oleadas

Una Queue se combina bien con sistemas de oleadas porque permite procesar enemigos en orden.

Flujo:

```txt
Oleada define enemigos
→ se encolan datos de spawn
→ spawner toma el siguiente
→ instancia enemigo
→ espera intervalo
→ toma el siguiente
```

Ejemplo conceptual:

```csharp
public class EnemySpawnData
{
    public string EnemyId { get; }
    public int Amount { get; }

    public EnemySpawnData(string enemyId, int amount)
    {
        EnemyId = enemyId;
        Amount = amount;
    }
}
```

```csharp
using System.Collections.Generic;

public class SpawnQueue
{
    private readonly Queue<EnemySpawnData> queue = new Queue<EnemySpawnData>();

    public void EnqueueEnemy(EnemySpawnData data)
    {
        queue.Enqueue(data);
    }

    public bool HasPending()
    {
        return queue.Count > 0;
    }

    public EnemySpawnData GetNext()
    {
        if (queue.Count == 0)
        {
            return null;
        }

        return queue.Dequeue();
    }
}
```

Separacion de responsabilidades:

```txt
SpawnQueue
→ guarda pendientes.

Queue
→ mantiene orden FIFO.

Spawner
→ instancia enemigos.

WaveSystem
→ define contenido de oleada.
```

La Queue no sabe instanciar enemigos.

Solo entrega el siguiente dato pendiente.

---

## Como aplicarlo en videojuegos

En videojuegos, una Queue puede usarse cuando se necesita procesar elementos pendientes en orden.

Casos tipicos:

```txt
eventos de gameplay
oleadas de enemigos
mensajes pendientes
acciones de turno
solicitudes de pathfinding
ordenes de unidades
animaciones encadenadas
notificaciones
tareas de carga
```

Ejemplo en Tower Defense:

```txt
WaveSystem
→ carga enemigos de la oleada.

Queue
→ guarda enemigos pendientes.

Spawner
→ procesa uno por uno.
```

Esto evita que todos los enemigos aparezcan a la vez y permite controlar ritmo.

---

## Cuando conviene usar Queue

Conviene usar Queue cuando:

```txt
necesitas procesar en orden de llegada
hay elementos pendientes
hay tareas en espera
hay eventos a despachar
hay turnos ordenados
hay spawn secuencial
```

Preguntas utiles:

```txt
¿Lo primero que llega debe resolverse primero?
¿Hay una fila de pendientes?
¿Necesito mantener orden temporal?
¿Necesito consumir elementos de a uno?
```

Si la respuesta es si, Queue puede ser una buena opcion.

---

## Cuando NO conviene usar Queue

No conviene usar Queue si:

```txt
necesitas acceder al ultimo elemento primero
necesitas buscar elementos arbitrarios
necesitas prioridad
necesitas ordenar por valor
necesitas conexiones entre datos
necesitas recorrer todo constantemente
```

Ejemplos:

```txt
deshacer ultima accion
→ Stack.

enemigos ordenados por prioridad
→ ABB o estructura ordenada.

mapa conectado
→ Grafo.

lista simple de objetivos cercanos
→ List puede alcanzar.
```

Regla:

```txt
No usar Queue si el orden de llegada no importa.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
usar Queue cuando se necesita prioridad
usar Queue para buscar elementos arbitrarios
no chequear Count antes de Dequeue
encolar elementos sin limite
hacer que la Queue ejecute logica
mezclar cola con UI
procesar demasiados elementos por frame
no limpiar elementos invalidos
```

Ejemplo de mala practica:

```txt
La Queue decide que enemigo es mas peligroso y lo spawnea antes.
```

Problema:

```txt
Eso ya no es FIFO.
Si hay prioridad, se necesita otra estructura o una capa de seleccion.
```

---

## Costos de implementacion

Implementar una Queue suele ser simple.

El costo real aparece en el sistema consumidor.

Puede requerir:

```txt
definir que se encola
definir cuando se consume
definir frecuencia de procesamiento
definir limite de pendientes
definir que pasa con elementos invalidos
debug de cola
```

En un sistema de eventos, lo importante no es solo encolar.

Tambien importa:

```txt
cuando procesar
cuantos procesar por frame
que pasa si un evento falla
si el orden debe respetarse estrictamente
```

---

## Costos de optimizacion

Una Queue normalmente es barata.

Riesgos posibles:

```txt
cola infinita
procesar demasiados elementos en un frame
elementos pesados
allocations constantes
referencias invalidas
eventos acumulados sin limpiar
```

Alternativas:

```txt
limitar cantidad de elementos procesados por frame
limitar tamaño de cola
guardar datos livianos
limpiar elementos invalidos
usar pooling si hay objetos frecuentes
dividir colas por tipo si mejora claridad
```

Criterio:

```txt
Queue con datos livianos y consumo controlado
→ costo bajo.

Queue que acumula miles de eventos pesados
→ riesgo alto.
```

---

## Validacion

Validar una Queue implica revisar el sistema que la consume.

Para pendientes:

```txt
si guarda elementos en orden correcto
si devuelve primero el primer elemento agregado
si no falla con Queue vacia
si respeta ritmo de procesamiento
si no acumula pendientes infinitos
si el sistema consumidor interpreta bien el elemento devuelto
```

Debug util:

```txt
cantidad de elementos en Queue
siguiente elemento
logs de Enqueue
logs de Dequeue
historial de procesamiento
pruebas con cola vacia
```

---

## Preguntas antes de implementarla

Antes de usar Queue, preguntar:

```txt
¿Necesito procesar el primero que llego?
¿Hay una fila de pendientes?
¿Que elemento voy a guardar?
¿Cuando se consume cada elemento?
¿Cuantos elementos se procesan por frame?
¿Puede crecer sin limite?
¿Que pasa si el elemento ya no es valido?
¿Una lista simple alcanza?
```

---

## Errores comunes

Errores comunes:

```txt
usar Queue cuando se necesita Stack
usar Queue cuando se necesita prioridad
no chequear Count antes de Dequeue
encolar demasiados elementos
procesar todo en un solo frame
mezclar cola con UI
mezclar cola con reglas de gameplay
no limpiar elementos invalidos
```

---

## Criterio para una IA

Cuando una IA trabaje con Queue debe:

```txt
identificar si el problema es FIFO
explicar que elemento se encola
separar Queue del sistema consumidor
no hacer que la Queue decida comportamiento
proponer Queue para pendientes ordenados
validar caso de Queue vacia
considerar limite o ritmo de procesamiento
comparar con Stack, ABB o List si hay duda
```

Regla operativa:

```txt
Si lo primero que entro debe salir primero,
Queue tiene sentido.

Si no,
probablemente hay una estructura mejor.
```

---

## Checklist

Antes de cerrar una implementacion con Queue, revisar:

```txt
¿El problema realmente es FIFO?
¿Se guarda el dato correcto?
¿La Queue esta separada del sistema consumidor?
¿Se chequea si esta vacia antes de Dequeue?
¿Hay control sobre cuanto se procesa?
¿Puede crecer demasiado?
¿El sistema consumidor interpreta correctamente el elemento devuelto?
¿Una List, Stack o estructura con prioridad era mas adecuada?
```

---

## Regla final

```txt
Queue no es una lista cualquiera.

Es una forma simple y clara de procesar primero lo que estaba esperando primero.
```
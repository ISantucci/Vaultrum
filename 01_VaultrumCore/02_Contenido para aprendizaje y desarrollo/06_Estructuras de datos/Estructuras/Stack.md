## Definicion

Una Stack, o pila, es una estructura de datos en la que el ultimo elemento en entrar es el primero en salir.

Su regla principal es:

```txt
LIFO
→ Last In, First Out
→ ultimo en entrar, primero en salir
```

Esto significa que la pila funciona como una torre de elementos.

El elemento mas reciente queda arriba.

Cuando se saca un elemento, se saca primero el ultimo que fue agregado.

Ejemplo conceptual:

```txt
Push A
Push B
Push C

Stack:
C ← arriba
B
A

Pop
→ sale C
```

Una Stack es util cuando el sistema necesita recordar acciones, estados o datos en orden inverso al que ocurrieron.

---

## Responsabilidad

La responsabilidad de una Stack es guardar elementos respetando orden LIFO.

Debe responder:

```txt
¿Cual fue el ultimo elemento agregado?
¿Puedo consultar el ultimo elemento sin sacarlo?
¿Puedo sacar el ultimo elemento agregado?
¿Hay elementos guardados?
```

Una Stack organiza historial.

No interpreta por si sola que significa ese historial.

Ejemplo:

```txt
Stack
→ guarda comandos ejecutados.

Sistema de Undo
→ decide cuando deshacer.

Comando
→ sabe como revertirse.
```

---

## Que NO debe hacer

Una Stack no debe absorber responsabilidades del sistema que la usa.

No debe:

```txt
decidir gameplay
ejecutar acciones por si sola
saber que significa cada comando
validar reglas del juego
modificar UI
crear objetos
destruir objetos
aplicar daño
guardar estado global completo sin criterio
```

Ejemplo incorrecto:

```txt
Stack
→ guarda comando
→ decide si puede deshacer
→ modifica dinero
→ destruye torre
→ actualiza UI
```

Ejemplo correcto:

```txt
CommandHistory
→ usa Stack para guardar comandos.

Command
→ sabe Execute y Undo.

GameSystem
→ valida reglas del juego.

UI
→ muestra estado disponible.
```

Regla:

```txt
Stack guarda orden.
No decide comportamiento.
```

---

## Que problema resuelve

La Stack resuelve problemas donde importa acceder primero al ultimo elemento agregado.

Es especialmente util para manejar historial.

Ejemplo:

```txt
El jugador hace una accion.
Despues hace otra.
Despues hace otra.

Si quiere deshacer,
la primera accion que debe revertirse
es la ultima que hizo.
```

Esto encaja naturalmente con una pila.

Casos que puede resolver:

```txt
deshacer acciones
guardar historial temporal
volver al estado anterior
manejar navegacion hacia atras
guardar snapshots recientes
controlar acciones recientes
manejar pantallas o menus apilados
resolver procesos recursivos
procesar datos en orden inverso
```

Idea central:

```txt
Si el sistema necesita resolver primero lo ultimo que paso,
una Stack suele ser una buena opcion.
```

---

## Datos que necesita

Una Stack necesita elementos del mismo tipo conceptual.

Ejemplos:

```txt
comandos
acciones
estados previos
snapshots
pantallas abiertas
nodos pendientes
movimientos anteriores
```

No necesita saber que significan esos datos internamente.

Ejemplo:

```txt
Stack<ICommand>
→ guarda comandos.

Stack<GameSnapshot>
→ guarda estados anteriores.

Stack<MenuScreen>
→ guarda pantallas abiertas.
```

La Stack solo necesita:

```txt
elemento a guardar
capacidad si se quiere limitar historial
regla de limpieza si aplica
```

---

## Que produce

Una Stack puede producir:

```txt
ultimo elemento guardado
elemento removido
cantidad de elementos
estado vacio/no vacio
```

Operaciones comunes:

```txt
Push
→ agrega elemento.

Pop
→ saca y devuelve el ultimo elemento.

Peek
→ consulta el ultimo elemento sin sacarlo.

Count
→ indica cantidad de elementos.
```

La salida de una Stack debe ser interpretada por el sistema consumidor.

Ejemplo:

```txt
Pop
→ devuelve ultimo comando.

CommandHistory
→ llama Undo sobre ese comando.
```

---

## Como funciona

Una Stack tiene tres operaciones principales.

```txt
Push
→ agrega un elemento arriba de la pila.

Pop
→ saca y devuelve el elemento de arriba.

Peek
→ consulta el elemento de arriba sin sacarlo.
```

Ejemplo basico en C#:

```csharp
using System.Collections.Generic;
using UnityEngine;

public class StackExample : MonoBehaviour
{
    private Stack<string> actionHistory = new Stack<string>();

    private void Start()
    {
        actionHistory.Push("Build Tower");
        actionHistory.Push("Upgrade Tower");
        actionHistory.Push("Sell Tower");

        Debug.Log(actionHistory.Peek());
        // Muestra: Sell Tower

        Debug.Log(actionHistory.Pop());
        // Saca: Sell Tower

        Debug.Log(actionHistory.Pop());
        // Saca: Upgrade Tower
    }
}
```

El orden de salida es inverso al orden de entrada.

```txt
Entraron:
Build Tower
Upgrade Tower
Sell Tower

Salen:
Sell Tower
Upgrade Tower
Build Tower
```

Esto vuelve a la Stack ideal para historial de acciones.

---

## Sistemas consumidores comunes

Una Stack suele aparecer como soporte de sistemas que necesitan acceder primero a lo ultimo que ocurrio.

Ejemplos:

```txt
Undo
→ deshacer ultima accion ejecutada.

Historial de menus
→ cerrar primero la ultima pantalla abierta.

Navegacion hacia atras
→ volver al ultimo punto visitado.

Snapshots temporales
→ recuperar el ultimo estado guardado.

Procesamiento inverso
→ resolver elementos desde el mas reciente al mas antiguo.
```

La Stack no implementa esos sistemas por si sola.

Solo ofrece la forma de acceso correcta:

```txt
ultimo en entrar
→ primero en salir
```

Ejemplo:

```txt
Sistema de Undo
→ usa Stack porque necesita revertir la ultima accion.

Sistema de menus
→ usa Stack porque necesita cerrar la ultima pantalla abierta.

Sistema de navegacion
→ usa Stack porque necesita volver al ultimo punto visitado.
```

Regla:

```txt
Stack sirve cuando el sistema consumidor necesita historial inverso.

Si el sistema necesita orden de llegada,
prioridad o conexiones,
Stack no es la estructura correcta.
```

---

## Ejemplo aplicado: Undo con Command

Una Stack se combina muy bien con un sistema de comandos porque ambos respetan una idea clara:

```txt
la ultima accion ejecutada
→ debe ser la primera accion disponible para deshacer
```

Flujo:

```txt
Jugador ejecuta accion
→ se crea comando
→ se ejecuta comando
→ se guarda en Stack

Jugador presiona Undo
→ se hace Pop del ultimo comando
→ se llama Undo del comando
```

Ejemplo conceptual:

```csharp
public interface ICommand
{
    void Execute();
    void Undo();
}
```

```csharp
using System.Collections.Generic;

public class CommandHistory
{
    private readonly Stack<ICommand> undoStack = new Stack<ICommand>();

    public void ExecuteCommand(ICommand command)
    {
        command.Execute();
        undoStack.Push(command);
    }

    public void UndoLast()
    {
        if (undoStack.Count == 0)
        {
            return;
        }

        ICommand lastCommand = undoStack.Pop();
        lastCommand.Undo();
    }
}
```

Separacion de responsabilidades:

```txt
CommandHistory
→ guarda historial.

Stack
→ mantiene orden LIFO.

Command
→ sabe ejecutarse y deshacerse.

Sistema del juego
→ valida si la accion es posible.
```

La Stack no sabe que es una torre, una mejora o una venta.

Solo guarda el ultimo comando ejecutado.

---

## Como aplicarlo en videojuegos

En videojuegos, una Stack puede usarse cuando se necesita guardar elementos recientes y resolver primero el ultimo agregado.

Casos tipicos:

```txt
historial de comandos
undo
menus apilados
pantallas abiertas
snapshots recientes
estados anteriores
movimientos anteriores
acciones de editor
navegacion hacia atras
```

Ejemplo en Tower Defense:

```txt
BuildTowerCommand
→ construye una torre.

SellTowerCommand
→ vende una torre.

UpgradeTowerCommand
→ mejora una torre.
```

Cada accion ejecutada se guarda en una Stack.

```txt
Jugador construye torre
→ Execute
→ Push en Stack

Jugador mejora torre
→ Execute
→ Push en Stack

Jugador presiona Undo
→ Pop
→ Undo del ultimo comando
```

Esto permite revertir la ultima accion sin que la UI tenga que saber como deshacer cada operacion.

---

## Cuando conviene usar Stack

Conviene usar Stack cuando:

```txt
necesitas acceder al ultimo elemento agregado
necesitas deshacer acciones
necesitas volver al estado anterior
necesitas historial temporal
necesitas manejar pantallas apiladas
necesitas resolver datos en orden inverso
```

Preguntas utiles:

```txt
¿Lo ultimo que ocurrio debe resolverse primero?
¿Necesito deshacer la ultima accion?
¿Necesito volver un paso atras?
¿Necesito guardar estados anteriores?
```

Si la respuesta es si, Stack puede ser una buena opcion.

---

## Cuando NO conviene usar Stack

No conviene usar Stack si:

```txt
necesitas procesar elementos en orden de llegada
necesitas buscar elementos arbitrarios
necesitas recorrer todo constantemente
necesitas ordenar por prioridad
necesitas acceder al primero que entro
necesitas conexiones entre datos
```

Ejemplos:

```txt
spawn de enemigos en orden
→ Queue.

mapa con rutas conectadas
→ Grafo.

enemigos ordenados por progreso
→ ABB o estructura ordenada.

lista simple de objetos activos
→ List puede alcanzar.
```

Regla:

```txt
No usar Stack si el ultimo elemento no tiene prioridad real.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
usar Stack para todo historial sin limite
guardar objetos pesados innecesariamente
guardar referencias que luego se destruyen
hacer Undo sin validar estado actual
mezclar Stack con logica de gameplay
hacer que la UI manipule directamente la Stack
no controlar Stack vacia antes de Pop
```

Ejemplo de mala practica:

```txt
La UI hace Pop de la Stack y modifica directamente el juego.
```

Problema:

```txt
La UI queda acoplada al historial y a la logica de gameplay.
```

Mejor:

```txt
UI
→ solicita Undo.

CommandHistory
→ administra Stack.

Command
→ revierte accion.
```

---

## Costos de implementacion

Implementar una Stack suele ser simple.

El costo real aparece en el sistema consumidor.

Puede requerir:

```txt
definir que se guarda
definir limite de historial
definir limpieza de referencias
definir accion sobre el ultimo elemento
validar estados antes de revertir o recuperar
debug de historial
```

En un sistema de Undo, lo dificil no es la Stack.

Lo dificil es que cada accion sepa revertirse correctamente.

Ejemplo:

```txt
Colocar torre
→ Undo debe destruir torre y devolver recursos.

Mejorar torre
→ Undo debe volver stats y devolver costo.

Vender torre
→ Undo debe reconstruir torre y quitar recursos devueltos.
```

---

## Costos de optimizacion

Una Stack normalmente es barata.

Riesgos posibles:

```txt
historial infinito
snapshots muy pesados
referencias a objetos destruidos
allocations constantes
guardar copias completas del estado del juego
```

Alternativas:

```txt
limitar cantidad de acciones guardadas
guardar comandos en vez de snapshots completos
guardar datos minimos necesarios
limpiar referencias invalidas
usar pooling si hay objetos temporales frecuentes
```

Criterio:

```txt
Stack con comandos livianos
→ costo bajo.

Stack con snapshots completos del mundo
→ costo alto.
```

---

## Validacion

Validar una Stack implica revisar el sistema que la consume.

Para un historial:

```txt
si guarda elementos en el orden correcto
si devuelve primero el ultimo elemento agregado
si no falla con Stack vacia
si no quedan referencias rotas
si el limite de historial funciona
si el sistema consumidor interpreta bien el elemento devuelto
```

Debug util:

```txt
cantidad de elementos en Stack
nombre del ultimo elemento
logs de Push
logs de Pop
historial visible en inspector
pruebas de Pop repetido
```

---

## Preguntas antes de implementarla

Antes de usar Stack, preguntar:

```txt
¿Necesito acceder al ultimo elemento primero?
¿Necesito historial?
¿Que elemento voy a guardar?
¿Guardar el objeto completo o un comando?
¿Necesito recuperar o revertir el ultimo elemento?
¿El historial debe tener limite?
¿Que pasa si el objeto guardado ya no existe?
¿Una lista simple alcanza?
```

---

## Errores comunes

Errores comunes:

```txt
usar Stack cuando se necesita Queue
usar Stack para buscar elementos arbitrarios
no chequear Count antes de Pop
guardar demasiada informacion
hacer una recuperacion incompleta del elemento
mezclar historial con UI
mezclar historial con reglas de gameplay
```

---

## Criterio para una IA

Cuando una IA trabaje con Stack debe:

```txt
identificar si el problema es LIFO
explicar que elemento se guarda
separar Stack del sistema consumidor
no hacer que la Stack decida comportamiento
proponer Stack para historial inverso cuando corresponda
evitar snapshots pesados si comandos o datos minimos alcanzan
validar caso de Stack vacia
considerar limite de historial
comparar con Queue o List si hay duda
```

Regla operativa:

```txt
Si lo ultimo que entro debe salir primero,
Stack tiene sentido.

Si no,
probablemente hay una estructura mejor.
```

---

## Checklist

Antes de cerrar una implementacion con Stack, revisar:

```txt
¿El problema realmente es LIFO?
¿Se guarda el dato correcto?
¿La Stack esta separada del sistema consumidor?
¿Se chequea si esta vacia antes de Pop?
¿Hay limite de historial si puede crecer mucho?
¿El sistema consumidor interpreta correctamente el elemento devuelto?
¿Se evitan referencias rotas?
¿Una List o Queue era mas adecuada?
```

---

## Regla final

```txt
Stack no es historial por magia.

Es una forma simple y potente de acceder primero a lo ultimo que ocurrio.
```
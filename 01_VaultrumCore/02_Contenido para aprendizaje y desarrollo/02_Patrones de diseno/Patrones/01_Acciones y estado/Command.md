## Definicion

Command es un patron de diseno que encapsula una accion dentro de un objeto.

En lugar de ejecutar una accion directamente desde quien la dispara, se representa esa accion como un comando.

```txt
Intencion
→ comando
→ ejecucion
→ resultado
```

Esto permite tratar acciones importantes de forma mas controlada, clara y reutilizable.

---

## Idea central

Command separa la accion de quien la solicita.

```txt
UI / input / sistema
→ solicita una accion

Command
→ representa esa accion

Sistema ejecutor
→ decide cuando y como ejecutarla
```

El objetivo no es crear una clase para cada metodo.

El objetivo es encapsular acciones que necesitan un flujo mas controlado que una llamada directa.

---

## Que problema resuelve

Command ayuda cuando una accion no deberia quedar mezclada dentro de UI, input u otro sistema que solo deberia solicitarla.

Problemas comunes:

- la UI ejecuta logica de gameplay directamente,
- el input modifica estado sin pasar por un sistema claro,
- varias acciones distintas necesitan un flujo comun,
- una accion debe validarse antes de ejecutarse,
- una accion debe registrarse,
- una accion puede ejecutarse desde distintos origenes,
- una accion debe poder repetirse o encolarse,
- una accion importante queda dispersa entre varios scripts.

---

## Cuando conviene usarlo

Conviene considerar Command cuando la accion:

- modifica estado importante,
- representa una decision del jugador o del sistema,
- necesita validacion,
- necesita trazabilidad,
- puede venir de distintos lugares,
- podria entrar en un historial,
- podria ejecutarse de forma diferida,
- forma parte de un flujo de acciones controladas.

Ejemplos posibles:

```txt
colocar una torre
vender una torre
comprar una mejora
usar una habilidad
mover una unidad
confirmar una construccion
cancelar una accion
ejecutar una accion de editor
```

Estos son ejemplos de uso posible.

No significan que toda accion de este tipo deba usar Command automaticamente.

---

## Cuando NO conviene usarlo

No conviene usar Command si:

- la accion es trivial,
- una llamada directa es mas clara,
- no modifica estado importante,
- no necesita validacion especial,
- no necesita registro,
- no necesita flujo comun,
- solo existe un caso aislado,
- crear el comando agrega mas complejidad que valor.

Ejemplo:

```txt
Abrir o cerrar un panel simple de UI
```

Eso puede resolverse con una llamada directa si no hay mas necesidades alrededor.

---

## Como decidir si aplica

Antes de proponer Command, la IA debe responder:

```txt
¿Que accion se quiere encapsular?
¿Quien dispara hoy esa accion?
¿Quien deberia ejecutarla realmente?
¿La accion modifica estado importante?
¿Necesita validacion?
¿Necesita trazabilidad?
¿Puede venir de mas de un origen?
¿Ya existe un flujo de comandos o acciones en el proyecto?
¿Una solucion simple alcanza?
```

Si la respuesta muestra que la accion es simple y local, probablemente no hace falta Command.

Si la respuesta muestra que la accion necesita control, validacion o trazabilidad, Command puede ser una buena opcion.

---

## Estructura conceptual

Una estructura simple puede ser:

```txt
Command
→ representa una accion

Execute()
→ ejecuta la accion
```

Una estructura mas completa puede sumar:

```txt
CanExecute()
→ valida si puede ejecutarse

Undo()
→ revierte la accion si el sistema lo necesita

CommandInvoker
→ recibe y ejecuta comandos

CommandHistory
→ registra comandos ejecutados si hace falta
```

Estas piezas son opcionales.

No todo uso de Command necesita validacion, historial o undo.

La estructura debe responder al problema real.

---

## Ejemplo conceptual breve

Sin Command:

```txt
Boton de comprar mejora
→ revisa monedas
→ aplica mejora
→ descuenta recursos
→ actualiza UI
→ muestra feedback
```

Problema:

```txt
La UI empieza a manejar demasiada logica.
La accion de comprar queda mezclada con la visualizacion.
Si otra parte del juego quiere comprar una mejora, puede duplicar logica.
```

Con Command:

```txt
Boton de comprar mejora
→ solicita BuyUpgradeCommand

BuyUpgradeCommand
→ representa la accion de comprar mejora

Sistema correspondiente
→ valida, ejecuta y comunica resultado
```

La UI deja de ser dueña de la accion.

---

## Ejemplo aplicado a videojuegos

En un juego, una accion importante suele tener varias partes:

```txt
intencion del jugador
validacion
ejecucion
resultado
feedback
```

Command puede servir cuando se quiere encapsular esa accion para que no quede repartida.

Ejemplo:

```txt
PlaceTowerCommand
→ representa la accion de colocar una torre
```

Ese comando podria contener o coordinar la informacion necesaria para ejecutar la accion, segun la arquitectura del proyecto.

Lo importante no es el nombre del comando.

Lo importante es que la accion queda separada de quien la disparo.

---

## Sobre undo, historial y repeticion

Command suele usarse en sistemas con:

- undo,
- redo,
- historial,
- repeticion de acciones,
- acciones encoladas,
- acciones diferidas.

Pero esas son capacidades posibles, no obligaciones.

```txt
Command puede facilitar undo.
Pero Command no significa undo.
```

Si una accion necesita deshacerse, el comando puede guardar el estado necesario para revertirla.

Si no necesita deshacerse, no se agrega esa complejidad.

---

## Como debe usarlo una IA

Cuando una IA trabaje sobre una accion importante, debe evaluar si Command aporta valor real.

Debe evitar este razonamiento:

```txt
Hay una accion
→ creo un Command
```

Debe usar este razonamiento:

```txt
Hay una accion
→ reviso quien la dispara
→ reviso quien deberia ejecutarla
→ reviso si necesita control
→ reviso si ya existe un flujo parecido
→ decido si Command aporta valor
```

Antes de implementar, la IA debe presentar:

```txt
Accion detectada
Problema actual
Sistema existente relacionado
Motivo para usar o no usar Command
Alternativa simple
Riesgos
Validacion esperada
```
---
## Como NO debe usarlo una IA

Una IA no debe usar Command como respuesta automatica cada vez que detecta una accion.

No debe razonar asi:

```txt
Hay una accion
→ entonces necesita Command
```

Ese razonamiento es incorrecto.

Command solo tiene sentido si la accion necesita control, validacion, trazabilidad, desacoplamiento o integracion con un flujo comun.

La IA no debe:

- crear un comando para cada metodo,
- convertir acciones simples en estructuras pesadas,
- crear un sistema de comandos nuevo si ya existe uno compatible,
- usar Command solo porque el nombre suena profesional,
- meter logica de UI dentro del comando,
- usar el comando como excusa para esconder dependencias,
- agregar undo, historial o invoker si el problema no lo necesita,
- modificar arquitectura existente sin justificarlo,
- aplicar Command sin comparar contra una solucion simple.

Ejemplo de mal uso:

```txt
Problema:
Un boton abre un panel de opciones.

Mala decision:
Crear OpenOptionsPanelCommand, CommandInvoker y CommandHistory.

Motivo:
La accion es simple, local y no necesita trazabilidad ni flujo controlado.
```

Ejemplo de mejor criterio:

```txt
Problema:
Un boton confirma una compra que modifica recursos, desbloquea una mejora y debe validar condiciones.

Decision posible:
Analizar si Command aporta valor porque la accion modifica estado importante y necesita validacion.
```

La IA debe recordar:

```txt
Command no reemplaza el criterio.
Command solo se usa cuando encapsular la accion mejora el sistema.
```
---
## Reutilizacion antes que invencion

Si el proyecto ya tiene un flujo para comandos o acciones controladas, la IA debe intentar reutilizarlo.

Ejemplo:

```txt
Ya existe un sistema para acciones de construccion.

Aparece una nueva accion de venta.

Primero se analiza si puede integrarse al flujo existente.
No se crea un sistema paralelo sin justificacion.
```

El objetivo es sostener coherencia dentro del proyecto.

---

## Senales de que Command puede servir

Puede valer la pena analizar Command si:

- una accion importante esta dentro de UI,
- una accion importante esta duplicada en varios lugares,
- el input modifica estado directamente,
- distintas fuentes disparan la misma accion,
- hace falta validar antes de ejecutar,
- hace falta registrar que accion ocurrio,
- se necesita ordenar acciones,
- se quiere separar intencion de ejecucion.

Estas señales no obligan a usar Command.

Solo indican que corresponde analizarlo.

---

## Senales de Command mal aplicado

Command probablemente esta mal aplicado si:

- se crea un comando para cada metodo trivial,
- aparecen muchas clases sin beneficio claro,
- el flujo se vuelve mas dificil de leer,
- no hay validacion, trazabilidad ni desacoplamiento real,
- el comando conoce demasiados detalles de UI,
- se crea un sistema nuevo aunque ya existia uno parecido,
- la accion simple se vuelve artificialmente compleja,
- nadie puede explicar por que el comando existe.

---

## Preguntas antes de implementar

Antes de implementar Command, una IA debe responder:

```txt
¿Que accion se quiere representar?
¿Quien la solicita?
¿Quien deberia ejecutarla?
¿Que estado modifica?
¿Que datos necesita?
¿Hay validaciones?
¿Existe una alternativa mas simple?
¿Existe un flujo similar en el proyecto?
¿Que archivos se tocarian?
¿Como se valida que funciono?
```

Si estas preguntas no pueden responderse, no se implementa todavia.

---

## Formato de propuesta esperado

Antes de ejecutar, la IA deberia proponer:

```txt
Patron:
Command

Accion a encapsular:
...

Problema actual:
...

Por que aplica:
...

Sistema existente relacionado:
...

Alternativa simple:
...

Alcance:
...

Archivos a tocar:
...

Riesgos:
...

Validacion:
...
```

---

## Resultado esperado

Aplicar bien Command deberia permitir:

- separar intencion de ejecucion,
- reducir logica dentro de UI o input,
- controlar acciones importantes,
- reutilizar flujos de accion,
- validar acciones con mas claridad,
- registrar acciones si hace falta,
- facilitar historial o undo solo cuando el proyecto lo necesite,
- reducir duplicacion,
- mejorar mantenibilidad.

---

## Regla final

```txt
Command no existe para convertir metodos en clases.
Existe para encapsular acciones importantes cuando necesitan control, validacion o trazabilidad.
```
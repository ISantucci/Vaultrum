## Proposito

Esta seccion reune patrones de diseno aplicados a videojuegos, software y sistemas desarrollados con criterio arquitectonico.

No existe para usar patrones por costumbre.
No existe para decorar el codigo con nombres tecnicos.
No existe para inventar estructuras innecesarias.
No existe para reemplazar el analisis del problema.

Existe para que una persona o una IA puedan consultar soluciones conocidas, comparar alternativas y decidir si un patron corresponde al problema real del proyecto.

---

## Idea central

Un patron de diseno no es una solucion automatica.

Es una respuesta conocida a un tipo de problema recurrente.

```txt
Problema real
→ contexto del proyecto
→ sistema existente
→ patron candidato
→ costo
→ beneficio
→ decision
```

El objetivo no es aplicar patrones.

El objetivo es resolver problemas de forma clara, mantenible, validable y coherente con el proyecto.

---

## Cuándo usar esta seccion

Consultar esta seccion cuando haga falta:

- resolver un problema tecnico recurrente,
- decidir si corresponde usar un patron,
- revisar si un patron ya existe en el proyecto,
- extender una solucion existente,
- evitar inventar una arquitectura nueva sin necesidad,
- preparar una implementacion,
- auditar una propuesta de IA,
- revisar codigo generado por IA,
- detectar sobrearquitectura,
- justificar una decision tecnica,
- mantener coherencia entre sistemas.

---

## Como debe usar esta seccion una IA

Una IA debe usar esta seccion antes de proponer patrones o ejecutar cambios tecnicos.

Debe usarla para responder:

```txt
¿Que problema real hay?
¿Ya existe una solucion parecida en el proyecto?
¿Hay un patron documentado que aplique?
¿El patron reduce complejidad o la aumenta?
¿El patron mejora mantenibilidad?
¿El patron respeta lo que ya existe?
¿El patrón es entendible y mantenible por el maintainer?
¿Hace falta aplicarlo ahora?
¿Hay una solucion mas simple?
```

La IA no debe decir:

```txt
Usemos este patron porque es buena practica.
```

Debe decir:

```txt
Este problema se parece a este tipo de situacion.
Este patron podria servir por este motivo.
Este es el costo de aplicarlo.
Esta es la alternativa mas simple.
Esta es la validacion necesaria.
```

---

## Regla para agentes en Modo Programador

Cuando un agente trabaje en Modo Programador, debe consultar esta seccion como parte del analisis tecnico.

Antes de ejecutar, debe identificar:

```txt
Problema tecnico
Sistema existente relacionado
Patron ya usado en el proyecto
Patron candidato si corresponde
Riesgo de duplicar solucion
Riesgo de sobrearquitectura
Alternativa mas simple
Decision recomendada
Validacion necesaria
```

El agente no queda autorizado a implementar solo por encontrar un patron aplicable.

Primero debe proponer.

Despues se valida.

Recién despues se ejecuta.

---

## Como recorrer esta seccion

El recorrido recomendado es:

```txt
1. Entender el problema.
2. Revisar si ya existe una solucion en el proyecto.
3. Identificar el tipo de problema.
4. Buscar el patron candidato.
5. Leer la nota del patron correspondiente.
6. Revisar cuándo conviene usarlo.
7. Revisar cuándo NO conviene usarlo.
8. Comparar contra una solucion mas simple.
9. Proponer la decision.
10. Validar antes de ejecutar.
```

No hace falta leer todos los patrones para cada tarea.

Se consulta el patron que pueda resolver el problema real.

---

## Criterio principal

El criterio de esta seccion es:

```txt
Primero problema.
Despues patron.
Nunca al reves.
```

Un patron mal aplicado puede ser peor que una solucion simple.

---

## Reutilizacion antes que invencion

Si el proyecto ya tiene una forma sana de resolver un problema, la IA debe priorizar reutilizar o extender ese sistema antes de crear uno nuevo.

Preguntas obligatorias:

```txt
¿Esto ya existe?
¿Hay un flujo parecido?
¿Hay un patron ya implementado?
¿Hay una convencion del proyecto?
¿Puedo extender sin romper?
¿Estoy creando un sistema paralelo?
```

Ejemplo:

```txt
Si ya existe un flujo para acciones reversibles,
una nueva accion reversible deberia analizar primero si puede integrarse a ese flujo.

No se crea un sistema nuevo de acciones solo porque la accion es nueva.
```

El objetivo es mantener coherencia.

```txt
Mismo tipo de problema
→ mismo criterio de solucion
→ menor deuda
→ mayor mantenibilidad
```

---

## Patrones incluidos

Los patrones concretos viven dentro de:

```txt
02_Patrones de diseno/01_Patrones/
```

Estan agrupados por tipo de problema que ayudan a resolver.

La organizacion no busca clasificar patrones de forma academica.

Busca ayudar a una persona o una IA a encontrar rapidamente que patron puede servir segun el problema tecnico actual.

---

## 01_Acciones y estado

Patrones relacionados con acciones, ejecucion controlada, historial o restauracion de estado.

Consultar esta carpeta cuando el problema este relacionado con:

- acciones importantes,
- validacion de acciones,
- trazabilidad,
- historial,
- undo/redo,
- snapshots,
- restauracion de estado,
- separacion entre intencion y ejecucion.

### [[Command]]

Encapsula una accion como objeto.

Consultar cuando una accion necesita control, validacion, trazabilidad, ejecucion diferida o separacion entre quien la solicita y quien la ejecuta.

### [[Memento]]

Guarda y restaura estados sin exponer todos los detalles internos del objeto.

Consultar cuando se necesita restaurar un estado anterior, crear snapshots, checkpoints o soportar undo en acciones no triviales.

---

## 02_Creacion y datos

Patrones relacionados con creacion de objetos, variantes configurables y datos compartidos.

Consultar esta carpeta cuando el problema este relacionado con:

- creacion de objetos,
- prefabs,
- variantes,
- datos configurables,
- balance,
- hardcodeo,
- datos repetidos,
- separacion entre tipo e instancia.

### [[Factory]]

Centraliza la creacion de objetos.

Consultar cuando la creacion depende de datos, variantes, prefabs, configuraciones o reglas que no deberian estar dispersas.

### [[Type Object]]

Separa los datos compartidos de un tipo de objeto de sus instancias concretas.

Consultar cuando hay variantes configurables que comparten estructura pero cambian datos.

### [[Flyweight]]

Reduce duplicacion de datos compartidos entre muchas instancias.

Consultar cuando muchos objetos repiten la misma informacion base y conviene compartirla.

---

## 03_Comunicacion y flujo

Patrones relacionados con eventos, notificaciones, desacoplamiento y procesamiento ordenado.

Consultar esta carpeta cuando el problema este relacionado con:

- comunicacion entre sistemas,
- eventos,
- reacciones desacopladas,
- orden de procesamiento,
- eventos diferidos,
- efectos encadenados,
- sistemas que no deberian conocerse directamente.

### [[Observer]]

Permite que un sistema notifique cambios sin conocer directamente a todos los interesados.

Consultar cuando varios sistemas necesitan reaccionar a un cambio sin quedar acoplados entre si.

### [[Event Queue]]

Encola eventos para procesarlos de forma ordenada o diferida.

Consultar cuando conviene controlar el orden de eventos, evitar efectos encadenados inmediatos o diferir procesamiento.

---

## 04_Comportamiento

Patrones relacionados con comportamientos variables, estados y formas alternativas de actuar.

Consultar esta carpeta cuando el problema este relacionado con:

- comportamientos por estado,
- comportamientos intercambiables,
- condicionales por tipo,
- IA,
- ataques,
- movimientos,
- reglas variables,
- transiciones claras.

### [[State]]

Separa comportamientos segun el estado actual de un objeto o sistema.

Consultar cuando un objeto cambia claramente su comportamiento segun una condicion, fase o estado.

### [[Strategy]]

Permite intercambiar comportamientos sin modificar el sistema que los usa.

Consultar cuando existen varias formas de resolver una misma accion, decision, calculo o comportamiento.

---

## 05_Acceso y coordinacion

Patrones relacionados con acceso, coordinacion, simplificacion de subsistemas y servicios compartidos.

Consultar esta carpeta cuando el problema este relacionado con:

- acceso a subsistemas,
- coordinacion de varios sistemas,
- entradas simplificadas,
- servicios compartidos,
- instancia unica,
- dependencias globales,
- managers,
- riesgo de acoplamiento.

### [[Facade]]

Expone una entrada simple hacia uno o varios subsistemas.

Consultar cuando un sistema externo necesita interactuar con varios sistemas internos sin conocer todos sus detalles.

### [[Singleton]]

Garantiza una unica instancia accesible de un sistema.

Consultar solo cuando realmente debe existir una instancia global y el acceso compartido esta justificado.

### [[Service Locator]]

Centraliza la busqueda de servicios o dependencias.

Consultar solo en casos donde se necesita acceso controlado a servicios, cuidando no ocultar dependencias importantes.

---

## 06_Optimizacion practica

Patrones relacionados con reutilizacion de objetos y reduccion de costo en runtime.

Consultar esta carpeta cuando el problema este relacionado con:

- objetos temporales,
- instanciacion repetida,
- destruccion repetida,
- rendimiento,
- garbage collector,
- reutilizacion de instancias,
- picos de performance.

### [[Object Pool]]

Reutiliza objetos en lugar de crearlos y destruirlos constantemente.

Consultar cuando hay objetos temporales que aparecen muchas veces durante gameplay.

---

## Guia rapida de decision

Esta guia no decide automaticamente.

Solo orienta la busqueda.

```txt
Acciones reversibles, historial o undo
→ Command / Memento

Creacion de objetos con variantes
→ Factory / Type Object

Datos compartidos por muchas instancias
→ Type Object / Flyweight

Eventos entre sistemas
→ Observer / Event Queue

Objetos temporales repetidos
→ Object Pool

Comportamientos por estado
→ State

Comportamientos intercambiables
→ Strategy

Acceso simple a subsistemas complejos
→ Facade

Instancia unica global
→ Singleton, solo con cuidado

Acceso a servicios
→ Service Locator, solo con justificacion
```

---

## Criterio de uso

Un patron conviene cuando:

- resuelve un problema real,
- reduce fragilidad,
- mejora claridad,
- evita duplicacion,
- respeta la arquitectura existente,
- facilita extension razonable,
- puede validarse,
- el maintainer puede mantenerlo,
- no agrega mas complejidad que valor.

Un patron no conviene cuando:

- el problema es simple,
- solo hay un caso aislado,
- se aplica por costumbre,
- no mejora mantenibilidad,
- obliga a crear demasiadas clases,
- oculta dependencias,
- complica la lectura,
- no se puede justificar.

---

## Antes de proponer un patron

Una IA debe responder estas preguntas antes de recomendar un patron:

```txt
¿Cual es el problema?
¿Que pasaria si no uso ningun patron?
¿Existe una solucion simple suficiente?
¿El proyecto ya usa este patron?
¿Hay que extender algo existente?
¿Que cambia si aplico el patron?
¿Que archivos o sistemas se ven afectados?
¿Que riesgo introduce?
¿Como se valida que funciono?
```

Si no puede responder estas preguntas, no debe proponer el patron todavia.

---

## Antes de ejecutar un patron

Antes de ejecutar una implementacion basada en patrones, la IA debe entregar:

```txt
Patron propuesto
Problema que resuelve
Sistema existente relacionado
Archivos que podria tocar
Archivos que no deberia tocar
Motivo de uso
Alternativa mas simple considerada
Riesgos
Validacion esperada
Decision requerida
```

La ejecucion requiere aprobacion.

---

## Señales de patron mal aplicado

Una solucion probablemente usa mal un patron si:

- el patron aparece antes que el problema,
- se crean clases que no aportan claridad,
- nadie entiende por que existe la estructura,
- se duplican sistemas ya existentes,
- se agregan interfaces sin necesidad,
- se ocultan dependencias importantes,
- se vuelve dificil modificar algo simple,
- se aplica un patron nuevo sin revisar lo que ya existe,
- el cambio no puede explicarse con claridad,
- la IA no puede justificar por que ese patron era mejor que una solucion simple.

---

## Señales de patron faltante

Puede faltar un patron o una estructura mas clara si:

- el mismo tipo de codigo se repite muchas veces,
- cada variante nueva obliga a modificar una clase central,
- una clase acumula acciones diferentes,
- la UI modifica gameplay directamente,
- hay muchos condicionales por tipo,
- se crean y destruyen objetos repetidamente en gameplay,
- varios sistemas se llaman entre si de forma rigida,
- no hay forma clara de deshacer o restaurar una accion,
- el comportamiento cambia por estados pero todo vive en una misma clase.

Detectar estas señales no significa aplicar un patron automaticamente.

Significa iniciar analisis.

---

## Patrones y Unity

En Unity, los patrones deben convivir con el modelo de componentes, prefabs, escenas, ScriptableObjects e Inspector.

Una solucion con patrones debe cuidar que:

- no pelee contra Unity,
- permita configurar valores cuando corresponde,
- no esconda referencias importantes,
- no hardcodee datos de balance,
- respete componentes existentes,
- no convierta managers en clases gigantes,
- no meta logica de gameplay dentro de UI,
- no cree abstracciones que dificulten usar el Inspector.

El patron debe adaptarse al proyecto.

No el proyecto al patron.

---

## Uso correcto dentro de Vaultrum

El uso correcto de esta seccion es:

```txt
Problema real
→ sistema existente
→ patron candidato
→ lectura puntual
→ decision tecnica
→ validacion
```

No es:

```txt
Quiero usar patrones
→ busco donde meterlos
→ agrego abstracciones
→ complico el sistema
```

Los patrones deben ayudar a pensar.

No deben reemplazar el criterio.

---

## Resultado esperado

Usar bien esta seccion deberia permitir:

- elegir soluciones conocidas con criterio,
- evitar inventar arquitectura innecesaria,
- mantener coherencia entre sistemas,
- preparar mejores prompts para IAs,
- auditar propuestas tecnicas,
- detectar patrones mal aplicados,
- detectar patrones faltantes,
- justificar decisiones,
- reducir deuda tecnica,
- mejorar mantenibilidad,
- evitar sobrearquitectura.

---

## Regla final

```txt
Un patron no se usa porque existe.
Se usa porque el problema lo justifica y el proyecto puede sostenerlo.
```
## Definicion

State es un patron que separa el comportamiento de un objeto segun su estado actual.

```txt
Objeto
→ estado actual
→ comportamiento correspondiente
```

Cuando cambia el estado, cambia la forma de actuar.

---

## Idea central

State evita que todos los comportamientos vivan mezclados en una sola clase llena de condicionales.

```txt
Estado A
→ comportamiento A

Estado B
→ comportamiento B
```

El objetivo es ordenar comportamientos claramente diferentes.

---

## Que problema resuelve

State ayuda cuando un objeto cambia mucho su comportamiento segun una condicion o fase.

Problemas comunes:

- muchos `if` por estado,
- comportamientos mezclados,
- transiciones dificiles de entender,
- una clase crece demasiado,
- agregar un estado nuevo rompe estados existentes,
- bugs por estados incompatibles.

---

## Cuando conviene usarlo

Conviene considerar State cuando:

- hay varios estados claros,
- cada estado tiene comportamiento distinto,
- existen transiciones,
- los condicionales crecen mucho,
- se agregaran estados nuevos,
- el flujo necesita orden.

Ejemplos posibles:

```txt
NPC patrullando
NPC persiguiendo
NPC atacando
NPC huyendo
juego pausado
oleada preparando
oleada activa
mision bloqueada, activa o completada
```

---

## Cuando NO conviene usarlo

No conviene usar State si:

- solo hay dos condiciones simples,
- un booleano alcanza,
- los estados no tienen comportamiento propio,
- dividir en clases complica mas,
- el sistema todavia es pequeño,
- no hay transiciones relevantes.

---

## Como decidir si aplica

Antes de proponer State, la IA debe responder:

```txt
¿Que estados existen?
¿Cada estado cambia comportamiento?
¿Hay transiciones claras?
¿Los condicionales estan creciendo?
¿Agregar un estado nuevo seria riesgoso?
¿Existe una maquina de estados en el proyecto?
¿Una solucion simple alcanza?
```

---

## Estructura conceptual

```txt
Contexto
→ mantiene estado actual

State
→ define comportamiento

Estados concretos
→ implementan comportamiento especifico
```

La estructura puede ser simple o mas formal segun el proyecto.

---

## Ejemplo conceptual breve

Sin State:

```txt
Enemy
→ if patrullando
→ if persiguiendo
→ if atacando
→ if huyendo
```

Problema:

```txt
La clase concentra todos los comportamientos.
Cada estado nuevo complica mas el flujo.
```

Con State:

```txt
PatrolState
ChaseState
AttackState
FleeState

Enemy
→ delega comportamiento al estado actual
```

---

## Como debe usarlo una IA

Una IA debe considerar State cuando detecta comportamientos separados por estados.

Debe razonar asi:

```txt
Hay comportamientos por estado
→ identifico estados
→ identifico transiciones
→ reviso si ya existe FSM
→ propongo State si mejora claridad
```

Antes de implementar, debe presentar:

```txt
Estados detectados
Comportamientos por estado
Transiciones
Sistema existente
Alternativa simple
Riesgos
Validacion esperada
```

---

## Como NO debe usarlo una IA

Una IA no debe usar State para cualquier condicion.

No debe:

- crear clases de estado para booleanos simples,
- formalizar una FSM sin necesidad,
- duplicar una maquina de estados existente,
- esconder transiciones,
- crear estados sin comportamiento propio,
- sobrecomplicar una logica chica,
- cambiar arquitectura sin validar.

Ejemplo de mal uso:

```txt
Problema:
Un objeto puede estar activo o inactivo.

Mala decision:
Crear ActiveState e InactiveState.

Motivo:
Un booleano o flag puede alcanzar.
```

---

## Reutilizacion antes que invencion

Si el proyecto ya tiene una maquina de estados, la IA debe integrarse a ese flujo antes de crear uno nuevo.

---

## Senales de que State puede servir

Puede valer la pena analizar State si:

- hay muchos condicionales por estado,
- los estados tienen comportamientos distintos,
- hay transiciones claras,
- agregar estados rompe codigo existente,
- el objeto se volvio dificil de leer,
- hay estados incompatibles mezclados.

---

## Senales de State mal aplicado

State probablemente esta mal aplicado si:

- cada estado hace casi lo mismo,
- hay demasiadas clases sin beneficio,
- las transiciones son dificiles de seguir,
- se creo FSM para una condicion simple,
- se duplican estados existentes,
- la solucion es mas compleja que el problema.

---

## Preguntas antes de implementar

```txt
¿Que estados existen?
¿Que hace cada estado?
¿Como entra y sale de cada estado?
¿Que transiciones hay?
¿Quien decide cambiar de estado?
¿Existe FSM actual?
¿Como se valida?
```

---

## Formato de propuesta esperado

```txt
Patron:
State

Estados:
...

Problema actual:
...

Transiciones:
...

Sistema existente:
...

Alternativa simple:
...

Riesgos:
...

Validacion:
...
```

---

## Resultado esperado

Aplicar bien State deberia permitir:

- separar comportamientos,
- reducir condicionales,
- ordenar transiciones,
- agregar estados con menor riesgo,
- mejorar lectura,
- controlar mejor objetos complejos.

---

## Regla final

```txt
State no existe para reemplazar cualquier condicion.
Existe para ordenar comportamientos claramente distintos segun el estado.
```
## Definicion

Strategy es un patron que permite intercambiar comportamientos sin modificar el sistema que los usa.

```txt
Contexto
→ usa una estrategia

Estrategia
→ define una forma de resolver algo
```

---

## Idea central

Strategy separa el comportamiento variable del objeto que lo necesita.

```txt
Misma accion
→ distintas formas de resolverla
```

El objetivo es cambiar comportamiento sin llenar el codigo de condicionales.

---

## Que problema resuelve

Strategy ayuda cuando hay varias formas de hacer una misma cosa.

Problemas comunes:

- muchos `if` por tipo de comportamiento,
- algoritmos intercambiables mezclados en una clase,
- agregar una variante obliga a modificar codigo central,
- comportamientos duplicados,
- una clase contiene demasiadas formas de resolver algo.

---

## Cuando conviene usarlo

Conviene considerar Strategy cuando:

- existen varias variantes de comportamiento,
- el comportamiento puede cambiar,
- se quiere intercambiar una logica,
- hay algoritmos alternativos,
- se quiere evitar condicionales por tipo,
- se necesita configurar comportamiento.

Ejemplos posibles:

```txt
formas de ataque
calculo de daño
seleccion de objetivo
movimiento
decision de IA
calculo de recompensa
reglas de spawn
```

---

## Cuando NO conviene usarlo

No conviene usar Strategy si:

- solo hay una variante,
- no se espera cambiar comportamiento,
- un metodo simple alcanza,
- crear estrategias agrega ruido,
- las variantes no comparten una intencion comun,
- todavia no se entiende bien el sistema.

---

## Como decidir si aplica

Antes de proponer Strategy, la IA debe responder:

```txt
¿Que comportamiento varia?
¿Cuantas variantes reales hay?
¿Todas resuelven la misma intencion?
¿El contexto puede usar cualquiera de ellas?
¿Hay condicionales por tipo?
¿Existe una estrategia ya usada?
¿Una solucion simple alcanza?
```

---

## Estructura conceptual

```txt
Contexto
→ mantiene referencia a estrategia

Strategy
→ contrato de comportamiento

Estrategias concretas
→ implementan variantes
```

La estructura puede adaptarse al proyecto.

---

## Ejemplo conceptual breve

Sin Strategy:

```txt
EnemyAttack
→ if melee
→ if ranged
→ if area
→ if poison
```

Problema:

```txt
Cada ataque nuevo modifica la clase central.
```

Con Strategy:

```txt
MeleeAttackStrategy
RangedAttackStrategy
AreaAttackStrategy

EnemyAttack
→ usa la estrategia asignada
```

---

## Como debe usarlo una IA

Una IA debe considerar Strategy cuando detecta comportamientos intercambiables.

Debe razonar asi:

```txt
Hay variantes de comportamiento
→ reviso si comparten intencion
→ reviso si se cambian desde datos o codigo
→ reviso si ya existe estrategia
```

Antes de implementar, debe presentar:

```txt
Comportamiento variable
Variantes reales
Contexto que las usa
Sistema existente
Alternativa simple
Riesgos
Validacion esperada
```

---

## Como NO debe usarlo una IA

Una IA no debe usar Strategy para cualquier metodo.

No debe:

- crear estrategias si solo hay una variante,
- separar comportamientos que no son intercambiables,
- crear muchas clases prematuras,
- duplicar un sistema existente,
- ocultar logica simple,
- usar Strategy para evitar entender el problema.

Ejemplo de mal uso:

```txt
Problema:
Un enemigo solo tiene un tipo de ataque.

Mala decision:
Crear AttackStrategy.

Motivo:
No hay variantes reales todavia.
```

---

## Reutilizacion antes que invencion

Si el proyecto ya tiene un sistema de comportamientos intercambiables, la IA debe integrarse ahi antes de crear otro.

---

## Senales de que Strategy puede servir

Puede valer la pena analizar Strategy si:

- hay muchas variantes de una misma accion,
- se usan condicionales por tipo,
- se quiere configurar comportamiento,
- cambiar una variante toca clase central,
- hay algoritmos alternativos,
- el comportamiento puede cambiar en runtime o por datos.

---

## Senales de Strategy mal aplicada

Strategy probablemente esta mal aplicada si:

- hay una sola variante,
- las estrategias no comparten intencion,
- se crean clases sin beneficio,
- el flujo se vuelve menos claro,
- se usa para evitar un metodo simple,
- se duplica logica.

---

## Preguntas antes de implementar

```txt
¿Que comportamiento varia?
¿Que variantes existen?
¿Todas resuelven lo mismo?
¿Quien elige la estrategia?
¿Puede configurarse?
¿Existe sistema similar?
¿Como se valida?
```

---

## Formato de propuesta esperado

```txt
Patron:
Strategy

Comportamiento variable:
...

Variantes:
...

Contexto:
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

Aplicar bien Strategy deberia permitir:

- intercambiar comportamientos,
- reducir condicionales,
- agregar variantes con menos riesgo,
- configurar logica,
- separar algoritmos,
- mejorar mantenibilidad.

---

## Regla final

```txt
Strategy no existe para separar cualquier metodo.
Existe para intercambiar comportamientos reales que comparten una misma intencion.
```
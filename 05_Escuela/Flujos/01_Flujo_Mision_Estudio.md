## Propósito

Transformar un gap del Core (o un pedido del owner) en una **misión de estudio acotada**: pregunta concreta, presupuesto y barra de calidad. Es la puerta del área: sin misión, no se estudia.

---

## Entrada del flujo

- Un gap detectado en el Core (ej: faltan Fundamentos de Experiencia — Ley #1), o un pedido de estudio del owner.

Si no hay gap concreto, el flujo no avanza: se pide precisión al owner o se cierra.

---

## Transformación que realiza

- Parte del Core: ubica el gap y consulta si ya hay algo (principio 1).
- Traduce el gap en una pregunta de estudio verificable.
- Hace la dedup inicial: ¿es alta nueva o actualización de una nota existente?
- Fija presupuesto de tokens y barra de calidad.
- Corre el gate AiCare de arranque (presupuesto validado, contexto base medido).

---

## Salida esperada / formato

```txt
## Misión (gap estudiado)
## Pregunta de estudio (y cuándo se considera respondida)
## Dedup contra el Core (nuevo / actualiza a: <nota del Core>)
## Presupuesto de tokens
## Barra de calidad (criterios de aceptación)
## Estado AiCare (ANTES: presupuesto validado, contexto base medido)
```

---

## Criterios de aceptación

- El gap es concreto y la pregunta es verificable.
- Se hizo dedup contra el Core.
- Hay presupuesto y barra definidos.
- AiCare de arranque corrido.

---

## Condiciones para avanzar

Avanza al `02_Flujo_Investigacion` cuando la misión supera el gate.
No avanza si falta gap, presupuesto o barra.

---

## Qué debe evitar

No abre misiones sin gap ("estudiar sobre X" a secas). No fija "tokens libres hasta gastarse". No arranca sin AiCare.

---

## Resultado final

Una misión acotada y aprobable que le permite al Investigador buscar sin desbordarse.

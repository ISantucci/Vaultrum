## Propósito

Verificar la barra de calidad del candidato `EST` y hacer el handoff al Área de Conocimiento. Es el último gate del área: la Escuela **no mergea al Core**, entrega candidatos.

---

## Entrada del flujo

- Un candidato `EST` del [[03_Flujo_Destilacion]].

---

## Transformación que realiza

- Chequea la barra de calidad de la misión (reutilizable, claro, citado, no verbatim).
- Confirma la dedup contra el Core (nuevo o actualización, nunca duplicado).
- Corre el gate AiCare de handoff (que el candidato no infle el contexto).
- Entrega el `EST` a Conocimiento, o lo devuelve al Destilador / lo descarta con motivo.

---

## Gate de handoff

```txt
[ ] Reutilizable, claro, citado, no verbatim
[ ] No duplica el Core (o es actualización marcada)
[ ] AiCare handoff: no infla el contexto ni recarga lo existente
```

---

## Salida esperada / formato

```txt
## Candidato EST evaluado
## Barra de calidad: cumple / falta <qué>
## Dedup: nuevo / actualiza a: <nota del Core>
## Estado AiCare (handoff: no infla, no duplica)
## Decisión: handoff a Conocimiento / vuelve al Destilador / descartado (motivo)
```

---

## Criterios de aceptación

- El `EST` cumple la barra completa.
- La dedup está resuelta.
- AiCare de handoff corrido.

---

## Handoff

El `EST` que pasa se entrega al **Área de Conocimiento**, que lo trata como candidato de commit: dedup + ubicación + diff → gate de aprobación del owner → merge a `main`. La Escuela no toca `main`.

```
Escuela (EST validado) → Conocimiento (commit) → Owner (merge a main)
```

---

## Qué debe evitar

No mergea al Core ni propone a `main`. No deja pasar `EST` sin cita, dedup o AiCare. No acepta "por las dudas".

---

## Resultado final

Un candidato `EST` curado entra al pipeline de Conocimiento; lo que no cumple vuelve o se descarta sin dejar rastro en el Core.

## Propósito

El Validador de Estudio verifica la barra de calidad del candidato `EST` antes del handoff. Es el último gate del área: solo lo que pasa llega al Área de Conocimiento.

No investiga ni destila, y **no mergea al Core**. Existe para que la Escuela no intoxique el Core: entrega candidatos reutilizables, citados y sin duplicar, o los devuelve/descarta.

---

## Responsabilidad principal

El Validador de Estudio debe responder:

¿Este `EST` cumple la barra y no ensucia el Core? ¿Se entrega, vuelve o se descarta?

Trabaja sobre cuatro responsabilidades:

- chequear la barra de calidad de la misión (reutilizable, claro, citado, no verbatim),
- confirmar la dedup contra el Core (nuevo o actualización, nunca duplicado),
- correr el gate AiCare de handoff (que el candidato no infle el contexto),
- entregar el `EST` al Área de Conocimiento, o devolverlo/descartarlo con motivo.

---

## Cuándo se activa

Después del Destilador, sobre cada candidato `EST` antes de salir del área.

Ningún `EST` sale sin pasar por acá.

---

## Barra de handoff (qué habilita la entrega)

```txt
[ ] Reutilizable: sirve para futuros pedidos, no solo para este caso
[ ] Claro: se entiende como criterio/baseline por humanos e IAs (principio 8)
[ ] Citado: cada fundamento tiene su fuente
[ ] No verbatim: concepto destilado, no texto con copyright
[ ] No duplica el Core (o está marcado como actualización clara)
[ ] AiCare ANTES DEL HANDOFF: no infla el contexto ni recarga lo que ya existe
```

Si no cumple, vuelve al Destilador (o se descarta). Descartar es una salida válida.

---

## Qué debe hacer

Revisar el `EST` contra la barra de calidad de la misión.
Confirmar la dedup: si toca algo del Core, marcarlo como actualización, no como alta.
Correr el gate AiCare de handoff.
Si pasa: entregar el `EST` al Área de Conocimiento. Si no: devolver con motivo o descartar.

---

## Qué debe evitar

No investiga ni destila (eso es Investigador y Destilador).
No mergea al Core ni propone a `main`: eso es Conocimiento + owner.
No deja pasar `EST` sin cita, sin dedup o sin AiCare.
No acepta "por las dudas": ante la duda, vuelve o se descarta.

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

## Flujos a implementar

- [[04_Flujo_Validacion_Estudio]]

El detalle operativo vive en el documento del flujo.

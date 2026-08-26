## Propósito

El Destilador convierte el material bruto en **principios y fundamentos claros y reutilizables + citas**. Es el que transforma "un juego hace X" en "el baseline de este tipo de experiencia es X".

No busca fuentes ni valida el handoff. Existe para producir el candidato `EST`: útil para humanos e IAs (principio 8), sin texto verbatim con copyright.

---

## Responsabilidad principal

El Destilador debe responder:

¿Cuál es el fundamento reutilizable detrás de este material, y cómo lo usa la IA como baseline?

Trabaja sobre cuatro responsabilidades:

- extraer el principio/fundamento del material bruto (el loop, el feedback, el juice, las table-stakes),
- escribirlo claro, reutilizable e indexable, no como resumen de una fuente,
- conservar las citas de origen (concepto destilado + fuente, nunca verbatim),
- marcar aplicación y límites: cuándo la IA lo trae por default y cuándo NO aplica.

---

## Cuándo se activa

Después del Investigador, sobre el material bruto ya podado por AiCare (sin duplicados ni ruido).

No destila material sin citar ni fuera de la misión.

---

## Qué debe hacer

Leer el material bruto y separar el principio reutilizable del caso puntual.
Escribir el fundamento como criterio: qué es, cuándo se aplica como baseline, cuándo no.
Volcarlo al **libro que corresponde**: un libro de `Fundamentos` si es transversal, o uno de `Juegos` (con género/tipo) si es específico de un juego. Actualiza el libro existente antes de crear uno nuevo.
Mantener la cita de cada fuente que sostiene el principio.
Dejar el candidato `EST` con la estructura del área, listo para validar.

---

## Qué debe evitar

No busca ni junta fuentes (eso es Investigador).
No valida ni hace el handoff a Conocimiento (eso es Validador de Estudio).
No copia texto verbatim con copyright: destila el concepto y cita la fuente.
No infla el Core: si un fundamento no es claro y reutilizable, no lo escribe.

---

## Salida esperada / formato (`EST`)

```txt
## Misión (gap estudiado) + presupuesto usado
## Fundamento / concepto destilado (reutilizable, claro)
## Aplicación (cuándo y cómo lo usa la IA como baseline)
## Límites (cuándo NO aplica)
## Fuentes (citas)
## Dedup: ¿actualiza algo del Core o es nuevo?
## Estado AiCare (poda del material bruto aplicada antes de destilar)
```

---

## Flujos a implementar

- `03_Flujo_Destilacion`

El detalle operativo vive en el documento del flujo.

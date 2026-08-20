## Propósito

Esta carpeta contiene las salidas formales de la Escuela Vaultrum.

Una salida aparece cuando una misión de estudio fue acotada, investigada, destilada y validada. El resultado queda registrado como un candidato de estudio (`EST`) listo para el handoff al Área de Conocimiento.

La Escuela **no mergea al Core**: sus salidas son candidatos, no cambios a `main`.

---

## Índice interno

- [[00_Indice_est]]

---

## Regla de salida

Cada `EST` cuelga de una misión de estudio (gap + presupuesto + barra). La numeración es propia del área y correlativa:

```
EST-001   (misión: Fundamentos de Experiencia)
EST-002   (siguiente misión)
```

Un `EST` no es un cambio al Core: es el insumo que el Área de Conocimiento trata como candidato de commit.

```
EST (Escuela) → commit (Conocimiento) → merge a main (Owner)
```

---

## Regla operativa

Antes de crear una salida, revisar el índice para confirmar el número y linkear a la misión. Ningún `EST` se registra sin cita y sin haber pasado por AiCare (arranque y handoff). Cada `EST` debe ser trazable a su misión.

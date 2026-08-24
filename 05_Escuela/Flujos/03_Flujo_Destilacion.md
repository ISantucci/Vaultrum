## Propósito

Convertir el material bruto en un candidato `EST`: **fundamento reutilizable + citas**, escrito claro para humanos e IAs, sin texto verbatim con copyright.

---

## Entrada del flujo

- Material bruto citado del [[02_Flujo_Investigacion]].

Antes de destilar, AiCare poda el material (duplicados/ruido) para no destilar basura.

---

## Transformación que realiza

- Separa el principio reutilizable del caso puntual (el loop, el feedback, el juice, las table-stakes).
- Lo escribe como criterio/baseline, no como resumen de una fuente.
- Conserva la cita de cada fundamento (concepto destilado + fuente).
- Marca aplicación (cuándo la IA lo trae por default) y límites (cuándo NO aplica).

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

## Criterios de aceptación

- El fundamento es reutilizable y claro, no un resumen de fuente.
- Cada principio está citado.
- No hay texto verbatim con copyright.
- Aplicación y límites explícitos.

---

## Condiciones para avanzar

Avanza al `04_Flujo_Validacion_Estudio` cuando el `EST` está escrito y citado.
No avanza si el fundamento es vago o falta cita.

---

## Qué debe evitar

No busca ni junta fuentes. No valida ni hace handoff. No copia verbatim. No infla el Core con fundamentos vagos.

---

## Resultado final

Un candidato `EST` claro, citado y reutilizable, listo para validarse antes del handoff.

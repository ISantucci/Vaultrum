## Propósito

Completar el `GDS-XXX.n` con su capa numérica: parámetros configurables, valores iniciales, curvas de dificultad/progresión/economía y cómo se tunea y testea.

---

## Entrada del flujo

- `GDS-XXX.n` con reglas, estados y feedback ya definidos (`02_Flujo_Diseno_Sistema`).

Puede omitirse si el sistema no tiene valores que impacten la experiencia.

---

## Transformación que realiza

- Lista cada parámetro configurable con valor inicial y rango sugerido.
- Define curvas cuando el sistema escala (dificultad, costos, recompensas, velocidad).
- Indica el mecanismo de configuración esperado (ScriptableObject, tabla de datos, Inspector) sin imponer implementación.
- Define cómo se valida el balance (qué medir, qué rango es aceptable).

---

## Salida esperada / formato

Completa el `GDS-XXX.n` con:

```txt
## Parámetros configurables (valor inicial + rango sugerido)
## Curvas (dificultad / progresión / economía)
## Mecanismo de configuración esperado
## Cómo se valida el balance (qué medir)
```

---

## Criterios de aceptación

- Cada valor de balance tiene un valor inicial razonable.
- Las curvas necesarias están definidas.
- Nada queda hardcodeado: todo es configurable.
- Está claro cómo se mide que el balance funciona.

---

## Condiciones para avanzar

Avanza al `04_Flujo_Validacion_Diseno` cuando la capa numérica está cerrada.
Si al balancear aparece que las reglas no cierran, rebota al Diseñador de Sistema.

---

## Qué debe evitar

No cambia las reglas base. No hardcodea. No inventa parámetros que no afectan la experiencia. No define arquitectura de código.

---

## Resultado final

Un `GDS-XXX.n` con reglas + balance, listo para validación.

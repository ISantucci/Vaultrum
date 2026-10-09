## Propósito

Transformar el encuadre de gameplay en un sistema jugable concreto: reglas, entradas, salidas/feedback y estados. Abre el `GDS-XXX.n`.

---

## Entrada del flujo

- Encuadre del `01_Flujo_Analisis_Gameplay` (objetivo + experiencia esperada).

Si el encuadre no trae experiencia clara, vuelve al Analista.

---

## Transformación que realiza

- Define las reglas del sistema.
- Define entradas (jugador/sistema) y salidas/feedback.
- Define estados y transiciones.
- Señala qué valores necesitarán balance (sin fijar números).
- Verifica numeración: `GDS-XXX.n` hereda del `RQ-XXX.n`. Revisar `00_Indice_gds`.

---

## Salida esperada / formato

```txt
## GDS-XXX.n — Título
## Requerimiento asociado (RQ-XXX.n)
## Objetivo del sistema
## Reglas
## Entradas (jugador / sistema)
## Salidas y feedback
## Estados / variaciones
## Valores que necesitarán balance
## Integraciones esperadas
## Experiencia esperada
```

---

## Criterios de aceptación

- Reglas claras, sin huecos ni contradicciones.
- Entradas, salidas y feedback definidos.
- Estados y transiciones claros.
- El sistema aporta a la experiencia (sin complejidad de más).
- `GDS-XXX.n` asignado y linkeado a su `RQ`.

---

## Condiciones para avanzar

Avanza al `03_Flujo_Balance` cuando las reglas están cerradas.
Si el sistema tiene números relevantes, pasa por Balance; si no, puede saltar directo a `04_Flujo_Validacion_Diseno`.
Si el encuadre era insuficiente, rebota al Analista.

---

## Qué debe evitar

No programa. No fija valores de balance. No sobrecomplejiza. No define reglas imposibles de validar.

---

## Resultado final

Un `GDS-XXX.n` abierto con las reglas del sistema, listo para su capa de balance.

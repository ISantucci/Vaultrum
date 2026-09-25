## Propósito

El Flujo de Objetivo convierte un pedido de medición en **un KPI primario definido entero**, con sus diagnósticas y sus guardrails, antes de que exista un solo evento.

Existe porque el orden importa: si los eventos se diseñan antes que la pregunta, la pregunta termina siendo la que los eventos permiten contestar.

---

## Entrada del flujo

- un `RQ-XXX.n` que declara **MET aplica**, con el objetivo escrito;
- el `GDS-XXX.n` cerrado, con su sección *Experiencia esperada*;
- la **fase** y el **modelo de negocio**, del cuaderno del proyecto o del `TL`.

Si falta la fase o el objetivo, el flujo no arranca: devuelve a Producción. Si falta el comportamiento esperado, devuelve a Game Design.

---

## Transformación que realiza

- Reconstruye el objetivo real detrás del pedido y lo escribe en una o dos frases.
- Escribe el comportamiento esperado como algo que el jugador **hace**.
- Ubica la etapa del journey que afecta: entrar, volver, interactuar, pagar, recomendar.
- Elige **un** KPI primario compatible con la fase y lo define entero: nombre, fórmula, población, ventana, fuente, baseline —o su ausencia declarada— y objetivo numérico si existe.
- Agrega las diagnósticas que explicarían un movimiento del KPI.
- Agrega al menos un guardrail: lo que no se puede romper para moverlo.
- Escribe qué decisión habilita cada resultado posible.

El criterio de fondo vive en el Core, en `Objetivo antes que metrica` y `Fases del producto y que medir`: este flujo lo aplica, no lo repite.

---

## Salida esperada / formato

```txt
## Fase y modelo            fase: <una de las ocho> · modelo: <o "no aplica — por qué">
## Objetivo
## Comportamiento esperado
## KPI primario             nombre · formula · poblacion · ventana · fuente · baseline · objetivo
## Métricas diagnósticas
## Guardrails
## Decisión que habilita
```

Queda como la primera mitad del `MET-XXX.n`. El KPI queda **congelado** desde acá.

---

## Criterios de aceptación

El flujo puede darse por cerrado cuando:

- el objetivo y el comportamiento esperado están escritos y son distintos entre sí,
- hay exactamente un KPI primario, con sus seis claves,
- ninguna métrica es prematura para la fase declarada,
- hay al menos un guardrail,
- cada resultado posible del KPI cambia alguna decisión.

---

## Condiciones para avanzar

Avanza cuando el `02_Disenador_Medicion` puede diseñar eventos sin volver a preguntar qué se quiere saber.

Queda **Pausado** cuando el objetivo no se puede escribir sin una decisión del owner o de Producción, o cuando la fase no está declarada.

No debe avanzar si:

- el KPI se eligió antes que el objetivo,
- la población del KPI no está escrita,
- el plan mide algo que ningún resultado haría cambiar.

---

## Qué debe evitar este flujo

No convierte "subir una métrica" en objetivo sin preguntar qué resultado representa. No elige por popularidad del género. No suma KPIs primarios para no decidir.

---

## Resultado final

Una pregunta cerrada, con su número, su denominador y lo que no se puede romper, escrita antes de que el dato exista.

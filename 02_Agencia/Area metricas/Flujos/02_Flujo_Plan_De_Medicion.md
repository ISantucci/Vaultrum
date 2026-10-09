## Propósito

El Flujo de Plan de Medición convierte el KPI congelado en **el tracking plan mínimo** que lo mide, los criterios con que se verifica cada evento y la línea de privacidad. Cierra la mitad A del área: el `MET-XXX.n`.

Existe para que Programación reciba un contrato y no una intención, y para que Control de Calidad tenga algo contra qué verificar la telemetría antes de que alguien le crea.

---

## Entrada del flujo

- la primera mitad del `MET-XXX.n`, cerrada por el `01_Flujo_Objetivo`;
- el presupuesto de eventos de la fase: en Pre-Production, Production y Testing, el tope de `13_Playtesting_y_validacion`;
- lo que el proyecto ya registra, si registra algo: no se duplica un evento que existe.

---

## Transformación que realiza

- Por cada métrica declarada —KPI, diagnósticas, guardrails— lista qué cambio de estado del juego la produce.
- Escribe un evento por pregunta, en `snake_case`, sin valores dinámicos en el nombre, con los parámetros que la pregunta necesita y ninguno más.
- Declara el contexto mínimo: versión, entorno, sesión, identificador pseudónimo.
- Cuenta los eventos contra el presupuesto de la fase. Si se pasa, recorta o escribe `tope: N — <razón>`.
- Escribe la QA de eventos para Control de Calidad: dispara, una vez, en el momento correcto, con sus parámetros y tipos, en el entorno correcto, con el signo correcto.
- Escribe la línea de privacidad: qué no se recolecta y dónde queda el dato.
- Declara lo que deliberadamente no se mide.

---

## Salida esperada / formato

```txt
## Tracking plan
   | Evento | Disparo | Parametros | Pregunta | KPI |
## QA de eventos
## Privacidad
## Lo que no se mide
## Estado
```

Se suma a la primera mitad y completa el `MET-XXX.n`, que se mide con:

```txt
python3 "02_Agencia/Area metricas/Herramientas/metricas.py" plan <MET-XXX.n.md> --verificar
```

---

## Criterios de aceptación

- cada evento tiene pregunta y alimenta una métrica declarada,
- ningún nombre lleva fecha, id o número de nivel adentro,
- ningún parámetro es un dato personal,
- el total de eventos respeta el presupuesto de la fase, o su excepción está escrita con razón,
- la QA de eventos cubre cada evento,
- `metricas.py plan` devuelve EN LEY.

---

## Condiciones para avanzar

Avanza cuando Programación puede implementar los eventos del `MET-XXX.n` junto con el `SOL` del hilo, sin inventar ninguno.

Queda **Pausado** cuando el juego no puede registrar lo que el KPI necesita sin una decisión técnica que no está tomada: se rebota al `01_Analista_Objetivo` con el motivo, no se cambia el KPI desde acá.

No debe avanzar si:

- hay eventos "por las dudas",
- el plan pasa el tope de la fase sin razón escrita,
- la QA de eventos quedó para después.

---

## Qué debe evitar este flujo

No implementa. No verifica en la build. No elige otro KPI porque el primero era difícil de instrumentar.

---

## Resultado final

Un contrato de telemetría corto, que Programación implementa, Control de Calidad verifica y el Lector va a poder leer.

## Propósito

El Área de Programación de Vaultrum transforma requerimientos ya definidos en soluciones técnicas construidas con criterio Vaultrum: SOLID, apoyadas en el conocimiento del Core, sin hardcodeo, expansibles y mantenibles.

Su función es tomar el "qué" que produce Producción (y el "cómo debe jugarse" que produce Game Design) y convertirlo en el "cómo se implementa", sin romper lo existente y sin sobrearquitecturar.

El área no existe para escribir código rápido. Existe para llegar a la mejor solución posible mediante iteración entre sus sub-agentes, dejando registro formal de la solución y de la ejecución.

---

## Entrada del área

El Área de Programación consume:

- un `RQ-XXX.n` (requerimiento) del Área de Producción, y
- si existe, su `GDS-XXX.n` (game design spec) del Área de Game Design.

Si no hay un RQ claro, el área no arranca: deriva a Producción. Si el RQ es jugable y no tiene GDS, deriva a Game Design o lo marca como pendiente.

---

## Sub-agentes del área

### [[01_Analista_Tecnico]]

Consume el RQ (+ GDS), lee el proyecto real y consulta el Core. Produce un diagnóstico técnico: qué existe, qué se reutiliza, qué conocimiento de Vaultrum aplica, qué riesgos hay. No propone la solución final ni escribe código.

### [[02_Disenador_Solucion]]

Convierte el diagnóstico en una **solución técnica validada** (`SOL-XXX.n`): arquitectura, separación de responsabilidades, patrones del Core, parámetros configurables, alternativas descartadas. Es el gate: la solución se aprueba antes de ejecutar. No escribe la implementación final.

### [[03_Ejecutor_Tecnico]]

Ejecuta solo el alcance aprobado de la SOL y produce la implementación real + reporte (`EJ-XXX.n`). Respeta convenciones, no toca fuera de alcance, no hardcodea. No rediseña la solución.

### [[04_Revisor_Tecnico]]

Valida la ejecución contra los criterios de aceptación (usa Core, SOLID, sin hardcodeo, alcance respetado, expansible). Si no cumple, **rebota** al sub-agente que corresponda. Es quien cierra —o reabre— el loop. No ejecuta ni rediseña; dictamina.

---

## Cómo trabaja el área — el loop de iteración

El área no es una línea recta: es un **loop** que no cierra hasta que la solución es "lo más vaultrumita posible".

```
RQ (+ GDS)
  ↓
Analista Técnico      → diagnóstico
  ↓
Diseñador de Solución → SOL-XXX.n        ⟵ gate de aprobación
  ↓
Ejecutor Técnico      → EJ-XXX.n
  ↓
Revisor Técnico       → ¿cumple criterios?
        ├── Sí  → cierra la revisión y pasa el hilo a Control de Calidad
        └── No  → rebota:
                  · falta criterio técnico   → Analista
                  · solución mal planteada    → Diseñador
                  · implementación desviada   → Ejecutor
```

El loop se repite hasta que el Revisor da OK contra los criterios de aceptación. Ahí cierra la **revisión técnica** del hilo `.n`, y el hilo pasa al **Área de Control de Calidad**, que corre su gate (`QA-XXX.n`). Cuando todos los hilos están verificados, la entrega vuelve al Área de Producción, que la cierra con su `VE-XXX`.

---

## Salida del área

El área produce, por cada requerimiento:

- una **solución técnica** registrada como `SOL-XXX.n`,
- una **ejecución/reporte** registrada como `EJ-XXX.n`.

Ambas se registran en la carpeta `00_Salidas_programacion` del área, con sus índices, respetando la numeración heredada del RQ.

Queda registrada en `Salidas/`:

- [[00_Salidas_programacion|Índice de salidas del área]]

---

## Regla operativa

Primero entender el requerimiento y el proyecto real.
Después consultar el Core.
Después proponer solución y validarla (gate).
Después ejecutar solo lo aprobado.
Después revisar contra criterios y rebotar si hace falta.

No se ejecuta código hasta que la solución fue propuesta y aprobada.

---

## Límites del área

El Área de Programación no debe absorber responsabilidades de otras áreas.

- No define alcance ni prioridad (eso es Producción).
- No se verifica a sí misma: el Revisor Técnico valida **cómo está construido** el hilo; que lo construido se sostenga lo decide el **Área de Control de Calidad**, con su propio gate y su evidencia.
- No define reglas de gameplay ni feedback (eso es Game Design).
- No documenta conocimiento permanente del vault (eso es Conocimiento).
- No inventa requerimientos: si falta uno, deriva a Producción.

Puede detectar que un aprendizaje merece volver al Core, pero no lo formaliza: lo marca y lo deriva a Conocimiento.

---

## Encadenado con otras áreas

Recibe de: **Producción** (`RQ`), **Game Design** (`GDS`) y, si existen, **Level Design** (`LDS`) y **UI/UX** (`UXS`).
Entrega a: **Control de Calidad** (el `EJ` en OK y la build identificable, para el gate), **Producción** (el timeline verificado vuelve para la validación de entrega) y **Conocimiento** (aprendizajes reutilizables detectados durante la ejecución).

Control de Calidad le devuelve defectos con evidencia y, cuando corresponde, pedidos de **testabilidad**: instrumentación, semillas fijas, atajos de estado o logs que bajan el costo de todas las verificaciones que vienen después.

La numeración `.n` se mantiene entre `RQ / GDS / LDS / UXS / SOL / EJ / QA` para que todo el hilo de trabajo sea rastreable de punta a punta. El `QA` de entrega y el `VE` de cierre cuelgan del `TL`, sin `.n`.

## Flujos del área

Cada flujo es un paso del loop del área. Se entra por el flujo que corresponde al estado del trabajo, no por todos.

### [[01_Flujo_Analisis_Tecnico|Flujo Analisis Tecnico]]

### [[02_Flujo_Diseno_Solucion|Flujo Diseno Solucion]]

### [[03_Flujo_Ejecucion|Flujo Ejecucion]]

### [[04_Flujo_Revision|Flujo Revision]]

---

## Skill del área

El área corre como la skill `vaultrum-programador` (fuente versionada en `02_Agencia/Area programacion/Skills/vaultrum-programador/SKILL.md`).

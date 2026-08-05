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
        ├── Sí  → cierra el hilo
        └── No  → rebota:
                  · falta criterio técnico   → Analista
                  · solución mal planteada    → Diseñador
                  · implementación desviada   → Ejecutor
```

El loop se repite hasta que el Revisor da OK contra los criterios de aceptación. Recién ahí el hilo (`.n`) se considera cerrado.

---

## Salida del área

El área produce, por cada requerimiento:

- una **solución técnica** registrada como `SOL-XXX.n`,
- una **ejecución/reporte** registrada como `EJ-XXX.n`.

Ambas se registran en la carpeta [[00_Indice_salidas]] del área, con sus índices, respetando la numeración heredada del RQ.

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
- No define reglas de gameplay ni feedback (eso es Game Design).
- No documenta conocimiento permanente del vault (eso es Conocimiento).
- No inventa requerimientos: si falta uno, deriva a Producción.

Puede detectar que un aprendizaje merece volver al Core, pero no lo formaliza: lo marca y lo deriva a Conocimiento.

---

## Encadenado con otras áreas

Recibe de: **Producción** (`RQ`) y **Game Design** (`GDS`).
Entrega a: **Conocimiento** (aprendizajes reutilizables detectados durante la ejecución).

La numeración `.n` se mantiene entre `RQ / GDS / SOL / EJ` para que todo el hilo de trabajo sea rastreable de punta a punta.

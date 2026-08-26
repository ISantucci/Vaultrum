## Índice de Validaciones de Entrega (VE)

Registro de los cierres de entrega del Área de Producción.

Cada `VE-XXX` valida **la entrega de un timeline** (`TL-XXX`) contra la intención original, el diseño acordado y la definición de terminado. La produce el `04_Validador_Entrega` corriendo el `04_Flujo_Validacion_Entrega`.

---

## Registro

Los artefactos de un proyecto **no se registran acá**. Viven en la carpeta del proyecto, en `06_Proyectos/<Proyecto>/01_Produccion/`, y se listan en el cuaderno de ese proyecto.

Este índice es el **contrato de salida** del área: qué produce, qué forma tiene, cómo se numera y cuándo está cerrado. No es un archivo.

> Entrada a los proyectos: `00_Proyectos`. Por qué dejaron de vivir acá: `TL-008_La_Agencia_Es_La_Empresa`.

## Regla

- Un `VE` cuelga de un **`TL-XXX`**, no de un `RQ`. Se valida lo que el jugador recibe, y eso es la iteración completa, no un requerimiento suelto.
- Se abre cuando los hilos `.n` del timeline tienen su `EJ` con revisión técnica en OK.
- Estado del `VE`: **Cerrado** / **Ajustar** / **Pausado**. Acá el estado del paso y el del artefacto coinciden, porque el `VE` es un dictamen: no tiene ciclo de vida propio.
- **Todo `VE` declara su modo de cierre**: `Checklist` o `Veredicto`. La diferencia está más abajo.
- *Ajustar* debe indicar a dónde rebota —un área, o un sub-agente de Producción— y con qué hallazgo concreto.
- *Pausado* debe declarar qué falta para poder validar (principio 9).
- Un `TL` no se considera entregado sin su `VE` en estado **Cerrado**.
- Si la validación detecta un aprendizaje reutilizable, se marca y se deriva al Área de Conocimiento (no se formaliza acá).

---

## Los dos modos de cerrar un `VE`

Un `VE` llega a **Cerrado** por uno de dos caminos. Los dos son válidos y el `VE` declara cuál usó.

| Modo | Qué es | Qué dice | Qué NO dice |
|------|--------|----------|-------------|
| **Checklist** | se recorren los ítems de la definición de terminado, uno por uno, sobre el entregable corriendo | cuál de los ítems falla | si el conjunto se sostiene como experiencia |
| **Veredicto** | el owner usa el entregable y emite un juicio global | si el conjunto funciona | cuál de los ítems falla |

Reglas del modo veredicto:

- Solo lo emite **el owner**, sobre el entregable **corriendo**. Nunca desde el código, nunca otra persona o agente.
- El `VE` registra el veredicto textual y **declara la deuda**: qué ítems no se recorrieron.
- Si en la iteración siguiente aparece un problema que la checklist habría atrapado, el aprendizaje es del sistema, no del entregable.

Los dos son verificaciones parciales y los dos declaran su alcance. Criterio del Core: `Verificacion parcial declarada`.

**Por qué se formaliza:** `VE-003` cerró por veredicto sin que ese modo existiera escrito, lo que dejó la duda de si era un cierre legítimo o una excepción. Es legítimo — y ahora tiene nombre, condiciones y una deuda que se declara en vez de omitirse.

---

## Por qué por timeline y no por requerimiento

La definición de terminado es del **entregable**, no de la pieza: "hay condición de victoria", "se puede volver a jugar sin reiniciar" o "el objetivo se entiende sin explicación" no son verificables contra un `RQ` de paletas. Un `VE` por `.n` obligaría a marcar N/A la mayor parte del checklist en cada hilo.

La revisión por hilo ya existe y es del Revisor Técnico del Área de Programación: valida **cómo está construido** ese `.n`. El `VE` valida **qué se entregó** como conjunto. Son dos cortes distintos, no dos capas del mismo corte.

# Blueprint — Refactor de la Agencia

Documento base del refactor de la Agencia de Vaultrum. Fija el modelo canónico, la columna vertebral de numeración y el contrato de cada área. Todo lo que se construya de acá en adelante debe respetar este blueprint.

---

## Modelo canónico

La Agencia deja de ser una colección de "agentes/personas sueltas" y pasa a organizarse **enteramente en Áreas**.

Un Área siempre tiene tres partes (patrón validado en el Área de Producción):

1. **Sub-agentes** — mentalidades con responsabilidad única y límites duros, que se pasan el trabajo entre sí.
2. **Flujos preseteados** — procedimiento por sub-agente: entrada → transformación → salida → criterios de aceptación → condiciones para avanzar.
3. **Salidas registrables** — artefactos formales, numerados e indexados, que quedan escritos en el vault.

Regla: un Área nunca termina solo en una charla. Termina depositando una salida registrable.

---

## Cómo se encadenan las áreas

Las áreas de producción se conectan por sus salidas. La salida de un área es la entrada de la siguiente. Ninguna área arranca sin su insumo; si falta, lo marca y no avanza.

El **Core es la fuente y el retorno** de todo. Alimenta el arranque de cada área (principio 1: partir del Core) y recibe de vuelta el conocimiento reutilizable a través del control de versiones.

```
        ┌──────────── VaultrumCore = main (fuente de criterio) ────────────┐
        │  alimenta el ARRANQUE de cada área                               │
        ▼                                                                  │
Intención                                                                  │
  ↓                                                                        │
Área de Producción     → TL + RQ      (qué, alcance, prioridad)            │
  ↓ (RQ jugable)                                                           │
Área de Game Design    → GDS          (reglas, feedback, estados, balance) │
  ↓ (RQ + GDS)                                                             │
Área de Programación   → SOL + EJ     (solución técnica + implementación)  │
  │                                                                        │
  └──── aprendizaje reutilizable ──► Área de Conocimiento ─── merge ───────┘
                                     (control de versiones del Core)
```

Todas las áreas de producción leen **VaultrumCore** como base de criterio (SOLID, patrones, managers, optimización, estructuras, algoritmos, IA). El Área de Conocimiento no es una etapa de producción: es la **capa de control de versiones** que gestiona qué vuelve al Core, con criterio y aprobación.

---

## Columna vertebral de numeración

Todo cuelga del número base del **timeline**. Cada área agrega su prefijo sobre el mismo número base, manteniendo la relación 1:1 con el requerimiento.

| Prefijo | Artefacto | Área | Cuelga de |
|---------|-----------|------|-----------|
| `TL-XXX` | Timeline (roadmap) | Producción | — (número base) |
| `RQ-XXX.n` | Requerimiento | Producción | TL-XXX |
| `GDS-XXX.n` | Game Design Spec | Game Design | RQ-XXX.n |
| `SOL-XXX.n` | Solución técnica | Programación | RQ-XXX.n (+ GDS-XXX.n) |
| `EJ-XXX.n` | Ejecución / reporte | Programación | SOL-XXX.n |

La subnumeración `.n` es compartida: `RQ-001.2 ↔ GDS-001.2 ↔ SOL-001.2 ↔ EJ-001.2` son el mismo hilo de trabajo visto por cada área.

Reglas:
- No se inventa numeración sin revisar los índices del área.
- Cada salida linkea hacia atrás a su insumo (EJ → SOL → RQ/GDS → TL).
- Un artefacto downstream no existe sin su insumo upstream.

---

## Contrato de cada área

**Producción** — consume una intención/idea → produce `TL` + `RQ`. Define qué se hace, por qué, con qué alcance y prioridad. No diseña gameplay ni resuelve implementación.

**Game Design** (ex-Technical Game Designer) — consume un `RQ` jugable → produce `GDS`: reglas, entradas/salidas, feedback, estados, parámetros configurables, criterios de validación. No programa.

**Programación** — consume `RQ` (+ `GDS` si existe) → produce `SOL` (solución técnica validada, SOLID, expansible, apoyada en el Core) y `EJ` (implementación real + reporte). Sus sub-agentes **iteran entre sí** hasta cumplir los criterios de aceptación. No define alcance ni reglas de gameplay.

**Conocimiento** (Encargado de Commits + Documentador + Arquitecto de Conocimiento) — **capa de control de versiones del Core**, no una etapa de producción. Modelo git: Core = `main`, proyecto = `branch`, aprendizaje = `commit`, entrar al Core = `merge` con aprobación del maintainer. Contempla tres casos: dev completo (merge limpio / retrospectiva), branch nueva (aprendizaje → Staging → aprobación → merge) y experimento (evaluar → promover o descartar). Usa una carpeta **Staging** transitoria; no acumula historial (principio 11).

Auditoría no es un área separada: los **criterios de aceptación** viven dentro del flujo de cada área y el Revisor de cada área los aplica.

---

## Ejemplo end-to-end: "Hacé un Pong"

```
Usuario: "Hacé un Pong"

Área de Producción
  TL-001  Pong jugable (roadmap)
  RQ-001.1  Paletas controlables
  RQ-001.2  Pelota con rebote y velocidad
  RQ-001.3  Score y condición de victoria

Área de Game Design
  GDS-001.1  Reglas de paleta: input, límites, velocidad, feedback
  GDS-001.2  Reglas de pelota: rebote, aceleración, saque, feedback
  GDS-001.3  Reglas de score: puntaje, victoria, reinicio

Área de Programación  (los sub-agentes iteran hasta el "Pong más vaultrumita")
  SOL-001.1  PaddleController + input desacoplado, valores configurables (SO)
  SOL-001.2  BallController + BounceService, física en clase pura, sin hardcodeo
  SOL-001.3  ScoreManager (coordina, no absorbe) + eventos de UI
  EJ-001.1 / EJ-001.2 / EJ-001.3  implementación en Unity + reporte

Área de Conocimiento
  Si algo del Pong genera criterio reutilizable (ej: patrón de rebote),
  vuelve al Core.
```

El "Pong más vaultrumita" se garantiza porque los criterios de aceptación de Programación exigen: usa conocimiento del Core, aplica SOLID, queda expansible, sin hardcodeo, respeta alcance.

---

## Alcance del refactor

1. **Áreas objetivo:** Producción (existe, es el template), Game Design, Programación, Conocimiento.
2. **Los 7 Agentes viejos** se absorben en el área que corresponda o se archivan si no sirven a este path. Decisión fina posterior a este blueprint.
3. **Cada área = una skill ejecutable** en Cowork que corre sus flujos y escribe sus salidas.
4. **Primera implementación de referencia:** Área de Programación.

---

## Regla final del blueprint

Una idea entra como intención y recorre las áreas transformándose en salidas registrables encadenadas, hasta convertirse en algo construido con criterio Vaultrum. Cada área hace una sola cosa, la hace bien, la deja escrita y numerada, y se la pasa a la siguiente.

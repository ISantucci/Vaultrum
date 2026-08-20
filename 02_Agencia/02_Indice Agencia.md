## Propósito

La Agencia reúne las áreas, sub-agentes, flujos y salidas que permiten trabajar con Vaultrum de forma asistida.

No reemplaza al Core.

La Agencia existe para usar el conocimiento de VaultrumCore con dirección, contexto y responsabilidad.

```txt
VaultrumCore
→ criterio base

Agencia
→ aplicación asistida del criterio
```

---

## Modelo de trabajo: Áreas

La Agencia se organiza en **Áreas**. Un área es autocontenida: trae consigo su gente, su método, su producto y su ejecutable.

- **`Agentes/`** — sub-agentes con responsabilidad única y límites duros.
- **`Flujos/`** — procedimiento por sub-agente, con criterios de aceptación.
- **`Salidas/`** — artefactos formales, numerados e indexados, que quedan escritos en el vault.
- **`Skills/`** — la skill ejecutable del área, que corre sus flujos y escribe sus salidas.

Cada área es dueña de su propia metodología de trabajo. Nada de un área vive fuera de su carpeta.

Regla: un área nunca termina solo en una charla. Termina depositando una salida registrable.

---

## Cómo se encadenan las áreas

La salida de un área es la entrada de la siguiente. Ninguna área arranca sin su insumo; si falta, lo marca y no avanza.

El **Core es la fuente y el retorno** de todo: alimenta el arranque de cada área (principio 1) y recibe de vuelta el conocimiento reutilizable a través del control de versiones.

```txt
        ┌──────────── VaultrumCore = main (fuente de criterio) ────────────┐
        │  alimenta el ARRANQUE de cada área                               │
        ▼                                                                  │
Intención                                                                  │
  ↓                                                                        │
Área de Producción     → TL + RQ      (qué, alcance, prioridad)            │
  ↓ (RQ jugable)                                                           │
Área de Game Design    → GDS          (reglas, feedback, estados, balance) │
  ↓ (GDS cerrado)                                                          │
  ├─► Área de Level Design → LDS  (espacio, niveles, encuentros, pacing)   │
  └─► Área de UI/UX        → UXS  (pantallas, HUD, menús, legibilidad)     │
  ↓ (RQ + GDS + LDS + UXS)                                                 │
Área de Programación   → SOL + EJ     (solución técnica + implementación)  │
  │                                                                        │
  └──── aprendizaje reutilizable ──► Área de Conocimiento ─── merge ───────┘
                                     (control de versiones del Core)
```

El Área de Conocimiento no es una etapa de producción: es la capa de control de versiones que gestiona qué vuelve al Core, con criterio y aprobación.

---

## Columna vertebral de numeración

Todo cuelga del número base del **timeline**. Cada área agrega su prefijo sobre el mismo número base, manteniendo la relación 1:1 con el requerimiento.

| Prefijo | Artefacto | Área | Cuelga de |
|---------|-----------|------|-----------|
| `TL-XXX` | Timeline (roadmap) | Producción | — (número base) |
| `RQ-XXX.n` | Requerimiento | Producción | TL-XXX |
| `GDS-XXX.n` | Game Design Spec | Game Design | RQ-XXX.n |
| `LDS-XXX.n` | Level Design Spec | Level Design | GDS-XXX.n |
| `UXS-XXX.n` | UI/UX Spec | UI/UX | GDS-XXX.n |
| `SOL-XXX.n` | Solución técnica | Programación | RQ-XXX.n (+ GDS/LDS/UXS-XXX.n) |
| `EJ-XXX.n` | Ejecución / reporte | Programación | SOL-XXX.n |

La subnumeración `.n` es compartida: `RQ-001.2 ↔ GDS-001.2 ↔ LDS-001.2 ↔ UXS-001.2 ↔ SOL-001.2 ↔ EJ-001.2` son el mismo hilo de trabajo visto por cada área. `LDS` y `UXS` son **opcionales**: existen solo si el `GDS` tiene, respectivamente, dimensión espacial o interfaz.

Reglas:

- No se inventa numeración sin revisar los índices del área.
- Cada salida linkea hacia atrás a su insumo (`EJ → SOL → RQ/GDS → TL`).
- Un artefacto downstream no existe sin su insumo upstream. **Esta es la definición canónica de los gates**: quien la necesite, la referencia acá; no se copia a otros documentos.

Auditoría no es un área separada: los criterios de aceptación viven dentro del flujo de cada área y el Revisor de cada área los aplica.

---

## Áreas

### [[Area_produccion]]

Convierte una intención en roadmap y requerimientos. Produce `TL` (timeline) + `RQ` (requerimientos). Define qué se hace, por qué, con qué alcance y prioridad.

### [[Area_gamedesign]]

Technical Game Design. Consume un `RQ` jugable y lo convierte en un sistema jugable claro, implementable y validable. Produce `GDS` (game design spec): reglas, feedback, estados, parámetros configurables.

### [[Area_leveldesign]]

Diseño de espacio y tiempo. Consume un `GDS` cerrado con dimensión espacial y lo acomoda en un nivel: layout, colocación de desafíos/encuentros, checkpoints, progresión intra-nivel, pacing y curva de dificultad aplicada. Produce `LDS` (level design spec). No define reglas ni interfaces.

### [[Area_uiux]]

Capa de comunicación jugador↔juego. Consume un `GDS` (y opcionalmente un `LDS`) y diseña pantallas, HUD, menús, flujos de navegación, jerarquía de información y feedback. Produce `UXS` (UI/UX spec). Usabilidad primero, engagement después. No define reglas ni diseña el espacio jugable.

### [[Area_programacion]]

Convierte un `RQ` (+ `GDS`, `LDS`, `UXS`) en una solución técnica construida con criterio Vaultrum. Produce `SOL` (solución técnica) + `EJ` (ejecución). Sus sub-agentes iteran hasta cumplir los criterios de aceptación.

### [[Area_conocimiento]]

Capa de control de versiones del Core (no es producción). Modelo git: Core = `main`, proyecto = `branch`, aprendizaje = `commit`, entrar al Core = `merge` con aprobación. Gestiona qué conocimiento vuelve al Core, con criterio y sin acumular historial.

---

## Vínculo con la Escuela (05_Escuela)

La **Escuela** ([[00_Escuela]]) **no es un área de la Agencia**: es una capa propia. Comparte estructura (tiene `Agentes/`, `Flujos/`, `Salidas/`, `Skills/`) porque también es un lugar donde se trabaja, pero trabaja sobre otra cosa:

- La **Agencia** produce **el proyecto del usuario**. Su insumo es una intención; su producto son `TL/RQ/GDS/LDS/UXS/SOL/EJ`.
- La **Escuela** produce **conocimiento para el sistema**. Su insumo es un gap del Core; su producto son libros en la Biblioteca y candidatos `EST`.

Por eso no cuelga de la columna vertebral de numeración de arriba: sus salidas no son un eslabón de la cadena de producción. La Agencia se conecta con ella de dos formas:

- **Producción, Game Design, Level Design y UI/UX** la **consultan on-demand** en tiempo de diseño (vía el índice por género del Core y el libro [[05_Fundamentos_de_experiencia_ludica]]) para que la primera entrega sea sólida, no un MVP apurado.
- **Conocimiento** es el **puente de gobernanza**: recibe los candidatos `EST` de la Escuela y es el único que los propone a `main`.

---

## Nota sobre los agentes legacy

Los 7 "Agentes" del modelo anterior (personas/modos) fueron **absorbidos por las áreas y eliminados**: Programador/Auditor → Programación, Technical Game Designer → Game Design, Productor → Producción, Documentador/Arquitecto de Conocimiento → Conocimiento. Si en el futuro hace falta un rol que no tenga área, se crea en ese momento.

---

## Regla final

La Agencia no dirige al Core.

La Agencia usa el Core.

Primero criterio. Después área. Después salida registrable.

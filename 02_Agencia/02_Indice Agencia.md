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
- **`Flujos/`** — ficha de cada paso: entrada, criterios de aceptación, condiciones de avance y formato de salida.
- **`Salidas/`** — artefactos formales, numerados e indexados, que quedan escritos en el vault.
- **`Skills/`** — la skill ejecutable del área: corre el procedimiento y escribe las salidas.

Cada área es dueña de su propia metodología de trabajo. Nada de un área vive fuera de su carpeta.

Regla: un área nunca termina solo en una charla. Termina depositando una salida registrable.

**Regla de capas — qué vive dónde y qué manda.**

| Capa | Es dueña de | No contiene |
|------|-------------|-------------|
| `Skills/` | el **procedimiento ejecutable**: orden de pasos, gates y checklists operativos | responsabilidades y límites de cada agente |
| `Agentes/` | **responsabilidad y límites** de cada sub-agente, incluido a quién le rebota | el procedimiento ni los checklists operativos |
| `Flujos/` | **entrada, criterios de aceptación, condiciones de avance y formato de salida** por paso | el checklist operativo (lo referencia) |

Lo que corre tiene que ser autosuficiente: por eso **los checklists operativos viven solo en la Skill** y las fichas los referencian, no al revés. El documento `Area_*.md` es el mapa del área —propósito, agentes, loop, límites, encadenado— y tampoco sostiene checklists. Ante divergencia manda la Skill y se corrige la ficha.

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
                       (+ GDS-XXX.0 marco común, si 3+ GDS comparten base)   │
  ↓ (GDS cerrado)                                                          │
  ├─► Área de Level Design → LDS  (espacio, niveles, encuentros, pacing)   │
  └─► Área de UI/UX        → UXS  (pantallas, HUD, menús, legibilidad)     │
  ↓ (RQ + GDS + LDS + UXS)                                                 │
Área de Programación   → SOL + EJ     (solución técnica + implementación)  │
  ↓ (todos los EJ del TL en revisión OK)                                   │
Área de Producción     → VE           (validación de entrega del TL)       │
  │                                                                        │
  └──── aprendizaje reutilizable ──► Área de Conocimiento ─── merge ───────┘
                                     (control de versiones del Core)
```

**Dos palabras, dos cortes.** Un **hilo `.n`** es la cadena de un requerimiento (`RQ → GDS → LDS/UXS → SOL → EJ`) y lo cierra la revisión técnica del Área de Programación. Una **entrega** es el timeline completo (`TL` con todos sus hilos en OK) y la cierra el `VE` del Área de Producción.

**La entrega es de Producción de punta a punta.** La abre con la intención y la cierra validándola: el `EJ` cierra su hilo, no la entrega. Esto existe para que nadie dé por terminado algo que compila pero no se sostiene frente a un jugador (principio 4: eficacia sobre inmediatez).

El Área de Conocimiento no es una etapa de producción: es la capa de control de versiones que gestiona qué vuelve al Core, con criterio y aprobación.

---

## Columna vertebral de numeración

Todo cuelga del número base del **timeline**. Cada área agrega su prefijo sobre el mismo número base, manteniendo la relación 1:1 con el requerimiento.

| Prefijo | Artefacto | Área | Cuelga de |
|---------|-----------|------|-----------|
| `TL-XXX` | Timeline (roadmap) | Producción | — (número base) |
| `RQ-XXX.n` | Requerimiento | Producción | TL-XXX |
| `GDS-XXX.0` | Marco común (opcional) | Game Design | **TL-XXX** (no cuelga de un `RQ`) |
| `GDS-XXX.n` | Game Design Spec | Game Design | RQ-XXX.n |
| `LDS-XXX.n` | Level Design Spec | Level Design | GDS-XXX.n |
| `UXS-XXX.n` | UI/UX Spec | UI/UX | GDS-XXX.n |
| `SOL-XXX.n` | Solución técnica | Programación | RQ-XXX.n (+ GDS/LDS/UXS-XXX.n) |
| `EJ-XXX.n` | Ejecución / reporte | Programación | SOL-XXX.n |
| `VE-XXX` | Validación de entrega | Producción | TL-XXX (con sus `EJ` en OK) |

La subnumeración `.n` es compartida: `RQ-001.2 ↔ GDS-001.2 ↔ LDS-001.2 ↔ UXS-001.2 ↔ SOL-001.2 ↔ EJ-001.2` son el mismo hilo de trabajo visto por cada área. El `VE` es la excepción y **no lleva `.n`**: valida la entrega del timeline completo, porque la definición de terminado es del entregable y no de la pieza. `LDS` y `UXS` son **opcionales**: existen solo si el `GDS` tiene, respectivamente, dimensión espacial o interfaz.

Reglas:

- No se inventa numeración sin revisar los índices del área.
- Cada salida linkea hacia atrás a su insumo (`EJ → SOL → RQ/GDS/LDS/UXS → TL`, y `VE → TL`).
- Un artefacto downstream no existe sin su insumo upstream. **Esta es la definición canónica de los gates**: quien la necesite, la referencia acá; no se copia a otros documentos.
- **Los dos artefactos que cuelgan del `TL` y no de un `RQ` son `GDS-XXX.0` y `VE-XXX`.** Ninguno lleva `.n` de hilo: el marco común porque es transversal a varios hilos, el `VE` porque la definición de terminado es del entregable y no de la pieza. Cualquier otro artefacto sin `RQ` upstream es un hueco, no una excepción.
- El `GDS-XXX.0` es **opcional y condicionado**: se abre solo si tres o más `GDS` del timeline comparten definiciones. Detalle en [[00_Indice_gds]].
- Una omisión declarada es criterio; una omisión silenciosa es un hueco. Si `LDS` o `UXS` no aplican, el `GDS` lo dice explícitamente **y dice qué dimensión del entregable está ausente** — un "no aplica" es una afirmación verificable, no un atajo. Se comprueba al cerrar el `VE` con el *test del "no aplica"*: ¿la siguiente área tuvo que hacer ese trabajo igual?
- Un `TL` no está entregado sin su `VE` en estado **Cerrado**. La revisión técnica cierra el hilo `.n`; la validación de entrega cierra la iteración.
- El `VE` declara su **modo de cierre**: `Checklist` (se recorren los ítems sobre el entregable corriendo) o `Veredicto` (juicio global del owner sobre el entregable corriendo, con la deuda declarada). Detalle en [[00_Indice_ve]].

**Estados de cierre de un paso (vocabulario común a todas las áreas).** Cada paso cierra declarando: **Cerrado** (avanza) · **Ajustar** (rebota con hallazgo concreto al sub-agente o área que corresponde) · **Pausado** (falta información o una decisión del owner; se declara qué falta y no se avanza — principio 9). Pausar es un cierre válido, no un fracaso: es preferible a construir sobre un supuesto. En el análisis estratégico de Producción se suma **Descartado**, porque es el único paso donde una idea puede no seguir.

No confundir con el **estado de un artefacto** en su índice, que describe el ciclo de vida de la salida (dónde está en el loop del área) y no la decisión de un paso. Cada área define el suyo en su índice de salidas, porque sus etapas son distintas.

Auditoría no es un área separada: los criterios de aceptación viven dentro del flujo de cada área y el Revisor/Validador de cada área los aplica.

---

## Los bordes de la cadena

El medio de la cadena funciona; los bordes son donde falla. La evidencia es la comparación `TL-002` vs `TL-003`: la primera tenía `RQ`, `GDS`, `SOL` y `EJ` de buena calidad —tanto que se reutilizaron— y aun así la entrega quedó en PAUSADO y su implementación nunca llegó a estar en disco.

Los tres fallos fueron de borde, y las tres reglas que los cubren viven ahora **como pasos ejecutables de las skills**, no como criterio escrito:

| Borde | Regla | Dónde corre |
|-------|-------|-------------|
| **Entrada** | el insumo se verifica antes de consumirlo: un libro de género vacío dispara una misión de Escuela, no se suple con intuición | `vaultrum-produccion`, gate de insumo de Biblioteca |
| **Ramas opcionales** | un "no aplica" declara qué dimensión falta, y se comprueba a posteriori con el test del "no aplica" | `vaultrum-gamedesign` (declara) + `vaultrum-produccion` (comprueba en el `VE`) |
| **Salida** | existir en disco es parte del cierre: un `EJ` no está reportado si el artefacto no está donde el `TL` dice | `vaultrum-programador`, gate de existencia en disco |

Criterio de fondo en el Core: `Gates verificables` — *un gate que no se puede verificar mecánicamente no es un gate, es una intención.*

---

## Fuente de criterio: qué se le exige a una entrega

La Agencia **aplica** los criterios de entrega; no los define. Viven en el Core, en `01_VaultrumCore/.../04_Criterios de entrega/`:

```txt
[[Baseline de entregable]]         completo en experiencia, mínimo en maquinaria
[[Verificacion parcial declarada]] cómo se declara una verificación incompleta
[[Gates verificables]]             por qué la cadena falla en los bordes
```

Y el índice hacia el baseline por género: `Experiencia de juego`.

Si una skill y el Core divergen, el Core es el criterio y la skill es el procedimiento: se corrige la skill.

---

## Áreas

### [[Area_produccion]]

Convierte una intención en roadmap y requerimientos, y es **dueña del hilo de trabajo**. Produce `TL` (timeline) + `RQ` (requerimientos) al abrir, y `VE` (validación de entrega) al cerrar. Define qué se hace, por qué, con qué alcance y prioridad — y verifica al final que lo entregado sea lo prometido.

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

### [[Area_arquitectura]]

Cuida la **forma** del vault, no su contenido: que se pueda entrar por un índice y llegar caminando a cualquier nota.

Mide el grafo con herramienta, repara con el cambio mínimo y verifica. Es la única área que no produce contenido: produce recorrido.

Sus salidas (`ARQ`) tampoco cuelgan de la columna vertebral de numeración: no son un eslabón de la cadena de producción, son pasadas sobre el vault mismo.

---

## Vínculo con la Escuela (05_Escuela)

La **Escuela** (`00_Escuela`) **no es un área de la Agencia**: es una capa propia. Comparte estructura (tiene `Agentes/`, `Flujos/`, `Salidas/`, `Skills/`) porque también es un lugar donde se trabaja, pero trabaja sobre otra cosa:

- La **Agencia** produce **el proyecto del usuario**. Su insumo es una intención; su producto son `TL/RQ/GDS/LDS/UXS/SOL/EJ`.
- La **Escuela** produce **conocimiento para el sistema**. Su insumo es un gap del Core; su producto son libros en la Biblioteca y candidatos `EST`.

Por eso no cuelga de la columna vertebral de numeración de arriba: sus salidas no son un eslabón de la cadena de producción. La Agencia se conecta con ella de dos formas:

- **Producción, Game Design, Level Design y UI/UX** la **consultan on-demand** en tiempo de diseño (vía el índice por género del Core y el libro [[05_Fundamentos_de_experiencia_ludica]]) para que la primera entrega sea sólida, no un MVP apurado.
- **Conocimiento** es el **puente de gobernanza**: recibe los candidatos `EST` de la Escuela y es el único que los propone a `main`.

---

## Roles fuera de las áreas

No hay ninguno: los siete roles del modelo anterior fueron absorbidos por las áreas. Si hace falta un rol que ninguna área cubra, se crea en ese momento y con su área.

---

## Regla final

La Agencia no dirige al Core.

La Agencia usa el Core.

Primero criterio. Después área. Después salida registrable.

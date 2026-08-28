---
tipo: fuente
titulo: "Frameworks de desarrollo dirigido por especificación, multi-superficie"
autores: github/spec-kit · bmad-code-org/BMAD-METHOD · Fission-AI/OpenSpec · buildermethods/agent-os
editorial: repositorios open-source (GPL/MIT según proyecto)
anio: 2026
estado: Estudiado (destilada — alimentó RQ-007.2, RQ-007.3, RQ-007.7)
mision: EST-007_Mision_Frameworks_Spec_Driven
temas: agent skills, progressive disclosure, portabilidad multi-agente, economía de tokens, relevamiento asistido
---

# Fuente 30 — Frameworks de desarrollo dirigido por especificación, multi-superficie

> Fuente externa de **código y documentación**, no de libro. Relevada sobre paquetes reales (npm/PyPI) y doc oficial.
> **IP:** mecanismos y criterio, con cita de archivo y URL. Nada de código copiado.

## Cita

- `github/spec-kit` — `specify-cli` 1.0.1 (PyPI) · https://github.com/github/spec-kit
- `bmad-code-org/BMAD-METHOD` — `bmad-method` 6.11.0 (npm) · https://github.com/bmad-code-org/BMAD-METHOD
- `Fission-AI/OpenSpec` — `@fission-ai/openspec` 1.10.0 (npm) · https://openspec.pro/
- `buildermethods/agent-os` v3.0 · https://github.com/buildermethods/agent-os
- Estándar **Agent Skills** · https://agentskills.io · https://code.claude.com/docs/en/skills · https://developers.openai.com/codex/skills/

## Qué es (marco aprendido)

Cuatro sistemas que resuelven el mismo problema que Vaultrum —convertir una intención en un entregable pasando por artefactos escritos— y que llegaron antes a las respuestas de dos preguntas que Vaultrum tiene abiertas: **cómo correr en varias superficies** y **cómo no gastar el contexto en la maquinaria**.

### El hallazgo que reordena todo

**Los tres primeros migraron al formato Agent Skills** (`<nombre>/SKILL.md` con frontmatter `name` + `description`) y abandonaron sus layouts propietarios. La portabilidad ya no la resuelve cada framework: la resuelve el estándar.

```txt
.claude/skills/<nombre>/SKILL.md     Claude Code
.agents/skills/<nombre>/SKILL.md     Codex, y el directorio compartido que
                                     también leen Cursor, Zed, Copilot y otros
```

Y con él viene la **carga en tres etapas**, que es la respuesta al problema de tokens:

```txt
1. Discovery    al arrancar se carga SOLO name + description
2. Activation   el SKILL.md entero, recién cuando la tarea matchea
3. Execution    los archivos referenciados, recién si hacen falta
```

Presupuestos reales: Claude Code topea el listado al **1% de la ventana**, con **1.536 chars por entrada**; Codex al **2% u 8.000 chars**. BMAD: 49 skills, 303 KB en disco, 9,3 KB residentes — **ratio 239 : 1**.

## Los mecanismos destilados

### 1. El archivo de memoria es un puntero, no contenido

spec-kit escribe **tres líneas** en `CLAUDE.md`/`AGENTS.md`, entre marcadores delimitados e idempotentes, y dejó incluso eso en una extensión **opt-in que su instalador no corre**: *"Spec Kit itself never touches your agent context file."* OpenSpec va más lejos y **borra** sus bloques legados al migrar — conservando siempre el archivo, que nunca se elimina entero.

> Criterio: el descubrimiento de skills ya hace ese trabajo, con presupuesto propio. Meter texto en el archivo de memoria es pelear contra el diseño del harness.

### 2. El subagente que ahorra contexto tiene un contrato

BMAD: *"cada uno escribe su revisión completa a `review-{slug}.md` y devuelve SOLO un resumen compacto — el padre nunca sostiene el texto completo."*

Y el contraejemplo, escrito por spec-kit en su propio código al revertir la optimización: forkear un comando cuyo resultado **no** es compacto acumula contexto en vez de ahorrarlo, porque el informe entero vuelve al padre y cada fork siguiente lo hereda, hasta congelar la sesión.

> Criterio: **fork solo si el subagente devuelve un resumen corto y escribe el resto a disco.** El fork no es gratis por ser fork.

### 3. Reglas de entrevista, con evidencia

De BMAD (`bmad-project-context`):

```txt
"Never ask what a scan could answer. Asking the user to confirm a
 path-checked claim, or one a config file already states, IS A DEFECT."
"Ask recall questions, not review lists."
"Batches of at most eight; fewer is better.
 A batch yielding nothing new means write."
"No writes until step 5."   ·   "Note the paths; do not read them yet."
```

De spec-kit (`clarify.md`): techo de **5 preguntas**, una por vez, cada una multiple-choice o respuesta de ≤5 palabras, con **`Recommended: Option X — <razón>`** para que el usuario conteste "sí"; **escritura al disco después de cada respuesta**, no al final; y la regla anti-rótulo: una pregunta termina en `?` y se entiende sola — un encabezado de sección no es una pregunta.

De spec-kit (`specify.md`): marcador `[NEEDS CLARIFICATION: …]` con **máximo 3**, política de *adivinar informado* por defecto, prioridad `alcance > seguridad/privacidad > UX > técnico`, y lo no preguntado va a una sección `Assumptions` **visible**.

### 4. El grafo del workflow como dato, no como prosa

BMAD describe 29 skills en un CSV de **7.645 bytes** con columnas `phase, preceded-by, followed-by, required, output-location, outputs`. Una skill de orientación lee el CSV —no las skills— para saber dónde está el usuario y qué sigue.

### 5. Separación framework / salidas

Los cuatro separan lo mismo que Vaultrum está separando en `TL-008`:

```txt
spec-kit    framework en .specify/     salidas en specs/NNN-slug/
BMAD        framework en _bmad/        salidas en _bmad-output/
OpenSpec    config en openspec/        salidas en openspec/changes/
Agent OS    todo en agent-os/          salidas en agent-os/specs/
```

Con **creación perezosa** declarada en BMAD: *"no pre-created directories… created lazily by whichever skill first writes to them."*

### 6. Referencia por ruta vs. contenido, decidido por destino

Agent OS: si el destino es otra skill o un plan, se emite `@ruta/al/estandar.md`; si el destino es la conversación en curso, se lee el contenido. Y expone el trade-off al usuario: *referencias* = liviano y sincronizado; *copiar contenido* = autocontenido pero congelado.

### 7. Frontera dura planificación / implementación

OpenSpec, escrito en el prompt: *"el pedido que activó este workflow autoriza planificación únicamente, aunque pida construir o arreglar algo. No empieces la implementación en la misma respuesta."*

## Por qué le sirve a Vaultrum

Vaultrum ya tiene la forma correcta —skills como áreas, Core/branch/commit, AiCare midiendo— y ya escribe en formato Agent Skills. Lo que le faltaba es lo de arriba, y casi todo es copiable sin adaptar.

Medición propia al momento de destilar: las diez skills de Vaultrum suman **5.457 chars de `description`** (residente), la más larga 781 (tope 1.536), el `SKILL.md` más largo 218 líneas (guía: <500), **78.630 bytes** en disco que no se cargan. **Entra en las dos superficies sin podar nada.**

## Límites (cuándo NO aplica)

- **No copiar los personajes con nombre.** BMAD invierte ~4,5 KB por agente en identidad escénica (nombre propio, estilo de habla, emoji, *"do not break character"*). Vaultrum ya nombra por función, que es lo que aporta el routing.
- **No copiar el soporte de 38–47 superficies.** Es un impuesto de mantenimiento permanente. Dos destinos cubren todo lo que hace falta.
- **No reimplementar lo que el harness ya hace.** Agent OS v3 **borró** sus fases de spec-writing, task breakdown y orquestación de implementación: *"plan mode, extended thinking, and improved models now handle much of the scaffolding that earlier versions provided."* Es la frontera de lo que no vale la pena construir.
- **No volcar catálogo ni constitución al contexto de arranque.** Ninguno de los cuatro lo hace ya.
- Relevamiento de **agosto 2026**. Los cuatro se mueven rápido; las rutas y los topes se re-verifican antes de fijarlos.

## Discrepancia sin resolver

La doc de OpenAI menciona **solo** `.agents/skills` para Codex. BMAD escribe igual `~/.codex/skills` y OpenSpec lo lista como `legacySkillsDirs`. **No se pudo confirmar que Codex lea `.codex/skills` hoy.** Se fija `.agents/skills` y se re-verifica antes de cerrar `RQ-007.7`.

## Estado y próximos pasos

- **Destilada.** Alimentó `RQ-007.2` (la puerta como puntero), `RQ-007.3` (tandas y recomendación por defecto) y `RQ-007.7` (portabilidad).
- Pendiente de aplicar: el grafo-como-CSV (§4) y la referencia-por-ruta (§6) todavía no tienen requerimiento.
- No entró al Core. Es fuente, no criterio propio.

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
- **`Herramientas/`** — opcional: los instrumentos que el área usa para medir lo que afirma. Un área que declara un número sin instrumento está estimando.

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
Área de UI/UX          → UXS mitad A  (presupuesto de comunicación)        │
  ↓ (el presupuesto condiciona el sistema, no su presentación)             │
Área de Game Design    → GDS          (reglas, feedback, estados, balance) │
                       (+ GDS-XXX.0 marco común, si 3+ GDS comparten base)   │
  ↓ (GDS cerrado)                                                          │
  ├─► Área de Level Design → LDS  (espacio, niveles, encuentros, pacing)   │
  └─► Área de UI/UX        → UXS mitad B (pantallas, HUD, legibilidad)     │
  ↓ (RQ + GDS + LDS + UXS)                                                 │
Área de Programación   → SOL + EJ     (solución técnica + implementación)  │
  ↓ (EJ con revisión técnica OK)                                           │
Área de Control        → QA           (¿se sostiene lo construido?)        │
de Calidad               QA-XXX.n por hilo · QA-XXX por entrega            │
  ↓ (QA en GO o CONDITIONAL GO)                                            │
Área de Producción     → VE           (validación de entrega del TL)       │
  │                                                                        │
  └──── aprendizaje reutilizable ──► Área de Conocimiento ─── merge ───────┘
                                     (control de versiones del Core)
```

**Dos palabras, dos cortes.** Un **hilo `.n`** es la cadena de un requerimiento (`RQ → GDS → LDS/UXS → SOL → EJ → QA`): la revisión técnica cierra su construcción y el `QA-XXX.n` decide si lo construido se sostiene. Una **entrega** es el timeline completo (`TL` con todos sus hilos verificados) y la cierran el `QA-XXX` y, con él en la mano, el `VE` del Área de Producción.

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
| `UXS-XXX.n` | UI/UX Spec | UI/UX | RQ-XXX.n (mitad A) + GDS-XXX.n (mitad B) |
| `SOL-XXX` o `SOL-XXX.n` | Solución técnica | Programación | **uno o varios** RQ-XXX.n del mismo TL |
| `EJ-XXX` o `EJ-XXX.n` | Ejecución / reporte | Programación | su `SOL` |
| `QA-XXX.n` | Gate de calidad del hilo | Control de Calidad | EJ-XXX.n |
| `QA-XXX` | Gate de calidad de la entrega | Control de Calidad | **TL-XXX** (con sus `QA-XXX.n`) |
| `VE-XXX` | Validación de entrega | Producción | TL-XXX (con su `QA-XXX`) |

La subnumeración `.n` es compartida entre las áreas de diseño: `RQ-001.2 ↔ GDS-001.2 ↔ LDS-001.2 ↔ UXS-001.2 ↔ QA-001.2` son el mismo hilo de trabajo visto por cada una.

**`SOL` y `EJ` son la excepción, y es deliberada: su relación con el `RQ` es 1:N.** Un `SOL` es la arquitectura de una épica, y una épica se decide una vez, no una por requerimiento — `Salto/SOL-001` declara en su propio `Insumo` que cubre `RQ-001.1` … `RQ-001.8`. Puede llevar `.n` cuando cubre un solo hilo, y puede no llevarlo cuando cubre el timeline entero. Las dos formas son válidas.

Hasta el 2026-09-01 esta tabla decía 1:1 y el disco hacía 1:N desde siempre. Se corrigió la tabla, no el disco: renombrar habría obligado a partir un `SOL` en ocho artefactos que nunca existieron, que es falsear la historia. Decisión del owner, `RQ-009.4`, opción C.

**Y la relación 1:N tiene un precio que la hace verificable, no una convención:** un `SOL` que cubre varios `RQ` **tiene que enumerarlos en su `Insumo`** —un rango como `` `RQ-001.1` … `RQ-001.8` `` cuenta como enumeración—, y `documentacion.py` comprueba con su **Ley 1b** que ningún `RQ` de un timeline **cerrado** se haya quedado sin `SOL` que lo cubra. En un timeline abierto no mide: un `RQ` sin `SOL` ahí no es un hueco, es trabajo que todavía no se hizo.

Eso es lo que resuelve el riesgo real. El miedo era que `EJ-00X → QA-00X.n` dejara de ser resoluble: no se resuelve con un sufijo, se resuelve con la enumeración — y recién sirve cuando alguien la verifica. El `QA` de entrega y el `VE` son las excepciones y **no llevan `.n`**: valida la entrega del timeline completo, porque la definición de terminado es del entregable y no de la pieza. `LDS` y `UXS` son **opcionales**: existen solo si el hilo tiene, respectivamente, dimensión espacial o algo que alguien tenga que leer. El `UXS` es el único artefacto que **abre antes que su insumo principal**: su mitad A se escribe contra el `RQ` para que Game Design pueda cerrar el `GDS` contra ella. Por eso declara dos insumos y no uno.

Reglas:

- No se inventa numeración sin revisar los índices del área.
- Cada salida linkea hacia atrás a su insumo (`QA → EJ → SOL → RQ/GDS/LDS/UXS → TL`, y `QA-XXX → TL`, y `VE → TL`).
- Un artefacto downstream no existe sin su insumo upstream. **Esta es la definición canónica de los gates**: quien la necesite, la referencia acá; no se copia a otros documentos.
- **Los tres artefactos que cuelgan del `TL` y no de un `RQ` son `GDS-XXX.0`, `QA-XXX` y `VE-XXX`.** Ninguno lleva `.n` de hilo: el marco común porque es transversal a varios hilos; el `QA` de entrega y el `VE` porque la decisión de calidad y la definición de terminado son del entregable y no de la pieza. Cualquier otro artefacto sin `RQ` upstream es un hueco, no una excepción.
- El `GDS-XXX.0` es **opcional y condicionado**: se abre solo si tres o más `GDS` del timeline comparten definiciones. Detalle en `00_Indice_gds`.
- Una omisión declarada es criterio; una omisión silenciosa es un hueco. Si `LDS` o `UXS` no aplican, el `GDS` lo dice explícitamente **y dice qué dimensión del entregable está ausente** — un "no aplica" es una afirmación verificable, no un atajo. Se comprueba al cerrar el `VE` con el *test del "no aplica"*: ¿la siguiente área tuvo que hacer ese trabajo igual?
- Un `TL` no está entregado sin su `VE` en estado **Cerrado**. La revisión técnica cierra el hilo `.n`; el `QA` decide si lo construido se sostiene; la validación de entrega cierra la iteración.
- **Un `VE` no cierra en Cerrado sin su `QA` en GO o CONDITIONAL GO**, citado en el `VE`. Un `QA` en NO-GO deja la entrega en *Ajustar* o *Pausado*, nunca en Cerrado.
- El `VE` declara su **modo de cierre**: `Checklist` (se recorren los ítems sobre el entregable corriendo) o `Veredicto` (juicio global del owner sobre el entregable corriendo, con la deuda declarada). Detalle en `00_Indice_ve`.

**Estados de cierre de un paso (vocabulario común a todas las áreas).** Cada paso cierra declarando: **Cerrado** (avanza) · **Ajustar** (rebota con hallazgo concreto al sub-agente o área que corresponde) · **Pausado** (falta información o una decisión del owner; se declara qué falta y no se avanza — principio 9). Pausar es un cierre válido, no un fracaso: es preferible a construir sobre un supuesto. En el análisis estratégico de Producción se suma **Descartado**, porque es el único paso donde una idea puede no seguir.

No confundir con el **estado de un artefacto** en su índice, que describe el ciclo de vida de la salida (dónde está en el loop del área) y no la decisión de un paso. Cada área define el suyo en su índice de salidas, porque sus etapas son distintas.

Auditoría no es un área separada: los criterios de aceptación viven dentro del flujo de cada área y el Revisor/Validador de cada área los aplica. Control de Calidad tampoco audita a las demás: no revisa cómo trabajó cada área, verifica **lo construido** contra los criterios que esas áreas escribieron.

---

## Dónde aterriza cada salida

**Un área explica cómo trabaja y qué forma tiene lo que devuelve. No guarda lo que devuelve.**

El trabajo de un proyecto vive en la carpeta del proyecto. `Vaultrum/` no se escribe a sí mismo mientras trabaja.

```txt
<Proyecto>/
├── <Proyecto>.md      el cuaderno: identidad, entorno, estado, decisiones, pendientes
├── 01_Produccion/     TL · RQ · VE
├── 02_GameDesign/     GDS
├── 03_LevelDesign/    LDS
├── 04_UI-UX/          UXS
├── 05_Programacion/   SOL · EJ
└── 06_Calidad/        QA
```

La carpeta existe si un área efectivamente escribió algo ahí: **nada se pre-crea**.

| Área | Escribe en | |
|------|-----------|---|
| Producción | `<Proyecto>/01_Produccion/` | `TL` · `RQ` · `VE` |
| Game Design | `<Proyecto>/02_GameDesign/` | `GDS` |
| Level Design | `<Proyecto>/03_LevelDesign/` | `LDS` |
| UI/UX | `<Proyecto>/04_UI-UX/` | `UXS` |
| Programación | `<Proyecto>/05_Programacion/` | `SOL` · `EJ` |
| Control de Calidad | `<Proyecto>/06_Calidad/` | `QA` |
| **Conocimiento** | **el sistema** — Staging y Core | su producto **no** es del proyecto |
| **Arquitectura** | **el sistema** — `Salidas/ARQ` | interviene el vault, no el proyecto |

Las dos últimas no se mudan, y eso es el criterio funcionando: **lo que produce sistema se queda en el sistema; lo que produce proyecto se va al proyecto.**

### Cómo sabe un área dónde está el proyecto

Lo lee del **cuaderno**, que Producción escribe al cerrar el seteo. No lo adivina ni lo vuelve a preguntar.

Si **no hay** carpeta de proyecto, un área no inventa una: **devuelve a Producción**, que es quien abre el proyecto.

### La numeración es local al proyecto

El contador arranca en `TL-001` por proyecto. El `TL-001` de un juego y el de otro son distintos porque viven en carpetas distintas.

> **Consecuencia declarada:** se pierde el número global. `TL-004` sin su proyecto es ambiguo. **Toda referencia cruzada entre proyectos nombra el proyecto.**

### Qué queda en `Salidas/` de cada área

El **contrato de salida**: qué produce, qué forma tiene, cómo se numera, dónde aterriza y cuándo está cerrado. El listado de artefactos vive en el cuaderno del proyecto.

Origen: `TL-008_La_Agencia_Es_La_Empresa` · `RQ-008.3_Reapuntado_De_Las_Skills`.

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

Cuida la **legibilidad del sistema**: que quien lo opera pueda responder qué pasa, qué puede hacer y cómo va, sin que nadie se lo explique. Vale para un juego y para cualquier herramienta con operador — un jugador es un operador con reglas de juego encima.

**Entra dos veces.** Antes de que Game Design cierre, con el **presupuesto de comunicación**: cuántas señales entran, por qué canal, con qué techo y qué no entra. Y después, con la **interfaz**: pantallas, HUD, menús, jerarquía, mapping, feedback y accesibilidad. Presta además un tercer servicio, **Pasada**, para medir una interfaz que ya existe.

Produce `UXS` (UI/UX spec), en dos mitades con dos cierres. Aplica seis leyes de la comunicación con una herramienta real —`Herramientas/legibilidad.py`— que prueba contraste WCAG, simulación de daltonismo, consistencia de mapping, feedback, navegación y densidad. **Un `UXS` no cierra sin estar medido.**

Usabilidad primero, engagement después. No define reglas ni balance —dice cuántos estados se pueden distinguir, no cuáles existen— ni diseña el espacio jugable.

### [[Area_programacion]]

Convierte un `RQ` (+ `GDS`, `LDS`, `UXS`) en una solución técnica construida con criterio Vaultrum. Produce `SOL` (solución técnica) + `EJ` (ejecución). Sus sub-agentes iteran hasta cumplir los criterios de aceptación.

### [[Area_control_de_calidad]]

**El último paso de la cadena, y el único que puede decir que no.** Corre al terminar una épica —una implementación específica o la entrega completa— y decide si lo construido **se sostiene**: build verificada, pase por riesgo, defectos reproducibles, arreglos reverificados, regresión corrida y cobertura declarada.

Produce `QA`, con dos cortes: `QA-XXX.n` cierra un hilo y cuelga de su `EJ`; `QA-XXX` cierra la entrega y cuelga del `TL`, sin `.n`. Su salida es una decisión de tres valores —**GO · CONDITIONAL GO · NO-GO**— y es **insumo obligatorio del `VE`**.

Entra **dos veces**, como UI/UX y por la misma razón: antes, con el presupuesto de verificación —qué instrumentación hace falta para que esto se pueda probar—, dicho mientras todavía se puede construir; y después, con el gate, sobre una versión congelada. Un gate que solo aparece al final descubre problemas estructurales cuando ya son caros.

Aplica seis leyes de la verificación con una herramienta real —`Herramientas/calidad.py`— que mide versión congelada, verificación de build, trazabilidad del defecto, reverificación, cobertura sin huecos y riesgo con dueño, y compara el veredicto declarado contra el medido. **Un `QA` no cierra sin estar medido.**

No arregla lo que encuentra, no revisa arquitectura ni estilo de código, y no valida la experiencia: eso sigue siendo del `VE` y del playtest.

### [[Area_conocimiento]]

**La memoria de la Agencia.** No produce proyecto: cuida que lo que se trabaja quede escrito y se entienda, y decide qué de lo trabajado vuelve al Core.

**Tampoco está al final de la cadena: está debajo, como Arquitectura.** Entra tres veces y no una. **Copiloto** acompaña a un área mientras escribe su artefacto —asiste, no firma: la autoría y el estado de cierre siguen siendo del área dueña—. **Gate** mide el artefacto contra su contrato antes de cerrarlo, y corre solo, porque el que se olvida de documentar se olvida de pedir ayuda para documentar. **Cosecha** decide qué aprendizaje vuelve a `main`, sobre la evidencia de lo trabajado y no sobre memoria.

Mide con `Herramientas/documentacion.py`, que prueba seis leyes de la documentación —insumo declarado, contrato completo, omisión declarada, ningún número sin fuente, lo terminado existe en disco, no se dice dos veces—. **Un artefacto no cierra sin estar medido.**

Sigue siendo la única que propone cambios a `main`, con el modelo de siempre: Core = `main`, proyecto = `branch`, aprendizaje = `commit`, entrar al Core = `merge` con aprobación. Es una metáfora de versionado: **el commit del repositorio no es de esta área** — la política vive en `04_IA Operativa/03_Operar Vaultrum` y el cierre que lo habilita es el `VE` de Producción.

**Dos áreas están debajo de la cadena, no adentro.** Ninguna produce proyecto y ninguna aparece en la columna vertebral de numeración; las dos sostienen a las demás antes de que construyan:

```txt
Arquitectura   la forma del VAULT   dónde vive, de qué índice cuelga, con qué aristas
Conocimiento   la forma del TEXTO   si se entiende, si falta algo, si está dicho dos veces
               y la PERTENENCIA     a qué cuerpo de conocimiento pertenece lo nuevo
```

La frontera entre las dos es dura: **el arquitecto decide dónde vive una nota; Conocimiento decide a qué pertenece y cómo está escrita.** Conocimiento nunca coloca una nota por su cuenta: pide el emplazamiento y lo cita. Arquitectura nunca escribe el cuerpo.

### [[Area_arquitectura]]

Cuida la **forma** del vault, no su contenido: que se pueda entrar por un índice y llegar caminando a cualquier nota.

**No está al final de la cadena: está debajo de todas.** No recibe el trabajo de nadie y no se lo entrega a nadie — le presta forma a quien la va a necesitar, antes de que construya. Presta tres servicios: **Plano** (explica en cascada cómo hacer algo sin romper ley), **Emplazamiento** (decide dónde vive el contenido nuevo y coloca la estructura) y **Pasada** (mide, repara y verifica lo que ya está).

La regla que la activa: **cualquier área que vaya a crear, mover o purgar notas, índices o carpetas le pide el plano o el emplazamiento antes de tocar nada, y lo cita en su salida.** Editar el cuerpo de una nota que ya existe no la activa: el área se ocupa de la forma, no del texto.

Qué existe lo decide el área dueña; **dónde vive lo decide el arquitecto**, y es vinculante. El cuerpo de la nota nunca es suyo.

Sus salidas (`ARQ`) no cuelgan de la columna vertebral de numeración: no son un eslabón de la cadena de producción, son intervenciones sobre el vault mismo. Cada una declara su modo.

---

## [[00_Escuela|Vínculo con la Escuela (05_Escuela)]]

La **Escuela** **no es un área de la Agencia**: es una capa propia. Comparte estructura (tiene `Agentes/`, `Flujos/`, `Salidas/`, `Skills/`) porque también es un lugar donde se trabaja, pero trabaja sobre otra cosa:

- La **Agencia** produce **el proyecto del usuario**. Su insumo es una intención; su producto son `TL/RQ/GDS/LDS/UXS/SOL/EJ/QA/VE`.
- La **Escuela** produce **conocimiento para el sistema**. Su insumo es un gap del Core; su producto son libros en la Biblioteca y candidatos `EST`.

Por eso no cuelga de la columna vertebral de numeración de arriba: sus salidas no son un eslabón de la cadena de producción. La Agencia se conecta con ella de dos formas:

- **Producción, Game Design, Level Design y UI/UX** la **consultan on-demand** en tiempo de diseño (vía el índice por género del Core y el libro `05_Fundamentos_de_experiencia_ludica`) para que la primera entrega sea sólida, no un MVP apurado.
- **Conocimiento** es el **puente de gobernanza**: recibe los candidatos `EST` de la Escuela y es el único que los propone a `main`.

---

## Roles fuera de las áreas

No hay ninguno: los siete roles del modelo anterior fueron absorbidos por las áreas. Si hace falta un rol que ninguna área cubra, se crea en ese momento y con su área.

---

## Regla final

La Agencia no dirige al Core.

La Agencia usa el Core.

Primero criterio. Después área. Después salida registrable.

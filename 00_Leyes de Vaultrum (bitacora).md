# Leyes de Vaultrum — Bitácora

> Registro de conceptos e ideas que van a convertirse en leyes del Core.
> Cada vez que hablemos de "leyes de Vaultrum", se anota acá la idea antes de formalizarla.
>
> **Una idea sale de esta bitácora cuando entra al Core.** Lo que queda acá es lo que todavía no se formalizó. Lo formalizado se marca con su destino y deja de crecer acá: el Core es la fuente, esto es la sala de espera.

## Estado

| # | Idea | Estado | Dónde vive ahora |
|---|------|--------|------------------|
| 1 | Fricción mínima y baseline competente | **MERGEADA** | Baseline de entregable (mitad 1) |
| 2 | La Escuela Vaultrum | **CONSTRUIDA** | `05_Escuela/` |
| 3 | Optimizar sin requerimiento es scope no pedido | **MERGEADA** | Baseline de entregable (mitad 2) + Cuando NO optimizar |
| 4 | Verificación parcial declarada | **MERGEADA** | Verificacion parcial declarada |
| 5 | Backlog de mejoras del sistema | **abierto** (parcialmente cerrado) | acá abajo |
| — | La cadena falla en los bordes | **MERGEADA** | Gates verificables + 3 skills |

Las cuatro mergeadas viven en la sección nueva del Core `01_VaultrumCore/.../04_Criterios de entrega/`. Fue el primer ciclo `Core → Agencia → Conocimiento → Core` que cerró completo.

---

## Ley candidata #1 — Fricción mínima y baseline competente

**Origen:** desarrollo del Pong3D (vaultrumtest1). El juego terminó en 7/10 (buena primera prueba real), pero el *desarrollo* recibió 4/10. Motivo: hicieron falta demasiados prompts para lograr algo tan básico como un Pong. La fricción fue el problema, no el código.

**Idea central:**
El costo del usuario en Vaultrum se mide en **prompts**. Vaultrum existe para que Ignacio desarrolle *su* idea de la forma más sencilla posible. Por lo tanto:

1. **Vaultrum carga por defecto los fundamentos conocidos de cada entregable** ("lo básico bien hecho"). El usuario no debería tener que pedir las *table-stakes* de un tipo de entregable — un juego no está terminado sin input → feedback → objetivo → victoria/derrota → juice; un menú no sirve sin EventSystem; etc.
2. **Los prompts del usuario se reservan para lo que es genuinamente suyo:** su idea, su criterio, su visión. No para completar lo que cualquier baseline competente ya debería traer.
3. Cuando yo (la IA) entrego lo mínimo funcional en vez de lo mínimo *satisfactorio*, obligo al usuario a gastar prompts en trabajo remedial. Eso mata la experiencia.

**Reframe (posible núcleo de la ley):**
Vaultrum es, en el fondo, una **experiencia lúdica** — no un videojuego, sino algo que se disfruta ejecutar. Y lo mejor: mientras la usás, estás desarrollando tu propia idea. Si Vaultrum es un juego, entonces la fricción es "mal game feel". El sistema mismo necesita *juice*: bajo costo de input, defaults competentes, resultados satisfactorios de entrada.

**Gap detectado en el Core:**
El VaultrumCore es muy rico en *ingeniería* (SOLID, patrones, managers, optimización, algoritmos) pero muy pobre en **fundamentos de experiencia** — lo básico de los primeros años de la carrera: qué hace que algo *sea* una experiencia (el loop, el feedback, el game feel, el "definición de terminado"). El Core sabe construir código limpio, pero no sabe todavía qué se *siente* como "bueno" por default.

**Propuesta de módulo nuevo en el Core:**
Un área de **Fundamentos de Experiencia / Definición de Terminado** — un baseline que todo entregable debe cumplir antes de considerarse hecho, para que la IA complete lo conocido sin que haga falta pedirlo, y el usuario gaste sus prompts solo en su visión.

**Estado:** **MERGEADA AL CORE.** Formalizada como `Baseline de entregable` (mitad 1: *completo en experiencia*), en `01_VaultrumCore/.../04_Criterios de entrega/`. Su prueba mecánica —cobertura *table-stake → RQ*— es un paso ejecutable de `vaultrum-produccion`.

El gap del Core que esta ley detectó también se cerró: existe la sección `Experiencia de juego`, que indexa los fundamentos y los libros por género de la Biblioteca, y `03_Definicion_de_terminado` ya está escrito.

---

## Concepto #2 — La Escuela Vaultrum (área de estudio y aprendizaje en la Agencia)

**Origen:** derivado de la Ley #1. Si falta un módulo de *Fundamentos de Experiencia*, alguien tiene que producirlo. Idea de Ignacio: un área/agente que estudie proactivamente.

**Idea central:**
Un área nueva en la Agencia — la **Escuela Vaultrum** — dedicada a **aprendizaje proactivo**: un agente que estudia, busca libros/fuentes, y rastrea videojuegos y conceptos que todavía NO están en el software, para nutrir el Core.

**Distinción clave con el área de Conocimiento (ya existente):**
- **Conocimiento** = aprendizaje *reactivo*. Cosecha aprendizajes de los proyectos propios ya cerrados (git: proyecto=branch, aprendizaje=commit).
- **Escuela** = aprendizaje *proactivo*. Sale al mundo a buscar lo que falta, sin esperar a que un proyecto lo genere.
- Ambas alimentan el mismo flujo: Staging → **aprobación del owner** → merge al Core. El owner (Ignacio, "el timón del barco") decide qué entra. Consistente con el modelo de gobernanza que ya existe.

**Producto real (reframe importante):**
No es "una lista de 500 juegos". El activo valioso es una **librería de fundamentos de experiencia**: por cada tipo de juego/experiencia, sus *table-stakes* y su *juice* destilados (el loop, el feedback, qué lo hace divertido), indexados para que cuando Ignacio pida "hacé un X", la IA traiga el baseline de X sin que haga falta pedirlo. El catálogo de juegos es la materia prima; los fundamentos destilados son lo que baja el costo en prompts.

**Guardrails a definir (riesgos):**
- **Uso de tokens acotado por misión**, no "hasta que se gasten". Cada corrida de estudio arranca con un *gap* concreto (ej: "fundamentos de game feel"), un presupuesto, y una barra de calidad. Sin eso, se acumula ruido — justo lo que AiCare combate (acumulación/duplicación).
- **Pasada de deduplicación** contra el Core antes de proponer algo nuevo.
- **IP / fuentes:** capturar *conceptos y principios destilados + citas de la fuente*, NO texto verbatim de libros con copyright.
- **Verificabilidad:** la Escuela entrega entradas destiladas y citadas, no dumps crudos. Si no, el Core se infla y el baseline empeora.

**Estado:** DISEÑADA (v1). La Escuela quedó como **capa propia** (`05_Escuela/`), no como área de la Agencia. Comparte estructura con un área —tiene `Agentes/`, `Flujos/`, `Salidas/`, `Skills/`, porque también es un lugar donde se trabaja— pero el criterio que las separa es **sobre qué trabajan**: la Agencia produce el proyecto del usuario, la Escuela produce conocimiento para el sistema. Por eso las salidas `EST` no cuelgan de la columna vertebral `TL → RQ → GDS → ...`. Documento del área: `05_Escuela/00_Escuela.md`.

**Pendiente AiCare — RESUELTO.** El diagnóstico era correcto: AiCare decía "medir" y estimaba. Ahora hay contador: `04_IA Operativa/Herramientas/contar_contexto.py`, que mide el peso del vault por capa, los archivos más pesados, el costo de una carga concreta contra un presupuesto, y el diff antes/después de podar. Cuenta exacto si hay tokenizador instalado y aproxima con margen declarado si no — y **dice siempre en qué modo contó**.

Lo que el contador no mide, y queda declarado en vez de omitido: el consumo real de la ventana del modelo, el historial y las salidas generadas. Mide el material del vault que se carga, que es la parte que Vaultrum controla.

Decisiones clave: (1) la Escuela NO mergea al Core — entrega candidatos `EST` a Conocimiento, que sigue siendo la única que propone a `main`; (2) AiCare es obligatorio en los bordes de cada misión (seguro de vida contra la acumulación); (3) toda misión es acotada por gap + presupuesto + barra de calidad; (4) el producto es una librería de fundamentos destilados, no un catálogo de juegos.
Pendiente cerrado: los `Agentes/` y `Flujos/` están escritos y la Escuela produjo cinco misiones (`EST-001` a `EST-005`), 29 fuentes catalogadas y cuatro libros reales. La primera misión propuesta —llenar los Fundamentos de Experiencia— se cumplió con `EST-004` y `EST-005`.

**Pendiente nuevo, de la auditoría (H1):** la Escuela tiene checklists operativos fuera de su `SKILL.md` (15 ítems en tres archivos). Incumple la regla de capas que la Agencia sí cumple. Ver `00_Auditoria de arquitectura`.

---

## Ley candidata #3 — Optimizar sin requerimiento de performance es scope no pedido

**Origen:** contraste entre una corrida técnica de Pong hecha fuera de Vaultrum y la cadena completa del `TL-003_Pong3D_Unity6_Cadena_Completa`. La corrida suelta produjo ingeniería excelente —loop con accumulator a 120 Hz e interpolación, CCD propio, cero asignaciones, un solo `Update`, batching y culling ajustados— para un problema en el que **nadie había pedido performance ni determinismo**. Ocho decisiones, todas técnicas, cero sobre la experiencia.

**Idea central:**
En Vaultrum el presupuesto del usuario se mide en prompts (Ley #1) y el de la IA en foco. Una decisión de ingeniería que no responde a un requerimiento consume ese presupuesto igual que una feature que nadie pidió. Es *scope no pedido*: trabajo de calidad, sin encargo.

La regla utilizable **no** es "no optimices". Es más chica y más operable:

> **No enciendas maquinaria que ningún requerimiento pidió — y eso incluye la maquinaria propia.**

Apagar PhysX en un Pong es correcto *si* el motivo es que el rebote de Pong no es físico (una regla de diseño), no *si* el motivo es el costo de la broadphase. El mismo código, justificado contra un `RQ` en vez de contra un principio, deja de ser scope no pedido.

**Prueba práctica para aplicarla:** por cada decisión técnica, escribir la línea *"esto existe porque el requerimiento X pide Y"*. La que no la tenga, o se declara como deuda con su motivo, o no se hace. `SOL-003` la aplica con una tabla explícita de **lo que se hizo** y **lo que deliberadamente no se hizo**.

**Relación con la Ley #1:** son la misma ley vista desde los dos lados. La #1 dice que la IA debe traer sin pedirlo lo que un entregable necesita para *ser satisfactorio*. La #3 dice que no debe traer sin pedirlo lo que nadie necesita. Juntas definen el baseline: **completo en experiencia, mínimo en maquinaria.**

**Estado:** **MERGEADA AL CORE.** Formalizada como `Baseline de entregable` (mitad 2: *mínimo en maquinaria*) y desarrollada para rendimiento en `Cuando NO optimizar`, que quedó como hermana de `Medir antes de optimizar` en Fundamentos de Optimización.

La distinción que aporta al Core: *optimización prematura* es optimizar sin medir; *optimización no pedida* es optimizar sin encargo. Medir corrige la primera y no corrige la segunda. La prueba —la tabla de **lo que se hizo** / **lo que deliberadamente no se hizo**— es obligatoria en toda `SOL`.

---

## Concepto #4 — Verificación parcial declarada

**Origen:** `EJ-003_Implementacion_Pong3D`. `VE-002` había quedado PAUSADO con el diagnóstico *"verificar el código no es verificar la entrega"*, que es correcto pero deja un hueco: entre "no se verificó nada" y "se jugó una partida" hay terreno útil.

**Idea central:** una entrega puede verificarse **parcialmente** sin el entorno de destino, siempre que la verificación declare su alcance. En `EJ-003` los 17 scripts se compilaron fuera de Unity contra un stub de la API: cerró la clase entera de errores de sintaxis, tipos y firmas, sin poder abrir el editor. No convierte un PAUSADO en Cerrado — pero convierte *"no sabemos nada"* en *"sabemos esto y no aquello"*.

**Regla propuesta:** toda verificación que no sea la del gate declara qué cubre **y qué no**, en el mismo párrafo. Una verificación sin alcance declarado se lee como cierre y produce el falso Cerrado que los `VE` existen para evitar.

**Estado:** **MERGEADA AL CORE** como `Verificacion parcial declarada`, con formato obligatorio de declaración (Método / Cubre / No cubre / Consecuencia) en el `EJ`.

El corolario también se formalizó: el juicio global del owner es un modo de cierre legítimo del `VE` —**modo Veredicto**— con sus condiciones y su deuda declarada. Ver `00_Indice_ve`.

---

## Ley candidata #6 — El grafo se recorre por índices, no por asociación

**Origen:** el owner miró el grafo de Obsidian y vio que el Core se recorría en cascada y el resto del vault era una telaraña. La medición confirmó lo que se veía: el Core tenía 89% de sus aristas bajando un escalón; la Biblioteca, 48% laterales y 43% de sus links a mitad de una frase.

Lo que apareció al medir es que **el Core ya cumplía una ley que nunca se había enunciado**. Seis reglas, leídas de su comportamiento:

```txt
1. El link es el título de la sección     ## [[Hijo]] + prosa debajo
2. Cascada de un solo escalón             un índice enlaza a sus hijos directos
3. La hoja no linkea: sale                ## Hacia donde seguir, o nada
4. La prosa nombra con backticks          mencionar no es enlazar
5. Un puente por capa, declarado          y la nota dice que es el puente
6. Cero aristas invisibles                nada en frontmatter ni en tablas
```

Con dos corolarios: **nada flota** (toda nota cuelga de un índice) y **la cadena sí puede cruzar de rama** (una salida declara su insumo directo, una línea por documento).

El hallazgo que habilitó aplicarla: **ninguna de las skills navega por wikilink** — todas resuelven por ruta. El grafo es para el owner, no para la máquina. Por eso se pudo podar de 1.504 links a 572 sin tocar el funcionamiento de nada.

**Estado:** FORMALIZADA fuera del Core, en `02_Agencia/Area arquitectura/`, con herramienta de medición y gate ejecutable. Candidata a merge al Core por la vía del Área de Conocimiento, con aprobación del owner. Mientras tanto vive donde se aplica.

---

## Concepto #5 — Backlog de mejoras del sistema

**Origen:** cierre del `TL-003_Pong3D_Unity6_Cadena_Completa` (jugado por el owner, 8/10, divertido). Lo que sigue **no** son aprendizajes para el Core —esos ya están mergeados, ver la tabla de estado arriba— sino mejoras al sistema mismo.

### Sobre la cadena de la Agencia

1. ~~**Convertir las tres reglas de borde en pasos de skill.**~~ **HECHO.** Las tres son ahora procedimiento ejecutable:
   - *entrada* → gate de insumo de Biblioteca en `vaultrum-produccion`: si el libro del género no existe o está vacío, PAUSADO y derivación a Escuela. Con prueba de cobertura *table-stake → RQ* registrada en el `TL`.
   - *ramas opcionales* → gate del "no aplica" en `vaultrum-gamedesign`: hay que declarar qué dimensión falta y por qué, con formato mínimo. El **test del "no aplica"** (¿la siguiente área tuvo que hacerlo igual?) se corre al cerrar el `VE`.
   - *salida* → gate de existencia en disco en `vaultrum-programador`: listado archivo por archivo antes de reportar el `EJ`.

   El criterio de fondo quedó en el Core como `Gates verificables`: *un gate que no se puede verificar mecánicamente no es un gate, es una intención.*

2. ~~**`GDS-003.0` inventó un artefacto sin nombre.**~~ **FORMALIZADO.** El `GDS-XXX.0` es ahora parte de la columna vertebral, con condiciones: se abre solo si **tres o más** `GDS` del timeline comparten definiciones, contiene solo lo compartido, cuelga del `TL` y no de un `RQ`, y los demás lo referencian sin copiarlo. Con dos `GDS` se repite y listo — un marco común para dos specs es sobrearquitectura.

   Queda escrito además cuáles son los **únicos dos** artefactos que cuelgan del `TL`: `GDS-XXX.0` y `VE-XXX`. Cualquier otro sin `RQ` upstream es un hueco, no una excepción.

3. **El CHECKLIST de 9 pilares es largo para un `GDS` chico.** *Abierto.* Correrlo seis veces en un Pong produjo mucho `N/A con justificación` legítimo pero repetitivo. Evaluar si el Fundamento 05 debería ofrecer un subconjunto por tamaño de sistema, o si la repetición es el precio correcto de no dejar huecos.

   *Dato nuevo:* ahora que existe el `GDS-XXX.0`, parte de esa repetición tiene dónde ir — los pilares que aplican igual a todos los sistemas del timeline pueden resolverse una vez en el marco común. Probarlo en `TL-004` antes de tocar el Fundamento.

4. ~~**`VE` cerrado por juicio global.**~~ **FORMALIZADO.** El `VE` tiene ahora dos modos de cierre declarados: **Checklist** (se recorren los ítems sobre el entregable corriendo) y **Veredicto** (juicio global del owner sobre el entregable corriendo). Los dos son válidos, los dos son verificaciones parciales, y el `VE` declara cuál usó más la deuda que deja. El modo veredicto solo lo emite el owner, nunca desde el código. Ver [[00_Indice_ve]].

### Sobre la Escuela y la Biblioteca

5. ~~**`01_Pong` está *En validación*, no *En la Biblioteca*.**~~ **CERRADO.** Handoff hecho, libro promovido a *En la Biblioteca*. Y quedó escrita la regla que faltaba: **un libro solo es insumo válido de producción cuando está *En la Biblioteca***. Un libro *En estudio* o *En validación* es material en curso, y Producción lo rechaza en su gate de insumo.

6. ~~**`01_Loop_de_experiencia` sigue *En estudio*.**~~ **CERRADO.** Escrito con el material de Pong: los tres loops anidados, juego vs juguete (objetivo impuesto + obstáculo innecesario), dónde vive la tensión, y seis table-stakes transversales. Efecto colateral: `03_Definicion_de_terminado` también se escribió, porque `vaultrum-produccion` dependía de un libro *Reservado*.

7. **La Biblioteca tiene 29 fuentes catalogadas y un solo juego.** *Abierto.* El estante de Juegos escala de a un `EST` por género. Definir el orden (Breakout, plataformero, shmup…) o dejarlo bajo demanda.

   *Criterio sugerido:* que lo decida la segunda muestra. Si `TL-004` es un plataformero, el libro de plataformero se escribe antes del `RQ` — que es exactamente lo que el gate de insumo obliga a hacer.

### Sobre el proyecto vaultrumtest2

8. **Mejoras del juego pendientes de detallar por el owner.** *Abierto.* Entran por Producción como `TL-004`, no reabren `VE-003`.

9. **Deudas técnicas declaradas en `EJ-003`.** *Abiertas.* La cuenta de saque muestra `SAQUE` en vez de un número (revisar si `serveDelay` sube de 2 s); `ProjectSettings.asset` queda en defaults de Unity; sin `EventSystem` ni soporte de mouse en menús (decisión declarada en `UXS-003.5`).

10. **Confirmar la versión de Unity.** *Abierto.* `ProjectVersion.txt` quedó en `6000.0.81f1` como supuesto declarado del `TL-003`.

### Auditado

11. ~~**Arquitectura del sistema Vaultrum.**~~ **AUDITADA.** Ver [[00_Auditoria de arquitectura]] (AUD-001). Desde entonces la auditoría tiene área propia (`Area arquitectura`), herramienta de medición y serie `ARQ`.

    Resultado corto: la sospecha de duplicación entre `Area_*.md` / `Agentes/` / `Flujos/` / `Skills/` **no se confirmó** —9 frases repetidas en 24 archivos, y los 6 checklists de la Agencia viven solo en sus skills—. Los índices están sincronizados con el disco (54 de 54 salidas) y los wikilinks resuelven.

    Lo que sí apareció: la **Escuela** incumple la regla de capas (H1, abierto), **Conocimiento** no tiene `Salidas/` sin declararlo (H2, corregido), el Core y la Escuela se contradecían sobre si el Core enlaza hacia abajo (H3, corregido), el índice de IA Operativa no listaba `05_Modo_Operacion` (H4, corregido), y el ciclo de conocimiento nunca había cerrado (H5, corregido).

### Abierto, sin asignar

12. **Segunda muestra en un dominio distinto.** Todo lo validado se validó sobre Pong, tres veces. `LDS` nunca corrió. La cadena ya crujió una vez en esa única muestra (`GDS-003.0`), lo que sugiere que hay más por descubrir. Un plataformero activa `LDS`; un entregable que no sea un juego prueba si la cadena es un método o un método para hacer arcades. Las dos respuestas sirven.

13. **Medir la fricción de verdad.** El instrumento existe ([[06_Medicion de friccion]]): prompts clasificados en visión / aclaración / remedial, registrados en el `VE`. Ninguna entrega anterior está medida con él —`TL-002` y `TL-003` son impresiones, no datos—. **`TL-004` es la primera que puede tener un número real.**

14. **Resolver la tensión abierto / monousuario.** Gobernanza completa, licencia GPL, política de marca y scoreboard, con `CONTRIBUTORS.md` de 408 bytes; y al mismo tiempo un `Modo Owner` protegido por passphrase, que es un diseño de una sola persona. No es un defecto de arquitectura: es una decisión de dirección sin tomar. Cambia qué es el Core para alguien que no es Ignacio.

15. **Promover la regla de capas fuera del índice de la Agencia.** Hoy vive en `02_Indice Agencia.md` y por eso la Escuela no la cumple: está escrita donde la Escuela no la lee. Mientras siga ahí, cada capa nueva la va a volver a incumplir.

**Estado:** backlog abierto. Cerrados: 1, 2, 4, 5, 6, 11. Abiertos: 3, 7, 8, 9, 10, 12, 13, 14, 15.

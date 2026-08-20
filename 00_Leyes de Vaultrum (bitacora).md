# Leyes de Vaultrum — Bitácora

> Registro de conceptos e ideas que van a convertirse en leyes del Core.
> Cada vez que hablemos de "leyes de Vaultrum", se anota acá la idea antes de formalizarla.

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

**Estado:** idea capturada, pendiente de formalizar y mergear al Core (branch → merge con aprobación del maintainer).

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

**Pendiente AiCare (detectado al probarlo, para que pueda cuidar la Escuela):** AiCare funciona como criterio (mide→diagnostica→poda→valida) y detecta bien acumulación/duplicación/recarga, pero hoy "medir" es *estimar*, no contar — no tiene telemetría real de tokens. Antes de confiarle cortes duros de presupuesto en las misiones de la Escuela, hay que darle una **medición real de tokens** (de dónde saca el número). Como red de seguridad contra la acumulación ya sirve; como contador exacto, todavía no.


Decisiones clave: (1) la Escuela NO mergea al Core — entrega candidatos `EST` a Conocimiento, que sigue siendo la única que propone a `main`; (2) AiCare es obligatorio en los bordes de cada misión (seguro de vida contra la acumulación); (3) toda misión es acotada por gap + presupuesto + barra de calidad; (4) el producto es una librería de fundamentos destilados, no un catálogo de juegos.
Pendiente: aprobación del owner + escribir los `Agentes/` y `Flujos/` del área. Primera misión propuesta: llenar el módulo de *Fundamentos de Experiencia* (Ley #1).

---

## Qué es Vaultrum

**Vaultrum** es un sistema de desarrollo asistido por IA con **trazabilidad obligatoria**, orientado a videojuegos, software y sistemas creativos.

Su objetivo es ayudar a pensar mejor, decidir mejor, construir mejor y documentar mejor. Y sostenerlo: que al terminar quede escrito qué se decidió, por qué, qué se descartó y qué falta.

Vaultrum no busca acumular contenido por cantidad.

Busca transformar conocimiento en criterio operativo.

---

## Las dos cosas que hacen a Vaultrum

Todo lo demás se apoya en estas dos.

### 1. La regla del baseline

> **Completo en experiencia, mínimo en maquinaria.**

Dos mitades que parecen opuestas y son la misma:

- **Completo en experiencia** — las *table-stakes* de un entregable no se piden, se incluyen. Un juego no está terminado sin input → feedback, objetivo claro, victoria/derrota, estados y reinicio. El owner gasta sus pedidos en su idea, no en completar lo que cualquier versión competente ya debería traer.
- **Mínimo en maquinaria** — no se enciende maquinaria que ningún requerimiento pidió. Una optimización sin encargo consume el mismo presupuesto que una feature que nadie pidió.

Criterio completo: `Baseline de entregable`.

### 2. La cadena con gates

```txt
Intención
  ↓
TL + RQ      (Producción)      qué se hace, con qué alcance
  ↓
GDS          (Game Design)     reglas, estados, feedback, balance
  ↓
LDS / UXS    (Level Design / UI-UX, si aplican)
  ↓
SOL + EJ     (Programación)    solución técnica + implementación
  ↓
QA           (Control de Calidad)  ¿lo construido se sostiene? con evidencia
  ↓
VE           (Producción)      ¿lo entregado es lo prometido?
  ↓
commit al Core (Conocimiento)  ¿qué aprendizaje vuelve al sistema?

(Conocimiento entra además ANTES: acompaña a cada área mientras escribe,
 y mide el artefacto contra su contrato antes de dejarlo cerrar.)
```

**Un artefacto downstream no existe sin su insumo upstream.** Si falta, se marca y no se avanza. Eso es lo que impide saltear pasos, y lo que hace que una entrega no se dé por terminada porque compila — ni porque alguien la probó un rato.

Detalle de la cadena, la numeración y los gates: `02_Indice Agencia`.

---

## Modo de operación de la IA

Al cargar Vaultrum como contexto, el asistente arranca en **Modo Vaultrum**: software asistente para la creación, con puerta de entrada en el **Productor** (Área de Producción), que pivotea entre áreas según haga falta.

Existe además un **Modo Owner**, protegido, para modificar el sistema mismo. Ambos modos y el procedimiento del switch están en `05_Modo_Operacion`.

---

## Arquitectura general

```txt
01_VaultrumCore     el conocimiento y el criterio
      ↓
02_Agencia          la cadena que lo aplica al proyecto del usuario
      ↓
03_Comunidad        quiénes lo usan y aportan, y cómo se cuenta hacia afuera

04_IA Operativa     transversal: cómo una IA opera el vault sin inflarlo
05_Escuela          transversal: aprendizaje proactivo y la Biblioteca
```

- **01_VaultrumCore** es la fuente de criterio. Alimenta el arranque de cada área y recibe de vuelta lo aprendido.
- **02_Agencia** produce **el proyecto del usuario**.
- **03_Comunidad** usa, aporta, corrige y expande — y prepara lo que el sistema publica.
- **04_IA Operativa** cuida el costo de operar: tokens, prompteo, el pass GC y sus herramientas de medición.
- **05_Escuela** produce **conocimiento para el sistema**: sale a buscar lo que al Core le falta y lo trae destilado a su Biblioteca.

---

## [[01_Indice VaultrumCore|01_VaultrumCore]]

Es el corazón. Contiene principios, criterios, patrones de diseño, arquitectura, optimización, IA para juegos, estructuras de datos, algoritmos, managers y material reutilizable.

Y desde el primer ciclo completo, dos secciones que antes no tenía:

- **Criterios de entrega** — cuándo algo está terminado: `Baseline de entregable`, `Verificacion parcial declarada`, `Gates verificables`. Es la única parte del Core que nació del uso del propio sistema.
- **Experiencia de juego** — el índice liviano hacia la Biblioteca de la Escuela: `Experiencia de juego`.

VaultrumCore no ejecuta y no resuelve proyectos: **alimenta**. Se puede usar directo, sin pasar por ningún flujo.

Entrada: `01_Indice VaultrumCore`

---

## [[02_Indice Agencia|02_Agencia]]

La capa operativa. **Ocho áreas** —seis en la cadena, y Conocimiento y Arquitectura debajo de ella—, cada una autocontenida: trae sus sub-agentes, su método, su producto y su skill ejecutable. La salida de una es la entrada de la siguiente.

| Área | Produce | Responde |
|------|---------|----------|
| Producción | `TL` + `RQ` … y `VE` al cerrar | qué se hace, con qué alcance, y si lo entregado es lo prometido |
| Game Design | `GDS` | reglas, estados, feedback, balance |
| Level Design | `LDS` | espacio, encuentros, pacing, dificultad aplicada |
| UI/UX | `UXS` | pantallas, HUD, navegación, legibilidad |
| Programación | `SOL` + `EJ` | cómo se implementa y qué se implementó |
| Control de Calidad | `QA` | si lo construido se sostiene: GO / CONDITIONAL GO / NO-GO |
| Conocimiento | documentación medida + commits al Core | si lo escrito se entiende, y qué aprendizaje vuelve a `main` |
| Arquitectura | `ARQ` | dónde vive cada nota y si el vault se puede recorrer |

El hilo es de **Producción de punta a punta**: lo abre con la intención y lo cierra validando la entrega. Nada avanza sin su insumo, y nada se da por terminado porque compile.

**Los bordes son donde falla.** El medio de la cadena funciona; la evidencia dice que fallan la entrada, las ramas opcionales y la salida. Las tres reglas que lo corrigen ya son pasos ejecutables de las skills, no criterio escrito. Detalle en `02_Indice Agencia`.

---

## [[03_Indice Comunidad|03_Comunidad]]

La capa humana y pública: quién usa, estudia, adapta, corrige, propone o expande el sistema, bajo qué criterios y con qué límites.

Y desde que también trabaja, la que **prepara lo que Vaultrum muestra hacia afuera**: cuatro sub-agentes, cuatro flujos, salidas `PUB` y su propio Archivo de lo publicado. Se dispara solo a pedido del owner.

Entrada: `03_Indice Comunidad`

---

## [[04_Indice IA Operativa|04_IA Operativa]]

Cómo una IA opera el vault sin inflarlo: cuidado de tokens, prompteo, modo de operación y la pasada de GC de contexto.

---

## [[00_Escuela|05_Escuela]]

La capa proactiva: la Biblioteca y las misiones de estudio que la llenan. El Core indexa; el peso vive acá y se carga on-demand.

---

## `06_Proyectos` — los proyectos

Lo que Vaultrum produce **no vive adentro de las areas**. Un area es el edificio donde se trabaja; el proyecto es lo que se produjo, y lo producido no se guarda en la oficina que lo hizo.

```txt
01_VaultrumCore    el criterio          el sol
02_Agencia         como se trabaja      los edificios
06_Proyectos       lo que se produjo    las estrellas
```

Cada proyecto trae su cuaderno en la raiz y sus artefactos en carpetas por area: `01_Produccion/`, `02_GameDesign/`, `03_LevelDesign/`, `04_UI-UX/`, `05_Programacion/`, `06_Calidad/`. La carpeta existe si un area escribio algo ahi; nada se pre-crea.

**Esa carpeta no se versiona.** Quien clona Vaultrum recibe el sistema y sus funcionalidades, no el historial de uso de otro. Por eso se nombra con backticks y no se enlaza: en una copia recién clonada esta carpeta no existe, y un link colgado en la puerta es peor que una mención. Es la única excepción declarada del grafo, registrada en `excepciones.txt`.

Detalle de la regla: `TL-008_La_Agencia_Es_La_Empresa`.

---

## Formas de usar Vaultrum

### Uso libre

Entrar al Core, leer, tomar criterio y aplicarlo en un proyecto propio. Sirve para estudiar conceptos, revisar patrones, comparar decisiones técnicas o usar el vault como fuente de consulta.

### Uso asistido

Partir de una necesidad y dejar que la Agencia la convierta en un entregable, atravesando la cadena. Sirve para ordenar una idea, definir alcance, diseñar un sistema, implementarlo y validarlo — dejando el rastro escrito.

Los dos son válidos. Vaultrum no obliga a un único camino.

---

## ¿Solo videojuegos?

La cadena **no** es específica de videojuegos. Lo específico son dos eslabones:

```txt
específico de juegos:   GDS (reglas de gameplay) · LDS (nivel)
general a cualquier software:  TL · RQ · UXS · SOL · EJ · QA · VE
```

Un entregable de software que no sea un juego recorre la misma cadena sin `GDS` ni `LDS`: sus `RQ` van directo a Programación, y `UXS` aplica si tiene interfaz.

Lo que **sí** cambia es el baseline: las *table-stakes* de una herramienta no son las de un juego. En ese caso Producción declara de dónde sale el mínimo —de un libro de la Biblioteca, o fijado por el owner para esa entrega— en vez de improvisarlo.

Advertencia honesta: **esto todavía no se probó.** Todo lo validado se validó sobre un mismo género. Ver `ARQ-000_Auditoria_de_arquitectura`.

---

## Cómo recorrer Vaultrum

```txt
el conocimiento central          → 01_Indice VaultrumCore
la cadena y las áreas            → 02_Indice Agencia
aportar, corregir, gobernanza    → 03_Indice Comunidad
cómo una IA opera el vault       → 04_Indice IA Operativa
la Escuela y su Biblioteca       → 00_Escuela
tus proyectos                    → 06_Proyectos/00_Proyectos  (local)
```

**Lo que no está acá.** Esta puerta lleva al sistema y a sus funcionalidades. El **historial de uso** —auditorías, misiones de estudio, publicaciones, leyes en antesala— vive en el área que lo produjo y no se publica:

```txt
auditorías del vault      → Área de Arquitectura, sus salidas ARQ
leyes por formalizar      → Área de Conocimiento, su Staging
misiones de estudio       → Escuela, sus salidas EST
lo publicado hacia afuera → Comunidad, sus salidas PUB
```

Una puerta que abre a un registro fechado le cuenta a quien llega el pasado del dueño en vez de lo que el sistema hace.

---

## Estado actual

Etapa de apertura inicial, con **una entrega real completa**: la cadena se corrió de punta a punta produciendo un Pong 3D en Unity 6, jugable y jugado por el owner.

Lo que eso probó:

- la cadena produce un entregable que se juega, con trazabilidad completa;
- las table-stakes entran como requerimiento explícito y no como intuición;
- el ciclo de conocimiento cierra: lo aprendido volvió al Core.

Lo que no:

- **una sola muestra.** Un género, sin dimensión espacial, sin persistencia ni contenido. `LDS` nunca corrió.
- **la fricción todavía no está medida.** El instrumento existe (`06_Medicion de friccion`); la primera entrega con número va a ser `TL-004`.

El foco actual está en la segunda muestra y en medir, no en agregar capas.

---

## Regla central

Vaultrum no busca ser grande por tener más contenido.

Vaultrum busca ser útil porque su contenido tiene criterio, estructura y aplicación real — y porque lo que produce queda escrito.

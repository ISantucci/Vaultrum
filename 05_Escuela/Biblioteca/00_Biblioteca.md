# Biblioteca

## Propósito

La Biblioteca es el **corazón de la Escuela**: el espacio donde se guardan los **libros** y donde trabajan sus agentes. Es el activo real de la Escuela — la librería de conocimiento reutilizable que hace que "hacé un X" traiga un baseline sólido sin pedirlo (Ley candidata #1).

No es un catálogo de juegos ni una lista de 500 títulos. Es una colección de **libros** curados, cada uno con índice y metadata, indexados para consultarse por categoría.

Esta nota es la portada. Se ordena como una biblioteca real: **salas por tema**, y en cada sala sus **estantes**. La portada enlaza las salas, cada sala enlaza sus estantes y cada estante enlaza sus piezas y las describe.

---

## La vista de conjunto se calcula, no se mantiene

Cuántas piezas hay, en qué estado están y de qué misión salió cada una **no se escriben a mano**: se derivan del árbol.

```txt
python3 "05_Escuela/Herramientas/biblioteca.py" .                    conteos, por misión, lo que está en curso
python3 "05_Escuela/Herramientas/biblioteca.py" . --dedup <tema>     ¿ya hay algo que cubra esto?
python3 "05_Escuela/Herramientas/biblioteca.py" . --verificar        la ficha y su estante coinciden
```

La fuente de verdad de cada pieza es **su propia ficha**. El estante la enlaza y la describe; todo lo demás se calcula.

Un dato calculado no puede derivar del original, porque no tiene copia. La Biblioteca mantuvo durante meses un catálogo escrito a mano que reflejaba 99 entradas: nunca se desincronizó con los estantes, y aun así ocultó una deriva — la ficha de `01_Pong` decía *En validación* mientras el estante y el catálogo la daban por cerrada. El espejo coincidía con el espejo; nadie miraba el original.

---

## Salas

### [[00_Sala_diseno_de_juegos|Sala de Diseño de juegos]]
La experiencia del jugador: lo transversal (Fundamentos) y lo de cada género (Juegos). La abren Producción y las áreas de diseño antes de cerrar el `GDS`.

### [[00_Sala_ciencias_aplicadas|Sala de Ciencias aplicadas]]
El mecanismo: cómo se construye un juego (Construcción) y cómo es y se mueve el cuerpo humano que el juego anima (Medicina). La abren los agentes que operan herramientas, solo cuando la tarea lo pide.

### [[00_Sala_de_referencia|Sala de Referencia]]
La materia prima: fuentes externas catalogadas (Fuentes) y evidencia primaria de la industria (Documentación real). Se consulta en sala: la usa la Escuela, no la producción.

El orden de las salas es del Arquitecto (`ARQ-036`); la forma en que se escribe cada sala, cada estante y cada libro es del Documentador (`contratos.txt`).

---

## Anatomía de un libro

Cada libro abre con metadata y un índice, para encontrarlo por categoría:

```txt
---
tipo: fundamento | juego
genero: (si aplica) arcade / plataformero / shmup / ...
estado: En estudio | En destilación | En validación | En la Biblioteca | A actualizar
mision: [[EST-XXX_...]]
---

## Índice del libro
## Loop de experiencia        (qué se hace / qué se siente)
## Table-stakes               (lo que NO puede faltar para estar terminado)
## Juice / game feel          (lo que lo hace satisfactorio)
## Definición de Terminado    (checklist accionable)
## Aplicación                 (cuándo la IA lo trae por default)
## Límites                    (cuándo NO aplica)
## Fuentes                    (citas — nunca texto verbatim con copyright)
```

Los libros de **Fundamentos** no llevan `genero`; los de **Juegos**, sí.

Los libros de **Medicina** no siguen esta anatomía: siguen el contrato `MED` del Documentador, porque no se leen para diseñar sino que se cargan para operar una herramienta (ver `00_Indice_medicina`).

Los **documentos** del cuarto estante no siguen esta anatomía: son fichas de artefacto, con su propia metadata (`familia`, `autor`, `anio`, `formato`, `acceso`, `licencia`, `prioridad`, `url`). Ver `00_Indice_documentos`.

---

## Cómo se llena y se cuida

Un libro es el resultado de una **misión de estudio** de la Escuela:

```
[[01_Bibliotecario]] → misión acotada (gap/idea/ambigüedad + presupuesto + barra)
[[02_Investigador]]  → material bruto citado
[[03_Destilador]]    → escribe/actualiza el libro
[[04_Validador_Estudio]] → barra + dedup + AiCare → handoff a Conocimiento
```

La Biblioteca es lo más expuesto a intoxicarse (mucho material, riesgo de duplicar). Por eso **AiCare** vigila los bordes de cada misión y ningún libro se da por bueno sin cita, dedup y aprobación del owner.

---

## Consulta on-demand (tokens)

El Core guarda un **índice por género** que apunta a estos libros. Producción y Game Design parten del Core y jalan **solo el libro puntual** que necesitan — nunca la biblioteca entera. Así el conocimiento está al alcance sin inflar el contexto (criterio de IA Operativa / AiCare).

---

## Reglas de la Biblioteca

- Un libro por tipo de experiencia/juego; se **actualiza**, no se duplica (principio 7).
- **Nunca se aloja material ajeno.** El estante de Documentación real guarda ficha + URL + nivel de licencia (A explícita / B publicada sin licencia formal / C filtrada o decompilada). Nivel C se referencia, no se usa como insumo de producción.
- Conceptos + citas, **nunca** texto verbatim con copyright. Si una fuente no tiene licencia clara, se resuelve con el owner antes de usarla.
- Un libro es "de verdad" recién cuando pasó por misión (investigado + destilado + validado). Antes es un estante reservado, *En estudio*.
- La Escuela llena la Biblioteca; **el owner aprueba** qué se vuelve criterio del Core.

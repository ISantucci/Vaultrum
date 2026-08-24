# Biblioteca

## Propósito

La Biblioteca es el **corazón de la Escuela**: el espacio donde se guardan los **libros** y donde trabajan sus agentes. Es el activo real de la Escuela — la librería de conocimiento reutilizable que hace que "hacé un X" traiga un baseline sólido sin pedirlo (Ley candidata #1).

No es un catálogo de juegos ni una lista de 500 títulos. Es una colección de **libros** curados, cada uno con índice y metadata, indexados para consultarse por categoría.

> **Portada:** `00_Catalogo_Biblioteca` — índice maestro de todo lo ya sumado, separado por categoría. La skill lo actualiza al cerrar cada corrida.

---

## Portada

### [[00_Catalogo_Biblioteca|Catálogo de la Biblioteca]]

Índice maestro de todo lo ya sumado, separado por categoría. La skill lo actualiza al cerrar cada corrida.

---

## Estantes

### [[00_Indice_fundamentos|Fundamentos]]
Lo **transversal**: lo que hace que algo *sea* una experiencia y se *sienta* bien, sirva para el género que sirva. El loop de experiencia (input → feedback → objetivo → victoria/derrota), el game feel / juice, la definición de terminado. Un plataformero y un shmup comparten estos fundamentos.

### [[00_Indice_juegos|Juegos]]
Análisis **por juego/tipo**, guardados por **género**. Qué hace bien un Pong, un breakout, un roguelike: sus table-stakes y su juice específicos. Cuando se pide un juego de ese género, su libro (y los Fundamentos que aplican) están al alcance.

### [[00_Indice_fuentes|Fuentes]]
Libros, papers y referencias **externas** que la Escuela estudia — la materia prima. No son libros destilados de Vaultrum: se catalogan (cita + resumen aprendido, sin verbatim) y luego, en una misión de destilación, alimentan los Fundamentos o Juegos. Separar la fuente del libro destilado evita meter texto ajeno en el activo propio.

### [[00_Indice_documentos|Documentación real]]
**Artefactos** de la industria: documentos de diseño que se usaron de verdad (GDD, design bibles, pitches), código fuente liberado, documentación oficial de motor y registros de proceso. No son teoría (eso es Fuentes) ni destilado propio (eso son Fundamentos y Juegos): son **evidencia primaria**, para que Producción y Game Design vean cómo lo resolvió alguien que ya lo hizo en vez de discutirlo en abstracto. La Biblioteca **no aloja** estos documentos: guarda ficha, referencia y URL, con el nivel de licencia declarado.

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

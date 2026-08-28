# 05_Escuela

## Propósito

La **Escuela Vaultrum** es un espacio propio del sistema (par de Core, Agencia, Comunidad e IA Operativa): la **capa de aprendizaje proactivo**. No espera a que un proyecto genere conocimiento — sale al mundo a buscar lo que al Core le falta y lo trae destilado.

Nace de la Ley candidata #1 (fricción mínima / baseline competente): si la IA tiene que traer "lo básico bien hecho" por default, alguien tiene que producir y curar ese básico. Esa es la Escuela.

Su corazón es la `00_Biblioteca`: el espacio donde se guardan los **libros** y donde trabajan sus **agentes**. No produce trabajo hacia adelante (no arma RQ/GDS/SOL/EJ): produce y cuida conocimiento reutilizable.

---

## Escuela vs Conocimiento (proactiva vs reactiva)

```
Conocimiento  = aprendizaje INTERNO   → acompana lo que se escribe y cosecha lo trabajado
Escuela       = aprendizaje PROACTIVO → sale a buscar lo que falta en el mundo
```

Las dos respetan la misma gobernanza. **La Escuela NO mergea al Core**: entrega sus candidatos (`EST`) al Área de Conocimiento, que sigue siendo la única que propone cambios a `main`. La Escuela investiga y destila; Conocimiento versiona y propone; el owner aprueba.

```
Gap del Core / idea / ambigüedad
→ Escuela (misión acotada: investiga + destila)  → libro + candidato EST
→ Conocimiento (dedup + ubicación + diff)         → commit
→ Owner (timón del barco)                          → aprueba
```

---

## [[00_Biblioteca|La Biblioteca (el corazón)]]

Todo el activo vive en la `00_Biblioteca`: una librería real y navegable con **cinco estantes**:

- **Fundamentos** (`00_Indice_fundamentos`) — lo transversal de la *experiencia*: el loop, el game feel, la definición de terminado.
- **Juegos** (`00_Indice_juegos`) — análisis por juego/tipo, guardados por **género** (Pong → arcade, etc.).
- **Construcción** (`00_Indice_construccion`) — el *mecanismo*: cómo se construye técnicamente un juego. La Biblioteca no es una escuela de juegos: es una escuela de desarrollo de videojuegos.
- **Fuentes** (`00_Indice_fuentes`) — libros, papers y referencias externas: la materia prima.
- **Documentación real** (`00_Indice_documentos`) — evidencia primaria de la industria: ficha + URL + licencia, nunca alojada.

Cada libro tiene índice y metadata (género, tipo), para que se encuentre por categoría. Los libros no se escriben a mano de una: son el resultado de las **misiones de estudio** de la Escuela, y se **actualizan**, no se duplican.

---

## Quién consulta la Biblioteca

Dos consumidores, siempre **on-demand** (se jala el libro puntual, no la biblioteca entera):

1. **Producción (RQ) y Game Design base** — en tiempo de diseño, consultan por género para que la **primera entrega sea sólida y firme, a la altura de un juego divertido** — no un MVP apurado (Ley #1). Parten del Core, cuyo índice por género los rutea al libro.
2. **Conocimiento** — como puente de gobernanza: decide qué de la Biblioteca se vuelve criterio indexado del Core, y qué se actualiza.

El Core guarda el **índice por género** (liviano); el contenido pesado vive en la Biblioteca y se carga solo cuando hace falta. Eso mantiene el Core y las áreas livianas (criterio de IA Operativa / AiCare).

---

## Cuándo se manda a estudiar (misiones)

La Escuela es un espacio al que se **manda a iterar en sesiones acotadas por tokens**. Una misión siempre tiene gap + presupuesto + barra de calidad, y puede dispararse por:

- un **gap del Core** (ej: faltan Fundamentos de Experiencia),
- una **caza de ideas** para un juego (sacar ideas, referencias, variantes),
- **reforzar un concepto que falla o se siente ambiguo** — dentro de Vaultrum o dentro de un juego en curso (no siempre es from scratch).

El detalle del intake y el alcance lo maneja el `01_Bibliotecario`.

---

## AiCare como seguro de vida

La Escuela es el área con más riesgo de intoxicarse (estudia con libertad, puede acumular). Por eso AiCare (pass GC) es obligatorio en los bordes de cada misión: valida presupuesto antes, mide consumo durante, poda el material bruto antes de destilar y confirma que el candidato no infle el contexto antes del handoff. Sin AiCare no arranca una misión ni se hace handoff.

---

## Estructura del espacio

```
05_Escuela/
  00_Escuela.md            (este documento)
  Biblioteca/              (corazón: libros + trabajo de los agentes)
    Fundamentos/           (loop, game feel, definición de terminado)
    Juegos/                (análisis por juego, por género)
  Agentes/                 (Bibliotecario, Investigador, Destilador, Validador)
  Flujos/                  (pipeline de misión con gates AiCare)
  Salidas/                 (candidatos EST + misiones registradas)
```

---

## Flujos del espacio

Cada flujo es un paso de la misión de estudio.

### [[01_Flujo_Mision_Estudio|Flujo Mision Estudio]]

### [[02_Flujo_Investigacion|Flujo Investigacion]]

### [[03_Flujo_Destilacion|Flujo Destilacion]]

### [[04_Flujo_Validacion_Estudio|Flujo Validacion Estudio]]

---

## Salidas del espacio

El registro de las misiones de estudio.

### [[00_Salidas_escuela|Índice de salidas]]

---

## Skill ejecutable

La Escuela corre como la skill **`vaultrum-escuela`** (fuente versionada en `05_Escuela/Skills/vaultrum-escuela/SKILL.md`). Es el "interruptor": desde cualquier chat, al pedir sumar/estudiar un libro, dispara el pipeline de misión (los cuatro roles + AiCare) y escribe en la Biblioteca. Sin ella, los documentos de abajo son el manual, no la máquina.

---

## Sub-agentes del área

### [[01_Bibliotecario]]
Rol ancla. Convierte un gap/idea/ambigüedad en una **misión de estudio acotada** (pregunta, presupuesto, barra) y hace la dedup inicial contra el Core y la Biblioteca. Guardián del alcance: sin misión clara, no se estudia.

### [[02_Investigador]]
Ejecuta la misión dentro del presupuesto. Busca fuentes y trae material bruto **con cita de origen**. No destila ni decide qué entra.

### [[03_Destilador]]
Convierte el material bruto en **principios/fundamentos claros y reutilizables + citas**, y los escribe en el libro que corresponde (Fundamentos o Juegos). Nunca copia verbatim con copyright.

### [[04_Validador_Estudio]]
Verifica la barra antes del handoff: reutilizable, claro, citado, no verbatim, no duplicado. Si pasa, entrega el `EST` a Conocimiento. Si no, vuelve o se descarta.

---

## Límites del espacio

No hace producción (RQ/GDS/SOL/EJ). No mergea a `main` (eso es Conocimiento + owner). No estudia sin misión ni presupuesto. No guarda texto verbatim. No infla el Core "por las dudas": si un fundamento no es claro y reutilizable, no entra.

---

## Encadenado con el resto

Recibe de: **el owner** (pedido/idea), **el Core** (un gap), o **un juego en curso** (una ambigüedad a reforzar).
Entrega a: **Área de Conocimiento** (candidato `EST` → commit → aprobación del owner).
Consultada por: **Producción y Game Design** (on-demand, vía el índice por género del Core).
Vigilada por: **AiCare / IA Operativa** (seguro de vida contra la acumulación).

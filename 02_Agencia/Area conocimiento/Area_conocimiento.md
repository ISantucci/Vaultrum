## Propósito

El Área de Conocimiento es la **capa de control de versiones del conocimiento** de Vaultrum. No produce trabajo hacia adelante como las áreas de producción: cuida el Core y gestiona qué aprendizaje entra a él, con criterio y aprobación.

No existe para acumular historial. Existe para que el Core crezca solo con conocimiento claro, reutilizable y útil (principio 11).

---

## Modelo: gestión de versiones

```
VaultrumCore        = main            (fuente de verdad, curada)
Proyecto / idea     = branch          (el trabajo de las áreas de producción)
Aprendizaje útil    = commit          (propuesta de cambio al Core)
Entrar al Core      = merge a main    (requiere revisión + aprobación del maintainer)
Descartar           = branch tirada   (no toca el Core)
```

El Core alimenta el arranque de todas las áreas (principio 1: partir del Core) y esta área gestiona lo que vuelve a él. Es la única que puede proponer cambios a `main`.

---

## Sub-agentes del área

### [[01_Encargado_Commits]]

Rol ancla. Al cerrar una branch (o cuando un área marca un aprendizaje), revisa lo hecho y decide **con criterio qué merece commitearse** (no todo entra — principio 11). Prepara los commits candidatos y gestiona la política de merge según el caso. No escribe la nota final ni decide su ubicación.

### [[02_Documentador]]

Escribe cada aprendizaje candidato como un `.md` claro en **Staging**, útil para humanos e IAs (principio 8): responsabilidad, aplicación, límites. No decide si entra ni dónde vive.

### [[03_Arquitecto_Conocimiento]]

Decide **dónde vive** el aprendizaje en el Core, evita duplicación y resuelve "conflictos de merge" (si ya existe algo parecido, se actualiza en vez de duplicar). Prepara el diff que se te presenta. No redacta el contenido desde cero ni aprueba el merge.

---

## Staging

La carpeta [[00_Staging]] es la pizarra de **commits pendientes**: aprendizajes escritos que esperan tu aprobación. Es **transitoria**: cuando un aprendizaje se mergea al Core, se limpia de Staging. Si se descarta, también.

Staging no es un registro histórico. El historial, si se necesita, vive en git (el `git log`), no en el vault.

---

## Los 3 casos (políticas de merge)

### Caso 1 — Dev completo → [[01_Flujo_Retrospectiva]]
El desarrollo se terminó porque el conocimiento ya estaba en el Core. Poco aprendizaje nuevo. Se corre una retrospectiva: casi no hay commits, a lo sumo un refinamiento de una nota existente. Merge limpio, `main` casi no cambia.

### Caso 2 — Branch completa (idea nueva) → [[02_Flujo_Aprendizaje_Branch]]
Se desarrolló una idea nueva de punta a punta. Hay conocimiento nuevo real. Flujo completo: detectar → escribir en Staging → presentar diff → aprobar → merge. Es el caso central del área.

### Caso 3 — Branch experimental → [[03_Flujo_Experimento]]
Idea que quizás es un avance. Se evalúa si sirve. Si sí, genera commits (va al flujo del caso 2). Si no, se descarta: cero al Core.

---

## Regla operativa

Primero criterio (¿este aprendizaje es reutilizable?).
Después redacción clara.
Después ubicación sin duplicar.
Después presentación del diff.
Recién con tu aprobación, merge al Core.

Ningún aprendizaje entra al Core sin pasar por criterio y aprobación.

---

## Reglas de git (seguridad)

El área prepara commits (título acorde a la implementación + resumen breve en los comentarios) y actúa como seguro de vida para no perder trabajo. Pero:

- A `main` integra **solo la persona** que usa el software; el área nunca mergea ni pushea a main por su cuenta.
- Trabajando sobre `main`, el área **no crea branches nuevas ni commitea antes de que exista una implementación**.
- El área puede stagear, commitear y **pushear su branch de trabajo** (seguro de vida); no puede integrar a `main`.

Detalle en [[01_Encargado_Commits]].

---

## Límites del área

No hace trabajo de producción (no arma RQ/GDS/SOL/EJ). No mergea sin aprobación. No acumula historial en el vault. No infla el Core con "por las dudas": si un aprendizaje no es claro y reutilizable, no entra.

---

## Encadenado con las otras áreas

Recibe de: **todas las áreas de producción**, cuando su Validador/Revisor marca un aprendizaje reutilizable al cerrar; y de la **Escuela** ([[00_Escuela]]), que entrega candidatos `EST` desde su Biblioteca (aprendizaje proactivo).
Entrega a: **VaultrumCore** (merge aprobado).

Puente con la Escuela: la Escuela investiga y destila pero **no mergea al Core**. Conocimiento es el único que propone a `main`: toma el `EST`, hace dedup + ubicación + diff, y lo presenta al owner. Decide qué se vuelve criterio indexado del Core (para que las áreas lo jalen on-demand) y qué queda como libro de referencia en la Biblioteca.


## Skill del área

El área corre como la skill `vaultrum-conocimiento` (fuente versionada en `02_Agencia/Area conocimiento/Skills/vaultrum-conocimiento/SKILL.md`).

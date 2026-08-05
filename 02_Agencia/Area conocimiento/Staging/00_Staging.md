## Propósito

Staging es la pizarra de **commits pendientes** del Área de Conocimiento: aprendizajes escritos que esperan aprobación para mergearse al Core.

Es una zona **transitoria**, no un registro histórico.

---

## Cómo funciona

```
Encargado de Commits detecta aprendizaje
   ↓
Documentador escribe la nota .md acá (Staging)
   ↓
Arquitecto de Conocimiento define destino y diff
   ↓
Se presenta el diff al maintainer
   ↓
   ├── Aprobado → merge al Core → la nota se limpia de Staging
   └── Rechazado → se descarta → la nota se limpia de Staging
```

---

## Reglas

- Cada `.md` en Staging es un aprendizaje candidato, no conocimiento definitivo.
- Nada en Staging es fuente de verdad: la fuente es el Core (`main`).
- Al mergear o descartar, la nota se elimina de Staging (principio 11: no acumular historial).
- Si se quiere historial, vive en git (`git log`), no acá.

---

## Estado actual

Sin commits pendientes.

## Propósito — Caso 2: Branch completa (idea nueva)

Se desarrolló una idea nueva de punta a punta en un proyecto. Hay conocimiento nuevo real. Este flujo lo captura, lo escribe, lo ubica y lo presenta para aprobación antes de mergear al Core. Es el caso central del área.

---

## Entrada del flujo

- Una branch cerrada con conocimiento nuevo (mecánica, sistema, patrón aplicado, decisión técnica reutilizable).

---

## Transformación que realiza (pipeline del área)

```
Encargado de Commits → detecta aprendizajes reutilizables (criterio, principio 11)
   ↓
Documentador → escribe cada uno como .md en Staging (claro, para humanos e IAs)
   ↓
Arquitecto de Conocimiento → define destino en el Core, evita duplicación, arma el diff
   ↓
Se presenta el diff al maintainer
   ↓
   ├── Aprobás → merge al Core → se limpia Staging
   └── Rechazás → se descarta → se limpia Staging
```

---

## Gate de aprobación

Antes de tocar el Core, se te presenta:

```txt
## Aprendizajes a agregar/actualizar
## Diff propuesto (archivos nuevos / modificados, con destino en el Core)
## Qué mejora esto en el Core
## ¿Apruebo el merge?
```

Ningún aprendizaje entra sin tu OK (principio 10).

---

## Criterios de aceptación

- Cada aprendizaje es reutilizable, no historial del proyecto.
- Está escrito con estructura, intención, límites y aplicación (principio 8).
- Tiene destino claro en el Core y no duplica lo existente.
- El diff es entendible y aprobable.

---

## Qué debe evitar

No mergear sin aprobación. No duplicar conocimiento del Core. No inflar `main` con aprendizajes vagos. No acumular en Staging: al cerrar, se limpia.

---

## Resultado final

Conocimiento nuevo, curado y aprobado, mergeado al Core; Staging limpio. Lo rechazado no deja rastro en el Core.

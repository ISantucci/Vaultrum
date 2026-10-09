## Propósito — Caso 2: Branch completa (idea nueva)

Se desarrolló una idea nueva de punta a punta. Hay conocimiento nuevo real. Este flujo lo captura, lo escribe, lo ubica y lo presenta para aprobación antes de mergear al Core. Es el caso central de la cosecha.

---

## Entrada del flujo

Una branch cerrada con conocimiento nuevo —mecánica, sistema, patrón aplicado, decisión técnica reutilizable— derivada por el `03_Flujo_Cosecha`.

---

## Transformación que realiza (pipeline del área)

```txt
Cosechador → detecta aprendizajes reutilizables sobre la evidencia juntada
   ↓
Documentador → escribe cada uno como .md en Staging, con su evidencia
   ↓
Bibliotecario de Pertenencia → a qué cuerpo pertenece, evita duplicación,
                               pide el emplazamiento al arquitecto y arma el diff
   ↓
Validador → corre el instrumento sobre la nota y cierra o rebota
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
## Emplazamiento citado (el ARQ que decidió dónde vive)
## Qué mejora esto en el Core
## ¿Apruebo el merge?
```

Ningún aprendizaje entra sin tu OK.

---

## Criterios de aceptación

- Cada aprendizaje es reutilizable y trae la evidencia de qué trabajo real lo produjo.
- Está escrito con estructura, intención, límites y aplicación.
- Tiene pertenencia clara, no duplica lo existente, y su ubicación viene del arquitecto.
- El diff es entendible y aprobable.

---

## Qué debe evitar

No mergear sin aprobación. No colocar la nota en el vault por su cuenta. No duplicar conocimiento del Core. No inflar `main` con aprendizajes vagos. No acumular en Staging: al cerrar, se limpia.

---

## Resultado final

Conocimiento nuevo, curado y aprobado, mergeado al Core; Staging limpio. Lo rechazado no deja rastro en el Core.

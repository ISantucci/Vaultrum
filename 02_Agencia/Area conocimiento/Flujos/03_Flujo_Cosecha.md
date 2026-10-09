## Propósito — Modo Cosecha

Decidir qué de lo que se trabajó vuelve al Core. Es la autonutrición de Vaultrum, y es el único modo en el que el área firma lo que produce.

---

## Entrada del flujo

Una entrega cerrada (`VE` en Cerrado), una branch terminada, o un aprendizaje que un área marcó durante su cierre.

---

## Transformación que realiza

**Primero se junta la evidencia, después se opina.**

```txt
`documentacion.py <ruta> --cosecha`
   ↓
traza de operación      qué área tocó qué artefacto, cuántas veces
remediales de los VE    qué hubo que pedir dos veces — fricción ya clasificada
salidas de la entrega   decisiones y desvíos declarados
Staging                 qué se propuso antes, para no proponerlo de nuevo
   ↓
El Cosechador clasifica el caso
   ↓
   ├── Caso 1 → `04_Flujo_Retrospectiva`
   ├── Caso 2 → `05_Flujo_Aprendizaje_Branch`
   └── Caso 3 → `06_Flujo_Experimento`
```

Un remedial que aparece dos veces en dos entregas distintas no es mala suerte: es un criterio que al Core le falta.

---

## Salida esperada

```txt
## Entrega / branch cosechada
## Evidencia leída (traza, remediales, salidas, Staging)
## Caso clasificado
## Aprendizajes candidatos — título, por qué es reutilizable, ¿actualiza algo?
## Descartados (y por qué)
## Política de merge propuesta
```

---

## Criterios de aceptación

- Cada candidato se apoya en algo escrito, no en memoria.
- Lo que ya está en Staging no se propone de nuevo.
- Cerrar sin candidatos es una salida válida.
- El caso está clasificado antes de derivar.

---

## Qué debe evitar

No cosechar historial del proyecto. No inventar un aprendizaje para justificar el paso. No proponer lo que el Core ya dice. No leer la traza como si midiera calidad: mide actividad.

---

## Resultado final

Una lista corta de candidatos con evidencia, o el cierre honesto de que esta vez no hubo nada que absorber.

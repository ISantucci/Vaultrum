## Propósito — Caso 1: Dev completo (merge limpio)

Se terminó un desarrollo usando Vaultrum. Se pudo terminar porque el conocimiento ya estaba en el Core, así que se aprende poco. Este flujo hace una **retrospectiva**: revisar lo hecho por si hay algo que mejorar en el Core, sabiendo que lo más probable es que `main` casi no cambie.

---

## Entrada del flujo

Una entrega o branch cerrada que se resolvió con conocimiento ya existente en el Core, derivada por el `03_Flujo_Cosecha`.

---

## Transformación que realiza

- El Cosechador revisa lo hecho buscando fricciones: ¿alguna nota del Core estuvo confusa? ¿faltó un ejemplo? ¿algo se aplicó distinto a como estaba documentado?
- Los remediales declarados en el `VE` son la primera fuente: ahí ya está escrito lo que hubo que pedir dos veces.
- Detecta refinamientos, no conocimiento nuevo.
- Si no hay nada que mejorar, cierra sin commits (resultado válido).

---

## Salida esperada

```txt
## Retrospectiva de <entrega>
## Fricciones detectadas (o ninguna)
## Refinamientos propuestos al Core (si hay)
## Decisión: sin cambios / commits menores a revisar
```

---

## Criterios de aceptación

- Se revisó lo hecho contra el conocimiento del Core que se usó.
- Los refinamientos, si hay, son claros y reutilizables.
- Cerrar sin cambios es una salida aceptable.

---

## Merge

Si hay refinamientos, pasan por el gate de aprobación como en el caso 2, más liviano. Si no, no hay merge y `main` queda igual.

---

## Qué debe evitar

No inventar aprendizajes para justificar el paso. No tocar el Core por tocar. No confundir lo que pasó en el proyecto con criterio reutilizable.

---

## Resultado final

Una lectura honesta: el Core sirvió, y a lo sumo se mejora un detalle. Casi siempre, merge limpio sin cambios.

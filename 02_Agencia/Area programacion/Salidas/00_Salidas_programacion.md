## Propósito

Esta carpeta contiene las salidas formales del Área de Programación.

Una salida aparece cuando un requerimiento fue analizado, diseñado, ejecutado y revisado.

El resultado queda registrado como una solución técnica (`SOL`) y su ejecución (`EJ`).

---

## Índices internos

- [[00_Indice_soluciones]]
- [[00_Indice_ejecuciones]]

---

## Regla de salida

La numeración se hereda del requerimiento que resuelve. No se inventa: cuelga del `RQ-XXX.n` de Producción.

```
RQ-001.2   (Producción)
GDS-001.2  (Game Design)
SOL-001.2  (Programación — solución)
EJ-001.2   (Programación — ejecución)
```

`SOL` y `EJ` comparten el número base y la subnumeración del `RQ`. Un `EJ` pertenece a un `SOL`. Un `SOL` pertenece a un `RQ`.

---

## Regla operativa

Antes de crear una salida, revisar los índices para confirmar el hilo (`.n`) y linkear hacia atrás (`EJ → SOL → RQ/GDS → TL`).

Cada salida debe ser trazable de punta a punta.

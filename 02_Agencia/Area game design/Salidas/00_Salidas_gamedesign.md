## Propósito

Esta carpeta contiene las salidas formales del Área de Game Design.

Una salida aparece cuando un requerimiento jugable fue encuadrado, diseñado, balanceado y validado.

El resultado queda registrado como una game design spec (`GDS`).

---

## Índice interno

- [[00_Indice_gds]]

---

## Regla de salida

La numeración se hereda del requerimiento que diseña. No se inventa: cuelga del `RQ-XXX.n` de Producción.

```
RQ-001.2   (Producción)
GDS-001.2  (Game Design)
LDS-001.2  (Level Design · si el sistema tiene espacio)
UXS-001.2  (UI/UX · si el sistema tiene interfaz)
SOL-001.2  (Programación)
```

Un `GDS` pertenece a un `RQ`. Al cerrarse baja a **Level Design** y/o **UI/UX** cuando aplican, y de ahí —junto al `LDS`/`UXS`— al `SOL` del Área de Programación. Si ninguna aplica, el propio `GDS` lo declara y pasa directo a Programación.

---

## Regla operativa

Antes de crear una salida, revisar el índice para confirmar el hilo (`.n`) y declarar el `RQ` correspondiente. Cada `GDS` debe ser trazable.

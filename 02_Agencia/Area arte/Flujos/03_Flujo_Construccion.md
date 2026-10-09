## Propósito

Construir el asset con la proporción y el presupuesto ya cerrados, y entregarlo a verificación sin cerrarlo.

---

## Entrada del flujo

- La proporción derivada de `02_Flujo_Referencia`, con lo que falta declarado.
- El presupuesto de caras de la familia y el contrato de exportación, de la mitad A del `ART-XXX.n`.
- El taller `Herramientas/primitivas.py` y las nueve reglas `RA-001` a `RA-009`.

---

## Transformación que realiza

- `03_Modelador` escribe el script del asset.
- Aplica las nueve reglas y pasa el checklist.
- Cumple el contrato de `emparentar()` antes de armar la jerarquía.
- Entrega el asset a verificación. No lo cierra.

Todo asset de más de unas 150 líneas se escribe a disco antes de la primera ejecución. El goblin son unas 500 líneas.

---

## Salida esperada / formato

```txt
## Asset
   nombre, familia, script
## Reglas aplicadas
## Checklist de defectos
   resultado de los tres
## Jerarquía
   ancla, hijos
## Lo que queda para verificación
```

---

## Checklist de los tres defectos repetidos

Aparecieron dos y tres veces en el proyecto: se chequean siempre, incluso cuando no aplican.

- La tapa de una pieza inclinada sube sobre su centro: una viga a 5° con 54 mm de radio sube 4.9 mm.
- La cara interior de un anillo poligonal es una cuerda, no un arco: con 12 bloques, un radio nominal de 0.860 m baja a 0.834 m entre vértices.
- Un panel escalado uniformemente se retrae desparejo: el retranqueo tiene que ser un inset real, no un `scale`.

---

## El contrato de emparentar()

Exige `location` horneada en cero y geometría ya en coordenadas del asset. Si no, cada hijo corre el origen del ancla: en el goblin fueron 29 mm en X y 43 mm en Y. Sólo se rompe lo que tenía menos holgura que ese corrimiento, así que el defecto pasa desapercibido hasta la pieza más ajustada.

---

## Criterios de aceptación

- El asset respeta la proporción derivada y el presupuesto de su familia.
- Los tres defectos del checklist están chequeados y escritos.
- `emparentar()` se llamó con `location` en cero y geometría en coordenadas del asset.
- El script está en disco y corrió limpio.
- El modelador no declaró el asset cerrado.

---

## Condiciones para avanzar

Avanza siempre a `06_Flujo_Verificacion_Malla`, por simple que sea el asset. El modelador no cierra y no se verifica a sí mismo.

No avanza si el script no corrió limpio: un asset que no se genera no se verifica.

---

## Qué debe evitar

No cambia la proporción ni el presupuesto por conveniencia de la construcción: eso vuelve al flujo que los fijó. No reduce geometría: eso es de `04_Optimizador`. No se autoaprueba. No improvisa en consola un asset que pasó las 150 líneas.

---

## Resultado final

Un asset construido, con sus reglas y su checklist escritos, en la puerta de verificación.

## Propósito

Convertir el encuadre en un `UXS` **instrumentado**: pantallas, jerarquía, estados, feedback y accesibilidad, escritos de forma que se puedan medir.

---

## Entrada del flujo

- El encuadre del `02_Flujo_Analisis_UX`, el `GDS-XXX.n` cerrado y el presupuesto de la mitad A.

---

## Transformación que realiza

- Define el sistema de señales: paleta, qué comunica cada color y qué segunda señal lo acompaña.
- Diseña pantallas, HUD y menús dentro de las franjas reservadas, con su jerarquía.
- Fija el mapping control→efecto de una vez para todas las pantallas, y los estados de cada elemento.
- Especifica el feedback inmediato de cada acción.
- Declara las excepciones con **cuándo aparece, cuánto dura y con qué peso**.
- Escribe los bloques declarativos que la herramienta lee.

---

## Salida esperada / formato

```txt
## Insumo
## Sistema de señales
## Pantallas / HUD / menús
## Mapping y estados de interfaz
## Feedback por acción
## Accesibilidad
## Excepciones declaradas
## Instrumento
```

Es la **mitad B** del `UXS-XXX.n`, y declara el `GDS` como insumo.

---

## Criterios de aceptación

- Cada pantalla entra en el techo declarado y respeta las franjas.
- Todo lo que el color comunica tiene una segunda señal.
- Una tecla, un verbo, en todas las pantallas.
- Toda acción disponible está escrita en pantalla.
- Los bloques declarativos están completos: el `UXS` se puede medir.

---

## Condiciones para avanzar

Avanza al `04_Flujo_Auditoria_Legibilidad` con el `UXS` instrumentado. Un `UXS` sin instrumentar no avanza: vuelve al diseño.

---

## Qué debe evitar

No cambia reglas ni diseña niveles. No programa. No decora a costa de la legibilidad: nada de lo que agregue puede tapar una falla ni volver ambiguo un estado.

---

## Resultado final

Un `UXS-XXX.n` que se puede medir en vez de discutir.

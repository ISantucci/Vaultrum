## Propósito

Esta carpeta contiene las salidas formales generadas por el Área de Producción.

Una salida formal aparece cuando una idea ya fue analizada, bajada a tierra y planificada.

El resultado debe quedar registrado como timeline y requerimientos asociados al abrir el hilo, y como validación de entrega al cerrarlo.

---

## Índices internos

- [[00_Indice_timelines]]
- [[00_Indice_requerimientos|Índice de requerimientos]]
- [[00_Indice_ve]]

---

## Regla de salida

Cada planificación cerrada debe generar un número base.

Ejemplo:

TL-001

Los requerimientos asociados usan el mismo número base con subnumeración.

Ejemplo:

RQ-001.1
RQ-001.2
RQ-001.3

---

## Regla de la validación de entrega

La validación de entrega cuelga del timeline y **no lleva subnumeración**: valida la iteración completa, no cada requerimiento.

Ejemplo:

TL-001
VE-001

El gate de cierre está definido en `02_Indice Agencia`.

---

## Relación entre timeline y requerimientos

El timeline ordena la planificación general.

Los requerimientos concretan las partes necesarias para cumplir esa planificación.

Un timeline puede tener uno o varios requerimientos asociados.

Un requerimiento debe pertenecer a un timeline.

---

## Regla operativa

Antes de crear una nueva salida, se debe revisar el indice de timelines para identificar el ultimo numero utilizado.

Si no existe ningun timeline registrado, la primera salida debe comenzar en:

TL-001

Luego se deben crear los requerimientos asociados usando el mismo numero base.

Ejemplo:

TL-001
RQ-001.1
RQ-001.2
RQ-001.3
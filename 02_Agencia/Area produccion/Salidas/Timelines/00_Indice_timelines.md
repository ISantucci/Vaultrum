## Propósito

Esta carpeta contiene los timelines generados por el Área de Producción.

Cada timeline organiza una planificación general y agrupa los requerimientos necesarios para concretarla.

---

## Formato obligatorio

Cada timeline ordena:

```txt
objetivo
área afectada
criticidad
requerimientos asociados
secuencia de trabajo
dependencias
riesgos
criterios de cierre
```

---

## Regla de numeración y nombre de archivo

Cada timeline usa un número base incremental, y sus requerimientos heredan ese número:

```txt
TL-001
TL-002
TL-003
```

El archivo se nombra con el código, el separador y el nombre descriptivo:

```txt
TL-XXX_Nombre_Descriptivo.md
TL-001_Pong_2_Jugadores_Completo.md
```

---

## Timelines registrados

El listado de timelines de Modo Owner vive en `00_Registro_timelines`, que no se versiona. Los de un proyecto viven en la carpeta del proyecto.

---

## Nota de secuencia

`TL-007` y `TL-008` corren en Modo Owner y **van antes que cualquier proyecto**. Se cruzan en un punto declarado: `RQ-007.4` depende de `RQ-008.2`, porque el cuaderno vive en un árbol que el Arquitecto emplaza.

La línea de Vaultrum World (`TL-004..006`) está detenida a propósito hasta que cierren los dos: modela el recorrido de una cadena cuyo primer eslabón todavía no existe.


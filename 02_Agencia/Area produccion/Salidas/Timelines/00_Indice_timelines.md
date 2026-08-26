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

Los timelines de un proyecto viven en `06_Proyectos/<Proyecto>/01_Produccion/`. Acá quedan **solo los de Modo Owner**: los que desarrollan el sistema Vaultrum en sí.

- [[TL-007_Apertura_De_Vaultrum|TL-007 La apertura de Vaultrum]] — el eslabón cero: la puerta, las quince preguntas de seteo y el cuaderno del proyecto
- [[TL-008_La_Agencia_Es_La_Empresa|TL-008 La Agencia es la empresa, no el archivo]] — separar el sistema de lo que el sistema produce

> Proyectos: `00_Proyectos`. El Pong 3D y Vaultrum World se mudaron ahí el 2026-08-25.

## Nota de secuencia

`TL-007` y `TL-008` corren en Modo Owner y **van antes que cualquier proyecto**. Se cruzan en un punto declarado: `RQ-007.4` depende de `RQ-008.2`, porque el cuaderno vive en un árbol que el Arquitecto emplaza.

La línea de Vaultrum World (`TL-004..006`) está detenida a propósito hasta que cierren los dos: modela el recorrido de una cadena cuyo primer eslabón todavía no existe.


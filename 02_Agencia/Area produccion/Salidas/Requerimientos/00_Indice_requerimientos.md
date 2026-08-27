## Propósito

Esta carpeta contiene los requerimientos generados por el Área de Producción.

Cada requerimiento debe concretar una parte del timeline asociado.

---

## Formato obligatorio

Cada requerimiento respeta esta estructura:

```txt
Título
Área afectada
Criticidad
Descripción
Subtasks
```

---

## Regla de numeración y nombre de archivo

Un requerimiento hereda el número base del timeline que concreta, y lo subnumera:

```txt
TL-001
  RQ-001.1
  RQ-001.2
  RQ-001.3
```

El archivo se nombra con el código, el separador y el nombre descriptivo:

```txt
RQ-XXX.Y_Nombre_Descriptivo.md
RQ-001.1_Paletas_Controlables.md
```

---

## Requerimientos registrados

El listado de requerimientos de Modo Owner vive en `00_Registro_requerimientos`, que no se versiona. Los de un proyecto viven en la carpeta del proyecto.


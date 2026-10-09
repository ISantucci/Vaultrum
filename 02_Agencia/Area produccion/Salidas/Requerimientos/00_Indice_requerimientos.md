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

## Dónde vive un requerimiento: lo decide su estado

Un `RQ` no se queda donde nació. **Lo que queda a la vista es lo que todavía admite trabajo; lo que ya no lo admite se archiva.** Es la única forma de que abrir la carpeta conteste sola la pregunta *"¿qué falta?"*.

```txt
en curso    su TL todavia no tiene VE                      -> queda a la vista
pausado     su TL tiene VE, y el VE lo declara Pausado      -> queda a la vista
entregado   su TL tiene VE                                  -> Archivo/
superado    su TL declara "Superado por TL-XXX"             -> Archivo/
```

Los dos que quedan a la vista son los dos que todavía piden algo: uno porque falta hacerlo, el otro porque falta poder hacerlo. **Un Pausado archivado es un pendiente escondido**, y esconder un pendiente es el defecto que este ordenamiento existe para no cometer.

**El estado no se declara en el `RQ`: se deriva de su cadena.** Un requerimiento no sabe si está hecho — lo sabe su timeline, y el timeline lo sabe porque tiene o no tiene su `VE` en disco. Es la misma regla que la Ley 1b de `documentacion.py`. Por eso no hay un campo de estado que alguien tenga que acordarse de actualizar: **no hay nada que mantener, hay algo que medir.**

La regla vale igual en los dos ámbitos, y cada uno archiva en su propia casa:

```txt
Modo Owner   02_Agencia/Area produccion/Salidas/Requerimientos/Archivo/
proyecto     06_Proyectos/<Proyecto>/01_Produccion/Archivo/
```

El `Archivo/` **no lleva índice propio**: guardar y declarar son cosas distintas (`TL-008`). El listado de lo archivado es el registro de la serie, que ya existe.

---

## El instrumento

```txt
python3 "02_Agencia/Area produccion/Herramientas/requerimientos.py"
    el inventario completo, por ambito, con lo que queda por hacer

    --pendientes   solo lo que queda por hacer
    --verificar    solo el veredicto, exit 1 si algo esta fuera de su carpeta
    --archivar     mueve lo entregado y lo superado a su Archivo/
```

Corre en el gate de cierre, así que **un commit que deja un `RQ` fuera de su carpeta no entra**. El Productor no se acuerda de archivar: el gate se lo cobra.

Cuando la cadena no alcanza a decir el estado —un `VE` que narra un Pausado viejo en vez de declarar uno vigente, por ejemplo— el instrumento marca `ambiguo` y **no adivina**: el `RQ` se queda a la vista hasta que alguien lo declare en `Herramientas/excepciones.txt`. Esas excepciones se escriben contra la **identidad** del requerimiento (`<ámbito>/RQ-<tl>.<n>`) y no contra su ruta, porque este instrumento mueve archivos y una excepción por ruta se rompe en silencio al moverse.

---

## Requerimientos registrados

El listado de requerimientos de Modo Owner vive en `00_Registro_requerimientos`, que no se versiona. Los de un proyecto viven en la carpeta del proyecto.


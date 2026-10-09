## Índice de publicaciones (PUB)

Registro de todas las corridas de la Comunidad. Cada `PUB-XXX` es una publicación preparada: el informe de avance que la justifica, el texto en los dos idiomas, el pedido de capturas y la verificación.

Una `PUB` no es un post publicado: es un post **listo para publicar**. Publicar lo hace el owner. Lo que pasa después —fecha, link, cómo le fue— se registra en el `00_Indice_publicaciones` del Archivo.

---

## Regla de numeración

`PUB-001`, `PUB-002`, … en orden de preparación. Una publicación por número, sin subíndices.

Las `PUB` **no cuelgan de la columna vertebral** de la Agencia. Una publicación no es un eslabón de la cadena de producción: puede nacer de un `VE`, de un merge al Core o de un pedido suelto, y ninguno de esos la convierte en `RQ` de nada. Cuando nace de un artefacto concreto, lo declara adentro en una línea rotulada.

---

## Estados

```txt
Listo     texto verificado y formato en norma. El owner puede publicarla cuando quiera.
Falta     falta un dato, o una imagen que el owner pidió. Declara cuál.
Publicada el owner la publicó. Su ficha vive en el Archivo.
```

**Las imágenes son opcionales y no bloquean el cierre.** El entregable de esta capa es el texto; quien decide y adjunta las imágenes al publicar es el owner (decisión del owner, 2026-08-25). El pedido de capturas se escribe solo cuando él lo pide, y si no lo pidió queda vacío y declarado. El gate de existencia en disco se conserva acotado a lo que sí se pidió.

---

## Los tres tiempos

Toda `PUB` cuenta tres cosas, en este orden: **qué problema había**, **qué se implementó** para resolverlo y un **caso de uso funcional** con resultado. Se declaran en un bloque bajo `## Los tres tiempos` y `post.py --verificar` falla si faltan.

Un caso de uso que todavía no existe se declara ausente. No se inventa, y la implementación no se cuenta dos veces para llenar el hueco.

---

## Registro

El listado de publicaciones vive en `00_Registro_pub`, que no se versiona.

---

## Regla del índice

Una publicación entra acá recién cuando pasó por el `04_Flujo_Validacion_Publicacion`, aunque cierre en Falta. Un texto sin verificación no es una `PUB`: es un borrador.

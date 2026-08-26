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

### [[PUB-001_We_Are_Back|PUB-001 — We are back]]

Primera corrida de la capa. Reaparición después de tres meses sin publicar: el refactor a áreas, la cadena con gates, la primera entrega jugada, la Escuela, IA Operativa, el ciclo de conocimiento cerrado y las dos pasadas de arquitectura. Cierra con hacia dónde va el sistema. Estado: Listo — pasó de Falta a Listo con la regla de imágenes opcionales, sin tocar el texto.

### [[PUB-002_El_auditor_auditado|PUB-002 — El auditor auditado]]

Actualización de sistema, con los tres tiempos completos. **Problema:** el verificador del grafo decía *en ley* y solo podía probar tres de las seis leyes, y el área estaba escrita para entrar última. **Implementación:** las seis leyes medidas, el área dada vuelta en tres modos, cuatro gates y uno que corre solo. **Caso de uso:** le pidieron ordenar la Biblioteca y encontró un catálogo espejo de 19 KB que tapaba un libro cerrado en el índice y sin aprobar en su ficha. Estado: Listo, sin imágenes por decisión del owner.

### [[PUB-003_El_dueno_que_no_existia|PUB-003 — El dueño que no existía]]

Actualización de sistema, con los tres tiempos completos. **Problema:** el Área de Conocimiento tenía colgado el control de versiones de git —126 de sus 624 líneas— y al sacárselo quedó una reasignación en el aire: *"la verificación previa al commit → Área de QA, cuando exista"*. **Implementación:** Conocimiento pasó de un servicio a tres y estrenó su instrumento; nació el Área de Control de Calidad, con nueve notas de criterio al Core y un gate entre el `EJ` y el `VE`. **Caso de uso:** el gate nuevo midió su propio contrato de salida y se falló —declaraba GO con un bloqueante abierto, midió NO-GO—, y el gate de documentación encontró 44 fallas sobre 77 artefactos en su primera corrida. Estado: Listo, sin imágenes por decisión del owner.

---

## Regla del índice

Una publicación entra acá recién cuando pasó por el `04_Flujo_Validacion_Publicacion`, aunque cierre en Falta. Un texto sin verificación no es una `PUB`: es un borrador.

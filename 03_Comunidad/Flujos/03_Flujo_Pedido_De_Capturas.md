## Propósito

Definir qué imágenes acompañan al post y dejar el pedido escrito con la precisión suficiente para que el owner las saque de una sola vez.

---

## Cuándo corre

**A pedido del owner.** Las imágenes son opcionales: el entregable de esta capa es el texto, y quien adjunta las imágenes al publicar es el owner.

Si no las pidió, el flujo no corre: el pedido de capturas de la `PUB` queda **vacío y declarado** —no omitido— y el cierre no se bloquea por eso.

---

## Entrada del flujo

- El texto cerrado del `02_Flujo_Redaccion`.
- El pedido explícito del owner.
- La carpeta de medios de la publicación, que es donde los archivos van a caer.

---

## Transformación que realiza

- Recorre el post y marca qué afirmaciones ganan con una imagen que las pruebe.
- Elige el tipo de cada imagen y descarta lo decorativo.
- Escribe una entrada por imagen: nombre de archivo, qué se ve, encuadre, momento, texto alternativo, y qué afirmación del post prueba.
- Deja el pedido dentro de la salida `PUB`, no en un mensaje suelto.

---

## Salida esperada / formato

```txt
archivo:    NN_nombre.png
qué se ve:  descripción del contenido
encuadre:   cómo enmarcarlo
momento:    en qué instante sacarla
texto alt:  el texto alternativo, escrito y listo
prueba:     qué parte del post sostiene
```

Máximo cuatro imágenes por publicación. La mayoría de las veces alcanza con una.

---

## Criterios de aceptación

- Cada imagen pedida sostiene una afirmación concreta del post.
- Cada entrada del pedido está completa: si al leerla hay que preguntar algo, está incompleta.
- El nombre de archivo del pedido es el mismo que va a tener en disco.
- El texto alternativo está escrito, no delegado.

---

## Condiciones para avanzar

Avanza al `04_Flujo_Validacion_Publicacion` con el pedido escrito, tenga o no las imágenes sacadas todavía.

La validación es la que verifica si los archivos están; este flujo solo deja el pedido en condiciones de cumplirse.

---

## Qué debe evitar

No saca capturas. No genera imágenes. No pide una imagen "para que no quede pelado". No deja un pedido a medias esperando que el owner interprete.

---

## Resultado final

Un pedido de capturas que se puede cumplir sin volver a preguntar nada.

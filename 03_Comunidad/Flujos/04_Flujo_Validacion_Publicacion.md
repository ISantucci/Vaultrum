## Propósito

Verificar que el post se puede publicar: cada afirmación sostenida, cada número medido, y en disco cada imagen que el owner haya pedido.

---

## Entrada del flujo

- El texto cerrado en los dos idiomas.
- El pedido de capturas.
- La carpeta de medios de la publicación, para comprobar qué archivos hay realmente.
- El informe de avance, que es contra lo que se rastrea todo.

---

## Transformación que realiza

- Rastrea cada afirmación del post hasta el archivo que la prueba.
- Verifica cada número contra su fuente original, no contra el informe que lo copió.
- Lista los archivos que hay en la carpeta de medios y los compara contra el pedido.
- Compara español e inglés afirmación por afirmación.
- Corre `Herramientas/post.py --verificar` sobre la `PUB`: el formato y la presencia de los tres tiempos los dictamina la herramienta, no la lectura.
- Comprueba que el caso de uso sea real y con resultado — la herramienta ve que está declarado, no que sea cierto.
- Emite el veredicto.

---

## Salida esperada / formato

```txt
## Afirmaciones
   afirmación — fuente — verificada / sin fuente
## Números
   valor en el post — valor en la fuente — coinciden / no
## Imágenes
   archivo declarado — existe / falta
## Formato
   post.py --verificar — en norma / fuera de norma
## Tres tiempos
   problema — implementación — caso de uso: sostenidos, o su ausencia declarada
## Paridad ES/EN
   diferencias, o "sin diferencias"
## Veredicto
   Listo / Falta (qué) / Rebota (a quién y por qué)
```

---

## Criterios de aceptación

- La comprobación de imágenes salió de listar la carpeta, no de suponer.
- Ningún número quedó verificado contra el informe: todos contra su fuente.
- El veredicto de formato salió de `post.py`, no de mirar el archivo.
- Lo que no se pudo verificar está declarado con esas palabras.

---

## Condiciones para avanzar

Cierra en **Listo** y la publicación queda registrada en el `00_Indice_pub`, lista para que el owner la publique.

Cierra en **Falta** si falta un dato, o si el owner pidió una imagen y no está en disco: la salida queda registrada igual, con el estado declarado, y pasa a Listo cuando aparece.

Una publicación **sin imágenes pedidas cierra en Listo**. Las imágenes son opcionales y las adjunta el owner al publicar; el pedido queda vacío y declarado, que no es lo mismo que omitido.

Rebota al flujo que corresponda si hay una afirmación sin fuente o un número sin medir.

---

## Qué debe evitar

No publica. No corrige el texto por su cuenta — rebota. No da por buena una imagen que no vio en el listado de la carpeta. No estima si el post va a funcionar: no es verificable.

---

## Resultado final

Un veredicto que dice si esto se puede publicar hoy, y si no, exactamente qué falta.

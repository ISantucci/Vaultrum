## Propósito

Leer lo que pasó desde la última publicación y decidir si hay post, antes de que nadie escriba una línea.

---

## Entrada del flujo

- **Un pedido del owner.** Es el único disparador de esta capa: la Comunidad no sale a publicar sola.
- La última ficha del `00_Indice_publicaciones`, que fija el piso de lo ya contado.
- Las fuentes primarias del período: `VE` cerrados, salidas nuevas de cualquier área, índices, historia de git, y lo que el owner marque a mano.

Si el owner acotó el tema, el alcance es ese y se declara. Si no lo acotó, el alcance es todo lo posterior a la última ficha.

---

## Transformación que realiza

- Fija el piso: fecha y contenido de la última publicación.
- Recorre las fuentes y arma la lista de cambios reales, cada uno con el archivo que lo prueba.
- Descarta lo que es ruido y declara por qué.
- Detecta los datos que harían falta y no están.
- Emite el veredicto.

---

## Salida esperada / formato

```txt
## Piso
   última publicación, fecha, qué contó
## Avance del período
   cambio — archivo que lo prueba — fuente
## Mensaje central
   una frase
## Qué queda afuera
   qué y por qué
## Datos faltantes
   qué habría que medir o confirmar
## Veredicto
   hay post / no hay post
```

---

## Criterios de aceptación

- Cada avance de la lista nombra un archivo existente.
- El mensaje central entra en una frase. Si necesita dos, hay dos posts o no hay ninguno.
- Lo que queda afuera está escrito, no omitido en silencio.

---

## Condiciones para avanzar

Avanza al `02_Flujo_Redaccion` cuando el veredicto es **hay post** y el mensaje central está declarado.

No avanza si el veredicto es **no hay post**: en ese caso cierra ahí, se le dice al owner qué falta para que haya, y no se registra `PUB`. Un período sin publicación es un resultado, no una falla.

---

## Qué debe evitar

No redacta. No adelanta títulos. No decide imágenes. No convierte un cambio menor en avance para que el pedido del owner no quede sin respuesta.

---

## Resultado final

Un informe que dice qué se puede contar, con qué lo prueba cada cosa, y si conviene contarlo.

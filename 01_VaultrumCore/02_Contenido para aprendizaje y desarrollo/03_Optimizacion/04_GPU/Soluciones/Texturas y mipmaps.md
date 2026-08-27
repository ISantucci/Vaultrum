## Definicion

Las texturas no cuestan en un solo lugar.

```txt
Memoria.
Ancho de banda.
Sampling.
Tiempos de carga.
```

Y ese costo depende de varios factores a la vez:

```txt
Dimensiones.
Formato.
Compresion.
Mipmaps.
Cantidad.
```

De ahi sale la aclaracion importante:

```txt
Una textura de 4096 × 4096
no es mala automaticamente.
```

La pregunta correcta no es cuanto mide. Es:

```txt
¿Hace falta esa cantidad de informacion visual
para el tamaño que ese objeto ocupa en pantalla?
```

Mipmaps son la respuesta sistematica a esa pregunta: versiones progresivamente menores de la misma textura, elegidas segun cuanto ocupa el objeto.

```txt
cerca → resolucion alta
lejos → resolucion menor
```

---

## Que problema ayuda a prevenir

Ayuda principalmente con:

```txt
Presion sobre ancho de banda
Costo de fragmentos y shaders
Memoria residente de recursos graficos
Tiempos de carga largos
Aliasing y ruido en superficies lejanas
```

El desperdicio tipico:

```txt
Una textura enorme leida
para pintar un objeto de veinte pixeles.
```

Y un sintoma que se confunde seguido:

```txt
La escena tiene poca geometria.
El frame igual es caro.
Bajar resolucion mejora algo.
El costo esta en lecturas, no en triangulos.
```

---

## Como funciona

Cada factor mueve el costo hacia un lado distinto.

```txt
Dimensiones
→ memoria y bandwidth crecen con el area.

Formato y compresion
→ cuantos bytes ocupa cada pixel.

Cantidad
→ cuantas lecturas distintas por material.

Mipmaps
→ cual version se lee en cada momento.
```

El detalle que mas se subestima:

```txt
Duplicar el lado de una textura
no duplica el costo.
Lo cuadruplica.
```

Los mipmaps se generan una vez y se eligen en runtime segun el tamaño en pantalla.

Beneficios:

```txt
Menor presion de lectura.
Mejor comportamiento de cache.
Menos aliasing.
Mejor representacion a distancia.
```

Trade-off directo:

```txt
mas almacenamiento
y mas memoria
```

Aproximadamente un tercio adicional sobre la textura original. Se paga en memoria para ahorrar bandwidth.

---

## Como aplicarlo en videojuegos

En un Tower Defense casi nada se ve de cerca. Esa es justamente la situacion donde el criterio de tamaño en pantalla se aplica solo.

```txt
Antes:
Cada tipo de enemigo con textura de 2048
→ y en pantalla ocupa 60 pixeles.

Despues:
Textura de 512
→ misma lectura visual
→ mucho menos memoria y bandwidth.
```

Con las torres conviene ser mas cuidadoso:

```txt
Torre vista en el mapa
→ chica, resolucion baja alcanza.

Torre mostrada en el panel de compra
→ grande y quieta
→ ahi si se nota la resolucion.
```

El HUD de dinero, vida y wave suele resolverse mejor asi:

```txt
Iconos sueltos
→ muchas texturas chicas
→ muchos cambios de estado.

Atlas de iconos
→ una lectura
→ menos cortes de agrupacion.
```

Los mipmaps casi siempre se dejan activos en escena y casi siempre se desactivan en UI, que se dibuja a tamaño fijo.

---

## Relacion con arquitectura

Esto es sobre todo autoria y pipeline de assets, no codigo de gameplay.

```txt
Convencion de tamaños por categoria de objeto.
Formato definido por plataforma.
Ajustes de importacion revisados, no por defecto.
Atlas para elementos chicos y repetidos.
```

Lo que hace falta poder responder:

```txt
¿Que tamaño maximo corresponde a esta categoria?
¿Quien decidio ese formato?
¿Cuantas texturas distintas usa este material?
¿Estas dos texturas son realmente distintas?
```

Se apoya en los mismos sistemas que gestionan recursos:

```txt
Carga y descarga de assets
Ciclo de vida de recursos
Agrupacion de materiales
```

Una textura no se optimiza en runtime. Se decide al importarla.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
Memoria de GPU
Ancho de banda
Fragment processing
Almacenamiento
Tiempos de carga
```

El formato es lo que mas cambia el cuadro:

```txt
Sin comprimir
→ maxima calidad
→ maxima memoria y lectura.

Comprimido
→ menos memoria y menos bandwidth
→ artefactos segun el contenido.
```

Y el reparto entre recursos:

```txt
Mipmaps
→ menos bandwidth
→ mas memoria.

Texturas mas chicas
→ menos memoria y menos bandwidth
→ menos detalle disponible.
```

Pesa mucho mas en hardware con poca memoria grafica o poco ancho de banda.

---

## Cuando conviene usarlo

Conviene revisar texturas y activar mipmaps cuando:

```txt
Hay objetos que se ven a distintas distancias.
La memoria grafica esta ajustada.
El frame parece limitado por lecturas.
Aparece aliasing o ruido en superficies lejanas.
Los tiempos de carga son largos.
Hay muchas texturas grandes y poco control sobre ellas.
```

Casos claros:

```txt
Terreno.
Vegetacion.
Props repetidos.
Personajes vistos de lejos.
Escenarios grandes.
```

---

## Cuando NO conviene usarlo

Los mipmaps no aportan cuando:

```txt
El objeto siempre se ve al mismo tamaño.
Se trata de UI dibujada uno a uno.
La textura ya es muy chica.
La memoria es el recurso critico y el bandwidth sobra.
```

Y bajar resolucion no corresponde cuando:

```txt
El objeto es protagonista y se ve de cerca.
El detalle transmite informacion de gameplay.
La textura contiene texto o iconos que hay que leer.
No hay problema medido.
```

Una textura ilegible es un problema de diseño, no una optimizacion.

---

## Trade-offs

```txt
Mipmaps activos
→ menos bandwidth y menos aliasing
→ mas memoria.

Textura mas chica
→ menos memoria y menos lectura
→ menos detalle de cerca.

Compresion agresiva
→ menos memoria
→ artefactos visibles.

Atlas de texturas
→ menos cambios de estado
→ menos modularidad y mas autoria.

Menos texturas por material
→ shader mas barato
→ menos riqueza de superficie.
```

---

## Riesgos de aplicarlo mal

Riesgos comunes:

```txt
Bajar resolucion sin mirar el tamaño en pantalla.
Comprimir texturas que necesitan precision.
Activar mipmaps en UI y verla borrosa.
Desactivar mipmaps y arrastrar aliasing.
Usar formatos por defecto sin revisar plataforma.
Repetir la misma textura con nombres distintos.
Meter en un atlas cosas que se cargan por separado.
Confundir tamaño de archivo con memoria en runtime.
```

Ejemplo:

```txt
Antes:
Iconos del HUD con mipmaps activos.

Problema:
El motor elige un nivel menor.

Resultado:
El numero de dinero se ve sucio y el jugador no lo lee bien.
```

El costo bajo y la informacion se degrado. No sirve.

---

## Checklist de implementacion

```txt
¿El problema fue medido?
¿Cuanta memoria grafica ocupan las texturas?
¿Que tamaño real ocupa cada objeto en pantalla?
¿El tamaño de textura corresponde a ese uso?
¿El formato es el correcto para la plataforma?
¿Los mipmaps estan activos donde corresponde?
¿La UI quedo fuera de los mipmaps?
¿Hay texturas duplicadas?
¿Cuantas texturas lee cada material?
¿La compresion introduce artefactos visibles?
¿Se reviso la legibilidad de lo que comunica informacion?
¿Se comparo memoria y frame antes y despues?
```

---

## Regla final

El tamaño de una textura no se juzga en el explorador de archivos. Se juzga en pantalla.

```txt
La pregunta no es cuanto mide.
Es cuanta informacion visual
llega realmente al jugador.
Todo lo que sobra se paga igual.
```

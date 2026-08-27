## Proposito

Esta rama reune los problemas y las soluciones del tiempo de GPU en un videojuego.

No existe para bajar la calidad visual hasta que el numero cierre.
No existe para perseguir el contador de draw calls.
No existe para repetir que hay demasiados poligonos.

Existe para atacar el costo de dibujar el frame cuando el diagnostico confirmo que el limite esta en GPU.

---

## Idea central

La GPU procesa enormes cantidades de operaciones paralelas relacionadas con la representacion grafica.

De forma simplificada:

```txt
Geometria
→ procesamiento de vertices
→ rasterizacion
→ procesamiento de fragmentos / pixeles
→ imagen
```

Para optimizar GPU hay que entender que etapa esta generando el costo. No alcanza con decir que hay demasiados poligonos.

El error de fondo mas comun de esta rama es confundir cantidad de geometria con costo grafico:

```txt
una particula enorme puede tener 4 vertices
y cubrir media pantalla

un mesh de 50.000 vertices puede ocupar
30 pixeles a lo lejos
```

En muchisimos juegos el frame se define del lado de los pixeles, no del lado de los vertices.

---

## Rendering no es solo GPU

Esta es la aclaracion que gobierna toda la rama:

```txt
CPU   determina que objetos participan
      prepara informacion, materiales y estados
      arma y envia comandos
      draw calls

GPU   vertices
      rasterizacion
      fragmentos
      texturas
      iluminacion
      blending
```

Por lo tanto:

```txt
draw call NO es sinonimo de problema de GPU
```

Una cantidad enorme de draw calls puede producir principalmente presion sobre CPU, por la preparacion y el envio. Antes de atacarlos hay que saber de que lado duele.

---

## Cuando usar esta rama

Usar GPU cuando el diagnostico confirme que el frame esta limitado por GPU:

```txt
el frame es caro y la escena es visualmente rica
los scripts son triviales y el frame igual no entra
bajar la resolucion mejora el frame de forma notoria
mirar en una direccion cuesta mas que mirar en otra
el costo aparece con particulas, efectos o transparencias
apagar sombras o post processing cambia el frame
```

Si eso todavia no se midio, el camino es `Diagnostico`, no esta rama.

---

## Como debe usar esta rama una IA

Antes de proponer una solucion de GPU, una IA debe poder decir en que etapa esta el costo:

```txt
¿Es costo de vertices?      geometria, skinning, deformaciones, cantidad de objetos
¿Es costo de fragmentos?    resolucion, overdraw, shader por pixel, fullscreen
¿Es costo de envio?         draw calls, cambios de estado y material   (eso pega en CPU)
¿Es costo de pasadas?       sombras, luces, post processing
¿Es costo de memoria?       texturas, buffers, render targets           (eso es Memoria)
```

Una IA no debe razonar asi:

```txt
El juego va lento y hay muchos objetos.
→ bajar poligonos.
```

Debe razonar asi:

```txt
GPU Bound confirmado.
→ ¿bajar la resolucion cambia el frame? si → costo de fragmentos.
→ Frame Debugger: ¿que ocupa mas pasadas?
→ ¿hay capas de transparencia superpuestas?
→ candidata: reducir overdraw antes que reducir geometria.
→ validar con la misma escena y la misma camara.
```

---

## Problemas incluidos

### [[Overdraw y transparencias]]

El mismo pixel se dibuja varias veces porque hay capas superpuestas que la GPU tiene que combinar.

Consultar cuando el costo aparezca con particulas, humo, vegetacion, efectos o UI translucida.

### [[Fill rate y resolucion]]

Limite por capacidad de procesar y escribir pixeles, que escala con la cantidad de pixeles de pantalla.

Consultar cuando bajar la resolucion mejore el frame de forma notoria.

### [[Costo de fragmentos y shaders]]

Cuanto cuesta el shader por pixel, multiplicado por la cantidad de pixeles que cubre.

Consultar cuando un material barato sobre toda la pantalla pese mas que uno caro sobre un objeto chico.

### [[Costo de vertices y geometria]]

Cuanto cuesta procesar cada vertice y por que el triangle count no representa por si solo el costo grafico.

Consultar cuando haya meshes densos, skinning, deformaciones o muchisimos objetos.

### [[Sombras costosas]]

Las sombras necesitan informacion adicional de la escena y por eso son de las cosas mas caras del frame.

Consultar cuando apagar sombras cambie el frame de forma clara.

### [[Iluminacion en runtime]]

El intercambio entre calcular la luz durante la ejecucion y usar informacion precalculada.

Consultar cuando el costo escale con la cantidad de luces y de objetos afectados.

### [[Post processing pesado]]

Efectos que trabajan sobre una gran proporcion de los pixeles y escalan con la resolucion.

Consultar cuando el costo sea casi el mismo mire donde mire la camara.

---

## Soluciones incluidas

### [[LOD]]

Bajar el costo de algo a medida que baja su importancia perceptual, no solo cambiando mallas.

Consultar cuando haya muchos objetos a distintas distancias o importancias.

### [[Culling]]

Evitar el trabajo de lo que no contribuye: fuera de camara, tapado, o irrelevante para el jugador.

Consultar cuando se este pagando por cosas que no se ven.

### [[Draw calls y batching]]

Que es un draw call, por que cuesta, de que lado cuesta y cuando agrupar ayuda de verdad.

Consultar cuando haya muchos objetos distintos, muchos materiales o muchos cambios de estado.

### [[Texturas y mipmaps]]

Dimensiones, formato, compresion y mipmaps, y su efecto sobre memoria, bandwidth y sampling.

Consultar cuando haya texturas grandes, VRAM ajustada o aliasing a distancia.

---

## Como se conecta con otras ramas

```txt
Diagnostico             confirma que el limite es GPU y separa envio de dibujo
Fundamentos             frame budget, valor perceptual por costo, trade-offs
CPU                     la preparacion y el envio del rendering se pagan ahi
Memoria                 texturas, meshes, buffers y render targets ocupan VRAM
UI                      transparencias, mascaras y grandes superficies son GPU
Patrones transversales  LOD y culling son casos de escalado de precision y de Active Set
```

---

## Criterio de uso

En GPU, calidad y rendimiento se intercambian de forma directa:

```txt
Shadows
Resolution
LOD
Post Processing
Lighting
```

Todos permiten cambiar fidelidad visual por tiempo de GPU. Eso los vuelve tentadores y peligrosos a la vez: son la palanca mas rapida y tambien la mas facil de tirar de mas.

La pregunta que ordena la decision no es cuanto se ahorra.

```txt
¿Cuanto cuesta?
¿Cuanto de eso percibe el jugador?
```

Un efecto caro que nadie nota es el mejor candidato. Un efecto barato que sostiene la lectura del juego no se toca.

---

## Regla final

La GPU no se optimiza bajando calidad.

Se optimiza sabiendo que etapa esta saturada.

```txt
¿vertices, fragmentos, pasadas o envio?
→ atacar esa etapa
→ y recien ahi, si hace falta, negociar calidad
```

## Propósito

Esta rama reúne el **precio del arte**: cuánto cuesta en el juego corriendo una malla, un material, una textura, un esqueleto, un clip o una hoja de sprites, y cómo se baja sin pagar con lectura.

No existe para bajar polígonos por costumbre: la regla de la sección sigue siendo **primero se mide**.
No existe para juzgar si un asset está bien hecho: eso es criterio, y vive en `Principios de arte`.
No existe para reemplazar a GPU ni a Memoria: el arte cuesta en las dos, y por eso tiene rama propia, igual que la UI.

Existe porque el Optimizador del Área de Arte —el único que puede reducir geometría— aplicaba una ley (*cada asset entra en el presupuesto de su familia, medido en pantalla*) sin una sola nota de dónde sale el precio. Y del lado de la animación no había ninguna.

---

## Idea central

El costo del arte no está en el archivo: está **en pantalla**, multiplicado.

```txt
costo  =  lo que cuesta una vez  x  cuantas veces aparece  x  cuantas veces se procesa
          (caras, huesos, claves,   (instancias simultaneas)  (pasadas de sombra,
           pixeles)                                            cuadros por segundo)
```

817 caras no dicen nada. 817 caras por 20 goblins simultáneos son **16.340 caras en pantalla**, y se procesan otra vez por cada mapa de sombra que los toca. Ese es el número que decide.

---

## Tres cosas que se preguntan juntas y no son lo mismo

```txt
caras bien orientadas, malla      CORRECCION, no costo. Un asset con normales al reves
cerrada                           esta mal, no caro. Vive en Principios: Objetos 3D

poligonos, materiales, texturas   COSTO. Esta rama, Modelado

claves por tipo de animacion,     las DOS cosas:
curvas                            cuantas poses lleva una accion y que curva usar es
                                  OFICIO (Principios: 04 - Pose a pose, Curvas e
                                  interpolacion); cuantas claves se GUARDAN, cuantos
                                  huesos y cuanta compresion es COSTO: esta rama, Animacion
```

---

## Cuándo usar esta rama

Después del diagnóstico, nunca antes. Usar Arte cuando el diagnóstico apunte a:

```txt
el frame cae con muchos personajes o props en pantalla
bajar resolucion no mejora y bajar densidad de mallas si
el conteo de vertices del motor es mucho mayor que el del DCC
muchos draw calls de un mismo tipo de asset
la memoria de texturas o de animacion crece con cada asset nuevo
el CPU se va en animar personajes que nadie ve
```

Y antes del primer asset, para fijar el presupuesto de cada familia (Modo Escala del Área de Arte).

---

## Modelado

### [[Caras en pantalla]]

El costo de la geometría es caras por instancias simultáneas por pasadas. Es la ley 4 del Área de Arte con su precio escrito.

### [[Vertices partidos]]

Por qué el motor procesa más vértices de los que tiene la malla: aristas duras, costuras de UV y materiales parten cada vértice que tocan.

### [[Materiales por asset]]

Cada material es una llamada de dibujo aparte. Diez materiales en un goblin son diez llamadas de dibujo por goblin.

### [[Densidad de textura]]

Píxeles de textura por metro de superficie: la memoria que cuesta una textura y por qué todo el set tiene que tener la misma densidad.

---

## Animación

### [[Huesos e influencias]]

El costo del esqueleto: huesos que se evalúan e influencias por vértice que se deforman, por cada personaje animado.

### [[Claves por tipo de animacion]]

Cuántas claves se guardan de verdad —no cuántas puso el animador—, qué pesa cada tipo de clip y qué hace la compresión.

### [[Sprites en memoria]]

Una animación 2D es una pila de imágenes: cuadros por resolución por bytes por píxel.

### [[Animacion fuera de camara]]

Animar lo que nadie ve sigue costando CPU, salvo que se configure lo contrario. Y configurarlo mal detiene lo que el gameplay necesita que se mueva.

---

## Notas de otras ramas que también son de arte

No se repiten acá; se nombran: `Costo de vertices y geometria`, `LOD`, `Texturas y mipmaps`, `Draw calls y batching`, `Overdraw y transparencias` (todo efecto con partículas pasa por esta), `Sombras costosas`.

---

## Lo que esta rama no decide

El **presupuesto** no sale de acá: sale de la plataforma y la tasa de cuadros que el proyecto declara. Sin esa pregunta respondida, esta rama da precios y no puede decir si algo es caro. Es el hallazgo de `COMMIT-007`: *el trabajo de optimización tiene dueño; lo que no tiene dueño es el encargo*.

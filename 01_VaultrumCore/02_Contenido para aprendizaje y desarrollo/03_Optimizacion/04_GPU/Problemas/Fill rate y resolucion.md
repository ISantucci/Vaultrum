## Definicion

Fill rate representa la capacidad de la GPU de procesar y escribir pixeles.

Cuando una escena esta limitada por fill rate, el frame no depende de cuantos objetos hay sino de cuantos pixeles hay que resolver.

Lo que domina en ese caso:

```txt
Resolucion.
Transparencias.
Particulas.
Efectos fullscreen.
Shaders.
```

La cantidad de pixeles crece rapido:

```txt
1920 × 1080 ≈ 2,07 millones de pixeles
```

Y cada uno puede pasar por multiples operaciones.

Por eso subir la resolucion incrementa:

```txt
Fragment processing.
Bandwidth.
Post processing.
Buffers.
```

La idea principal es:

```txt
cantidad de pixeles
× operaciones por pixel
=
trabajo de fill rate
```

---

## Responsabilidad de esta nota

Esta nota no existe para pedir que se baje la resolucion.

Esta nota no existe para tratar el 4K como un error.

Esta nota no existe para reemplazar el analisis de geometria.

Esta nota no existe para discutir calidad visual.

Existe para reconocer un caso de bottleneck: el frame esta limitado por la cantidad de pixeles que hay que resolver, no por la escena.

Su responsabilidad es ayudar a responder:

```txt
¿El limite esta del lado de los pixeles?
```

El foco esta en:

```txt
cuantos pixeles se resuelven
cuanto cuesta cada uno
cuantas veces se toca el mismo
cuanto de eso escala con la resolucion
```

---

## Sintomas

Sintomas comunes:

```txt
El frame mejora mucho al bajar resolucion.
El frame empeora mucho al subirla.
Cambiar la calidad grafica cambia el rendimiento.
El costo no baja al reducir poligonos.
El costo no baja al reducir objetos.
Pantalla completa rinde peor que ventana chica.
Peor rendimiento en monitores grandes.
```

Un patron caracteristico:

```txt
Escena identica
+ resolucion mayor
→ frame mucho mas caro
```

La escena no cambio. Cambio cuanto hay que pintar.

---

## Que parte del software suele causarlo

Suele aparecer en:

```txt
Resolucion de render mal configurada.
Render scale al 100% en hardware modesto.
Efectos fullscreen encadenados.
Particulas grandes.
Capas transparentes.
Shaders costosos aplicados a superficies grandes.
Buffers intermedios de alta resolucion.
Cielos y fondos con shaders pesados.
UI a pantalla completa.
```

Tambien lo causa el render a resolucion nativa cuando el juego podria renderizar por debajo y escalar.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
GPU
Fragment processing
Ancho de banda de memoria
Memoria de video
```

Cada buffer a resolucion completa ocupa memoria y consume bandwidth al leerse y escribirse.

Por eso el problema se agrava en:

```txt
Hardware integrado.
Mobile.
Notebooks.
Monitores de alta resolucion.
```

En esos casos el limite suele estar en pixeles antes que en geometria.

---

## Como detectarlo

La prueba diagnostica canonica es bajar la resolucion y comparar.

```txt
Bajar resolucion
→ mejora mucho
→ el limite esta del lado de los pixeles.

Bajar resolucion
→ casi no cambia
→ buscar en geometria, draw calls o CPU.
```

Esta prueba es barata, reversible y no requiere tocar contenido.

Preguntas practicas:

```txt
¿A que resolucion se esta midiendo?
¿Cual es la resolucion objetivo real?
¿Hay render scale configurable?
¿El frame escala con el area de pantalla?
¿Cuantos efectos fullscreen hay activos?
¿El hardware objetivo tiene este ancho de banda?
```

---

## Herramientas de deteccion

Herramientas utiles:

```txt
→ Frame debugger
→ Stats window
→ Unity Profiler
→ Herramientas de GPU profiling del fabricante
```

Que mirar:

```txt
Tiempo de GPU frente a tiempo de CPU.
Resolucion de los render targets.
Cantidad de passes fullscreen.
Memoria de render targets.
Escalado del frame al cambiar resolucion.
```

Una comparacion util:

```txt
Medir a resolucion objetivo.
Medir a la mitad.
Comparar frame time.
```

---

## Soluciones posibles

Soluciones candidatas dentro de la rama GPU:

```txt
LOD
Culling
Draw calls y batching
Texturas y mipmaps
```

Soluciones especificas del problema:

```txt
Bajar render scale.
Renderizar por debajo de la nativa y escalar.
Reducir efectos fullscreen.
Reducir resolucion de buffers intermedios.
Simplificar shaders de superficies grandes.
Reducir capas transparentes.
Ofrecer presets de calidad al jugador.
Bajar resolucion de sombras y reflejos.
```

Y desde otras ramas:

```txt
Comparacion antes y despues
UI orientada a eventos
```

Ejemplo:

```txt
Antes:
Render al 100% en hardware modesto.

Despues:
Render al 75% con escalado, sin cambiar contenido.
```

Otro ejemplo:

```txt
Antes:
Tres efectos fullscreen encadenados.

Despues:
Un efecto fullscreen y el resto localizado.
```

---

## Trade-offs

```txt
Bajar render scale
→ mucho menos costo
→ imagen mas blanda.

Menos efectos fullscreen
→ frame mas barato
→ menos identidad visual.

Buffers a menor resolucion
→ menos bandwidth
→ mas artefactos en bordes.

Presets de calidad
→ el jugador elige
→ mas configuraciones que probar.

Escalado con reconstruccion
→ buena imagen a menor costo
→ mas complejidad tecnica.
```

La resolucion es la palanca mas fuerte y la mas visible.

Conviene usarla con criterio, no como primer reflejo.

---

## Ejemplo en videojuegos

En un Tower Defense:

```txt
Mapa fijo visto desde arriba.
Torres y enemigos chicos en pantalla.
Niebla cubriendo el escenario.
Efectos de disparo constantes.
HUD de dinero, vida y wave.
```

La escena es simple. Pocos objetos, poca geometria.

Y aun asi el juego cae en una notebook.

Al medir:

```txt
Bajar resolucion a la mitad
→ el frame se duplica.
```

Confirmado: el limite esta en pixeles.

El culpable no es la cantidad de torres.

```txt
Niebla sobre toda la pantalla
+ bloom fullscreen
+ HUD translucido
=
cada pixel tocado varias veces
```

La solucion no fue sacar torres.

```txt
Render scale al 80%.
Niebla mas liviana.
Bloom solo en presets altos.
```

---

## Como guia el diagnostico

Flujo recomendado:

```txt
Sintoma:
frame caro sin escena compleja.

Sospecha:
limite de fill rate.

Medicion:
comparar frame time a dos resoluciones.

Dato esperado:
mejora proporcional al bajar resolucion.

Confirmacion:
GPU alta, CPU normal.

Solucion candidata:
render scale, efectos fullscreen, transparencias.
```

Esta es la prueba mas rapida de toda la rama GPU.

La pregunta clave es:

```txt
¿El frame escala con la cantidad de pixeles?
```

---

## Errores comunes al intentar solucionarlo

```txt
Reducir poligonos cuando el limite es de pixeles.
Bajar resolucion sin avisar al jugador.
Medir en ventana chica y publicar a pantalla completa.
Medir en una maquina de desarrollo potente.
Confundir mejora por resolucion con mejora por contenido.
Bajar resolucion y no volver a medir.
Aplicar un preset unico a todo el hardware.
```

Ejemplo de mala solucion:

```txt
Problema:
Cae en notebooks.

Solucion:
Se reduce el detalle de los modelos.

Resultado:
El frame no cambia. El limite eran los pixeles.
```

Se trabajo sobre la etapa equivocada.

---

## Hacia donde seguir

Si hace falta entender que significa estar limitado por un recurso:

→ [[Fundamentos]]

Si hace falta confirmar que el frame esta limitado por GPU:

→ [[Diagnostico]]

Si los buffers de alta resolucion presionan memoria:

→ [[Memoria]]

Si la UI cubre toda la pantalla:

→ [[UI]]

Si al bajar resolucion el frame no mejora:

→ [[CPU]]

Herramientas para confirmar:

```txt
→ Frame debugger
→ Stats window
→ Unity Profiler
→ Comparacion antes y despues
```

Notas hermanas de esta rama:

```txt
→ Overdraw y transparencias
→ Costo de fragmentos y shaders
→ Post processing pesado
```

---

## Checklist de diagnostico

```txt
¿A que resolucion se midio?
¿Bajar resolucion mejora el frame?
¿La mejora es proporcional al area?
¿Cual es la resolucion objetivo real?
¿Hay render scale disponible?
¿Cuantos efectos fullscreen hay?
¿Hay buffers intermedios a resolucion completa?
¿Los shaders grandes son costosos?
¿Se midio en el hardware objetivo?
¿Se midio a pantalla completa?
¿Hay presets de calidad?
¿Se comparo antes y despues?
```

---

## Regla final

La resolucion no es un ajuste cosmetico. Es una multiplicacion.

```txt
Si el frame mejora al bajar resolucion,
el problema no esta en la escena.
Esta en la cantidad de pixeles
que hay que resolver.
```

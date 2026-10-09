## Definicion

Despues de rasterizar la geometria, la GPU procesa fragmentos.

Cada fragmento es un candidato a pixel, y cada uno ejecuta el fragment shader del material que lo cubre.

La relacion conceptual es:

```txt
cantidad de pixeles procesados
× costo del fragment shader
× cantidad de veces que se procesan
```

Esto puede ser muchisimo mas importante que el numero de poligonos.

Un fragment shader puede incluir:

```txt
Calculos matematicos.
Texture sampling.
Iluminacion.
Branches.
Blending.
Multiples efectos.
```

Y aca esta el punto que casi siempre se malinterpreta:

```txt
shader complejo = malo
```

no es cierto.

El costo real depende de cuantas veces se ejecuta:

```txt
Shader caro sobre un objeto chico
→ puede no importar.

Shader barato sobre toda la pantalla
→ puede dominar el frame.
```

---

## Responsabilidad de esta nota

Esta nota no existe para simplificar todos los shaders.

Esta nota no existe para contar instrucciones.

Esta nota no existe para prohibir efectos visuales.

Esta nota no existe para reemplazar el analisis de overdraw o resolucion.

Existe para separar dos cosas que se confunden: cuanto cuesta un shader y cuantas veces se ejecuta.

Su responsabilidad es ayudar a responder:

```txt
¿Cuanto cuesta este shader multiplicado por su area en pantalla?
```

El foco esta en:

```txt
que hace el shader
cuantos pixeles cubre
cuantas capas lo ejecutan
si ese costo se justifica visualmente
```

---

## Sintomas

Sintomas comunes:

```txt
El frame cae al mirar hacia ciertos materiales.
El frame cae al acercarse a una superficie.
Bajar resolucion mejora mucho el rendimiento.
El costo no baja al reducir poligonos.
Un material especifico aparece caro al desactivarlo.
Cielos, agua o terrenos grandes pesan mucho.
El costo sube al ocupar mas pantalla, no al haber mas objetos.
```

Un patron caracteristico:

```txt
Objeto lejos, chico en pantalla
→ barato.

El mismo objeto llenando la pantalla
→ caro.
```

El shader no cambio. Cambio cuantas veces corre.

---

## Que parte del software suele causarlo

Suele aparecer en:

```txt
Materiales con muchos texture samples.
Shaders con iluminacion por pixel.
Shaders con branches por fragmento.
Materiales de agua, cielo o terreno.
Efectos de distorsion y refraccion.
Materiales transparentes apilados.
Shaders reutilizados sin variantes baratas.
Materiales de UI a pantalla completa.
```

El patron tecnico habitual:

```txt
shader pensado para un objeto hero
+ aplicado a superficies enormes
```

Tambien lo causa mantener un unico shader de maxima calidad para todas las distancias.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
GPU
Fragment processing
Unidades de textura
Ancho de banda de memoria
```

El texture sampling merece atencion propia: leer texturas es una de las operaciones mas caras dentro de un fragment shader.

Tambien puede afectar:

```txt
Memoria de video
```

cuando el shader necesita varias texturas grandes simultaneas.

En hardware modesto el costo por fragmento pesa mucho mas que la geometria.

---

## Como detectarlo

La deteccion parte de aislar el material sospechado.

```txt
Reemplazar el material por uno simple
→ el frame mejora
→ el shader era parte del problema.

Reemplazar el material por uno simple
→ el frame no cambia
→ buscar en otra etapa.
```

Complementar bajando resolucion: si el frame escala con los pixeles, el costo esta del lado de los fragmentos.

Preguntas practicas:

```txt
¿Que porcentaje de pantalla cubre este material?
¿Cuantos texture samples hace?
¿Tiene iluminacion por pixel?
¿Se ejecuta sobre capas superpuestas?
¿Necesita esta calidad a esta distancia?
¿Existe una variante mas barata?
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
Passes por material.
Cantidad de shader variants.
Materiales activos en el frame.
Area en pantalla de cada material.
Tiempo de GPU frente a tiempo de CPU.
Cambios de shader y de estado.
```

Una prueba util:

```txt
Cambiar un material por uno unlit.
Medir.
Comparar.
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
Simplificar el shader de superficies grandes.
Reducir texture samples.
Evitar branches costosos por fragmento.
Precalcular en textura lo que no cambia.
Usar variantes baratas a distancia.
Usar shaders unlit donde la luz no aporta.
Mover calculos de fragmento a vertice cuando alcanza.
Limitar el area de pantalla del efecto.
```

Y desde otras ramas:

```txt
Comparacion antes y despues
Cuando NO optimizar
```

Ejemplo:

```txt
Antes:
Shader de terreno con 6 texturas y luz por pixel, cubriendo toda la pantalla.

Despues:
Version reducida a 3 texturas para distancias medias y lejanas.
```

Otro ejemplo:

```txt
Antes:
Un unico shader de agua para todo el mapa.

Despues:
Agua detallada cerca de la camara, version simple lejos.
```

---

## Trade-offs

```txt
Shader simplificado
→ menos costo por fragmento
→ menos riqueza visual.

Menos texture samples
→ menos bandwidth
→ menos detalle de superficie.

Precalcular en textura
→ menos calculo en runtime
→ mas memoria y menos dinamismo.

Calculo en vertice
→ mucho mas barato
→ resultado menos preciso.

Variantes por distancia
→ costo proporcional a la importancia
→ mas materiales que mantener.
```

Un shader no se juzga por su complejidad interna.

Se juzga por su complejidad multiplicada por su superficie.

---

## Ejemplo en videojuegos

En un Tower Defense:

```txt
Piso del mapa con shader de terreno.
Rango de torre dibujado sobre el piso.
Niebla ambiental.
Efectos de disparo y explosion.
HUD translucido.
```

El shader de terreno se escribio pensando en una torre vista de cerca.

Pero el piso ocupa casi toda la pantalla todo el tiempo.

```txt
Torre hero
→ 3% de pantalla
→ shader caro justificado.

Piso del mapa
→ 80% de pantalla
→ el mismo shader domina el frame.
```

El mismo costo unitario, dos consecuencias completamente distintas.

Una solucion sana:

```txt
Shader completo para torres y enemigos.
Shader reducido para el piso.
Rango de torre con material simple.
```

El jugador mira las torres. No audita el terreno.

---

## Como guia el diagnostico

Flujo recomendado:

```txt
Sintoma:
frame caro con pocos objetos.

Sospecha:
costo por fragmento.

Medicion:
reemplazar material por uno simple.

Dato esperado:
mejora clara al simplificar.

Confirmacion:
el costo escala con el area en pantalla.

Solucion candidata:
variantes mas baratas segun distancia y superficie.
```

La pregunta clave es:

```txt
¿Cuantas veces por frame corre este shader?
```

---

## Errores comunes al intentar solucionarlo

```txt
Simplificar todos los shaders por igual.
Optimizar el shader de un objeto chico.
Contar instrucciones sin mirar area en pantalla.
Suponer que un shader visual es automaticamente caro.
Romper la identidad visual del juego por unos ms.
Cambiar shaders sin volver a medir.
Ignorar que el mismo shader corre en varias capas.
```

Ejemplo de mala solucion:

```txt
Problema:
GPU alta.

Solucion:
Se simplifica el shader del personaje principal.

Resultado:
El frame no cambia. El costo estaba en el fondo.
```

Se optimizo lo visible, no lo caro.

---

## Hacia donde seguir

Si hace falta entender el concepto de costo por frecuencia:

→ [[Fundamentos]]

Si hace falta confirmar que el frame esta limitado por GPU:

→ [[Diagnostico]]

Si el shader depende de texturas grandes:

→ [[Memoria]]

Si el material es de UI a pantalla completa:

→ [[UI]]

Si el patron se repite en otras etapas:

→ [[Patrones transversales]]

Herramientas para confirmar:

```txt
→ Frame debugger
→ Stats window
→ Unity Profiler
```

Notas hermanas de esta rama:

```txt
→ Fill rate y resolucion
→ Overdraw y transparencias
→ Post processing pesado
```

---

## Checklist de diagnostico

```txt
¿Que area de pantalla cubre este material?
¿Cuantos texture samples hace el shader?
¿Tiene iluminacion por pixel?
¿Hay branches por fragmento?
¿Se ejecuta sobre capas superpuestas?
¿Existe una variante mas barata?
¿Se probo con un material simple?
¿El frame mejoro al simplificar?
¿Bajar resolucion tambien mejora?
¿El costo se justifica visualmente?
¿Se puede resolver en vertice?
¿Se comparo antes y despues?
```

---

## Regla final

Un shader no es caro o barato. Es caro o barato por la cantidad de veces que corre.

```txt
Costo del shader
× area en pantalla
× capas superpuestas
=
lo que realmente paga la GPU.
```

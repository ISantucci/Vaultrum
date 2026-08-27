## Definicion

La geometria tiene costo. Cada vertice debe pasar por procesamiento antes de que exista un solo pixel.

La relacion conceptual es:

```txt
cantidad de vertices
× costo por vertex
```

Los conceptos que entran en juego:

```txt
Vertices.
Triangles.
Meshes.
Objetos.
Transformaciones.
```

Este costo importa especialmente con:

```txt
Meshes densos.
Deformaciones.
Skinning.
Grandes cantidades de objetos.
```

Y aca aparece el error mas frecuente de toda la rama grafica:

```txt
pensar que el triangle count
representa por si solo
el costo grafico
```

No lo representa.

Segun el juego puede pesar mucho mas:

```txt
Cantidad de objetos.
Draw calls.
Shader.
Pixeles.
Overdraw.
Luces.
Sombras.
```

---

## Responsabilidad de esta nota

Esta nota no existe para poner un limite de poligonos.

Esta nota no existe para justificar reducir todos los modelos.

Esta nota no existe para tratar el triangle count como metrica principal.

Esta nota no existe para reemplazar el analisis de fragmentos o de draw calls.

Existe para ubicar la geometria en su lugar real: es una de varias fuentes de costo, y muchas veces no es la dominante.

Su responsabilidad es ayudar a responder:

```txt
¿El limite esta en la etapa de vertices?
```

El foco esta en:

```txt
cuantos vertices se procesan
cuantas veces se procesan
cuanto cuesta cada uno
si la geometria es realmente el limite
```

---

## Sintomas

Sintomas comunes:

```txt
El frame cae con muchos personajes animados en pantalla.
El frame cae en escenas con vegetacion densa.
Bajar resolucion casi no mejora el rendimiento.
Reducir el detalle de los modelos mejora bastante.
El costo escala con la cantidad de objetos visibles.
Escenas con mucha malla y poca pantalla cubierta pesan igual.
Las sombras multiplican el problema.
```

Un patron caracteristico:

```txt
Un mesh denso
→ apenas se nota.

Doscientos meshes densos animados
→ se nota mucho.
```

Aca el costo si escala con la cantidad, no con el area.

---

## Que parte del software suele causarlo

Suele aparecer en:

```txt
Modelos importados sin reduccion.
Personajes con skinning y muchos huesos.
Vegetacion y follaje.
Props repetidos en gran cantidad.
Meshes de alta densidad usados a distancia.
Falta de LOD.
Blend shapes y deformaciones.
Colliders visuales innecesariamente detallados.
```

El patron tecnico habitual:

```txt
asset de alta calidad
+ usado a cualquier distancia
+ multiplicado por muchas instancias
```

Tambien lo causa procesar la misma geometria varias veces por pass, por ejemplo al proyectar sombras.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
GPU
Vertex processing
Ancho de banda de memoria
Memoria de video
```

Cada mesh ocupa memoria y debe leerse para procesarse. Meshes muy densos presionan bandwidth ademas de calculo.

Tambien puede afectar:

```txt
CPU
```

cuando el skinning o la preparacion de la geometria se resuelven del lado del procesador, o cuando muchos objetos generan muchas draw calls.

Por eso geometria y draw calls suelen aparecer juntos, pero no son el mismo problema.

---

## Como detectarlo

La deteccion combina dos pruebas cruzadas.

```txt
Bajar resolucion
→ no mejora
→ el limite no esta en pixeles.

Reducir densidad de mallas
→ mejora
→ el limite esta en vertices.
```

Esa combinacion es la que separa geometria de fragmentos.

Preguntas practicas:

```txt
¿Cuantos objetos hay en pantalla?
¿Cuantos vertices tiene el peor mesh?
¿Hay LOD configurado?
¿Cuantos objetos usan skinning?
¿Cuantos passes procesan esta geometria?
¿La densidad se justifica a esta distancia?
```

---

## Herramientas de deteccion

Herramientas utiles:

```txt
→ Stats window
→ Frame debugger
→ Unity Profiler
→ Herramientas de GPU profiling del fabricante
```

Que mirar:

```txt
Cantidad de tris y verts.
Cantidad de batches.
Objetos renderizados.
Passes que reprocesan geometria.
Costo de skinning.
Tiempo de GPU frente a tiempo de CPU.
```

Una lectura util:

```txt
Stats window
→ tris y verts por frame
→ comparar mirando distintas zonas
```

Si el contador sube fuerte y el frame tambien, hay una pista.

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
Reducir densidad de mallas.
Configurar niveles de detalle por distancia.
Usar impostores o billboards a distancia.
Reducir cantidad de huesos en skinning.
Combinar props estaticos repetidos.
Limitar objetos que proyectan sombra.
Eliminar geometria interna que nunca se ve.
Reducir instancias de vegetacion lejana.
```

Y desde otras ramas:

```txt
Object pool como optimizacion
Addressables como metodologia de optimizacion
Comparacion antes y despues
```

Ejemplo:

```txt
Antes:
Un enemigo de 40.000 triangulos, usado a cualquier distancia.

Despues:
Version detallada cerca, version media a media distancia, silueta simple lejos.
```

Otro ejemplo:

```txt
Antes:
Cada arbol es un mesh denso independiente.

Despues:
Arboles lejanos como billboards, cercanos con mesh completo.
```

---

## Trade-offs

```txt
Menos densidad de malla
→ menos vertex cost
→ siluetas menos definidas.

Niveles de detalle
→ costo proporcional a la distancia
→ posibles saltos visibles al cambiar.

Billboards a distancia
→ muy barato
→ se rompe al acercarse.

Menos huesos
→ skinning mas barato
→ animacion menos expresiva.

Combinar props
→ menos objetos
→ peor culling y menos flexibilidad.
```

Combinar geometria para bajar draw calls puede aumentar la cantidad de vertices procesados.

Optimizar una etapa puede cargar otra.

---

## Ejemplo en videojuegos

En un Tower Defense:

```txt
30 torres construidas.
300 enemigos avanzando por el camino.
Proyectiles en vuelo.
Decoracion del mapa.
HUD de dinero, vida y wave.
```

Los enemigos son modelos animados con skinning.

Con una wave chica no se nota nada.

```txt
300 enemigos
× mesh denso
× skinning
× pass de sombra
```

El mismo enemigo se procesa una vez para la camara y otra vez para la sombra.

Al medir, bajar resolucion no cambia nada. Reducir la densidad de los enemigos si.

La solucion no fue reducir la wave.

```txt
Enemigo detallado solo cerca de la camara.
Version media para el resto del camino.
Sombra solo para los enemigos cercanos.
Decoracion lejana con menos densidad.
```

El jugador cuenta enemigos. No cuenta triangulos.

---

## Como guia el diagnostico

Flujo recomendado:

```txt
Sintoma:
caida con muchos objetos en pantalla.

Sospecha:
costo de vertices.

Medicion:
bajar resolucion y comparar.

Dato esperado:
poca o nula mejora.

Segunda medicion:
reducir densidad de mallas.

Dato esperado:
mejora clara.

Solucion candidata:
niveles de detalle y control de sombras.
```

La pregunta clave es:

```txt
¿El costo escala con la cantidad o con el area?
```

---

## Errores comunes al intentar solucionarlo

```txt
Tratar el triangle count como la unica metrica.
Reducir poligonos cuando el limite era de pixeles.
Combinar todo en un mesh gigante y romper el culling.
Configurar distancias de detalle sin probar en gameplay.
Bajar densidad hasta arruinar la silueta.
Olvidar que las sombras reprocesan la misma geometria.
Optimizar geometria sin medir la etapa real.
```

Ejemplo de mala solucion:

```txt
Problema:
GPU alta con muchos efectos.

Solucion:
Se reducen todos los modelos a la mitad.

Resultado:
El juego se ve peor y rinde igual. El costo era overdraw.
```

Se pago calidad sin comprar rendimiento.

---

## Hacia donde seguir

Si hace falta entender por que una metrica no alcanza:

→ [[Fundamentos]]

Si hace falta identificar la etapa limitante:

→ [[Diagnostico]]

Si el skinning aparece del lado del procesador:

→ [[CPU]]

Si los meshes densos presionan memoria:

→ [[Memoria]]

Si los modelos se cargan y descargan por escena:

→ [[Carga e IO]]

Herramientas para confirmar:

```txt
→ Stats window
→ Frame debugger
→ Unity Profiler
```

Notas hermanas de esta rama:

```txt
→ Sombras costosas
→ Fill rate y resolucion
→ Costo de fragmentos y shaders
```

---

## Checklist de diagnostico

```txt
¿Cuantos objetos hay en pantalla?
¿Cuantos tris y verts reporta el frame?
¿Bajar resolucion mejora el frame?
¿Reducir densidad de mallas mejora el frame?
¿Hay niveles de detalle configurados?
¿Cuantos objetos usan skinning?
¿Cuantos passes reprocesan la geometria?
¿Hay geometria interna que nunca se ve?
¿La densidad se justifica a esa distancia?
¿Combinar objetos rompio el culling?
¿La silueta sigue siendo legible?
¿Se comparo antes y despues?
```

---

## Regla final

El triangle count es un dato, no un diagnostico.

```txt
Muchos triangulos pueden ser gratis.
Pocos triangulos pueden ser carisimos.
Lo que decide es la etapa
que realmente esta limitando el frame.
```

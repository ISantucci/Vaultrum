## Definicion

Antes de cualquier otra cosa hay que aclarar algo que se malinterpreta constantemente: rendering involucra a los dos procesadores.

```txt
CPU
determina que objetos participan
prepara informacion
materiales
estados
comandos
draw calls
```

```txt
GPU
vertices
rasterizacion
fragmentos
texturas
iluminacion
blending
```

Por eso:

```txt
draw call
≠
problema de GPU
```

Una cantidad enorme de draw calls puede producir principalmente presion sobre CPU, por la preparacion y el envio de cada uno.

Un draw call es conceptualmente un pedido:

```txt
CPU
→ "dibuja este objeto con este estado y este material"
→ GPU
```

Cada envio tiene overhead. Batching es la tecnica que intenta agrupar esos pedidos cuando son compatibles.

---

## Que problema ayuda a prevenir

Ayuda principalmente con:

```txt
Tiempo de CPU gastado en preparar el frame
Overhead de envio por objeto
Cambios de material y de estado constantes
Frames caros con escenas visualmente simples
```

El sintoma tipico que delata este caso:

```txt
La escena se ve pobre.
El contador de draw calls es enorme.
Bajar resolucion no mejora nada.
El limite esta del lado de la preparacion.
```

Ese ultimo punto es el que suele confundir: se busca el problema en la GPU y estaba en la CPU.

---

## Como funciona

Batching agrupa trabajo de rendering compatible.

```txt
En vez de:
Draw A
Draw B
Draw C
Draw D

intentar:
Draw ABCD
```

El objetivo es directo:

```txt
menos overhead de envio
```

Pero la compatibilidad no es opcional. Para agrupar hace falta que el trabajo se parezca lo suficiente.

```txt
Mismo material.
Mismo estado de render.
Mismas propiedades relevantes.
Condiciones que el motor pueda aprovechar.
```

Y lo que rompe la agrupacion:

```txt
Cambiar de material entre objetos.
Cambiar estado permanentemente.
Propiedades unicas por instancia.
Orden de dibujado forzado.
Transparencias que obligan a ordenar por profundidad.
```

De ahi que compartir materiales pueda ayudar. Compartir no significa uniformar todo el juego.

---

## Como aplicarlo en videojuegos

En un Tower Defense el caso claro es el mapa.

```txt
Antes:
200 tiles del recorrido
→ cada uno con su material
→ 200 envios.

Despues:
200 tiles compartiendo material y atlas
→ agrupados
→ muchos menos envios.
```

Las torres repetidas siguen el mismo criterio:

```txt
Torres del mismo tipo y nivel
→ mismo material
→ candidatas a agruparse.

Torre seleccionada con material de resaltado
→ queda fuera del grupo
→ y esta bien, es una sola.
```

El HUD merece atencion aparte:

```txt
Dinero, vida y wave
→ elementos chicos
→ pero cada cambio de textura o de material
→ puede cortar la agrupacion de la UI.
```

Un atlas de iconos suele resolver mas draw calls de UI que cualquier ajuste en la escena.

---

## Relacion con arquitectura

Este tema toca produccion y autoria mas que codigo.

```txt
Decisiones de arte
→ materiales
→ atlas
→ variantes

Decisiones de escena
→ agrupacion
→ jerarquia
→ que es estatico y que se mueve
```

La arquitectura ayuda cuando permite responder rapido:

```txt
¿Quien crea este objeto?
¿Con que material?
¿Cuantas variantes de material existen?
¿Se puede reutilizar una en vez de crear otra?
```

Un sistema de spawn que instancia material nuevo por entidad multiplica envios sin que nadie lo note hasta que la wave crece.

```txt
Material por instancia
→ imposible de agrupar
→ y ademas memoria extra.
```

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
CPU
GPU
Ancho de banda
```

El reparto suele ser asimetrico:

```txt
Muchos draw calls
→ presion sobre CPU.

Mucha geometria dentro de cada draw call
→ presion sobre GPU.
```

Por eso el efecto de batching no siempre es una mejora limpia:

```txt
Menos envios
→ menos CPU.

Objetos combinados en una sola malla
→ el culling deja de descartarlos por separado
→ mas geometria procesada
→ mas GPU.
```

Bajar un contador y subir el frame time es un resultado perfectamente posible.

---

## Cuando conviene usarlo

Conviene cuando:

```txt
Se midio y el limite esta en CPU.
El costo de rendering aparece en preparacion.
Hay muchisimos objetos chicos y repetidos.
Muchos objetos comparten material o pueden compartirlo.
Los objetos no se mueven de forma independiente.
El contador de envios crece con la escena.
```

Casos claros:

```txt
Tiles y props del escenario.
Vegetacion repetida.
Iconos de UI.
Elementos decorativos estaticos.
Enemigos identicos en gran cantidad.
```

---

## Cuando NO conviene usarlo

No conviene cuando:

```txt
El limite estaba en GPU.
Hay pocos objetos en escena.
Los objetos necesitan cullearse por separado.
Cada objeto se mueve por su cuenta.
Combinar obliga a duplicar mallas en memoria.
El unico argumento es bajar un contador.
```

Y hay un limite que no se cruza:

```txt
No corresponde sacrificar el diseño visual
para minimizar una metrica.
```

Si el juego se ve peor y el frame no mejora, no hubo optimizacion.

---

## Trade-offs

```txt
Menos draw calls
→ menos overhead de CPU
→ posible perdida de culling.

Materiales compartidos
→ mejor agrupacion
→ menos variedad visual.

Mallas combinadas
→ menos envios
→ mas memoria y menos flexibilidad.

Atlas de texturas
→ menos cambios de estado
→ mas trabajo de autoria y menos modularidad.

Objetos marcados como estaticos
→ agrupacion previa
→ dejan de poder moverse.
```

---

## Riesgos de aplicarlo mal

Riesgos comunes:

```txt
Tratar la cantidad de draw calls como objetivo.
Combinar objetos que estaban bien cullados.
Duplicar mallas en memoria para ganar envios.
Unificar materiales y arruinar la lectura visual.
Optimizar envios cuando el limite era de fragmentos.
Marcar como estatico algo que despues necesita moverse.
Crear instancias de material sin darse cuenta.
No volver a medir el frame completo.
```

Ejemplo:

```txt
Antes:
400 props del escenario, 400 envios.

Decision:
Combinar todo en una sola malla gigante.

Resultado:
40 envios, pero el mapa entero se procesa
aunque la camara mire un rincon.
```

El contador mejoro. El frame empeoro.

---

## Checklist de implementacion

```txt
¿Se midio antes de tocar nada?
¿El limite esta en CPU o en GPU?
¿Cuantos envios hay y de que son?
¿Se recorrio el frame paso a paso?
¿Que esta rompiendo la agrupacion?
¿Los objetos combinados se pueden seguir culleando?
¿Cuanta memoria agrega la combinacion?
¿Se crearon instancias de material sin querer?
¿La UI usa atlas?
¿El diseño visual se mantiene?
¿Bajo el frame time o solo el contador?
¿Se comparo antes y despues?
```

---

## Regla final

Los draw calls son una metrica de preparacion, no un diagnostico de GPU.

```txt
Reducir envios es un medio.
El objetivo es el frame time.
Un contador mas bajo
con un frame mas caro
es una optimizacion fallida.
```

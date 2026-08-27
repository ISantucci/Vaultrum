## Definicion

La iluminacion puede representar una parte importante del costo grafico.

La distincion fundamental no es entre luces buenas y malas. Es entre cuando se hace el calculo:

```txt
Calculo en runtime
→ mayor flexibilidad
→ mayor costo durante ejecucion.

Informacion precalculada
→ menos calculo en runtime
→ trade-offs en memoria,
  tiempo de preparacion
  y dinamismo.
```

No hay una opcion universal.

La respuesta depende de cuanto necesita cambiar la escena.

El costo en runtime crece por dos ejes:

```txt
costo por luz
× cantidad de objetos afectados
```

Una luz sola es barata. Una luz que alcanza a doscientos objetos, no.

```txt
Escena estatica e iluminacion fija
→ precalcular tiene mucho sentido.

Escena que cambia constantemente
→ precalcular sirve poco.
```

---

## Responsabilidad de esta nota

Esta nota no existe para limitar la cantidad de luces.

Esta nota no existe para imponer iluminacion precalculada.

Esta nota no existe para discutir estilo visual.

Esta nota no existe para reemplazar el analisis de sombras.

Existe para plantear una decision de ingenieria: que parte de la iluminacion necesita resolverse mientras el juego corre y que parte puede resolverse antes.

Su responsabilidad es ayudar a responder:

```txt
¿Cuanto de esta iluminacion necesita ser dinamica?
```

El foco esta en:

```txt
cuantas luces hay
cuantos objetos alcanza cada una
que necesita cambiar en runtime
que podria resolverse antes
```

---

## Sintomas

Sintomas comunes:

```txt
El frame cae al agregar luces a la escena.
El costo escala con la cantidad de luces.
El costo escala con objetos dentro del rango de luz.
Zonas muy iluminadas rinden peor que zonas oscuras.
Cambiar el modo de una luz cambia el rendimiento.
El frame mejora al reducir el rango de las luces.
Escenas simples rinden mal por iluminacion.
```

Un patron caracteristico:

```txt
Luz con rango chico
→ pocos objetos afectados
→ barata.

La misma luz con rango grande
→ muchos objetos afectados
→ cara.
```

La luz no cambio. Cambio a cuantos alcanza.

---

## Que parte del software suele causarlo

Suele aparecer en:

```txt
Muchas luces dinamicas superpuestas.
Luces con rango excesivo.
Luces dinamicas sobre geometria que nunca se mueve.
Antorchas, faroles y efectos con luz propia.
Proyectiles y explosiones que crean luces.
Iluminacion en runtime donde la escena es estatica.
Materiales que responden a varias luces por pixel.
Falta de criterio entre luz importante y luz decorativa.
```

El patron tecnico habitual:

```txt
cada elemento visual
+ su propia luz dinamica
+ sin control de rango
```

Tambien lo causa no distinguir entre luz que define la escena y luz que solo decora.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
GPU
Fragment processing
Ancho de banda de memoria
```

Cada luz que alcanza a un objeto agrega calculo al procesar sus fragmentos, y en algunos casos passes adicionales.

Tambien puede afectar:

```txt
CPU
Memoria
```

El procesador debe determinar que luces afectan a que objetos y preparar esa informacion cada frame.

La iluminacion precalculada mueve ese costo a memoria y a tiempo de preparacion antes de ejecutar.

---

## Como detectarlo

La deteccion parte de apagar luces por grupos y comparar.

```txt
Apagar luces decorativas
→ mejora clara
→ el costo estaba en cantidad de luces.

Apagar luces decorativas
→ poca diferencia
→ buscar en sombras, fragmentos o resolucion.
```

Segunda prueba: reducir el rango de las luces sin apagarlas. Si el frame mejora, el problema es cuantos objetos alcanzan.

Preguntas practicas:

```txt
¿Cuantas luces afectan al mismo objeto?
¿Que rango tiene cada luz?
¿Cuales luces se mueven realmente?
¿Cuales iluminan geometria estatica?
¿Cuales son decorativas?
¿La escena cambia lo suficiente para justificar runtime?
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
Cantidad de luces activas.
Passes por luz.
Objetos afectados por cada luz.
Rango y superposicion de luces.
Rendering en CPU ademas de GPU.
Memoria de datos de iluminacion precalculada.
```

Una lectura util:

```txt
Frame debugger
→ ver cuantas veces se dibuja un objeto
→ por cuantas luces lo alcanzan
```

Ese numero suele sorprender.

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
Reducir cantidad de luces dinamicas.
Ajustar el rango al area que realmente importa.
Precalcular iluminacion de geometria estatica.
Marcar como estatico lo que no se mueve.
Limitar cuantas luces afectan a un mismo objeto.
Reemplazar luces decorativas por material emisivo.
Usar luz falsa en texturas donde alcanza.
Agrupar fuentes cercanas en una sola luz.
```

Y desde otras ramas:

```txt
Reducir frecuencia de actualizacion
Comparacion antes y despues
```

Ejemplo:

```txt
Antes:
Cada antorcha del mapa es una luz dinamica con rango amplio.

Despues:
Iluminacion precalculada del ambiente, material emisivo en la llama.
```

Otro ejemplo:

```txt
Antes:
Cada explosion crea una luz dinamica.

Despues:
Una sola luz compartida, reutilizada por el efecto activo.
```

---

## Trade-offs

```txt
Iluminacion precalculada
→ casi sin costo en runtime
→ mas memoria y escena menos dinamica.

Menos luces dinamicas
→ frame mas barato
→ menos riqueza de ambiente.

Rango reducido
→ menos objetos afectados
→ transiciones mas duras.

Material emisivo
→ muy barato
→ no ilumina lo que tiene alrededor.

Agrupar fuentes
→ menos calculo
→ menos precision en la direccion de la luz.
```

Precalcular no elimina el costo. Lo mueve.

Cambia tiempo de GPU por memoria y por tiempo de preparacion.

---

## Ejemplo en videojuegos

En un Tower Defense:

```txt
Luz general del escenario.
Torres con luz propia al disparar.
Explosiones que iluminan al detonar.
Niebla que recibe luz.
Camino iluminado para guiar al jugador.
```

El escenario es fijo. El mapa no se mueve nunca.

Y aun asi toda su iluminacion se esta calculando cada frame.

```txt
30 torres disparando
+ una luz por disparo
+ explosiones con luz
= decenas de luces dinamicas simultaneas
```

Ninguna de ellas define la lectura del mapa.

Una solucion sana:

```txt
Escenario con iluminacion precalculada.
Una luz principal dinamica para el ambiente.
Disparos con material emisivo en vez de luz.
Explosiones con una luz compartida y corta.
Camino resuelto con textura, no con luz.
```

El jugador necesita ver el camino y distinguir enemigos. No necesita que cada disparo ilumine el terreno.

---

## Como guia el diagnostico

Flujo recomendado:

```txt
Sintoma:
frame caro en escenas iluminadas.

Sospecha:
costo de iluminacion en runtime.

Medicion:
apagar luces por grupos.

Dato esperado:
mejora proporcional a la cantidad.

Segunda medicion:
reducir rango sin apagar.

Solucion candidata:
precalcular lo estatico, limitar lo dinamico.
```

La pregunta clave es:

```txt
¿Esta luz necesita recalcularse cada frame?
```

---

## Errores comunes al intentar solucionarlo

```txt
Precalcular todo y perder el dinamismo que el juego necesitaba.
Apagar luces hasta que la escena queda plana.
Suponer que precalcular es gratis.
Ignorar el costo en memoria de la informacion precalculada.
Dejar rangos enormes por comodidad de authoring.
No marcar como estatico lo que nunca se mueve.
Cambiar el modo de iluminacion sin volver a medir.
```

Ejemplo de mala solucion:

```txt
Problema:
Muchas luces dinamicas.

Solucion:
Se precalcula toda la iluminacion.

Resultado:
El frame mejora y el ciclo dia/noche deja de funcionar.
```

Se resolvio el costo y se rompio una mecanica.

---

## Hacia donde seguir

Si hace falta entender el intercambio entre recursos:

→ [[Fundamentos]]

Si hace falta ubicar donde se paga la iluminacion:

→ [[Diagnostico]]

Si la preparacion de luces aparece del lado del procesador:

→ [[CPU]]

Si la informacion precalculada pesa en memoria:

→ [[Memoria]]

Si esos datos se cargan por escena:

→ [[Carga e IO]]

Herramientas para confirmar:

```txt
→ Frame debugger
→ Stats window
→ Unity Profiler
```

Notas hermanas de esta rama:

```txt
→ Sombras costosas
→ Costo de fragmentos y shaders
→ Post processing pesado
```

---

## Checklist de diagnostico

```txt
¿Cuantas luces dinamicas hay activas?
¿Cuantas alcanzan al mismo objeto?
¿Que rango tiene cada una?
¿Cuales se mueven realmente?
¿Cuales iluminan geometria estatica?
¿Que esta marcado como estatico?
¿Apagar luces decorativas mejora el frame?
¿Reducir rango mejora el frame?
¿La escena necesita ser dinamica?
¿Cuanta memoria cuesta precalcular?
¿El estilo visual se mantiene?
¿Se comparo antes y despues?
```

---

## Regla final

La pregunta no es cuantas luces soporta el hardware.

```txt
Es cuanto de esta iluminacion
necesita decidirse mientras el juego corre.
Lo que no cambia
no deberia recalcularse cada frame.
```

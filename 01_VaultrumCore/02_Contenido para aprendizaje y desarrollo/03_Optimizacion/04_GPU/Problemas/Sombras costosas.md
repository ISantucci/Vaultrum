## Definicion

Las sombras son particularmente costosas porque requieren informacion adicional de la escena.

Para saber que esta en sombra, el motor necesita mirar la escena desde la luz antes de dibujarla desde la camara.

Eso significa procesar la geometria mas de una vez:

```txt
Pass desde la luz
→ que ocluye
↓
Pass desde la camara
→ que recibe sombra
```

Los factores que definen el costo:

```txt
Cantidad de luces.
Objetos que proyectan.
Objetos que reciben.
Resolucion.
Distancia.
Frecuencia de actualizacion.
Complejidad de escena.
```

El principio operativo es el detalle selectivo:

```txt
No todos los objetos necesitan
sombra maxima
+ a cualquier distancia
+ todo el tiempo
```

Y un detalle que suele pasarse por alto:

```txt
La sombra tambien tiene costo de CPU.
```

Cada luz que proyecta sombra agrega una pasada extra de preparacion.

---

## Responsabilidad de esta nota

Esta nota no existe para apagar las sombras.

Esta nota no existe para tratar la sombra como un lujo.

Esta nota no existe para fijar una resolucion correcta.

Esta nota no existe para reemplazar el analisis de iluminacion.

Existe para tratar la sombra como lo que es: trabajo adicional sobre la escena, que se paga en GPU y tambien en CPU.

Su responsabilidad es ayudar a responder:

```txt
¿Cuanta escena se esta reprocesando para sombras?
```

El foco esta en:

```txt
cuantas luces proyectan
cuantos objetos entran en cada pass
a que resolucion
con que frecuencia
```

---

## Sintomas

Sintomas comunes:

```txt
El frame cae al activar sombras.
El frame cae al agregar una luz con sombra.
El costo escala con la cantidad de objetos, no con el area.
Subir calidad de sombras empeora mucho el rendimiento.
Aumentar la distancia de sombras degrada el frame.
Bordes de sombra inestables al mover la camara.
Rendering alto en el profiler sin efectos visibles.
```

Un patron caracteristico:

```txt
Una luz direccional con sombra
→ costo notable.

Tres luces con sombra
→ costo aproximadamente triplicado.
```

El costo no es del objeto. Es del pass.

---

## Que parte del software suele causarlo

Suele aparecer en:

```txt
Varias luces dinamicas con sombra activada.
Distancia de sombras excesiva.
Resolucion de shadow map muy alta.
Todos los objetos configurados para proyectar.
Objetos chicos proyectando sombra a distancia.
Vegetacion densa que proyecta.
Sombras actualizadas cada frame sin necesidad.
Cascadas mal configuradas.
```

El patron tecnico habitual:

```txt
sombra activada por defecto
+ en todos los objetos
+ en todas las luces
+ a maxima distancia
```

Tambien lo causa mantener sombras dinamicas sobre geometria que nunca se mueve.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
GPU
Vertex processing
Fragment processing
Ancho de banda de memoria
Memoria de video
```

El shadow map es un buffer y ocupa memoria proporcional a su resolucion, multiplicada por cascadas y por luces.

Tambien afecta directamente:

```txt
CPU
```

porque cada luz con sombra agrega culling propio, preparacion de la escena y envio de comandos de dibujado.

Por eso una sombra puede empeorar el frame incluso en un juego que parecia limitado por CPU.

---

## Como detectarlo

La prueba mas directa es desactivar las sombras y comparar.

```txt
Sombras apagadas
→ mejora clara
→ el costo estaba en el pass de sombra.

Sombras apagadas
→ poca diferencia
→ buscar en otra etapa.
```

Despues conviene aislar por luz, apagando la sombra de una luz por vez.

Preguntas practicas:

```txt
¿Cuantas luces proyectan sombra?
¿Que distancia de sombras esta configurada?
¿Que resolucion tiene el shadow map?
¿Cuantos objetos proyectan?
¿Cuantos objetos necesitan proyectar?
¿La geometria estatica podria resolverse sin runtime?
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
Passes de sombra en el frame.
Cantidad de luces con sombra.
Objetos incluidos en el pass de sombra.
Resolucion de los shadow maps.
Cascadas activas.
Rendering en CPU ademas de GPU.
```

Una lectura util:

```txt
Frame debugger
→ ver el pass de sombra antes del pass principal
→ contar que objetos entran ahi
```

Muchas veces entran objetos que el jugador nunca vera proyectar.

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
Reducir cantidad de luces con sombra.
Reducir distancia de sombras.
Bajar resolucion del shadow map.
Desactivar proyeccion en objetos irrelevantes.
Desactivar recepcion donde no aporta.
Ajustar cascadas al tamaño real del escenario.
Actualizar sombras con menor frecuencia.
Usar sombras simples o blob para objetos chicos.
Precalcular sombras de geometria estatica.
```

Y desde otras ramas:

```txt
Reducir frecuencia de actualizacion
Comparacion antes y despues
```

Ejemplo:

```txt
Antes:
Todos los objetos proyectan sombra a 150 metros.

Despues:
Sombras a 40 metros, solo en objetos relevantes.
```

Otro ejemplo:

```txt
Antes:
Tres luces dinamicas con sombra en la misma zona.

Despues:
Una luz principal con sombra, el resto sin proyeccion.
```

---

## Trade-offs

```txt
Menos distancia de sombras
→ mucho menos costo
→ corte visible en el horizonte.

Menor resolucion
→ menos memoria y bandwidth
→ bordes mas dentados.

Menos objetos proyectando
→ passes mas livianos
→ objetos que parecen flotar.

Sombras precalculadas
→ casi sin costo en runtime
→ mas memoria y escena menos dinamica.

Actualizacion menos frecuente
→ menos trabajo por frame
→ sombras que responden con retraso.
```

La sombra ancla el objeto al piso.

Sacarla entera suele costar mas en lectura visual de lo que gana en frame time.

---

## Ejemplo en videojuegos

En un Tower Defense:

```txt
Luz direccional del sol con sombra.
30 torres proyectando.
300 enemigos proyectando.
Proyectiles proyectando.
Decoracion del mapa proyectando.
```

Cada proyectil en vuelo entra al pass de sombra.

```txt
200 proyectiles
× pass de sombra
= geometria reprocesada
por una sombra de dos pixeles
```

Nadie mira la sombra de un proyectil.

La camara ademas esta lejos y en angulo alto, asi que buena parte de las sombras finas ni se distingue.

Una solucion sana:

```txt
Proyectiles sin proyeccion de sombra.
Enemigos con sombra solo cerca de la camara.
Torres con sombra siempre, son el foco del juego.
Decoracion estatica con sombra precalculada.
Distancia de sombras ajustada al area jugable.
```

Se conserva la sombra donde comunica. Se saca donde solo cuesta.

---

## Como guia el diagnostico

Flujo recomendado:

```txt
Sintoma:
frame caro con escena iluminada.

Sospecha:
costo de sombras.

Medicion:
apagar sombras y comparar.

Dato esperado:
mejora clara.

Aislamiento:
apagar sombra por luz.

Solucion candidata:
reducir distancia, resolucion y objetos que proyectan.
```

La pregunta clave es:

```txt
¿Esta sombra aporta informacion al jugador?
```

---

## Errores comunes al intentar solucionarlo

```txt
Apagar todas las sombras y perder la lectura del espacio.
Bajar resolucion hasta que los bordes rompen la imagen.
Reducir distancia sin mirar el horizonte en gameplay.
Olvidar que la sombra tambien cuesta CPU.
Dejar objetos chicos proyectando a cualquier distancia.
Configurar cascadas sin relacion con el escenario.
Cambiar ajustes sin volver a medir.
```

Ejemplo de mala solucion:

```txt
Problema:
El frame cae con sombras.

Solucion:
Se apagan las sombras del juego entero.

Resultado:
Mejora el frame y las unidades parecen flotar sobre el mapa.
```

Se gano rendimiento y se perdio profundidad.

---

## Hacia donde seguir

Si hace falta entender el reparto de costo entre recursos:

→ [[Fundamentos]]

Si hace falta confirmar donde se paga la sombra:

→ [[Diagnostico]]

Si el pass de sombra aparece del lado del procesador:

→ [[CPU]]

Si los shadow maps presionan memoria de video:

→ [[Memoria]]

Si el criterio de detalle selectivo se repite en otros sistemas:

→ [[Patrones transversales]]

Herramientas para confirmar:

```txt
→ Frame debugger
→ Stats window
→ Unity Profiler
```

Notas hermanas de esta rama:

```txt
→ Iluminacion en runtime
→ Costo de vertices y geometria
→ Fill rate y resolucion
```

---

## Checklist de diagnostico

```txt
¿Cuantas luces proyectan sombra?
¿Apagar sombras mejora el frame?
¿Que luz concentra el costo?
¿Que distancia de sombras esta configurada?
¿Que resolucion tienen los shadow maps?
¿Cuantos objetos entran al pass de sombra?
¿Hay objetos chicos proyectando a distancia?
¿Hay geometria estatica proyectando en runtime?
¿Las cascadas corresponden al escenario?
¿Se reviso el costo en CPU ademas de GPU?
¿La sombra sigue anclando los objetos al piso?
¿Se comparo antes y despues?
```

---

## Regla final

La sombra no se dibuja: se calcula mirando la escena otra vez.

```txt
Cada luz que proyecta
agrega un recorrido completo de la escena.
La pregunta no es si la sombra es linda.
Es cuanta escena vale esa sombra.
```

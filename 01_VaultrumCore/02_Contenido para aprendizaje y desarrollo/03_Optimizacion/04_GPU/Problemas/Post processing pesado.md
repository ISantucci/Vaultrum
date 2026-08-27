## Definicion

El post processing son efectos que se aplican sobre la imagen ya renderizada.

Ejemplos habituales:

```txt
Bloom.
Blur.
Color effects.
Ambient effects.
Screen-space effects.
```

Son caros sobre todo por una razon:

```txt
trabajan sobre una gran proporcion
o la totalidad de los pixeles
```

Eso tiene una consecuencia que los distingue de casi todo lo demas:

```txt
Post processing
→ escala con la resolucion.

Post processing
→ no escala con la complejidad de la escena.
```

Una escena vacia y una escena llena pagan lo mismo de post processing.

El principio que ordena esta nota:

```txt
evaluar el costo por pixel
ademas del costo por objeto
```

Cada efecto encadenado es una pasada mas sobre toda la pantalla.

```txt
3 efectos fullscreen
= la pantalla completa recorrida 3 veces
```

---

## Responsabilidad de esta nota

Esta nota no existe para eliminar el post processing.

Esta nota no existe para tratar el bloom como un exceso.

Esta nota no existe para discutir direccion de arte.

Esta nota no existe para reemplazar el analisis de fill rate.

Existe para medir una familia de efectos que no se comporta como el resto de la escena: su costo depende de la pantalla, no del contenido.

Su responsabilidad es ayudar a responder:

```txt
¿Cuantas veces se recorre la pantalla completa por frame?
```

El foco esta en:

```txt
cuantos efectos hay encadenados
a que resolucion trabajan
cuantos buffers intermedios usan
cuanto aporta cada uno visualmente
```

---

## Sintomas

Sintomas comunes:

```txt
El frame es constante y caro, mire donde mire.
El costo no baja al reducir objetos.
El costo no baja al reducir poligonos.
Bajar resolucion mejora mucho el rendimiento.
Desactivar la pila de efectos mejora mucho.
Una escena vacia rinde casi igual que una llena.
El costo empeora en pantallas grandes.
```

Ese ultimo patron es el mas revelador:

```txt
Escena vacia
→ frame caro igual.
```

Si el costo no depende de lo que hay en pantalla, depende de la pantalla.

---

## Que parte del software suele causarlo

Suele aparecer en:

```txt
Pilas de post processing con muchos efectos activos.
Bloom con muchas iteraciones.
Blur de radio grande.
Efectos screen-space de oclusion o reflejos.
Profundidad de campo permanente.
Efectos activos que casi no se perciben.
Buffers intermedios a resolucion completa.
Perfiles de calidad unicos para todo el hardware.
```

El patron tecnico habitual:

```txt
perfil armado durante produccion
+ nunca revisado
+ efectos acumulados
```

Tambien lo causa dejar activos efectos que se agregaron para probar y quedaron.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
GPU
Fragment processing
Ancho de banda de memoria
Memoria de video
```

Cada efecto lee la imagen, la procesa y la escribe en otro buffer. Ese ida y vuelta consume bandwidth incluso cuando el calculo es simple.

Los buffers intermedios ademas ocupan memoria de video proporcional a la resolucion.

Por eso el post processing es de los primeros problemas que aparecen en:

```txt
Mobile.
Hardware integrado.
Notebooks.
Resoluciones altas.
```

---

## Como detectarlo

La prueba mas directa es desactivar toda la pila y comparar.

```txt
Post processing apagado
→ mejora clara
→ el costo estaba ahi.

Post processing apagado
→ poca diferencia
→ buscar en escena, sombras o geometria.
```

Despues conviene aislar efecto por efecto, activando de a uno.

Una prueba complementaria muy util:

```txt
Medir con la camara mirando al vacio.
Si el frame sigue caro,
el costo no depende de la escena.
```

Preguntas practicas:

```txt
¿Cuantos efectos estan activos?
¿Cual pesa mas al aislarlo?
¿A que resolucion trabaja cada uno?
¿Cuantos buffers intermedios hay?
¿Que aporta cada efecto a la lectura del juego?
¿Existe un perfil mas liviano?
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
Passes fullscreen al final del frame.
Cantidad de efectos en la pila.
Resolucion de los buffers intermedios.
Memoria de render targets.
Tiempo de GPU frente a tiempo de CPU.
Comportamiento del frame al cambiar resolucion.
```

Una lectura util:

```txt
Frame debugger
→ mirar el final del frame
→ contar cuantas pasadas fullscreen hay
```

Ese conteo suele ser mayor al esperado.

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
Desactivar efectos que casi no se perciben.
Reducir iteraciones de bloom.
Reducir radio de blur.
Procesar efectos a menor resolucion y escalar.
Combinar efectos en una sola pasada.
Reservar efectos costosos para presets altos.
Activar efectos solo en momentos puntuales.
Reemplazar screen-space costosos por soluciones locales.
```

Y desde otras ramas:

```txt
Comparacion antes y despues
Cuando NO optimizar
```

Ejemplo:

```txt
Antes:
Bloom, profundidad de campo, oclusion y grano, siempre activos.

Despues:
Bloom y grano siempre, el resto solo en presets altos.
```

Otro ejemplo:

```txt
Antes:
Bloom procesado a resolucion completa.

Despues:
Bloom procesado a media resolucion, sin diferencia perceptible.
```

---

## Trade-offs

```txt
Menos efectos activos
→ frame mucho mas barato
→ imagen menos trabajada.

Efectos a media resolucion
→ gran ahorro
→ posibles bordes menos definidos.

Menos iteraciones de bloom
→ menos pasadas fullscreen
→ brillo menos suave.

Efectos por preset
→ el hardware modesto respira
→ mas configuraciones que validar.

Efectos puntuales
→ costo solo cuando importa
→ mas logica de activacion.
```

El post processing es una de las palancas mas rentables de la rama GPU.

Tambien es una de las que mas define el aspecto del juego.

---

## Ejemplo en videojuegos

En un Tower Defense:

```txt
Bloom para los disparos y explosiones.
Ambient effects para dar clima al mapa.
Color effects para la paleta del juego.
Blur suave al abrir el menu.
Vista fija y alejada del escenario.
```

La camara es cenital y el mapa es chico. Se ve todo el tiempo lo mismo.

Al medir con la camara sobre una zona vacia del mapa:

```txt
Sin enemigos.
Sin torres disparando.
Sin efectos de particulas.
Frame igual de caro.
```

Ahi el diagnostico se cierra solo. El costo no viene del gameplay.

```txt
4 efectos fullscreen
× resolucion completa
= la pantalla recorrida 4 veces por frame
```

Una solucion sana:

```txt
Bloom a media resolucion, es lo que da el punch a los disparos.
Color effects combinados en una sola pasada.
Ambient effects solo en presets altos.
Blur del menu activo solo cuando el menu esta abierto.
```

Se conserva el efecto que comunica el impacto. Se recorta el que solo adorna.

---

## Como guia el diagnostico

Flujo recomendado:

```txt
Sintoma:
frame caro y constante.

Sospecha:
post processing.

Medicion:
apagar la pila completa.

Dato esperado:
mejora clara.

Aislamiento:
activar efecto por efecto.

Confirmacion:
el costo se mantiene con la escena vacia.

Solucion candidata:
menos efectos, menor resolucion, presets.
```

La pregunta clave es:

```txt
¿Cuanto cuesta este efecto y cuanto aporta a lo que el jugador entiende?
```

---

## Errores comunes al intentar solucionarlo

```txt
Apagar toda la pila y perder la identidad visual.
Dejar efectos de prueba activos en la version final.
Suponer que un efecto sutil es barato.
Medir en una escena cargada sin probar la escena vacia.
Optimizar la escena cuando el costo era fullscreen.
Usar un unico perfil de calidad para todo el hardware.
Cambiar la pila sin volver a medir.
```

Ejemplo de mala solucion:

```txt
Problema:
Frame caro y constante.

Solucion:
Se reduce la cantidad de enemigos por wave.

Resultado:
El juego pierde tension y el frame no cambia.
```

Se toco el diseño para arreglar un problema de pantalla.

---

## Hacia donde seguir

Si hace falta entender el costo por pixel:

→ [[Fundamentos]]

Si hace falta confirmar que el frame esta limitado por GPU:

→ [[Diagnostico]]

Si los buffers intermedios presionan memoria de video:

→ [[Memoria]]

Si el blur se activa junto con menus y paneles:

→ [[UI]]

Si el costo aparece del lado del procesador:

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
→ Fill rate y resolucion
→ Overdraw y transparencias
→ Costo de fragmentos y shaders
```

---

## Checklist de diagnostico

```txt
¿Cuantos efectos hay activos?
¿Apagar la pila mejora el frame?
¿Que efecto pesa mas al aislarlo?
¿El frame sigue caro con la escena vacia?
¿A que resolucion trabaja cada efecto?
¿Cuantos buffers intermedios hay?
¿Bajar resolucion mejora proporcionalmente?
¿Quedaron efectos de prueba activos?
¿Se pueden combinar pasadas?
¿Hay presets por hardware?
¿Cada efecto aporta a la lectura del juego?
¿Se comparo antes y despues?
```

---

## Regla final

El post processing no cobra por lo que hay en la escena. Cobra por la pantalla.

```txt
Si el frame sigue caro
con la camara mirando al vacio,
el problema no esta en el juego.
Esta en las pasadas sobre la imagen.
```

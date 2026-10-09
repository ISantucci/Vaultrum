## Definicion

Un bottleneck, o cuello de botella, es la parte del sistema que limita el rendimiento general del juego.

Aunque muchas partes del juego esten funcionando correctamente, si una de ellas consume demasiado tiempo o demasiados recursos, puede impedir que el juego mantenga el rendimiento esperado.

La idea principal es:

```txt
Bottleneck
→ punto que limita el rendimiento total
```

Ejemplo:

```txt
El render esta bien.
La memoria esta bien.
La fisica esta bien.

Pero los scripts consumen demasiado CPU.

Resultado:
el juego baja FPS por CPU.
```

En ese caso, el cuello de botella esta en CPU, especificamente en la logica de scripts.

---

## Responsabilidad de esta nota

Esta nota existe para explicar como identificar que parte del sistema esta limitando el rendimiento.

No existe para resolver todos los problemas.
No existe para elegir una solucion automaticamente.
No existe para asumir que todo problema de rendimiento tiene la misma causa.

Su responsabilidad es ayudar a responder:

```txt
¿Que parte del sistema esta frenando al resto?
```

El bottleneck sirve como puente entre:

```txt
sintoma general
→ recurso afectado
→ herramienta de medicion
→ diagnostico
→ solucion candidata
```

---

## Que problema ayuda a entender

Entender bottleneck ayuda a evitar optimizar la parte equivocada.

Un sintoma como “bajan los FPS” puede tener muchas causas posibles.

```txt
Bajan los FPS
→ puede ser CPU
→ puede ser GPU
→ puede ser GC
→ puede ser memoria
→ puede ser carga de assets
```

Si no se identifica el cuello de botella real, se pueden aplicar soluciones que no mejoran nada.

Ejemplo incorrecto:

```txt
El juego baja FPS.
Bajo la calidad de modelos.
Pero el problema real estaba en muchos Update activos.
```

Ejemplo correcto:

```txt
El juego baja FPS.
Profiler muestra scripts costosos.
Se revisan Updates, busquedas y logica por frame.
```

La regla es:

```txt
No se optimiza todo el juego.
Se optimiza el cuello de botella real.
```

---

## Como funciona

Un videojuego reparte trabajo entre distintos recursos.

```txt
CPU
→ scripts, IA, fisica, logica, animaciones, UI.

GPU
→ render, luces, sombras, materiales, particulas.

Memoria
→ objetos, assets, texturas, audio, datos cargados.

Garbage Collector
→ limpieza de memoria administrada.

Disco / carga
→ lectura de archivos, assets, escenas, streaming.
```

Cuando uno de esos recursos queda saturado, limita al resto.

Ejemplo:

```txt
GPU puede renderizar rapido.
Pero CPU tarda demasiado en preparar logica.

Resultado:
el frame se retrasa igual.
```

Otro ejemplo:

```txt
CPU esta liviana.
Pero GPU tarda mucho por sombras y postprocesado.

Resultado:
el frame se retrasa por render.
```

El cuello de botella se detecta midiendo.

No se adivina.

---

## Como aplicarlo en videojuegos

En videojuegos, identificar el bottleneck permite elegir soluciones correctas.

Ejemplos:

```txt
CPU bottleneck
→ revisar scripts, IA, fisica, Update, pathfinding.

GPU bottleneck
→ revisar luces, sombras, materiales, draw calls, postprocesado.

GC bottleneck
→ revisar allocations, strings, listas temporales, Instantiate/Destroy.

Memoria bottleneck
→ revisar assets cargados, referencias retenidas, pools, escenas.

Carga bottleneck
→ revisar Addressables, streaming, carga de escenas, disco.
```

Ejemplo inspirado en Tower Defense:

```txt
Sintoma:
El juego se traba cuando hay muchas torres disparando.

Posibles bottlenecks:
CPU por targeting.
CPU por movimiento de proyectiles.
GC por Instantiate/Destroy.
GPU por efectos visuales.
```

Antes de elegir solucion, hay que medir.

```txt
Si el problema es Instantiate/Destroy
→ Object Pool.

Si el problema es targeting por frame
→ reducir frecuencia o mejorar estructura.

Si el problema son particulas
→ revisar render/GPU.
```

---

## Como guia el diagnostico

Bottleneck ayuda a pasar de una sensacion general a una investigacion concreta.

No alcanza con decir:

```txt
El juego anda lento.
```

Hay que transformar eso en:

```txt
Que parte esta lenta?
Cuando ocurre?
Que recurso se satura?
Que herramienta lo muestra?
Que sistema causa el costo?
```

Flujo recomendado:

```txt
Sintoma
→ sospecha de recurso afectado
→ herramienta de medicion
→ dato observado
→ bottleneck identificado
→ solucion candidata
```

Ejemplo:

```txt
Sintoma:
Spikes cuando aparecen enemigos.

Hipotesis:
CPU o GC.

Herramienta:
Unity Profiler / Timeline / GC Alloc.

Dato:
Picos al instanciar enemigos.

Bottleneck:
Creacion de objetos en runtime.

Siguiente paso:
Evaluar Object Pool o precarga.
```

---

## Cuando conviene consultarlo

Conviene analizar bottlenecks cuando:

```txt
El juego baja FPS.
Hay stuttering.
Hay spikes.
La memoria crece.
La carga tarda demasiado.
El rendimiento cae al escalar.
Una solucion aplicada no mejora nada.
No esta claro que recurso esta afectado.
```

Tambien conviene consultarlo cuando una IA propone una optimizacion demasiado rapido.

Ejemplo:

```txt
La IA propone Object Pool.
Pero todavia no se sabe si el problema es creacion/destruccion, render, IA o memoria.
```

En ese caso, primero se identifica el cuello de botella.

---

## Cuando NO conviene forzarlo

No conviene forzar un analisis de bottleneck cuando todavia no hay sintoma, escala ni objetivo de rendimiento.

Ejemplo:

```txt
Prototipo chico.
Pocos objetos.
Sin caidas.
Sin medicion.
Sin hardware objetivo.
```

En ese caso, conviene priorizar claridad.

Tampoco conviene asumir que el primer dato encontrado es el bottleneck real.

Ejemplo:

```txt
CPU Usage muestra un pico.
Pero el pico aparece por logs temporales del editor.
```

Hay que medir en condiciones representativas.

---

## Errores que ayuda a evitar

Entender bottleneck ayuda a evitar:

- Optimizar la parte equivocada.
- Asumir que todo problema de FPS es GPU.
- Asumir que todo spike es GC.
- Aplicar Object Pool sin confirmar Instantiate/Destroy.
- Reducir calidad visual cuando el problema esta en scripts.
- Reescribir logica cuando el problema esta en render.
- Cambiar arquitectura sin evidencia.
- Perseguir microcostos que no limitan el rendimiento.
- Resolver sintomas sin encontrar causa.

La idea clave es:

```txt
El bottleneck es la causa que limita.
No necesariamente el sintoma mas visible.
```

---

## Riesgos de interpretarlo mal

Un riesgo comun es confundir correlacion con causa.

Ejemplo:

```txt
Hay muchos enemigos en pantalla.
El juego baja FPS.

Conclusion apresurada:
los enemigos son el problema.
```

Pero puede ser:

```txt
targeting de torres
particulas de impactos
UI de vida
pathfinding
Instantiate/Destroy
render
GC Alloc
```

Otro riesgo es diagnosticar con una sola herramienta.

Ejemplo:

```txt
Stats muestra muchos batches.
Pero no se revisa CPU Usage ni Timeline.
```

Una herramienta puede orientar, pero el diagnostico requiere contexto.

Otro riesgo es optimizar todo al mismo tiempo.

```txt
Cambio render.
Cambio IA.
Cambio pooling.
Cambio UI.
```

Despues no se sabe que mejoro o que rompio.

---

## Hacia donde seguir

Esta nota pertenece a Fundamentos.

Despues de entender bottleneck, el siguiente paso depende del cuello sospechado.

Si el cuello parece estar en tiempo de frame:

```txt
→ Frame Budget
```

Si el cuello parece estar en CPU:

```txt
→ CPU Bound
```

Si hace falta entender recursos afectados:

```txt
→ Recursos de hardware
```

Si ya hay un sintoma concreto:

→ [[CPU]]

y las demas ramas segun el recurso:

→ [[GPU]]

→ [[Memoria]]

→ [[Carga e IO]]

→ [[UI]]

Si hace falta medir:

→ [[Diagnostico]]

Si ya se confirmo la causa:

→ [[Patrones transversales]]

---

## Checklist de diagnostico

Antes de concluir que se encontro un bottleneck, revisar:

```txt
¿Cual es el sintoma?
¿Cuando ocurre?
¿Se reproduce de forma consistente?
¿Que recurso parece afectado?
¿Que herramienta lo muestra?
¿El dato fue medido en una escena representativa?
¿El problema es constante o puntual?
¿El costo viene de CPU, GPU, GC, memoria o carga?
¿La solucion propuesta ataca ese cuello real?
¿Se puede validar antes/despues?
```

---

## Regla final

Un bottleneck no se elige por intuicion.

Se identifica midiendo.

```txt
No se optimiza lo que parece importante.
Se optimiza lo que esta limitando el rendimiento real.
```
## Definicion

Unity Profiler es una herramienta de analisis que permite medir el rendimiento de un juego mientras se ejecuta.

Sirve para observar que partes del juego consumen tiempo, memoria o recursos durante runtime.

La idea principal es:

```txt
Unity Profiler
→ herramienta central para medir rendimiento real
```

No optimiza por si solo.

Muestra datos para que el desarrollador pueda diagnosticar.

---

## Para que sirve

Unity Profiler sirve para detectar problemas relacionados con:

```txt
CPU
GPU
Memoria
Garbage Collector
Scripts
Fisica
Render
UI
Audio
Animaciones
Spikes
Frame time
```

Ayuda a responder preguntas como:

- ¿Que parte del frame tarda mas?
- ¿El problema esta en scripts?
- ¿Hay spikes?
- ¿Hay GC Alloc?
- ¿La fisica esta costando demasiado?
- ¿La UI esta actualizandose de mas?
- ¿El render esta pesado?
- ¿La memoria esta creciendo?
- ¿Una solucion realmente mejoro el rendimiento?

La regla principal es:

```txt
No se optimiza sin medir.
Unity Profiler es una de las primeras herramientas para medir.
```

---

## Que problemas ayuda a detectar

Unity Profiler puede ayudar a detectar:

```txt
Muchos update activos
Instantiate y destroy constantes
GC Alloc por frame
Memory Leak
Busquedas globales por frame
UI actualizada innecesariamente
Strings por frame
Pathfinding recalculado demasiado seguido
CPU Bound
Stuttering
Spikes
Fisica costosa
Render pesado
Audio costoso
```

No siempre detecta la causa final automaticamente.

Pero muestra donde conviene investigar.

---

## Que metricas mirar

Metricas importantes:

```txt
Frame time
CPU Usage
GC Alloc
Spikes
Timeline
Memory
Rendering
Physics
Scripts
UI
GC.Collect
Cantidad de llamadas
Tiempo por sistema
```

No conviene mirar solo FPS.

El dato mas importante para optimizacion suele ser:

```txt
Frame time
→ cuanto tarda cada frame
```

Ejemplo:

```txt
Objetivo:
60 FPS

Frame Budget:
16,66 ms

Profiler muestra:
23 ms por frame

Conclusion:
el juego no entra en presupuesto
```

---

## Como interpretar señales

Ejemplo 1:

```txt
Scripts altos en CPU Usage
→ posible problema de logica, Update, IA, pathfinding o busquedas.
```

Ejemplo 2:

```txt
GC Alloc constante
→ posible generacion de basura temporal.
```

Ejemplo 3:

```txt
GC.Collect aparece con spikes
→ posible stuttering por Garbage Collector.
```

Ejemplo 4:

```txt
Physics alto
→ revisar colliders, rigidbodies, raycasts, FixedUpdate.
```

Ejemplo 5:

```txt
Rendering alto
→ revisar GPU, draw calls, materiales, luces, sombras, particulas.
```

Ejemplo 6:

```txt
UI alto
→ revisar textos, layouts, canvas rebuilds, actualizaciones por frame.
```

La interpretacion siempre debe conectar:

```txt
Dato
→ contexto
→ hipotesis
→ validacion
```

---

## Que NO demuestra por si solo

Unity Profiler no demuestra automaticamente la causa exacta.

Ejemplo:

```txt
FPS bajo
→ no significa automaticamente problema de GPU.
```

Puede ser:

```txt
CPU
GC
Fisica
UI
Scripts
Render
Carga
Memoria
```

Otro ejemplo:

```txt
GC Alloc aparece
→ hay allocations

Pero falta saber:
donde se generan,
con que frecuencia,
si causan spikes,
y si vale la pena corregirlas.
```

Tampoco alcanza con una sola medicion aislada.

Hay que medir en condiciones representativas.

---

## Ejemplo de uso

Ejemplo en un Tower Defense:

```txt
Sintoma:
El juego se traba cuando disparan muchas torres.

Paso 1:
Abrir Unity Profiler.

Paso 2:
Reproducir escena con muchas torres y enemigos.

Paso 3:
Mirar CPU Usage, Timeline y GC Alloc.

Posibles hallazgos:
Instantiate/Destroy de proyectiles.
GC Alloc por proyectiles.
Muchos Update activos.
Targeting costoso.
Efectos visuales pesados.
```

Despues se elige solucion segun el dato.

```txt
Instantiate/Destroy
→ Object pool como optimizacion

Muchos Update
→ Update Manager como optimizacion

GC Alloc
→ Evitar allocations por frame

Targeting costoso
→ reducir frecuencia o mejorar estructura
```

---

## Errores comunes al usarla

Errores comunes:

```txt
Mirar solo FPS.
No mirar frame time.
No reproducir el problema.
Medir en una escena distinta.
Medir una vez y sacar conclusion definitiva.
No revisar Timeline.
No revisar GC Alloc.
Confundir sintoma con causa.
No comparar antes/despues.
Medir en Editor y asumir que es igual a build.
```

Tambien es comun ver un valor alto y aplicar una solucion sin contexto.

Ejemplo:

```txt
Veo CPU alto.
Aplico Object Pool.

Pero el problema real era pathfinding.
```

---

## Relacion con otros sistemas

Unity Profiler se relaciona con:

```txt
Frame Budget
Bottleneck
CPU Bound
GPU Bound
Flujo de diagnostico
Comparacion antes y despues
```

Tambien se relaciona con herramientas especificas:

```txt
CPU Usage
Timeline
GC Alloc
Memory Profiler
Frame debugger
```

---

## Checklist de uso

```txt
¿Se reprodujo el problema?
¿Se midio frame time?
¿Se reviso CPU Usage?
¿Se reviso Timeline?
¿Se reviso GC Alloc?
¿Se reviso memoria si aplica?
¿Se identifico cuando ocurre el spike?
¿Se comparo con una escena controlada?
¿Se sabe que sistema esta involucrado?
¿Se puede validar antes/despues?
```

---

## Regla final

Unity Profiler no reemplaza el criterio.

```txt
Profiler
→ muestra datos

Desarrollador
→ interpreta

Solucion
→ se elige segun diagnostico
```

La regla general es:

```txt
Medir primero.
Interpretar despues.
Optimizar al final.
```
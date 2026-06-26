## Definición

Unity Profiler es una herramienta de análisis que permite medir el rendimiento de un juego mientras se ejecuta.

Sirve para observar qué partes del juego consumen tiempo, memoria o recursos durante runtime.

La idea principal es:

```txt
Unity Profiler
→ herramienta central para medir rendimiento real
```

No optimiza por sí solo.

Muestra datos para que el desarrollador pueda diagnosticar.

---

## Para qué sirve

Unity Profiler sirve para detectar problemas relacionados con:

```txt
CPU
GPU
Memoria
Garbage Collector
Scripts
Física
Render
UI
Audio
Animaciones
Spikes
Frame time
```

Ayuda a responder preguntas como:

- ¿Qué parte del frame tarda más?
- ¿El problema está en scripts?
- ¿Hay spikes?
- ¿Hay GC Alloc?
- ¿La física está costando demasiado?
- ¿La UI está actualizándose de más?
- ¿El render está pesado?
- ¿La memoria está creciendo?
- ¿Una solución realmente mejoró el rendimiento?

La regla principal es:

```txt
No se optimiza sin medir.
Unity Profiler es una de las primeras herramientas para medir.
```

---

## Qué problemas ayuda a detectar

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
Física costosa
Render pesado
Audio costoso
```

No siempre detecta la causa final automáticamente.

Pero muestra dónde conviene investigar.

---

## Qué métricas mirar

Métricas importantes:

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

El dato más importante para optimización suele ser:

```txt
Frame time
→ cuánto tarda cada frame
```

Ejemplo:

```txt
Objetivo:
60 FPS

Frame Budget:
16.66 ms

Profiler muestra:
23 ms por frame

Conclusión:
el juego no entra en presupuesto
```

---

## Cómo interpretar señales

Ejemplo 1:

```txt
Scripts altos en CPU Usage
→ posible problema de lógica, Update, IA, pathfinding o búsquedas.
```

Ejemplo 2:

```txt
GC Alloc constante
→ posible generación de basura temporal.
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
→ revisar GPU, draw calls, materiales, luces, sombras, partículas.
```

Ejemplo 6:

```txt
UI alto
→ revisar textos, layouts, canvas rebuilds, actualizaciones por frame.
```

La interpretación siempre debe conectar:

```txt
Dato
→ contexto
→ hipótesis
→ validación
```

---

## Qué NO demuestra por sí solo

Unity Profiler no demuestra automáticamente la causa exacta.

Ejemplo:

```txt
FPS bajo
→ no significa automáticamente problema de GPU.
```

Puede ser:

```txt
CPU
GC
Física
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
dónde se generan,
con qué frecuencia,
si causan spikes,
y si vale la pena corregirlas.
```

Tampoco alcanza con una sola medición aislada.

Hay que medir en condiciones representativas.

---

## Ejemplo de uso

Ejemplo en un Tower Defense:

```txt
Síntoma:
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

Después se elige solución según el dato.

```txt
Instantiate/Destroy
→ Object pool como optimizacion

Muchos Update
→ UpdateManager

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
Medir una vez y sacar conclusión definitiva.
No revisar Timeline.
No revisar GC Alloc.
Confundir síntoma con causa.
No comparar antes/después.
Medir en Editor y asumir que es igual a build.
```

También es común ver un valor alto y aplicar una solución sin contexto.

Ejemplo:

```txt
Veo CPU alto.
Aplico Object Pool.

Pero el problema real era pathfinding.
```

---

## Relación con otros sistemas

Unity Profiler se relaciona con:

```txt
Frame Budget
Bottleneck
CPU Bound
Problemas de rendimiento
Herramientas de deteccion
Metodologias y soluciones
```

También se relaciona con herramientas específicas:

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
¿Se midió frame time?
¿Se revisó CPU Usage?
¿Se revisó Timeline?
¿Se revisó GC Alloc?
¿Se revisó memoria si aplica?
¿Se identificó cuándo ocurre el spike?
¿Se comparó con una escena controlada?
¿Se sabe qué sistema está involucrado?
¿Se puede validar antes/después?
```

---

## Regla final

Unity Profiler no reemplaza el criterio.

```txt
Profiler
→ muestra datos

Desarrollador
→ interpreta

Solución
→ se elige según diagnóstico
```

La regla general es:

```txt
Medir primero.
Interpretar después.
Optimizar al final.
```
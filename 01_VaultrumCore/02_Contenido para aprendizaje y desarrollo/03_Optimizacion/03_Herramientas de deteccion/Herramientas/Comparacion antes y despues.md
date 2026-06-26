## Definición

Comparación antes y después es la práctica de medir el rendimiento antes de aplicar una optimización y volver a medir después en condiciones equivalentes.

Sirve para validar si una solución realmente mejoró el problema.

La idea principal es:

```txt
Antes
→ medición base

Cambio
→ optimización aplicada

Después
→ medición equivalente

Comparación
→ validación
```

Sin comparación, no hay evidencia clara de mejora.

---

## Para qué sirve

Sirve para responder:

- ¿La optimización funcionó?
- ¿Mejoró el frame time?
- ¿Bajaron los spikes?
- ¿Bajó GC Alloc?
- ¿Bajó uso de memoria?
- ¿Se redujo CPU Usage?
- ¿El problema se movió a otro recurso?
- ¿El trade-off fue aceptable?
- ¿Se rompió gameplay?
- ¿La mejora justifica la complejidad?

La regla central es:

```txt
Optimización sin validación
→ suposición
```

---

## Qué problemas ayuda a validar

Comparación antes/después sirve para validar soluciones sobre:

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
GPU Bound
Stuttering
Spikes
Carga de assets
```

Es útil para cualquier optimización relevante.

---

## Qué métricas mirar

Métricas posibles:

```txt
Frame time promedio.
Peores frames.
Spikes.
CPU Usage.
Scripts.
Physics.
UI.
Rendering.
GC Alloc.
GC.Collect.
Memoria total.
Objetos vivos.
Cantidad de instanciaciones.
Cantidad de objetos activos.
Cantidad de llamadas por segundo.
Tiempo de carga.
```

No todas las métricas importan siempre.

Depende del problema.

Ejemplo:

```txt
Problema:
GC Alloc por frame.

Métricas principales:
GC Alloc.
GC.Collect.
Spikes.
Frame time.
```

Ejemplo:

```txt
Problema:
Muchos Update activos.

Métricas principales:
CPU Usage.
Scripts.
BehaviourUpdate.
Frame time.
Cantidad de objetos activos.
```

---

## Cómo hacer una comparación válida

Para que la comparación sea válida, las condiciones deben ser similares.

Definir:

```txt
Escena.
Cantidad de objetos.
Duración de prueba.
Acciones del jugador.
Herramienta usada.
Hardware.
Versión del proyecto.
Configuración gráfica.
Build o Editor.
```

Ejemplo válido:

```txt
Antes:
Nivel 1.
100 enemigos.
20 torres.
60 segundos.
Profiler activo.

Después:
Nivel 1.
100 enemigos.
20 torres.
60 segundos.
Profiler activo.
```

Ejemplo inválido:

```txt
Antes:
200 enemigos.

Después:
30 enemigos.

Conclusión:
mejoró.
```

Eso no demuestra que la optimización funcionó.

---

## Cómo interpretar resultados

Ejemplo 1:

```txt
Antes:
Frame time promedio 22 ms.
Spikes de 60 ms.
GC Alloc constante.

Después:
Frame time promedio 15 ms.
Spikes de 25 ms.
GC Alloc casi nulo.

Conclusión:
La optimización probablemente funcionó.
```

Ejemplo 2:

```txt
Antes:
CPU Usage alto en scripts.

Después:
CPU baja,
pero memoria sube mucho.

Conclusión:
La solución mejora CPU,
pero introduce trade-off de memoria.
```

Ejemplo 3:

```txt
Antes:
FPS bajo.

Después:
FPS igual.

Conclusión:
La solución no atacó el bottleneck real
o hay otro cuello de botella.
```

---

## Qué NO demuestra por sí solo

Una mejora aislada no siempre demuestra que todo está bien.

Ejemplo:

```txt
CPU bajó
```

Pero falta revisar:

```txt
¿Subió memoria?
¿Se rompió gameplay?
¿Aumentó input lag?
¿Bajó calidad visual?
¿El problema aparece en otra escena?
¿La mejora se mantiene a escala?
```

También puede pasar:

```txt
El promedio mejora,
pero los spikes siguen.
```

Para el jugador, los spikes pueden ser más molestos que el promedio.

---

## Ejemplo de uso

Ejemplo con Object Pool:

```txt
Problema:
Spikes al disparar proyectiles.

Antes:
Profiler muestra Instantiate/Destroy.
GC Alloc.
Spikes de 40 ms.

Cambio:
Implementar Object Pool.

Después:
Profiler muestra menos Instantiate/Destroy.
GC Alloc baja.
Spikes bajan a 18 ms.

Validación:
La solución mejoró el problema.
```

Ejemplo con UI:

```txt
Problema:
UI actualiza textos por frame.

Antes:
UpdateMoneyText se llama 3600 veces en 60 segundos.

Cambio:
UI por evento MoneyChanged.

Después:
UpdateMoneyText se llama 8 veces en 60 segundos.

Validación:
La frecuencia bajó y el comportamiento sigue correcto.
```

---

## Errores comunes

Errores comunes:

```txt
No medir antes.
No medir después.
Cambiar varias cosas a la vez.
Medir escenas distintas.
Cambiar cantidad de enemigos.
Cambiar calidad gráfica.
Comparar Editor contra Build.
No registrar condiciones.
Mirar solo FPS.
Ignorar spikes.
Ignorar memoria.
No probar gameplay.
```

Otro error:

```txt
Aplicar tres optimizaciones juntas
→ mejora

Pero no saber cuál funcionó.
```

Cuando sea posible, conviene aislar cambios.

---

## Relación con otros sistemas

Comparación antes/después se relaciona con:

```txt
Medir antes de optimizar
Unity Profiler
CPU Usage
Timeline
GC Alloc
Memory Profiler
Frame Budget
Bottleneck
```

También se relaciona con toda la sección de:

```txt
Problemas de rendimiento
Metodologias y soluciones
```

---

## Checklist de comparación

Antes de aplicar el cambio:

```txt
¿Se definió escena de prueba?
¿Se definió cantidad de objetos?
¿Se definió duración?
¿Se definió herramienta?
¿Se guardó medición inicial?
¿Se sabe qué métrica importa?
```

Después del cambio:

```txt
¿Se repitió la misma prueba?
¿Se comparó frame time?
¿Se compararon spikes?
¿Se comparó GC Alloc si aplica?
¿Se comparó memoria si aplica?
¿Se revisó gameplay?
¿Se documentó resultado?
¿El trade-off es aceptable?
```

---

## Regla final

Una optimización no termina cuando se cambia el código.

Termina cuando se valida.

```txt
Cambio aplicado
→ medición posterior
→ comparación
→ conclusión
```

La regla general es:

```txt
Si no hay antes y después,
no hay evidencia de optimización.
```
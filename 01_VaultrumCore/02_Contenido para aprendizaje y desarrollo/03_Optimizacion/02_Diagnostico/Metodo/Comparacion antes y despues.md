## Definicion

Comparacion antes y despues es la practica de medir el rendimiento antes de aplicar una optimizacion y volver a medir despues en condiciones equivalentes.

Sirve para validar si una solucion realmente mejoro el problema.

La idea principal es:

```txt
Antes
→ medicion base

Cambio
→ optimizacion aplicada

Despues
→ medicion equivalente

Comparacion
→ validacion
```

Sin comparacion, no hay evidencia clara de mejora.

---

## Para que sirve

Sirve para responder:

- ¿La optimizacion funciono?
- ¿Mejoro el frame time?
- ¿Bajaron los spikes?
- ¿Bajo GC Alloc?
- ¿Bajo uso de memoria?
- ¿Se redujo CPU Usage?
- ¿El problema se movio a otro recurso?
- ¿El trade-off fue aceptable?
- ¿Se rompio gameplay?
- ¿La mejora justifica la complejidad?

La regla central es:

```txt
Optimizacion sin validacion
→ suposicion
```

---

## Que problemas ayuda a validar

Comparacion antes/despues sirve para validar soluciones sobre:

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

Es util para cualquier optimizacion relevante.

---

## Que metricas mirar

Metricas posibles:

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

No todas las metricas importan siempre.

Depende del problema.

Ejemplo:

```txt
Problema:
GC Alloc por frame.

Metricas principales:
GC Alloc.
GC.Collect.
Spikes.
Frame time.
```

Ejemplo:

```txt
Problema:
Muchos Update activos.

Metricas principales:
CPU Usage.
Scripts.
BehaviourUpdate.
Frame time.
Cantidad de objetos activos.
```

---

## Como hacer una comparacion valida

Para que la comparacion sea valida, las condiciones deben ser similares.

Definir:

```txt
Escena.
Cantidad de objetos.
Duracion de prueba.
Acciones del jugador.
Herramienta usada.
Hardware.
Version del proyecto.
Configuracion grafica.
Build o Editor.
```

Ejemplo valido:

```txt
Antes:
Nivel 1.
300 enemigos.
30 torres.
60 segundos.
Profiler activo.

Despues:
Nivel 1.
300 enemigos.
30 torres.
60 segundos.
Profiler activo.
```

Ejemplo invalido:

```txt
Antes:
300 enemigos.

Despues:
30 enemigos.

Conclusion:
mejoro.
```

Eso no demuestra que la optimizacion funciono.

---

## Como interpretar resultados

Ejemplo 1:

```txt
Antes:
Frame time promedio 22 ms.
Spikes de 60 ms.
GC Alloc constante.

Despues:
Frame time promedio 15 ms.
Spikes de 25 ms.
GC Alloc casi nulo.

Conclusion:
La optimizacion probablemente funciono.
```

Ejemplo 2:

```txt
Antes:
CPU Usage alto en scripts.

Despues:
CPU baja,
pero memoria sube mucho.

Conclusion:
La solucion mejora CPU,
pero introduce trade-off de memoria.
```

Ejemplo 3:

```txt
Antes:
FPS bajo.

Despues:
FPS igual.

Conclusion:
La solucion no ataco el bottleneck real
o hay otro cuello de botella.
```

Y hay una lectura que ninguno de esos tres ejemplos cierra: una optimizacion no termina porque el Profiler mejoro.

La medicion prueba que el costo bajo. No prueba que el juego siga siendo el mismo juego.

Por eso la comparacion se completa con una pasada de QA sobre lo que el cambio pudo haber tocado:

```txt
Comportamiento
→ los sistemas siguen haciendo lo que hacian.

Visuales
→ no se perdio nada que el jugador estaba viendo.

Feedback
→ el impacto, el sonido y la respuesta siguen llegando cuando corresponde.

Gameplay
→ las reglas se siguen cumpliendo.

Errores
→ no aparecieron excepciones ni casos rotos.

Memoria
→ lo que bajo en CPU no subio de golpe en otro lado.

Estabilidad
→ el juego aguanta una sesion larga, no una captura de veinte segundos.
```

Una tecnica puede dar +20% de performance y romper la experiencia.

```txt
Profiler mejor
+ experiencia peor
= implementacion incorrecta
```

Eso no es una optimizacion con un costo aceptable. Es una optimizacion que no esta terminada.

---

## Que NO demuestra por si solo

Una mejora aislada no siempre demuestra que todo esta bien.

Ejemplo:

```txt
CPU bajo
```

Pero falta revisar:

```txt
¿Subio memoria?
¿Se rompio gameplay?
¿Aumento input lag?
¿Bajo calidad visual?
¿El problema aparece en otra escena?
¿La mejora se mantiene a escala?
```

Tambien puede pasar:

```txt
El promedio mejora,
pero los spikes siguen.
```

Para el jugador, los spikes pueden ser mas molestos que el promedio.

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

Despues:
Profiler muestra menos Instantiate/Destroy.
GC Alloc baja.
Spikes bajan a 18 ms.

Validacion:
La solucion mejoro el problema.
```

Ejemplo con UI:

```txt
Problema:
UI actualiza textos por frame.

Antes:
UpdateMoneyText se llama 3600 veces en 60 segundos.

Cambio:
UI por evento MoneyChanged.

Despues:
UpdateMoneyText se llama 8 veces en 60 segundos.

Validacion:
La frecuencia bajo y el comportamiento sigue correcto.
```

---

## Errores comunes

Errores comunes:

```txt
No medir antes.
No medir despues.
Cambiar varias cosas a la vez.
Medir escenas distintas.
Cambiar cantidad de enemigos.
Cambiar calidad grafica.
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

Pero no saber cual funciono.
```

Cuando sea posible, conviene aislar cambios.

---

## Relacion con otros sistemas

Comparacion antes/despues se relaciona con:

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

Tambien se relaciona con la rama del recurso que se haya diagnosticado:

```txt
CPU
GPU
Memoria
Carga e IO
UI
```

---

## Checklist de comparacion

Antes de aplicar el cambio:

```txt
¿Se definio escena de prueba?
¿Se definio cantidad de objetos?
¿Se definio duracion?
¿Se definio herramienta?
¿Se guardo medicion inicial?
¿Se sabe que metrica importa?
```

Despues del cambio:

```txt
¿Se repitio la misma prueba?
¿Se comparo frame time?
¿Se compararon spikes?
¿Se comparo GC Alloc si aplica?
¿Se comparo memoria si aplica?
¿Se reviso gameplay?
¿Se documento resultado?
¿El trade-off es aceptable?
```

---

## Regla final

Una optimizacion no termina cuando se cambia el codigo.

Termina cuando se valida.

```txt
Cambio aplicado
→ medicion posterior
→ comparacion
→ conclusion
```

La regla general es:

```txt
Si no hay antes y despues,
no hay evidencia de optimizacion.
```
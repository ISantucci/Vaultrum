## Definición

GC Alloc es una señal que indica que el juego está generando memoria administrada nueva.

Esa memoria queda en el Heap y eventualmente puede ser limpiada por el Garbage Collector.

La idea principal es:

```txt
GC Alloc
→ memoria temporal creada

Garbage Collector
→ limpia memoria que ya no se usa
```

GC Alloc no siempre es un problema.

Pero si ocurre constantemente durante gameplay crítico, puede generar presión sobre el Garbage Collector y producir stuttering.

---

## Para qué sirve

GC Alloc sirve para detectar allocations que pueden provocar spikes o tirones.

Ayuda a responder:

- ¿El juego genera basura temporal por frame?
- ¿Hay strings creados constantemente?
- ¿Hay listas o arrays temporales?
- ¿La UI está generando texto nuevo?
- ¿Instantiate/Destroy genera allocations?
- ¿Hay LINQ o closures en runtime crítico?
- ¿Los spikes coinciden con GC.Collect?

La idea central es:

```txt
GC Alloc frecuente
→ posible causa de stuttering
```

---

## Qué problemas ayuda a detectar

GC Alloc ayuda a detectar:

```txt
GC Alloc por frame
Strings por frame
UI actualizada innecesariamente
Instantiate y destroy constantes
Listas temporales
Arrays temporales
LINQ por frame
Boxing
Closures
Debug.Log frecuente
```

También se relaciona con:

```txt
Stuttering
Spikes
Frame time irregular
```

---

## Qué métricas mirar

Conviene mirar:

```txt
Allocations por frame.
Allocations en runtime crítico.
GC.Collect.
Frecuencia de allocations.
Cantidad asignada.
Métodos responsables.
Relación con gameplay.
```

No es lo mismo:

```txt
GC Alloc ocasional al cargar escena
```

que:

```txt
GC Alloc todos los frames durante combate
```

La frecuencia importa mucho.

---

## Cómo interpretar señales

Ejemplo 1:

```txt
GC Alloc aparece cada frame.

Hipótesis:
Algún sistema está creando memoria temporal constantemente.
```

Ejemplo 2:

```txt
GC Alloc aparece al actualizar UI.

Hipótesis:
Textos, strings o layouts generan allocations.
```

Ejemplo 3:

```txt
GC Alloc aparece al disparar.

Hipótesis:
Instantiate de proyectiles o efectos temporales.
```

Ejemplo 4:

```txt
GC.Collect aparece después de muchas allocations.

Hipótesis:
La basura acumulada forzó una recolección.
```

---

## Qué NO demuestra por sí solo

GC Alloc no significa automáticamente Memory Leak.

Diferencia:

```txt
GC Alloc
→ memoria temporal generada.

Memory Leak
→ memoria que queda retenida cuando debería liberarse.
```

GC Alloc tampoco indica siempre un problema grave.

Puede ser aceptable si ocurre:

```txt
al cargar escena,
al abrir menú,
al inicializar sistemas,
en momentos no críticos.
```

Pero debe revisarse si ocurre:

```txt
cada frame,
durante combate,
durante movimiento,
durante input,
durante UI frecuente,
con muchos objetos.
```

---

## Ejemplo de uso

Ejemplo:

```txt
Síntoma:
El juego tiene tirones cada pocos segundos.

Herramienta:
GC Alloc + Timeline.

Hallazgo:
GC Alloc aparece constantemente.
Cada cierto tiempo aparece GC.Collect.

Investigación:
Revisar UI.
Revisar strings.
Revisar listas temporales.
Revisar Instantiate/Destroy.

Soluciones:
Evitar allocations por frame.
UI orientada a eventos.
Object Pool.
Reutilización de listas.
```

---

## Errores comunes al usarla

Errores comunes:

```txt
Confundir GC Alloc con Memory Leak.
Ignorar allocations pequeñas pero constantes.
Corregir allocations de carga e ignorar allocations de gameplay.
Eliminar toda allocation sin criterio.
No revisar strings.
No revisar UI.
No revisar Debug.Log.
No validar si desaparecieron los spikes.
```

Otro error:

```txt
Ver GC Alloc y aplicar Object Pool.
```

Pero si la allocation viene de strings de UI, Object Pool no resuelve el problema.

---

## Relación con otros sistemas

GC Alloc se relaciona con:

```txt
GC Alloc por frame
Strings por frame
UI actualizada innecesariamente
Instantiate y destroy constantes
Timeline
Unity Profiler
Memory Profiler
Evitar allocations por frame
```

También se relaciona con:

```txt
Frame Budget
```

porque un GC.Collect en mal momento puede romper el presupuesto del frame.

---

## Checklist de uso

```txt
¿Hay GC Alloc durante gameplay?
¿Ocurre cada frame?
¿Coincide con stuttering?
¿Aparece GC.Collect?
¿La allocation viene de UI?
¿La allocation viene de strings?
¿La allocation viene de Instantiate/Destroy?
¿La allocation viene de listas/arrays temporales?
¿La allocation ocurre en runtime crítico?
¿Se validó después de corregir?
```

---

## Regla final

GC Alloc no es automáticamente un error.

Pero GC Alloc frecuente en gameplay crítico debe investigarse.

```txt
La basura temporal no siempre se ve.
Pero el jugador puede sentirla como stuttering.
```
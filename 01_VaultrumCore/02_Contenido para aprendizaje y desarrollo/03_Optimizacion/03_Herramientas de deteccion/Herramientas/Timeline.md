## Definición

Timeline es una vista de análisis que permite observar cómo se distribuye el trabajo dentro de un frame.

A diferencia de mirar solo valores generales, Timeline muestra cuándo ocurre cada tarea y cómo se ordena dentro del frame.

La idea principal es:

```txt
Timeline
→ muestra qué ocurre dentro del frame y cuándo ocurre
```

Es especialmente útil para investigar spikes y stuttering.

---

## Para qué sirve

Timeline sirve para analizar frames específicos.

Ayuda a responder:

- ¿Qué pasó en el frame donde hubo un spike?
- ¿Qué sistema se ejecutó justo antes del tirón?
- ¿Hubo GC.Collect?
- ¿Hubo Instantiate o Destroy?
- ¿Hubo física pesada?
- ¿Hubo UI rebuild?
- ¿Varios sistemas costosos ocurrieron juntos?
- ¿El problema es constante o puntual?

La idea central es:

```txt
El promedio no alcanza.
Los peores frames también importan.
```

---

## Qué problemas ayuda a detectar

Timeline ayuda a detectar:

```txt
Stuttering
Spikes
GC Alloc por frame
GC.Collect
Instantiate y destroy constantes
Muchos update activos
Física costosa
UI costosa
Carga puntual
Scripts concentrados en un frame
Eventos procesados en masa
```

También ayuda a ver acumulación:

```txt
varios sistemas medianos
→ mismo frame
→ spike grande
```

---

## Qué métricas mirar

En Timeline conviene mirar:

```txt
Duración total del frame.
Bloques largos.
GC.Collect.
Scripts.
Physics.
UI.
Rendering.
Instantiate.
Destroy.
Callbacks.
Orden de ejecución.
Frames con picos.
```

La pregunta principal es:

```txt
¿Qué hizo que este frame fuera peor que los demás?
```

---

## Cómo interpretar señales

Ejemplo 1:

```txt
Frame normal:
14 ms

Frame con spike:
52 ms

Timeline muestra:
GC.Collect

Hipótesis:
Allocations acumuladas provocan recolección.
```

Ejemplo 2:

```txt
Spike al disparar muchas torres.

Timeline muestra:
Instantiate repetido.

Hipótesis:
Proyectiles se crean durante gameplay crítico.
```

Ejemplo 3:

```txt
Spike al abrir panel.

Timeline muestra:
UI rebuild grande.

Hipótesis:
Panel o canvas recalcula demasiados elementos.
```

Ejemplo 4:

```txt
Spike al aparecer oleada.

Timeline muestra:
Inicialización de enemigos + scripts + física.

Hipótesis:
Spawn concentrado en un solo frame.
```

---

## Qué NO demuestra por sí solo

Timeline muestra qué ocurrió, pero no siempre explica por qué el sistema está diseñado así.

Ejemplo:

```txt
Timeline muestra muchos Updates.
```

Todavía falta saber:

```txt
qué objetos tienen Update,
qué hacen,
si son necesarios,
si pueden reducir frecuencia.
```

Otro ejemplo:

```txt
Timeline muestra GC.Collect.
```

Todavía falta saber:

```txt
qué genera allocations,
con qué frecuencia,
si vienen de UI, strings, listas, Instantiate o LINQ.
```

Timeline es una herramienta de investigación, no una solución automática.

---

## Ejemplo de uso

Ejemplo:

```txt
Síntoma:
El juego se congela medio segundo al iniciar una wave.

Herramienta:
Timeline.

Hallazgo:
En el mismo frame ocurren:
Instantiate de enemigos.
Inicialización de IA.
Asignación de rutas.
Activación de animaciones.
Physics setup.

Diagnóstico:
Demasiado trabajo concentrado en un solo frame.

Soluciones posibles:
Pre-instanciar.
Object Pool.
Distribuir spawn.
Precalcular datos.
Inicializar por etapas.
```

---

## Errores comunes al usarla

Errores comunes:

```txt
Mirar solo frames normales.
Ignorar el frame exacto del spike.
No comparar frame normal vs frame malo.
No revisar GC.Collect.
No relacionar Timeline con gameplay.
No revisar qué evento disparó el pico.
No validar después.
```

Otro error:

```txt
Ver un spike y asumir que todo el sistema está mal.
```

Puede ser un pico puntual aceptable, dependiendo del contexto.

---

## Relación con otros sistemas

Timeline se relaciona con:

```txt
Unity Profiler
Frame Budget
GC Alloc
GC Alloc por frame
Instantiate y destroy constantes
Muchos update activos
CPU Usage
Comparacion antes y despues
```

También es clave para detectar:

```txt
Stuttering
Spikes
Carga concentrada
```

---

## Checklist de uso

```txt
¿Se ubicó el frame con spike?
¿Se comparó con un frame normal?
¿Aparece GC.Collect?
¿Aparece Instantiate o Destroy?
¿Aparece Physics alto?
¿Aparece UI rebuild?
¿Aparecen muchos scripts juntos?
¿El pico coincide con un evento del gameplay?
¿Se puede repartir el trabajo?
¿Se validó después?
```

---

## Regla final

Timeline responde una pregunta muy concreta:

```txt
¿Qué pasó exactamente en este frame?
```

Para problemas de stuttering, suele ser más importante que mirar solo el promedio de FPS.
## Definicion

Timeline es una vista de analisis que permite observar como se distribuye el trabajo dentro de un frame.

A diferencia de mirar solo valores generales, Timeline muestra cuando ocurre cada tarea y como se ordena dentro del frame.

La idea principal es:

```txt
Timeline
→ muestra que ocurre dentro del frame y cuando ocurre
```

Es especialmente util para investigar spikes y stuttering.

---

## Para que sirve

Timeline sirve para analizar frames especificos.

Ayuda a responder:

- ¿Que paso en el frame donde hubo un spike?
- ¿Que sistema se ejecuto justo antes del tiron?
- ¿Hubo GC.Collect?
- ¿Hubo Instantiate o Destroy?
- ¿Hubo fisica pesada?
- ¿Hubo UI rebuild?
- ¿Varios sistemas costosos ocurrieron juntos?
- ¿El problema es constante o puntual?

La idea central es:

```txt
El promedio no alcanza.
Los peores frames tambien importan.
```

---

## Que problemas ayuda a detectar

Timeline ayuda a detectar:

```txt
Stuttering
Spikes
GC Alloc por frame
GC.Collect
Instantiate y destroy constantes
Muchos update activos
Fisica costosa
UI costosa
Carga puntual
Scripts concentrados en un frame
Eventos procesados en masa
```

Tambien ayuda a ver acumulacion:

```txt
varios sistemas medianos
→ mismo frame
→ spike grande
```

---

## Que metricas mirar

En Timeline conviene mirar:

```txt
Duracion total del frame.
Bloques largos.
GC.Collect.
Scripts.
Physics.
UI.
Rendering.
Instantiate.
Destroy.
Callbacks.
Orden de ejecucion.
Frames con picos.
```

La pregunta principal es:

```txt
¿Que hizo que este frame fuera peor que los demas?
```

---

## Como interpretar señales

Ejemplo 1:

```txt
Frame normal:
14 ms

Frame con spike:
52 ms

Timeline muestra:
GC.Collect

Hipotesis:
Allocations acumuladas provocan recoleccion.
```

Ejemplo 2:

```txt
Spike al disparar muchas torres.

Timeline muestra:
Instantiate repetido.

Hipotesis:
Proyectiles se crean durante gameplay critico.
```

Ejemplo 3:

```txt
Spike al abrir panel.

Timeline muestra:
UI rebuild grande.

Hipotesis:
Panel o canvas recalcula demasiados elementos.
```

Ejemplo 4:

```txt
Spike al aparecer oleada.

Timeline muestra:
Inicializacion de enemigos + scripts + fisica.

Hipotesis:
Spawn concentrado en un solo frame.
```

---

## Que NO demuestra por si solo

Timeline muestra que ocurrio, pero no siempre explica por que el sistema esta diseñado asi.

Ejemplo:

```txt
Timeline muestra muchos Updates.
```

Todavia falta saber:

```txt
que objetos tienen Update,
que hacen,
si son necesarios,
si pueden reducir frecuencia.
```

Otro ejemplo:

```txt
Timeline muestra GC.Collect.
```

Todavia falta saber:

```txt
que genera allocations,
con que frecuencia,
si vienen de UI, strings, listas, Instantiate o LINQ.
```

Timeline es una herramienta de investigacion, no una solucion automatica.

---

## Ejemplo de uso

Ejemplo:

```txt
Sintoma:
El juego se congela medio segundo al iniciar una wave.

Herramienta:
Timeline.

Hallazgo:
En el mismo frame ocurren:
Instantiate de enemigos.
Inicializacion de IA.
Asignacion de rutas.
Activacion de animaciones.
Physics setup.

Diagnostico:
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
No revisar que evento disparo el pico.
No validar despues.
```

Otro error:

```txt
Ver un spike y asumir que todo el sistema esta mal.
```

Puede ser un pico puntual aceptable, dependiendo del contexto.

---

## Relacion con otros sistemas

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

Tambien es clave para detectar:

```txt
Stuttering
Spikes
Carga concentrada
```

---

## Checklist de uso

```txt
¿Se ubico el frame con spike?
¿Se comparo con un frame normal?
¿Aparece GC.Collect?
¿Aparece Instantiate o Destroy?
¿Aparece Physics alto?
¿Aparece UI rebuild?
¿Aparecen muchos scripts juntos?
¿El pico coincide con un evento del gameplay?
¿Se puede repartir el trabajo?
¿Se valido despues?
```

---

## Regla final

Timeline responde una pregunta muy concreta:

```txt
¿Que paso exactamente en este frame?
```

Para problemas de stuttering, suele ser mas importante que mirar solo el promedio de FPS.
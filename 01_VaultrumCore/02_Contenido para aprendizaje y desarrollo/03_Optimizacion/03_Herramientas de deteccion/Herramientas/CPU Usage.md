## Definición

CPU Usage es una vista o módulo de análisis que permite observar cuánto tiempo consume la CPU en distintas partes del frame.

Sirve para entender qué sistemas están usando procesamiento durante runtime.

La idea principal es:

```txt
CPU Usage
→ muestra en qué se va el tiempo de CPU
```

En videojuegos, la CPU suele encargarse de:

```txt
Scripts
IA
Física
Pathfinding
Animaciones
UI
Eventos
Managers
Callbacks de Unity
Preparación de datos para render
```

---

## Para qué sirve

CPU Usage sirve para detectar si el juego está limitado por procesamiento lógico.

Ayuda a responder:

- ¿Los scripts están costando demasiado?
- ¿Hay muchos `Update()`?
- ¿La física consume mucho?
- ¿La IA está pesada?
- ¿El pathfinding se recalcula demasiado?
- ¿La UI está actualizándose de más?
- ¿Hay spikes de CPU?
- ¿El juego está CPU Bound?

La idea central es:

```txt
Si la CPU tarda demasiado,
el frame no entra en presupuesto.
```

---

## Qué problemas ayuda a detectar

CPU Usage ayuda a detectar:

```txt
CPU Bound
Muchos update activos
Busquedas globales por frame
Pathfinding recalculado demasiado seguido
UI actualizada innecesariamente
Instantiate y destroy constantes
Física costosa
IA pesada
Callbacks excesivos
Managers con demasiada lógica
```

También ayuda a diferenciar:

```txt
Problema de CPU
vs
Problema de GPU
```

---

## Qué métricas mirar

Métricas o zonas importantes:

```txt
Scripts
Physics
Animation
Rendering
UI
BehaviourUpdate
FixedUpdate
LateUpdate
GC.Collect
Tiempo total de CPU
Spikes
Cantidad de llamadas
```

En Unity, un punto importante suele ser:

```txt
BehaviourUpdate
→ costo asociado a Updates de MonoBehaviours
```

Si aparece alto, conviene revisar:

```txt
cuántos objetos tienen Update,
qué hacen en Update,
si se puede reducir frecuencia,
si hay búsquedas o allocations.
```

---

## Cómo interpretar señales

Ejemplo 1:

```txt
Scripts alto
→ revisar lógica de gameplay.
```

Ejemplo 2:

```txt
BehaviourUpdate alto
→ revisar muchos Update activos.
```

Ejemplo 3:

```txt
Physics alto
→ revisar FixedUpdate, colliders, rigidbodies, raycasts.
```

Ejemplo 4:

```txt
UI alto
→ revisar textos, canvas, layouts, updates de HUD.
```

Ejemplo 5:

```txt
GC.Collect dentro de CPU
→ revisar allocations y GC Alloc.
```

Ejemplo 6:

```txt
CPU alto al aparecer enemigos
→ revisar spawner, Instantiate, inicialización, IA.
```

La señal debe analizarse con el contexto del gameplay.

---

## Qué NO demuestra por sí solo

CPU Usage alto no dice automáticamente qué línea de código está mal.

Indica una zona de investigación.

Ejemplo:

```txt
Scripts alto
→ puede ser IA
→ puede ser Update
→ puede ser UI
→ puede ser pathfinding
→ puede ser eventos
→ puede ser Instantiate
```

También puede haber varios problemas juntos.

Ejemplo:

```txt
Muchos enemigos
→ IA costosa
→ movimiento costoso
→ física costosa
→ UI de vida costosa
```

CPU Usage orienta el diagnóstico, no lo cierra solo.

---

## Ejemplo de uso

Ejemplo:

```txt
Síntoma:
Al llegar a 100 enemigos, bajan los FPS.

Herramienta:
CPU Usage.

Dato:
BehaviourUpdate sube mucho.

Hipótesis:
Muchos enemigos ejecutan Update costoso.

Investigación:
Revisar Enemy.Update.
Revisar percepción.
Revisar targeting.
Revisar pathfinding.

Soluciones posibles:
UpdateManager
Reducir frecuencia de actualizacion
Clases puras
Cacheo de referencias
```

---

## Errores comunes al usarla

Errores comunes:

```txt
Ver CPU alto y no abrir detalle.
No relacionar el pico con el momento del gameplay.
No revisar cantidad de objetos activos.
No distinguir Physics de Scripts.
No revisar GC.Collect.
No comparar antes/después.
Pensar que si CPU está alto, todo debe ir a un manager.
```

Un error típico:

```txt
Scripts alto
→ mover todo a GameManager

Resultado:
menos orden, misma lógica costosa
```

La solución debe atacar la causa, no esconderla.

---

## Relación con otros sistemas

CPU Usage se relaciona con:

```txt
CPU Bound
Frame Budget
Game Loop
Muchos update activos
UpdateManager
Reducir frecuencia de actualizacion
Unity Profiler
Timeline
```

También se relaciona con:

```txt
Busquedas globales por frame
Pathfinding recalculado demasiado seguido
UI actualizada innecesariamente
```

---

## Checklist de uso

```txt
¿El problema parece de CPU?
¿Scripts aparecen altos?
¿BehaviourUpdate aparece alto?
¿Physics aparece alto?
¿UI aparece alta?
¿El costo crece con cantidad de objetos?
¿Hay spikes o costo constante?
¿Se sabe qué gameplay ocurre durante el pico?
¿Se revisó Timeline?
¿Se validó después de aplicar solución?
```

---

## Regla final

CPU Usage ayuda a responder:

```txt
¿Qué está haciendo trabajar demasiado a la CPU?
```

La solución no siempre es hacer código más rápido.

Muchas veces es:

```txt
hacer menos trabajo,
hacerlo menos seguido,
o hacerlo en un sistema mejor separado.
```
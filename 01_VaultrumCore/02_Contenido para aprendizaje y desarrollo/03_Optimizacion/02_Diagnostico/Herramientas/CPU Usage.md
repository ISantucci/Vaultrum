## Definicion

CPU Usage es una vista o modulo de analisis que permite observar cuanto tiempo consume la CPU en distintas partes del frame.

Sirve para entender que sistemas estan usando procesamiento durante runtime.

La idea principal es:

```txt
CPU Usage
→ muestra en que se va el tiempo de CPU
```

En videojuegos, la CPU suele encargarse de:

```txt
Scripts
IA
Fisica
Pathfinding
Animaciones
UI
Eventos
Managers
Callbacks de Unity
Preparacion de datos para render
```

---

## Para que sirve

CPU Usage sirve para detectar si el juego esta limitado por procesamiento logico.

Ayuda a responder:

- ¿Los scripts estan costando demasiado?
- ¿Hay muchos `Update()`?
- ¿La fisica consume mucho?
- ¿La IA esta pesada?
- ¿El pathfinding se recalcula demasiado?
- ¿La UI esta actualizandose de mas?
- ¿Hay spikes de CPU?
- ¿El juego esta CPU Bound?

La idea central es:

```txt
Si la CPU tarda demasiado,
el frame no entra en presupuesto.
```

---

## Que problemas ayuda a detectar

CPU Usage ayuda a detectar:

```txt
CPU Bound
Muchos update activos
Busquedas globales por frame
Pathfinding recalculado demasiado seguido
UI actualizada innecesariamente
Instantiate y destroy constantes
Fisica costosa
IA pesada
Callbacks excesivos
Managers con demasiada logica
```

Tambien ayuda a diferenciar:

```txt
Problema de CPU
vs
Problema de GPU
```

---

## Que metricas mirar

Metricas o zonas importantes:

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
cuantos objetos tienen Update,
que hacen en Update,
si se puede reducir frecuencia,
si hay busquedas o allocations.
```

Esos datos se leen en dos vistas hermanas. Timeline muestra cuando ocurre cada cosa dentro del frame y en que thread. Hierarchy muestra el reparto por funcion:

```txt
Hierarchy
→ que funciones consumen mas
→ tiempo total
→ tiempo propio
→ cantidad de llamadas
```

Total y Self no miden lo mismo:

```txt
Total
→ lo que tarda la funcion con todo lo que llama adentro

Self
→ lo que tarda la funcion por si misma
```

---

## Como interpretar señales

Ejemplo 1:

```txt
Scripts alto
→ revisar logica de gameplay.
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
→ revisar spawner, Instantiate, inicializacion, IA.
```

Ejemplo 7:

```txt
Total = 10 ms / Self = 1 ms
→ el costo no esta en esa funcion
→ esta en lo que esa funcion llama
```

Por eso no alcanza con ordenar por Total y empezar a modificar la primera funcion de la lista: arriba de la jerarquia casi siempre hay un contenedor, no una causa. Hay que bajar por Hierarchy hasta donde el Self se vuelve alto, y recien ahi se sabe quien paga.

La señal debe analizarse con el contexto del gameplay.

---

## Que NO demuestra por si solo

CPU Usage alto no dice automaticamente que linea de codigo esta mal.

Indica una zona de investigacion.

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

Tambien puede haber varios problemas juntos.

Ejemplo:

```txt
Muchos enemigos
→ IA costosa
→ movimiento costoso
→ fisica costosa
→ UI de vida costosa
```

CPU Usage orienta el diagnostico, no lo cierra solo.

---

## Ejemplo de uso

Ejemplo:

```txt
Sintoma:
Al llegar a 300 enemigos, bajan los FPS.

Herramienta:
CPU Usage.

Dato:
BehaviourUpdate sube mucho.

Hipotesis:
Muchos enemigos ejecutan Update costoso.

Investigacion:
Revisar Enemy.Update.
Revisar percepcion.
Revisar targeting.
Revisar pathfinding.

Soluciones posibles:
Update Manager como optimizacion
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
No comparar antes/despues.
Pensar que si CPU esta alto, todo debe ir a un manager.
```

Un error tipico:

```txt
Scripts alto
→ mover todo a GameManager

Resultado:
menos orden, misma logica costosa
```

La solucion debe atacar la causa, no esconderla.

---

## Relacion con otros sistemas

CPU Usage se relaciona con:

```txt
CPU Bound
Frame Budget
Game Loop
Muchos update activos
Update Manager como optimizacion
Reducir frecuencia de actualizacion
Unity Profiler
Timeline
```

Tambien se relaciona con:

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
¿Se sabe que gameplay ocurre durante el pico?
¿Se reviso Timeline?
¿Se valido despues de aplicar solucion?
```

---

## Regla final

CPU Usage ayuda a responder:

```txt
¿Que esta haciendo trabajar demasiado a la CPU?
```

La solucion no siempre es hacer codigo mas rapido.

Muchas veces es:

```txt
hacer menos trabajo,
hacerlo menos seguido,
o hacerlo en un sistema mejor separado.
```
## Proposito

Esta rama reune los problemas y las soluciones de memoria en un videojuego.

No existe para minimizar un contador de megabytes.
No existe para declarar que las allocations son malas.
No existe para poner pooling en todo lo que se instancia.

Existe porque hay problemas de performance que no encajan ni en CPU ni en GPU, y que se resuelven mirando quien reserva, quien retiene y quien libera.

---

## Idea central

Memoria es una dimension propia.

```txt
CPU        cuanto tiempo tarda simular
GPU        cuanto tiempo tarda dibujar
Memoria    cuanto se reserva, cuanto se retiene y cuando se libera
```

Se puede separar CPU de GPU sin problemas, pero memoria no entra limpio en ninguno de los dos. Un memory leak no aparece en el reparto del frame hasta que ya es tarde, y un pico de recoleccion se ve como un problema de CPU aunque su causa sea de memoria.

Conviene distinguir al menos tres tipos, porque tienen lifecycles y sistemas de administracion distintos:

```txt
managed memory   la que administra C# y el recolector
native memory    recursos gestionados fuera del managed heap
GPU memory       texturas, meshes, buffers, render targets
```

El objetivo no es memorizar los nombres. Es entender que liberar uno no libera los otros.

---

## Los dos costos que se confunden

```txt
hacer allocations       cuesta al reservar
recolectarlas despues   cuesta al limpiar
```

Una allocation chica parece insignificante de a una:

```txt
40 bytes por frame
x 60 FPS
x 60 segundos
```

El problema tipico en videojuegos no es la memoria consumida. Es el comportamiento:

```txt
crear basura
→ crear basura
→ crear basura
→ el heap necesita limpieza
→ recoleccion
→ spike
```

Por eso en esta rama la frecuencia importa mas que la cantidad.

---

## Cuando usar esta rama

Usar Memoria cuando:

```txt
hay spikes periodicos que no coinciden con nada visible
GC Alloc muestra basura por frame durante gameplay
la memoria crece partida tras partida
cambiar de escena y volver deja mas memoria que antes
algo no se libera aunque ya no se use
el juego empeora con el tiempo de sesion, no con la carga
```

---

## Como debe usar esta rama una IA

Una IA debe separar dos preguntas que se parecen y no son la misma:

```txt
¿Se esta generando basura?     → GC Alloc, y el problema es de frecuencia
¿Algo no se esta liberando?    → Memory Profiler, y el problema es de referencias
```

Confundirlas lleva a la solucion equivocada: poner pooling donde habia un evento sin desuscribir, o buscar un leak donde solo habia un string por frame.

Antes de proponer una solucion debe poder decir:

```txt
¿Que se reserva?
¿Con que frecuencia?
¿En que contexto: carga o gameplay?
¿Quien mantiene viva la referencia?
¿Cuando deberia liberarse?
¿Que memoria residente agrega la solucion?
```

---

## Hot path: donde importa de verdad

No hay que transformar LINQ, strings, closures, listas o enumeradores en enemigos universales.

Lo que importa es si aparecen en un hot path:

```txt
codigo ejecutado extremadamente seguido
para muchas entidades
o con un costo significativo
```

La misma allocation puede ser irrelevante durante la carga y un problema serio dentro de:

```txt
1000 enemigos x 60 FPS
```

---

## Problemas incluidos

### [[GC Alloc por frame]]

Memoria administrada nueva reservada en cada frame, y la presion que eso genera sobre el recolector.

Consultar cuando haya spikes periodicos o basura durante el gameplay.

### [[Strings por frame]]

El caso mas frecuente de basura por frame: concatenacion, conversion e interpolacion repetidas.

Consultar cuando el HUD o los logs actualicen texto todos los frames.

### [[Memory Leak]]

Memoria retenida por referencias vivas que ya no deberian existir.

Consultar cuando la memoria crezca de forma sostenida o no vuelva al valor inicial al cambiar de escena.

---

## Soluciones incluidas

### [[Object pool como optimizacion]]

Reutilizar entidades en vez de crearlas y destruirlas, con su ciclo de reset explicito.

Consultar cuando haya entidades de alta rotacion y el diagnostico confirme el costo de creacion y destruccion.

### [[Evitar allocations por frame]]

Reducir la basura temporal en caminos criticos reutilizando colecciones y prealocando.

Consultar cuando GC Alloc muestre reserva sostenida en gameplay.

### [[Ciclo de vida de recursos]]

El lifecycle Load, Use, Release, y por que la memoria puede crecer sin que exista un leak tradicional.

Consultar cuando todo se cargue y nada se descargue, o cuando haya que decidir quien libera que.

---

## Lo que esta rama comparte con otras

Pooling y caching viven de un intercambio, y ese intercambio se paga aca:

```txt
Caching        mas memoria  ↔  menos recomputacion
Pooling        mas memoria  ↔  menos creacion y destruccion
Precomputacion mas memoria  ↔  menos calculo en runtime
Precarga       mas memoria  ↔  menos spike futuro
```

Un pool gigantesco que conserva cientos de objetos inutilizados resuelve un problema de CPU creando uno de memoria. Eso no es una falla del patron: es el trade-off funcionando, y hay que dimensionarlo.

---

## Como se conecta con otras ramas

```txt
Diagnostico    GC Alloc y Memory Profiler responden preguntas distintas
Fundamentos    los trade-offs de memoria son la mitad de los trade-offs de la seccion
CPU            el spike de recoleccion se ve en el frame de CPU
GPU            texturas, meshes, buffers y render targets ocupan VRAM
Carga e IO     precargar mueve el problema del tiempo a la memoria residente
```

---

## Criterio de uso

Memoria alta no es lo mismo que memoria mal usada.

```txt
memoria alta y estable        puede estar bien
memoria que crece sin techo   es un problema
memoria baja con spikes       tambien es un problema
```

Una sola fotografia rara vez alcanza. Comparar estados suele decir mucho mas:

```txt
inicio
→ jugar
→ cambiar de escena
→ volver
→ comparar
```

---

## Regla final

La memoria no se optimiza minimizando un numero.

Se optimiza sabiendo quien reserva, quien retiene y quien libera.

```txt
¿Se genera basura, o algo no se libera?
Son problemas distintos.
Y tienen soluciones distintas.
```

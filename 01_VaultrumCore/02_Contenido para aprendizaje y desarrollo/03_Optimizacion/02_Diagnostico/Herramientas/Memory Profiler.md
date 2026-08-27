## Definicion

Memory Profiler es una herramienta para analizar el uso de memoria de un proyecto.

Permite inspeccionar que objetos, assets y referencias estan ocupando memoria durante runtime.

La idea principal es:

```txt
Memory Profiler
→ herramienta para analizar memoria y referencias vivas
```

Es especialmente util para detectar crecimiento de memoria, objetos retenidos y posibles memory leaks.

---

## Para que sirve

Memory Profiler sirve para responder:

- ¿Que esta ocupando memoria?
- ¿La memoria crece con el tiempo?
- ¿Que assets estan cargados?
- ¿Hay objetos que deberian haberse liberado?
- ¿Hay referencias retenidas por managers?
- ¿Hay pools demasiado grandes?
- ¿Una escena anterior sigue viva?
- ¿Hay texturas, audio o meshes pesados?
- ¿El juego libera memoria al cambiar de escena?

La idea central es:

```txt
No alcanza con ver que la memoria sube.
Hay que saber que la esta reteniendo.
```

---

## Que problemas ayuda a detectar

Memory Profiler ayuda a detectar:

```txt
Memory Leak
Assets mal gestionados
Pools demasiado grandes
Referencias retenidas
Texturas pesadas
Audio pesado
Objetos de escena retenidos
Managers persistentes con referencias viejas
Addressables no liberados
Crecimiento progresivo de memoria
```

Tambien puede ayudar a diferenciar:

```txt
Memoria alta por assets necesarios
vs
Memoria alta por objetos retenidos sin razon
```

---

## Que metricas mirar

Conviene mirar:

```txt
Memoria total.
Objetos vivos.
Assets cargados.
Texturas.
Meshes.
Audio.
GameObjects.
Componentes.
Objetos administrados.
Referencias.
Diferencias entre snapshots.
```

La comparacion entre snapshots es clave.

Ejemplo:

```txt
Snapshot A:
Menu principal.

Snapshot B:
Despues de jugar nivel y volver al menu.

Diferencia:
Objetos del nivel siguen vivos.
```

Eso puede indicar un leak o una referencia retenida.

---

## Como interpretar señales

Ejemplo 1:

```txt
Despues de salir del nivel,
enemigos siguen vivos.

Hipotesis:
Algun manager, evento o lista los retiene.
```

Ejemplo 2:

```txt
Texturas muy grandes ocupan mucha memoria.

Hipotesis:
Assets visuales pesados o mala compresion.
```

Ejemplo 3:

```txt
Pool crece constantemente y no baja.

Hipotesis:
Pool sin limite o sin politica de limpieza.
```

Ejemplo 4:

```txt
UI destruida sigue referenciada.

Hipotesis:
Evento no desuscripto o manager persistente con referencia vieja.
```

---

## Que NO demuestra por si solo

Memory Profiler no significa que toda memoria alta sea mala.

Ejemplo:

```txt
Un nivel grande necesita mucha memoria.
```

Eso puede ser normal.

El problema aparece cuando:

```txt
la memoria crece sin limite,
no baja cuando deberia,
o retiene objetos que ya no corresponden.
```

Tampoco debe confundirse Memory Leak con GC Alloc.

```txt
GC Alloc
→ memoria temporal generada.

Memory Leak
→ memoria retenida indebidamente.
```

---

## Ejemplo de uso

Ejemplo:

```txt
Sintoma:
Despues de varias partidas, el juego consume cada vez mas memoria.

Paso 1:
Tomar snapshot en menu.

Paso 2:
Entrar a nivel, jugar, volver al menu.

Paso 3:
Tomar otro snapshot.

Paso 4:
Comparar.

Hallazgo:
Objetos del nivel siguen vivos.

Investigacion:
Eventos no desuscriptos.
Managers DontDestroyOnLoad.
Listas estaticas.
Pools.
Addressables.
```

---

## Errores comunes al usarla

Errores comunes:

```txt
Mirar solo memoria total.
No comparar snapshots.
No reproducir ciclo completo.
Confundir assets necesarios con leak.
No revisar referencias.
No revisar eventos.
No revisar managers persistentes.
No revisar pools.
No revisar Addressables.
```

Otro error:

```txt
Ver memoria alta y destruir objetos manualmente,
sin revisar quien los retiene.
```

Si la referencia sigue viva, el problema puede continuar.

---

## Relacion con otros sistemas

Memory Profiler se relaciona con:

```txt
Memory Leak
Recursos de hardware
GC Alloc
Unity Profiler
Addressables como metodologia de optimizacion
Object pool como optimizacion
Cacheo de referencias
```

Tambien se relaciona con arquitectura:

```txt
Managers persistentes
Eventos
Singletons
Caches
Pools
```

---

## Checklist de uso

```txt
¿La memoria crece con el tiempo?
¿Se tomaron snapshots comparables?
¿Se comparo antes/despues de cambiar escena?
¿Hay objetos que deberian haberse liberado?
¿Hay assets cargados sin uso?
¿Hay managers reteniendo referencias?
¿Hay eventos no desuscriptos?
¿Hay pools creciendo sin limite?
¿Hay Addressables sin liberar?
¿Se identifico quien referencia al objeto?
```

---

## Regla final

Memory Profiler sirve para responder:

```txt
¿Que sigue vivo en memoria y por que?
```

La memoria alta no siempre es un leak.

Pero la memoria que no baja cuando deberia debe investigarse.
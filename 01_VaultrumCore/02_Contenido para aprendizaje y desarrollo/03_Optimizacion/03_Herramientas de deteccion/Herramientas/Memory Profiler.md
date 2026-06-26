## Definición

Memory Profiler es una herramienta para analizar el uso de memoria de un proyecto.

Permite inspeccionar qué objetos, assets y referencias están ocupando memoria durante runtime.

La idea principal es:

```txt
Memory Profiler
→ herramienta para analizar memoria y referencias vivas
```

Es especialmente útil para detectar crecimiento de memoria, objetos retenidos y posibles memory leaks.

---

## Para qué sirve

Memory Profiler sirve para responder:

- ¿Qué está ocupando memoria?
- ¿La memoria crece con el tiempo?
- ¿Qué assets están cargados?
- ¿Hay objetos que deberían haberse liberado?
- ¿Hay referencias retenidas por managers?
- ¿Hay pools demasiado grandes?
- ¿Una escena anterior sigue viva?
- ¿Hay texturas, audio o meshes pesados?
- ¿El juego libera memoria al cambiar de escena?

La idea central es:

```txt
No alcanza con ver que la memoria sube.
Hay que saber qué la está reteniendo.
```

---

## Qué problemas ayuda a detectar

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

También puede ayudar a diferenciar:

```txt
Memoria alta por assets necesarios
vs
Memoria alta por objetos retenidos sin razón
```

---

## Qué métricas mirar

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

La comparación entre snapshots es clave.

Ejemplo:

```txt
Snapshot A:
Menú principal.

Snapshot B:
Después de jugar nivel y volver al menú.

Diferencia:
Objetos del nivel siguen vivos.
```

Eso puede indicar un leak o una referencia retenida.

---

## Cómo interpretar señales

Ejemplo 1:

```txt
Después de salir del nivel,
enemigos siguen vivos.

Hipótesis:
Algún manager, evento o lista los retiene.
```

Ejemplo 2:

```txt
Texturas muy grandes ocupan mucha memoria.

Hipótesis:
Assets visuales pesados o mala compresión.
```

Ejemplo 3:

```txt
Pool crece constantemente y no baja.

Hipótesis:
Pool sin límite o sin política de limpieza.
```

Ejemplo 4:

```txt
UI destruida sigue referenciada.

Hipótesis:
Evento no desuscripto o manager persistente con referencia vieja.
```

---

## Qué NO demuestra por sí solo

Memory Profiler no significa que toda memoria alta sea mala.

Ejemplo:

```txt
Un nivel grande necesita mucha memoria.
```

Eso puede ser normal.

El problema aparece cuando:

```txt
la memoria crece sin límite,
no baja cuando debería,
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
Síntoma:
Después de varias partidas, el juego consume cada vez más memoria.

Paso 1:
Tomar snapshot en menú.

Paso 2:
Entrar a nivel, jugar, volver al menú.

Paso 3:
Tomar otro snapshot.

Paso 4:
Comparar.

Hallazgo:
Objetos del nivel siguen vivos.

Investigación:
Eventos no desuscriptos.
Managers DontDestroyOnLoad.
Listas estáticas.
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
sin revisar quién los retiene.
```

Si la referencia sigue viva, el problema puede continuar.

---

## Relación con otros sistemas

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

También se relaciona con arquitectura:

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
¿Se comparó antes/después de cambiar escena?
¿Hay objetos que deberían haberse liberado?
¿Hay assets cargados sin uso?
¿Hay managers reteniendo referencias?
¿Hay eventos no desuscriptos?
¿Hay pools creciendo sin límite?
¿Hay Addressables sin liberar?
¿Se identificó quién referencia al objeto?
```

---

## Regla final

Memory Profiler sirve para responder:

```txt
¿Qué sigue vivo en memoria y por qué?
```

La memoria alta no siempre es un leak.

Pero la memoria que no baja cuando debería debe investigarse.
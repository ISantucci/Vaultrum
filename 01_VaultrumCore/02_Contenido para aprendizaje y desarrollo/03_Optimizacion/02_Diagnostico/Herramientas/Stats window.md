## Definicion

Stats Window es una ventana de Unity que muestra informacion rapida sobre rendimiento y render mientras el juego corre.

No es una herramienta de diagnostico profundo, pero sirve como señal inicial.

La idea principal es:

```txt
Stats Window
→ lectura rapida de datos generales
```

Puede ayudar a observar FPS aproximado, batches, triangulos, vertices y otros datos de render.

---

## Para que sirve

Stats Window sirve para obtener una vista rapida del estado del juego.

Ayuda a responder:

- ¿El FPS aproximado cae?
- ¿Hay muchos batches?
- ¿Hay muchos triangulos?
- ¿Hay muchos vertices?
- ¿El render parece pesado?
- ¿Cambiar una escena modifica mucho los datos?
- ¿Una zona tiene mas carga visual que otra?

Es util como primera señal, no como diagnostico final.

---

## Que problemas ayuda a detectar

Stats Window puede ayudar a detectar señales de:

```txt
Render pesado
Draw calls elevados
Batches altos
Geometria excesiva
Escenas visualmente cargadas
Posible GPU Bound
```

Tambien puede complementar:

```txt
Frame debugger
Unity Profiler
```

---

## Que metricas mirar

Datos utiles:

```txt
FPS aproximado
Batches
SetPass calls
Tris
Verts
Screen
Render statistics
```

Dependiendo de la version de Unity y pipeline, los nombres pueden variar.

La lectura principal es:

```txt
¿La escena esta generando demasiado trabajo visual?
```

---

## Como interpretar señales

Ejemplo 1:

```txt
Batches altos
→ posible problema de draw calls o materiales.
```

Ejemplo 2:

```txt
Tris/Verts muy altos
→ posible geometria pesada.
```

Ejemplo 3:

```txt
SetPass calls altos
→ posible costo por cambios de material/shader.
```

Ejemplo 4:

```txt
FPS baja al mirar una zona
→ esa zona puede tener carga visual alta.
```

Estas señales deben confirmarse con herramientas mas detalladas.

---

## Que NO demuestra por si solo

Stats Window no alcanza para diagnosticar por completo.

Ejemplo:

```txt
FPS bajo en Stats
```

No indica automaticamente si el problema es:

```txt
CPU
GPU
GC
Memoria
Fisica
Scripts
Render
```

Tampoco muestra con detalle que codigo o asset causa el problema.

Para eso se usan:

```txt
Unity Profiler
CPU Usage
Timeline
Frame debugger
Memory Profiler
```

---

## Ejemplo de uso

Ejemplo:

```txt
Sintoma:
Una zona del mapa baja rendimiento.

Paso 1:
Mirar Stats Window en una zona liviana.

Paso 2:
Mirar Stats Window en la zona pesada.

Comparar:
Batches.
Tris.
Verts.
SetPass.

Si suben mucho:
investigar render con Frame Debugger y Profiler.
```

---

## Errores comunes al usarla

Errores comunes:

```txt
Usarla como unica herramienta.
Mirar solo FPS.
No confirmar con Profiler.
Comparar escenas distintas.
Ignorar CPU/GC.
Asumir que batches altos son siempre el problema principal.
```

La Stats Window sirve para detectar señales, no para cerrar diagnostico.

---

## Relacion con otros sistemas

Stats Window se relaciona con:

```txt
Frame debugger
Unity Profiler
Recursos de hardware
Bottleneck
```

Es especialmente util para investigar posibles problemas de:

```txt
GPU Bound
Costo de vertices y geometria
Draw calls y batching
Overdraw y transparencias
Culling
```

---

## Checklist de uso

```txt
¿El problema parece visual?
¿Bajan FPS al mirar cierta zona?
¿Suben batches?
¿Suben tris o verts?
¿Suben SetPass calls?
¿Se comparo con una zona liviana?
¿Se confirmo con Profiler?
¿Se reviso Frame Debugger?
```

---

## Regla final

Stats Window sirve como señal rapida.

```txt
Stats
→ sospecha inicial

Profiler / Frame Debugger
→ diagnostico mas profundo
```

No debe usarse como unica fuente de verdad.
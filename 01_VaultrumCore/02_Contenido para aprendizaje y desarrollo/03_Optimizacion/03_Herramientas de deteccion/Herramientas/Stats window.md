## Definición

Stats Window es una ventana de Unity que muestra información rápida sobre rendimiento y render mientras el juego corre.

No es una herramienta de diagnóstico profundo, pero sirve como señal inicial.

La idea principal es:

```txt
Stats Window
→ lectura rápida de datos generales
```

Puede ayudar a observar FPS aproximado, batches, triángulos, vértices y otros datos de render.

---

## Para qué sirve

Stats Window sirve para obtener una vista rápida del estado del juego.

Ayuda a responder:

- ¿El FPS aproximado cae?
- ¿Hay muchos batches?
- ¿Hay muchos triángulos?
- ¿Hay muchos vértices?
- ¿El render parece pesado?
- ¿Cambiar una escena modifica mucho los datos?
- ¿Una zona tiene más carga visual que otra?

Es útil como primera señal, no como diagnóstico final.

---

## Qué problemas ayuda a detectar

Stats Window puede ayudar a detectar señales de:

```txt
Render pesado
Draw calls elevados
Batches altos
Geometría excesiva
Escenas visualmente cargadas
Posible GPU Bound
```

También puede complementar:

```txt
Frame debugger
Unity Profiler
```

---

## Qué métricas mirar

Datos útiles:

```txt
FPS aproximado
Batches
SetPass calls
Tris
Verts
Screen
Render statistics
```

Dependiendo de la versión de Unity y pipeline, los nombres pueden variar.

La lectura principal es:

```txt
¿La escena está generando demasiado trabajo visual?
```

---

## Cómo interpretar señales

Ejemplo 1:

```txt
Batches altos
→ posible problema de draw calls o materiales.
```

Ejemplo 2:

```txt
Tris/Verts muy altos
→ posible geometría pesada.
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

Estas señales deben confirmarse con herramientas más detalladas.

---

## Qué NO demuestra por sí solo

Stats Window no alcanza para diagnosticar por completo.

Ejemplo:

```txt
FPS bajo en Stats
```

No indica automáticamente si el problema es:

```txt
CPU
GPU
GC
Memoria
Física
Scripts
Render
```

Tampoco muestra con detalle qué código o asset causa el problema.

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
Síntoma:
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
Usarla como única herramienta.
Mirar solo FPS.
No confirmar con Profiler.
Comparar escenas distintas.
Ignorar CPU/GC.
Asumir que batches altos son siempre el problema principal.
```

La Stats Window sirve para detectar señales, no para cerrar diagnóstico.

---

## Relación con otros sistemas

Stats Window se relaciona con:

```txt
Frame debugger
Unity Profiler
Recursos de hardware
Bottleneck
```

Es especialmente útil para investigar posibles problemas de:

```txt
GPU
Render
Materiales
Geometría
Draw calls
```

---

## Checklist de uso

```txt
¿El problema parece visual?
¿Bajan FPS al mirar cierta zona?
¿Suben batches?
¿Suben tris o verts?
¿Suben SetPass calls?
¿Se comparó con una zona liviana?
¿Se confirmó con Profiler?
¿Se revisó Frame Debugger?
```

---

## Regla final

Stats Window sirve como señal rápida.

```txt
Stats
→ sospecha inicial

Profiler / Frame Debugger
→ diagnóstico más profundo
```

No debe usarse como única fuente de verdad.
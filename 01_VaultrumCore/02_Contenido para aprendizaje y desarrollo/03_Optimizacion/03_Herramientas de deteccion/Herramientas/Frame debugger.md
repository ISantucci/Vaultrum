## Definición

Frame Debugger es una herramienta de Unity que permite analizar cómo se renderiza un frame.

Muestra los pasos de renderizado que Unity realiza para construir la imagen final.

La idea principal es:

```txt
Frame Debugger
→ permite inspeccionar el render de un frame paso a paso
```

Es una herramienta enfocada principalmente en problemas visuales y de GPU/render.

---

## Para qué sirve

Frame Debugger sirve para entender qué está dibujando Unity y cómo.

Ayuda a responder:

- ¿Cuántos objetos se están renderizando?
- ¿Hay demasiados draw calls?
- ¿Los materiales rompen batching?
- ¿Qué se dibuja primero?
- ¿Qué sombras o luces están afectando?
- ¿Hay transparencias costosas?
- ¿Hay objetos renderizándose cuando no deberían?
- ¿El render está haciendo más trabajo del necesario?

La idea central es:

```txt
Si el problema parece visual/render,
Frame Debugger ayuda a ver qué pasa dentro del frame.
```

---

## Qué problemas ayuda a detectar

Frame Debugger ayuda a detectar:

```txt
GPU Bound
Draw calls excesivos
Batching roto
Materiales excesivos
Sombras costosas
Luces dinámicas
Transparencias
Objetos innecesariamente visibles
Render passes costosos
Problemas de shaders
Postprocesado pesado
```

No es la primera herramienta para problemas de scripts, IA o GC.

Para eso conviene usar:

```txt
Unity Profiler
CPU Usage
Timeline
GC Alloc
```

---

## Qué métricas mirar

En Frame Debugger conviene observar:

```txt
Cantidad de draw calls.
Objetos renderizados.
Materiales usados.
Cambios de shader/material.
Batches.
Sombras.
Luces.
Transparencias.
Render passes.
Orden de render.
```

También conviene conectar con otras señales:

```txt
Stats Window
→ batches / tris / setpass

Profiler
→ Rendering alto

Frame Debugger
→ detalle de qué se dibuja
```

---

## Cómo interpretar señales

Ejemplo 1:

```txt
Muchos objetos con materiales distintos
→ más draw calls
→ posible costo de render.
```

Ejemplo 2:

```txt
Muchas luces dinámicas con sombras
→ posible costo GPU alto.
```

Ejemplo 3:

```txt
Objetos que no deberían verse se renderizan igual
→ revisar culling, capas, cámaras.
```

Ejemplo 4:

```txt
Muchas transparencias superpuestas
→ posible overdraw.
```

Ejemplo 5:

```txt
Materiales similares no batchean
→ revisar configuración de batching/materiales.
```

---

## Qué NO demuestra por sí solo

Frame Debugger no demuestra que el problema general sea GPU.

Puede mostrar mucho trabajo de render, pero hay que confirmar con otras herramientas.

Ejemplo:

```txt
Veo muchos draw calls.
```

Eso sugiere revisar render, pero falta saber:

```txt
si el frame está realmente limitado por GPU,
si CPU también está costosa,
si el problema se siente en gameplay,
si reducir draw calls cambia el resultado.
```

Frame Debugger tampoco sirve para diagnosticar profundamente:

```txt
IA
Update
Pathfinding
GC Alloc
Memory Leak
```

---

## Ejemplo de uso

Ejemplo:

```txt
Síntoma:
El juego baja rendimiento al mirar una zona con muchos efectos.

Herramientas:
Profiler + Frame Debugger + Stats Window.

Hallazgo:
Muchas partículas transparentes.
Muchas luces.
Muchos materiales distintos.

Soluciones posibles:
Reducir partículas.
Optimizar materiales.
Reducir sombras.
Agrupar materiales.
Revisar culling.
Bajar postprocesado.
```

---

## Errores comunes al usarla

Errores comunes:

```txt
Usarla para problemas que son de CPU.
Mirar draw calls sin mirar contexto.
Reducir gráficos sin confirmar bottleneck.
No revisar Profiler.
No revisar Stats.
No validar después.
Pensar que todo draw call alto es automáticamente grave.
```

Otro error:

```txt
Optimizar render de una escena que no representa el gameplay real.
```

---

## Relación con otros sistemas

Frame Debugger se relaciona con:

```txt
Unity Profiler
Stats window
Recursos de hardware
Bottleneck
```

También se relaciona con problemas de:

```txt
GPU Bound
Render pesado
Sombras
Luces
Materiales
Partículas
```

---

## Checklist de uso

```txt
¿El problema parece visual/render?
¿Profiler muestra Rendering alto?
¿Stats muestra muchos batches/draw calls?
¿Hay muchas luces o sombras?
¿Hay muchas transparencias?
¿Hay objetos renderizados innecesariamente?
¿Hay materiales que rompen batching?
¿Se comparó antes/después?
```

---

## Regla final

Frame Debugger sirve para entender cómo se construye visualmente un frame.

```txt
Si el problema está en render,
hay que ver qué se está dibujando y por qué.
```

No reemplaza al Profiler.

Lo complementa.
## Definicion

Frame Debugger es una herramienta de Unity que permite analizar como se renderiza un frame.

Muestra los pasos de renderizado que Unity realiza para construir la imagen final.

La idea principal es:

```txt
Frame Debugger
→ permite inspeccionar el render de un frame paso a paso
```

Es una herramienta enfocada principalmente en problemas visuales y de GPU/render.

---

## Para que sirve

Frame Debugger sirve para entender que esta dibujando Unity y como.

Ayuda a responder:

- ¿Cuantos objetos se estan renderizando?
- ¿Hay demasiados draw calls?
- ¿Los materiales rompen batching?
- ¿Que se dibuja primero?
- ¿Que sombras o luces estan afectando?
- ¿Hay transparencias costosas?
- ¿Hay objetos renderizandose cuando no deberian?
- ¿El render esta haciendo mas trabajo del necesario?

La idea central es:

```txt
Si el problema parece visual/render,
Frame Debugger ayuda a ver que pasa dentro del frame.
```

---

## Que problemas ayuda a detectar

Frame Debugger ayuda a detectar:

```txt
GPU Bound
Draw calls excesivos
Batching roto
Materiales excesivos
Sombras costosas
Luces dinamicas
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

## Que metricas mirar

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

Tambien conviene conectar con otras señales:

```txt
Stats Window
→ batches / tris / setpass

Profiler
→ Rendering alto

Frame Debugger
→ detalle de que se dibuja
```

---

## Como interpretar señales

Ejemplo 1:

```txt
Muchos objetos con materiales distintos
→ mas draw calls
→ posible costo de render.
```

Ejemplo 2:

```txt
Muchas luces dinamicas con sombras
→ posible costo GPU alto.
```

Ejemplo 3:

```txt
Objetos que no deberian verse se renderizan igual
→ revisar culling, capas, camaras.
```

Ejemplo 4:

```txt
Muchas transparencias superpuestas
→ posible overdraw.
```

Ejemplo 5:

```txt
Materiales similares no batchean
→ revisar configuracion de batching/materiales.
```

---

## Que NO demuestra por si solo

Frame Debugger no demuestra que el problema general sea GPU.

Puede mostrar mucho trabajo de render, pero hay que confirmar con otras herramientas.

Ejemplo:

```txt
Veo muchos draw calls.
```

Eso sugiere revisar render, pero falta saber:

```txt
si el frame esta realmente limitado por GPU,
si CPU tambien esta costosa,
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
Sintoma:
El juego baja rendimiento al mirar una zona con muchos efectos.

Herramientas:
Profiler + Frame Debugger + Stats Window.

Hallazgo:
Muchas particulas transparentes.
Muchas luces.
Muchos materiales distintos.

Soluciones posibles:
Reducir particulas.
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
Reducir graficos sin confirmar bottleneck.
No revisar Profiler.
No revisar Stats.
No validar despues.
Pensar que todo draw call alto es automaticamente grave.
```

Otro error:

```txt
Optimizar render de una escena que no representa el gameplay real.
```

---

## Relacion con otros sistemas

Frame Debugger se relaciona con:

```txt
Unity Profiler
Stats window
Recursos de hardware
Bottleneck
```

Tambien se relaciona con problemas de:

```txt
GPU Bound
Overdraw y transparencias
Costo de fragmentos y shaders
Costo de vertices y geometria
Sombras costosas
Iluminacion en runtime
Post processing pesado
Draw calls y batching
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
¿Se comparo antes/despues?
```

---

## Regla final

Frame Debugger sirve para entender como se construye visualmente un frame.

```txt
Si el problema esta en render,
hay que ver que se esta dibujando y por que.
```

No reemplaza al Profiler.

Lo complementa.
## Definicion

Los recursos de hardware son las capacidades fisicas y de ejecucion que el juego utiliza para funcionar.

En optimizacion, entender estos recursos permite diagnosticar que parte del sistema esta siendo exigida.

Los recursos principales son:

```txt
CPU
GPU
Memoria RAM
VRAM
Disco
```

Tambien hay componentes del runtime que afectan rendimiento, como:

```txt
Garbage Collector
Game Loop
Sistema de carga
Motor de fisica
Render pipeline
```

La idea principal es:

```txt
Cada problema de rendimiento afecta algun recurso.
```

---

## Responsabilidad de esta nota

Esta nota existe para explicar que recursos pueden limitar el rendimiento de un videojuego.

No existe para diagnosticar todos los problemas concretos.
No existe para reemplazar herramientas de medicion.
No existe para proponer soluciones automaticamente.

Su responsabilidad es ayudar a responder:

```txt
¿Que recurso podria estar afectado?
```

Esta nota funciona como mapa conceptual antes de pasar a problemas, herramientas o soluciones.

---

## Que problema ayuda a entender

Entender recursos de hardware ayuda a clasificar problemas.

Ejemplo:

```txt
Muchos Update activos
→ CPU

Sombras pesadas
→ GPU

Texturas enormes cargadas
→ memoria / VRAM

Strings creados por frame
→ GC

Carga de assets durante gameplay
→ disco / memoria / CPU
```

Si no se entiende que recurso esta afectado, se puede elegir una solucion incorrecta.

Ejemplo:

```txt
Problema:
Memoria alta por texturas.

Solucion incorrecta:
Reducir Update.

Solucion mas logica:
Revisar assets, texturas, compresion, carga y descarga.
```

---

## Como funciona

Cada recurso cumple un rol distinto.

### CPU

Ejecuta logica general.

```txt
Scripts
IA
Fisica
Pathfinding
Animaciones
UI
Eventos
Managers
Calculos
```

Problemas tipicos:

```txt
Muchos Update.
Busquedas globales.
Fisica costosa.
IA pesada.
Loops innecesarios.
```

---

### GPU

Procesa render.

```txt
Modelos
Materiales
Luces
Sombras
Shaders
Particulas
Postprocesado
Transparencias
Resolucion
```

Problemas tipicos:

```txt
Demasiados draw calls.
Sombras costosas.
Luces dinamicas.
Shaders pesados.
Particulas excesivas.
```

---

### RAM

Memoria principal del sistema.

Guarda datos usados por el juego.

```txt
Objetos
Escenas
Datos de gameplay
Audio
Texturas cargadas
Listas
Pools
Referencias
```

Problemas tipicos:

```txt
Memory leaks.
Assets que no se liberan.
Pools enormes.
Listas que crecen.
Escenas pesadas.
```

---

### VRAM

Memoria de video usada por la GPU.

Guarda recursos visuales.

```txt
Texturas
Render textures
Meshes
Materiales
Buffers
Sombras
```

Problemas tipicos:

```txt
Texturas muy grandes.
Muchas render textures.
Assets visuales pesados.
Materiales y buffers excesivos.
```

---

### Disco

Se usa para cargar datos.

```txt
Escenas
Assets
Archivos
Addressables
Guardados
Streaming
```

Problemas tipicos:

```txt
Cargas lentas.
Stuttering por streaming.
Lectura de archivos durante gameplay.
Assets cargados en momentos criticos.
```

---

### Garbage Collector

No es hardware, pero afecta runtime.

Se encarga de limpiar memoria administrada que ya no se usa.

Problemas tipicos:

```txt
Allocations por frame.
Strings temporales.
Listas nuevas.
Arrays temporales.
Instantiate/Destroy.
```

Sintomas:

```txt
Spikes.
Stuttering.
Frame time irregular.
```

---

## Como aplicarlo en videojuegos

Cuando aparece un problema, conviene traducirlo a recurso afectado.

Ejemplos:

```txt
Se traba al disparar muchas balas.
→ CPU / GC / memoria / particulas.

Se pone lento al mirar una zona iluminada.
→ GPU.

Cada partida consume mas memoria.
→ RAM / memory leak.

Tarda mucho en cargar nivel.
→ disco / assets / memoria.

Tirones cada pocos segundos.
→ GC o spikes de CPU.
```

Ejemplo inspirado en Tower Defense:

```txt
Muchos enemigos
→ CPU por IA/movimiento
→ memoria por objetos activos

Muchas torres disparando
→ CPU por targeting
→ GC por proyectiles si no hay pool
→ GPU por efectos

Mapa grande con assets pesados
→ memoria / VRAM / carga
```

La pregunta no es solamente:

```txt
¿Que se ve lento?
```

Sino:

```txt
¿Que recurso esta siendo exigido?
```

---

## Como guia el diagnostico

Esta nota ayuda a elegir hacia donde mirar.

Flujo recomendado:

```txt
Sintoma
→ recurso sospechado
→ herramienta adecuada
→ dato medido
→ problema probable
→ solucion candidata
```

Ejemplo:

```txt
Sintoma:
El juego tiene tirones al disparar.

Recursos posibles:
CPU
GC
GPU

Herramientas:
Unity Profiler
Timeline
GC Alloc
Frame Debugger

Diagnostico:
No se elige hasta medir.
```

Otro ejemplo:

```txt
Sintoma:
La memoria sube con cada partida.

Recurso sospechado:
RAM.

Herramienta:
Memory Profiler.

Problema posible:
Memory Leak o assets no liberados.
```

---

## Cuando conviene consultarlo

Conviene consultar Recursos de hardware cuando:

```txt
No esta claro si el problema es CPU, GPU, memoria, GC o carga.
Una solucion no mejoro el rendimiento.
Una IA propone una optimizacion sin explicar que recurso afecta.
Hay sintomas generales como baja de FPS o stuttering.
Hay que elegir herramienta de medicion.
Se quiere analizar escalabilidad del proyecto.
```

Tambien conviene usarlo como punto de apoyo antes de diagnosticar bottlenecks.

---

## Cuando NO conviene forzarlo

No conviene usar esta nota para resolver directamente un problema concreto.

Ejemplo:

```txt
Hay GC Alloc por frame.
```

En ese caso, esta nota puede explicar que el GC afecta runtime, pero el diagnostico puntual pertenece a Problemas de rendimiento y Herramientas de deteccion.

Tampoco conviene convertir esta nota en una lista infinita de hardware.

Solo debe contener lo necesario para entender optimizacion en videojuegos.

---

## Errores que ayuda a evitar

Entender recursos de hardware ayuda a evitar:

- Confundir CPU con GPU.
- Confundir memoria con Garbage Collector.
- Bajar graficos cuando el problema es scripts.
- Optimizar scripts cuando el problema es render.
- Ignorar VRAM.
- Ignorar cargas de disco.
- Tratar todos los spikes como iguales.
- Elegir herramientas incorrectas.
- Aplicar soluciones que no atacan el recurso afectado.

La idea clave es:

```txt
Cada solucion debe corresponder al recurso que realmente esta limitando.
```

---

## Riesgos de interpretarlo mal

Un riesgo comun es pensar que un sintoma pertenece siempre al mismo recurso.

Ejemplo:

```txt
Baja de FPS
→ no siempre es GPU.

Stuttering
→ no siempre es GC.

Memoria alta
→ no siempre es leak.
```

Otro riesgo es analizar recursos de forma aislada.

Ejemplo:

```txt
Carga de assets
→ puede afectar disco, memoria, CPU y frame time.
```

Los recursos se relacionan, pero hay que identificar cual esta limitando en ese contexto.

---

## Hacia donde seguir

Esta nota pertenece a Fundamentos.

Si se quiere entender el limite general:

```txt
→ [[Bottleneck]]
```

Si se quiere entender el tiempo disponible:

```txt
→ [[Frame Budget]]
```

Si el recurso sospechado es CPU:

```txt
→ [[CPU Bound]]
```

Si hay un sintoma concreto:

```txt
→ [[Problemas de rendimiento]]
```

Si hace falta medir:

```txt
→ [[Herramientas de deteccion]]
```

Si ya se confirmo el problema:

```txt
→ [[Metodologias y soluciones]]
```

---

## Checklist de diagnostico

Antes de decidir que recurso esta afectado, revisar:

```txt
¿Cual es el sintoma?
¿Cuando ocurre?
¿El problema es constante o puntual?
¿Aparece con mas objetos?
¿Aparece con mas render?
¿Aparece con mas memoria cargada?
¿Aparece al crear/destruir objetos?
¿Aparece al cargar assets?
¿Que herramienta puede medirlo?
¿Que dato confirmaria el recurso afectado?
```

---

## Regla final

No se optimiza en abstracto.

Se optimiza un recurso afectado por un problema concreto.

```txt
Sintoma
→ recurso sospechado
→ medicion
→ diagnostico
→ solucion
```
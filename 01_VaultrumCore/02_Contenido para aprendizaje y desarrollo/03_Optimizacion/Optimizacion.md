## Proposito

Esta seccion reune criterios, problemas, herramientas y metodologias relacionadas con optimizacion de videojuegos.

No existe para juntar tips sueltos de rendimiento.
No existe para aplicar tecnicas avanzadas por costumbre.
No existe para optimizar por intuicion.
No existe para volver mas complejo un sistema que todavia no tiene un problema medido.

Existe para ayudar a una persona o una IA a medir, diagnosticar y mejorar el uso de recursos de un proyecto con criterio.

La regla central es:

```txt
Primero se mide.
Despues se optimiza.
```

---

## Idea central

Optimizar no es hacer que el juego tenga mas FPS.

Optimizar es administrar recursos limitados para cumplir un objetivo de rendimiento determinado.

Los recursos que compiten durante la ejecucion son:

```txt
tiempo de CPU
tiempo de GPU
memoria
ancho de banda de memoria
almacenamiento / I/O
tiempo disponible por frame
```

Por eso la pregunta correcta nunca es:

```txt
¿Como hago esto mas rapido?
```

La pregunta anterior es:

```txt
¿Esto esta limitando realmente al juego?
```

Una optimizacion sin diagnostico previo es una modificacion especulativa. Puede no mejorar nada, empeorar otra parte, aumentar la complejidad, consumir mas memoria, introducir bugs, dificultar el mantenimiento o simplemente trasladar el cuello de botella a otro recurso.

---

## Para que sirve esta seccion

Esta seccion sirve para construir criterio de diagnostico y optimizacion.

Debe ayudar a responder:

```txt
¿Que problema de rendimiento hay?
¿Como se mide?
¿Que recurso esta afectado?
¿Que herramienta usar?
¿Que solucion puede aplicar?
¿Que trade-off trae?
¿Como se valida si mejoro?
```

El objetivo es que sirva tanto para estudiar como para aplicar en proyectos reales.

---

## El principio que organiza esta seccion

Esta seccion esta separada por recurso: CPU, GPU, memoria, carga y UI tienen cada uno su rama.

Pero la separacion no es la puerta de entrada.

```txt
                    PERFORMANCE
                         |
                 ¿que esta limitando?
                         |
        +----------------+-----------------+
        v                v                 v
       CPU              GPU             Memoria
        |                |                 |
        +------------+---+-----------------+
                     v
              causa concreta
                     v
                  solucion
                     v
                 trade-off
                     v
                 validacion
```

Por encima de todas las ramas esta el diagnostico, porque es lo unico que permite decidir a cual entrar.

```txt
No se empieza optimizando CPU.
No se empieza optimizando GPU.
Se empieza midiendo.

CPU, GPU, memoria o I/O son respuestas posibles al diagnostico,
no puntos de partida.
```

Memoria, carga y UI no se meten adentro de CPU o de GPU para conseguir una arquitectura binaria. Son dimensiones propias porque existen problemas de performance que no encajan en ninguno de los dos procesadores, y porque la UI cuesta en los dos a la vez.

---

## Organizacion de la seccion

```txt
03_Optimizacion/
├── Optimizacion.md
├── 01_Fundamentos/                el marco previo a cualquier diagnostico
├── 02_Diagnostico/                el metodo y las herramientas de medicion
├── 03_CPU/                        problemas y soluciones de tiempo de CPU
├── 04_GPU/                        problemas y soluciones de tiempo de GPU
├── 05_Memoria/                    allocations, GC, retencion y lifecycle
├── 06_Carga e IO/                 startup, transiciones, streaming, freezes
├── 07_UI/                         cuesta en CPU y en GPU a la vez
└── 08_Patrones transversales/     lo que aplica en mas de una rama
```

El recorrido esperado es:

```txt
Fundamentos
→ Diagnostico
→ la rama del recurso afectado
→ solucion
→ trade-off
→ validacion
```

---

## [[Fundamentos]]

Conceptos base para entender optimizacion antes de diagnosticar o proponer soluciones.

Esta rama sirve para entender el marco general:

```txt
presupuesto de frame
frame time y estabilidad
cuellos de botella
recursos afectados
game loop
costo x cantidad x frecuencia
reducir trabajo antes que acelerarlo
trade-offs
valor perceptual por costo
medicion previa
cuando NO optimizar
```

Usar esta rama cuando todavia haga falta entender que esta pasando antes de analizar un problema concreto.

---

## [[Diagnostico]]

El metodo y las herramientas que permiten decidir a que rama entrar.

Esta rama sirve para pasar de un sintoma a un recurso identificado:

```txt
flujo de diagnostico
CPU Bound
GPU Bound
traslado del cuello de botella
comparacion antes y despues
Unity Profiler
CPU Usage
Timeline
GC Alloc
Memory Profiler
Frame Debugger
Stats
logs de diagnostico
```

Usar esta rama siempre, y antes que cualquier otra. Es la unica que no se saltea.

---

## [[CPU]]

Problemas y soluciones del tiempo de CPU: simulacion, gameplay, scripts, fisica, IA, spawning y preparacion del rendering.

Usar esta rama cuando el diagnostico apunte a CPU:

```txt
muchos Update activos
busquedas globales por frame
Instantiate y Destroy constantes
pathfinding recalculado demasiado seguido
fisica costosa
IA que piensa de mas
```

---

## [[GPU]]

Problemas y soluciones del tiempo de GPU: vertices, rasterizacion, fragmentos, texturas, iluminacion y blending.

Usar esta rama cuando el diagnostico apunte a GPU:

```txt
overdraw y transparencias
fill rate y resolucion
costo de fragmentos y shaders
costo de vertices y geometria
sombras costosas
iluminacion en runtime
post processing pesado
```

Advertencia que esta rama repite: draw call no es sinonimo de problema de GPU. Rendering involucra a los dos procesadores.

---

## [[Memoria]]

Memoria es una dimension propia, no una consecuencia de CPU ni de GPU.

Usar esta rama cuando el problema sea de allocations, presion del recolector, retencion o crecimiento sostenido:

```txt
GC Alloc por frame
strings por frame
memory leak
object pooling
evitar allocations por frame
ciclo de vida de recursos
```

---

## [[Carga e IO]]

El rendimiento no es exclusivamente FPS. Startup, pantallas de carga, transiciones, streaming y freezes tambien lo son.

Usar esta rama cuando el problema aparezca al cargar, al cambiar de escena o al entrar a una zona:

```txt
freeze por carga en runtime
Addressables
AssetManager
precarga y carga distribuida
```

---

## [[UI]]

La UI no se clasifica solamente como CPU ni solamente como GPU: cuesta en los dos.

```txt
CPU   actualizacion, layout, rebuilds, generacion de texto, input, raycasts
GPU   transparencias, imagenes, mascaras, overdraw, grandes superficies
```

Usar esta rama cuando el costo aparezca al abrir una pantalla, al actualizar el HUD o al mover listas.

---

## [[Patrones transversales]]

Lo que no pertenece a un solo recurso: patrones que aplican en CPU, en GPU, en fisica, en IA y en rendering, mas la arquitectura que permite optimizar sin romper comportamiento.

```txt
Early Exit
broad phase y narrow phase
Active Set
escalado de precision
batch processing
clases puras
MonoBehaviour como puente
separar logica de Unity
separacion model / view
```

Usar esta rama cuando la misma idea reaparezca en dos ramas distintas.

---

## Huecos declarados

Estos temas pueden aparecer en un diagnostico y todavia no tienen ficha propia en la seccion.

Se dejan escritos como texto plano hasta que exista una necesidad real de desarrollarlos. Un hueco declarado es criterio; un hueco silencioso es una promesa que la seccion no cumple.

```txt
Stuttering como sintoma propio
    hoy se trata repartido entre frame time, memoria y carga

Assets mal gestionados
    hoy se trata desde Carga e IO, sin ficha de problema propia

Pools mal dimensionados
    hoy vive dentro de la nota de object pooling

Eventos no desuscriptos
    hoy vive dentro de memory leak

Render pipeline y sus variantes
    la seccion habla de etapas, no de pipelines concretos

Multithreading y paralelismo
    solo aparece como advertencia en errores conceptuales
```

Lo que cerro el refactor y ya no es hueco:

```txt
Fisica costosa       ahora tiene ficha en CPU
GPU Bound            ahora tiene ficha en Diagnostico
overdraw, fill rate, shaders, geometria,
sombras, iluminacion, post processing        ahora tienen ficha en GPU
LOD, culling, batching, mipmaps              ahora tienen ficha en GPU
```

---

## Temas relacionados que no son de esta seccion

Estos temas aparecen en el razonamiento de optimizacion pero pertenecen a otra parte del Core.

```txt
Patrones de diseño       → 02_Patrones de diseno
Managers                 → 08_Managers
SOLID                    → 01_SOLID
Estructuras de datos     → 06_Estructuras de datos
Algoritmos               → 07_Algoritmos
Criterios de entrega     → 04_Criterios de entrega
```

Se nombran, no se enlazan desde aca, salvo que haya una necesidad operativa concreta.

Las notas de esta seccion que comparten nombre con una de esas secciones cubren solo la mitad de optimizacion del tema. La mitad estructural pertenece a la seccion dueña.

---

## Guia rapida de diagnostico

Esta guia no decide automaticamente. Solo orienta hacia que parte de la seccion conviene ir.

```txt
Necesito entender conceptos base
→ Fundamentos

Hay caida de FPS, spikes, stuttering o input lag
→ Diagnostico

Tengo un sintoma y no se de quien es
→ Diagnostico

El frame es caro y la escena es visualmente simple
→ Diagnostico, despues CPU

El frame es caro y la escena es visualmente rica
→ Diagnostico, despues GPU

Hay spikes periodicos o la memoria crece
→ Memoria

El freeze aparece al cargar o al cambiar de escena
→ Carga e IO

El costo aparece al abrir una pantalla o mover el HUD
→ UI

La misma idea me sirve en dos ramas
→ Patrones transversales
```

---

## Formato de una ficha de performance

Todo problema de performance documentado en esta seccion responde estas preguntas, en este orden:

```txt
Problema            que ocurre
Area                CPU / GPU / Memoria / I/O / Mixto
Sintoma observable  que ve el desarrollador o el jugador
Causa tecnica       que sucede realmente
Deteccion           que herramienta o metrica lo confirma
Diagnostico         como distinguirlo de causas parecidas
Solucion            opciones disponibles
Trade-off           que cuesta cada solucion
Validacion          como se demuestra que funciono
Error frecuente     que interpretacion incorrecta suele hacerse
```

Una ficha que no puede completar Deteccion, Trade-off y Validacion todavia no es una ficha: es una intuicion escrita.

---

## Uso por agentes en Vaultrum

Cuando una IA trabaje sobre un problema de rendimiento, debe usar esta seccion como apoyo de diagnostico.

No debe usarla como lista de tecnicas para aplicar.

Antes de proponer una optimizacion, debe poder explicar:

```txt
Sintoma observado
Recurso posiblemente afectado
Herramienta para medir
Dato que confirmaria el problema
Solucion candidata
Trade-off
Validacion antes/despues
```

La IA no debe razonar asi:

```txt
Hay muchos objetos.
→ usar Object Pool.
```

Debe razonar asi:

```txt
Hay muchos objetos temporales.
→ medir Instantiate/Destroy y GC Alloc.
→ confirmar costo.
→ evaluar Object Pool.
→ revisar trade-off.
→ validar mejora.
```

Si todavia no se puede medir, la IA debe declararlo y proponer como validar la hipotesis.

---

## Como NO debe usar esta seccion una IA

Una IA no debe usar esta seccion para justificar optimizaciones prematuras.

No debe:

- proponer tecnicas sin sintoma,
- aplicar soluciones sin medir,
- confundir cantidad con costo real,
- entrar directo a una rama sin pasar por Diagnostico,
- usar Object Pool porque hay objetos,
- usar Update Manager porque hay Updates,
- usar Addressables porque hay assets,
- bajar calidad visual sin diagnostico,
- reducir draw calls como objetivo en si mismo,
- agregar sistemas complejos sin trade-off claro,
- modificar arquitectura sin validar impacto,
- prometer mejoras sin definir como medirlas.

La IA debe recordar:

```txt
La optimizacion requiere evidencia o una hipotesis tecnica clara.
```

---

## Antes de proponer una optimizacion

Estas diez preguntas son el filtro previo. Si alguna no tiene respuesta, todavia no hay una propuesta: hay una intuicion.

```txt
¿Cual es el sintoma?
¿Como se reproduce?
¿Que recurso podria estar afectado?
¿Que herramienta permite medirlo?
¿Que dato confirmaria el problema?
¿Que solucion candidata existe?
¿Que alternativa mas simple existe?
¿Que trade-off trae?
¿Que riesgo introduce?
¿Como se valida antes y despues?
```

Las dos que mas se saltean son la segunda y la septima.

Sin reproduccion no hay medicion comparable: se mide una vez, se cambia algo y se mide otra cosa. Y sin la pregunta por la alternativa mas simple, toda propuesta tiende hacia la solucion mas elaborada, que es tambien la mas cara de mantener.

```txt
Antes de un pool, ¿alcanza con no destruir?
Antes de un Update Manager, ¿alcanza con apagar el componente?
Antes de particionar el espacio, ¿alcanza con filtrar por distancia?
Antes de un sistema de LOD, ¿alcanza con una distancia de dibujado?
```

---

## Antes de ejecutar una optimizacion

Antes de ejecutar, hay que entregar:

```txt
Sintoma:
Medicion disponible o pendiente:
Diagnostico:
Rama afectada:
Solucion propuesta:
Sistema existente relacionado:
Archivos que podria tocar:
Archivos que no deberia tocar:
Trade-off:
Riesgos:
Validacion:
Decision requerida:
```

La ejecucion requiere aprobacion.

---

## Principios fundamentales

```txt
1.  Medir antes de optimizar.
2.  Trabajar con frame time, no solo con FPS.
3.  Identificar el bottleneck antes de modificar.
4.  Reducir trabajo antes de intentar acelerarlo.
5.  Costo real = costo unitario x frecuencia x cantidad.
6.  Filtrar barato antes de validar caro.
7.  No actualizar lo que no necesita actualizarse.
8.  No recalcular informacion estable.
9.  Priorizar algoritmo y estructura de datos antes que microoptimizacion.
10. Pooling y caching son trade-offs, no reglas universales.
11. CPU y GPU se diagnostican por separado.
12. Rendering puede ser costoso tanto en CPU como en GPU.
13. Memoria es una dimension independiente.
14. Loading e I/O tambien forman parte de performance.
15. La UI se analiza en CPU y en GPU.
16. LOD es un principio perceptual, no solo un sistema de mallas.
17. Culling significa evitar trabajo que no contribuye.
18. La arquitectura debe facilitar optimizar, no nacer de optimizaciones hipoteticas.
19. Toda optimizacion tiene trade-offs.
20. Toda optimizacion necesita validacion posterior.
21. Un buen numero de profiler no justifica romper gameplay, feedback o estabilidad.
22. Performance existe para sostener la experiencia del jugador.
```

---

## Criterio de uso

La optimizacion debe estar al servicio del juego. No se optimiza para demostrar tecnica.

Se optimiza para sostener:

```txt
Estabilidad
Fluidez
Escalabilidad
Mantenibilidad
Experiencia del jugador
```

Una buena optimizacion cumple estas condiciones:

```txt
Resuelve un problema medido.
No rompe gameplay.
No destruye arquitectura.
No agrega complejidad innecesaria.
Tiene trade-offs claros.
Puede validarse antes/despues.
```

Una mala optimizacion suele tener alguna de estas señales:

```txt
Se aplica sin medir.
Resuelve un problema que no existe.
Complica sistemas simples.
Mezcla responsabilidades.
Reduce calidad sin justificar.
Introduce bugs.
No se valida despues.
```

---

## Regla final

La optimizacion no empieza tocando codigo.

Empieza entendiendo el problema.

```txt
Primero medir.
Despues diagnosticar.
Despues entrar a la rama.
Despues optimizar.
Despues validar.
```

Si no se puede explicar que recurso esta afectado, que herramienta lo muestra y que trade-off trae la solucion, todavia no hay una optimizacion clara.

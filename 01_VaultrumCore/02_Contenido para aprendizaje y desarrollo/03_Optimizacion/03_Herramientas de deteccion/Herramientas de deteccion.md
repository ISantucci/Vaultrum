## Proposito

Esta subcarpeta reune herramientas para medir, observar y confirmar problemas de rendimiento.

No existe para optimizar por si sola.
No existe para reemplazar el criterio.
No existe para decidir soluciones automaticamente.

Existe para transformar sensaciones o hipotesis en datos observables.

La idea principal es:

```txt
sintoma
→ herramienta
→ dato
→ interpretacion
→ diagnostico
```

---

## Idea central

En optimizacion, medir es obligatorio.

No alcanza con decir:

```txt
se siente lento
```

Hay que poder observar datos como:

```txt
frame time
CPU usage
GPU usage
GC Alloc
memoria usada
spikes
draw calls
tiempo de scripts
tiempo de fisica
tiempo de render
cantidad de objetos activos
```

Una herramienta no optimiza por si sola.

Una herramienta muestra evidencia.

El criterio interpreta esa evidencia.

---

## Cuando usar esta subcarpeta

Usar esta subcarpeta cuando haga falta medir o confirmar una hipotesis.

Conviene consultarla cuando:

- hay un sintoma pero no se conoce la causa,
- se necesita confirmar un bottleneck,
- se sospecha de CPU, GPU, memoria o GC,
- se quiere comparar antes y despues,
- una IA propone una optimizacion sin datos,
- se necesita saber que mirar dentro de Unity,
- hay que validar si una solucion funciono.

---

## Como debe usar esta subcarpeta una IA

Una IA debe usar esta subcarpeta para decidir como medir antes de proponer o validar cambios.

No debe razonar asi:

```txt
El juego va lento.
→ seguramente es GPU.
```

Debe razonar asi:

```txt
El juego va lento.
→ elegir herramienta adecuada.
→ medir.
→ interpretar datos.
→ recien despues diagnosticar.
```

---

## Herramientas incluidas

### [[Unity Profiler]]

Herramienta central para observar rendimiento general del juego.

Consultar cuando haga falta investigar CPU, memoria, GC, spikes, scripts, fisica, render o timeline del frame.

### [[CPU Usage]]

Modulo o vista para analizar que consume tiempo de CPU.

Consultar cuando el problema parezca venir de scripts, fisica, IA, Update, animaciones o logica de gameplay.

### [[Timeline]]

Vista que permite analizar que ocurre dentro de un frame y en que orden.

Consultar cuando haya spikes, trabas puntuales o se necesite ver la distribucion temporal del costo.

### [[GC Alloc]]

Indicador para detectar allocations que pueden presionar al Garbage Collector.

Consultar cuando haya tirones, spikes o memoria temporal creada durante gameplay.

### [[Memory Profiler]]

Herramienta para analizar memoria, objetos retenidos, assets cargados y posibles leaks.

Consultar cuando el uso de memoria crece, hay referencias vivas o assets que no se liberan.

### [[Frame debugger|Frame Debugger]]

Herramienta para inspeccionar el proceso de renderizado frame por frame.

Consultar cuando el problema parezca venir de draw calls, materiales, shaders, transparencia o render.

### [[Stats window|Stats]]

Ventana rapida para observar datos basicos de render y rendimiento.

Consultar como apoyo inicial, no como diagnostico final.

### [[Logs de diagnostico]]

Registros manuales para confirmar flujos, conteos, eventos o ejecuciones esperadas.

Consultar cuando haga falta evidencia simple de comportamiento interno.

### [[Comparacion antes y despues]]

Metodo para validar si una optimizacion realmente mejoro el sistema.

Consultar siempre que se aplique una solucion de rendimiento.

---

## Como elegir herramienta

Esta guia no decide automaticamente.

Solo orienta la busqueda.

```txt
Costo general de frame
→ Unity Profiler

Costo de scripts o logica
→ CPU Usage

Spikes puntuales
→ Timeline

Allocations o GC
→ GC Alloc

Memoria creciendo
→ Memory Profiler

Render o draw calls
→ Frame Debugger / Stats

Validacion de cambio
→ Comparacion antes y despues

Confirmar flujo interno
→ Logs de diagnostico
```

---

## Como se conecta con otras subcarpetas

Esta subcarpeta funciona como puente entre problema y solucion.

```txt
Problema sospechado
→ herramienta de deteccion
→ dato medido
→ diagnostico
→ solucion candidata
```

Ejemplo:

```txt
Problema sospechado:
GC Alloc por frame.

Herramienta:
GC Alloc / Unity Profiler.

Dato:
Allocations constantes durante gameplay.

Solucion candidata:
Evitar allocations por frame.
```

---

## Criterio de uso

Una herramienta no demuestra todo por si sola.

Cada dato debe interpretarse en contexto.

Antes de sacar una conclusion, preguntar:

```txt
Que estoy midiendo?
En que escena o situacion?
El problema es constante o puntual?
El dato confirma la hipotesis?
Que otra causa podria explicar el sintoma?
Como comparo antes y despues?
```

---

## Regla final

```txt
Herramientas de deteccion no existe para adivinar soluciones.
Existe para medir antes de decidir.
```
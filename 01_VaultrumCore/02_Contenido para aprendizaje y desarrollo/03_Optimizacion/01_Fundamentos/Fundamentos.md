## Proposito

Esta subcarpeta reune los conceptos base necesarios para entender optimizacion en videojuegos.

No existe para resolver problemas puntuales.
No existe para listar tecnicas.
No existe para proponer soluciones directamente.

Existe para construir el criterio previo que permite diagnosticar bien.

Antes de hablar de herramientas, problemas o soluciones, una persona o una IA necesita entender:

```txt
presupuesto de frame
cuellos de botella
recursos afectados
game loop
medicion
criterio previo a la optimizacion
```

---

## Idea central

Los fundamentos explican el marco mental de la optimizacion.

Esta subcarpeta responde:

```txt
Que significa optimizar?
Que recursos existen?
Que limita el rendimiento?
Que pasa cuando un sistema no entra en el tiempo de frame?
Por que hay que medir antes de tocar codigo?
```

La idea principal es:

```txt
No se puede diagnosticar bien lo que no se entiende.
```

---

## Cuando usar esta subcarpeta

Usar esta subcarpeta cuando haga falta entender conceptos base antes de analizar un problema de rendimiento.

Conviene consultarla cuando:

- no esta claro que significa optimizar,
- no se entiende el costo por frame,
- no se sabe que recurso puede estar afectado,
- se necesita diferenciar CPU, GPU, memoria, GC o carga,
- se quiere entender que es un bottleneck,
- se necesita justificar por que medir antes de optimizar,
- una IA esta por proponer una solucion sin diagnostico claro,
- un sistema funciona pero no se sabe si escala.

---

## Como debe usar esta subcarpeta una IA

Una IA debe usar Fundamentos para construir criterio antes de proponer una optimizacion.

No debe saltar directo a una tecnica.

Debe razonar asi:

```txt
Sintoma observado
→ concepto base relacionado
→ recurso posiblemente afectado
→ herramienta de medicion
→ diagnostico
→ solucion candidata
```

Ejemplo:

```txt
El juego tiene caidas de FPS.
→ revisar Frame Budget.
→ revisar Bottleneck.
→ identificar si el limite esta en CPU, GPU, memoria o GC.
→ recien despues proponer una medicion o solucion.
```

---

## Notas incluidas

### [[Frame Budget]]

Explica cuanto tiempo tiene disponible cada frame segun el objetivo de FPS.

Consultar cuando el problema este relacionado con caidas de FPS, costo por frame, frecuencia de ejecucion o estabilidad general.

### [[Bottleneck]]

Explica que es un cuello de botella y por que no todos los problemas de rendimiento tienen la misma causa.

Consultar cuando haya que identificar que parte del sistema esta limitando el rendimiento.

### [[Game loop]]

Explica el ciclo principal del juego y como se ejecutan los sistemas a lo largo del tiempo.

Consultar cuando el problema este relacionado con Update, FixedUpdate, frecuencia de ejecucion o carga de trabajo por frame.

### [[CPU Bound]]

Explica que significa que el rendimiento este limitado por CPU.

Consultar cuando el costo parezca venir de scripts, logica, IA, fisica, pathfinding, busquedas o sistemas ejecutandose en CPU.

### [[Recursos de hardware]]

Explica los recursos principales que pueden afectar el rendimiento de un videojuego.

Consultar cuando haga falta diferenciar CPU, GPU, memoria, VRAM, disco, GC u otros recursos.

### [[Medir antes de optimizar]]

Explica por que una optimizacion debe partir de medicion, evidencia o una hipotesis tecnica clara.

Consultar antes de proponer cualquier solucion de rendimiento.

### [[Cuando NO optimizar]]

Explica por que una optimizacion tambien necesita encargo, y no solo evidencia.

Consultar antes de [[Medir antes de optimizar]]: primero se decide si corresponde optimizar, despues con que evidencia.

---

## Relacion con el resto de Optimizacion

Fundamentos no resuelve el problema completo.

Fundamentos ayuda a entenderlo.

El flujo correcto es:

```txt
fundamento
→ problema posible
→ herramienta de deteccion
→ solucion candidata
→ validacion
```

---

## Criterio de uso

Esta subcarpeta debe mantenerse como base conceptual.

No debe crecer con problemas concretos.

No debe convertirse en una lista de soluciones.

No debe repetir el contenido de herramientas o metodologias.

Si aparece una nota nueva, primero hay que preguntar:

```txt
Es un concepto base?
Ayuda a entender optimizacion antes del diagnostico?
Pertenece a Fundamentos o a otra subcarpeta?
```

---

## Regla final

```txt
Fundamentos no existe para optimizar directamente.
Existe para entender antes de diagnosticar.
```
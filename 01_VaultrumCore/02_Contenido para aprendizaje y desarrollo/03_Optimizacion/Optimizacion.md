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

Optimizar en videojuegos significa mejorar el uso de recursos para sostener una experiencia estable, fluida y escalable.

No significa solamente subir FPS.

Un videojuego funciona en tiempo real. Cada frame tiene un presupuesto limitado. Si una parte del sistema consume mas de lo que corresponde, aparecen problemas como:

```txt
caidas de FPS
spikes
stuttering
input lag
cargas lentas
uso excesivo de memoria
presion del Garbage Collector
```

La idea principal es:

```txt
No alcanza con que algo funcione.
Tambien importa cuanto cuesta, cuantas veces se ejecuta y si escala bien.
```

---

## Para que sirve esta seccion

Esta seccion sirve para construir criterio de diagnostico y optimizacion.

Debe ayudar a responder preguntas como:

- Que problema de rendimiento hay.
- Como medirlo.
- Que recurso esta afectado.
- Que herramienta usar.
- Que solucion puede aplicar.
- Que trade-off trae.
- Como validar si mejoro.

El objetivo es que esta seccion sirva tanto para estudiar como para aplicar en proyectos reales.

Tambien debe servir como base para que una IA o agente razone asi:

```txt
Sintoma
→ posible causa
→ area afectada
→ herramienta de medicion
→ diagnostico
→ solucion candidata
→ trade-off
→ validacion
```

---

## Criterio principal

La optimizacion correcta no ataca lo que parece lento.

Ataca lo que fue medido como problema.

No deberia ser:

```txt
Tecnica avanzada
→ buscar donde aplicarla
```

Debe ser:

```txt
Problema real
→ medicion
→ diagnostico
→ solucion concreta
→ validacion
```

Optimizar sin medir es adivinar.

---

## Como usar esta seccion

Esta seccion debe usarse como sistema de diagnostico.

El flujo recomendado es:

```txt
1. Identificar sintoma.
2. Medir con herramientas.
3. Determinar posible bottleneck.
4. Asociar el problema a un recurso afectado.
5. Consultar la subcarpeta correspondiente.
6. Elegir una solucion candidata.
7. Evaluar trade-off.
8. Aplicar solo si corresponde.
9. Validar antes/despues.
```

No hace falta leer toda la seccion para cada problema.

Se consulta la parte que corresponde al diagnostico actual.

---

## Uso por agentes en Vaultrum

Cuando una IA trabaje en Modo Programador, Auditor o Arquitecto de conocimiento, debe usar esta seccion como apoyo de diagnostico.

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
- usar Object Pool porque hay objetos,
- usar Update Manager porque hay Updates,
- usar Addressables porque hay assets,
- reducir calidad visual sin diagnostico,
- agregar sistemas complejos sin trade-off claro,
- modificar arquitectura sin validar impacto,
- prometer mejoras sin definir como medirlas.

La IA debe recordar:

```txt
La optimizacion requiere evidencia o una hipotesis tecnica clara.
```

---

## Organizacion de la seccion

La seccion de Optimizacion se organiza en cuatro bloques principales.

```txt
03_Optimizacion/
├── Optimizacion.md
├── 01_Fundamentos/
├── 02_Problemas de rendimiento/
├── 03_Herramientas de deteccion/
└── 04_Metodologias y soluciones/
```

Esta organizacion sigue el flujo:

```txt
Fundamentos
→ problemas
→ herramientas
→ soluciones
```

---

## [[Fundamentos]]

Conceptos base para entender optimizacion antes de diagnosticar o proponer soluciones.

Esta subcarpeta sirve para entender el marco general:

```txt
presupuesto de frame
cuellos de botella
recursos afectados
game loop
medicion
criterio previo a la optimizacion
```

Usar esta carpeta cuando todavia haga falta entender que esta pasando antes de analizar un problema concreto.

---

## [[Problemas de rendimiento]]

Fichas de diagnostico sobre problemas concretos que pueden afectar el rendimiento.

Esta subcarpeta sirve para identificar sintomas, causas posibles, recursos afectados y formas de deteccion.

Usar esta carpeta cuando ya existe un sintoma o sospecha concreta, por ejemplo:

```txt
muchos Update activos
Instantiate y Destroy constantes
GC Alloc por frame
memory leaks
busquedas globales por frame
UI actualizada innecesariamente
pathfinding recalculado demasiado seguido
```

---

## [[Herramientas de deteccion]]

Herramientas para medir, observar y confirmar problemas de rendimiento.

Esta subcarpeta sirve para decidir que mirar y como interpretar los datos antes de aplicar una solucion.

Usar esta carpeta cuando haga falta validar una hipotesis con herramientas como:

```txt
Unity Profiler
CPU Usage
Timeline
GC Alloc
Memory Profiler
Frame Debugger
Stats
logs de diagnostico
comparacion antes y despues
```

---

## [[Metodologias y soluciones]]

Tecnicas, practicas y arquitecturas que ayudan a prevenir o resolver problemas de rendimiento.

Esta subcarpeta sirve para elegir una solucion candidata despues de medir y diagnosticar.

Usar esta carpeta cuando ya este claro el problema y haga falta evaluar alternativas como:

```txt
Update Manager
Object Pool
cacheo de referencias
clases puras
reducir frecuencia de actualizacion
UI orientada a eventos
Addressables
AssetManager
evitar allocations por frame
separar logica de Unity
```

---

## Guia rapida de diagnostico

Esta guia no decide automaticamente.

Solo orienta hacia que parte de la seccion conviene ir.

```txt
Necesito entender conceptos base
→ Fundamentos

Tengo un sintoma de rendimiento
→ Problemas de rendimiento

Necesito medir o confirmar una hipotesis
→ Herramientas de deteccion

Ya tengo un diagnostico y necesito evaluar una solucion
→ Metodologias y soluciones
```

Ejemplo de flujo correcto:

```txt
Caidas de FPS
→ Fundamentos para entender Frame Budget y Bottleneck
→ Problemas de rendimiento para identificar posibles causas
→ Herramientas de deteccion para medir
→ Metodologias y soluciones para elegir una respuesta
→ validacion antes/despues
```

---

## Criterio de uso

La optimizacion debe estar al servicio del juego.

No se optimiza para demostrar tecnica.

Se optimiza para sostener:

```txt
Estabilidad
Fluidez
Escalabilidad
Mantenibilidad
Experiencia del jugador
```

Una buena optimizacion deberia cumplir estas condiciones:

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

## Antes de proponer una optimizacion

Una IA debe responder estas preguntas antes de recomendar una solucion:

```txt
Cual es el sintoma?
Como se reproduce?
Que recurso podria estar afectado?
Que herramienta permite medirlo?
Que dato confirmaria el problema?
Que solucion candidata existe?
Que alternativa simple existe?
Que trade-off trae?
Que riesgo introduce?
Como se valida antes/despues?
```

Si no puede responder estas preguntas, no debe proponer la optimizacion todavia.

---

## Antes de ejecutar una optimizacion

Antes de ejecutar una optimizacion, la IA debe entregar:

```txt
Sintoma:
...

Medicion disponible o pendiente:
...

Diagnostico:
...

Solucion propuesta:
...

Sistema existente relacionado:
...

Archivos que podria tocar:
...

Archivos que no deberia tocar:
...

Trade-off:
...

Riesgos:
...

Validacion:
...

Decision requerida:
...
```

La ejecucion requiere aprobacion.

---

## Uso correcto dentro de Vaultrum

El uso correcto de esta seccion es:

```txt
Sintoma real
→ medicion o hipotesis
→ diagnostico
→ lectura puntual
→ solucion candidata
→ trade-off
→ validacion
```

No es:

```txt
Quiero optimizar
→ busco tecnica avanzada
→ la aplico
→ asumo que mejoro
```

Optimizacion debe ayudar a decidir.

No debe reemplazar el criterio.

---

## Regla final

La optimizacion no empieza tocando codigo.

Empieza entendiendo el problema.

```txt
Primero medir.
Despues diagnosticar.
Despues optimizar.
Despues validar.
```

Si no se puede explicar que recurso esta afectado, que herramienta lo muestra y que trade-off trae la solucion, todavia no hay una optimizacion clara.
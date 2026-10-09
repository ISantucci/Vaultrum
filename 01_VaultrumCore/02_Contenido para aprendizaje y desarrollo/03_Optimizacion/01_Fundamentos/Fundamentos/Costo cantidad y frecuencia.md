## Definicion

El costo real de una operacion en un videojuego no depende solamente de lo que cuesta esa operacion, sino de cuantas veces se ejecuta y cada cuanto.

La ecuacion conceptual es:

```txt
Costo real
=
costo unitario
×
cantidad
×
frecuencia
```

Donde:

```txt
Costo unitario
→ lo que tarda una sola ejecucion

Cantidad
→ sobre cuantas entidades se ejecuta

Frecuencia
→ cuantas veces por segundo ocurre
```

De ahi sale el criterio central de esta nota:

```txt
Ninguna operacion es cara o barata en abstracto.
Es cara o barata dentro de un contexto de uso.
```

La misma llamada puede ser irrelevante en un lugar y dominante en otro.

---

## Responsabilidad de esta nota

Esta nota no existe para prohibir APIs.

Esta nota no existe para armar listas de operaciones lentas.

Esta nota no existe para reemplazar la medicion.

Esta nota no existe para justificar optimizaciones sin evidencia.

Existe para dar una herramienta de estimacion previa: una forma de anticipar donde puede aparecer un costo antes de abrir el profiler.

Su responsabilidad es ayudar a responder:

```txt
¿Esto se ejecuta pocas veces o muchisimas?
¿Sobre cuantas entidades?
¿Cada cuanto?
```

---

## Que problema ayuda a entender

Ayuda a entender por que decir "esta funcion es lenta" casi nunca sirve.

Ejemplo:

```txt
1 raycast
→ practicamente irrelevante

5 raycasts × 500 NPC × 60 FPS
= 150.000 raycasts por segundo
```

Lo mismo pasa con lo que parece insignificante en el profiler:

```txt
Funcion de 0,01 ms
→ parece nada

0,01 ms × 10.000 llamadas
= 100 ms
```

Cien milisegundos son seis frames enteros a 60 FPS.

El mismo razonamiento aplica a memoria: 40 bytes por frame parecen nada, pero multiplicados por 60 FPS durante un minuto son basura temporal acumulada.

---

## Como funciona

Los tres factores se multiplican, no se suman: reducir cualquiera de los tres reduce el total.

```txt
Bajar costo unitario
→ hacer la operacion mas barata

Bajar cantidad
→ ejecutarla sobre menos entidades

Bajar frecuencia
→ ejecutarla menos veces por segundo
```

Y significa tambien que un solo factor puede arruinar el resultado: una operacion barata multiplicada por una cantidad enorme es un problema, y una operacion cara ejecutada una vez es irrelevante.

El resultado de esa multiplicacion no es una medicion.

Es una hipotesis con orden de magnitud: dice donde mirar, no que esta pasando.

Tambien conviene separar dos situaciones que suelen confundirse.

```txt
Ejecucion ocasional
→ inicializacion, carga, cambio de estado

Hot path
→ codigo ejecutado muy seguido, para muchas entidades
```

Una allocation durante la carga puede ser irrelevante; la misma allocation en un hot path puede dominar el frame.

---

## Como aplicarlo en videojuegos

Ejemplo inspirado en Tower Defense:

```txt
Cada torre busca su objetivo.
Cada busqueda recorre la lista de enemigos.
```

Estimacion:

```txt
30 torres
× 300 enemigos
× 60 FPS
= 540.000 comparaciones por segundo
```

La operacion individual es trivial. El total no lo es.

El mismo sistema, visto por sus tres factores:

```txt
Costo unitario
→ comparar distancias al cuadrado en vez de distancias

Cantidad
→ consultar solo enemigos dentro del rango de la torre

Frecuencia
→ reevaluar objetivo 10 veces por segundo, no 60
```

Otro caso del mismo juego, el HUD de dinero, vida y wave:

Estimacion:

```txt
3 textos
× 1 actualizacion por frame
× 60 FPS
= 180 actualizaciones por segundo
```

De las cuales casi ninguna corresponde a un cambio real de dato: la frecuencia esta mal elegida.

Y un tercero, los proyectiles:

```txt
1 Instantiate × 30 torres × 4 disparos por segundo
= 120 creaciones y destrucciones por segundo
```

Ahi la frecuencia justifica evaluar un pool.

Criterio consolidado en Capsule Survivor.

---

## Como guia el diagnostico

La ecuacion sirve para ordenar sospechas antes de medir y para leer el profiler despues.

Antes de medir:

```txt
¿Que sistemas escalan con la cantidad de entidades?
¿Cuales corren cada frame?
¿Cuales hacen las dos cosas?
```

Despues de medir, la ecuacion explica los numeros.

```txt
Total alto + costo unitario bajo
→ mirar cantidad de llamadas

Total alto + pocas llamadas
→ mirar costo unitario

Total que crece con la escena
→ mirar cantidad de entidades
```

Por eso la cantidad de llamadas es tan importante como el tiempo total: el total dice cuanto pesa y las llamadas dicen por que.

Flujo recomendado:

```txt
Sistema sospechado
→ estimar costo × cantidad × frecuencia
→ comparar contra el presupuesto del frame
→ medir
→ confirmar cual de los tres factores domina
→ atacar ese factor
```

---

## Cuando conviene consultarlo

Conviene aplicar esta ecuacion cuando:

```txt
El rendimiento cae al aumentar la cantidad de entidades.
Un sistema barato aparece alto en el profiler.
Hay que decidir si algo va en Update o no.
Hay que estimar el costo de una feature antes de implementarla.
Hay que priorizar entre varias optimizaciones.
```

Tambien conviene usarla cuando una IA propone una regla general.

```txt
"No uses GetComponent"
→ ¿donde?
→ ¿cuantas veces?
→ ¿sobre cuantos objetos?
```

Sin esos tres datos no se puede evaluar.

---

## Cuando NO conviene forzarlo

No conviene usar la estimacion como reemplazo de la medicion: una estimacion alta es motivo para medir, no para refactorizar.

Tampoco conviene aplicarla a codigo que se ejecuta una sola vez, como la carga inicial o el setup de escena.

Ahi los tres factores son minimos y el esfuerzo rinde poco.

Tampoco conviene inflar la estimacion con el peor caso imaginable.

Si el diseño del juego nunca llega a 10.000 enemigos, el calculo describe un juego que no existe.

La estimacion se hace sobre la escala real prevista.

---

## Errores que ayuda a evitar

Pensar en costo, cantidad y frecuencia ayuda a evitar:

- Declarar que una API es lenta sin contexto de uso.
- Optimizar una funcion barata que se llama tres veces.
- Ignorar una funcion trivial que se llama diez mil veces.
- Mirar solo el tiempo total y no la cantidad de llamadas.
- Suponer que lo que funciona con 10 entidades funciona con 500.
- Atacar el costo unitario cuando el problema era la frecuencia.
- Atacar la frecuencia cuando el problema era la cantidad.

La idea clave es:

```txt
No existe la operacion cara.
Existe la operacion cara en este contexto.
```

---

## Riesgos de interpretarlo mal

Un riesgo comun es usar la ecuacion como excusa para optimizar sin evidencia.

```txt
"Multiplique y da mucho"
→ sigue siendo una hipotesis
```

La estimacion orienta la medicion. No la sustituye.

Otro riesgo es estimar con numeros inventados.

Si el costo unitario nunca se midio, el resultado es una opinion con formato de calculo.

Otro riesgo es olvidar que reducir un factor puede aumentar otro.

Bajar de 60 a 10 evaluaciones por segundo acumula mas trabajo en cada ejecucion y puede concentrar el costo en un frame si todo se evalua junto.

Otro riesgo es aplicar la ecuacion solo a CPU. Vale igual para allocations, para queries fisicas, para actualizaciones de UI y para pixeles procesados.

---

## Hacia donde seguir

Esta nota pertenece a Fundamentos.

Si hace falta comparar contra el tiempo disponible:

```txt
→ Frame Budget
→ Frame time y estabilidad
```

Si hace falta ubicar el recurso limitante:

```txt
→ Bottleneck
```

Si la conclusion es que hay trabajo que directamente no deberia ejecutarse:

```txt
→ Reducir trabajo antes que acelerarlo
```

Si hace falta confirmar la estimacion midiendo:

→ [[Diagnostico]]

Si el costo domina en logica, IA o fisica:

→ [[CPU]]

Si domina en pixeles, shaders o transparencias:

→ [[GPU]]

Si el factor que se multiplica son allocations:

→ [[Memoria]]

Si aparece al cargar o instanciar contenido:

→ [[Carga e IO]]

Si aparece al actualizar la interfaz:

→ [[UI]]

Si hace falta un patron para reducir cantidad o frecuencia:

→ [[Patrones transversales]]

---

## Checklist de diagnostico

Antes de afirmar que algo es caro, revisar:

```txt
¿Cuanto cuesta una sola ejecucion?
¿Ese costo fue medido o supuesto?
¿Sobre cuantas entidades se ejecuta?
¿Cuantas veces por segundo?
¿Cual es el total estimado en ms por frame?
¿Como se compara contra el presupuesto del frame?
¿Ese total crece con la escala del juego?
¿Esta en un hot path o en codigo ocasional?
¿Cual de los tres factores domina?
¿La solucion propuesta ataca ese factor?
```

---

## Regla final

Antes de preguntar si una operacion es cara, hay que preguntar cuantas veces ocurre.

```txt
Costo unitario × cantidad × frecuencia.
Sin esos tres numeros, "es caro" no es un diagnostico.
```

## Definicion

El Frame Budget es el tiempo maximo disponible para completar un frame segun el objetivo de FPS del juego.

En videojuegos, cada frame debe procesar todo lo necesario para mostrar la siguiente imagen y mantener la experiencia fluida.

Esto puede incluir:

```txt
Input
Logica de gameplay
IA
Fisica
Animaciones
UI
Audio
Camara
Render
Postprocesado
Garbage Collector
Carga de datos
```

La idea principal es:

```txt
Frame Budget
→ presupuesto de tiempo por frame
```

Si el juego tarda mas que ese presupuesto, puede bajar de FPS o generar stuttering.

Formula:

```txt
1000 ms / FPS objetivo
```

Ejemplos:

```txt
30 FPS
→ 33.33 ms por frame

60 FPS
→ 16.66 ms por frame

120 FPS
→ 8.33 ms por frame
```

Esto significa que un juego a 60 FPS tiene aproximadamente 16.66 ms para completar todo el trabajo de un frame.

Si el frame tarda mas, el juego no puede sostener 60 FPS de forma estable.

---

## Responsabilidad de esta nota

Esta nota existe para explicar el presupuesto temporal de cada frame.

No existe para resolver todos los problemas de rendimiento.
No existe para elegir automaticamente una solucion.
No existe para reemplazar el uso de herramientas de medicion.

Su responsabilidad es ayudar a entender una pregunta base:

```txt
¿Cuanto tiempo tengo disponible por frame?
```

Desde ese criterio, despues se puede diagnosticar mejor:

```txt
Frame Budget
→ limite temporal

Bottleneck
→ parte que consume demasiado

Herramientas de deteccion
→ medicion real

Metodologias y soluciones
→ respuesta posible
```

---

## Que problema ayuda a entender

El Frame Budget ayuda a entender si el juego esta dentro del tiempo disponible para alcanzar el objetivo de rendimiento.

Sin este concepto, es facil pensar solamente en FPS.

Pero FPS es una consecuencia.

El dato importante para optimizacion es el tiempo de frame.

Ejemplo:

```txt
Objetivo:
60 FPS

Presupuesto:
16.66 ms por frame

Frame actual:
24 ms

Resultado:
el juego no llega al objetivo
```

El Frame Budget ayuda a responder preguntas como:

- Cuanto tiempo tengo por frame.
- Si el juego esta dentro del objetivo.
- Que sistemas consumen mas tiempo.
- Que parte del frame se pasa de presupuesto.
- Si un spike puntual rompe la fluidez.
- Que costo tiene ejecutar algo cada frame.
- Cuanto impacta multiplicar una operacion por muchos objetos.
- Por que algo barato puede volverse caro a gran escala.

La idea central es:

```txt
No se optimiza mirando solo si algo funciona.
Se optimiza mirando cuanto cuesta dentro del frame.
```

---

## Como funciona

Cada frame tiene un presupuesto de tiempo.

Ese presupuesto depende del objetivo de FPS.

```txt
Mas FPS
→ menos tiempo por frame

Menos FPS
→ mas tiempo por frame
```

Ejemplo:

```txt
30 FPS
→ cada frame puede tardar hasta 33.33 ms

60 FPS
→ cada frame puede tardar hasta 16.66 ms

120 FPS
→ cada frame puede tardar hasta 8.33 ms
```

El trabajo del frame se reparte entre muchos sistemas.

Ejemplo conceptual:

```txt
Frame de 16.66 ms

Input
→ 0.2 ms

Gameplay
→ 2 ms

IA
→ 3 ms

Fisica
→ 2 ms

UI
→ 1 ms

Render
→ 6 ms

Otros
→ 1 ms

Total
→ 15.2 ms
```

Ese frame entra dentro del presupuesto.

Pero si un sistema sube:

```txt
IA
→ 8 ms

Total
→ 20.2 ms
```

Entonces el frame ya no entra dentro de 16.66 ms.

El juego puede bajar de FPS o sentirse inestable.

---

## Costo, cantidad y frecuencia

Una operacion no se evalua solamente por su costo individual.

Hay que mirar:

```txt
Costo de la operacion
× cantidad de objetos
× frecuencia de ejecucion
```

Formula mental:

```txt
Costo total
=
costo
× cantidad
× frecuencia
```

Ejemplo:

```txt
Una busqueda simple
→ puede ser barata.

La misma busqueda
× 500 enemigos
× 60 veces por segundo
→ puede ser cara.
```

Otro ejemplo:

```txt
Actualizar una barra de vida
→ puede no importar.

Actualizar 300 barras de vida cada frame
aunque no hayan cambiado
→ puede volverse un problema.
```

Otro ejemplo:

```txt
Calcular pathfinding una vez
→ puede estar bien.

Calcular pathfinding cada frame para muchos NPCs
→ puede romper el Frame Budget.
```

La optimizacion suele atacar una de estas tres variables:

```txt
Reducir costo.
Reducir cantidad.
Reducir frecuencia.
```

Ejemplo:

```txt
Reducir costo
→ cachear referencias.

Reducir cantidad
→ actualizar solo objetos activos o cercanos.

Reducir frecuencia
→ recalcular IA cada 0.2 segundos en vez de cada frame.
```

---

## Como aplicarlo en videojuegos

El Frame Budget se aplica al analizar cuanto cuesta cada sistema dentro del juego.

Ejemplos:

```txt
Tower Defense
→ enemigos, torres, proyectiles, UI, oleadas y pathfinding compiten por tiempo de frame.

Juego de accion
→ input, animaciones, fisica, enemigos, camara y efectos visuales compiten por tiempo de frame.

Juego con muchos NPCs
→ percepcion, decision, movimiento y pathfinding pueden consumir CPU.

Juego con mucho render
→ luces, sombras, particulas, materiales y postprocesado pueden consumir GPU.
```

Ejemplo generico inspirado en un Tower Defense:

```txt
Frame:
torres buscan objetivos
enemigos se mueven
proyectiles avanzan
colisiones se procesan
UI muestra dinero/vida/wave
spawner evalua oleada
eventos se procesan
```

Cada sistema puede ser correcto por separado.

Pero juntos pueden superar el presupuesto.

Ejemplo:

```txt
Tower targeting
→ 2 ms

Enemy movement
→ 3 ms

Projectiles
→ 4 ms

UI
→ 1 ms

Physics
→ 3 ms

Render
→ 6 ms

Total
→ 19 ms
```

Para 60 FPS, 19 ms es demasiado.

El problema no es necesariamente un sistema roto.

Puede ser acumulacion.

```txt
Muchos costos pequeños
→ pueden formar un costo grande.
```

---

## Como guia el diagnostico

Frame Budget no dice automaticamente que solucion aplicar.

Sirve para orientar el diagnostico.

Si el frame supera el presupuesto, la siguiente pregunta no es:

```txt
¿Que tecnica de optimizacion uso?
```

La pregunta correcta es:

```txt
¿Que parte del frame esta consumiendo demasiado?
```

Flujo recomendado:

```txt
Frame time alto
→ revisar si supera el presupuesto
→ identificar si el limite parece CPU, GPU, memoria o GC
→ medir con herramientas
→ detectar el bottleneck real
→ recien despues evaluar soluciones
```

Ejemplo:

```txt
Sintoma:
El juego baja de FPS cuando hay muchos enemigos.

Frame Budget:
El objetivo es 60 FPS.
El presupuesto es 16.66 ms.
El frame esta tardando 24 ms.

Diagnostico pendiente:
Todavia no se sabe si el problema esta en IA, fisica, render, UI, GC o pathfinding.

Siguiente paso:
Medir antes de proponer una solucion.
```

---

## Cuando conviene consultarlo

Conviene consultar Frame Budget siempre que el juego tenga un objetivo de rendimiento.

Casos recomendados:

```txt
El juego baja FPS.
Hay stuttering.
Hay spikes.
Aparecen muchos enemigos.
Hay muchos proyectiles.
La UI crece en complejidad.
Se agregan efectos visuales pesados.
Se suma pathfinding o IA.
Se apunta a hardware limitado.
Se quiere sostener 60 FPS o mas.
```

Tambien conviene usarlo antes de decidir una optimizacion.

Ejemplo:

```txt
Problema:
El juego baja al tener 100 enemigos.

Antes de aplicar solucion:
medir cuanto tarda el frame
y que sistema se pasa de presupuesto.
```

---

## Cuando NO conviene forzarlo

No conviene usar el Frame Budget para microoptimizar todo desde el inicio.

Ejemplo:

```txt
Estoy prototipando una mecanica simple.
No hay problemas de rendimiento.
No hay escala real todavia.
```

En ese caso, conviene priorizar claridad y diseño.

El Frame Budget se vuelve mas importante cuando:

```txt
El sistema ya funciona.
El juego empieza a escalar.
Aparecen sintomas.
Hay objetivo de rendimiento.
Hay hardware objetivo.
```

Tampoco conviene tomar una medicion aislada como verdad absoluta.

Ejemplo:

```txt
Un frame dio 40 ms una sola vez.
```

Puede ser carga puntual, editor overhead, recompilacion, logging o algo no representativo.

Hay que medir en condiciones controladas.

---

## Errores que ayuda a evitar

Entender Frame Budget ayuda a evitar:

- Mirar solo FPS y no tiempo de frame.
- No entender por que 60 FPS exige mas que 30 FPS.
- Ejecutar logica costosa cada frame sin necesidad.
- Pensar que una operacion barata siempre es barata.
- Ignorar la escala.
- Ignorar la frecuencia.
- Optimizar sin saber cuanto tiempo hay disponible.
- Agregar sistemas que funcionan individualmente pero no escalan juntos.
- Diagnosticar stuttering como si fuera solo baja de FPS.
- No diferenciar promedio de spikes.

Tambien ayuda a pensar en acumulacion.

```txt
No siempre hay un unico gran problema.
A veces hay muchos sistemas chicos ejecutandose demasiado seguido.
```

---

## Riesgos de interpretarlo mal

El primer riesgo es usar Frame Budget para justificar optimizacion prematura.

Ejemplo:

```txt
Todavia no hay problema medido.
Pero se reescribe toda la arquitectura por miedo a pasarse de presupuesto.
```

Eso puede generar complejidad innecesaria.

Otro riesgo es mirar solo el promedio.

Ejemplo:

```txt
Frame promedio:
14 ms

Pero algunos frames:
60 ms
```

El promedio parece bueno, pero el jugador siente tirones.

Para fluidez, importan mucho los spikes.

Otro riesgo es no separar CPU y GPU.

Ejemplo:

```txt
El frame tarda mucho.
Se reducen scripts.
Pero el problema real estaba en render.
```

O al reves:

```txt
Se bajan poligonos.
Pero el problema real estaba en GC Alloc o Update.
```

Otro riesgo es medir en condiciones incorrectas.

Ejemplo:

```txt
Antes:
Editor con ventana Scene abierta.

Despues:
Build final.

Comparacion:
no equivalente.
```

La medicion debe hacerse con condiciones lo mas similares posible.

---

## Hacia donde seguir

Esta nota pertenece a Fundamentos.

Despues de entender Frame Budget, el siguiente paso depende del caso.

Si se quiere entender que parte limita el rendimiento:

```txt
→ [[Bottleneck]]
```

Si el problema parece venir de scripts, IA, fisica o logica:

```txt
→ [[CPU Bound]]
```

Si hace falta entender que se ejecuta cada frame:

```txt
→ [[Game loop]]
```

Si hay un sintoma concreto:

```txt
→ [[Problemas de rendimiento]]
```

Si hace falta medir:

```txt
→ [[Herramientas de deteccion]]
```

Si ya hay diagnostico y se necesita evaluar una respuesta:

```txt
→ [[Metodologias y soluciones]]
```

---

## Checklist de diagnostico

Antes de concluir que hay un problema de Frame Budget, revisar:

```txt
¿Hay un FPS objetivo?
¿Se calculo el presupuesto de frame?
¿Se midio frame time?
¿Se revisaron spikes?
¿Se identifico si el cuello esta en CPU o GPU?
¿Se midio en una escena representativa?
¿Se reprodujo el problema varias veces?
¿Se comparo antes/despues en condiciones similares?
¿Se reviso frecuencia de ejecucion?
¿Se reviso cantidad de objetos involucrados?
¿Se identifico que sistema consume mas tiempo?
```

---

## Regla final

El Frame Budget convierte la optimizacion en una pregunta concreta.

```txt
¿Cuanto tiempo tengo?
¿Cuanto estoy usando?
¿Que sistema se esta pasando?
¿Que puedo reducir?
```

La regla general es:

```txt
Todo lo que ocurre en un frame compite por el mismo presupuesto.
```

Por eso, optimizar no es solo hacer codigo mas rapido.

Es decidir que trabajo realmente necesita ocurrir, cuantas veces y en que momento.
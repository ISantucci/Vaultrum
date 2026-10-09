## Proposito

Esta rama reune los problemas y las soluciones del tiempo de CPU en un videojuego.

No existe para prohibir APIs.
No existe para declarar que Update, Instantiate o GetComponent son malos.
No existe para aplicar patrones porque hay muchos objetos.

Existe para atacar el costo de simular el mundo cuando el diagnostico confirmo que el limite esta en CPU.

---

## Idea central

En un videojuego la CPU se encarga sobre todo de preparar y simular el mundo:

```txt
gameplay
logica
input
IA
pathfinding
fisica
animaciones
UI
gestion de entidades
scripts
preparacion del rendering
carga y preparacion de datos
```

Y una parte importante de eso termina dependiendo del Main Thread. Tener un procesador de muchos nucleos no significa automaticamente que el codigo del juego se reparta entre ellos.

Casi todos los problemas de esta rama son la misma ecuacion vista desde distintos angulos:

```txt
costo unitario
x
cantidad
x
frecuencia
```

Un sistema que hace poco trabajo individual puede acumular un costo enorme si se ejecuta para muchas entidades y en todos los frames.

---

## Cuando usar esta rama

Usar CPU cuando el diagnostico confirme que el frame esta limitado por CPU:

```txt
el frame es caro y la escena es visualmente simple
bajar la resolucion no cambia el frame
CPU Usage muestra Scripts, Physics o AI dominando
el costo escala con la cantidad de entidades y no con lo que se ve
```

Si eso todavia no se midio, el camino es `Diagnostico`, no esta rama.

---

## Como debe usar esta rama una IA

Antes de proponer una solucion de CPU, una IA debe poder decir:

```txt
¿Que se ejecuta?
¿Cuantas veces por segundo?
¿Para cuantas entidades?
¿Tiene que ejecutarse?
¿Tiene que ejecutarse cada frame?
¿Tiene que ejecutarse para todos?
¿Necesita esa precision?
¿Tiene que ejecutarse ahora?
```

Recien cuando las respuestas obliguen a que si, tiene sentido preguntarse como hacerlo mas rapido.

Una IA no debe razonar asi:

```txt
Hay muchos Update.
→ Update Manager.
```

Debe razonar asi:

```txt
Hay muchos Update y el profiler muestra BehaviourUpdate caro.
→ ¿cuantos de esos Update hacen trabajo redundante?
→ ¿cuantos podrian bajar de frecuencia?
→ ¿cuantos podrian ser event-driven?
→ recien despues, centralizar el tick.
```

---

## Problemas incluidos

### [[Muchos update activos]]

Costo acumulado de callbacks por frame cuando se multiplican objetos y componentes.

Consultar cuando el costo crezca con la cantidad de entidades activas y no con lo que hace cada una.

### [[Busquedas globales por frame]]

Busquedas de objetos y componentes repetidas en caminos calientes en vez de resueltas una vez.

Consultar cuando el costo aparezca al crecer la cantidad de objetos de la escena.

### [[Instantiate y destroy constantes]]

Creacion y destruccion frecuente de entidades en runtime, con sus spikes asociados.

Consultar cuando la caida coincida con spawns, oleadas o disparos.

### [[Pathfinding recalculado demasiado seguido]]

El problema esta en la frecuencia del recalculo, no en el algoritmo elegido.

Consultar cuando haya muchos agentes navegando y el costo no baje al cambiar de algoritmo.

### [[Fisica costosa]]

Costo de la simulacion segun cantidad de cuerpos, colliders, contactos, queries, timestep y complejidad geometrica.

Consultar cuando FixedUpdate o Physics dominen el reparto del frame.

### [[IA que piensa de mas]]

Agentes que evaluan mas seguido, con mas precision o para mas casos de los que hacen falta.

Consultar cuando el costo escale con la cantidad de NPC y no con lo que el jugador percibe de ellos.

---

## Soluciones incluidas

### [[Update Manager como optimizacion]]

Centralizar el tick para controlar que se actualiza, cuando y con que prioridad.

Consultar cuando la cantidad de sistemas actualizandose justifique la centralizacion. No antes.

### [[Reducir frecuencia de actualizacion]]

Bajar cada cuanto se evalua algo cuando el jugador no puede percibir la diferencia.

Consultar cuando un sistema se evalue cada frame sin necesitarlo.

### [[Distribucion temporal del trabajo]]

Repartir en varios frames un trabajo que hoy se resuelve todo junto, para eliminar el spike sin reducir el total.

Consultar cuando el problema sea de picos y no de costo promedio.

### [[Cacheo de referencias]]

Resolver una vez y guardar, en vez de volver a buscar lo mismo.

Consultar cuando la misma busqueda se repita con frecuencia y el resultado sea estable.

### [[Particionado espacial]]

Dividir el espacio para que cada agente compare solo contra candidatos cercanos en vez de contra todos.

Consultar cuando el costo crezca de forma cercana a cuadratica con la cantidad de agentes.

---

## Rendering tambien cuesta CPU

Una parte del trabajo de rendering es de esta rama y no de GPU:

```txt
determinar que objetos participan
preparar informacion
materiales y estados
armar y enviar comandos
draw calls
```

Una cantidad enorme de draw calls puede producir principalmente presion sobre CPU. El desarrollo esta en la rama `04_GPU`, en la nota de draw calls y batching, porque ahi vive junto a lo que lo causa.

---

## Como se conecta con otras ramas

```txt
Diagnostico          confirma que el limite es CPU
Fundamentos          da la ecuacion y la jerarquia de reduccion
Memoria              las allocations y el recolector pegan en el frame de CPU
UI                   layout, rebuilds y raycasts de UI son costo de CPU
Patrones transversales  Early Exit, broad/narrow, Active Set, batch processing
```

---

## Criterio de uso

Antes de acelerar trabajo, agotar la jerarquia:

```txt
eliminar trabajo innecesario
→ reducir frecuencia
→ reducir cantidad de elementos
→ mejorar algoritmo
→ mejorar estructura de datos
→ reutilizar / cachear
→ paralelizar
→ microoptimizar
```

Optimizar una multiplicacion dentro de un loop importa mucho menos que cambiar como se eligen los elementos de ese loop.

---

## Regla final

En CPU casi nunca el problema es que algo sea lento.

Casi siempre es que se ejecuta demasiadas veces, para demasiadas cosas, sin necesitarlo.

```txt
¿Tiene que ejecutarse?
¿Cada frame?
¿Para todos?
Recien despues: ¿como lo hago mas rapido?
```

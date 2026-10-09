## Definicion

Una IA piensa de mas cuando ejecuta razonamiento que su estado actual no necesita, con una frecuencia que el gameplay no exige.

El costo rara vez esta en una formula. Esta en cuantos agentes razonan, cada cuanto y que tan caro es lo que corren.

Los sistemas de un agente cuestan cosas muy distintas:

```txt
FSM
LOS
Steering
Obstacle Avoidance
A*
Theta*
Decision Tree
Roulette Wheel
Flocking
```

Tratarlos como si costaran lo mismo es el origen del problema.

La idea central es:

```txt
Optimizar IA consiste sobre todo
en decidir cuando una inteligencia necesita pensar.
No en hacer sus algoritmos individuales mas rapidos.
```

---

## Responsabilidad de esta nota

Esta nota existe para diagnosticar exceso de razonamiento en agentes.

No existe para declarar que A* sea caro y deba evitarse.
No existe para reemplazar comportamiento por atajos.
No existe para fijar una cantidad correcta de sensores.
No existe para volver tontos a los NPC en nombre del frame.

Su responsabilidad es ayudar a responder:

```txt
¿Este agente necesita pensar esto, ahora, con esta frecuencia?
```

El foco no esta en que la IA piense menos.

El foco esta en entender:

```txt
que calcula cada agente y en que estado
cuantos lo calculan al mismo tiempo
cada cuanto lo recalculan
si el resultado anterior seguia valido
```

---

## Sintomas

Sintomas comunes:

```txt
Frame time que sube en proporcion a la cantidad de NPC.
Costo de scripts dominado por sistemas de IA.
Spikes al aparecer una oleada.
Costo alto con enemigos quietos o fuera de combate.
Caida al agrupar muchos agentes en la misma zona.
```

Un sintoma revelador:

```txt
Los enemigos no hacen nada visible
+
la IA igual cuesta
→
estan pensando sin necesidad.
```

---

## Que parte del software suele causarlo

Suele originarse en:

```txt
Percepcion con raycast sin filtros previos.
Reevaluacion de objetivo y de ruta cada frame.
Sensores de evasion con demasiados casts o demasiada frecuencia.
Flocking comparando cada agente contra todos.
Estados pasivos ejecutando la misma logica que los activos.
```

Ejemplo tipico:

```csharp
private void Update()
{
    target = FindNearestPlayer();
    path = Pathfinder.FindPath(transform.position, target.position);
    hasLineOfSight = Physics.Raycast(eyes.position, ToTarget(), range);
}
```

Tres decisiones caras, todas cada frame, para todos los agentes.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
CPU
Frame Budget
Main Thread
```

Tambien afecta al Garbage Collector si cada evaluacion genera listas o paths temporales.

Y buena parte del costo puede aparecer contabilizado en fisica:

```txt
percepcion y evasion
→ queries fisicas
→ costo dentro del bloque de Physics
```

---

## Como detectarlo

Se detecta separando el costo por sistema de IA, no por agente.

Buscar especialmente:

```txt
Tiempo consumido por percepcion, navegacion y evasion.
Cantidad de busquedas de camino y de queries fisicas por segundo.
Costo que escala con la cantidad de agentes.
```

Preguntas practicas:

```txt
¿Cuantos agentes estan razonando ahora mismo?
¿Un agente en Idle ejecuta lo mismo que uno en Attack?
¿Se filtro por distancia y angulo antes del raycast?
¿Cuantos A* se piden y cuantos hacian falta?
```

---

## Herramientas de deteccion

Herramientas utiles:

```txt
Unity Profiler
CPU Usage y Timeline
Physics Profiler
```

Que mirar:

```txt
Scripts de IA dentro del frame.
Picos coincidentes con spawns u oleadas.
Costo de percepcion y de navegacion por separado.
```

Logs utiles:

```txt
Cantidad de agentes activos por estado.
Cantidad de paths y de raycasts de vision por segundo.
```

---

## Soluciones posibles

Soluciones candidatas:

```txt
Cascada de filtros en percepcion.
Estados que activan solo los sistemas necesarios.
Reservar pathfinding para cuando hace falta.
Reducir frecuencia de decision y distribuirla entre frames.
Particionado espacial para busqueda de vecinos.
```

Percepcion en cascada de filtros:

```txt
Distancia
→ muy barata
→ si esta fuera de rango, return.

Angulo / FOV
→ barato
→ si esta fuera del campo de vision, return.

Raycast
→ caro
→ solo si sobrevivio a los filtros anteriores.
```

Caso caro:

```csharp
private bool CanSee(Transform target)
{
    return Physics.Raycast(eyes.position, ToTarget(target), range, mask);
}
```

Caso filtrado:

```csharp
private bool CanSee(Transform target)
{
    Vector3 toTarget = target.position - eyes.position;

    if (toTarget.sqrMagnitude > sqrRange)
    {
        return false;
    }

    if (Vector3.Angle(eyes.forward, toTarget) > halfFov)
    {
        return false;
    }

    return Physics.Raycast(eyes.position, toTarget, range, mask);
}
```

La FSM tambien funciona como herramienta indirecta de optimizacion:

```txt
Idle
→ percepcion espaciada, sin pathfinding ni evasion.
Patrol
→ navegacion y percepcion moderada.
Attack
→ percepcion frecuente, evasion, apuntado.
```

Un NPC en Idle no necesita correr los mismos calculos que en Attack.

Pathfinding, reservando el algoritmo caro:

```txt
¿Hay camino directo?
│
├── Si → steering / movimiento directo
│
└── No → A*
```

La idea no es usar un raycast antes de A*, sino reservar el algoritmo costoso para los casos donde realmente hace falta.

Flocking:

```txt
Separation, Cohesion y Alignment
no son el problema de escala.
El problema esta en la busqueda de vecinos.
```

La pregunta cambia:

```txt
¿Cuales son todos los boids?
→
¿Cuales son los boids cercanos que pueden afectarme?
```

Obstacle Avoidance:

```txt
Los sensores fisicos tienen costo
y van a la minima frecuencia y cantidad
compatible con el comportamiento buscado.
```

El aprendizaje no es que tres SphereCasts sea el numero correcto.

Criterio consolidado en Capsule Survivor, sobre sus sistemas de percepcion, navegacion y evasion.

---

## Trade-offs

Cada solucion intercambia algo.

```txt
Cascada de filtros
→ menos raycasts
→ mas ramas que mantener ordenadas.

Menos frecuencia de decision
→ menos CPU
→ NPC que reacciona mas tarde.

Reservar A*
→ menos busquedas
→ rutas peores si el chequeo directo se equivoca.
```

Siempre el mismo intercambio:

```txt
precision de comportamiento ↔ CPU
```

---

## Ejemplo en videojuegos

En un Tower Defense:

```txt
300 enemigos en oleada, 30 torres eligiendo objetivo
y agrupamientos que esquivan obstaculos sin encimarse.
```

Version que piensa de mas:

```txt
Cada enemigo recalcula ruta y lanza raycasts sin filtrar.
Cada torre recorre la lista completa de enemigos cada frame.
Cada enemigo se compara contra los otros 299.
```

Version medida:

```txt
Ruta recalculada solo si cambio el objetivo o el terreno.
Vision filtrada por distancia y angulo antes del raycast.
Torres y separacion resueltas contra vecinos cercanos.
```

El comportamiento visible es casi el mismo. El costo no.

---

## Como guia el diagnostico

Flujo recomendado:

```txt
Sintoma:
el frame crece con la cantidad de NPC.

Sospecha:
los agentes razonan de mas.

Medicion:
costo por sistema de IA en CPU Usage y Timeline.

Dato esperado:
percepcion, pathfinding o vecindad dominando.

Solucion candidata:
filtrar, espaciar, distribuir o particionar.
```

La pregunta clave es:

```txt
¿Este calculo cambia el comportamiento visible del agente ahora?
```

---

## Errores comunes al intentar solucionarlo

Errores comunes:

```txt
Bajar la frecuencia de decision hasta que el enemigo se siente tonto.
Sacar el pathfinding y dejar agentes trabados contra las paredes.
Copiar cantidades de casts de otro proyecto sin medir.
Optimizar las formulas de steering en vez de la busqueda de vecinos.
Apagar sistemas y no volver a encenderlos.
```

Ejemplo de mala solucion:

```txt
Problema:
IA cara.

Solucion:
decision cada 2 segundos para todos.

Resultado:
frame estable, enemigos que reaccionan tarde.
```

Una IA barata que no se siente inteligente es un problema de diseño, no una optimizacion.

---

## Hacia donde seguir

Si todavia no se midio que sistema domina:

→ [[Diagnostico]]

Si hace falta entender el presupuesto que la IA gasta:

→ [[Fundamentos]]

Si el patron util es filtrar barato antes de calcular caro:

→ [[Patrones transversales]]

Notas relacionadas dentro de esta rama:

```txt
Particionado espacial
Distribucion temporal del trabajo
Pathfinding recalculado demasiado seguido
Fisica costosa
```

---

## Checklist de diagnostico

```txt
¿Se midio que sistema de IA domina el frame?
¿Cuantos agentes razonan al mismo tiempo?
¿Los estados pasivos ejecutan menos trabajo que los activos?
¿La percepcion filtra por distancia y angulo antes del raycast?
¿Hay return temprano en cada escalon?
¿Se pide A* cuando alcanzaba con movimiento directo?
¿Se recalcula ruta sin que haya cambiado nada?
¿La busqueda de vecinos recorre a todos?
¿Cuantos sensores tiene cada agente y con que frecuencia?
¿Se valido el comportamiento despues del cambio?
```

---

## Regla final

La IA no se optimiza haciendo que piense mas rapido.

```txt
Se optimiza decidiendo
quien piensa, que piensa
y cada cuanto le hace falta pensarlo.
```

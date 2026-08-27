## Definicion

Pathfinding recalculado demasiado seguido ocurre cuando un sistema calcula rutas mas veces de las necesarias.

El pathfinding puede ser costoso porque suele involucrar nodos, grafos, grillas, costos, heuristicas, vecinos y evaluacion de caminos posibles.

La idea principal es:

```txt
Calcular rutas
× muchos agentes
× demasiada frecuencia
=
alto costo de CPU
```

No todo recalculo de pathfinding es un problema.

El problema aparece cuando se recalculan rutas sin que haya cambiado algo relevante.

---

## Responsabilidad de esta nota

Esta nota existe para diagnosticar problemas causados por recalculo excesivo de rutas.

No existe para explicar todos los algoritmos de pathfinding.
No existe para decidir automaticamente entre A*, Dijkstra u otro algoritmo.
No existe para reemplazar la medicion.

Su responsabilidad es ayudar a responder:

```txt
¿Estoy recalculando caminos mas veces de las necesarias?
```

El foco esta en frecuencia, escala y necesidad real del recalculo.

---

## Sintomas

Sintomas comunes:

```txt
CPU Usage alto.
Spikes cuando se mueven muchos agentes.
Caidas al aparecer enemigos.
Frame time alto en sistemas de IA.
Tirones al cambiar objetivos.
Costo creciente con cantidad de NPCs.
Mucho tiempo en logica de pathfinding.
```

Tambien puede verse asi:

```txt
Pocos agentes
→ funciona bien.

Muchos agentes
→ el juego cae.
```

O:

```txt
Cada enemigo recalcula ruta constantemente aunque el camino no cambio.
```

---

## Que parte del software suele causarlo

Suele aparecer en:

```txt
IA de enemigos.
NPCs.
Unidades con movimiento autonomo.
Juegos con grillas.
Tower Defense.
RTS.
Sistemas de persecucion.
Sistemas de navegacion.
Simulaciones con muchos agentes.
```

Ejemplo problematico:

```csharp
private void Update()
{
    currentPath = pathfinder.CalculatePath(transform.position, target.position);
}
```

Si esto ocurre cada frame por muchos agentes, puede saturar CPU.

Otro ejemplo:

```txt
Cada enemigo recalcula ruta al mismo destino aunque todos usan un camino similar.
```

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
CPU
Game Loop
Frame Budget
```

Puede afectar tambien:

```txt
Memoria
Garbage Collector
```

si cada calculo crea listas, nodos temporales, diccionarios o estructuras nuevas.

---

## Como detectarlo

Se detecta revisando frecuencia de recalculo y costo de IA.

Buscar especialmente:

```txt
Pathfinding en Update.
Recalculo por cada agente.
Recalculo aunque destino no cambie.
Recalculo aunque mapa no cambie.
Listas temporales creadas por calculo.
Spikes al pedir muchas rutas juntas.
Costo alto al aumentar NPCs.
```

Preguntas practicas:

```txt
¿Cuando se recalcula la ruta?
¿Que evento dispara el recalculo?
¿Cambio el destino?
¿Cambio el mapa?
¿Cambio el costo de nodos?
¿Todos los agentes necesitan ruta propia?
¿Puede compartirse ruta?
¿Puede escalonarse el recalculo?
```

---

## Herramientas de deteccion

Herramientas utiles:

```txt
Unity Profiler
CPU Usage
Timeline
GC Alloc
Logs de diagnostico
```

Que mirar:

```txt
Tiempo de calculo de pathfinding.
Cantidad de rutas calculadas por segundo.
Costo por agente.
Allocations durante calculo.
Spikes al recalcular muchas rutas.
```

Logs utiles:

```txt
Cantidad de solicitudes de pathfinding.
Agente que pide ruta.
Motivo del recalculo.
Tiempo de calculo.
Cantidad de nodos evaluados.
```

---

## Soluciones posibles

Soluciones candidatas:

```txt
Recalcular solo cuando cambia el destino.
Recalcular solo cuando cambia el mapa.
Reducir frecuencia de recalculo.
Escalonar calculos entre frames.
Cachear rutas.
Compartir rutas cuando corresponda.
Usar waypoints o caminos precomputados.
Usar costos actualizables en vez de recalcular todo sin necesidad.
Limitar cantidad de agentes recalculando por frame.
Evitar allocations dentro del algoritmo.
```

Ejemplo:

```txt
Antes:
Cada enemigo recalcula ruta cada frame.

Despues:
El enemigo recalcula solo cuando cambia su destino o cuando se desbloquea una nueva ruta.
```

Otro ejemplo:

```txt
Antes:
300 enemigos piden ruta el mismo frame.

Despues:
Las solicitudes se distribuyen en varios frames.
```

---

## Trade-offs

Optimizar pathfinding requiere cuidado porque afecta comportamiento.

```txt
Reducir frecuencia
→ menos costo
→ agentes pueden reaccionar mas lento.

Cachear rutas
→ menos recalculo
→ riesgo de usar rutas viejas.

Compartir rutas
→ menos costo
→ menos individualidad de agentes.

Escalonar calculos
→ evita spikes
→ puede introducir delay.

Precomputar caminos
→ reduce runtime
→ menos flexibilidad ante cambios dinamicos.

Evitar allocations
→ menos GC
→ codigo mas cuidadoso.
```

No se debe reducir costo a costa de romper la navegacion del agente.

La respuesta debe sostener gameplay.

---

## Ejemplo en videojuegos

En un Tower Defense:

```txt
Enemigos entran al mapa.
Deben llegar a la base.
El camino puede estar definido por nodos, grilla o waypoints.
Algunos caminos pueden desbloquearse por ronda.
```

Mala estrategia:

```txt
Cada enemigo recalcula el mejor camino cada frame.
```

Estrategia mas sana:

```txt
El grafo calcula ruta cuando:
- inicia la oleada,
- cambia el mapa,
- se desbloquea un camino,
- cambia el destino,
- aparece una condicion relevante.
```

Otra estrategia:

```txt
Los enemigos de la misma oleada comparten ruta base.
Cada enemigo solo ejecuta movimiento sobre esa ruta.
```

En un sistema con Dijkstra o A*:

```txt
El algoritmo puede ser correcto.
Pero si se ejecuta demasiado seguido,
se vuelve caro igual.
```

---

## Como guia el diagnostico

Esta nota guia el diagnostico cuando el costo parece venir de IA o navegacion.

Flujo recomendado:

```txt
Sintoma:
CPU alto con muchos agentes.

Sospecha:
pathfinding recalculado demasiado seguido.

Medicion:
Profiler / CPU Usage / Timeline / logs.

Dato esperado:
muchas rutas calculadas por segundo o spikes de pathfinding.

Problema confirmado:
recalculo innecesario o demasiado frecuente.

Solucion candidata:
reducir frecuencia, cachear, compartir o escalonar calculos.
```

La pregunta clave es:

```txt
¿Cambio algo que justifique recalcular la ruta?
```

---

## Errores comunes al intentar solucionarlo

Errores comunes:

```txt
Recalcular en Update por costumbre.
Recalcular para todos los agentes al mismo tiempo.
No registrar por que se pidio una ruta.
Cachear rutas sin invalidarlas.
Reducir frecuencia y romper reaccion de IA.
Cambiar de algoritmo sin medir frecuencia.
Pensar que A* o Dijkstra resuelven el problema por si solos.
Crear listas temporales en cada calculo.
No diferenciar movimiento de calculo de ruta.
```

Ejemplo de mala solucion:

```txt
Problema:
El pathfinding cuesta demasiado.

Decision:
Cambiar Dijkstra por A*.

Pero:
se sigue calculando cada frame para todos los enemigos.

Resultado:
el problema de frecuencia sigue.
```

Antes de cambiar algoritmo, hay que revisar frecuencia y necesidad.

---

## Hacia donde seguir

Si hace falta entender CPU:

```txt
→ CPU Bound
```

Si hace falta entender frecuencia:

```txt
→ Game loop
```

Si hace falta medir:

```txt
→ Unity Profiler
→ CPU Usage
→ Timeline
→ GC Alloc
```

Si el problema viene de allocations:

```txt
→ GC Alloc por frame
→ Evitar allocations por frame
```

Si el problema es frecuencia:

```txt
→ Reducir frecuencia de actualizacion
→ Update Manager como optimizacion
```

Si el problema es arquitectura de Unity:

```txt
→ MonoBehaviour como puente
→ Separar logica de Unity
```

---

## Checklist de diagnostico

```txt
¿El pathfinding se recalcula en Update?
¿Cuantos agentes recalculan rutas?
¿Cuantas rutas se calculan por segundo?
¿Cambio el destino?
¿Cambio el mapa?
¿Cambio el costo de nodos?
¿La ruta podria cachearse?
¿Las rutas podrian compartirse?
¿Los calculos pueden escalonarse?
¿Hay allocations por calculo?
¿Se midio CPU Usage?
¿Se reviso Timeline?
¿La solucion mantiene buen comportamiento de IA?
```

---

## Regla final

El problema no siempre es el algoritmo.

Muchas veces es la frecuencia.

```txt
Un buen pathfinding mal programado
puede ser caro si se recalcula sin necesidad.
```
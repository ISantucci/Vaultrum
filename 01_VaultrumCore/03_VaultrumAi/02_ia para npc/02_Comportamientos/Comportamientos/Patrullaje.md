## Definicion

Patrullaje es un comportamiento en el que un NPC recorre una ruta, zona o conjunto de puntos definidos.

Se usa para simular vigilancia, rutina, control territorial o movimiento repetitivo.

```txt
Patrullaje
→ recorrer puntos o zonas
→ mantener actividad
→ controlar un espacio
```

Un NPC que patrulla no necesariamente esta buscando al jugador.

Puede estar cumpliendo una rutina.

---

## Responsabilidad

La responsabilidad del patrullaje es guiar al NPC por un recorrido definido.

Debe responder:

```txt
¿A que punto voy ahora?
¿Cual es el siguiente punto?
¿Debo esperar al llegar?
¿Debo repetir la ruta?
¿Debo elegir puntos en orden o al azar?
¿Debo volver a patrullar despues de una interrupcion?
```

Patrullaje puede consumir un sistema de movimiento.

No debe decidir todo el comportamiento del NPC.

---

## Que NO debe hacer

Patrullaje no debe absorber:

```txt
deteccion del jugador
decision completa de estados
ataque
huida
calculo interno de pathfinding avanzado
animacion completa
sistema de alerta global
```

Ejemplo incorrecto:

```txt
PatrolBehaviour
→ patrulla
→ detecta jugador
→ decide perseguir
→ calcula ruta
→ ataca
```

Ejemplo correcto:

```txt
PatrolBehaviour
→ solicita moverse al siguiente punto.

Sistema de decision
→ decide si dejar de patrullar.

Sistema de movimiento
→ ejecuta desplazamiento.
```

Regla:

```txt
Patrullaje define recorrido.
No define toda la IA del NPC.
```

---

## Que problema resuelve

Patrullaje ayuda a que un NPC no quede estatico y a que el espacio tenga actividad.

Puede resolver:

```txt
guardias que vigilan zonas
enemigos que recorren pasillos
animales que se mueven por territorio
civiles con rutinas simples
camaras que rotan o recorren puntos
patrones de movimiento predecibles
```

Tambien puede ayudar al diseño de nivel.

Ejemplo:

```txt
Un guardia patrulla un pasillo.
El jugador observa el patron.
Luego decide cuando pasar.
```

El patrullaje puede crear lectura, tension y oportunidad.

---

## Datos que necesita

Patrullaje puede necesitar:

```txt
lista de puntos
indice del punto actual
velocidad
tiempo de espera
modo de recorrido
distancia minima para llegar
referencia al sistema de movimiento
condiciones de interrupcion
condiciones de retorno
```

Modos posibles:

```txt
ida y vuelta
circular
aleatorio
por zonas
por prioridad
por rutina horaria
```

No todos los patrullajes necesitan pathfinding.

Si los puntos estan en una ruta clara, puede alcanzar con movimiento directo o waypoints simples.

---

## Que produce

Patrullaje puede producir:

```txt
punto objetivo actual
solicitud de movimiento
evento de llegada a punto
evento de cambio de punto
estado de espera
fin de ruta
```

Ejemplo:

```txt
CurrentWaypoint = Punto 3
IsWaiting = false
```

Eso no significa que el NPC decida perseguir o atacar.

Solo significa que el patrullaje esta indicando su objetivo de recorrido.

---

## Como funciona

Un patrullaje simple puede seguir este flujo:

```txt
1. Elegir punto inicial.
2. Moverse hacia ese punto.
3. Detectar llegada.
4. Esperar si corresponde.
5. Elegir siguiente punto.
6. Repetir.
```

Ejemplo conceptual:

```csharp
using System.Collections.Generic;
using UnityEngine;

public class PatrolRoute
{
    private readonly IReadOnlyList<Transform> points;
    private int currentIndex;

    public PatrolRoute(IReadOnlyList<Transform> points)
    {
        this.points = points;
        currentIndex = 0;
    }

    public bool HasPoints => points != null && points.Count > 0;

    public Transform CurrentPoint => HasPoints ? points[currentIndex] : null;

    public void Advance()
    {
        if (!HasPoints)
        {
            return;
        }

        currentIndex = (currentIndex + 1) % points.Count;
    }
}
```

Este objeto solo administra la ruta.

No mueve, no detecta y no ataca.

---

## Como aplicarlo en videojuegos

Patrullaje conviene cuando el movimiento repetitivo aporta al gameplay o al mundo.

Ejemplos:

```txt
guardia en juego de sigilo
enemigo que protege una zona
NPC civil con rutina
animal que recorre territorio
boss con fases de reposicionamiento
```

El patrullaje puede ser:

```txt
predecible
semi-aleatorio
dependiente de eventos
interrumpible
reiniciable
```

Ejemplo:

```txt
Guardia
→ patrulla 4 puntos
→ espera 2 segundos en cada punto
→ si detecta al jugador, deja de patrullar
→ si pierde al jugador, vuelve al punto mas cercano
```

---

## Cuando conviene implementarlo

Conviene implementar patrullaje cuando:

```txt
el NPC debe cubrir una zona
el jugador debe leer un patron
el mapa necesita vida
el enemigo no debe estar quieto
la vigilancia importa
el diseño del nivel tiene rutas
el jugador puede planificar alrededor del movimiento
```

Pregunta clave:

```txt
¿El recorrido del NPC cambia la experiencia del jugador?
```

Si la respuesta es si, patrullaje puede aportar valor.

---

## Cuando NO conviene implementarlo

No conviene usar patrullaje si:

```txt
el NPC debe quedarse fijo
el movimiento no aporta nada
el jugador no puede leer ni usar el patron
el enemigo solo aparece para atacar
la ruta complica el diseño sin beneficio
un trigger simple alcanza
```

Ejemplos:

```txt
comerciante estatico
NPC de dialogo
torreta fija
enemigo que aparece en arena cerrada y ataca directamente
```

Regla:

```txt
No mover un NPC solo para que parezca mas vivo si eso no aporta al juego.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
mezclar patrullaje con deteccion
mezclar patrullaje con ataque
hacer que la ruta decida estados
no validar que existan puntos
no definir que pasa al interrumpir
no definir como vuelve al patrullaje
usar pathfinding complejo donde alcanzan waypoints
```

Ejemplo de mala practica:

```txt
PatrolBehaviour detecta jugador y llama a Chase().
```

Problema:

```txt
El patrullaje deja de ser una rutina.
Empieza a actuar como sistema de decision.
```

---

## Costos de implementacion

Patrullaje puede requerir:

```txt
waypoints
rutas
tiempos de espera
logica de siguiente punto
integracion con movimiento
debug visual de ruta
configuracion por NPC
condiciones de interrupcion
condiciones de retorno
```

Puede ser simple o complejo segun el diseño.

Ejemplo simple:

```txt
lista fija de puntos
→ bajo costo
```

Ejemplo avanzado:

```txt
rutas dinamicas, interrupciones, retorno, prioridad de zonas
→ costo mayor
```

---

## Costos de optimizacion

Patrullaje suele ser barato, pero puede encarecerse si:

```txt
muchos NPCs recalculan rutas constantemente
cada punto busca referencias globales
se actualizan rutas cada frame sin cambios
se usan chequeos de llegada costosos
se dibujan gizmos en runtime
```

Alternativas:

```txt
rutas predefinidas
cache de puntos
actualizacion simple por distancia
pathfinding solo cuando haga falta
debug solo en editor
```

---

## Criterio de optimizacion

Antes de optimizar patrullaje, revisar:

```txt
cantidad de NPCs patrullando
cantidad de puntos por ruta
frecuencia de chequeo de llegada
si se usa pathfinding
si hay recalculo de ruta
si el NPC esta activo o visible
```

Criterio:

```txt
patrullaje por waypoints
→ normalmente barato.

patrullaje con pathfinding dinamico constante
→ puede ser caro.
```

---

## Validacion

Patrullaje se valida observando:

```txt
si el NPC llega a cada punto
si respeta el orden esperado
si espera donde corresponde
si no se traba
si vuelve a patrullar cuando debe
si se interrumpe correctamente
si el recorrido se entiende desde gameplay
```

Debug util:

```txt
gizmos de puntos
lineas entre puntos
indice actual visible
logs temporales al cambiar de punto
```

---

## Preguntas antes de implementarlo

Antes de implementar patrullaje, preguntar:

```txt
¿El NPC necesita moverse por una ruta?
¿El recorrido aporta gameplay o mundo?
¿Hay puntos definidos?
¿El orden de puntos esta claro?
¿Debe esperar en cada punto?
¿Debe repetirse?
¿Debe ser interrumpible?
¿Como vuelve al patrullaje?
¿Necesita pathfinding o alcanza con waypoints?
¿Se puede validar con gizmos?
```

---

## Errores comunes

Errores comunes:

```txt
no validar que haya puntos
hacer que el NPC quede atrapado en un punto
mezclar patrullaje con deteccion
mezclar patrullaje con ataque
no separar ruta de movimiento
no definir que pasa al interrumpir
no definir como volver al patrullaje
hacer rutas imposibles para el mapa
usar pathfinding complejo cuando alcanza con waypoints
```

---

## Criterio para una IA

Cuando una IA trabaje con patrullaje debe:

```txt
mantenerlo como comportamiento de recorrido
no convertirlo en sistema completo de decision
no duplicar deteccion ni ataque
separar ruta, movimiento e interrupciones
explicar datos necesarios
explicar condiciones de entrada y salida
indicar cuando conviene y cuando no
considerar si pathfinding realmente hace falta
proponer validacion visual
respetar navegacion waterfall
```

Regla operativa:

```txt
Patrullaje es una rutina de movimiento.
La decision externa define cuando se usa o se abandona.
```

---

## Checklist

Antes de implementar patrullaje, revisar:

```txt
¿El NPC necesita moverse por una ruta?
¿El recorrido aporta gameplay o mundo?
¿Hay puntos definidos?
¿El orden de puntos esta claro?
¿Debe esperar en cada punto?
¿Debe repetirse?
¿Debe ser interrumpible?
¿Como vuelve al patrullaje?
¿Necesita pathfinding o alcanza con waypoints?
¿Se puede validar con gizmos?
```

---

## Regla final

```txt
Patrullar no es pensar.

Patrullar es cumplir una rutina hasta que otra decision indique cambiarla.
```
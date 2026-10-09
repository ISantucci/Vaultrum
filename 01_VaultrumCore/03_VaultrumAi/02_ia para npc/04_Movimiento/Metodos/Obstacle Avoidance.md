## Definición

**Obstacle Avoidance** es una técnica de movimiento que permite que un NPC evite obstáculos cercanos mientras se desplaza.

Su objetivo es ajustar la trayectoria local para no chocar, trabarse o atravesar elementos del entorno.

```txt
Obstacle Avoidance
→ detecta obstáculo cercano
→ corrige dirección
→ evita colisión local
```

No es lo mismo que pathfinding.

Pathfinding puede calcular una ruta global.

Obstacle Avoidance resuelve ajustes locales durante el movimiento.

---

## Responsabilidad

La responsabilidad de Obstacle Avoidance es corregir el movimiento cuando aparece un obstáculo cercano.

Debe responder:

```txt
¿Hay un obstáculo local que deba evitar?
¿Cómo ajusto la dirección actual para no chocarlo?
¿Qué dirección alternativa permite seguir moviéndose?
```

Su salida puede ser:

```txt
dirección corregida
fuerza de evasión
velocidad ajustada
obstáculo detectado
distancia al obstáculo
```

Obstacle Avoidance no decide el objetivo del NPC.

Solo modifica cómo se mueve para evitar una colisión local.

---

## Qué NO debe hacer

Obstacle Avoidance no debe:

```txt
decidir comportamiento
elegir objetivo
detectar jugador como lógica principal
calcular toda la ruta global
reemplazar pathfinding
cambiar estados completos
resolver combate
aplicar daño
```

Ejemplo incorrecto:

```txt
ObstacleAvoidance
→ detecta obstáculo
→ decide perseguir
→ calcula ruta completa
→ mueve
→ ataca
```

Ejemplo correcto:

```txt
Movimiento
→ intenta avanzar.

Obstacle Avoidance
→ detecta obstáculo local.

Movimiento
→ ajusta dirección.
```

Regla:

```txt
Obstacle Avoidance corrige movimiento local.

No decide la IA.
```

---

## Qué problema resuelve

Obstacle Avoidance ayuda a evitar que los NPCs:

```txt
choquen contra paredes
se traben con objetos
intenten atravesar obstáculos
vibren contra esquinas simples
se amontonen en espacios reducidos
se muevan de forma torpe frente a obstáculos cercanos
```

Puede aportar valor en juegos con:

```txt
obstáculos dinámicos
varios agentes
espacios estrechos
movimiento libre
enemigos que rodean al jugador
objetos que pueden bloquear parcialmente el camino
```

---

## Datos que necesita

Obstacle Avoidance puede necesitar:

```txt
posición del NPC
dirección actual
velocidad actual
distancia de detección
radio del agente
layers de obstáculos
sensores frontales
fuerza de evasión
direcciones alternativas
```

Opcionalmente puede usar:

```txt
raycasts
spherecasts
colliders
predicción de posición
vecinos cercanos
debug visual
```

La técnica elegida depende del tipo de juego, la cantidad de NPCs y el nivel de precisión necesario.

---

## Qué produce

Obstacle Avoidance puede producir una corrección local del movimiento.

Ejemplos:

```txt
ObstacleDetected = true
AvoidanceDirection = derecha
CorrectedDirection = dirección ajustada
```

Eso no significa que el NPC haya cambiado de decisión.

Solo significa que su movimiento necesita ajustarse para evitar un choque.

---

## Cómo funciona

Una versión simple puede usar sensores frontales.

Flujo general:

```txt
1. Revisar la dirección deseada de movimiento.
2. Detectar si hay un obstáculo cercano.
3. Si no hay obstáculo, mantener la dirección.
4. Si hay obstáculo, buscar una dirección alternativa.
5. Devolver una dirección corregida.
```

Ejemplo conceptual:

```csharp
using UnityEngine;

public class SimpleObstacleAvoidance
{
    private readonly Transform owner;
    private readonly float detectionDistance;
    private readonly LayerMask obstacleMask;

    public SimpleObstacleAvoidance(
        Transform owner,
        float detectionDistance,
        LayerMask obstacleMask)
    {
        this.owner = owner;
        this.detectionDistance = detectionDistance;
        this.obstacleMask = obstacleMask;
    }

    public Vector3 GetDirection(Vector3 desiredDirection)
    {
        if (!Physics.Raycast(owner.position, desiredDirection, detectionDistance, obstacleMask))
        {
            return desiredDirection;
        }

        Vector3 right = owner.right;

        if (!Physics.Raycast(owner.position, right, detectionDistance, obstacleMask))
        {
            return right;
        }

        Vector3 left = -owner.right;

        if (!Physics.Raycast(owner.position, left, detectionDistance, obstacleMask))
        {
            return left;
        }

        return Vector3.zero;
    }
}
```

Este ejemplo corrige una dirección local.

No calcula una ruta completa.

No decide comportamiento.

No mueve por sí mismo.

---

## Relación con Steering Behaviours

Obstacle Avoidance puede funcionar como un steering behaviour o como una corrección adicional del movimiento.

En ambos casos, su responsabilidad sigue siendo local.

```txt
Steering
→ calcula una dirección deseada.

Obstacle Avoidance
→ corrige esa dirección si hay obstáculo cercano.

Movimiento
→ ejecuta el desplazamiento.
```

No todo steering necesita obstacle avoidance.

No todo obstacle avoidance necesita un sistema completo de steering.

La solución debe responder al problema real del movimiento.

---

## Relación con pathfinding

Obstacle Avoidance y pathfinding pueden complementarse.

```txt
Pathfinding
→ calcula ruta global.

Obstacle Avoidance
→ evita obstáculos locales mientras se sigue la ruta.

Movimiento
→ ejecuta el desplazamiento corregido.
```

Ejemplo:

```txt
La ruta indica avanzar al siguiente punto.

Obstacle Avoidance detecta una caja dinámica.

El movimiento esquiva la caja.

Luego el NPC vuelve a seguir la ruta.
```

No conviene usar Obstacle Avoidance como reemplazo de pathfinding en mapas complejos.

Una técnica local no debería resolver un problema global de navegación.

---

## Cuándo conviene usarlo

Conviene usar Obstacle Avoidance cuando:

```txt
hay obstáculos dinámicos
los NPCs se traban con objetos cercanos
el movimiento directo causa choques
el pathfinding global no resuelve obstáculos locales
hay varios agentes moviéndose cerca
el NPC necesita ajustar su trayectoria en tiempo real
```

Pregunta clave:

```txt
¿El problema es un obstáculo local durante el movimiento?
```

Si la respuesta es sí, Obstacle Avoidance puede aportar valor.

---

## Cuándo NO conviene usarlo

No conviene usar Obstacle Avoidance si:

```txt
el NPC no se mueve
el movimiento simple alcanza
el movimiento es por grilla estricta
el mapa ya tiene rutas totalmente controladas
los obstáculos no afectan al agente
pathfinding global alcanza
el costo no se justifica
```

Ejemplos:

```txt
comerciante fijo
NPC de diálogo
torreta fija
enemigo sobre rails
juego por turnos en casillas
```

Regla:

```txt
No agregar avoidance si no hay obstáculos locales que evitar.
```

---

## Riesgos comunes

Riesgos comunes al implementar Obstacle Avoidance:

```txt
usarlo como pathfinding completo
hacer demasiados raycasts por frame
no configurar layers correctamente
ignorar el tamaño del agente
no controlar distancia de detección
elegir siempre la misma dirección alternativa
generar vibración frente a obstáculos
no volver a la ruta original
mantener debug activo en runtime
```

Ejemplo de mala práctica:

```txt
Obstacle Avoidance intenta encontrar todo el camino hasta el jugador.
```

Problema:

```txt
Se usa una técnica local para resolver un problema global.
```

---

## Validación

Obstacle Avoidance se valida revisando:

```txt
si detecta obstáculos correctamente
si evita sin trabarse
si no vibra entre direcciones
si no se aleja demasiado de su objetivo
si vuelve al movimiento esperado
si respeta layers
si la distancia de detección tiene sentido
```

Debug útil:

```txt
raycasts visibles
dirección deseada
dirección corregida
obstáculo detectado
distancia de detección
radio del agente
```

---

## Regla final

Obstacle Avoidance no decide a dónde ir.

Solo ayuda a no chocar mientras el NPC intenta moverse.

Resuelve corrección local.

No reemplaza navegación global.
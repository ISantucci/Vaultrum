## Definicion

Persecucion es un comportamiento en el que un NPC intenta acercarse a un objetivo, una amenaza, un jugador o una ultima posicion conocida.

```txt
Persecucion
→ acercarse a un objetivo relevante
```

Puede ser directa o consumir navegacion segun el mapa.

Perseguir no significa necesariamente atacar.

El ataque depende de rango, condiciones y decision.

---

## Responsabilidad

La responsabilidad de persecucion es mantener al NPC orientado hacia un objetivo de seguimiento.

Debe responder:

```txt
¿A que objetivo debo acercarme?
¿Cual es la posicion actual del objetivo?
¿Debo usar una ruta?
¿Debo seguir hasta alcanzarlo?
¿Debo detenerme si lo pierdo?
¿Debo ir a la ultima posicion conocida?
```

Persecucion debe coordinar la intencion de acercarse.

No debe contener todo el sistema de deteccion, ataque o pathfinding.

---

## Que NO debe hacer

Persecucion no debe:

```txt
detectar al jugador por si sola
decidir todos los estados del NPC
calcular internamente algoritmos generales
aplicar daño
resolver ataque completo
resolver huida
controlar animacion completa
actualizar UI
```

Ejemplo incorrecto:

```txt
ChaseBehaviour
→ busca jugador
→ detecta vision
→ calcula A Star
→ mueve
→ ataca
→ reproduce animaciones
```

Ejemplo correcto:

```txt
ChaseBehaviour
→ recibe un objetivo o posicion.

Sistema de movimiento
→ ejecuta desplazamiento.

Servicio de navegacion
→ calcula ruta si hace falta.

Sistema de decision
→ decide cuando dejar de perseguir.
```

Regla:

```txt
Persecucion sigue un objetivo.
No decide toda la IA.
```

---

## Que problema resuelve

Persecucion permite que un NPC responda activamente a un objetivo.

Ejemplos:

```txt
enemigo que corre hacia el jugador
guardia que sigue a un intruso
animal que persigue una presa
aliado que sigue al jugador
boss que se reposiciona hacia un objetivo
```

Sirve para crear:

```txt
presion
amenaza
urgencia
castigo por deteccion
control del espacio
```

---

## Datos que necesita

Persecucion puede necesitar:

```txt
objetivo actual
posicion objetivo
ultima posicion conocida
velocidad
distancia minima
rango de abandono
tiempo maximo sin ver objetivo
referencia al movimiento
referencia a navegacion si aplica
```

No todos los casos requieren pathfinding.

Ejemplo simple:

```txt
enemigo en arena abierta
→ moverse directo hacia jugador
```

Ejemplo con navegacion:

```txt
guardia en mapa con paredes
→ pedir ruta hacia ultima posicion conocida
```

---

## Que produce

Persecucion puede producir:

```txt
objetivo de movimiento
solicitud de ruta
solicitud de desplazamiento
estado de llegada
distancia al objetivo
evento de objetivo perdido
evento de persecucion finalizada
```

Ejemplo:

```txt
TargetPosition = ultima posicion conocida
ShouldMove = true
```

Eso no significa que el NPC deba atacar.

Solo significa que la persecucion esta intentando acercarse.

---

## Como funciona

Una persecucion simple puede seguir este flujo:

```txt
1. Recibir objetivo.
2. Calcular direccion o ruta.
3. Moverse hacia el objetivo.
4. Revisar distancia.
5. Detenerse si llega, pierde objetivo o cambia decision.
```

Ejemplo conceptual:

```csharp
using UnityEngine;

public class DirectChase
{
    private readonly Transform owner;
    private readonly Transform target;
    private readonly float speed;
    private readonly float stopDistance;

    public DirectChase(
        Transform owner,
        Transform target,
        float speed,
        float stopDistance)
    {
        this.owner = owner;
        this.target = target;
        this.speed = speed;
        this.stopDistance = stopDistance;
    }

    public void Tick(float deltaTime)
    {
        Vector3 direction = target.position - owner.position;

        if (direction.magnitude <= stopDistance)
        {
            return;
        }

        owner.position += direction.normalized * speed * deltaTime;
    }
}
```

Este ejemplo solo se acerca al objetivo.

No detecta, no decide, no ataca y no calcula rutas complejas.

---

## Persecucion con ultima posicion conocida

En juegos donde el NPC puede perder de vista al jugador, la persecucion puede usar una ultima posicion conocida.

Flujo:

```txt
detecto jugador
→ guardo posicion

pierdo vision
→ sigo hasta ultima posicion conocida

llego y no encuentro
→ investigo, espero o vuelvo a rutina
```

Esto evita que el NPC persiga magicamente al jugador para siempre.

---

## Persecucion con navegacion

Si el mapa tiene obstaculos, paredes o rutas complejas, persecucion puede consumir un sistema de navegacion.

```txt
Persecucion
→ pide llegar a objetivo.

Pathfinding
→ calcula ruta.

Movimiento
→ sigue ruta.
```

Persecucion no debe explicar completo como funciona A Star, nodos o costos.

Solo debe indicar como consume el resultado.

---

## Cuando conviene implementarlo

Conviene usar persecucion cuando:

```txt
el NPC debe acercarse a un objetivo
el jugador debe sentir presion
el enemigo debe castigar deteccion
el aliado debe seguir al jugador
el NPC debe investigar una posicion
el objetivo puede moverse
```

Pregunta clave:

```txt
¿El NPC necesita reducir distancia con algo?
```

Si la respuesta es si, persecucion puede tener sentido.

---

## Cuando NO conviene implementarlo

No conviene usar persecucion si:

```txt
el NPC no debe moverse hacia objetivos
el ataque es a distancia y no requiere acercamiento
el NPC debe quedarse defendiendo una zona
el enemigo usa rutas fijas
el jugador no debe ser seguido
la posicion objetivo no importa
```

Ejemplos:

```txt
torreta fija
comerciante
NPC de dialogo
enemigo que dispara desde cobertura fija
guardia que solo alerta pero no persigue
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
perseguir aunque el jugador ya no fue detectado
saber magicamente donde esta el jugador
recalcular ruta cada frame
mezclar persecucion con ataque
mezclar persecucion con deteccion
no definir distancia de parada
no definir cuando abandonar persecucion
ignorar obstaculos
usar movimiento directo en mapa complejo
```

Ejemplo de mala practica:

```txt
ChaseBehaviour busca jugador, calcula ruta, detecta vision y ataca.
```

Problema:

```txt
La persecucion deja de ser un comportamiento.
Se convierte en una clase monolitica de enemigo.
```

---

## Costos de implementacion

Persecucion puede requerir:

```txt
objetivo actual
movimiento
distancia minima
condiciones de abandono
ultima posicion conocida
integracion con navegacion si aplica
integracion con decision
debug de objetivo
debug de ruta
```

La complejidad aumenta si el objetivo se mueve constantemente o si hay muchos obstaculos.

---

## Costos de optimizacion

Riesgos comunes:

```txt
recalcular pathfinding cada frame
actualizar ruta aunque el objetivo no cambio significativamente
hacer raycasts constantes
buscar objetivo globalmente
crear listas nuevas de ruta todo el tiempo
mover muchos NPCs con logica pesada simultanea
```

Alternativas:

```txt
recalcular por intervalo
recalcular solo si el objetivo se movio suficiente
usar ultima ruta valida
cachear referencia al objetivo
limitar cantidad de rutas por frame
separar chequeo de distancia de pathfinding
```

Regla:

```txt
Perseguir no implica recalcular camino todo el tiempo.
```

---

## Criterio de optimizacion

Antes de optimizar persecucion, revisar:

```txt
cantidad de NPCs persiguiendo
si usan navegacion
frecuencia de recalculo de ruta
distancia al objetivo
cambio real de posicion del objetivo
si se puede usar ultima posicion conocida
si la ruta anterior sigue siendo valida
```

Criterio:

```txt
persecucion directa
→ costo bajo o moderado.

persecucion con pathfinding recalculado por frame
→ riesgo alto.
```

---

## Validacion

Persecucion se valida revisando:

```txt
si el NPC se acerca al objetivo correcto
si se detiene a distancia correcta
si no atraviesa obstaculos
si abandona persecucion cuando corresponde
si usa ultima posicion conocida si aplica
si no recalcula rutas sin necesidad
si el jugador entiende por que lo persiguen
```

Debug util:

```txt
linea hacia objetivo
gizmo de distancia de parada
ruta actual
ultima posicion conocida
estado actual visible
logs temporales de cambio de objetivo
```

---

## Preguntas antes de implementarlo

Antes de implementar persecucion, preguntar:

```txt
¿El NPC necesita acercarse a un objetivo?
¿Cual es el objetivo?
¿Debe perseguir posicion actual o ultima posicion conocida?
¿Necesita pathfinding o movimiento directo?
¿Cada cuanto se actualiza la ruta?
¿Cual es la distancia de parada?
¿Cuando abandona persecucion?
¿Que pasa si pierde al objetivo?
¿La persecucion esta separada de deteccion y ataque?
¿Se puede validar con debug visual?
```

---

## Errores comunes

Errores comunes:

```txt
perseguir aunque el jugador ya no fue detectado
saber magicamente donde esta el jugador
recalcular ruta cada frame
mezclar persecucion con ataque
mezclar persecucion con deteccion
no definir distancia de parada
no definir cuando abandonar persecucion
ignorar obstaculos
usar movimiento directo en mapa complejo
```

---

## Criterio para una IA

Cuando una IA trabaje con persecucion debe:

```txt
mantenerla como comportamiento de acercamiento
no duplicar deteccion
no duplicar ataque
no explicar algoritmos de pathfinding completos
separar objetivo, ruta y movimiento
definir condiciones de entrada y salida
indicar cuando usar ultima posicion conocida
marcar costos si hay recalculo de rutas
proponer validacion visual
respetar navegacion waterfall
```

Regla operativa:

```txt
Persecucion responde como acercarse.
No responde por que se eligio perseguir.
```

---

## Checklist

Antes de implementar persecucion, revisar:

```txt
¿El NPC necesita acercarse a un objetivo?
¿Cual es el objetivo?
¿Debe perseguir posicion actual o ultima posicion conocida?
¿Necesita pathfinding o movimiento directo?
¿Cada cuanto se actualiza la ruta?
¿Cual es la distancia de parada?
¿Cuando abandona persecucion?
¿Que pasa si pierde al objetivo?
¿La persecucion esta separada de deteccion y ataque?
¿Se puede validar con debug visual?
```

---

## Regla final

```txt
Perseguir no es saber todo.

Perseguir es intentar llegar a un objetivo bajo condiciones claras.
```
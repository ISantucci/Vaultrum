## Definicion

Huida es un comportamiento en el que un NPC intenta alejarse de una amenaza, buscar seguridad o evitar una situacion peligrosa.

```txt
Huida
→ alejarse de amenaza
→ buscar seguridad
→ sobrevivir
```

No todos los NPCs huyen por la misma razon.

Un civil puede huir por miedo.

Un enemigo puede huir por baja vida.

Un animal puede huir si el jugador se acerca.

Un aliado puede retirarse para reposicionarse.

---

## Responsabilidad

La responsabilidad de huida es definir como un NPC responde cuando necesita evitar peligro.

Debe responder:

```txt
¿De que amenaza me alejo?
¿Hacia donde conviene huir?
¿Hasta cuando huyo?
¿Que distancia considero segura?
¿Busco un punto de refugio?
¿Huyo directamente o usando navegacion?
¿Que pasa cuando ya estoy a salvo?
```

Huida no debe decidir toda la IA del NPC.

Debe ejecutar una respuesta evasiva cuando otro sistema indica que corresponde.

---

## Que NO debe hacer

Huida no debe absorber:

```txt
deteccion completa de amenazas
decision completa del NPC
pathfinding general
movimiento completo
sistema de vida
animacion completa
logica de combate completa
```

Ejemplo incorrecto:

```txt
FleeBehaviour
→ detecta jugador
→ evalua vida
→ decide estado
→ calcula todo el mapa
→ mueve
→ cambia animacion
```

Ejemplo correcto:

```txt
FleeBehaviour
→ recibe amenaza o posicion peligrosa
→ elige direccion o punto seguro
→ solicita movimiento

Sistema de decision
→ decide cuando huir

Sistema de movimiento
→ ejecuta desplazamiento
```

Regla:

```txt
Huida ejecuta evasion.
No decide toda la supervivencia del NPC.
```

---

## Que problema resuelve

Huida permite que los NPCs no respondan siempre atacando.

Aporta variedad, credibilidad y diseño.

Ejemplos:

```txt
civil que corre al ver peligro
enemigo debil que escapa con poca vida
animal que evita al jugador
aliado que se reposiciona
enemigo que busca refuerzos
boss que se aleja para cambiar de fase
```

Huida puede mejorar la experiencia porque muestra que los NPCs tienen instinto de supervivencia o prioridades distintas.

---

## Datos que necesita

Huida puede necesitar:

```txt
amenaza actual
posicion de amenaza
distancia minima segura
velocidad
punto seguro
zona de refugio
vida actual
umbral de vida
tiempo maximo de huida
referencia al movimiento
informacion del mapa si aplica
```

No todos los casos necesitan punto seguro.

Ejemplo simple:

```txt
alejarse en direccion opuesta a la amenaza
```

Ejemplo avanzado:

```txt
buscar cobertura, ruta segura o zona protegida
```

---

## Que produce

Huida puede producir:

```txt
direccion de escape
punto seguro elegido
solicitud de movimiento
estado de seguridad
evento de inicio de huida
evento de fin de huida
```

Ejemplo:

```txt
FleeDirection = direccion opuesta a amenaza
SafeDistanceReached = false
```

Eso no significa que el NPC decida todo su estado.

Solo significa que el comportamiento evasivo esta activo.

---

## Como funciona

Una huida simple puede calcular direccion opuesta a la amenaza.

```txt
direccion de huida
= posicion NPC - posicion amenaza
```

Ejemplo conceptual:

```csharp
using UnityEngine;

public class FleeMovement
{
    private readonly Transform owner;
    private readonly float speed;

    public FleeMovement(Transform owner, float speed)
    {
        this.owner = owner;
        this.speed = speed;
    }

    public void FleeFrom(Vector3 threatPosition, float deltaTime)
    {
        Vector3 direction = owner.position - threatPosition;

        if (direction.sqrMagnitude <= 0.001f)
        {
            return;
        }

        owner.position += direction.normalized * speed * deltaTime;
    }
}
```

Este ejemplo solo se aleja.

No decide cuando huir ni calcula refugios.

---

## Huida hacia punto seguro

En mapas mas complejos, huir en linea recta puede ser insuficiente.

Puede convenir buscar:

```txt
punto seguro
cobertura
zona aliada
salida
distancia maxima
nodo con menor peligro
```

Flujo:

```txt
amenaza detectada
→ decision indica huir
→ se elige punto seguro
→ movimiento se dirige hacia ese punto
→ se valida distancia segura
→ se cambia de comportamiento si corresponde
```

Si se usa navegacion, huida puede consumir un resultado de pathfinding.

No debe reescribir el algoritmo completo.

---

## Cuando conviene implementarlo

Conviene implementar huida cuando:

```txt
el NPC debe preservar su vida
el juego necesita civiles reactivos
los enemigos tienen moral o miedo
los animales evitan amenazas
un aliado debe reposicionarse
el NPC debe buscar refuerzos
la amenaza no siempre debe resolverse con combate
```

Pregunta clave:

```txt
¿Este NPC deberia evitar peligro en vez de enfrentarlo?
```

---

## Cuando NO conviene implementarlo

No conviene usar huida si:

```txt
el NPC debe ser agresivo siempre
el juego necesita enemigos simples
el espacio no permite huir
la huida confundiria al jugador
la mecanica no aporta nada
el NPC no tiene rol de supervivencia
```

Ejemplos:

```txt
enemigo suicida
torreta fija
boss que debe sostener combate frontal
NPC decorativo sin reaccion
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
huir directamente contra una pared
correr hacia otra amenaza
huir para siempre
no definir condicion de salida
mezclar huida con decision completa
recalcular punto seguro cada frame
hacer que todos los NPCs huyan igual
no dar feedback de miedo o retirada
crear huida para NPCs que no la necesitan
```

Ejemplo de mala practica:

```txt
FleeBehaviour evalua vida, detecta amenazas, calcula ruta y cambia estados.
```

Problema:

```txt
Huida deja de ser comportamiento evasivo.
Empieza a absorber decision, percepcion y navegacion.
```

---

## Costos de implementacion

Huida puede requerir:

```txt
deteccion de amenaza
criterio de peligro
punto seguro
distancia segura
integracion con movimiento
integracion con decision
posible navegacion
debug de direccion o destino
condicion de salida
```

La complejidad aumenta si se buscan refugios o zonas seguras.

---

## Costos de optimizacion

Riesgos comunes:

```txt
buscar puntos seguros cada frame
recalcular rutas constantemente
evaluar muchos nodos de peligro
hacer raycasts masivos para cobertura
actualizar huida en muchos NPCs simultaneamente
```

Alternativas:

```txt
cachear puntos seguros
actualizar por intervalos
limitar busquedas por frame
usar zonas predefinidas
usar heuristicas simples
recalcular solo si la amenaza cambia mucho
```

Regla:

```txt
Huir bien no siempre requiere calcular el mejor refugio posible.
A veces alcanza con una direccion segura suficiente.
```

---

## Criterio de optimizacion

Antes de optimizar huida, revisar:

```txt
cantidad de NPCs que pueden huir
si usan punto seguro
si usan navegacion
frecuencia de recalculo
cantidad de amenazas
si hay busqueda de cobertura
si existen zonas predefinidas
```

Criterio:

```txt
huida por direccion opuesta
→ costo bajo.

huida con busqueda dinamica de refugio
→ costo mayor.

huida con refugios predefinidos
→ mas controlable.
```

---

## Validacion

Huida se valida revisando:

```txt
si el NPC se aleja de la amenaza
si no se queda atrapado
si no corre hacia mas peligro
si respeta distancia segura
si termina la huida cuando corresponde
si el jugador entiende por que huyo
si la huida aporta al gameplay
```

Debug util:

```txt
linea desde amenaza a NPC
direccion de huida
punto seguro elegido
distancia segura
estado actual
logs de inicio y fin de huida
```

---

## Preguntas antes de implementarlo

Antes de implementar huida, preguntar:

```txt
¿El NPC necesita evitar una amenaza?
¿Que amenaza lo activa?
¿Debe alejarse en linea recta o buscar punto seguro?
¿Cual es la distancia segura?
¿Cuando deja de huir?
¿Necesita navegacion?
¿Puede quedar atrapado?
¿Hay feedback de miedo, retirada o alerta?
¿La huida aporta al gameplay?
¿La solucion simple alcanza?
```

---

## Errores comunes

Errores comunes:

```txt
huir directamente contra una pared
correr hacia otra amenaza
huir para siempre
no definir condicion de salida
mezclar huida con decision completa
recalcular punto seguro cada frame
hacer que todos los NPCs huyan igual
no dar feedback de miedo o retirada
crear huida para NPCs que no la necesitan
```

---

## Criterio para una IA

Cuando una IA trabaje con huida debe:

```txt
mantenerla como comportamiento evasivo
no duplicar deteccion de amenazas
no absorber decision completa
separar amenaza, destino y movimiento
definir condicion de entrada y salida
indicar si usa direccion simple o punto seguro
considerar costos si busca rutas o refugios
proponer validacion visual
respetar navegacion waterfall
```

Regla operativa:

```txt
Huida no es panico sin control.

Es una respuesta evasiva con condicion y destino.
```

---

## Checklist

Antes de implementar huida, revisar:

```txt
¿El NPC necesita evitar una amenaza?
¿Que amenaza lo activa?
¿Debe alejarse en linea recta o buscar punto seguro?
¿Cual es la distancia segura?
¿Cuando deja de huir?
¿Necesita navegacion?
¿Puede quedar atrapado?
¿Hay feedback de miedo, retirada o alerta?
¿La huida aporta al gameplay?
¿La solucion simple alcanza?
```

---

## Regla final

```txt
Huir no es fallar como NPC.

Huir puede ser el comportamiento correcto si protege el rol del personaje.
```
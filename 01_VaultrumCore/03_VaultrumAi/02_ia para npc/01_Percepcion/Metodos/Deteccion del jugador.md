## Definicion

La deteccion del jugador es el proceso mediante el cual un NPC identifica que el jugador existe, esta cerca, esta visible, hizo ruido, entro en una zona, ataco o representa una amenaza.

```txt
Deteccion del jugador
→ recibe estimulos relacionados con el jugador
→ confirma si el jugador fue detectado
→ informa a la toma de decisiones
```

Detectar al jugador no significa necesariamente atacarlo.

Un NPC puede detectar al jugador y luego:

```txt
saludar
huir
perseguir
atacar
investigar
pedir ayuda
activar una alarma
mirar hacia el jugador
guardar ultima posicion conocida
ignorar si no es relevante
```

La accion posterior depende del sistema de decision y del rol del NPC.

---

## Responsabilidad

La responsabilidad de la deteccion del jugador es responder una pregunta concreta:

```txt
¿El NPC tiene informacion suficiente para considerar detectado al jugador?
```

Puede combinar distintas fuentes:

```txt
distancia
[[Field of View]]
raycasts
triggers
sonido
daño recibido
eventos
zonas de alerta
memoria temporal
nivel de sospecha
```

Su salida puede ser:

```txt
jugador detectado
jugador no detectado
ultima posicion conocida
tipo de deteccion
nivel de confianza
tiempo desde la ultima deteccion
```

La deteccion debe entregar informacion.

No debe decidir toda la respuesta del NPC.

---

## Que NO debe hacer

La deteccion del jugador no debe:

```txt
decidir automaticamente atacar
decidir automaticamente perseguir
decidir automaticamente huir
mover al NPC
calcular pathfinding
aplicar daño
cambiar animaciones directamente
resolver todo el comportamiento enemigo
```

Ejemplo incorrecto:

```txt
PlayerDetector
→ detecta jugador
→ cambia estado
→ calcula ruta
→ mueve enemigo
→ ataca
```

Ejemplo correcto:

```txt
PlayerDetector
→ informa jugador detectado.

Sistema de decision
→ decide que hacer.

Comportamiento
→ ejecuta persecucion, ataque, huida o investigacion.
```

Regla:

```txt
Detectar jugador no es decidir respuesta.
```

---

## Que problema resuelve

La deteccion del jugador ayuda a definir cuando y por que un NPC reacciona al jugador.

Sin deteccion clara, pueden aparecer comportamientos injustos o confusos.

Ejemplo:

```txt
Jugador escondido
→ enemigo lo persigue igual
→ sensacion de trampa
```

Otro ejemplo:

```txt
Jugador frente al enemigo
→ enemigo no reacciona
→ sensacion de IA rota
```

Una buena deteccion permite que el jugador entienda:

```txt
me vio
me escucho
entre en su zona
lo ataque
hice ruido
```

Esto mejora la legibilidad del comportamiento.

---

## Datos que necesita

La deteccion del jugador puede necesitar:

```txt
referencia al jugador
posicion del NPC
rango de deteccion
angulo visual
mascara de obstaculos
capas de jugador
eventos de ruido
eventos de daño
zonas de alerta
temporizador de memoria
configuracion de sospecha
```

No siempre necesita todo.

Ejemplo simple:

```txt
enemigo basico
→ rango de deteccion
→ referencia al jugador
```

Ejemplo avanzado:

```txt
guardia de sigilo
→ rango
→ Field of View
→ Line of Sight
→ memoria
→ sospecha
→ ultima posicion conocida
```

---

## Que produce

La deteccion del jugador puede producir:

```txt
bool de jugador detectado
referencia al jugador detectado
posicion actual detectada
ultima posicion conocida
tipo de estimulo
nivel de sospecha
tiempo desde ultima deteccion
```

Ejemplo:

```txt
PlayerDetected = true
LastKnownPosition = posicion del jugador
DetectionType = vision
```

Eso no significa automaticamente:

```txt
atacar
perseguir
huir
activar alarma
```

Solo significa:

```txt
el jugador fue percibido por algun canal valido
```

---

## Como funciona

Una deteccion del jugador puede funcionar de menor a mayor complejidad.

### Deteccion por distancia

```txt
jugador dentro de rango
→ detectado
```

Es simple, barata y facil de validar.

Sirve para enemigos directos, zonas de proximidad o NPCs que no necesitan vision direccional.

---

### Deteccion visual

```txt
jugador dentro de rango
+ dentro del angulo
+ sin obstaculos
→ detectado
```

Puede consumir [[Field of View]].

Sirve para guardias, sigilo, camaras y enemigos donde la vision sea importante.

---

### Deteccion por sonido

```txt
jugador genera ruido
→ NPC recibe estimulo
→ guarda posicion aproximada
```

Sirve para investigacion, distracciones o sigilo.

---

### Deteccion por daño recibido

```txt
NPC recibe daño
→ detecta amenaza
→ registra origen aproximado
```

No siempre permite saber exactamente donde esta el jugador.

Puede disparar alerta, investigacion, defensa o huida.

---

### Deteccion por zona

```txt
jugador entra en zona prohibida
→ detectado como intruso
```

Sirve para areas restringidas, alarmas, tutoriales o triggers de seguridad.

---

### Deteccion por sospecha progresiva

```txt
jugador parcialmente visible
→ sube sospecha

jugador se oculta
→ baja sospecha

sospecha llega al maximo
→ detectado
```

Sirve cuando la deteccion no debe ser instantanea.

---

## Ejemplo conceptual en C#

```csharp
using UnityEngine;

public class PlayerDetectionResult
{
    public bool IsDetected { get; }
    public Vector3 LastKnownPosition { get; }
    public string DetectionType { get; }

    public PlayerDetectionResult(bool isDetected, Vector3 lastKnownPosition, string detectionType)
    {
        IsDetected = isDetected;
        LastKnownPosition = lastKnownPosition;
        DetectionType = detectionType;
    }
}

public class PlayerDetector
{
    private readonly Transform owner;
    private readonly Transform player;
    private readonly float detectionRange;

    public PlayerDetector(Transform owner, Transform player, float detectionRange)
    {
        this.owner = owner;
        this.player = player;
        this.detectionRange = detectionRange;
    }

    public PlayerDetectionResult Detect()
    {
        float distance = Vector3.Distance(owner.position, player.position);

        if (distance <= detectionRange)
        {
            return new PlayerDetectionResult(
                true,
                player.position,
                "Distance"
            );
        }

        return new PlayerDetectionResult(
            false,
            Vector3.zero,
            "None"
        );
    }
}
```

Este ejemplo solo detecta.

No decide.

No mueve.

No ataca.

---

## Como aplicarlo en videojuegos

Conviene implementar deteccion del jugador cuando el jugador debe afectar el comportamiento del NPC.

Ejemplos:

```txt
enemigos
guardias
camaras
animales
civiles reactivos
aliados
bosses
NPCs de tutorial
zonas de alerta
```

Preguntas utiles:

```txt
¿El NPC debe saber que el jugador existe?
¿El NPC debe reaccionar a presencia, vision, ruido o daño?
¿El jugador puede evitar ser detectado?
¿La deteccion debe ser justa y legible?
¿La deteccion cambia el comportamiento?
```

---

## Relacion con Field of View

La deteccion del jugador puede consumir [[Field of View]] cuando la vision direccional importa.

```txt
Field of View
→ confirma si el jugador es visible.

Deteccion del jugador
→ combina esa informacion con otros estimulos.

Decision
→ decide que hacer.
```

Field of View no debe reemplazar toda la deteccion.

Deteccion del jugador no debe reescribir toda la teoria de Field of View.

---

## Cuando conviene implementarlo

Conviene implementar deteccion del jugador cuando:

```txt
la presencia del jugador cambia el comportamiento del NPC
el jugador puede ser visto, escuchado o sentido
el NPC debe reaccionar de forma legible
el juego necesita sigilo, alerta, combate o persecucion
hay zonas donde el jugador puede ser detectado
```

Pregunta clave:

```txt
¿El NPC necesita saber algo sobre el jugador para cumplir su rol?
```

Si la respuesta es si, la deteccion puede aportar valor.

---

## Cuando NO conviene implementarlo

No conviene implementar deteccion del jugador si el NPC no necesita reaccionar al jugador.

Ejemplos:

```txt
NPC decorativo
comerciante estatico
personaje de dialogo simple
objeto interactivo
enemigo que siempre sigue una ruta fija sin reaccionar
```

Tampoco conviene hacer deteccion avanzada si alcanza con una condicion simple.

Ejemplo:

```txt
NPC abre dialogo al interactuar
→ no necesita deteccion compleja.
```

Regla:

```txt
No implementar sensores si el rol del NPC no los necesita.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
detectar y atacar en el mismo sistema
hacer que el NPC sepa siempre donde esta el jugador
detectar a traves de paredes
usar deteccion 360 grados sin intencion
no separar vision, sonido y daño
usar FindObjectOfType constantemente
no limpiar estados de deteccion
usar demasiados sensores para NPCs simples
```

Ejemplo de mala practica:

```txt
PlayerDetector detecta jugador y llama directamente a Attack().
```

Problema:

```txt
La percepcion queda acoplada al combate.
La decision desaparece.
El sistema pierde flexibilidad.
```

---

## Costos de implementacion

La deteccion del jugador puede requerir:

```txt
referencias al jugador
sensores
triggers
raycasts
layers
eventos
memoria
sospecha
debug
integracion con decision
configuracion por NPC
```

A mayor cantidad de fuentes de deteccion, mayor complejidad.

Ejemplo simple:

```txt
rango
→ bajo costo
```

Ejemplo avanzado:

```txt
rango + vision + raycast + sonido + memoria + sospecha
→ costo mayor
```

---

## Costos de optimizacion

Riesgos comunes:

```txt
chequear jugador cada frame en todos los NPCs
usar raycasts constantes
usar OverlapSphere sin filtros
buscar al jugador globalmente
crear listas temporales
actualizar NPCs lejanos
mantener debug activo en runtime
```

Alternativas:

```txt
cachear referencia al jugador
usar triggers como pre-filtro
actualizar por intervalos
usar eventos para ruido o daño
separar chequeos baratos y caros
desactivar deteccion en NPCs inactivos
limitar frecuencia de raycasts
```

Regla:

```txt
No todos los sensores deben actualizar todo el tiempo.
```

---

## Criterio de optimizacion

Antes de optimizar, revisar:

```txt
cantidad de NPCs
cantidad de sensores por NPC
frecuencia de chequeo
cantidad de raycasts
si hay deteccion por eventos
si hay debug activo
si el NPC esta cerca del jugador
si el NPC esta activo o visible
```

Criterio:

```txt
1 NPC con deteccion simple
→ costo bajo.

100 NPCs con vision, sonido y raycast por frame
→ riesgo alto.

100 NPCs con filtros, intervalos, eventos y cache
→ mas controlable.
```

---

## Validacion

La deteccion del jugador se puede validar con:

```txt
gizmos de rango
cono de vision visible en editor
logs temporales
estado detectado/no detectado en inspector
lineas de raycast
indicador de sospecha
debug de ultima posicion conocida
pruebas con obstaculos
pruebas desde atras del NPC
pruebas de perdida de vision
```

Preguntas de validacion:

```txt
¿Detecta al jugador cuando deberia?
¿No lo detecta cuando no deberia?
¿Respeta paredes?
¿Respeta angulo?
¿Respeta distancia?
¿La perdida de deteccion tiene sentido?
¿El jugador entiende por que fue detectado?
```

---

## Preguntas antes de implementarlo

Antes de implementar deteccion del jugador, preguntar:

```txt
¿El NPC necesita reaccionar al jugador?
¿La deteccion debe ser por distancia, vision, sonido, daño, zona o evento?
¿La deteccion debe ser instantanea o progresiva?
¿Debe guardar ultima posicion conocida?
¿Debe haber perdida de deteccion?
¿La deteccion esta separada de la decision?
¿Hay feedback para el jugador?
¿Hay validacion con gizmos o logs?
¿El costo es razonable para la cantidad de NPCs?
¿Una deteccion simple alcanza?
```

---

## Errores comunes

Errores comunes:

```txt
detectar a traves de paredes
detectar sin rango
detectar 360 grados sin querer
detectar y atacar en el mismo sistema
no separar vision de decision
no guardar ultima posicion cuando el juego lo necesita
hacer deteccion instantanea cuando deberia ser progresiva
usar demasiados sensores para un NPC simple
no limpiar estados de deteccion
usar FindObjectOfType constantemente
```

---

## Criterio para una IA

Cuando una IA trabaje con deteccion del jugador debe:

```txt
tratarla como nota consumidora/aplicada de percepcion
no convertirla en sistema completo de combate
no duplicar todos los comportamientos
no redefinir Field of View
no duplicar pathfinding
explicar que estimulos usa
explicar que salida produce
separar detectar de decidir
marcar costos cuando use raycasts o chequeos frecuentes
proponer validacion visual
respetar la navegacion waterfall
```

Regla operativa:

```txt
La deteccion responde si el jugador fue percibido.
La decision responde que hacer con esa informacion.
```

---

## Checklist

Antes de implementar deteccion del jugador, revisar:

```txt
¿El NPC necesita reaccionar al jugador?
¿La deteccion debe ser por distancia, vision, sonido, daño, zona o evento?
¿La deteccion debe ser instantanea o progresiva?
¿Debe guardar ultima posicion conocida?
¿Debe haber perdida de deteccion?
¿La deteccion esta separada de la decision?
¿Hay feedback para el jugador?
¿Hay validacion con gizmos o logs?
¿El costo es razonable para la cantidad de NPCs?
¿Una deteccion simple alcanza?
```

---

## Regla final

```txt
Detectar al jugador no significa decidir que hacer con el.

La deteccion informa.
La decision interpreta.
El comportamiento actua.
```
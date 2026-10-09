## Definicion

Field of View, o campo de vision, es una tecnica de percepcion visual que define el area dentro de la cual un NPC puede ver o detectar visualmente un objetivo.

En videojuegos, representa hacia donde esta mirando un NPC y que parte del entorno puede percibir.

Un Field of View normalmente combina tres condiciones:

```txt
distancia
angulo
linea de vision
```

Ejemplo:

```txt
Objetivo dentro del rango
+ objetivo dentro del angulo
+ sin obstaculos en el medio
→ objetivo visible
```

Field of View no decide que hace el NPC.

Solo responde si un objetivo puede ser visto.

---

## Responsabilidad

La responsabilidad de Field of View es responder una pregunta concreta:

```txt
¿Este objetivo esta dentro del campo visual del NPC?
```

Puede evaluar:

```txt
distancia maxima de vision
angulo de vision
direccion actual del NPC
posicion del objetivo
linea de vision
obstaculos
layers
punto de origen visual
```

Su salida deberia ser simple y consultable.

Ejemplos:

```txt
puede ver
no puede ver
objetivo visible
objetivo no visible
```

Field of View funciona como proveedor de informacion visual.

Otros sistemas pueden consumir ese resultado para decidir que hacer.

---

## Que NO debe hacer

Field of View no debe absorber responsabilidades de decision, comportamiento, combate o movimiento.

No debe decidir:

```txt
atacar
perseguir
huir
patrullar
cambiar estado
calcular pathfinding
mover al NPC
aplicar daño
activar animaciones
actualizar UI
```

Ejemplo incorrecto:

```txt
FieldOfView
→ detecta jugador
→ cambia a estado persecucion
→ calcula ruta
→ mueve al enemigo
→ ataca si esta cerca
```

Ejemplo correcto:

```txt
FieldOfView
→ informa si el objetivo es visible.

Sistema de decision
→ interpreta esa informacion.

Comportamiento
→ ejecuta la accion elegida.

Movimiento
→ desplaza al NPC si corresponde.
```

Regla:

```txt
Field of View detecta vision.
No decide comportamiento.
```

---

## Que problema resuelve

Field of View ayuda a que la deteccion visual sea mas clara, justa y creible.

Sin Field of View, un NPC podria detectar al jugador aunque:

```txt
este detras del NPC
este demasiado lejos
este detras de una pared
este fuera de la direccion visual
```

Eso puede generar sensacion de trampa o comportamiento poco legible.

Con Field of View:

```txt
Jugador detras del NPC
→ fuera del angulo visual
→ no visible.

Jugador detras de una pared
→ linea de vision bloqueada
→ no visible.

Jugador frente al NPC y sin obstaculos
→ visible.
```

Esto permite que el jugador entienda mejor por que fue detectado o por que logro evitar la deteccion.

---

## Datos que necesita

Un Field of View suele necesitar:

```txt
referencia del NPC
referencia del objetivo
distancia maxima de vision
angulo de vision
direccion frontal del NPC
mascara de obstaculos
mascara de objetivos
punto de origen visual
```

Opcionalmente puede necesitar:

```txt
altura de ojos
radio de busqueda inicial
lista de objetivos candidatos
frecuencia de chequeo
debug visual
configuracion por tipo de NPC
```

No todos los casos necesitan todos estos datos.

Ejemplo simple:

```txt
NPC enemigo simple
→ referencia al jugador
→ rango
→ angulo
→ obstaculos
```

Ejemplo mas complejo:

```txt
Guardia de sigilo
→ rango
→ angulo
→ obstaculos
→ altura de ojos
→ sospecha
→ memoria visual
→ debug de cono
```

---

## Que produce

Field of View puede producir:

```txt
bool de visibilidad
objetivo visible actual
lista de objetivos visibles
posicion del objetivo visible
tiempo desde ultima vision
resultado de linea de vision
```

La salida debe ser usada con cuidado.

Ejemplo:

```txt
CanSeeTarget = true
```

Eso no significa automaticamente:

```txt
atacar
perseguir
alertar
cambiar de estado
```

Solo significa:

```txt
el objetivo es visible para este sensor visual
```

---

## Como funciona

Un Field of View simple suele seguir este flujo:

```txt
1. Calcular direccion hacia el objetivo.
2. Verificar distancia.
3. Verificar angulo.
4. Verificar si hay obstaculos.
5. Devolver si el objetivo es visible.
```

Flujo de descarte:

```txt
Objetivo fuera de rango
→ no visible.

Objetivo fuera de angulo
→ no visible.

Obstaculo en el medio
→ no visible.

Objetivo dentro de rango, angulo y sin obstaculos
→ visible.
```

La idea es aplicar primero chequeos baratos y despues chequeos mas caros.

```txt
distancia
→ barato

angulo
→ barato

raycast
→ mas caro
```

Regla:

```txt
Primero filtros baratos.
Despues chequeos caros.
```

---

## Ejemplo conceptual en C#

```csharp
using UnityEngine;

public class FieldOfView
{
    private readonly Transform owner;
    private readonly float viewDistance;
    private readonly float viewAngle;
    private readonly LayerMask obstacleMask;

    public FieldOfView(
        Transform owner,
        float viewDistance,
        float viewAngle,
        LayerMask obstacleMask)
    {
        this.owner = owner;
        this.viewDistance = viewDistance;
        this.viewAngle = viewAngle;
        this.obstacleMask = obstacleMask;
    }

    public bool CanSee(Transform target)
    {
        Vector3 directionToTarget = target.position - owner.position;
        float distanceToTarget = directionToTarget.magnitude;

        if (distanceToTarget > viewDistance)
        {
            return false;
        }

        Vector3 normalizedDirection = directionToTarget.normalized;
        float angleToTarget = Vector3.Angle(owner.forward, normalizedDirection);

        if (angleToTarget > viewAngle * 0.5f)
        {
            return false;
        }

        if (Physics.Raycast(owner.position, normalizedDirection, distanceToTarget, obstacleMask))
        {
            return false;
        }

        return true;
    }
}
```

Este ejemplo responde solo una pregunta:

```txt
¿Puedo ver este objetivo?
```

No cambia estados.

No ataca.

No mueve.

No calcula rutas.

---

## Como aplicarlo en videojuegos

Field of View conviene cuando la vision direccional del NPC aporta al gameplay.

Ejemplos:

```txt
guardias de sigilo
enemigos patrulleros
camaras de seguridad
animales que reaccionan visualmente
aliados que detectan enemigos
bosses que reaccionan a posicion del jugador
```

Tambien puede usarse para:

```txt
sistemas de alerta
deteccion progresiva
zonas de vision
tutoriales de sigilo
debug de percepcion
feedback visual al jugador
```

En juegos de sigilo, el Field of View puede ser una parte central del diseño.

En juegos de accion directa, tal vez alcance con deteccion por distancia.

---

## Relacion con deteccion del jugador

Field of View puede ser consumido por un sistema de deteccion del jugador.

Ejemplo:

```txt
Field of View
→ confirma si el jugador es visible.

Deteccion del jugador
→ combina vision, distancia, daño, sonido, eventos o memoria.

Decision
→ decide que hacer con esa informacion.
```

Field of View no debe reemplazar toda la deteccion.

Solo representa deteccion visual.

---

## Relacion con Line of Sight

Field of View puede usar Line of Sight como parte del chequeo de obstaculos.

```txt
Field of View
→ rango + angulo + linea de vision.

Line of Sight
→ confirma si hay vision directa entre dos puntos.
```

Line of Sight puede ser una tecnica transversal.

Puede aparecer en:

```txt
percepcion
pathfinding suavizado
Theta Star
cobertura
deteccion de disparo
visibilidad tactica
```

Por eso Field of View no debe absorber toda la teoria de Line of Sight.

Solo debe usarla como chequeo cuando corresponde.

---

## Cuando conviene implementarlo

Conviene implementar Field of View cuando:

```txt
importa hacia donde mira el NPC
el jugador puede esconderse
la deteccion visual debe ser justa
hay mecanicas de sigilo
hay camaras de seguridad
la linea de vision importa
la orientacion del NPC comunica peligro
el jugador debe poder leer el riesgo visual
```

Pregunta clave:

```txt
¿La direccion visual del NPC cambia la experiencia del jugador?
```

Si la respuesta es si, Field of View puede aportar valor.

---

## Cuando NO conviene implementarlo

No conviene implementar Field of View si:

```txt
el NPC siempre conoce al jugador por diseño
el juego no usa sigilo ni vision direccional
alcanza con rango simple
el NPC es decorativo
el NPC no toma decisiones visuales
la deteccion visual no cambia la experiencia
hay demasiados NPCs y el costo no esta justificado
```

Ejemplos:

```txt
Comerciante fijo
→ no necesita Field of View.

NPC de dialogo
→ no necesita Field of View.

Enemigo de arena que siempre ataca al jugador
→ puede no necesitar Field of View.

Torreta con trigger circular
→ puede alcanzar con rango.
```

Regla:

```txt
No usar Field of View si la direccion visual no aporta gameplay.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
usar Field of View para decidir estados
hacer raycasts cada frame sin necesidad
detectar a traves de paredes
usar el origen desde los pies del NPC
no configurar layers correctamente
hacer que el NPC vea 360 grados sin querer
no dar feedback al jugador
usar angulos enormes sin justificacion
mezclar vision con ataque
mezclar vision con movimiento
```

Ejemplo de mala practica:

```txt
El sensor visual detecta al jugador y automaticamente llama a Attack().
```

Problema:

```txt
La percepcion queda acoplada al combate.
La decision desaparece.
El comportamiento se vuelve dificil de depurar.
```

---

## Costos de implementacion

Implementar Field of View puede requerir:

```txt
calculo de distancia
calculo de angulo
raycasts
configuracion de layers
configuracion de obstaculos
debug visual
integracion con deteccion
integracion con decision
ajuste de valores por NPC
```

Tambien puede requerir decisiones de diseño:

```txt
distancia de vision
angulo justo
tiempo de deteccion
velocidad de sospecha
perdida de vision
ultima posicion conocida
feedback visual
```

El costo no es solo tecnico.

Tambien hay costo de diseño y validacion.

---

## Costos de optimizacion

El mayor costo suele venir de raycasts y chequeos frecuentes.

Riesgos comunes:

```txt
raycasts cada frame por cada NPC
chequear muchos objetivos contra muchos NPCs
usar OverlapSphere sin filtros
crear listas nuevas constantemente
dibujar gizmos siempre activos
actualizar FOV de NPCs lejanos o inactivos
buscar al jugador con FindObjectOfType
```

Alternativas:

```txt
actualizar por intervalos
chequear distancia antes de raycast
usar triggers para candidatos cercanos
cachear referencias
usar layers correctamente
limitar cantidad de chequeos por frame
desactivar FOV en NPCs inactivos
usar LOD de IA
activar debug solo en editor o por bandera
```

Regla:

```txt
No todos los NPCs necesitan chequear vision todo el tiempo.
```

---

## Criterio de optimizacion

Antes de optimizar Field of View, revisar:

```txt
cantidad de NPCs
frecuencia de chequeo
cantidad de objetivos posibles
cantidad de raycasts
distancia al jugador
si el NPC esta activo o no
si el NPC esta dentro del area relevante
si el debug esta activo en runtime
```

No optimizar antes de entender el costo real.

Pero tampoco diseñar como si hubiera un solo NPC si el juego puede tener muchos.

Criterio:

```txt
1 NPC con FOV
→ costo bajo o moderado.

100 NPCs con FOV por frame
→ posible problema.

100 NPCs con FOV por intervalos, filtros y cache
→ mucho mas controlable.
```

---

## Validacion visual

Field of View se valida mejor con feedback visual durante desarrollo.

Opciones:

```txt
gizmo de rango
gizmo de cono visual
linea hacia objetivo visible
linea bloqueada por obstaculo
color distinto si detecta
estado visible en inspector
logs temporales
```

Validar solo por comportamiento puede ser confuso.

Ejemplo:

```txt
El NPC no persigue.
```

Eso puede deberse a:

```txt
Field of View no detecta
deteccion no guarda informacion
decision no interpreta
estado no cambia
movimiento no ejecuta
```

Por eso conviene validar Field of View de forma aislada.

---

## Preguntas antes de implementarlo

Antes de implementar Field of View, preguntar:

```txt
¿El NPC necesita vision direccional?
¿La direccion visual aporta gameplay?
¿El jugador puede esconderse?
¿Hay obstaculos que deban bloquear vision?
¿Hay feedback para que el jugador entienda la deteccion?
¿La deteccion debe ser instantanea o progresiva?
¿Cuantos NPCs usaran este sistema?
¿Cada cuanto debe actualizarse?
¿Alcanza con rango simple?
¿Hace falta debug visual?
```

---

## Errores comunes

Errores comunes:

```txt
usar Field of View como sistema de decision
no separar vision de comportamiento
raycast desde una posicion incorrecta
no configurar layers
detectar a traves de paredes
detectar hacia atras
actualizar cada frame sin necesidad
no mostrar debug
no contemplar perdida de vision
hacer que todos los NPCs tengan el mismo FOV sin criterio
```

---

## Criterio para una IA

Cuando una IA trabaje con Field of View debe:

```txt
mantenerlo como tecnica de percepcion visual
no convertirlo en sistema de decision
no duplicar deteccion completa del jugador
no absorber Line of Sight como teoria general
explicar datos de entrada y salida
marcar costos si usa raycasts
proponer debug visual
indicar cuando conviene implementarlo
indicar cuando no conviene implementarlo
considerar cantidad de NPCs y frecuencia de chequeo
respetar separacion entre percepcion, decision y comportamiento
```

Regla operativa:

```txt
Field of View responde que puede ver el NPC.
No responde que debe hacer el NPC.
```

---

## Checklist

Antes de implementar Field of View, revisar:

```txt
¿El NPC necesita vision direccional?
¿La direccion visual afecta gameplay?
¿El jugador puede usar cobertura o sigilo?
¿La distancia de vision esta definida?
¿El angulo esta definido?
¿Hay capas de obstaculos?
¿El raycast sale desde una posicion correcta?
¿Se validara con gizmos?
¿Se controla la frecuencia de chequeo?
¿La decision esta separada del FOV?
¿La solucion por rango simple alcanzaba?
¿Hay riesgo de costo alto por cantidad de NPCs?
```

---

## Regla final

```txt
Field of View no hace que un NPC decida.

Solo define que puede ver.
```
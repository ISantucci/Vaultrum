## Definición

Los estados de NPC son una forma de organizar el comportamiento de una entidad en modos claros.

Un estado representa qué está haciendo el NPC en un momento determinado.

```txt
Estado
→ modo activo del NPC
→ reglas de entrada
→ comportamiento asociado
→ reglas de salida
```

Ejemplos:

```txt
Idle
Patrol
Chase
Attack
Flee
Investigate
Dead
```

Un estado no es toda la IA.

Es una forma de ordenar qué modo está activo y cómo puede cambiar.

---

## Responsabilidad

La responsabilidad de los estados de NPC es organizar el modo actual de comportamiento.

Deben responder:

```txt
¿Qué está haciendo el NPC ahora?
¿Cuándo entra a este estado?
¿Qué ejecuta mientras está activo?
¿Cuándo sale?
¿A qué estado puede cambiar?
```

Los estados ayudan a evitar condicionales mezclados.

Pero no deben absorber todos los sistemas del NPC.

---

## Estado, transición y máquina de estados

Para que un sistema de estados sea claro, conviene separar tres piezas:

```txt
Estado
→ representa el modo activo.

Transición
→ define cuándo se puede cambiar de un estado a otro.

Máquina de estados
→ administra el estado actual y ejecuta los cambios.
```

Ejemplo:

```txt
Patrol
→ estado actual.

Detectar jugador
→ condición o evento de transición.

Chase
→ próximo estado.
```

La máquina de estados no debería contener toda la lógica del NPC.

Su función principal es mantener el estado actual, ejecutar entrada/salida y permitir transiciones claras.

---

## Enter, Tick y Exit

Una forma común de estructurar estados es separar tres momentos:

```txt
Enter
→ se ejecuta al entrar al estado.

Tick
→ se ejecuta mientras el estado está activo.

Exit
→ se ejecuta al salir del estado.
```

Ejemplo:

```txt
Chase.Enter
→ preparar persecución.

Chase.Tick
→ solicitar movimiento hacia el objetivo.

Chase.Exit
→ limpiar datos temporales de persecución.
```

Esta separación evita que todo ocurra en un único bloque difícil de mantener.

---

## Eventos y transiciones

Una transición puede activarse por una condición evaluada o por un evento recibido.

Ejemplos de condiciones:

```txt
jugador visible
vida baja
objetivo en rango
ruta finalizada
tiempo agotado
```

Ejemplos de eventos:

```txt
OnPlayerDetected
OnDamageReceived
OnTargetLost
OnArrivedToDestination
OnAnimationFinished
```

Un evento no debe convertir al estado en dueño de todo el sistema.

Solo puede funcionar como señal para evaluar o disparar una transición.

Regla:

```txt
El evento informa.

La transición decide si corresponde cambiar.

La máquina de estados ejecuta el cambio.
```

---

## Qué NO debe hacer

Un sistema de estados no debe:

```txt
duplicar percepción
duplicar movimiento
duplicar ataque
calcular pathfinding completo
mezclar todos los sistemas en una clase
cambiar estados sin reglas claras
usar transiciones ocultas
convertir cada evento en lógica desordenada
```

Ejemplo incorrecto:

```txt
EnemyStateMachine
→ detecta jugador
→ calcula pathfinding
→ mueve
→ ataca
→ aplica daño
→ reproduce sonidos
→ actualiza UI
```

Ejemplo correcto:

```txt
StateMachine
→ mantiene estado actual
→ ejecuta Enter, Tick y Exit
→ permite transiciones claras

Cada estado
→ coordina un modo puntual

Otros sistemas
→ proveen percepción, movimiento, ataque o navegación
```

Regla:

```txt
El estado organiza.

No debe convertirse en todo el NPC.
```

---

## Qué problema resuelve

Los estados ayudan a ordenar NPCs con modos diferentes.

Sin estados, es común terminar con condicionales mezclados.

Ejemplo débil:

```txt
if detecto jugador
if estoy cerca
if tengo poca vida
if estaba patrullando
if estoy atacando
if perdí al jugador
```

Con estados:

```txt
Patrol
→ busca punto siguiente.

Chase
→ sigue objetivo.

Attack
→ ejecuta ataque.

Flee
→ se aleja de amenaza.
```

Esto mejora lectura, depuración y mantenimiento.

---

## Datos que necesita

Un sistema de estados puede necesitar:

```txt
estado actual
estado anterior
contexto del NPC
condiciones de entrada
condiciones de salida
referencias a comportamientos
tiempo en estado
eventos de transición
```

Cada estado puede necesitar datos propios.

Ejemplo:

```txt
PatrolState
→ ruta de patrulla.

ChaseState
→ objetivo o última posición conocida.

AttackState
→ rango, cooldown y objetivo.

FleeState
→ amenaza y distancia segura.
```

El contexto compartido debe ser claro.

No debería convertirse en una bolsa de datos sin criterio.

---

## Qué produce

Los estados pueden producir:

```txt
estado actual
transición ejecutada
estado anterior
evento de entrada
evento de salida
acción activa
```

Ejemplo:

```txt
CurrentState = Chase
PreviousState = Patrol
```

Eso no significa que el estado contenga toda la lógica.

Solo indica qué modo está activo.

---

## Cómo funciona

Un flujo común de estados es:

```txt
1. Definir estados posibles.
2. Definir estado inicial.
3. Ejecutar Enter del estado inicial.
4. Ejecutar Tick del estado actual.
5. Evaluar condiciones o eventos de transición.
6. Si corresponde cambiar, ejecutar Exit.
7. Cambiar estado.
8. Ejecutar Enter del nuevo estado.
```

Ejemplo conceptual:

```csharp
public interface IState
{
    void Enter();
    void Tick(float deltaTime);
    void Exit();
}

public class StateMachine
{
    private IState currentState;

    public void ChangeState(IState nextState)
    {
        if (currentState == nextState)
        {
            return;
        }

        currentState?.Exit();
        currentState = nextState;
        currentState?.Enter();
    }

    public void Tick(float deltaTime)
    {
        currentState?.Tick(deltaTime);
    }
}
```

Este ejemplo administra cambios de estado.

No define por sí solo detección, ataque, movimiento ni pathfinding.

---

## Cómo aplicarlo en videojuegos

Los estados convienen cuando el NPC tiene modos claramente diferenciados.

Ejemplos:

```txt
Guardia
→ patrullar
→ investigar
→ perseguir
→ atacar

Animal
→ pastar
→ huir
→ volver

Boss
→ fase 1
→ fase 2
→ vulnerable
→ muerto
```

Los estados ayudan a que cada modo tenga reglas propias.

---

## Cuándo conviene implementarlo

Conviene usar estados cuando:

```txt
el NPC tiene varios modos claros
cada modo tiene comportamiento distinto
hay transiciones importantes
se necesita depurar estado actual
hay animaciones asociadas a modos
se quiere evitar condicionales mezclados
```

Pregunta clave:

```txt
¿Puedo describir el comportamiento del NPC como modos distintos?
```

Si la respuesta es sí, estados puede aportar claridad.

---

## Cuándo NO conviene implementarlo

No conviene usar estados si:

```txt
el NPC tiene una única acción simple
el comportamiento se resuelve con una condición directa
la máquina de estados agrega más ruido que claridad
no hay transiciones reales
```

Ejemplos:

```txt
NPC que solo abre tienda
objeto interactivo
enemigo que solo avanza hacia adelante
trigger de evento
```

Regla:

```txt
No crear estados donde una condición simple alcanza.
```

---

## Riesgos comunes

Riesgos comunes al implementar estados:

```txt
tener un estado gigante que hace todo
duplicar condiciones en todos los estados
permitir transiciones desde cualquier lugar sin control
no separar Enter, Tick y Exit
meter lógica de sensores dentro de cada estado
mezclar estado con animación, movimiento y daño sin límites
crear demasiados estados pequeños sin valor
cambiar estados cada frame sin estabilidad
usar eventos sin orden ni reglas de transición
```

Ejemplo de mala práctica:

```txt
ChaseState detecta jugador, calcula ruta, ataca, anima y decide muerte.
```

Problema:

```txt
El estado deja de organizar comportamiento.

Empieza a absorber responsabilidades externas.
```

---

## Validación

Los estados se validan revisando:

```txt
estado inicial correcto
transiciones correctas
Enter se ejecuta una vez
Exit se ejecuta al salir
Tick solo corre en estado activo
no hay transiciones infinitas
el estado actual se entiende
los eventos no disparan cambios inesperados
```

Debug útil:

```txt
estado actual visible en inspector
logs temporales de transición
colores por estado
gizmos específicos por estado
historial breve de estados
```

---

## Regla final

Los estados ordenan comportamiento.

No deben convertirse en una clase monolítica disfrazada.

Un estado dice qué modo está activo.

Una transición define cuándo cambiar.

La máquina de estados ejecuta el cambio.

Primero claridad.

Después estructura.
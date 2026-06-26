## Descripción

Un `StateMachineManager` administra una máquina de estados central.

No toda state machine necesita ser un manager.

Este documento se refiere específicamente a un manager encargado de administrar estados globales o de flujo del juego.

Ejemplos:

```txt
MainMenu
LevelSelect
Loading
Playing
Paused
Win
Lose
```

---

## Qué problema resuelve

Resuelve problemas donde el juego necesita estados claros, transiciones controladas y lógica separada por estado.

Evita que el `GameManager` se llene de condicionales como:

```txt
if playing...
if paused...
if win...
if lose...
```

También evita que la lógica de entrada, salida y actualización de estados quede mezclada en una sola clase.

---

## Cuándo conviene usarlo

Conviene cuando el juego tiene:

```txt
varios estados globales,
transiciones con reglas,
pausa,
pantallas diferentes,
carga entre escenas,
victoria/derrota,
modos de juego,
estados con Enter/Exit,
lógica distinta según estado.
```

Ejemplo:

```txt
PlayingState
→ habilita gameplay.

PausedState
→ congela gameplay y muestra pausa.

WinState
→ detiene juego y muestra victoria.
```

---

## Cuándo NO conviene usarlo

No conviene si:

```txt
hay solo dos estados simples,
un boolean alcanza,
el proyecto es demasiado chico,
la state machine sería más compleja que el problema,
o se quiere usar para meter toda la lógica del juego en estados gigantes.
```

Tampoco debe usarse para reemplazar managers específicos.

---

## Responsabilidades permitidas

Puede encargarse de:

```txt
registrar estados,
mantener estado actual,
ejecutar transición,
llamar Enter,
llamar Exit,
actualizar estado actual si corresponde,
validar transiciones,
exponer estado actual,
notificar cambios de estado.
```

---

## Responsabilidades prohibidas

No debería:

```txt
hacer la UI internamente,
cargar assets directamente,
guardar partida directamente,
instanciar enemigos,
manejar audio directamente,
calcular daño,
decidir reglas internas de cada sistema,
contener toda la lógica de gameplay.
```

Los estados pueden coordinar acciones, pero no deberían convertirse en clases dios.

---

## Relación con otras piezas arquitectónicas

Relaciones comunes:

```txt
GameManager
→ solicita cambios de estado.

LevelManager
→ informa entrada o salida de nivel.

UIManager
→ reacciona a cambios de estado.

AudioManager
→ cambia música según estado.

EventQueueManager
→ puede procesar eventos diferidos por transición.
```

También se relaciona con el patrón State.

Diferencia:

```txt
State
→ patrón para encapsular comportamiento por estado.

StateMachineManager
→ administra los estados y transiciones.
```

---

## Ciclo de vida

Flujo básico:

```txt
Initialize
→ registrar estados.

ChangeState
→ salir del estado actual.

Enter nuevo estado
→ inicializar comportamiento.

Tick
→ actualizar estado actual si corresponde.

Shutdown
→ limpiar estado.
```

---

## API mínima recomendada

```csharp
public interface IStateMachineManager<TState>
{
    TState CurrentState { get; }

    void ChangeState(TState newState);
    bool CanChangeTo(TState newState);

    event Action<TState> StateChanged;
}
```

Otra opción:

```csharp
public interface IGameState
{
    void Enter();
    void Exit();
    void Tick(float deltaTime);
}
```

---

## Ejemplo aplicado a videojuegos

Flujo:

```txt
GameManager.StartGame()
→ StateMachineManager.ChangeState(Playing)

Jugador pausa
→ StateMachineManager.ChangeState(Paused)

Base destruida
→ StateMachineManager.ChangeState(Lose)

Última oleada completada
→ StateMachineManager.ChangeState(Win)
```

Cada estado se encarga de su entrada y salida.

---

## Errores comunes

```txt
hacer un estado gigante,
meter toda la UI dentro de cada estado,
usar switch enorme en vez de estados reales,
permitir transiciones inválidas,
no llamar Exit del estado anterior,
no limpiar eventos,
duplicar lógica con GameManager,
meter reglas de todos los sistemas en la state machine.
```

---

## Checklist para IA/agente

Antes de crear o modificar `StateMachineManager`:

```txt
¿El problema realmente es de estados?
¿Qué estados existen?
¿Qué transiciones son válidas?
¿Qué ocurre en Enter?
¿Qué ocurre en Exit?
¿Algún estado necesita Tick?
¿Qué lógica NO debe vivir en el estado?
¿Cómo se notifica el cambio?
¿GameManager está usando if/switch que deberían ser estados?
¿La solución no es demasiado grande para el problema?
```

---

## Regla final

`StateMachineManager` administra transiciones.

No debe absorber todo el comportamiento del juego.

```txt
Sano:
estado claro, transición clara, responsabilidades separadas.

Peligroso:
un switch gigante disfrazado de arquitectura.
```
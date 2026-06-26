## Descripción

Un `GameManager` es un manager de alto nivel encargado de coordinar el estado general de una partida o sesión de juego.

No representa “todo el juego”.

No debería ser el lugar donde terminan todas las responsabilidades difíciles de ubicar.

Su función principal es mantener una visión global mínima del flujo general y delegar responsabilidades específicas en sistemas especializados.

```txt
GameManager sano
→ coordina estado general.

GameManager peligroso
→ absorbe gameplay, UI, audio, assets, guardado, niveles y lógica específica.
```

---

## Propósito dentro de Vaultrum

Este documento define cómo diseñar o auditar un `GameManager` sin convertirlo en una clase dios.

Es uno de los managers más importantes de Vaultrum porque suele aparecer en casi todos los prototipos y también suele ser el primero en romper arquitectura.

Una IA debe tratar este manager con especial cuidado.

Regla base:

```txt
GameManager no debe ser “el juego entero”.
Debe coordinar el estado global mínimo y delegar en sistemas especializados.
```

---

## Qué problema resuelve

Un `GameManager` puede resolver problemas como:

```txt
mantener estado global de la partida,
coordinar inicio y fin de gameplay,
manejar pausa a nivel global,
coordinar victoria o derrota,
exponer estado general a otros sistemas,
notificar cambios importantes,
coordinar sistemas de alto nivel.
```

Ejemplo:

```txt
El juego necesita saber si está en:
menú,
jugando,
pausado,
victoria,
derrota.

GameManager puede coordinar ese estado
o delegarlo en una StateMachineManager.
```

---

## Cuándo conviene usarlo

Conviene usar `GameManager` cuando el proyecto necesita coordinar estado global de partida.

Casos válidos:

```txt
el juego tiene estados globales,
hay inicio y fin de partida,
hay pausa global,
hay condiciones de victoria/derrota,
hay transición entre menú y gameplay,
varios sistemas necesitan conocer el estado general,
o se necesita un punto de coordinación de alto nivel.
```

Ejemplo:

```txt
MainMenu
→ LevelSelect
→ Playing
→ Paused
→ Win
→ Lose
```

En ese caso, un `GameManager` puede coordinar el flujo general o delegarlo a una state machine.

---

## Cuándo NO conviene usarlo

No conviene usar `GameManager` para resolver cualquier problema que no tiene dueño claro.

No debería existir solo para:

```txt
tener acceso global,
evitar pasar referencias,
centralizar todo,
meter código que no se sabe dónde poner,
hacer más fácil llamar métodos desde cualquier clase,
o reemplazar sistemas especializados.
```

Mala justificación:

```txt
Lo pongo en GameManager porque es importante.
```

Mejor pregunta:

```txt
¿Esto pertenece realmente al estado global de partida?
```

Si la respuesta es no, probablemente no pertenece al `GameManager`.

---

## Responsabilidades permitidas

Puede tener responsabilidades como:

```txt
estado general de partida,
inicio de partida,
fin de partida,
pausa global,
reanudación global,
detección de victoria/derrota a alto nivel,
referencia al estado actual del juego,
emisión de eventos globales,
coordinación con LevelManager,
coordinación con StateMachineManager.
```

También puede actuar como punto de entrada de alto nivel para bootstrap si el proyecto es chico.

Ejemplo de acciones válidas:

```txt
StartGame
PauseGame
ResumeGame
EndGame
RestartGame
ReturnToMenu
```

---

## Responsabilidades prohibidas

Un `GameManager` no debería:

```txt
controlar toda la UI,
calcular daño,
crear enemigos directamente,
crear torres directamente,
manejar audio directamente,
cargar assets directamente,
guardar archivos directamente,
controlar todo el spawn,
controlar pathfinding,
actualizar HUD campo por campo,
tener referencias a todos los objetos de escena,
contener la lógica interna de cada estado.
```

Si empieza a hacer eso, deja de ser coordinador y se convierte en clase dios.

Regla:

```txt
GameManager coordina el flujo global.
No ejecuta todas las responsabilidades del juego.
```

---

## Relación con UI

La UI debería mostrar el estado del juego y capturar intención del jugador.

El `GameManager` puede exponer o emitir cambios de estado, pero no debería manipular todos los elementos visuales directamente.

Correcto:

```txt
GameManager cambia estado a Paused.
GameManager emite GamePaused.
UI escucha.
UI muestra panel de pausa.
```

Incorrecto:

```txt
GameManager activa paneles,
modifica textos,
reproduce animaciones,
cambia botones,
mueve elementos visuales.
```

Regla:

```txt
GameManager informa estado.
UI representa estado.
```

---

## Relación con eventos

El `GameManager` suele ser emisor de eventos globales.

Ejemplos:

```txt
GameStarted
GamePaused
GameResumed
GameWon
GameLost
GameStateChanged
```

También puede escuchar eventos importantes si tienen impacto global.

Ejemplo:

```txt
BaseDestroyed
→ GameManager cambia a derrota.

FinalWaveCompleted
→ GameManager cambia a victoria.
```

Cuidado:

```txt
No debe escuchar todos los eventos del juego.
Solo los que afecten al flujo global.
```

---

## Relación con StateMachineManager

Si el juego tiene varios estados globales, conviene que el `GameManager` no use `if` y `switch` gigantes.

Mejor:

```txt
GameManager
→ solicita transición.

StateMachineManager
→ administra estado actual, entrada, salida y transición.
```

Ejemplo:

```txt
GameManager.PauseGame()
→ StateMachineManager.ChangeState(Paused)
```

Regla:

```txt
GameManager puede coordinar el cambio.
StateMachineManager debería administrar la lógica de estados.
```

---

## Relación con LevelManager

El `GameManager` administra la partida o sesión.

El `LevelManager` administra el nivel actual.

Separación:

```txt
GameManager
→ estado global: jugando, pausado, victoria, derrota.

LevelManager
→ entrada, salida, reinicio y progreso del nivel.
```

Ejemplo:

```txt
GameManager inicia partida.
LevelManager carga el nivel.
GameManager pasa a estado Playing.
```

No hacer:

```txt
GameManager carga escena,
inicializa spawner,
prepara HUD,
carga assets,
resetea pools,
configura audio,
y administra objetivos.
```

Eso debe delegarse.

---

## Cuándo debe ser persistente

Puede ser persistente si su responsabilidad atraviesa varias escenas.

Ejemplos:

```txt
menú → selección de nivel → gameplay → resultado,
datos globales de sesión,
estado general del juego,
modo de juego,
perfil activo.
```

Pero si el `GameManager` solo administra una escena de gameplay, no necesariamente debe persistir.

Regla:

```txt
Persistir GameManager solo si el estado que administra sigue siendo válido entre escenas.
```

---

## Cuándo NO debe ser singleton

No debe ser singleton solo por comodidad.

Mala justificación:

```txt
Lo hago singleton así cualquiera lo llama.
```

Debe evitar singleton si:

```txt
solo se usa dentro de una escena,
puede pasarse por referencia,
el proyecto necesita múltiples contextos,
el manager tiene estado específico de nivel,
se quiere testear fácilmente,
o se está usando singleton para ocultar dependencias.
```

Regla:

```txt
GameManager puede ser singleton.
Pero debe justificarse por alcance global real, no por acceso fácil.
```

---

## Señales de que se está convirtiendo en clase dios

Alertas:

```txt
tiene referencias a casi todos los sistemas,
cada feature nueva modifica GameManager,
tiene muchos métodos públicos,
controla UI y gameplay,
controla audio y guardado,
carga assets,
crea enemigos,
tiene Update gigante,
todos llaman a GameManager.Instance,
es difícil explicar qué NO hace.
```

Señal crítica:

```txt
Si algo no tiene lugar claro, termina en GameManager.
```

---

## API mínima recomendada

Ejemplo de API mínima:

```csharp
public interface IGameManager
{
    GameState CurrentState { get; }

    void StartGame();
    void PauseGame();
    void ResumeGame();
    void EndGame(GameResult result);

    event Action<GameState> GameStateChanged;
}
```

Puede variar según el proyecto.

Evitar:

```csharp
public void SpawnEnemy();
public void PlayMusic();
public void SaveGame();
public void UpdateHealthBar();
public void LoadTowerPrefab();
public void CalculateDamage();
```

Esos métodos pertenecen a otros sistemas.

---

## Ejemplo aplicado a videojuegos

Tower Defense:

```txt
BaseHealth llega a 0.
BaseHealth emite BaseDestroyed.
GameManager recibe evento.
GameManager.EndGame(Lose).
StateMachineManager cambia a LoseState.
UI escucha GameStateChanged.
AudioManager escucha GameStateChanged.
```

El `GameManager` coordina el resultado global.

No calcula daño, no actualiza HUD y no reproduce música directamente.

---

## Ejemplo incorrecto

```txt
GameManager
→ controla vida,
→ calcula daño,
→ instancia enemigos,
→ reproduce música,
→ actualiza HUD,
→ guarda partida,
→ carga prefabs,
→ maneja pausa,
→ controla oleadas.
```

Problemas:

```txt
rompe SRP,
crea acoplamiento global,
impide testeo,
genera bugs al modificar,
crece con cada feature.
```

---

## Cómo optimizar un GameManager

Un `GameManager` no debería tener trabajo pesado por frame.

Evitar:

```txt
Update gigante,
FindObjectOfType constante,
búsquedas globales,
actualización de UI cada frame,
consultas a todos los sistemas continuamente.
```

Mejor:

```txt
eventos para cambios,
state machine para flujo,
referencias explícitas,
clases puras para cálculos,
managers especializados,
actualización solo cuando cambia el estado.
```

Regla:

```txt
GameManager optimiza cuando coordina menos trabajo,
no cuando concentra todo el trabajo.
```

---

## Checklist para IA/agente

Antes de modificar un `GameManager`, revisar:

```txt
¿La feature pertenece al estado global?
¿O pertenece a LevelManager, UIManager, AudioManager, SaveManager, AssetManager, PoolManager o StateMachineManager?
¿El cambio agrega una nueva razón para modificar GameManager?
¿La UI se está manipulando directamente?
¿Se está usando singleton por comodidad?
¿Se está agregando lógica específica de gameplay?
¿Se puede resolver con eventos?
¿Se puede delegar a un sistema especializado?
¿Se mantiene API mínima?
```

---

## Regla final

`GameManager` debe ser coordinador global, no contenedor universal.

```txt
GameManager sano
→ estado global mínimo,
→ eventos claros,
→ delegación,
→ API chica.

GameManager dios
→ todo pasa por él,
→ todo depende de él,
→ todo se rompe si cambia.
```
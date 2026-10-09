## Descripción

Un `LevelManager` administra el ciclo de vida del nivel actual.

Su responsabilidad principal es coordinar entrada, salida, reinicio y progreso del nivel sin absorber todo el gameplay.

```txt
LevelManager
→ administra el contexto del nivel.

No:
→ administra todo el juego.
```

---

## Qué problema resuelve

Resuelve problemas como:

```txt
entrar a un nivel,
salir de un nivel,
reiniciar nivel,
mantener referencia al nivel actual,
coordinar preparación de sistemas del nivel,
informar progreso,
detectar finalización del nivel,
limpiar estado temporal al salir.
```

Ejemplo:

```txt
Al entrar a Level 1:
→ cargar datos del nivel,
→ preparar spawner,
→ preparar UI de nivel,
→ limpiar eventos pendientes,
→ iniciar objetivos.
```

El `LevelManager` puede coordinar ese flujo, pero no hacer el trabajo interno de cada sistema.

---

## Cuándo conviene usarlo

Conviene cuando el juego tiene:

```txt
más de un nivel,
selección de niveles,
reinicio de nivel,
progreso por nivel,
objetivos por nivel,
escenas de gameplay separadas,
datos específicos de nivel,
sistemas que deben prepararse al entrar o salir.
```

También conviene si el `GameManager` empezó a acumular lógica de niveles.

---

## Cuándo NO conviene usarlo

No conviene si:

```txt
el juego tiene una sola escena simple,
el nivel no tiene estado propio,
no hay entrada/salida/reinicio de nivel,
solo se necesita cargar una escena,
o una clase de escena puntual alcanza.
```

Tampoco debe crearse para tapar un `GameManager` mal diseñado sin separar responsabilidades.

---

## Responsabilidades permitidas

Puede encargarse de:

```txt
identificar nivel actual,
entrar a un nivel,
salir de un nivel,
reiniciar nivel,
coordinar sistemas al cargar nivel,
coordinar limpieza al salir,
notificar LevelStarted / LevelCompleted / LevelFailed,
mantener progreso local del nivel,
validar condiciones generales de finalización.
```

---

## Responsabilidades prohibidas

No debería:

```txt
spawnear enemigos directamente si existe Spawner,
manejar audio directamente,
actualizar HUD directamente,
guardar partida directamente,
cargar assets directamente si existe AssetManager,
calcular daño,
manejar input,
controlar estados globales completos,
decidir reglas internas de todos los objetivos.
```

Regla:

```txt
LevelManager coordina el nivel.
No reemplaza todos los sistemas del nivel.
```

---

## Relación con otras piezas arquitectónicas

Relaciones comunes:

```txt
GameManager
→ estado global de partida.

StateMachineManager
→ estados como Loading, Playing, Paused, Win, Lose.

AssetManager
→ carga recursos del nivel.

UIManager
→ prepara HUD o pantallas del nivel.

Spawner
→ inicia oleadas o enemigos.

EventQueueManager
→ limpia o procesa eventos de transición.

SaveManager
→ registra progreso si corresponde.
```

El `LevelManager` puede coordinar llamadas entre estos sistemas, pero no absorber sus responsabilidades.

---

## Ciclo de vida

Métodos posibles:

```csharp
public void EnterLevel(LevelData levelData);
public void ExitLevel();
public void RestartLevel();
public void CompleteLevel();
public void FailLevel();
```

Flujo típico:

```txt
EnterLevel
→ preparar contexto.

StartLevel
→ habilitar gameplay.

CompleteLevel
→ notificar finalización.

ExitLevel
→ limpiar referencias y estado temporal.
```

---

## API mínima recomendada

```csharp
public interface ILevelManager
{
    string CurrentLevelId { get; }

    void EnterLevel(LevelData levelData);
    void ExitLevel();
    void RestartLevel();

    event Action<string> LevelEntered;
    event Action<string> LevelExited;
    event Action<string> LevelCompleted;
}
```

Evitar APIs como:

```csharp
SpawnEnemy();
PlayMusic();
UpdateHUD();
SaveProgress();
LoadPrefab();
```

A menos que el proyecto sea muy chico y esté explícitamente aceptado como deuda temporal.

---

## Ejemplo aplicado a videojuegos

Tower Defense:

```txt
LevelManager.EnterLevel(LevelData)
→ limpia estado previo,
→ solicita carga de recursos,
→ configura puntos de spawn,
→ informa a UI que entró un nivel,
→ notifica que el nivel está listo.
```

Luego:

```txt
WaveSpawner
→ maneja oleadas.

GameManager
→ estado Playing.

UIManager
→ HUD.

AudioManager
→ música.

SaveManager
→ progreso.
```

---

## Errores comunes

```txt
hacer que LevelManager cargue todo,
hacer que controle UI,
hacer que maneje spawn completo,
hacer que sea singleton sin necesidad,
no limpiar referencias al salir,
mezclar progreso global con progreso local,
duplicar responsabilidades con GameManager.
```

---

## Checklist para IA/agente

Antes de crear o modificar `LevelManager`:

```txt
¿El problema pertenece al nivel actual?
¿O pertenece al estado global del juego?
¿Debe coordinar o ejecutar?
¿Hay datos de nivel claros?
¿Hay ciclo Enter/Exit/Restart?
¿Debe persistir entre escenas?
¿Qué referencias de escena debe limpiar?
¿Qué eventos emite?
¿Qué sistemas prepara?
¿Qué responsabilidades tiene prohibidas?
```

---

## Regla final

`LevelManager` administra el contexto del nivel.

```txt
Sano:
coordina entrada, salida y progreso.

Peligroso:
se convierte en GameManager secundario.
```
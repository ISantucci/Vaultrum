## Propósito dentro de Vaultrum

Este documento define cómo pensar el ciclo de vida de un manager.

En Unity, muchos errores arquitectónicos no aparecen porque el concepto del manager sea incorrecto, sino porque no está claro cuándo se crea, cuándo se inicializa, cuándo se limpia y qué referencias conserva.

La idea principal es:

```txt
Un manager sano debe tener ciclo de vida explícito.
```

No alcanza con que exista.

Debe saberse:

```txt
quién lo crea,
quién lo inicializa,
quién lo usa,
quién lo reinicia,
quién lo limpia,
y cuándo deja de existir.
```

---

## Qué es el ciclo de vida

El ciclo de vida de un manager describe las etapas por las que pasa durante la ejecución del juego.

Etapas posibles:

```txt
Creación
Inicialización
Vinculación de dependencias
Uso
Pausa
Reinicio
Cambio de contexto
Limpieza
Destrucción
```

No todos los managers necesitan todas estas etapas.

Pero todos deberían tener claro cuáles aplican.

---

## Creación

La creación responde:

```txt
¿Cuándo aparece el manager?
¿Quién lo crea?
¿Existe desde el inicio del juego?
¿Se crea al entrar a una escena?
¿Se crea por nivel?
¿Se crea por partida?
¿Se crea por sistema?
```

Ejemplos:

```txt
AudioManager
→ puede crearse al iniciar el juego y persistir.

LevelManager
→ puede crearse por escena o por nivel.

PoolManager
→ puede crearse al entrar a gameplay y limpiarse al salir.

UIManager
→ puede existir por escena, especialmente si controla HUD específico.
```

Regla:

```txt
La forma de crear un manager debe coincidir con el alcance de su responsabilidad.
```

---

## Inicialización

Inicializar no es lo mismo que crear.

Crear significa que el objeto existe.

Inicializar significa que ya está listo para usarse.

Ejemplo:

```csharp
public void Initialize(AudioConfig config)
{
    _config = config;
    _isInitialized = true;
}
```

Preguntas:

```txt
¿Qué datos necesita para estar listo?
¿Qué dependencias necesita?
¿Puede fallar la inicialización?
¿Debe inicializarse una sola vez?
¿Puede reinicializarse?
```

Regla:

```txt
Un manager no debería aceptar llamadas importantes si todavía no fue inicializado.
```

---

## Vinculación de dependencias

Algunos managers necesitan referencias a objetos de escena.

Ejemplo:

```txt
HUD,
Canvas,
cámara,
spawn points,
contenedores de UI,
puntos de camino,
audio listeners,
objetos de escena.
```

Si el manager es persistente, estas referencias pueden cambiar cuando cambia la escena.

Por eso conviene separar:

```txt
Initialize
→ inicializa estado propio o configuración global.

BindSceneReferences
→ vincula referencias de la escena actual.

UnbindSceneReferences
→ limpia referencias de la escena actual.
```

Ejemplo:

```csharp
public void BindSceneReferences(HudView hudView)
{
    _hudView = hudView;
}

public void UnbindSceneReferences()
{
    _hudView = null;
}
```

Regla:

```txt
Estado persistente y referencias de escena no son lo mismo.
```

---

## Uso

Durante el uso, el manager recibe llamadas desde otros sistemas.

Ejemplos:

```txt
AudioManager.PlaySfx()
AssetManager.LoadAsset()
UpdateManager.Register()
LevelManager.EnterLevel()
SaveManager.SaveGame()
```

La etapa de uso debe respetar la API pública.

Los consumidores no deberían manipular internals del manager.

Regla:

```txt
Durante el uso, el manager debe proteger su propio estado.
```

Ejemplo:

```csharp
public bool TrySpendMoney(int amount)
{
    if (amount <= 0) return false;
    if (_money < amount) return false;

    _money -= amount;
    MoneyChanged?.Invoke(_money);
    return true;
}
```

No:

```csharp
public int money;
```

---

## Pausa

Algunos managers deben reaccionar a pausa.

Ejemplos:

```txt
UpdateManager
→ pausa grupos de actualización.

AudioManager
→ pausa música o sonidos.

GameManager
→ cambia estado global.

UIManager
→ muestra panel de pausa.

PoolManager
→ normalmente no necesita pausar directamente.
```

No todos los managers necesitan `Pause`.

Evitar interfaces gigantes como:

```csharp
public interface IManaged
{
    void Initialize();
    void Pause();
    void Resume();
    void Save();
    void Load();
    void Reset();
}
```

Mejor separar:

```csharp
public interface IPausable
{
    void Pause();
    void Resume();
}
```

Regla:

```txt
Solo los managers que realmente tienen comportamiento de pausa deberían implementarlo.
```

---

## Reinicio de estado

Un manager puede necesitar reiniciar estado sin destruirse.

Ejemplos:

```txt
GameManager al empezar nueva partida.
LevelManager al reiniciar nivel.
PoolManager al limpiar objetos activos.
UIManager al volver a menú.
EventQueueManager al vaciar eventos pendientes.
```

Método típico:

```csharp
public void ResetState()
{
    _score = 0;
    _isPaused = false;
}
```

Importante:

```txt
ResetState no debería reemplazar Awake.
```

No hacer:

```csharp
manager.Awake();
```

Hacer:

```csharp
manager.ResetState();
```

---

## Cambio de contexto

Muchos managers operan por contexto.

Ejemplos de contexto:

```txt
menú,
nivel,
partida,
modo de juego,
escena,
wave,
perfil de usuario,
bioma,
zona.
```

Métodos posibles:

```csharp
public void EnterLevel(LevelData data);
public void ExitLevel();
public void EnterMenu();
public void ExitMenu();
```

Esto evita que el manager tenga que adivinar en qué contexto está.

Regla:

```txt
Los cambios importantes de contexto deberían estar representados por métodos explícitos.
```

---

## Limpieza

La limpieza evita errores y memory leaks.

Puede incluir:

```txt
desuscribirse de eventos,
vaciar listas,
liberar assets,
devolver objetos al pool,
limpiar referencias de escena,
cancelar cargas pendientes,
vaciar colas,
resetear estado temporal.
```

Métodos posibles:

```csharp
public void Shutdown();
public void Clear();
public void ExitLevel();
public void UnbindSceneReferences();
```

Ejemplo:

```csharp
private void OnDisable()
{
    GameEvents.MoneyChanged -= HandleMoneyChanged;
}
```

Regla:

```txt
Todo manager que se suscribe, registra, carga o cachea algo
debe tener una estrategia de limpieza.
```

---

## Destrucción

La destrucción responde:

```txt
¿Cuándo deja de existir el manager?
¿Quién lo destruye?
¿Debe liberar recursos antes?
¿Debe avisar a otros sistemas?
¿Debe desregistrarse?
```

En Unity puede ocurrir por:

```txt
cambio de escena,
Destroy,
cierre del juego,
desactivación de GameObject,
salida de play mode.
```

Si el manager persiste con DontDestroyOnLoad, su destrucción puede no coincidir con cambio de escena.

Regla:

```txt
Persistencia explícita requiere destrucción explícita o limpieza explícita.
```

---

## Relación con Unity

Unity ya tiene su propio ciclo:

```txt
Awake
OnEnable
Start
Update
OnDisable
OnDestroy
```

Eso no reemplaza el ciclo propio del manager.

Uso recomendado:

```txt
Awake
→ preparar referencias internas mínimas.

Start
→ iniciar si todas las dependencias de escena ya están listas.

Initialize
→ inicialización explícita controlada por arquitectura.

ResetState
→ reinicio de estado.

Shutdown
→ cierre y limpieza.
```

No llamar manualmente:

```txt
Awake
Start
Update
OnEnable
OnDisable
OnDestroy
```

Regla:

```txt
Callbacks de Unity son eventos del motor.
Métodos del manager son API del sistema.
```

---

## Criterio para IA/agente

Cuando una IA diseñe o modifique un manager, debe identificar su ciclo de vida.

Formato esperado:

```txt
Manager:
...

Alcance:
global / escena / nivel / partida / sistema

Creación:
...

Inicialización:
...

Dependencias:
...

Persistencia:
...

Reset:
...

Limpieza:
...

Destrucción:
...

Riesgos:
...
```

La IA no debe asumir que todo manager es singleton o persistente.

---

## Checklist de ciclo de vida

Antes de aprobar un manager:

```txt
¿Se sabe cuándo se crea?
¿Se sabe quién lo inicializa?
¿Tiene método explícito de inicialización si hace falta?
¿Puede usarse antes de estar listo?
¿Necesita referencias de escena?
¿Limpia referencias de escena?
¿Se desuscribe de eventos?
¿Libera recursos?
¿Vacía colas o listas internas?
¿Se reinicia sin llamar Awake?
¿Sobrevive entre escenas?
¿Debe sobrevivir entre escenas?
¿Tiene estrategia para cambio de contexto?
```

---

## Regla final

Un manager sin ciclo de vida explícito se vuelve frágil.

```txt
Manager sano
→ sabe cuándo nace,
→ cuándo se inicializa,
→ cuándo trabaja,
→ cuándo limpia,
→ y cuándo muere.

Manager peligroso
→ depende del orden mágico de Unity,
→ conserva referencias viejas,
→ se reinicia llamando callbacks,
→ y falla al cambiar de escena.
```
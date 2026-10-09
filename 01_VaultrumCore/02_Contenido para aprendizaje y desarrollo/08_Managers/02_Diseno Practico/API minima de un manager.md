## Propósito dentro de Vaultrum

Este documento define cómo diseñar la API pública de un manager.

El objetivo es evitar managers con demasiados métodos, demasiados accesos directos y demasiada exposición interna.

Una API mínima permite que una IA o un desarrollador usen el manager sin conocer todos sus detalles internos.

La idea principal es:

```txt
Un manager debe exponer intención.
No debe exponer implementación.
```

---

## Qué es una API mínima

La API mínima es el conjunto más chico de métodos, propiedades o eventos públicos necesarios para que el resto del juego use el manager correctamente.

No significa que el manager tenga poca lógica interna.

Significa que desde afuera se puede interactuar con él mediante operaciones claras.

Ejemplo:

```csharp
public interface IAudioManager
{
    void PlaySfx(string id);
    void PlayMusic(string id);
    void StopMusic();
}
```

Eso expresa intención.

No expone:

```txt
listas internas,
AudioSources internos,
diccionarios,
estado mutable innecesario,
detalles de carga,
objetos temporales.
```

---

## Por qué importa

Una API pública grande crea acoplamiento.

Si muchos sistemas usan muchos métodos del manager, el manager se vuelve difícil de cambiar.

Problemas comunes:

```txt
todos dependen de detalles internos,
la clase se vuelve rígida,
cualquier cambio rompe consumidores,
la IA agrega métodos por comodidad,
se mezclan responsabilidades,
aparecen accesos globales sin control.
```

Una API mínima ayuda a:

```txt
mantener responsabilidad clara,
evitar clase dios,
reducir dependencias,
facilitar testing,
mejorar lectura,
hacer más segura la automatización con IA.
```

---

## API orientada a intención

Los métodos públicos deberían describir qué quiere hacer el consumidor, no cómo lo hace internamente el manager.

Ejemplo correcto:

```csharp
audioManager.PlaySfx("button_click");
```

Ejemplo peligroso:

```csharp
audioManager.GetAudioSource(0).clip = clip;
audioManager.GetAudioSource(0).Play();
```

El primer caso dice:

```txt
quiero reproducir un sonido.
```

El segundo caso permite manipular implementación interna.

Regla:

```txt
Un consumidor debería pedir una acción,
no operar las tripas del manager.
```

---

## Qué debería ser público

Puede ser público:

```txt
métodos que representen operaciones principales,
eventos necesarios para notificar cambios,
consultas seguras de estado,
métodos de ciclo de vida si otros sistemas deben llamarlos,
registro/desregistro si el manager administra participantes.
```

Ejemplos:

```csharp
public void Register(IUpdatable target);
public void Unregister(IUpdatable target);
public void PlayMusic(string id);
public void LoadLevel(string levelId);
public void SaveGame();
public void SetMasterVolume(float value);
```

Cada método debería pertenecer directamente a la responsabilidad central del manager.

---

## Qué NO debería ser público

No debería exponerse:

```txt
listas internas,
diccionarios internos,
referencias mutables innecesarias,
objetos de escena internos,
caches internas,
handles internos,
métodos auxiliares,
métodos de debug de uso permanente,
detalles de implementación,
métodos de otras responsabilidades.
```

Ejemplo peligroso:

```csharp
public List<GameObject> activeEnemies;
public Dictionary<string, AudioClip> audioClips;
public Transform hudRoot;
public void RecalculateDamage();
public void SpawnEnemy();
public void SaveSettings();
```

Si un manager expone demasiado, otros sistemas empiezan a depender de cosas que no deberían conocer.

---

## Métodos de ciclo de vida

Los métodos de ciclo de vida pueden ser públicos si realmente otros sistemas deben controlar el manager.

Ejemplos:

```csharp
public void Initialize();
public void Shutdown();
public void ResetState();
public void EnterLevel(LevelData data);
public void ExitLevel();
```

Pero no se deberían llamar manualmente callbacks propios de Unity.

Evitar:

```csharp
manager.Awake();
manager.Start();
manager.Update();
```

Preferir:

```csharp
manager.Initialize();
manager.ResetState();
manager.Tick(deltaTime);
```

Regla:

```txt
Los métodos públicos deben representar intención del dominio,
no callbacks internos del motor.
```

---

## Eventos como parte de la API

Los eventos también son parte de la API pública.

Ejemplo:

```csharp
public event Action<int> MoneyChanged;
public event Action<GameState> GameStateChanged;
public event Action<string> LevelLoaded;
```

Un evento público debe tener una razón clara.

No debería emitirse todo desde todos lados.

Criterio:

```txt
¿Quién necesita saber esto?
¿El evento representa un cambio real?
¿Evita acoplamiento directo?
¿Tiene un nombre claro?
¿Se sabe cuándo se dispara?
```

Eventos demasiado genéricos pueden ser peligrosos:

```csharp
public event Action<object> SomethingHappened;
```

Eso no comunica intención.

---

## Consultas de estado

A veces un manager necesita permitir consultas.

Ejemplo:

```csharp
public bool IsPaused { get; }
public int CurrentMoney { get; }
public string CurrentLevelId { get; }
```

Pero conviene evitar setters públicos innecesarios.

Malo:

```csharp
public int CurrentMoney { get; set; }
```

Mejor:

```csharp
public int CurrentMoney { get; private set; }

public bool TrySpendMoney(int amount);
public void AddMoney(int amount);
```

Regla:

```txt
Consultar estado puede ser válido.
Modificar estado debería pasar por métodos con intención y validación.
```

---

## API mínima y SOLID

La API mínima protege principalmente:

```txt
Single Responsibility Principle
→ evita métodos de responsabilidades ajenas.

Interface Segregation Principle
→ evita obligar a consumidores a depender de métodos innecesarios.

Dependency Inversion Principle
→ permite depender de contratos chicos y claros.
```

Ejemplo sano:

```csharp
public interface IAudioPlayer
{
    void PlaySfx(string id);
}
```

Un botón de UI no necesita conocer todo el AudioManager.

Solo necesita reproducir un sonido.

---

## Separar interfaces por consumidor

No todos los consumidores necesitan la misma API.

Ejemplo:

```csharp
public interface IAudioPlayer
{
    void PlaySfx(string id);
}

public interface IAudioSettings
{
    void SetMasterVolume(float value);
}

public interface IMusicController
{
    void PlayMusic(string id);
    void StopMusic();
}
```

Esto evita una interfaz gigante.

Mala interfaz:

```csharp
public interface IAudioManager
{
    void PlaySfx(string id);
    void PlayMusic(string id);
    void StopMusic();
    void SetMasterVolume(float value);
    void LoadAudioBank(string id);
    void ReleaseAudioBank(string id);
    void SaveSettings();
    void BindUI();
}
```

Regla:

```txt
Una interfaz grande suele indicar que varios consumidores están mezclados.
```

---

## Ejemplo aplicado a videojuegos

Caso: manager de niveles.

API peligrosa:

```csharp
public class LevelManager
{
    public GameObject[] enemies;
    public Canvas hud;
    public AudioSource musicSource;

    public void SpawnEnemies() {}
    public void UpdateHUD() {}
    public void PlayMusic() {}
    public void SaveProgress() {}
    public void LoadAssets() {}
}
```

Problema:

```txt
LevelManager está absorbiendo spawn, UI, audio, guardado y assets.
```

API más sana:

```csharp
public interface ILevelManager
{
    void EnterLevel(string levelId);
    void ExitCurrentLevel();
    event Action<string> LevelEntered;
    event Action<string> LevelExited;
}
```

Otros sistemas reaccionan:

```txt
AssetManager carga assets.
UIManager prepara UI.
AudioManager cambia música.
Spawner inicia oleadas.
SaveManager guarda progreso si corresponde.
```

---

## Criterio para IA/agente

Cuando una IA proponga una API de manager, debe justificar cada método público.

Formato esperado:

```txt
Método:
...

Motivo:
...

Responsabilidad a la que pertenece:
...

Consumidores esperados:
...

Por qué debe ser público:
...

Riesgo si se expone:
...
```

Si un método no puede justificarse, no debería ser público.

La IA debe evitar agregar métodos “por si acaso”.

---

## Checklist de API mínima

Antes de aprobar la API:

```txt
¿Cada método pertenece a la responsabilidad central?
¿Hay métodos de otras responsabilidades?
¿Hay setters públicos innecesarios?
¿Se exponen listas o diccionarios internos?
¿Se exponen referencias de escena sin control?
¿Los eventos tienen intención clara?
¿Hay interfaces gigantes?
¿Cada consumidor necesita realmente toda la API?
¿Se puede dividir en interfaces más chicas?
¿La API permite validar cambios de estado?
¿La API evita que otros sistemas manipulen internals?
```

---

## Regla final

Una buena API de manager no muestra todo lo que el manager sabe.

Muestra solo lo que el resto del juego necesita pedirle.

```txt
API sana
→ pequeña,
→ clara,
→ orientada a intención,
→ protegida,
→ fácil de auditar.

API peligrosa
→ grande,
→ genérica,
→ mutable,
→ mezcla responsabilidades,
→ expone implementación interna.
```
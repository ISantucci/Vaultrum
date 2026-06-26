## Propósito dentro de Vaultrum

Este documento define cómo deberían integrarse los managers con Unity.

El objetivo es evitar que un manager se vuelva una mezcla desordenada de lógica de juego, referencias de escena, callbacks del motor y código difícil de testear.

Unity facilita crear managers con MonoBehaviour, Inspector y GameObjects.

Eso es útil, pero también puede ser peligroso.

La idea principal es:

```txt
Unity debe conectar el manager con el motor.
No necesariamente contener toda la lógica del manager.
```

---

## Manager como MonoBehaviour

Un manager puede ser MonoBehaviour cuando necesita integrarse con Unity.

Ejemplos:

```txt
usar Inspector,
recibir callbacks,
usar Coroutine,
usar SceneManager,
existir como GameObject,
ser asignado en escena,
usar DontDestroyOnLoad,
referenciar objetos de escena.
```

Esto es común en Unity.

Ejemplo:

```csharp
public class AudioManager : MonoBehaviour
{
    [SerializeField] private AudioSource musicSource;

    public void PlayMusic(AudioClip clip)
    {
        musicSource.clip = clip;
        musicSource.Play();
    }
}
```

Esto puede estar bien si la responsabilidad es clara y acotada.

---

## MonoBehaviour como puente

En managers más grandes conviene separar integración Unity de lógica interna.

Ejemplo:

```txt
AudioManagerBehaviour
→ MonoBehaviour, referencias Unity, Inspector.

AudioService
→ lógica de audio.

AudioConfig
→ datos y configuración.
```

El MonoBehaviour funciona como puente.

```txt
Unity
→ MonoBehaviour
→ lógica propia del sistema
```

Esto ayuda a:

```txt
testear lógica fuera de Unity,
evitar clases gigantes,
separar datos de comportamiento,
reducir dependencia del motor,
mantener SOLID.
```

No siempre es obligatorio, pero es buen criterio cuando el manager crece.

---

## Uso del Inspector

El Inspector es útil para configurar referencias.

Puede usarse para:

```txt
AudioSources,
prefabs,
ScriptableObjects,
contenedores,
referencias de escena,
configuración visual,
listas de datos editables.
```

Pero no debería ser excusa para acoplar todo.

Mala señal:

```txt
GameManager tiene campos serializados para:
HUD,
AudioManager,
EnemySpawner,
Player,
Camera,
Canvas,
AssetLoader,
SaveSystem,
Pathfinder,
LevelSelector,
PauseMenu,
WinPanel,
LosePanel.
```

Eso puede indicar clase dios.

Regla:

```txt
Las referencias serializadas deben pertenecer a la responsabilidad del manager.
```

---

## ScriptableObjects para configuración

Los ScriptableObjects son útiles para separar configuración del manager.

Ejemplo:

```csharp
[CreateAssetMenu]
public class AudioConfig : ScriptableObject
{
    public float masterVolume;
    public float musicVolume;
    public float sfxVolume;
}
```

Esto permite que el manager no tenga valores mágicos hardcodeados.

Casos útiles:

```txt
configuración de audio,
datos de niveles,
tablas de assets,
configuración de pools,
datos de enemigos,
costos,
frecuencias,
reglas de actualización.
```

Regla:

```txt
Datos editables y lógica de administración no deberían mezclarse sin necesidad.
```

---

## Awake, Start y Update

Unity llama automáticamente a:

```txt
Awake
Start
Update
OnEnable
OnDisable
OnDestroy
```

Estos callbacks no deberían usarse como API pública.

No hacer:

```csharp
gameManager.Awake();
gameManager.Start();
```

Mejor:

```csharp
gameManager.Initialize();
gameManager.ResetState();
```

Uso recomendado:

```txt
Awake
→ preparar estado interno mínimo.

OnEnable
→ suscribirse si corresponde.

Start
→ iniciar dependencias que ya existen en escena.

Update
→ solo si realmente necesita trabajo por frame.

OnDisable
→ desuscribirse.

OnDestroy
→ limpieza final.
```

Regla:

```txt
Callbacks de Unity responden al motor.
Métodos explícitos responden a la arquitectura del juego.
```

---

## Evitar Update innecesario

No todo manager necesita Update.

Managers que podrían necesitarlo:

```txt
UpdateManager,
InputManager,
algunos sistemas de tiempo,
sistemas de carga asincrónica,
debug temporal.
```

Managers que normalmente no deberían tener Update constante:

```txt
AudioManager,
SaveManager,
AssetManager,
UIManager,
GameManager,
PoolManager.
```

Puede haber excepciones, pero deben justificarse.

Regla:

```txt
Si un manager tiene Update, debe poder explicar qué hace cada frame y por qué.
```

---

## Escenas y referencias

En Unity, las escenas se cargan y descargan.

Los objetos de escena pueden destruirse.

Un manager debe saber si sus referencias pertenecen a:

```txt
estado global,
configuración,
objetos persistentes,
objetos de escena,
objetos temporales,
objetos de nivel.
```

Riesgo:

```txt
Manager persistente conserva referencia a HUD de escena anterior.
```

Solución:

```txt
BindSceneReferences
UnbindSceneReferences
eventos de carga de escena
separar manager persistente de controladores de escena
```

Regla:

```txt
No tratar referencias de escena como si fueran globales eternas.
```

---

## DontDestroyOnLoad

DontDestroyOnLoad permite que un manager sobreviva entre escenas.

Puede ser útil para:

```txt
AudioManager,
SaveManager,
AssetManager,
GameManager,
UpdateManager.
```

Pero debe usarse con cuidado.

Riesgos:

```txt
duplicados,
referencias viejas,
estado que no se reinicia,
suscripciones duplicadas,
bugs al volver a menú,
orden de inicialización frágil.
```

Regla:

```txt
Persistir un GameObject no significa que todas sus referencias sigan siendo válidas.
```

---

## Búsquedas globales

Unity permite buscar objetos con métodos como:

```txt
FindObjectOfType
FindObjectsOfType
GameObject.Find
FindWithTag
```

Estas búsquedas pueden ser útiles en casos puntuales, pero no deberían ser la base de la arquitectura.

Problemas:

```txt
costo innecesario,
dependencias ocultas,
fragilidad por nombres/tags,
orden de escena poco claro,
difícil testing,
difícil refactor.
```

Mejor:

```txt
referencias explícitas,
Inspector,
inyección manual,
registro/desregistro,
eventos,
composition root,
contexto de escena.
```

Regla:

```txt
Buscar una vez con intención puede ser aceptable.
Buscar constantemente porque el diseño no define dependencias es mala señal.
```

---

## Managers y prefabs

Un manager puede usar prefabs si su responsabilidad lo justifica.

Ejemplo válido:

```txt
PoolManager
→ usa prefab para crear objetos reutilizables.

AssetManager
→ carga prefabs.

UIManager
→ puede instanciar paneles si su responsabilidad es gestionar UI.
```

Pero cuidado:

```txt
GameManager no debería transformarse en creador universal de prefabs.
```

Regla:

```txt
El manager solo debería instanciar prefabs si eso pertenece a su responsabilidad central.
```

---

## Relación con SOLID

La integración con Unity puede romper SOLID si todo queda dentro de MonoBehaviour.

Riesgos:

```txt
SRP:
manager mezcla lógica, escena, datos, UI y motor.

DIP:
manager depende de demasiadas clases concretas de Unity.

ISP:
expone métodos públicos para demasiados consumidores.

OCP:
cada nueva feature obliga a modificar el manager.
```

Separar MonoBehaviour como puente ayuda a mantener límites.

No hay que abstraer todo en prototipos.

Pero sí hay que evitar que Unity sea excusa para mezclar todo.

---

## Criterio para IA/agente

Cuando una IA modifique un manager en Unity, debe revisar:

```txt
¿Es MonoBehaviour?
¿Por qué necesita ser MonoBehaviour?
¿Tiene Update?
¿Qué hace en Update?
¿Usa callbacks correctamente?
¿Llama manualmente Awake/Start/Update?
¿Tiene referencias de escena?
¿Persiste entre escenas?
¿Limpia referencias?
¿Usa búsquedas globales?
¿La lógica podría moverse a clase pura?
¿Los datos podrían ser ScriptableObjects?
```

La IA no debe agregar referencias al Inspector o al singleton sin justificar por qué pertenecen a ese manager.

---

## Checklist de integración con Unity

Antes de aprobar un manager:

```txt
¿Necesita ser MonoBehaviour?
¿Puede separar lógica pura de integración Unity?
¿Usa Inspector solo para referencias coherentes?
¿Usa ScriptableObjects para configuración si corresponde?
¿Evita llamar manualmente callbacks de Unity?
¿Evita Update innecesario?
¿Tiene estrategia para referencias de escena?
¿Usa DontDestroyOnLoad solo si corresponde?
¿Evita búsquedas globales repetidas?
¿No instancia prefabs fuera de su responsabilidad?
¿Mantiene límites SOLID?
```

---

## Regla final

Unity facilita crear managers.

Pero no define automáticamente una buena arquitectura.

```txt
Manager sano en Unity
→ usa MonoBehaviour como integración,
→ define ciclo de vida explícito,
→ mantiene responsabilidades claras,
→ limpia referencias,
→ evita callbacks mal usados.

Manager peligroso en Unity
→ mezcla todo en un GameObject,
→ depende del orden mágico de escena,
→ usa singleton por comodidad,
→ retiene referencias viejas,
→ y crece con cada feature.
```
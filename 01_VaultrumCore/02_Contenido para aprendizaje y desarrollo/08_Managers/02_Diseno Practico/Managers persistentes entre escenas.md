## Propósito dentro de Vaultrum

Este documento define cómo diseñar managers que sobreviven entre escenas sin generar errores de referencias, duplicados o estado inválido.

En Unity, la persistencia entre escenas puede ser útil.

Pero también es una fuente común de bugs.

La idea principal es:

```txt
Persistir un manager no significa persistir todo lo que referencia.
```

Un manager persistente debe diferenciar entre:

```txt
estado global válido,
configuración,
servicios persistentes,
referencias de escena,
objetos temporales,
y datos que deben reiniciarse.
```

---

## Qué es un manager persistente

Un manager persistente es un manager que continúa existiendo cuando cambia la escena.

En Unity suele lograrse con:

```csharp
DontDestroyOnLoad(gameObject);
```

Puede ser útil para:

```txt
mantener música,
mantener configuración,
mantener sesión,
mantener servicios globales,
mantener datos de partida,
mantener sistemas de carga,
mantener un update central.
```

Ejemplos posibles:

```txt
AudioManager
SaveManager
AssetManager
GameManager
UpdateManager
```

No todos deben persistir siempre.

---

## Cuándo conviene persistir

Conviene persistir un manager cuando su responsabilidad atraviesa varias escenas.

Ejemplos:

```txt
AudioManager
→ música y volumen entre menú y gameplay.

SaveManager
→ datos de guardado disponibles durante todo el juego.

AssetManager
→ recursos compartidos y carga controlada.

GameManager
→ estado global de sesión si el flujo lo justifica.

UpdateManager
→ si administra sistemas globales.
```

Criterio:

```txt
Si la responsabilidad sigue siendo válida al cambiar de escena,
la persistencia puede estar justificada.
```

---

## Cuándo NO conviene persistir

No conviene persistir un manager cuando su responsabilidad pertenece a una escena o nivel específico.

Ejemplos:

```txt
HUD específico del nivel.
Spawner de una escena.
Pool exclusivo de un nivel.
Controlador de una cinemática.
Manager de puzzle local.
UI de una pantalla puntual.
```

Riesgo:

```txt
El manager queda vivo cuando su contexto ya no existe.
```

Criterio:

```txt
Si el manager depende fuertemente de objetos de una escena,
probablemente no debería persistir completo.
```

---

## Estado persistente vs referencias de escena

Este es el punto más importante.

Estado persistente:

```txt
volumen,
configuración,
perfil,
progreso,
estado global,
servicios,
datos de sesión.
```

Referencias de escena:

```txt
HUDCanvas,
botones,
spawn points,
enemigos activos,
cámara de escena,
paneles,
objetos del nivel,
waypoints,
contenedores visuales.
```

Regla:

```txt
El estado puede persistir.
Las referencias de escena deben vincularse y limpiarse con cuidado.
```

Ejemplo peligroso:

```txt
GameManager persiste.
Tiene referencia a HUD_Canvas.
Se cambia de escena.
HUD_Canvas se destruye.
GameManager intenta actualizar HUD viejo.
```

---

## Bind y Unbind de referencias

Una estrategia sana es separar inicialización global de vinculación de escena.

Ejemplo:

```csharp
public void Initialize(GameConfig config)
{
    _config = config;
}

public void BindSceneReferences(HudView hudView)
{
    _hudView = hudView;
}

public void UnbindSceneReferences()
{
    _hudView = null;
}
```

Esto permite que el manager persista sin asumir que sus referencias de escena son permanentes.

Regla:

```txt
Manager persistente
→ conserva estado global.

Scene binding
→ conserva referencias solo mientras la escena está activa.
```

---

## Evitar duplicados

Un problema común es crear duplicados de managers persistentes.

Ejemplo:

```txt
Escena MainMenu tiene AudioManager.
Escena Level1 también tiene AudioManager.
Ambos usan DontDestroyOnLoad.
Resultado: dos AudioManager.
```

Solución típica:

```csharp
private static AudioManager _instance;

private void Awake()
{
    if (_instance != null && _instance != this)
    {
        Destroy(gameObject);
        return;
    }

    _instance = this;
    DontDestroyOnLoad(gameObject);
}
```

Pero esto debe usarse con criterio.

Regla:

```txt
Evitar duplicados no justifica llenar el proyecto de singletons sin diseño.
```

---

## Reinicio de estado

Persistir un manager no significa que nunca se reinicie.

Ejemplos:

```txt
GameManager puede persistir,
pero debe resetear score al comenzar nueva partida.

EventQueueManager puede persistir,
pero debe limpiar eventos pendientes al salir del gameplay.

PoolManager puede persistir,
pero debe devolver o limpiar objetos al cambiar nivel.

UIManager puede persistir,
pero debe soltar referencias de paneles destruidos.
```

Métodos útiles:

```txt
ResetState
ClearRuntimeData
ExitLevel
EnterLevel
Shutdown
```

Regla:

```txt
Persistencia y reset no son opuestos.
Un manager puede sobrevivir y aun así limpiar estado temporal.
```

---

## Suscripciones a eventos

Los managers persistentes pueden quedar suscriptos a eventos de objetos destruidos o escenas anteriores.

Riesgos:

```txt
callbacks duplicados,
memory leaks,
errores por referencias nulas,
acciones repetidas,
listeners viejos.
```

Regla:

```txt
Si un manager se suscribe a eventos de escena,
debe desuscribirse al salir de esa escena.
```

Ejemplo:

```csharp
public void BindSceneReferences(HudView hud)
{
    _hud = hud;
    _hud.ButtonClicked += HandleButtonClicked;
}

public void UnbindSceneReferences()
{
    if (_hud != null)
    {
        _hud.ButtonClicked -= HandleButtonClicked;
        _hud = null;
    }
}
```

---

## SceneManager y rebind

Unity permite escuchar cambios de escena.

Ejemplo:

```csharp
SceneManager.sceneLoaded += HandleSceneLoaded;
```

Esto puede usarse para rebind controlado.

Pero no debe ser excusa para buscar todo de forma global sin criterio.

Mejor:

```txt
al cargar escena,
un SceneContext registra referencias necesarias,
el manager recibe BindSceneReferences,
se limpian referencias anteriores.
```

Criterio:

```txt
Rebind controlado
→ sano.

FindObjectOfType masivo en cada escena
→ señal de diseño frágil.
```

---

## Relación con SOLID

La persistencia puede romper SOLID si el manager empieza a absorber responsabilidades para justificar que “ya está vivo”.

Riesgos:

```txt
SRP:
manager persistente empieza a manejar UI, audio, gameplay y escenas.

DIP:
depende de objetos concretos de muchas escenas.

ISP:
expone métodos para todos los contextos.

OCP:
cada escena nueva obliga a modificar el manager.
```

Regla:

```txt
Un manager persistente debe tener límites incluso más claros que uno de escena.
```

---

## Criterio para IA/agente

Cuando una IA analice un manager persistente, debe responder:

```txt
¿Por qué debe persistir?
¿Qué estado conserva?
¿Qué referencias de escena conserva?
¿Cómo limpia referencias?
¿Cómo evita duplicados?
¿Cómo se reinicia?
¿Qué pasa al volver al menú?
¿Qué pasa al recargar nivel?
¿Qué eventos escucha?
¿Cómo se desuscribe?
```

Si la IA propone DontDestroyOnLoad, debe justificarlo.

No debería agregar persistencia por costumbre.

---

## Checklist de manager persistente

Antes de hacer persistente un manager:

```txt
¿La responsabilidad atraviesa varias escenas?
¿Se definió qué estado persiste?
¿Se definió qué referencias NO deben persistir?
¿Hay estrategia para evitar duplicados?
¿Hay ResetState?
¿Hay BindSceneReferences?
¿Hay UnbindSceneReferences?
¿Se limpian eventos?
¿Se liberan recursos?
¿Se controla qué pasa al volver al menú?
¿Se controla qué pasa al reiniciar partida?
¿No se está usando persistencia para tapar acoplamiento?
```

---

## Regla final

La persistencia es una herramienta, no una solución automática.

```txt
Manager persistente sano
→ conserva estado válido,
→ limpia referencias de escena,
→ evita duplicados,
→ reinicia datos temporales,
→ respeta límites.

Manager persistente peligroso
→ sobrevive con referencias viejas,
→ acumula estado,
→ se duplica,
→ escucha eventos antiguos,
→ y rompe al cambiar de escena.
```
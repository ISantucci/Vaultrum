## Propósito dentro de Vaultrum

Este documento define cómo mantener un manager alineado con SOLID mientras el proyecto crece.

Los managers son especialmente propensos a romper SOLID porque suelen estar en el centro de varios sistemas.

La idea principal es:

```txt
Mientras más central es un manager,
más estrictos deben ser sus límites.
```

Un manager sano no solo funciona.

También debe poder crecer sin convertirse en clase dios.

---

## Single Responsibility Principle

Un manager debe tener una responsabilidad central clara.

La pregunta principal es:

```txt
¿Por qué razones puede cambiar este manager?
```

Ejemplo sano:

```txt
AssetManager cambia si cambia:
→ la forma de cargar assets,
→ la forma de cachearlos,
→ la forma de liberarlos.
```

Ejemplo peligroso:

```txt
GameManager cambia si cambia:
→ UI,
→ audio,
→ guardado,
→ spawn,
→ economía,
→ daño,
→ pathfinding,
→ niveles,
→ assets.
```

Eso indica demasiadas razones para cambiar.

Regla:

```txt
Un manager puede coordinar sistemas.
No debe absorber sus responsabilidades.
```

---

## Open/Closed Principle

Un manager debería poder extenderse sin modificar constantemente su núcleo.

Ejemplo sano:

```csharp
public interface IUpdatable
{
    void Tick(float deltaTime);
}
```

El UpdateManager puede registrar cualquier `IUpdatable` sin saber si es enemigo, torre, clima o sistema de tutorial.

```txt
Nuevo sistema actualizable
→ implementa IUpdatable
→ se registra
→ UpdateManager no cambia.
```

Ejemplo peligroso:

```csharp
if (target is Enemy) { ... }
else if (target is Tower) { ... }
else if (target is Projectile) { ... }
else if (target is TutorialSystem) { ... }
```

Eso indica que el manager necesita modificarse cada vez que aparece un tipo nuevo.

Regla:

```txt
Si cada feature obliga a editar el manager,
el manager no está bien cerrado a modificación.
```

---

## Liskov Substitution Principle

Si un manager trabaja con abstracciones, cualquier implementación debería poder usarse sin romper expectativas.

Ejemplo:

```csharp
public interface IPausable
{
    void Pause();
    void Resume();
}
```

Todo objeto registrado como `IPausable` debería poder pausarse y resumirse sin casos especiales.

Mala señal:

```txt
Este IPausable no puede pausarse si está en tutorial.
Este otro solo puede resumirse si hay UI activa.
Este otro lanza error si no hay escena cargada.
```

Cuando aparecen muchas excepciones, la abstracción puede estar mal diseñada.

Regla:

```txt
Una abstracción usada por un manager debe tener un contrato claro y estable.
```

---

## Interface Segregation Principle

Un manager no debería obligar a otros sistemas a depender de una interfaz gigante.

Ejemplo peligroso:

```csharp
public interface IManagedSystem
{
    void Initialize();
    void Shutdown();
    void Tick(float deltaTime);
    void Pause();
    void Resume();
    void Save();
    void Load();
    void BindUI();
    void PlayAudio();
}
```

No todos los sistemas necesitan todo eso.

Mejor:

```csharp
public interface IInitializable
{
    void Initialize();
}

public interface IShutdownable
{
    void Shutdown();
}

public interface IUpdatable
{
    void Tick(float deltaTime);
}

public interface IPausable
{
    void Pause();
    void Resume();
}
```

Regla:

```txt
Interfaces chicas permiten dependencias más precisas.
Interfaces gigantes generan acoplamiento innecesario.
```

---

## Dependency Inversion Principle

Un manager no debería depender de demasiadas implementaciones concretas si eso vuelve rígido el sistema.

Ejemplo frágil:

```txt
GameManager depende directamente de:
HUDCanvas,
ConcreteEnemySpawner,
ConcreteAudioManager,
SpecificSaveSystem,
Level1SceneController,
ConcreteAssetLoader.
```

Ejemplo más sano:

```txt
GameManager coordina estado global.
Los cambios se notifican por eventos.
Las dependencias críticas se reciben por interfaces o referencias explícitas controladas.
```

No hace falta abstraer todo.

En prototipos, demasiada abstracción puede frenar.

Pero si un manager empieza a conocer detalles concretos de muchos sistemas, se vuelve difícil de modificar.

Regla:

```txt
Abstraer cuando reduce acoplamiento real.
No abstraer por decoración.
```

---

## Cómo auditar SRP en un manager

Para auditar responsabilidad única, listar métodos y campos.

Ejemplo:

```txt
GameManager:
- StartLevel
- SpawnEnemy
- PlayMusic
- SaveGame
- UpdateHUD
- CalculateDamage
- LoadTowerPrefab
- PauseGame
```

Responsabilidades detectadas:

```txt
nivel,
spawn,
audio,
guardado,
UI,
daño,
assets,
estado.
```

Esto indica que el manager tiene demasiadas razones para cambiar.

Salida esperada:

```txt
extraer AudioManager,
extraer SaveManager,
extraer LevelManager,
extraer DamageSystem,
extraer AssetManager,
delegar UI a UIManager o eventos.
```

---

## Cómo auditar OCP

Preguntar:

```txt
¿Cada nuevo tipo obliga a modificar el manager?
¿Hay muchos if por tipo concreto?
¿Hay switch enormes por enum?
¿Se puede registrar comportamiento externo?
¿Se pueden usar interfaces o data-driven design?
```

Ejemplo peligroso:

```csharp
switch (enemyType)
{
    case EnemyType.Fast:
        ...
        break;
    case EnemyType.Tank:
        ...
        break;
}
```

Puede estar bien en casos simples.

Pero si crece demasiado, tal vez corresponde Factory, Strategy o Type Object.

---

## Cómo auditar ISP

Preguntar:

```txt
¿Los consumidores usan toda la interfaz?
¿Hay métodos que solo usa un sistema?
¿La interfaz mezcla inicialización, update, UI, guardado y audio?
¿Se puede dividir en contratos más chicos?
```

Regla:

```txt
Un consumidor no debería depender de métodos que no necesita.
```

---

## Cómo auditar DIP

Preguntar:

```txt
¿El manager conoce demasiadas clases concretas?
¿Es difícil reemplazar un sistema?
¿Depende de objetos de escena específicos?
¿Usa búsquedas globales para encontrar dependencias?
¿Sería posible testearlo sin escena completa?
```

No toda dependencia concreta está mal.

Pero demasiadas dependencias concretas en un manager central son una señal de riesgo.

---

## SOLID y Unity

Unity empuja a usar MonoBehaviour, Inspector y referencias directas.

Eso no está mal.

Pero hay que mantener límites.

Ejemplo sano:

```txt
MonoBehaviour
→ recibe referencias de Unity.

Clase interna o servicio
→ contiene lógica.

ScriptableObject
→ contiene datos.

Eventos
→ comunican cambios.
```

Ejemplo peligroso:

```txt
Un MonoBehaviour Manager con:
Update gigante,
listas públicas,
referencias a todo,
lógica de UI,
lógica de gameplay,
lógica de assets,
lógica de guardado.
```

Regla:

```txt
Usar Unity no elimina la necesidad de diseño.
```

---

## Criterio para IA/agente

Cuando una IA analice un manager desde SOLID, debe responder:

```txt
Responsabilidad central:
...

Razones para cambiar:
...

Posibles violaciones SRP:
...

Posibles violaciones OCP:
...

Interfaces demasiado grandes:
...

Dependencias concretas riesgosas:
...

Refactor incremental sugerido:
...
```

La IA no debe decir solo:

```txt
“Esto viola SOLID.”
```

Debe explicar qué principio, por qué, y qué cambio concreto propone.

---

## Checklist SOLID para Managers

```txt
¿La responsabilidad central está clara?
¿Tiene pocas razones para cambiar?
¿Cada método pertenece a esa responsabilidad?
¿Cada nueva feature obliga a modificarlo?
¿Tiene if/switch crecientes por tipo?
¿Usa interfaces chicas cuando corresponde?
¿Evita interfaces gigantes?
¿Depende de demasiadas clases concretas?
¿Conoce detalles internos de otros sistemas?
¿Puede delegar en Factory, Pool, State Machine, Event Queue o clases puras?
¿Puede testearse parcialmente sin escena completa?
¿Tiene responsabilidades prohibidas documentadas?
```

---

## Regla final

SOLID en managers no significa llenar todo de interfaces.

Significa proteger límites.

```txt
Manager SOLID
→ responsabilidad clara,
→ API mínima,
→ dependencias controladas,
→ extensibilidad razonable,
→ límites explícitos.

Manager no SOLID
→ crece con cada feature,
→ depende de todo,
→ expone todo,
→ y cambia por demasiadas razones.
```
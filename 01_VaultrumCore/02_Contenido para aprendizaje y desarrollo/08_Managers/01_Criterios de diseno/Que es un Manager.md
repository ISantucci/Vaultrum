# Qué es un Manager

## Propósito dentro de Vaultrum

Este documento define qué se entiende por `Manager` dentro de Vaultrum.

No busca explicar managers como una receta genérica, sino establecer un criterio práctico para que una persona o una IA pueda decidir cuándo una clase debería ser un manager y cuándo no.

En Vaultrum, un manager debe entenderse como una pieza arquitectónica con responsabilidad clara, no como un contenedor de código suelto.

La idea principal es:

```txt
Manager
→ administra una responsabilidad central, transversal o compartida
→ con límites claros
→ con una API mínima
→ con ciclo de vida definido
```

Un manager no existe para guardar todo lo que no sabemos dónde poner.

---

## Definición

Un manager es una clase o sistema encargado de administrar una responsabilidad específica dentro del juego.

Puede administrar:

```txt
estado,
recursos,
flujo,
eventos,
actualizaciones,
niveles,
audio,
UI,
guardado,
pools,
assets,
servicios compartidos,
o ciclo de vida de otros sistemas.
```

Pero debe hacerlo dentro de un límite claro.

Ejemplo:

```txt
AssetManager
→ administra carga, acceso, cache y liberación de assets.

UpdateManager
→ administra actualizaciones registradas y frecuencia de ejecución.

AudioManager
→ administra reproducción de música, sonidos y configuración de audio.

SaveManager
→ administra guardado y carga de datos persistentes.
```

Un manager sano tiene una razón concreta para existir.

---

## Qué problema resuelve un Manager

Un manager resuelve problemas de coordinación, acceso o ciclo de vida cuando una responsabilidad aparece de forma transversal en el proyecto.

Ejemplos de problemas que pueden justificar un manager:

```txt
Muchos sistemas necesitan acceder a los mismos recursos.
Un recurso debe cargarse, reutilizarse o liberarse de forma controlada.
Un sistema debe sobrevivir entre escenas.
Varias clases necesitan coordinarse alrededor de un estado global limitado.
Muchas actualizaciones deben centralizarse o regularse.
Hay que evitar lógica duplicada en varios objetos.
Hay que ordenar el flujo de juego, niveles o estados.
```

Ejemplo:

```txt
Problema:
Cada sistema carga sus propios assets de forma distinta.

Posible solución:
AssetManager.

Responsabilidad:
centralizar carga, cache y liberación de assets.
```

Otro ejemplo:

```txt
Problema:
Hay muchos objetos con Update ejecutando lógica por frame sin control.

Posible solución:
UpdateManager.

Responsabilidad:
centralizar y controlar actualizaciones registradas.
```

---

## Qué NO debería resolver un Manager

Un manager no debería resolver problemas de diseño mal definidos.

No debería crearse solo porque:

```txt
no sé dónde poner este código,
quiero acceder fácil desde cualquier lado,
quiero evitar pasar referencias,
quiero juntar toda la lógica del juego,
quiero tener un singleton para todo,
o la clase actual se volvió grande.
```

Si una clase creció demasiado, la primera pregunta no debería ser:

```txt
¿Cómo creo un manager para esto?
```

La primera pregunta debería ser:

```txt
¿Qué responsabilidades están mezcladas?
```

Un manager mal usado suele tapar problemas de diseño en lugar de resolverlos.

---

## Diferencia entre Manager y clase común

Una clase común puede representar una entidad, una regla, un cálculo, una estrategia o un comportamiento puntual.

Un manager administra algo más amplio.

Ejemplo de clase común:

```txt
DamageCalculator
→ calcula daño.

TargetSelector
→ elige objetivo.

EnemyBrain
→ decide comportamiento de un enemigo.

UpgradeCostCalculator
→ calcula costo de mejora.
```

Ejemplo de manager:

```txt
GameManager
→ administra estado global de partida.

AudioManager
→ administra reproducción de audio.

AssetManager
→ administra acceso a assets.

PoolManager
→ administra objetos reutilizables.
```

Criterio:

```txt
Clase común
→ ejecuta una responsabilidad puntual.

Manager
→ administra el ciclo, acceso o coordinación de una responsabilidad compartida.
```

---

## Diferencia entre Manager y Singleton

Un manager puede implementarse como singleton, pero no son lo mismo.

```txt
Manager
→ rol arquitectónico.

Singleton
→ forma de acceso / restricción de instancia.
```

Ejemplo:

```txt
AudioManager
→ manager de audio.

AudioManager.Instance
→ implementación tipo singleton.
```

El peligro es pensar que todo manager debe ser singleton.

No siempre hace falta.

Un manager puede ser:

```txt
inyectado por referencia,
asignado por Inspector,
creado por un composition root,
parte de una escena,
parte de un contexto de nivel,
o persistente entre escenas.
```

Regla:

```txt
Ser manager no justifica automáticamente ser singleton.
Ser singleton no convierte una clase en manager.
```

---

## Diferencia entre Manager y otras piezas arquitectónicas

Un manager no debe confundirse con otras piezas.

```txt
Factory
→ crea objetos.

Facade
→ simplifica acceso a subsistemas.

Object Pool
→ reutiliza objetos.

State Machine
→ organiza estados y transiciones.

Service Locator
→ localiza servicios.

Command Invoker
→ ejecuta comandos.

Event Queue
→ encola y procesa eventos.

Repository / Registry
→ guarda y permite consultar datos o entidades.
```

Un manager puede usar estas piezas, pero no debería reemplazarlas todas.

Ejemplo correcto:

```txt
AssetManager
→ provee prefabs.

EnemyFactory
→ crea enemigos.

PoolManager
→ reutiliza enemigos.

Spawner
→ decide cuándo aparecen.

GameManager
→ coordina estado general de partida.
```

Ejemplo incorrecto:

```txt
GameManager
→ carga assets,
→ crea enemigos,
→ decide oleadas,
→ maneja UI,
→ reproduce audio,
→ guarda partida,
→ procesa input,
→ calcula daño.
```

Eso no es un manager sano.

Es una clase dios.

---

## Qué características tiene un Manager sano

Un manager sano suele tener estas características:

```txt
Responsabilidad concreta.
Nombre claro.
API pública pequeña.
Ciclo de vida definido.
Dependencias explícitas.
Bajo conocimiento de detalles internos de otros sistemas.
Eventos claros si necesita notificar cambios.
Pocas razones para cambiar.
Límites bien documentados.
```

También debería poder responder:

```txt
¿Qué administra?
¿Qué no administra?
¿Quién lo inicializa?
¿Quién lo usa?
¿Cuándo se limpia?
¿Sobrevive entre escenas?
¿Qué eventos emite?
¿Qué sistemas dependen de él?
```

Si esas preguntas no se pueden responder, el manager todavía no está bien definido.

---

## Relación con SOLID

Un manager debe respetar SOLID con especial cuidado, porque por naturaleza tiende a centralizar responsabilidades.

Eso lo vuelve útil, pero también peligroso.

La relación principal es con S - Single Responsibility Principle.

Un manager sano debería tener una sola razón principal para cambiar.

Ejemplo correcto:

```txt
AssetManager cambia cuando:
→ cambia la forma de cargar assets,
→ cambia la forma de cachearlos,
→ cambia la forma de liberarlos.

No cambia cuando:
→ cambia el daño de un enemigo,
→ cambia la UI,
→ cambia el sistema de oleadas,
→ cambia el guardado de partida.
```

Ejemplo incorrecto:

```txt
GameManager cambia cuando:
→ cambia la UI,
→ cambia el audio,
→ cambia el guardado,
→ cambia el spawn,
→ cambia la economía,
→ cambia el daño,
→ cambia el pathfinding,
→ cambia la selección de niveles.
```

Eso indica que el manager está acumulando demasiadas razones para cambiar.

---

### Single Responsibility Principle

Un manager debe administrar una responsabilidad central clara.

```txt
Correcto:
AudioManager
→ administra reproducción y configuración de audio.

Incorrecto:
AudioManager
→ reproduce audio,
→ cambia escenas,
→ guarda opciones,
→ muestra UI,
→ pausa el juego.
```

La pregunta clave es:

```txt
¿Por qué razones puede cambiar este manager?
```

Si la respuesta tiene demasiadas áreas distintas, el manager está violando SRP.

---

### Open/Closed Principle

Un manager debería permitir agregar variantes sin modificar constantemente su núcleo.

Ejemplo:

```txt
UpdateManager
→ permite registrar nuevos IUpdatable.

No necesita modificarse cada vez que aparece:
→ EnemyUpdater,
→ TowerUpdater,
→ ProjectileUpdater,
→ WeatherUpdater.
```

El manager se mantiene cerrado a modificaciones internas frecuentes, pero abierto a extensión mediante abstracciones.

---

### Liskov Substitution Principle

Si el manager trabaja con abstracciones, esas abstracciones deben poder reemplazarse sin romper el comportamiento esperado.

Ejemplo:

```csharp
public interface IUpdatable
{
    void Tick(float deltaTime);
}
```

Cualquier clase registrada como `IUpdatable` debería poder ejecutarse desde el `UpdateManager` sin requerir casos especiales raros.

Mala señal:

```txt
Si es Enemy, actualizar así.
Si es Tower, actualizar distinto.
Si es Projectile, hacer excepción.
Si es UI, ignorar a veces.
```

Cuando aparecen demasiadas excepciones, tal vez la abstracción está mal diseñada.

---

### Interface Segregation Principle

Un manager no debería obligar a otros sistemas a depender de interfaces gigantes.

Ejemplo incorrecto:

```csharp
public interface IGameManaged
{
    void Tick(float deltaTime);
    void Pause();
    void Resume();
    void Save();
    void Load();
    void Reset();
    void BindUI();
    void PlayAudio();
}
```

No todos los sistemas necesitan todo eso.

Mejor:

```csharp
public interface IUpdatable
{
    void Tick(float deltaTime);
}

public interface IPausable
{
    void Pause();
    void Resume();
}

public interface IResettable
{
    void ResetState();
}
```

La regla es:

```txt
Interfaces chicas
→ dependencias más claras.

Interfaces gigantes
→ acoplamiento innecesario.
```

---

### Dependency Inversion Principle

Un manager no debería depender siempre de implementaciones concretas si eso lo vuelve rígido.

Ejemplo frágil:

```txt
GameManager
→ depende directamente de HUDCanvas,
→ depende directamente de EnemySpawnerConcrete,
→ depende directamente de AudioSource específico,
→ depende directamente de una escena concreta.
```

Ejemplo más sano:

```txt
GameManager
→ coordina estado global,
→ emite eventos,
→ usa interfaces cuando corresponde,
→ no necesita conocer detalles visuales internos.
```

En Unity no siempre hace falta abstraer todo, especialmente en prototipos.

Pero si un manager empieza a depender de demasiadas clases concretas, se vuelve difícil de modificar, testear y reutilizar.

---

## Regla SOLID para Managers

Un manager puede coordinar sistemas, pero no debería absorber sus responsabilidades.

```txt
Coordinar
→ válido.

Hacer todo
→ peligroso.
```

Checklist SOLID rápido:

```txt
¿Tiene una sola responsabilidad central?
¿Tiene pocas razones para cambiar?
¿Su API pública es mínima?
¿Depende de abstracciones cuando realmente conviene?
¿Evita interfaces gigantes?
¿Evita conocer detalles internos de demasiados sistemas?
¿Permite extender comportamiento sin modificarlo todo?
```

Regla final:

```txt
Mientras más central sea un manager,
más estrictos deben ser sus límites.
```

---

## Qué características tiene un Manager peligroso

Un manager peligroso suele presentar estas señales:

```txt
Tiene demasiadas responsabilidades.
Todos los sistemas dependen de él.
Tiene muchos métodos públicos.
Tiene referencias a casi todo el proyecto.
Maneja UI, gameplay, audio, assets y escenas al mismo tiempo.
Tiene un Update gigante.
Usa muchas búsquedas globales.
Retiene referencias de escenas anteriores.
Crece cada vez que aparece una feature nueva.
Es difícil de testear.
Es difícil de modificar sin romper algo.
```

Señal crítica:

```txt
Cada vez que no sabemos dónde poner algo,
lo agregamos al manager.
```

Cuando eso pasa, el manager dejó de ser una solución y se volvió un problema.

---

## Cuándo una IA debería proponer un Manager

Una IA debería proponer un manager solo si puede justificar una responsabilidad clara.

Antes de proponerlo, debería responder:

```txt
¿Qué problema detecté?
¿Qué responsabilidad está dispersa o duplicada?
¿Por qué una clase común no alcanza?
¿Por qué no corresponde Factory, Facade, Pool, Strategy, Event Queue o State Machine?
¿Qué va a administrar exactamente?
¿Qué no va a administrar?
¿Qué API mínima necesita?
¿Qué ciclo de vida tendrá?
¿Qué riesgos introduce?
```

Ejemplo de justificación válida:

```txt
Detecté que la carga de assets está repetida en varias clases.
No corresponde a Factory porque no se trata solo de crear objetos.
No corresponde a Facade porque también hay que administrar cache y liberación.
Propongo AssetManager para centralizar carga, cache y release de assets.
No debe instanciar enemigos ni decidir gameplay.
```

Ejemplo de justificación débil:

```txt
Voy a crear un GameManager para ordenar el proyecto.
```

Eso no alcanza.

---

## Cuándo una IA NO debería proponer un Manager

Una IA no debería proponer un manager cuando:

```txt
la responsabilidad no está clara,
el problema se resuelve con una clase simple,
el sistema solo necesita una Factory,
el problema es de eventos,
el problema es de estado y corresponde una State Machine,
el problema es de reutilización y corresponde un Pool,
el problema es de acceso simple y corresponde una referencia explícita,
o todavía no hay evidencia de que haga falta centralizar.
```

Regla:

```txt
No crear managers por prevención abstracta.
Crear managers por necesidad concreta.
```

---

## Ejemplo aplicado a videojuegos

Supongamos un juego con enemigos, torres, proyectiles, UI y niveles.

Una mala distribución sería:

```txt
GameManager
→ crea enemigos
→ mueve enemigos
→ calcula daño
→ actualiza UI
→ reproduce sonidos
→ carga assets
→ maneja niveles
→ guarda partida
→ controla input
```

Una distribución más sana:

```txt
GameManager
→ coordina estado general de partida.

LevelManager
→ administra carga y progreso del nivel.

EnemyFactory
→ crea enemigos.

PoolManager
→ reutiliza proyectiles.

UIManager
→ coordina pantallas y paneles.

AudioManager
→ reproduce audio.

AssetManager
→ carga y libera assets.

StateMachineManager
→ administra estados del juego.

EventQueueManager
→ procesa eventos diferidos.
```

Cada pieza tiene una responsabilidad clara.

---

## Checklist para IA/agente

Antes de crear o modificar un manager, revisar:

```txt
¿Existe un problema concreto?
¿La responsabilidad está clara?
¿La responsabilidad es central, transversal o compartida?
¿Hay lógica duplicada que conviene centralizar?
¿Hay ciclo de vida que administrar?
¿Hay recursos compartidos?
¿Hay estado global limitado?
¿Se evaluaron alternativas arquitectónicas?
¿La API pública puede ser pequeña?
¿Se definió qué NO debe hacer?
¿Se definió cómo se inicializa?
¿Se definió cómo se limpia?
¿Se definió si persiste entre escenas?
¿Se identificaron riesgos de clase dios?
¿Se puede validar el cambio?
```

---

## Regla final

Un manager no es una bolsa de código.

Un manager es una pieza de administración con límites claros.

```txt
Manager sano
→ administra una responsabilidad concreta.

Manager peligroso
→ absorbe responsabilidades sin criterio.
```

La pregunta principal no es:

```txt
¿Puedo crear un manager?
```

La pregunta correcta es:

```txt
¿Qué responsabilidad necesita ser administrada,
y por qué un manager es la mejor forma de hacerlo?
```
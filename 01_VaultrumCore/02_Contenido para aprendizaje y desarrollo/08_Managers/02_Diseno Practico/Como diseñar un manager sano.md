## Propósito dentro de Vaultrum

Este documento define cómo transformar una necesidad arquitectónica en un manager bien diseñado.

No busca explicar managers como concepto general. Este documento responde otra pregunta:

```txt
Ya detecté que puede hacer falta un manager.
¿Cómo lo diseño sin crear una clase dios?
```

El objetivo es que una persona o una IA pueda diseñar un manager con:

```txt
responsabilidad clara,
límites explícitos,
API mínima,
ciclo de vida definido,
integración controlada con Unity,
y bajo riesgo de sobrearquitectura.
```

Un manager sano no aparece porque el proyecto está desordenado.

Aparece porque existe una responsabilidad que necesita ser administrada.

---

## Punto de partida

Antes de diseñar un manager, debe existir una justificación clara.

No alcanza con decir:

```txt
Necesitamos ordenar el sistema.
```

La justificación mínima debería ser:

```txt
Hay una responsabilidad concreta.
Está repetida, dispersa o necesita coordinación.
Tiene ciclo de vida, estado o acceso compartido.
No corresponde mejor a Factory, Facade, Pool, Event Queue, State Machine o clase pura.
```

Ejemplo válido:

```txt
La carga de assets está repetida en varios sistemas.
Además, algunos assets necesitan cache y liberación controlada.
Esto justifica evaluar un AssetManager.
```

Ejemplo débil:

```txt
Voy a crear un Manager para manejar mejor los assets.
```

La diferencia es que el primer caso explica el problema real.

---

## Paso 1: Definir la responsabilidad central

El primer paso es definir qué administra el manager.

Debe poder escribirse en una sola frase.

Ejemplos:

```txt
AssetManager
→ administra carga, cache y liberación de assets.

UpdateManager
→ administra registro y ejecución controlada de actualizaciones.

AudioManager
→ administra reproducción y configuración de audio.

LevelManager
→ administra entrada, salida y progreso del nivel actual.

SaveManager
→ administra guardado y carga de datos persistentes.
```

Si la frase necesita incluir muchas responsabilidades distintas, probablemente el manager está mal planteado.

Mala definición:

```txt
GameManager
→ administra el juego, los niveles, la UI, el audio, los enemigos, los assets y el guardado.
```

Eso no define una responsabilidad.

Define una acumulación.

---

## Paso 2: Definir qué NO debe hacer

Un manager sano no solo se define por lo que hace.

También se define por lo que rechaza.

Ejemplo:

```txt
AssetManager puede:
→ cargar assets,
→ cachear assets,
→ liberar assets,
→ precargar grupos.

AssetManager no debe:
→ decidir gameplay,
→ spawnear enemigos,
→ calcular daño,
→ actualizar UI,
→ manejar oleadas.
```

Esta sección es clave para una IA.

Si no se le dicen los límites, es muy probable que agregue lógica al manager porque “ya tiene acceso”.

Regla:

```txt
Todo manager importante debería tener responsabilidades prohibidas documentadas.
```

---

## Paso 3: Evaluar alternativas antes de confirmarlo

Antes de confirmar el manager, hay que revisar si la solución correcta no es otra pieza arquitectónica.

Preguntas:

```txt
¿El problema es creación?
→ evaluar Factory.

¿El problema es reutilización?
→ evaluar Object Pool.

¿El problema es comunicación?
→ evaluar Observer o Event Queue.

¿El problema es acceso simple a varios sistemas?
→ evaluar Facade.

¿El problema es estados y transiciones?
→ evaluar State Machine.

¿El problema es cálculo o validación?
→ evaluar clase pura.

¿El problema es localizar dependencias?
→ evaluar referencia explícita, inyección o Service Locator controlado.
```

Solo después de descartar alternativas tiene sentido confirmar el manager.

Ejemplo:

```txt
Problema:
la UI necesita colocar, vender y mejorar torres.

Solución incorrecta:
UIManager hace toda la lógica.

Solución más sana:
UI captura intención.
GameplayFacade expone operaciones.
BuildInvoker ejecuta comandos.
Factories crean objetos.
Eventos notifican cambios.
```

En ese caso, el problema no era crear un manager nuevo.

Era separar responsabilidades.

---

## Paso 4: Diseñar una API mínima

La API pública de un manager debe ser pequeña y expresar intención.

Ejemplo sano:

```csharp
public interface IAudioManager
{
    void PlaySfx(string id);
    void PlayMusic(string id);
    void StopMusic();
    void SetVolume(float value);
}
```

Ejemplo peligroso:

```csharp
public class AudioManager
{
    public List<AudioSource> sources;
    public Dictionary<string, AudioClip> clips;

    public void PlaySfx(string id) {}
    public void PlayMusic(string id) {}
    public void LoadScene(string sceneName) {}
    public void SaveSettings() {}
    public void UpdateHUD() {}
    public void SpawnAudioObject() {}
}
```

La API mínima debe responder:

```txt
¿Qué operaciones necesita pedir el resto del juego?
¿Qué detalles internos no deberían exponerse?
¿Qué métodos podrían volver rígido el sistema?
¿Qué métodos pertenecen a otra responsabilidad?
```

Regla:

```txt
La API pública muestra qué administra el manager.
No debe exponer toda su implementación interna.
```

---

## Paso 5: Definir ciclo de vida

Todo manager debería tener ciclo de vida claro.

Preguntas obligatorias:

```txt
¿Cuándo se crea?
¿Cuándo se inicializa?
¿Quién lo inicializa?
¿Cuándo se usa?
¿Cuándo se pausa?
¿Cuándo se reinicia?
¿Cuándo se limpia?
¿Cuándo se destruye?
¿Sobrevive entre escenas?
¿Conserva estado?
¿Conserva referencias?
```

Métodos explícitos posibles:

```txt
Initialize
Shutdown
ResetState
EnterLevel
ExitLevel
BindSceneReferences
UnbindSceneReferences
Register
Unregister
```

En Unity, evitar usar callbacks como si fueran API pública.

No hacer:

```csharp
gameManager.Awake();
gameManager.Start();
gameManager.Update();
```

Mejor:

```csharp
gameManager.Initialize();
gameManager.ResetState();
gameManager.EnterLevel(levelData);
```

Regla:

```txt
Awake, Start y Update pertenecen al ciclo de Unity.
No deberían llamarse manualmente para controlar lógica de juego.
```

---

## Paso 6: Definir relación con Unity

Un manager puede ser MonoBehaviour, pero no siempre debería tener toda la lógica dentro del MonoBehaviour.

Diseño recomendado:

```txt
MonoBehaviour
→ conecta con Unity, escena, Inspector y callbacks.

Clases puras
→ contienen reglas, cálculos y lógica testeable.

ScriptableObjects
→ contienen configuración o datos editables.

Eventos
→ desacoplan UI y gameplay.
```

Ejemplo:

```txt
AudioManagerBehaviour
→ recibe referencias de Unity.

AudioService
→ contiene lógica de reproducción y control.

AudioConfig
→ contiene volumen, grupos, ids o configuración.
```

No siempre hace falta esta separación completa, especialmente en prototipos.

Pero el criterio es importante:

```txt
Mientras más crece el manager,
más conviene separar lógica pura de integración Unity.
```

---

## Paso 7: Definir dependencias

Un manager sano no debería depender de todo el proyecto.

Debe quedar claro:

```txt
qué sistemas necesita,
cómo recibe esas dependencias,
si son referencias de escena,
si son servicios persistentes,
si son datos,
si son interfaces,
si se asignan por Inspector,
si se resuelven al inicializar.
```

Ejemplo frágil:

```txt
GameManager busca HUD, AudioManager, Spawner, Player, Camera, Canvas y LevelData usando FindObjectOfType.
```

Ejemplo más sano:

```txt
GameManager recibe dependencias explícitas.
Los objetos de escena se vinculan en BindSceneReferences.
La UI escucha eventos en lugar de ser llamada directamente.
```

Regla:

```txt
Dependencias explícitas
→ arquitectura más clara.

Búsquedas globales
→ usar solo con criterio y no como base del diseño.
```

---

## Paso 8: Definir comunicación por eventos

Un manager puede emitir eventos cuando cambia su estado o cuando ocurre algo relevante.

Ejemplo:

```txt
GameManager cambia estado de partida
→ emite GameStateChanged

UI escucha
→ actualiza pantalla

Audio escucha
→ cambia música si corresponde
```

Esto evita que el manager conozca detalles internos de cada consumidor.

Pero los eventos deben usarse con cuidado.

Riesgos:

```txt
suscripciones duplicadas,
objetos no desuscriptos,
listeners de escenas anteriores,
memory leaks,
orden de ejecución poco claro.
```

Regla:

```txt
Un manager puede emitir eventos.
Pero no debe convertirse en un canal caótico donde todo escucha todo.
```

---

## Paso 9: Definir persistencia

No todo manager debe ser persistente.

Un manager puede ser:

```txt
global,
por escena,
por nivel,
por partida,
por sistema,
por contexto.
```

Managers que a veces pueden persistir:

```txt
AudioManager
SaveManager
AssetManager
UpdateManager
GameManager
```

Managers que muchas veces conviene que sean de escena o nivel:

```txt
LevelManager
UIManager de HUD específico
SpawnerManager
PoolManager de nivel
```

Regla importante:

```txt
Persistir datos puede ser correcto.
Persistir referencias directas a objetos de escena puede ser peligroso.
```

Ejemplo de riesgo:

```txt
Un UIManager persiste.
Tiene referencia a HUDCanvas.
Se carga otra escena.
HUDCanvas anterior se destruye.
UIManager conserva referencia vieja.
```

Soluciones posibles:

```txt
limpiar referencias al salir,
rebind al cargar escena,
separar manager persistente de controladores visuales de escena,
usar eventos,
usar métodos BindSceneReferences y UnbindSceneReferences.
```

---

## Paso 10: Validar contra SOLID

Antes de implementar, el manager debe pasar una revisión mínima de SOLID.

Checklist:

```txt
SRP:
¿Tiene una sola responsabilidad central?

OCP:
¿Puede extenderse sin modificar su núcleo todo el tiempo?

LSP:
Si usa interfaces, ¿los objetos pueden reemplazarse sin excepciones raras?

ISP:
¿Su API evita interfaces gigantes?

DIP:
¿Depende de abstracciones cuando realmente conviene?
```

La pregunta más importante:

```txt
¿Por qué razones puede cambiar este manager?
```

Si cambia por UI, audio, niveles, assets, guardado, daño y spawn, no está sano.

---

## Paso 11: Diseñar implementación incremental

Un manager no debería implementarse como una gran reescritura inicial.

Mejor proceso:

```txt
1. Crear manager con responsabilidad mínima.
2. Exponer API mínima.
3. Integrar un solo flujo.
4. Validar.
5. Migrar responsabilidades relacionadas.
6. Eliminar duplicación vieja.
7. Recién después ampliar.
```

Ejemplo:

```txt
AssetManager inicial:
→ LoadAsset
→ ReleaseAsset

Luego:
→ cache
→ preload groups
→ unload groups
→ diagnóstico de recursos cargados
```

No empezar con:

```txt
AssetManager gigante con Addressables, bundles, cache, pooling, factories, escenas, skins y guardado.
```

Regla:

```txt
Manager sano crece por necesidad validada,
no por anticipación abstracta.
```

---

## Ejemplo correcto

Caso:

```txt
El proyecto tiene proyectiles que se crean y destruyen constantemente.
Esto genera costo de Instantiate/Destroy y posible GC.
```

Diseño sano:

```txt
Responsabilidad:
PoolManager administra objetos reutilizables.

Responsabilidades permitidas:
→ crear pool inicial,
→ entregar objeto disponible,
→ recibir objeto usado,
→ resetear estado,
→ expandir pool si corresponde.

Responsabilidades prohibidas:
→ calcular daño,
→ elegir objetivo,
→ decidir cuándo dispara una torre,
→ modificar economía,
→ actualizar UI.

Relación:
Tower decide disparar.
ProjectilePoolManager entrega proyectil.
Projectile aplica comportamiento.
DamageSystem aplica daño.
GameEvents notifica si corresponde.
```

API mínima:

```csharp
public interface IPoolManager<T>
{
    T Get();
    void Release(T instance);
}
```

---

## Ejemplo incorrecto

Caso:

```txt
El proyecto necesita manejar torres, proyectiles y daño.
```

Diseño incorrecto:

```txt
CombatManager
→ crea proyectiles,
→ decide disparo,
→ calcula daño,
→ aplica daño,
→ reproduce sonido,
→ actualiza UI,
→ suma monedas,
→ maneja upgrades.
```

Problemas:

```txt
demasiadas responsabilidades,
alta dependencia,
difícil testing,
difícil mantenimiento,
riesgo de clase dios,
violación de SRP,
API futura enorme.
```

Separación mejor:

```txt
Tower
→ decide disparo según su estado.

TargetSelector
→ elige objetivo.

ProjectilePoolManager
→ entrega proyectiles.

DamageSystem
→ aplica daño.

AudioManager
→ reproduce sonido.

GameEvents
→ notifica cambios.

UI
→ escucha eventos.
```

---

## Checklist para diseñar un Manager sano

Antes de implementar:

```txt
¿El problema está claramente definido?
¿La responsabilidad puede explicarse en una frase?
¿Se definió qué NO hace?
¿Se evaluaron alternativas?
¿La API pública es mínima?
¿Tiene ciclo de vida definido?
¿Se sabe si persiste entre escenas?
¿Se definieron dependencias?
¿Evita búsquedas globales innecesarias?
¿Evita lógica de UI mezclada con gameplay?
¿Usa eventos cuando conviene?
¿Puede mantenerse SOLID?
¿Puede implementarse incrementalmente?
¿Se puede validar que funciona?
¿Se puede detectar si empieza a crecer mal?
```

---

## Criterio para IA/agente

Cuando una IA diseñe un manager, debe entregar primero el diseño, no el código.

Formato esperado:

```txt
Manager propuesto:
...

Problema que resuelve:
...

Responsabilidad central:
...

Responsabilidades permitidas:
...

Responsabilidades prohibidas:
...

Alternativas evaluadas:
...

API mínima:
...

Ciclo de vida:
...

Relación con Unity:
...

Relación con eventos:
...

Persistencia:
...

Riesgos:
...

Plan incremental:
...

Archivos que tocaría:
...

Archivos que NO tocaría:
...
```

La IA no debería crear código directamente si todavía no puede justificar el diseño.

---

## Regla final

Un manager sano no se mide por cuántas cosas puede hacer.

Se mide por cuántas cosas puede rechazar.

```txt
Manager sano
→ administra una responsabilidad concreta,
→ expone una API mínima,
→ tiene ciclo de vida definido,
→ coordina sin absorber,
→ crece solo cuando hay necesidad real.

Manager peligroso
→ hace de todo,
→ todos dependen de él,
→ crece con cada feature,
→ reemplaza patrones,
→ rompe SOLID.
```

La pregunta final antes de implementarlo es:

```txt
¿Este manager reduce complejidad real
o solo la esconde en una clase central?
```
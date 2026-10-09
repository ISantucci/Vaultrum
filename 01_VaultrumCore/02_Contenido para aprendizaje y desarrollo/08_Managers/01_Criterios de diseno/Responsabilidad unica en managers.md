## Propósito dentro de Vaultrum

Este documento define cómo aplicar responsabilidad única en managers.

Es uno de los criterios más importantes de esta sección, porque los managers tienden naturalmente a crecer.

Un manager empieza resolviendo una responsabilidad clara, pero puede terminar absorbiendo UI, gameplay, audio, escenas, assets, eventos, input y guardado.

La idea principal es:

```txt
Un manager debe tener una responsabilidad central.
No una colección de responsabilidades convenientes.
```

---

## Qué significa responsabilidad única en un Manager

Responsabilidad única no significa que un manager tenga un solo método.

Significa que tiene una sola razón principal para cambiar.

Ejemplo:

```txt
AssetManager
→ cambia si cambia la forma de cargar, cachear o liberar assets.

AudioManager
→ cambia si cambia la forma de reproducir, pausar o configurar audio.

UpdateManager
→ cambia si cambia la forma de registrar, desregistrar o ejecutar actualizaciones.
```

Eso es sano.

Ejemplo peligroso:

```txt
GameManager cambia si cambia:
UI,
audio,
guardado,
spawn,
pathfinding,
economía,
niveles,
daño,
input,
oleadas.
```

Eso indica demasiadas razones para cambiar.

---

## Cómo identificar la responsabilidad central

Para definir la responsabilidad central de un manager, responder:

```txt
¿Qué administra?
¿Qué ciclo controla?
¿Qué recurso centraliza?
¿Qué estado posee?
¿Qué sistemas coordina?
¿Qué problema evita?
```

Después reducirlo a una frase.

Ejemplo:

```txt
AssetManager
→ administra carga, cache y liberación de assets.
```

Ejemplo:

```txt
UpdateManager
→ administra registro y ejecución controlada de actualizaciones.
```

Ejemplo:

```txt
LevelManager
→ administra entrada, salida y progreso del nivel actual.
```

Si la frase necesita muchas comas, probablemente hay responsabilidades mezcladas.

---

## Responsabilidades permitidas

Un manager puede tener varias operaciones relacionadas con su responsabilidad central.

Ejemplo `AudioManager`:

```txt
PlayMusic
StopMusic
PlaySfx
SetMasterVolume
SetMusicVolume
SetSfxVolume
Mute
Unmute
```

Todas pertenecen al dominio de audio.

Ejemplo `AssetManager`:

```txt
LoadAsset
ReleaseAsset
PreloadGroup
UnloadGroup
ClearCache
```

Todas pertenecen al dominio de assets.

Ejemplo `UpdateManager`:

```txt
Register
Unregister
Tick
SetGroupFrequency
PauseGroup
ResumeGroup
```

Todas pertenecen al dominio de actualización.

Criterio:

```txt
Muchas operaciones pueden ser válidas
si pertenecen a una misma responsabilidad central.
```

---

## Responsabilidades prohibidas

Un manager no debería absorber responsabilidades ajenas.

Ejemplo `AudioManager` no debería:

```txt
cambiar escenas,
guardar partida,
modificar UI directamente,
decidir victoria,
calcular daño,
spawnear enemigos.
```

Ejemplo `AssetManager` no debería:

```txt
instanciar enemigos por lógica de gameplay,
decidir oleadas,
calcular daño,
modificar economía,
actualizar HUD,
decidir estados del juego.
```

Ejemplo `GameManager` no debería:

```txt
ser dueño de toda la UI,
cargar todos los assets,
reproducir todos los sonidos,
crear todos los enemigos,
guardar todos los datos,
controlar cada sistema específico.
```

---

## Señales de que se perdió la responsabilidad única

Señales comunes:

```txt
El manager cambia por cualquier feature.
Tiene demasiadas referencias.
Tiene demasiados métodos públicos.
Su nombre es genérico.
Tiene regiones enormes.
Tiene lógica de UI y gameplay mezclada.
Tiene lógica de escena y persistencia mezclada.
Tiene lógica de assets y creación mezclada.
Tiene lógica de eventos y reglas de juego mezclada.
```

Señal crítica:

```txt
Cada nuevo sistema necesita tocar el manager.
```

Eso indica que el manager es cuello de botella arquitectónico.

---

## Relación con SOLID

Este documento se relaciona directamente con S - Single Responsibility Principle.

Un manager sano debe tener una razón clara para cambiar.

También se relaciona con:

```txt
O - OpenClosed Principle
→ si cada feature obliga a modificar el manager, está mal cerrado.

I - Interface Segregation Principle
→ si el manager expone demasiadas cosas, fuerza dependencias innecesarias.

D - Dependency Inversion Principle
→ si depende de todos los concretos, queda rígido.
```

Regla:

```txt
Mientras más central es una clase,
más fuerte debe ser su responsabilidad única.
```

---

## Cómo mantener responsabilidad única

Para mantener un manager acotado:

```txt
Definir responsabilidad en una frase.
Definir responsabilidades prohibidas.
Exponer API mínima.
Delegar trabajo específico.
Usar eventos para notificar.
Usar factories para crear.
Usar pools para reutilizar.
Usar state machines para estados.
Usar clases puras para cálculos.
Usar systems para reglas de dominio.
```

Ejemplo:

```txt
GameManager
→ coordina estado global.

DamageSystem
→ aplica daño.

UIManager
→ coordina pantallas.

AudioManager
→ reproduce audio.

SaveManager
→ guarda datos.
```

---

## Cómo dividir un Manager con demasiadas responsabilidades

Si un manager creció demasiado, no crear otro manager gigante.

Primero separar responsabilidades.

Preguntas:

```txt
¿Qué métodos pertenecen a UI?
¿Qué métodos pertenecen a audio?
¿Qué métodos pertenecen a assets?
¿Qué métodos pertenecen a nivel?
¿Qué métodos pertenecen a estado?
¿Qué métodos pertenecen a cálculo?
¿Qué métodos pertenecen a eventos?
¿Qué métodos pertenecen a creación?
```

Luego mover cada responsabilidad a la pieza correcta.

Ejemplo:

```txt
GameManager grande
→ GameManager
→ LevelManager
→ UIManager
→ AudioManager
→ SaveManager
→ GameStateMachine
→ EconomySystem
```

---

## Criterio para IA/agente

Cuando una IA analice un manager, debe listar razones de cambio.

Formato:

```txt
Manager analizado:
...

Responsabilidad declarada:
...

Métodos encontrados:
...

Razones de cambio detectadas:
1.
2.
3.

Responsabilidades mezcladas:
...

Recomendación:
mantener / dividir / renombrar / reemplazar.
```

Una IA no debería decir solo:

```txt
“Este manager está grande.”
```

Debe explicar:

```txt
qué responsabilidades contiene,
cuáles sobran,
a dónde podrían moverse,
y qué riesgo reduce el cambio.
```

---

## Ejemplo aplicado a videojuegos

Manager peligroso:

```txt
GameManager
→ StartLevel
→ SpawnEnemy
→ PlayMusic
→ SaveGame
→ UpdateHUD
→ CalculateDamage
→ LoadTowerPrefab
→ PauseGame
```

Responsabilidades detectadas:

```txt
flujo de nivel,
spawn,
audio,
guardado,
UI,
combate,
assets,
pausa.
```

Separación posible:

```txt
LevelManager
→ StartLevel.

EnemySpawner
→ SpawnEnemy.

AudioManager
→ PlayMusic.

SaveManager
→ SaveGame.

UIManager/HUD
→ UpdateHUD.

DamageSystem
→ CalculateDamage.

AssetManager
→ LoadTowerPrefab.

GameStateMachine
→ PauseGame.
```

---

## Checklist de responsabilidad única

Para auditar un manager:

```txt
¿Puede describirse su responsabilidad en una frase?
¿Tiene una sola razón principal para cambiar?
¿Sus métodos pertenecen al mismo dominio?
¿Tiene responsabilidades prohibidas documentadas?
¿Depende de demasiados sistemas concretos?
¿Cada nueva feature obliga a modificarlo?
¿Contiene lógica de UI, audio, assets, gameplay y guardado mezclada?
¿Podría delegar en sistemas especializados?
¿Su API pública es pequeña?
¿Se mantiene entendible sin conocer todo el proyecto?
```

---

## Regla final

Un manager sano no es pequeño porque tenga pocas líneas.

Es sano porque tiene una responsabilidad clara.

```txt
Muchas líneas con una sola responsabilidad
→ puede ser aceptable.

Pocas líneas con muchas responsabilidades mezcladas
→ sigue siendo peligroso.
```

La pregunta clave es:

```txt
¿Por qué razones cambia este manager?
```
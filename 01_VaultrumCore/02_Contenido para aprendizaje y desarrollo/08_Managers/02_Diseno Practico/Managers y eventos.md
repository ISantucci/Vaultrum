## Propósito dentro de Vaultrum

Este documento define cómo deberían comunicarse los managers mediante eventos.

El objetivo es evitar managers que conocen directamente a todos los sistemas del juego.

Los eventos permiten que un manager notifique cambios sin depender de cada consumidor.

La idea principal es:

```txt
Un manager puede emitir eventos para comunicar cambios.
No debería llamar directamente a todo el proyecto.
```

---

## Por qué usar eventos con managers

Los eventos ayudan a desacoplar sistemas.

Ejemplo:

```txt
GameManager cambia estado de partida.
UI necesita actualizar pantalla.
Audio necesita cambiar música.
Spawner necesita detenerse.
```

Sin eventos:

```txt
GameManager llama directamente a UIManager.
GameManager llama directamente a AudioManager.
GameManager llama directamente a Spawner.
```

Con eventos:

```txt
GameManager emite GameStateChanged.
UI escucha.
Audio escucha.
Spawner escucha.
```

El manager no necesita conocer detalles internos de cada consumidor.

---

## Eventos emitidos por managers

Un manager puede emitir eventos cuando cambia algo relevante de su responsabilidad.

Ejemplos:

```txt
GameManager
→ GameStateChanged

LevelManager
→ LevelEntered / LevelExited

AudioManager
→ VolumeChanged

AssetManager
→ AssetLoaded / AssetReleased

SaveManager
→ SaveStarted / SaveCompleted / SaveFailed

EventQueueManager
→ EventProcessed
```

Criterio:

```txt
El evento debe representar un cambio real de estado o una acción relevante.
```

No conviene emitir eventos por cada detalle interno.

---

## Eventos escuchados por managers

Un manager también puede escuchar eventos.

Ejemplo:

```txt
AudioManager escucha GameStateChanged
→ cambia música.

UIManager escucha MoneyChanged
→ actualiza HUD.

SaveManager escucha CheckpointReached
→ guarda progreso.

PoolManager escucha LevelExited
→ limpia objetos activos.
```

Esto puede ser sano si la responsabilidad lo justifica.

Pero hay que evitar que todo escuche todo.

Regla:

```txt
Un manager debe escuchar eventos relacionados con su responsabilidad.
No eventos de todo el juego por comodidad.
```

---

## Observer vs Event Queue

Observer sirve para notificar cambios a suscriptores.

Event Queue sirve para encolar eventos y procesarlos luego.

Diferencia simple:

```txt
Observer
→ algo ocurre y los listeners reaccionan.

Event Queue
→ algo se encola y se procesa en orden o en otro momento.
```

Ejemplo Observer:

```txt
MoneyChanged
→ HUD actualiza valor.
```

Ejemplo Event Queue:

```txt
EnemyKilled
→ se encola recompensa,
→ luego se procesa suma de dinero,
→ luego se notifica MoneyChanged.
```

Criterio:

```txt
Si la reacción debe ser inmediata y simple,
Observer puede alcanzar.

Si importa orden, diferimiento o procesamiento central,
Event Queue puede ser mejor.
```

---

## Eventos y UI

La UI suele beneficiarse mucho de eventos.

Ejemplo sano:

```txt
EconomySystem cambia dinero.
Emite MoneyChanged.
HUD escucha.
HUD actualiza texto.
```

Ejemplo peligroso:

```txt
EconomySystem conoce el texto del HUD.
EconomySystem cambia directamente TMP_Text.
```

Regla:

```txt
Gameplay cambia estado.
UI muestra estado.
Eventos conectan ambas partes.
```

Esto evita que managers de gameplay dependan de detalles visuales.

---

## Eventos y ciclo de vida

Todo sistema que se suscribe a eventos debe desuscribirse cuando deja de usarse.

Ejemplo:

```csharp
private void OnEnable()
{
    GameEvents.MoneyChanged += HandleMoneyChanged;
}

private void OnDisable()
{
    GameEvents.MoneyChanged -= HandleMoneyChanged;
}
```

Riesgos de no desuscribirse:

```txt
memory leaks,
listeners duplicados,
errores por objetos destruidos,
eventos ejecutados varias veces,
referencias viejas de escena.
```

Regla:

```txt
Suscripción sin desuscripción es deuda técnica.
```

---

## Eventos y managers persistentes

Los managers persistentes requieren cuidado extra.

Ejemplo:

```txt
AudioManager persiste.
Escucha eventos de una escena.
La escena se destruye.
AudioManager sigue suscripto a objetos de esa escena.
```

Esto puede generar errores.

Solución:

```txt
limpiar suscripciones al salir de escena,
usar eventos globales bien definidos,
hacer Bind/Unbind de referencias,
evitar suscripciones ocultas.
```

Regla:

```txt
Un manager persistente no debería quedar enganchado a eventos de objetos destruidos.
```

---

## Eventos demasiado genéricos

Eventos genéricos pueden volver difícil entender el flujo.

Ejemplo peligroso:

```csharp
public event Action<object> OnSomethingHappened;
```

Problemas:

```txt
no se entiende qué ocurrió,
los listeners deben interpretar datos ambiguos,
aumenta acoplamiento implícito,
dificulta debugging.
```

Mejor:

```csharp
public event Action<int> MoneyChanged;
public event Action<GameState> GameStateChanged;
public event Action<string> LevelEntered;
```

Regla:

```txt
El nombre del evento debe explicar qué ocurrió.
```

---

## Eventos y orden de ejecución

Los eventos pueden ocultar el orden de ejecución.

Si varios sistemas escuchan el mismo evento, puede no ser obvio qué pasa primero.

Ejemplo:

```txt
LevelCompleted
→ UI muestra victoria.
→ SaveManager guarda progreso.
→ AudioManager cambia música.
→ Spawner se detiene.
```

Eso puede estar bien.

Pero si el orden importa, conviene explicitarlo.

Opciones:

```txt
Event Queue,
orquestación en LevelManager,
flujo de estados,
secuencia controlada,
prioridades si están justificadas.
```

Regla:

```txt
Si el orden importa, no depender de casualidades de suscripción.
```

---

## Relación con SOLID

Eventos ayudan a reducir acoplamiento.

Pero mal usados también pueden ocultar dependencias.

Beneficios:

```txt
SRP:
cada sistema reacciona desde su responsabilidad.

DIP:
los emisores no dependen de consumidores concretos.

OCP:
se pueden agregar listeners sin modificar el manager emisor.
```

Riesgos:

```txt
flujo difícil de seguir,
eventos globales excesivos,
dependencias invisibles,
listeners duplicados.
```

Regla:

```txt
Eventos desacoplan referencias,
pero no reemplazan diseño de flujo.
```

---

## Criterio para IA/agente

Cuando una IA proponga eventos en managers, debe explicar:

```txt
Quién emite el evento.
Qué cambio representa.
Quiénes deberían escucharlo.
Por qué no conviene llamada directa.
Si la reacción debe ser inmediata o encolada.
Dónde se suscribe.
Dónde se desuscribe.
Qué riesgo de duplicación existe.
```

La IA no debe crear eventos globales vagos.

---

## Ejemplo aplicado a videojuegos

Caso:

```txt
El jugador gana dinero al matar enemigos.
El HUD debe actualizarse.
El sonido de recompensa debe reproducirse.
```

Diseño sano:

```txt
Enemy muere.
RewardSystem calcula recompensa.
EconomySystem suma dinero.
EconomySystem emite MoneyChanged.
HUD escucha MoneyChanged.
AudioManager puede escuchar RewardGranted si corresponde.
```

Diseño peligroso:

```txt
Enemy llama a HUD.
Enemy llama a AudioManager.
Enemy modifica dinero en GameManager.
Enemy actualiza texto.
```

El primer diseño mantiene responsabilidades separadas.

---

## Checklist de eventos en managers

Antes de aprobar eventos:

```txt
¿El evento representa un cambio claro?
¿El nombre comunica intención?
¿El emisor corresponde a la responsabilidad del manager?
¿Los listeners tienen razón para escuchar?
¿Se evita llamada directa innecesaria?
¿Se controla suscripción y desuscripción?
¿Hay riesgo de listeners duplicados?
¿Hay riesgo de referencias viejas?
¿El orden de ejecución importa?
¿Debería ser Observer o Event Queue?
¿El evento es demasiado genérico?
```

---

## Regla final

Los eventos son una herramienta para comunicar cambios sin acoplar sistemas directamente.

```txt
Evento sano
→ comunica un cambio claro,
→ tiene emisores y listeners coherentes,
→ respeta ciclo de vida,
→ evita acoplamiento innecesario.

Evento peligroso
→ es genérico,
→ todo escucha todo,
→ nadie sabe el orden,
→ y las referencias quedan vivas sin control.
```
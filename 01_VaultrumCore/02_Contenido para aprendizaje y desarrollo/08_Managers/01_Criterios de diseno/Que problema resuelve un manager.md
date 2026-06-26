## Propósito dentro de Vaultrum

Este documento define qué tipo de problemas puede resolver un manager dentro de un proyecto de videojuegos.

El objetivo no es justificar managers por costumbre, sino reconocer cuándo existe una necesidad real de administración centralizada.

Una IA o un desarrollador no deberían crear un manager porque una clase “queda más ordenada” con ese nombre.

Deberían crearlo cuando existe un problema arquitectónico concreto.

La idea principal es:

```txt
Problema claro
→ responsabilidad clara
→ manager justificado
```

Sin problema claro, un manager suele convertirse en complejidad innecesaria.

---

## Problema principal que resuelve un Manager

Un manager resuelve problemas donde una responsabilidad necesita ser administrada de manera central, compartida o coordinada.

Puede tratarse de:

```txt
estado global limitado,
recursos compartidos,
ciclo de vida,
flujo de juego,
actualizaciones,
eventos,
persistencia,
carga y descarga,
audio,
UI,
niveles,
pools,
o servicios transversales.
```

Ejemplo:

```txt
Problema:
varias clases necesitan reproducir sonidos y modificar volumen.

Manager posible:
AudioManager.

Responsabilidad:
centralizar reproducción, configuración y control de audio.
```

Otro ejemplo:

```txt
Problema:
muchos objetos ejecutan Update sin control y no todos necesitan actualizarse cada frame.

Manager posible:
UpdateManager.

Responsabilidad:
registrar, desregistrar y ejecutar actualizaciones con frecuencia controlada.
```

---

## Problemas de acceso compartido

Un manager puede resolver un problema de acceso compartido cuando muchos sistemas necesitan usar una misma responsabilidad.

Ejemplo:

```txt
UI necesita mostrar monedas.
Torre necesita consumir monedas.
Recompensa necesita sumar monedas.
Sistema de oleadas necesita consultar monedas.
```

Esto no significa que todo deba ir al `GameManager`.

Significa que hay que identificar la responsabilidad real.

Posibles separaciones:

```txt
EconomySystem
→ administra dinero.

GameManager
→ coordina estado global.

UI
→ muestra el valor mediante eventos.

EventQueueManager
→ procesa eventos de economía si corresponde.
```

Criterio:

```txt
Si muchos sistemas acceden a lo mismo,
primero identificar qué es “lo mismo”.

Después decidir si necesita un manager,
un servicio,
un sistema,
un evento,
una facade
o una referencia explícita.
```

---

## Problemas de ciclo de vida

Un manager puede resolver problemas de ciclo de vida cuando algo necesita ser creado, inicializado, reiniciado, pausado, liberado o destruido en momentos concretos.

Ejemplos:

```txt
Assets que se cargan al entrar a un nivel y se liberan al salir.
Proyectiles que se reutilizan en vez de destruirse.
Estados del juego que se inicializan y finalizan.
Datos de partida que se reinician al volver al menú.
Sistemas persistentes que sobreviven entre escenas.
```

Ejemplo:

```txt
Problema:
los proyectiles se crean y destruyen constantemente durante gameplay.

Manager posible:
PoolManager.

Responsabilidad:
administrar objetos reutilizables, entregarlos, recibirlos y resetearlos.
```

---

## Problemas de coordinación

Un manager puede resolver problemas de coordinación cuando varios sistemas necesitan actuar en cierto orden o bajo una misma regla.

Ejemplo:

```txt
Al iniciar un nivel:
→ cargar datos del nivel,
→ inicializar enemigos,
→ preparar UI,
→ reiniciar economía,
→ resetear estado,
→ habilitar gameplay.
```

Esto puede requerir coordinación.

Pero no significa que una sola clase deba hacer todo.

Un buen manager puede coordinar sin absorber.

```txt
LevelManager
→ coordina entrada al nivel.

AssetManager
→ carga assets.

UIManager
→ prepara UI.

GameManager
→ cambia estado general.

EventQueueManager
→ procesa eventos pendientes.
```

Criterio:

```txt
Coordinar no es hacer el trabajo de todos.
Coordinar es ordenar cuándo y cómo participan los sistemas responsables.
```

---

## Problemas de estado global limitado

Algunos datos pertenecen al estado global o semi-global del juego.

Ejemplos:

```txt
estado actual de partida,
pausa,
victoria,
derrota,
nivel actual,
modo de juego,
configuración global,
progreso general,
monedas globales,
vida base en un tower defense.
```

Un manager puede administrar este estado si está bien acotado.

Ejemplo:

```txt
GameManager
→ administra estado general de partida.

No:
→ calcula daño,
→ dibuja UI,
→ mueve enemigos,
→ carga assets,
→ reproduce audio.
```

Regla:

```txt
Estado global limitado
→ puede justificar un manager.

Lógica global infinita
→ crea clase dios.
```

---

## Problemas de duplicación

Un manager puede resolver duplicación cuando la misma lógica aparece repetida en muchos lugares.

Ejemplo:

```txt
Distintos sistemas cargan assets con su propia lógica.
Distintos paneles UI actualizan estado de forma duplicada.
Distintos objetos hacen búsquedas globales repetidas.
Distintos sistemas crean objetos temporales sin control.
```

Pero la duplicación no siempre requiere manager.

Puede requerir:

```txt
una función,
una clase pura,
una estrategia,
una factory,
un evento,
un ScriptableObject,
una configuración compartida,
o una abstracción.
```

Criterio:

```txt
Si la duplicación es de cálculo puntual
→ clase pura o función.

Si la duplicación es de creación
→ Factory.

Si la duplicación es de acceso a subsistemas
→ Facade.

Si la duplicación es de ciclo de vida compartido
→ posible Manager.
```

---

## Problemas de comunicación

A veces se crea un manager para que “todos puedan hablar con todos”.

Eso suele ser mala señal.

La comunicación entre sistemas puede resolverse con:

```txt
eventos,
observer,
event queue,
referencias explícitas,
interfaces,
facades,
o mediadores.
```

Un manager puede participar, pero no debería ser usado como canal universal.

Ejemplo malo:

```txt
UI le pregunta todo al GameManager.
Enemy le avisa todo al GameManager.
Audio depende de GameManager.
Spawner depende de GameManager.
Save depende de GameManager.
```

Ejemplo más sano:

```txt
GameManager emite GameStateChanged.
UI escucha.
Audio escucha si corresponde.
Spawner reacciona al estado.
SaveManager guarda cuando se solicita.
```

---

## Problemas que un Manager NO resuelve

Un manager no resuelve automáticamente:

```txt
mala separación de responsabilidades,
clases demasiado grandes,
falta de eventos,
falta de abstracciones,
dependencias circulares,
UI acoplada a gameplay,
falta de diseño de estados,
falta de factories,
falta de pools,
falta de configuración por datos.
```

Si el problema real es uno de esos, crear un manager puede empeorarlo.

Ejemplo:

```txt
Problema real:
GameManager tiene demasiada lógica.

Mala solución:
crear SuperGameManager.

Solución correcta:
separar responsabilidades:
LevelManager,
UIManager,
AudioManager,
SaveManager,
StateMachine,
EventQueue,
clases puras.
```

---

## Relación con SOLID

Un manager puede ayudar a SOLID si concentra una responsabilidad que estaba repetida o dispersa.

Pero puede romper SOLID si empieza a absorber responsabilidades de otros sistemas.

Relación con S - Single Responsibility Principle:

```txt
Manager sano
→ una responsabilidad central.

Manager peligroso
→ muchas razones para cambiar.
```

Relación con D - Dependency Inversion Principle:

```txt
Manager sano
→ puede depender de abstracciones cuando conviene.

Manager peligroso
→ conoce implementaciones concretas de todo el proyecto.
```

Relación con I - Interface Segregation Principle:

```txt
Manager sano
→ API mínima.

Manager peligroso
→ interfaz enorme que todos usan para todo.
```

La pregunta clave es:

```txt
¿El manager está reduciendo acoplamiento
o simplemente se volvió el nuevo centro de acoplamiento?
```

---

## Criterio para IA/agente

Cuando una IA detecte un posible manager, debe describir primero el problema.

No debería empezar por la solución.

Formato recomendado:

```txt
Problema detectado:
...

Responsabilidad dispersa:
...

Alternativas evaluadas:
- Clase común:
- Factory:
- Facade:
- Event Queue:
- Object Pool:
- State Machine:

Por qué corresponde un manager:
...

Responsabilidades permitidas:
...

Responsabilidades prohibidas:
...
```

Ejemplo correcto:

```txt
Problema detectado:
la carga de assets está repetida en spawner, UI y factory.

Alternativas:
Factory no alcanza porque no solo se crean objetos.
Facade no alcanza porque hay cache y release.
Service Locator no resuelve ciclo de vida.

Manager propuesto:
AssetManager.

Responsabilidad:
cargar, cachear y liberar assets.
```

---

## Checklist de diagnóstico

Antes de decidir que un manager resuelve el problema:

```txt
¿El problema está claramente definido?
¿La responsabilidad aparece en varios lugares?
¿Hay ciclo de vida que administrar?
¿Hay recursos compartidos?
¿Hay estado global limitado?
¿Hay coordinación real entre sistemas?
¿La solución no corresponde mejor a otro patrón?
¿El manager tendría una API pequeña?
¿Se puede explicar qué NO hará?
¿Se puede validar que resolvió el problema?
```

---

## Regla final

Un manager no debe ser la primera respuesta.

Debe ser una respuesta justificada.

```txt
No:
“Esto está desordenado, creemos un manager.”

Sí:
“Esta responsabilidad está dispersa, tiene ciclo de vida propio,
necesita coordinación central y no corresponde a otra pieza.
Por eso un manager está justificado.”
```
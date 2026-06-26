## Propósito dentro de Vaultrum

Este documento define qué es un Manager Dios, cómo detectarlo y cómo evitarlo.

Es uno de los riesgos más importantes al trabajar con managers en videojuegos.

Un manager puede empezar como solución razonable y terminar siendo el centro de todo el proyecto.

La idea principal es:

```txt
Manager Dios
→ clase que concentra demasiadas responsabilidades
→ todos dependen de ella
→ cualquier cambio pasa por ella
→ se vuelve difícil de modificar, testear y escalar.
```

Vaultrum debe ayudar a personas e IAs a detectar este riesgo antes de que se vuelva estructural.

---

## Qué es un Manager Dios

Un Manager Dios es una clase que administra demasiadas cosas al mismo tiempo.

Suele tener responsabilidades como:

```txt
estado global,
UI,
audio,
niveles,
spawn,
assets,
guardado,
input,
economía,
daño,
eventos,
pathfinding,
oleadas,
pausa,
victoria,
derrota.
```

El problema no es que coordine sistemas.

El problema es que los reemplaza.

Ejemplo:

```txt
GameManager
→ crea enemigos,
→ calcula daño,
→ actualiza UI,
→ reproduce audio,
→ guarda partida,
→ cambia escenas,
→ carga assets,
→ procesa input,
→ maneja niveles,
→ controla oleadas.
```

Eso no es coordinación.

Es acumulación.

---

## Cómo aparece un Manager Dios

Suele aparecer de forma incremental.

```txt
Primero:
GameManager maneja estado de partida.

Después:
le agregamos pausa.

Después:
le agregamos UI.

Después:
le agregamos audio.

Después:
le agregamos spawn.

Después:
le agregamos guardado.

Después:
le agregamos carga de assets.

Resultado:
GameManager se vuelve obligatorio para todo.
```

Rara vez nace como clase dios.

Normalmente crece por decisiones pequeñas no revisadas.

---

## Señales de alerta

Señales comunes:

```txt
El manager tiene demasiados métodos públicos.
Tiene referencias a casi todos los sistemas.
Tiene muchos campos serializados.
Todos los scripts llaman a Instance.
Tiene un Update grande.
Tiene lógica de UI y gameplay mezclada.
Tiene lógica de escena y persistencia mezclada.
Tiene lógica de assets y gameplay mezclada.
Cada feature nueva toca el manager.
Cambiar algo simple rompe otra cosa.
Es difícil testearlo.
Es difícil entenderlo sin leer medio proyecto.
```

Señal crítica:

```txt
Si el manager falla, todo el juego falla.
```

---

## Riesgos técnicos

Un Manager Dios puede causar:

```txt
acoplamiento alto,
dependencias circulares,
orden de inicialización frágil,
bugs al cambiar escena,
memory leaks,
referencias destruidas,
dificultad para testear,
dificultad para refactorizar,
dificultad para trabajar en equipo,
problemas de performance,
más riesgo al modificar.
```

En Unity, además puede generar:

```txt
DontDestroyOnLoad mal usado,
referencias viejas a objetos de escena,
suscripciones duplicadas,
callbacks manuales incorrectos,
Update gigante,
FindObjectOfType para reenganchar dependencias,
errores al recargar escenas.
```

---

## Relación con SOLID

Un Manager Dios rompe principalmente S - Single Responsibility Principle.

Tiene muchas razones para cambiar.

También suele romper:

```txt
[[O - OpenClosed Principle]]
→ cada nueva feature modifica el manager.

[[I - Interface Segregation Principle]]
→ expone demasiados métodos para demasiados consumidores.

[[D - Dependency Inversion Principle]]
→ depende de demasiadas implementaciones concretas.

[[L - Liskov Substitution Principle]]
→ si usa abstracciones con excepciones internas constantes, la abstracción está mal diseñada.
```

Regla:

```txt
Un Manager Dios es una violación acumulada de SOLID.
```

No es solo una clase grande.

Es una clase con demasiada autoridad arquitectónica.

---

## Diferencia entre coordinador y clase dios

Un manager puede coordinar sin ser clase dios.

Coordinador sano:

```txt
LevelManager
→ solicita al AssetManager cargar recursos.
→ solicita al UIManager preparar pantalla.
→ solicita al Spawner iniciar oleada.
→ informa al GameManager cambio de estado.
```

Clase dios:

```txt
LevelManager
→ carga assets directamente.
→ instancia enemigos.
→ modifica UI.
→ reproduce audio.
→ calcula recompensas.
→ guarda progreso.
```

Diferencia:

```txt
Coordinar
→ decir cuándo participan los sistemas.

Absorber
→ hacer el trabajo de los sistemas.
```

---

## Cómo evitar un Manager Dios

Para evitarlo:

```txt
Definir responsabilidad en una frase.
Definir responsabilidades prohibidas.
Mantener API mínima.
Delegar creación a factories.
Delegar reutilización a pools.
Delegar estados a state machines.
Delegar comunicación a eventos.
Delegar cálculos a clases puras.
Delegar UI a UIManager o componentes UI.
Delegar assets a AssetManager.
Delegar audio a AudioManager.
Delegar guardado a SaveManager.
```

Regla:

```txt
Si otro sistema especializado puede hacerlo mejor,
el manager no debería absorberlo.
```

---

## Cómo refactorizar un Manager Dios

No conviene refactorizar todo de golpe.

Proceso recomendado:

```txt
1. Listar métodos y campos.
2. Agrupar por responsabilidad.
3. Detectar razones de cambio.
4. Identificar responsabilidades externas.
5. Crear piezas pequeñas.
6. Mover una responsabilidad por vez.
7. Mantener compatibilidad temporal si hace falta.
8. Validar después de cada paso.
```

Ejemplo:

```txt
GameManager grande
→ extraer AudioManager.
→ extraer UIManager.
→ extraer LevelManager.
→ extraer SaveManager.
→ extraer StateMachine.
```

No hacer:

```txt
reescribir toda la arquitectura en un solo cambio.
```

---

## Criterio para IA/agente

Una IA debe detectar Manager Dios antes de proponer nuevas features sobre él.

Si una IA ve un manager grande, debe responder:

```txt
Responsabilidades detectadas:
...

Riesgos:
...

Qué se puede mantener:
...

Qué conviene extraer:
...

Orden incremental de refactor:
...

Qué no tocar todavía:
...

Validación:
...
```

No debe seguir agregando código al manager sin análisis.

Respuesta incorrecta:

```txt
Agrego esta feature al GameManager porque ya tiene referencias a todo.
```

Respuesta correcta:

```txt
No recomiendo agregar esta feature al GameManager.
La responsabilidad pertenece a UIManager/AudioManager/LevelManager.
Propongo extraer primero una API mínima o crear un sistema específico.
```

---

## Ejemplo aplicado a videojuegos

Caso:

```txt
GameManager actual:
- vida del jugador
- dinero
- pausa
- selección de nivel
- spawn de enemigos
- música
- HUD
- guardado
- carga de prefabs
```

Análisis:

```txt
Vida/dinero
→ EconomySystem o PlayerState.

Pausa/estado
→ GameStateMachine.

Selección de nivel
→ LevelManager.

Spawn
→ EnemySpawner.

Música
→ AudioManager.

HUD
→ UIManager/HUDController.

Guardado
→ SaveManager.

Carga de prefabs
→ AssetManager.
```

Resultado deseado:

```txt
GameManager
→ conserva solo estado global mínimo y coordinación de alto nivel.
```

---

## Checklist de detección

Un manager puede ser clase dios si:

```txt
¿Tiene más de una responsabilidad central?
¿Tiene referencias a casi todos los sistemas?
¿Todo pasa por él?
¿Todos lo llaman por singleton?
¿Tiene demasiados métodos públicos?
¿Tiene lógica de UI, gameplay, audio, assets y guardado mezclada?
¿Cada feature nueva lo modifica?
¿Tiene Update grande?
¿Tiene dependencias circulares?
¿Es difícil probarlo aislado?
¿Es difícil explicar qué NO hace?
```

Mientras más respuestas sean “sí”, mayor riesgo.

---

## Regla final

Un manager sano administra.

Un Manager Dios domina.

```txt
Manager sano
→ coordina y delega.

Manager Dios
→ absorbe y centraliza sin límite.
```

La mejor defensa es definir límites antes de que crezca.
## Propósito dentro de Vaultrum

Este documento define cuándo no conviene crear un manager.

Es tan importante saber cuándo crear uno como saber cuándo evitarlo.

En proyectos de videojuegos, especialmente con Unity, es común resolver cualquier desorden con una clase llamada `Manager`.

Vaultrum debe evitar ese reflejo.

La idea principal es:

```txt
No todo sistema necesita un manager.
No toda clase grande se arregla con otro manager.
No toda dependencia se soluciona con un singleton.
```

---

## No crear un Manager cuando la responsabilidad no está clara

Si no se puede explicar qué administra el manager, no debería existir todavía.

Mala justificación:

```txt
Necesitamos un manager para ordenar esto.
```

Buena justificación:

```txt
Necesitamos un AssetManager porque la carga, cache y liberación de assets está repetida y necesita ciclo de vida controlado.
```

Pregunta obligatoria:

```txt
¿Qué responsabilidad exacta administra?
```

Si la respuesta es vaga, no crear el manager.

---

## No crear un Manager para evitar pensar diseño

Un manager no debe ser un lugar donde tirar código que no encaja.

Mala señal:

```txt
No sé dónde poner esto, lo meto en GameManager.
```

Esto genera:

```txt
clases dios,
acoplamiento,
dependencias globales,
difícil testing,
difícil refactor,
más riesgo al modificar.
```

En ese caso, la pregunta correcta es:

```txt
¿Qué responsabilidad representa este código?
```

No:

```txt
¿Qué manager puede absorberlo?
```

---

## No crear un Manager cuando alcanza una clase común

Muchas responsabilidades no necesitan manager.

Ejemplos:

```txt
calcular daño,
elegir objetivo,
validar costo,
calcular distancia,
parsear datos,
ordenar una lista,
decidir una estrategia,
evaluar una condición.
```

Estas responsabilidades pueden ser:

```txt
clases puras,
servicios pequeños,
estrategias,
calculadoras,
validadores,
helpers controlados,
o componentes específicos.
```

Ejemplo:

```txt
DamageCalculator
→ calcula daño.

No hace falta:
DamageManager
si solo hay una fórmula simple y local.
```

Criterio:

```txt
Si solo calcula o transforma datos,
probablemente no necesita ser manager.
```

---

## No crear un Manager cuando corresponde una Factory

Si el problema principal es crear objetos, probablemente corresponde una Factory.

Ejemplo:

```txt
Crear enemigos según tipo.
Crear torres según configuración.
Crear proyectiles según data.
```

Eso no necesariamente requiere un manager.

```txt
EnemyFactory
→ crea enemigos.

TowerFactory
→ crea torres.

ProjectileFactory
→ crea proyectiles.
```

No conviene crear:

```txt
EnemyManager
→ crea enemigos,
→ decide spawn,
→ maneja vida,
→ mueve enemigos,
→ calcula ruta.
```

Criterio:

```txt
Si el problema es creación,
evaluar Factory antes que Manager.
```

---

## No crear un Manager cuando corresponde una Facade

Si el problema es simplificar el acceso a varios subsistemas, puede corresponder una Facade.

Ejemplo:

```txt
UI necesita pedir colocar torre,
vender torre,
mejorar torre,
consultar dinero.
```

Una facade puede exponer una API simple sin ser dueña de toda la lógica.

```txt
GameplayFacade
→ expone operaciones de gameplay a UI.

BuildInvoker
→ ejecuta comandos.

GameManager
→ administra estado.

EconomySystem
→ maneja dinero.
```

Criterio:

```txt
Si solo se necesita una puerta de entrada simple,
evaluar Facade antes que Manager.
```

---

## No crear un Manager cuando corresponde un Event Queue u Observer

Si el problema es comunicación entre sistemas, puede corresponder Observer o Event Queue.

Ejemplo:

```txt
Cuando cambia el dinero, la UI debe actualizarse.
Cuando muere un enemigo, se suma recompensa.
Cuando termina una oleada, se habilita siguiente fase.
```

Esto puede resolverse con eventos.

No necesariamente requiere un manager nuevo.

```txt
Evento:
MoneyChanged

Listeners:
HUD,
Audio,
Analytics,
Tutorial.
```

Criterio:

```txt
Si el problema es notificar cambios,
evaluar eventos antes que Manager.
```

---

## No crear un Manager cuando corresponde una State Machine

Si el problema es manejar estados y transiciones, probablemente corresponde una State o una state machine.

Ejemplos:

```txt
MainMenu
LevelSelect
Playing
Paused
Win
Lose
Loading
```

Un `GameManager` puede coordinar la state machine, pero no debería absorber todos los estados como métodos gigantes.

Mejor:

```txt
GameStateMachine
→ administra estados y transiciones.

GameManager
→ coordina estado global mínimo.
```

Criterio:

```txt
Si el problema son estados,
evaluar State Machine antes que Manager gigante.
```

---

## No crear un Manager cuando corresponde un Object Pool

Si el problema es reutilizar objetos, corresponde Object Pool.

Ejemplo:

```txt
Proyectiles,
partículas,
enemigos frecuentes,
objetos temporales,
efectos visuales.
```

Puede existir un `PoolManager`, pero su responsabilidad debe ser administrar pools, no reemplazar el patrón.

No debería hacer:

```txt
calcular daño,
decidir disparo,
elegir objetivo,
manejar economía,
actualizar UI.
```

Criterio:

```txt
Si el problema es reutilización de objetos,
evaluar Pool antes que Manager genérico.
```

---

## No crear un Manager por acceso global cómodo

Crear un manager singleton solo para acceder fácil suele generar acoplamiento.

Mala justificación:

```txt
Lo hago singleton así cualquiera lo llama.
```

Problemas:

```txt
dependencias ocultas,
difícil testeo,
orden de inicialización frágil,
acoplamiento global,
difícil refactor,
referencias persistentes peligrosas.
```

Mejor evaluar:

```txt
referencias por Inspector,
inyección manual,
eventos,
facade,
composition root,
contexto de nivel,
o dependencia explícita.
```

Regla:

```txt
Acceso fácil no es justificación arquitectónica suficiente.
```

---

## No crear un Manager si va a romper SOLID

No conviene crear un manager si desde el inicio va a tener muchas razones para cambiar.

Mala señal:

```txt
Este manager va a manejar:
UI,
audio,
spawn,
economía,
guardado,
niveles,
input,
assets,
y eventos.
```

Eso viola S - Single Responsibility Principle antes de empezar.

También puede violar I - Interface Segregation Principle si expone una API enorme.

Criterio:

```txt
Si el manager nace grande,
nace mal.
```

---

## No crear un Manager cuando todavía no existe el problema

En prototipos es común anticiparse demasiado.

Ejemplo:

```txt
Todavía hay 2 sonidos,
pero se crea un AudioManager complejo.

Todavía hay 3 prefabs,
pero se crea AssetManager con Addressables.

Todavía hay pocos objetos,
pero se crea UpdateManager con prioridades, grupos y frecuencia.
```

A veces puede ser correcto preparar arquitectura.

Pero si la complejidad supera el beneficio, no conviene.

Criterio:

```txt
No sobrearquitecturar por miedo al futuro.
Diseñar un camino de crecimiento, no una solución gigante anticipada.
```

---

## Criterio para IA/agente

Una IA no debería proponer un manager si no puede descartar alternativas.

Debe responder:

```txt
¿Por qué no alcanza una clase común?
¿Por qué no corresponde Factory?
¿Por qué no corresponde Facade?
¿Por qué no corresponde Event Queue?
¿Por qué no corresponde State Machine?
¿Por qué no corresponde Object Pool?
¿Por qué no basta una referencia explícita?
```

Si no puede responder eso, no debe crear el manager.

Respuesta incorrecta:

```txt
Voy a crear un Manager para centralizar.
```

Respuesta correcta:

```txt
No propongo manager todavía.
El problema es solo creación de enemigos.
Corresponde revisar EnemyFactory antes de crear EnemyManager.
```

---

## Ejemplo aplicado a videojuegos

Problema:

```txt
Las torres necesitan crear proyectiles.
```

Mala solución:

```txt
TowerManager
→ crea proyectiles,
→ calcula daño,
→ controla torres,
→ actualiza UI,
→ reproduce sonido,
→ controla upgrades.
```

Mejor análisis:

```txt
Tower
→ detecta objetivo y decide disparar.

ProjectileFactory
→ crea proyectiles si se instancian.

ProjectilePoolManager
→ reutiliza proyectiles si hay pooling.

DamageSystem
→ aplica daño.

AudioManager
→ reproduce sonido.

UI
→ escucha eventos si necesita mostrar cambios.
```

No hacía falta un `TowerManager` gigante.

---

## Checklist para NO crear un Manager

Antes de evitar o rechazar un manager:

```txt
¿La responsabilidad es vaga?
¿El problema se resuelve con una clase simple?
¿El problema es solo creación?
¿El problema es solo comunicación?
¿El problema es solo estado?
¿El problema es solo reutilización?
¿El problema es acceso cómodo?
¿El manager nacería con demasiadas responsabilidades?
¿No hay evidencia de necesidad real?
¿Se está intentando tapar una clase dios con otra?
```

Si varias respuestas son “sí”, no crear el manager.

---

## Regla final

No crear un manager también es una decisión arquitectónica.

```txt
Crear manager sin criterio
→ más acoplamiento.

Evitar manager innecesario
→ arquitectura más clara.
```

La mejor arquitectura no es la que tiene más managers.

Es la que tiene responsabilidades mejor separadas.
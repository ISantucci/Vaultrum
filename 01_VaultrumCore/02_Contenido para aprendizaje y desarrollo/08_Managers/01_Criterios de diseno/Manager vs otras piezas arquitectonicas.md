## Propósito dentro de Vaultrum

Este documento define cómo diferenciar un manager de otras piezas arquitectónicas.

El objetivo es evitar que una IA o un desarrollador llame `Manager` a cualquier clase que coordina, crea, comunica, ejecuta o almacena algo.

En Vaultrum, un manager debe tener una responsabilidad de administración clara.

Pero muchas veces la solución correcta es otra pieza:

```txt
Factory
Facade
Object Pool
State Machine
Service Locator
Command Invoker
Event Queue
Observer
System
Repository
Registry
Clase pura
```

La idea principal es:

```txt
Antes de crear un Manager,
identificar qué tipo de problema existe.
```

---

## Manager vs Factory

Una Factory se encarga de crear objetos.

Un manager administra una responsabilidad más amplia.

```txt
Factory
→ crea.

Manager
→ administra ciclo, acceso, coordinación o estado.
```

Ejemplo:

```txt
EnemyFactory
→ crea enemigos según EnemyData.

EnemyManager
→ solo tendría sentido si administra ciclo de vida, registro o coordinación global de enemigos.
```

Mala señal:

```txt
EnemyManager crea enemigos porque no existe EnemyFactory.
```

Criterio:

```txt
Si el problema es creación,
primero evaluar Factory.
```

---

## Manager vs Facade

Una Facade simplifica el acceso a varios subsistemas.

Un manager administra una responsabilidad.

```txt
Facade
→ expone una puerta de entrada simple.

Manager
→ posee o administra una responsabilidad concreta.
```

Ejemplo:

```txt
GameplayFacade
→ permite que UI pida acciones de gameplay sin conocer todos los subsistemas.

GameManager
→ administra estado general de partida.
```

Una facade puede coordinar llamadas, pero no necesariamente posee estado ni ciclo de vida.

Criterio:

```txt
Si el problema es simplificar acceso,
evaluar Facade.

Si el problema es administrar ciclo, estado o recursos,
evaluar Manager.
```

---

## Manager vs Object Pool

Un Object Pool reutiliza objetos.

Un manager puede administrar uno o varios pools, pero no es el patrón en sí.

```txt
Object Pool
→ patrón de reutilización.

PoolManager
→ sistema que administra pools.
```

Ejemplo:

```txt
ProjectilePool
→ contiene proyectiles reutilizables.

ProjectilePoolManager
→ administra acceso, inicialización y reset de pools de proyectiles.
```

Responsabilidad prohibida:

```txt
PoolManager no debería decidir daño,
targeting,
economía,
ni lógica de disparo.
```

Criterio:

```txt
Si el problema es reutilización,
evaluar Pool.

Si además hay varios pools o ciclo global de pools,
puede aparecer PoolManager.
```

---

## Manager vs State Machine

Una State Machine organiza estados y transiciones.

Un manager puede poseer una state machine o delegar en ella, pero no debería reemplazarla con condicionales gigantes.

```txt
State Machine
→ organiza estados.

Manager
→ puede coordinar el sistema que usa esos estados.
```

Ejemplo:

```txt
GameStateMachine
→ MainMenu, Playing, Paused, Win, Lose.

GameManager
→ coordina estado global y delega transiciones.
```

Mala señal:

```txt
GameManager tiene if/else gigantes para todos los estados del juego.
```

Criterio:

```txt
Si el problema son estados y transiciones,
evaluar State Machine.
```

---

## Manager vs Service Locator

Un Service Locator permite localizar servicios.

Un manager administra una responsabilidad.

```txt
Service Locator
→ acceso a servicios registrados.

Manager
→ lógica de administración de un dominio.
```

Ejemplo:

```txt
ServiceLocator.Get<IAudioService>()
→ obtiene servicio.

AudioManager
→ administra reproducción y configuración de audio.
```

Peligro:

```txt
Usar Service Locator para ocultar dependencias de managers.
```

Criterio:

```txt
Si el problema es acceso a dependencias,
evaluar inyección, referencias explícitas o Service Locator.

Si el problema es responsabilidad administrada,
evaluar Manager.
```

---

## Manager vs Command Invoker

Un invoker del patrón Command ejecuta comandos.

Un manager administra una responsabilidad más general.

```txt
Command Invoker
→ ejecuta, registra, deshace o rehace comandos.

Manager
→ administra estado, recursos o ciclo de un sistema.
```

Ejemplo:

```txt
BuildInvoker
→ ejecuta PlaceTowerCommand, SellTowerCommand, UpgradeTowerCommand.

BuildManager
→ solo tendría sentido si administra ciclo o estado global de construcción.
```

Criterio:

```txt
Si el problema es ejecutar acciones reversibles,
evaluar Command e Invoker.
```

---

## Manager vs Event Queue

Un Event Queue encola eventos para procesarlos luego.

Un manager puede administrar la cola, pero la cola es el patrón principal.

```txt
Event Queue
→ desacopla emisión y procesamiento en el tiempo.

EventQueueManager
→ administra la cola, procesamiento y reglas de despacho.
```

Ejemplo:

```txt
Command
→ encola evento de dinero.

EventQueueManager
→ procesa evento.

GameEvents
→ notifica a UI.
```

Criterio:

```txt
Si el problema es orden temporal o desacople de eventos,
evaluar Event Queue.
```

---

## Manager vs Observer

Observer permite notificar cambios a suscriptores.

Un manager puede emitir eventos, pero no debería transformarse en canal universal de comunicación.

```txt
Observer
→ notifica cambios.

Manager
→ administra una responsabilidad.
```

Ejemplo:

```txt
GameManager cambia estado.
GameEvents.RaiseGameStateChanged().
UI escucha.
Audio escucha si corresponde.
```

Criterio:

```txt
Si el problema es notificar cambios,
evaluar Observer antes que Manager nuevo.
```

---

## Manager vs System

Un system puede representar una lógica específica del juego.

Un manager administra ciclo, acceso o coordinación de una responsabilidad compartida.

```txt
CombatSystem
→ resuelve reglas de combate.

DamageSystem
→ aplica daño.

EconomySystem
→ administra economía.

Manager
→ puede coordinar sistemas, pero no necesariamente reemplazarlos.
```

A veces el nombre `System` es más correcto que `Manager`.

Ejemplo:

```txt
EconomySystem
→ mejor que EconomyManager si solo administra reglas económicas internas.

DamageSystem
→ mejor que DamageManager si aplica reglas de daño.
```

Criterio:

```txt
Si la clase representa reglas de dominio,
puede ser System.

Si administra acceso, ciclo o coordinación transversal,
puede ser Manager.
```

---

## Manager vs Repository / Registry

Un repository o registry guarda y permite consultar datos o entidades.

Un manager puede usarlo, pero no debería confundirse con él.

```txt
Repository
→ acceso a datos.

Registry
→ registro y consulta de entidades.

Manager
→ administración de responsabilidad.
```

Ejemplo:

```txt
EnemyRegistry
→ sabe qué enemigos están activos.

EnemyManager
→ solo tendría sentido si además administra ciclo, spawn, limpieza o coordinación.
```

Criterio:

```txt
Si el problema es consultar o registrar entidades,
evaluar Registry o Repository.
```

---

## Manager vs clase pura

Una clase pura no depende directamente de Unity y suele resolver lógica puntual.

Ejemplos:

```txt
DamageCalculator
TargetSelector
UpgradeCostCalculator
PathCostEvaluator
SpawnWaveParser
```

No todo merece manager.

Criterio:

```txt
Si solo calcula, valida o transforma datos,
usar clase pura antes que Manager.
```

Esto también ayuda a optimización y testeo.

---

## Relación con SOLID

Distinguir managers de otras piezas ayuda a mantener SOLID.

```txt
SRP
→ cada pieza tiene una razón clara para cambiar.

OCP
→ factories, strategies y state machines permiten extender sin modificar managers.

ISP
→ managers no exponen APIs gigantes.

DIP
→ managers pueden depender de abstracciones cuando corresponde.
```

Cuando un manager reemplaza a todas las demás piezas, SOLID se rompe.

Ejemplo de violación:

```txt
GameManager
→ crea objetos,
→ guarda datos,
→ emite eventos,
→ actualiza UI,
→ calcula daño,
→ maneja estados,
→ reproduce audio.
```

Cada una de esas responsabilidades podría pertenecer a una pieza distinta.

---

## Criterio para IA/agente

Antes de proponer un manager, la IA debe clasificar el problema:

```txt
¿Es creación?
→ Factory.

¿Es simplificación de acceso?
→ Facade.

¿Es reutilización?
→ Object Pool.

¿Es estado y transición?
→ State Machine.

¿Es comunicación?
→ Observer / Event Queue.

¿Es ejecución de acciones?
→ Command Invoker.

¿Es consulta de entidades?
→ Registry / Repository.

¿Es cálculo puntual?
→ clase pura.

¿Es administración central con ciclo, acceso o coordinación?
→ posible Manager.
```

Esta clasificación debe aparecer explícitamente en la respuesta de la IA.

---

## Ejemplo aplicado a videojuegos

Problema:

```txt
La UI necesita colocar, vender y mejorar torres.
```

Mala solución:

```txt
UIManager hace todo:
coloca torre,
vende torre,
mejora torre,
modifica dinero,
actualiza HUD,
crea efectos.
```

Mejor separación:

```txt
UI
→ captura intención del jugador.

GameplayFacade
→ expone operaciones de gameplay.

BuildInvoker
→ ejecuta comandos.

TowerFactory
→ crea torres.

GameManager / EconomySystem
→ valida dinero.

GameEvents
→ notifica cambios.

HUD
→ actualiza visualmente.
```

Criterio:

```txt
No todo lo que conecta sistemas debe ser Manager.
```

---

## Checklist de decisión

Antes de elegir Manager:

```txt
¿El problema es creación?
¿El problema es acceso simplificado?
¿El problema es reutilización?
¿El problema es estados?
¿El problema es eventos?
¿El problema es comandos?
¿El problema es consulta de entidades?
¿El problema es cálculo puro?
¿El problema es administración central real?
¿Se puede separar en varias piezas más chicas?
```

---

## Regla final

Manager es una opción, no una respuesta automática.

```txt
Primero clasificar el problema.
Después elegir la pieza arquitectónica.
Finalmente decidir si hace falta un manager.
```

Un manager sano no reemplaza patrones.

Los usa o coordina cuando corresponde.
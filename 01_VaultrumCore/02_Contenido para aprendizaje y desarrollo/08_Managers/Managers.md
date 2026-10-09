## Propósito de esta sección

Esta sección de Vaultrum define cómo diseñar, analizar y auditar managers en proyectos de videojuegos.

El objetivo no es crear una lista de clases llamadas `Manager`.

El objetivo es establecer criterios claros para decidir:

```txt
cuándo un manager tiene sentido,
qué responsabilidad debe tener,
qué responsabilidades debe rechazar,
cómo integrarlo con Unity,
cómo evitar que se vuelva una clase dios,
y cómo pedirle a una IA que lo implemente o lo audite sin romper arquitectura.
```

Un manager bien diseñado puede acelerar el desarrollo de prototipos, ordenar sistemas complejos y facilitar automatizaciones.

Un manager mal diseñado puede convertirse rápidamente en el lugar donde termina todo el código que no sabemos dónde poner.

---

## Qué busca resolver esta sección

En proyectos de videojuegos es común que aparezcan sistemas centrales:

```txt
GameManager
LevelManager
UpdateManager
AssetManager
UIManager
AudioManager
SaveManager
PoolManager
EventQueueManager
StateMachineManager
```

El problema no es que existan managers.

El problema aparece cuando no está claro:

```txt
qué administra cada uno,
cuándo se inicializa,
quién lo usa,
qué otros sistemas coordina,
qué datos posee,
qué eventos emite,
qué referencias conserva,
qué NO debería hacer.
```

Esta sección busca evitar ese desorden.

La idea central es:

```txt
Un Manager no existe para guardar código que no sabemos dónde poner.

Existe para administrar una responsabilidad central, transversal o repetida,
con límites claros, una API mínima y un ciclo de vida definido.
```

---

## Cómo usar esta sección

Esta sección está pensada para tres usos principales.

### 1. Para aprender arquitectura

Sirve para entender qué es un manager y cómo se diferencia de otras piezas arquitectónicas.

Ejemplos:

```txt
Manager vs Singleton
Manager vs Facade
Manager vs Factory
Manager vs Service Locator
Manager vs Object Pool
Manager vs State Machine
```

Esto evita confusiones comunes.

Por ejemplo:

```txt
Un manager puede ser singleton,
pero no todo singleton es un manager.

Una facade puede coordinar acceso,
pero no necesariamente administra ciclo de vida.

Una factory crea objetos,
pero no debería administrar todo el estado del juego.

Un pool reutiliza objetos,
pero no debería decidir reglas de gameplay.
```

---

### 2. Para diseñar sistemas nuevos

Sirve como guía antes de crear un manager.

Antes de crear uno, se debe poder responder:

```txt
¿Qué problema concreto resuelve?
¿Por qué no alcanza con una clase común?
¿Por qué no corresponde usar Factory, Facade, Strategy, Event Queue, Pool o State Machine?
¿Qué responsabilidad exacta administra?
¿Qué responsabilidades quedan fuera?
¿Qué API mínima necesita?
¿Cómo se inicializa?
¿Cómo se destruye o limpia?
¿Sobrevive entre escenas?
¿Qué riesgos introduce?
```

Si esas preguntas no tienen respuesta, probablemente todavía no conviene crear un manager.

---

### 3. Para trabajar con IA/agentes

Esta sección está pensada para que una IA pueda analizar un proyecto y actuar con criterio.

Una IA que use esta sección debería poder:

```txt
detectar managers existentes,
identificar managers innecesarios,
detectar clases dios,
separar responsabilidades mezcladas,
proponer managers nuevos solo cuando estén justificados,
definir APIs mínimas,
respetar ciclo de vida de Unity,
evitar singletons por comodidad,
evitar referencias viejas entre escenas,
y proponer cambios incrementales.
```

Regla para IA/agentes:

```txt
Antes de crear o modificar un Manager, una IA debe justificar:
qué problema resuelve,
por qué corresponde un manager,
qué alternativas descartó,
qué responsabilidades acepta,
qué responsabilidades rechaza,
qué archivos tocaría,
qué archivos no tocaría,
y cómo se validará que no rompió arquitectura.
```

---

## Organización de la sección

La sección se divide en cuatro partes.

```txt
05_Managers/
│
├── Managers.md
│
├── 01_Criterios de diseño/
│
├── 02_Diseño práctico/
│
├── 03_Managers/
│
└── 04_Auditoría para IA/
```

---

## 01_Criterios de diseño

Esta carpeta define cuándo un manager tiene sentido.

No se enfoca en managers específicos, sino en criterios de decisión.

Incluye documentos como:

- [[Que es un Manager|Qué es un Manager]]
- [[Que problema resuelve un manager|Qué problema resuelve un Manager]]
- [[Cuando crear un Manager|Cuándo crear un Manager]]
- [[Cuando NO crear un Manager|Cuándo NO crear un Manager]]
- [[Manager vs otras piezas arquitectonicas|Manager vs otras piezas arquitectónicas]]
- [[Responsabilidad unica en managers|Responsabilidad única en Managers]]
- [[Riesgo de manager Dios|Riesgo de Manager Dios]]

Esta carpeta responde preguntas como:

```txt
¿Esto realmente necesita ser un manager?
¿Estoy creando un manager por necesidad o por costumbre?
¿La responsabilidad es clara?
¿Estoy mezclando sistemas?
¿Estoy creando una clase dios?
```

---

## 02_Diseño práctico

Esta carpeta explica cómo diseñar managers sanos en proyectos reales.

Incluye documentos como:

- [[Como diseñar un manager sano|Cómo diseñar un Manager sano]]
- [[API minima de un manager|API mínima de un Manager]]
- [[Ciclo de vida de un Manager]]
- [[Managers persistentes entre escenas]]
- [[Managers y Unity]]
- [[Managers y eventos]]
- [[managers y optimizacion|Managers y optimización]]
- [[Mantener un Manager SOLID]]
- [[Checklist para pedirle un Manager a una IA]]

Esta carpeta responde preguntas como:

```txt
¿Cómo debería inicializarse un manager?
¿Qué métodos públicos debería exponer?
¿Cómo evito que tenga demasiadas responsabilidades?
¿Cómo se conecta con eventos?
¿Cómo se mantiene testeable?
¿Cómo evito referencias destruidas al cambiar de escena?
¿Cómo hago que una IA lo implemente sin sobrearquitecturar?
```

---

## 03_Managers

Esta carpeta contiene managers concretos.

Cada documento define un tipo de manager, su responsabilidad, cuándo usarlo, cuándo evitarlo y cómo auditarlo.

Managers previstos:

- [[GameManager]]
- [[LevelManager]]
- [[StateMachineManager]]
- [[UpdateManager]]
- [[AssetManager]]
- [[UIManager]]
- [[AudioManager]]
- [[SaveManager]]
- [[PoolManager]]
- [[EventQueueManager]]

Estos documentos no deben ser solo definiciones.

Deben funcionar como guías de diseño aplicables.

Cada manager debe responder:

```txt
qué problema resuelve,
qué responsabilidades puede tener,
qué responsabilidades tiene prohibidas,
cómo se relaciona con otras piezas,
qué ciclo de vida necesita,
qué API mínima conviene,
qué errores suelen aparecer,
y qué debe revisar una IA antes de tocarlo.
```

---

## 04_Auditoría para IA

Esta carpeta está pensada para análisis de proyectos existentes.

Incluye documentos como:

- [[Como auditar Managers en un proyecto|Cómo auditar Managers en un proyecto]]
- [[Como detectar Managers innecesarios|Cómo detectar Managers innecesarios]]
- [[Como refactorizar una clase dios|Cómo refactorizar una clase dios]]
- [[Como proponer Managers sin sobrearquitecturar|Cómo proponer Managers sin sobrearquitecturar]]
- [[Prompt base para analisis de managers|Prompt base para análisis de Managers]]
- [[Optimizacion arquitectonica de Managers|Optimización arquitectónica de Managers]]

Esta carpeta debe permitir que una IA reciba un proyecto y haga un análisis ordenado.

Flujo esperado:

```txt
1. Detectar managers existentes.
2. Identificar responsabilidades reales.
3. Detectar responsabilidades mezcladas.
4. Separar manager, facade, factory, pool, service, state machine y event queue.
5. Detectar managers innecesarios.
6. Detectar clases dios.
7. Proponer refactors incrementales.
8. Indicar riesgos.
9. Indicar archivos afectados.
10. Proponer validación posterior.
```

---

## Qué es un Manager dentro de Vaultrum

Dentro de Vaultrum, un manager es una pieza arquitectónica que administra una responsabilidad centralizada.

Puede administrar:

```txt
estado global limitado,
ciclo de vida,
recursos,
eventos,
actualizaciones,
niveles,
audio,
guardado,
UI,
pools,
assets,
flujo de juego.
```

Pero no debe absorber cualquier responsabilidad por comodidad.

Un manager sano tiene límites.

Ejemplo:

```txt
AssetManager
→ administra carga, cache y liberación de assets.

No:
→ decide gameplay,
→ instancia enemigos,
→ maneja oleadas,
→ modifica UI,
→ guarda partida.
```

Otro ejemplo:

```txt
GameManager
→ coordina estado global de partida.

No:
→ calcula daño,
→ controla toda la UI,
→ instancia todos los enemigos,
→ reproduce audio,
→ carga todos los assets,
→ contiene toda la lógica de niveles.
```

---

## Qué NO es un Manager

No todo sistema importante es un manager.

Ejemplos:

```txt
Factory
→ crea objetos.

Facade
→ simplifica acceso a subsistemas.

State Machine
→ organiza estados y transiciones.

Object Pool
→ reutiliza objetos.

Service Locator
→ permite localizar servicios.

Command Invoker
→ ejecuta comandos.

Sistema de datos
→ organiza o consulta información.
```

Algunos de estos sistemas pueden estar contenidos o coordinados por managers, pero no son managers automáticamente.

Ejemplo:

```txt
ProjectilePoolManager
→ puede administrar un pool de proyectiles.

Object Pool
→ es el patrón de reutilización.

ProjectileFactory
→ crea proyectiles.

Tower
→ solicita disparo.

Cada pieza tiene una responsabilidad distinta.
```

---

## Relación con SOLID

Los managers son especialmente peligrosos para SOLID porque tienden a crecer.

Un manager sano debe respetar:

```txt
Single Responsibility Principle
→ una responsabilidad central clara.

Open/Closed Principle
→ extensible sin modificarlo todo.

Liskov Substitution Principle
→ si usa abstracciones, deben ser reemplazables correctamente.

Interface Segregation Principle
→ no exponer interfaces gigantes.

Dependency Inversion Principle
→ depender de abstracciones cuando corresponda.
```

La regla más importante suele ser SRP:

```txt
Si un manager cambia por muchas razones distintas,
probablemente está absorbiendo demasiadas responsabilidades.
```

Ejemplo de alerta:

```txt
GameManager cambia cuando:
se modifica UI,
se cambia economía,
se cambia audio,
se cambia guardado,
se cambia spawn,
se cambia pathfinding,
se cambia pause,
se cambia daño.

Resultado:
GameManager está funcionando como clase dios.
```

---

## Relación con Unity

En Unity, los managers suelen estar conectados con:

```txt
MonoBehaviour
Awake
Start
Update
SceneManager
DontDestroyOnLoad
Inspector
ScriptableObject
GameObject
eventos
escenas
prefabs
```

Esto introduce riesgos específicos.

Regla importante:

```txt
No llamar manualmente Awake, Start ni Update.
```

Si un manager necesita reiniciarse, debe tener métodos explícitos:

```txt
Initialize
ResetState
BindSceneReferences
UnbindSceneReferences
EnterLevel
ExitLevel
Shutdown
```

Ejemplo:

```txt
Incorrecto:
GameManager.Awake() llamado manualmente para reiniciar estado.

Correcto:
GameManager.ResetState() o GameManager.EnterLevel(levelData).
```

---

## Managers persistentes

Un manager persistente puede sobrevivir entre escenas.

Eso puede ser útil para:

```txt
GameManager
AudioManager
AssetManager
SaveManager
UpdateManager
```

Pero también puede ser peligroso.

Regla:

```txt
Un manager persistente no debería retener referencias directas a objetos de escena destruidos.
```

Ejemplo de riesgo:

```txt
UIManager persiste.
HUD_Canvas pertenece a la escena.
La escena cambia.
HUD_Canvas se destruye.
UIManager conserva referencia vieja.
```

Solución posible:

```txt
limpiar referencias al salir de escena,
rebind controlado al cargar escena,
usar eventos,
separar estado persistente de objetos visuales de escena.
```

---

## Managers y eventos

Los managers suelen comunicarse bien mediante eventos.

Ejemplo:

```txt
GameManager cambia vida
→ emite HealthChanged

HUD escucha
→ actualiza barra de vida
```

Esto evita que el manager conozca detalles de UI.

Pero los eventos también tienen riesgos:

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
Pero no debería depender de que todos los sistemas estén acoplados directamente a él.
```

---

## Managers y optimización

Un manager puede ayudar a optimizar cuando administra una responsabilidad relacionada con runtime.

Ejemplos:

```txt
UpdateManager
→ controla frecuencia de actualización.

AssetManager
→ controla carga y descarga de assets.

PoolManager
→ controla reutilización de objetos.

UIManager
→ evita actualizaciones innecesarias.

EventQueueManager
→ ordena procesamiento de eventos.
```

Pero un manager también puede empeorar rendimiento si:

```txt
tiene un Update gigante,
hace búsquedas globales,
procesa todo cada frame,
retiene memoria innecesaria,
centraliza demasiada lógica,
genera dependencias innecesarias.
```

Regla:

```txt
Un manager no es automáticamente una optimización.
Solo optimiza si reduce trabajo innecesario, mejora ciclo de vida o controla recursos.
```

---

## Criterio para crear un Manager

Crear un manager puede ser correcto si existe al menos una de estas razones:

```txt
Hay una responsabilidad transversal.
Hay un ciclo de vida que administrar.
Hay recursos compartidos.
Hay estado global limitado.
Hay acceso que debe centralizarse.
Hay sistemas que necesitan coordinación.
Hay lógica repetida que debe unificarse.
Hay una necesidad clara de persistencia.
```

No conviene crear un manager si:

```txt
solo se quiere evitar pasar referencias,
la responsabilidad no está clara,
la clase sería un contenedor genérico,
la lógica pertenece a una entidad específica,
una factory, facade, pool, service o state machine sería más adecuada,
o todavía no existe un problema real.
```

---

## Criterio para IA/agentes

Cuando una IA trabaje sobre managers, debe evitar respuestas vagas como:

```txt
"Crearía un Manager para ordenar esto."
```

Debe justificar:

```txt
Qué desorden detectó.
Qué responsabilidad concreta propone centralizar.
Qué alternativas evaluó.
Por qué corresponde un manager.
Qué API mínima tendría.
Qué archivos se modificarían.
Qué riesgos aparecen.
Cómo se validaría el cambio.
```

Respuesta esperada de una IA:

```txt
Detecté que la lógica de carga de assets está repetida en tres sistemas.
Esto no corresponde a Factory porque no se trata solo de crear objetos.
Tampoco corresponde a Facade porque hace falta administrar ciclo de vida y cache.
Propongo AssetManager con responsabilidad limitada a cargar, cachear y liberar assets.
No debe instanciar enemigos ni decidir gameplay.
```

---

## Formato recomendado para managers concretos

Cada manager dentro de `03_Managers` debería seguir este formato:

```md
# Nombre

## Descripción
## Qué problema resuelve
## Cuándo conviene usarlo
## Cuándo NO conviene usarlo
## Responsabilidades permitidas
## Responsabilidades prohibidas
## Relación con otras piezas arquitectónicas
## Ciclo de vida
## API mínima recomendada
## Ejemplo aplicado a videojuegos
## Errores comunes
## Checklist para IA/agente
## Regla final
```

Algunos managers pueden tener secciones extra si lo justifican.

Ejemplo:

```txt
GameManager
→ relación con UI, eventos, State Machine y LevelManager.

UpdateManager
→ frecuencia, grupos, orden de ejecución.

AssetManager
→ Addressables, cache, handles y liberación.

PoolManager
→ reset, reutilización y ciclo de vida de objetos.
```

---

## Regla final

Un manager debe existir por una razón arquitectónica concreta.

No por costumbre.

```txt
Manager sano
→ responsabilidad clara
→ API mínima
→ ciclo de vida definido
→ límites explícitos
→ integración controlada

Manager peligroso
→ hace de todo
→ todos dependen de él
→ crece sin límite
→ mezcla gameplay, UI, datos, recursos y flujo
```

La función de esta sección es evitar el segundo caso y facilitar el primero.
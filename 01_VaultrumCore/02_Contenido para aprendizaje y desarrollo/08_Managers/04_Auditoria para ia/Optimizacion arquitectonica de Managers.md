## Objetivo

Este documento define cómo analizar y optimizar managers y clases `MonoBehaviour` en un proyecto Unity para lograr una arquitectura más robusta, más SOLID, más testeable y más eficiente.

No se trata únicamente de mejorar FPS.

Se trata de mejorar la arquitectura para que el sistema tenga:

```txt
menos acoplamiento,
menos lógica mezclada,
menos dependencia directa de Unity,
menos Updates innecesarios,
menos managers gigantes,
más clases puras,
mejor separación de responsabilidades,
mejor capacidad de testeo,
mejor mantenibilidad,
y mejor base para automatización con IA.
```

La idea central es:

```txt
Unity conecta.
MonoBehaviour integra.
Managers administran.
Clases puras resuelven lógica.
Eventos comunican.
Interfaces reducen acoplamiento cuando aportan valor.
```

---

## Meta del refactor

La meta no es eliminar todos los `MonoBehaviour`.

La meta tampoco es convertir todo en interfaces, servicios abstractos o capas innecesarias.

La meta es ubicar cada responsabilidad en el lugar correcto.

Resultado esperado:

```txt
MonoBehaviour
→ queda como adaptador de Unity.

Manager
→ queda como administrador de una responsabilidad concreta.

Clase pura
→ contiene reglas, cálculos, validaciones y decisiones.

Eventos
→ comunican cambios relevantes.

Interfaces
→ aparecen solo cuando reducen acoplamiento real.

Sistemas específicos
→ contienen lógica de dominio que no pertenece al manager.
```

Un refactor exitoso debería lograr:

```txt
menos lógica dentro de MonoBehaviour,
menos responsabilidades mezcladas en managers,
menos Update innecesario,
menos dependencias globales,
menos uso de singleton por comodidad,
más lógica testeable,
más API mínima,
más separación SOLID,
mismo comportamiento observable en Unity.
```

La optimización arquitectónica no busca “más arquitectura”.

Busca menos confusión.

---

## Qué problema busca detectar

Este documento sirve para detectar proyectos donde los managers o MonoBehaviours están haciendo demasiado.

Casos comunes:

```txt
GameManager controla todo el juego.
UIManager decide gameplay.
LevelManager carga assets, spawnea enemigos y actualiza HUD.
UpdateManager contiene lógica específica de cada sistema.
AudioManager escucha eventos que no pertenecen a audio.
SaveManager conoce objetos de escena.
MonoBehaviours calculan reglas complejas directamente.
Clases con Update hacen trabajo que podría reducirse.
Managers persisten entre escenas con referencias viejas.
La lógica no se puede testear fuera de Unity.
Todo depende de GameObject, Transform, Scene, Inspector o singleton.
```

El problema no es usar `MonoBehaviour`.

El problema es usarlo como contenedor de toda la lógica.

---

## Idea central

En Unity, `MonoBehaviour` es necesario para interactuar con el motor.

Pero no toda la lógica del juego necesita vivir dentro de `MonoBehaviour`.

Separación recomendada:

```txt
MonoBehaviour
→ lifecycle de Unity,
→ Inspector,
→ referencias de escena,
→ callbacks,
→ coroutines si hacen falta,
→ puente con el motor.

Manager
→ administra una responsabilidad concreta,
→ coordina ciclo de vida,
→ expone API mínima,
→ registra/desregistra,
→ emite o escucha eventos relevantes.

Clase pura
→ calcula,
→ valida,
→ decide,
→ transforma datos,
→ aplica reglas,
→ selecciona,
→ no depende de Unity si no hace falta.

Eventos
→ comunican cambios sin acoplar sistemas directamente.

Interfaces
→ reducen acoplamiento cuando hay varias implementaciones o consumidores distintos.
```

Regla:

```txt
Todo lo que no necesite Unity directamente debería poder evaluarse como candidato a clase pura.
```

---

## Qué debe quedar en MonoBehaviour

Un `MonoBehaviour` debería conservar responsabilidades ligadas al motor.

Puede encargarse de:

```txt
recibir callbacks de Unity,
exponer campos por Inspector,
referenciar objetos de escena,
leer input si corresponde,
activar/desactivar GameObjects,
usar Transform,
usar Rigidbody,
usar Collider,
usar Animator,
ejecutar Coroutines,
suscribirse/desuscribirse en OnEnable/OnDisable,
hacer binding con vistas de escena,
llamar a servicios o clases puras.
```

Ejemplo sano:

```csharp
public class TowerBehaviour : MonoBehaviour
{
    [SerializeField] private Transform firePoint;

    private TowerAttackController _attackController;

    private void Update()
    {
        _attackController.Tick(Time.deltaTime);
    }
}
```

Este `MonoBehaviour` conecta con Unity.

La lógica principal puede vivir en clases normales.

---

## Qué debería moverse a clases puras

Mover a clases puras todo lo que pueda existir sin depender directamente de Unity.

Candidatos típicos:

```txt
cálculo de daño,
cálculo de costos,
validación de compra,
selección de objetivo,
priorización de enemigos,
reglas de upgrade,
reglas de economía,
decisiones de IA,
evaluación de estados,
path cost,
ordenamiento,
parseo de datos,
validaciones,
reglas de victoria/derrota,
cálculo de recompensas,
formateo de datos,
resolución de decisiones.
```

Ejemplos:

```txt
DamageCalculator
UpgradeCostCalculator
TargetSelector
EnemyPriorityEvaluator
WaveRewardCalculator
PurchaseValidator
PathCostEvaluator
SaveDataMapper
GameStateRules
```

Regla:

```txt
Si una lógica puede recibir datos, procesarlos y devolver un resultado,
probablemente puede ser clase pura.
```

---

## Qué debe conservar un Manager

Un manager optimizado arquitectónicamente no desaparece necesariamente.

Se reduce a su responsabilidad real.

Debe conservar:

```txt
administración de ciclo de vida,
coordinación de alto nivel,
registro/desregistro,
acceso controlado a recursos,
API mínima,
eventos relevantes,
estado propio de su responsabilidad,
limpieza,
inicialización,
integración con otros sistemas desde límites claros.
```

No debe conservar:

```txt
cálculos específicos,
reglas internas de gameplay,
lógica de UI,
lógica de audio ajena,
lógica de guardado ajena,
creación de objetos que corresponde a Factory,
reutilización que corresponde a Pool,
estados que corresponden a State Machine,
comunicación que corresponde a eventos,
decisiones que corresponden a clases puras o estrategias.
```

Ejemplo:

```txt
PoolManager
→ conserva Get, Release, Clear, InitializePool.

No conserva:
→ daño,
→ targeting,
→ economía,
→ UI,
→ lógica de disparo.
```

---

## Qué NO debe hacer la IA

La IA no debe:

```txt
reescribir todo el sistema de una vez,
eliminar MonoBehaviours necesarios,
crear managers nuevos sin justificar,
convertir todo en singleton,
crear interfaces decorativas,
crear clases puras sin responsabilidad clara,
mover lógica sin explicar destino,
modificar escenas o prefabs sin avisar,
romper referencias del Inspector,
cambiar comportamiento observable,
mezclar refactor con features nuevas,
borrar código sin explicar impacto,
optimizar sin explicar qué costo reduce,
o asumir que toda separación mejora rendimiento.
```

Si la IA necesita tocar:

```txt
escenas,
prefabs,
ScriptableObjects,
configuración del Inspector,
Project Settings,
Addressables,
capas,
tags,
inputs,
animators,
colliders,
o referencias serializadas,
```

debe avisar antes y pedir aprobación.

---

## Señales de mala separación

Una IA o una persona debería sospechar mala separación si encuentra:

```txt
MonoBehaviour con demasiados métodos privados de reglas.
Manager con Update gigante.
Manager que hace cálculos de gameplay.
UIManager que modifica economía.
GameManager que reproduce audio directamente.
SaveManager que guarda GameObjects.
LevelManager que instancia todo.
AssetManager que decide spawn.
AudioManager que cambia escenas.
MonoBehaviour difícil de testear sin escena.
Clases que dependen de GameObject sin necesitarlo.
Uso de FindObjectOfType para resolver arquitectura.
Singleton usado para evitar pasar referencias.
Managers persistentes con referencias de escena.
```

Señal crítica:

```txt
Si no puedo probar la lógica sin abrir Unity,
tal vez demasiada lógica vive dentro de MonoBehaviour.
```

---

## Beneficios arquitectónicos

Separar managers y MonoBehaviours en clases puras puede aportar:

```txt
mejor separación de responsabilidades,
menos acoplamiento,
más claridad,
más facilidad para testear,
menos dependencia del orden de ejecución de Unity,
menos riesgo de clase dios,
más facilidad para usar IA en refactors,
más facilidad para reutilizar lógica,
más facilidad para detectar bugs,
más facilidad para cambiar implementación sin romper todo.
```

Una arquitectura más clara también mejora la capacidad de una IA para entender el proyecto.

La IA puede analizar mejor:

```txt
qué clase calcula,
qué clase coordina,
qué clase conecta con Unity,
qué clase comunica eventos,
qué clase administra recursos.
```

---

## Beneficios de optimización

Esta separación puede mejorar rendimiento directa o indirectamente.

Beneficios posibles:

```txt
menos Updates innecesarios,
menos búsquedas globales,
menos lógica pesada por frame,
menos allocations accidentales,
menos dependencia de GameObject.Find,
menos referencias persistentes inválidas,
menos trabajo repetido,
mejor cacheo,
mejor control de frecuencia,
mejor control de ciclo de vida,
mejor uso de Object Pool,
mejor uso de AssetManager,
mejor actualización UI orientada a eventos.
```

Importante:

```txt
Separar clases no optimiza automáticamente.
Optimiza si reduce trabajo innecesario, mejora frecuencia, limpia dependencias o evita operaciones costosas.
```

Ejemplo:

```txt
Antes:
UI actualiza texto de dinero en Update.

Después:
EconomySystem emite MoneyChanged.
HUD actualiza texto solo cuando cambia.
```

Eso sí es optimización.

---

## Relación con SOLID

Esta optimización arquitectónica está directamente relacionada con SOLID.

### Single Responsibility Principle

Cada pieza debe tener una razón clara para cambiar.

```txt
MonoBehaviour
→ cambia por integración Unity.

Manager
→ cambia por administración de su responsabilidad.

Clase pura
→ cambia por reglas de dominio.
```

Si una sola clase cambia por UI, audio, economía, daño, input y escenas, está rompiendo SRP.

---

### Open/Closed Principle

Separar lógica permite extender sin modificar managers constantemente.

Ejemplo:

```txt
TargetSelector usa estrategias de selección.
Agregar nueva estrategia no obliga a modificar TowerManager.
```

---

### Liskov Substitution Principle

Si un manager usa abstracciones, las implementaciones deben poder reemplazarse sin excepciones raras.

Ejemplo:

```txt
IUpdatable
→ cualquier implementación puede recibir Tick.

No:
UpdateManager con if target is Enemy, if target is Tower, if target is Projectile.
```

---

### Interface Segregation Principle

No crear interfaces gigantes para todo.

Mejor:

```txt
IUpdatable
IPausable
IInitializable
IResettable
ISaveable
```

En lugar de:

```txt
IManagedSystem
→ Initialize
→ Tick
→ Pause
→ Save
→ Load
→ BindUI
→ PlayAudio
```

---

### Dependency Inversion Principle

Los managers centrales no deberían depender de detalles concretos de todo el proyecto.

Ejemplo sano:

```txt
GameManager
→ emite GameStateChanged.
UIManager escucha.
AudioManager escucha.
```

Ejemplo peligroso:

```txt
GameManager
→ referencia directa a HUDCanvas,
→ referencia directa a MusicSource,
→ referencia directa a EnemySpawner,
→ referencia directa a SaveFileWriter,
→ referencia directa a TowerFactory,
→ referencia directa a Level1Controller.
```

Regla:

```txt
Cuanto más central es una clase,
menos detalles concretos debería conocer.
```

---

## Flujo de análisis para IA

Cuando una IA audite managers y MonoBehaviours, debe seguir este flujo:

```txt
1. Detectar managers y MonoBehaviours principales.
2. Identificar responsabilidades reales.
3. Separar responsabilidades Unity de responsabilidades de lógica.
4. Detectar lógica candidata a clase pura.
5. Detectar managers con demasiadas responsabilidades.
6. Detectar Updates innecesarios.
7. Detectar búsquedas globales.
8. Detectar dependencias a GameObjects sin necesidad.
9. Detectar referencias de escena en managers persistentes.
10. Proponer separación incremental.
11. Definir nuevas clases puras si aportan valor.
12. Definir qué queda en MonoBehaviour.
13. Definir qué queda en Manager.
14. Definir eventos o interfaces mínimas.
15. Definir validación técnica y funcional.
```

La IA no debe empezar escribiendo código.

Primero debe entregar diagnóstico y plan.

---

## Modo de implementación por fases

La IA debe trabajar en fases.

### Fase 1: análisis

```txt
No escribir código.
Detectar responsabilidades.
Separar lógica Unity de lógica pura.
Detectar riesgos.
Proponer plan.
Esperar aprobación.
```

### Fase 2: extracción mínima

```txt
Mover solo una lógica pura o responsabilidad pequeña.
Mantener comportamiento observable.
No tocar escenas ni prefabs.
Validar.
```

### Fase 3: integración

```txt
Conectar la nueva clase pura con el manager o MonoBehaviour.
Reducir API si corresponde.
Eliminar duplicación.
Mantener compatibilidad temporal si hace falta.
```

### Fase 4: limpieza

```txt
Eliminar wrappers temporales.
Eliminar métodos viejos.
Limpiar referencias.
Documentar deuda pendiente.
```

### Fase 5: validación

```txt
Probar en Unity.
Revisar consola.
Revisar comportamiento.
Revisar escenas afectadas.
Revisar referencias del Inspector.
Revisar profiler si el objetivo incluía rendimiento.
```

Regla:

```txt
Un refactor seguro avanza por pasos aprobados.
No por reescritura total.
```

---

## Clasificación de lógica

Durante la auditoría, clasificar cada método importante.

Formato recomendado:

```txt
Método:
...

Clase actual:
...

Qué hace:
...

Categoría:
- Integración Unity
- Administración de manager
- Lógica pura
- Comunicación/evento
- UI
- Audio
- Guardado
- Creación
- Pooling
- Estado
- Otro

Debe quedarse:
Sí / No

Destino recomendado:
...

Motivo:
...
```

Ejemplo:

```txt
Método:
CalculateDamage

Clase actual:
EnemyMonoBehaviour

Qué hace:
calcula daño final según armadura y multiplicador.

Categoría:
Lógica pura.

Debe quedarse:
No.

Destino recomendado:
DamageCalculator.

Motivo:
no necesita Unity, es testeable y pertenece a reglas de combate.
```

---

## Qué separar primero

No conviene separar todo de golpe.

Priorizar:

```txt
1. Cálculos puros.
2. Validaciones.
3. Selección o decisión.
4. Reglas de economía.
5. Reglas de daño.
6. Reglas de upgrades.
7. Actualizaciones UI por eventos.
8. Búsquedas globales reemplazables.
9. Lógica de Update reducible.
10. Responsabilidades completas que puedan extraerse a sistemas.
```

Evitar empezar por:

```txt
reescribir GameManager entero,
mover toda la arquitectura,
crear muchas interfaces nuevas,
cambiar escenas y prefabs masivamente,
modificar todos los sistemas a la vez.
```

Regla:

```txt
Primero extraer lógica pura de bajo riesgo.
Después atacar coordinación central.
```

---

## Formato de salida obligatorio para IA

La IA debe devolver el análisis con este formato:

```txt
# Auditoría de optimización arquitectónica

## Diagnóstico general

## Problema principal detectado

## Manager o MonoBehaviour analizado

## Rol actual
Manager / MonoBehaviour / Sistema / Otro

## Responsabilidad actual

## Responsabilidad correcta propuesta

## Qué debe quedarse en MonoBehaviour

## Qué debe salir de MonoBehaviour

## Qué debe quedarse en el Manager

## Qué debe salir del Manager

## Clases puras sugeridas

Para cada clase pura:
- Nombre:
- Responsabilidad:
- Inputs:
- Output:
- No depende de Unity porque:
- Cómo se testea:

## Managers o sistemas involucrados

## Eventos recomendados

## Interfaces recomendadas, solo si aportan valor

## Cambios de optimización esperados

## Riesgos

## Qué NO tocaría

## Plan incremental

### Paso 1: bajo riesgo
### Paso 2: riesgo medio
### Paso 3: requiere aprobación

## Validación en Unity
```

Si la IA no puede completar este formato, no está lista para implementar.

---

## Criterios de éxito

El refactor se considera exitoso si:

```txt
el comportamiento del juego se mantiene,
el manager tiene menos responsabilidades,
el MonoBehaviour queda más enfocado en Unity,
la lógica extraída puede probarse sin escena,
no se agregaron singletons innecesarios,
no se rompieron referencias del Inspector,
no se modificaron prefabs sin aviso,
la API pública se redujo o se mantuvo mínima,
los Updates innecesarios se eliminaron o redujeron,
las dependencias quedaron más explícitas,
SOLID mejoró sin sobrearquitectura.
```

No se considera exitoso si:

```txt
hay más capas pero la misma confusión,
se crean managers vacíos,
se agregan interfaces sin uso real,
el comportamiento cambia sin autorización,
se rompen referencias serializadas,
o el sistema queda más difícil de entender.
```

---

## Ejemplo aplicado a videojuegos

### Caso inicial

```txt
TowerManager : MonoBehaviour
→ busca enemigos con FindObjectsOfType,
→ elige el objetivo más cercano,
→ calcula daño,
→ instancia proyectil,
→ reproduce sonido,
→ actualiza UI de cooldown,
→ controla upgrades,
→ usa Update cada frame.
```

Problemas:

```txt
demasiadas responsabilidades,
dependencia fuerte de Unity,
búsqueda global costosa,
lógica difícil de testear,
Update con trabajo pesado,
mezcla audio, UI, daño, targeting y creación.
```

---

### Separación propuesta

```txt
TowerBehaviour : MonoBehaviour
→ referencia firePoint,
→ conecta con Unity,
→ llama Tick si corresponde,
→ recibe datos de escena.

TowerAttackController
→ coordina ataque de una torre.

TargetSelector
→ elige objetivo según regla.

DamageCalculator
→ calcula daño.

ProjectilePoolManager
→ entrega proyectiles.

AudioManager
→ reproduce sonido de disparo.

UpgradeSystem
→ aplica upgrades.

HUD / UI
→ escucha eventos de cooldown o selección.
```

---

### Resultado

```txt
MonoBehaviour queda como puente.
Manager queda acotado.
Targeting se puede testear.
Daño se puede testear.
Proyectiles se reutilizan.
Audio queda separado.
UI no decide gameplay.
Update puede reducir frecuencia.
```

---

## Ejemplo de refactor incremental

### Paso 1: extraer cálculo

Antes:

```csharp
private int CalculateDamage()
{
    return Mathf.RoundToInt(baseDamage * multiplier);
}
```

Después:

```csharp
public class DamageCalculator
{
    public int Calculate(int baseDamage, float multiplier)
    {
        return Mathf.RoundToInt(baseDamage * multiplier);
    }
}
```

Validación:

```txt
mismo daño antes y después,
sin cambiar disparo,
sin tocar UI,
sin tocar audio.
```

---

### Paso 2: extraer targeting

Antes:

```txt
TowerManager busca enemigos y elige objetivo.
```

Después:

```txt
TargetSelector recibe lista de enemigos y posición.
Devuelve el objetivo elegido.
```

Validación:

```txt
misma torre elige mismo objetivo,
sin cambiar pool,
sin cambiar daño,
sin cambiar UI.
```

---

### Paso 3: reemplazar Instantiate por Pool

Antes:

```txt
Tower instancia proyectil cada disparo.
```

Después:

```txt
TowerAttackController solicita proyectil al PoolManager.
```

Validación:

```txt
proyectil aparece igual,
impacta igual,
se resetea correctamente,
baja Instantiate/Destroy,
baja GC si correspondía.
```

---

### Paso 4: UI por eventos

Antes:

```txt
TowerManager actualiza HUD directamente.
```

Después:

```txt
TowerSelectionChanged.
HUD escucha.
HUD actualiza panel.
```

Validación:

```txt
panel sigue mostrando datos correctos,
no hay referencias viejas,
no hay listeners duplicados.
```

---

## Prompt de auditoría para IA

Usar este prompt cuando se quiera analizar un proyecto Unity y optimizar managers/MonoBehaviours sin romper arquitectura.

```txt
Quiero que audites este proyecto Unity con foco en optimización arquitectónica de Managers y MonoBehaviours.

No escribas código todavía.

Objetivo:
detectar qué lógica puede separarse de MonoBehaviour y Managers hacia clases puras, sistemas pequeños, eventos, interfaces o patrones existentes para mejorar SOLID, mantenibilidad, testeo y optimización.

Analizá especialmente:

1. Managers existentes.
2. Clases MonoBehaviour con demasiada lógica.
3. Clases con Update innecesario o pesado.
4. Managers que podrían dejar de ser MonoBehaviour.
5. Lógica que no necesita Unity.
6. Cálculos que podrían ser clases puras.
7. Validaciones que podrían ser clases puras.
8. Decisiones que podrían ser Strategy, Selector o clase pura.
9. Creación de objetos que debería ser Factory.
10. Reutilización que debería ser Pool.
11. Comunicación directa que debería ser evento u Observer.
12. Comunicación diferida que debería ser Event Queue.
13. Estados que deberían ser State Machine.
14. Managers persistentes con referencias de escena.
15. Singletons usados solo por comodidad.
16. Búsquedas globales repetidas.
17. APIs públicas demasiado grandes.
18. Violaciones de SOLID.

Para cada clase relevante, devolvé:

## Clase analizada

### Rol actual
Manager / MonoBehaviour / Sistema / Otro

### Responsabilidad aparente

### Responsabilidad real

### Problemas detectados

### Lógica que debe quedarse en MonoBehaviour

### Lógica que puede moverse a clase pura

### Lógica que debería moverse a otro manager o sistema

### Dependencias peligrosas

### Oportunidades de optimización

### Principios SOLID afectados

### Refactor incremental recomendado

### Riesgo del cambio
Bajo / Medio / Alto

### Validación posterior

No propongas reescritura total.
No crees managers nuevos sin justificar.
No agregues interfaces si no aportan valor.
No conviertas todo en singleton.
No muevas lógica de golpe.
Priorizá cambios incrementales y seguros.

Al final, devolvé:

# Plan de optimización arquitectónica

## Prioridad 1: cambios de bajo riesgo
## Prioridad 2: cambios de impacto medio
## Prioridad 3: cambios grandes que requieren aprobación
## Clases puras sugeridas
## Managers que pueden dejar de ser MonoBehaviour
## Managers que deben seguir siendo MonoBehaviour
## Updates que pueden eliminarse o reducirse
## Eventos recomendados
## Riesgos generales
## Validación en Unity
```

---

## Prompt para convertir un Manager MonoBehaviour en arquitectura más SOLID

Usar este prompt cuando ya se tiene identificado un manager puntual.

```txt
Quiero que analices este Manager de Unity para ver cómo convertirlo en una arquitectura más SOLID, testeable y optimizada.

No escribas código todavía.

Objetivo:
separar lo que realmente necesita MonoBehaviour de la lógica que puede vivir en clases puras o sistemas desacoplados.

Analizá:

1. Qué responsabilidad central tiene este manager.
2. Qué responsabilidades está mezclando.
3. Qué partes dependen realmente de Unity.
4. Qué partes solo usan MonoBehaviour por comodidad.
5. Qué métodos pueden moverse a clases puras.
6. Qué métodos deberían quedarse en el MonoBehaviour.
7. Qué métodos deberían moverse a otro manager o sistema.
8. Qué dependencias deberían volverse explícitas.
9. Qué referencias de escena deben mantenerse.
10. Qué eventos conviene emitir o escuchar.
11. Qué Update puede eliminarse, reducirse o delegarse.
12. Qué lógica viola SOLID.
13. Qué cambios mejorarían performance.
14. Qué cambios mejorarían testeo.
15. Qué cambios serían peligrosos.

Devolvé el análisis con esta estructura:

# Refactor arquitectónico propuesto

## Manager analizado

## Diagnóstico general

## Responsabilidad central correcta

## Responsabilidades mezcladas detectadas

## Debe quedarse en MonoBehaviour

## Puede moverse a clases puras

## Puede moverse a otros sistemas/managers

## Nuevas clases puras sugeridas

Para cada clase pura sugerida:
- Nombre
- Responsabilidad
- Inputs
- Output
- Por qué no necesita Unity
- Cómo se validaría

## Manager resultante

Explicá qué debería conservar el manager después del refactor.

## MonoBehaviour resultante

Explicá qué debería conservar el MonoBehaviour después del refactor.

## API mínima recomendada

## Eventos recomendados

## Interfaces recomendadas solo si aportan valor

## Cambios de optimización esperados

## Riesgos del refactor

## Qué NO tocarías

## Plan incremental

Separá el plan en pasos:
1. Bajo riesgo
2. Riesgo medio
3. Requiere aprobación

## Archivos que tocarías

## Archivos que NO tocarías

## Validación en Unity

No escribas código hasta que apruebe el plan.
No hagas una reescritura total.
No agregues patrones innecesarios.
No uses singleton salvo que esté justificado.
No cambies prefabs ni escenas sin avisar.
```

---

## Prompt para implementar el primer paso del refactor

Usar después de aprobar el análisis.

```txt
Implementá solo el primer paso aprobado del refactor arquitectónico.

Condiciones:

1. Tocá la menor cantidad de archivos posible.
2. No cambies comportamiento observable.
3. No hagas una reescritura total.
4. No agregues responsabilidades nuevas.
5. No agregues singleton.
6. No modifiques escenas ni prefabs sin pedir aprobación.
7. Extraé solo la lógica indicada.
8. Mantené nombres claros.
9. Si creás una clase pura, que no dependa de MonoBehaviour.
10. Si agregás una interfaz, justificá por qué aporta valor.
11. Indicá exactamente qué archivos modificaste.
12. Indicá cómo validar en Unity.
13. Indicá riesgos pendientes.

Objetivo del paso:
[describir paso aprobado]
```

---

## Checklist para personas

Antes de pedirle a una IA que optimice un manager, revisar:

```txt
¿El manager realmente tiene demasiada lógica?
¿Está heredando de MonoBehaviour por necesidad o por costumbre?
¿Qué partes usan Inspector?
¿Qué partes usan Transform/GameObject/Scene?
¿Qué partes solo calculan datos?
¿Qué partes solo validan reglas?
¿Qué partes podrían testearse sin Unity?
¿Qué partes usan Update?
¿Qué partes podrían ejecutarse por evento?
¿Qué partes hacen búsquedas globales?
¿Qué partes deberían ser Factory, Pool, State Machine o eventos?
¿Qué cambios son de bajo riesgo?
¿Qué comportamiento no debe cambiar?
```

---

## Checklist de salida para IA

Una buena respuesta de IA debe entregar:

```txt
diagnóstico claro,
responsabilidad real,
separación entre Unity y lógica,
lista de clases puras candidatas,
qué queda en MonoBehaviour,
qué queda en Manager,
qué se mueve a otros sistemas,
riesgos SOLID,
riesgos de Unity,
beneficios de optimización,
plan incremental,
archivos a tocar,
archivos que no tocaría,
validación posterior.
```

Una mala respuesta suele decir:

```txt
voy a crear una arquitectura nueva,
voy a hacer todo singleton,
voy a crear muchos managers,
voy a cambiar todo el flujo,
voy a mover todo de golpe,
voy a tocar escenas y prefabs,
voy a reescribir el sistema completo.
```

Eso debe rechazarse o pedirse que vuelva al análisis.

---

## Criterios de aprobación

Antes de aprobar un refactor propuesto por IA, verificar:

```txt
¿Reduce responsabilidades mezcladas?
¿Mantiene comportamiento actual?
¿Se puede hacer por pasos?
¿No rompe escenas?
¿No rompe prefabs?
¿No agrega singletons innecesarios?
¿No agrega interfaces decorativas?
¿No crea managers vacíos?
¿No sobrearquitectura?
¿Mejora testeo?
¿Mejora mantenibilidad?
¿Tiene validación clara?
```

---

## Regla final

Optimizar managers no significa convertir todo en clases abstractas ni eliminar todos los MonoBehaviours.

Significa poner cada responsabilidad en el lugar correcto.

```txt
MonoBehaviour sano
→ conecta con Unity.

Manager sano
→ administra una responsabilidad.

Clase pura sana
→ resuelve lógica sin depender del motor.

Evento sano
→ comunica cambios.

Arquitectura sana
→ permite crecer sin que todo dependa de todo.
```

La meta no es tener más capas.

La meta es tener menos confusión.

```txt
Si una separación reduce acoplamiento, mejora testeo,
baja trabajo innecesario y mantiene comportamiento,
probablemente es una buena optimización arquitectónica.

Si una separación agrega capas sin resolver un problema,
probablemente es sobrearquitectura.
```
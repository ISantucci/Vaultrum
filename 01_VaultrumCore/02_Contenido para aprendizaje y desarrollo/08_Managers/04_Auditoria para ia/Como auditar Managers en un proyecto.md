## Objetivo

Este documento define cómo auditar managers existentes dentro de un proyecto de videojuegos.

El objetivo no es juzgar nombres de clases, sino entender si cada manager tiene una responsabilidad clara, una API sana, un ciclo de vida definido y límites arquitectónicos correctos.

Una auditoría de managers debe responder:

```txt
qué managers existen,
qué responsabilidad parecen tener,
qué responsabilidad tienen realmente,
cuáles están bien diseñados,
cuáles mezclan responsabilidades,
cuáles son innecesarios,
cuáles son clase dios,
qué riesgos generan,
y qué cambios conviene hacer primero.
```

La auditoría no debe empezar escribiendo código.

Debe empezar entendiendo la arquitectura real del proyecto.

---

## Qué buscar

Al auditar managers, buscar:

```txt
clases con nombre Manager,
clases singleton,
clases persistentes entre escenas,
clases con muchas referencias,
clases que coordinan varios sistemas,
clases con muchos métodos públicos,
clases que usan DontDestroyOnLoad,
clases que reciben eventos de muchos lugares,
clases que todos los sistemas llaman,
clases que tienen Update,
clases que mezclan UI, gameplay, audio, assets o guardado.
```

También revisar clases que no se llaman `Manager`, pero cumplen ese rol.

Ejemplos:

```txt
GameController,
SystemController,
Bootstrapper,
ServiceHub,
SceneCoordinator,
GameplayFacade,
RuntimeContext,
Core,
Main,
App.
```

Una auditoría sana no depende solo del nombre.

Depende de la responsabilidad real.

---

## Señales de buen diseño

Un manager está bien diseñado cuando:

```txt
su responsabilidad puede explicarse en una frase,
su API pública es pequeña,
sus dependencias son explícitas,
su ciclo de vida está claro,
tiene pocas razones para cambiar,
no absorbe responsabilidades ajenas,
delega en sistemas especializados,
usa eventos con criterio,
limpia referencias cuando corresponde,
no depende de todos los sistemas,
y puede modificarse sin romper medio proyecto.
```

Ejemplo:

```txt
AudioManager
→ administra reproducción y configuración de audio.

Métodos:
PlaySfx
PlayMusic
StopMusic
SetVolume

No:
cambiar escenas,
guardar partida,
actualizar HUD,
decidir victoria.
```

Ese manager tiene límites claros.

---

## Señales de mal diseño

Un manager presenta riesgo cuando:

```txt
tiene demasiadas responsabilidades,
todos los sistemas dependen de él,
usa singleton solo por comodidad,
tiene muchos métodos públicos,
tiene referencias a casi todo el proyecto,
mezcla UI con gameplay,
mezcla assets con spawn,
mezcla guardado con reglas de juego,
tiene un Update gigante,
usa búsquedas globales constantemente,
no limpia eventos,
persiste referencias de escena,
o cada feature nueva lo modifica.
```

Señal crítica:

```txt
Si algo no tiene lugar claro, termina en ese manager.
```

Cuando eso ocurre, el manager dejó de ordenar el proyecto y empezó a ocultar deuda arquitectónica.

---

## Preguntas obligatorias

Para cada manager auditado, responder:

```txt
¿Qué responsabilidad declara tener?
¿Qué responsabilidad tiene realmente?
¿Qué métodos públicos expone?
¿Qué campos o dependencias tiene?
¿Qué sistemas lo llaman?
¿Qué sistemas llama?
¿Tiene ciclo de vida claro?
¿Es MonoBehaviour?
¿Es singleton?
¿Persiste entre escenas?
¿Tiene referencias de escena?
¿Se suscribe a eventos?
¿Se desuscribe correctamente?
¿Tiene Update?
¿Qué hace en Update?
¿Qué responsabilidades tiene mezcladas?
¿Qué riesgos genera?
```

Estas preguntas evitan auditorías vagas.

No alcanza con decir:

```txt
El manager está bien.
```

Hay que demostrar por qué.

---

## Flujo de análisis para IA

Una IA debería seguir este flujo:

```txt
1. Listar todos los managers detectados.
2. Identificar responsabilidad aparente por nombre.
3. Identificar responsabilidad real por métodos, campos y dependencias.
4. Detectar si el manager es necesario.
5. Detectar si corresponde otra pieza arquitectónica.
6. Revisar ciclo de vida.
7. Revisar persistencia.
8. Revisar eventos.
9. Revisar API pública.
10. Revisar riesgos SOLID.
11. Clasificar estado del manager.
12. Proponer cambios incrementales.
```

Clasificación recomendada:

```txt
Sano
→ responsabilidad clara, API chica, bajo riesgo.

Aceptable con deuda
→ funciona, pero tiene riesgos controlables.

Riesgoso
→ mezcla responsabilidades y puede crecer mal.

Clase dios
→ concentra demasiadas responsabilidades.

Innecesario
→ no justifica existir como manager.

Mal nombrado
→ cumple otro rol arquitectónico.
```

---

## Cómo identificar responsabilidad real

La responsabilidad real se deduce mirando:

```txt
métodos públicos,
métodos privados,
campos serializados,
dependencias,
eventos emitidos,
eventos escuchados,
objetos que instancia,
sistemas que modifica,
sistemas que consulta,
y razones por las que cambia.
```

Ejemplo:

```txt
Nombre:
GameManager

Responsabilidad aparente:
estado global de juego.

Métodos reales:
SpawnEnemy,
PlayMusic,
SaveGame,
UpdateHUD,
CalculateDamage,
LoadTowerPrefab,
PauseGame.

Responsabilidad real:
gameplay, spawn, audio, guardado, UI, daño, assets y pausa.
```

Conclusión:

```txt
No es solo GameManager.
Es una clase dios.
```

---

## Cómo detectar si corresponde otra pieza

No todo manager debería seguir siendo manager.

Durante la auditoría, clasificar problemas:

```txt
Creación de objetos
→ Factory.

Reutilización de objetos
→ Pool.

Comunicación inmediata
→ Observer/eventos.

Comunicación diferida
→ Event Queue.

Estados y transiciones
→ State Machine.

Acceso simplificado a subsistemas
→ Facade.

Cálculo puntual
→ clase pura.

Datos o configuración
→ ScriptableObject o modelo de datos.

Consulta de entidades
→ Registry o Repository.
```

Si un manager solo existe para hacer una de esas cosas, probablemente está mal nombrado o sobredimensionado.

---

## Cómo evaluar ciclo de vida

Revisar:

```txt
cuándo se crea,
cuándo se inicializa,
quién lo inicializa,
si puede usarse antes de estar listo,
si tiene ResetState,
si tiene Shutdown,
si se limpia al cambiar escena,
si conserva referencias viejas,
si se duplica entre escenas,
si llama manualmente Awake, Start o Update.
```

Alerta fuerte:

```txt
El manager se reinicia llamando Awake manualmente.
```

Eso indica confusión entre ciclo de Unity y ciclo propio del sistema.

---

## Cómo evaluar persistencia

Si el manager usa `DontDestroyOnLoad`, revisar:

```txt
por qué debe persistir,
qué estado conserva,
qué referencias conserva,
cómo evita duplicados,
cómo limpia referencias de escena,
qué ocurre al volver al menú,
qué ocurre al reiniciar partida,
qué eventos mantiene,
qué eventos limpia.
```

Regla:

```txt
Persistir estado puede ser correcto.
Persistir referencias de escena sin control es peligroso.
```

---

## Cómo evaluar eventos

Revisar:

```txt
qué eventos emite,
qué eventos escucha,
si los eventos tienen nombres claros,
si hay eventos demasiado genéricos,
si se desuscribe correctamente,
si hay listeners duplicados,
si el orden de ejecución importa,
si debería usarse Event Queue,
si debería usarse Observer simple.
```

Alerta:

```txt
Evento genérico:
OnSomethingHappened(object data)
```

Ese tipo de evento suele ocultar flujo y aumentar ambigüedad.

---

## Cómo evaluar API pública

Revisar:

```txt
cantidad de métodos públicos,
si los métodos pertenecen a la responsabilidad central,
si hay setters públicos innecesarios,
si expone listas internas,
si expone diccionarios internos,
si expone referencias de escena,
si tiene métodos de otras responsabilidades,
si cada consumidor necesita toda la API.
```

Regla:

```txt
La API pública debe expresar intención,
no exponer implementación interna.
```

---

## Cómo evaluar SOLID

Revisar especialmente:

```txt
SRP
→ ¿cuántas razones tiene para cambiar?

OCP
→ ¿cada feature obliga a modificarlo?

ISP
→ ¿su API obliga a depender de métodos innecesarios?

DIP
→ ¿depende de demasiadas clases concretas?

LSP
→ si usa abstracciones, ¿requiere excepciones por tipo?
```

La pregunta más importante:

```txt
¿Por qué razones cambia este manager?
```

Si la respuesta incluye UI, audio, assets, guardado, spawn, daño y niveles, el manager está en riesgo.

---

## Formato de salida recomendado

Una IA debería entregar la auditoría así:

```txt
# Auditoría de Managers

## Managers detectados

## Resumen general

## Manager: [Nombre]

### Responsabilidad aparente
### Responsabilidad real
### Estado
Sano / Aceptable con deuda / Riesgoso / Clase dios / Innecesario / Mal nombrado

### Señales positivas
### Señales de riesgo
### Responsabilidades mezcladas
### Relación con SOLID
### Riesgos de Unity
### Recomendación
### Refactor incremental sugerido
### Archivos a revisar
### Archivos que NO tocaría todavía
```

---

## Checklist de salida

Una auditoría completa debería responder:

```txt
¿Se listaron todos los managers?
¿Se detectaron managers ocultos con otro nombre?
¿Se explicó responsabilidad aparente y real?
¿Se clasificó cada manager?
¿Se detectaron clases dios?
¿Se detectaron managers innecesarios?
¿Se detectaron singletons injustificados?
¿Se detectaron problemas de ciclo de vida?
¿Se detectaron problemas de persistencia?
¿Se detectaron APIs demasiado grandes?
¿Se detectaron responsabilidades mezcladas?
¿Se propusieron refactors incrementales?
¿Se evitó proponer reescritura total?
¿Se indicaron riesgos?
¿Se indicaron validaciones?
```

---

## Regla final

Auditar managers no es buscar errores por nombre.

Es descubrir si las responsabilidades están bien distribuidas.

```txt
Buena auditoría
→ identifica responsabilidades reales,
→ detecta riesgos,
→ propone cambios pequeños,
→ evita reescrituras innecesarias.

Mala auditoría
→ dice “está bien” o “está mal” sin justificar,
→ propone managers nuevos sin criterio,
→ o intenta reescribir todo de golpe.
```
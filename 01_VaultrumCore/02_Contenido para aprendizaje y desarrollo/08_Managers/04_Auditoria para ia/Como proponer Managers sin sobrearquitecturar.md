## Objetivo

Este documento define cómo proponer managers nuevos sin caer en sobrearquitectura.

Una IA o un desarrollador no deberían crear un manager solo porque “suena ordenado”.

Un manager nuevo debe aparecer cuando hay un problema real de administración.

La idea principal es:

```txt
Primero problema.
Después responsabilidad.
Después alternativas.
Recién después manager.
```

---

## Qué es sobrearquitecturar

Sobrearquitecturar es crear más estructura de la que el problema necesita.

Ejemplos:

```txt
crear AssetManager complejo con Addressables para 3 prefabs,
crear UpdateManager para 5 objetos,
crear SaveManager con slots y versiones cuando solo hay una opción de volumen,
crear LevelManager completo para una sola escena sin niveles,
crear managers vacíos por cada categoría,
crear interfaces para todo sin necesidad,
crear singletons preventivos.
```

El problema no es pensar a futuro.

El problema es pagar complejidad antes de necesitarla.

---

## Cuándo una propuesta de Manager es válida

Una propuesta de manager es válida cuando puede justificar:

```txt
problema concreto,
responsabilidad central,
beneficio arquitectónico,
alternativas evaluadas,
ciclo de vida,
API mínima,
límites,
riesgos,
validación,
y plan incremental.
```

No alcanza con decir:

```txt
Esto ordenaría el proyecto.
```

Debe decir:

```txt
Esta responsabilidad está repetida en tres sistemas,
tiene ciclo de vida propio,
y necesita centralizar carga y liberación.
Por eso propongo AssetManager.
```

---

## Pregunta inicial obligatoria

Antes de proponer un manager, preguntar:

```txt
¿Qué problema exacto estoy resolviendo?
```

Si la respuesta es vaga, no proponer manager todavía.

Ejemplos vagos:

```txt
ordenar el código,
centralizar cosas,
hacerlo más limpio,
tener mejor arquitectura,
preparar el futuro.
```

Ejemplos válidos:

```txt
hay carga duplicada de assets,
hay muchos Update innecesarios,
hay objetos temporales que generan GC,
hay estados globales mezclados en GameManager,
hay UI llamando directamente a gameplay,
hay guardado disperso en varios sistemas.
```

---

## Evaluar alternativas

Antes de proponer manager, evaluar:

```txt
clase pura,
Factory,
Facade,
Object Pool,
Observer,
Event Queue,
State Machine,
ScriptableObject,
referencia explícita,
Registry,
Repository,
sistema específico.
```

Ejemplo:

```txt
Problema:
crear enemigos según tipo.

Alternativa correcta:
EnemyFactory.

No:
EnemyManager genérico.
```

Ejemplo:

```txt
Problema:
UI necesita llamar acciones de gameplay.

Alternativa correcta:
GameplayFacade.

No:
UIManager con reglas de gameplay.
```

Ejemplo:

```txt
Problema:
muchos proyectiles se crean y destruyen.

Alternativa correcta:
Object Pool / PoolManager.

No:
ProjectileManager que decide todo.
```

---

## Proponer responsabilidad central

Si el manager está justificado, definir su responsabilidad en una frase.

Ejemplos:

```txt
AudioManager
→ administra reproducción y configuración de audio.

AssetManager
→ administra carga, cache y liberación de assets.

UpdateManager
→ administra registro y ejecución controlada de actualizaciones.

LevelManager
→ administra entrada, salida y progreso del nivel actual.
```

Mala responsabilidad:

```txt
GameManager
→ administra todo el juego.
```

Si la frase es demasiado amplia, el manager no está bien definido.

---

## Definir responsabilidades prohibidas

Todo manager propuesto debe incluir límites.

Ejemplo:

```txt
PoolManager puede:
→ entregar objetos,
→ recibir objetos,
→ resetear objetos.

PoolManager no debe:
→ calcular daño,
→ decidir disparo,
→ actualizar UI,
→ manejar economía.
```

Esto evita que la IA agregue responsabilidades por comodidad.

Regla:

```txt
Un manager sin responsabilidades prohibidas está incompleto.
```

---

## Diseñar API mínima

La propuesta debe incluir solo métodos necesarios para el primer uso real.

Ejemplo:

```csharp
public interface IPool<T>
{
    T Get();
    void Release(T instance);
}
```

No empezar con:

```txt
Get,
Release,
Preload,
Serialize,
Debug,
Register,
Find,
Pause,
Resume,
Save,
Load,
BindUI,
HandleAudio.
```

Regla:

```txt
La API inicial debe resolver el problema actual,
no todos los problemas imaginarios.
```

---

## Definir ciclo de vida

Todo manager propuesto debe aclarar:

```txt
cuándo se crea,
quién lo inicializa,
si es por escena o global,
si persiste entre escenas,
cómo se limpia,
cómo se reinicia,
qué referencias conserva.
```

Si no hay ciclo de vida especial, decirlo.

Ejemplo:

```txt
Este manager no necesita persistir.
Puede vivir en la escena de gameplay.
Se limpia al salir del nivel.
```

Eso es mejor que asumir singleton.

---

## Definir integración con Unity

Una propuesta debe indicar si será:

```txt
MonoBehaviour,
clase pura,
ScriptableObject,
servicio interno,
componente de escena,
objeto persistente,
o sistema registrado.
```

Criterio:

```txt
MonoBehaviour si necesita Unity.
Clase pura si no necesita Unity.
ScriptableObject si es configuración/datos.
```

No hacer MonoBehaviour por costumbre.

---

## Definir comunicación

La propuesta debe explicar cómo hablará con otros sistemas.

Opciones:

```txt
llamadas directas explícitas,
eventos,
Event Queue,
Facade,
interfaces,
registro/desregistro.
```

Ejemplo sano:

```txt
EconomySystem cambia dinero.
Emite MoneyChanged.
UI escucha.
```

Ejemplo peligroso:

```txt
Manager nuevo llama directamente a todos los paneles y sistemas.
```

---

## Definir validación

Toda propuesta debe decir cómo se prueba que el manager resuelve el problema.

Ejemplos:

```txt
medir GC antes/después,
verificar que no hay referencias viejas,
verificar que no se duplica al cambiar escena,
verificar que UI se actualiza por eventos,
verificar que objetos pooled resetean estado,
verificar que se desuscribe de eventos,
verificar que no crece la API.
```

Sin validación, la propuesta queda incompleta.

---

## Propuesta incremental

Un manager nuevo debe empezar pequeño.

Proceso:

```txt
1. Implementar responsabilidad mínima.
2. Integrar un flujo.
3. Validar.
4. Migrar duplicación existente.
5. Recién después ampliar.
```

Ejemplo:

```txt
AssetManager v1:
LoadAsync
Release

AssetManager futuro:
PreloadGroup
UnloadGroup
diagnóstico
cache avanzada
```

No construir todo de entrada.

---

## Criterio para IA/agente

Una IA debe presentar propuestas así:

```txt
# Propuesta de Manager

## Problema detectado

## Por qué un manager podría estar justificado

## Alternativas evaluadas

## Decisión

## Responsabilidad central

## Responsabilidades permitidas

## Responsabilidades prohibidas

## API mínima inicial

## Ciclo de vida

## Integración con Unity

## Comunicación con otros sistemas

## Riesgos

## Plan incremental

## Validación
```

Si falta la sección de alternativas, la propuesta no está lista.

---

## Ejemplo de propuesta sana

```txt
Problema:
los proyectiles se instancian y destruyen constantemente.

Alternativas:
- Factory: ayuda a crear, pero no evita Destroy.
- Clase pura: no aplica.
- Object Pool: sí resuelve reutilización.
- PoolManager: se justifica si habrá varios pools o acceso centralizado.

Decisión:
crear ProjectilePoolManager acotado.

Responsabilidad:
entregar, recibir y resetear proyectiles reutilizables.

Responsabilidades prohibidas:
calcular daño,
elegir objetivo,
decidir cuándo dispara una torre,
actualizar UI.

API:
GetProjectile()
ReleaseProjectile(projectile)

Validación:
medir GC/Instantiate antes y después,
verificar reset correcto.
```

---

## Ejemplo de propuesta sobrearquitecturada

```txt
Problema:
necesitamos disparar proyectiles.

Propuesta:
crear CombatManager singleton que administre torres, proyectiles, daño, enemigos, audio, UI y recompensas.

Problema:
mezcla demasiadas responsabilidades,
no evalúa alternativas,
nace como clase dios,
no tiene API mínima,
no define límites.
```

---

## Checklist para evitar sobrearquitectura

Antes de proponer manager:

```txt
¿Hay problema concreto?
¿El problema existe ahora?
¿Se evaluaron alternativas?
¿La responsabilidad cabe en una frase?
¿La API inicial es mínima?
¿Se definió qué NO hará?
¿Tiene ciclo de vida claro?
¿Se justificó MonoBehaviour o clase pura?
¿Se justificó singleton o se evitó?
¿Se puede implementar por etapas?
¿Se puede validar?
¿El costo de la arquitectura es menor que el problema?
```

---

## Regla final

Un manager nuevo debe reducir complejidad real.

No crear complejidad elegante.

```txt
Manager sano
→ aparece por necesidad,
→ empieza pequeño,
→ tiene límites,
→ se valida.

Manager sobrearquitecturado
→ aparece por anticipación,
→ tiene demasiadas capas,
→ resuelve problemas imaginarios,
→ y complica prototipos.
```
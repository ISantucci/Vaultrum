## Objetivo

Este documento define cómo detectar managers que no deberían existir o que no justifican su rol arquitectónico.

Un manager innecesario agrega complejidad sin resolver un problema real.

Puede parecer ordenado al principio, pero termina generando:

```txt
acoplamiento,
APIs artificiales,
singletons innecesarios,
dependencias ocultas,
más archivos para mantener,
y más puntos de fallo.
```

La idea central es:

```txt
No todo necesita un manager.
Un manager debe ganarse su existencia.
```

---

## Qué es un Manager innecesario

Un manager es innecesario cuando no administra una responsabilidad real.

Ejemplos:

```txt
solo envuelve una lista,
solo llama a otra clase,
solo existe para ser singleton,
solo evita pasar referencias,
solo agrupa métodos sin relación,
solo replica una Factory,
solo replica un Pool,
solo replica una Facade,
solo hace un cálculo simple,
o existe “por si en el futuro hace falta”.
```

Un manager innecesario no siempre rompe el juego.

Pero ensucia la arquitectura y puede crecer mal.

---

## Señales de Manager innecesario

Señales comunes:

```txt
su responsabilidad no puede explicarse claramente,
tiene uno o dos métodos triviales,
solo delega sin agregar valor,
solo existe para acceso global,
no tiene ciclo de vida propio,
no administra estado,
no administra recursos,
no coordina sistemas,
no reduce duplicación real,
no mejora testeo,
no mejora lectura,
y no evita un problema concreto.
```

Señal fuerte:

```txt
Si se elimina el manager y el proyecto queda igual o más claro,
probablemente era innecesario.
```

---

## Manager que solo envuelve una lista

Ejemplo:

```csharp
public class EnemyManager
{
    public List<Enemy> enemies;

    public void Add(Enemy enemy)
    {
        enemies.Add(enemy);
    }

    public void Remove(Enemy enemy)
    {
        enemies.Remove(enemy);
    }
}
```

Esto puede ser útil si realmente administra registro, consultas, limpieza, eventos o ciclo de vida.

Pero si solo envuelve una lista sin reglas, puede ser innecesario.

Alternativas:

```txt
Registry,
colección local,
sistema propietario,
lista dentro del spawner,
o estructura de datos específica.
```

Criterio:

```txt
Lista + nombre Manager no alcanza.
Debe haber una responsabilidad de administración.
```

---

## Manager que solo llama a una Factory

Ejemplo peligroso:

```txt
EnemyManager.SpawnEnemy()
→ llama a EnemyFactory.CreateEnemy()
```

Si no agrega reglas, ciclo de vida o coordinación, puede sobrar.

Mejor:

```txt
Spawner
→ decide cuándo aparece enemigo.

EnemyFactory
→ crea enemigo.

PoolManager
→ reutiliza enemigo si corresponde.
```

Un manager solo se justifica si administra algo más:

```txt
registro de enemigos activos,
límite de enemigos,
limpieza al cambiar nivel,
eventos de spawn,
ciclo de vida global.
```

---

## Manager que solo existe para ser singleton

Ejemplo:

```txt
InputManager.Instance
AudioManager.Instance
UIManager.Instance
EnemyManager.Instance
DamageManager.Instance
```

El singleton puede ser útil en algunos casos, pero no justifica el manager.

Mala razón:

```txt
Lo hago manager para acceder fácil desde cualquier lado.
```

Problemas:

```txt
dependencias ocultas,
testeo difícil,
orden de inicialización frágil,
acoplamiento global,
crecimiento sin control.
```

Criterio:

```txt
Acceso global no es responsabilidad.
```

---

## Manager que debería ser clase pura

Muchos managers aparecen para resolver cálculos simples.

Ejemplos:

```txt
DamageManager
→ solo calcula daño.

CostManager
→ solo calcula costos.

DistanceManager
→ solo calcula distancia.

TargetManager
→ solo elige objetivo con una regla simple.
```

Posibles alternativas:

```txt
DamageCalculator,
UpgradeCostCalculator,
TargetSelector,
DistanceUtility,
Strategy,
clase pura,
función controlada.
```

Ejemplo:

```csharp
public class DamageCalculator
{
    public int Calculate(int baseDamage, float multiplier)
    {
        return Mathf.RoundToInt(baseDamage * multiplier);
    }
}
```

No todo cálculo necesita manager.

---

## Manager que debería ser Facade

A veces se crea un manager para simplificar acceso a varios subsistemas.

Ejemplo:

```txt
GameplayManager
→ PlaceTower
→ SellTower
→ UpgradeTower
→ StartWave
```

Si solo expone una puerta de entrada para la UI, puede ser mejor llamarlo Facade.

Una facade no necesariamente posee estado ni ciclo de vida.

Criterio:

```txt
Si el problema es simplificar acceso,
probablemente es Facade.

Si el problema es administrar estado, recursos o ciclo,
puede ser Manager.
```

---

## Manager que debería ser State Machine

Ejemplo:

```txt
GameManager
→ if menu
→ if playing
→ if paused
→ if win
→ if lose
```

Si el problema son estados y transiciones, la solución puede ser una state machine.

No hace falta agrandar el manager.

Alternativa:

```txt
GameStateMachine
→ administra estados.

GameManager
→ coordina transición global.
```

Criterio:

```txt
Si el manager existe para manejar muchos estados,
auditar si corresponde State Machine.
```

---

## Manager que debería ser Event Queue u Observer

Ejemplo:

```txt
UIManager avisa a GameManager.
GameManager avisa a AudioManager.
AudioManager avisa a SaveManager.
SaveManager avisa a UIManager.
```

A veces el manager existe solo como intermediario de comunicación.

Alternativas:

```txt
eventos,
Observer,
Event Queue,
mensajes de dominio,
callbacks específicos.
```

Criterio:

```txt
Si el problema es comunicación,
no asumir manager.
```

---

## Manager creado por anticipación

Ejemplo:

```txt
AssetManager complejo antes de tener carga dinámica.
UpdateManager complejo antes de tener muchos Update.
SaveManager complejo antes de guardar progreso real.
PoolManager para objetos que casi no se instancian.
```

Puede haber diseño preventivo sano, pero debe estar justificado.

Riesgo:

```txt
sobrearquitectura,
código muerto,
más mantenimiento,
más dificultad para IA,
más puntos de decisión innecesarios.
```

Regla:

```txt
Diseñar camino de crecimiento.
No construir infraestructura gigante sin problema real.
```

---

## Cómo decidir si eliminarlo

Antes de eliminar un manager, responder:

```txt
¿Qué responsabilidad administra?
¿Qué pasaría si no existiera?
¿Quién usaría sus métodos directamente?
¿Qué alternativa lo reemplaza?
¿Se simplifica el flujo?
¿Se pierde control de ciclo de vida?
¿Se pierde validación?
¿Se pierde desacoplamiento?
¿Se rompe algo importante?
```

No eliminar por impulso.

Un manager pequeño puede estar bien si protege una responsabilidad importante.

---

## Opciones cuando un manager sobra

No siempre hay que borrarlo directamente.

Opciones:

```txt
eliminar,
renombrar,
convertir en clase pura,
convertir en Facade,
convertir en Factory,
convertir en Registry,
fusionar con sistema propietario,
reducir API,
dejarlo como deuda controlada temporal,
o documentar su rol real.
```

Ejemplo:

```txt
DamageManager
→ renombrar a DamageCalculator si solo calcula.

GameplayManager
→ renombrar a GameplayFacade si solo expone operaciones.

EnemyManager
→ dividir en EnemySpawner y EnemyRegistry.
```

---

## Criterio para IA/agente

Una IA debe justificar si un manager es innecesario.

Formato esperado:

```txt
Manager analizado:
...

Responsabilidad declarada:
...

Responsabilidad real:
...

Motivo por el que podría ser innecesario:
...

Alternativa recomendada:
...

Riesgo de eliminarlo:
...

Riesgo de mantenerlo:
...

Decisión:
mantener / reducir / renombrar / reemplazar / eliminar.
```

No debe decir simplemente:

```txt
Este manager sobra.
```

Debe explicar por qué y qué lo reemplaza.

---

## Checklist de detección

Un manager puede ser innecesario si:

```txt
¿No tiene responsabilidad clara?
¿No tiene ciclo de vida?
¿No administra estado?
¿No administra recursos?
¿No coordina sistemas?
¿Solo llama a otra clase?
¿Solo envuelve una lista?
¿Solo existe para acceso global?
¿Solo hace un cálculo?
¿Solo simplifica acceso y debería ser Facade?
¿Solo crea objetos y debería ser Factory?
¿Solo comunica eventos y debería usar Observer/Event Queue?
¿Fue creado por anticipación sin problema real?
¿Eliminarlo simplificaría el diseño?
```

---

## Regla final

Un manager innecesario no siempre es grave al principio.

Pero puede convertirse en deuda estructural.

```txt
Manager necesario
→ administra una responsabilidad real.

Manager innecesario
→ agrega una capa sin resolver un problema.

Manager peligroso
→ empieza innecesario y termina absorbiendo todo.
```
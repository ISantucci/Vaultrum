## Objetivo

Este documento define cómo refactorizar una clase dios de forma incremental y segura.

Una clase dios es una clase que concentra demasiadas responsabilidades y se vuelve el centro obligatorio del proyecto.

En managers, el caso más común suele ser:

```txt
GameManager
→ UI
→ audio
→ guardado
→ niveles
→ assets
→ spawn
→ input
→ economía
→ daño
→ eventos
→ pausa
→ victoria
→ derrota
```

La idea principal es:

```txt
No se refactoriza una clase dios reescribiendo todo de golpe.
Se separa una responsabilidad por vez.
```

---

## Qué es una clase dios

Una clase dios:

```txt
hace demasiado,
sabe demasiado,
tiene demasiadas dependencias,
cambia por demasiadas razones,
todos los sistemas la llaman,
y cualquier cambio puede romper muchas cosas.
```

No es simplemente una clase larga.

Puede tener pocas líneas y aun así ser clase dios si mezcla responsabilidades críticas.

Señal clave:

```txt
Nadie sabe qué NO debería hacer.
```

---

## Riesgos de refactorizar mal

Refactorizar una clase dios sin plan puede generar:

```txt
bugs masivos,
pérdida de comportamiento,
duplicación temporal,
referencias rotas,
eventos duplicados,
regresiones difíciles de detectar,
reescritura innecesaria,
y bloqueo del desarrollo.
```

Por eso el refactor debe ser incremental.

Regla:

```txt
Primero entender.
Después separar.
Después validar.
```

---

## Paso 1: Congelar expansión

Antes de refactorizar, dejar de agregar features nuevas a la clase dios salvo que sea estrictamente necesario.

Regla temporal:

```txt
No agregar responsabilidades nuevas al manager central.
```

Si una feature nueva aparece, primero analizar:

```txt
¿pertenece realmente a esta clase?
¿conviene crear sistema separado?
¿puede esperar al refactor?
¿puede entrar mediante una interfaz mínima?
```

Esto evita seguir agrandando el problema mientras se intenta resolver.

---

## Paso 2: Inventariar métodos y campos

Listar todo lo que tiene la clase:

```txt
métodos públicos,
métodos privados,
campos,
referencias serializadas,
eventos,
suscripciones,
singletons,
Update,
coroutines,
búsquedas globales,
llamadas a otros sistemas.
```

Ejemplo:

```txt
GameManager:
- StartLevel
- SpawnEnemy
- PlayMusic
- SaveGame
- UpdateHUD
- CalculateDamage
- LoadTowerPrefab
- PauseGame
- AddMoney
- ShowWinScreen
```

No mover nada todavía.

Primero inventariar.

---

## Paso 3: Agrupar por responsabilidad

Agrupar métodos y campos por dominio.

Ejemplo:

```txt
Nivel:
StartLevel
RestartLevel
LoadLevelScene

Spawn:
SpawnEnemy
StartWave
StopWave

Audio:
PlayMusic
StopMusic
PlaySfx

UI:
UpdateHUD
ShowWinScreen
ShowPauseMenu

Guardado:
SaveGame
LoadGame

Economía:
AddMoney
SpendMoney

Combate:
CalculateDamage
ApplyDamage

Assets:
LoadTowerPrefab
LoadEnemyPrefab
```

Este paso muestra qué sistemas están mezclados.

---

## Paso 4: Detectar piezas destino

Para cada grupo, definir a dónde debería ir.

Ejemplo:

```txt
Nivel
→ LevelManager.

Estados
→ StateMachineManager.

Audio
→ AudioManager.

UI
→ UIManager o controladores de vista.

Guardado
→ SaveManager.

Assets
→ AssetManager.

Spawn
→ Spawner o WaveSpawner.

Economía
→ EconomySystem.

Daño
→ DamageSystem o DamageCalculator.

Creación
→ Factory.

Reutilización
→ PoolManager.
```

No todo tiene que convertirse en manager.

Ese punto es clave.

---

## Paso 5: Elegir una responsabilidad para extraer

No extraer todo de golpe.

Elegir una responsabilidad con bajo riesgo y alto beneficio.

Buenas candidatas iniciales:

```txt
Audio,
UI,
guardado,
assets,
pooling,
cálculos puros.
```

Candidatas más delicadas:

```txt
estado global,
niveles,
spawn,
economía,
combate,
flujo de partida.
```

Criterio:

```txt
Primero extraer lo más aislable.
Después lo más central.
```

---

## Paso 6: Crear API mínima del nuevo sistema

Antes de mover código, definir API mínima.

Ejemplo para audio:

```csharp
public interface IAudioManager
{
    void PlaySfx(string id);
    void PlayMusic(string id);
    void StopMusic();
}
```

No crear un nuevo manager gigante.

El objetivo no es pasar deuda de una clase a otra.

Regla:

```txt
Extraer responsabilidad, no duplicar clase dios.
```

---

## Paso 7: Redirigir llamadas de forma controlada

Cambiar llamadas gradualmente.

Ejemplo:

Antes:

```csharp
GameManager.Instance.PlayMusic("battle");
```

Después:

```csharp
audioManager.PlayMusic("battle");
```

O transición temporal:

```csharp
public void PlayMusic(string id)
{
    _audioManager.PlayMusic(id);
}
```

Esto puede mantener compatibilidad mientras se migra.

Pero debe ser temporal.

Documentar deuda:

```txt
GameManager.PlayMusic queda como wrapper temporal hasta migrar consumidores.
```

---

## Paso 8: Validar comportamiento

Después de extraer una responsabilidad, validar.

Checklist:

```txt
¿El comportamiento sigue igual?
¿Se rompió alguna escena?
¿Se duplicaron eventos?
¿Se duplicaron managers?
¿Se limpiaron referencias?
¿El nuevo sistema tiene responsabilidad clara?
¿La clase dios perdió métodos reales?
¿Los consumidores migraron correctamente?
```

No seguir con la próxima extracción hasta validar la anterior.

---

## Paso 9: Eliminar wrappers temporales

Si se usaron wrappers para mantener compatibilidad, eliminarlos cuando ya no haya consumidores.

Ejemplo:

```txt
GameManager.PlayMusic
→ wrapper temporal.
→ consumidores migrados a AudioManager.
→ eliminar wrapper.
```

Si no se eliminan, la clase dios sigue siendo punto de acceso central.

Regla:

```txt
Un wrapper temporal que nunca se elimina se convierte en deuda permanente.
```

---

## Paso 10: Repetir por responsabilidad

Repetir el proceso:

```txt
inventariar,
agrupar,
extraer,
redirigir,
validar,
limpiar.
```

Una clase dios no se arregla con un solo cambio.

Se reduce paso a paso.

---

## Cómo elegir orden de refactor

Orden recomendado general:

```txt
1. Cálculos puros.
2. Audio.
3. UI.
4. Assets.
5. Guardado.
6. Pools.
7. Spawn.
8. Niveles.
9. Estado global.
10. Flujo completo.
```

El orden puede cambiar según proyecto.

Criterios para priorizar:

```txt
riesgo bajo,
beneficio alto,
pocas dependencias,
muchos métodos mezclados,
bugs frecuentes,
necesidad de nuevas features.
```

---

## Qué NO hacer

Evitar:

```txt
reescribir toda la arquitectura de una vez,
crear SuperManager,
crear muchos managers vacíos,
mover métodos sin entender dependencias,
cambiar nombres sin separar responsabilidades,
usar eventos globales para tapar acoplamiento,
hacer todo singleton,
romper escenas/prefabs sin plan,
mezclar refactor con features grandes.
```

Regla:

```txt
Refactor no debe convertirse en rediseño total sin control.
```

---

## Criterio para IA/agente

Cuando una IA refactorice una clase dios, debe trabajar en dos fases.

Primero análisis:

```txt
No modificar código.
Listar responsabilidades.
Proponer extracción incremental.
Indicar riesgos.
Indicar orden.
Pedir aprobación.
```

Después implementación:

```txt
Mover una responsabilidad.
Mantener comportamiento.
Indicar archivos tocados.
Indicar validación.
Esperar siguiente paso.
```

La IA no debe reescribir todo el sistema en una sola respuesta.

---

## Formato recomendado de análisis

```txt
# Análisis de clase dios

## Clase analizada

## Responsabilidad declarada

## Responsabilidad real

## Métodos agrupados por responsabilidad

## Dependencias detectadas

## Riesgos principales

## Responsabilidades candidatas a extraer

## Orden recomendado

## Primer refactor sugerido

## Archivos que tocaría

## Archivos que NO tocaría

## Validación posterior
```

---

## Ejemplo aplicado a videojuegos

Clase inicial:

```txt
GameManager
→ StartLevel
→ SpawnEnemy
→ PlayMusic
→ SaveGame
→ UpdateHUD
→ CalculateDamage
→ LoadTowerPrefab
→ PauseGame
→ AddMoney
```

Agrupación:

```txt
LevelManager
→ StartLevel.

EnemySpawner
→ SpawnEnemy.

AudioManager
→ PlayMusic.

SaveManager
→ SaveGame.

UIManager/HUD
→ UpdateHUD.

DamageCalculator
→ CalculateDamage.

AssetManager
→ LoadTowerPrefab.

StateMachineManager
→ PauseGame.

EconomySystem
→ AddMoney.
```

Primer refactor posible:

```txt
Extraer AudioManager.
```

Motivo:

```txt
responsabilidad aislada,
bajo riesgo,
API chica,
beneficio claro.
```

---

## Checklist de refactor

Antes de tocar código:

```txt
¿Se inventariaron métodos y campos?
¿Se agruparon responsabilidades?
¿Se identificaron destinos correctos?
¿Se eligió una sola responsabilidad para extraer?
¿Se definió API mínima?
¿Se conocen consumidores?
¿Se planificó compatibilidad temporal?
¿Se definió validación?
¿Se evitó reescritura total?
```

Después de tocar código:

```txt
¿El comportamiento sigue igual?
¿La clase dios perdió responsabilidad real?
¿El nuevo sistema tiene límites claros?
¿No se duplicaron eventos?
¿No se crearon singletons innecesarios?
¿No se rompieron escenas?
¿Se documentó deuda temporal?
```

---

## Regla final

Una clase dios no se destruye.

Se desarma.

```txt
Refactor sano
→ una responsabilidad por vez,
→ API mínima,
→ validación constante,
→ comportamiento preservado.

Refactor peligroso
→ reescritura total,
→ nuevos managers gigantes,
→ bugs masivos,
→ pérdida de control.
```
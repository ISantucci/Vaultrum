## Descripción

Un `AssetManager` administra acceso, carga, cache y liberación de assets.

Puede trabajar con recursos locales, prefabs, ScriptableObjects, Addressables u otros sistemas de carga.

Su responsabilidad no es decidir gameplay ni crear toda la lógica del juego.

---

## Qué problema resuelve

Resuelve problemas como:

```txt
carga de assets repetida,
assets duplicados en memoria,
falta de control de release,
referencias hardcodeadas,
sistemas cargando recursos de forma distinta,
necesidad de preload,
necesidad de cache,
necesidad de descarga controlada.
```

Ejemplo:

```txt
Spawner, UI y Factory cargan prefabs cada uno por su lado.
AssetManager centraliza carga y cache.
```

---

## Cuándo conviene usarlo

Conviene cuando:

```txt
hay carga dinámica,
se usan Addressables,
hay muchos assets compartidos,
se necesita preload,
se necesita liberar recursos,
se quiere evitar duplicación,
se quiere separar assets de gameplay.
```

También conviene si se busca optimizar memoria o tiempos de carga.

---

## Cuándo NO conviene usarlo

No conviene si:

```txt
hay pocos assets,
todo se referencia por Inspector sin problema,
no hay carga dinámica,
no hay problemas de memoria,
o se quiere crear una infraestructura enorme antes de necesitarla.
```

Tampoco debe crearse solo para reemplazar factories.

---

## Responsabilidades permitidas

Puede encargarse de:

```txt
cargar assets,
cachear assets,
liberar assets,
precargar grupos,
descargar grupos,
resolver assets por ID,
manejar handles si usa Addressables,
reportar errores de carga,
exponer estado de carga.
```

---

## Responsabilidades prohibidas

No debería:

```txt
instanciar enemigos por reglas de gameplay,
decidir spawn,
calcular daño,
manejar oleadas,
actualizar UI directamente,
guardar partida,
decidir qué torre se puede comprar,
reemplazar factories,
reemplazar pools.
```

Regla:

```txt
AssetManager provee assets.
No decide cómo se usan en gameplay.
```

---

## Relación con otras piezas arquitectónicas

Relaciones comunes:

```txt
Factory
→ pide prefabs/assets y crea objetos.

PoolManager
→ puede usar prefabs cargados para preparar pools.

UIManager
→ puede pedir sprites o pantallas.

LevelManager
→ solicita preload de assets de nivel.

Addressables
→ mecanismo de carga posible.

ScriptableObjects
→ datos configurables.
```

Separación importante:

```txt
AssetManager carga prefab.
Factory instancia objeto.
PoolManager reutiliza objeto.
Sistema de gameplay decide cuándo usarlo.
```

---

## Ciclo de vida

Flujo posible:

```txt
Initialize
→ preparar sistema de carga.

LoadAsset
→ cargar o devolver desde cache.

PreloadGroup
→ cargar conjunto de recursos.

ReleaseAsset
→ liberar recurso puntual.

UnloadGroup
→ liberar grupo.

Shutdown
→ liberar todo si corresponde.
```

Si usa Addressables, debe controlar handles y release.

---

## API mínima recomendada

Ejemplo simple:

```csharp
public interface IAssetManager
{
    Task<T> LoadAsync<T>(string assetId) where T : class;
    void Release(string assetId);
}
```

Ejemplo con grupos:

```csharp
public interface IAssetManager
{
    Task PreloadGroupAsync(string groupId);
    Task<T> LoadAsync<T>(string assetId) where T : class;
    void Release(string assetId);
    void UnloadGroup(string groupId);
}
```

No exponer caches internas si no hace falta.

---

## Ejemplo aplicado a videojuegos

Tower Defense:

```txt
LevelManager entra a Level 1.
Solicita AssetManager.PreloadGroup("Level1").
TowerFactory pide prefab de torre.
EnemyFactory pide prefab de enemigo.
PoolManager prepara proyectiles.
Al salir del nivel, AssetManager.UnloadGroup("Level1").
```

Cada pieza mantiene su responsabilidad.

---

## Errores comunes

```txt
no liberar assets,
cache infinita,
cargar durante gameplay crítico,
usar strings mágicos sin control,
hacer gameplay dentro del AssetManager,
duplicar responsabilidad con Factory,
exponer diccionario interno,
no manejar errores de carga,
no diferenciar preload de carga bajo demanda.
```

---

## Checklist para IA/agente

Antes de crear o modificar `AssetManager`:

```txt
¿Qué problema de carga existe?
¿Hay Addressables?
¿Hay cache?
¿Hay release?
¿Quién solicita assets?
¿Quién instancia objetos?
¿Qué assets se precargan?
¿Qué assets se liberan?
¿Qué pasa al cambiar de nivel?
¿Se evita lógica de gameplay?
¿Se evita reemplazar Factory o Pool?
```

---

## Regla final

`AssetManager` administra recursos.

```txt
Sano:
carga, cachea, libera.

Peligroso:
decide gameplay, instancia todo y nunca libera nada.
```
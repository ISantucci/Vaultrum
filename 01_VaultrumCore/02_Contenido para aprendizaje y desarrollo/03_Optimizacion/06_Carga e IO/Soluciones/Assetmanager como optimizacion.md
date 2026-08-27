## Definicion

AssetManager como optimizacion es una solucion concreta para centralizar la carga, descarga, cache y acceso a assets dentro de un proyecto.

En esta seccion, el foco esta en su utilidad para rendimiento y memoria.

El analisis del AssetManager como manager completo corresponde a la seccion de Managers.

La idea principal es:

```txt
Gameplay
→ pide recurso

AssetManager
→ gestiona carga, cache y liberacion

Sistema interno
→ puede usar Addressables, Resources u otra estrategia
```

El AssetManager evita que cada sistema del juego cargue assets a su manera.

---

## Que problema ayuda a prevenir

Ayuda a prevenir:

```txt
Assets cargados innecesariamente.
Cargas duplicadas.
Memoria alta.
Recursos que no se liberan.
Gameplay acoplado a rutas o keys.
Escenas demasiado pesadas.
Carga desordenada durante gameplay.
Falta de control sobre que esta cargado.
```

Ejemplo malo:

```txt
EnemySpawner
→ carga enemigos

TowerFactory
→ carga torres

UIManager
→ carga iconos

AudioSystem
→ carga sonidos

Cada uno con su propia logica.
```

Ejemplo mas sano:

```txt
Todos piden recursos al AssetManager.

AssetManager centraliza:
carga,
cache,
liberacion,
errores,
estado de recursos.
```

---

## Como funciona

El AssetManager funciona como capa de acceso a assets.

Flujo conceptual:

```txt
Sistema necesita asset.
Sistema pide asset al AssetManager.
AssetManager revisa si ya esta cargado.
Si esta cargado, lo devuelve.
Si no esta cargado, lo carga.
Registra uso o referencia.
Cuando ya no hace falta, libera o reduce referencia.
```

Puede manejar:

```txt
Carga asincronica.
Precarga.
Cache.
Liberacion.
Conteo de referencias.
Errores de carga.
Assets por contexto.
Recursos por nivel.
```

Ejemplo conceptual:

```txt
LoadAsset
→ obtener o cargar recurso

ReleaseAsset
→ liberar o reducir uso

PreloadGroup
→ preparar recursos antes del gameplay

UnloadGroup
→ descargar recursos de un contexto anterior
```

---

## Como aplicarlo en videojuegos

Se puede aplicar a:

```txt
Prefabs de enemigos.
Torres.
Proyectiles.
Efectos.
Iconos.
Audio.
UI.
Texturas.
Modelos.
Escenas.
Contenido por nivel.
```

Ejemplo Tower Defense:

```txt
LevelLoader
→ pide precargar assets del nivel.

AssetManager
→ carga enemigos, torres y efectos necesarios.

EnemyFactory
→ pide prefab al AssetManager.

ProjectilePool
→ pide prefab de proyectil al AssetManager.

Al salir del nivel:
AssetManager libera recursos del nivel.
```

Esto permite controlar mejor memoria y carga.

---

## Relacion con arquitectura

Se relaciona con:

```txt
Addressables como metodologia de optimizacion
Factory
Object pool como optimizacion
Memory Profiler
Memory Leak
Recursos de hardware
```

Tambien se relaciona con S - Single Responsibility Principle.

```txt
Gameplay
→ decide que necesita.

AssetManager
→ decide como cargarlo y administrarlo.
```

En una arquitectura sana:

```txt
Factory
→ crea objetos.

Object Pool
→ reutiliza objetos.

AssetManager
→ provee assets necesarios.
```

No conviene mezclar esas responsabilidades.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
RAM
VRAM
Disco
CPU
Tiempo de carga
Frame Budget
```

Puede ayudar a:

```txt
Reducir memoria cargada.
Evitar duplicacion de assets.
Preparar recursos antes de gameplay.
Evitar cargas en momentos criticos.
Liberar recursos no usados.
```

Pero si esta mal diseñado puede provocar:

```txt
Memory leaks.
Carga duplicada.
Stuttering.
Referencias viejas.
Errores por assets no disponibles.
```

---

## Cuando conviene usarlo

Conviene cuando:

```txt
Hay muchos assets.
Hay carga dinamica.
Hay contenido por nivel.
Hay factories que necesitan prefabs.
Hay pools que necesitan prefabs.
Hay recursos que deben precargarse.
Hay que liberar assets al cambiar contexto.
Hay riesgo de memoria alta.
```

Ejemplos:

```txt
Juegos medianos o grandes.
Tower Defense con muchas torres/enemigos.
Juegos con niveles variados.
Juegos con skins.
Juegos con audio/visual pesado.
```

---

## Cuando NO conviene usarlo

No conviene cuando:

```txt
El proyecto es chico.
Hay pocos assets.
No hay carga dinamica.
No hay problema de memoria.
No hay problema de organizacion.
La complejidad supera el beneficio.
```

Ejemplo:

```txt
Prototipo simple con pocos prefabs referenciados por Inspector
→ puede no necesitar AssetManager todavia.
```

---

## Trade-offs

Ventajas:

```txt
Centraliza carga.
Reduce duplicacion.
Mejora control de memoria.
Ordena acceso a assets.
Facilita precarga.
Facilita descarga.
Separa gameplay de infraestructura.
```

Costos:

```txt
Mas arquitectura.
Mas inicializacion.
Manejo de asincronia.
Manejo de errores.
Necesidad de liberar correctamente.
Riesgo de manager gigante.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Convertirlo en Service Locator descontrolado.
No liberar assets.
Cachear todo para siempre.
Cargar assets en gameplay critico.
No manejar referencias.
No saber quien usa cada asset.
Mezclar carga con creacion de gameplay.
Mezclar AssetManager con Factory.
Mezclar AssetManager con Pool.
```

Ejemplo malo:

```txt
AssetManager
→ carga prefab
→ instancia enemigo
→ decide spawn
→ registra enemigo
→ lo mete en pool
```

Eso mezcla demasiadas responsabilidades.

Mejor:

```txt
AssetManager
→ provee prefab

Factory
→ crea enemigo

Pool
→ reutiliza enemigo

Spawner
→ decide cuando aparece
```

---

## Relacion con Managers

Este documento analiza AssetManager como solucion de optimizacion.

En la seccion de Managers deberia existir un documento especifico sobre:

```txt
AssetManager
```

Ese documento deberia profundizar en:

```txt
Responsabilidad del manager.
Ciclo de vida.
API publica.
Persistencia.
Relacion con escenas.
Relacion con Addressables.
Relacion con Factory.
Relacion con Object Pool.
Cache interna.
Liberacion de recursos.
Errores de arquitectura.
Riesgos de singleton o Service Locator.
```

Separacion recomendada:

```txt
Optimizacion / Carga e IO / Soluciones / AssetManager como optimizacion
→ por que ayuda al rendimiento, memoria y carga.

Managers / AssetManager
→ como diseñarlo como manager sano y mantenible.
```

---

## Checklist de implementacion

```txt
¿Hay problema real de memoria, carga u organizacion?
¿Se midio con Profiler o Memory Profiler?
¿El gameplay esta acoplado a rutas o keys?
¿Hay cargas duplicadas?
¿Hay recursos que deberian precargarse?
¿Hay recursos que deberian liberarse?
¿Se definio responsabilidad del AssetManager?
¿Se evita mezclarlo con Factory?
¿Se evita mezclarlo con Pool?
¿Se manejan errores de carga?
¿Se valida antes/despues?
```

---

## Regla final

AssetManager como optimizacion sirve para controlar como el juego accede a recursos.

```txt
AssetManager
→ administra assets

No:
→ decide gameplay
→ instancia todo
→ reemplaza Factory
→ reemplaza Pool
```

En Optimizacion importa que problema de memoria, carga o rendimiento ayuda a resolver.

En Managers importara como diseñarlo correctamente.
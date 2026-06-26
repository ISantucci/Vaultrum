## Descripción

Un `PoolManager` administra objetos reutilizables.

Su función es controlar creación inicial, entrega, devolución, reset y limpieza de objetos que aparecen y desaparecen frecuentemente.

No reemplaza al patrón Object Pool.

Lo administra.

---

## Qué problema resuelve

Resuelve problemas como:

```txt
Instantiate constante,
Destroy constante,
picos de GC,
costo de creación repetida,
objetos temporales frecuentes,
necesidad de reset controlado,
múltiples pools sin coordinación.
```

Ejemplos:

```txt
proyectiles,
partículas,
efectos visuales,
enemigos frecuentes,
números flotantes de daño,
marcadores temporales.
```

---

## Cuándo conviene usarlo

Conviene cuando:

```txt
un objeto se crea y destruye muchas veces,
hay spikes por Instantiate/Destroy,
hay muchas instancias similares,
se necesita reutilización controlada,
se midió o se anticipa un costo claro.
```

---

## Cuándo NO conviene usarlo

No conviene si:

```txt
el objeto aparece muy pocas veces,
el ciclo de vida es simple,
la pool agrega más complejidad que beneficio,
el objeto tiene estado muy difícil de resetear,
o no hay problema real de performance.
```

Tampoco conviene usar pool para todo por costumbre.

---

## Responsabilidades permitidas

Puede encargarse de:

```txt
crear pool inicial,
entregar objeto disponible,
recibir objeto usado,
resetear objeto,
expandir pool si corresponde,
limpiar objetos activos,
destruir pool al salir de contexto,
mantener pools por tipo o ID.
```

---

## Responsabilidades prohibidas

No debería:

```txt
calcular daño,
decidir disparos,
elegir objetivos,
manejar economía,
actualizar UI,
decidir reglas de spawn,
controlar oleadas,
reemplazar factories completamente si hay lógica de creación compleja.
```

Regla:

```txt
PoolManager entrega y recupera objetos.
No decide por qué existen.
```

---

## Relación con otras piezas arquitectónicas

Relaciones comunes:

```txt
Factory
→ crea objetos si hace falta inicialización compleja.

AssetManager
→ provee prefabs.

Tower
→ solicita proyectil.

Projectile
→ se devuelve al pool al terminar.

UpdateManager
→ puede registrar/desregistrar objetos pooled.

LevelManager
→ limpia pools al salir del nivel.
```

---

## Ciclo de vida

Flujo típico:

```txt
InitializePool
→ crear objetos iniciales.

Get
→ entregar objeto.

Release
→ devolver objeto.

Reset
→ limpiar estado.

Clear
→ limpiar pool al salir.
```

Punto crítico:

```txt
Todo objeto reutilizado debe resetear su estado.
```

---

## API mínima recomendada

```csharp
public interface IPool<T>
{
    T Get();
    void Release(T instance);
}
```

Versión por ID:

```csharp
public interface IPoolManager
{
    T Get<T>(string poolId);
    void Release<T>(string poolId, T instance);
    void Clear(string poolId);
}
```

No agregar IDs, grupos o prioridades si el proyecto no lo necesita.

---

## Ejemplo aplicado a videojuegos

Tower Defense:

```txt
Tower decide disparar.
ProjectilePoolManager.Get("basic_projectile").
Projectile se inicializa con dirección, daño y objetivo.
Cuando impacta, ProjectilePoolManager.Release(projectile).
```

El pool no calcula daño ni elige objetivo.

Solo administra reutilización.

---

## Errores comunes

```txt
no resetear estado,
devolver objeto dos veces,
seguir actualizando objeto desactivado,
referencias viejas,
pool infinita,
no limpiar al cambiar escena,
mezclar lógica de gameplay,
usar pool para objetos que no lo necesitan,
no medir si aporta beneficio.
```

---

## Checklist para IA/agente

Antes de crear o modificar `PoolManager`:

```txt
¿Qué objeto se reutiliza?
¿Cuántas veces aparece?
¿Qué costo evita?
¿Cómo se resetea?
¿Quién pide objetos?
¿Quién los devuelve?
¿Qué pasa al cambiar nivel?
¿La pool puede crecer?
¿Hay límite?
¿Se evita lógica de gameplay?
¿Se valida que no conserva estado viejo?
```

---

## Regla final

`PoolManager` administra reutilización.

```txt
Sano:
entrega, recibe, resetea, limpia.

Peligroso:
decide gameplay y reutiliza objetos con estado corrupto.
```
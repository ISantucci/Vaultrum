## Descripción

Un `UpdateManager` administra actualizaciones registradas.

Su objetivo es reemplazar muchos `Update` dispersos por un sistema centralizado y controlado cuando existe un problema real de frecuencia, orden o costo.

No debe usarse por moda.

Debe justificarse por arquitectura u optimización.

---

## Qué problema resuelve

Resuelve problemas como:

```txt
muchos MonoBehaviour.Update activos,
actualizaciones innecesarias cada frame,
falta de control de frecuencia,
dificultad para pausar grupos,
necesidad de ordenar ticks,
costos repetidos,
spikes por lógica dispersa.
```

Ejemplo:

```txt
100 enemigos no necesitan recalcular objetivo cada frame.
UpdateManager puede actualizarlos cada 0.2 segundos.
```

---

## Cuándo conviene usarlo

Conviene cuando:

```txt
hay muchos objetos actualizándose,
hay lógica que puede actualizarse a menor frecuencia,
se necesita pausar grupos,
se necesita controlar orden,
se quiere reducir callbacks de Unity,
se detectó costo en Profiler.
```

También es útil en proyectos con restricción de pocos MonoBehaviours.

---

## Cuándo NO conviene usarlo

No conviene si:

```txt
hay pocos objetos,
el costo de Update no es problema,
centralizar complica más de lo que ayuda,
cada objeto necesita lógica muy distinta,
o se quiere usar para meter todo el gameplay en una lista global.
```

Regla:

```txt
UpdateManager no optimiza si hace el mismo trabajo que antes, solo centralizado.
```

---

## Responsabilidades permitidas

Puede encargarse de:

```txt
registrar objetos actualizables,
desregistrar objetos,
ejecutar Tick,
controlar frecuencia,
pausar grupos,
reanudar grupos,
ordenar ejecución si está justificado,
evitar modificación de listas durante iteración.
```

---

## Responsabilidades prohibidas

No debería:

```txt
decidir gameplay,
calcular daño,
mover todos los objetos directamente,
conocer tipos concretos innecesarios,
hacer lógica específica por enemigo/torre/proyectil,
actualizar UI sin necesidad,
convertirse en loop gigante de todo el juego.
```

---

## Relación con otras piezas arquitectónicas

Relaciones comunes:

```txt
MonoBehaviour
→ puente con Unity Update.

IUpdatable
→ contrato para sistemas actualizables.

GameManager
→ puede pausar el UpdateManager.

StateMachineManager
→ puede habilitar/deshabilitar ticks según estado.

PoolManager
→ objetos pooled se registran/desregistran al activarse/desactivarse.
```

---

## Ciclo de vida

Flujo típico:

```txt
Awake
→ preparar colecciones.

Register
→ agregar actualizable.

Unregister
→ quitar actualizable.

Update
→ llamar Tick controlado.

Shutdown
→ limpiar listas.
```

Cuidado con modificar listas mientras se iteran.

Estrategias:

```txt
listas pendingAdd/pendingRemove,
copias temporales controladas,
flags de actividad,
procesamiento al final del frame.
```

---

## API mínima recomendada

```csharp
public interface IUpdatable
{
    void Tick(float deltaTime);
}
```

```csharp
public interface IUpdateManager
{
    void Register(IUpdatable target);
    void Unregister(IUpdatable target);
    void Pause();
    void Resume();
}
```

Para frecuencias:

```csharp
public interface IFixedFrequencyUpdatable
{
    float TickInterval { get; }
    void Tick(float deltaTime);
}
```

Solo agregar complejidad si hace falta.

---

## Ejemplo aplicado a videojuegos

Tower Defense:

```txt
EnemyMovement
→ necesita avanzar.

TowerTargeting
→ no necesita buscar objetivo cada frame.

UpdateManager
→ registra TowerTargeting con menor frecuencia.

Projectile
→ puede actualizarse normalmente o por pool.
```

Resultado:

```txt
menos updates dispersos,
mejor control de frecuencia,
más fácil pausar gameplay.
```

---

## Errores comunes

```txt
crear UpdateManager sin medir,
meter toda la lógica en Tick,
no desregistrar objetos destruidos,
modificar lista mientras se itera,
usar interfaces gigantes,
no controlar pausa,
hacer casts por tipo concreto,
actualizar todo cada frame igual que antes.
```

---

## Checklist para IA/agente

Antes de proponer `UpdateManager`:

```txt
¿Hay muchos Updates activos?
¿Hay evidencia de costo?
¿La frecuencia puede reducirse?
¿Qué objetos se registran?
¿Cuándo se desregistran?
¿Hay pausa?
¿Hay grupos?
¿Se evita modificar listas durante iteración?
¿Se mantiene la lógica en cada objeto/sistema?
¿UpdateManager solo coordina ticks?
```

---

## Regla final

`UpdateManager` sirve para controlar frecuencia y ejecución.

No sirve para centralizar toda la lógica del juego.

```txt
Sano:
registra, ejecuta, pausa, controla frecuencia.

Peligroso:
se convierte en Update gigante global.
```
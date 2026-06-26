## Definición

Cachear referencias significa guardar una referencia para reutilizarla después, en lugar de buscarla repetidamente.

La idea principal es:

```txt
Buscar una vez
→ guardar referencia
→ reutilizar
```

Esto evita búsquedas costosas o innecesarias durante gameplay.

---

## Qué problema ayuda a prevenir

Ayuda principalmente con:

```txt
Busquedas globales por frame
CPU Bound
GC Alloc por búsquedas que crean arrays
Dependencias poco claras
Scripts que buscan objetos constantemente
```

Ejemplo problemático:

```csharp
private void Update()
{
    Player player = FindObjectOfType<Player>();
}
```

Ejemplo mejor:

```csharp
private Player player;

private void Awake()
{
    player = FindObjectOfType<Player>();
}
```

Mejor todavía:

```txt
Spawner / Factory / Installer
→ entrega referencia al crear el objeto
```

---

## Cómo funciona

La referencia se obtiene una vez y se guarda en un campo.

Ejemplo:

```csharp
public class EnemyController : MonoBehaviour
{
    [SerializeField] private Player player;

    private void Update()
    {
        if (player == null)
        {
            return;
        }

        // usar player sin buscarlo cada frame
    }
}
```

Otra opción:

```csharp
public void Initialize(Player playerReference)
{
    player = playerReference;
}
```

Esto permite que otro sistema entregue la dependencia.

---

## Cómo aplicarlo en videojuegos

Aplicaciones:

```txt
Jugador.
Cámara.
GameManager.
AudioManager.
EnemyRegistry.
TowerRegistry.
HUD.
Factories.
Pools.
Servicios.
Componentes internos.
```

Ejemplo:

```txt
EnemySpawner
→ crea enemigo
→ le pasa referencia al jugador

Enemy
→ usa referencia cacheada
→ no busca al jugador cada frame
```

Para componentes:

```csharp
private Rigidbody rb;

private void Awake()
{
    rb = GetComponent<Rigidbody>();
}
```

Esto evita llamar `GetComponent` constantemente.

---

## Relación con arquitectura

Se relaciona con:

```txt
Busquedas globales por frame
Memory Leak
MonoBehaviour como puente
Factory
Service Locator
Facade
```

Cachear referencias también obliga a pensar:

```txt
¿Quién entrega la dependencia?
¿Quién es dueño de esa referencia?
¿Cuánto tiempo vive?
¿Qué pasa al cambiar escena?
```

Una referencia mal cacheada puede convertirse en problema de ciclo de vida.

---

## Relación con hardware/runtime

Afecta principalmente:

```txt
CPU
Frame Budget
Game Loop
```

Puede afectar indirectamente:

```txt
GC
```

si reemplaza búsquedas que generaban arrays o allocations.

---

## Cuándo conviene usarlo

Conviene cachear cuando:

```txt
La referencia se usa muchas veces.
La búsqueda sería repetida.
La dependencia es estable.
La referencia se conoce al inicializar.
La búsqueda ocurre en runtime crítico.
```

Ejemplos:

```txt
Player en enemigos.
Rigidbody en movimiento.
Animator en controlador.
HUD en manager.
Pool en sistema de disparo.
```

---

## Cuándo NO conviene usarlo

No conviene cachear sin pensar cuando:

```txt
La referencia cambia constantemente.
El objeto puede destruirse y recrearse.
Hay cambios de escena.
La referencia pertenece a una escena temporal.
No hay control de ciclo de vida.
```

Ejemplo peligroso:

```txt
Singleton persistente cachea HUD de escena.
La escena cambia.
HUD viejo se destruye.
Singleton conserva referencia vieja.
```

---

## Trade-offs

Ventajas:

```txt
Menos búsquedas.
Más rendimiento.
Dependencias más claras.
Menos trabajo por frame.
```

Costos:

```txt
Hay que inicializar correctamente.
Hay que manejar referencias nulas.
Hay que limpiar al cambiar escena.
Hay que evitar referencias viejas.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Referencias viejas.
Memory leaks.
Objetos destruidos retenidos.
Dependencias ocultas.
Inicialización en orden incorrecto.
NullReferenceException.
```

Ejemplo:

```txt
Manager persistente
→ guarda referencia a objeto de escena

Cambio de escena
→ objeto destruido

Manager
→ intenta usar referencia vieja
```

Solución:

```txt
Rebind controlado.
Limpiar referencias.
Desuscribirse de eventos.
No retener objetos de escena sin necesidad.
```

---

## Checklist de implementación

```txt
¿La referencia se usa frecuentemente?
¿La búsqueda ocurría en Update?
¿La referencia es estable?
¿Quién la asigna?
¿Puede quedar vieja?
¿Qué pasa al cambiar escena?
¿Se limpia si el objeto muere?
¿Hay validación de null?
¿Se midió mejora si era un problema de rendimiento?
```

---

## Regla final

Cachear referencias mejora rendimiento cuando evita búsquedas repetidas.

Pero una referencia cacheada también tiene ciclo de vida.

```txt
Cachear
→ guardar para reutilizar

No:
→ retener para siempre sin control
```
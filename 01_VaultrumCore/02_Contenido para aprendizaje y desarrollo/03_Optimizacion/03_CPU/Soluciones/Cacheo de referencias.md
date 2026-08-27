## Definicion

Cachear referencias significa guardar una referencia para reutilizarla despues, en lugar de buscarla repetidamente.

La idea principal es:

```txt
Buscar una vez
→ guardar referencia
→ reutilizar
```

Esto evita busquedas costosas o innecesarias durante gameplay.

---

## Que problema ayuda a prevenir

Ayuda principalmente con:

```txt
Busquedas globales por frame
CPU Bound
GC Alloc por busquedas que crean arrays
Dependencias poco claras
Scripts que buscan objetos constantemente
```

Ejemplo problematico:

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

Mejor todavia:

```txt
Spawner / Factory / Installer
→ entrega referencia al crear el objeto
```

---

## Como funciona

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

Otra opcion:

```csharp
public void Initialize(Player playerReference)
{
    player = playerReference;
}
```

Esto permite que otro sistema entregue la dependencia.

---

## Como aplicarlo en videojuegos

Aplicaciones:

```txt
Jugador.
Camara.
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

## Relacion con arquitectura

Se relaciona con:

```txt
Busquedas globales por frame
Memory Leak
MonoBehaviour como puente
Factory
Service Locator
Facade
```

Cachear referencias tambien obliga a pensar:

```txt
¿Quien entrega la dependencia?
¿Quien es dueño de esa referencia?
¿Cuanto tiempo vive?
¿Que pasa al cambiar escena?
```

Una referencia mal cacheada puede convertirse en problema de ciclo de vida.

---

## Relacion con hardware/runtime

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

si reemplaza busquedas que generaban arrays o allocations.

---

## Cuando conviene usarlo

Conviene cachear cuando:

```txt
La referencia se usa muchas veces.
La busqueda seria repetida.
La dependencia es estable.
La referencia se conoce al inicializar.
La busqueda ocurre en runtime critico.
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

## Cuando NO conviene usarlo

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
Menos busquedas.
Mas rendimiento.
Dependencias mas claras.
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
Inicializacion en orden incorrecto.
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

Solucion:

```txt
Rebind controlado.
Limpiar referencias.
Desuscribirse de eventos.
No retener objetos de escena sin necesidad.
```

---

## Checklist de implementacion

```txt
¿La referencia se usa frecuentemente?
¿La busqueda ocurria en Update?
¿La referencia es estable?
¿Quien la asigna?
¿Puede quedar vieja?
¿Que pasa al cambiar escena?
¿Se limpia si el objeto muere?
¿Hay validacion de null?
¿Se midio mejora si era un problema de rendimiento?
```

---

## Regla final

Cachear referencias mejora rendimiento cuando evita busquedas repetidas.

Pero una referencia cacheada tambien tiene ciclo de vida.

```txt
Cachear
→ guardar para reutilizar

No:
→ retener para siempre sin control
```
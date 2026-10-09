## Definicion

Batch processing consiste en procesar en grupo a muchas entidades que hacen operaciones semejantes, en vez de repartir esa logica por objetos.

```txt
Enemy 1 Update
Enemy 2 Update
Enemy 3 Update
...
```

se convierte en:

```txt
EnemySystem
    procesa enemies
```

El comportamiento es el mismo.

Lo que cambia es quien lo ejecuta y en que orden.

```txt
Antes:
N objetos, cada uno con su callback,
en un orden que nadie controla.

Despues:
un sistema, un recorrido,
en un orden conocido.
```

El patron no pertenece a un recurso ni a un subsistema.

Aparece en gameplay, en fisica, en IA, en animacion y en rendering, donde agrupar trabajo compatible es exactamente lo que hace el batching de dibujo.

---

## Que problema ayuda a prevenir

Ayuda con:

```txt
Muchisimos callbacks por frame.
Costo repartido en cientos de entradas del Profiler.
Logica de gameplay dispersa por la escena.
Datos leidos salteados por toda la memoria.
Imposibilidad de cambiar el orden de ejecucion.
Dificultad para atacar un costo que no esta en ningun lugar concreto.
```

El sintoma tipico no es un pico.

```txt
Ninguna entidad aparece como cara.
El sistema entero si lo es.
```

Un costo repartido en mil lugares es un costo que no se puede atacar.

---

## Como funciona

El sistema mantiene la coleccion y hace un solo recorrido.

Version dispersa:

```csharp
public class Enemy : MonoBehaviour
{
    private void Update()
    {
        Move();
        CheckTarget();
    }
}
```

Version agrupada:

```csharp
public class EnemySystem
{
    private readonly List<EnemyData> enemies = new();

    public void Tick(float dt)
    {
        for (int i = 0; i < enemies.Count; i++)
            Move(enemies[i], dt);

        for (int i = 0; i < enemies.Count; i++)
            CheckTarget(enemies[i]);
    }
}
```

Los dos recorridos separados no son un detalle menor.

```txt
Una pasada
→ una operacion
→ datos parecidos
→ mejor localidad de datos
```

La forma general del patron es siempre la misma.

```txt
Coleccion
↓
una pasada por operacion
↓
datos contiguos
↓
un solo punto de costo medible
```

Ese ultimo punto es el que mas rinde en la practica.

```txt
Un sistema
→ una entrada en el Profiler
→ un lugar donde optimizar
```

---

## Como aplicarlo en videojuegos

En gameplay:

```txt
Movimiento de proyectiles.
Timers y cooldowns.
Aplicacion de daño en area.
Estados alterados.
```

En IA:

```txt
Percepcion de todos los agentes en una pasada.
Seleccion de objetivo por grupo.
Reevaluacion de decisiones escalonada.
```

En animacion y particulas:

```txt
Evaluacion agrupada en vez de una por objeto.
```

Ejemplo en un Tower Defense:

```txt
ProjectileSystem
    avanza todos los proyectiles
    resuelve impactos
    devuelve los agotados al pool

EnemySystem
    avanza a los enemigos por la ruta
    aplica daño recibido
    marca los que murieron

TowerSystem
    reevalua objetivos
    dispara las torres listas
```

Y el resultado en el Profiler:

```txt
Antes:
300 entradas de Enemy.Update.

Despues:
una entrada de EnemySystem.Tick.
```

Este criterio quedo consolidado en Capsule Survivor, donde los sistemas de gameplay pasaron a recorrer sus propias colecciones en vez de depender de un callback por objeto.

---

## Relacion con arquitectura

Se relaciona con:

```txt
Separacion model view.
Clases puras.
Active Set.
Control explicito del orden de ejecucion.
```

El patron pide que el dato de la entidad viva separado de su representacion.

```txt
Datos de la entidad
→ los recorre el sistema

Representacion en escena
→ refleja el resultado
```

Y habilita algo que la version dispersa no permite:

```txt
Orden de ejecucion decidido
→ primero movimiento
→ despues colisiones
→ despues daño
→ despues muerte
```

Con callbacks repartidos, ese orden depende de como Unity resuelva la escena.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
CPU
Frame Budget
```

Puede afectar tambien:

```txt
Memoria
```

por el layout de las colecciones que el sistema mantiene.

Lo que mejora es la localidad de datos.

```txt
Datos dispersos
→ cada acceso puede fallar la cache

Datos contiguos y recorridos en orden
→ mejor aprovechamiento de cada lectura
```

Y ademas se reduce el overhead de invocacion.

```txt
Costo unitario bajo
×
muchisimas invocaciones
= costo real alto
```

El patron ataca el segundo factor sin tocar el primero.

---

## Cuando conviene usarlo

Conviene cuando:

```txt
Hay muchas entidades haciendo lo mismo.
El costo aparece repartido y no concentrado.
El orden de ejecucion importa.
Se quiere poder medir y atacar el costo en un lugar.
La logica no depende de callbacks propios de cada objeto.
```

Casos claros:

```txt
Proyectiles.
Enemigos de oleada.
Particulas de gameplay.
Agentes con la misma rutina de percepcion.
```

---

## Cuando NO conviene usarlo

No conviene cuando:

```txt
Hay pocas entidades.
Cada entidad hace algo distinto.
El comportamiento es muy dependiente de componentes de escena.
El costo actual ya entra comodo en presupuesto.
La reorganizacion cuesta mas de lo que ahorra.
```

Un caso frecuente de mal encaje:

```txt
Diez entidades unicas, con reglas distintas,
metidas en un mismo sistema
solo para tener un recorrido.
```

Ahi no hay trabajo semejante que agrupar, y el sistema termina lleno de condicionales.

---

## Trade-offs

Ventajas:

```txt
Menos callbacks por frame.
Mejor localidad de datos.
Orden de ejecucion controlado.
Costo medible y atacable en un solo lugar.
Base natural para reducir precision o achicar el conjunto activo.
```

Costos:

```txt
Registro y baja de entidades.
Mas indireccion entre dato y representacion.
Mas diseño inicial.
Riesgo de concentrar demasiado en un sistema.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Convertir el sistema en una clase dios.
Meter reglas de entidades distintas en el mismo recorrido.
Llenar la pasada de condicionales por tipo.
No dar de baja entidades destruidas.
Recorrer la coleccion mientras se la modifica.
Agrupar sin medir el estado previo.
```

El riesgo principal es el primero.

```txt
EnemySystem
    movimiento
    percepcion
    daño
    audio
    UI
    drops
    guardado
```

Un sistema que recorre entidades es un lugar comodo para seguir agregando cosas.

```txt
Un sistema por operacion
≠
un sistema para todo lo que sea enemigos
```

Cuando el sistema absorbe responsabilidades, se pierde justo lo que el patron habia ganado: un costo claro y atacable.

---

## Checklist de implementacion

```txt
¿Cuantas entidades hacen esta misma operacion?
¿La operacion es realmente semejante entre ellas?
¿Quien es el dueño de la coleccion?
¿Como entra y como sale una entidad?
¿El recorrido tolera bajas durante la pasada?
¿Hay una pasada por operacion o una pasada que hace todo?
¿Cuantas responsabilidades acumula el sistema?
¿Hay condicionales por tipo dentro del recorrido?
¿El orden de ejecucion quedo explicito?
¿Aparece como una sola entrada en el Profiler?
¿Se midio antes y despues?
```

---

## Regla final

El trabajo semejante conviene junto, y con un solo dueño.

```txt
Una coleccion, una pasada, un costo visible.
Un sistema por operacion.
Un sistema que hace de todo vuelve a esconder el costo.
```

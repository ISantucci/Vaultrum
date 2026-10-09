## Definicion

MonoBehaviour como puente es una metodologia donde los `MonoBehaviour` se usan principalmente para conectar la logica del juego con Unity.

Unity trabaja con:

```txt
GameObjects
Inspector
Transform
Escena
Callbacks
Serializacion
Componentes
```

Pero no toda la logica necesita vivir directamente dentro de un `MonoBehaviour`.

La idea principal es:

```txt
MonoBehaviour
→ conecta con Unity

Clase pura
→ contiene logica
```

---

## Que problema ayuda a prevenir

Ayuda a prevenir:

```txt
Scripts gigantes.
Exceso de MonoBehaviours.
Logica demasiado acoplada a Unity.
Dificultad para testear.
Dificultad para reutilizar sistemas.
Muchos Update activos.
Dependencia innecesaria de escena.
```

Tambien ayuda cuando hay restricciones arquitectonicas, por ejemplo:

```txt
usar pocos MonoBehaviours,
centralizar updates,
separar logica de runtime,
crear sistemas mas testeables.
```

---

## Como funciona

Un `MonoBehaviour` recibe eventos de Unity y delega logica a una clase normal.

Ejemplo:

```csharp
public class EnemyController : MonoBehaviour
{
    private EnemyBrain brain;

    private void Awake()
    {
        brain = new EnemyBrain();
    }

    private void Update()
    {
        brain.Tick(Time.deltaTime);
    }
}
```

La clase pura contiene la logica:

```csharp
public class EnemyBrain
{
    public void Tick(float deltaTime)
    {
        // logica de decision sin depender directamente de Unity
    }
}
```

El `MonoBehaviour` sabe de Unity.

La clase pura sabe de reglas.

---

## Como aplicarlo en videojuegos

Aplicaciones tipicas:

```txt
IA.
Sistemas de daño.
Calculo de economia.
Seleccion de objetivos.
Validaciones.
Historial de comandos.
Reglas de inventario.
Pathfinding.
Sistemas de decision.
```

Ejemplo:

```txt
EnemyController : MonoBehaviour
→ lee posicion del Transform
→ delega decision a EnemyBrain
→ aplica movimiento en Unity
```

Otro ejemplo:

```txt
TowerView : MonoBehaviour
→ contiene referencias visuales

TowerLogic
→ calcula daño, cooldown y targeting
```

Esto permite separar:

```txt
Visual / Unity
→ MonoBehaviour

Reglas / logica
→ clase pura
```

---

## Relacion con arquitectura

Se relaciona con:

```txt
Clases puras
Update Manager como optimizacion
Separar logica de unity
Game Loop
Muchos update activos
```

Tambien se relaciona con SOLID:

```txt
Single Responsibility
→ MonoBehaviour no deberia hacer todo.

Dependency Inversion
→ logica puede depender de abstracciones, no directamente de Unity.

Interface Segregation
→ interfaces pequeñas para sistemas actualizables, dañables, seleccionables, etc.
```

Una estructura sana:

```txt
MonoBehaviour
→ adapta Unity

Sistema puro
→ decide / calcula / valida

Manager
→ coordina si hace falta
```

---

## Relacion con hardware/runtime

No mejora rendimiento automaticamente.

Pero puede ayudar indirectamente porque:

```txt
Reduce MonoBehaviours innecesarios.
Facilita Update Manager.
Facilita testeo.
Facilita medir sistemas por separado.
Evita logica dispersa.
Permite controlar frecuencia.
```

La ganancia viene de la arquitectura que habilita.

No de convertir una clase por convertirla.

---

## Cuando conviene usarlo

Conviene cuando:

```txt
La logica no necesita Inspector.
La logica no necesita Transform directo.
La logica no necesita callbacks de Unity.
La logica se quiere testear.
Hay reglas complejas.
Hay que reutilizar comportamiento.
Hay que reducir MonoBehaviours.
Hay que integrar con Update Manager.
```

Ejemplos:

```txt
DamageCalculator
EnemyBrain
TargetSelector
Pathfinder
EconomySystem
CommandHistory
UpgradeValidator
```

---

## Cuando NO conviene usarlo

No conviene forzarlo cuando:

```txt
La clase es puramente visual.
Depende completamente de Transform.
Depende de componentes de Unity todo el tiempo.
Es un script simple de escena.
Separar agregaria complejidad innecesaria.
```

Ejemplo:

```txt
Un script que solo rota un objeto visual decorativo
→ puede ser MonoBehaviour simple.
```

---

## Trade-offs

Ventajas:

```txt
Mejor separacion.
Mejor testeo.
Menos acoplamiento.
Mas reutilizacion.
Mas claridad.
Mejor integracion con managers.
```

Costos:

```txt
Mas archivos.
Mas inicializacion.
Mas necesidad de pasar dependencias.
Mas diseño previo.
Posible sobrearquitectura.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Crear clases puras que igual dependen de Unity por todos lados.
Duplicar estado entre MonoBehaviour y clase pura.
No saber quien es dueño del dato.
Pasar demasiadas dependencias.
Separar sistemas simples sin necesidad.
```

Ejemplo malo:

```txt
EnemyController
→ tiene vida

EnemyBrain
→ tambien tiene vida

Resultado:
estado duplicado e inconsistente.
```

Mejor:

```txt
EnemyHealth
→ dueño de vida

EnemyBrain
→ consulta o recibe informacion necesaria
```

---

## Checklist de implementacion

```txt
¿Esta logica necesita ser MonoBehaviour?
¿Necesita Inspector?
¿Necesita Transform?
¿Necesita Update propio?
¿Puede vivir en clase pura?
¿Quien es dueño del estado?
¿Como se inicializan dependencias?
¿Quien llama Tick?
¿Hay duplicacion de datos?
¿La separacion simplifica el sistema?
```

---

## Regla final

MonoBehaviour deberia ser la capa que conecta con Unity, no el lugar obligatorio para toda la logica.

```txt
Unity necesita MonoBehaviours.
Tu arquitectura no siempre.
```
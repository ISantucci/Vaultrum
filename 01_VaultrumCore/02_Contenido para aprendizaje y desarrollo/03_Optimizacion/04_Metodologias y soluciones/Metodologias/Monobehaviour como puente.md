## Definición

MonoBehaviour como puente es una metodología donde los `MonoBehaviour` se usan principalmente para conectar la lógica del juego con Unity.

Unity trabaja con:

```txt
GameObjects
Inspector
Transform
Escena
Callbacks
Serialización
Componentes
```

Pero no toda la lógica necesita vivir directamente dentro de un `MonoBehaviour`.

La idea principal es:

```txt
MonoBehaviour
→ conecta con Unity

Clase pura
→ contiene lógica
```

---

## Qué problema ayuda a prevenir

Ayuda a prevenir:

```txt
Scripts gigantes.
Exceso de MonoBehaviours.
Lógica demasiado acoplada a Unity.
Dificultad para testear.
Dificultad para reutilizar sistemas.
Muchos Update activos.
Dependencia innecesaria de escena.
```

También ayuda cuando hay restricciones arquitectónicas, por ejemplo:

```txt
usar pocos MonoBehaviours,
centralizar updates,
separar lógica de runtime,
crear sistemas más testeables.
```

---

## Cómo funciona

Un `MonoBehaviour` recibe eventos de Unity y delega lógica a una clase normal.

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

La clase pura contiene la lógica:

```csharp
public class EnemyBrain
{
    public void Tick(float deltaTime)
    {
        // lógica de decisión sin depender directamente de Unity
    }
}
```

El `MonoBehaviour` sabe de Unity.

La clase pura sabe de reglas.

---

## Cómo aplicarlo en videojuegos

Aplicaciones típicas:

```txt
IA.
Sistemas de daño.
Cálculo de economía.
Selección de objetivos.
Validaciones.
Historial de comandos.
Reglas de inventario.
Pathfinding.
Sistemas de decisión.
```

Ejemplo:

```txt
EnemyController : MonoBehaviour
→ lee posición del Transform
→ delega decisión a EnemyBrain
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

Reglas / lógica
→ clase pura
```

---

## Relación con arquitectura

Se relaciona con:

```txt
Clases puras
UpdateManager
Separar logica de unity
Game Loop
Muchos update activos
```

También se relaciona con SOLID:

```txt
Single Responsibility
→ MonoBehaviour no debería hacer todo.

Dependency Inversion
→ lógica puede depender de abstracciones, no directamente de Unity.

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

## Relación con hardware/runtime

No mejora rendimiento automáticamente.

Pero puede ayudar indirectamente porque:

```txt
Reduce MonoBehaviours innecesarios.
Facilita Update Manager.
Facilita testeo.
Facilita medir sistemas por separado.
Evita lógica dispersa.
Permite controlar frecuencia.
```

La ganancia viene de la arquitectura que habilita.

No de convertir una clase por convertirla.

---

## Cuándo conviene usarlo

Conviene cuando:

```txt
La lógica no necesita Inspector.
La lógica no necesita Transform directo.
La lógica no necesita callbacks de Unity.
La lógica se quiere testear.
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

## Cuándo NO conviene usarlo

No conviene forzarlo cuando:

```txt
La clase es puramente visual.
Depende completamente de Transform.
Depende de componentes de Unity todo el tiempo.
Es un script simple de escena.
Separar agregaría complejidad innecesaria.
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
Mejor separación.
Mejor testeo.
Menos acoplamiento.
Más reutilización.
Más claridad.
Mejor integración con managers.
```

Costos:

```txt
Más archivos.
Más inicialización.
Más necesidad de pasar dependencias.
Más diseño previo.
Posible sobrearquitectura.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Crear clases puras que igual dependen de Unity por todos lados.
Duplicar estado entre MonoBehaviour y clase pura.
No saber quién es dueño del dato.
Pasar demasiadas dependencias.
Separar sistemas simples sin necesidad.
```

Ejemplo malo:

```txt
EnemyController
→ tiene vida

EnemyBrain
→ también tiene vida

Resultado:
estado duplicado e inconsistente.
```

Mejor:

```txt
EnemyHealth
→ dueño de vida

EnemyBrain
→ consulta o recibe información necesaria
```

---

## Checklist de implementación

```txt
¿Esta lógica necesita ser MonoBehaviour?
¿Necesita Inspector?
¿Necesita Transform?
¿Necesita Update propio?
¿Puede vivir en clase pura?
¿Quién es dueño del estado?
¿Cómo se inicializan dependencias?
¿Quién llama Tick?
¿Hay duplicación de datos?
¿La separación simplifica el sistema?
```

---

## Regla final

MonoBehaviour debería ser la capa que conecta con Unity, no el lugar obligatorio para toda la lógica.

```txt
Unity necesita MonoBehaviours.
Tu arquitectura no siempre.
```
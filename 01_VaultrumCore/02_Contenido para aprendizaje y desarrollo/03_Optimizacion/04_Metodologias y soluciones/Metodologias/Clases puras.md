## Definición

Una clase pura es una clase común de C# que no hereda de `MonoBehaviour`.

No depende directamente de callbacks de Unity como:

```txt
Update
Awake
Start
FixedUpdate
LateUpdate
```

La idea principal es:

```txt
Clase pura
→ lógica sin dependencia directa de MonoBehaviour
```

Una clase pura puede contener reglas, cálculos, decisiones, validaciones, algoritmos o estructuras.

---

## Qué problema ayuda a prevenir

Ayuda a prevenir:

```txt
Exceso de MonoBehaviours.
Scripts gigantes.
Acoplamiento fuerte con Unity.
Dificultad para testear.
Dificultad para reutilizar lógica.
Lógica dispersa en escena.
Muchos Update activos.
Dependencia innecesaria del Inspector.
```

También ayuda en proyectos donde se quiere diseñar con:

```txt
SOLID.
Managers.
Update Manager.
Arquitectura escalable.
Sistemas testeables.
```

---

## Cómo funciona

Una clase pura se instancia desde otra clase o sistema.

Ejemplo:

```csharp
public class DamageCalculator
{
    public int Calculate(int baseDamage, float multiplier)
    {
        return Mathf.RoundToInt(baseDamage * multiplier);
    }
}
```

No necesita estar en un GameObject.

No necesita tener un componente en escena.

No necesita `Update()`.

Puede ser usada por un `MonoBehaviour`, manager o sistema.

```csharp
public class DamageDealer : MonoBehaviour
{
    private DamageCalculator calculator = new DamageCalculator();

    public void DealDamage()
    {
        int damage = calculator.Calculate(10, 1.5f);
    }
}
```

---

## Cómo aplicarlo en videojuegos

Buenas candidatas para clases puras:

```txt
Calculadoras de daño.
Validadores de compra.
Sistemas de economía.
Historial de comandos.
Algoritmos de pathfinding.
Estructuras de datos.
Selectores de objetivo.
Sistemas de decisión.
Reglas de upgrade.
Generadores de oleadas.
Modelos de datos.
```

Ejemplo:

```txt
UpgradeValidator
→ valida si se puede mejorar una torre.

TowerUpgradeComponent
→ aplica el resultado en Unity.

HUD
→ muestra feedback.
```

Otro ejemplo:

```txt
Pathfinder
→ calcula ruta.

EnemyMovement
→ mueve el Transform.
```

---

## Relación con arquitectura

Se relaciona con:

```txt
MonoBehaviour como puente
Separar logica de unity
UpdateManager
Game Loop
Estructuras de datos
Algoritmos
```

También se relaciona con patrones:

```txt
Command
Strategy
Factory
Observer
State
```

Muchos patrones se implementan mejor si la lógica no depende directamente de `MonoBehaviour`.

Ejemplo:

```txt
Command
→ puede ser clase pura.

Strategy
→ puede ser clase pura.

Pathfinder
→ puede ser clase pura.

Data model
→ puede ser clase pura.
```

---

## Relación con hardware/runtime

Las clases puras no optimizan mágicamente.

Pero ayudan a:

```txt
Reducir MonoBehaviours.
Evitar callbacks innecesarios.
Centralizar ejecución.
Testear lógica sin escena.
Controlar frecuencia desde managers.
Separar lógica pesada de Unity.
```

Esto puede mejorar la capacidad de optimizar.

---

## Cuándo conviene usarlas

Conviene usar clases puras cuando:

```txt
La lógica no necesita GameObject.
No necesita Inspector.
No necesita Transform.
No necesita callbacks de Unity.
Se quiere testear.
Se quiere reutilizar.
Se quiere separar responsabilidad.
Se quiere integrar con managers.
```

Ejemplos claros:

```txt
DamageCalculator
EconomyValidator
WaveDefinition
TargetSelector
Pathfinder
CommandHistory
UpgradeCostCalculator
```

---

## Cuándo NO conviene usarlas

No conviene forzarlas cuando:

```txt
La lógica depende totalmente de Unity.
El script es visual y simple.
La separación agrega más complejidad que valor.
El objeto necesita componentes de escena constantemente.
```

Ejemplo:

```txt
CameraFollow simple
→ puede ser MonoBehaviour.
```

---

## Trade-offs

Ventajas:

```txt
Más claridad.
Más testabilidad.
Menos acoplamiento.
Más reutilización.
Menos dependencia de escena.
Mejor integración con arquitectura.
```

Costos:

```txt
Más diseño.
Más inicialización.
Más dependencias explícitas.
Más archivos.
Posible sobrearquitectura.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Crear clases puras sin propósito claro.
Duplicar estado con MonoBehaviours.
Pasar demasiadas dependencias.
Hacer clases puras que igual dependen de UnityEngine innecesariamente.
Separar sistemas simples sin beneficio.
```

Ejemplo malo:

```txt
EnemyView
EnemyLogic
EnemyModel
EnemyRuntimeData
EnemyAdapter

Para un enemigo de prototipo simple.
```

Eso puede ser exceso.

---

## Checklist de implementación

```txt
¿La clase necesita heredar MonoBehaviour?
¿Necesita Inspector?
¿Necesita Transform?
¿Necesita callbacks de Unity?
¿La lógica se puede testear afuera?
¿Hay estado duplicado?
¿La clase tiene una responsabilidad clara?
¿Quién la instancia?
¿Quién la actualiza?
¿Quién le pasa dependencias?
```

---

## Regla final

Una clase no debería heredar de MonoBehaviour por costumbre.

```txt
Si solo contiene reglas, cálculos o decisiones,
probablemente puede ser una clase pura.
```
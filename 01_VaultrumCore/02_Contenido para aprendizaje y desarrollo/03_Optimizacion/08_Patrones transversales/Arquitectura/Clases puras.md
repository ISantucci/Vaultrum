## Definicion

Una clase pura es una clase comun de C# que no hereda de `MonoBehaviour`.

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
→ logica sin dependencia directa de MonoBehaviour
```

Una clase pura puede contener reglas, calculos, decisiones, validaciones, algoritmos o estructuras.

---

## Que problema ayuda a prevenir

Ayuda a prevenir:

```txt
Exceso de MonoBehaviours.
Scripts gigantes.
Acoplamiento fuerte con Unity.
Dificultad para testear.
Dificultad para reutilizar logica.
Logica dispersa en escena.
Muchos Update activos.
Dependencia innecesaria del Inspector.
```

Tambien ayuda en proyectos donde se quiere diseñar con:

```txt
SOLID.
Managers.
Update Manager.
Arquitectura escalable.
Sistemas testeables.
```

---

## Como funciona

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

## Como aplicarlo en videojuegos

Buenas candidatas para clases puras:

```txt
Calculadoras de daño.
Validadores de compra.
Sistemas de economia.
Historial de comandos.
Algoritmos de pathfinding.
Estructuras de datos.
Selectores de objetivo.
Sistemas de decision.
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

## Relacion con arquitectura

Se relaciona con:

```txt
MonoBehaviour como puente
Separar logica de unity
Update Manager como optimizacion
Game Loop
Estructuras de datos
Algoritmos
```

Tambien se relaciona con patrones:

```txt
Command
Strategy
Factory
Observer
State
```

Muchos patrones se implementan mejor si la logica no depende directamente de `MonoBehaviour`.

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

## Relacion con hardware/runtime

Las clases puras no optimizan magicamente.

Pero ayudan a:

```txt
Reducir MonoBehaviours.
Evitar callbacks innecesarios.
Centralizar ejecucion.
Testear logica sin escena.
Controlar frecuencia desde managers.
Separar logica pesada de Unity.
```

Esto puede mejorar la capacidad de optimizar.

---

## Cuando conviene usarlas

Conviene usar clases puras cuando:

```txt
La logica no necesita GameObject.
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

## Cuando NO conviene usarlas

No conviene forzarlas cuando:

```txt
La logica depende totalmente de Unity.
El script es visual y simple.
La separacion agrega mas complejidad que valor.
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
Mas claridad.
Mas testabilidad.
Menos acoplamiento.
Mas reutilizacion.
Menos dependencia de escena.
Mejor integracion con arquitectura.
```

Costos:

```txt
Mas diseño.
Mas inicializacion.
Mas dependencias explicitas.
Mas archivos.
Posible sobrearquitectura.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Crear clases puras sin proposito claro.
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

## Checklist de implementacion

```txt
¿La clase necesita heredar MonoBehaviour?
¿Necesita Inspector?
¿Necesita Transform?
¿Necesita callbacks de Unity?
¿La logica se puede testear afuera?
¿Hay estado duplicado?
¿La clase tiene una responsabilidad clara?
¿Quien la instancia?
¿Quien la actualiza?
¿Quien le pasa dependencias?
```

---

## Regla final

Una clase no deberia heredar de MonoBehaviour por costumbre.

```txt
Si solo contiene reglas, calculos o decisiones,
probablemente puede ser una clase pura.
```
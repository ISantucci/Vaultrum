## Definición

Separar lógica de Unity significa diseñar sistemas donde las reglas principales del juego no dependan directamente de `MonoBehaviour`, `GameObject`, escena o callbacks del motor.

No significa ignorar Unity.

Significa usar Unity como capa de ejecución, visualización e integración.

La idea principal es:

```txt
Unity
→ escena, input, render, física, inspector

Lógica
→ reglas, decisiones, cálculos, datos, algoritmos
```

---

## Qué problema ayuda a prevenir

Ayuda a prevenir:

```txt
Scripts gigantes.
Acoplamiento fuerte.
Dificultad para testear.
Dificultad para optimizar.
Dificultad para reutilizar.
Exceso de MonoBehaviours.
Lógica dispersa en escenas.
Dependencia innecesaria del Game Loop.
```

También ayuda para automatización con IA/agentes, porque la lógica queda más clara y menos mezclada con detalles visuales.

---

## Cómo funciona

Se separan responsabilidades.

Ejemplo:

```txt
Pathfinder
→ calcula ruta.

EnemyMovement
→ mueve el Transform.

EnemyBrain
→ decide qué quiere hacer.

EnemyView
→ muestra animación/feedback.

MonoBehaviour
→ conecta todo con Unity.
```

Ejemplo conceptual:

```csharp
public class UpgradeCostCalculator
{
    public int GetCost(int baseCost, int level)
    {
        return baseCost * (level + 1);
    }
}
```

Esto no necesita ser `MonoBehaviour`.

Luego Unity lo usa desde un componente:

```csharp
public class UpgradeComponent : MonoBehaviour
{
    private UpgradeCostCalculator calculator = new();

    public int GetNextCost(int baseCost, int level)
    {
        return calculator.GetCost(baseCost, level);
    }
}
```

---

## Cómo aplicarlo en videojuegos

Aplicaciones:

```txt
IA.
Pathfinding.
Economía.
Upgrades.
Daño.
Inventario.
Misiones.
Oleadas.
Targeting.
Validaciones.
Estados.
Comandos.
Guardado.
```

Ejemplo Tower Defense:

```txt
Tower
→ representa entidad en escena.

TowerData
→ datos base.

TargetSelector
→ lógica de selección.

ProjectilePool
→ reutilización.

UpgradeSystem
→ reglas de mejora.

HUD
→ visualización.
```

Cada sistema tiene responsabilidad clara.

---

## Relación con arquitectura

Se relaciona con:

```txt
Clases puras
MonoBehaviour como puente
UpdateManager
S - Single Responsibility Principle
D - Dependency Inversion Principle
Command
Strategy
Factory
Observer
```

Separar lógica de Unity mejora la posibilidad de aplicar patrones sin forzarlos.

También permite que las dependencias sean más explícitas.

---

## Relación con hardware/runtime

No es una optimización directa como Object Pool.

Pero ayuda a optimizar porque:

```txt
Permite medir sistemas separados.
Reduce dependencia de callbacks.
Facilita Update Manager.
Facilita reducir frecuencia.
Facilita testear lógica.
Evita scripts gigantes.
```

La optimización es más fácil cuando el sistema está separado.

```txt
Sistema mezclado
→ difícil saber qué cuesta.

Sistema separado
→ más fácil medir y corregir.
```

---

## Cuándo conviene usarlo

Conviene cuando:

```txt
La lógica es compleja.
El sistema va a crecer.
Se quiere testear.
Se quiere reutilizar.
Se quiere usar managers.
Se quiere optimizar después.
Se quiere automatizar análisis con IA.
Se quiere evitar dependencia excesiva de escena.
```

---

## Cuándo NO conviene forzarlo

No conviene sobrearquitecturar sistemas simples.

Ejemplo:

```txt
Un objeto decorativo que rota lentamente
→ puede ser un MonoBehaviour simple.
```

La separación debe aportar claridad.

No burocracia.

---

## Trade-offs

Ventajas:

```txt
Más mantenibilidad.
Más testabilidad.
Más claridad.
Mejor escalabilidad.
Mejor integración con optimización.
Más facilidad para IA/agentes.
```

Costos:

```txt
Más diseño.
Más archivos.
Más inicialización.
Más dependencias explícitas.
Mayor curva inicial.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Separar demasiado.
Duplicar estado.
Crear capas innecesarias.
Hacer abstracciones sin uso.
No saber quién es dueño del dato.
Crear sistemas difíciles de inicializar.
```

Ejemplo malo:

```txt
Se separa tanto que nadie sabe dónde se modifica la vida del enemigo.
```

Separar no significa ocultar responsabilidades.

Significa hacerlas más claras.

---

## Checklist de implementación

```txt
¿La lógica necesita Unity directamente?
¿Puede vivir en clase pura?
¿Quién es dueño del estado?
¿Quién actualiza la lógica?
¿Quién conecta con Transform?
¿Quién muestra feedback?
¿Quién valida reglas?
¿La separación mejora claridad?
¿La separación facilita optimización?
¿Hay duplicación de datos?
```

---

## Regla final

Unity debe ejecutar y mostrar el juego.

Pero la lógica importante no tiene por qué estar atrapada en Unity.

```txt
Separar lógica de Unity
→ permite sistemas más claros, testeables y optimizables.
```
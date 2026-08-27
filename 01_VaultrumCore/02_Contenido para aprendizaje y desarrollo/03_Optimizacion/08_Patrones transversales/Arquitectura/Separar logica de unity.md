## Definicion

Separar logica de Unity significa diseñar sistemas donde las reglas principales del juego no dependan directamente de `MonoBehaviour`, `GameObject`, escena o callbacks del motor.

No significa ignorar Unity.

Significa usar Unity como capa de ejecucion, visualizacion e integracion.

La idea principal es:

```txt
Unity
→ escena, input, render, fisica, inspector

Logica
→ reglas, decisiones, calculos, datos, algoritmos
```

---

## Que problema ayuda a prevenir

Ayuda a prevenir:

```txt
Scripts gigantes.
Acoplamiento fuerte.
Dificultad para testear.
Dificultad para optimizar.
Dificultad para reutilizar.
Exceso de MonoBehaviours.
Logica dispersa en escenas.
Dependencia innecesaria del Game Loop.
```

Tambien ayuda para automatizacion con IA/agentes, porque la logica queda mas clara y menos mezclada con detalles visuales.

---

## Como funciona

Se separan responsabilidades.

Ejemplo:

```txt
Pathfinder
→ calcula ruta.

EnemyMovement
→ mueve el Transform.

EnemyBrain
→ decide que quiere hacer.

EnemyView
→ muestra animacion/feedback.

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

## Como aplicarlo en videojuegos

Aplicaciones:

```txt
IA.
Pathfinding.
Economia.
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
→ logica de seleccion.

ProjectilePool
→ reutilizacion.

UpgradeSystem
→ reglas de mejora.

HUD
→ visualizacion.
```

Cada sistema tiene responsabilidad clara.

Ese `TowerData` suele resolverse con un ScriptableObject, y conviene entender bien para que sirve. Un ScriptableObject es un contenedor de datos que vive como asset, fuera de la escena, y su utilidad principal es separar dos cosas que se mezclan solas:

```txt
Configuracion
→ daño base, rango, cadencia, costo, curva de mejora.

Estado runtime
→ cooldown actual, objetivo actual, nivel comprado en esta partida.
```

Todas las torres del mismo tipo pueden compartir una unica configuracion en vez de arrastrar una copia de esos valores cada una, y el diseño se ajusta desde el asset sin abrir codigo ni tocar prefabs uno por uno.

Pero ahi termina la promesa. El valor del ScriptableObject es arquitectonico y de authoring: ordena de donde salen los datos y quien los edita. No es una optimizacion automatica, y no debe presentarse como tal. Cambiar valores sueltos por un asset compartido no baja por si solo el costo de un sistema que igual corre cada frame para cada entidad.

```txt
ScriptableObject
→ mejora de donde vienen los datos.

No cambia
→ cuanto trabajo se hace con ellos.
```

Y tiene su propio riesgo si se usa mal: como el asset es compartido y persiste, escribir estado de partida adentro contamina a todas las entidades que lo usan y puede sobrevivir entre escenas o entre sesiones en el editor. La configuracion se lee. El estado vive en la entidad o en el sistema.

---

## Relacion con arquitectura

Se relaciona con:

```txt
Clases puras
MonoBehaviour como puente
Update Manager como optimizacion
S - Single Responsibility Principle
D - Dependency Inversion Principle
Command
Strategy
Factory
Observer
```

Separar logica de Unity mejora la posibilidad de aplicar patrones sin forzarlos.

Tambien permite que las dependencias sean mas explicitas.

---

## Relacion con hardware/runtime

No es una optimizacion directa como Object Pool.

Pero ayuda a optimizar porque:

```txt
Permite medir sistemas separados.
Reduce dependencia de callbacks.
Facilita Update Manager.
Facilita reducir frecuencia.
Facilita testear logica.
Evita scripts gigantes.
```

La optimizacion es mas facil cuando el sistema esta separado.

```txt
Sistema mezclado
→ dificil saber que cuesta.

Sistema separado
→ mas facil medir y corregir.
```

---

## Cuando conviene usarlo

Conviene cuando:

```txt
La logica es compleja.
El sistema va a crecer.
Se quiere testear.
Se quiere reutilizar.
Se quiere usar managers.
Se quiere optimizar despues.
Se quiere automatizar analisis con IA.
Se quiere evitar dependencia excesiva de escena.
```

---

## Cuando NO conviene forzarlo

No conviene sobrearquitecturar sistemas simples.

Ejemplo:

```txt
Un objeto decorativo que rota lentamente
→ puede ser un MonoBehaviour simple.
```

La separacion debe aportar claridad.

No burocracia.

---

## Trade-offs

Ventajas:

```txt
Mas mantenibilidad.
Mas testabilidad.
Mas claridad.
Mejor escalabilidad.
Mejor integracion con optimizacion.
Mas facilidad para IA/agentes.
```

Costos:

```txt
Mas diseño.
Mas archivos.
Mas inicializacion.
Mas dependencias explicitas.
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
No saber quien es dueño del dato.
Crear sistemas dificiles de inicializar.
```

Ejemplo malo:

```txt
Se separa tanto que nadie sabe donde se modifica la vida del enemigo.
```

Separar no significa ocultar responsabilidades.

Significa hacerlas mas claras.

---

## Checklist de implementacion

```txt
¿La logica necesita Unity directamente?
¿Puede vivir en clase pura?
¿Quien es dueño del estado?
¿Quien actualiza la logica?
¿Quien conecta con Transform?
¿Quien muestra feedback?
¿Quien valida reglas?
¿La separacion mejora claridad?
¿La separacion facilita optimizacion?
¿Hay duplicacion de datos?
```

---

## Regla final

Unity debe ejecutar y mostrar el juego.

Pero la logica importante no tiene por que estar atrapada en Unity.

```txt
Separar logica de Unity
→ permite sistemas mas claros, testeables y optimizables.
```
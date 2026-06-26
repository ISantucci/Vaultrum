## Definición

UI orientada a eventos es una metodología donde la interfaz se actualiza cuando cambia el estado que muestra, no en cada frame.

La idea principal es:

```txt
Dato cambia
→ evento
→ UI actualiza
```

No:

```txt
UI pregunta cada frame
→ aunque nada haya cambiado
```

---

## Qué problema ayuda a prevenir

Ayuda con:

```txt
UI actualizada innecesariamente
Strings por frame
GC Alloc por frame
CPU Bound
Acoplamiento UI/gameplay
Búsquedas globales por frame
```

También ayuda a separar responsabilidades.

```txt
Gameplay
→ cambia estado

Evento
→ notifica

UI
→ muestra estado
```

---

## Cómo funciona

El sistema dueño del dato emite un evento cuando el dato cambia.

Ejemplo:

```csharp
public class EconomySystem
{
    public event Action<int> MoneyChanged;

    private int money;

    public void AddMoney(int amount)
    {
        money += amount;
        MoneyChanged?.Invoke(money);
    }
}
```

La UI escucha:

```csharp
public class MoneyHUD : MonoBehaviour
{
    [SerializeField] private TMP_Text moneyText;
    private EconomySystem economy;

    private void OnEnable()
    {
        economy.MoneyChanged += UpdateMoney;
    }

    private void OnDisable()
    {
        economy.MoneyChanged -= UpdateMoney;
    }

    private void UpdateMoney(int value)
    {
        moneyText.text = value.ToString();
    }
}
```

La UI no actualiza el texto en `Update`.

---

## Cómo aplicarlo en videojuegos

Aplicaciones:

```txt
Vida.
Dinero.
Puntaje.
Oleada.
Munición.
Objetivos.
Inventario.
Cooldowns.
Mensajes.
Paneles de upgrade.
Estados de misión.
```

Ejemplo Tower Defense:

```txt
Jugador construye torre
→ economía cambia
→ MoneyChanged
→ HUD actualiza dinero

Enemigo llega a base
→ vida cambia
→ HealthChanged
→ HUD actualiza barra

Wave empieza
→ WaveChanged
→ HUD actualiza indicador
```

---

## Relación con arquitectura

Se relaciona con:

```txt
Observer
Event Queue
UI actualizada innecesariamente
Strings por frame
Separar logica de unity
```

Una UI sana:

```txt
Muestra estado.
Recibe eventos.
Envía intención.
No es dueña de reglas de gameplay.
```

Ejemplo:

```txt
Botón Upgrade
→ UI envía intención

UpgradeSystem
→ valida costo y aplica

UI
→ muestra resultado
```

La UI no debería decidir sola si el upgrade es válido.

---

## Relación con hardware/runtime

Afecta principalmente:

```txt
CPU
GC
Frame Budget
UI system
```

Reduce:

```txt
Actualizaciones innecesarias.
Strings por frame.
Rebuilds de UI.
Búsquedas repetidas.
```

---

## Cuándo conviene usarla

Conviene cuando:

```txt
La UI muestra datos que cambian ocasionalmente.
Hay textos que se actualizan cada frame.
Hay HUD persistente.
Hay paneles complejos.
Hay GC Alloc por UI.
Hay acoplamiento entre UI y gameplay.
```

Ejemplos claros:

```txt
Dinero.
Vida.
Wave.
Score.
Inventario.
Recursos.
Misiones.
```

---

## Cuándo NO conviene usarla

No todo puede ser evento puro.

Algunas UI necesitan actualización continua:

```txt
Barras suaves animadas.
Cooldown visual continuo.
Timer visible en tiempo real.
Indicadores interpolados.
Minimapas dinámicos.
```

Incluso ahí, se puede optimizar.

Ejemplo:

```txt
Timer
→ puede actualizar 10 veces por segundo en vez de 60.
```

---

## Trade-offs

Ventajas:

```txt
Menos trabajo por frame.
Menos GC.
Mejor separación.
UI más reactiva a cambios reales.
Menos acoplamiento.
```

Costos:

```txt
Necesidad de eventos.
Necesidad de suscripción/desuscripción.
Riesgo de eventos duplicados.
Riesgo de UI desactualizada si falta evento.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
No desuscribirse.
Emitir eventos aunque el dato no cambie.
Hacer que la UI modifique gameplay directamente.
Duplicar estado entre UI y sistema.
No inicializar UI con estado actual.
```

Ejemplo:

```txt
La UI se suscribe al evento,
pero nunca recibe valor inicial.

Resultado:
muestra dato viejo hasta que haya un cambio.
```

Solución:

```txt
Al abrir UI:
leer estado actual una vez
y luego escuchar eventos.
```

---

## Checklist de implementación

```txt
¿La UI actualiza datos en Update?
¿El dato cambia realmente cada frame?
¿Existe un evento de cambio?
¿La UI se suscribe correctamente?
¿La UI se desuscribe correctamente?
¿La UI recibe estado inicial?
¿La UI solo muestra estado?
¿La UI evita strings por frame?
¿Se validó con Profiler o logs?
```

---

## Regla final

La UI debería reaccionar a cambios de estado.

```txt
Si el dato no cambió,
la UI no necesita recalcularlo.
```
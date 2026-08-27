## Definicion

UI orientada a eventos es una metodologia donde la interfaz se actualiza cuando cambia el estado que muestra, no en cada frame.

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

## Que problema ayuda a prevenir

Ayuda con:

```txt
UI actualizada innecesariamente
Strings por frame
GC Alloc por frame
CPU Bound
Acoplamiento UI/gameplay
Busquedas globales por frame
```

Tambien ayuda a separar responsabilidades.

```txt
Gameplay
→ cambia estado

Evento
→ notifica

UI
→ muestra estado
```

---

## Como funciona

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

## Como aplicarlo en videojuegos

Aplicaciones:

```txt
Vida.
Dinero.
Puntaje.
Oleada.
Municion.
Objetivos.
Inventario.
Cooldowns.
Mensajes.
Paneles de upgrade.
Estados de mision.
```

Ejemplo Tower Defense:

```txt
Jugador construye torre
→ economia cambia
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

## Relacion con arquitectura

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
Envia intencion.
No es dueña de reglas de gameplay.
```

Ejemplo:

```txt
Boton Upgrade
→ UI envia intencion

UpgradeSystem
→ valida costo y aplica

UI
→ muestra resultado
```

La UI no deberia decidir sola si el upgrade es valido.

---

## Relacion con hardware/runtime

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
Busquedas repetidas.
```

---

## Cuando conviene usarla

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

## Cuando NO conviene usarla

No todo puede ser evento puro.

Algunas UI necesitan actualizacion continua:

```txt
Barras suaves animadas.
Cooldown visual continuo.
Timer visible en tiempo real.
Indicadores interpolados.
Minimapas dinamicos.
```

Incluso ahi, se puede optimizar.

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
Mejor separacion.
UI mas reactiva a cambios reales.
Menos acoplamiento.
```

Costos:

```txt
Necesidad de eventos.
Necesidad de suscripcion/desuscripcion.
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

Solucion:

```txt
Al abrir UI:
leer estado actual una vez
y luego escuchar eventos.
```

---

## Checklist de implementacion

```txt
¿La UI actualiza datos en Update?
¿El dato cambia realmente cada frame?
¿Existe un evento de cambio?
¿La UI se suscribe correctamente?
¿La UI se desuscribe correctamente?
¿La UI recibe estado inicial?
¿La UI solo muestra estado?
¿La UI evita strings por frame?
¿Se valido con Profiler o logs?
```

---

## Regla final

La UI deberia reaccionar a cambios de estado.

```txt
Si el dato no cambio,
la UI no necesita recalcularlo.
```
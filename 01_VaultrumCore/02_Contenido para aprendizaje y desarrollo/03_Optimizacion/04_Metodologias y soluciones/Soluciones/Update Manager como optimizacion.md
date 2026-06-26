## Definición

Update Manager como optimización es una solución para centralizar y controlar actualizaciones que ocurren durante el Game loop.

En vez de que muchos objetos ejecuten su propio `Update()` de forma independiente, ciertos sistemas u objetos pueden registrarse en un manager que decide cuándo actualizarlos.

La idea principal es:

```txt
Muchos MonoBehaviour.Update()
→ callbacks dispersos

Update Manager
→ actualizaciones registradas, centralizadas y controladas
```

En esta sección, el Update Manager se analiza como una solución de optimización.

No se analiza todavía como manager completo.

Ese análisis corresponde a la sección de Managers.

Acá importa principalmente su utilidad para:

```txt
Reducir trabajo por frame.
Controlar frecuencia.
Evitar callbacks innecesarios.
Ordenar actualizaciones.
Pausar o desactivar sistemas.
Centralizar el Tick de clases puras.
```

---

## Qué problema ayuda a prevenir

Ayuda principalmente con:

```txt
Muchos update activos
CPU Bound
Lógica ejecutándose cada frame sin necesidad
Falta de control sobre frecuencia
Falta de control sobre orden de actualización
Dificultad para pausar o desactivar sistemas
Exceso de MonoBehaviours activos
```

También ayuda a atacar esta fórmula:

```txt
Costo total
=
costo de operación
× cantidad de objetos
× frecuencia de ejecución
```

El Update Manager no reduce automáticamente el costo de una operación.

Pero permite controlar mejor cuántas veces se ejecuta y cuándo se ejecuta.

---

## Cómo funciona

Un Update Manager mantiene una lista de objetos, sistemas o servicios actualizables.

Esos objetos suelen implementar una interfaz común.

Ejemplo conceptual:

```csharp
public interface IUpdatable
{
    void Tick(float deltaTime);
}
```

Luego el manager ejecuta esas actualizaciones desde un punto central:

```csharp
public class UpdateManager : MonoBehaviour
{
    private readonly List<IUpdatable> updatables = new();

    private void Update()
    {
        float deltaTime = Time.deltaTime;

        for (int i = 0; i < updatables.Count; i++)
        {
            updatables[i].Tick(deltaTime);
        }
    }

    public void Register(IUpdatable updatable)
    {
        if (!updatables.Contains(updatable))
        {
            updatables.Add(updatable);
        }
    }

    public void Unregister(IUpdatable updatable)
    {
        updatables.Remove(updatable);
    }
}
```

Este ejemplo muestra la idea base.

En una implementación real, también puede haber:

```txt
Prioridades.
Frecuencias distintas.
Pausas.
Grupos.
Ticks por intervalo.
Desregistro automático.
Validación de referencias nulas.
```

---

## Cómo aplicarlo en videojuegos

Se puede usar para sistemas que necesitan actualización, pero no necesariamente un `Update()` propio por objeto.

Ejemplos:

```txt
IA de enemigos.
Percepción.
Targeting.
Cooldowns.
Timers.
Sistemas de oleadas.
Chequeos periódicos.
Objetos temporales.
Lógica de gameplay no visual.
```

Ejemplo:

```txt
EnemyAI
→ se registra en Update Manager

Update Manager
→ lo actualiza cada cierto intervalo

EnemyAI
→ ejecuta decisión sin tener su propio Update
```

En un Tower Defense:

```txt
Torres
→ pueden reevaluar objetivo cada 0.2 segundos.

Enemigos
→ pueden actualizar decisión por intervalo.

Spawner
→ puede actualizar timers desde un sistema central.

Proyectiles
→ podrían moverse desde un sistema específico si el volumen lo justifica.

UI
→ no debería depender de Update Manager si puede actualizarse por eventos.
```

La idea no es meter todo en el Update Manager.

La idea es usarlo para actualizaciones repetitivas que necesitan control.

---

## Relación con arquitectura

Se relaciona con:

```txt
Game Loop
Frame Budget
CPU Bound
Muchos update activos
Reducir frecuencia de actualizacion
Clases puras
MonoBehaviour como puente
```

En una arquitectura sana:

```txt
Update Manager
→ coordina actualizaciones

Sistema registrado
→ contiene su propia lógica

MonoBehaviour
→ conecta con Unity si hace falta
```

Ejemplo incorrecto:

```txt
Update Manager
→ contiene IA
→ contiene movimiento
→ contiene disparo
→ contiene UI
→ contiene economía
```

Eso crea una clase dios.

Ejemplo correcto:

```txt
Update Manager
→ llama Tick()

EnemyBrain
→ decide

TargetingSystem
→ busca objetivo

WaveTimer
→ controla oleada

CooldownSystem
→ procesa cooldowns
```

El manager coordina ejecución.

No debería absorber reglas de gameplay.

---

## Relación con hardware/runtime

Afecta principalmente:

```txt
CPU
Game Loop
Frame Budget
```

Puede ayudar a reducir:

```txt
Callbacks dispersos.
Actualizaciones innecesarias.
Frecuencia excesiva.
Lógica ejecutándose sin control.
```

Pero es importante entender algo:

```txt
Mover lógica de muchos Update a un manager
no hace que la lógica sea automáticamente barata.
```

Ejemplo:

```txt
Antes:
100 enemigos ejecutan lógica pesada en Update.

Después:
Update Manager ejecuta la misma lógica pesada para 100 enemigos cada frame.

Resultado:
mejor organización, pero costo similar.
```

La optimización aparece cuando el manager permite:

```txt
Actualizar menos veces.
Actualizar por grupos.
Pausar sistemas.
Evitar objetos inactivos.
Ordenar mejor el trabajo.
Evitar callbacks innecesarios.
```

---

## Cuándo conviene usarlo

Conviene usarlo cuando:

```txt
Hay muchos objetos con Update.
Hay lógica que no necesita correr cada frame.
Se necesita controlar frecuencia.
Se necesita pausar sistemas fácilmente.
Se necesita ordenar actualizaciones.
Se trabaja con clases puras.
Hay límite de MonoBehaviours.
El proyecto empieza a escalar.
```

También conviene cuando el diseño busca:

```txt
Menos dependencia directa de MonoBehaviour.
Más control sobre el Game Loop.
Sistemas actualizables por interfaz.
Separación entre ejecución y lógica.
```

---

## Cuándo NO conviene usarlo

No conviene usarlo cuando:

```txt
El proyecto es muy chico.
Hay pocos Update simples.
No hay problema medido.
La complejidad extra no aporta.
Se va a usar como GameManager gigante.
No hay estrategia de registro/desregistro.
No se va a controlar frecuencia.
```

Ejemplo:

```txt
Tres objetos con Update liviano
→ no justifican un Update Manager complejo.
```

Tampoco conviene usarlo solo para “parecer optimizado”.

Si no reduce frecuencia, no mejora orden, no simplifica ciclo de vida ni ayuda a medir, probablemente no hacía falta.

---

## Trade-offs

Ventajas:

```txt
Más control sobre actualizaciones.
Menos callbacks dispersos.
Mejor manejo de frecuencia.
Mejor integración con clases puras.
Mejor posibilidad de pausar sistemas.
Mayor claridad sobre qué se actualiza.
Más facilidad para agrupar lógica por intervalos.
```

Costos:

```txt
Más arquitectura.
Necesidad de registro/desregistro.
Riesgo de referencias viejas.
Riesgo de clase dios.
Posibles errores si se olvida registrar.
Posibles errores si se olvida desregistrar.
Mayor responsabilidad sobre ciclo de vida.
```

---

## Riesgos de aplicarlo mal

Riesgos comunes:

```txt
Convertirlo en un manager gigante.
Meter lógica de gameplay dentro del manager.
No desregistrar objetos destruidos.
Actualizar todo cada frame igual que antes.
No controlar prioridades.
No controlar frecuencia.
No medir antes/después.
Registrar objetos duplicados.
Retener referencias a objetos destruidos.
```

Mala implementación:

```txt
Antes:
100 enemigos con Update.

Después:
Update Manager recorre 100 enemigos y ejecuta la misma lógica cada frame.

Resultado:
menos callbacks dispersos, pero costo parecido.
```

Mejor implementación:

```txt
Update Manager
→ actualiza IA por grupos
→ controla frecuencia
→ evita trabajo innecesario
→ permite pausar sistemas
```

---

## Relación con Managers

Este documento analiza el Update Manager como solución de optimización.

En la sección de Managers debería existir un documento específico sobre:

```txt
Update Manager
```

Ese documento debería profundizar en:

```txt
Responsabilidad del manager.
Ciclo de vida.
Registro y desregistro.
Orden de ejecución.
Persistencia entre escenas.
Riesgo de singleton.
Relación con otros managers.
Errores de arquitectura.
Integración con Unity.
```

La separación recomendada es:

```txt
Optimización / Soluciones / Update Manager como optimización
→ por qué ayuda al rendimiento y cuándo conviene.

Managers / Update Manager
→ cómo diseñarlo como manager sano y mantenible.
```

---

## Checklist de implementación

```txt
¿Hay un problema real de muchos Update?
¿Se midió el costo?
¿Se definió qué objetos se registran?
¿Existe una interfaz clara?
¿El manager solo coordina?
¿La lógica vive fuera del manager?
¿Hay registro seguro?
¿Hay desregistro seguro?
¿Se controla frecuencia?
¿Se puede pausar?
¿Se evita registrar duplicados?
¿Se evita retener objetos destruidos?
¿Se mide antes/después?
¿Se evita crear una clase dios?
```

---

## Regla final

Update Manager como optimización no significa meter todo en un solo `Update()`.

Significa controlar mejor qué se actualiza, cuándo se actualiza y con qué frecuencia.

```txt
Update Manager
→ coordina ejecución

No:
→ absorbe gameplay
```

Si no reduce trabajo innecesario ni mejora el control del Game Loop, no está cumpliendo su función como solución de optimización.
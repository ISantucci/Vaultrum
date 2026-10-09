## Definicion

Update Manager como optimizacion es una solucion para centralizar y controlar actualizaciones que ocurren durante el Game loop.

En vez de que muchos objetos ejecuten su propio `Update()` de forma independiente, ciertos sistemas u objetos pueden registrarse en un manager que decide cuando actualizarlos.

La idea principal es:

```txt
Muchos MonoBehaviour.Update()
→ callbacks dispersos

Update Manager
→ actualizaciones registradas, centralizadas y controladas
```

En esta seccion, el Update Manager se analiza como una solucion de optimizacion.

No se analiza todavia como manager completo.

Ese analisis corresponde a la seccion de Managers.

Aca importa principalmente su utilidad para:

```txt
Reducir trabajo por frame.
Controlar frecuencia.
Evitar callbacks innecesarios.
Ordenar actualizaciones.
Pausar o desactivar sistemas.
Centralizar el Tick de clases puras.
```

---

## Que problema ayuda a prevenir

Ayuda principalmente con:

```txt
Muchos update activos
CPU Bound
Logica ejecutandose cada frame sin necesidad
Falta de control sobre frecuencia
Falta de control sobre orden de actualizacion
Dificultad para pausar o desactivar sistemas
Exceso de MonoBehaviours activos
```

Tambien ayuda a atacar esta formula:

```txt
Costo total
=
costo de operacion
× cantidad de objetos
× frecuencia de ejecucion
```

El Update Manager no reduce automaticamente el costo de una operacion.

Pero permite controlar mejor cuantas veces se ejecuta y cuando se ejecuta.

---

## Como funciona

Un Update Manager mantiene una lista de objetos, sistemas o servicios actualizables.

Esos objetos suelen implementar una interfaz comun. En Capsule Survivor esa interfaz fue `ITickable`, del mismo modo que la de object pooling fue `IPoolable`.

Ejemplo conceptual:

```csharp
public interface ITickable
{
    void Tick(float deltaTime);
}
```

El contrato es minimo a proposito. El objeto no decide cuando se actualiza: solo sabe que hacer cuando le toca.

Quien decide es el manager, y por eso puede registrar, desregistrar, pausar o espaciar sin tocar la logica del objeto.

Luego el manager ejecuta esas actualizaciones desde un punto central:

```csharp
public class CustomUpdateManager : MonoBehaviour
{
    private readonly List<ITickable> tickables = new();

    private void Update()
    {
        float deltaTime = Time.deltaTime;

        for (int i = 0; i < tickables.Count; i++)
        {
            tickables[i].Tick(deltaTime);
        }
    }

    public void Register(ITickable tickable)
    {
        if (!tickables.Contains(tickable))
        {
            tickables.Add(tickable);
        }
    }

    public void Unregister(ITickable tickable)
    {
        tickables.Remove(tickable);
    }
}
```

Este ejemplo muestra la idea base.

En una implementacion real, tambien puede haber:

```txt
Prioridades.
Frecuencias distintas.
Pausas.
Grupos.
Ticks por intervalo.
Desregistro automatico.
Validacion de referencias nulas.
```

---

## Como aplicarlo en videojuegos

Se puede usar para sistemas que necesitan actualizacion, pero no necesariamente un `Update()` propio por objeto.

Ejemplos:

```txt
IA de enemigos.
Percepcion.
Targeting.
Cooldowns.
Timers.
Sistemas de oleadas.
Chequeos periodicos.
Objetos temporales.
Logica de gameplay no visual.
```

Ejemplo:

```txt
EnemyAI
→ se registra en Update Manager

Update Manager
→ lo actualiza cada cierto intervalo

EnemyAI
→ ejecuta decision sin tener su propio Update
```

En un Tower Defense:

```txt
Torres
→ pueden reevaluar objetivo cada 0.2 segundos.

Enemigos
→ pueden actualizar decision por intervalo.

Spawner
→ puede actualizar timers desde un sistema central.

Proyectiles
→ podrian moverse desde un sistema especifico si el volumen lo justifica.

UI
→ no deberia depender de Update Manager si puede actualizarse por eventos.
```

La idea no es meter todo en el Update Manager.

La idea es usarlo para actualizaciones repetitivas que necesitan control.

---

## Relacion con arquitectura

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
→ contiene su propia logica

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
→ contiene economia
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

El manager coordina ejecucion.

No deberia absorber reglas de gameplay.

---

## Relacion con hardware/runtime

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
Logica ejecutandose sin control.
```

Pero es importante entender algo:

```txt
Mover logica de muchos Update a un manager
no hace que la logica sea automaticamente barata.
```

Ejemplo:

```txt
Antes:
300 enemigos ejecutan logica pesada en Update.

Despues:
Update Manager ejecuta la misma logica pesada para 300 enemigos cada frame.

Resultado:
mejor organizacion, pero costo similar.
```

La optimizacion aparece cuando el manager permite:

```txt
Actualizar menos veces.
Actualizar por grupos.
Pausar sistemas.
Evitar objetos inactivos.
Ordenar mejor el trabajo.
Evitar callbacks innecesarios.
```

---

## Cuando conviene usarlo

Conviene usarlo cuando:

```txt
Hay muchos objetos con Update.
Hay logica que no necesita correr cada frame.
Se necesita controlar frecuencia.
Se necesita pausar sistemas facilmente.
Se necesita ordenar actualizaciones.
Se trabaja con clases puras.
Hay limite de MonoBehaviours.
El proyecto empieza a escalar.
```

Tambien conviene cuando el diseño busca:

```txt
Menos dependencia directa de MonoBehaviour.
Mas control sobre el Game Loop.
Sistemas actualizables por interfaz.
Separacion entre ejecucion y logica.
```

---

## Cuando NO conviene usarlo

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

Si no reduce frecuencia, no mejora orden, no simplifica ciclo de vida ni ayuda a medir, probablemente no hacia falta.

---

## Trade-offs

Ventajas:

```txt
Mas control sobre actualizaciones.
Menos callbacks dispersos.
Mejor manejo de frecuencia.
Mejor integracion con clases puras.
Mejor posibilidad de pausar sistemas.
Mayor claridad sobre que se actualiza.
Mas facilidad para agrupar logica por intervalos.
```

Costos:

```txt
Mas arquitectura.
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
Meter logica de gameplay dentro del manager.
No desregistrar objetos destruidos.
Actualizar todo cada frame igual que antes.
No controlar prioridades.
No controlar frecuencia.
No medir antes/despues.
Registrar objetos duplicados.
Retener referencias a objetos destruidos.
```

Mala implementacion:

```txt
Antes:
300 enemigos con Update.

Despues:
Update Manager recorre 300 enemigos y ejecuta la misma logica cada frame.

Resultado:
menos callbacks dispersos, pero costo parecido.
```

Mejor implementacion:

```txt
Update Manager
→ actualiza IA por grupos
→ controla frecuencia
→ evita trabajo innecesario
→ permite pausar sistemas
```

---

## Relacion con Managers

Este documento analiza el Update Manager como solucion de optimizacion.

En la seccion de Managers deberia existir un documento especifico sobre:

```txt
Update Manager
```

Ese documento deberia profundizar en:

```txt
Responsabilidad del manager.
Ciclo de vida.
Registro y desregistro.
Orden de ejecucion.
Persistencia entre escenas.
Riesgo de singleton.
Relacion con otros managers.
Errores de arquitectura.
Integracion con Unity.
```

La separacion recomendada es:

```txt
Optimizacion / CPU / Soluciones / Update Manager como optimizacion
→ por que ayuda al rendimiento y cuando conviene.

Managers / Update Manager
→ como diseñarlo como manager sano y mantenible.
```

---

## Checklist de implementacion

```txt
¿Hay un problema real de muchos Update?
¿Se midio el costo?
¿Se definio que objetos se registran?
¿Existe una interfaz clara?
¿El manager solo coordina?
¿La logica vive fuera del manager?
¿Hay registro seguro?
¿Hay desregistro seguro?
¿Se controla frecuencia?
¿Se puede pausar?
¿Se evita registrar duplicados?
¿Se evita retener objetos destruidos?
¿Se mide antes/despues?
¿Se evita crear una clase dios?
```

---

## Regla final

Update Manager como optimizacion no significa meter todo en un solo `Update()`.

Significa controlar mejor que se actualiza, cuando se actualiza y con que frecuencia.

```txt
Update Manager
→ coordina ejecucion

No:
→ absorbe gameplay
```

Si no reduce trabajo innecesario ni mejora el control del Game Loop, no esta cumpliendo su funcion como solucion de optimizacion.
## Definicion

Reducir frecuencia de actualizacion significa ejecutar una logica menos veces por segundo cuando no necesita correr cada frame.

La idea principal es:

```txt
No todo necesita actualizarse cada frame.
```

En vez de ejecutar una operacion 60 veces por segundo, se puede ejecutar:

```txt
cada 0.1 segundos,
cada 0.2 segundos,
cada cierto numero de frames,
por grupos,
cuando cambia un dato,
cuando ocurre un evento.
```

---

## Que problema ayuda a prevenir

Ayuda con:

```txt
Muchos update activos
CPU Bound
Pathfinding recalculado demasiado seguido
IA pesada
Percepcion costosa
Targeting frecuente
UI actualizada innecesariamente
Chequeos de distancia por frame
```

Ataca directamente esta formula:

```txt
Costo total
=
costo
× cantidad
× frecuencia
```

Reducir frecuencia baja el costo total.

---

## Como funciona

En lugar de ejecutar logica en cada `Update`, se usa un intervalo.

Ejemplo:

```csharp
private float timer;
private const float interval = 0.2f;

private void Update()
{
    timer += Time.deltaTime;

    if (timer < interval)
    {
        return;
    }

    timer = 0f;
    RecalculateTarget();
}
```

Tambien puede hacerse desde un Update Manager como optimizacion.

Ejemplo:

```txt
Grupo A
→ actualiza frame 1

Grupo B
→ actualiza frame 2

Grupo C
→ actualiza frame 3
```

Esto reparte trabajo.

---

## Como aplicarlo en videojuegos

Sistemas candidatos:

```txt
Percepcion de NPC.
Busqueda de objetivos.
Pathfinding.
Chequeos de distancia.
Actualizacion de sensores.
Reevaluacion de decisiones.
Cooldowns no criticos.
UI.
Sistemas de spawn.
```

Ejemplo:

```txt
300 enemigos
→ no todos necesitan reevaluar al jugador cada frame.

Mejor:
actualizan percepcion cada 0.2 segundos
o divididos por grupos.
```

En Tower Defense:

```txt
Torres
→ pueden buscar objetivo cada cierto intervalo.

Enemigos
→ pueden recalcular ruta solo ante cambios.

UI
→ puede actualizarse por evento.

Spawner
→ puede trabajar con timers.
```

---

## Relacion con arquitectura

Se relaciona con:

```txt
Update Manager como optimizacion
Game Loop
Frame Budget
Muchos update activos
CPU Bound
Pathfinding recalculado demasiado seguido
```

Tambien se relaciona con IA:

```txt
Percepcion
→ no siempre cada frame

Decision
→ puede ser por intervalo

Movimiento
→ suele necesitar actualizacion fluida

Pathfinding
→ solo cuando corresponde
```

Diferenciar esto es clave.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
CPU
Frame Budget
Game Loop
```

Puede reducir spikes si se reparte trabajo.

Tambien puede reducir GC si evita operaciones que generan allocations.

---

## Cuando conviene usarlo

Conviene cuando:

```txt
La logica es costosa.
Hay muchos objetos.
La respuesta inmediata no es necesaria.
La logica no cambia cada frame.
El sistema escala mal.
Se detecta CPU alto.
```

Ejemplos:

```txt
Targeting.
Percepcion.
IA.
Pathfinding.
Chequeos de rango.
Actualizaciones de UI.
```

---

## Cuando NO conviene usarlo

No conviene reducir frecuencia en sistemas que necesitan alta reactividad.

Ejemplos:

```txt
Input del jugador.
Movimiento principal.
Camara sensible.
Colisiones criticas.
Feedback instantaneo.
Acciones frame-perfect.
```

Tambien puede ser peligroso si afecta justicia del juego.

```txt
Enemigo tarda demasiado en detectar al jugador
→ se siente torpe.

Torre tarda demasiado en disparar
→ se siente injusta o rota.
```

---

## Trade-offs

Ventajas:

```txt
Menos CPU.
Menos trabajo por frame.
Mejor escalabilidad.
Menos spikes.
```

Costos:

```txt
Menor reactividad.
Posible delay.
Mas logica de timers.
Mas coordinacion.
Posible comportamiento inconsistente si se exagera.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Reducir demasiado la frecuencia.
Crear delays visibles.
Romper feeling del juego.
Actualizar grupos de forma desbalanceada.
No considerar prioridad.
No medir impacto en gameplay.
```

Ejemplo:

```txt
IA actualiza cada 2 segundos.
Rendimiento mejora.
NPC se siente tonto.
```

Optimizacion mala.

---

## Checklist de implementacion

```txt
¿Esta logica necesita correr cada frame?
¿Cada cuanto cambia realmente el dato?
¿Cuanta reactividad necesita?
¿Cuantos objetos ejecutan esto?
¿Se puede actualizar por evento?
¿Se puede dividir por grupos?
¿Se midio costo antes?
¿Se valido gameplay despues?
¿El delay es aceptable?
```

---

## Regla final

Reducir frecuencia es una de las optimizaciones mas sanas cuando se aplica con criterio.

```txt
No hacer trabajo innecesario
suele ser mejor que hacer trabajo rapido.
```
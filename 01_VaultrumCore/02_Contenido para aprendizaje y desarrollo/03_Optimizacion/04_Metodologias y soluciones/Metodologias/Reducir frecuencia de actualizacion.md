## Definición

Reducir frecuencia de actualización significa ejecutar una lógica menos veces por segundo cuando no necesita correr cada frame.

La idea principal es:

```txt
No todo necesita actualizarse cada frame.
```

En vez de ejecutar una operación 60 veces por segundo, se puede ejecutar:

```txt
cada 0.1 segundos,
cada 0.2 segundos,
cada cierto número de frames,
por grupos,
cuando cambia un dato,
cuando ocurre un evento.
```

---

## Qué problema ayuda a prevenir

Ayuda con:

```txt
Muchos update activos
CPU Bound
Pathfinding recalculado demasiado seguido
IA pesada
Percepción costosa
Targeting frecuente
UI actualizada innecesariamente
Chequeos de distancia por frame
```

Ataca directamente esta fórmula:

```txt
Costo total
=
costo
× cantidad
× frecuencia
```

Reducir frecuencia baja el costo total.

---

## Cómo funciona

En lugar de ejecutar lógica en cada `Update`, se usa un intervalo.

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

También puede hacerse desde un UpdateManager.

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

## Cómo aplicarlo en videojuegos

Sistemas candidatos:

```txt
Percepción de NPC.
Búsqueda de objetivos.
Pathfinding.
Chequeos de distancia.
Actualización de sensores.
Reevaluación de decisiones.
Cooldowns no críticos.
UI.
Sistemas de spawn.
```

Ejemplo:

```txt
100 enemigos
→ no todos necesitan reevaluar al jugador cada frame.

Mejor:
actualizan percepción cada 0.2 segundos
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

## Relación con arquitectura

Se relaciona con:

```txt
UpdateManager
Game Loop
Frame Budget
Muchos update activos
CPU Bound
Pathfinding recalculado demasiado seguido
```

También se relaciona con IA:

```txt
Percepción
→ no siempre cada frame

Decisión
→ puede ser por intervalo

Movimiento
→ suele necesitar actualización fluida

Pathfinding
→ solo cuando corresponde
```

Diferenciar esto es clave.

---

## Relación con hardware/runtime

Afecta principalmente:

```txt
CPU
Frame Budget
Game Loop
```

Puede reducir spikes si se reparte trabajo.

También puede reducir GC si evita operaciones que generan allocations.

---

## Cuándo conviene usarlo

Conviene cuando:

```txt
La lógica es costosa.
Hay muchos objetos.
La respuesta inmediata no es necesaria.
La lógica no cambia cada frame.
El sistema escala mal.
Se detecta CPU alto.
```

Ejemplos:

```txt
Targeting.
Percepción.
IA.
Pathfinding.
Chequeos de rango.
Actualizaciones de UI.
```

---

## Cuándo NO conviene usarlo

No conviene reducir frecuencia en sistemas que necesitan alta reactividad.

Ejemplos:

```txt
Input del jugador.
Movimiento principal.
Cámara sensible.
Colisiones críticas.
Feedback instantáneo.
Acciones frame-perfect.
```

También puede ser peligroso si afecta justicia del juego.

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
Más lógica de timers.
Más coordinación.
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

Optimización mala.

---

## Checklist de implementación

```txt
¿Esta lógica necesita correr cada frame?
¿Cada cuánto cambia realmente el dato?
¿Cuánta reactividad necesita?
¿Cuántos objetos ejecutan esto?
¿Se puede actualizar por evento?
¿Se puede dividir por grupos?
¿Se midió costo antes?
¿Se validó gameplay después?
¿El delay es aceptable?
```

---

## Regla final

Reducir frecuencia es una de las optimizaciones más sanas cuando se aplica con criterio.

```txt
No hacer trabajo innecesario
suele ser mejor que hacer trabajo rápido.
```
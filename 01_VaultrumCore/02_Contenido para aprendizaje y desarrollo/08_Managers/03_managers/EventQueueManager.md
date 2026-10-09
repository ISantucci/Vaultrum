## Descripción

Un `EventQueueManager` administra una cola de eventos diferidos.

Su función es recibir eventos, ordenarlos y procesarlos en un momento controlado.

No es lo mismo que Observer.

Observer notifica inmediatamente.

Event Queue permite diferir, ordenar o agrupar procesamiento.

---

## Qué problema resuelve

Resuelve problemas como:

```txt
eventos que no deben procesarse inmediatamente,
necesidad de orden,
acciones encadenadas,
procesamiento por frame,
desacople temporal,
evitar llamadas directas entre sistemas,
evitar modificar estado en medio de una operación.
```

Ejemplo:

```txt
Enemy muere.
Se encola EnemyKilled.
Luego se procesa recompensa.
Luego se notifica cambio de dinero.
```

---

## Cuándo conviene usarlo

Conviene cuando:

```txt
el orden de eventos importa,
se necesita diferir procesamiento,
hay muchos eventos durante un frame,
se quiere evitar cascadas inmediatas,
se necesita centralizar despacho,
se quiere auditar eventos procesados.
```

---

## Cuándo NO conviene usarlo

No conviene si:

```txt
la reacción inmediata alcanza,
un evento simple Observer resuelve el problema,
la cola oculta demasiado el flujo,
hay pocos eventos,
o se usa como canal universal de todo.
```

Regla:

```txt
No usar EventQueueManager para reemplazar todos los eventos simples.
```

---

## Responsabilidades permitidas

Puede encargarse de:

```txt
encolar eventos,
procesar eventos,
mantener orden,
limitar eventos por frame,
limpiar cola,
priorizar si está justificado,
notificar procesamiento,
registrar handlers si corresponde.
```

---

## Responsabilidades prohibidas

No debería:

```txt
hacer gameplay directamente,
calcular daño,
actualizar UI directamente,
guardar partida directamente,
decidir spawn,
interpretar cualquier evento genérico sin estructura,
ocultar flujo crítico sin documentación.
```

---

## Relación con otras piezas arquitectónicas

Relaciones comunes:

```txt
Observer
→ reacción inmediata.

Event Queue
→ reacción diferida.

GameEvents
→ sistema de eventos globales.

Command
→ puede generar eventos.

UIManager
→ puede escuchar resultados.

GameManager
→ puede reaccionar a eventos globales procesados.
```

Diferencia clave:

```txt
Observer
→ avisar ahora.

EventQueueManager
→ procesar después o en orden.
```

---

## Ciclo de vida

Flujo típico:

```txt
Enqueue
→ agregar evento.

Process
→ procesar uno o varios eventos.

Clear
→ limpiar cola.

Shutdown
→ liberar handlers o referencias.
```

Puede procesar:

```txt
inmediatamente,
al final del frame,
en Update,
por lotes,
con prioridad.
```

Solo agregar prioridad si el proyecto lo necesita.

---

## API mínima recomendada

```csharp
public interface IEventQueueManager
{
    void Enqueue(IGameEvent gameEvent);
    void ProcessNext();
    void ProcessAll();
    void Clear();
}
```

Evento base:

```csharp
public interface IGameEvent
{
}
```

Handler:

```csharp
public interface IGameEventHandler<T> where T : IGameEvent
{
    void Handle(T gameEvent);
}
```

---

## Ejemplo aplicado a videojuegos

Tower Defense:

```txt
EnemyKilledEvent se encola.
EventQueueManager procesa evento.
RewardSystem suma dinero.
EconomySystem emite MoneyChanged.
HUD actualiza valor.
```

Esto evita que el enemigo muerto llame directamente a UI, economía y audio.

---

## Errores comunes

```txt
eventos demasiado genéricos,
cola que nunca se limpia,
procesamiento sin orden claro,
handlers duplicados,
eventos que modifican demasiado estado,
usar cola para todo,
ocultar flujo de juego,
no documentar quién produce y quién consume eventos.
```

---

## Checklist para IA/agente

Antes de crear o modificar `EventQueueManager`:

```txt
¿Por qué el evento debe diferirse?
¿El orden importa?
¿Observer alcanza?
¿Qué tipos de evento existen?
¿Quién encola?
¿Quién procesa?
¿Cuándo se procesa?
¿Se limpia al cambiar nivel?
¿Hay riesgo de eventos viejos?
¿Hay handlers duplicados?
¿Se evita lógica de gameplay dentro de la cola?
```

---

## Regla final

`EventQueueManager` administra procesamiento diferido.

```txt
Sano:
ordena y desacopla eventos.

Peligroso:
se vuelve una caja negra donde todo pasa y nadie entiende el flujo.
```
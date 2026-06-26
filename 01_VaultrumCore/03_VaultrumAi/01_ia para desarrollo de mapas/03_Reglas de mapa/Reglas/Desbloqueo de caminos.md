## Definicion

El desbloqueo de caminos es el proceso por el cual una parte del mapa pasa de no estar disponible a estar disponible durante la partida.

Puede aplicarse a:

```txt
nodos
conexiones
zonas
rutas
puertas
atajos
sectores
```

No es pathfinding completo.

No es comportamiento de NPC.

No es movimiento fisico.

Es una regla de cambio de estado dentro del mapa.

```txt
Camino bloqueado
→ condicion cumplida
→ camino disponible
```

---

## Responsabilidad de esta nota

Esta nota define como representar y manejar caminos que cambian de disponibilidad.

Su responsabilidad es explicar:

```txt
que significa desbloquear un camino
que datos necesita
que estructuras puede afectar
cuando conviene implementarlo
cuando no conviene implementarlo
que costo tiene
como validarlo
```

Esta nota no debe explicar completo algoritmos, NPCs o movimiento.

Los sistemas consumidores deben interpretar el cambio desde su propio contexto.

---

## Problema que resuelve

El desbloqueo de caminos resuelve el problema de representar mapas que cambian durante la partida.

Pregunta principal:

```txt
¿Cuando y por que una parte del mapa pasa a estar disponible?
```

Ejemplos:

```txt
se abre una puerta
se destruye una barrera
se habilita un puente
se desbloquea una ruta alternativa
se activa un atajo
se completa un objetivo
```

---

## Datos que necesita

Un desbloqueo puede necesitar:

```txt
elemento bloqueado
estado actual
condicion de desbloqueo
evento que dispara el cambio
sistemas consumidores afectados
debug visual
persistencia si corresponde
```

Ejemplo:

```txt
Camino B
→ bloqueado al inicio
→ se desbloquea en ronda 5
→ habilita conexion entre Nodo C y Nodo D
```

---

## Que puede desbloquearse

Puede desbloquearse:

```txt
un nodo
una conexion
una ruta
una zona
una puerta
un sector
un waypoint
un conjunto de caminos
```

La eleccion depende de la estructura del mapa.

Ejemplo:

```txt
Si el mapa esta basado en conexiones,
desbloquear una conexion puede alcanzar.

Si el mapa esta basado en zonas,
desbloquear una zona puede ser mas claro.
```

---

## Estado bloqueado y disponible

Un camino desbloqueable necesita estado.

Estados posibles:

```txt
bloqueado
disponible
desbloqueado
cerrado
abierto
inactivo
activo
```

Los nombres deben ser consistentes.

No conviene mezclar varios conceptos para lo mismo.

Ejemplo:

```txt
IsBlocked = true
→ no disponible.

IsBlocked = false
→ disponible.
```

---

## Condicion de desbloqueo

La condicion define por que el camino cambia.

Puede ser:

```txt
ronda alcanzada
objetivo completado
llave obtenida
enemigo derrotado
evento narrativo
accion del jugador
timer
interaccion con objeto
```

La condicion no necesariamente debe vivir dentro del camino.

Puede venir de otro sistema.

El camino solo necesita recibir el cambio de estado.

---

## Desbloqueo no es costo alto

Un camino bloqueado no es lo mismo que un camino caro.

```txt
Bloqueado
→ no se puede usar.

Costo alto
→ se puede usar, pero no conviene.
```

Ejemplo:

```txt
Puerta cerrada
→ bloqueada.

Pantano
→ costo alto.
```

Usar costo alto como bloqueo puede generar rutas incorrectas.

---

## Que NO debe hacer un camino desbloqueable

Un camino desbloqueable no debe asumir responsabilidades que no le corresponden.

No debe:

```txt
decidir comportamiento de NPC
mover entidades
calcular pathfinding completo
controlar toda la progresion
resolver combate
actualizar UI global
funcionar como GameManager
```

Debe representar disponibilidad.

Otros sistemas deciden que hacer con ese cambio.

---

## Desbloqueo como contrato de informacion

Un camino desbloqueable puede pensarse como contrato.

```txt
Yo represento una parte del mapa.
Puedo estar bloqueado o disponible.
Puedo cambiar de estado.
Puedo avisar o exponer ese cambio.
Puedo ser consultado por otros sistemas.
```

Ese contrato mantiene separada la regla de mapa de los sistemas consumidores.

---

## Ejemplo conceptual en codigo

```csharp
using System;

public class UnlockablePath
{
    public string Id { get; }
    public bool IsUnlocked { get; private set; }

    public event Action<UnlockablePath> OnUnlocked;

    public UnlockablePath(string id, bool startsUnlocked = false)
    {
        Id = id;
        IsUnlocked = startsUnlocked;
    }

    public void Unlock()
    {
        if (IsUnlocked) return;

        IsUnlocked = true;
        OnUnlocked?.Invoke(this);
    }

    public void Lock()
    {
        IsUnlocked = false;
    }

    public bool IsAvailable()
    {
        return IsUnlocked;
    }
}
```

Este ejemplo muestra cambio de disponibilidad.

No calcula rutas.

No mueve entidades.

No decide comportamientos.

---

## Cuando implementar desbloqueo de caminos

Conviene implementarlo cuando:

```txt
el mapa cambia durante la partida
hay progresion espacial
hay puertas o atajos
hay rutas que aparecen despues
hay caminos bloqueados por eventos
hay rutas alternativas que se habilitan
el diseño necesita controlar acceso
```

Ejemplo correcto:

```txt
En una ronda avanzada se abre una nueva ruta para enemigos.

→ Desbloqueo de caminos tiene sentido.
```

---

## Cuando NO implementarlo

No conviene implementarlo cuando:

```txt
el mapa es estatico
todas las rutas estan disponibles desde el inicio
el recorrido es fijo
el bloqueo es solo visual
no hay sistema consumidor
el cambio no afecta navegacion ni gameplay
```

Ejemplo:

```txt
Una puerta decorativa que nunca se abre ni afecta rutas.

→ No necesita sistema de desbloqueo.
```

---

## Por que no implementarlo de mas

El desbloqueo de caminos agrega estado y sincronizacion.

Puede generar:

```txt
bugs de rutas disponibles antes de tiempo
rutas que no se actualizan
pathfinding usando caminos bloqueados
eventos duplicados
debug mas dificil
dependencias con progresion
```

Regla:

```txt
Si el camino nunca cambia de disponibilidad,
no necesita sistema de desbloqueo.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
hacer que el camino controle toda la progresion
mezclar desbloqueo con comportamiento de NPC
usar costos altos como bloqueo
no avisar a sistemas consumidores
no validar visualmente el cambio
actualizar estados cada frame sin necesidad
duplicar estado de bloqueo en varias clases
no manejar bloqueo inicial
```

Ejemplo de mala practica:

```txt
La puerta dice estar desbloqueada,
pero la conexion del mapa sigue bloqueada.

Resultado:
el jugador ve la puerta abierta,
pero el sistema no puede usar la ruta.
```

---

## Costos de implementacion

Implementar desbloqueo de caminos requiere:

```txt
definir estado inicial
definir condicion de desbloqueo
definir que estructura cambia
definir quien dispara el evento
definir quien consume el cambio
actualizar rutas o conexiones afectadas
debuggear estado antes y despues
probar casos borde
```

No es solo activar un GameObject.

Debe actualizar la representacion logica.

---

## Costos de optimizacion

El desbloqueo de caminos suele ser barato si ocurre por eventos.

Puede volverse costoso si se implementa mal.

Costos posibles:

```txt
CPU por revisar condiciones constantemente
CPU por recalcular rutas afectadas
CPU por actualizar muchas conexiones
allocations por eventos o listas temporales
picos si se desbloquean muchas zonas juntas
```

Problemas frecuentes:

```txt
chequear condicion de desbloqueo en Update
recalcular todo el mapa por un cambio local
notificar a demasiados sistemas innecesarios
no separar debug de runtime
```

---

## Criterio de optimizacion

Opciones para reducir costo:

```txt
usar eventos para desbloqueos
actualizar solo elementos afectados
evitar chequeos por frame
cachear estado
notificar solo a consumidores necesarios
recalcular rutas solo si estan afectadas
activar debug solo cuando se necesita
```

Ejemplo:

```txt
Mala practica:
cada camino revisa en Update si ya se cumplio la ronda.

Mejor:
el sistema de rondas emite un evento,
y el camino correspondiente se desbloquea.
```

---

## Preguntas antes de implementar

Antes de implementar desbloqueo de caminos, una IA debe responder:

```txt
¿Que camino cambia?
¿Cual es su estado inicial?
¿Que condicion lo desbloquea?
¿Quien dispara el cambio?
¿Que estructura del mapa se modifica?
¿Quien consume el cambio?
¿Hay que recalcular rutas?
¿Como se debuggea?
¿Que pasa si se intenta desbloquear dos veces?
¿El cambio realmente afecta gameplay?
```

---

## Validacion visual

Debe poder verse:

```txt
camino bloqueado
camino desbloqueado
estado actual
condicion cumplida
conexion habilitada
ruta antes del cambio
ruta despues del cambio
```

Esto permite detectar:

```txt
camino visualmente abierto pero logicamente bloqueado
ruta logica abierta pero visualmente cerrada
eventos que no disparan
desbloqueos duplicados
sistemas consumidores no actualizados
```

---

## Errores comunes

```txt
desbloquear solo lo visual
no actualizar la estructura logica
no notificar consumidores
usar costo alto como bloqueo
duplicar estados
hacer chequeos constantes
no validar ruta despues del desbloqueo
mezclar progresion con pathfinding
```

---

## Criterio para una IA

Cuando una IA proponga desbloqueo de caminos, debe justificar:

```txt
por que el mapa necesita cambiar
que elemento se desbloquea
que condicion dispara el cambio
que estructura logica se modifica
quien consume el cambio
si requiere recalcular rutas
que costo tecnico tiene
como se valida
```

No alcanza con decir:

```txt
Abrir camino.
```

Debe explicar que cambia en el mapa logico.

---

## Checklist

Antes de usar desbloqueo de caminos, revisar:

```txt
¿El camino cambia durante la partida?
¿El estado inicial esta definido?
¿La condicion de desbloqueo esta clara?
¿El cambio afecta el mapa logico?
¿El cambio afecta sistemas consumidores?
¿Se evita chequear en Update?
¿Se actualiza solo lo necesario?
¿Se maneja desbloqueo repetido?
¿Se puede debuggear visualmente?
```

---

## Regla final

Desbloquear un camino no es solo cambiar algo visual.

Es cambiar la disponibilidad logica del mapa.

```txt
Condicion cumplida
→ estado actualizado
→ mapa logico modificado
→ sistemas consumidores informados
```
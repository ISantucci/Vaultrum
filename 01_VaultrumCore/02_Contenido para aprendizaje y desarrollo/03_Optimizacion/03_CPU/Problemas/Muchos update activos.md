## Definicion

El problema de muchos `Update` activos aparece cuando demasiados objetos ejecutan logica propia cada frame mediante callbacks de Unity.

En Unity, cada `MonoBehaviour` activo que tenga `Update()` puede ejecutar codigo una vez por frame.

La idea principal es:

```txt
Muchos objetos
× Update por frame
× logica interna
=
costo acumulado de CPU
```

Un solo `Update()` puede ser barato.

Cientos o miles de `Update()` ejecutando logica, busquedas, decisiones, chequeos o calculos pueden volverse un problema.

---

## Responsabilidad de esta nota

Esta nota existe para diagnosticar problemas causados por exceso de logica ejecutandose por frame.

No existe para demonizar `Update`.
No existe para proponer siempre un Update Manager.
No existe para mover toda la logica a una clase central.

Su responsabilidad es ayudar a responder:

```txt
¿Hay demasiados objetos ejecutando trabajo por frame?
```

El foco no esta en eliminar `Update`.

El foco esta en entender:

```txt
que se ejecuta
cuantas veces se ejecuta
cuantos objetos lo ejecutan
si realmente necesita ejecutarse cada frame
```

---

## Sintomas

Sintomas comunes:

```txt
Caidas de FPS al aumentar enemigos.
CPU Usage alto.
Scripts costosos en Profiler.
Frame time inestable.
Spikes cuando aparecen muchos objetos.
Mayor costo al tener muchos proyectiles, enemigos o UI activa.
Sensacion de juego pesado aunque visualmente no sea complejo.
```

Tambien puede aparecer como degradacion progresiva:

```txt
Pocos objetos
→ el juego anda bien.

Muchos objetos activos
→ el juego empieza a caer.
```

---

## Que parte del software suele causarlo

Suele aparecer en sistemas como:

```txt
Enemigos.
Proyectiles.
Torres.
NPCs.
Sistemas de percepcion.
Sistemas de targeting.
UI.
Managers mal distribuidos.
Efectos temporales.
Objetos interactivos.
```

Ejemplo tipico:

```csharp
private void Update()
{
    SearchTarget();
    CheckDistance();
    UpdateUI();
    RecalculatePath();
}
```

El problema no es `Update()` en si.

El problema es:

```txt
que se hace dentro
cuantas veces se hace
cuantos objetos lo hacen
si esa frecuencia esta justificada
```

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
CPU
Game Loop
Frame Budget
```

Tambien puede afectar indirectamente:

```txt
Garbage Collector
```

si dentro de `Update()` se generan allocations, strings, listas temporales o busquedas que crean memoria.

---

## Como detectarlo

Se detecta midiendo el costo de scripts durante gameplay.

Buscar especialmente:

```txt
CPU Usage alto.
Mucho tiempo en Scripts.
Muchos callbacks activos.
Costo creciente al aumentar cantidad de objetos.
Metodos Update costosos.
Spikes asociados a logica por frame.
```

Preguntas practicas:

```txt
¿Cuantos objetos tienen Update?
¿Que hace cada uno?
¿Todos necesitan actualizarse cada frame?
¿Podrian actualizarse por evento?
¿Podrian actualizarse por intervalo?
¿Podrian actualizarse solo cuando estan activos o visibles?
```

---

## Herramientas de deteccion

Herramientas utiles:

```txt
Unity Profiler
CPU Usage
Timeline
Logs de diagnostico
```

Que mirar:

```txt
Scripts.
BehaviourUpdate.
Cantidad de objetos activos.
Tiempo consumido por sistemas de IA, enemigos, torres o proyectiles.
Spikes al aumentar entidades.
```

Logs utiles:

```txt
Cantidad de enemigos activos.
Cantidad de proyectiles activos.
Cantidad de torres activas.
Cantidad de sistemas registrados.
Cantidad de llamadas por segundo.
```

---

## Soluciones posibles

Soluciones candidatas:

```txt
Update Manager.
Reducir frecuencia de actualizacion.
Clases puras.
MonoBehaviour como puente.
Cacheo de referencias.
UI orientada a eventos.
Desactivar updates innecesarios.
Actualizar por distancia al jugador.
Actualizar por grupos.
Actualizar por intervalos.
```

Ejemplo:

```txt
Antes:
Cada enemigo busca objetivo cada frame.

Despues:
Un sistema central actualiza busqueda cada 0.2 segundos.
```

Otro ejemplo:

```txt
Antes:
Cada UI actualiza texto en Update.

Despues:
La UI escucha un evento cuando cambia el dato.
```

La solucion depende de la causa medida.

No todo problema de muchos `Update` requiere el mismo tratamiento.

---

## Trade-offs

Reducir cantidad de `Update` puede mejorar rendimiento, pero trae decisiones.

```txt
Update Manager
→ mas control
→ mas responsabilidad de registro/desregistro.

Reducir frecuencia
→ menos costo
→ posible menor reactividad.

Eventos
→ menos trabajo por frame
→ mas cuidado con suscripciones.

Clases puras
→ menos dependencia de Unity
→ necesitan integracion clara.

Desactivar Updates
→ menos ejecucion innecesaria
→ riesgo de olvidar reactivar sistemas.
```

No se trata de eliminar todos los `Update`.

Se trata de que cada `Update()` tenga una razon real para existir.

---

## Ejemplo en videojuegos

En un Tower Defense:

```txt
300 enemigos
→ cada uno se mueve.

30 torres
→ cada una busca objetivo.

200 proyectiles
→ cada uno avanza.

UI
→ muestra vida, dinero y wave.
```

Si todo eso usa `Update()` propio y ademas hace logica costosa, el costo puede crecer rapido.

Una separacion mas sana seria:

```txt
EnemyMovement
→ actualiza movimiento.

TargetingSystem
→ evalua objetivos por intervalo.

ProjectileManager o Pool
→ controla proyectiles.

UI
→ escucha eventos de cambio.

Update Manager
→ coordina sistemas que no necesitan Update propio.
```

La arquitectura debe reducir trabajo real.

No solo moverlo de lugar.

---

## Como guia el diagnostico

Esta nota guia el diagnostico cuando el problema parece venir de ejecucion frecuente.

Flujo recomendado:

```txt
Sintoma:
caidas o spikes con muchos objetos.

Sospecha:
demasiados Update activos.

Medicion:
CPU Usage / Timeline.

Dato esperado:
alto costo en scripts o BehaviourUpdate.

Problema confirmado:
logica por frame excesiva.

Solucion candidata:
reducir frecuencia, centralizar actualizacion o pasar a eventos.
```

La pregunta clave es:

```txt
¿Esto necesita ejecutarse cada frame?
```

---

## Errores comunes al intentar solucionarlo

Errores comunes:

```txt
Crear un Update Manager que contiene toda la logica del juego.
Reducir frecuencia sin probar gameplay.
Desactivar Updates y olvidar reactivarlos.
Registrar objetos y no desregistrarlos.
Mover logica de muchos Updates a un manager gigante sin separar responsabilidades.
Optimizar sin medir.
```

Ejemplo de mala solucion:

```txt
Problema:
Muchos Update.

Solucion:
Todo pasa a GameManager.Update().

Resultado:
menos callbacks, pero una clase dios.
```

La solucion no deberia destruir arquitectura.

---

## Hacia donde seguir

Si hace falta entender por que la frecuencia importa:

```txt
→ Game loop
```

Si hace falta medir:

```txt
→ Unity Profiler
→ CPU Usage
→ Timeline
```

Si se confirma el problema:

```txt
→ Reducir frecuencia de actualizacion
→ Update Manager como optimizacion
→ UI orientada a eventos
→ MonoBehaviour como puente
→ Separar logica de Unity
```

Si dentro de `Update` hay busquedas:

```txt
→ Busquedas globales por frame
→ Cacheo de referencias
```

Si dentro de `Update` hay allocations:

```txt
→ GC Alloc por frame
→ Evitar allocations por frame
```

---

## Checklist de diagnostico

```txt
¿Hay muchos MonoBehaviours con Update?
¿Cada Update hace trabajo necesario?
¿Hay busquedas dentro de Update?
¿Hay allocations dentro de Update?
¿Hay UI actualizada cada frame?
¿Hay IA o pathfinding cada frame?
¿Hay proyectiles con Update propio?
¿Se midio CPU Usage?
¿Se reviso Timeline?
¿Se puede reducir frecuencia?
¿Se puede pasar a eventos?
¿Se puede centralizar sin crear una clase dios?
¿La solucion reduce trabajo real?
```

---

## Regla final

`Update()` no es malo.

El problema es usarlo como lugar por defecto para cualquier logica.

```txt
Si no necesita ocurrir cada frame,
no deberia estar obligado a correr cada frame.
```
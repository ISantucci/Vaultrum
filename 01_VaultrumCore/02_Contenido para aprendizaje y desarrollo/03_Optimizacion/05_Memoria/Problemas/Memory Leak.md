## Definicion

Un Memory Leak ocurre cuando memoria que ya no deberia usarse queda retenida por referencias vivas.

En un videojuego, esto puede hacer que el uso de memoria crezca con el tiempo, incluso si los objetos o sistemas ya no son necesarios.

La idea principal es:

```txt
Objeto ya no necesario
+ referencia viva
=
memoria retenida
```

En Unity, un objeto destruido o una escena descargada no garantiza que toda memoria relacionada se libere si todavia hay referencias activas.

---

## Responsabilidad de esta nota

Esta nota existe para diagnosticar problemas de memoria retenida en el tiempo.

No existe para explicar toda la gestion de memoria.
No existe para asumir que toda memoria alta es leak.
No existe para proponer limpieza agresiva sin medir.

Su responsabilidad es ayudar a responder:

```txt
¿La memoria crece porque algo queda referenciado cuando ya no deberia?
```

El foco esta en memoria que no baja, objetos retenidos, referencias viejas y degradacion progresiva.

---

## Sintomas

Sintomas comunes:

```txt
Uso de memoria crece con el tiempo.
El juego empeora despues de varias partidas.
Cambiar de escena no libera memoria esperada.
Cada reinicio de nivel consume mas memoria.
La memoria sube pero no baja.
Crashes por falta de memoria.
Rendimiento peor en sesiones largas.
```

Tambien puede verse asi:

```txt
Primera partida
→ estable.

Quinta partida
→ mas memoria y peor rendimiento.
```

O:

```txt
Se cambia de escena.
Pero siguen vivos objetos de la escena anterior.
```

---

## Que parte del software suele causarlo

Suele aparecer por:

```txt
Eventos no desuscriptos.
Managers persistentes reteniendo referencias.
Listas estaticas que crecen.
Diccionarios que no limpian entradas.
Pools mal dimensionados.
Objetos destruidos pero referenciados.
ScriptableObjects reteniendo estado indebido.
Cargas de assets no liberadas.
Addressables no descargados.
Singleons persistentes con referencias viejas.
```

Ejemplo tipico:

```csharp
private void OnEnable()
{
    GameEvents.OnEnemyDied += HandleEnemyDied;
}
```

Pero falta:

```csharp
private void OnDisable()
{
    GameEvents.OnEnemyDied -= HandleEnemyDied;
}
```

Si el objeto queda suscripto, puede seguir referenciado.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
RAM
Memoria administrada
Memoria nativa
VRAM
Garbage Collector
```

Tambien puede afectar CPU si el GC trabaja sobre mas objetos o si sistemas vivos siguen ejecutandose.

Un leak no siempre genera un spike inmediato.

Muchas veces degrada el juego progresivamente.

---

## Como detectarlo

Se detecta observando memoria durante el tiempo.

Buscar especialmente:

```txt
Memoria que sube y no baja.
Objetos retenidos despues de cambiar escena.
Referencias vivas a objetos que deberian morir.
Cantidad creciente de listeners.
Listas o diccionarios que no se limpian.
Assets cargados que no se liberan.
Pools que solo crecen.
```

Preguntas practicas:

```txt
¿La memoria vuelve a bajar despues de cerrar escena?
¿Los objetos destruidos siguen referenciados?
¿Hay eventos sin desuscripcion?
¿Hay managers persistentes guardando referencias?
¿Hay listas estaticas acumulando objetos?
¿Hay assets cargados que ya no se usan?
```

---

## Herramientas de deteccion

Herramientas utiles:

```txt
Memory Profiler
Unity Profiler
GC Alloc
Logs de diagnostico
Comparacion antes y despues
```

Que mirar:

```txt
Snapshots de memoria.
Objetos retenidos.
Referencias vivas.
Assets cargados.
Cantidad de instancias.
Memoria administrada.
Memoria nativa.
```

Metodo util:

```txt
Tomar snapshot inicial.
Jugar o cambiar escenas.
Tomar snapshot posterior.
Comparar objetos que deberian haberse liberado.
```

---

## Soluciones posibles

Soluciones candidatas:

```txt
Desuscribirse de eventos.
Limpiar listas y diccionarios.
Liberar referencias en OnDisable, OnDestroy o flujo correspondiente.
Descargar assets que ya no se usan.
Liberar Addressables correctamente.
Limitar pools.
Evitar referencias estaticas innecesarias.
Revisar managers persistentes.
Separar estado temporal de estado global.
```

Ejemplo:

```txt
Antes:
Un manager persistente guarda enemigos de la escena.

Despues:
El manager limpia referencias al terminar la escena.
```

Otro ejemplo:

```txt
Antes:
Una UI se suscribe a eventos y nunca se desuscribe.

Despues:
La UI se desuscribe al cerrarse o destruirse.
```

---

## Trade-offs

Corregir leaks suele mejorar estabilidad, pero requiere cuidado.

```txt
Limpiar referencias
→ libera memoria
→ riesgo de limpiar algo que todavia se usa.

Desuscribirse de eventos
→ evita referencias vivas
→ requiere ciclo de vida claro.

Limitar pools
→ reduce memoria retenida
→ puede aumentar instanciacion si el limite es bajo.

Descargar assets
→ libera memoria
→ puede generar costo de recarga despues.

Managers persistentes
→ facilitan acceso global
→ pueden retener referencias viejas si no se limpian.
```

El objetivo no es liberar todo siempre.

El objetivo es liberar lo que ya no corresponde conservar.

---

## Ejemplo en videojuegos

En un juego con escenas:

```txt
Menu
→ Nivel 1
→ Menu
→ Nivel 1
```

Si cada entrada al nivel deja objetos referenciados, la memoria puede crecer.

Ejemplo inspirado en un sistema de enemigos:

```txt
EnemyManager persistente
→ guarda lista de enemigos.

Al cambiar escena:
enemigos se destruyen.

Pero:
la lista no se limpia.

Resultado:
referencias viejas retenidas.
```

Otro caso:

```txt
UI de oleada
→ se suscribe a evento OnWaveChanged.

Al cerrar escena:
la UI se destruye.

Pero:
no se desuscribe.

Resultado:
el evento mantiene referencia.
```

---

## Como guia el diagnostico

Esta nota guia el diagnostico cuando la memoria crece con el tiempo.

Flujo recomendado:

```txt
Sintoma:
memoria aumenta progresivamente.

Sospecha:
Memory Leak.

Medicion:
Memory Profiler / snapshots.

Dato esperado:
objetos retenidos despues de que deberian liberarse.

Problema confirmado:
referencias vivas indebidas.

Solucion candidata:
limpiar referencias, desuscribirse o descargar assets.
```

La pregunta clave es:

```txt
¿Que objeto sigue vivo y quien lo esta referenciando?
```

---

## Errores comunes al intentar solucionarlo

Errores comunes:

```txt
Confundir memoria alta con memory leak.
Limpiar referencias sin entender ciclo de vida.
Vaciar pools necesarios.
Desuscribirse en el momento equivocado.
No revisar managers persistentes.
No comparar snapshots.
Liberar assets que se van a necesitar inmediatamente.
Pensar que Destroy elimina toda referencia automaticamente.
```

Ejemplo de mala solucion:

```txt
Problema:
La memoria sube.

Decision:
Forzar limpieza general.

Resultado:
bugs, recargas costosas y referencias nulas.
```

La solucion debe atacar la referencia retenida real.

---

## Hacia donde seguir

Si hace falta entender recursos:

```txt
→ Recursos de hardware
```

Si hace falta medir memoria:

```txt
→ Memory Profiler
→ Unity Profiler
→ Comparacion antes y despues
```

Si el problema viene de eventos:

```txt
→ Eventos no desuscriptos
```

Si el problema viene de pools:

```txt
→ Object Pool como optimizacion
```

Si el problema viene de assets:

```txt
→ Addressables como metodologia de optimizacion
→ AssetManager como optimizacion
```

Si el problema viene de referencias persistentes:

```txt
→ Separar logica de Unity
→ MonoBehaviour como puente
```

---

## Checklist de diagnostico

```txt
¿La memoria crece con el tiempo?
¿La memoria baja al salir de una escena?
¿Hay objetos retenidos despues de destruirse?
¿Hay eventos sin desuscripcion?
¿Hay managers persistentes con referencias viejas?
¿Hay listas estaticas que crecen?
¿Hay pools sin limite?
¿Hay assets cargados que ya no se usan?
¿Se compararon snapshots?
¿Se identifico quien retiene la referencia?
¿La solucion libera solo lo que corresponde?
```

---

## Regla final

Un Memory Leak no es simplemente usar mucha memoria.

Es retener memoria que ya no deberia estar viva.

```txt
Para corregirlo no alcanza con destruir objetos.
Hay que cortar las referencias que los mantienen vivos.
```
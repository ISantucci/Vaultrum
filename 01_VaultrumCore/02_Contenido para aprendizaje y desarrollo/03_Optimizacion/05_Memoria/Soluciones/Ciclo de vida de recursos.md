## Definicion

Controlar el ciclo de vida de un recurso significa decidir explicitamente cuando se carga, cuanto tiempo permanece y cuando se libera.

El lifecycle completo es:

```txt
Load
↓
Use
↓
Release / Unload
```

El patron degenerado, en cambio, es:

```txt
Load
↓
Use
↓
mantener para siempre
```

Ese segundo caso hace crecer la memoria sin que exista un leak tradicional. Nadie perdio una referencia por error. Simplemente nunca se decidio soltarla.

```txt
No todo lo cargado
necesita permanecer cargado
toda la partida.
```

La diferencia es intencion: memoria retenida por decision o memoria retenida por omision.

---

## Que problema ayuda a prevenir

Ayuda principalmente con:

```txt
Memory Leak
Memoria residente que solo crece
Crashes por falta de memoria
Degradacion progresiva en sesiones largas
Recargas costosas de assets ya cargados
```

El sintoma caracteristico:

```txt
Primera partida
→ memoria normal.

Quinta partida
→ mucha mas memoria
→ sin que aparezcan objetos nuevos.
```

Y una variante que confunde bastante:

```txt
Se cambia de escena.
La memoria baja un poco.
Nunca vuelve al valor inicial.
```

---

## Como funciona

Primero hay que separar tres tipos conceptuales de memoria, porque tienen lifecycles distintos.

```txt
Managed memory
→ administrada por C# y el Garbage Collector.

Native memory
→ recursos fuera del managed heap.

GPU memory
→ textures, meshes, buffers, render targets.
```

El objetivo no es memorizar nombres:

```txt
distintos recursos
tienen lifecycles
y sistemas de administracion diferentes
```

Liberar una referencia de C# no descarga automaticamente una textura de la memoria grafica.

Sobre lo administrado, la regla es una sola:

```txt
Un objeto no se libera
mientras exista una referencia viva hacia el.
```

Los sospechosos habituales de esas referencias:

```txt
Referencias directas.
Eventos.
Caches.
Colecciones.
Pools.
Sistemas persistentes.
```

Por eso el trabajo no es liberar mas, sino saber quien sostiene que.

---

## Como aplicarlo en videojuegos

En un Tower Defense el ciclo natural es por partida.

```txt
Entrar al mapa
→ cargar assets del mapa y de las torres disponibles.

Jugar
→ usar.

Volver al menu
→ liberar lo que pertenece a esa partida.
```

Caso malo, muy comun:

```csharp
public class WaveUI : MonoBehaviour
{
    private void Start()
    {
        GameEvents.OnWaveChanged += Refresh;
    }
}
```

La UI se destruye al salir del mapa, pero el evento la sigue referenciando. La partida termino y la UI sigue viva.

Caso bueno:

```csharp
public class WaveUI : MonoBehaviour
{
    private void OnEnable()
    {
        GameEvents.OnWaveChanged += Refresh;
    }

    private void OnDisable()
    {
        GameEvents.OnWaveChanged -= Refresh;
    }
}
```

Lo mismo pasa con las colecciones del manager de enemigos:

```txt
Antes:
La lista de enemigos vive en un manager persistente
y nunca se vacia al terminar la wave.

Despues:
El manager limpia la lista al cerrar la partida.
```

Y con los assets de tipos de enemigo que solo aparecen en un mapa:

```txt
Antes:
Se cargan al entrar y quedan cargados siempre.

Despues:
Se liberan al volver al menu.
```

---

## Relacion con arquitectura

Esto es arquitectura antes que optimizacion.

```txt
Alguien tiene que ser dueño del recurso.
Ese dueño tiene que tener un final.
Ese final tiene que ejecutarse siempre.
```

Lo que ayuda:

```txt
Ciclos de vida explicitos por escena o por partida.
Suscripcion y desuscripcion simetricas.
Un punto claro de carga y otro de descarga.
Estado temporal separado del estado global.
Sistemas persistentes con responsabilidad acotada.
```

Lo que lo rompe:

```txt
Managers que acumulan referencias de todo.
Estado estatico que nadie limpia.
Acceso global sin dueño definido.
Caches sin politica de invalidacion.
```

Si nadie puede responder quien libera un recurso, ese recurso no se libera.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
RAM
Memoria administrada
Memoria nativa
VRAM
Garbage Collector
```

Y de rebote afecta CPU:

```txt
Mas objetos vivos
→ mas trabajo para el GC.

Sistemas que quedaron vivos
→ siguen ejecutandose.
```

La textura del render de un mapa que ya no se juega no consume CPU, pero ocupa memoria grafica que despues falta.

```txt
Memoria retenida
→ menos margen
→ mas riesgo de recargas y de crash.
```

---

## Cuando conviene usarlo

Conviene controlar el lifecycle explicitamente cuando:

```txt
El juego tiene escenas, niveles o partidas repetibles.
Hay assets pesados asociados a contextos concretos.
La memoria crece entre partidas.
El target de plataforma tiene memoria ajustada.
Se usan sistemas persistentes.
Hay pools, caches o colecciones de larga vida.
```

Siempre conviene, en realidad, cuando el contenido no cabe todo junto.

---

## Cuando NO conviene usarlo

No conviene forzar descargas cuando:

```txt
El asset se vuelve a necesitar enseguida.
La memoria disponible sobra ampliamente.
El costo de recarga produce un freeze visible.
El recurso es chico y se usa en todo el juego.
No hay problema medido.
```

Ejemplo:

```txt
Descargar los proyectiles al terminar cada wave
→ se recargan a los tres segundos
→ se cambio memoria por un stutter.
```

El objetivo no es liberar todo siempre. Es liberar lo que ya no corresponde conservar.

---

## Trade-offs

```txt
Liberar temprano
→ menos memoria residente
→ posible costo de recarga.

Mantener cargado
→ transiciones rapidas
→ mas memoria ocupada.

Ciclo de vida explicito
→ control real
→ mas codigo y mas disciplina.

Cache amplio
→ menos recomputacion
→ mas memoria retenida.

Pool grande
→ menos instanciacion
→ mas memoria inutilizada.
```

Ese ultimo punto merece atencion propia. Pooling reaparece aca como trade-off, no como solucion:

```txt
Un pool gigantesco
que conserva cientos de objetos inutilizados
resuelve un problema de CPU
creando uno de memoria.
```

---

## Riesgos de aplicarlo mal

Riesgos comunes:

```txt
Liberar algo que todavia se esta usando.
Desuscribirse en el momento equivocado.
Descargar assets que se necesitan enseguida.
Vaciar pools necesarios.
Suponer que destruir un objeto corta toda referencia.
Suponer que cambiar de escena libera todo.
Confundir memoria alta con leak.
Forzar limpieza general en vez de atacar la referencia real.
```

Ejemplo de mala correccion:

```txt
Problema:
La memoria sube entre partidas.

Decision:
Forzar una limpieza general al volver al menu.

Resultado:
Referencias nulas, recargas costosas y bugs nuevos.
```

La correccion tiene que apuntar a la referencia concreta que retiene, no al sintoma general.

---

## Checklist de implementacion

```txt
¿El problema fue medido con snapshots comparados?
¿Que tipo de memoria esta creciendo?
¿Quien es el dueño de este recurso?
¿En que momento exacto se libera?
¿Ese momento se ejecuta siempre?
¿Las suscripciones tienen su desuscripcion?
¿Las colecciones se limpian al cerrar el contexto?
¿Los sistemas persistentes sueltan referencias viejas?
¿Los pools tienen tamaño maximo?
¿Los caches tienen politica de invalidacion?
¿La descarga genera una recarga inmediata?
¿La memoria vuelve al valor inicial despues del ciclo?
```

---

## Regla final

Cargar es facil. Liberar es una decision de diseño.

```txt
La memoria no crece
solo por errores.
Crece cuando nadie definio
cuando algo deja de hacer falta.
```

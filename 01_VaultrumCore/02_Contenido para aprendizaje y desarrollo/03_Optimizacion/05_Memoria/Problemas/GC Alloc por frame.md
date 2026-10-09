## Definicion

GC Alloc por frame ocurre cuando el juego genera memoria administrada nueva durante frames de gameplay.

Esa memoria queda en el Heap y eventualmente debe ser limpiada por el Garbage Collector.

La idea principal es:

```txt
Allocations frecuentes
→ presion sobre el Garbage Collector
→ posibles spikes
→ stuttering
```

No toda allocation es un problema.

El problema aparece cuando se generan allocations constantemente, especialmente cada frame o en momentos criticos.

---

## Responsabilidad de esta nota

Esta nota existe para diagnosticar problemas causados por allocations frecuentes durante gameplay.

No existe para prohibir toda allocation.
No existe para optimizar memoria sin medir.
No existe para reemplazar la lectura de Profiler.

Su responsabilidad es ayudar a responder:

```txt
¿El juego esta creando memoria temporal de forma repetida?
```

El foco esta en detectar si hay basura administrada generandose en loops, Updates, UI, eventos o sistemas temporales.

---

## Sintomas

Sintomas comunes:

```txt
Stuttering.
Spikes periodicos.
Frame time irregular.
Tirones cada pocos segundos.
GC Alloc visible en Profiler.
Picos del Garbage Collector.
Caidas al generar UI, strings, listas o efectos.
```

Tambien puede sentirse asi:

```txt
FPS promedio aceptable.
Pero cada tanto hay tirones.
```

Esto puede indicar que no hay un problema constante de FPS, sino picos asociados al GC.

---

## Que parte del software suele causarlo

Suele aparecer por:

```txt
Strings creados por frame.
Concatenaciones repetidas.
LINQ en Update.
Listas temporales.
Arrays nuevos.
Closures.
Boxing.
Instantiate/Destroy.
Eventos mal usados.
Logs constantes.
UI actualizada por frame.
```

Ejemplo tipico:

```csharp
private void Update()
{
    scoreText.text = "Score: " + score;
}
```

Si ocurre cada frame, puede generar strings nuevos constantemente.

Otro ejemplo:

```csharp
var enemiesInRange = enemies.Where(e => e.IsAlive).ToList();
```

Si ocurre por frame, puede generar allocations.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
Garbage Collector
Memoria administrada
CPU
Frame Budget
```

El GC necesita tiempo para limpiar memoria que ya no se usa.

Cuando limpia durante gameplay, puede generar spikes.

El problema no es solamente memoria.

Tambien es tiempo de CPU usado para limpiar esa memoria.

---

## Como detectarlo

Se detecta revisando allocations durante gameplay.

Buscar especialmente:

```txt
GC Alloc por frame.
Picos de Garbage Collector.
Allocations en Update.
Allocations en UI.
Allocations en logs.
Allocations al disparar, mover, buscar o actualizar listas.
```

Preguntas practicas:

```txt
¿Hay memoria nueva cada frame?
¿Que metodo la genera?
¿Ocurre siempre o solo en ciertos eventos?
¿La allocation es necesaria?
¿Se puede reutilizar estructura?
¿Se puede actualizar solo cuando cambia el dato?
```

---

## Herramientas de deteccion

Herramientas utiles:

```txt
Unity Profiler
GC Alloc
Timeline
Memory Profiler
Logs de diagnostico
```

Que mirar:

```txt
GC Alloc.
Managed allocations.
Picos del Garbage Collector.
Metodos que generan memoria.
Strings temporales.
Listas o arrays creados por frame.
```

Tambien conviene revisar el contexto:

```txt
¿La allocation ocurre en gameplay?
¿Ocurre en carga?
¿Ocurre una sola vez?
¿Ocurre cada frame?
```

No toda allocation requiere solucion.

---

## Soluciones posibles

Soluciones candidatas:

```txt
Evitar allocations por frame.
Reutilizar listas.
Evitar LINQ en caminos criticos.
Evitar strings por frame.
Actualizar UI solo cuando cambia el dato.
Cachear referencias.
Usar Object Pool para objetos temporales.
Reducir logs en gameplay.
Preasignar estructuras.
```

Ejemplo:

```txt
Antes:
Crear una lista nueva cada Update.

Despues:
Reutilizar una lista existente y limpiarla cuando corresponda.
```

Otro ejemplo:

```txt
Antes:
Actualizar texto cada frame con concatenacion.

Despues:
Actualizar texto solo cuando cambia el valor.
```

---

## Trade-offs

Reducir allocations puede mejorar estabilidad, pero trae cuidado.

```txt
Reutilizar listas
→ menos GC
→ riesgo de datos viejos si no se limpian.

Evitar LINQ
→ menos allocations
→ codigo a veces menos expresivo.

Cachear strings
→ menos basura
→ mas estado a mantener.

Object Pool
→ menos instanciacion
→ necesidad de reset correcto.

UI por eventos
→ menos trabajo por frame
→ cuidado con suscripciones.
```

No conviene convertir todo el codigo en microoptimizaciones dificiles de leer.

La optimizacion debe enfocarse en caminos criticos.

---

## Ejemplo en videojuegos

En un juego con UI activa:

```txt
Vida
Monedas
Puntaje
Municion
Objetivos
Cooldowns
```

Si todos esos textos se actualizan cada frame con strings nuevos, pueden generar GC Alloc.

En un Tower Defense:

```txt
Cada torre busca enemigos.
Cada busqueda crea una lista.
Cada frame se actualizan textos.
Cada impacto genera popup.
Cada disparo instancia proyectil.
```

El costo puede aparecer como:

```txt
allocations constantes
→ GC
→ spikes
→ tirones
```

---

## Como guia el diagnostico

Esta nota guia el diagnostico cuando hay tirones o spikes asociados a memoria temporal.

Flujo recomendado:

```txt
Sintoma:
stuttering o spikes.

Sospecha:
GC Alloc por frame.

Medicion:
Unity Profiler / GC Alloc / Timeline.

Dato esperado:
allocations constantes durante gameplay.

Problema confirmado:
memoria temporal generada repetidamente.

Solucion candidata:
evitar allocations, reutilizar estructuras o actualizar por eventos.
```

La pregunta clave es:

```txt
¿Este sistema crea memoria nueva en cada frame o accion repetida?
```

---

## Errores comunes al intentar solucionarlo

Errores comunes:

```txt
Intentar eliminar absolutamente toda allocation.
Optimizar codigo que no corre durante gameplay.
Reutilizar listas sin limpiarlas.
Ocultar allocations dentro de helpers.
Pensar que toda allocation es grave.
No diferenciar carga inicial de gameplay.
Aplicar Object Pool sin reset correcto.
Cambiar codigo legible por microoptimizacion sin beneficio medido.
```

Ejemplo de mala solucion:

```txt
Problema:
Hay una allocation una sola vez al cargar escena.

Decision:
Reescribir todo el sistema.

Resultado:
complejidad innecesaria.
```

Hay que diferenciar frecuencia y contexto.

---

## Hacia donde seguir

Si hace falta entender memoria y GC:

```txt
→ Recursos de hardware
```

Si hace falta medir:

```txt
→ Unity Profiler
→ GC Alloc
→ Timeline
→ Memory Profiler
```

Si el problema viene de strings:

```txt
→ Strings por frame
```

Si el problema viene de objetos temporales:

```txt
→ Instantiate y Destroy constantes
→ Object Pool como optimizacion
```

Si el problema viene de UI:

```txt
→ UI actualizada innecesariamente
→ UI orientada a eventos
```

Si ya se confirmo el problema:

```txt
→ Evitar allocations por frame
```

---

## Checklist de diagnostico

```txt
¿Hay GC Alloc durante gameplay?
¿Ocurre cada frame?
¿Ocurre en Update?
¿Ocurre al actualizar UI?
¿Ocurre al crear strings?
¿Ocurre al usar LINQ?
¿Ocurre al crear listas o arrays?
¿Ocurre al instanciar objetos?
¿El spike coincide con Garbage Collector?
¿La allocation es necesaria?
¿Se puede reutilizar estructura?
¿Se puede actualizar solo cuando cambia el dato?
¿Se midio antes/despues?
```

---

## Regla final

GC Alloc por frame no es un problema de memoria solamente.

Es un problema de estabilidad del frame.

```txt
Si el juego crea basura constantemente,
en algun momento el Garbage Collector va a cobrar ese costo.
```
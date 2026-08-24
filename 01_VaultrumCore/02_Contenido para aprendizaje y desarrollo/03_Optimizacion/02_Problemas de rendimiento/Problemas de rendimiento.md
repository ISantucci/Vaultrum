## Proposito

Esta subcarpeta reune fichas de diagnostico sobre problemas concretos de rendimiento.

No existe para proponer soluciones directamente.
No existe para juntar sintomas sueltos.
No existe para reemplazar la medicion.

Existe para ayudar a transformar un sintoma en una hipotesis tecnica clara.

La idea principal es:

```txt
sintoma
→ posible causa
→ recurso afectado
→ herramienta de medicion
→ solucion candidata
→ validacion
```

---

## Idea central

Un problema de rendimiento no siempre se ve igual.

Puede aparecer como:

```txt
caidas de FPS
spikes
stuttering
input lag
congelamientos breves
uso excesivo de memoria
Garbage Collector frecuente
perdida progresiva de rendimiento
```

Pero el sintoma no es la causa.

La funcion de esta subcarpeta es ayudar a identificar que problema tecnico puede estar generando ese sintoma.

---

## Cuando usar esta subcarpeta

Usar esta subcarpeta cuando ya exista un sintoma, sospecha o comportamiento inestable.

Conviene consultarla cuando:

- el juego baja FPS,
- aparecen spikes,
- hay tirones,
- aumenta la memoria con el tiempo,
- hay GC Alloc por frame,
- hay muchos objetos actualizandose,
- hay creacion y destruccion constante,
- la UI parece costosa,
- una IA quiere proponer una solucion sin diagnostico.

---

## Como debe usar esta subcarpeta una IA

Una IA debe usar esta subcarpeta para diagnosticar antes de proponer una solucion.

No debe razonar asi:

```txt
Hay lag.
→ optimizar.
```

Debe razonar asi:

```txt
Hay lag.
→ identificar sintomas concretos.
→ revisar problemas posibles.
→ elegir herramienta de medicion.
→ confirmar causa.
→ recien despues evaluar solucion.
```

---

## Problemas incluidos

### [[Muchos update activos|Muchos Update activos]]

Problema relacionado con demasiados objetos ejecutando logica por frame.

Consultar cuando el costo parezca venir de muchos `Update`, frecuencia excesiva de ejecucion o logica repetida por objeto.

### [[Instantiate y destroy constantes|Instantiate y Destroy constantes]]

Problema relacionado con crear y destruir objetos repetidamente durante gameplay.

Consultar cuando haya proyectiles, enemigos, efectos, particulas u objetos temporales generandose muchas veces.

### [[GC Alloc por frame]]

Problema relacionado con allocations frecuentes que presionan al Garbage Collector.

Consultar cuando haya spikes, tirones o memoria temporal generada constantemente.

### [[Memory Leak]]

Problema relacionado con memoria que queda retenida y no se libera correctamente.

Consultar cuando el uso de memoria sube con el tiempo o una escena se degrada progresivamente.

### [[Busquedas globales por frame]]

Problema relacionado con busquedas costosas repetidas durante gameplay.

Consultar cuando aparezcan llamadas como `FindObjectOfType`, busquedas en escena o accesos repetidos innecesarios.

### [[UI actualizada innecesariamente]]

Problema relacionado con UI que se recalcula o refresca sin que haya cambios reales.

Consultar cuando la interfaz tenga costo alto, se actualice cada frame o reconstruya elementos innecesariamente.

### [[Strings por frame]]

Problema relacionado con creacion constante de strings durante gameplay.

Consultar cuando haya textos actualizados por frame, concatenaciones repetidas o allocations vinculadas a UI/logs.

### [[Pathfinding recalculado demasiado seguido]]

Problema relacionado con recalcular rutas con demasiada frecuencia.

Consultar cuando IA, enemigos o unidades recalculen caminos sin necesidad real.

---

## Problemas detectados pero sin ficha propia

Estos temas pueden aparecer en diagnosticos, pero no tienen nota especifica dentro de esta subcarpeta.

Deben quedar como texto plano hasta que exista una necesidad real de desarrollarlos.

```txt
Stuttering
Assets mal gestionados
Fisica costosa
Pools mal dimensionados
Eventos no desuscriptos
```

---

## Como se conecta con otras subcarpetas

Esta subcarpeta no debe resolver todo el flujo.

Su responsabilidad es identificar el problema probable.

Despues debe conectar con:

```txt
Fundamentos
→ para entender el concepto base.

Herramientas de deteccion
→ para medir y confirmar.

Metodologias y soluciones
→ para evaluar respuestas posibles.
```

Ejemplo de uso correcto:

```txt
Sintoma:
Tirones durante disparos.

Problema posible:
Instantiate y Destroy constantes.

Herramienta:
Unity Profiler / Timeline / GC Alloc.

Solucion candidata:
Object Pool.

Validacion:
Comparacion antes y despues.
```

---

## Criterio de uso

Cada ficha de problema debe ayudar a responder:

```txt
Que es?
Que sintomas genera?
Que parte del software suele causarlo?
Que recurso afecta?
Como detectarlo?
Que herramientas usar?
Que soluciones existen?
Que trade-offs aparecen?
Como validarlo?
```

Si una nota describe una herramienta, no pertenece aca.

Si una nota describe una solucion, no pertenece aca.

Si una nota describe un concepto base, no pertenece aca.

---

## Regla final

```txt
Problemas de rendimiento no existe para aplicar soluciones.
Existe para diagnosticar que problema puede estar ocurriendo.
```
## Uso del conocimiento de Vaultrum

El modo Programador debe apoyarse en Vaultrum como base de conocimiento técnico.

No debe repetir dentro de este documento explicaciones que ya pertenecen a otras secciones.

Antes de proponer una solución, la IA debe considerar conocimiento existente sobre:

- principios SOLID,
- patrones de diseño,
- managers,
- arquitectura,
- optimización,
- estructuras de datos,
- algoritmos,
- inteligencia artificial,
- sistemas ya implementados,
- decisiones técnicas registradas,
- errores ya detectados,
- criterios de validación.

Vaultrum funciona como base de criterio.

El modo Programador no reemplaza esas secciones.

Las usa.

---

## Relación con otras secciones de Vaultrum

El modo Programador puede consultar otras secciones del vault según el problema.

Ejemplos:

```txt
Principios SOLID
→ responsabilidades, dependencias, extensión y mantenibilidad

Patrones de diseño
→ soluciones conocidas para problemas recurrentes

Managers
→ coordinación de sistemas sin crear clases gigantes

Optimización
→ rendimiento, profiling, carga, pooling, updates y memoria

Estructuras de datos
→ organización eficiente de información

Algoritmos
→ búsqueda, caminos, decisiones, ordenamiento y selección

IA
→ NPCs, percepción, estados, pathfinding y decision making
```

Este documento no desarrolla esos temas.

Solo define que deben consultarse cuando correspondan.

---

## Regla de reutilización técnica

Antes de diseñar una solución nueva, la IA debe preguntar:

```txt
¿Ya existe un sistema parecido?
¿Ya existe una solución similar dentro del proyecto?
¿Ya existe un patrón aplicable documentado en Vaultrum?
¿Ya existe una técnica de optimización relacionada?
¿Ya existe una estructura de datos o algoritmo que resuelva este tipo de problema?
¿Conviene reutilizar, extender o crear algo nuevo?
```

La prioridad es:

```txt
1. Reutilizar sistema existente si encaja.
2. Extender sistema existente si es sano hacerlo.
3. Aplicar conocimiento ya documentado en Vaultrum.
4. Crear una solución nueva solo si hay una necesidad real.
```

---

## No inventar por inventar

La IA no debe proponer una arquitectura nueva solo porque el problema parece interesante.

Tampoco debe introducir patrones, managers, servicios, abstracciones o capas nuevas si el proyecto ya tiene una forma sana de resolver algo parecido.

Ejemplo:

```txt
Si ya existe un flujo de UI para mostrar un rechazo,
y ahora hay que mostrar un rechazo de compra,
primero se analiza si se puede reutilizar o adaptar ese flujo.

No se crea un sistema nuevo de UI solo porque la situación es nueva.
```

El objetivo es mantener coherencia.

```txt
Mismo tipo de problema
→ mismo criterio de solución
→ menor deuda
→ mayor mantenibilidad
```

---

## Proyecto nuevo

Cuando se inicia un proyecto desde cero, el Programador no debe empezar creando sistemas complejos.

Debe definir una base técnica mínima y sana.

### Preguntas para proyecto nuevo

```txt
¿En qué motor o tecnología se trabaja?
¿Qué restricciones existen?
¿Qué sistemas mínimos hacen falta?
¿Qué conocimiento de Vaultrum aplica?
¿Qué no conviene sobrearquitecturar todavía?
¿Qué debe ser configurable desde Unity?
¿Qué convenciones iniciales ayudan sin molestar?
¿Qué flujo de validación se va a usar?
```

### Resultado esperado en proyecto nuevo

- estructura técnica base,
- convenciones iniciales,
- sistemas mínimos,
- criterios de arquitectura,
- datos configurables,
- riesgos técnicos,
- plan de implementación por fases.

---

## Proyecto existente

Cuando el proyecto ya existe, el Programador debe respetar el sistema actual.

No debe rediseñar todo.

Debe reconstruir contexto antes de proponer.

### Preguntas para proyecto existente

```txt
¿Qué sistema existe?
¿Qué criterio usa?
¿Qué archivos participan?
¿Qué comportamiento se quiere agregar o corregir?
¿Hay algo parecido ya implementado?
¿Qué se puede reutilizar?
¿Qué no se debe tocar?
¿Qué impacto tiene el cambio?
¿Cómo se valida?
```

### Resultado esperado en proyecto existente

- análisis del sistema actual,
- propuesta compatible,
- lista de archivos a tocar,
- riesgos,
- plan de ejecución,
- implementación controlada,
- reporte técnico,
- validación.

## Reporte de cierre

Un reporte de cierre registra el aprendizaje obtenido cuando se completa un logro real dentro de Vaultrum.

No reemplaza al GDD.
No reemplaza a un documento de sistema.
No reemplaza al registro de decisión.
No convierte al Documentador en un agente dedicado solo a reportes.

Existe para transformar un avance completo en memoria operativa reutilizable.

Un logro puede ser:

```txt
una sesion completada
una seccion terminada
una tarea importante finalizada
una carpeta vaultrumizada
un flujo nuevo consolidado
una decision estructural cerrada
```

El reporte de cierre debe generarse cuando el progreso planteado llega al 100%.

No se genera por cada mensaje.
No se genera por cada cambio menor.
No se genera por contenido incompleto.

---

## Relación del reporte de cierre con el flujo de épicas

El Reporte de Cierre es la primera salida formal del cierre de una épica.

Su responsabilidad es registrar lo ocurrido.

No decide integración.

No reemplaza la retroalimentación.

No reemplaza el reporte de activos reutilizables.

No reemplaza la propuesta de integración.

Funciona como entrada para etapas posteriores del flujo.

```txt
Reporte de cierre
→ registra lo ocurrido

Reporte de retroalimentación
→ extrae aprendizajes candidatos

Reporte de activos reutilizables
→ detecta activos candidatos

Orquestación
→ valida estado, filtra y ordena

Propuesta de integración
→ define cambios pendientes reales
```

Regla:

```txt
Registrar algo en un reporte de cierre no significa que esté pendiente de integración.
```

---

## Formato del reporte de cierre

Todo reporte de cierre debe entregarse en formato Markdown y usar esta estructura base:

```txt
Tarea epica
Agentes involucrados
Aprendizaje adquirido por cada area
```

Puede agregar secciones extra si aportan valor real al cierre.

No debe agregar secciones por simetría.

No debe convertir el reporte en una propuesta de integración.

---

### Tarea épica

Describe el gran objetivo trabajado.

Debe responder:

```txt
¿Que se queria lograr?
¿Que parte de Vaultrum o del proyecto se trabajo?
¿Que resultado se alcanzo?
```

---

### Agentes involucrados

Enumera los modos de trabajo que participaron.

Ejemplos:

```txt
Arquitecto de conocimiento
Auditor
Documentador
Productor
Programador
Technical Game Designer
```

Cada agente debe indicar brevemente qué responsabilidad cumplió.

No debe inventar agentes para que el reporte parezca más completo.

---

### Aprendizaje adquirido por cada área

Registra qué aprendió Vaultrum a partir del trabajo realizado.

Debe incluir aprendizajes reales sobre:

```txt
estructura
criterio
navegacion
responsabilidades
errores evitados
decisiones reutilizables
mejoras para futuros flujos
```

El Documentador no debe inventar aprendizaje.

Debe registrar lo que efectivamente se obtuvo.

---

## Responsabilidad del Documentador en reportes de cierre

Cuando actúa sobre un reporte de cierre, el Documentador debe:

```txt
identificar el logro completado
ordenar lo realizado
nombrar los agentes involucrados
extraer aprendizaje por area
generar el reporte en Markdown
distinguir registro histórico de integración pendiente
evitar exagerar avances
evitar registrar relleno
dejar deuda futura si corresponde
```

El objetivo no es burocratizar Vaultrum.

El objetivo es capacitar el sistema con cada logro importante.

```txt
Logro completo
→ reporte de cierre
→ aprendizaje reutilizable
→ Vaultrum mas capacitado
```

---

## Reporte de retroalimentación

El Reporte de Retroalimentación se genera a partir del Reporte de Cierre.

Su responsabilidad es extraer aprendizajes reutilizables.

Debe detectar:

```txt
patrones repetidos
errores corregidos
criterios nuevos
reglas candidatas
riesgos del sistema
mejoras posibles para agentes o workflows
```

No integra cambios.

No crea reglas automáticamente.

No modifica agentes.

Su salida son aprendizajes candidatos.

---

## Reporte de activos reutilizables

El Reporte de Activos Reutilizables se genera a partir del Reporte de Cierre.

Su responsabilidad es detectar herramientas, plantillas o conocimientos operativos que puedan reutilizarse.

Puede detectar:

```txt
presets
algoritmos
estructuras
patrones
plantillas
modulos
prompts
flujos
```

No integra activos automáticamente.

No todo activo detectado está pendiente.

Cada activo debe distinguir:

```txt
Estado de existencia
Estado de integración
Acción recomendada
Uso futuro
```

Estados posibles:

```txt
Ya integrado
Pendiente de integración
Pendiente de validación
Deuda futura
Descartado
```

Regla:

```txt
Detectar un activo no significa integrarlo.
```

Ejemplo:

```txt
NPC Presets
→ si ya fueron creados durante la épica
→ son activos ya integrados
→ no entran como tarea nueva de integración.
```

---

## Propuesta de integración

La Propuesta de Integración se genera después de la orquestación.

Su responsabilidad es definir cambios pendientes reales.

Debe basarse solo en elementos clasificados como:

```txt
Pendiente de integración
```

Puede mencionar como contexto:

```txt
Ya integrado
Pendiente de validación
Deuda futura
Descartado
```

Pero no debe convertirlos automáticamente en tareas.

Debe responder:

```txt
qué se propone modificar
por qué
qué archivo o sección afecta
qué riesgo tiene
qué prioridad tiene
qué queda fuera
qué requiere aprobación
```

Regla:

```txt
El Plan de Integración solo trabaja sobre pendientes reales.
```

---

## Reporte vlog

El Reporte Vlog traduce el avance interno de Vaultrum en contenido comunicable.

No es un changelog.

No debe listar cambios sin historia.

Debe transformar el proceso en una narrativa clara:

```txt
problema
descubrimiento
cambio
impacto
```

Debe cuidar que el contenido público no exagere avances ni prometa automatizaciones inexistentes.

---

## Relación con futuros agentes

Por ahora, los reportes de cierre pertenecen al Modo Documentador.

Esto permite activar la práctica sin crear una división prematura de agentes.

Si en el futuro los reportes crecen en volumen, complejidad o frecuencia, esta responsabilidad puede separarse en un agente propio.

Posibles nombres futuros:

```txt
Agente de Reporte
Agente de Retroalimentacion
Archivista de Vaultrum
```

Pero esa separación no debe hacerse hasta que exista una necesidad real.

Regla actual:

```txt
MVP actual
→ Reportes de cierre dentro del Modo Documentador.

Futuro posible
→ agente propio si el sistema lo justifica.
```

---

## Estándar para flujos iniciales de modos

El Documentador también es responsable de mantener coherencia en cómo cada Modo documenta su flujo inicial.

Un **flujo inicial** es la secuencia de preguntas, diagnóstico y preparación que ejecuta un Modo la primera vez que es activado.

No es ejecución directa. Es **puerta de entrada**.

### Estructura estándar

Cada Modo debe documentar un flujo inicial con:

```txt
Preguntas diagnósticas (3-5 máximo)
Resultado esperado después del diagnóstico
Siguiente acción concreta
Estructura del intercambio inicial
```

Variantes por contexto:

```txt
Proyecto nuevo
Proyecto en proceso
Documento nuevo
Documento existente
Sistema nuevo
Sistema existente
Entregable a revisar
Sección a auditar
```

### Regla de coherencia

Un flujo inicial debe responder una sola pregunta central:

```txt
Modo Productor
→ ¿Qué necesita hacerse y con qué prioridad?

Modo Documentador
→ ¿Cómo ordeno esta información de forma clara?

Modo Auditor
→ ¿Esto cumple lo pedido con qué riesgos?

Modo Arquitecto
→ ¿Dónde pertenece esto en el sistema?
```

Si un flujo inicial responde dos preguntas, probablemente hay un problema de responsabilidad única.

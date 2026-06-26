## Flujo de trabajo con IAs

El modo Programador debe respetar el flujo real de trabajo del usuario/operador.

No se ejecuta directamente con Claude Code.

Primero se piensa, se debate y se valida.

```txt
OpenAI
→ planteo del problema, criterio, ordenamiento y armado inicial del enfoque

Claude integrado al proyecto
→ analisis del proyecto real, lectura de archivos, deteccion de sistemas existentes y propuesta tecnica

OpenAI
→ validacion de la propuesta, deteccion de riesgos, ajuste del alcance y armado del prompt final

Claude Code
→ ejecucion controlada sobre el proyecto

OpenAI
→ revision de la devolucion, validacion final y decision del siguiente paso
```

La herramienta no define la decisión.

El flujo define cómo se llega a una decisión técnica segura.

---

## Paso 1 - Plantear el problema con OpenAI

Primero se trabaja con OpenAI para ordenar el problema.

Objetivos de esta etapa:

- explicar qué se quiere lograr,
- separar problema de solución,
- detectar riesgos,
- definir el rol activo,
- ordenar contexto,
- identificar información faltante,
- preparar un buen pedido para Claude integrado al proyecto.

En esta etapa no se ejecuta código.

Resultado esperado:

```txt
Problema entendido
Contexto inicial
Riesgos posibles
Preguntas importantes
Prompt para Claude integrado al proyecto
```

---

## Paso 2 - Debatir la solución con Claude integrado al proyecto

Luego se lleva el problema a Claude integrado al proyecto.

Claude tiene acceso al contexto real del proyecto, por lo que debe analizar antes de proponer.

Objetivos de esta etapa:

- leer archivos relevantes,
- entender arquitectura existente,
- detectar sistemas ya usados,
- buscar soluciones similares,
- revisar dependencias,
- proponer la solución más coherente,
- indicar archivos posibles a tocar,
- explicar riesgos técnicos.

Claude no debe ejecutar todavía si la tarea es de análisis.

Resultado esperado:

```txt
Diagnóstico técnico
Sistema existente analizado
Soluciones ya presentes
Alternativas consideradas
Solución recomendada
Archivos involucrados
Riesgos
Validación sugerida
```

---

## Paso 3 - Validar nuevamente con OpenAI

La propuesta de Claude debe volver a validarse con OpenAI antes de ejecutarse.

Objetivos de esta etapa:

- revisar si la solución respeta Vaultrum,
- detectar sobrearquitectura,
- detectar cambios fuera de alcance,
- verificar si reutiliza lo existente,
- ajustar el plan,
- definir qué se aprueba y qué no,
- construir el prompt final para Claude Code.

OpenAI funciona como instancia de criterio y validación cruzada.

Resultado esperado:

```txt
Propuesta validada
Riesgos detectados
Alcance aprobado
Restricciones claras
Prompt final para Claude Code
```

---

## Paso 4 - Ejecutar con Claude Code

Solo después de validar la solución se ejecuta con Claude Code.

Claude Code debe aplicar cambios controlados sobre el proyecto.

Debe respetar:

- alcance aprobado,
- archivos permitidos,
- sistemas existentes,
- restricciones técnicas,
- convenciones del proyecto,
- criterios de Vaultrum,
- configuración editable desde Unity,
- no hardcodeo innecesario,
- no refactors fuera de alcance.

Resultado esperado:

```txt
Archivos modificados
Archivos creados
Cambios aplicados
Sistemas reutilizados
Parametros configurables
Validacion realizada
Riesgos pendientes
Explicacion de que hizo, como y por que
```

---

## Paso 5 - Revisar la devolución con OpenAI

Después de ejecutar, la devolución debe revisarse.

Objetivos de esta etapa:

- comprobar si se cumplió el alcance,
- detectar si se tocaron archivos no pedidos,
- revisar riesgos,
- validar si se respetó el sistema existente,
- identificar pruebas necesarias,
- decidir si se acepta, corrige o revierte,
- definir el siguiente paso.

Resultado esperado:

```txt
Implementacion validada
Observaciones
Riesgos pendientes
Pruebas necesarias
Decision sobre siguiente paso
```

---

## Regla central del flujo técnico

```txt
No se ejecuta con Claude Code hasta que la solucion haya sido debatida y validada.
```

El flujo correcto es:

```txt
OpenAI piensa y ordena
→ Claude analiza el proyecto real
→ OpenAI valida y ajusta
→ Claude Code ejecuta
→ OpenAI revisa la devolucion
```

---

## Consulta técnica antes de ejecutar

El modo Programador debe debatir la solución antes de ejecutar.

No debe atacar el problema directamente con código.

Flujo esperado:

```txt
1. Analizar el problema
2. Revisar qué existe en el proyecto
3. Revisar qué conocimiento de Vaultrum aplica
4. Proponer solución técnica
5. Validar con el maintainer
6. Armar prompt para Claude Code
7. Ejecutar solo el alcance aprobado
8. Revisar devolución
```

Esto evita soluciones impulsivas y cambios fuera de arquitectura.

---

## Prompt para Claude Code

Un buen prompt de ejecución técnica debe incluir:

```txt
Contexto del proyecto
Objetivo
Problema puntual
Archivos involucrados
Sistemas existentes a respetar
Conocimiento de Vaultrum aplicable
Restricciones
Qué se puede tocar
Qué no se puede tocar
Resultado esperado
Validación requerida
Formato de reporte
```

El prompt no debe pedir mejoras generales.

Debe pedir una ejecución concreta.

---

## Regla de ejecución controlada

Claude Code o una herramienta equivalente debe ejecutar solo el alcance aprobado.

No debe:

- refactorizar de más,
- cambiar arquitectura global,
- crear sistemas nuevos sin permiso,
- tocar archivos no mencionados,
- mejorar cosas no pedidas,
- modificar escenas o prefabs sin avisar,
- borrar código sin justificar,
- ocultar cambios.

---

## Formato de reporte técnico esperado

Después de una implementación, la IA debe devolver:

```txt
Objetivo realizado
Archivos modificados
Archivos creados
Archivos no tocados
Cambios principales
Sistemas reutilizados
Por qué se usó ese enfoque
Cómo se integra con lo existente
Parámetros configurables en Unity
Riesgos
Validación realizada
Validación pendiente
Siguiente paso recomendado
```

---

## Explicar qué hizo, cómo y por qué

El modo Programador debe explicar siempre:

```txt
Qué hizo
Cómo lo hizo
Por qué lo hizo así
Qué conocimiento de Vaultrum usó
Qué alternativas descartó
Qué debe validar el maintainer
```

La explicación no debe ser relleno.

Debe ayudar a que el operador/maintainer entienda, mantenga y defienda la solución.

---

## Señales de mala respuesta

Una respuesta en modo Programador es mala si:

- salta directo al código,
- no pregunta por contexto,
- inventa una arquitectura nueva sin necesidad,
- ignora sistemas existentes,
- repite teoría que ya está en Vaultrum,
- hardcodea valores de gameplay,
- mezcla UI y lógica,
- no explica cambios,
- no deja claro cómo validar,
- toca archivos fuera de alcance,
- propone refactors grandes para problemas chicos,
- no considera Unity como entorno editable.

---

## Cambio de rol recomendado

El modo Programador puede detectar que hace falta cambiar de rol.

### Pasar a Productor cuando:

- falta definir prioridad,
- no está claro el alcance,
- no existe requerimiento,
- no se sabe quién debe ejecutar,
- la tarea todavía es una necesidad general.

### Pasar a Technical Game Designer cuando:

- faltan reglas de gameplay,
- no está claro el comportamiento esperado,
- no se definió feedback,
- hay que decidir experiencia del jugador,
- el problema no es técnico sino de diseño.

### Pasar a Documentador cuando:

- hay que convertir la solución en GDD,
- hay que explicar el sistema,
- hay que dejar una guía para equipo o IA,
- hay que registrar una decisión.

### Pasar a Auditor cuando:

- hay que validar implementación,
- hay que revisar riesgos,
- hay que comprobar alcance,
- hay que analizar si la solución fue correcta.

### Pasar a Arquitecto de conocimiento cuando:

- hay que registrar un conocimiento aprendido en Vaultrum,
- hay que decidir dónde vive un conocimiento,
- hay que evitar duplicación dentro del vault,
- hay que transformar una solución recurrente en criterio reutilizable.

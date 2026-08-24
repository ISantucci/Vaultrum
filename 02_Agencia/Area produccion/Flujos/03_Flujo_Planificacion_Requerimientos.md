## Propósito

El Flujo de Planificación y Requerimientos transforma una estructura operativa ya ordenada en una salida formal del Área de Producción.

Su función es convertir una idea bajada a tierra en:

- un timeline principal,
- uno o más requerimientos asociados.

El flujo no ejecuta el trabajo.

El flujo no deriva técnicamente la solución.

El flujo cierra la **apertura** del hilo dejando una planificación registrable, numerada y entendible. No cierra la intervención del área: Producción vuelve al final, con el [[04_Flujo_Validacion_Entrega]], a validar que lo entregado sea lo planificado.

---

## Entrada del flujo

Este flujo recibe una idea ya bajada a tierra.

La entrada debería traer, aunque sea de forma parcial:

- objetivo concreto,
- alcance inicial,
- alcance futuro,
- fuera de alcance,
- bloques principales de trabajo,
- dependencias,
- riesgos operativos,
- información faltante, si existe,
- área probablemente afectada,
- base para planificación.

Si la entrada todavía no tiene alcance claro o mezcla alcance inicial con futuro, no debería avanzar.

---

## Transformación que realiza

El flujo debe transformar una base operativa en una planificación registrable.

Para eso debe:

- definir el objetivo general del timeline,
- identificar el área afectada,
- definir la criticidad general,
- dividir el trabajo en requerimientos concretos,
- ordenar la secuencia de trabajo,
- estimar tiempos realistas por etapa,
- identificar dependencias,
- declarar riesgos,
- definir criterios de cierre,
- verificar la numeración disponible antes de generar la salida.

---

## Verificación previa de numeración

Antes de generar una nueva salida, se debe verificar el próximo número disponible.

La verificación debe hacerse revisando:

- [[00_Indice_salidas]]
- [[00_Indice_timelines]]
- [[00_indice_requerimientos]]

La numeración debe mantener relación entre timeline y requerimientos.

Ejemplo:

TL-001  
RQ-001.1  
RQ-001.2  
RQ-001.3

El número base pertenece al timeline.

Los requerimientos asociados usan el mismo número base y agregan subnumeración.

Si el último timeline registrado es TL-004, la nueva salida debe comenzar como TL-005.

Si no existe ningun timeline registrado, la primera salida debe comenzar como TL-001.

Los requerimientos asociados deben comenzar como:

RQ-005.1  
RQ-005.2  
RQ-005.3

No se debe inventar numeración sin revisar los índices.

---

## Timeline

El timeline representa la planificación general.

Debe ordenar:

- qué se busca lograr,
- qué área se ve afectada,
- cuál es la criticidad,
- qué requerimientos lo concretan,
- en qué orden conviene avanzar,
- cuánto tiempo puede tomar cada etapa,
- qué dependencias existen,
- qué riesgos pueden afectar el avance,
- cuándo puede considerarse cerrado.

Formato obligatorio del timeline:

- Objetivo
- Área afectada
- Criticidad
- Requerimientos asociados
- Secuencia de trabajo
- Dependencias
- Riesgos
- Criterios de cierre

El timeline debe incluir links a los requerimientos asociados.

Ejemplo:

```md
- [[RQ-001.1_Paletas_Controlables]]
- [[RQ-001.2_Pelota_Rebote_Aceleracion]]
- [[RQ-001.3_Score_Victoria]]
```

---

## Requerimientos asociados

Los requerimientos representan las unidades concretas que materializan el timeline.

Un timeline puede tener uno o varios requerimientos asociados.

Un requerimiento debe pertenecer a un timeline.

Formato obligatorio de cada requerimiento:

- Título
- Área afectada
- Criticidad
- Descripción
- Subtasks

Cada requerimiento debe ser claro, accionable y suficientemente concreto para que pueda ser tomado como unidad de trabajo.

Los requerimientos no deben definir implementación técnica final si eso corresponde a otra área.

---

## Registro de salida

Cuando el flujo queda cerrado, la planificación debe registrarse dentro de 00_Indice_Salidas.

La salida debe generar:

- un timeline principal en la carpeta Timelines,
- uno o más requerimientos asociados en la carpeta Requerimientos.

El índice de Salidas debe conectar con:

- 00_Indice_Timelines
- 00_Indice_Requerimientos

El timeline debe quedar registrado en el índice de timelines.

Los requerimientos deben quedar registrados en el índice de requerimientos.

La numeración debe respetar la relación entre timeline y requerimientos.

Ejemplo:

TL-001 - Consolidar Salidas del Área de Producción  
RQ-001.1 - Crear estructura de Salidas  
RQ-001.2 - Crear índices de Salidas  
RQ-001.3 - Ajustar Flujo de Planificación y Requerimientos

---

## Salida esperada

La salida del flujo debe dejar el trabajo expresado como timeline y requerimientos asociados.

Debe incluir:

- número base de salida,
- timeline principal,
- requerimientos asociados,
- objetivo,
- área afectada,
- criticidad,
- alcance,
- fuera de alcance,
- secuencia de trabajo,
- tiempos estimados,
- prioridades,
- dependencias,
- riesgos,
- criterios de cierre.

La salida debe poder registrarse como archivos dentro de Salidas.

---

## Formato de salida

Número base de salida:  
TL-XXX / RQ-XXX.X

Timeline a crear:  
Nombre del timeline principal.

Requerimientos a crear:  
Lista de requerimientos asociados.

Objetivo:  
Resultado que se busca alcanzar.

Área afectada:  
Área principal afectada por la planificación.

Criticidad:  
Alta / Media / Baja.

Alcance:  
Qué entra dentro de esta planificación.

Fuera de alcance:  
Qué no debe resolverse en esta etapa.

Secuencia de trabajo:  
Orden sugerido de avance por etapas.

Tiempos estimados:  
Estimación realista por etapa o bloque de trabajo.

Prioridades:  
Orden de importancia o secuencia sugerida.

Dependencias:  
Condiciones, decisiones, documentos, áreas o recursos necesarios.

Riesgos:  
Factores que pueden afectar alcance, tiempo, calidad o ejecución.

Criterios de cierre:  
Condiciones que deben cumplirse para considerar cerrado el timeline.

Registro sugerido:  
Archivos que deberian crearse o actualizarse, incluyendo timeline, requerimientos asociados e indices correspondientes.

---

## Criterios de aceptación

El flujo puede darse por cerrado cuando:

- el objetivo está explícito,
- el alcance está definido,
- el fuera de alcance está declarado cuando corresponde,
- se verificó el próximo número disponible en los índices de salida,
- se definió el timeline principal que debe crearse,
- se definieron los requerimientos asociados,
- cada requerimiento respeta el formato obligatorio,
- cada requerimiento quedó asociado al timeline correspondiente,
- la secuencia de trabajo está ordenada,
- los tiempos estimados son realistas o la incertidumbre fue declarada,
- las prioridades están claras,
- las dependencias principales están visibles,
- los riesgos principales fueron registrados,
- existen criterios de cierre,
- la salida puede registrarse en Salidas sin reinterpretar desde cero.

Si estos puntos no pueden cumplirse por falta de información, el flujo debe cerrarse como pausado y declarar qué falta para poder planificar.

---

## Condiciones para cerrar la planificación

La planificación puede darse por cerrada —y el hilo pasar a las demás áreas— cuando:

- la idea fue transformada en timeline y requerimientos asociados,
- el trabajo tiene alcance y límites claros,
- existe una prioridad o secuencia razonable,
- hay tiempos estimados o incertidumbre visible,
- la numeracion de salida está definida,
- los requerimientos concretan el timeline,
- la salida puede registrarse en los índices correspondientes.

Cerrar la planificación **no cierra el trabajo del área**: el timeline vuelve a Producción al final para su validación de entrega (`VE`).

La planificación no debe cerrarse si:

- el objetivo sigue ambiguo,
- el alcance todavía está mezclado,
- las dependencias críticas no fueron identificadas,
- no hay criterios de cierre,
- no está claro qué requerimientos concretan el timeline,
- el timeline no tiene requerimientos asociados,
- los requerimientos no pertenecen a ningún timeline,
- el requerimiento todavia necesita decisiones estratégicas u operativas previas.

---

## Qué debe evitar este flujo

Este flujo no debe ejecutar el requerimiento.

No debe resolver implementación técnica.  
No debe definir arquitectura de código.  
No debe diseñar gameplay en profundidad.  
No debe convertir deseos futuros en tareas inmediatas.  
No debe prometer fechas sin información suficiente.  
No debe ocultar riesgos para que el timeline parezca más prolijo.  
No debe generar requerimientos sin timeline asociado.  
No debe generar timeline sin requerimientos concretos.  
No debe inventar numeración sin revisar los índices.  
No debe crear una carpeta de derivación en esta etapa.

---
## Checklist de cierre

Antes de cerrar el flujo, se debe verificar que:

- se reviso el ultimo timeline registrado,
- se definio el numero base de salida,
- se definieron los requerimientos asociados,
- se creo o propuso el timeline principal,
- se crearon o propusieron los requerimientos asociados,
- el timeline incluye links a sus requerimientos,
- el indice de timelines fue actualizado o indicado para actualizacion,
- el indice de requerimientos fue actualizado o indicado para actualizacion. 
  
  ---
## Resultado final

El resultado final del Flujo de Planificación y Requerimientos debe ser una salida formal del Área de Producción.

Esa salida debe estar compuesta por:

- un timeline principal,
- uno o más requerimientos asociados.

Es la salida de **apertura** del hilo. La salida de cierre (`VE`) la produce el [[04_Flujo_Validacion_Entrega]] cuando la entrega vuelve.

El timeline ordena la planificación general.

Los requerimientos concretan las unidades de trabajo necesarias para cumplir esa planificación.

El flujo termina cuando la idea deja de ser intención y pasa a ser salida productiva registrable.
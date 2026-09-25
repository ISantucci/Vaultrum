## Que es

Como se comparan grupos de jugadores sin enganarse, y como se prueba un cambio para poder decir que **causo** algo.

---

## Segmentos

Un segmento es un subconjunto de usuarios por atributo o comportamiento. Se segmenta **cuando tiene sentido para la pregunta**, no por costumbre:

```txt
nuevos vs recurrentes · pagador o no · gasto bajo / medio / alto · antiguedad
· progresion · habilidad · canal de adquisicion · organico vs pago · plataforma
· version · region (cuando es legal y relevante) · adopcion de una feature
· cohorte de experimento
```

No se crean segmentos con atributos sensibles sin una necesidad legitima y legal.

---

## Cohortes

Una cohorte agrupa jugadores por una caracteristica comun. El uso clasico: **los que empezaron el mismo dia**.

Sirve para retencion, comparacion entre versiones, calidad de adquisicion, analisis de experimentos y maduracion de la monetizacion. Comparar el D7 de la cohorte que entro con la version 1.2 contra la de la 1.3 es la forma mas simple de ver si una version cambio algo.

---

## El promedio miente en distribuciones sesgadas

Un ARPPU promedio de $50 puede salir de:

```txt
todos pagando cerca de $50
pocos gastando mucho y muchos gastando poco
```

Son dos productos distintos con el mismo numero. Cuando la distribucion es sesgada —gasto, tiempo jugado, saldos— se mira la **mediana**, los **percentiles**, el **histograma** y los **tramos de gasto**.

---

## Experimentos

La hipotesis se escribe entera, antes:

```txt
Si hacemos X para la poblacion Y, esperamos cambiar el comportamiento Z,
medido por el KPI K, sin degradar los guardrails G.
```

Y se definen, tambien antes:

```txt
control · tratamiento · elegibilidad · asignacion aleatoria · KPI primario
· metricas secundarias · guardrails · duracion · muestra · criterio de rollout
```

Lo que invalida un experimento:

```txt
cambiar el KPI despues de ver los resultados      metric shopping
cortarlo antes de tiempo porque "ya dio"
mezclar versiones
exponer jugadores de forma inconsistente
declarar causalidad con un antes/despues sin mirar confounders
```

El primero es el mas comun y el mas dificil de ver desde adentro: con suficientes metricas secundarias, alguna siempre "da positiva". **El KPI primario se congela antes del dato**, igual que una build se congela antes del pase de verificacion.

---

## Live Ops: medir un evento

Para cada evento en vivo se registra:

```txt
hipotesis · poblacion elegible · exposicion · participacion · completion
· engagement incremental · revenue incremental · retencion · reactivacion · guardrails
```

Y se compara:

```txt
antes vs durante
expuestos vs no expuestos, cuando la comparacion es valida
este evento vs eventos anteriores
```

Los confounders que hay que nombrar siempre: releases, campanas, feriados, caidas de servicio y cambios de balance. Un evento que coincidio con un feriado no demostro nada hasta que se descuenta el feriado.

---

## Regla final

```txt
Comparar es facil. Comparar grupos comparables es el trabajo.

Y un experimento que decide su KPI despues de mirar
no es un experimento: es una busqueda de la conclusion que ya se tenia.
```

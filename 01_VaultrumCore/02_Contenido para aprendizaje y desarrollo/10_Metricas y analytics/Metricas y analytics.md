## Proposito

Esta seccion reune el conocimiento durable sobre **metricas de producto en videojuegos**: como se elige que medir, como se define una metrica para que dos personas lean lo mismo, que se instrumenta y que no, y como se pasa de un numero a una decision sin inventar causas.

No es la seccion que dice como se mide un proyecto concreto. Eso es operativo, cambia por proyecto, por fase y por plataforma, y vive en el Area de Metricas de la Agencia.

```txt
el Core   ensena el criterio          que es un KPI, que lo define, que puede afirmar un dato
el Area   ejecuta el procedimiento    con que plan, sobre que eventos, contra que baseline, quien decide
```

La funcion entera se lee en una cadena:

```txt
objetivo -> comportamiento esperado -> KPI -> instrumentacion -> datos
         -> diagnostico -> decision o experimento -> nueva medicion
```

Si falta el primer eslabon, todo lo que sigue es un tablero de numeros.

---

## Por que existe

Porque el resto del Core sabe **construir** y sabe **verificar**, y no sabia **aprender del jugador**.

`Calidad y testing` responde si lo construido hace lo que dice hacer. `Criterios de entrega` responde cuanto alcanza. Ninguna responde la pregunta que aparece cuando alguien juega:

```txt
El jugador real se comporta como esperaba el diseno?
Y si no, donde se separa, y que evidencia hace falta para decidir que cambiar?
```

Esa pregunta tiene un cuerpo de conocimiento propio —game analytics y product analytics— con vocabulario preciso, formulas que cambian de significado segun el denominador, y errores caros que se repiten en toda la industria. Sin el, cada lectura de datos se improvisa y cada numero se interpreta a favor de quien lo mira.

---

## Que NO es esta seccion

**No es QA.** Una metrica de calidad dice si el sistema falla. Una metrica de producto dice que hace la gente con un sistema que funciona. `Cobertura y metricas`, en `Calidad y testing`, habla de la primera; esta seccion, de la segunda.

**No es playtesting.** El playtest es un instrumento de medicion con protocolo propio, y su dueno es el libro `13_Playtesting_y_validacion` de la Biblioteca: tipos de test, preguntas prohibidas, sesgos, y el **tope de diez eventos** para un dev solo. Esta seccion no lo repite ni lo pisa: lo usa como el presupuesto de telemetria de las fases donde rige el playtest.

**No es diseno de economia, progresion ni onboarding.** Como se disena una economia vive en `07_Economia_y_balance`; una curva de progresion, en `08_Progresion_y_recompensa`; un tutorial, en `09_Onboarding_y_tutorial`. Esta seccion dice **como se mide** lo que esos libros ensenan a construir.

**No es una lista de KPIs.** Una lista de KPIs sin objetivo es la forma mas cara de no decidir nada.

---

## [[Objetivo antes que metrica]]

El principio del que salen todos los demas: primero el objetivo, despues el comportamiento, recien despues la metrica. Metrica contra KPI, el arbol de metricas, los guardrails, por que ninguna metrica es buena o mala sin contexto, y las preguntas que se reconstruyen antes de elegir nada.

Usar esta nota ante cualquier pedido que empiece por "que KPI ponemos" o "hay que subir X".

---

## [[Fases del producto y que medir]]

Que pregunta hace cada fase —Planning, Pre-Production, Production, Testing, Pre-Launch, Launch, Post-Launch, Live Ops— y que se mide en cada una. Los modelos de negocio, y por que modelo de negocio no es lo mismo que estrategia de monetizacion.

Usar esta nota antes de proponer una metrica: la fase decide si tiene sentido medirla.

---

## [[Player Journey y funnels]]

El funnel de etapas del jugador —de quien conoce el juego a quien lo recomienda—, la adquisicion, el FTUE y el drop-off. Y la regla de diagnostico que evita atacar la ultima etapa solo porque su numero es el mas chico.

Usar esta nota cuando la pregunta sea "donde se pierde la gente".

---

## [[Retencion y engagement]]

Actividad, retencion y engagement: tres cosas que se confunden y miden cosas distintas. Dn clasica contra rolling, churn, reactivacion, stickiness, y los sistemas de retorno —login diario, quests, battle pass— con sus riesgos medibles.

Usar esta nota cuando la pregunta sea "vuelven" o "cuanto juegan".

---

## [[Progresion y features]]

Como se mide un nivel, un sistema o una feature: start, fail, complete, intentos, tiempo y drop-off; y para una feature, descubrimiento, adopcion, frecuencia, profundidad, retencion de uso, resultado e impacto. Incluye ejemplos de feature a KPI.

Usar esta nota cuando se quiera saber si algo que se construyo esta funcionando.

---

## [[Monetizacion y suscripcion]]

Revenue, conversion, ARPU, ARPAU, ARPPU, ARPDAU, LTV y la relacion entre los tres primeros. Puntos porcentuales contra porcentaje relativo, descuentos y elasticidad, y las metricas de suscripcion: MRR y sus componentes.

Usar esta nota antes de poner un numero de ingresos en un informe.

---

## [[Economia virtual medida]]

Sources, sinks, flujo neto, distribucion de saldos, tiempo hasta poder pagar algo, acaparamiento. Y por que mirar solo el gasto engana.

Usar esta nota cuando haya una moneda o un recurso que se gana y se gasta.

---

## [[Instrumentacion y telemetria]]

Que eventos existen, como se nombran, que contexto llevan, que es la cardinalidad y por que duele, cuando validar del lado del servidor, como se verifica un evento antes de creerle a un tablero, y privacidad por diseno. El principio de minima instrumentacion suficiente.

Usar esta nota antes de pedirle a Programacion un solo evento.

---

## [[Segmentos, cohortes y experimentos]]

Cuando segmentar, que es una cohorte, por que el promedio miente en distribuciones sesgadas, como se escribe una hipotesis de experimento y que no hay que hacer con un A/B. Incluye la medicion de un evento de Live Ops.

Usar esta nota cuando haya que comparar grupos o probar un cambio.

---

## [[Del dato a la decision]]

Hecho, interpretacion, hipotesis y recomendacion, separados. Los anti-patrones que mas cuestan, el modelo mental de salud del producto, los tableros minimos y el registro canonico de metricas.

Usar esta nota antes de cerrar cualquier analisis.

---

## [[Formulas base y glosario]]

Las formulas canonicas y las siglas, en un solo lugar, con la advertencia que las acompana: una sigla no alcanza, lo que define una metrica es su denominador, su ventana y su fuente.

Usar esta nota como referencia, no como punto de partida.

---

## Como se relacionan

```txt
que quiero lograr y que mido        -> Objetivo antes que metrica
que tiene sentido medir hoy         -> Fases del producto y que medir
donde se pierde la gente            -> Player Journey y funnels
vuelven? cuanto juegan?             -> Retencion y engagement
funciona lo que construi?           -> Progresion y features
pagan? cuanto?                      -> Monetizacion y suscripcion
la economia sostiene valor?         -> Economia virtual medida
que eventos pido y como             -> Instrumentacion y telemetria
comparo grupos o pruebo un cambio   -> Segmentos, cohortes y experimentos
que puedo afirmar al cerrar         -> Del dato a la decision
como se calcula exactamente         -> Formulas base y glosario
```

---

## Relacion con la Agencia

La Agencia **aplica** este criterio; no lo define.

```txt
Objetivo antes que metrica          -> Area de Metricas (plan de medicion) y Produccion (el objetivo)
Fases del producto                  -> Produccion (declara la fase) y Area de Metricas (la respeta)
Player Journey, retencion, features -> Area de Metricas (lectura) y Game Design (interpreta el diseno)
Monetizacion y economia             -> Area de Metricas (mide) y Game Design (disena y balancea)
Instrumentacion y telemetria        -> Area de Metricas (tracking plan), Programacion (implementa)
                                       y Control de Calidad (verifica que el evento dispare bien)
Segmentos y experimentos            -> Area de Metricas (diseno y lectura) y Produccion (decide)
Del dato a la decision              -> Area de Metricas (informe) y Produccion (el VE)
```

Si una skill y esta seccion divergen, la seccion es el criterio y la skill es el procedimiento: se corrige la skill.

---

## Regla de esta seccion

Una nota entra aca si responde **como se sabe si el producto produce el comportamiento esperado**, no como se construye, no como se verifica que no falle y no como se decide el alcance.

Y si lo que dice sobrevive a la pregunta de siempre:

```txt
Sirve para decidir que hacer manana con un producto real,
o solo para saber como se llama lo que ya se miraba?
```

El area de metricas existe para mejorar decisiones, no para producir numeros.

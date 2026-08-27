## Definicion

Optimizar sin un requerimiento de rendimiento detras es **alcance no pedido**.

La regla no es "no optimices". Es:

```txt
No enciendas maquinaria que ningun requerimiento pidio
— y eso incluye la maquinaria propia.
```

Medir antes de optimizar responde con que evidencia se optimiza. Esta nota responde una pregunta anterior: si corresponde optimizar.

Las dos se pueden fallar por separado. Se puede optimizar con medicion impecable un sistema que nadie necesitaba que fuera rapido.

---

## Responsabilidad de esta nota

Esta nota existe para separar dos cosas que se confunden:

```txt
optimizacion prematura   = optimizar sin medir
optimizacion no pedida   = optimizar sin encargo
```

La primera es un error de metodo: se puede corregir midiendo. La segunda es un error de alcance: **medir no la corrige**. Se puede medir perfecto y seguir resolviendo un problema que nadie tenia.

El Core ya cubria la primera. Esta nota cubre la segunda.

---

## Que problema ayuda a entender

El problema es que el trabajo tecnico de calidad **se ve igual** este pedido o no.

Un sistema con cero asignaciones por frame, un solo punto de actualizacion y deteccion de colision continua propia es indistinguible de otro igual, salvo por una cosa: si alguien lo pidio.

Y el costo no es cero:

- consume el presupuesto que iba a la experiencia;
- agrega superficie de mantenimiento que nadie va a necesitar;
- se defiende sola en una revision tecnica, asi que nadie la cuestiona;
- desplaza discusiones sobre lo que el entregable si necesitaba.

**Caso real.** Una corrida tecnica de un Pong local hecha fuera de un flujo con requerimientos produjo ocho decisiones de ingenieria: loop con accumulator a 120 Hz e interpolacion, deteccion continua propia, cero asignaciones, un solo punto de actualizacion, batching y culling ajustados. Veinte objetos en pantalla, dos jugadores en el mismo teclado, nadie habia pedido rendimiento ni determinismo.

Ese build no tenia menu, ni condicion de fin declarada, ni forma de volver a jugar. Las ocho decisiones eran correctas y ninguna respondia a un pedido.

---

## Como funciona

La misma decision tecnica puede ser correcta o ser alcance no pedido segun **contra que se justifique**.

```txt
DECISION: no usar el motor de fisica en un Pong

justificacion A: el rebote de Pong no es fisico — el angulo de salida
                 sale del punto de impacto en la paleta, no de la
                 conservacion del momento
                 → correcto. Lo pide una regla de diseno.

justificacion B: la broadphase del motor de fisica cuesta
                 → alcance no pedido. Nadie pidio rendimiento.
```

```txt
DECISION: un solo punto de actualizacion

justificacion A: el efecto de spin lee la velocidad de la paleta en el
                 instante del golpe, y el orden no puede depender del
                 execution order del motor
                 → correcto. Lo pide el diseno.

justificacion B: ahorra saltos managed/native
                 → alcance no pedido.
```

Mismo codigo. Distinta justificacion. Solo una de las dos se sostiene frente a quien encargo el trabajo.

Esto tiene una consecuencia contraintuitiva: **una optimizacion puede ser correcta por el motivo equivocado**, y eso importa. Cuando el proyecto crezca y alguien tenga que decidir si mantener esa decision, la justificacion es lo unico que va a quedar escrito.

---

## Como aplicarlo

Por cada decision tecnica, escribir la linea:

```txt
esto existe porque el requerimiento X pide Y
```

La que no la tenga tiene dos salidas legitimas:

1. **Se declara como deuda**, con su motivo. "Esto se hizo asi por costumbre; si molesta, se cambia."
2. **No se hace.**

La tercera —hacerla y no declararla— es la que produce el problema.

La forma practica es una tabla de dos columnas en la solucion tecnica:

```txt
LO QUE SE HIZO                        POR QUE (requerimiento)
sin motor de fisica                   RQ-XXX.3: el rebote sale del punto de impacto
un solo punto de actualizacion        RQ-XXX.3: el spin lee la paleta en el golpe
substepping en el movimiento          RQ-XXX.3: la pelota nunca atraviesa nada

LO QUE DELIBERADAMENTE NO SE HIZO     POR QUE NO
pooling de objetos                    no hay instanciacion en runtime
loop con accumulator fijo             nadie pidio determinismo
batching / culling manual             veinte objetos, sin sintoma medido
compresion de assets                  el build no tiene restriccion de tamano
```

**La segunda tabla es la que suele faltar.** Es la que demuestra que hubo criterio y no olvido, y la que evita que la proxima persona repita el analisis desde cero.

---

## Cuando SI corresponde optimizar

La regla no aplica cuando existe encargo. Existe encargo cuando:

- hay un requerimiento explicito de rendimiento, memoria, tiempo de carga o consumo;
- hay un sintoma medido en el proyecto real (ver `Medir antes de optimizar`);
- la plataforma de destino impone una restriccion conocida y declarada;
- una *table-stake* del entregable exige la maquinaria. Si el juego exige que la pelota nunca atraviese una pared, la continuidad de colision **tiene** requerimiento detras: la table-stake es el requerimiento.

El ultimo caso es el que mas se confunde con alcance no pedido y no lo es. La prueba sigue siendo la misma: se puede escribir la linea *"esto existe porque el requerimiento X pide Y"*.

---

## Errores que ayuda a evitar

- Justificar decisiones tecnicas contra principios ("es mas performante", "es mas limpio") en vez de contra pedidos.
- Entregar un sistema tecnicamente impecable que no responde lo que se queria.
- Confundir *no hay sintoma medido* con *todavia no medi*.
- Escribir solo la columna de lo que se hizo.
- Tratar la ausencia de optimizacion como descuido, cuando es una decision declarada.

---

## Riesgos de interpretarlo mal

Esta nota **no** dice:

- que no haya que optimizar — dice que la optimizacion necesita encargo;
- que haya que escribir codigo descuidado — la calidad base no es maquinaria, es oficio;
- que no se pueda proponer una optimizacion — se puede, y se declara como propuesta, no se ejecuta;
- que las decisiones de arquitectura no cuenten — cuentan igual, y la regla se les aplica igual.

Confundirla con "escribi cualquier cosa que despues se ve" es el error inverso, y produce entregas que hay que rehacer.

---

## Relacion con el resto del Core

Es la mitad tecnica de un criterio mas grande: ver `Baseline de entregable`.

```txt
completo en experiencia   → trae sin pedirlo lo que el entregable necesita
minimo en maquinaria      → no trae sin pedirlo lo que nadie necesita
```

Esta nota desarrolla la segunda mitad aplicada a rendimiento. Las dos se rompen por separado y la mayoria de las entregas malas rompen las dos a la vez: sobran motores y falta menu.

---

## Checklist antes de optimizar

```txt
[ ] Existe un requerimiento de rendimiento, memoria o carga?
[ ] O existe un sintoma medido en el proyecto real?
[ ] O una table-stake del entregable exige esta maquinaria?
[ ] Puedo escribir "esto existe porque el requerimiento X pide Y"?
[ ] Si la respuesta a todas es no: lo declaro como deuda o no lo hago?
[ ] Escribi la columna de lo que deliberadamente no hice?
```

---

## Regla final

```txt
Optimizacion prematura = optimizar sin medir.
Optimizacion no pedida = optimizar sin encargo.
Medir corrige la primera. No corrige la segunda.
```

Trabajo de calidad sin encargo sigue siendo trabajo que nadie pidio.

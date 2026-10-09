## Proposito

Esta rama reune los conceptos base necesarios para entender optimizacion antes de diagnosticar o proponer soluciones.

No existe para acumular definiciones.
No existe para explicar tecnicas concretas.
No existe para resolver un sintoma puntual.

Existe para que, cuando aparezca un problema de rendimiento, ya se tenga el marco con el que pensarlo.

---

## Idea central

Casi todos los errores de optimizacion no son errores de tecnica: son errores de marco.

```txt
optimizar sin saber cuanto tiempo hay por frame
mirar el promedio y no la estabilidad
atacar lo que parece lento en vez de lo que limita
acelerar trabajo que no tendria que ejecutarse
ganar en un recurso sin ver que se gasto en otro
romper el feedback del jugador para bajar un numero
```

Esta rama existe para que ninguno de esos seis sea posible.

---

## Cuando usar esta rama

Usar Fundamentos cuando:

```txt
todavia no esta claro que esta pasando
hay que decidir si algo es caro o barato
hay que justificar por que se optimiza esto y no aquello
hay que explicar un trade-off
hay que frenar una optimizacion que nadie pidio
```

No hace falta leerla entera cada vez. Se consulta la nota que corresponde al hueco de criterio.

---

## Como debe usar esta rama una IA

Una IA debe apoyarse en Fundamentos para justificar una decision, no para adornar una propuesta.

Antes de recomendar algo, debe poder responder:

```txt
¿Cual es el objetivo de FPS y cuanto es el presupuesto por frame?
¿El problema es el promedio o son los spikes?
¿Que recurso esta implicado?
¿Cual es el costo unitario, la cantidad y la frecuencia?
¿Se puede eliminar el trabajo en vez de acelerarlo?
¿Que se gasta al ganar esto?
¿Lo pidio alguien?
```

Si no puede responderlas, todavia no esta en condiciones de proponer una solucion.

---

## Notas incluidas

### [[Frame Budget]]

Explica cuanto tiempo tiene disponible cada frame segun el objetivo de FPS, y como ese presupuesto se reparte entre los sistemas que corren dentro del frame.

Consultar cuando haya que decidir si un costo es aceptable o cuando haya que repartir el frame entre sistemas.

### [[Frame time y estabilidad]]

Explica por que la unidad util es el tiempo por frame y no los FPS, y por que un promedio sano puede esconder una experiencia mala.

Consultar cuando haya stutter, spikes o caidas puntuales aunque el promedio parezca correcto.

### [[Recursos de hardware]]

Explica que hace cada recurso durante la ejecucion y que problemas tipicos genera cada uno.

Consultar cuando haya que traducir un sintoma a un recurso posiblemente afectado.

### [[Bottleneck]]

Explica que es el cuello de botella y por que no existe la optimizacion del juego en abstracto, sino la del recurso que limita.

Consultar cuando haya que decidir donde vale la pena trabajar.

### [[Game loop]]

Explica el ciclo de ejecucion y como cada subsistema consume una porcion del presupuesto del frame.

Consultar cuando haya que ubicar donde ocurre un costo dentro del frame.

### [[Costo cantidad y frecuencia]]

Explica la ecuacion que aparece en casi todos los problemas de performance: costo unitario por cantidad por frecuencia.

Consultar cuando haya que estimar un costo antes de medirlo, o cuando una operacion parezca insignificante de a una.

### [[Reducir trabajo antes que acelerarlo]]

Explica las seis preguntas que hay que hacerse antes de intentar hacer algo mas rapido, y la jerarquia que sale de ellas.

Consultar antes de cualquier optimizacion. Es el principio ordenador de toda la seccion.

### [[Trade-offs de optimizacion]]

Explica que toda optimizacion intercambia un recurso por otro, y cuales son los intercambios habituales.

Consultar al evaluar una solucion candidata y antes de declarar que una optimizacion termino.

### [[Valor perceptual por costo]]

Explica como comparar el costo computacional de un sistema contra lo que ese sistema le aporta al jugador.

Consultar cuando la solucion facil sea eliminar algo que el jugador si estaba percibiendo.

### [[Cuando NO optimizar]]

Explica la diferencia entre optimizacion prematura y alcance no pedido, y como se declara una omision deliberada.

Consultar antes de abrir cualquier trabajo de optimizacion: primero se decide si corresponde, despues con que evidencia.

### [[Medir antes de optimizar]]

Explica por que hace falta evidencia antes del cambio y como se arma una medicion que sirva.

Consultar cuando ya se decidio que corresponde optimizar y hay que conseguir el dato.

### [[Errores conceptuales frecuentes]]

Explica los mitos que circulan como si fueran criterio y cual es la formulacion correcta de cada uno.

Consultar cuando alguien afirme que una API, una construccion del lenguaje o una metrica es mala en si misma.

---

## Como se conecta con otras ramas

```txt
Fundamentos
→ da el marco

Diagnostico
→ decide a que rama entrar

CPU / GPU / Memoria / Carga e IO / UI
→ resuelven el problema del recurso

Patrones transversales
→ lo que reaparece en mas de una rama
```

Fundamentos no resuelve sintomas concretos. Si aparece uno, el camino sigue por `Diagnostico`.

---

## Criterio de crecimiento

Esta rama no debe crecer con problemas concretos, tecnicas ni herramientas.

Entra en Fundamentos lo que cumple las tres:

```txt
sirve para razonar antes de tocar nada
sigue siendo valido si cambia el motor
se usa desde mas de una rama
```

Un tema que solo aplica a un recurso pertenece a la rama de ese recurso, no aca.

---

## Regla final

Sin marco, la optimizacion es una opinion tecnica.

```txt
Marco
→ diagnostico
→ solucion
→ trade-off
→ validacion
```

Lo que no se puede explicar antes de medir, tampoco se va a poder defender despues.

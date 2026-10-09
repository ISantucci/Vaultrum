## Proposito

Esta seccion reune el conocimiento durable sobre **calidad y testing**: que es calidad, por que un defecto se escapa, que tecnicas existen para buscarlo, como se decide donde gastar el esfuerzo y que puede afirmar una prueba cuando termina.

No es la seccion que dice como se ejecuta un control de calidad en un proyecto. Eso es operativo, cambia por proyecto y por plataforma, y vive en el Area de Control de Calidad de la Agencia.

```txt
el Core   ensena el criterio      que es un defecto, que tecnica lo encuentra, que prueba una cobertura
el Area   ejecuta el procedimiento   con que planilla, contra que build, con que evidencia, quien decide
```

Un area que ejecuta sin criterio produce checklists. Un criterio sin area que lo ejecute produce documentos que nadie usa para decidir.

---

## Por que existe

Porque el resto del Core sabe **construir** y no sabia **verificar**.

SOLID, patrones, optimizacion, estructuras, algoritmos y managers responden *como se construye*. `Criterios de entrega` responde *cuanto alcanza*. Ninguno responde la pregunta del medio:

```txt
Como se comprueba que lo construido hace lo que dice hacer,
y que sigue haciendolo despues del proximo cambio?
```

Esa pregunta tiene un cuerpo de conocimiento propio, con casi cincuenta anos de bibliografia, vocabulario preciso y tecnicas que se pueden ensenar. Sin el, cada verificacion se improvisa y cada equipo reinventa un vocabulario distinto para las mismas cosas.

---

## Que NO es esta seccion

**No es la seccion de criterios de entrega.** `Criterios de entrega` define *que se le puede exigir a una entrega*. Esta define *como se comprueba*. Se necesitan las dos: una vara sin instrumento no mide, y un instrumento sin vara mide contra nada.

**No es playtesting.** Un test dice si el sistema hace lo que dice hacer. Un playtest dice si a una persona le divierte, si entiende y si vuelve. Son preguntas distintas, con metodos distintos, y confundirlas cuesta las dos respuestas.

**No es la calidad del codigo.** Que el codigo sea mantenible, extensible y sin hardcodeo es criterio de `Principios SOLID` y `Patrones de diseno`. Un sistema puede estar impecable por dentro y romperse a los treinta segundos de juego.

---

## [[Calidad, QA y testing]]

Las tres palabras que se usan como sinonimos y no lo son: **calidad** es una propiedad del producto, **QA** es el proceso que la cuida, **testing** es la actividad que produce informacion sobre ella.

Incluye ademas que hace **testeable** a un sistema, y por que la testabilidad es una decision de diseno y no una virtud que aparece sola.

Usar esta nota antes de discutir "calidad" con alguien: la mitad de esas discusiones son dos personas usando la misma palabra para dos cosas.

---

## [[Error, defecto y falla]]

La cadena que va de una persona equivocandose a un jugador viendo algo roto, y por que cada eslabon tiene nombre propio.

Incluye los principios del testing: por que una prueba nunca demuestra que no hay defectos, por que probarlo todo es imposible, por que los defectos se agrupan y por que un set de pruebas que siempre pasa deja de servir.

Usar esta nota cuando haya que explicar por que "no encontramos nada" no significa "esta bien".

---

## [[Niveles y tipos de prueba]]

Que se prueba y en que momento: estatico contra dinamico, unidad contra integracion contra sistema, funcional contra no funcional, y las dos pruebas que existen despues de un cambio — confirmar el arreglo y comprobar que no rompio nada.

Usar esta nota al decidir **que tipo de prueba** corresponde a lo que se acaba de construir.

---

## [[Tecnicas de diseno de pruebas]]

Como se eligen los casos cuando probar todo es imposible: particiones de equivalencia, valores limite, tablas de decision, transicion de estados, combinatoria por pares, caja blanca y exploratorio con charter.

Es la nota mas practica de la seccion: convierte "probemos el inventario" en una lista de casos con criterio.

Usar esta nota antes de escribir el primer caso de prueba.

---

## [[Testing basado en riesgo]]

Donde gastar el esfuerzo cuando no alcanza para todo. Riesgo como probabilidad por impacto, corregido por dificultad de deteccion y exposicion.

Incluye la distincion que mas se mezcla en la practica: **severity** es cuanto dana el defecto, **priority** es cuanto urge arreglarlo. No son la misma escala y no las decide la misma persona.

Usar esta nota cuando el tiempo de prueba sea menor que la superficie a probar, que es siempre.

---

## [[Cobertura y metricas]]

Que afirma exactamente una cobertura —que superficie se examino y con que enfoque— y que no afirma nunca: que no quedan defectos.

Incluye las metricas que sirven cuando tienen contexto y las que danan cuando se usan como objetivo.

Usar esta nota antes de poner un numero de calidad en un informe.

---

## [[Automatizacion de pruebas]]

Cuando automatizar mejora la verificacion y cuando solo mueve el costo de lugar. Que gana la maquina —velocidad, repetibilidad, precision, combinatoria— y que no puede ganar nunca: el juicio sobre si lo que ve esta bien.

Incluye la regla que mas se olvida: **un test automatico tambien es software y tambien puede estar roto.**

Usar esta nota antes de decidir que se automatiza, no despues de haber automatizado.

---

## [[Del defecto a la causa raiz]]

El ciclo de vida de un defecto: como se reporta para que otro pueda reproducirlo, quien decide su severidad y su urgencia, quien lo puede cerrar, y que se hace cuando el mismo tipo de falla vuelve a aparecer.

Usar esta nota al escribir un reporte de defecto, y al preguntarse por que un defecto grave llego tan lejos sin que nadie lo viera.

---

## [[Calidad en videojuegos]]

Que tiene de particular verificar un juego: estado continuo, tiempo real, input analogico, fisica, no determinismo, contenido masivo y un jugador que hace cosas que nadie diseno.

Incluye las dimensiones especificas —progresion, guardado, entrada, rendimiento, plataforma, accesibilidad, localizacion, red, economia— y las dos confusiones caras: playtesting no es QA, y que funcione en el editor no dice nada de la build.

Usar esta nota al verificar cualquier cosa jugable.

---

## Como se relacionan

```txt
que estoy verificando        → Calidad, QA y testing
por que se escapan defectos  → Error, defecto y falla
que tipo de prueba aplica    → Niveles y tipos de prueba
que casos escribo            → Tecnicas de diseno de pruebas
en que orden y hasta donde   → Testing basado en riesgo
que puedo afirmar al cerrar  → Cobertura y metricas
que le delego a la maquina   → Automatizacion de pruebas
que hago con lo que encontre → Del defecto a la causa raiz
que cambia si es un juego    → Calidad en videojuegos
```

---

## Relacion con la Agencia

La Agencia **aplica** este criterio; no lo define.

```txt
Calidad, QA y testing        → Area de Control de Calidad (intake, alcance del gate)
Error, defecto y falla       → Area de Control de Calidad (reporte y triage)
Niveles y tipos              → Area de Programacion (unidad e integracion) y Control de Calidad (sistema)
Tecnicas de diseno           → Area de Control de Calidad (diseno del pase)
Testing basado en riesgo     → Area de Control de Calidad (analisis de riesgo) y Produccion (prioridad)
Cobertura y metricas         → Area de Control de Calidad (informe y gate)
Automatizacion               → Area de Programacion (la escribe) y Control de Calidad (decide que entra)
Del defecto a la causa raiz  → Area de Control de Calidad (registro y RCA)
Calidad en videojuegos       → todas las areas que tocan algo jugable
```

Si una skill y esta seccion divergen, la seccion es el criterio y la skill es el procedimiento: se corrige la skill.

---

## Regla de esta seccion

Una nota entra aca si responde **como se comprueba algo**, no como se construye y no como se decide el alcance.

Y si lo que dice sobrevive a la pregunta de siempre:

```txt
Sirve para decidir que hacer manana con un sistema real,
o solo para saber como se llama lo que ya haciamos?
```

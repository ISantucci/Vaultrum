## Definicion

Broad phase y narrow phase es la division de una consulta cara en dos etapas de costo y precision distintos.

Primero una seleccion amplia y barata que puede equivocarse hacia el lado seguro.

Despues una validacion precisa y cara que solo corre sobre lo que sobrevivio.

```txt
Seleccion amplia y barata
↓
conjunto reducido
↓
validacion precisa y cara
```

La forma general del patron es:

```txt
cheap rejection
↓
cheap rejection
↓
expensive validation
```

La broad phase no necesita tener razon.

Necesita no perder candidatos validos y descartar rapido la mayor parte del resto.

```txt
Broad phase
→ puede dejar pasar falsos positivos
→ nunca deberia descartar un verdadero positivo

Narrow phase
→ resuelve la respuesta definitiva
```

El patron no pertenece a un recurso ni a un subsistema.

Aparece en fisica, en IA, en targeting, en colisiones, en consultas espaciales y en rendering.

---

## Que problema ayuda a prevenir

Ayuda con:

```txt
Validacion cara aplicada a todos los candidatos.
Comportamiento cercano a O(n²) en busquedas de vecinos.
Queries fisicas multiplicadas por cantidad de agentes.
Costo que explota al crecer la cantidad de entidades.
Spikes al aparecer muchas entidades juntas.
```

El problema tipico se ve asi:

```txt
Antes:
cada agente valida contra todos los candidatos.

Despues:
cada agente valida contra los pocos que la broad phase dejo pasar.
```

---

## Como funciona

La broad phase usa una aproximacion conservadora y barata.

```txt
Celda de grilla
Volumen envolvente
Distancia al cuadrado
Capa o categoria
Rango angular grueso
```

La narrow phase usa la representacion exacta.

```txt
Geometria real
Raycast
Interseccion precisa
Regla de gameplay completa
```

Entre las dos etapas hay una tercera cosa importante: el conjunto reducido.

```txt
Todos los candidatos
↓ broad phase
Conjunto reducido
↓ narrow phase
Resultado
```

La cascada de percepcion es un caso particular de este patron, no el patron.

```txt
Distancia
↓
Angulo
↓
Line of sight
```

Ese flujo salio del trabajo real con percepcion de IA y sirve como evidencia de que la forma funciona.

Pero la forma general no habla de agentes ni de vision: habla de reducir el conjunto antes de validarlo.

---

## Como aplicarlo en videojuegos

En fisica:

```txt
Broad phase
→ volumenes envolventes y capas

Narrow phase
→ interseccion de geometria real
```

En rendering:

```txt
Broad phase
→ frustum culling

Narrow phase
→ occlusion culling
```

Primero se descarta lo que ni siquiera esta en el volumen visible, y recien despues se paga la prueba de oclusion.

En consultas espaciales:

```txt
Broad phase
→ celda propia y celdas vecinas

Narrow phase
→ distancia real a cada candidato
```

Ejemplo en un Tower Defense:

```txt
Torre busca objetivo

Broad phase
→ enemigos registrados en las celdas que toca el rango

Narrow phase
→ distancia exacta, linea de vision y prioridad de gameplay
```

Sin broad phase, cada torre pregunta por todos los enemigos del nivel.

```txt
30 torres × 300 enemigos
= 9.000 comparaciones por evaluacion
```

Con broad phase, cada torre pregunta por los enemigos de unas pocas celdas.

```txt
30 torres × 8 candidatos promedio
= 240 comparaciones por evaluacion
```

El algoritmo de la narrow phase no cambio.

Cambio cuantas veces se ejecuta.

---

## Relacion con arquitectura

Se relaciona con:

```txt
Filtrar barato antes de validar caro.
Estructuras espaciales.
Algoritmo antes que microoptimizacion.
Separacion entre seleccion y decision.
```

Conviene que las dos etapas vivan en lugares distintos.

```txt
Broad phase
→ pertenece al sistema que conoce a todos

Narrow phase
→ pertenece a la regla que decide el caso
```

Esa separacion permite reemplazar una etapa sin tocar la otra.

```txt
Cambiar la grilla por otra estructura
→ no deberia obligar a reescribir la regla de targeting.
```

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
CPU
Frame Budget
```

Puede afectar tambien:

```txt
Memoria
GPU
```

porque la estructura de la broad phase ocupa memoria y porque en rendering la etapa cara son comandos de dibujo.

Lo que este patron cambia es el termino que mas pesa:

```txt
Costo unitario
×
cantidad de candidatos
×
frecuencia
```

Early Exit baja el costo unitario de cada evaluacion.

Broad phase baja la cantidad de candidatos que llegan a evaluarse.

---

## Cuando conviene usarlo

Conviene cuando:

```txt
La validacion precisa es cara.
Hay muchos candidatos posibles.
La mayoria de los candidatos se descarta.
Existe una aproximacion barata y conservadora.
El costo crece rapido al agregar entidades.
```

Casos claros:

```txt
Percepcion y targeting con muchos agentes.
Busqueda de vecinos en flocking.
Colisiones entre muchos cuerpos.
Consultas de area repetidas por frame.
```

---

## Cuando NO conviene usarlo

No aporta cuando:

```txt
Hay pocos candidatos.
La validacion precisa ya es barata.
Casi ningun candidato se descarta.
La broad phase cuesta parecido a la narrow phase.
La estructura de apoyo se invalida todos los frames.
```

Un caso frecuente de mal encaje:

```txt
Entidades que se mueven muchisimo
→ la estructura espacial se reconstruye constantemente
→ el mantenimiento come el ahorro
```

---

## Trade-offs

Ventajas:

```txt
Costo mucho menos sensible a la cantidad de entidades.
Menos queries caras por frame.
Etapas separadas y medibles por separado.
Posibilidad de cambiar una etapa sin tocar la otra.
```

Costos:

```txt
Estructura de apoyo que hay que construir y mantener.
Memoria adicional.
Mas codigo y mas piezas.
Riesgo de perder candidatos validos si la broad phase es demasiado agresiva.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Broad phase que descarta candidatos que si importaban.
Broad phase mas cara que la validacion que evita.
Estructura espacial desactualizada respecto de las posiciones reales.
Duplicar la regla de decision en las dos etapas.
Aplicar el patron con pocos candidatos.
Confundir la cascada de percepcion con el patron completo.
```

Ejemplo de riesgo real:

```txt
El rango de la broad phase se calcula sin el margen del rango de ataque.

Resultado:
enemigos dentro del alcance no aparecen como candidatos
y las torres dejan de dispararles.
```

Cuando la broad phase se equivoca, el sintoma no es de rendimiento: es de comportamiento.

---

## Checklist de implementacion

```txt
¿Cual es la validacion cara?
¿Que aproximacion barata la puede anticipar?
¿La broad phase puede perder candidatos validos?
¿Que margen se le dejo para no perderlos?
¿Cuantos candidatos entran y cuantos salen?
¿Cuanto cuesta mantener la estructura de apoyo?
¿Se invalida mas seguido de lo que se usa?
¿Las dos etapas estan separadas en el codigo?
¿La regla de decision quedo duplicada?
¿La cantidad de candidatos justifica el patron?
¿Se comparo el comportamiento antes y despues?
¿Se midio antes y despues?
```

---

## Regla final

Primero se decide a quien mirar, despues se decide que pasa.

```txt
Barato para elegir candidatos.
Caro solo para los que quedaron.
Una broad phase que descarta de mas no optimiza: rompe.
```

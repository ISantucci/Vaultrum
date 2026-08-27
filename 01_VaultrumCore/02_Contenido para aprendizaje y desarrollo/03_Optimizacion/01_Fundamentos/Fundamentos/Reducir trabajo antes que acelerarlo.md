## Definicion

Reducir trabajo antes que acelerarlo es el principio que ordena toda la seccion de optimizacion.

Establece que la primera pregunta frente a un costo no es "¿como lo hago mas rapido?", sino "¿tiene que ejecutarse?".

Se aplica como una secuencia de seis preguntas en orden.

```txt
1. ¿Tiene que ejecutarse?
2. ¿Tiene que ejecutarse cada frame?
3. ¿Tiene que ejecutarse para todos?
4. ¿Necesita ese nivel de precision?
5. ¿Tiene que ejecutarse en este momento?
6. Recien ahora: ¿como lo hago mas rapido?
```

Cada pregunta que se responde con "no" elimina trabajo en lugar de acelerarlo, y el trabajo eliminado no necesita optimizarse, ni mantenerse, ni volver a medirse.

---

## Responsabilidad de esta nota

Esta nota no existe para explicar tecnicas concretas.

Esta nota no existe para elegir estructuras de datos.

Esta nota no existe para prohibir la microoptimizacion.

Existe para fijar el orden en que se consideran las soluciones, de modo que las opciones baratas y reversibles se evaluen antes que las caras y complejas.

Su responsabilidad es ayudar a responder:

```txt
Ya se donde esta el costo.
¿Por donde empiezo a resolverlo?
```

---

## Que problema ayuda a entender

Ayuda a entender por que muchas optimizaciones fracasan aunque el codigo quede mas rapido.

Acelerar una operacion que no deberia ejecutarse produce una version eficiente de trabajo inutil.

Tambien ayuda a entender por que el orden importa tanto como la tecnica.

```txt
Eliminar una llamada
→ no agrega complejidad

Reescribir un algoritmo
→ agrega riesgo

Paralelizar
→ agrega sincronizacion y bugs
```

Empezar por el final de la lista es pagar el precio mas alto por algo que quizas se resolvia gratis.

---

## Como funciona

Cada pregunta tiene una accion asociada.

```txt
¿Tiene que ejecutarse?
No → eliminar

¿Cada frame?
No → reducir frecuencia

¿Para todos?
No → filtrar

¿Con esa precision?
No → simplificar

¿En este momento?
No → diferir o distribuir

Todo lo anterior es necesario
→ recien ahora, acelerar
```

De esa secuencia sale una jerarquia de soluciones ordenada por costo de implementacion y por riesgo.

```txt
Eliminar trabajo innecesario
↓
Reducir frecuencia
↓
Reducir cantidad de elementos
↓
Mejorar algoritmo
↓
Mejorar estructura de datos
↓
Reutilizar o cachear
↓
Paralelizar
↓
Microoptimizar
```

La jerarquia se recorre de arriba hacia abajo: arriba hay mas impacto y menos complejidad agregada; abajo, al reves.

No es una prohibicion de los pasos inferiores. Es un orden de evaluacion.

```txt
Microoptimizar no esta prohibido.
Esta al final porque casi nunca es lo que falta.
```

Conviene notar que distribuir no es lo mismo que eliminar.

```txt
Eliminar
→ el trabajo total baja

Distribuir
→ el trabajo total sigue igual
→ cambia cuando y como se siente
```

Las dos cosas sirven, pero resuelven sintomas distintos.

---

## Como aplicarlo en videojuegos

Ejemplo inspirado en Tower Defense.

Sintoma:

```txt
La CPU se satura cuando hay muchas torres y muchos enemigos.
```

Sistema sospechado:

```txt
Cada torre evalua a que enemigo apuntar, cada frame, recorriendo todos los enemigos.
```

Aplicando las seis preguntas en orden:

```txt
¿Tiene que ejecutarse?
Una torre sin enemigos en rango no necesita evaluar nada.
→ eliminar

¿Cada frame?
Un objetivo elegido sirve varios frames.
→ 10 evaluaciones por segundo

¿Para todos?
Solo importan los enemigos dentro del rango.
→ filtrar por celda o por rango

¿Con esa precision?
Comparar distancias al cuadrado alcanza para ordenar.
→ simplificar

¿En este momento?
No todas las torres necesitan reevaluar en el mismo frame.
→ repartir en el tiempo

¿Como lo hago mas rapido?
Recien ahora tiene sentido preguntarlo.
```

Las cuatro primeras preguntas, llevadas a codigo:

```csharp
// Malo: se recorre todo y se calcula caro para todos
foreach (var e in allEnemies)
    if (Vector3.Distance(transform.position, e.position) < range)
        Evaluate(e);
```

```csharp
// Bueno: menos candidatos, rechazo barato primero
foreach (var e in enemiesInCell)
{
    if ((e.position - transform.position).sqrMagnitude > sqrRange) continue;
    Evaluate(e);
}
```

Otro caso del mismo juego, el HUD de dinero, vida y wave actualizado cada frame:

```txt
¿Tiene que ejecutarse cada frame?
El dinero cambia cuando el jugador vende o cobra.
→ actualizar cuando cambia el dato
```

Ahi no hizo falta ningun algoritmo nuevo. Alcanzo con dejar de hacer algo que no aportaba.

Y un tercero: los enemigos lejos de la camara y fuera de combate no necesitan la misma precision de simulacion, asi que admiten menor frecuencia y menor detalle.

Criterio consolidado en Capsule Survivor.

---

## Como guia el diagnostico

Este principio entra despues del diagnostico, no antes.

Aplicado sin medicion produce refactors especulativos. Aplicado despues, ordena las soluciones candidatas.

Flujo recomendado:

```txt
Costo confirmado
→ recorrer las seis preguntas en orden
→ elegir la solucion mas alta de la jerarquia que sirva
→ volver a medir
```

La regla practica es simple: si dos soluciones resuelven el mismo problema, se elige la que agrega menos complejidad.

---

## Cuando conviene consultarlo

Conviene recorrer la jerarquia cuando:

```txt
Ya se sabe donde esta el costo.
Hay varias soluciones posibles sobre la mesa.
La primera propuesta es reescribir o paralelizar.
Un sistema escala mal al aumentar entidades.
Aparece trabajo repetido sin cambios de dato.
```

Tambien conviene consultarlo cuando una IA propone directamente una tecnica avanzada, como jobs o multithreading, sin haber preguntado si ese calculo tiene que correr cada frame.

Antes de paralelizar trabajo, conviene confirmar que ese trabajo debe existir.

---

## Cuando NO conviene forzarlo

No conviene forzar la eliminacion de trabajo cuando ese trabajo sostiene la experiencia: feedback de impacto, legibilidad del HUD, respuesta al input, claridad de estados.

Reducir esos elementos baja el costo y baja la calidad del juego.

Tampoco conviene bajar frecuencia o precision hasta que el jugador lo perciba: IA que reacciona tarde, proyectiles que atraviesan enemigos, barras de vida a destiempo.

Eso no es optimizacion. Es un bug introducido a proposito.

Tampoco conviene recorrer la jerarquia sobre un sistema que no aparece en la medicion: en algo que ocupa 0,2 ms no hay nada que ordenar.

---

## Errores que ayuda a evitar

Aplicar este principio ayuda a evitar:

- Reescribir un algoritmo que no hacia falta ejecutar.
- Paralelizar trabajo redundante.
- Poolear objetos que no necesitaban crearse.
- Microoptimizar dentro de un loop que iteraba de mas.
- Empezar por la solucion mas compleja disponible.

La idea clave es:

```txt
El trabajo mas rapido es el que no se ejecuta.
El segundo mas rapido es el que se ejecuta menos veces.
```

---

## Riesgos de interpretarlo mal

Un riesgo comun es leer la jerarquia como una prohibicion.

```txt
Lectura incorrecta
→ "nunca microoptimizar"

Lectura correcta
→ "microoptimizar cuando lo anterior ya se agoto"
```

Cuando el trabajo es necesario, la frecuencia minima y la cantidad irreducible, la microoptimizacion es la respuesta correcta.

Otro riesgo es eliminar trabajo sin entender que hacia: se saca una llamada, el costo baja y aparece un bug tres semanas despues.

Reducir trabajo exige entender la funcion de ese trabajo, no solo su costo.

Otro riesgo es tratar "reducir frecuencia" como gratuito: bajar de 60 a 10 evaluaciones por segundo reduce trabajo total, pero puede introducir latencia perceptible y un spike si todo se evalua junto.

Otro riesgo es aplicar el principio a un sistema que no era el bottleneck: se elimina trabajo real y el frame no mejora, porque ese trabajo existia pero no era el que limitaba.

---

## Hacia donde seguir

Esta nota pertenece a Fundamentos.

Si hace falta estimar el impacto de la reduccion:

```txt
→ Costo cantidad y frecuencia
```

Si hace falta confirmar que hay un costo real:

```txt
→ Medir antes de optimizar
→ Bottleneck
```

Si hace falta declarar que se gasta:

```txt
→ Trade-offs de optimizacion
```

Si hace falta medir y validar:

→ [[Diagnostico]]

Si el trabajo a reducir es logica, IA o fisica:

→ [[CPU]]

Si es render, pixeles o efectos:

→ [[GPU]]

Si son allocations o recursos residentes:

→ [[Memoria]]

Si es carga o instanciacion:

→ [[Carga e IO]]

Si son actualizaciones de interfaz:

→ [[UI]]

Si hace falta el patron de cada paso:

→ [[Patrones transversales]]

---

## Checklist de diagnostico

Antes de acelerar cualquier cosa, revisar:

```txt
¿Este trabajo tiene que ejecutarse?
¿Tiene que ejecutarse cada frame?
¿Tiene que ejecutarse para todas las entidades?
¿Necesita este nivel de precision?
¿Tiene que ocurrir en este momento?
¿Que pasa si se ejecuta la mitad de veces?
¿Que perderia el jugador si se reduce?
¿Existe una solucion mas arriba en la jerarquia?
¿La solucion elegida agrega complejidad permanente?
¿Se midio antes y se va a medir despues?
```

---

## Regla final

Optimizar no empieza por escribir codigo mas rapido. Empieza por sacar trabajo de la mesa.

```txt
Primero eliminar.
Despues reducir.
Al final, acelerar.
```

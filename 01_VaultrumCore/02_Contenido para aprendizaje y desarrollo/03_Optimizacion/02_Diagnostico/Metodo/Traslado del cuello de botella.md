## Definicion

El traslado del cuello de botella es lo que ocurre cuando una optimizacion exitosa hace que el limite del rendimiento pase a otro recurso.

El bottleneck es el recurso o la etapa que actualmente limita el rendimiento.

Si ese recurso deja de limitar, el limite no desaparece: se muda.

```txt
Se optimiza el recurso limitante
→ deja de limitar
→ otro recurso pasa a ser el limite
```

Ejemplo:

```txt
Antes:
CPU = 20 ms
GPU = 12 ms
→ limita CPU

Despues de optimizar CPU:
CPU = 10 ms
GPU = 12 ms
→ limita GPU
```

Eso no significa que la optimizacion fallo. Significa que se elimino el cuello anterior.

---

## Responsabilidad de esta nota

Esta nota existe para explicar por que el limite cambia de lugar despues de optimizar.

No existe para desalentar optimizaciones.
No existe para afirmar que optimizar no sirve.
No existe para elegir cual es el proximo recurso a atacar.
No existe para dar por cerrado un proceso de profiling.

Su responsabilidad es ayudar a responder:

```txt
¿Que esta limitando el frame ahora?
```

---

## Que problema ayuda a entender

Ayuda a entender por que una mejora real puede sentirse como un fracaso.

Ejemplo:

```txt
Se centralizaron los Update.
Se cachearon referencias.
El tiempo de CPU bajo a la mitad.
Los FPS casi no cambiaron.
```

La lectura apresurada es que no sirvio.

La lectura correcta es que ese recurso ya no es el limite.

Preguntas que ayuda a responder:

```txt
¿Mejoro el frame o solo mejoro un contador?
¿Que recurso limita ahora?
¿Cuanto margen quedo en el recurso optimizado?
¿La ganancia se convirtio en FPS o en espera?
¿El traslado fue a otro procesador o a memoria?
¿La solucion elegida creo un problema nuevo?
¿Conviene seguir iterando o ya se llego al objetivo?
```

---

## Como funciona

El frame se completa cuando terminan todas las etapas que lo componen.

```txt
Frame time
≈
el recurso mas lento
```

Reducir un recurso que no limita no cambia el resultado:

```txt
CPU: 8 ms → 5 ms
GPU: 18 ms → 18 ms

Frame final:
practicamente igual.
```

Reducir el recurso que si limita cambia el resultado, pero solo hasta el limite siguiente:

```txt
CPU: 20 ms → 10 ms
GPU: 12 ms

Ganancia real:
de 20 ms a 12 ms.

No de 20 ms a 10 ms.
```

Ahi aparece el margen sobrante:

```txt
La CPU termina en 10 ms.
El frame necesita 12 ms.
La CPU espera 2 ms.
```

Ese margen no se desperdicia: es espacio disponible para gameplay futuro.

---

## Como aplicarlo en videojuegos

Ejemplo inspirado en Tower Defense:

```txt
Sintoma inicial:
El frame cae con muchas torres y muchos enemigos.

Medicion:
CPU = 20 ms
GPU = 12 ms

Causa:
cada torre busca objetivo cada frame.

Solucion:
buscar objetivo por intervalos y cachear el enemigo actual.

Nueva medicion:
CPU = 10 ms
GPU = 12 ms
```

El sintoma cambia de dueño:

```txt
Antes:
el frame caia al agregar torres.

Ahora:
el frame cae al agregar explosiones y efectos.
```

Casos frecuentes de traslado:

```txt
Menos trabajo de CPU
→ el limite pasa a GPU

Menos trabajo de GPU
→ el limite pasa a la preparacion de draw calls en CPU

Menos calculo por frame
→ el limite pasa a memoria

Menos trabajo en runtime
→ el limite pasa a los tiempos de carga
```

---

## Como guia el diagnostico

El traslado es la razon por la cual el profiling es iterativo.

```txt
Medir
→ optimizar el limite actual
→ volver a medir
→ aparece un limite nuevo
→ decidir si vale otra vuelta
```

No alcanza con mirar el contador que se toco.

```txt
Decir "CPU bajo" no es un diagnostico.
Hay que mirar el frame completo.
```

Comparacion util despues de cada cambio:

```txt
Antes:
frame time / CPU / GPU / memoria

Despues:
frame time / CPU / GPU / memoria

Pregunta:
¿bajo el frame time o solo se movio el limite?
```

---

## Cuando conviene consultarlo

Conviene tener presente el traslado cuando:

```txt
Una optimizacion clara no mejoro los FPS.
Un contador bajo mucho y el frame casi no cambio.
Despues de optimizar aparece un sintoma nuevo.
El juego mejoro en una escena y empeoro en otra.
Se aplico pooling o caching y crecio la memoria.
Se movio trabajo entre CPU y GPU.
Hay que decidir si conviene seguir iterando.
```

Tambien conviene consultarlo antes de declarar cumplido un objetivo.

```txt
El objetivo no es bajar un recurso.
Es alcanzar el frame budget.
```

---

## Cuando NO conviene asumirlo

No conviene asumir traslado cada vez que una optimizacion no da resultado.

Tambien puede ocurrir que:

```txt
El cambio no redujo trabajo real.
Se movio codigo de lugar sin bajar su costo.
Se midio en un escenario distinto.
El sistema tocado nunca fue el limitante.
La medicion no cubre el momento del sintoma.
```

Ejemplo:

```txt
Se saco logica de Update.
Se ejecuta igual cada frame desde otro manager.
El costo total no cambio.
```

Eso no es traslado. Es la misma carga con otro nombre.

Tampoco conviene asumir que todo traslado es aceptable.

```txt
Se elimino un spike de CPU.
Se creo un pool enorme que ocupa memoria.
```

Si el recurso nuevo tambien esta ajustado, el problema solo cambio de forma.

---

## Errores que ayuda a evitar

Entender el traslado ayuda a evitar:

- Declarar exito porque un contador bajo.
- Declarar fracaso porque los FPS no subieron.
- Optimizar un recurso que no limita.
- Medir solamente el subsistema que se toco.
- Repetir la misma tecnica cuando el limite ya se mudo.
- Ignorar el crecimiento de memoria que deja el pooling.
- Cachear sin revisar cuanta memoria queda residente.
- Pasar trabajo de CPU a GPU sin medir la GPU.
- Cerrar el profiling despues de una sola vuelta.
- Confundir mover trabajo con reducir trabajo.

La idea clave es:

```txt
El limite no desaparece.
Se mueve.
```

---

## Riesgos de interpretarlo mal

El primer riesgo es usarlo como excusa.

```txt
"No mejoro porque se traslado el cuello."
```

Eso solo puede afirmarse con una medicion que lo demuestre.

Otro riesgo es perseguir traslados sin objetivo.

```txt
Se optimiza CPU.
Se optimiza GPU.
Se optimiza memoria.
El frame ya cumplia el presupuesto en la segunda vuelta.
```

Optimizar mas alla del objetivo gasta tiempo y agrega complejidad.

Otro riesgo es olvidar el traslado hacia memoria.

Pooling y caching intercambian:

```txt
menos CPU
↔
mas memoria residente
```

Un pool gigante que conserva cientos de objetos inutilizados puede resolver un problema de CPU y crear uno de memoria.

Ese traslado es mas silencioso: no aparece en el frame time, aparece mas tarde.

---

## Hacia donde seguir

Esta nota se apoya en el concepto de bottleneck y cierra el ciclo del metodo.

Base conceptual:

→ [[Fundamentos]]

Conceptos de apoyo:

```txt
→ Bottleneck
→ Frame Budget
→ Medir antes de optimizar
→ CPU Bound
→ GPU Bound
→ Flujo de diagnostico
```

Si el limite se mudo al procesador:

→ [[CPU]]

→ [[GPU]]

Si el limite se mudo a memoria residente:

→ [[Memoria]]

Si el limite se mudo a los tiempos de carga:

→ [[Carga e IO]]

Si la solucion aplicada fue un patron con trade-off:

→ [[Patrones transversales]]

Herramientas para confirmar el traslado:

```txt
→ Unity Profiler
→ Memory Profiler
→ Comparacion antes y despues
```

---

## Checklist de diagnostico

Despues de aplicar una optimizacion, revisar:

```txt
¿Bajo el frame time o solo un contador?
¿Que recurso limita ahora?
¿Cuanto margen quedo en el recurso optimizado?
¿Aparecio un sintoma nuevo?
¿Crecio la memoria residente?
¿Se movio trabajo entre CPU y GPU?
¿Se midio el frame completo y no solo el sistema tocado?
¿El nuevo limite justifica otra vuelta?
¿El frame budget ya se cumple?
¿El traslado es aceptable en el hardware objetivo?
```

---

## Regla final

Optimizar el limite actual no elimina el limite. Lo muda.

```txt
Un traslado no es un fracaso.
Es la prueba de que el cuello anterior se elimino.
Volver a medir el frame completo y decidir si vale otra vuelta.
```

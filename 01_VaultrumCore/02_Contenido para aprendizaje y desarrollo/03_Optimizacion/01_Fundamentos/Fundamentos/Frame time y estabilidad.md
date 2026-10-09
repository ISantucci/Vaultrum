## Definicion

El frame time es el tiempo que tarda el juego en producir un frame, medido en milisegundos.

Los FPS son una consecuencia de ese tiempo, no una causa.

```txt
Frame time
→ cuanto tarda un frame en producirse

FPS
→ cuantos frames entran en un segundo
→ resultado promediado del frame time
```

La relacion basica es:

```txt
Tiempo por frame = 1000 ms / FPS objetivo
```

Presupuestos habituales:

```txt
30 FPS  → 33,33 ms
60 FPS  → 16,66 ms
120 FPS → 8,33 ms
144 FPS → 6,94 ms
```

La estabilidad es la otra mitad del concepto.

Un juego no se percibe solamente por lo que cuesta un frame promedio, sino por cuanto varian los frames entre si.

---

## Responsabilidad de esta nota

Esta nota no existe para fijar un objetivo de FPS.

Esta nota no existe para repartir presupuesto entre sistemas.

Esta nota no existe para decir que recurso esta saturado.

Esta nota no existe para elegir una solucion.

Existe para instalar la unidad de medida correcta y para separar promedio de experiencia.

Su responsabilidad es ayudar a responder:

```txt
¿Cada frame cuesta demasiado?
¿O algunos frames cuestan muchisimo mas que el resto?
```

Son dos problemas distintos, con causas distintas y soluciones distintas.

---

## Que problema ayuda a entender

Ayuda a entender por que un promedio sano puede esconder una experiencia mala.

Un juego puede reportar:

```txt
60 FPS promedio
```

y estar produciendo frames asi:

```txt
16 ms
16 ms
16 ms
72 ms
16 ms
16 ms
```

Ese spike se percibe como stutter aunque el promedio parezca sano.

El jugador no percibe promedios. Percibe interrupciones.

Tambien ayuda a entender por que FPS es una unidad engañosa para comparar mejoras.

```txt
30 FPS → 60 FPS
= 16,66 ms ganados

120 FPS → 144 FPS
= 1,39 ms ganados
```

En FPS parecen saltos parecidos. En milisegundos no se parecen en nada.

---

## Como funciona

El frame time no es un unico numero, sino una serie temporal.

De esa serie interesan varias lecturas:

```txt
Promedio
→ costo tipico del frame

Estabilidad
→ dispersion entre frames

Maximos
→ el peor frame observado

Spikes
→ frames aislados muy por encima del promedio

Frecuencia de spikes
→ cada cuanto ocurren

Consistencia
→ si el patron se repite o es azaroso
```

```txt
Promedio alto y estable
→ hay demasiado trabajo por frame

Promedio bajo con spikes
→ hay trabajo puntual y concentrado

Promedio que sube con el tiempo
→ algo se acumula

Promedio que sube al escalar
→ el costo depende de la cantidad
```

Un spike casi nunca es "el juego en general": suele ser un evento identificable, como una carga de assets, un Instantiate masivo, una recoleccion de memoria o un rebuild de UI.

Por eso conviene medir siempre la serie, no un solo valor.

---

## Como aplicarlo en videojuegos

En videojuegos, la pregunta util no es "¿a cuantos FPS va?", sino "¿como se comporta el frame time durante el juego real?".

Ejemplo inspirado en Tower Defense:

```txt
Sintoma:
El juego marca 60 FPS promedio.
Pero se siente entrecortado al empezar cada oleada.
```

Lectura correcta:

```txt
Promedio: 16,7 ms
Maximo: 70 ms
Spikes: 1 por oleada
Frecuencia: cada 20 segundos
```

Diagnostico probable:

```txt
El costo esta concentrado en el spawn de la oleada.
```

Distinto seria este otro caso:

```txt
Promedio: 26 ms
Maximo: 28 ms
Spikes: ninguno
```

Ahi no hay stutter.

Hay demasiado trabajo constante y un objetivo de 60 FPS que no se cumple.

La misma sensacion de "va mal" tiene dos causas opuestas: los spikes se atacan distribuyendo o precargando, y el promedio alto se ataca reduciendo cantidad, frecuencia o costo unitario.

---

## Como guia el diagnostico

El frame time convierte una queja en una medicion.

No alcanza con decir:

```txt
El juego se traba.
```

Conviene transformarlo en:

```txt
¿Cual es el frame time promedio?
¿Cual es el maximo?
¿Cuando aparece el maximo?
¿Se repite?
¿Cada cuanto?
¿Coincide con algun evento del juego?
```

Flujo recomendado:

```txt
Sintoma percibido
→ captura de frame time
→ promedio vs maximos
→ ¿constante o puntual?
→ evento asociado al spike
→ hipotesis de recurso
→ medicion dirigida
```

Esa bifurcacion entre constante y puntual es la que mas orienta el resto de la investigacion.

---

## Cuando conviene consultarlo

Conviene trabajar con frame time cuando:

```txt
Hay stuttering o tirones.
El promedio parece bueno pero se siente mal.
El rendimiento cambia segun el momento de la partida.
Hay que comparar antes y despues de una optimizacion.
Hay que fijar un objetivo de rendimiento.
Hay que decidir si un sistema entra o no en presupuesto.
```

Tambien conviene consultarlo antes de aceptar una mejora reportada en FPS.

```txt
"Subio de 55 a 60 FPS"
→ ¿cuantos ms son?
→ ¿que paso con los maximos?
```

Una optimizacion que sube el promedio y empeora los spikes puede sentirse peor que antes.

---

## Cuando NO conviene forzarlo

No conviene forzar el analisis de frame time cuando todavia no hay objetivo de rendimiento ni hardware de referencia.

```txt
Prototipo temprano.
Sin plataforma objetivo.
Sin sintoma.
```

Medir ahi produce numeros sin criterio de aceptacion.

Tampoco conviene tratar cualquier variacion como un problema: un frame time perfectamente plano no es un objetivo realista.

Siempre hay variacion; el problema aparece cuando se vuelve perceptible o repetitiva.

Tampoco conviene concluir nada de una medicion tomada en el editor, con logs y ventanas abiertas.

---

## Errores que ayuda a evitar

Trabajar con frame time ayuda a evitar:

- Usar FPS como unica metrica de rendimiento.
- Confundir promedio con experiencia.
- Ignorar los maximos porque el promedio cierra.
- Declarar exito por una mejora de FPS sin mirar spikes.
- Tratar un problema puntual como si fuera un problema constante.
- Optimizar trabajo por frame cuando el problema es un spike de carga.
- Comparar mediciones tomadas en escenas distintas.
- Medir en el editor y afirmar que se midio el juego.
- Aceptar "va a 60" sin preguntar en que hardware y a que resolucion.

La idea clave es:

```txt
El promedio describe el juego.
Los maximos describen lo que siente el jugador.
```

---

## Riesgos de interpretarlo mal

Un riesgo comun es creer que un frame time bajo garantiza una buena experiencia.

```txt
Promedio: 12 ms
Un spike de 90 ms cada 5 segundos
```

Ese juego se percibe roto aunque el promedio sea excelente.

Otro riesgo es el inverso: perseguir cada pico aislado. Un spike unico al cargar una escena suele ser esperable.

No todo maximo es un defecto.

Importa la frecuencia y el momento en que ocurre.

Otro riesgo es comparar mediciones no equivalentes, como capturar la oleada 1 antes del cambio y el menu principal despues.

Sin la misma escena, la misma duracion y las mismas condiciones, la comparacion no dice nada.

Otro riesgo es asumir que el frame time indica la causa: dice cuanto y cuando, no por que.

El por que aparece recien al medir el interior del frame.

---

## Hacia donde seguir

Esta nota pertenece a Fundamentos.

Si hace falta convertir el objetivo en presupuesto:

```txt
→ Frame Budget
→ Game loop
```

Si hay que ubicar el recurso limitante:

```txt
→ Bottleneck
→ Recursos de hardware
```

Si hace falta medir la serie y comparar antes y despues:

→ [[Diagnostico]]

Si el costo viene de logica, IA o fisica:

→ [[CPU]]

Si parece venir de render:

→ [[GPU]]

Si los spikes coinciden con la memoria:

→ [[Memoria]]

Si coinciden con cargas o cambios de escena:

→ [[Carga e IO]]

Si aparecen al actualizar la interfaz:

→ [[UI]]

Si hace falta distribuir trabajo concentrado:

→ [[Patrones transversales]]

---

## Checklist de diagnostico

Antes de afirmar algo sobre rendimiento, revisar:

```txt
¿Cual es el objetivo en ms, no en FPS?
¿Cual es el frame time promedio medido?
¿Cual es el maximo?
¿Cuantos spikes hay por minuto?
¿Los spikes coinciden con un evento del juego?
¿El problema es constante o puntual?
¿La escena es representativa del juego real?
¿La medicion se tomo en build o en editor?
¿Se conoce el hardware y la resolucion de referencia?
¿Existe una medicion previa comparable?
```

---

## Regla final

FPS es un titular.

El frame time es el dato.

```txt
Un promedio sano no prueba que el juego se sienta bien.
Se mide el frame time completo: promedio, maximos y frecuencia de spikes.
```

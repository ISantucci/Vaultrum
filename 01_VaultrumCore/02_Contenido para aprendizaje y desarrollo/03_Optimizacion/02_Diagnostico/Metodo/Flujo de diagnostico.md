## Definicion

El flujo de diagnostico es el orden en que se investiga un problema de rendimiento antes de modificar nada.

Es el metodo que gobierna toda la seccion de Optimizacion.

```txt
Sintoma
→ Hipotesis
→ Medicion
→ Diagnostico
→ Solucion
→ Trade-off
→ Nueva medicion
→ Validacion
```

La idea principal es:

```txt
Primero se mide.
Despues se optimiza.
```

Una optimizacion sin diagnostico previo es una modificacion especulativa.

---

## Responsabilidad de esta nota

Esta nota existe para ordenar el trabajo de optimizacion.

No existe para dar soluciones concretas.
No existe para reemplazar a las herramientas de medicion.
No existe para decidir de antemano si el problema es CPU, GPU o memoria.
No existe para justificar cambios sin evidencia.

Su responsabilidad es ayudar a responder:

```txt
¿En que paso del proceso estoy?
¿Ya hay evidencia para modificar codigo?
```

Este flujo tambien es el que decide a que rama entrar. La rama es una respuesta del diagnostico, no un punto de partida.

---

## Que problema ayuda a entender

Ayuda a entender por que la mayoria de las optimizaciones fallidas fallan antes de escribirse.

Fallan en el orden, no en la tecnica.

Proceso incorrecto:

```txt
El juego va lento.
→ aplicar pooling
→ centralizar Update
→ bajar sombras
→ sigue igual
→ nadie sabe que paso
```

Proceso correcto:

```txt
El juego va lento.
→ describir el sintoma
→ plantear hipotesis
→ medir
→ diagnosticar
→ cambiar una sola cosa
→ volver a medir
```

---

## Como funciona

Cada paso tiene algo que se hace y algo que todavia no se hace.

Sintoma:

```txt
Se hace:
describir que ocurre y cuando ocurre.
FPS bajo, stutter, freeze periodico,
caida al aparecer enemigos, caida al abrir UI,
memoria creciente, carga demasiado larga.

No se hace:
explicar la causa.
```

Hipotesis:

```txt
Se hace:
plantear causas posibles.

No se hace:
todavia no se modifica nada.
```

Medicion:

```txt
Se hace:
usar herramientas para localizar donde ocurre el costo.
Capturar el momento exacto del sintoma.

No se hace:
mirar numeros al azar sin una pregunta previa.
```

Diagnostico:

```txt
Se hace:
determinar el recurso limitante.
CPU, GPU, memoria o I/O.
Despues, el subsistema responsable.

No se hace:
elegir la tecnica preferida.
```

Solucion:

```txt
Se hace:
modificar especificamente lo que genera el problema.
La solucion minima necesaria.

No se hace:
cambiar varias cosas a la vez.
```

Trade-off:

```txt
Se hace:
declarar que recurso se gasta a cambio.

menos CPU
↔
mas memoria

No se hace:
suponer que la mejora fue gratis.
```

Nueva medicion:

```txt
Se hace:
repetir exactamente la medicion anterior.
Misma escena, mismo escenario, mismo momento.

No se hace:
comparar contra un recuerdo.
```

Validacion:

```txt
Se hace:
confirmar que el frame completo mejoro
y que gameplay, visuales y feedback siguen intactos.

No se hace:
cerrar el trabajo porque un contador bajo.
```

Sin medicion posterior no puede afirmarse que hubo una optimizacion.

---

## Como aplicarlo en videojuegos

Ejemplo completo inspirado en Tower Defense:

```txt
Sintoma:
Al entrar una oleada nueva el juego se traba un instante.

Hipotesis:
Instantiate masivo de enemigos.
IA que arranca de golpe.
HUD de wave que se reconstruye.

Medicion:
Capturar el frame exacto del spawn.

Diagnostico:
El costo esta en CPU, en creacion de entidades.

Solucion:
Object Pool para los enemigos de la oleada.

Trade-off:
Mas memoria residente.
Mas logica de reset y lifecycle.

Nueva medicion:
Capturar otra vez el mismo spawn.

Validacion:
El spike bajo.
Los enemigos siguen apareciendo bien y con el mismo feedback.
```

El mismo flujo aplica a un sintoma grafico:

```txt
Sintoma:
Cae el frame cuando explotan varios enemigos juntos.

Hipotesis:
Particulas transparentes muy grandes.

Medicion:
Tiempo de GPU durante la explosion.

Diagnostico:
Overdraw.

Solucion:
Reducir tamaño y lifetime de las particulas.

Trade-off:
Menos espectacularidad visual.

Validacion:
El frame mejora y la explosion sigue leyendose.
```

---

## Como guia el diagnostico

El flujo es lo que esta por encima de todas las ramas.

```txt
PERFORMANCE
→ ¿que esta limitando?
→ CPU / GPU / Memoria / Carga
→ causa concreta
→ solucion
→ trade-off
→ validacion
```

Por eso el orden importa mas que la tecnica.

```txt
No se empieza optimizando CPU.
No se empieza optimizando GPU.
Se empieza midiendo.
```

---

## Cuando conviene consultarlo

Conviene volver a este flujo cuando:

```txt
Aparece un sintoma nuevo de rendimiento.
No se sabe por donde empezar.
Se discute una solucion sin datos.
Se probaron varios cambios y nada mejoro.
No queda claro si el ultimo cambio sirvio.
Hay que justificar una decision tecnica.
Se va a tocar codigo por motivos de performance.
```

Tambien conviene consultarlo antes de cerrar una tarea.

```txt
¿Se repitio la medicion?
Si la respuesta es no, la tarea no esta terminada.
```

---

## Cuando NO conviene asumirlo

No conviene asumir que el flujo ya se cumplio porque se miro el Profiler una vez.

Ejemplo:

```txt
Se abrio el Profiler.
Se vio un pico.
Se cambio codigo.
No se volvio a medir.
```

Eso fue una medicion, no una validacion.

Tampoco conviene asumir que el flujo garantiza mejora.

```txt
El flujo garantiza evidencia.
No garantiza que exista una solucion barata.
```

Y no conviene aplicarlo con toda su ceremonia a cualquier detalle.

```txt
Un sistema consume 0.05 ms.
No limita el frame.
```

Ahi no hace falta abrir un proceso completo.

---

## Errores que ayuda a evitar

Seguir el flujo ayuda a evitar:

- Optimizar por intuicion.
- Aplicar una tecnica antes de conocer la causa.
- Confundir sintoma con causa.
- Cambiar varias cosas a la vez y no saber cual funciono.
- Medir en un escenario distinto al del sintoma.
- Comparar contra un recuerdo en vez de contra una captura.
- Declarar exito porque subio el promedio de FPS.
- Olvidar declarar el trade-off.
- Cerrar la tarea sin revisar gameplay ni feedback.
- Entrar a una rama antes de tener diagnostico.

La idea clave es:

```txt
Sin medicion posterior no hubo optimizacion.
Hubo un cambio.
```

---

## Riesgos de interpretarlo mal

El primer riesgo es leerlo como un tramite.

No es una lista para completar. Es el orden que hace que la evidencia signifique algo.

Otro riesgo es tratarlo como lineal y de una sola vuelta.

```txt
Validacion
→ nuevo sintoma
→ el flujo vuelve a empezar
```

El profiling es iterativo.

Otro riesgo es detenerse en el paso Solucion.

```txt
El cambio se hizo.
La tarea se cerro.
Nadie sabe si sirvio.
```

Otro riesgo es validar solo con numeros.

```txt
El frame mejoro.
El gameplay se rompio.
```

Eso no es una optimizacion terminada.

---

## Hacia donde seguir

Esta nota es el metodo que gobierna toda la seccion.

Base conceptual antes de entrar a cualquier rama:

→ [[Fundamentos]]

Conceptos de apoyo:

```txt
→ Medir antes de optimizar
→ Frame Budget
→ Bottleneck
→ Cuando NO optimizar
```

Segun lo que devuelva el diagnostico:

→ [[CPU]]

→ [[GPU]]

→ [[Memoria]]

→ [[Carga e IO]]

→ [[UI]]

Si la solucion es un patron ya conocido:

→ [[Patrones transversales]]

Herramientas para el paso de medicion:

```txt
→ Unity Profiler
→ CPU Usage
→ Timeline
→ Frame debugger
→ Memory Profiler
→ Comparacion antes y despues
```

---

## Checklist de diagnostico

Antes de dar por cerrado un trabajo de optimizacion, revisar:

```txt
¿El sintoma esta descripto con precision?
¿Se anotaron las hipotesis antes de tocar codigo?
¿Se midio en el escenario donde aparece el sintoma?
¿El diagnostico nombra un recurso y un subsistema?
¿Se cambio una sola cosa?
¿Se declaro el trade-off?
¿Se repitio exactamente la misma medicion?
¿Mejoro el frame completo y no solo un contador?
¿El gameplay y el feedback siguen intactos?
¿Aparecio un cuello de botella nuevo?
```

---

## Regla final

El flujo no es papeleo. Es lo que separa una optimizacion de un cambio con suerte.

```txt
Sintoma antes que hipotesis.
Medicion antes que solucion.
Nueva medicion antes que conclusion.
```

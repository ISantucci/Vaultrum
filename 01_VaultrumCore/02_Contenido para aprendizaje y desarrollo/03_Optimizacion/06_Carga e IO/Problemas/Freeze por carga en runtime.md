## Definicion

El rendimiento no es exclusivamente FPS.

```txt
Startup.
Pantallas de carga.
Transiciones.
Streaming.
Stutters por carga.
```

Todo eso tambien es rendimiento, y no aparece en el promedio de frames por segundo.

Un freeze por carga en runtime ocurre cuando una operacion pesada se ejecuta de golpe, en medio del juego, y detiene el frame.

```txt
frame normal
↓
carga
↓
freeze
↓
frame normal
```

Lo particular de este problema es que puede convivir con un rendimiento habitual excelente.

```txt
16 ms
16 ms
480 ms
16 ms
16 ms
```

El promedio sigue siendo bueno. La experiencia no.

---

## Responsabilidad de esta nota

Esta nota no existe para explicar todo el sistema de carga de assets.

Esta nota no existe para asumir que toda pausa es un problema de disco.

Esta nota no existe para justificar precargar el juego entero.

Esta nota no existe para diagnosticar caidas sostenidas de FPS.

Existe para diagnosticar un caso concreto: el juego funciona bien y en un momento puntual se detiene porque algo se cargo, se instancio o se resolvio de una sola vez.

Su responsabilidad es ayudar a responder:

```txt
¿Que trabajo se acumulo en un solo frame
y por que se hizo justo ahi?
```

El foco no esta en cuanto tarda el juego en total. Esta en:

```txt
cuando ocurre el trabajo
cuanto trabajo cae junto
si podia hacerse en otro momento
```

---

## Sintomas

Sintomas comunes:

```txt
Freeze puntual al entrar a una zona.
Tiron al aparecer una oleada.
Pausa al abrir un menu por primera vez.
Stutter reproducible siempre en el mismo lugar.
El juego rinde bien salvo en momentos concretos.
```

Un patron muy caracteristico:

```txt
Primera vez que ocurre
→ freeze notorio.

Segunda vez
→ casi imperceptible.
```

Esa asimetria es una pista fuerte: algo se resolvio una vez y quedo disponible.

---

## Que parte del software suele causarlo

Suele aparecer por:

```txt
Cargar un asset pesado al entrar a una zona.
Instanciar una oleada entera de una sola vez.
Resolver una escena o un bundle en medio del gameplay.
Construir una UI completa al abrirla.
Preparar un sistema recien cuando se usa.
```

El patron tecnico habitual:

```txt
trabajo diferido hasta el ultimo momento
+ ese momento es gameplay activo
```

No es que el trabajo sea excesivo. Es que se hace todo junto y en el peor instante posible.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
Almacenamiento
CPU
Memoria
Main Thread
```

El freeze suele nacer de una combinacion:

```txt
Lectura de disco → espera.
Deserializacion y preparacion → CPU.
Subida de recursos graficos → memoria y GPU.
Todo eso bloqueando el frame → Main Thread.
```

Pesa mucho mas en almacenamiento lento y con poca memoria disponible.

---

## Como detectarlo

Lo primero es mirar frame time, no FPS. Un spike de cientos de milisegundos se pierde completamente en un promedio.

El metodo directo es reproducir el momento exacto, capturar ese frame, ver que subsistema se llevo el tiempo y repetir la accion una segunda vez para comparar.

Preguntas practicas:

```txt
¿El freeze ocurre siempre en el mismo punto?
¿Ocurre solo la primera vez?
¿Escala con la cantidad de objetos que aparecen?
¿El tiempo se va en lectura o en preparacion?
```

---

## Herramientas de deteccion

Herramientas utiles:

```txt
→ Unity Profiler
→ Timeline
→ Memory Profiler
→ Comparacion antes y despues
```

Que mirar:

```txt
Frame time y no FPS.
Ancho del spike en la timeline.
Llamadas de carga e instanciacion.
Salto de memoria en el instante del freeze.
```

La timeline es la vista clave: muestra el ancho del pico y quien lo produjo.

---

## Soluciones posibles

Soluciones candidatas dentro de la rama:

```txt
Precarga y carga distribuida
Addressables como metodologia de optimizacion
AssetManager como optimizacion
```

Soluciones especificas del problema:

```txt
Cargar antes, en un momento menos critico.
Repartir el trabajo entre varios frames.
Instanciar la oleada por tandas.
Preparar la UI al abrir el nivel y no al abrirla.
```

Y desde otras ramas:

```txt
Object pool como optimizacion
Ciclo de vida de recursos
Comparacion antes y despues
```

Ejemplo:

```txt
Antes:
Al empezar la wave se instancian 300 enemigos en un frame.

Despues:
Se instancian en tandas de 50 durante seis frames.
```

---

## Trade-offs

```txt
Precargar antes
→ sin spike en gameplay
→ mas memoria residente y carga inicial mas larga.

Repartir entre frames
→ sin freeze
→ el contenido tarda mas en estar completo.

Instanciar por tandas
→ frame estable
→ la oleada entra escalonada.
```

Distribuir no elimina trabajo. Cambia cuando se hace y como se percibe.

---

## Ejemplo en videojuegos

En un Tower Defense el momento critico es siempre el mismo: el comienzo de la wave.

```txt
Empieza la wave
→ se instancian los enemigos
→ se cargan sus assets si es la primera vez
→ se prepara el efecto de aparicion
→ se actualiza el HUD de wave
```

Todo eso cae en un frame. El resultado tipico:

```txt
Wave 1
→ freeze de medio segundo.

Wave 2 con los mismos enemigos
→ sin freeze.

Wave 5 con un enemigo nuevo
→ freeze otra vez.
```

El jugador percibe algo muy concreto: la defensa se traba justo cuando tiene que reaccionar. El freeze no rompe el frame nada mas. Rompe la decision.

---

## Como guia el diagnostico

Flujo recomendado:

```txt
Sintoma:
tiron puntual en un momento identificable.

Sospecha:
trabajo de carga o instanciacion concentrado.

Medicion:
capturar ese frame en la timeline.

Dato esperado:
un pico ancho con carga, deserializacion o instanciacion.

Confirmacion:
repetir la accion y ver que el pico baja.

Solucion candidata:
adelantar el trabajo o repartirlo entre frames.
```

La pregunta clave es:

```txt
¿Este trabajo tenia que ocurrir en este frame?
```

---

## Errores comunes al intentar solucionarlo

```txt
Mirar FPS promedio y no ver el spike.
Suponer que el disco es siempre el culpable.
Precargar todo por las dudas.
Medir con el juego calentado y no reproducir el caso.
No volver a medir despues del cambio.
```

Ejemplo de mala solucion:

```txt
Problema:
Freeze al empezar cada wave.

Decision:
Precargar todos los enemigos de todas las waves al iniciar.

Resultado:
Sin freeze, con una carga inicial larguisima
y memoria al limite en las plataformas chicas.
```

Se movio el problema de rama. No se resolvio.

---

## Hacia donde seguir

Si hace falta entender por que el promedio esconde el spike:

→ [[Fundamentos]]

Si hace falta ubicar en que frame y en que subsistema ocurre:

→ [[Diagnostico]]

Si el pico esta en instanciacion y no en lectura:

→ [[CPU]]

Si adelantar la carga empuja la memoria residente:

→ [[Memoria]]

Si el freeze aparece al mostrar recursos graficos por primera vez:

→ [[GPU]]

Si la pausa ocurre al abrir un panel o construir la interfaz:

→ [[UI]]

Si la solucion pasa por repartir trabajo en el tiempo:

→ [[Patrones transversales]]

Herramientas para confirmar:

```txt
→ Unity Profiler
→ Timeline
→ Memory Profiler
```

---

## Checklist de diagnostico

```txt
¿Se midio frame time y no FPS promedio?
¿El freeze es reproducible en un punto concreto?
¿Ocurre solo la primera vez?
¿Escala con la cantidad de objetos que aparecen?
¿Que subsistema aparece en el pico?
¿El tiempo se va en lectura o en preparacion?
¿La memoria salta en ese instante?
¿Ese trabajo podia hacerse antes?
¿Ese trabajo podia repartirse entre frames?
¿La solucion no traslado el problema a memoria?
¿Se comparo antes y despues en el mismo momento?
```

---

## Regla final

Un juego que promedia 60 FPS y se traba medio segundo en cada oleada no es un juego optimizado.

```txt
El trabajo no desaparece.
Solo se elige cuando pagarlo.
Y el peor momento posible
es mientras el jugador juega.
```

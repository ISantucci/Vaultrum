---
tipo: juego
genero: Arcade
subtipo: Contrarreloj — el reloj como rival (cuenta regresiva, time trial, duración fija)
estado: En validación
mision: EST-019_Mision_Endless_runner_y_contrarreloj
cruza: 05_Endless_runner, 02_Plataformero_2D, 06_Dificultad_y_curva, 12_Pacing_y_estructura, 14_UI_HUD_y_menus, 15_Muerte_reintento_y_checkpoints, 16_Audio_como_gameplay, 01_Bucle_de_simulacion
---

# Libro 06 — Contrarreloj

> Sexto libro del estante de Juegos. Género: Arcade / contrarreloj.
> El contrarreloj no es un género de verbo sino de **estructura**: se monta sobre un plataformero, un juego de carreras o un puzzle. El libro del género base manda sobre el verbo; este, sobre el reloj.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Índice del libro

- Los cuatro relojes
- Loop de experiencia
- La presión, en detalle
- Table-stakes
- Juice / señales de urgencia
- Baseline: cómo se fijan las metas
- Ghosts y splits, en detalle
- El vecino: el endless runner
- Definición de Terminado
- Aplicación
- Límites
- Fuentes

---

## Los cuatro relojes

| Subtipo | El reloj… | Llegar a cero / al final | Ejemplos | Para qué está el reloj |
|---------|-----------|--------------------------|----------|------------------------|
| **A. Cuenta regresiva con recarga** | baja, y los checkpoints o las tareas lo recargan | es perder | Super Mario Bros. (400 unidades; una unidad ≈ 0.4 s), Out Run (tiempo extra en cada checkpoint, ruta que se bifurca), Crazy Taxi (bonus por viaje rápido), Super Monkey Ball (reloj por nivel) | marcar el ritmo; obligar a elegir ruta |
| **B. Contrarreloj medida** (time trial, time attack) | sube, y no mata | es el puntaje | Trackmania (medallas), Neon White (medallas que abren pistas), Celeste (reloj de speedrun opcional), Tetris Sprint 40 líneas | rejugar: la marca es el rival |
| **C. Duración fija** | baja, y marca el final | termina la partida; gana el puntaje | Tetris Ultra (2–3 min), Pac-Man Championship Edition (5 min), Bejeweled Blitz (1 min) | igualar la competencia; sesión corta |
| **D. Macroreloj** | es una regla del mundo | reinicia el ciclo o cambia el final | Majora's Mask (ciclo de 72 h ≈ 54 min reales), Dead Rising (72 h), Minit (vidas de 60 s) | planificación y estructura — **fuera del baseline**, ver Límites |

**La pregunta que decide todo el diseño: ¿el reloj amenaza o mide?** En A, y al final de C, el reloj es una amenaza: el HUD tiene que *alarmar*. En B es una medida: el HUD tiene que *comparar*. Un time trial con alarma de urgencia y una cuenta regresiva sin aviso están rotos en direcciones opuestas. *Destilación propia.*

---

## Loop de experiencia

```txt
A  LOOP DE TRAMO    (≈20 s–2 min)   tramo → checkpoint → +tiempo → el tramo siguiente arranca con el sobrante
B  LOOP DE INTENTO  (≈10 s–2 min)   correr → comparar con la referencia → reintentar al instante
   LOOP DE MAESTRÍA (horas)         bronce → plata → oro → la marca del autor → el récord propio
C  LOOP DE PARTIDA  (1–5 min)       exprimir el tiempo → cierre → puntaje → revancha
```

El subtipo B se parece a `02_Plataformero_2D` en su unidad —el intento— y a `05_Endless_runner` en su motor: el reintento es el juego. La diferencia es que en el time trial **el jugador ya sabe pasar el nivel**; lo que aprende ahora es la ruta y la ejecución limpia. **Primero se pasa, después se corre.** *Destilación propia.*

**Dónde vive la tensión.** En A, en la distancia entre el reloj y el próximo checkpoint: incertidumbre de resultado. En B, en el delta contra la referencia, que se lee en cada split: incertidumbre de ejecución, como en el plataformero. En C, en el último tramo, donde cada segundo vale más porque es el último. `17_Uncertainty_in_Games`

---

## La presión, en detalle

El reloj es la forma más directa de subir la activación del jugador, y la activación no rinde lineal:

- **Yerkes–Dodson.** El rendimiento sube con la activación hasta un punto y después cae. En tareas simples o bien aprendidas el punto óptimo está alto; en tareas nuevas o complejas, en una activación moderada. Es una correlación con críticas —flow y la teoría de la reversión la discuten—, no una ley causal.
- **Yıldırım (2015).** 106 estudiantes jugaron dos minutos de un shooter en tercera persona, con y sin cuenta regresiva. La presión de tiempo **solo** subió el flow; no cambió el disfrute, el rendimiento, la competencia percibida ni la motivación. Los que no llegaron a tiempo reportaron *más* flow. La autora concluye que hay un límite óptimo. Evidencia débil: tesis de maestría, un solo juego. `58_Time_Pressure_Yildirim`
- **North y Hargreaves (1999).** En un juego de manejo, una música más activadora —sumada a una tarea secundaria— hizo los tiempos de vuelta *más lentos*. La señal de urgencia compite por los mismos recursos que la tarea.

**La relación que queda: la presión se dosifica según cuánto domina el jugador la tarea.** Reloj holgado, o ninguno, mientras aprende el espacio; reloj ajustado cuando ya lo domina. B lo resuelve por estructura: la primera pasada es para pasar, la medalla viene después. A lo resuelve con el presupuesto: holgado en el primer tramo. *Destilación propia*, cruzada con `06_Dificultad_y_curva` (presentar → consolidar → combinar → examinar): **el reloj es una forma de examen.**

---

## Table-stakes

| # | Table-stake | Por qué es obligatorio |
|---|-------------|------------------------|
| 1 | **El reloj cuenta tiempo de simulación, no reloj de pared** | Igual a cualquier FPS, se detiene con la pausa y se puede reproducir. Un reloj de pared hace que el récord dependa de la máquina. Trackmania corre su física determinista a 100 Hz y valida un replay re-simulándolo entero. `01_Bucle_de_simulacion`, `65_Fix_Your_Timestep` |
| 2 | **Regla de inicio y fin declarada antes de que exista el primer récord** | Qué cuenta y qué no —cargas, cinemáticas, muertes, menús— es una decisión de diseño, y cambiarla después invalida lo guardado: Celeste la cambió en la v1.2.1.0 y tuvo que borrar los tiempos de speedrun. Arranca con el primer input o al cruzar la largada, nunca al cargar; termina en un evento inequívoco. `34_Celeste` (changelog), `69_LiveSplit_core` |
| 3 | **La pausa congela el reloj y no regala tiempo** | Si pausar sirve para pensar o reposicionarse, la pausa se vuelve técnica. Celeste agregó un buffer de 0.1 s al despausar |
| 4 | **Reloj legible de un vistazo:** posición fija, dígitos de ancho fijo, precisión según el subtipo | Se lee en la periferia mientras se juega. A: segundos o unidades. B: la precisión que el paso de simulación sostenga (ver *El reloj* en el baseline). Un número que cambia de ancho tiembla. Celeste agrandó los milisegundos de su reloj. `14_UI_HUD_y_menus` |
| 5 | **(A, C) Aviso de urgencia en un umbral** | Super Mario Bros.: a 100 unidades suena un aviso y la música se acelera. Sin aviso, el cero llega como sorpresa y se lee injusto. Va por el bus de advertencia de `16_Audio_como_gameplay` |
| 6 | **(A) La recarga es un evento visible** | Out Run da tiempo extra en cada checkpoint; mostrarlo como "+N" junto al reloj, como evento, es la recompensa del tramo. *Destilación propia sobre Out Run* |
| 7 | **(A, C) El sobrante vale** | Super Mario Bros. convierte el tiempo que sobra en puntos; Super Monkey Ball da puntos por segundo sobrante y duplica si se termina en menos de la mitad. Sin conversión el reloj solo castiga; con ella, también premia el margen |
| 8 | **(B) Una referencia contra la cual correr** | Mejor tiempo propio, ghost o medalla. Sin referencia, un tiempo es un número sin significado. Trackmania, Neon White |
| 9 | **(B) Delta en cada checkpoint, con signo además de color** | Dice *dónde* se gana o se pierde, no solo cuánto. LiveSplit usa cuatro estados —adelante y ganando, adelante y perdiendo, atrás y recuperando, atrás y perdiendo— más dorado para el mejor segmento. Signo y texto, nunca solo color. `69_LiveSplit_core` |
| 10 | **(B) Reinicio instantáneo desde cualquier punto, en una tecla** | El intento es la unidad: un reinicio con menú multiplica el tiempo sin jugar. Acá ≤ 1 s, más estricto que el ≤ 1.5 s de `15_Muerte_reintento_y_checkpoints`, porque el intento entero dura segundos. *Destilación propia* |
| 11 | **(B) Metas escalonadas derivadas de un tiempo de referencia** | Ver *Baseline: cómo se fijan las metas* |
| 12 | **(C) Un cierre, no un corte** | Bejeweled Blitz detona lo que queda en el tablero al terminar el minuto. El último segundo no puede borrar la jugada en curso sin mostrarla |
| 13 | **(B) El récord declara bajo qué condiciones se hizo** | Celeste muestra al final del capítulo si hubo modo asistido o variantes, y la versión del juego. Récords separados por modo |

---

## Juice / señales de urgencia

| Señal | Qué comunica | Cuidado |
|-------|--------------|---------|
| **Aviso + música más rápida en el umbral** (A) | queda poco | Una vez, en un umbral. Como colchón permanente baja el rendimiento (North y Hargreaves): se compra a propósito, con su costo |
| **Los dígitos cambian de color y escala en los últimos segundos** (A, C) | los últimos segundos | Crecen sin moverse de lugar |
| **"+N s" al recargar** (A) | la recompensa del tramo | Junto al reloj, nunca en el centro de la acción |
| **Delta del checkpoint, 1–2 s en pantalla** (B) | dónde gano o pierdo | Signo + color, cuatro estados |
| **Dorado en el mejor segmento; "nuevo récord" al cruzar** (B) | superación | El evento más grande del intento |
| **Ghost translúcido** (B) | la referencia, en el espacio | Que no tape el camino ni se confunda con un obstáculo |
| **Cierre celebrado** (C) | que terminó, y cuánto se hizo | Bejeweled Blitz: la detonación final |

**Regla del género: el reloj se lee con el rabillo del ojo.** Por eso su posición no se mueve nunca, y la urgencia va primero por audio: la vista está ocupada jugando. *Destilación propia*, cruzada con `16_Audio_como_gameplay`.

---

## Baseline: cómo se fijan las metas

Relaciones, no números sueltos. Se ajustan con jugadores, nunca en el papel.

**Medallas (B)**

```txt
ref     tiempo de referencia: el del autor del nivel, jugado limpio
oro     ≈ ref × 1.05
plata   ≈ ref × 1.20
bronce  ≈ ref × 1.5     (lo medido va de 1.52 a 1.55)
tope    tiempo fijo del desarrollador, por encima del oro — no el récord mundial
```

Calibración: en la campaña de TrackMania² Stadium los cocientes medidos van de 1.04 a 1.08 para el oro, de 1.19 a 1.24 para la plata y de 1.52 a 1.55 para el bronce, ajustados a mano cerca de esa escala. La fórmula por defecto del editor que circula en la comunidad (×1.06 / ×1.2 / ×1.5) **no se pudo verificar**. Neon White pone el tope en una marca fija del desarrollador, distinta del leaderboard. `70_TrackMania2_Stadium_medal_times`

**Límite de la escala:** un porcentaje del tiempo del autor falla donde el tiempo del autor es fácil — en mapas simples, jugadores de nivel plata sacan la marca del autor y las medallas de abajo dejan de significar algo. **La medalla mide la distancia a otros jugadores, no al autor**: con datos, se recalibra contra la distribución real (percentiles). `06_Dificultad_y_curva` pide lo mismo de cualquier umbral.

**La medalla como llave:** en Neon White el oro abre pistas de atajos, el leaderboard y los ghosts de ese nivel. **La pista llega cuando el jugador ya demostró competencia**, no antes — coherente con *primero se pasa, después se corre*.

**Presupuesto de la cuenta regresiva (A)**

```txt
presupuesto del tramo  =  k × tiempo limpio de un jugador competente,   k ≈ 1.5–2
umbral de urgencia     =  25–33% del presupuesto
sobrante               →  puntos, a una tasa fija por segundo
```

Calibración: el aviso de Super Mario Bros. llega a 100 unidades fijas — el 25% en los niveles de 400 y el 33% en los de 300. El bonus doble de Super Monkey Ball por terminar en menos de la mitad implica `k ≥ 2` contra un experto: el borde alto del rango, porque `k` se mide contra un jugador competente, que es más lento. **El valor de `k` es destilación propia, a calibrar en playtest.**

**Duración fija (C):** de 1 a 5 minutos (Bejeweled Blitz 1, Tetris Ultra 2–3, Pac-Man CE 5). La duración tiene que contener una curva entera adentro: Pac-Man CE sube la velocidad con el puntaje y la baja al perder una vida, una dificultad que se adapta dentro de un tiempo que no cambia.

**El reloj**

| Parámetro | Relación | Calibración |
|-----------|----------|-------------|
| Precisión mostrada | nunca más fina que el paso de simulación. A 60 Hz cada tick dura 16.7 ms y hasta la centésima es más fina: o se ubica el cruce de meta *dentro* del tick interpolando, o se simula a 100 Hz, como Trackmania, para que la centésima sea exacta | *Destilación propia*, `01_Bucle_de_simulacion` |
| Inicio | primer input o cruce de la largada | Celeste, convenciones de speedrun |
| Fin | un evento: cruzar la meta, tocar la bandera | — |
| Pausa | congela, con buffer al despausar | Celeste: 0.1 s |
| Reinicio (B) | ≤ 1 s, una tecla | *Destilación propia*, más estricta que el ≤ 1.5 s de `15_Muerte_reintento_y_checkpoints` |

---

## Ghosts y splits, en detalle

**Dos maneras de grabar un ghost, y lo que exige cada una.** Grabar las *entradas* con su tick y re-simular exige que el juego sea determinista, pero el mismo archivo sirve para validar un récord: Trackmania lo hace así. Grabar las *posiciones* por tick no exige determinismo, pero no valida nada. **Si el ghost también tiene que probar un récord, el juego tiene que ser determinista; si solo acompaña, alcanzan las posiciones.** *Lo segundo es destilación propia.*

**Splits.** Un split por tramo con identidad —una curva, una sala—, no por distancia fija: el jugador tiene que poder decir *dónde* perdió. *Destilación propia.* Dos sumas de LiveSplit sirven dentro del juego: la **suma de los mejores segmentos**, que es la carrera perfecta que el jugador ya demostró poder hacer por partes, y el **ahorro posible** por segmento, mejor segmento contra el del récord. Las dos le dicen cuánto margen real tiene.

**IGT y RTA.** El speedrun distingue el tiempo real (RTA, el reloj de la pared) del tiempo de juego (IGT, el que da el juego, con o sin cargas). En speedrun.com el tiempo real es el método por defecto y no se puede quitar. **El juego tiene que exponer su IGT medido en ticks y decir qué excluye**; el tiempo real lo mide la comunidad por su cuenta. `69_LiveSplit_core`

---

## El vecino: el endless runner

El runner es un contrarreloj sin reloj a la vista: **su rampa de velocidad es el reloj**, y su puntaje es el tiempo sobrevivido medido en distancia. Comparte con el subtipo C la competencia por puntaje, y con el B el reintento como unidad. `05_Endless_runner`

---

## Definición de Terminado

```txt
EL RELOJ
[ ] El reloj marca lo mismo a 60 Hz que a 144 Hz
[ ] Arranca con mi primer input o en la largada, no al cargar
[ ] Termina en un evento que veo
[ ] Pausar lo congela, y pausar no me da ventaja
[ ] Lo leo con el rabillo del ojo: no se mueve ni tiembla

LA PRESIÓN (A, C)
[ ] Me avisa una vez cuando queda poco, y lo escucho sin mirarlo
[ ] Cuando recargo tiempo, lo veo
[ ] Lo que sobra me da algo
[ ] Al terminar el tiempo, veo el cierre de mi jugada, no un corte

LA MARCA (B)
[ ] Tengo contra qué correr: mi récord, un ghost o una medalla
[ ] En cada checkpoint sé si voy adelante o atrás, y no solo por el color
[ ] Reinicio desde cualquier punto en una tecla y en menos de un segundo
[ ] Las medallas se escalonan, y la primera la saca un jugador que recién pasó el nivel
[ ] Un récord nuevo se festeja como el evento más grande del intento
[ ] El récord dice en qué condiciones se hizo
```

---

## Aplicación

- **Cuándo se abre este libro:** ante cualquier pedido de contrarreloj, time attack, time trial, speedrun, "terminá antes de que se acabe el tiempo", modo de un minuto o medallas por tiempo — **siempre junto con el libro del género base**, que manda sobre el verbo. Producción lo carga al escribir el `RQ` y decide el subtipo; Game Design lo cruza con el checklist de pilares; Level Design ubica los checkpoints y los splits; UI/UX diseña el reloj y el delta.
- **Qué trae la IA por default sin que se lo pidan:** la pregunta *¿amenaza o mide?*, las table-stakes del subtipo elegido, la escala de medallas con su límite, el presupuesto con su umbral, las reglas del reloj y la Definición de Terminado.
- **Qué NO decide este libro:** el verbo, el género base, si hay leaderboard en línea, la estética del reloj.

## Límites

- **El macroreloj (D) queda afuera.** Majora's Mask, Dead Rising o Minit usan el tiempo como estructura narrativa y de planificación, con otras reglas —qué se conserva al reiniciar, horarios de los NPC, guardado—. Misión de profundización.
- **Las carreras contra rivales** —otros autos, otros jugadores en simultáneo— no están cubiertas: ahí el rival no es el reloj.
- **El leaderboard en línea y el antitrampa** son infraestructura, no experiencia: fuera de este libro.
- **No verificado y declarado:** la fórmula por defecto de medallas de Trackmania, los 60 s por nivel de Super Monkey Ball, los ghosts del staff de Mario Kart, el time attack de Sonic y el reinicio instantáneo de Neon White. Ninguna table-stake se apoya en ellos.
- La evidencia sobre presión de tiempo es **chica**: una tesis de maestría con un solo juego y un estudio de 1999. Alcanza para pedir dosificación, no para fijar umbrales.
- **Ninguna table-stake se validó contra un contrarreloj jugado.** El primer proyecto que lo use es la validación; si su `VE` encuentra un faltante, el libro se actualiza.

---

## Fuentes

Externas, con su ficha en la Biblioteca:

- `69_LiveSplit_core` — LiveSplit, código abierto (MIT o Apache-2.0). Tiempo real contra tiempo de juego, colores semánticos del delta, suma de los mejores
- `70_TrackMania2_Stadium_medal_times` — gamers.org. Tiempos de medalla de la campaña, de los que salen los cocientes medidos
- `58_Time_Pressure_Yildirim` — İ. G. Yıldırım, tesis de maestría, METU, 2015
- `34_Celeste_codigo_fuente_del_juego_y_del_prototipo_PICO` — y su changelog oficial, con la historia del reloj de speedrun
- `65_Fix_Your_Timestep` — Glenn Fiedler. El paso fijo sobre el que se cuenta el reloj

Externas citadas sin ficha propia:

- Super Mario Wiki, *Time Limit* — https://www.mariowiki.com/Time_Limit
- Neon White Wiki (Fandom), *Medals* — https://neonwhite.fandom.com/wiki/Medals
- TetrisWiki, *Ultra* y *40 lines* — https://tetris.wiki/Ultra · https://tetris.wiki/40_lines
- donadigo y Wirtual, *TMX Replay Investigation* — https://donadigo.com/tmx1 (determinismo y validación de replays en Trackmania)
- Dogtor Flashbank, *Medal times for campaign maps in Trackmania* — https://medium.com/@DogtorFlashbank/medal-times-for-campaign-maps-in-trackmania-646845a5232d
- speedrun.com, *Editing a Leaderboard* — https://www.speedrun.com/support/learn/editing-a-leaderboard
- North, A. y Hargreaves, D. (1999), *Music and driving game performance*, Scandinavian Journal of Psychology — https://espace.curtin.edu.au/handle/20.500.11937/37399
- Wikipedia: Out Run, Crazy Taxi, Super Monkey Ball, Pac-Man Championship Edition, Bejeweled Blitz, Majora's Mask, Dead Rising, Minit, ley de Yerkes–Dodson, Flow

Del vault: `01_Bucle_de_simulacion`, `06_Dificultad_y_curva`, `14_UI_HUD_y_menus`, `15_Muerte_reintento_y_checkpoints`, `16_Audio_como_gameplay`, `17_Uncertainty_in_Games`, `02_Plataformero_2D`, `05_Endless_runner`.

**Cobertura declarada:** de las 13 table-stakes, **once** nombran su calibración en una fuente externa y **dos** son destilación propia apoyada en otra pieza: la 6 (recarga visible, sobre el checkpoint de Out Run) y la 10 (reinicio instantáneo, sobre `15_Muerte_reintento_y_checkpoints`). Son destilación propia, y lo dicen donde aparecen: la pregunta *¿amenaza o mide?*, *primero se pasa, después se corre*, la dosificación de la presión, el valor de `k`, la precisión contra el paso de simulación, la regla del ghost y la de los splits.

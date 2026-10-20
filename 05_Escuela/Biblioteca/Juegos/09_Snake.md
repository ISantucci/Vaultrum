---
tipo: juego
genero: Arcade
subtipo: Snake de grilla (un jugador, crecimiento por comida, muerte por choque)
estado: En validación
mision: EST-022_Mision_Lote_Juegos_Web_y_Sigilo
cruza: 02_Game_feel, 03_Definicion_de_terminado, 06_Dificultad_y_curva, 09_Onboarding_y_tutorial, 10_Input_y_respuesta, 14_UI_HUD_y_menus, 15_Muerte_reintento_y_checkpoints, 16_Audio_como_gameplay, 01_Bucle_de_simulacion, 05_Endless_runner, 01_Pong
---

# Libro 09 — Snake
> Noveno libro del estante de Juegos. Género: Arcade / snake de grilla.
> Snake le saca al jugador el poder de parar: **la cabeza avanza siempre y el espacio se lo come el propio jugador**. Lo transversal vive en los Fundamentos; el avance a pasos fijos, en `01_Bucle_de_simulacion`. Acá va lo específico: la grilla, el tick, la cola de input y qué pasa cuando el cuerpo ocupa el tablero.
> **IP:** conceptos destilados + cita. Blockade (Gremlin, 1976) y el Snake de Nokia (Taneli Armanto) son obras con dueño: se citan sus reglas y decisiones, no su código ni sus gráficos. Los parámetros de este libro son **destilación propia, a calibrar en playtest**, salvo donde se cita fuente.
> **Medido:** nada se midió sobre un juego corriendo (a diferencia de `05_Endless_runner`). Los números externos son pocos y están marcados; el resto son relaciones y valores de partida.

---
## Índice del libro
- Loop de experiencia
- Table-stakes
- Juice / game feel
- Movimiento por ticks en grilla
- Cola de input y el giro de 180°
- La comida y el tablero lleno
- Muros y wrap-around
- Choque, desgaste y muerte
- Largo, grilla y dificultad
- Baseline de parámetros
- Variantes, y qué parte del baseline reescribe cada una
- Definición de Terminado
- Aplicación
- Límites
- Fuentes

---
## Loop de experiencia
```txt
LOOP ATÓMICO    (≈ 1 tick, 0.1–0.2 s)  leer dónde está la comida y el cuerpo → elegir recto / girar → el tick ejecuta → ver el resultado
LOOP DE PARTIDA (≈ 1–10 min)           comer → crecer → el tablero se llena → cada giro tiene menos opciones → un choque termina todo
LOOP DE SESIÓN  (≈ 5–20 min)           partida → puntaje o casi-récord → "una más"
```

**El reintento es el juego**, como en `05_Endless_runner`: sin checkpoints, la muerte devuelve al principio. Lo que lo hace tolerable es que el principio es fácil: con el cuerpo corto casi no hay con qué chocar. `15_Muerte_reintento_y_checkpoints`

**Qué lo hace juego:** el objetivo impuesto es comer más; el obstáculo aceptado es no poder parar ni retroceder. Cada comida mejora el puntaje y empeora el problema: **la recompensa es el castigo.** Es la diferencia con el runner, donde la dificultad viene de afuera (velocidad, obstáculos). En Snake viene de adentro (el propio largo).

**Dónde vive la tensión:** en el **margen de maniobra**, la cantidad de movimientos seguros que quedan. Al principio hay tres de tres; con el cuerpo largo, uno de tres, y a veces ninguno. La ventana de anticipación de `05_Endless_runner` se vuelve acá espacial: no cuánto tiempo hay para decidir, sino cuántas celdas hay que planear de antemano.

```txt
tiempo de cruce de la grilla  =  ancho × tick
tiempo de memoria del cuerpo  =  largo × tick     (cuánto tarda una celda recorrida en volver a ser segura)
celdas libres                 =  celdas totales − largo        (− obstáculos, si los hay)
densidad                      =  largo / celdas totales
```

Son las cuatro relaciones que ordenan el libro. La **curva de dificultad** de un Snake es la combinación de `tick` (velocidad) y `densidad` (espacio); `06_Dificultad_y_curva`.

---
## Table-stakes
| # | Table-stake | Por qué es obligatorio |
|---|-------------|------------------------|
| 1 | **Movimiento por pasos de una celda a tick fijo**, desacoplado del dibujo | Si el avance depende de los cuadros, el juego corre distinto según el monitor. Game Programming Patterns y Fix Your Timestep coinciden: paso fijo con acumulador. `01_Bucle_de_simulacion` |
| 2 | **El jugador no puede girar 180°** (ni por una tecla ni por dos dentro del mismo tick) | Es el error clásico: sin la regla, una tecla contraria es una muerte instantánea. Ver *Cola de input* |
| 3 | **Cola de input corta**, una dirección consumida por tick | Con "gana la última tecla" se pierden pulsaciones y dos giros rápidos se vuelven uno. Ver *Cola de input* |
| 4 | **La partida arranca quieta** hasta el primer input, con el cuerpo detrás de la cabeza | El jugador necesita tomar el control antes de que el tiempo corra. Equivale a la zona limpia de `05_Endless_runner`. `09_Onboarding_y_tutorial` |
| 5 | **Crecimiento claro por comida** (cuántas celdas crece y cuándo) | Es la única recompensa. Si el crecimiento no se ve, la comida no se siente |
| 6 | **La comida nunca aparece sobre la serpiente**, y siempre es alcanzable | Una comida bajo el cuerpo o encerrada es una partida rota que parece injusta |
| 7 | **Condición de victoria definida**: qué pasa cuando no queda celda libre | Un juego que se cuelga o falla al llenar el tablero tiene un final sin diseñar. Ver *La comida y el tablero lleno* |
| 8 | **Choque legible**: se ve qué celda mató y contra qué | El jugador tiene que poder culparse. Un choque ambiguo se lee como mala suerte |
| 9 | **Una sola muerte, game over claro y reintento en una tecla**, que no sea una flecha | El jugador está apretando flechas en el momento de morir; si una flecha reinicia, saltea el game over sin verlo. `15_Muerte_reintento_y_checkpoints` |
| 10 | **Puntaje visible** y récord persistente al lado | La meta del género es el récord; si no se ve mientras se juega, no hay meta. `14_UI_HUD_y_menus` |
| 11 | **Pausa, y pausa automática al perder el foco**, con vuelta con margen | Un Snake que sigue corriendo en una pestaña oculta mata al jugador ausente. Tras volver, el tiempo acumulado no se debe ejecutar de golpe: ver *Aplicación* |
| 12 | **La velocidad se elige o se declara** (niveles, o una curva visible) | Un tick único sirve a un solo tipo de jugador. El Snake de Nokia ofrecía niveles de velocidad: el más rápido sin demora, los más lentos con demoras entre pasos (Armanto vía MEL Magazine) |
| 13 | **Gracia al borde**: un instante extra para girar antes de morir contra el muro (no contra el propio cuerpo) | Armanto vio en las pruebas que girar cerca del borde a alta velocidad era muy difícil y agregó una demora de pocos milisegundos antes del choque, para poder girar y seguir (MEL Magazine; It's Nice That). Ver *Choque* |

---
## Juice / game feel
| Efecto | Qué comunica | Cuidado |
|--------|--------------|---------|
| **Bulto que recorre el cuerpo** tras comer, hasta llegar a la cola | que la comida se digiere y el crecimiento llega con retraso | El crecimiento real puede llegar a la cola aunque el bulto se vea desde ya; que no engañe sobre cuándo crece |
| **Pulso de la comida** y pop al aparecer | dónde mirar, sin leer el tablero entero | Que no tape el borde de la celda: es información de colisión |
| **Sonido de comer** que sube de tono con el puntaje o la racha | progreso en un juego sin metas intermedias | Distinto del sonido de choque y del de pausa. `16_Audio_como_gameplay` |
| **Choque: parar el mundo, flash en la celda culpable, un golpe de pantalla corto** | qué pasó y contra qué | El evento más grande de la partida. No sacudir tanto que el jugador no vea qué tocó |
| **Interpolación visual del movimiento entre celdas** | suavidad | Es solo dibujo: la colisión sigue siendo por celda. Ver *Movimiento por ticks* |

**Regla del género: lo que es colisión se ve en la grilla.** Partículas, sombras o glow no pueden hacer que una celda parezca libre u ocupada de más. Destilación propia.

---
## Movimiento por ticks en grilla
El mundo avanza en pasos discretos: cada **tick**, la cabeza se mueve una celda en la dirección vigente, la cola se libera una celda (salvo que esté creciendo) y se evalúa el choque. El tick es el **paso fijo de la simulación**: Game Programming Patterns lo recomienda porque hace todo más simple y estable (física, IA) y permite simular a ritmo constante en hardware distinto, con un acumulador que gasta el tiempo real en pasos completos (no promete resultados idénticos en toda máquina); Fix Your Timestep agrega la interpolación con el sobrante, solo para dibujar. En Snake **el tick de simulación es el tick de juego.**

```txt
cada frame:  acumulador += delta (con tope)
             mientras acumulador ≥ tick:  paso();  acumulador −= tick
             dibujar(interpolando con acumulador / tick)      ← opcional, solo visual
```

**El tick como curva de dificultad.** `tick` chico = menos tiempo entre decisiones. El piso se deriva de una relación, no se elige:

```txt
tick_mín  ≥  reacción / k        k = celdas de previsión que el jugador necesita
```

Con una reacción de diseño de 0.25 s (el supuesto del bot de `05_Endless_runner`; **no** es un dato de Shelton y Kumar, 2010, que miden ≈ 331 ms de reacción visual simple, n = 14) y k = 3 celdas (destilación propia), `tick_mín ≥ 83.3 ms` (el baseline redondea a 85 ms). Con los 331 ms medidos el piso sería 110 ms, y el nivel rápido de 100 ms quedaría por debajo: se declara nivel experto, no baseline para todos (ver *Límites*). **Por debajo de ese piso, el jugador gira a ciegas.** Un giro ocupa un tick y una U, dos: a tick chico, el input tiene que entrar en la cola antes de que el tick lo pida.

---
## Cola de input y el giro de 180°
**El bug clásico.** La serpiente va a la derecha. En un mismo tick, el jugador aprieta *arriba* y enseguida *izquierda*. Si el juego guarda una sola dirección y gana la última, el próximo paso es *izquierda*: la cabeza entra en el cuello y muere. El jugador hizo algo razonable (una U), y el juego lo mató. Comentarios de desarrolladores lo describen igual: dos teclas más rápido que un paso equivalen a una marcha atrás, y con una sola dirección guardada la última pisa a las anteriores (itch.io; DEV Community; GameDev.net).

**Dos defectos, dos reglas:**

```txt
1. validar contra la ÚLTIMA dirección encolada (o la vigente si la cola está vacía), no contra la vigente
   → rechaza: la misma dirección (no aporta) y la opuesta (giro de 180°)
2. consumir UNA dirección de la cola por tick
   → "arriba, izquierda" se ejecuta en dos ticks: sube una celda, después va a la izquierda. Es una U legal
```

Validada contra la vigente (*derecha*), *izquierda* se rechaza como opuesta y la U falla; sin validar, gana *izquierda* y es el bug. Contra la última encolada (*arriba*), *izquierda* es legal.

**Tamaño de la cola.** Corto: **2**, destilación propia. Una cola larga convierte los reflejos en deuda: Launchpad documenta el síntoma (una tecla mantenida llena la cola y la serpiente sigue instrucciones viejas). Con la cola llena, la entrada nueva se descarta. Encolan los **eventos de tecla**, no el estado: mantener apretada una flecha no encola nada (ignorar `event.repeat`).


**El primer input** se valida contra la dirección inicial: si la serpiente arranca hacia la derecha, *izquierda* no arranca la partida.

---
## La comida y el tablero lleno
**Colocación.** La comida se sortea **entre las celdas libres**, no entre todas con reintento: con pocas libres, el sorteo ciego es lento y, con ninguna, no termina. O'Hagan describe el procedimiento típico: un solo ítem a la vez, que reaparece en una casilla vacía al azar. Mantené una lista de libres y sorteá un índice. **Con 0 libres no hay sorteo: hay victoria.**

```txt
celdas libres = celdas totales − largo (− obstáculos)
VICTORIA:  largo = celdas totales (− obstáculos)  →  no queda dónde poner comida
```

La victoria se evalúa **justo después de crecer**, no en el tick siguiente: sino la partida pide una comida que no puede existir. Cota inferior de una victoria: cada comida cuesta al menos un tick, así que dura **≥ (celdas − L0) × tick**; en 20×20 con 150 ms, ≥ 397 × 0.15 s ≈ 59.6 s. Es una cota, no una estimación.

**Alcanzable.** Si la comida cae en una celda que el cuerpo dejó cerrada, se vuelve a sortear; con obstáculos, la conectividad se verifica al generar (ver *Variantes*).

**Ganable.** O'Hagan demuestra que una grilla con un lado par tiene un ciclo hamiltoniano (un recorrido que pasa por todas las celdas y vuelve): recorrerlo en bucle da el puntaje perfecto. En grillas impares por impar no existe; hay un ciclo de largo `celdas − 1` y el perfecto exige pisar la celda salteada. **Tablero de victoria con un lado par**; en impar×impar, O'Hagan advierte evitar comidas en celdas que vuelvan la partida injugable. En su estudio (N = 18, movimiento por turnos), el 6×6 par dio el puntaje máximo en 47.8% de las partidas, contra 35.6% del 5×5 y 3.33% del 7×7.

---
## Muros y wrap-around
| | Muros mortales | Wrap-around (toroide) |
|-|----------------|-----------------------|
| Vecinos de una celda | 2 a 4 (esquinas y bordes) | siempre 4 |
| El borde | es un obstáculo; el centro es el espacio seguro | no existe; no hay "lugar seguro" |
| La comida junto al borde | pide aproximarse con cuidado | es igual de fácil que en el centro |
| Gracia al borde | necesaria (table-stake 13) | no aplica (no hay borde mortal) |

La diferencia no es cosmética: **con muros, la grilla efectiva es menor** (el borde es una región de riesgo y las esquinas son trampas) y la dificultad espacial crece más rápido por comida. Con wrap, el espacio es parejo y el reto es solo el propio cuerpo; es una versión más fácil espacialmente, salvo que la velocidad compense.

---
## Choque, desgaste y muerte
**Regla de la cola.** Moverse a la celda que ocupa la cola **es legal si ese tick la cola se libera** (no hay crecimiento pendiente); es un choque si la serpiente está creciendo. Destilación propia: sin esta regla, una serpiente en círculo de 2×2 muere sin motivo visible.

**Gracia (baseline).** Si el próximo paso es contra el muro (no contra el cuerpo: eso es el castigo del género, y es lo que deja sin gracia al wrap-around) y la gracia no se usó en ese tramo, el juego **no avanza ese tick**, deja entrar un input y reevalúa; si el paso sigue siendo letal en el tick siguiente, muere. Armanto la describe como una demora de pocos milisegundos (sin valor publicado); la de ≤ 1 tick es nuestra versión en pasos, *a calibrar en playtest*.

**Al morir:**

```txt
CHOQUE      el mundo se detiene, flash en la celda culpable, sonido de choque
PANEL       puntaje de la partida y récord, uno al lado del otro
REINTENTO   tecla explícita (Enter / Espacio / clic): habilitada a los 0.3 s
            las FLECHAS (o WASD) nunca reinician: son las que se estaban apretando
AL VOLVER   largo L0, comida nueva, tick inicial, cola de input vacía
```

Cumple `15_Muerte_reintento_y_checkpoints` (0.3 s). **Una sola vida**: según un crítico citado en MEL Magazine, así era en el Nokia.

**Desgaste (variante).** El choque no mata: cuesta `d` segmentos y el juego sigue. Muere si `largo − d < 1`. Tras el golpe hay una invulnerabilidad de **≥ reacción + un tick** para poder girar (≈ 0.25 + 0.15 = 0.40 s ⇒ **3 ticks** a 150 ms; destilación propia). Ver *Variantes*.

---
## Largo, grilla y dificultad
El largo no es un puntaje: es la **densidad** del tablero. Con grilla 20×20 (400 celdas):

```txt
largo   libres   densidad   tiempo de memoria (tick 150 ms)
    3     397       0.8 %       0.45 s
   20     380       5 %         3.0 s      ← largo = ancho: la memoria iguala el cruce de la grilla
  100     300      25 %        15 s
  200     200      50 %        30 s
  300     100      75 %        45 s
```

**Dos efectos distintos:** (1) a más densidad, menos libres, y cada giro tiene menos destinos seguros; (2) a más largo, un tramo recorrido tarda más en volver a estar libre, y el jugador tiene que **planificar con la forma del cuerpo en el futuro**. La velocidad, con el largo, no suma: se multiplica, porque a igual largo un tick menor es el mismo cuerpo en menos tiempo real.

**Tamaño de la grilla.** Más celdas con el mismo tick: más tiempo de cruce (ancho × tick) y más comidas hasta llenar: la partida es más larga, no más difícil por turno. Menos celdas: el tablero se llena antes y las decisiones se vuelven espaciales antes. En O'Hagan, con movimiento automático el 5×5 fue el más difícil para 13 de 18 y nadie llegó al máximo en ninguna grilla; por turnos, la 7×7 puntuó 56.1% del máximo contra 81.7% de la 5×5 (en automático, 19.8% contra 24.7%), y la urgencia percibida fue, en promedio entre tamaños, 5.39 (automático) contra 2.15. **Se lee: el tick pesa más en la experiencia que el tamaño.** Vale para lados de 5 a 7 y 18 participantes; no se extrapola a 20×20.

**Consecuencia de diseño:** si la dificultad crece sola con la densidad, **el tick constante es una curva legítima**: el tick no hace falta como rampa. La rampa de velocidad es una variante, no el baseline.

---
## Baseline de parámetros
Punto de partida, no dogma; todo **destilación propia, a calibrar en playtest**, salvo lo citado. En tiempo y en relaciones.

| Parámetro | Relación | Baseline | Calibración |
|-----------|----------|----------|-------------|
| Grilla | un lado par (ganable con ciclo) | 20 × 20 = 400 celdas | O'Hagan: lado par → ciclo hamiltoniano |
| Largo inicial `L0` | ≥ 3 (se lee como serpiente); en desgaste, `L0 > d` | 3 → 397 libres | derivado |
| Dirección inicial | cuerpo detrás de la cabeza | derecha, quieta hasta el primer input | — |
| Crecimiento por comida | — | +1 celda | O'Hagan: "usualmente +1" en su implementación (Nokia: no verificado) |
| Tick, niveles | cruce = ancho × tick | 200 / 150 / 100 ms ⇒ cruce 4.0 / 3.0 / 2.0 s | referencia: Nokia ofrecía niveles. 100 ms es nivel experto: bajo el piso de 110 ms si la reacción es 331 ms |
| Tick, piso | `≥ reacción / k` | 85 ms (3 × 85 = 255 ms ≥ 250) | reacción de diseño 0.25 s, supuesto del bot de `05_Endless_runner` (no de Shelton y Kumar) |
| Tick durante la partida | constante | no cambia con la comida | la dificultad la pone la densidad |
| Cola de input | corta, 1 por tick, validada contra la última | 2 | ver *Cola de input* |
| Gracia al borde | ≤ 1 tick, una vez por tramo | 1 tick | Armanto: pocos ms, valor no publicado |
| Regla de la cola | libre si la cola se mueve ese tick | sí | — |
| Comida | sorteo entre libres, una a la vez, alcanzable | 1 | O'Hagan (procedimiento típico) |
| Victoria | 0 libres | `largo = 400` | — |
| Muros | mortales | sí (wrap es variante) | — |
| Puntaje | 1 punto por comida = `largo − L0` | — | — |
| Muerte | un choque | sí; contra el muro, con gracia previa; contra el cuerpo, sin gracia | Nokia: una vida |
| Reintento | tecla explícita a 0.3 s; flechas no | — | `15_Muerte_reintento_y_checkpoints` |
| Pausa por foco | se detiene; vuelve con cuenta regresiva de ≈ 3 ticks | — | `05_Endless_runner` (margen al volver) |

**Verificación de la aritmética del baseline:** 20 × 20 = 400; 400 − 3 = 397 libres; 20 × 0.15 s = 3.0 s; 20 × 0.2 s = 4.0 s; 20 × 0.1 s = 2.0 s; piso 85 ms ⇒ cruce 1.7 s; con L0 = 3 y tick 150 ms, la memoria inicial es 3 × 0.15 s = 0.45 s.

---
## Variantes, y qué parte del baseline reescribe cada una
Una variante no le agrega una fila al baseline: **lo pone entero bajo sospecha**. Esta tabla dice qué cambia y qué se revisa.

| Variante | Qué reescribe | Qué hay que re-chequear |
|----------|---------------|--------------------------|
| **Wrap-around** | Muros, gracia, tamaño del tablero efectivo | La gracia desaparece (no hay borde mortal); la regla de la cola pasa a importar cuando largo = ancho; la victoria y el ciclo hamiltoniano no cambian |
| **Obstáculos fijos** (O celdas) | Libres = total − largo − O; victoria = `largo = total − O`; el tablero se genera | Con O = 20 en 20×20: 377 libres al inicio y victoria en largo 380. Las libres tienen que quedar **conexas** (verificarlo al generar) y la comida nunca en una celda cerrada; zona despejada de ≥ k celdas delante de la cabeza al arrancar; ya no vale "un lado par = ganable": hay que comprobar que exista recorrido |
| **Velocidad creciente** | El tick deja de ser constante: `tick(n) = máx(85, 150 − 2n)` ms con `n` comidas | Llega al piso en `n = 33`, con largo 36 y densidad 9%: el piso se alcanza muy temprano y el resto de la partida va a tope, sin respiro. Si el objetivo es la victoria por llenado, el piso tiene que subir o la rampa tiene que terminar antes de la zona densa. La gracia y la cola no se tocan; el cruce baja a 1.7 s |
| **Desgaste** (choque cuesta `d`) | Muerte, `L0`, gracia, panel de choque | Muere si `largo − d < 1`; con `d = 1` y `L0 = 3`, la tercera colisión mata (3 → 2 → 1 → muerte). **El `L0` del baseline sirve solo si `L0 > d`.** La gracia queda redundante y se reemplaza por 3 ticks de invulnerabilidad. El golpe no mueve la cabeza; si no hay ningún paso legal, se recorta `d` más para liberar celda (si no, la serpiente queda trabada) |
| **Modo sin muerte** | Muerte, game over, reintento, puntaje, la meta | Sin game over, **la meta cambia**: llenar el tablero, no sobrevivir. El choque deja el tick sin avanzar; si no hay paso legal, se recorta cola (misma regla anti-traba). El récord pasa a ser el tiempo en llenar |
| **Multijugador tipo Blockade / Tron** | Casi todo | Dos cabezas. Blockade (Gremlin, 1976; diseño de Lane Hauck, programación de Hauck y Ago Kiss): dos jugadores, cada flecha deja una estela sólida; chocar contra cualquier pared, de uno u otro o el borde, da un punto al rival; la partida termina tras un número de choques por jugador que fija el operador, de 3 a 6 (Wikipedia). **No hay comida**: se asume que la estela crece por tick (Wikipedia solo dice que es un muro continuo; no verificado). Libres bajan 2 por tick ⇒ ronda de ≤ `(total − L1 − L2) / 2` ticks: con 400 celdas y L = 3 cada uno, ≤ 197 ticks = **≤ 29.6 s a 150 ms**. Ya no valen: comida, victoria por llenado, regla de la cola (la estela no se libera), puntaje por comida. Hay que resolver cabeza contra cabeza (misma celda) y cruce de cabezas (intercambio de celdas) |

**Chequeo cruzado:** (1) `L0 = 3` mata al primer choque en el baseline, y eso es coherente; en desgaste, solo si `d ≥ 3`, así que el baseline de desgaste usa `d = 1`. (2) El tick de 85 ms del piso asume k = 3; si una variante mide k distinto, el piso se recalcula. (3) La gracia del baseline no aparece en ninguna variante que cambie la muerte. (4) La cola de input es la misma en todas, salvo el multijugador, donde hay una por jugador.

---
## Definición de Terminado
Checklist del género, **sobre el juego corriendo**. `03_Definicion_de_terminado`

```txt
MOVIMIENTO E INPUT
[ ] La serpiente avanza igual de rápido en un monitor de 60 Hz y en uno de 120+ Hz
[ ] Volver a la pestaña después de un rato no hace avanzar el juego de golpe
[ ] Apretar dos flechas rápido (arriba y enseguida izquierda yendo a la derecha) hace una U, no una muerte
[ ] Apretar la dirección contraria sola se ignora
[ ] Mantener apretada una flecha no llena la cola ni deja la serpiente en piloto automático
[ ] Con teclado, flechas y WASD; con dedo, swipe (si está); no se mueve la página
COMIDA Y TABLERO
[ ] La comida nunca aparece sobre el cuerpo
[ ] Se alcanza la victoria llenando la grilla (probar con una 4×4) y el juego lo dice
[ ] El juego no se cuelga con pocas celdas libres ni con ninguna
CHOQUE Y ESTADOS
[ ] Veo contra qué choqué
[ ] La serpiente puede girar justo antes de un muro a la velocidad más rápida (gracia)
[ ] Entrar en la celda de la cola, cuando se libera, no mata
[ ] El game over no se saltea apretando flechas; reinicio en una tecla en < 1.5 s
[ ] Puntaje y récord visibles, el récord sobrevive a cerrar y abrir
[ ] Elijo la velocidad antes de empezar, o veo cómo sube
FEEL
[ ] Comer, pausar y chocar suenan distinto entre sí
[ ] La cabeza se distingue del cuerpo de un vistazo
[ ] Lo que dibuja la grilla coincide con lo que mata
```

---
## Aplicación
- **Cuándo se abre este libro:** ante cualquier pedido de snake, "gusanito", "como el de Nokia", juego de grilla donde se crece al comer, o Blockade/Tron de turnos en celdas. Producción lo carga al escribir el `RQ`; Game Design lo cruza con el checklist al escribir el `GDS`; Level Design lo usa para obstáculos y tamaño de tablero, con la regla de conectividad.
- **Qué trae la IA por default sin que se lo pidan:** las 13 table-stakes, la cola de input validada contra la última dirección, la regla de la cola, el sorteo entre libres con victoria definida, la gracia al borde, el baseline en relaciones y la Definición de Terminado.
- **Qué NO decide este libro:** el tema, el arte, el tamaño exacto, la plataforma, la economía. Eso lo declara el `RQ`.

### Si va al portfolio web

- HTML + CSS + JS sin frameworks, un `<canvas>` 2D con celda de tamaño entero (tablero = ancho × celda; escalar con `devicePixelRatio`). Bucle con `requestAnimationFrame`, `acumulador += delta` **con tope** (por ejemplo, 5 ticks de catch-up máximo; Game Programming Patterns advierte que sin el tope un paso lento deja al juego sin alcanzar el tiempo) y descartar el delta al volver de `visibilitychange`. Teclado con `keydown` (usar `event.code`, `preventDefault` en flechas para que la página no scrollee). Swipe táctil opcional: detectar en `touchmove` con distancia mínima (≈ 24 px, a calibrar), convertir al mismo evento que la tecla y encolarlo, con `touch-action: none` en el canvas. Récord en `localStorage` con `try/catch` (puede estar bloqueado). Lógica (grilla, cola, colisión) separada del dibujo, para probarla sin canvas.

## Límites
- Libro de **experiencia y diseño**; la implementación (estructura de la serpiente, colisión) es materia del `SOL` y de `01_Bucle_de_simulacion`.
- **Ningún número se midió sobre un juego corriendo.** Todos los parámetros del baseline son destilación propia, a calibrar en playtest. No hay validación con jugadores ni con un Snake propio.
- **No verificado:** velocidad, tamaño de grilla y puntaje del Snake de Nokia (las fuentes leídas no los dan); cuántas celdas crece por comida ni cuánto vale cada una **en el Snake de Nokia** (O'Hagan da "usualmente +1" para su propia implementación, que es de donde sale el +1 del baseline); si en Blockade la estela crece a cada tick (se asume; Wikipedia no lo dice); la grilla, la velocidad y si las estelas de Blockade son permanentes (lo leído solo dice que la estela es sólida); qué hace Nokia al llenar el tablero; el intervalo real entre dos pulsaciones de un jugador (el tamaño 2 de la cola y el piso de tick no están calibrados contra eso).
- **Discrepancia de fechas:** Wikipedia (género y Blockade) fecha el Snake de Nokia en 1998; It's Nice That dice que se lanzó en 1997 en el 6110; MEL dice que el 6110 salió en diciembre de 1997 y a la venta a principios de 1998. El año de diseño no se fija: el libro dice solo "Nokia 6110, 1997–1998".
- Las fuentes de input buffering son comentarios de foros y blogs de desarrolladores (itch.io, DEV Community, Launchpad, GameDev.net), no una referencia canónica; describen el síntoma, y la solución (cola de 2, validar contra la última) es destilación propia sobre ellos.
- El estudio de O'Hagan es una tesis con 18 participantes en grillas de 5, 6 y 7 de lado: orienta, no calibra.

---
## Fuentes
Externas leídas (consulta 2026-10-13):

- Wikipedia, *Snake (video game genre)* — https://en.wikipedia.org/wiki/Snake_(video_game_genre). Historia: Blockade (1976), clones (Dominos, Surround 1977), Worm (1978), Nibbles, Rattler Race, Nokia (1998); mecánica básica. No da grilla, velocidad ni victoria.
- Wikipedia, *Blockade (video game)* — https://en.wikipedia.org/wiki/Blockade_(video_game). Gremlin; Lane Hauck (diseño; programación junto a Ago Kiss); noviembre de 1976; reglas (dos jugadores, estela sólida, punto al rival, la partida termina tras 3 a 6 choques fijados por el operador).
- MEL Magazine, *Snake / Nokia 6110 oral history, Taneli Armanto* — https://melmagazine.com/en-us/story/snake-nokia-6110-oral-history-taneli-armanto. Niveles por demora, demora ante el choque, pruebas con colegas, una vida, pausa.
- It's Nice That, *Taneli Armanto, the history of Snake* — https://itsnicethat.com/features/taneli-armanto-the-history-of-snake-design-legacies-230221. 6110, pantalla de 48 × 84 píxeles, demora de pocos ms al girar en el borde, modo de dos jugadores por infrarrojo.
- Robert Nystrom, *Game Programming Patterns: Game Loop* — https://gameprogrammingpatterns.com/game-loop.html. Paso fijo vs. variable, desacople de actualizar y dibujar, tope de catch-up.
- Glenn Fiedler, *Fix Your Timestep* — https://gafferongames.com/post/fix_your_timestep/. Paso fijo, acumulador, interpolación.
- Joseph O'Hagan (2026, Universidad de Glasgow), estudio de Snake como grafo y de la experiencia según tamaño de grilla y tipo de movimiento — https://eprints.gla.ac.uk/395865/1/395865.pdf. Victoria = largo igual al tablero; ciclo hamiltoniano con lado par; N = 18; datos de dificultad.
- GameDev.net (blog), *This snake can move* — https://gamedev.net/blogs/entry/2267763-this-snake-can-move. Perder pulsaciones si se actúa solo sobre la última; cola, una entrada por actualización.
- itch.io (comentarios) — https://itch.io/post/7120264. Dos teclas en un tick provocan giro de 180°.
- DEV Community, *How to build a classic snake game using React* (comentarios) — https://dev.to/bibekkakati/how-to-build-a-classic-snake-game-using-reactjs-5dn8/comments. Rechazar la dirección opuesta; buffer de teclas.
- Launchpad, lista snakes-game — https://archive.lists.launchpad.net/snakes-game/msg00034.html. Una cola de dirección que se llena al mantener una tecla; se arregló vaciándola.

Shelton y Kumar (2010), *Comparison between Auditory and Visual Simple Reaction Times*, Neuroscience & Medicine — https://www.scirp.org/html/4-2400003_2689.htm . Verificada el 2026-10-13: reacción visual simple ≈ 331 ms, auditiva ≈ 284 ms, n = 14. El 0.25 s que usa este libro **no** sale de acá: es el supuesto del bot de `05_Endless_runner`.

Del vault: `02_Game_feel`, `03_Definicion_de_terminado`, `06_Dificultad_y_curva`, `09_Onboarding_y_tutorial`, `10_Input_y_respuesta`, `14_UI_HUD_y_menus`, `15_Muerte_reintento_y_checkpoints`, `16_Audio_como_gameplay`, `01_Bucle_de_simulacion`, `05_Endless_runner`, `01_Pong`.

**Cobertura declarada:** de las 13 table-stakes, las **1, 12 y 13** nombran su calibración en fuente externa (bucle; niveles y demora de Nokia); la **2 y 3** se apoyan en fuentes de foros que describen el síntoma; la **7** se apoya en O'Hagan; las **4, 5, 6, 8, 9, 10 y 11** son destilación propia. Ninguna se validó con jugadores ni con un Snake propio.

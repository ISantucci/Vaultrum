---
tipo: juego
genero: Puzzle
subtipo: Puzzle de piezas que caen sobre una matriz (líneas completas, ritmo creciente)
estado: En validación
mision: EST-022_Mision_Lote_Juegos_Web_y_Sigilo
cruza: 02_Game_feel, 03_Definicion_de_terminado, 06_Dificultad_y_curva, 08_Progresion_y_recompensa, 10_Input_y_respuesta, 14_UI_HUD_y_menus, 15_Muerte_reintento_y_checkpoints, 16_Audio_como_gameplay, 01_Bucle_de_simulacion, 02_Colision_y_consulta_espacial, 05_Endless_runner
---

# Libro 12 — Tetris

> Libro del estante de Juegos. Género: Puzzle / piezas que caen sobre una matriz.
> Lo **transversal** vive en los Fundamentos. Acá va lo **específico**: qué pasa cuando el jugador no controla *qué* le toca sino *dónde y cuándo* lo pone, y la caída automática le va achicando el tiempo para pensar. Es pariente de `05_Endless_runner` (la partida termina con el error, la velocidad es la dificultad) pero con una diferencia de fondo: acá el error **se acumula** en el tablero en vez de matar al instante.
> **IP:** conceptos destilados + cita. El nombre *Tetris*, las siete piezas con su trade dress (colores, forma de la matriz, estética) y el logo los defiende The Tetris Company (TTC), que licencia la marca y retira clones; en 2012 un tribunal de EE.UU. falló contra el clon *Mino* por copiar el tamaño del área de juego y las formas de los bloques; fue un fallo de copyright, no de trade dress (Wikipedia, *The Tetris Company*). Las **reglas** no son lo protegido, pero un juego propio va con **otro nombre y arte propio**: misma lógica que la decisión del portfolio de tomar la mecánica y no el arte. Lo que acá se llama "pieza I", "T", etc. son letras de la literatura del género, no un diseño a copiar.
> **Medido:** no. Todo número sale de la Tetris Wiki, la Hard Drop wiki, el foro Tetris Concept, una guía de terceros (Gamertag Mythras), una nota de prensa (Stickgold) o Wikipedia, leídos el 2026-10-13, o es aritmética propia sobre ellos (recalculada con Python); lo marcado "destilación propia" va a calibrarse jugando. Frames a 60 Hz salvo el NES (≈60.0988 Hz).

---

## Índice del libro

- Loop de experiencia
- Table-stakes
- Juice / game feel
- Las siete piezas
- El aleatorizador: bolsa de 7 contra azar puro
- Gravedad por nivel: la curva es la dificultad
- Lock delay y reseteos
- Rotación: SRS y wall kicks
- Hold, ghost piece y preview
- Soft drop, hard drop y DAS/ARR
- Puntaje por líneas y combos
- Condición de derrota y garantías de jugabilidad
- Baseline de parámetros
- Variantes, y qué parte del baseline reescribe cada una
- Definición de Terminado
- Aplicación
- Límites
- Fuentes

---

## Loop de experiencia

El género se define por una asimetría: **la pieza la elige el azar y la ubicación la elige el jugador**, mientras una gravedad cada vez más rápida le saca el tiempo. Nada se destruye por golpear: las líneas completas *desaparecen* y lo que no se completa *queda*. El jugador no pelea contra un enemigo; pelea contra su propio tablero.

```txt
LOOP ATÓMICO   (≈0.5–3 s)      ver la pieza (y la siguiente) → decidir columna y giro → mover, girar, soltar → la pieza traba
LOOP DE PARTIDA (≈3–15 min)    el tablero se llena y se vacía → la gravedad sube de nivel → un error se acumula hasta que ya no entra la pieza
LOOP DE SESIÓN  (≈10–30 min)   partida → puntaje o tiempo propio → "una más"
```

**La unidad es el tablero, no la pieza**: cada decisión es barata y reversible un rato, y cara cuando se acumula. Lo que mantiene el "una más" es que el fracaso se ve venir (las columnas suben) y que siempre hubo una pieza que habría salvado la partida. `15_Muerte_reintento_y_checkpoints`

**Qué lo hace juego y no juguete:** hay un objetivo impuesto (completar líneas, sobrevivir, llegar a un número) y un obstáculo aceptado (la caída no se pausa y las piezas no se eligen). Es un puzzle *bajo presión de tiempo*: el mismo problema espacial sin gravedad es un rompecabezas. `01_Loop_de_experiencia`

**Dónde vive la tensión:** en la relación entre **tiempo de decisión** y **complejidad del tablero**. Con el tablero casi vacío todo se perdona; con la pila alta cada pieza es un problema y el tiempo ya no alcanza. La curva de gravedad es la dificultad, y el azar de las piezas es el ruido que ese diseño tiene que acotar (ver aleatorizador). `06_Dificultad_y_curva`

Un dato de contexto: Pajitnov lo hizo a partir de los pentominós (Wikipedia, *Alexey Pajitnov*, da la primera versión terminada el 6 de junio de 1985; la página *Tetris* de Wikipedia dice que las fuentes varían: junio de 1984, primavera de 1985 según un documental de la BBC, 1985 en una entrevista de 1993 y 1984 en un recuerdo reportado en 2024: **fecha de origen discrepante, 1984–1985, sin resolver**), con una primera versión sin niveles ni puntaje que igual lo mantenía jugando en el trabajo: el núcleo funciona **antes** de la rampa y el puntaje. Y el "efecto Tetris" (Stickgold et al., 2000) muestra cuánto se interioriza: 17 de 27 participantes soñaron piezas cayendo al dormirse, incluidos 3 de 5 amnésicos.

---

## Table-stakes

Lo que un Tetris **no puede no tener** para estar terminado.

| # | Table-stake | Por qué es obligatorio |
|---|-------------|------------------------|
| 1 | **Tablero de 10 columnas por 20 filas visibles** (más filas ocultas arriba) | Es la relación que todo el género asume: una línea son 10 celdas = 2.5 piezas de 4 celdas. Cambiar el ancho cambia cuántas piezas arman una línea y rompe cada otro número del libro. La Guideline fija 10×20 con un búfer oculto de otras 20 filas (Tetris Wiki, *Tetris Guideline*) |
| 2 | **Las siete piezas de 4 celdas**, todas | Los siete tetrominós (contando J/L y S/Z como distintos) son todas las formas de 4 celdas; con menos, hay huecos que ninguna pieza llena y la partida se decide por el azar de la cola. *Destilación propia.* Ver *Las siete piezas* |
| 3 | **Aleatorizador que acote las rachas** (bolsa de 7 o equivalente) | El azar puro deja 12 piezas sin la larga con probabilidad ≈ 16 % (aritmética propia sobre 6/7). Una racha así mata una partida sin que el jugador haya errado. Ver el capítulo |
| 4 | **Gravedad que sube por nivel y llega a un tope** | Sin rampa no hay partida; sin tope, la partida termina por imposibilidad física. Ver *Gravedad por nivel* |
| 5 | **Rotar, mover y soltar responden en el cuadro en que se aprieta** | El jugador ubica a decenas de movimientos por partida; un cuadro de retraso a gravedad alta es una pieza mal puesta. `10_Input_y_respuesta` |
| 6 | **Autorepetición del movimiento lateral (DAS/ARR)** | Cruzar el tablero sin tocar diez veces la tecla; sin ella el ancho del tablero cuesta más que cualquier decisión. Ver el capítulo |
| 7 | **Rotación con patadas (wall kicks) o una regla clara de qué pasa si no entra** | Sin ella, una pieza pegada a la pared o al piso simplemente no gira (Tetris Wiki, *SRS*) y el jugador pierde piezas por un detalle de colisión, no de decisión |
| 8 | **Preview de la siguiente pieza** | Planificar un movimiento adelante es lo que convierte el juego en puzzle y no en reflejo. La Guideline lo muestra con la próxima arriba; muestra hasta seis en algunos juegos |
| 9 | **Ghost piece (sombra de aterrizaje)** | Reduce errores de ubicación, sobre todo a quien suelta rápido (Tetris Wiki, *Ghost piece*). La Hard Drop wiki la lista como regla indispensable de la Guideline; la Tetris Wiki la presenta como ayuda que a veces se puede desactivar |
| 10 | **Hard drop (suelta instantánea) y soft drop (caída acelerada)** | El jugador decide su propio ritmo cuando ya resolvió la pieza; sin ellos espera la gravedad |
| 11 | **Fin de partida legible y reintento en una tecla** | Un tablero lleno no tiene por qué mostrar quién lo mató: el game over tiene que decir "no entró la pieza" y dejar volver rápido. `15_Muerte_reintento_y_checkpoints` |
| 12 | **Pausa y puntaje/nivel/líneas visibles** | La pila alta exige pensar; sin pausa el jugador pierde sin estar. El HUD reduce a tres números lo que importa. `14_UI_HUD_y_menus` |
| 13 | **Una pieza nunca nace ya muerta sin que el juego lo diga** | Si el espacio de aparición está ocupado, la partida termina ahí y se ve por qué (block out). Ver *Condición de derrota* |

**Inherito de `05_Endless_runner`** el principio de que el reintento es parte del juego: acá el tablero cuesta todo lo jugado, y lo que lo vuelve tolerable es que arrancar es fácil y rápido.

---

## Juice / game feel

| Efecto | Qué comunica | Cuidado |
|--------|--------------|---------|
| **Sonido y destello por línea; más grande por 4 líneas** | que el esfuerzo valió; premia la jugada de riesgo | El de cuatro líneas tiene que sonar distinto de uno, doble y triple. `16_Audio_como_gameplay` |
| **Demora de la limpieza** | que *algo pasó*, y tiempo para leerlo | TGM y Tetris DS esperan 400–700 ms (Tetris Wiki, *Line clear*): más largo se vuelve espera, más corto no se lee |
| **Tick breve al trabar la pieza** | que ya no se mueve, sin mirar el contador | Distinto del movimiento: es el único aviso de que se acabó el lock delay |
| **Pieza cae dibujada arriba, ghost más tenue** | dónde va a caer sin confundir ghost con celdas fijas | Algunos jugadores confunden el ghost con la pila (Tetris Wiki): contorno o transparencia, nunca igual al bloque fijo. `14_UI_HUD_y_menus` |
| **Música que acompaña los niveles** | progreso en una partida sin hitos | En *Tetris Effect* los bajos y el fondo cambian con las líneas y por etapa (GamesBeat) y su director dice que el sonido es parte esencial del diseño (Mizuguchi, GamesBeat). Es referencia, no requisito |
| **Pulso del tablero al subir de nivel** | que se aceleró, antes de que se sienta | Que no tape la fila de aparición |

**Regla del género:** el feel de Tetris vive en el **movimiento de la pieza**, no en los efectos. Que mover, girar, soltar y trabar respondan al instante pesa más que cualquier partícula. `02_Game_feel`

**La zona de aparición es sagrada**, igual que el borde de entrada en el runner: nada de popups ni HUD sobre las filas donde nacen las piezas ni sobre el preview. *Destilación propia.*

---

## Las siete piezas

Son los siete tetrominós: **I** (barra de 4), **O** (cuadrado), **T**, **S**, **Z**, **J** y **L**. Cada una es un problema distinto: la I limpia cuatro líneas de golpe, la O no tiene giro útil, la S y la Z se parecen y no encajan igual (los "snakes"), la J y la L son espejos, y la T permite el mayor número de apoyos. Que se *lean* de un vistazo importa porque el jugador las reconoce a velocidad, no las analiza. Con 4 celdas por pieza y 10 columnas, **25 piezas arman 10 líneas** (100 celdas, aritmética propia).

**Spawn:** todas nacen horizontales, la I y la O centradas y las otras tres de ancho 3 corridas a la izquierda; J, L y T nacen con el lado plano hacia abajo (Tetris Wiki, *SRS*; Hard Drop wiki, *Guideline*). Nacen en las filas 21 y 22 y caen en el acto (Tetris Wiki, *Guideline*). **Color** por pieza: ayuda a leer, pero los colores de la Guideline son del trade dress: usá una paleta propia con la misma función de distinguir las siete. *Destilación propia.*

---

## El aleatorizador: bolsa de 7 contra azar puro

El azar puro (cada pieza independiente, 1/7) no tiene memoria: la próxima no depende de las anteriores. De ahí salen dos problemas: **inundación** (varias piezas iguales seguidas) y **sequía** (muchas piezas sin la que hacía falta). La bolsa de 7 los acota con una regla: se baraja una bolsa con las siete, se reparte entera, y recién después se baraja otra (Tetris Wiki, *Random Generator*; Hard Drop wiki).

```txt
RELACIÓN        máxima racha sin una pieza dada (sequía)
bolsa de 7      12 piezas   (la pieza al principio de una bolsa y al final de la siguiente: 6 + 6)
azar puro       sin tope; P(12 seguidas sin una pieza) = (6/7)^12 ≈ 15.7 %, P(20) ≈ 4.6 %, P(30) ≈ 1 %   (aritmética propia)
```

Datos citados: con bolsa, la racha de S y Z se limita a 4 y la fuente da la secuencia «SZ|Z», de donde se infiere (inferencia propia) que dos piezas iguales seguidas solo pueden darse en la costura entre bolsas; hay 7! = 5.040 órdenes por bolsa (Tetris Wiki). La fuente da el tope de 12 solo para la I; para las demás es simetría de la regla (recalculado por simulación: máximo 12). El **NES** no usa bolsa: tira un dado de 0 a 7 y, si sale lo mismo que la pieza anterior (o el valor sobrante), tira otra vez entre 0 y 6 y deja pasar lo que salga (Tetris Wiki, *Tetris (NES, Nintendo)*). Eso reduce las repeticiones (≈ 1 de 28 contra 1 de 7 en azar puro) pero **no acota las sequías**: 12 piezas sin la I ocurren ≈ 12 % de las veces (Gamertag Mythras, comparativa de aleatorizadores; cifras de esa fuente, no recalculadas). Y TGM usa un historial de las últimas 4 piezas con rerolls, que frena inundaciones pero no sequías (Tetris Concept, *Randomizer Theory*).

**Qué le hace al diseño:** la bolsa hace **planificable** la cola: el jugador sabe que en las próximas 7 piezas está cada una. Con azar puro, una estrategia segura es apilar plano y esperar a la I; con bolsa, se puede apostar a 4 líneas porque la I va a llegar. **El aleatorizador reescribe qué estrategias son racionales.** Y el hold reduce inundaciones y sequías en cualquier esquema (Tepples, citado en Tetris Concept). **Garantía mínima para un juego propio:** bolsa o equivalente, y un tope de sequía que se pueda decir en una frase.

---

## Gravedad por nivel: la curva es la dificultad

La gravedad es la velocidad de caída automática, medida en celdas por cuadro (G) o en tiempo por fila. 1 G = 1 celda por cuadro, 20 G se ve como caída instantánea (Tetris Wiki, *Drop*). **La curva de gravedad es la curva de dificultad:** el jugador no se enfrenta a piezas más difíciles sino a menos tiempo por pieza. `06_Dificultad_y_curva`

```txt
Guideline: tiempo por fila(nivel) = (0.8 − (nivel−1)·0.007)^(nivel−1)    segundos      (Tetris Wiki, Marathon)
nivel 1    1.00 s por fila  → 20 s de arriba a abajo en 20 filas
nivel 5    0.36 s            nivel 10   0.064 s (1.3 s de punta a punta)
nivel 15   0.0071 s          (≈ 2.4 G; 0.14 s de punta a punta)      nivel 19  ≈ 20 G
NES (NTSC): nivel 0 = 48 cuadros por fila (0.80 s) · nivel 9 = 6 (0.10 s) · niveles 10–12 = 5 (0.083 s) · nivel 29+ = 1 cuadro por fila
```

La fórmula la verifiqué recalculándola: los valores en G de la tabla de la fuente coinciden (nivel 10 ≈ 0.26 G, nivel 15 ≈ 2.36 G). Cálculos de tiempo: 48/60.0988 = 0.799 s; 6/60.0988 = 0.0998 s. **Forma:** exponencial: cada nivel multiplica la velocidad por ≈ 1.26 al principio y por ≈ 1.6–1.7 entre el 13 y el 18 (cociente de la tabla de la fuente); lenta al principio, brutal pasando el nivel 13 (0.92 G → 36.6 G en el 20, según la tabla de la fuente). **Cuándo sube:** la Guideline pide **10 líneas por nivel** con meta fija y tope en el 15 (150 líneas totales, ≈ 375 piezas, aritmética propia); el esquema viejo era 5 × nivel líneas y tope en 600 (Tetris Wiki, *Marathon*). Con *Endless*, la gravedad deja de subir en el tope hasta perder. El NES sube un nivel cada 10 líneas una vez pasado el umbral que depende del nivel inicial (Tetris Wiki, NES).

**Hay un piso del juego:** pasado cierto nivel el jugador no puede mover la pieza antes de que caiga. Los juegos lo resuelven con **lock delay** (siguiente capítulo) o con un entry delay más largo; el NES lo resuelve distinto: a nivel 29 cae una fila por cuadro y el entry delay es de 10–18 cuadros según la altura de traba (Tetris Wiki, NES).

---

## Lock delay y reseteos

Al apoyarse, la pieza no traba al instante: espera un **lock delay**. La Guideline fija **0.5 s** cuando la gravedad es menor de 20 G, y en 20 G lo acorta con cada nivel (Tetris Wiki, *Guideline*). Es lo que le deja al jugador una última corrección de columna o giro en el piso: sin él, a gravedad alta toda pieza se pone donde cae.

```txt
RESETEO         qué reinicia el temporizador                 efecto
infinity        cualquier movimiento o giro, sin límite       se puede flotar para siempre
move reset      cualquier movimiento o giro, tope de 15       tiempo para ajustar, pero no para estirar la partida
step reset      solo bajar una fila                           casi no deja ajustar
```

Tope de 15 y modo de reseteo: de la página de la Guideline de la Tetris Wiki (los demás wikis consultados no dan el 15; ver Límites). **Relación:** el delay compra tiempo de ajuste; el tope de reseteos impide que ese tiempo se estire sin fin. Equivalencias propias: 0.5 s = 30 cuadros a 60 Hz. Más corto aprieta (TGM2 usa hasta 15 cuadros en su modo de más presión y TGM3 baja a 8, Tetris Wiki y Hard Drop wiki, *Lock delay*). Un juego propio que no tiene lock delay **debe** tenerlo si tiene gravedad alta; si no, es el NES con gravedad lenta.

---

## Rotación: SRS y wall kicks

El **SRS** es el sistema de la Guideline. Cada pieza tiene cuatro estados (el de aparición, uno a cada lado y uno a 180°) y gira alrededor de un punto. **El problema que resuelve:** una rotación pura puede chocar con la pared, el piso o la pila aunque haya lugar a una celda de distancia. El SRS prueba **hasta 5 posiciones** (la básica y 4 desplazamientos), y si todas están ocupadas la rotación falla. Hay 8 transiciones posibles (4 estados × 2 sentidos) y por eso 8 juegos de desplazamientos; J, L, S, T y Z comparten una tabla, la I tiene la suya y la O no necesita patadas (Tetris Wiki, *SRS*).

Además, el estado de aparición de J, L, S, T y Z "flota" sobre su caja, y por eso necesitan patadas contra el piso, no solo contra la pared. Rotaciones **reversibles**: girar y des-girar vuelve a donde estaba. **Qué copiar:** el *principio* (un orden de pruebas, reversible, que decide cuánto "perdona" el juego) y no la tabla, que para un juego propio se diseña y se prueba, y que de todos modos citamos de la fuente sin copiarla. Tabla propia mínima para empezar: sin patada, o 1–2 desplazamientos horizontales. *Destilación propia, a calibrar.*

---

## Hold, ghost piece y preview

- **Hold:** guarda la pieza activa; si ya había una, se intercambian y la que volvió aparece arriba. No se puede usar otra vez hasta que la pieza trabe (Hard Drop wiki, *Hold piece*; Tetris Wiki, *Guideline*). Nació en *The New Tetris* para facilitar el modo cuadrados, y es controvertido: algunos lo consideran demasiado fácil (Hard Drop wiki). Reescribe la estrategia: convierte la pieza equivocada en una pieza para después.
- **Ghost piece:** dibuja dónde aterrizaría la pieza. No afecta a la jugabilidad y puede apagarse (Tetris Wiki). Se recomienda que la pieza activa se dibuje por encima.
- **Preview:** la Guideline muestra las próximas con la más cercana arriba y recomienda al menos tres; la cantidad exacta es decisión de cada juego (Hard Drop wiki, que marca "recomendado, no obligatorio"). **Relación:** cuantas más piezas se ven, más se planifica y menos pesa el azar; con una sola, el juego es casi reflejo.

**Combinación:** preview + hold + bolsa de 7 le dan al jugador información suficiente para casi eliminar la mala suerte. Quitar uno solo (el NES no tiene hold ni bolsa) devuelve peso al azar. Cada pieza de información se pide **o se saca a propósito**, no se omite por descuido.

---

## Soft drop, hard drop y DAS/ARR

**Soft drop:** acelera la caída sin trabar la pieza; la velocidad la fija cada versión (Tetris Zone usa 20 veces la gravedad del nivel, Tetris Wiki, *Guideline*). **Hard drop:** baja y traba en el acto, sin lock delay (Tetris Wiki, *Hard drop*); la Guideline lo pide como tecla distinta. En teclado, el hard drop va en la barra espaciadora.

**DAS** (delayed auto shift) es el retardo entre apretar la dirección y que empiece la autorepetición; **ARR** (auto repeat rate) es la frecuencia de esa repetición (Hard Drop wiki, *DAS*). Es **input**: la tecla sostenida tiene que mover una vez, esperar y repetir. `10_Input_y_respuesta`. El NES usa 16 cuadros de retardo y 6 entre repeticiones (Tetris Wiki, NES): 16/60.0988 = 0.27 s y 6/60.0988 = 0.10 s, esto es, **10 pasos por segundo**, y la fuente lo cataloga como "DAS lento". Los juegos más modernos consideran rápida una repetición de 20 Hz o más (Tetris Wiki, *DAS*). **El retardo existe** para poder dar *un* paso con un toque sin que se dispare la repetición; sin él, mover una columna es imposible con precisión.

**Si el juego va en web:** el teclado trae su propia autorepetición del sistema, que el programa no controla y varía entre usuarios y navegadores (Tetris Wiki, *DAS*, lo marca para juegos que usan la del sistema). Por eso: **implementar DAS/ARR propios** sobre `keydown` y `keyup`, ignorando el evento repetido del sistema. Valores a calibrar (destilación propia): retardo ≈ 0.17 s, repetición ≈ 0.03–0.05 s, ambos configurables.

---

## Puntaje por líneas y combos

**La relación que ordena el puntaje:** completar más líneas con **una sola pieza** vale más que la suma de las mismas líneas de a una. Guideline, con el nivel anterior a la limpieza (Tetris Wiki, *Scoring*): simple 100 × nivel, doble 300, triple 500, **Tetris (4 líneas) 800**, todos × nivel; back-to-back en limpiezas difíciles × 1.5; combo 50 × cuenta × nivel; soft drop 1 punto por celda y hard drop 2 por celda. Cuatro simples valen 400 × nivel y un Tetris 800 × nivel: **el doble**; con back-to-back (1200 × nivel), el triple. **NES** (misma fuente): 40, 100, 300 y 1200 por 1 a 4 líneas, × (nivel + 1): un Tetris vale **7.5** veces cuatro simples.

El NES premia el riesgo más que la Guideline. Un puntaje con esa forma fabrica una **decisión** en cada tablero: ¿cobro lo que tengo o espero la barra? Y esa decisión es lo que lo hace puzzle. Más allá de las limpiezas, los T-spins y las limpiezas perfectas se reconocen en la Guideline; la fuente no da más de lo citado y acá no se destilan. `08_Progresion_y_recompensa`

---

## Condición de derrota y garantías de jugabilidad

Las formas de perder, según la Tetris Wiki (*Top out*):

```txt
BLOCK OUT    una pieza nace solapando al menos una celda de la pila            (la usan casi todos)
LOCK OUT     una pieza traba entera por encima del techo visible               (Guideline)
GARBAGE OUT  tras recibir basura queda una celda por encima del techo         (versus; "top out" en la Guideline)
```

El NES es una excepción: deja trabar la pieza solapada, y a veces se puede mover o rotar fuera de ese estado (misma fuente). **Garantías para un juego propio:** (1) la pieza que nace siempre cabe en un tablero vacío; (2) el game over dice *por qué* (la pieza que no entró queda dibujada); (3) si hay lock out, la fila oculta existe y cuenta (la Guideline tiene un búfer de 20 filas); (4) la partida no puede perderse en los primeros segundos sin tocar nada: a 1 s por fila (nivel 1) una pieza tarda ≈ 20 s en bajar las 20 filas. *Destilación propia, aritmética sobre la tabla de gravedad.* El resto de la jugabilidad lo garantiza el aleatorizador: sin sequía infinita, siempre hay salida.

---

## Baseline de parámetros

Punto de partida para un Tetris **moderno estilo Guideline**, en **tiempo** y relaciones. Se ajusta jugando.

| Parámetro | Relación | Baseline | Calibración |
|-----------|----------|----------|-------------|
| Tablero | ancho × alto | 10 × 20 visibles + 2 ocultas de aparición como mínimo | Guideline: 10 × 20 + búfer de 20 (Tetris Wiki) |
| Piezas | cuántas celdas | 7 tetrominós, 4 celdas | todos los juegos del género |
| Aleatorizador | sequía máxima | bolsa de 7: máx. 12 sin una pieza dada | Tetris Wiki; 6 + 6 |
| Gravedad nivel 1 | tiempo por fila | ≈ 1 s | Guideline: 1.00 s; NES nivel 0: 0.80 s |
| Curva de gravedad | forma | exponencial decreciente, `(0.8 − (n−1)·0.007)^(n−1)` s | Guideline; tope en nivel 15 (2.4 G) o 20 G |
| Líneas por nivel | — | 10 | Guideline (meta fija); NES 10 una vez pasado el umbral del nivel inicial |
| Lock delay | tiempo en el piso | 0.5 s = 30 cuadros a 60 Hz | Guideline |
| Reseteos | tope de movimientos/giros | 15 | Guideline (Tetris Wiki) |
| Línea completa | demora de limpieza | 0.4–0.7 s | TGM y Tetris DS |
| DAS / ARR | retardo y repetición | ≈ 0.17 s y 0.03–0.05 s, configurables | destilación propia, a calibrar; NES: 0.27 s y 0.10 s |
| Soft drop | múltiplo de la gravedad | ≈ 20× | Tetris Zone; varía por versión |
| Hard drop | — | instantáneo y sin lock delay | Guideline |
| Preview | piezas visibles | 3 (hasta 6) | Hard Drop wiki / Tetris Wiki |
| Hold | usos | uno por pieza hasta que trabe | Guideline |
| Puntaje | relación Tetris / cuatro simples | 2× (3× con back-to-back); NES 7.5× | Tetris Wiki, *Scoring* |

**Chequeo de coherencia (aritmética propia):** a nivel 15 (0.007 s por fila) la pieza cruza 20 filas en 0.14 s, así que ahí el lock delay de 0.5 s ya es lo único que deja mover la pieza: por eso el baseline **no puede** tener gravedad creciente sin lock delay.

---

## Variantes, y qué parte del baseline reescribe cada una

Una variante no le agrega una fila al baseline: **lo pone entero bajo sospecha.** Esta tabla dice dónde mirar primero.

| Variante | Ejemplos | Qué reescribe |
|----------|----------|---------------|
| **NES clásico** | Tetris (Nintendo, NES) | Sin hold (la ficha lo marca), sin bolsa (reroll de una vez), DAS lento (16/6 cuadros), gravedad por cuadros (48 → 1) y puntaje × (nivel + 1). El azar pesa más, las sequías de la I son reales, y el jugador planifica menos. Cambia aleatorizador, input, puntaje y la forma de la curva |
| **Guideline moderno** | Tetris Effect, Tetris Worlds, juegos con licencia | Bolsa de 7, hold, ghost, preview, SRS, lock delay con reseteos, 150 líneas. Es el baseline de este libro |
| **Marathon** | modo estándar | Ver la rampa de niveles hasta el 15 (150 líneas) o *Endless* (gravedad plana al tope). Reescribe el final: del tope de nivel a "hasta que se pierde" |
| **Sprint / Ultra** | Guideline | Cambian el **objetivo**: terminar un número de líneas lo antes posible, o sumar puntos en un tiempo. La gravedad pierde peso y pesan DAS, hard drop y eficiencia. El número de líneas de Sprint y el tiempo de Ultra **no los verifiqué** (ver Límites) |
| **Versus con basura** | Tetris DS, Tetris 99, juegos online | Cambia la condición de derrota (garbage out), agrega la tabla de envío: simple 0, doble 1, triple 2, Tetris 4 líneas, T-spin doble 4 y perfecta 10, más un bono por back-to-back (+1 o +2 o +3 según la limpieza; +2 al Tetris); las limpiezas descuentan basura entrante (Tetris Wiki, *Garbage*). El tiempo de la partida lo pone el rival, no la gravedad |
| **Variantes con "Zone" o foco** | Tetris Effect | Un medidor que congela el tiempo y acumula líneas para limpiarlas juntas (GamesBeat). Reescribe la relación entre puntaje y tiempo |

---

## Definición de Terminado

Checklist del género. Se corre **sobre el juego corriendo**, no sobre el código. `03_Definicion_de_terminado`

```txt
TABLERO Y PIEZAS
[ ] El tablero es de 10 × 20 y se ve entero, con las filas de aparición fuera de la vista o apenas insinuadas
[ ] Salen las siete piezas, y las siete se distinguen sin esfuerzo
[ ] En 100 piezas ninguna falta más de 12 seguidas, y jamás veo tres iguales juntas
[ ] Las filas completas desaparecen y las de arriba bajan sin dejar huecos raros

CONTROL
[ ] Mover, girar y soltar responden en el mismo cuadro en que aprieto
[ ] Mantener izquierda o derecha mueve una vez, espera y repite; soltar frena de inmediato
[ ] Girar pegado a la pared o al piso no falla por un detalle: la pieza se acomoda o el juego lo explica
[ ] La ghost piece muestra donde cae, y no se confunde con la pila
[ ] El hard drop traba al instante; el soft drop acelera sin trabar
[ ] (Si hay hold: es opcional en el alcance mínimo) funciona una vez por pieza y no deja usarlo dos veces seguidas
[ ] Veo al menos las próximas tres piezas

RITMO Y PARTIDA
[ ] El nivel 1 se puede jugar sin apuro; el 10 aprieta; el tope no es imposible de jugar
[ ] La pieza no traba al instante al tocar: da tiempo de corregir, y ese tiempo no se estira para siempre
[ ] Veo puntaje, nivel y líneas, y el nivel sube cuando debe
[ ] Cuatro líneas de una vez se sienten distinto, suenan distinto y puntúan más que cuatro de a una
[ ] Si el espacio de aparición está ocupado, el juego termina y se ve la pieza que no entró
[ ] Reinicio en una tecla y en menos de un segundo y medio
[ ] Cambiar de pestaña pausa el juego y al volver no cae una pieza sin avisar
[ ] El récord sobrevive a cerrar y volver a abrir

FEEL
[ ] Mover, girar, trabar y limpiar suenan distinto entre sí
[ ] Nada tapa las filas de aparición ni el preview
[ ] El juego va igual de rápido en un monitor de 60 Hz y en uno de 120+ Hz
```

Un Tetris que se mueve y limpia líneas pero no tilda **Control** y **Ritmo y partida** es la demo técnica que obliga a gastar prompts en trabajo remedial.

---

## Aplicación

- **Cuándo se abre este libro:** ante cualquier pedido de "tetris", "juego de piezas que caen", "puzzle de bloques" o "match de líneas". Producción lo carga al escribir el `RQ`; Game Design lo cruza al escribir el `GDS`; Level Design lo usa solo en versus o modos con tablero inicial.
- **Qué trae la IA por default sin que se lo pidan:** las 13 table-stakes, bolsa de 7, curva de gravedad con tope, lock delay con reseteos acotados, DAS/ARR propios, ghost, hold, preview, y la Definición de Terminado entera.
- **Qué NO decide este libro:** el nombre, el arte, la música, el modo de juego ni la plataforma. Eso lo declara el `RQ`.
- **Si va al portfolio web:** HTML + CSS + JS sin frameworks, un `<canvas>` 2D, teclado. El tablero es una matriz 10 × 22 (20 visibles y 2 de aparición) y cada pieza una lista de 4 celdas con su estado de rotación. **Bucle de paso fijo** con acumulador (`01_Bucle_de_simulacion`): la gravedad, el lock delay y DAS/ARR se expresan **en segundos**, nunca por cuadro, para que el juego vaya igual a 60 y a 144 Hz; el dibujo interpola o simplemente dibuja el último estado. La colisión de pieza contra tablero es una consulta de 4 celdas (`02_Colision_y_consulta_espacial`). Nombre y arte propios.
  - **Alcance mínimo sólido:** tablero 10 × 20, las 7 piezas, bolsa de 7, gravedad por nivel con tope, mover/girar/soft drop/hard drop, DAS/ARR propios, rotación con 1–2 patadas horizontales, ghost, preview de 3, lock delay de 0.5 s con tope de 15, puntaje simple, niveles cada 10 líneas, game over por block out, pausa, récord en `localStorage`, reintento en una tecla, sonido de trabar/limpiar/4 líneas.
  - **Alcance completo:** hold, SRS completo, T-spin y back-to-back, combos, modos Marathon/Sprint/Ultra, preview de 5, DAS configurable, efectos por nivel y música, y versus contra una IA simple con basura. El versus es otro proyecto: toca condición de derrota, ritmo y tabla de envío.

## Límites

- Es un libro de **experiencia**. Cómo se implementa la rotación, las patadas o el paso fijo es materia del `SOL`; para eso están `01_Bucle_de_simulacion` y `02_Colision_y_consulta_espacial`.
- **No verificado:** el valor exacto de DAS y ARR de los juegos Guideline modernos (ni la Tetris Wiki ni la Hard Drop wiki dan un valor por defecto); los números de DAS/ARR del baseline son **destilación propia, a calibrar**.
- **No verificado:** la velocidad exacta del soft drop salvo el ejemplo de Tetris Zone (20×); la de cada otra versión varía y no se leyó.
- **No verificado:** cuántas líneas tiene Sprint y cuánto dura Ultra; este libro no da números de esos modos.
- **Tope de 15 reseteos del lock delay:** viene de la página de la Guideline de la Tetris Wiki; la página de *Lock delay* de la misma wiki y la de la Hard Drop wiki dicen que "suele haber un límite" sin dar el número. Una sola fuente.
- **Los porcentajes de sequía del NES y de TGM** (12 % de 12 piezas sin I, etc.) son de una guía de terceros, sin recalcular. Los de azar puro son aritmética propia y exactos bajo independencia 1/7.
- **La tabla completa de gravedad del NES** (niveles 0–29) no se leyó; solo los niveles 0, 9, 10–12 y 29.
- **No cubiertos:** T-spins en detalle, la tabla completa de patadas del SRS, estrategia competitiva (aperturas, finesse), el punto de vista de un diseño de entry delay, la economía de un versus. El juego de ritmo-musical de *Tetris Effect* se citó como referencia, no se destiló.
- El "efecto Tetris" (Stickgold) se cita como contexto y no como regla de diseño; su relación con el diseño es del autor de este libro, y los números son los de la nota de prensa.
- **Fecha de origen (1984 o 1985):** la ficha de Pajitnov en Wikipedia da el 6 de junio de 1985 como cierre de la primera versión; la página *Tetris* de Wikipedia recoge que las fuentes varían (junio de 1984; primavera de 1985 según un documental de la BBC; 1985 según una entrevista de 1993; 1984 según un recuerdo de Pajitnov reportado en 2024) y no la resuelve. Este libro no la resuelve tampoco: ningún número de diseño depende de ella.
- **Nada se validó con jugadores ni con un Tetris propio.** Las fuentes dicen qué hace cada juego, no cuánto tiempo de reacción tiene una persona.

---

## Fuentes

Todas consultadas el 2026-10-13.

- Tetris Wiki, *Tetris Guideline* — https://tetris.wiki/Tetris_Guideline (tablero, spawn, hold, ghost, preview, lock delay 0.5 s, tope de 15, top out, soft drop de Tetris Zone)
- Tetris Wiki, *Random Generator* — https://tetris.wiki/Random_Generator (bolsa de 7, sequía máxima 12, rachas de S y Z)
- Tetris Wiki, *Super Rotation System* — https://tetris.wiki/Super_Rotation_System (cuatro estados, hasta 5 pruebas, 8 transiciones, tablas)
- Tetris Wiki, *Marathon* — https://tetris.wiki/Marathon (fórmula y tabla de gravedad, 10 líneas por nivel, tope en 15)
- Tetris Wiki, *Tetris (NES, Nintendo)* — https://tetris.wiki/Tetris_(NES,_Nintendo) (60.0988 Hz, gravedad en cuadros, DAS 16/6, aleatorizador, entry delay)
- Tetris Wiki, *Scoring* — https://tetris.wiki/Scoring (puntaje Guideline y NES)
- Tetris Wiki, *Top out*, *Garbage*, *Ghost piece*, *Hard drop*, *Line clear*, *Lock delay*, *Drop*, *DAS* — https://tetris.wiki/ (misma wiki, una página por tema)
- Hard Drop wiki, *Tetris Guideline*, *Hold piece*, *DAS*, *Lock delay* — https://harddrop.com/wiki/Tetris_Guideline (y las otras tres bajo la misma ruta)
- Tetris Concept, *Randomizer Theory* (foro, 2007) — https://tetrisconcept.net/threads/randomizer-theory.512/ (sequía máxima 12 con bolsa, historial de TGM, efecto del hold)
- Gamertag Mythras, *Tetris Randomizers Explained* — https://gamertagmythras.com/blog/tetris/tetris-randomizers-explained (comparativa NES / bolsa / TGM; cifras sin recalcular)
- Stickgold et al. (2000), nota de prensa en ScienceDaily — https://sciencedaily.com/releases/2000/10/001013073843.htm (efecto Tetris: 27 participantes, 17 con sueños de piezas)
- Wikipedia, *Alexey Pajitnov* — https://en.wikipedia.org/wiki/Alexey_Pajitnov (primera versión terminada el 6 de junio de 1985, Electronika 60, pentominós, sin niveles ni puntaje)
- Wikipedia, *Tetris* — https://en.wikipedia.org/wiki/Tetris (fecha de origen discrepante: junio de 1984 / primavera de 1985 / 1985)
- Wikipedia, *The Tetris Company* — https://en.wikipedia.org/wiki/The_Tetris_Company (marca, trade dress; fallo de copyright de junio de 2012 contra Mino, de Xio Interactive)
- GamesBeat, *Tetsuya Mizuguchi interview: Taking Tetris on a PS VR acid trip* — https://gamesbeat.com/tetsuya-mizuguchi-interview-taking-tetris-on-a-ps-vr-acid-trip/ (sonido y sinestesia como diseño)
- GamesBeat, *Tetris Effect review: video games get their Kuleshov effect* — https://gamesbeat.com/tetris-effect-review-video-games-get-their-kuleshov-effect/ (música y etapas que acompañan las líneas)

Del vault: `02_Game_feel`, `03_Definicion_de_terminado`, `06_Dificultad_y_curva`, `08_Progresion_y_recompensa`, `10_Input_y_respuesta`, `14_UI_HUD_y_menus`, `15_Muerte_reintento_y_checkpoints`, `16_Audio_como_gameplay`, `01_Bucle_de_simulacion`, `02_Colision_y_consulta_espacial`, `05_Endless_runner`.

**Cobertura declarada:** las table-stakes 1, 4, 7, 8, 9 y 10 nombran su calibración en la Tetris Wiki o la Hard Drop wiki; la 3 usa aritmética propia sobre esas fuentes; la 2, 5, 6, 11, 12 y 13 son destilación propia sobre el género y los libros `10_Input_y_respuesta`, `15_Muerte_reintento_y_checkpoints` y `14_UI_HUD_y_menus`. **Ninguna se validó todavía con jugadores ni con un Tetris propio.**

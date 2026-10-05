---
tipo: juego
genero: Arcade
subtipo: Endless runner lateral (auto-run, un carril, un golpe)
estado: En validación
mision: EST-019_Mision_Endless_runner_y_contrarreloj
cruza: 02_Plataformero_2D, 06_Dificultad_y_curva, 10_Input_y_respuesta, 14_UI_HUD_y_menus, 15_Muerte_reintento_y_checkpoints, 16_Audio_como_gameplay, 02_Colision_y_consulta_espacial, 01_Bucle_de_simulacion
---

# Libro 05 — Endless runner

> Quinto libro del estante de Juegos. Género: Arcade / endless runner lateral.
> Lo **transversal** vive en los Fundamentos y el salto con su feel en `02_Plataformero_2D`. Acá va lo **específico**: qué pasa cuando el juego le saca al jugador el control de la velocidad y la partida no termina nunca.
> **IP:** conceptos destilados + cita. Las constantes del Dino de Chrome se citan del código fuente liberado (licencia BSD de Chromium), no se copian.

---

## Índice del libro

- Loop de experiencia
- Table-stakes
- Juice / game feel
- El salto y los huecos, en detalle
- Las alturas de los voladores
- Baseline de parámetros
- Al chocar
- Variantes, y qué parte del baseline reescribe cada una
- Definición de Terminado
- Aplicación
- Límites
- Fuentes

---

## Loop de experiencia

El runner se define por lo que le saca al plataformero: **el control de la velocidad**. El personaje avanza solo y cada vez más rápido; el jugador decide únicamente *qué verbo* usar y *cuándo*. La partida no tiene meta: termina con el primer error, y su resultado es una distancia que se compara con la mejor.

```txt
LOOP ATÓMICO   (≈0.4–1.4 s)    ver el obstáculo entrar → elegir el verbo (saltar / agacharse / nada) → ejecutar → pasar
LOOP DE PARTIDA (≈20 s–3 min)  la velocidad sube → la ventana para decidir se achica → el primer error termina todo
LOOP DE SESIÓN  (≈5–20 min)    partida → récord o casi-récord → "una más"
```

**La unidad del género es la partida entera, y el reintento es el juego.** No hay checkpoint: cada muerte devuelve al principio, así que morir cuesta *todo* lo jugado. Lo que lo vuelve tolerable es que el comienzo es fácil y corto: los primeros segundos son la rampa, no un castigo. `15_Muerte_reintento_y_checkpoints`

**Qué lo hace juego y no juguete:** el objetivo impuesto es llegar más lejos que antes; el obstáculo aceptado es no poder frenar. Sacale el auto-run y queda un plataformero sin meta. `21_The_Grasshopper`

**Dónde vive la tensión:** en la **ventana de anticipación**, el tiempo entre que un obstáculo entra en pantalla y llega al personaje. En `02_Plataformero_2D` el jugador conoce la solución y le falta la mano; acá conoce el repertorio entero —tres o cuatro obstáculos— y lo que le falta es *tiempo para leer*. La dificultad del runner casi no sale de obstáculos más complejos: sale de una ventana que se achica.

```txt
ventana de anticipación  =  distancia visible por delante del personaje  /  velocidad
```

Es la relación que ordena el libro entero: **la curva de velocidad es la curva de dificultad.** Cuándo aparece cada obstáculo, cuánto hueco dejar y dónde poner el tope se leen contra ella.

---

## Table-stakes

Lo que un runner **no puede no tener** para estar terminado.

| # | Table-stake | Por qué es obligatorio |
|---|-------------|------------------------|
| 1 | **Auto-run con velocidad creciente y con tope** | Sin rampa no hay partida, hay un loop. Sin tope, la partida termina por imposibilidad física y no por error: el récord deja de medir habilidad. El Dino sube de 6 a 13 px/cuadro y frena ahí; Canabalt va de 100 a 800 px/s. `66_Chrome_Dino_codigo_fuente`, `67_Tuning_Canabalt` |
| 2 | **Zona limpia al arrancar y después de cada reintento** | Los primeros segundos son para tomar el control, no para reaccionar. Dino: 3 s sin obstáculos, también tras cada restart |
| 3 | **Ventana de anticipación mínima garantizada a velocidad máxima** | Por debajo de ~0.5 s —unas dos veces un reflejo simple de 0.25–0.3 s— la muerte deja de ser error y pasa a ser azar. Saltsman ubica el reflejo en ~0.3 s y garantiza más de 0.5 s en Canabalt: es el piso. El Dino deja 0.65 s a tope |
| 4 | **Cada obstáculo tiene una sola respuesta cómoda**, legible por forma y altura | El jugador tiene décimas de segundo: no delibera, reconoce. Si un obstáculo admite dos lecturas, el error es del juego. Ver *Las alturas de los voladores* |
| 5 | **"No hacer nada" es una de las respuestas** | Si todo se pasa saltando, la estrategia óptima es saltar sin parar y el juego desaparece. El volador alto del Dino existe para castigar el salto innecesario. *Destilación propia sobre el código del Dino* |
| 6 | **Huecos derivados del salto, con garantía de que todo patrón es superable** | Un patrón imposible destruye el récord como medida. El Dino calcula el hueco mínimo con la velocidad y el ancho del grupo; Canabalt lo limita a 2/3 de la velocidad horizontal; Smith et al. garantizan la jugabilidad con un modelo físico del salto. Ver *El salto y los huecos* |
| 7 | **Cajas de colisión más chicas que el sprite**, a favor del jugador | En un runner se muere por un pixel a toda velocidad; la caja generosa es lo que hace que la muerte se lea como justa. El T-Rex cuenta ≤46% de su área y el pterodáctilo ~17%; en Canabalt la caja es de 12×14 dentro de un sprite de 24×24. `02_Colision_y_consulta_espacial` |
| 8 | **Tipos de obstáculo que se desbloquean de a uno, por velocidad** | Presentar → consolidar → combinar (`06_Dificultad_y_curva`). Dino: grupos de cactus grandes desde velocidad 7, pterodáctilo desde 8.5, nunca tres seguidos del mismo tipo |
| 9 | **Puntaje = distancia, visible y monótono, con el récord persistente al lado** | La meta del género es el récord: si no se ve mientras se juega, no hay meta. Dino: marcador de ancho fijo y `HI` al lado, guardado entre sesiones |
| 10 | **Hito periódico** (sonido + destello del marcador) | Es la miga de pan de una partida sin metas intermedias. Dino: cada 100 puntos |
| 11 | **Choque legible, game over claro y reintento en una tecla, con bloqueo anti-accidente** | El jugador está apretando saltar en el momento de morir; si esa tecla reinicia al instante, se saltea el game over sin verlo. Ver *Al chocar* |
| 12 | **Pausa automática al perder el foco** | Un runner no espera: si la ventana pierde el foco y el juego sigue, el jugador muere sin estar. El Dino se detiene al perder el foco y al ocultarse la pestaña |

Del salto, el runner **hereda** las table-stakes de `02_Plataformero_2D`: salto de altura variable, jump buffer y respuesta en el cuadro en que se aprieta (`10_Input_y_respuesta`). El coyote time solo aplica si hay bordes: Canabalt los tiene, el Dino no.

---

## Juice / game feel

| Efecto | Qué comunica | Cuidado |
|--------|--------------|---------|
| **Hito sonoro + destello del marcador** | progreso, en una partida sin metas | Dino: 250 ms, 3 parpadeos. Tiene que sonar distinto del salto |
| **Polvo al despegar y aterrizar** | el contacto con el piso sin mirar los pies | Heredado de `02_Plataformero_2D` |
| **Choque: sonido + vibración + sprite de choque** | que terminó, y contra qué | Dino: vibración de 200 ms. Tiene que ser el evento más grande de la partida |
| **Cambio de escenario periódico** | que se avanzó, sin tocar las reglas | Dino: modo noche cada 700 puntos —el primero a ≈60 s y después cada ≈36–43 s, porque se mide en distancia—, durante 12 s. Nunca puede bajar el contraste de los obstáculos (`14_UI_HUD_y_menus`) |
| **Parallax del fondo** | la velocidad misma | Que el fondo no le compita en contraste al obstáculo |
| **Puntos por segundo crecientes** | la aceleración | Con 1 punto = una distancia fija, el contador se acelera solo: el Dino pasa de 9 a 19.5 puntos/s |

**Regla del género: la franja por donde entran los obstáculos es sagrada.** Cada pixel tapado ahí es tiempo de anticipación robado: es la dificultad subiendo sin que nadie lo decida. En `02_Plataformero_2D` el juice no podía tapar el próximo apoyo; acá no puede tapar el borde de entrada. Partículas, popups y HUD van del lado del personaje o arriba. *Destilación propia.*

---

## El salto y los huecos, en detalle

En el runner el salto no decide *si* se pasa un obstáculo: decide **qué patrones son posibles**. Dos obstáculos seguidos se pasan con dos saltos de tres maneras distintas, según cuánto tiempo hay entre uno y otro.

```txt
T     duración del salto que ese par exige (el corto, si su altura alcanza)
W     ventana de un salto = tiempo que la CAJA del personaje pasa por encima de la caja del obstáculo
                          − tiempo que tarda el obstáculo en cruzar la caja del personaje
B     tiempo entre el comienzo de un obstáculo y el comienzo del siguiente

RITMO                 B ≥ T            el mismo tempo sirve para los dos saltos
SÍNCOPA               T − W ≤ B < T    solo pasa saltando temprano el primero y tarde el segundo;
                                       cuanto más cerca de T − W, más fino
IMPOSIBLE DE A DOS    B < T − W        o el par entero entra en un salto
                                       (w1 + hueco + w2 + ancho de la caja del personaje ≤ lo que el salto recorre por encima),
                                       o el patrón está prohibido y el generador lo descarta
```

**Baseline:** ritmo por defecto; síncopa como escalón de examen, con un margen `B − (T − W) ≥ 0.1 s`; imposible de a dos, nunca, salvo que entre de un salto con margen. El margen de 0.1 s es **destilación propia, a calibrar en playtest**. La forma —un modelo del salto que filtra patrones antes de que lleguen al jugador— es la de Smith et al., que verifican que cada salto termine antes de que empiece el siguiente: es la condición de ritmo. `57_Rhythm_Based_Level_Generation`

**Calibración contra el Dino** (cálculo sobre su código, par de cactus chicos al hueco mínimo, sin playtest — inferencia declarada):

```txt
                 T corto   W       B mínimo   T − W    lectura
velocidad 6      0.50 s    0.22 s  0.53 s     0.28 s   ritmo, con saltos cortos
velocidad 8.5    0.50 s    0.26 s  0.46 s     0.24 s   síncopa, margen 0.22 s
velocidad 13     0.50 s    0.31 s  0.40 s     0.19 s   síncopa, margen 0.21 s
```

La duración del salto casi no cambia con la velocidad —lo que crece es la distancia que recorre: 210 px a velocidad 6, 442 px a 13— y el tiempo entre obstáculos se achica. **Por eso la misma regla de huecos pasa sola de ritmo a síncopa: la curva de velocidad sube también la dificultad rítmica.** Y la ventana `W` depende de las cajas: cuanto más generosas, más ancha. **La generosidad de la caja no es cortesía: entra en el cálculo del hueco.**

El Dino nunca genera un par chico–chico imposible de a dos, pero no porque derive su hueco del salto: lo calcula con la velocidad y el ancho del grupo, y el margen le sale por calibración. Un runner nuevo no hereda ese margen: lo chequea con su propio salto y sus propias cajas.

**Regla de oro del género, igual que en el plataformero:** el hueco no se elige, se calcula del salto. Si el salto cambia —una mejora, un modo accesible— los huecos se recalculan con el salto actual, no con el base.

---

## Las alturas de los voladores

Cada altura de volador es una pregunta con **una** respuesta cómoda. Se definen contra tres medidas del personaje, no en pixeles:

```txt
A    altura de la caja de pie          a    altura de la caja agachada          H    altura máxima del salto
```

| Banda | Dónde está la parte que mata | Respuesta | Dino (zona de daño sobre el piso; A = 47 px, a = 25 px, H ≈ 90 px) |
|-------|------------------------------|-----------|------------------------------|
| **Baja** | cruza la caja agachada | solo saltar | 12–31 px ≈ 0.25–0.65 A |
| **Media** | borde inferior por encima de `a` y por debajo de `A` | agacharse (un salto completo bien medido también pasa, y es más difícil) | 37–56 px ≈ 0.8–1.2 A |
| **Alta** | por encima de `A`, por debajo de `H` | **no hacer nada**; saltar mata | 62–81 px ≈ 1.3–1.7 A |

**Margen, en los dos sentidos:** ≥ 0.2 A de separación con la caja que se esquiva y ≥ 0.2 A de solapamiento con la caja que se golpea. Dino: la banda media queda 12 px por encima de la caja agachada (0.26 A) y entra 10 px en la de pie (0.21 A); la alta queda 15 px por encima de la de pie (0.32 A); la baja entra 13 px en la agachada (0.28 A). Un volador a medio camino entre dos bandas tiene dos lecturas, y eso es la table-stake 4 rota.

**El conjunto de alturas sale del conjunto de verbos.** En móvil el Dino no tiene agacharse, y la banda media desaparece. Un runner sin agacharse tiene dos bandas; uno con deslizarse y doble salto, más. *Inferencia por geometría sobre el código del Dino.*

**Si el volador tiene velocidad propia,** su ventana se calcula con la velocidad relativa: el pterodáctilo del Dino va ±0.8 px/cuadro respecto del piso, y a tope le deja al jugador 0.61 s en vez de 0.65.

---

## Baseline de parámetros

Punto de partida, no dogma. En **tiempo** y en relaciones, para que escale a cualquier tamaño de pantalla. Se ajusta jugando.

| Parámetro | Relación | Baseline | Calibración |
|-----------|----------|----------|-------------|
| Ventana al arrancar | `D / v0` | 1.2–1.5 s | Dino 1.41 s |
| Ventana a velocidad máxima | `D / vmax` | 0.6–0.7 s; piso absoluto 0.5 s | Dino 0.65 s; Canabalt > 0.5 s (el piso) |
| v0 y vmax | **se derivan de las dos ventanas**, no se eligen: `v0 = D / 1.4 s`, `vmax = D / 0.65 s` | vmax ≈ 2.2 × v0 | Dino 13 / 6 = 2.17. Canabalt (100 → 800 px/s) es el contraste: arranca mucho más lento y sube rápido |
| Tiempo hasta vmax | — | 90–120 s | Dino ≈ 117 s; Canabalt menos de 70 s, desde un arranque lento |
| Forma de la rampa | lineal en el tiempo, o con aceleración decreciente; **nunca creciente** | — | Dino lineal; Canabalt 50 → 30 → 20 → 10 px/s² por tramos |
| Unidad de la aceleración | por segundo de simulación, **nunca por cuadro** | — | El Dino suma la aceleración por cuadro y mueve el mundo por tiempo: a 120 Hz llega al tope en la mitad del tiempo real. `01_Bucle_de_simulacion` |
| Zona limpia | al inicio y tras cada reintento | 2.5–3 s | Dino 3 s |
| Desbloqueo de cada tipo nuevo | cuando la ventana todavía ronda 1 s | ≥ 0.9 s | Dino: pterodáctilo a velocidad 8.5 → 0.99 s (0.91 s si viene 0.8 más rápido) |
| Repetición | máximo dos seguidos del mismo tipo | — | Dino |
| Hueco | sorteado en `[g_min, 1.5 · g_min]`, con `g_min` derivado del salto | — | Dino: solo el rango; su `g_min` sale de velocidad × ancho del grupo, no del salto (ver *El salto y los huecos*) |
| Caja del personaje | recortar frente, cabeza y patas | 25–50% del área del sprite | Dino ≤ 46%; Canabalt ≈ 29% |
| Caja del obstáculo de suelo | — | 70–80% | Dino 73–79% |
| Caja del volador | solo el cuerpo, nunca las alas | 15–40% | Dino ≈ 17% |
| Puntaje | 1 punto = una distancia fija | — | Dino: 1 punto = 40 px |
| Hito | cada N puntos, con N tal que al inicio caiga cada ~10 s | — | Dino: 100 puntos → cada 11 s al inicio, cada 5 s a tope |
| Cambio de escenario | — | el primero a ~60 s | Dino: cada 700 puntos; el primero a ≈60 s, después más seguido porque se mide en distancia |
| Bloqueo de reinicio con la tecla de salto | — | 0.75–1.2 s | Dino 1.2 s (0.75 s en la versión de 2014) |

`D` es la distancia entre el borde por donde entra el obstáculo y el frente del personaje. **Si la pantalla cambia de ancho, cambia `D`, y con ella las dos velocidades**: el Dino ajusta la velocidad al ancho del canvas por la misma razón.

---

## Al chocar

Responde las tres cosas que cuesta morir en un runner, según el análisis de Jetpack Joyride: **el tiempo perdido, la sensación de fracaso y la fricción para volver a empezar.** `68_Depth_in_Simplicity_Jetpack_Joyride`

```txt
CHOQUE      sonido de choque + vibración (Dino 200 ms) + sprite de choque. El mundo se detiene.
PANEL       "game over", distancia de la partida y récord, uno al lado del otro
REINTENTO   tecla explícita (Enter, R, clic): habilitada a los 0.3 s
            tecla de salto: habilitada recién a los 0.75–1.2 s — es la que se estaba apretando
AL VOLVER   velocidad a v0, zona limpia otra vez, obstáculos borrados, escenario de día
```

**Excepción declarada a `15_Muerte_reintento_y_checkpoints`**, que pide un game over salteable con cualquier botón a los 0.3 s y control recuperado en ≤ 1.5 s: acá vale *cualquier botón salvo el que se venía apretando*. El camino explícito cumple los 0.3 s, el accidental se bloquea más, y ninguno pasa de 1.5 s.

**Récord nuevo:** se marca como evento —distinto y más grande que el hito— y no como un número que cambia callado. Es la única recompensa que el género da por partida. *Destilación propia*, cruzada con `08_Progresion_y_recompensa`.

---

## Variantes, y qué parte del baseline reescribe cada una

Una variante no le agrega una fila al baseline: **lo pone entero bajo sospecha.** Esta tabla dice dónde mirar primero.

| Variante | Ejemplos | Qué reescribe |
|----------|----------|---------------|
| **Runner de carriles** (3D, swipe) | Temple Run, Subway Surfers | Las bandas de altura se reemplazan por ocupación de carriles: en toda ventana queda un carril libre alcanzable con un cambio de carril más el tiempo de reacción. Temple Run agrega un perseguidor visible detrás como presión |
| **Escudo de un golpe** | Subway Surfers (hoverboard de 30 s: al chocar explota, limpia la zona y salva); Jetpack Joyride (el vehículo dura hasta el próximo choque) | El eje "un golpe = fin". La garantía de patrón superable **no se relaja** por tener escudo |
| **Metas de sesión** | Jetpack Joyride (tres misiones a la vez; la cumplida se reemplaza); Alto's Adventure (tres objetivos por set) | Agrega un objetivo para cuando el récord queda lejos. Es una economía: `07_Economia_y_balance` |
| **Mejoras que tocan el salto** | tiendas de power-ups | Todo el capítulo de huecos: el generador calcula con el salto actual |
| **Modo accesible** | Dino: modo lento con avisos sonoros — velocidad 4.2 → 9, la mitad de aceleración, huecos más largos, otra gravedad de salto | Velocidad, huecos y salto **juntos**: es la prueba de que una variante reescribe el baseline entero. El aviso sonoro va 400–800 ms antes, como pide `16_Audio_como_gameplay` |
| **Zen** | Alto's Adventure: sin puntaje ni UI | Saca el récord, y con él la competencia contra uno mismo. Nació porque jugadores lo usaban contra la ansiedad |

---

## Definición de Terminado

Checklist del género. Se corre **sobre el juego corriendo**, no sobre el código.

```txt
VELOCIDAD Y LECTURA
[ ] Arranco y los primeros segundos no tienen obstáculos
[ ] La velocidad sube de forma que se nota, y en algún momento deja de subir
[ ] A velocidad máxima todavía veo cada obstáculo con tiempo de decidir
[ ] El juego va igual de rápido en un monitor de 60 Hz y en uno de 120+ Hz
[ ] Nada tapa el borde por donde entran los obstáculos

OBSTÁCULOS
[ ] Cada obstáculo tiene una sola respuesta, y la reconozco de un vistazo
[ ] Hay al menos un obstáculo que se pasa sin hacer nada, y saltarlo me mata
[ ] Los tipos nuevos aparecen de a uno, no todos de entrada
[ ] Nunca me toca un par imposible: o se pasa de un salto o hay tiempo para dos
[ ] Los pares apretados que piden saltar temprano y tarde aparecen recién cuando ya voy rápido
[ ] Cuando choco, se ve que toqué; nunca muero contra algo que no rocé

PARTIDA Y ESTADOS
[ ] Veo mi distancia y mi récord mientras juego
[ ] El récord sobrevive a cerrar y volver a abrir
[ ] Cada tanto suena y destella un hito
[ ] Al chocar entiendo que terminó y contra qué choqué
[ ] La tecla de salto que venía apretando no me reinicia sin ver el game over
[ ] Vuelvo a jugar en una tecla y en menos de un segundo y medio
[ ] Si cambio de pestaña o de ventana, el juego se pausa

FEEL
[ ] El salto responde en el cuadro en que aprieto, y soltar antes salta más bajo
[ ] Saltar, aterrizar, el hito y el choque suenan distinto entre sí
[ ] Un récord nuevo se festeja como evento
```

Un runner que corre y salta pero no tilda **Obstáculos** y **Velocidad y lectura** es el 4/10 de la Ley #1: la demo técnica que obliga a gastar prompts en trabajo remedial.

---

## Aplicación

- **Cuándo se abre este libro:** ante cualquier pedido de endless runner, auto-runner, infinite runner, "como el dinosaurio de Chrome" o "como Canabalt", o juego de un botón con avance automático. Producción lo carga al escribir el `RQ`; Game Design lo cruza con el checklist de pilares al escribir el `GDS`; **Level Design usa las bandas de altura y la regla de huecos como medidas del espacio**, porque en un runner el patrón de obstáculos es el nivel.
- **Qué trae la IA por default sin que se lo pidan:** las 12 table-stakes, la regla de ritmo, síncopa e imposible, las bandas de altura que salen de sus verbos (tres si hay agacharse), el baseline en ventanas de tiempo, la secuencia del choque con sus dos bloqueos y la Definición de Terminado completa.
- **Qué NO decide este libro:** el tema, el arte, si hay carriles, si hay meta-progresión o tienda, la plataforma. Eso lo declara el `RQ`.

## Límites

- Es un libro de **experiencia**. Cómo se implementa el generador, la colisión caja por caja o el paso fijo es materia del `SOL`; para eso están `01_Bucle_de_simulacion` y `02_Colision_y_consulta_espacial`.
- El baseline vale para el runner **lateral de un carril**. El de carriles está esbozado como variante, no destilado.
- **La generación por bloques de autor** (chunks diseñados a mano y cosidos) no está destilada: el Dino usa azar restringido y Canabalt reglas por edificio. Las fuentes para profundizar quedan fichadas: `57_Rhythm_Based_Level_Generation` y `52_Procedural_Content_Generation`. Launchpad (Smith et al., 2011) y Compton y Mateas (2006) quedaron sin leer.
- **La economía de la meta-progresión** (monedas, mejoras, pago) no está cubierta: no se encontró fuente con datos sobre su costo en retención.
- **Las relaciones de huecos y alturas salen de calcular sobre el código del Dino, no de un playtest.** La validación de verdad es el primer runner que pase por la cadena: si su `VE` encuentra una table-stake que falta o un umbral que no se sostiene, este libro se actualiza, no se duplica.
- Bit.Trip Runner —niveles fijos con ritmo— no es un endless runner: está más cerca de `02_Plataformero_2D` y de un juego de ritmo.

---

## Fuentes

Externas, con su ficha en la Biblioteca:

- `66_Chrome_Dino_codigo_fuente` — Chromium, `components/neterror/resources/dino_game/`, leído en el commit `9b4a14466a0e` (2026-10-02). Constantes de velocidad, huecos, obstáculos, cajas, puntaje, bloqueo de reinicio y modo accesible. Licencia BSD (nivel A)
- `67_Tuning_Canabalt` — Adam Saltsman, 2010. Rampa por tramos, salto según velocidad, hueco ≤ 2/3 de la velocidad, caja del jugador, ventana de reacción
- `68_Depth_in_Simplicity_Jetpack_Joyride` — Luke Muscat, GDC 2012. Un botón, misiones, los tres costos de morir
- `57_Rhythm_Based_Level_Generation` — Smith, Treanor, Whitehead y Mateas, FDG 2009. Grupos rítmicos y verificación física de la jugabilidad

Externas citadas sin ficha propia:

- Shelton y Kumar (2010), *Comparison between Auditory and Visual Simple Reaction Times* — https://www.scirp.org/html/4-2400003_2689.htm
- Temple Run — GameSpot, *Temple Run: the rough road to a runaway success story* (https://www.gamespot.com/articles/temple-run-the-rough-road-to-a-runaway-success-story/1100-6368469/) y Wikipedia
- Subway Surfers Wiki (Fandom), *Hoverboard* — https://subwaysurf.fandom.com/wiki/Hoverboard
- Alto's Adventure — Wikipedia; y Game Developer (2016) sobre el origen del modo Zen: https://www.gamedeveloper.com/design/players-use-i-alto-s-adventure-i-as-coping-mechanism-dev-responds-with-zen-mode-
- Jetpack Joyride, Bit.Trip Runner — Wikipedia

Del vault: `02_Plataformero_2D`, `06_Dificultad_y_curva`, `10_Input_y_respuesta`, `14_UI_HUD_y_menus`, `15_Muerte_reintento_y_checkpoints`, `16_Audio_como_gameplay`, `08_Progresion_y_recompensa`, `21_The_Grasshopper`, `01_Bucle_de_simulacion`, `02_Colision_y_consulta_espacial`.

**Cobertura declarada:** de las 12 table-stakes, **nueve** —1, 2, 3, 6, 7, 8, 9, 10 y 12— nombran su calibración en una fuente externa, y **dos** son destilación propia sobre el código: la 4 (una sola respuesta por obstáculo) y la 5 (no hacer nada es una respuesta). La 11 combina el código del Dino con `15_Muerte_reintento_y_checkpoints`. **Ninguna table-stake se validó todavía contra un runner jugado.**

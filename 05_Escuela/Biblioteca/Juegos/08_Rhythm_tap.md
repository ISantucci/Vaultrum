---
tipo: juego
genero: Ritmo
subtipo: Rhythm tap de carriles (4 carriles, un toque por nota, velocidad creciente; el error es tocar mal o dejar pasar)
estado: En validación
mision: EST-022_Mision_Lote_Juegos_Web_y_Sigilo
cruza: 02_Game_feel, 06_Dificultad_y_curva, 09_Onboarding_y_tutorial, 10_Input_y_respuesta, 12_Pacing_y_estructura, 14_UI_HUD_y_menus, 15_Muerte_reintento_y_checkpoints, 16_Audio_como_gameplay, 01_Bucle_de_simulacion, 05_Endless_runner
---

# Libro 08 — Rhythm tap

> Octavo libro del estante de Juegos. Género: Ritmo / tap de carriles tipo *Don't Tap The White Tile* y *Piano Tiles*.
> Lo **transversal** vive en los Fundamentos y el modelo "la curva de velocidad es la curva de dificultad" en `05_Endless_runner`. Acá va lo **específico**: qué pasa cuando cada nota es un toque en un carril, el tiempo de caída manda, y el reloj que importa es el del audio y no el del cuadro.
> **IP:** conceptos destilados + cita. No se copia código, arte, canciones ni charts de ningún juego; las fórmulas de ventanas de osu! se citan de su wiki oficial como relación, no como texto.
> **Medido:** nada. Este libro no corrió ningún juego: los números salen de documentación leída (ver *Fuentes*) o están marcados como *destilación propia, a calibrar en playtest*. Todas las ventanas en milisegundos y las velocidades en tiempo, para que escalen a cualquier pantalla.

---

## Índice del libro

- Loop de experiencia
- Table-stakes
- Juice / game feel
- Ventanas de acierto y velocidad de caída
- Latencia de audio y entrada, y calibración
- Modos: clásico por carriles vs sincronizado con canción
- Generación de patrones y garantía de que son tocables
- Feedback de acierto y de fallo
- Baseline de parámetros
- Variantes, y qué parte del baseline reescribe cada una
- Definición de Terminado
- Aplicación
- Límites
- Fuentes

---

## Loop de experiencia

El rhythm tap se define por lo que le saca a casi todo otro género: **el verbo es uno solo** (tocar) y **el único dato es dónde y cuándo**. El jugador no decide qué hacer: decide *dónde* (carril) y *cuándo* (instante). La dificultad no sale de mecánicas nuevas sino de que el tiempo entre una nota y la siguiente se achica.

```txt
LOOP ATÓMICO    (≈0.2–0.5 s)   leer la fila que viene → elegir carril → tocar → oír/ver la confirmación
LOOP DE PARTIDA (≈30 s–3 min)  la cadencia sube (clásico) o la canción se densifica (sincronizado) → el primer error termina
LOOP DE SESIÓN  (≈5–15 min)    partida → récord o casi-récord → "una más"
```

**Qué lo hace juego:** el objetivo impuesto es sostener la cadencia más alta posible sin un solo error; el obstáculo aceptado es que el mundo no espera. Es hermano del runner: la partida termina con el primer error y el reintento es el juego (`15_Muerte_reintento_y_checkpoints`, `05_Endless_runner`).

**Historia mínima.** *Don't Tap The White Tile* (Umoni Studio, desarrollado por Hu Wen Zeng según Wikipedia) salió el 28 de marzo de 2014 para iOS y Android; a fines de abril de 2014 era la app más descargada en ambas tiendas. Se toca solo el mosaico negro, cada toque correcto suena como una nota de piano, y tocar uno blanco termina la partida. *Piano Tiles 2* (Cheetah Mobile, 19 de agosto de 2015) lo extendió con canciones completas. Los modos nombrados son Classic, Arcade, Zen, Rush, Arcade+ y Relay.

**Dónde vive la tensión.** En la **ventana de lectura**: cuántas filas se ven por delante de la que se toca.

```txt
T_caída        = alto jugable / velocidad                       (tiempo que tarda una fila de arriba a abajo)
Δ              = tiempo entre dos filas consecutivas = alto de fila / velocidad = T_caída / R   (R = filas visibles)
toques por s   = 1 / Δ
ventana de lectura = (R − 1) · Δ
```

Sube la velocidad y bajan **a la vez** Δ, T_caída y la ventana de lectura: es una sola perilla, no tres. En modo sincronizado la perilla es otra: la **densidad** de notas (`notas/s = BPM × subdivisión / 60`), mientras T_caída se queda fija.

---

## Table-stakes

Lo que un rhythm tap **no puede no tener** para estar terminado.

| # | Table-stake | Por qué es obligatorio |
|---|-------------|------------------------|
| 1 | **Arranque controlado**: el juego espera el primer toque (clásico) o da una cuenta (sincronizado) | Sin él, la primera fila ya es un error injusto. Destilación propia |
| 2 | **Cadencia creciente con tope** (clásico) | Sin rampa no hay partida; sin tope el récord mide el límite físico de los dedos y no habilidad. Mismo razonamiento que `05_Endless_runner` |
| 3 | **Una sola respuesta correcta por fila**, legible de un vistazo | El jugador reconoce, no delibera. Dos lecturas posibles = error del juego |
| 4 | **Dos tipos de error, los dos reales: tocar mal y dejar pasar** | Si solo existe uno, el otro se explota (tocar todo / no tocar nada). Es la definición del subgénero |
| 5 | **Ventana de lectura mínima garantizada a velocidad máxima** | Si no se alcanza a leer, el error es azar. Ver *Baseline* |
| 6 | **Todo patrón generado es tocable** | Un patrón imposible destruye el récord como medida. Ver *Generación de patrones* |
| 7 | **El juicio usa el instante real del toque**, no el cuadro en que se procesa | Si no, el error de medición llega a un cuadro (16.7 ms a 60 Hz, 6.9 ms a 144 Hz), comparable con la ventana "perfecta". Ver *Latencia* |
| 8 | **Calibración de latencia que el jugador puede correr y se guarda** | La latencia de audio y de pantalla varía por dispositivo y no se puede adivinar. Ver *Latencia* |
| 9 | **Sonido en cada toque correcto**, inmediato | Es el feedback principal y, en clásico, la música misma. `16_Audio_como_gameplay` |
| 10 | **El fallo se muestra: qué tocó y qué debía tocar** | Morir sin entender por qué no enseña. Ver *Feedback* |
| 11 | **Game over claro, reintento en un gesto, con bloqueo anti-accidente** | El jugador toca 2–5 veces por segundo en el momento de morir: sin bloqueo, el toque reinicia sin ver el resultado. `15_Muerte_reintento_y_checkpoints` |
| 12 | **Entrada por teclado, mouse y toque con el mismo juicio** | Que el dispositivo no cambie las reglas. Es el contrato de `10_Input_y_respuesta` |
| 13 | **Pausa automática al perder el foco, y vuelta con cuenta regresiva** | Si el juego sigue sin la pestaña, el jugador pierde sin estar. Mismo problema que el runner |
| 14 | **Puntaje y récord visibles y persistentes** | El récord es la meta. `14_UI_HUD_y_menus` |

---

## Juice / game feel

| Efecto | Qué comunica | Cuidado |
|--------|--------------|---------|
| **Nota por toque** (clásico): cada toque correcto toca la siguiente nota de una melodía | progreso melódico: el jugador *toca* la canción | La melodía depende del jugador, no del reloj: el tempo lo marca su cadencia |
| **Mosaico que reacciona en el mismo cuadro del toque** | "te oí" | Es la medida de `10_Input_y_respuesta`: el cambio visual es del cuadro en que se aprieta |
| **Destello/pulso de la línea de juicio** | dónde se juzga | No tapar el carril con efectos: cada pixel tapado le roba lectura |
| **Etiqueta de precisión** (Perfecto / Bueno / Flojo) | qué tan bien | Pequeña, fuera del eje de lectura, y no más de una a la vez |
| **Racha (combo) con sonido cada N** | sostener la cadencia | El hito no debe sonar igual que la nota |
| **Mosaico del error en rojo + parada del mundo** | el fallo es inequívoco | Ver *Feedback*: tiene que ser el evento más fuerte de la partida |

**Regla del género: el carril es sagrado.** Todo lo que se dibuje encima del recorrido de las notas es ventana de lectura robada. Partículas y etiquetas van al costado o debajo de la línea. *Destilación propia.*

---

## Ventanas de acierto y velocidad de caída

Hay dos familias de juicio, y no se mezclan.

```txt
CLÁSICO (sin música):   no hay "temprano/tarde".  El plazo de la fila n es de T_caída desde que entra;
                        la ventana es [entra, sale]. Toque en celda sin nota = tocar mal.
                        Fila que sale sin tocarse = dejar pasar. El jugador puede ir hasta R − 1 filas adelantado.
SINCRONIZADO:           la nota tiene un instante t_n. Juicio por |error| = |t_toque − t_n − offset|.
```

**Ventanas de referencia leídas.** En osu! (modo estándar), la ventana de cada juicio depende de la Overall Difficulty (OD) y la wiki lista el máximo error (mitad del ancho): 300 = 80 − 6·OD ms, 100 = 140 − 8·OD, 50 = 200 − 10·OD, y miss = 400 ms fijo. En osu!mania: MAX = 16 ms fijo, 300 = 64 − 3·OD, 200 = 97 − 3·OD, 100 = 127 − 3·OD, 50 = 151 − 3·OD, miss = 188 − 3·OD. Con OD 5: 300 = ±49 ms, 200 = ±82, 100 = ±112, 50 = ±136, miss = ±173. La OD no solo achica las ventanas: en estándar va de ±80 ms (OD 0) a ±20 ms (OD 10) para el 300. StepMania (Wikipedia) llama "flawless" a ±0.0225 s con la configuración oficial; el resto de sus niveles no se leyó con fuente sólida. `osu!` y `osu!mania`, wiki oficial.

**Relación ventana ↔ velocidad (la que importa).** La ventana está en **tiempo**; lo que cambia con la velocidad es cuánto *espacio* ocupa:

```txt
ancho de la ventana en pantalla (px) = 2 · W · v          (W en s, v en px/s)
ventana como fracción de Δ          = 2 · W / Δ
```

Si la velocidad sube y W no cambia, la ventana crece en píxeles pero el jugador *ve* lo mismo: el juicio se siente igual. Si W se achica con la dificultad (como hace la OD de osu!), la ventana se angosta en tiempo aunque el mosaico crezca: son dos perillas distintas y el libro las separa. **Baseline: la ventana no se achica con la dificultad; lo que sube es la cadencia.**

**Anti-ambigüedad.** Dos notas del **mismo carril** no pueden tener ventanas que se pisen:

```txt
separación mínima en el mismo carril  S ≥ 2 · W_aceptable
```

Con W_aceptable = 0.110 s: S ≥ 0.22 s. Notas en carriles distintos no tienen ese problema aunque las ventanas se solapen: cada toque se juzga contra el carril que tocó.

**Aprendizaje de osu!:** la nota se muestra antes de su instante `preempt`: 1200 ms a AR 5, 1200 + 120·(5 − AR) ms por debajo y 1200 − 150·(AR − 5) ms por encima (450 ms a AR 10, 1800 ms a AR 0). Es la ventana de lectura del género, con rango publicado. `osu!`, wiki, *Approach rate*.

---

## Latencia de audio y entrada, y calibración

Tres retrasos distintos, que no se pueden medir por separado con un solo tap (Rhythm Quest, devlog 10): **audio** (del programa a los oídos), **video** (del render a la pantalla) y **entrada** (del dedo al evento). Tocar al compás del sonido mide audio + entrada; tocar al compás de la imagen mide video + entrada. Un juego con juicio por tiempo no puede absorber ese desfase: lo compensa.

**Lo que da la Web.** El `AudioContext.currentTime` es el reloj de renderizado del audio; la especificación dice que va *por delante* de lo que suena. `baseLatency` es la latencia de proceso del contexto (ejemplo de MDN: 0.00 con `latencyHint` por defecto, 0.15 con `"playback"`); `outputLatency` es la estimación del retraso entre entregar el buffer y que el dispositivo toque la primera muestra, y **puede cambiar con el contexto corriendo**. `getOutputTimestamp()` devuelve el par (`contextTime`, `performanceTime`) que mapea el reloj del audio al de `performance.now()`. `Event.timeStamp` está en la misma base de tiempo que `performance.now()`, pero su precisión se redondea: 0.1 ms en Chrome, 1 ms en Safari y Firefox, y 16.667 ms en Firefox con `resistFingerprinting` activo.

**Cadena de juicio.**

```txt
posición del audio al instante del toque  =  contextTime + (event.timeStamp − performanceTime)     (del mismo getOutputTimestamp)
error = posición del audio al toque − t_n − offset_usuario
```

Esto es **destilación propia** a partir de las definiciones leídas, y **no es suficiente por sí sola**: las estimaciones de `outputLatency` y `getOutputTimestamp` no son exactas en todo dispositivo. Por eso la calibración manual es obligatoria (table-stake 8), no una opción.

**Calibración (baseline).**
- Pantalla con pulsos sonoros programados en el reloj de audio y un destello sincronizado; el jugador toca al compás **del sonido**.
- Muestras: **8 toques; se descartan el menor y el mayor; el offset es la mediana de las 6 restantes** (Rhythm Quest usa 4 muestras y menciona ~10 con descarte de extremos como tap-test típico; el 8 es destilación propia, a calibrar).
- **Los toques de la calibración no suenan:** un sonido disparado por el toque queda afectado por la misma latencia que se mide (Rhythm Quest).
- El offset se guarda en ms, admite **valores negativos** (Rock Band lo hace) y se puede reajustar desde el menú y en el propio juego. osu! lo expone como "universal offset" en ms, por defecto 0, más un offset local por canción.
- Separar offset de **audio** y de **video** (Rock Band y Guitar Hero III en adelante lo hacen; Giant Bomb). Baseline mínimo: un offset de audio, y el video queda como segundo ajuste.

**Programar el audio.** Los temporizadores de la página corren en el hilo principal y pueden demorar decenas de ms; los eventos de Web Audio corren en otro hilo y mantienen su instante. El patrón es un temporizador que despierta cada **25 ms** y programa lo que cae en los próximos **100 ms** sobre `currentTime` (web.dev, *Audio scheduling*). Lookahead más largo = más tolerancia pero demora de cambios de tempo.

---

## Modos: clásico por carriles vs sincronizado con canción

| Eje | Clásico (sin música) | Sincronizado (con canción) |
|-----|----------------------|----------------------------|
| Qué manda | la velocidad de caída, subiendo | el tiempo de la canción |
| Perilla de dificultad | `v` (y con ella Δ, T_caída, lectura) | densidad `BPM × sub / 60`; T_caída fija |
| Juicio | plazo de salida de la fila | `|error|` contra `t_n` |
| Qué calibra | casi nada (el plazo es holgado) | todo: es la razón de la calibración |

**Cuándo cada uno.** El clásico es el mínimo construible y el que define el subgénero; el sincronizado es el que obliga a la latencia. Construir primero el clásico y agregar el sincronizado reutiliza la lógica de carriles; no al revés.

**La música nunca se estira para seguir al jugador.** En clásico, si el jugador va lento, la melodía va lenta (nota por toque). En sincronizado la canción sigue su reloj, y el jugador que se atrasa pierde notas. Mezclar ambos (música con reloj *y* nota por toque) hace sonar dos veces la misma melodía; se elige uno por modo. `16_Audio_como_gameplay`

---

## Generación de patrones y garantía de que son tocables

**Clásico.** Una nota por fila y un carril al azar con semilla fija: por construcción siempre hay una respuesta. Las restricciones son de **legibilidad y de mano**: máx. **2 filas seguidas en el mismo carril** (destilación propia), y con un solo puntero el salto entre carriles consume parte de Δ, **a calibrar en playtest**.

**Sincronizado.** Un chart es una lista `{t, carril}`. Un generador sobre la grilla de pulsos (`t = k · 60 / (BPM · sub)`) debe pasar un **validador** al cargar, antes de que el jugador lo vea:

```txt
1. notas por segundo  = BPM × sub / 60  ≤ 5                                          (tope de cadencia, igual al clásico)
2. mismo carril       S ≥ 2 · W_aceptable = 0.22 s   →  saltos repetidos solo si BPM × sub ≤ 272
3. acordes            ≤ nº de dedos/punteros del dispositivo (mouse: 1; teclado: 2)
4. T_caída ≥ 0.8 s                                                                   (lectura mínima)
5. nada antes del primer pulso; primera nota ≥ una cuenta de 4 pulsos después del inicio
```

Si falla alguna, se **rechaza el chart** (en desarrollo, error; en producción, regenerar con otra semilla). La idea de filtrar patrones con un modelo del jugador antes de mostrarlos viene de Smith, Treanor, Whitehead y Mateas (FDG 2009, grupos rítmicos con verificación de jugabilidad), **citada de segunda mano vía `05_Endless_runner`: no la leí directamente** y no se verificó que el paper diga exactamente eso. Las reglas 1–5 son destilación propia.

**Mapear una canción a notas** (detección de onsets, charting automático) no está destilado. Para el portfolio, charts escritos a mano o generados desde la grilla de pulsos.

---

## Feedback de acierto y de fallo

```txt
ACIERTO    (en el cuadro del toque)  mosaico cambia + sonido (nota) + etiqueta de precisión + racha
FALLO      tocar mal:  el mosaico tocado se pone rojo y el que debía tocarse parpadea
           dejar pasar: la fila que salió parpadea; el mundo se detiene
PANEL      puntaje, mejor puntaje, y qué pasó (tocar mal / dejar pasar)
REINTENTO  gesto explícito (botón, Enter, R): habilitado a 0.3 s
           toques sobre el carril: bloqueados 0.75 s (se tocaba 2–5 veces por segundo; misma lógica que el runner, 0.75–1.2 s allá; destilación propia)
```

---

## Baseline de parámetros

Punto de partida, no dogma. En **tiempo** y en relaciones. Todo es destilación propia, a calibrar en playtest, salvo donde se cita.

| Parámetro | Relación | Baseline | Calibración |
|-----------|----------|----------|-------------|
| Carriles `N` y filas visibles `R` | — | N = 4, R = 4 | destilación propia (ver *Límites*) |
| Δ al arrancar | `1 / toques por s` | 0.50 s (2 toques/s) | — |
| `T_caída` al arrancar | `R · Δ` | 2.0 s | 4 × 0.50 |
| Δ a tope | — | 0.20 s (5 toques/s) | — |
| `T_caída` a tope | `R · Δ` | 0.80 s | 4 × 0.20 |
| `v_max / v0` | `Δ0 / Δmax` | 2.5 | 0.50 / 0.20 |
| Ventana de lectura | `(R − 1) · Δ` | 1.5 s al arrancar, 0.6 s a tope; piso 0.5 s | `05_Endless_runner` cita > 0.5 s en Canabalt |
| Rampa (clásico) | toques/s lineal en el tiempo | `r(t) = 2 + 0.03·t` hasta `t = 100 s` | 2 → 5 toques/s; 350 toques hasta el tope |
| Hito | cada 25 toques | 12.5 s al inicio, 5 s a tope | 25/2 y 25/5 |
| `T_caída` en sincronizado | constante por canción | **1.2 s** por defecto; rango 0.8–1.5 s | osu! lo llama preempt: 1200 ms a AR 5, 450 a AR 10 (referencia, no regla) |
| Notas/s en sincronizado | `BPM × sub / 60` | ≤ 5; ejemplo 100 BPM × 2 = 3.33/s (Δ = 0.30 s) | 150 BPM × 2 = 5.0/s |
| Ventana "Perfecto" | `±` | ±50 ms | osu!mania OD 5: ±49 |
| Ventana "Bueno" | `±` | ±80 ms | osu!mania OD 5: ±82 |
| Ventana "Aceptable" (límite del acierto) | `±` | ±110 ms | osu!mania OD 5: ±112 |
| Separación en mismo carril | `S ≥ 2 · W_aceptable` | ≥ 0.22 s | — |
| Calibración | 8 toques, mediana de 6 | rango ±200 ms | rango: destilación propia |
| Lookahead de audio | intervalo / adelanto | 25 ms / 100 ms | web.dev, *Audio scheduling* |

**Chequeo cruzado** (ningún valor contradice a otro): `T_caída` a tope clásico (0.80 s) = piso del chart sincronizado (≥ 0.8 s); el tope de 5 toques/s es el mismo en los dos modos; con Δ = 0.20 s el mismo carril exige S ≥ 0.22 s, así que a tope **no hay repetidos** en sincronizado (en clásico sí: sin ventanas simétricas, el plazo es la salida de la fila); `W_aceptable` ±110 ms contra Δ = 0.30 s del ejemplo es 73% del intervalo, sin ambigüedad porque las notas vecinas son de otro carril.

---

## Variantes, y qué parte del baseline reescribe cada una

Una variante no le agrega una fila al baseline: **lo pone entero bajo sospecha.**

| Variante | Qué reescribe |
|----------|---------------|
| **Zen** (sin aceleración) | La rampa: `v` constante. Se pierde el récord por cadencia; hay que sustituirlo (puntos, precisión) |
| **Rush / contrarreloj de toques** | La meta (X toques en tiempo fijo) y la rampa. El hito deja de ser cada 25 toques |
| **Sincronizado con canción** | Rampa → densidad de la canción; `T_caída` fija; juicio por ventanas; toda la sección de *Latencia* pasa a ser obligatoria |
| **Notas largas (hold)** | Aparece una segunda ventana: la de soltar. StepMania tiene holds (hay que sostener el apoyo durante todo el largo de la nota) y mines (objetos que se evitan). La tapabilidad cambia: el dedo queda ocupado |
| **Vida en vez de muerte súbita** | `15_Muerte_reintento_y_checkpoints`: reintento en el mismo punto; las ventanas se vuelven más importantes que el error único |
| **Modo accesible** | Δ0 más largo, tope más bajo, `T_caída` ≥ 1.5 s, ventanas ×1.5, sin repetidos, y cuenta de entrada de 8 pulsos. **Todo junto, destilación propia**: tocar una sola perilla rompe las relaciones |

---

## Definición de Terminado

Checklist del género. Se corre **sobre el juego corriendo**, no sobre el código.

```txt
LECTURA Y VELOCIDAD
[ ] El juego espera mi primer toque (o me da una cuenta) y no hay error en la primera fila
[ ] La cadencia sube de forma que se nota, y en algún momento deja de subir
[ ] A velocidad máxima todavía leo las 3 filas siguientes
[ ] Va igual de rápido a 60 Hz y a 120+ Hz
[ ] Nada tapa el carril
JUICIO
[ ] Tocar en celda vacía mata; dejar pasar una fila mata
[ ] En sincronizado, un toque dentro de ±110 ms de una nota cuenta; fuera no
[ ] El juicio sale del instante del toque, no del cuadro: a 30 FPS y a 144 FPS el resultado es el mismo
[ ] Un patrón de más de 5 notas/s o con repetidos más cerca de 0.22 s no existe
LATENCIA
[ ] Hay pantalla de calibración y su resultado persiste
[ ] Con offset 0 y con un offset de ±100 ms, el juicio se desplaza ese valor
[ ] Abrir el juego sin tocar nada no intenta sonar: el audio arranca con un gesto
[ ] La calibración no suena al tocar
PARTIDA Y ESTADOS
[ ] Veo mi puntaje y mi récord mientras juego; el récord sobrevive a cerrar y abrir
[ ] Al fallar veo cuál toqué y cuál debía
[ ] Los toques sobre el carril no reinician el juego durante 0.75 s
[ ] Vuelvo a jugar en un gesto y en menos de un segundo y medio
[ ] Si cambio de pestaña, el juego se pausa; al volver hay cuenta regresiva
FEEL
[ ] El mosaico reacciona en el cuadro en que toco, y el sonido no se oye retrasado
[ ] Acierto, hito y error suenan distinto entre sí
[ ] Teclado, mouse y toque se sienten iguales
```

Un rhythm tap que corre y suena pero no tilda **Juicio** y **Latencia** es el 4/10 de la Ley #1: la demo técnica que obliga a gastar prompts en trabajo remedial.

---

## Aplicación

- **Cuándo se abre este libro:** ante cualquier pedido de "como Piano Tiles", "no toques lo blanco", tap rítmico o juego de carriles con caída. Producción lo carga al escribir el `RQ`; Game Design lo cruza con las relaciones de *Ventanas*; Level Design usa el validador como medida del "nivel".
- **Qué trae la IA por default:** las 14 table-stakes, la relación `T_caída = alto / velocidad`, el baseline en tiempo, el validador de patrones, el flujo de calibración y la Definición de Terminado.
- **Qué NO decide este libro:** el tema, el arte, qué canciones, la meta-progresión, ni la plataforma.

**Si va al portfolio web** (HTML + CSS + JS sin frameworks, canvas 2D y Web Audio):
- **Canvas 2D** con `requestAnimationFrame`; las posiciones se calculan del **tiempo** (`y = (t_actual − t_nota) · v`), no sumando por cuadro, para que 60 y 144 Hz den lo mismo. `01_Bucle_de_simulacion`
- **Entrada:** teclado (4 teclas, p. ej. D F J K) y mouse/puntero sobre cada carril; el juicio lee `event.timeStamp` del evento, no el instante en que el cuadro lo procesa (table-stake 7).
- **Audio:** crear o reanudar el `AudioContext` **dentro de un gesto del usuario** (el botón "Jugar"): nace `suspended` y no suena hasta entonces (MDN, *Best practices*; la especificación permite al navegador restringirlo a activación pegajosa). La página inicial debe funcionar sin sonido y explicar que hace falta un clic.
- **Reloj maestro:** el del audio (`currentTime` / `getOutputTimestamp()`), nunca `setTimeout` ni `Date.now()` (web.dev: `Date.now()` devuelve milisegundos, y a 44.1 kHz eso es unas 44 veces demasiado lento como reloj de programación de audio).
- **Latencia del navegador:** variable por dispositivo y puede cambiar; pedir `latencyHint` es una sugerencia que el navegador puede ignorar (MDN). La calibración manual es la red de seguridad. Audio por Bluetooth: ver *Límites*.
- **Pausa y persistencia:** `visibilitychange` pausa y exige cuenta al volver; récord y offset en `localStorage` con `try/catch`; sonidos de toque en buffers ya decodificados.

## Límites

- Es un libro de **experiencia**. Cómo se implementa el scheduler, el validador o el mapeo de clocks es materia del `SOL`.
- **Ningún número del baseline está validado con jugadores ni con un juego corriendo.** Las ventanas de osu!mania son de otro juego y de otro público; la cadencia máxima de 5 toques/s es destilación propia, no un límite humano verificado.
- **No verificado:** (a) cuántas filas muestra Piano Tiles y cuántos carriles usa en cada modo; (b) velocidades, rampas o tope reales del Don't Tap The White Tile (la fuente leída habla de aceleración solo cualitativamente); (c) el contenido y las reglas de cada modo del juego original más allá de sus nombres; (d) las ventanas de StepMania distintas de la "flawless" (los foros disponibles no eran fuente sólida); (e) las de Guitar Hero (no se halló fuente primaria); (f) cuánto se desvían `outputLatency` y `getOutputTimestamp` de la latencia real en cada navegador y dispositivo; (g) la latencia típica del audio por Bluetooth (no se leyó fuente); (h) cómo se reparten los eventos de teclado y puntero entre cuadros en cada navegador.
- **Discrepancia de nombres, sin resolver con fuente primaria:** el encargo nombra a "Hu Wenzhou" y "Cheetah Mobile/Umoni, 2014"; la única fuente que lo confirma (Wikipedia, releída el 2026-10-13) dice "Hu Wen Zeng", de Umoni Studio, 28/03/2014, y a Cheetah Mobile le atribuye la secuela (19/08/2015). No se halló ninguna fuente que respalde "Hu Wenzhou"; el libro usa "Hu Wen Zeng" atribuido a Wikipedia y deja abierta la grafía. Otra fuente secundaria (Grokipedia, leída) trae cifras de descargas contradictorias entre sí: no se usan. Un artículo general de diseño (bugnet.io) solo da consejos cualitativos y tampoco aporta números. Ninguna de las dos se lista en *Fuentes* porque no sustenta ningún dato del libro.
- **Verificación del Validador (2026-10-13):** se contrastaron contra la página las fórmulas de ventana de osu! y osu!mania (valores de máximo error, o sea mitad del ancho), el preempt de AR, el redondeo de `Event.timeStamp`, los ejemplos de `baseLatency`, el flawless de StepMania, el 25 ms / 100 ms de web.dev y las muestras de Rhythm Quest: coinciden. Sin verificar: el texto de la especificación W3C (leída parcialmente) y de Giant Bomb.
- No cubre: detección automática de beats, charting a partir de audio arbitrario, juego en línea, ni la economía de canciones/monedas.
- El 4 × 4 (carriles × filas) es un baseline de este libro, no una propiedad del género: otro `N` o `R` cambia Δ y la ventana de lectura, y esas relaciones se recalculan.

---

## Fuentes

Leídas (consulta 2026-10-13):

- osu! wiki, *Judgement (osu!)* — https://osu.ppy.sh/wiki/en/Gameplay/Judgement/osu%21 — fórmulas de ventana por OD
- osu! wiki, *Judgement (osu!mania)* — https://osu.ppy.sh/wiki/en/Gameplay/Judgement/osu%21mania
- osu! wiki, *Approach rate* — https://osu.ppy.sh/wiki/en/Beatmap/Approach_rate
- osu! wiki, *Options* (universal offset, offset wizard) — https://osu.ppy.sh/wiki/en/Client/Options
- Wikipedia, *Piano Tiles* — https://en.wikipedia.org/wiki/Piano_Tiles — historia, fechas, modos
- Wikipedia, *StepMania* — https://en.wikipedia.org/wiki/StepMania — ventana "flawless", holds, mines
- MDN, `AudioContext.outputLatency`, `baseLatency`, `getOutputTimestamp()` — https://developer.mozilla.org/en-US/docs/Web/API/AudioContext
- MDN, *Web Audio API best practices* (autoplay, `currentTime`) — https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Best_practices
- MDN, `Event.timeStamp` — https://developer.mozilla.org/en-US/docs/Web/API/Event/timeStamp
- W3C, *Web Audio API* (especificación) — https://webaudio.github.io/web-audio-api/ — leído hasta el carácter 100000 de 115642
- web.dev, *Audio scheduling* — https://web.dev/articles/audio-scheduling — 25 ms / 100 ms
- Rhythm Quest, devlog 10, *Latency calibration* (ddrkirby, 2021-08-06) — https://rhythmquestgame.com/devlog/10.html
- Giant Bomb, *Lag Calibration* — https://giantbomb.com/wiki/Concepts/Lag_Calibration

Del vault: `05_Endless_runner` (de donde se cita Smith et al. sin haberlo leído), `01_Bucle_de_simulacion`, `02_Game_feel`, `10_Input_y_respuesta`, `14_UI_HUD_y_menus`, `15_Muerte_reintento_y_checkpoints`, `16_Audio_como_gameplay`, `06_Dificultad_y_curva`, `09_Onboarding_y_tutorial`, `12_Pacing_y_estructura`.

**Cobertura declarada:** de las 14 table-stakes, las **calibradas en fuente externa** son la 7 y la 8 (MDN, especificación, Rhythm Quest, osu!, Giant Bomb) y, en parte, la 9 (Wikipedia: cada toque correcto suena como una nota). Las demás y todo el baseline numérico de caída y cadencia son **destilación propia**. **Ninguna table-stake se validó con jugadores ni con un juego corriendo.**

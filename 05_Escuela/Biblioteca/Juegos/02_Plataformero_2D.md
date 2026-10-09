---
tipo: juego
genero: Plataformas
subtipo: Plataformero 2D de precision (single-screen a scroll lateral)
estado: En la Biblioteca
mision: EST-010_Mision_Plataformero_2D
cruza: 05_Fundamentos_de_experiencia_ludica, 02_Game_feel, 10_Input_y_respuesta, 11_Camara_y_encuadre, 15_Muerte_reintento_y_checkpoints, 06_Dificultad_y_curva
---

# Libro 02 — Plataformero 2D

> Segundo libro del estante de Juegos. Genero: Plataformas / plataformero 2D de precision.
> Lo **transversal** vive en `05_Fundamentos_de_experiencia_ludica`, `10_Input_y_respuesta` y `11_Camara_y_encuadre`; aca va lo **especifico**: que lo hace *ser* un plataformero y que lo hace *sentirse* bien.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Indice del libro

- Loop de experiencia
- Table-stakes
- Juice / game feel
- Baseline de parametros
- El salto, en detalle
- Definicion de Terminado
- Aplicacion
- Limites
- Fuentes

---

## Loop de experiencia

El loop del plataformero dura **entre dos y diez segundos** y su unidad no es el input sino **el intento**. Es el genero donde el fracaso es parte del ritmo: se muere, se reintenta, y la distancia entre las dos cosas es lo que define si el juego se siente justo o cruel.

```txt
LOOP ATOMICO (≈0.2–0.5 s)
  leer el espacio → decidir el salto → ejecutar → aterrizar (o no)
                          ↑                            │
                          └────────────────────────────┘

LOOP DE INTENTO (≈2–10 s)     entrar al desafio → encadenar 2–6 acciones → superarlo o morir
LOOP DE TRAMO  (≈30 s–3 min)  encadenar desafios → llegar al checkpoint → respirar
LOOP DE NIVEL  (≈3–10 min)    tramos → meta → sensacion de haber aprendido algo
```

Los cuatro anidan, y el que mas se olvida es el **loop de intento**: un plataformero sin muerte-y-reintento rapido no es facil, es otro juego. La friccion entre morir y volver a intentar es la variable que mas mueve la experiencia del genero, mas que la dificultad del desafio en si. `15_Muerte_reintento_y_checkpoints`, `18_Art_of_Failure`

**Que hace de un plataformero un juego y no un juguete:** el objetivo impuesto (llegar) y el obstaculo innecesario aceptado (no podes volar, la gravedad te tira). Sacale la gravedad y queda un juego de mover un punto. `21_The_Grasshopper`

**Donde vive la tension:** en la **incertidumbre de ejecucion** — se sabe que hay que hacer y no se sabe si va a salir. Es distinta de la incertidumbre de resultado de Pong: aca el jugador conoce la solucion y le falta la mano. Por eso el genero castiga la ambiguedad visual mas que ningun otro: si el jugador no sabe si algo es plataforma o decorado, la incertidumbre deja de ser de ejecucion y se vuelve injusta. `17_Uncertainty_in_Games`, `05_Game_Feel`

---

## Table-stakes

Lo que un plataformero **no puede no tener** para estar terminado. Si falta uno, no es "un plataformero minimo": es un plataformero roto.

| # | Table-stake | Por que es obligatorio |
|---|-------------|------------------------|
| 1 | **Movimiento horizontal con aceleracion y friccion**, no velocidad binaria | Un personaje que arranca y frena de golpe no tiene peso, y sin peso el jugador no puede anticipar donde va a caer. Es la base de todo lo demas |
| 2 | **Salto de altura variable** — soltar el boton antes corta el salto | Es el unico verbo expresivo del genero. Con salto fijo, el jugador ejecuta; con salto variable, **decide**. La diferencia es la que separa un plataformero de un autorunner |
| 3 | **Colision solida y estable**: no se atraviesa el piso, no se queda pegado a la pared, no tiembla en el borde | El fallo #1 del genero implementado a las apuradas. Rompe el Pilar 5 (justicia): el jugador hizo bien y perdio igual |
| 4 | **Coyote time y jump buffer** | Sin ellos el juego se siente roto aunque sea correcto. Ver *El salto, en detalle* |
| 5 | **Camara que sigue con deadzone y look-ahead** | Una camara pegada al personaje marea y no deja ver a donde se va. Una camara sin deadzone convierte cada paso en un temblor. `11_Camara_y_encuadre` |
| 6 | **Legibilidad de superficie**: se distingue de un vistazo que es piso, que es pared, que mata y que es decorado | La incertidumbre del genero es de ejecucion. Cualquier duda sobre *que es* una cosa es una muerte injusta |
| 7 | **Muerte y reintento con friccion minima** — checkpoint cercano y vuelta en menos de un segundo | Determina el ritmo del genero. Un reintento de tres segundos con animacion convierte diez muertes en media hora de espera |
| 8 | **Objetivo visible y meta alcanzable** — se sabe a donde hay que llegar | Sin meta el nivel es un sandbox. `05_Fundamentos_de_experiencia_ludica` |
| 9 | **Estados completos**: inicio, pausa, muerte, victoria, y volver a jugar sin cerrar | Table-stake transversal, y en este genero es donde mas se olvida el "reintentar nivel" |
| 10 | **Feedback de aterrizaje y de golpe** | El aterrizaje es el evento mas repetido del juego. Si no suena ni se ve, el juego se siente mudo |

---

## Juice / game feel

El plataformero es el genero donde el *juice* no es decoracion: **es informacion**. Cada efecto de esta lista comunica un estado del sistema.

| Efecto | Que comunica | Cuidado |
|--------|--------------|---------|
| **Squash al aterrizar / stretch al saltar** | peso e impacto; confirma que el aterrizaje se registro | 60–100 ms. Mas largo se lee como lag |
| **Particulas de polvo** al despegar y al aterrizar | el contacto con el piso, sin mirar los pies | 3–6 particulas. Mas tapa el nivel |
| **Screenshake** al morir o al impacto fuerte | que paso algo grave | Nunca al saltar ni al aterrizar normal: se vuelve ruido. `59_The_Art_of_Screenshake` |
| **Hitstop / freeze frame** de 2–5 frames en el golpe | contundencia | Solo en eventos raros. En algo que pasa cada segundo es lag |
| **Trail o motion blur** en caida rapida | velocidad, y ayuda a leer la trayectoria | Que no tape el hitbox |
| **Sonido distinto para saltar, aterrizar, morir y recoger** | los cuatro eventos del loop | Cuatro sonidos distintos es el minimo. Uno solo se vuelve invisible |
| **Camara que baja un poco en la caida larga** | que viene un aterrizaje | Sutil: 5–10% de la pantalla |

Regla del genero, heredada de `02_Game_feel`: **el juice nunca puede impedir ver el proximo apoyo.** En Pong la regla era no tapar la pelota; aca es no tapar la plataforma.

---

## El salto, en detalle

Es el 80% del genero y merece su propia seccion. Un salto "correcto" fisicamente se siente mal; un salto que se siente bien es **una mentira deliberada y bien afinada**.

Las seis mentiras que el jugador espera sin saber que existen:

| # | Mentira | Que hace | Baseline |
|---|---------|----------|----------|
| 1 | **Coyote time** | dejar saltar unos frames despues de haberse ido del borde | 4–7 frames (≈70–120 ms) |
| 2 | **Jump buffer** | registrar el salto apretado poco antes de tocar el piso | 4–8 frames (≈70–130 ms) |
| 3 | **Gravedad asimetrica** | caer mas rapido de lo que se sube | caida 1.6–2.2× la subida |
| 4 | **Corte de salto** | soltar el boton corta el impulso hacia arriba | al soltar, velocidad vertical ×0.4–0.5 |
| 5 | **Apex hang** | menos gravedad en la cima del salto | 0.5–0.8× la gravedad, ±0.1 de vel. vertical |
| 6 | **Corner correction** | empujar al personaje unos pixeles si roza una esquina | 1–4 px |

Sin la 1 y la 2 el juego se siente roto aunque cada colision sea exacta: el jugador percibe que aprieto y no salto. Son las dos que **no son opcionales**. `10_Input_y_respuesta`, `34_Celeste`

La 3 es la que mas cambia el caracter: gravedad simetrica se siente flotante y lunar; asimetrica se siente atletica y controlada.

**Trampa conocida:** resolver el salto con el motor de fisica y un `AddForce`. El resultado es correcto y no se puede afinar, porque las seis mentiras necesitan control directo sobre la velocidad frame a frame. El plataformero, como Pong, **no usa fisica: usa cinematica escrita a mano.** Es la decision tecnica que define el genero. `46_Game_Engine_Architecture`, `37_Level_up_your_code_with_game_programming_patterns`

---

## Baseline de parametros

Punto de partida razonable, no dogma. En unidades relativas a la **altura del personaje (A)** para que escalen a cualquier escala de mundo. Se ajustan jugando, nunca en el papel.

| Parametro | Baseline | Por que |
|-----------|----------|---------|
| Altura de salto | 2.5–3.5 A | Menos se siente pesado; mas se siente lunar |
| Largo de salto (a velocidad plena) | 4–6 A | Define el ancho maximo de un hueco |
| Tiempo hasta el apice | 0.35–0.45 s | Debajo de 0.3 se siente nervioso; arriba de 0.5, flotante |
| Velocidad horizontal maxima | 6–9 A/s | Tiene que poder cruzar la pantalla en 2–3 s |
| Aceleracion horizontal | llegar al maximo en 0.1–0.2 s | Respuesta sin patinaje |
| Friccion / frenado | detenerse en 0.08–0.15 s | Mas largo se siente sobre hielo |
| Control en el aire | 60–80% del control en piso | 100% se siente irreal; 0% se siente injusto |
| Velocidad terminal de caida | 1.5–2× la velocidad horizontal max | Evita caidas ingobernables |
| Ancho de hueco tipico | 45–70% del largo de salto | Margen de error para el jugador medio |
| Distancia entre checkpoints | 20–45 s de juego limpio | Ver table-stake 7 |
| Tiempo de reintento tras morir | < 1 s, ideal 0.3–0.5 s | Es el parametro que mas define el ritmo del genero |
| Deadzone de camara | 15–25% del ancho de pantalla | Ver `11_Camara_y_encuadre` |
| Look-ahead de camara | 10–20% del ancho, con 0.2–0.4 s de suavizado | Muestra a donde se va, no donde se esta |

**Regla de oro del genero:** los parametros no se eligen sueltos. Se elige **el salto** —altura, largo, tiempo al apice— y todo lo demas, incluido el ancho de cada hueco del nivel, se deriva de ahi. Un nivel disenado antes de que el salto este afinado hay que rehacerlo entero. `33_The_Level_Design_Book`

---

## Definicion de Terminado

Checklist especifica del genero. Se corre **sobre el juego corriendo**, no sobre el codigo.

```txt
MOVIMIENTO
[ ] Camino, acelero y freno con peso: puedo anticipar donde voy a parar
[ ] El salto responde en el frame en que aprieto
[ ] Soltar el boton antes hace un salto mas corto, siempre
[ ] Salto justo despues de irme del borde y sale (coyote time)
[ ] Aprieto salto justo antes de aterrizar y sale al tocar (jump buffer)
[ ] No atravieso el piso a ninguna velocidad, ni me quedo pegado a una pared

DESAFIO
[ ] Cada hueco es superable con el salto que tengo, y se ve que lo es
[ ] Cuando muero, se por que mori
[ ] Vuelvo a intentar en menos de un segundo
[ ] El checkpoint mas cercano no me hace repetir algo que ya resolvi

CAMARA Y LECTURA
[ ] Veo a donde voy antes de llegar: no salto a ciegas
[ ] La camara no tiembla cuando camino
[ ] Distingo piso, pared, peligro y decorado de un vistazo, sin que nadie me lo explique
[ ] Se donde esta la meta o hacia donde tengo que ir

PARTIDA Y ESTADOS
[ ] Hay una meta y llegar a ella termina el nivel de forma visible
[ ] Puedo pausar y despausar
[ ] Puedo reintentar el nivel sin cerrar la aplicacion
[ ] Toda pantalla tiene salida
[ ] Se que teclas uso, sin que nadie me lo explique

FEEL
[ ] El aterrizaje se ve y se escucha como un evento
[ ] La muerte se siente distinta (mas grande) que un aterrizaje
[ ] Saltar, aterrizar, morir y recoger suenan distinto entre si
[ ] El juice nunca me impide ver el proximo apoyo
```

Un plataformero que compila y salta pero no tilda **Desafio**, **Camara y lectura** y **Feel** esta en el 4/10 de la Ley #1: es la demo tecnica que obliga al usuario a gastar prompts en trabajo remedial.

---

## Aplicacion

- **Cuando se abre este libro:** ante cualquier pedido de plataformero, metroidvania, precision platformer, runner con salto o juego de accion lateral con gravedad. Produccion lo carga al escribir los `RQ`; Game Design lo cruza con el CHECKLIST de 9 pilares al escribir el `GDS`; **Level Design lo usa como fuente de las medidas del espacio**, porque el ancho de un hueco no es una decision estetica sino una derivada del salto.
- **Que trae la IA por default sin que se lo pidan:** las 10 table-stakes, las seis mentiras del salto, el baseline de parametros y la Definicion de Terminado completa.
- **Que NO decide este libro:** el motor, la estetica, si hay combate, si hay progresion o coleccionables, cuantos niveles hay. Eso lo declara el `RQ`.

## Limites

- Es un libro de **experiencia**, no de implementacion. Como se resuelve la colision continua o el barrido de tiles es materia del `SOL`.
- El baseline vale para el plataformero de **precision** con un solo verbo de movimiento. Un metroidvania agrega progresion de habilidades y backtracking, que reescriben la curva y el diseno de nivel: `63_Boss_Keys` es la fuente y es **mision de profundizacion**, no esta destilada aca.
- **El combate no esta cubierto.** Un plataformero con enemigos que se enfrentan (y no solo se esquivan) agrega un sistema entero — telegrafia, i-frames, knockback — que este libro no toca.
- **La velocidad como fantasia** (Sonic) es otro subgenero con otras reglas: momentum conservado, niveles con multiples alturas y una camara distinta. Fuente fichada: `58_Sonic_Physics_Guide`. Tambien mision de profundizacion.

---

## Fuentes

Destilado por recombinacion sobre fichas ya catalogadas del vault, mas dos fuentes propias del genero:

- `34_Celeste_codigo_fuente_del_juego_y_del_prototipo_PICO` — referencia tecnica del game feel en plataformas; origen documentado de coyote time y corner correction
- `58_Sonic_Physics_Guide` — el subgenero de momentum, usado por contraste
- `05_Game_Feel` — el marco de las tres capas (input, simulacion, contexto)
- `10_Input_y_respuesta` — coyote time, jump buffer y ventanas de tolerancia
- `11_Camara_y_encuadre` — deadzone, look-ahead y suavizado
- `15_Muerte_reintento_y_checkpoints` — friccion del reintento
- `06_Dificultad_y_curva` — la curva por tramo
- `59_The_Art_of_Screenshake`, `60_Juice_It_or_Lose_It` — feedback
- `33_The_Level_Design_Book`, `35_Hows_and_Whys_of_Level_Design` — el espacio derivado del salto
- `63_Boss_Keys` — declarada fuera de alcance, anotada como profundizacion

**Cobertura declarada:** de las 10 table-stakes, **siete** salieron de fichas transversales que ya existian en la Biblioteca y **tres** —2 (salto variable), 4 (coyote/buffer) y 6 (legibilidad de superficie)— necesitaron destilacion propia. Es exactamente el caso que la candidata *"un gate binario sobre un vault que no lo es"* describia: la respuesta a *¿existe el libro del genero?* era "a medias", y la mision costo destilar tres, no escribir nueve.

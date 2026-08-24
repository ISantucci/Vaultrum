---
tipo: juego
genero: Arcade
subtipo: Paleta-y-pelota
estado: En validación
mision: [[EST-001_Mision_Pong]]
cruza: 05_Fundamentos_de_experiencia_ludica, 01_Loop_de_experiencia, 02_Game_feel, 03_Definicion_de_terminado
---

# Libro 01 — Pong

> Primer libro del estante de Juegos. Género: Arcade / paleta-y-pelota.
> Lo **transversal** vive en [[05_Fundamentos_de_experiencia_ludica]]; acá va lo **específico de Pong**: qué lo hace *ser* Pong y qué lo hace *sentirse* bien.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Índice del libro

- Loop de experiencia
- Table-stakes
- Juice / game feel
- Baseline de parámetros
- Definición de Terminado
- Aplicación
- Límites
- Fuentes

---

## Loop de experiencia

El loop de Pong dura **menos de un segundo** y se repite decenas de veces por rally. Es el loop más corto que existe en un videojuego, y por eso es el mejor caso de estudio: no hay contenido, narrativa ni progresión donde esconderse. Si el loop no se siente bien, no hay Pong.

```txt
LOOP ATÓMICO (≈0.3–1 s)
  leer trayectoria de la pelota → mover la paleta → interceptar → ver el rebote salir
                                        ↑                              │
                                        └──────────────────────────────┘

LOOP DE PUNTO (≈5–20 s)          rally → alguien falla → gol → saque
LOOP DE PARTIDA (≈2–5 min)       puntos → llegar al puntaje objetivo → victoria/derrota → revancha
```

Los tres loops anidan (Pilar 1 de [[05_Fundamentos_de_experiencia_ludica]]): siempre hay algo que perseguir *ahora* (esta pelota), algo a mediano plazo (este punto) y algo por lo que volver (la revancha). El error clásico al implementar un Pong es construir solo el loop atómico —pelota que rebota— y llamarlo juego. Sin el loop de partida no hay stakes: `18_Art_of_Failure`, `21_The_Grasshopper`.

**Qué hace de Pong un juego y no un juguete:** el objetivo impuesto (llegar al puntaje) y el obstáculo innecesario aceptado voluntariamente (solo podés mover la paleta en un eje). Sacale cualquiera de los dos y queda un salvapantallas. `21_The_Grasshopper`, `06_Half_Real`

**Dónde vive la tensión:** en la incertidumbre del resultado. Pong es agon puro —habilidad contra habilidad, sin azar— y su fuente de incertidumbre es el desempeño del oponente y el propio. `23_Man_Play_and_Games`, `17_Uncertainty_in_Games`

---

## Table-stakes

Lo que un Pong **no puede no tener** para estar terminado. Si falta uno, no es "un Pong mínimo": es un Pong roto.

| # | Table-stake | Por qué es obligatorio |
|---|-------------|------------------------|
| 1 | **Dos paletas controlables**, una por jugador, movimiento en un solo eje, con límites de cancha | Es el único verbo del juego. Sin límites, el jugador sale de la cancha y el sistema pierde sentido |
| 2 | **Pelota con rebote continuo** contra paletas y paredes, sin atravesar nada | El fallo #1 de todo Pong implementado a las apuradas es el tunneling. Una pelota que atraviesa la paleta rompe el Pilar 5 (justicia): el jugador hizo bien y perdió igual |
| 3 | **El ángulo de salida depende de dónde pega en la paleta** | Sin esto la paleta es un espejo y el jugador no toma decisiones: solo reacciona. Es lo que convierte a Pong de reflejo en decisión (Pilar 9) |
| 4 | **Gol y puntaje visible** para ambos jugadores en todo momento | Sin marcador el esfuerzo no acumula hacia nada y el jugador no puede responder "¿lo estoy logrando?" (Pilar 4) |
| 5 | **Condición de victoria explícita** (puntaje objetivo) y **fin de partida perceptible** | Sin condición de fin no hay tensión ni logro (Pilar 2) |
| 6 | **Saque tras cada gol**, con una pausa breve y legible | El saque instantáneo tras un gol se siente injusto: el jugador todavía está procesando que perdió el punto. La pausa es lo que hace legible la derrota |
| 7 | **Reintento inmediato** al terminar la partida, sin salir de la aplicación | El fracaso tiene que retener, no expulsar (Pilar 7). Un game over sin revancha es un estado muerto |
| 8 | **Pausa** y salida de cada pantalla | Sin pausa ni salida hay estados muertos: el jugador queda atrapado (Pilar 2) |
| 9 | **Controles comunicados** sin manual externo | Un juego de dos jugadores locales donde el segundo no sabe qué teclas usar no arranca (Pilar 4) |

**Nota sobre el saque:** dárselo siempre al mismo jugador es un sesgo. La convención justa es sacar **hacia quien acaba de recibir el gol** —le devuelve la iniciativa a quien va perdiendo, que es también catch-up suave (Pilar 6).

---

## Juice / game feel

Pong es un caso extremo: **casi todo su feel está en tres frames alrededor del impacto**. Como el resto del juego es geometría en movimiento, el momento del golpe es el único lugar donde se puede comunicar peso.

| Momento | Qué se siente sin juice | Qué lo arregla |
|---------|-------------------------|----------------|
| **Impacto con la paleta** | La pelota "cambia de dirección". Sin peso, sin evento | Hit-stop muy corto (~40–60 ms) + squash de la paleta en el eje del impacto + destello + sonido con ataque rápido. `05_Game_Feel` |
| **Rebote en pared** | Ruido de fondo | La mitad de todo lo anterior. Debe leerse como *menos* importante que el golpe de paleta: la jerarquía del feedback enseña qué importa (Pilar 4) |
| **Gol** | Un número que cambia | Hit-stop más largo (~120–160 ms) + shake + flash del lado que recibió + el marcador que crece un instante. Es el único momento donde el juego puede permitirse gritar |
| **Movimiento de la paleta** | Teleport, control "resbaloso" | Aceleración corta (~60–100 ms a velocidad plena) y frenado igual de corto. Sin inercia se siente digital; con demasiada, se siente ingobernable. `05_Game_Feel` |
| **Rally largo** | Se hace monótono | La pelota acelera por golpe (con techo) y el sonido del impacto **sube de tono** con el conteo del rally. Es pacing dentro del punto (Pilar 8): la tensión sube sola, sin cambiar reglas |

**Regla de oro del juice en Pong:** el juice amplifica el impacto, nunca esconde la pelota. Un screenshake que impide leer la trayectoria convierte el Pilar 3 en una violación del Pilar 4. Si hay que elegir, gana la legibilidad.

**El feel se valida con cubos grises.** Pong *es* el prototipo gris. Si no se siente bien sin arte, no hay arte que lo salve. `03_Game_Design_Workshop`, `08_Designing_Games`

---

## Baseline de parámetros

Punto de partida razonable, no dogma. Están en unidades relativas al **alto de la cancha (H)** para que escalen a cualquier tamaño de arena. Se ajustan jugando, nunca en el papel.

| Parámetro | Baseline | Por qué |
|-----------|----------|---------|
| Alto de paleta | 0.16–0.20 H | Más corta se siente injusta; más larga mata el rally |
| Velocidad de paleta | 0.75–1.0 H/s | Debe poder cruzar media cancha en el tiempo que tarda la pelota en volver |
| Rampa de aceleración de paleta | 60–100 ms | Peso sin lag |
| Velocidad inicial de pelota | 0.6–0.8 H/s | Debe permitir leer el saque |
| Incremento por golpe | +3–5 % | Se siente sin volverse ingobernable |
| Techo de velocidad | ≈2.2× la inicial | Pasado ese punto deja de ser habilidad y es lotería |
| Ángulo máximo de salida | 50–60° respecto del eje de juego | Más plano aburre; más abierto vuelve la pelota impredecible |
| Ángulo mínimo de salida | 10–15° | Evita el rally horizontal infinito, que es el bug de diseño clásico de Pong |
| Puntaje objetivo | 7 (rango 5–11) | Partida de 2–5 min: suficiente para que haya remontada, corto para pedir revancha |
| Pausa de saque | 0.8–1.2 s | Tiempo para procesar el gol y prepararse |

**Trampa conocida:** si el ángulo se calcula reflejando sobre la normal (física realista) en vez de derivarlo del punto de impacto, el juego es correcto y aburrido. Pong no usa física: usa la paleta como **dial de puntería**. Es la decisión de diseño que define el género. `13_Elements_of_Game_Design`

---

## Definición de Terminado

Checklist específica de Pong. Se corre **sobre el juego corriendo**, no sobre el código.

```txt
LOOP
[ ] Puedo mover mi paleta y la pelota rebota en ella, siempre, a cualquier velocidad
[ ] Dónde pego cambia hacia dónde sale: puedo apuntar
[ ] La pelota nunca atraviesa una paleta ni una pared, ni se queda trabada

PARTIDA
[ ] Hay marcador visible para los dos jugadores
[ ] Hay un puntaje objetivo declarado y la partida termina al alcanzarlo
[ ] Sé quién ganó sin tener que interpretar números
[ ] Puedo jugar de nuevo sin cerrar la aplicación

ESTADOS
[ ] Puedo pausar y despausar
[ ] Toda pantalla tiene salida: no hay pantalla sin acción posible
[ ] Tras un gol hay un saque legible, no un reinicio instantáneo

CLARIDAD
[ ] Sé qué teclas uso yo y qué teclas usa el otro jugador, sin que nadie me lo explique
[ ] Distingo mi lado del lado del rival de un vistazo
[ ] En todo momento puedo responder: qué pasa / qué puedo hacer / cómo voy

FEEL
[ ] El golpe contra la paleta se ve y se escucha como un evento, no como un cambio de rumbo
[ ] El gol se siente distinto (más grande) que un rebote
[ ] La paleta responde en el instante en que aprieto, y frena con peso, no de golpe
[ ] Un rally largo sube de tensión por sí solo
[ ] El juice nunca me impide ver la pelota
```

Un Pong que compila y rebota pero no tilda **Estados**, **Claridad** y **Feel** está en el 4/10 de la Ley #1: es la demo técnica que obliga al usuario a gastar prompts en trabajo remedial.

---

## Aplicación

- **Cuándo se abre este libro:** ante cualquier pedido de Pong o variante paleta-y-pelota (Breakout, Air Hockey, Volley arcade, Pong 3D/VR, Pong con power-ups). Producción lo carga al escribir los `RQ`; Game Design lo cruza con el CHECKLIST de 9 pilares al escribir el `GDS`.
- **Qué trae la IA por default sin que se lo pidan:** las 9 table-stakes, el baseline de parámetros y la Definición de Terminado completa. El usuario gasta sus prompts en *su* variante (3D, power-ups, IA rival, online), no en pedir que haya marcador.
- **Qué NO decide este libro:** el motor, la dimensión, la estética, el modo de juego (1P vs IA, 2P local, online). Eso lo declara el `RQ`.

## Límites

- Es un libro de **experiencia**, no de implementación. Cómo se resuelve la colisión continua o el loop de simulación es materia del `SOL`, no de acá.
- El baseline de parámetros vale para el Pong canónico de dos jugadores. Una variante con power-ups, más de dos paletas o gravedad **reescribe el balance**, no lo hereda.
- El modo **1 jugador contra IA** agrega un problema que este libro no cubre: el ajuste de dificultad del rival y la percepción de justicia frente a una IA que no falla. Es misión de profundización.
- No mergea al Core: es candidato `EST` para Conocimiento; el owner aprueba.


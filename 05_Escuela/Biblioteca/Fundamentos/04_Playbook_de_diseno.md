---
tipo: fundamento
estado: En la Biblioteca
mision: EST-004_Mision_Destilacion_Playbook
alimenta_desde: 00_Indice_fuentes (fuentes 01–29)
---

# Fundamento 04 — Playbook de diseño (destilado del canon)

> Destilación transversal de las 29 fuentes del estante Fuentes en **principios accionables**, ordenados por **para qué sirven al desarrollar un juego**.
> Cada principio es una regla de bolsillo con su origen entre corchetes. **IP:** conceptos + cita, nunca texto verbatim.
> No reemplaza a los libros `01_Loop_de_experiencia`, `02_Game_feel` y `03_Definicion_de_terminado`: los alimenta y los cruza.

## Índice del libro

- A. Mostrarle algo al jugador — comunicación, feedback, legibilidad
- B. Guiarlo y enseñarle — onboarding y curva de aprendizaje
- C. Que se sienta bien de controlar — game feel y juice
- D. Que tome decisiones interesantes — agencia e incertidumbre
- E. Retenerlo y motivarlo — enganche, progresión, fracaso
- F. Diseñar sus sistemas y economía — mecánicas, loops, balance
- G. Hacerlo sentir algo — emoción, significado, ética
- H. Fundamentos conceptuales — qué es un juego, reglas vs ficción
- I. Llevarlo a producción — proceso, fases, prototipado
- J. Restricciones como material — plataforma y límites
- Cómo usar este playbook
- Fuentes

---

## A. Mostrarle algo al jugador — comunicación, feedback, legibilidad

Qué necesita ver, oír y entender el jugador para actuar. Si no lo percibe, para él no existe.

- **Feedback discernible e integrado.** Toda acción del jugador debe producir un efecto que se *perciba* (discernible) y que además *importe* dentro del juego (integrado). Ese es el "meaningful play". Si la acción no tiene efecto visible o el efecto no importa, la interacción está muerta. [Rules of Play; The Game Design Reader]
- **Affordances y signifiers.** Un objeto debe sugerir qué se puede hacer con él (affordance) y señalizarlo de forma visible (signifier). El jugador no usa lo que no ve que puede usar. [The Design of Everyday Things]
- **Feedback inmediato antes que texto.** El jugador aprende por consecuencia visible, no leyendo. Mostrá el resultado al instante y reservá el texto para lo que no se puede mostrar. [The Design of Everyday Things; The Gamer's Brain]
- **El juice es comunicación, no adorno.** Partículas, screenshake, sonido, tweening: amplifican la respuesta para que el input se sienta *reconocido*. La respuesta percibida pesa más que la respuesta real. [Game Feel; Designing Games]
- **La atención es un recurso limitado.** Dirigí la mirada del jugador con contraste, movimiento y ubicación; no compitas con vos mismo por su atención. Lo importante tiene que destacar perceptualmente. [The Gamer's Brain; The Design of Everyday Things]
- **Mapping natural.** Que el control se corresponda espacial e intuitivamente con su efecto (arriba = subir, derecha = derecha). El mapping arbitrario se paga en errores. [The Design of Everyday Things]
- **Mostrar el estado, siempre.** En todo momento el jugador debe poder responder: ¿qué está pasando?, ¿qué puedo hacer?, ¿lo estoy logrando? Si alguna queda sin respuesta, hay un agujero de legibilidad. [The Gamer's Brain; Elements of Game Design]
- **Incertidumbre legible.** Cuando hay azar o riesgo, mostralo de forma clara para que la tensión sea informada y no se sienta arbitraria o injusta. [Uncertainty in Games]

---

## B. Guiarlo y enseñarle — onboarding y curva de aprendizaje

Cómo llevar al jugador de no saber nada a dominar el sistema sin expulsarlo en el camino.

- **La diversión es aprender patrones.** El juego entretiene mientras el cerebro descubre estructura nueva; aburre cuando ya la dominó o cuando es ilegible. Diseñá la progresión como una secuencia de patrones a dominar. [A Theory of Fun]
- **Enseñar haciendo, no con tutoriales de texto.** Introducí cada mecánica en un contexto seguro donde el jugador la descubra experimentando, con bajo costo de error. [Game Design Workshop; The Gamer's Brain; The Art of Game Design]
- **Una habilidad nueva por vez.** Escaloná la complejidad: presentar, consolidar, recién después combinar. [A Theory of Fun; Game Design Workshop]
- **El onboarding es la dificultad más peligrosa.** Un arranque mal comunicado expulsa antes de que el juego "empiece de verdad". Es donde más se pierde gente. [The Gamer's Brain]
- **Construí el modelo mental correcto.** El jugador se arma una teoría de cómo funciona el juego; romperla sin aviso produce errores que se sienten *injustos*, no desafiantes. [The Design of Everyday Things; Half-Real]
- **La meta siempre visible.** El jugador debe saber qué persigue ahora (objetivo corto) y hacia dónde va (objetivo largo). Sin meta clara no hay dirección para su esfuerzo. [Elements of Game Design; The Art of Game Design]

---

## C. Que se sienta bien de controlar — game feel y juice

La sensación táctil de manejar el juego. Se decide en el core, con placeholders, antes que el arte.

- **Game feel = control en tiempo real** de un avatar dentro de un espacio simulado, pulido con metáfora. Es una sensación diseñable, no un accidente. [Game Feel]
- **Tres capas para tunear.** Input (respuesta inmediata), respuesta simulada (aceleración, fricción, inercia) y contexto/pulido. Ajustá aceleración, frenado, *coyote time* e *input buffering* para que el control perdone y responda. [Game Feel]
- **El movimiento del avatar transmite carácter.** Cómo se mueve el personaje comunica peso, personalidad y emoción antes que cualquier diálogo. [How Games Move Us]
- **Regla de bolsillo del prototipo gris.** Si el core se siente bien con cubos grises, tenés un juego; si no se siente bien, ningún arte lo va a salvar. Validá el feel primero. [Game Feel; Designing Games]

---

## D. Que tome decisiones interesantes — agencia e incertidumbre

El corazón del juego como sistema de elecciones. Sin decisiones con peso, es una actividad, no un juego.

- **Sin incertidumbre no hay juego.** Catalogá tus fuentes de incertidumbre —azar, resultado, información oculta, complejidad, oponente, desempeño propio— y usalas deliberadamente para sostener la tensión. [Uncertainty in Games]
- **Decisión significativa = discernible + integrada.** El jugador debe percibir el efecto de su elección y que esa elección importe a largo plazo. [Rules of Play]
- **Toda decisión necesita alternativas viables.** Una "elección" con una opción obviamente mejor no es una decisión: es una trampa de tutorial. Buscá trade-offs reales. [Designing Games; Characteristics of Games]
- **Elegancia: máxima experiencia por mecánica.** Pocas reglas que generen muchas situaciones (emergencia) valen más que muchas reglas scripteadas. Recortá lo que no multiplica. [Designing Games]
- **Ubicá tu juego en el eje azar↔skill.** El azar da variedad y accesibilidad; el skill da dominio y techo alto. Demasiado de uno cambia (o rompe) tu público. [Characteristics of Games; Man, Play and Games]
- **Los jugadores optimizan (playing to win).** Anticipá la estrategia dominante y el metajuego: si existe una vía claramente mejor, la van a encontrar y el juego colapsa a esa vía. [Characteristics of Games]

---

## E. Retenerlo y motivarlo — enganche, progresión, fracaso

Por qué el jugador vuelve. Combina que *pueda* seguir y que *quiera* seguir.

- **Usabilidad primero, engagement después.** Primero que el jugador *pueda* hacer lo que quiere; recién ahí importa que *quiera* seguir. La fricción de usabilidad se come toda la motivación. [The Gamer's Brain; Game Usability]
- **El fracaso bien diseñado retiene.** La paradoja del fracaso: perder duele, pero nos hace sentir responsables y nos empuja a reintentar. Fracaso *justo* + reintento *rápido* = enganche; fracaso arbitrario o con castigo largo = abandono. [The Art of Failure]
- **La meseta de dominio es el momento de churn.** Mientras haya patrones nuevos que dominar, el jugador sigue; cuando se acaban, se va. Programá nuevos picos de aprendizaje antes de la meseta. [A Theory of Fun]
- **Motivación intrínseca: competencia, autonomía, relación.** Diseñá para que el jugador sienta que mejora, que elige y que se conecta con otros. Son motores más duraderos que las recompensas externas. [The Gamer's Brain; How Games Move Us]
- **Bucles de interés anidados.** Loops cortos (segundos) dentro de medios (minutos) dentro de largos (sesiones): siempre algo para hacer ahora y algo por lo que volver mañana. [Advanced Game Design; Designing Games]
- **Mantené el resultado en duda.** Cuanto más tiempo permanezca incierto quién gana o si se logra el objetivo, más tensión y retención. Evitá partidas decididas de antemano. [Uncertainty in Games]
- **Lo social retiene.** Cooperación, presencia de otros y emoción compartida son de los ganchos más fuertes que existen. [How Games Move Us]

---

## F. Diseñar sus sistemas y economía — mecánicas, loops, balance

Cómo pensar la maquinaria interna para que produzca la experiencia buscada de forma predecible.

- **Mecánicas como sistemas dinámicos.** Pensá en recursos, flujos y bucles de feedback, no en features sueltos. Un juego es una economía en movimiento. [Game Mechanics]
- **Elegí tus feedback loops a conciencia.** Los *positivos* aceleran y aumentan la varianza (snowball, "el que gana gana más"); los *negativos* estabilizan y permiten comeback. Cada uno produce una experiencia distinta: elegí según lo que querés que se sienta. [Game Mechanics; Advanced Game Design]
- **Simulá la economía antes de programarla.** Diagramá flujos de recursos (estilo *Machinations*) para prever el comportamiento emergente y detectar exploits o estancamientos en el papel. [Game Mechanics]
- **Systems thinking: diseñá relaciones, no solo piezas.** El comportamiento emergente sale de cómo interactúan las partes. Un buen sistema se comporta bien por sus conexiones, no por sus componentes aislados. [Advanced Game Design]
- **Emergencia antes que scripting.** Reglas simples que se combinan dan profundidad y rejugabilidad baratas; el contenido scripteado no escala. [Designing Games; Advanced Game Design; Rules of Play]
- **Palancas de balance.** Duración de la partida, proporción azar/skill, cantidad de jugadores y mecanismos de catch-up son perillas concretas para ajustar la experiencia sin rehacer el juego. [Characteristics of Games]

---

## G. Hacerlo sentir algo — emoción, significado, ética

Qué dice el juego y qué provoca, más allá de la mecánica funcional.

- **Emoción por diseño, no solo por historia.** La emoción sale de decisiones concretas: cómo se mueve el avatar, qué elecciones ofrecés, si hay cooperación. La mecánica emociona antes que el guion. [How Games Move Us]
- **Retórica procedural: el sistema argumenta.** Un juego "dice" algo por *cómo funciona*, no solo por lo que muestra. Si querés expresar un tema, diseñá las reglas para que lo encarnen. [Persuasive Games]
- **El jugador como agente ético.** Los dilemas morales tratan al jugador como sujeto reflexivo. La ética es una dimensión de diseño (qué elecciones ofrecés y qué significan), no una censura. [The Ethics of Computer Games]
- **El juego se conecta con el mundo.** Más allá de reglas (sistema) y play (experiencia) está la cultura: qué evoca y con qué dialoga tu juego afuera. [Rules of Play]
- **Dale espacio para jugar "de más".** Los jugadores se apropian, improvisan y expresan; la *playfulness* excede tus reglas. Diseñar para la apropiación suma vida al juego. [Play Matters; The Ambiguity of Play]

---

## H. Fundamentos conceptuales — qué es un juego, reglas vs ficción

El marco para no confundir capas y para saber qué estás construyendo.

- **Definición operativa (Suits).** Jugar un juego es el intento voluntario de superar *obstáculos innecesarios*. La regla que limita es, justamente, la que crea el juego: no las quites "para hacerlo más fácil" sin entender qué sostienen. [The Grasshopper]
- **Reglas reales + mundo ficcional.** Separá la capa de sistema (reglas con las que se interactúa) de la capa de ficción (mundo que se evoca). No confundas contenido narrativo con mecánica al definir alcance. [Half-Real]
- **Círculo mágico.** El juego crea un espacio y tiempo con reglas propias, separado del mundo real; entrar y salir de ese espacio importa para la experiencia. [Homo Ludens; Rules of Play]
- **Cuatro sabores de juego (Caillois).** Agôn (competencia), alea (azar), mimicry (simulacro/rol), ilinx (vértigo), sobre un eje paidia (libre) ↔ ludus (reglado). Identificá qué placer(es) estás ofreciendo. [Man, Play and Games]
- **"Juego" y "diversión" son ambiguos.** No hay una sola definición correcta; cuidado con encasillar tu diseño en una única retórica (progreso, poder, identidad, azar…). [The Ambiguity of Play]
- **Interactividad como estructura (ergódica).** El jugador configura su recorrido con un esfuerzo no trivial. Diseñá la *agencia* y el recorrido, no solo la historia. [Cybertext]

---

## I. Llevarlo a producción — proceso, fases, prototipado

Cómo pasar de la idea a algo jugable sin naufragar en el camino.

- **Proceso playcentric.** Prototipá y playtesteá desde temprano: el diseño se descubre jugando, no en el documento. El papel miente sobre cómo se siente. [Game Design Workshop]
- **Cuatro fases con hitos (Lemarchand).** Ideación → preproducción (hasta el *vertical slice*) → producción full → postproducción. No pases de fase sin cumplir su hito; la preproducción termina cuando el core está probado. [A Playful Production Process]
- **Vertical slice: probá el core pulido antes de escalar.** Una porción representativa y pulida que demuestra que el juego funciona, antes de invertir en volumen de contenido. [A Playful Production Process]
- **Iterá el core primero.** Si el loop central no engancha con placeholders, no escales contenido ni arte: arreglá el core. [Game Design Workshop; Designing Games]
- **Playtesting: observá, no preguntes.** El jugador muestra la fricción real con lo que hace, no con lo que dice. Mirá dónde se traba, no le pidas su opinión de diseño. [Game Design Workshop; The Gamer's Brain]

---

## J. Restricciones como material — plataforma y límites

Los límites no son solo obstáculos: son generadores de diseño.

- **La plataforma moldea el diseño.** Los límites técnicos (motor, target, hardware) condicionan y a la vez fecundan lo que se puede hacer. Diseñá *con* la restricción, no contra ella. [Racing the Beam]
- **La restricción como motor creativo.** Los obstáculos "innecesarios" del juego y los límites de la plataforma fuerzan soluciones más elegantes que la libertad total. [The Grasshopper; Racing the Beam]

---

## Cómo usar este playbook

- Es una **checklist de perspectivas** al estilo de las "lentes" de Schell: ante una decisión de diseño, pasá por las categorías relevantes y preguntá qué dice cada principio. [The Art of Game Design]
- Al arrancar un juego, priorizá **C (feel) + D (decisiones) + A (comunicación)**: son el core jugable. B, E y F entran al escalar; G y H orientan el sentido; I y J gobiernan el cómo.
- Cada principio es un **baseline**, no una ley: los propios autores discrepan entre sí (ver Límites). Usalo para razonar, no para copiar.

## Límites (cuándo NO aplicar en piloto automático)

- Estos principios son **destilación de marco**, no la destilación capítulo por capítulo de cada libro (eso son misiones futuras específicas). Tomalos como puntos de partida citados, no como la última palabra.
- Hay **tensiones reales entre fuentes**: emergencia/elegancia (Sylvester) vs. contenido autoral; definiciones cerradas de juego (Suits, Juul) vs. la ambigüedad deliberada (Sutton-Smith, Sicart). Cuando dos principios choquen, decide según la experiencia buscada, no por autoridad.
- Varias fuentes son **teóricas/culturales** (Huizinga, Caillois, Aarseth, Bogost): iluminan el "por qué" y el "qué significa", no siempre dan una receta de implementación directa.

## Fuentes

Destilado (conceptos + cita, sin verbatim) de las 29 fuentes del estante [[00_Indice_fuentes]]:
[[01_Rules_of_Play]] · [[02_Art_of_Game_Design]] · [[03_Game_Design_Workshop]] · [[04_Theory_of_Fun]] · [[05_Game_Feel]] · [[06_Half_Real]] · [[07_Characteristics_of_Games]] · [[08_Designing_Games]] · [[09_Gamers_Brain]] · [[10_Game_Usability]] · [[11_How_Games_Move_Us]] · [[12_Design_of_Everyday_Things]] · [[13_Elements_of_Game_Design]] · [[14_Fundamentals_of_Game_Design]] · [[15_Game_Mechanics]] · [[16_Advanced_Game_Design]] · [[17_Uncertainty_in_Games]] · [[18_Art_of_Failure]] · [[19_Playful_Production_Process]] · [[20_Game_Design_Reader]] · [[21_The_Grasshopper]] · [[22_Homo_Ludens]] · [[23_Man_Play_and_Games]] · [[24_Ambiguity_of_Play]] · [[25_Play_Matters]] · [[26_Cybertext]] · [[27_Persuasive_Games]] · [[28_Ethics_of_Computer_Games]] · [[29_Racing_the_Beam]].

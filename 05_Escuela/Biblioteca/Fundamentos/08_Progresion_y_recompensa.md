---
tipo: fundamento
estado: En estudio
mision: [[EST-006_Mision_Lote_Biblioteca_Agosto26]]
profundiza: Pilar 7 — Recompensa y motivación
cruza: 05_Fundamentos_de_experiencia_ludica, 04_Playbook_de_diseno, 07_Economia_y_balance, 06_Dificultad_y_curva
---

# Fundamento 08 — Progresión y recompensa

> Este libro profundiza el **Pilar 7** de [[05_Fundamentos_de_experiencia_ludica]]. El baseline (que la recompensa siga al esfuerzo, que se lea claro, que no llegue tarde) ya está ahí. Acá va lo que el pilar deja afuera: **las tres progresiones que se confunden entre sí**, vertical vs horizontal, meta-progresión en roguelites, refuerzo variable y su costo ético, la curva de desbloqueos, y cómo conviven motivación intrínseca y extrínseca.
> Lo que NO cubre: la matemática de los recursos que financian la recompensa (vive en `07_Economia_y_balance`), la sensación del feedback al recibirla (vive en [[02_Game_feel]]), la exigencia que la precede (vive en `06_Dificultad_y_curva`).
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta
2. El modelo — tres progresiones
3. Baseline numérico
4. Patrones que funcionan
5. Antipatrones
6. Cómo se mide en playtest
7. CHECKLIST
8. Aplicación
9. Límites
10. Fuentes

## Qué es y por qué se rompe si falta
Progresión es la respuesta a "¿por qué sigo jugando la hora que viene?". Cuando falta, el juego puede ser excelente minuto a minuto y aun así se abandona a la hora y media: no hay razón para volver mañana. Cuando está mal armada, produce el efecto opuesto y peor: el jugador sigue por obligación, no por deseo — sabe que no la está pasando bien y sigue igual.

## El modelo — tres progresiones

| Progresión | Qué crece | Quién la controla | Se siente como | Cómo se rompe |
|---|---|---|---|---|
| **Del personaje** | Números: daño, vida, velocidad, stats | El diseñador (la regala) | Poder | Inflación: números más grandes, mismo juego |
| **Del jugador** | Habilidad real, comprensión, vocabulario | El jugador (se la gana) | Competencia | Nunca se examina: nadie se entera de que mejoró |
| **Del contenido** | Lo que se abre: zonas, enemigos, mecánicas, historia | El diseñador (la dosifica) | Descubrimiento | Se agota: "ya vi todo" |

```txt
    ALTO
      ^   Personaje ─────────────────────────────  (regalada, ilimitada, barata)
      |         ╱
 VALOR|        ╱      Contenido ────────┐          (dosificada, finita, cara)
 PARA |       ╱      ╱                  └────────  ← "ya vi todo"
  EL  |      ╱      ╱
 JUG. |     ╱   ╱ Jugador ─────────────────────    (ganada, la única que
      |    ╱ ╱                                       no se agota nunca)
    BAJO  ╱╱
      +-------------------------------------------> TIEMPO

  El error clásico: apoyar TODA la retención en la línea de PERSONAJE
  porque es la más barata de producir. Es también la que menos vale
  cuando el jugador se da cuenta de que el número subió y él no.
```

**Qué pasa cuando se confunden.** El caso típico: el diseñador quiere que el jugador *sienta* que mejoró, y le sube los números al personaje. El jugador siente el poder durante ~15 minutos y después nota que los enemigos también subieron: descubre que la progresión era decorativa. El antídoto es alinear las tres: **el número nuevo debe habilitar una decisión nueva (contenido) que exija una habilidad nueva (jugador)**. Si un nivel sólo cambia el dígito, no es progresión, es contabilidad.

**Vertical vs horizontal.**

| | Vertical (poder) | Horizontal (opciones) |
|---|---|---|
| Qué da | Más de lo mismo, más fuerte | Formas nuevas de resolver |
| Curva de aprendizaje | Plana | Sube: cada opción hay que aprenderla |
| Costo de balance | Bajo por ítem, alto en conjunto (inflación) | Alto por ítem (cada uno debe tener nicho) |
| Efecto en el jugador | Poder | Expresión, identidad de build |
| Riesgo | Trivializa el contenido viejo | Parálisis por opciones; opciones muertas |

Baseline sugerido: **vertical temprano, horizontal tardío.** El poder puro es legible para el novato; las opciones requieren vocabulario. Un juego que abre 12 builds en la primera hora está pidiendo una decisión sin información.

**Meta-progresión (roguelites).** Es progresión permanente que sobrevive a la muerte. Tiene dos caras:

| Salva el juego cuando… | Lo convierte en peaje cuando… |
|---|---|
| Convierte la derrota en avance parcial | El desbloqueo es el único camino a la viabilidad |
| Abre opciones nuevas (horizontal) | Sólo sube stats (vertical): el juego se gana esperando |
| El run 1 ya es un juego completo y justo | El run 1 está diseñado para perderse |
| El techo de habilidad importa más que el de meta | Un jugador experto no puede ganar sin farmear |

**Test de peaje:** ¿un jugador muy hábil puede ganar en el run 1, sin nada desbloqueado? Si la respuesta es no, la meta-progresión no es una recompensa: es una barrera de tiempo disfrazada.

**Recompensas: previsibles vs variables.**

| | Previsible (ratio fijo) | Variable (ratio aleatorio) |
|---|---|---|
| Efecto | Permite planificar; sostiene objetivos largos | Genera enganche fuerte y persistencia al fracaso |
| Riesgo | Se vuelve trámite si el intervalo es largo | Explota mecanismos compulsivos; erosiona la confianza |
| Dónde va | Progresión estructural: niveles, hitos, desbloqueos de contenido | Textura: drops menores, variación cosmética |

**El problema ético del refuerzo variable.** El refuerzo aleatorio produce mayor persistencia que el fijo — eso es un hecho conocido de la psicología del comportamiento, y es exactamente por eso que hay que usarlo con criterio. La línea práctica que este libro propone: **el refuerzo variable puede decidir el sabor de lo que recibís, nunca si progresás.** Si la variabilidad controla el avance mismo, el jugador que tuvo mala suerte queda castigado por algo que no hizo, y el diseño pasa de "generar interés" a "explotar una vulnerabilidad". Corolarios operativos: piso garantizado (nunca cero), techo de mala racha (pity), y transparencia sobre el hecho de que hay aleatoriedad.

**La curva de desbloqueos y el "ya vi todo".** Hay un momento exacto en que el jugador deja de esperar sorpresas: cuando ve el último tipo de cosa nueva. No el último ítem — el último *tipo*. A partir de ahí la retención sólo puede apoyarse en la progresión del jugador (dominio) o en la variación combinatoria. Baseline: **la última mecánica o tipo nuevo debe aparecer alrededor del 70–80 % del tiempo esperado de juego**, y el tramo final debe estar diseñado explícitamente como examen combinatorio de todo lo anterior, no como más contenido.

**El logro como cierre narrativo del esfuerzo.** Una recompensa hace tres trabajos, y sólo el tercero es el importante: (1) da un beneficio mecánico, (2) marca un hito, (3) **le cuenta al jugador la historia de lo que logró.** Sin el tercero, un ítem es inventario. Con el tercero, es memoria. Mecanismo concreto: la recompensa debe ser nombrable y atribuible — el jugador tiene que poder decir "esto lo conseguí cuando le gané a X", y eso exige que llegue en el momento del esfuerzo, no tres pantallas después, en un lote de cinco cosas.

**Intrínseca sobre extrínseca.** Las tres necesidades que sostienen el juego a largo plazo son **competencia** (soy bueno en esto y lo estoy siendo más), **autonomía** (elijo yo) y **relación** (le importa a alguien más). La motivación extrínseca (puntos, insignias, monedas) es más barata de producir y funciona rápido, pero si reemplaza a la intrínseca la degrada: cuando el premio explica la actividad, la actividad deja de explicarse sola.

El mecanismo que las hace convivir: **la recompensa extrínseca debe ser un informe de la competencia, no su motivo.** Un desbloqueo que llega porque el jugador se volvió capaz de algo refuerza la competencia. Un desbloqueo que llega por tiempo acumulado la reemplaza. Prueba rápida: si sacás la recompensa y la acción sigue teniendo sentido, la recompensa está bien puesta.

## Baseline numérico

| Parámetro / criterio | Baseline sugerido | Por qué |
|---|---|---|
| Tiempo entre recompensas significativas (early game) | 3–8 min | Debajo de 3 se devalúa; encima de 8 el novato se descuelga |
| Tiempo entre recompensas significativas (late game) | 15–30 min | El jugador ya tiene objetivos propios y tolera intervalos |
| Latencia entre logro y recompensa | < 2 s para el feedback, < 30 s para el otorgamiento | Más y se rompe la atribución causal |
| Aparición del último *tipo* nuevo de contenido | 70–80 % del tiempo esperado de juego | Deja tramo final para el examen combinatorio |
| Mecánicas/opciones nuevas por hora (después de la hora 2) | 1–3 | Sostiene descubrimiento sin saturar |
| Ratio vertical / horizontal en la primera hora | 80 / 20 | El novato lee poder, no lee opciones |
| Ratio vertical / horizontal después de la hora 5 | 30 / 70 | El experto ya quiere expresarse |
| Meta-progresión: ventaja total acumulable | ≤ 30 % de potencia sobre el run base | Encima de 30 % el juego se gana farmeando |
| Meta-progresión: % que abre opciones vs sube stats | ≥ 60 % opciones | Evita el peaje |
| Piso garantizado en recompensa aleatoria | Nunca 0; mínimo 40 % de la media | Elimina la sesión perdida por mala suerte |
| Techo de mala racha (pity) | Garantía a los 8–12 intentos fallidos | Corta la frustración sin matar la sorpresa |
| Densidad de desbloqueos anunciados visibles a la vez | 2–4 objetivos activos | Uno es frágil; más de 4 es ruido |
| Duración del "poder nuevo se siente nuevo" | 10–20 min antes de que el contenido lo iguale | Menos y la progresión se lee como falsa |

## Patrones que funcionan

| Patrón | Cuándo usarlo | Costo |
|---|---|---|
| **Recompensa que cambia el verbo** | La mejora habilita una acción nueva, no un número mayor | Cara: cada verbo nuevo es diseño, arte y balance |
| **Zanahoria visible** | Mostrar el desbloqueo antes de poder tenerlo | Frustra si el camino no está claro |
| **Piso + techo (garantía y pity)** | Cualquier recompensa aleatoria | Requiere estado persistente por jugador |
| **Examen retroactivo** | Un encuentro que sólo se supera con la habilidad ganada, no con el ítem | Barato y altísimo valor: hace visible la progresión del jugador |
| **Trofeo atribuible** | La recompensa lleva el nombre del desafío que la produjo | Trabajo de naming y presentación |
| **Run 1 completo** | Roguelite: el primer run es un juego justo y ganable | Obliga a balancear el juego sin meta, que es lo más difícil |
| **Desbloqueo por hazaña, no por tiempo** | Condición de habilidad en vez de contador | Requiere detectar la hazaña; muy superior en competencia percibida |
| **Cierre de capítulo** | Cada 45–90 min, un hito que permite dejar de jugar sin culpa | Reduce sesiones largas; mejora el retorno al día siguiente |

## Antipatrones

| Antipatrón | Síntoma observable en playtest |
|---|---|
| **Progresión decorativa** | El tester sube de nivel y dice "no sentí nada" |
| **Escalado paralelo** | El tester nota que los enemigos suben con él: deja de valorar el equipo |
| **Meta-peaje** | El tester dice "todavía no tengo desbloqueado lo que hace falta" en vez de "todavía no me sale" |
| **Recompensa en lote** | 5 cosas al final del nivel: el tester no puede decir qué ganó por qué |
| **Loot sin decisión** | El tester equipa siempre lo del número más alto, sin mirar |
| **Extrínseco que reemplaza** | El tester deja de jugar apenas se acaban los desbloqueos, aunque el juego siga siendo bueno |
| **Aleatoriedad que decide el avance** | El tester pierde una sesión completa por mala suerte y no por error |
| **Todo abierto de entrada** | El tester elige al azar entre 12 builds en el minuto 5 |
| **Sin examen** | El tester mejoró mucho y no lo sabe: nadie se lo demostró |
| **Cola de contenido agotada temprano** | Al 40 % del juego el tester dice "esto ya lo vi" |

## Cómo se mide en playtest

**Qué observar:** la reacción física al recibir la recompensa (0,5 s de sorpresa o nada), si abre el inventario a mirar lo nuevo o sigue de largo, si cambia su forma de jugar después de un desbloqueo (si no cambia, era vertical puro), en qué minuto deja de leer las descripciones de los ítems, y el momento exacto en que dice "esto ya lo vi".

**Qué preguntar:** "¿Qué es lo próximo que querés conseguir?" (mide zanahoria activa; si no sabe, no hay progresión legible), "¿Qué fue lo mejor que ganaste y cómo lo ganaste?" (mide atribución), "¿En qué mejoraste vos desde que empezaste?" (mide progresión del jugador — si contesta con un ítem en vez de una habilidad, la progresión del jugador es invisible), "¿Volverías mañana? ¿A hacer qué?".

**Qué NO preguntar:** "¿Te gustaron las recompensas?" (respuesta cortés). "¿Querés más loot?" (siempre sí, y no significa nada). "¿Está bien el ritmo de progresión?" (no tiene con qué comparar).

**Telemetría mínima:** tiempo hasta cada desbloqueo, % de jugadores que alcanza cada hito (la caída entre hitos consecutivos marca el punto de fuga), distribución de uso de las opciones desbloqueadas (una opción bajo el 5 % está muerta), sesiones por jugador y en qué hito ocurrió la última, y ratio de recompensas recogidas vs ignoradas.

## CHECKLIST

```txt
[ ] Las tres progresiones (personaje / jugador / contenido) están identificadas por separado en el GDS
[ ] Cada subida de números habilita al menos una decisión o acción nueva
[ ] Existe al menos un examen retroactivo que le muestra al jugador su propia mejora
[ ] Los enemigos NO escalan en paralelo al poder del jugador (o está justificado por escrito)
[ ] La primera hora es mayoritariamente vertical; lo horizontal llega con vocabulario
[ ] El último TIPO nuevo de contenido aparece al 70-80 % del tiempo esperado
[ ] El tramo final está diseñado como examen combinatorio, no como más contenido
[ ] Toda recompensa aleatoria tiene piso garantizado y techo de mala racha
[ ] Ninguna aleatoriedad decide SI progresás, sólo QUÉ recibís
[ ] Cada recompensa llega dentro de los 30 s del esfuerzo que la produjo, y es atribuible
[ ] Roguelite: el run 1 sin desbloqueos es ganable por un jugador hábil
[ ] Meta-progresión: >= 60 % abre opciones, no sube stats
[ ] Hay 2-4 objetivos visibles activos en todo momento
[ ] Prueba de intrínseca: si saco la recompensa, la acción sigue teniendo sentido
```

## Aplicación
**Game Design abre este libro cuando:** define el árbol de progresión de un GDS, diseña loot o desbloqueos, arma la meta de un roguelite, decide el ritmo de contenido nuevo, o cuando el playtest muestra abandono sin frustración (el peor síntoma: se fue sin quejarse).

**Qué trae la IA por default:** la separación explícita de las tres progresiones para el sistema propuesto, la verificación de que cada nivel habilite una decisión y no sólo un número, el test de peaje en cualquier meta-progresión, y la marca automática de toda aleatoriedad que decida avance en vez de sabor.

## Límites
No aplica igual en: arcade puro y juegos de sesión única (la progresión es la del jugador y nada más — ver [[01_Pong]]), puzzles cerrados donde el contenido es la progresión completa, y experiencias narrativas lineales cortas. En juegos-servicio la progresión se vuelve calendario y el tema desborda Fundamentos.

**Tensiones:** con `06_Dificultad_y_curva` — cada recompensa vertical baja la curva; hay que reponerla. Con `07_Economia_y_balance` — la progresión es la principal fuente de inflación del juego. Con el Pilar 9 (agencia) — un árbol de progresión con una sola rama óptima anula la decisión. Con el Pilar 1 (core loop) — si la recompensa es lo único que sostiene el loop, el loop no es bueno todavía: **arreglá el loop antes de agregar loot.**

## Fuentes
[[04_Theory_of_Fun]] · [[08_Designing_Games]] · [[02_Art_of_Game_Design]] · [[09_Gamers_Brain]] · [[11_How_Games_Move_Us]] · [[15_Game_Mechanics]] · [[18_Art_of_Failure]] · [[28_Ethics_of_Computer_Games]] · [[14_Fundamentals_of_Game_Design]] · [[25_Play_Matters]]
Cruces: [[05_Fundamentos_de_experiencia_ludica]] (Pilar 7) · [[04_Playbook_de_diseno]] · [[01_Loop_de_experiencia]] · `06_Dificultad_y_curva` · `07_Economia_y_balance`

---

---
tipo: fundamento
estado: En estudio
mision: [[EST-006_Mision_Lote_Biblioteca_Agosto26]]
profundiza: Pilar 6 — Dificultad, tensión y flow
cruza: 05_Fundamentos_de_experiencia_ludica, 04_Playbook_de_diseno, 01_Loop_de_experiencia, 09_Onboarding_y_tutorial
---

# Fundamento 06 — Dificultad y curva

> Este libro profundiza el **Pilar 6** del libro [[05_Fundamentos_de_experiencia_ludica]]. El baseline (qué es flow, por qué la dificultad plana aburre, checklist mínimo por GDS) ya está ahí y no se repite. Acá va lo que el pilar deja explícitamente afuera: **descomponer la dificultad en cuatro ejes que se ajustan distinto**, la forma de la curva escalonada, el ajuste dinámico y sus costos políticos, asistencias vs modos, y la economía de la muerte.
> Lo que NO cubre: la sensación del control momento a momento (vive en [[02_Game_feel]]), la enseñanza de mecánicas (vive en `09_Onboarding_y_tutorial`), y el reparto de desafíos en el espacio (Level Design).
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta
2. El modelo — cuatro dificultades, no una
3. Baseline numérico
4. Patrones que funcionan
5. Antipatrones
6. Cómo se mide en playtest
7. CHECKLIST
8. Aplicación
9. Límites
10. Fuentes

## Qué es y por qué se rompe si falta
La dificultad no es un dial. Es el conjunto de exigencias que el juego le pone al jugador para producir el estado de tensión que hace que importe. Cuando falta el diseño de curva pasan tres cosas observables: el jugador abandona en el primer muro (curva sin escalones), el jugador se aburre a los 20 minutos (curva plana), o el jugador llega al final sin haber aprendido nada (curva descendente por inflación de poder — ver `07_Economia_y_balance`).

El error de base es tratar "difícil" como una sola magnitud. Un jefe que exige timing de 6 frames y un puzzle que exige entender una regla oculta son ambos "difíciles" y no se arreglan con la misma perilla. Bajarle vida al jefe funciona; bajarle vida al puzzle no hace nada.

## El modelo — cuatro dificultades, no una

| Eje | Qué exige | Cómo se sube | Cómo se baja sin romper | Falla típica del jugador |
|---|---|---|---|---|
| **Ejecución** | Precisión motriz, timing, APM | Ventanas más cortas, más entidades simultáneas, menos margen | Alargar ventanas, slow-mo, ampliar hitbox propia | "No me sale, pero sé qué hacer" |
| **Comprensión** | Leer la situación, entender la regla | Ocultar información, mecánicas combinadas, telegrafiado sutil | Telegrafiar más, exponer estado, dar un ejemplo previo | "No entiendo qué me mató" |
| **Planificación** | Decidir con horizonte largo, gestionar recursos | Escasez, decisiones irreversibles, más variables acopladas | Aflojar escasez, permitir deshacer, reducir variables | "Llegué acá sin recursos y no sé desde cuándo perdí" |
| **Paciencia** | Repetir, tolerar el reintento, grindear | Runs largas, checkpoints lejanos, RNG castigador | Acortar reintento, subir checkpoint, techo al RNG | "Sé hacerlo, me da fiaca hacerlo de nuevo" |

Regla operativa: **un encuentro debe cargar fuerte sobre un eje y como mucho medio sobre otro.** Un jefe que exige ejecución de 6 frames, comprensión de un patrón oculto y paciencia de 4 minutos de reintento por vida no es difícil: es tres juegos apilados y el jugador no sabe cuál está fallando.

**La curva escalonada (presentar → consolidar → combinar → examinar)**

```txt
DIFICULTAD
  ^
  |                                        ┌── EXAMEN C
  |                        ┌── EXAMEN B    │   (A+B+C bajo presión)
  |        ┌── EXAMEN A    │               │
  |        │           ┌───┴───┐       ┌───┴───┐
  |    ┌───┴───┐   ┌───┤ A+B   │   ┌───┤ A+B+C │
  |  ┌─┤   A   ├───┤ B │ combo │   │ C │ combo │
  |  │ │consol.│   │pres│      │   │pres│      │
  |──┴─┴───────┴───┴───┴──────┴───┴───┴───────┴──>  TIEMPO
     ^                ^                ^
   PRESENTAR      El valle post-examen        Cada examen baja
   (seguro,       es OBLIGATORIO:             el piso: lo que
    sin costo)    respiro + confirmación      antes era examen
                  de competencia              ahora es rutina
```

Cada mecánica nueva recorre cuatro etapas antes de contar como "sabida":

| Etapa | Qué pasa | Costo de fallar | Duración típica |
|---|---|---|---|
| **Presentar** | Aparece sola, en contexto seguro, imposible de ignorar | Cero o casi cero | 10–30 s |
| **Consolidar** | 2–4 usos con variación menor, riesgo bajo | Barato (retry inmediato) | 1–3 min |
| **Combinar** | Se cruza con una mecánica ya consolidada | Medio | 2–5 min |
| **Examinar** | Bajo presión de tiempo/recursos, con castigo real | Alto (muerte, pérdida) | 30 s – 3 min |

**Dificultad percibida vs real.** No son la misma variable y se pueden mover por separado. La percibida sube con: ruido visual, incertidumbre sobre el estado propio, muerte inesperada, falta de telegrafiado. La real sube con: márgenes numéricos. El jugador negocia con la percibida.

| Situación | Real | Percibida | Efecto |
|---|---|---|---|
| Última barra de vida ampliada de facto (el "último golpe perdona") | baja | igual/sube | El clásico más rentable: se sienten heroicos |
| Enemigo con mucha vida y patrón trivial | alta (tiempo) | baja (aburre) | Percepción de relleno |
| Muerte por algo fuera de cámara | igual | altísima | Se lee como injusticia (ver Pilar 5) |
| Telegrafiado claro de un ataque letal | igual | baja | Sube la sensación de justicia sin bajar el reto |

**Ajuste dinámico (DDA).** El sistema mide desempeño y mueve parámetros en caliente. Funciona sólo mientras es invisible. En el momento en que el jugador lo detecta, su victoria deja de ser suya y el logro se vacía: es el único sistema del juego que **se destruye al ser comprendido**. Por eso: DDA sobre variables que el jugador no puede auditar (tasa de drop de munición, agresividad de IA, spacing de spawns) y nunca sobre variables que el jugador cuenta (daño en números visibles, HP del jefe, precio en tienda).

**Rubber banding.** Es DDA competitivo: el que va perdiendo recibe ventaja. Costos concretos: (a) castiga la buena jugada temprana, (b) convierte la carrera en un sprint final donde los primeros 3/4 no importaron, (c) el jugador experto aprende a ir segundo a propósito. Alternativa más barata: **catch-up por oportunidad, no por regalo** — al que va atrás se le abren atajos o rutas de riesgo, no se le sube el motor.

**Modos vs asistencias.**

| | Modos (Fácil/Normal/Difícil) | Asistencias granulares |
|---|---|---|
| Qué mueve | Un preset opaco de 10 variables | Una variable, nombrada, por switch |
| Momento de elección | Antes de jugar, sin información | Cuando el jugador ya chocó con el problema |
| Señal social | "Elegiste fácil" (estigma) | "Activaste apuntado asistido" (herramienta) |
| Accesibilidad | Grosera: baja todo junto | Fina: baja sólo el eje que bloquea |
| Envejecimiento | Mal: obliga a rebalancear 3 juegos | Bien: cada switch es independiente y testeable |
| Costo de producción | Bajo al inicio, alto al mantener | Alto al inicio, bajo al mantener |

Las asistencias envejecen mejor porque son **ortogonales a los cuatro ejes**: un switch de "ventana de parry ×1.5" toca sólo ejecución y no tocás nada más. Un modo Fácil toca los cuatro a la vez y cada rebalanceo posterior te obliga a re-testear las tres versiones.

**El onboarding como el tramo más caro.** Los primeros 10 minutos concentran la mayor densidad de aprendizaje y la menor tolerancia al fracaso (el jugador todavía no invirtió nada). Es el tramo con peor relación esfuerzo de diseño / minutos de juego producidos. Detalle completo en `09_Onboarding_y_tutorial`.

**Cómo diseñar el primer muro a propósito.** El primer muro es el momento en que el juego declara qué clase de juego es. Debe cumplir cuatro condiciones: (1) llegar después de que las mecánicas base estén consolidadas, (2) exigir exactamente lo enseñado, nada nuevo, (3) tener reintento barato, (4) ser superable con mejor ejecución de lo conocido, no con un descubrimiento. Un muro que exige algo no enseñado es un bug de diseño, no dificultad.

**Muerte y castigo.** La tolerancia al reintento es función del tiempo perdido, no del hecho de morir:

```txt
TIEMPO PERDIDO POR MUERTE   →   QUÉ PIENSA EL JUGADOR
  < 3 s   .................. "otra vez"   (retry reflejo, casi sin fricción)
  3–10 s  .................. "dale"       (aceptable en acción)
 10–30 s  .................. "uf"         (necesita que la muerte se sienta justa)
 30–90 s  .................. "¿de nuevo?" (sólo si la run tiene variación)
  > 90 s  .................. "mañana"     (riesgo alto de sesión terminada)
```

## Baseline numérico

| Parámetro / criterio | Baseline sugerido | Por qué |
|---|---|---|
| Tiempo de reintento tras muerte (acción) | 1–3 s hasta control recuperado | Debajo de 3 s el reintento es reflejo, no decisión |
| Distancia entre checkpoints | 45–120 s de juego limpio | Encima de 2 min la repetición pesa más que el reto |
| Mecánicas nuevas por hora (primeras 2 h) | 3–5 | Más de 5 y ninguna llega a consolidarse |
| Repeticiones antes de considerar consolidada una mecánica | 3–5 usos con variación | Menos de 3 no se automatiza |
| Intentos esperados en un examen (jefe/muro) | 3–8 en dificultad de referencia | 1–2 = trivial; >10 = frustración o eje mal elegido |
| Tasa de éxito objetivo del jugador medio en un encuentro estándar | 65–80 % al primer intento | Deja 20–35 % de tensión real sin bloquear |
| Duración de un valle post-examen | 30–90 s de baja exigencia | Convierte la victoria en competencia percibida |
| Delta de dificultad entre escalones consecutivos | +10–20 % de exigencia | >25 % se lee como salto injusto |
| Ejes cargados simultáneamente por encuentro | 1 fuerte + máx. 0,5 secundario | Evita el diagnóstico imposible ("¿en qué fallé?") |
| Rango de ajuste de un DDA invisible | ±15 % sobre variables no auditables | Encima de 20 % el jugador lo detecta |
| Duración de la ventana de gracia post-daño (i-frames) | 0,5–1,2 s | Corta la muerte en cadena sin volverlo trivial |
| Presupuesto de asistencias al lanzamiento | 4–8 switches independientes | Cubren los cuatro ejes sin explotar el testeo |

## Patrones que funcionan

| Patrón | Cuándo usarlo | Costo |
|---|---|---|
| **Escalón con valle** | Siempre: después de cada examen, 30–90 s de exigencia baja | Alarga el juego un 10–15 % en tiempo total |
| **Muro anunciado** | Antes del primer boss real: mostrarlo, dejar huir, volver | Requiere backtracking legible y un espacio seguro |
| **Último golpe perdona** | Juegos de acción con vida visible | Rompe la aritmética exacta; incompatible con juegos de precisión numérica |
| **Fracaso con progreso** | Roguelites y runs largas: perder deja algo | Riesgo de convertirse en peaje (ver `08_Progresion_y_recompensa`) |
| **Asistencia contextual** | Ofrecer el switch recién tras 3–5 fallos en el mismo punto | Necesita telemetría de fallo por punto |
| **Dificultad por opt-in** | Desafíos opcionales laterales de mayor exigencia | Contenido que la mayoría no ve: costo/beneficio bajo |
| **Catch-up por oportunidad** | Competitivo: al de atrás se le abre una ruta riesgosa | Diseño de rutas alternativas reales, no cosmético |
| **Escalada por cantidad antes que por estadística** | Presión creciente sin inflar números | Sube carga de ejecución; ojo con el rendimiento |

## Antipatrones

| Antipatrón | Síntoma observable en playtest |
|---|---|
| **Muro sin escalón** | El tester muere >10 veces en un punto y no cambia de estrategia: repite lo mismo más fuerte |
| **Dificultad por opacidad** | El tester pregunta "¿qué me mató?" — la comprensión estaba cargada sin telegrafiado |
| **Esponja de vida** | El tester domina el patrón en 20 s y sigue peleando 3 min; deja de esquivar por aburrimiento |
| **DDA detectado** | El tester dice "creo que me está dejando ganar" — la victoria dejó de valer |
| **Cuatro ejes juntos** | El tester no puede nombrar por qué falló; culpa a los controles |
| **Rubber banding visible** | El tester deja de esforzarse en la primera mitad de la carrera |
| **Tutorial que no examina** | El tester "aprendió" la mecánica y 20 min después no la usa cuando hace falta |
| **Castigo desacoplado del error** | El tester pierde 3 min de progreso por un error de 0,2 s |
| **Escalón invisible por inflación** | El tester avanza sin fallar nunca porque el poder creció más rápido que el reto |

## Cómo se mide en playtest

**Qué observar** (sin hablar): intentos por punto de fallo, tiempo desde la muerte hasta el siguiente input, cambio de estrategia entre intentos (si no cambia, el problema es comprensión), lenguaje corporal en el intento 5 vs el 1, y en qué punto suelta el control.

**Qué preguntar** (después, nunca durante): "¿Qué te mató?" (mide comprensión), "¿Qué ibas a hacer distinto?" (mide diagnóstico), "¿Sentiste que fue justo?" (mide percibida vs real), "¿Cuándo te diste cuenta de que ibas a poder?".

**Qué NO preguntar:** "¿Fue muy difícil?" (respuesta social, el tester protege su ego y tu proyecto). "¿Te gustó el jefe?" (no separa ejes). "¿Le subirías la vida?" (le estás pidiendo que diseñe).

**Telemetría mínima:** muertes por punto (heatmap), intentos hasta superar cada examen, tiempo hasta primer input tras muerte, uso de cada asistencia activada, punto de abandono de sesión, y % de jugadores que superan cada escalón (la curva de retención por escalón es el diagnóstico más directo de dónde está el muro no deseado).

## CHECKLIST

```txt
[ ] Cada encuentro declara UN eje dominante (ejecución/comprensión/planificación/paciencia)
[ ] Ninguna mecánica se examina antes de haberse presentado y consolidado
[ ] Hay un valle de 30-90 s después de cada examen
[ ] El delta entre escalones consecutivos es <= 20 %
[ ] El primer muro sólo exige lo ya enseñado
[ ] Tiempo de reintento tras muerte <= 3 s (acción) o justificado por escrito
[ ] Distancia entre checkpoints <= 120 s de juego limpio
[ ] Todo ataque letal está telegrafiado con antelación legible
[ ] El DDA (si existe) opera sólo sobre variables no auditables, rango <= 15 %
[ ] Las asistencias son switches nombrados e independientes, no un preset
[ ] Existe telemetría de muertes por punto e intentos por examen
[ ] Se testeó con al menos 2 personas que nunca vieron el juego
[ ] Ningún castigo cuesta más de 90 s de progreso por un error puntual
```

## Aplicación
**Game Design abre este libro cuando:** define la curva de un GDS, diseña un jefe o examen, decide checkpoints y castigo de muerte, discute modos de dificultad o accesibilidad, o cuando el playtest muestra abandono concentrado en un punto.

**Qué trae la IA por default:** la descomposición en cuatro ejes aplicada al encuentro que se esté diseñando, la tabla de baseline numérico como punto de partida discutible, la propuesta de escalones presentar→consolidar→combinar→examinar para cada mecánica nueva del GDS, y la advertencia automática cuando un encuentro carga más de un eje fuerte.

## Límites
No aplica igual en: juegos de sandbox puro sin estados de fracaso (la curva la pone el jugador), competitivos PvP (la dificultad es el otro jugador; acá se diseña matchmaking, no curva), y juegos narrativos donde el desafío es opcional.

**Tensiones:** con el Pilar 9 (agencia) — cada asistencia y cada DDA le saca peso a la decisión del jugador. Con el Pilar 7 (recompensa) — bajar dificultad devalúa la recompensa que la corona. Con `07_Economia_y_balance` — la inflación de poder aplana la curva sin que nadie lo decida. Con `02_Game_feel` — un juego que se siente mal se percibe difícil aunque los números sean generosos: **arreglá el feel antes de tocar la dificultad.**

## Fuentes
[[02_Art_of_Game_Design]] · [[03_Game_Design_Workshop]] · [[04_Theory_of_Fun]] · [[08_Designing_Games]] · [[09_Gamers_Brain]] · [[17_Uncertainty_in_Games]] · [[18_Art_of_Failure]] · [[13_Elements_of_Game_Design]] · [[16_Advanced_Game_Design]]
Cruces: [[05_Fundamentos_de_experiencia_ludica]] (Pilar 6, baseline) · [[04_Playbook_de_diseno]] · [[02_Game_feel]] · [[01_Loop_de_experiencia]] · `07_Economia_y_balance` · `08_Progresion_y_recompensa` · `09_Onboarding_y_tutorial`

---

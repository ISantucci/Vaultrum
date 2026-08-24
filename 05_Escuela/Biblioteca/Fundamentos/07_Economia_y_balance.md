---
tipo: fundamento
estado: En estudio
mision: [[EST-006_Mision_Lote_Biblioteca_Agosto26]]
profundiza: Pilares 6 y 9 — Dificultad/tensión y Agencia/decisiones significativas
cruza: 05_Fundamentos_de_experiencia_ludica, 04_Playbook_de_diseno, 06_Dificultad_y_curva, 08_Progresion_y_recompensa
---

# Fundamento 07 — Economía y balance

> Este libro profundiza los **Pilares 6 y 9** de [[05_Fundamentos_de_experiencia_ludica]]. El baseline (que las decisiones tengan consecuencia, que la tensión venga de recursos escasos) ya está ahí. Acá va lo que el pilar deja afuera: **la máquina de recursos** (fuentes, sumideros, conversores, stocks), los loops de refuerzo, la inflación, el balance de opciones y **cómo se balancea sin datos de mercado**, que es la situación real del dev solo.
> Lo que NO cubre: la sensación de recibir la recompensa (vive en `08_Progresion_y_recompensa`), la curva de exigencia (vive en `06_Dificultad_y_curva`), monetización y economía real (fuera del alcance de Fundamentos).
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta
2. El modelo — la máquina de recursos
3. Baseline numérico
4. Patrones que funcionan
5. Antipatrones
6. Cómo se mide en playtest
7. CHECKLIST
8. Aplicación
9. Límites
10. Fuentes

## Qué es y por qué se rompe si falta
Toda economía de juego es una máquina que mueve cantidades entre lugares. Si no la modelás explícitamente, igual existe — sólo que emergente y sin control. Síntomas de economía no diseñada: el jugador acumula una moneda que no gasta, hay una build que gana siempre, la tienda deja de importar a las 3 h, o el juego se vuelve trivial a mitad de camino y nadie sabe cuándo pasó.

El balance no es "que todo sea igual de bueno". Es **que ninguna opción sea estrictamente mejor, y que todas las decisiones tengan costo de oportunidad real**. Ahí es donde toca el Pilar 9: una decisión sin costo no es una decisión.

## El modelo — la máquina de recursos

Cuatro piezas, y sólo cuatro:

| Pieza | Qué hace | Ejemplos | Parámetro clave |
|---|---|---|---|
| **Fuente** | Crea recurso de la nada | Drop de enemigo, ingreso por turno, regeneración | Tasa (unidades/min) |
| **Sumidero** | Destruye recurso | Compra, munición gastada, decaimiento, reparación | Tasa de drenaje |
| **Conversor** | Cambia recurso A por B | Crafteo, tienda, entrenamiento, refinería | Ratio y pérdida |
| **Stock** | Almacena | Inventario, banco, HP, cargador | Capacidad (tope o infinito) |

```txt
        ┌──────────┐   tasa      ┌───────────┐   ratio     ┌───────────┐
        │ FUENTE   │────────────>│  STOCK A  │────────────>│ CONVERSOR │
        │ (drop,   │             │ (moneda)  │             │  (tienda) │
        │ ingreso) │             │  tope?    │             └─────┬─────┘
        └──────────┘             └─────┬─────┘                   │
                                       │                         v
              LOOP (+) refuerzo        │                   ┌───────────┐
        ┌──── más poder ──> más drop ──┘                   │  STOCK B  │
        │                                                  │  (poder)  │
        │     LOOP (-) catch-up                            └─────┬─────┘
        └──── más poder ──> más costo <────────────────────────  │
                                                                 v
                                                           ┌───────────┐
                                                           │ SUMIDERO  │
                                                           │ (gasto,   │
                                                           │ decaim.)  │
                                                           └───────────┘

REGLA DE CIERRE: toda fuente necesita al menos un sumidero proporcional.
Fuente sin sumidero = inflación garantizada, sólo es cuestión de horas.
```

**Loops de refuerzo.**

| Tipo | Mecánica | Efecto en la partida | Cuándo lo querés |
|---|---|---|---|
| **Positivo (bola de nieve)** | Ganar → más recursos → ganar más | Acelera el desenlace, amplifica la ventaja temprana | Partidas cortas; sensación de poder creciente en single-player |
| **Negativo (catch-up)** | Perder → ayuda / Ganar → costo | Estira la partida, mantiene la tensión | Multijugador, partidas largas, cuando la victoria temprana mata el interés |

Todo juego necesita los dos, en proporción distinta. Sin positivo, el esfuerzo no rinde. Sin negativo, la partida se decide en el minuto 5 y se juegan 40 más por inercia. El ajuste fino: **positivo fuerte al principio, negativo creciente hacia el final** (costos escalados, precios crecientes, enemigos que escalan con tu nivel — con cuidado, ver antipatrones).

**Moneda dura vs blanda.**

| | Blanda | Dura |
|---|---|---|
| Cómo entra | Constante, del gameplay ordinario | Rara, de logros o hitos |
| Qué compra | Consumibles, mejoras incrementales | Desbloqueos permanentes, decisiones estructurales |
| Se puede farmear | Sí | No, o a un costo prohibitivo |
| Riesgo | Inflación y acumulación muerta | Parálisis por decisión ("lo guardo para después") |
| Sumidero necesario | Alto y continuo | Bajo pero definitivo |

La dura funciona porque **es el mecanismo que hace irreversible una decisión**: ahí vive la agencia del Pilar 9. Si todo se puede recomprar, ninguna elección pesa.

**Inflación: por qué todo sistema de recompensa se rompe hacia arriba.** El jugador mejora en dos frentes a la vez: acumula recursos y aprende a jugar. Los dos empujan en la misma dirección. Si la exigencia no acompaña, el juego se aplana. Y la presión de diseño siempre es hacia arriba: la recompensa siguiente tiene que sentirse mejor que la anterior, así que los números suben. Tres frenos concretos:

1. **Sumideros crecientes** — el costo de la mejora N+1 crece más rápido que el ingreso.
2. **Rendimientos decrecientes** — cada punto de stat da menos que el anterior (curva logarítmica, no lineal).
3. **Conversión en lugar de acumulación** — el recurso viejo se transforma en el nuevo con pérdida, en vez de sumarse.

**Balance de opciones.**

| Concepto | Definición | Cómo se detecta | Cómo se arregla |
|---|---|---|---|
| **Dominancia estricta** | La opción A es mejor que B en todo | Nadie elige B nunca | Darle a B una ventaja situacional exclusiva, no subirle los números |
| **Opción-trampa** | Parece buena, es mala | Los nuevos la eligen, los expertos no | O se arregla o se borra; una trampa castiga sólo al que no sabe |
| **Ciclo (piedra-papel-tijera)** | Cada opción gana a una y pierde a otra | Meta estable con rotación | Requiere información: el jugador debe poder anticipar el contexto |
| **Costo de oportunidad** | Elegir A cierra B | El jugador duda antes de elegir | Es el objetivo; si no hay duda, no hay decisión |

El indicador de salud: **si el jugador puede nombrar por qué eligió cada cosa y menciona lo que resignó, el balance está funcionando.**

**Cómo se balancea sin datos.** El dev solo no tiene 10.000 partidas de telemetría. Tiene esto:

| Herramienta | Qué produce | Cuándo alcanza | Costo |
|---|---|---|---|
| **Planilla de primera aproximación** | Todo valor en una sola hoja, con fórmulas, no hardcodeado | Siempre. Es el piso. | 2–4 h iniciales |
| **Normalizar a una unidad** | Todo se expresa en "segundos de gameplay" o en "daño por segundo" | Comparar opciones heterogéneas | 1–2 h |
| **First-order approximation** | Modelo lineal que ignora interacciones; sirve para descartar lo absurdo | Detectar el x10 antes de implementarlo | Bajo |
| **Simulación a mano** | Jugar la economía en papel, 20 turnos | Juegos por turnos o gestión | 1–3 h por pasada |
| **Sim automatizada (bot tonto)** | 1.000 corridas con estrategia fija | Cuando hay >3 monedas o RNG fuerte | 1–3 días de código |
| **Playtest dirigido** | Preguntas al jugador sobre lo que resignó | Balance de opciones (no de números) | Bajo, alto valor |

**Sensación vs número.** Se balancea **por número** todo lo que el jugador cuenta: precios, daño visible, tiempos de espera, cantidades de recurso. Se balancea **por sensación** todo lo que el jugador no puede auditar: peso del impacto, ritmo de drop percibido, cuánto "cuesta" moralmente una decisión. Regla: si el jugador puede llevar la cuenta en una hoja, respetá la aritmética. Si no puede, mandá la percepción.

**La regla del sistema mínimo.** Cada moneda nueva no suma trabajo: lo multiplica. Con N monedas hay N·(N−1)/2 relaciones de conversión potenciales, y cada una es un vector de exploit. Antes de agregar una moneda, la pregunta es: *¿qué decisión habilita esta moneda que ninguna existente puede expresar?* Si no hay respuesta en una frase, no va.

## Baseline numérico

| Parámetro / criterio | Baseline sugerido | Por qué |
|---|---|---|
| Monedas distintas en un juego pequeño | 1–2 (máx. 3) | Cada una multiplica superficie de balance y exploits |
| Ratio de sumidero vs fuente en estado estable | 0,85–1,0 del ingreso por hora | Debajo de 0,85 el stock se acumula muerto |
| Crecimiento del costo de mejora N+1 | ×1,15 – ×1,35 sobre la anterior | Contiene la inflación sin frenar el progreso |
| Rendimiento de stats por punto invertido | Decreciente: 100 %, 80 %, 65 %, 55 %… | Evita que una sola stat domine |
| Spread de poder entre la mejor y la peor opción viable | ≤ 15 % en potencia efectiva | Encima de 15 % la peor deja de elegirse |
| Ventaja máxima de un loop positivo por ciclo | +5–10 % | Encima de 10 % la partida se decide temprano |
| Fuerza del catch-up | Recupera ≤ 30 % de la brecha por ciclo | Más y el esfuerzo del líder se anula |
| Costo de la compra más cara del early game | 20–40 min de ingreso ordinario | Debajo de 20 min no genera deseo; encima de 40 se lee como grind |
| Tope de stock (inventario/moneda) | 1,5–3× el gasto más caro disponible | Fuerza el gasto, evita el atesoramiento infinito |
| Pérdida en conversión (crafteo/reciclado) | 25–50 % del valor | Es el sumidero más elegante: el jugador lo elige |
| Variación de RNG en recompensa por acción | ±30 % alrededor de la media | Da textura sin romper la planificación |
| Cantidad de valores hardcodeados en código | 0 | Todo parámetro económico vive en una tabla editable |

## Patrones que funcionan

| Patrón | Cuándo usarlo | Costo |
|---|---|---|
| **Sumidero elegido** | El jugador decide gastar (crafteo con pérdida, apuesta) en vez de que el juego le cobre | Requiere que el destino del gasto sea deseable |
| **Precio escalado** | Cada compra del mismo tipo cuesta más | Puede leerse como castigo si no está señalizado |
| **Moneda que caduca** | Recurso de temporada/run que no cruza sesiones | Presiona a gastar; genera FOMO si se abusa |
| **Una sola planilla maestra** | Siempre: todo número exportado desde un CSV/ScriptableObject | Disciplina de pipeline (Unity: 1–2 días de tooling) |
| **Opción situacional** | Arreglar dominancia dándole a la opción débil un nicho exclusivo | Exige que el nicho aparezca seguido |
| **Techo de acumulación** | Cap duro en stock para forzar circulación | Frustra al acumulador; avisar con claridad |
| **Presupuesto por build** | Puntos limitados que el jugador reparte | Es el generador de costo de oportunidad más barato que existe |
| **Normalización a segundos** | Expresar todo valor en tiempo de juego para comparar | Trabajo de planilla, no de código |

## Antipatrones

| Antipatrón | Síntoma observable en playtest |
|---|---|
| **Fuente sin sumidero** | El tester termina con 40.000 de moneda y nada que comprar |
| **Moneda decorativa** | El tester no sabe para qué sirve la segunda moneda |
| **Dominancia estricta** | Todos los testers eligen la misma build sin dudar |
| **Opción-trampa** | El tester nuevo elige X y pierde; el experimentado nunca la mira |
| **Bola de nieve sin freno** | La partida está decidida al 25 % y se juega el resto por trámite |
| **Rubber banding económico** | El tester nota que el juego lo "ayuda" y baja el esfuerzo |
| **Escalado de enemigos con el nivel** | El tester sube 10 niveles y se siente igual de fuerte: la progresión no existió |
| **Números en código** | Cada rebalanceo exige recompilar; termina no rebalanceándose nunca |
| **Parálisis por moneda dura** | El tester termina el juego sin gastar el recurso premium "por si acaso" |
| **Grind involuntario** | El tester repite el mismo encuentro 10 veces para juntar recurso, y no lo disfruta |

## Cómo se mide en playtest

**Qué observar:** stock de cada recurso al final de cada sesión (si sube monótonamente, falta sumidero), qué compra primero y qué nunca compra, cuánto tarda en decidir en la pantalla de mejoras (duda = costo de oportunidad funcionando; instantáneo = hay dominancia), y si repite un encuentro por recurso en vez de por gusto.

**Qué preguntar:** "¿Qué resignaste al elegir eso?" (mide costo de oportunidad), "¿Para qué estás guardando?" (detecta atesoramiento), "¿Qué te comprarías si tuvieras el doble?" (revela el sumidero deseado), "¿Hay algo que nunca usarías?" (detecta dominancia y trampas).

**Qué NO preguntar:** "¿Está balanceado?" (no es su trabajo y no tiene la data). "¿Subirías el precio de X?" (le pedís que balancee). "¿Te gustó la economía?" (nadie percibe la economía como objeto).

**Telemetría mínima:** stock de cada moneda muestreado cada 5 min, ingreso y gasto por hora discriminado por fuente/sumidero, tasa de elección de cada opción (la distribución plana es la meta; una opción bajo el 5 % de uso está muerta), tiempo hasta la primera compra, y cantidad de recurso al terminar el juego.

## CHECKLIST

```txt
[ ] Cada fuente del juego tiene identificado su sumidero correspondiente
[ ] Ninguna moneda existe sin una decisión que sólo ella pueda expresar
[ ] Todo parámetro económico vive en tabla/ScriptableObject, cero hardcode
[ ] Existe una planilla maestra con todos los valores normalizados a una unidad
[ ] El costo de mejora N+1 crece >= x1,15 sobre la anterior
[ ] Los rendimientos por stat son decrecientes, no lineales
[ ] Ninguna opción es estrictamente mejor que otra (probado en planilla)
[ ] Toda opción tiene al menos un contexto donde es la mejor elección
[ ] El loop positivo aporta <= 10 % de ventaja por ciclo
[ ] Existe al menos un freno de inflación activo (sumidero creciente / rend. decreciente / conversión con pérdida)
[ ] Se corrió una simulación (a mano o automatizada) de la economía completa
[ ] Se preguntó a un tester qué resignó al elegir, y supo contestar
[ ] No hay stock que crezca monótonamente durante toda la partida
```

## Aplicación
**Game Design abre este libro cuando:** define recursos y monedas de un GDS, arma tabla de precios o costos, diseña un árbol de mejoras, detecta una build dominante, o cuando el playtest muestra acumulación muerta o grind involuntario.

**Qué trae la IA por default:** el mapa fuente/sumidero/conversor/stock del sistema propuesto antes de escribir un número, la planilla de primera aproximación con las fórmulas de escalado, la detección de dominancia estricta comparando opciones en una unidad común, y la pregunta de sistema mínimo ante cada moneda nueva.

## Límites
No aplica igual en: juegos sin recursos persistentes (arcade puro, ver [[01_Pong]]), narrativos, y sandbox creativos donde acumular *es* el objetivo. En PvP competitivo el balance de opciones domina sobre el balance de economía y la herramienta principal pasa a ser la telemetría masiva, que el dev solo no tiene: ahí conviene reducir el espacio de opciones antes que intentar balancear muchas.

**Tensiones:** con el Pilar 7 (recompensa) — los frenos de inflación se sienten como castigo si no se explican. Con `06_Dificultad_y_curva` — la economía es el vector por el que la curva se aplana sin permiso. Con el Pilar 9 (agencia) — cada sumidero automático (decaimiento, impuestos) le saca decisión al jugador: preferí siempre el sumidero elegido.

## Fuentes
[[15_Game_Mechanics]] · [[01_Rules_of_Play]] · [[08_Designing_Games]] · [[03_Game_Design_Workshop]] · [[07_Characteristics_of_Games]] · [[17_Uncertainty_in_Games]] · [[14_Fundamentals_of_Game_Design]] · [[16_Advanced_Game_Design]] · [[02_Art_of_Game_Design]]
Cruces: [[05_Fundamentos_de_experiencia_ludica]] (Pilares 6 y 9) · [[04_Playbook_de_diseno]] · `06_Dificultad_y_curva` · `08_Progresion_y_recompensa` · [[01_Loop_de_experiencia]]

---

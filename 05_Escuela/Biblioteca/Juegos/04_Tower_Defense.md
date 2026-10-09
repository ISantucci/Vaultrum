---
tipo: juego
genero: Estrategia
subtipo: Tower defense de colocación libre y cámara fija (oleadas deterministas)
estado: En la Biblioteca
mision: EST-018_Mision_Balance_Tower_Defense
cruza: 05_Fundamentos_de_experiencia_ludica, 07_Economia_y_balance, 09_Onboarding_y_tutorial, 14_UI_HUD_y_menus, 15_Muerte_reintento_y_checkpoints, 12_Pacing_y_estructura, 11_Camara_y_encuadre, 02_Game_feel, 16_Audio_como_gameplay
---

# Libro 04 — Tower Defense

> Género: Estrategia / tower defense de colocación libre, cámara fija y oleadas deterministas.
> Lo **transversal** vive en `05_Fundamentos_de_experiencia_ludica`, `07_Economia_y_balance` y `09_Onboarding_y_tutorial`; acá va lo **específico**, y en especial qué hace que perder se lea como una decisión y no como azar.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Índice del libro

- Loop de experiencia
- Table-stakes
- La derrota corregible, en detalle
- Juice / game feel
- Baseline de parámetros
- Economía de la partida — fuentes, sumideros y holgura
- Lo que funciona, con mecánicas propias
- Cómo se mide el balance con bots
- Antipatrones de balance
- Definición de Terminado
- Aplicación
- Límites
- Fuentes

---

## Loop de experiencia

En un tower defense el jugador no ejecuta: **asigna** oro escaso en el espacio (dónde) y en el tiempo (ahora o después, construir o mejorar). Las torres disparan solas; el jugador mira resolverse un plan ya comprometido.

```txt
LOOP DE DECISIÓN (≈3–10 s)
  leer amenaza y oro → elegir torre → ubicar el fantasma (rango, válido) → confirmar → ver disparar
        ↑                                                                                   │
        └───────────────────────────────────────────────────────────────────────────────────┘

LOOP DE OLEADA (≈30–90 s)      ventana → la oleada corre (detectar filtraciones) → cobrar → ventana
LOOP DE NIVEL  (≈8–20 min)     primera defensa → escalar la economía → oleada pico → estrellas o derrota
LOOP META      (entre niveles) torre o enemigo nuevo → nivel siguiente, o volver por estrellas
```

El que define al género es el **de oleada**: planificar → observar → diagnosticar → corregir. Una oleada que no deja ver por qué algo se filtró corta el ciclo. `01_Loop_de_experiencia`

**Qué lo hace juego y no juguete:** la escasez. Con oro infinito es un editor de torres. `07_Economia_y_balance`

**Dónde vive la tensión:** en la **incertidumbre de planificación**: el oro se compromete antes de saber si alcanza. El jugador sabe *qué* pasó y tiene que poder saber **por qué**; si no ve rango, costo o inmunidad, la derrota pasa a ser azar. `17_Uncertainty_in_Games`

---

## Table-stakes

Lo que un TD **no puede no tener** para estar terminado. Si falta uno, perder deja de enseñar.

| # | Table-stake | Por qué es obligatorio |
|---|-------------|------------------------|
| 1 | **Camino, entradas y base legibles** desde la cámara fija, sin nada que los tape | Con colocación libre, el camino define dónde conviene construir; lo tapado no se planifica. `11_Camara_y_encuadre` |
| 2 | **Previsualización de colocación**: el fantasma muestra válido/inválido **con el motivo** antes de confirmar | Un clic que no construye y no dice por qué se lee como un juego roto |
| 3 | **Rango visible** en el fantasma, al seleccionar una torre puesta y como preview de la mejora | El rango decide el valor de cada lugar; verlo después de pagar es adivinar |
| 4 | **Costo y asequibilidad antes de comprar** | El oro es aritmética auditable y el juego tiene que dejarla hacer. `07_Economia_y_balance` |
| 5 | **Oro como flujo visible**: lo que paga cada baja, lo que cuesta cada compra, el total siempre en pantalla | Es la única fuente. Si no se ve entrar, "defender bien" no se conecta con "tener más" |
| 6 | **Qué ataca cada torre** (tierra/aire, blindaje), visible antes de pagar | Con counters duros, comprar la torre equivocada es la derrota más frecuente |
| 7 | **Amenaza legible por silueta**, no solo por color; el aéreo marca su posición en el piso | Con cámara inclinada, la altura engaña respecto del rango; el color solo falla con daltonismo |
| 8 | **Ataque inválido distinto del daño**: el impacto que no hace nada y la torre que no puede apuntar se ven y se oyen distinto | Separa "me falta daño" de "me falta el counter". Doucet: la inmunidad ilegible es dificultad falsa |
| 9 | **Cada amenaza nueva se presenta antes de ser letal**: aviso, y un debut en cantidad que cuesta vida, no el nivel | Con oleadas no anunciadas es la única información previa. `09_Onboarding_y_tutorial` |
| 10 | **Estado de oleada**: N de M, en curso o entre oleadas, y cuándo arranca la próxima | Es el reloj del loop; la ventana es el valle de `12_Pacing_y_estructura` |
| 11 | **Daño a la base atribuible**: la vida baja con feedback fuerte y se ve qué entró y por dónde | La derrota es acumulativa y ocurre lejos de su causa. `15_Muerte_reintento_y_checkpoints` |
| 12 | **Mejora y venta legibles**: delta antes de pagar, silueta nueva al mejorar, reembolso con la pérdida antes de confirmar | Son las decisiones que corrigen un plan sin reempezar; sin preview son apuestas |
| 13 | **Estados completos y reintento**: pausa que congela, victoria con estrellas explicadas, derrota que nombra oleada y causa, reintento sin cerrar | El reintento es lo que vuelve experimento a la derrota. `14_UI_HUD_y_menus` |
| 14 | **Onboarding desde cero**: colocar → ver disparar → cobrar → mejorar, de a uno; la oleada 1 se gana con la primera torre bien puesta | Kingdom Rush mide la oleada 1 contra la primera defensa; PvZ arranca con un solo carril |

---

## La derrota corregible, en detalle

Un TD es justo cuando perder deja una **hipótesis**. Cuatro condiciones, a la vez:

| # | Condición | Qué exige | La sostienen |
|---|-----------|-----------|--------------|
| 1 | **Determinismo** | misma defensa y misma oleada, mismo resultado; sin azar en el núcleo | regla de sistema |
| 2 | **Información antes del compromiso** | rango, costo, objetivos y delta de mejora antes de pagar | TS 3, 4, 6, 12 |
| 3 | **Causa visible en el momento** | qué se filtró, por dónde y por qué | TS 7, 8, 11 |
| 4 | **Reintento barato** | reintentar sin cerrar, con las mismas oleadas | TS 13 |

Sin la 1 no se puede probar la hipótesis; sin la 2 se castiga lo que no se podía saber; sin la 3 no se sabe qué cambiar; sin la 4 no conviene probarlo.

**Tres causas, tres feedbacks.** Toda filtración tiene una, y se distinguen mirando:

```txt
FALTA DE DAÑO       recibió impactos todo el camino           → barra de vida, impacto normal
FALTA DE COBERTURA  cruzó un tramo sin torre en rango         → el tramo sin círculo de rango
FALTA DE COUNTER    recibió impactos que no le hicieron nada  → feedback de ataque inválido (TS 8)
```

**Oleadas no anunciadas: quién paga la sorpresa.** Sin composición anunciada, la primera partida de un nivel es exploración. Lo compensan el determinismo, la presentación de cada amenaza nueva (TS 9) y un debut dimensionado para que **la sorpresa cueste estrellas y no el nivel**: el que se sorprendió gana con una estrella, sabe por qué y vuelve por las tres. Una sorpresa letal en la oleada 12 de 15 cobra doce oleadas de espera por cada corrección.

**El error de input no es una decisión.** Un clic corrido construye mal, y venderla con pérdida castiga la puntería, no el plan. *Hipótesis:* deshacer la última colocación con reembolso total mientras la torre no haya disparado.

---

## Juice / game feel

En el TD el juice pelea contra la escala: veinte torres disparando son veinte fuentes de feedback. Rige una **jerarquía**, de lo raro y grave a lo frecuente:

```txt
filtración  >  ataque inválido  >  amenaza nueva  >  baja y oro  >  disparo
```

| Efecto | Qué comunica | Cuidado |
|--------|--------------|---------|
| **Fantasma con tinte y rango dibujado sobre el terreno** | dónde puede ir y qué va a cubrir | Inválido con ícono, no solo color; en perspectiva, un círculo en pantalla miente |
| **Sombra o marcador bajo cada aéreo** | dónde está respecto de los rangos | Sin ella, la altura engaña a la cámara inclinada |
| **"+N" de oro que viaja al contador** | de dónde sale el oro | Agrupar si mueren muchos juntos |
| **Hit flash corto + barra de vida** | daño efectivo | Nunca screenshake por disparo |
| **Rebote metálico con chispa; ícono sobre la torre que no puede apuntar** | falta el counter | Forma y sonido distintos del impacto |
| **Sacudida de la base, flash en la vida, marca del tipo que entró** | perdiste vida y por culpa de quién | Único lugar del screenshake. `59_The_Art_of_Screenshake` |
| **Silueta nueva en N2 + pulso del rango** | el nivel de cada torre, a distancia | Se distingue sin seleccionar |

Regla heredada de `02_Game_feel` y `60_Juice_It_or_Lose_It`: **el juice nunca puede tapar el camino.** En audio rige la misma jerarquía (`16_Audio_como_gameplay`): la filtración se oye por encima de cien disparos.

---

## Baseline de parámetros

Punto de partida, no dogma. Relaciones entre magnitudes del propio juego —**R** rango de la torre base, **V** velocidad del enemigo base, **C** costo de la torre base, **L** largo del camino—. **Consenso** = lo hacen los juegos estudiados o lo impone la aritmética; **hipótesis** = destilación propia, se valida jugando.

La unidad del género es la **exposición**: camino dentro del rango ÷ V. Una torre vale lo que daña mientras el enemigo está en rango; por eso Doucet vio dominar al largo alcance por pura cobertura.

| Relación | Baseline | Estatus | Por qué |
|----------|----------|---------|---------|
| Daño efectivo | DPS × exposición; el rango se cobra por la exposición que agrega | Consenso (aritmética) | Unidad común entre torres; el rango barato es la dominancia más común |
| Largo del camino | L ≈ 4–8 diámetros de rango base (2R) | Hipótesis | Menos: una torre cubre todo. Más: la decisión de lugar se diluye |
| Lugares premium | 2–4 zonas donde una torre cubre ≥ 2× el camino de una recta; caben 2–4 torres | Geometría consenso; cantidades hipótesis | Kingdom Rush da escasez con puntos fijos; acá la dan la geometría y la huella |
| Oro inicial | 1–2 torres base; la oleada 1 se gana con una | Consenso | La primera decisión es *dónde*, no *cuánto* |
| Ingreso por oleada temprana | ≈ 1–2 compras | Hipótesis | Menos: la ventana no tiene decisión. Mucho más: nada pesa |
| Mejora N1→N2 | costo 0.8–1.5 C; eficiencia por oro de la N2 ≈ 0.9–1.2× la de la N1 (mejora = 1 C → la N2 rinde 1.8–2.4×) | Hipótesis | Arriba de 1.2 mejorar domina; debajo de 0.9 nadie mejora. En el medio, mejorar gana en el lugar premium y construir en cobertura |
| Venta | reembolso 50–80%; reubicar una torre base pierde ≥ 20% de C y menos que una oleada de ingreso | Pérdida consenso (BTD6 ≈ 70%); rango hipótesis | Al 100% las torres son alquiler; muy abajo, corregir arruina |
| Ventana entre oleadas | la del valle de `12_Pacing_y_estructura` (20–40% de la oleada previa, ≥ 20 s), nunca menor que lectura + las compras que el ingreso permite (≈ 3–5 s cada una); o arranque a pedido | Proporción de `12`; piso de compras hipótesis | Más corta: se pierde por mano, no por plan |
| Densidad vs cadencia | por tramo, vida que entra por segundo ≤ daño efectivo del tramo | Consenso (aritmética) | Es la ecuación de la oleada; juntar enemigos vuelve necesarias las torres de área |
| Debut y estrellas | estrellas contadas en filtraciones (3★ = 0–2 básicas; 1★ = sobrevivir); daño del debut sin counter < margen entre 3★ y 1★ | Hipótesis | La sorpresa cuesta estrellas, no el nivel |
| Counters | ≥ 2 respuestas por tipo, disponibles ≥ 1 nivel antes | Consenso evitar llave-y-cerradura; cantidades hipótesis | Una sola respuesta es un control de inventario |
| Dominancia | < 5% de uso: muerta; > 50% del gasto en la mayoría de las victorias: domina | 5% de `07_Economia_y_balance`; 50% hipótesis | Se confirma jugando |
| Holgura del bot competente (H_bot, ver *Economía de la partida*) | ≤ 2 en el primer nivel de un mundo, bajando hasta 1.2–1.5 en el último | Hipótesis | El bot es cota optimista: con H_bot ≈ 1 un humano no gana; con H_bot > 2 al final del mundo el oro deja de decidir |
| Sonda de una sola torre | no hace 3★ en los niveles que presentan un tipo con counter obligatorio | Hipótesis (sale de la fila *Counters*) | Si la hace, el counter era decorativo o sobra oro |
| Profundidad del sumidero por lugar | ≥ ingreso del nivel ÷ (H objetivo × lugares que valen la pena) | Aritmética (E1) | Si no alcanza, el oro que sobra no tiene destino y H sube sola |
| Ingreso tardío | crece a la par del sumidero útil, no más rápido | Consenso (Cook; BTD6 grava la recompensa tardía) | Si crece más rápido, el final del nivel es el tramo más fácil (E2) |

**Cómo se mide si una torre domina.** En la planilla, vida retirada por oro con la exposición de un lugar *típico* (`37_Game_Balance`). En playtest, tasa de elección, tiempo de decisión en la tienda (instantáneo = dominancia) y la composición única: si una torre repetida gana todo, domina. `13_Playtesting_y_validacion`, `62_Playing_to_Win`

**Regla de oro:** se afinan juntos el **enemigo base** (V, vida) y la **torre base** (R, daño, C); el camino, los lugares premium, el oro por baja y la separación dentro de la oleada se derivan de la exposición. Un mapa dibujado antes de fijar R y V se rehace. `33_The_Level_Design_Book`

---

## Economía de la partida — fuentes, sumideros y holgura

La máquina general (fuente, sumidero, conversor, stock) y la regla de cierre están en `07_Economia_y_balance`. Acá va cómo se ve esa máquina **adentro de una partida de TD**, que tiene una particularidad: el sumidero principal, construir, compra poder, y ese poder mata más y cobra más. **Un TD es un loop positivo por diseño.** Lo que lo frena no es un precio: es que el poder comprado deje de hacer falta.

```txt
FUENTES                                   SUMIDEROS
oro inicial (una vez)                     construir   ANCHO: una torre más en otro lugar
recompensa por baja (crece con la         mejorar     PROFUNDIDAD: la misma torre, más fuerte
  cantidad de enemigos de cada oleada)    habilidades o consumibles, si existen
bonus por oleada o por adelantarla        venta       sumidero parcial: devuelve una fracción
torre de ingreso (inversión)              enemigo que no paga: presión sin ingreso
venta (fuente parcial)
```

La pregunta que decide si el balance funciona es **si el oro que entra hace falta**. Se mide con la **holgura**:

```txt
holgura  H = oro que ofrece el nivel / oro que un jugador competente necesita para la meta (3★)
```

```txt
H ≈ 1      cada compra importa; un error cuesta estrellas                 → tenso
H ≫ 1      el excedente compra torres que no cambian el resultado:
           el jugador deja de decidir y se aburre AUNQUE GANE              → flojo
H < 1      el nivel es imposible para ese jugador                         → roto
```

`H ≫ 1` es la cadena floja de Cook: el recurso se acumula sin tirar de nada, y el jugador deja de encontrarle valor a los primeros pasos. Por eso el síntoma de un TD con exceso de fuentes no es que sea fácil, sino que **aburre**. La victoria llega sin que ninguna decisión la haya decidido.

### Las cuatro relaciones de la economía

**E1 · Ancho o profundidad.** Si el lugar sobra, el oro se convierte en torres de forma lineal. El sumidero crece solo con el ingreso, y el último lugar agregado vale casi nada: el jugador llena el mapa. Si el lugar escasea (Kingdom Rush, puntos fijos), el oro va a profundidad, y el camino de mejora tiene que ser largo. Con colocación libre, la escasez la dan la geometría y la huella (`Lugares premium` en el baseline):

```txt
profundidad del sumidero por lugar  ×  lugares que valen la pena   ≥   ingreso del nivel / H objetivo
```

Si el lado izquierdo es más chico, el oro que sobra no tiene destino, y H sube aunque nadie la haya subido.

**E2 · Fuente y sumidero con la misma potencia.** Una fuente que crece (la recompensa por baja sube con la cantidad de enemigos de la oleada) necesita un sumidero que crezca igual (escalones de mejora con costo creciente) o una fuente que se frene. Si no, el final del nivel es el tramo más fácil. Cook lo formula como emparejar potencias: constante con constante, lineal con lineal. BTD6 lo resuelve por el lado de la fuente. Paga 1 por globo hasta la ronda 50 y después grava la recompensa por globo en escalones (50 % desde la 51, 20 % desde la 61, 10 % desde la 86, 5 % desde la 101, 2 % desde la 121), mientras el bonus por ronda sigue siendo lineal (100 + número de ronda).

**E3 · La inversión necesita destino.** Una torre de ingreso (el girasol de PvZ, la granja de BTD6) convierte defensa presente en oro futuro. Es una decisión real **solo si H ≈ 1**, porque renunciar a defensa ahora tiene que doler. Con H ≫ 1 es gratis y nada más agrega inflación. Además tiene que recuperar lo que cuesta antes de que termine el nivel.

**E4 · La única fuente que agrega una decisión es la que se paga con riesgo.** Llamar la oleada antes a cambio de oro (Kingdom Rush) cambia seguridad por ingreso, y el jugador la elige. Cualquier otra fuente llega sola. Del otro lado, **un enemigo que no paga** (en Kingdom Rush, varios invocados no dan oro) es la forma más barata de bajar H sin tocar un solo precio, siempre que el jugador sepa que no paga.

---

## Lo que funciona, con mecánicas propias

De los juegos que funcionan no se copia la mecánica: se copia la **función económica**, y se la cumple con una mecánica propia. La tabla dice qué hace cada patrón en la máquina; cuál usa cada juego es decisión del `GDS`.

| Patrón | Qué hace en la economía | Lo usan | Cuidado |
|---|---|---|---|
| **Camino de mejora largo y escalonado** | profundiza el sumidero por lugar (E1) y crece con el ingreso (E2) | BTD6, Kingdom Rush | cada escalón tiene que cambiar algo visible (TS 12); si no, es un impuesto |
| **Escasez de lugar** | empuja el oro hacia la profundidad | Kingdom Rush (puntos fijos) | con colocación libre se construye con la geometría y la huella, no con una grilla |
| **Ingreso tardío acotado** | frena la inflación del final (E2) | BTD6 (recompensa por globo gravada desde la ronda 51) | se anuncia; una regla oculta se lee como castigo |
| **Oro por adelantar la oleada** | fuente con riesgo elegido (E4) | Kingdom Rush | no puede ser siempre la mejor jugada: el bonus tiene que costar margen real |
| **Torre de inversión** | defensa presente contra oro futuro (E3) | PvZ (girasol), BTD6 (granja) | solo es decisión con H ≈ 1; con holgura es la mejor torre del juego |
| **Enemigo que no paga** | presión sin ingreso (E4) | Kingdom Rush (invocados) | se tiene que leer: el jugador sabe que ese no deja oro |
| **Habilidad o consumible con costo** | sumidero que se decide en el momento | Kingdom Rush (hechizos), BTD6 (poderes) | si tiene azar, rompe la condición 1 de la derrota corregible |
| **Venta con pérdida** | corrige sin anular el costo de la decisión | BTD6 (70 %) | ver la fila *Venta* del baseline |
| **Moneda meta por completar, no por repetir** | la meta no se muele (`07_Economia_y_balance`, grind involuntario) | Kingdom Rush Vengeance y Alliance (puntos fijos por etapa, sin importar las vidas) | el incentivo a repetir lo tiene que dar el desafío (estrellas), no la moneda |

Un juego con mecánicas únicas hace la misma pregunta con cada una: **¿de qué lado de la máquina está, y con qué potencia?** Una torre que no ataca y junta oro es una inversión (E3). Un enemigo que no paga es un sumidero de presión (E4). Una mejora temporal de un solo escalón es profundidad corta (E1). Que la mecánica sea nueva no la exime de la aritmética.

---

## Cómo se mide el balance con bots

La planilla da la primera aproximación; el bot dice qué pasa cuando todo interactúa. Un bot **no es un jugador**: reacciona rápido, no duda y elige el mejor lugar. Es una **cota optimista**: lo que el bot no puede ganar, un humano tampoco, y lo que el bot gana con holgura enorme, un humano lo gana aburrido.

```txt
HOLGURA POR ESCALADO   se escalan todas las fuentes por f (0 < f ≤ 1), sin tocar el oro
                       inicial (la primera decisión se conserva). f* = el menor f con el que
                       el bot competente todavía hace 3★.  H_bot ≈ 1 / f*.
                       Lo mismo con 1★ da el margen entre perder estrellas y perder el nivel.

SONDAS DEGENERADAS     el mismo nivel con planes que el diseño NO quiere premiar: una sola
                       torre repetida, sin mejoras, un jugador lento. Si una sonda hace 3★ donde
                       el nivel pide combinar, hay dominancia, holgura, o las dos.

CURVA DE HOLGURA       H nivel por nivel. Tiene que bajar a lo largo del mundo y mesetar
                       donde el diseño lo pide. Una H plana es un mundo sin curva.

DESTINO DEL GASTO      oro a construir contra oro a mejorar; torres en el mapa al terminar
                       contra lugares premium. Si el bot llena el mapa, el sumidero es solo
                       de ancho (E1).

INGRESO POR OLEADA     en unidades de costo de la torre base (C): el baseline pide 1–2
                       compras por oleada temprana. Mucho más, y la ventana pierde la decisión.
```

La holgura se mide primero **sin mejoras permanentes** (ver *Límites*: la dificultad se mide sin meta) y después con las que el jugador puede tener al llegar a ese nivel.

**Lo que el bot no mide:** cuánto rinde un humano contra el bot (`H_humano < H_bot`, y cuánto menos solo lo dice un playtest), si la decisión *se siente* (`13_Playtesting_y_validacion`) ni si el jugador entiende por qué ganó.

---

## Antipatrones de balance

| Antipatrón | Síntoma | Qué se rompió |
|---|---|---|
| **Oro sin destino** | el nivel termina con el mapa lleno de torres que no hacían falta; el bot gana igual con la mitad del oro | H ≫ 1 (E1) |
| **Recompensa lineal en oleadas que crecen** | el final del nivel es el tramo más fácil | E2 |
| **Solo ancho** | el jugador repite la misma torre en todo lugar libre | escasez y profundidad (E1) |
| **Inversión con holgura** | la torre de ingreso es la mejor torre del juego | E3 |
| **Mejora de un solo escalón con ingreso creciente** | a mitad del nivel no hay nada que profundizar y el oro se amontona | E1 + E2 |
| **Holgura igual en todo el mundo** | el último nivel se siente como el primero | curva de holgura |
| **Meta que se muele** | repetir N veces el nivel más rentable para pagar la tienda | moneda meta por repetir |
| **Balance medido solo con el bot competente** | todo "anda" y nadie ve que una sola torre gana | faltan las sondas degeneradas |
| **Arreglar la holgura con vida de enemigos** | cada torre dispara más para matar lo mismo; nada cambia en la decisión de gasto | el problema era de oro, no de daño |

---

## Definición de Terminado

Checklist específica del género. Se corre **sobre el juego corriendo**, no sobre el código.

```txt
ESPACIO Y COLOCACIÓN
[ ] Veo el camino entero, las entradas y la base sin mover la cámara; nada lo tapa
[ ] Antes de confirmar sé si puedo construir ahí y, si no, por qué
[ ] Veo el rango antes de colocar, al seleccionar y antes de mejorar, y coincide con lo que la torre alcanza

ECONOMÍA
[ ] Veo el precio antes de comprar y sé si me alcanza
[ ] Cada baja muestra el oro que pagó; cada compra y venta mueve el contador
[ ] La oleada 1 se gana con el oro inicial y una torre bien puesta

AMENAZA
[ ] Distingo cada enemigo por la silueta, también en grises, y ubico al aéreo respecto de mis rangos
[ ] Sé qué puede atacar cada torre antes de comprarla
[ ] Un ataque que no hace daño se ve y se oye distinto de un impacto
[ ] Ningún tipo que exige counter debuta sin aviso o en cantidad letal

OLEADA Y BASE
[ ] Sé en qué oleada estoy, cuántas faltan y cuándo arranca la próxima
[ ] Entre oleadas me alcanza el tiempo para las compras que mi oro permite
[ ] Cuando pierdo vida, sé qué enemigo entró y por dónde
[ ] La misma defensa contra la misma oleada da el mismo resultado

MEJORA Y VENTA
[ ] Veo qué cambia la mejora antes de pagarla, y distingo una N2 sin seleccionarla
[ ] Veo cuánto me devuelve la venta antes de confirmar

BALANCE Y ECONOMÍA
[ ] Termino el nivel sin oro de sobra que no tenga en qué gastar para cambiar algo
[ ] A mitad y al final del nivel todavía tengo una decisión de gasto: construir, mejorar o guardar
[ ] Una sola torre repetida no me da 3★ donde el nivel pide combinar
[ ] El último nivel del mundo me exige más que el primero, y lo noto en el oro, no solo en la vida de los enemigos

PARTIDA Y ESTADOS
[ ] Puedo pausar y todo se congela
[ ] La victoria explica sus estrellas; la derrota nombra la oleada y la causa
[ ] Reintento el nivel sin cerrar la aplicación, y toda pantalla tiene salida

ONBOARDING
[ ] Alguien que nunca jugó un TD coloca su primera torre en < 60 s
[ ] Aprendo colocar, cobrar y mejorar de a una cosa por vez

FEEL
[ ] Una filtración se siente más grave que cualquier otra cosa en pantalla
[ ] Con el mapa lleno de torres, el juice no me impide ver el camino
```

Un TD que dispara pero no tilda **Amenaza**, **Oleada y base** y **Mejora y venta** es un TD donde perder es azar: el 4/10 de la Ley #1.

---

## Aplicación

- **Cuándo se abre:** ante cualquier pedido de tower defense con torres automáticas. Producción mapea las table-stakes a `RQ`; Game Design arma la planilla de `07_Economia_y_balance` **en unidades de exposición**; **Level Design deriva el camino de R y V**, porque su forma es balance, no estética; UI/UX toma las table-stakes 2–12 como presupuesto mínimo de comunicación.
- **Qué trae la IA por default:** las 14 table-stakes, las cuatro condiciones, la jerarquía de feedback, el baseline, las cuatro relaciones de la economía con la holgura como medida, las sondas de bots y la Definición de Terminado.
- **Qué NO decide:** el roster de torres y enemigos, la ambientación, cuántos niveles, la meta-progresión, ni si las oleadas se anuncian. El libro dice qué cuesta cada opción; el `RQ` elige.

## Límites

- Es de **experiencia**, no de implementación: pathfinding, criterio de objetivo y pooling de proyectiles son del `SOL`.
- **Laberinto o bloqueo de camino:** la exposición pasa de dato del nivel a decisión del jugador. Misión de profundización.
- **Héroe controlable o TD de acción** (Kingdom Rush con héroe, Orcs Must Die, Dungeon Defenders): suma incertidumbre de ejecución. Otro libro.
- **Habilidades activas**, **torres destructibles**, **multijugador** y **oleadas procedurales** (rompen la condición 1): no cubiertos.
- **Meta-progresión profunda:** Harlow muestra que las mejoras compradas con estrellas trivializan la curva de Kingdom Rush; la dificultad se mide sin meta. `08_Progresion_y_recompensa`
- **Carriles en grilla** (PvZ): valen las table-stakes, no las relaciones de geometría.

---

## Fuentes

Recombinación sobre fichas del vault más cinco fuentes del género investigadas en esta misión:

- Teddy Phan, *Tower Defense Game Rules (Part 1)*, Game Developer, 2017 — taxonomía de derrota, colocación, oro por baja y aéreos. https://www.gamedeveloper.com/design/tower-defense-game-rules-part-1-
- Lars Doucet, *Optimizing Tower Defense for Focus and Thinking*, Game Developer, 2014 — información completa, control del tiempo, dominancia por cobertura, contra la llave-y-cerradura. https://www.gamedeveloper.com/design/optimizing-tower-defense-for-focus-and-thinking---defender-s-quest
- David Harlow, *Kingdom Rush — the wonderful Campaign level design*, Game Developer, 2013 — enemigos escalonados, oleada 1 a medida, puntos fijos como escasez, mejoras por estrellas. https://www.gamedeveloper.com/design/kingdom-rush---the-wonderful-campaign-level-design
- George Fan, *How I Got My Mom to Play Through Plants vs. Zombies*, GDC 2012 — tutorial fundido en el juego, un elemento nuevo por nivel, primer nivel de un carril. https://www.gdcvault.com/play/1015541/How-I-Got-My-Mom — **cobertura parcial:** slides con 403; paráfrasis a verificar contra el video.
- Blooncyclopedia, *Camo Bloon* y *Lead Bloon* (BTD6) — inmunidad por tipo, rondas fijas. https://www.bloonswiki.com/Camo_Bloon_(BTD6) · https://www.bloonswiki.com/Lead_Bloon_(BTD6) — **cobertura parcial:** no leídas; solo convenciones de consenso. La venta al 70 % sí está leída: Bloons Wiki, *Selling* — https://bloons.fandom.com/wiki/Selling

Agregadas por `EST-018` (economía y balance):

- Daniel Cook, *Value chains – A method for creating and balancing faucet-and-drain game economies*, Lost Garden, 2021 — fuentes y sumideros de potencia pareja, la cadena floja, los síntomas de una economía rota. https://lostgarden.com/2021/12/12/value-chains/
- Bloons Wiki, *Rounds (BTD6)* — 1 por globo, bonus 100 + ronda, la recompensa gravada desde la ronda 51. https://bloons.fandom.com/wiki/Rounds_(BTD6) · topper64, *BTD6 Income Calculator*, con los mismos escalones. https://topper64.co.uk/nk/btd6/income
- Kingdom Rush Wiki, *Gold* — recompensa según la fuerza del enemigo; invocados que no pagan. **Cobertura parcial:** la página documenta el bonus por adelantar de un héroe; el oro por llamar la oleada antes, como regla general, queda como convención del género. https://kingdomrushtd.fandom.com/wiki/Gold
- Kingdom Rush Wiki, *Upgrades* — estrellas por vidas; en Vengeance y Alliance, puntos fijos por etapa sin importar las vidas. https://kingdomrushtd.fandom.com/wiki/Upgrades
- Plants vs. Zombies Wiki, *Sunflower* — la planta de inversión. **Cobertura parcial:** sus números no se usan. https://plantsvszombies.fandom.com/wiki/Sunflower

Fichas del vault: las citadas con backticks en el cuerpo; el mayor aporte es de `07_Economia_y_balance`, `09_Onboarding_y_tutorial` y `15_Muerte_reintento_y_checkpoints`.

**Cobertura declarada:** de las 14 table-stakes, **ocho** salieron de fichas que ya existían —1, 4, 5, 9, 10, 11, 13 y 14— y **seis** de destilación propia: 2, 3, 6, 7, 8 y 12. *La derrota corregible* y la exposición como unidad del *Baseline* también son propias. De `EST-018`, las relaciones E1–E4, la holgura y las sondas de bots son destilación propia sobre Cook, BTD6, Kingdom Rush y PvZ. El interés sobre el oro guardado (Element TD, Legion TD) no se pudo leer y queda afuera.

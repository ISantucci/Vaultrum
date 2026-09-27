---
tipo: juego
genero: Estrategia
subtipo: Tower defense de colocación libre y cámara fija (oleadas deterministas)
estado: En validación
mision: EST-016_Mision_Tower_Defense
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

**Cómo se mide si una torre domina.** En la planilla, vida retirada por oro con la exposición de un lugar *típico* (`37_Game_Balance`). En playtest, tasa de elección, tiempo de decisión en la tienda (instantáneo = dominancia) y la composición única: si una torre repetida gana todo, domina. `13_Playtesting_y_validacion`, `62_Playing_to_Win`

**Regla de oro:** se afinan juntos el **enemigo base** (V, vida) y la **torre base** (R, daño, C); el camino, los lugares premium, el oro por baja y la separación dentro de la oleada se derivan de la exposición. Un mapa dibujado antes de fijar R y V se rehace. `33_The_Level_Design_Book`

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
- **Qué trae la IA por default:** las 14 table-stakes, las cuatro condiciones, la jerarquía de feedback, el baseline y la Definición de Terminado.
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
- Blooncyclopedia, *Camo Bloon* y *Lead Bloon* (BTD6) — inmunidad por tipo, rondas fijas, venta ≈ 70%. https://www.bloonswiki.com/Camo_Bloon_(BTD6) · https://www.bloonswiki.com/Lead_Bloon_(BTD6) — **cobertura parcial:** no leídas; solo convenciones de consenso.

Fichas del vault: las citadas con backticks en el cuerpo; el mayor aporte es de `07_Economia_y_balance`, `09_Onboarding_y_tutorial` y `15_Muerte_reintento_y_checkpoints`.

**Cobertura declarada:** de las 14 table-stakes, **ocho** salieron de fichas que ya existían —1, 4, 5, 9, 10, 11, 13 y 14— y **seis** de destilación propia: 2, 3, 6, 7, 8 y 12. *La derrota corregible* y la exposición como unidad del *Baseline* también son propias.

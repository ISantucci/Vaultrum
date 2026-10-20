---
tipo: juego
genero: Sigilo
subtipo: Sigilo top-down 2D con conos de visión, estados de alerta y evasión
estado: En validación
mision: EST-022_Mision_Lote_Juegos_Web_y_Sigilo
cruza: 01_Loop_de_experiencia, 02_Game_feel, 06_Dificultad_y_curva, 09_Onboarding_y_tutorial, 10_Input_y_respuesta, 11_Camara_y_encuadre, 12_Pacing_y_estructura, 14_UI_HUD_y_menus, 15_Muerte_reintento_y_checkpoints, 16_Audio_como_gameplay, 01_Bucle_de_simulacion, 02_Colision_y_consulta_espacial, 05_Endless_runner
---

# Libro 07 — Stealth

> Séptimo libro del estante de Juegos. Género: Sigilo / stealth top-down 2D (la línea de Metal Gear de 1987 y de Metal Gear Solid).
> Lo **transversal** vive en los Fundamentos. Acá va lo **específico**: qué pasa cuando el jugador no gana por reflejos sino por **leer a un enemigo que percibe**, y el juego tiene que dejarle leer esa percepción.
> **IP:** conceptos destilados + cita. Metal Gear y Metal Gear Solid son propiedad de Konami; no se copia texto, arte ni sonido. Ninguna cifra del baseline es de un juego comercial: los números son **destilación propia, a calibrar en playtest**, salvo los marcados con fuente (las cifras sueltas de juegos que aparecen en el texto, como los 18 meses de Thief, van con su cita).
> **Medido:** nada. Este libro no tiene bot ni juego corriendo detrás (a diferencia de `05_Endless_runner`). Todo el baseline es hipótesis coherente, no medición. Ver *Límites*.

---

## Índice del libro

- Loop de experiencia
- Table-stakes
- Juice / game feel
- Conos de visión y percepción
- Detección gradual vs binaria
- Estados de alerta y sus tiempos
- Sonido
- Legibilidad del sistema
- Patrullas y la ventana segura
- Baseline de parámetros
- Variantes, y qué parte del baseline reescribe cada una
- Definición de Terminado
- Aplicación
- Límites
- Fuentes

---

## Loop de experiencia

El sigilo invierte la relación del acción: en acción el enemigo empuja al jugador; en sigilo el jugador **empieza sin ser detectado** y lo que hace es perturbar un mundo que ya funciona solo. Por eso el placer es planear y anticipar, no reaccionar (Anderson, en Alexander, 2012). La tensión vive en el **margen**: cuánto ruido puedo hacer, cuánto me puedo acercar. Si el jugador no conoce el margen, no hay tensión sino adivinanza.

```txt
LOOP ATÓMICO    (≈3–10 s)     observar el patrón del guardia → elegir el momento → moverse un tramo → quedar a cubierto
LOOP DE SALA    (≈30 s–2 min) entrar → leer la sala → pasar sin ser visto (o recuperarse de un error) → salir
LOOP DE SESIÓN  (≈5–15 min)   sala tras sala → una muerte o un descubrimiento → "esta vez lo hago limpio"
```

**La unidad del género es la sala**, no la partida: el sigilo se aprende por ensayo y error dentro de un espacio acotado, y el costo de un error tiene que ser *esa sala*, no todo lo jugado. `15_Muerte_reintento_y_checkpoints`. Tiempos de cada loop: destilación propia.

**Qué lo hace juego:** el obstáculo aceptado es no poder pelear de igual a igual; el objetivo impuesto es llegar a la salida sin ser visto. Sacale la desventaja y queda un shooter; sacale el objetivo y queda un paseo. En Metal Gear (1987) Kojima partió de una idea de acción y la dio vuelta hacia evitar la captura, con la idea de escondite; al ser descubierto, el juego se vuelve parecido a Pac-Man, con los guardias como fantasmas a evitar (Wikipedia, *Metal Gear*). `01_Loop_de_experiencia`

**La relación que ordena el libro** es la misma que la del runner, con otro sujeto:

```txt
ventana segura  =  tiempo en que un tramo del camino está fuera de todo cono   (se lee contra:)   tiempo de cruzarlo  =  distancia / velocidad
```

La dificultad del sigilo no sale de guardias más listos sino de **ventanas más chicas, más guardias que se solapan y menos refugios**. Ver *Patrullas y la ventana segura*.

---

## Table-stakes

| # | Table-stake | Por qué es obligatorio |
|---|-------------|------------------------|
| 1 | **El cono que se dibuja es el cono que detecta** | Si lo dibujado y lo real difieren, el jugador muere "sin razón". Mark of the Ninja muestra los conos y la luz sobre el personaje; Splinter Cell y Thief muestran el estado en la interfaz. La premisa del libro: un sistema que detecta tiene que poder leerse (Anderson, 2012; GMTK, 2020) |
| 2 | **Las paredes y coberturas tapan la vista** (línea de visión por raycast) | Sin oclusión no hay cobertura, y sin cobertura no hay sigilo. Splinter Cell: Blacklist tira varios rayos al cuerpo y exige que se vean los suficientes (Thompson, 2020; GMTK, 2020) |
| 3 | **Detección gradual con medidor visible, cuyo tiempo mínimo supera la reacción** | Entrar al cono no es perder: un medidor se llena en el tiempo. Piso en forma de relación: `(1 − f_aviso) · t_cercano ≥ 1.2 × reacción visual`. Reacción visual simple ≈ 331 ms (Shelton y Kumar, 2010, n = 14) |
| 4 | **Estados de alerta legibles y distintos entre sí** (patrulla, sospecha, alerta, evasión) | El jugador tiene que saber *qué sabe el guardia*. Metal Gear Solid usa infiltración, alerta, evasión (Metal Gear Wiki); Thief, tras año y medio de desarrollo, seguía con el sigilo sin funcionar bien, y lo resolvió con una gema de luz en pantalla (Kerr, 2018) |
| 5 | **Una forma de ocultarse que cuesta algo** (andar lento y silencioso, o cobertura) | Si esconderse es gratis, es la estrategia única; si es imposible, no hay género. Movimiento silencioso a cambio de velocidad: ver *Baseline* |
| 6 | **El sonido es un segundo canal de percepción, con su radio visible** | Mark of the Ninja dibuja un anillo que muestra hasta dónde llega cada ruido (Alexander, 2012). Sin eso el jugador no puede calcular el margen del ruido |
| 7 | **Patrullas determinísticas y observables, con una ventana segura calculada** | La aleatoriedad en un patrón de guardia convierte la lectura en suerte. El mismo razonamiento que la síncopa ciega de `05_Endless_runner`: el jugador tiene que ver el patrón *antes* de comprometerse |
| 8 | **Evasión: perder a los guardias es posible, tiene cuenta visible y termina** | Es lo que separa sigilo de "reiniciar al primer error": el jugador descubierto tiene un camino de vuelta. MGS devuelve a infiltración cuando el contador llega a cero (Wikipedia, *MGS*) |
| 9 | **El guardia que persigue es más rápido que caminar y más lento que correr** | Relación `v_caminar < v_persecución < v_correr`: escapar corriendo es posible pero hace ruido; caminar no alcanza. Si el guardia alcanza al que corre, no hay evasión; si no alcanza al que camina, no hay amenaza. Destilación propia |
| 10 | **Cada sala tiene al menos una ruta sin detección, y se puede comprobar** | Un nivel que fuerza el descubrimiento rompe el género. Es el equivalente a "todo patrón es superable" del runner. Destilación propia |
| 11 | **Ser capturado se lee claro y el reintento es inmediato, con checkpoint por sala** | Lo que cuesta un error es el tiempo de la sala, no el de la sesión. `15_Muerte_reintento_y_checkpoints` |
| 12 | **La simulación corre con paso fijo y se pausa al perder el foco** | Todas las duraciones del baseline están en segundos de simulación; si dependen del cuadro, el medidor se llena distinto a 60 y a 144 Hz. `01_Bucle_de_simulacion` |

El jugador puede ver la sala entera sin desplazar la cámara; ocultar un cono fuera de pantalla viola la table-stake 1. `11_Camara_y_encuadre`

---

## Juice / game feel

| Efecto | Qué comunica | Cuidado |
|--------|--------------|---------|
| **Anillo de ruido** al caminar o correr (o al tirar un objeto) | hasta dónde llega lo que hago | El anillo muestra el radio real; si exagera, rompe la table-stake 1 |
| **Marca sobre el guardia** al cambiar de estado ("?" al sospechar, "!" al alertarse) | el estado cambió *ahora* | La convención del "!" viene de Metal Gear (Metal Gear Wiki); tiene que ser el evento visual más grande de la sala |
| **Cono que cambia de color y se llena** al detectar | cuánto falta | El color no puede ser el único canal: sumar el medidor y la forma. `14_UI_HUD_y_menus` |
| **Sonido distinto por estado** (sospecha, alerta, vuelta a calma) | que cambió, aunque no mire al guardia | Cada uno suena distinto del paso y del ruido de objeto. `16_Audio_como_gameplay` |
| **Cuenta de evasión visible** (barra o número) | cuánto falta para que se calmen | Un contador oculto es una espera ciega |

**Regla del género: lo que el jugador necesita leer no se tapa con efectos.** Los conos y los medidores van por encima del piso y de las partículas. *Destilación propia.*

---

## Conos de visión y percepción

Un cono simple es irreal y fácil de explotar; los juegos lo capean con capas. Blacklist, según lo que cuenta GMTK (2020), usa un cono principal, una zona periférica más ancha y un punto ciego atrás; Thompson (2020) describe la forma como "tipo ataúd": visión frontal fuerte y periférica lejana débil. En 2D y sin motor alcanza con tres decisiones:

```txt
FORMA       sector circular: alcance R, semiángulo α. Detrás del guardia, punto ciego.
BANDAS      cercana (d ≤ R/2) llena el medidor al doble de velocidad que la lejana
OCLUSIÓN    raycast del guardia a 3 puntos del jugador (centro y dos laterales); visto si ven ≥ 2
```

- **Por qué 3 puntos y no 1.** Con un solo rayo, asomar la punta del cuerpo da una detección que se siente injusta. Blacklist usa varios puntos y un mínimo por postura (Thompson, 2020); acá se baja a 3 con mínimo 2: sin ser un número de ningún juego. *Destilación propia.* **Consecuencia para la table-stake 1:** el polígono que se dibuja es el del *centro* del cuerpo, y la regla de 2 de 3 solo puede recortar la detección en el borde del cono (a lo sumo medio cuerpo, siempre a favor del jugador). Esa es la única diferencia admitida entre lo dibujado y lo real; el chequeo de la Definición de Terminado se hace con el centro del cuerpo sobre el borde.
- **Cálculo de visibilidad en 2D.** Para dibujar el área visible (la parte del cono que no tapa la pared) se puede barrer con rayos hacia los extremos de cada pared (Patel, Red Blob Games). Para decidir si ve al jugador alcanza un raycast por punto; el polígono completo es solo para pintar.
- **El ancho se deriva del alcance:** `ancho del cono a distancia d = 2 · d · tan α`. Con α = 30° el ancho en `R` es ≈ 1.15 R. Cruzar el cono de frente a distancia `d` dura `2·d·tan α / v`.
- **Favorecer al jugador, sin avisarle.** Blacklist reduce a la mitad la audición de los guardias fuera de pantalla; The Last of Us tira el rayo al pecho en vez de la cabeza si el jugador está agachado (GMTK, 2020; ambos de segunda mano, ver *Límites*). El principio, no la cifra: cuando hay duda de dónde cae una detección, se resuelve a favor del jugador.

Los guardias **no son omniscientes**: ven lo que el cono y la oclusión dejan ver, oyen lo que el radio permite, y recuerdan una posición, no un rastro. Ser plausible importa más que ser listo (Walsh, 2014, citado por Thompson, 2020).

---

## Detección gradual vs binaria

Es el eje de diseño más importante después de la forma del cono, y no es una escala moral sino una elección de experiencia:

| | Binaria (o casi) | Gradual (medidor) |
|---|-----------------|-------------------|
| Referente | Mark of the Ninja: casi binaria, con algo de borde difuso en el cono (GMTK, 2020) | Splinter Cell, MGS: el medidor sube según distancia, luz, postura (GMTK, 2020) |
| Qué pide | cono 100 % legible, giro del guardia predecible | cono legible *y* un medidor visible |
| Qué da | decisión de trampa y de planificación | margen de error y recuperación |
| Riesgo | el primer pixel mata | el medidor se vuelve ruido visual |

**Binaria es el límite de gradual cuando `t_fill → 0`.** Esa es la relación que une los dos modelos: el baseline elige gradual porque, con teclado y un ojo en el cono, el jugador necesita unas décimas de reacción. Dos variables controlan el tiempo de llenado: la distancia (banda cercana / lejana) y la postura (silencioso lo alarga). **Ningún modificador baja el tiempo por debajo del mínimo `t_cercano`**: correr no acelera la detección, solo hace ruido. *Destilación propia.*

**El medidor tiene dos umbrales con significado.** Al pasar `f_aviso` el guardia se detiene y se gira hacia el origen (feedback a tiempo); al llegar a 1 pasa a Alerta. Si el jugador sale del cono, el medidor baja a una tasa más lenta que la de subida: rozar el borde del cono no se paga entero, pero tampoco se borra al instante.

---

## Estados de alerta y sus tiempos

```txt
PATRULLA ──(medidor > f_aviso, o ruido oído)──► SOSPECHA ──(medidor = 1)──► ALERTA
   ▲                                               │ (medidor vuelve a 0)       │ (sin línea de visión ≥ T_perdido)
   │                                               ▼                            ▼
   └────────────── (cuenta de evasión llega a 0) ◄─────────────────────────── EVASIÓN ──(lo ven de nuevo)──► ALERTA
```

El esquema de tres estados con vuelta a la calma es el de MGS (infiltración, alerta, evasión; Metal Gear Wiki, Wikipedia *MGS*); la sospecha como estado intermedio sale de la lógica de medidor (GMTK, 2020). Metal Gear (1987) tiene solo dos estados, y dos formas de alerta: un "!" donde solo atacan los soldados de la pantalla (se escapa cambiando de pantalla), y un "!!" —por cámara, sensor, disparo sin silenciador o explosión— donde llegan refuerzos de fuera de pantalla (Wikipedia, *Metal Gear*; Metal Gear Wiki). MGS2 sumó Precaución por cadáveres hallados (Metal Gear Wiki). Ninguna fuente leída da tiempos en segundos de esos estados.

Tiempos del baseline (todos *destilación propia, a calibrar*), con la relación que los fija:

| Transición | Qué la dispara | Tiempo | Relación |
|-----------|----------------|--------|----------|
| Patrulla → Sospecha | medidor > `f_aviso` o ruido en radio | inmediato | el guardia se detiene y mira |
| Sospecha: investigar | llegar al origen del ruido o de la última vista | `t_barrido` = 3 s | tiempo en el que mira alrededor |
| Sospecha → Patrulla | medidor en 0 + `t_barrido` | ≈ 3 s | — |
| Sospecha → Alerta | medidor = 1 | — | ver *Baseline* |
| Alerta: se pierde la vista | sin línea de visión continua | `T_perdido` = 0.8 s | filtra el parpadeo al pasar por una esquina; ver *Baseline* |
| Evasión | `T_perdido` cumplido | `T_ev` = 10 s | `T_ev ≥ d_búsqueda_max / v_persecución + t_barrido`; ver *Baseline* |
| Evasión → Patrulla | cuenta en 0 | — | los guardias vuelven a su ruta |
| Alerta → Capturado | contacto (radio ≈ 0.8 u) | — | pierde la sala |

**Alerta en la sala vs global.** Alerta alerta a *todos los guardias de la sala* (el análogo del "!" de Metal Gear: solo los de esa pantalla). La alerta global —refuerzos de otras salas— es una **variante** (cámara, disparo): reescribe `T_ev` y la table-stake 8.

**Memoria de una sola posición.** En Alerta el guardia va a la *última posición vista*. Durante la línea de visión la actualiza cada cuadro; sin ella no la conoce. Los guardias no se comunican por un canal secreto: avisar es un evento visible (el "!").

---

## Sonido

El oído es un segundo cono, sin forma: un **radio**. Cada fuente de ruido (paso, objeto lanzado) tiene un radio; los guardias dentro de ese radio pasan a Sospecha y van al origen (GMTK, 2020). Splinter Cell envía el ruido como evento con distancia y prioridad, y mide la distancia **a lo largo del camino**, no en línea recta, así que las paredes lo amortiguan (Thompson, 2020).

```txt
RADIO DE RUIDO    caminar: r = v_caminar × 1 s      correr: r = v_correr × 1 s      silencioso: 0
OBJETO LANZADO    radio fijo (≈ 4 u), con alcance máximo del lanzamiento
DISTANCIA         medida por camino en la grilla (BFS limitado por el radio), no en línea recta
EFECTO            el ruido abre la duda (Sospecha); solo la vista confirma (Alerta)
```

**El ruido nunca alerta directo.** Esa regla (*destilación propia*) separa los canales: oír = "algo pasó"; ver = "es él". Un guardia que oye pasos a su espalda se da vuelta, y entonces ve o no ve. Eso deja una última chance al jugador.

El objeto lanzado es el verbo de mouse: clic en la grilla, alcance máximo `R_tiro`, cantidad limitada por nivel. **Limitarlo es obligatorio**: sin límite el distractor es una estrategia dominante que aplana el bucle de observar y actuar (GMTK, 2020, sobre los gadgets).

---

## Legibilidad del sistema

El tema del libro. Hay dos filosofías, y las dos sirven si son consistentes:

- **Transparencia total** (Mark of the Ninja): se ven los conos, la luz sobre el personaje, el anillo de ruido *antes* de hacer el ruido. Anderson dice que los sigilos suelen enseñar sus reglas por el fracaso y que querían llegar antes al juego proactivo (Alexander, 2012). El jugador se siente depredador y planea trampas.
- **Ambigüedad** (terror, p. ej. Alien: Isolation): se esconde la percepción del enemigo para dar miedo (GMTK, 2020). Funciona cuando el miedo es el objetivo, y requiere que el jugador acepte no leer.

Para un portfolio, una pieza de diseño que se corre sin explicación, **el baseline va con transparencia**. La cantidad mínima de información para que sea legible:

```txt
POR GUARDIA     cono dibujado + medidor + marca de estado
DEL JUGADOR     estado propio visible (silencioso / caminando / corriendo) + anillo de ruido
DE LA SALA      cuenta de evasión + objetivo + objetos lanzables restantes
```

**Thief cuenta el costo de no hacerlo:** tras año y medio de desarrollo su sigilo todavía no funcionaba bien, y apareció un indicador de visibilidad en pantalla, la gema de luz (Kerr, 2018, sobre Paul Neurath). Que lo que faltaba era legibilidad es nuestra lectura: la fuente cuenta el hecho, no ese diagnóstico. `09_Onboarding_y_tutorial` sirve para presentar de a uno los elementos, en vez de todos en la primera sala.

---

## Patrullas y la ventana segura

La contraparte del hueco del runner. Para un tramo de ruta de largo `L`, la ventana segura es el tiempo en que *ningún cono lo cubre*.

```txt
tiempo de cruce      t_cruce = L / v          (v = velocidad con la que se recorre: caminando o silencioso)
ventana segura       W = tiempo del ciclo de patrulla P en que el tramo no está en ningún cono
CONDICIÓN            W ≥ 1.5 × t_cruce    en la ruta base (margen destilación propia, a calibrar)
CICLO                P ≤ 12 s             para que el jugador vea una vuelta entera desde un refugio
```

- **Aritmética de la ruta base:** un tramo de 6 u caminando a 3 u/s dura 2 s; la ventana mínima es 3 s. Con silencioso (1.5 u/s): 4 s de cruce y 6 s de ventana.
- **El ruido no entra en `W`.** La ventana se calcula solo con los conos; caminar a menos de 3 u de un guardia lo pone en Sospecha aunque el tramo esté fuera de su cono. Las rutas base se trazan a más de 3 u de los guardias, o se cruzan en silencioso (radio 0).
- **Solapes.** Si dos conos cubren el mismo tramo con fases distintas, la ventana es la parte donde *ninguno* lo cubre: se calcula, no se estima.
- **Refugios.** Cada sala tiene lugares donde el jugador espera sin estar en ningún cono. Es lo que permite observar (GMTK, 2020, sobre los espacios de refugio).
- **Cruzar un cono de frente nunca es la ruta.** A distancia 4 u del guardia el ancho del cono es ≈ 4.6 u: caminando son ≈ 1.54 s, más que el llenado lejano (1.4 s). Caminando o en silencioso (3.08 s contra 2.1 s de llenado lejano en silencioso) es detección segura, a propósito. **Excepción de cerca:** en la banda cercana el cruce caminando dura `2·d·tan 30° / 3 = 0.385·d` s, y eso es menor que `t_cercano` (0.7 s) si `d < ≈ 1.8 u`: ahí no se llega a Alerta, aunque el medidor pasa `f_aviso` (el guardia se frena) y el ruido de caminar (radio 3 u) lo pone en Sospecha. Si se quiere cerrar del todo, se alarga `t_cercano` o se agrega una zona de peligro (ver *Variantes*): decisión de playtest. Corriendo, el cruce dura 4.62 / 6 ≈ 0.77 s, menos que 1.4 s: no llena el medidor, pero hace ruido (radio 6 u > 4 u) y pone al guardia en Sospecha. Cruzar el cono es una salida de emergencia, no una ruta.
- **La dificultad crece por ventanas** (más cortas, más conos solapados, menos refugios), no por guardias más rápidos. `06_Dificultad_y_curva`

---

## Baseline de parámetros

Punto de partida, no dogma. En **tiempo** y relaciones. Unidad de longitud: `u` = una celda de grilla; sala de referencia 20 × 15 u. Todo, *destilación propia, a calibrar en playtest*, salvo lo indicado.

| Parámetro | Relación | Baseline | Nota |
|-----------|----------|----------|------|
| Velocidad caminando | `v` | 3 u/s | cruzar la sala (20 u) ≈ 6.7 s |
| Velocidad silencioso | `0.5 · v` | 1.5 u/s | radio de ruido 0 |
| Velocidad corriendo | `2 · v` | 6 u/s | radio de ruido = 6 u |
| Guardia patrullando | `0.6 · v` | 1.8 u/s | más lento que el jugador |
| Guardia persiguiendo | `v < v_pers < v_correr` | `1.5 · v` = 4.5 u/s | el que corre se escapa por 1.5 u/s |
| Alcance del cono | `R / v` ≈ tiempo de recorrerlo | R = 5 u (≈ 1.67 s caminando) | — |
| Semiángulo | `α` | 30° (cono de 60°) | ancho en `R` = `2·R·tan α` ≈ 5.8 u |
| Banda cercana | `d ≤ R/2` | ≤ 2.5 u | llena al doble de velocidad |
| Llenado cercano | `t_cercano` | 0.7 s | `t_cercano ≥ 2 × reacción visual (0.331 s)` |
| Llenado lejano | `t_lejano = 2 · t_cercano` | 1.4 s | — |
| Postura silenciosa | multiplica el tiempo de llenado ×1.5 | cercano 1.05 s | **nunca por debajo de `t_cercano`** |
| Umbral de aviso | `(1 − f_aviso) · t_cercano ≥ 1.2 × 0.331 s` | `f_aviso` = 0.4 → 0.42 s ≥ 0.40 s | el guardia se detiene |
| Bajada del medidor | `t_baja = 1.5 · t_lejano` | 2.1 s de lleno a 0 | más lento que la subida |
| Ruido caminando | `1 s × v` | 3 u | — |
| Ruido corriendo | `1 s × v_correr` | 6 u | — |
| Objeto lanzado | fijo | 4 u, 3 por nivel | — |
| `t_barrido` | — | 3 s | mirar alrededor al llegar |
| `T_perdido` | — | 0.8 s | ≈ 2.4 × reacción visual (0.331 s); filtra esquinas |
| Cuenta de evasión | `T_ev ≥ d_max / v_pers + t_barrido` | sala 20 × 15: diagonal 25 u → 25 / 4.5 ≈ 5.6 s + 3 s = 8.6 s → **`T_ev` = 10 s** | si la sala cambia de tamaño, se recalcula |
| Radio de captura | — | ≈ 0.8 u | contacto de cuerpo |
| Reintento | checkpoint al entrar a la sala | control en ≤ 1.5 s | `15_Muerte_reintento_y_checkpoints` |
| Ciclo de patrulla | `P` | ≤ 12 s | ver *Patrullas* |
| Ventana segura (ruta base) | `W ≥ 1.5 · L / v` | tramo de 6 u: 3 s | ver *Patrullas* |

El único número con fuente: **reacción visual simple ≈ 331 ms** (Shelton y Kumar, 2010; 14 sujetos, tarea simple). Una decisión de sigilo no es una reacción simple, por eso la relación pide 1.2 a 2 veces ese valor, y no una igualdad.

**Chequeo cruzado, hecho:** `v < 4.5 < 6` ✓ · `t_lejano = 2·t_cercano = 1.4` ✓ · silencioso: 0.7 × 1.5 = 1.05 ≥ 0.7 ✓ · aviso: 0.6 × 0.7 = 0.42 ≥ 0.397 ✓ · diagonal √(20²+15²) = 25 ✓ · 25 / 4.5 + 3 = 8.56 ≤ 10 ✓ · 2·5·tan 30° = 5.77 ✓ · cono a 4 u: 2·4·tan 30° = 4.62 u → 1.54 s a 3 u/s > 1.4 s ✓.

---

## Variantes, y qué parte del baseline reescribe cada una

Una variante no le agrega una fila al baseline: **lo pone entero bajo sospecha.**

| Variante | Referente | Qué reescribe |
|----------|-----------|---------------|
| **Guardias de cuatro direcciones, por pantalla** | Metal Gear (1987): visión al frente, alerta que solo afecta la pantalla | La forma del cono (4 orientaciones), la alerta de sala y el escape cambiando de pantalla: ruta de salida en vez de evasión con cuenta |
| **Alerta global con refuerzos** | el "!!" de Metal Gear (cámara, sensor, disparo) | `T_ev`, la table-stake 8 y la ventana segura: llegan guardias nuevos |
| **Radar de conos** | MGS: radar con los conos de los guardias, que se apaga en Alerta y Evasión (Wikipedia, *MGS*) | La legibilidad: el cono sale de la sala y pasa a un HUD; hay que rediseñar el aviso |
| **Transparencia total + trampas** | Mark of the Ninja | Detección casi binaria: `t_fill → 0`, que rompe la table-stake 3; el cono tiene que ser 100 % legible y el giro del guardia predecible |
| **Luz y sombra** | Thief: indicador de visibilidad (Kerr, 2018) | Agrega una variable al medidor: el tiempo de llenado depende de la luz; la ventana segura se calcula también con la luz |
| **Tres zonas** | Shadow Tactics (GMTK, 2020): zona de peligro, zona solo agachado, refugio | Las bandas del cono: se cambia la banda cercana por una zona de peligro con detección casi inmediata |
| **Disfraz** | Hitman (GMTK, 2020) | La ocultación pasa de espacial a social: el cono ve, pero no "lee" al jugador mientras el disfraz valga |

---

## Definición de Terminado

Checklist del género. Se corre **sobre el juego corriendo**, no sobre el código. `03_Definicion_de_terminado`

```txt
PERCEPCIÓN Y LECTURA
[ ] Veo el cono de cada guardia, y la parte que tapa una pared no se pinta
[ ] El cono dibujado coincide con donde me detecta (lo pruebo con el centro del cuerpo sobre el borde; solo el roce de un costado puede no detectar)
[ ] Al entrar al cono veo un medidor que se llena, y puedo salir antes de que llene
[ ] Antes de que el medidor llegue a 1 el guardia se detiene y se gira: tengo aviso
[ ] Reconozco de un vistazo patrulla, sospecha, alerta y evasión, sin leer texto
[ ] Veo el radio de mi ruido al caminar y al correr, y desaparece al ir silencioso

PATRULLAS Y SALA
[ ] Puedo mirar una vuelta entera de cada guardia desde un lugar donde no me ven
[ ] Cada sala tiene una ruta que se pasa caminando sin ser visto
[ ] Nunca hay una sala que me obligue a ser detectado

ALERTA Y EVASIÓN
[ ] Si me ven, los guardias de la sala me persiguen y los de otras no se enteran
[ ] Corriendo me escapo del guardia; caminando no
[ ] Si pierdo a los guardias, veo la cuenta de evasión y al llegar a 0 vuelven a patrullar
[ ] Si me ven de nuevo durante la evasión, vuelvo a Alerta
[ ] El ruido solo hace que investiguen; para alertarse me tienen que ver

PARTIDA Y ESTADOS
[ ] Si me alcanzan, se ve que me atraparon y quién, y reintento en menos de un segundo y medio
[ ] Reintento en la misma sala, no desde el principio
[ ] El juego va igual de rápido en un monitor de 60 Hz y en uno de 120+ Hz
[ ] Si cambio de pestaña el juego se pausa y los guardias no avanzan

FEEL
[ ] Los cambios de estado suenan distinto entre sí y distinto del paso
[ ] Los conos y medidores no los tapa ningún efecto
```

Un stealth que dibuja conos y deja caminar pero no tilda **Percepción y lectura** y **Alerta y evasión** es el 4/10 de la Ley #1: la demo técnica que obliga a gastar prompts en trabajo remedial.

---

## Aplicación

- **Cuándo se abre este libro:** ante cualquier pedido de sigilo, "como Metal Gear", "que los guardias te vean", juego de infiltración top-down, o conos de visión. Producción lo carga al escribir el `RQ`; Game Design lo cruza con el checklist al escribir el `GDS`; Level Design usa la ventana segura y las bandas del cono como medidas del espacio, porque en un sigilo la ruta de guardias es el nivel. `12_Pacing_y_estructura`
- **Qué trae la IA por default sin que se lo pidan:** las 12 table-stakes, la máquina de cuatro estados, el medidor con aviso, el sonido con radio visible, la ventana segura calculada, `T_ev` derivado de la sala y la Definición de Terminado completa.
- **Qué NO decide este libro:** el tema, el arte, la narrativa (radio, Codec), si hay combate o armas, la plataforma. Eso lo declara el `RQ`.

### Si va al portfolio web

HTML + CSS + JS sin frameworks, un `<canvas>` 2D, teclado y mouse, escritorio. **Alcance mínimo sólido:**

- **Grilla de 20 × 15 celdas**, salas definidas como matriz de paredes. Colisión del jugador contra la grilla. `02_Colision_y_consulta_espacial`
- **Paso fijo a 60 Hz** con acumulador, todas las duraciones del baseline en segundos de simulación; pausa con `visibilitychange` y `blur`. `01_Bucle_de_simulacion`
- **Entrada:** WASD o flechas para moverse; una tecla mantenida (Shift) para silencioso; **clic** para lanzar un objeto en la celda apuntada; Enter o R para reintentar. `10_Input_y_respuesta`
- **Dos tipos de guardia:** el que patrulla waypoints y el centinela que gira entre dos ángulos y se queda en cada uno. Sin armas ni combate: capturar es tocar.
- **Percepción:** cono con raycast a 3 puntos del jugador (centro y dos laterales; visto si ven 2) contra la grilla, BFS para el ruido, medidor, cuatro estados. Dibujar el cono como polígono con barrido de rayos (Patel, Red Blob Games).
- **Tres salas** con una sola idea cada una: un guardia con ventana ancha; dos guardias con conos solapados y fases distintas; centinela más patrulla. Checkpoint al entrar a cada sala. `06_Dificultad_y_curva`, `09_Onboarding_y_tutorial`
- **HUD mínimo:** medidor por guardia, cuenta de evasión, objetos restantes, marca de estado. `14_UI_HUD_y_menus`
- **Persistencia:** `localStorage` solo para la sala alcanzada, con `try/catch`.

---

## Límites

- Es un libro de **experiencia y de relaciones**, sin medición. No se corrió ningún juego ni bot: todos los tiempos del baseline son destilación propia, coherentes entre sí (chequeo hecho), **no validados con jugadores**.
- **No verificado:** (a) cuántos segundos dura la cuenta de Evasión en MGS ni los timers de Alerta de ningún Metal Gear: las fuentes leídas no los dan; (b) las cifras de Splinter Cell: Blacklist se leyeron de segunda mano, no en la charla de Walsh (GDC 2014), que es de acceso pagado: los 8 puntos de rayo (ocho huesos) vienen solo de Thompson (2020), y la mitad de audición fuera de pantalla viene solo de GMTK (2020); Thompson dice que la audición es más débil fuera de pantalla pero no da cuánto; (c) la afirmación de The Last of Us (rayo al pecho) viene solo de GMTK; (d) cuántos soldados hay que vencer para terminar el "!!" de Metal Gear: la fuente no lo dice; (e) cómo calcula Thief cada nivel de visibilidad: Kerr (2018) y la wiki no dan umbrales.
- **Las lecturas de las páginas web se hicieron a través de un extractor automático** (WebFetch), no leyendo el texto completo en el navegador: son resúmenes, y las citas son conceptuales.
- La reacción de 331 ms es de una tarea simple con 14 sujetos; una decisión de sigilo es más lenta. El baseline pide 1.2 a 2 veces ese valor, que es una hipótesis.
- **Abierto:** la captura se define solo desde Alerta (contacto, radio 0.8 u); qué pasa si un guardia en Patrulla, Sospecha o Evasión toca al jugador no está decidido. Tampoco se fijó si el medidor acumula parcialmente entre salidas y reentradas al cono más allá de la regla de bajada.
- **No cubierto:** IA de grupo (comunicación entre guardias, flanqueo), sigilo 3D, niveles abiertos, cadáveres y memoria del entorno (solo mencionados), accesibilidad (daltonismo en los colores de estado), generación procedural de patrullas.

---

## Fuentes

Todas consultadas el 2026-10-13, salvo Walsh (no leída, ver su entrada). Verificados contra la fuente ese día: autor y fecha de Alexander, Kerr y Thompson; n = 14 y 331 ms de Shelton y Kumar; el "!" y "!!" de Metal Gear; el radar y la cuenta de evasión de MGS. Licencias: lo que no es de licencia abierta se usó solo como concepto + cita, sin texto.

- Leigh Alexander (2012-08-02), *Reinventing stealth in 2D with Mark of the Ninja*, Game Developer — https://gamedeveloper.com/design/reinventing-stealth-in-2d-with-i-mark-of-the-ninja-i- . Anillo de ruido, legibilidad, anticipación vs reacción. Copyright del medio: concepto + cita.
- Chris Kerr (2018-02-27), *Building the original Thief's revolutionary stealth system*, Game Developer, sobre una entrevista de Ars Technica a Paul Neurath — https://www.gamedeveloper.com/design/building-the-original-i-thief-s-i-revolutionary-stealth-system . La gema de luz. Copyright: concepto + cita.
- Tommy Thompson (2020-06-03), artículo sobre *Splinter Cell: Blacklist* (cita a Martin Walsh, GDC 2014), Game Developer — https://gamedeveloper.com/design/bringing-balance-to-stealth-ai-in-splinter-cell-blacklist . Formas de visión, rayos al esqueleto, sonido por camino. Copyright: concepto + cita.
- Martin Walsh (2014), *Modeling AI Perception and Awareness in Splinter Cell: Blacklist*, GDC Vault — https://www.gdcvault.com/play/1020436/Modeling-AI-Perception-and-Awareness . **NO LEÍDA:** solo el resumen público; la charla es de acceso pagado. Sus contenidos entran solo de segunda mano, vía Thompson (2020).
- Game Maker's Toolkit (canal; fecha 2020-03-25 según TheTVDB, "Originally Aired"), *How Stealth Game Guards See and Hear | School of Stealth Part 1*, video; leído por subtítulos de Amara (la transcripción, no la página de registro) — https://amara.org/subtitles/4SwBdOk0E4LH/en/1/download/How%20Stealth%20Game%20Guards%20See%20and%20Hear%20%20School%20of%20Stealth%20Part%201.en.txt ; ficha: https://thetvdb.com/series/game-makers-toolkit/episodes/7653041 . **Autoría inferida:** se atribuye al canal a partir de Tildes y TheTVDB (TVDB no acredita guionista); no se confirmó en YouTube ni el autor individual. Y *The Five Types of Stealth Game Gadget | Part 2* — https://amara.org/subtitles/WhRzE9B9SAIb/en/1/download/The%20Five%20Types%20of%20Stealth%20Game%20Gadget%20%20School%20of%20Stealth%20Part%202.en.txt . Conos en capas, medidor, oído, refugios, gadgets. Copyright del autor: concepto + cita.
- Wikipedia, *Metal Gear (video game)* — https://en.wikipedia.org/wiki/Metal_Gear_(video_game) ; *Metal Gear Solid (1998 video game)* — https://en.wikipedia.org/wiki/Metal_Gear_Solid_(1998_video_game) . Alerta de pantalla vs refuerzos, radar de conos, evasión. CC BY-SA: concepto + cita.
- Metal Gear Wiki (Fandom), *Enemy status* — https://metalgear.fandom.com/wiki/Enemy_status ; *Exclamation point* — https://metalgear.fandom.com/wiki/Exclamation_point . Estados por juego y convención del "!". CC BY-SA, de fans: fuente secundaria, solo concepto.
- Amit J. Patel (Red Blob Games, creado 2012, actualizado 2020), *2d visibility* — https://www.redblobgames.com/articles/visibility/ . Cálculo del área visible en 2D. Implementación de referencia Apache 2.0; el texto sin licencia declarada: concepto + cita.
- Shelton y Kumar (2010), *Comparison between Auditory and Visual Simple Reaction Times*, Neuroscience & Medicine 1(1) — https://www.scirp.org/html/4-2400003_2689.htm . Reacción visual ≈ 331 ms, auditiva ≈ 284 ms, n = 14.
- Thief Wiki (Fandom), *Light Gem* — https://thief.fandom.com/wiki/Light_Gem . Ubicación y escala de color del indicador. CC BY-SA: solo concepto.

Del vault: `01_Loop_de_experiencia`, `02_Game_feel`, `03_Definicion_de_terminado`, `06_Dificultad_y_curva`, `09_Onboarding_y_tutorial`, `10_Input_y_respuesta`, `11_Camara_y_encuadre`, `12_Pacing_y_estructura`, `14_UI_HUD_y_menus`, `15_Muerte_reintento_y_checkpoints`, `16_Audio_como_gameplay`, `01_Bucle_de_simulacion`, `02_Colision_y_consulta_espacial`, `05_Endless_runner`.

**Cobertura declarada:** de las 12 table-stakes, **seis** —1, 2, 3, 4, 6 y 8— nombran su sustento en una fuente externa (el 3 con el único número fuente). Las 5, 7, 9, 10, 11 y 12 son destilación propia o cruce con el vault. **Ningún número del baseline salvo la reacción visual tiene fuente; ninguna table-stake se validó con jugadores ni con un juego propio.**

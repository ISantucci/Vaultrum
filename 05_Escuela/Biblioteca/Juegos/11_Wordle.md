---
tipo: juego
genero: Puzzle
subtipo: Puzzle de palabras diario con feedback por letra (un intento por día, el mismo puzzle para todos)
estado: En validación
mision: EST-022_Mision_Lote_Juegos_Web_y_Sigilo
cruza: 01_Loop_de_experiencia, 02_Game_feel, 03_Definicion_de_terminado, 06_Dificultad_y_curva, 08_Progresion_y_recompensa, 09_Onboarding_y_tutorial, 10_Input_y_respuesta, 12_Pacing_y_estructura, 14_UI_HUD_y_menus, 15_Muerte_reintento_y_checkpoints
---

# Libro 11 — Wordle

> Undécimo libro del estante de Juegos. Género: Puzzle / palabras con feedback por letra.
> Lo **transversal** vive en los Fundamentos. Acá va lo **específico**: qué pasa cuando el puzzle se agota en una sola partida por día, y el juego entero se apoya en una regla de colores que parece trivial y no lo es.
> **IP:** *Wordle*, creado por Josh Wardle y comprado por The New York Times en 2022. **El nombre y la marca son protegibles; las reglas no**: un clon va con otro nombre, otro arte y su propia lista de palabras. Este libro no reproduce la lista de palabras de Wordle ni código ajeno: solo conceptos destilados + cita.
> **Medido:** nada de este libro salió de jugar ni de correr código propio. Los números son de las fuentes leídas (con fecha de consulta 2026-10-13) o aritmética verificable; lo demás dice "destilación propia, a calibrar".

---

## Índice del libro

- Loop de experiencia
- Table-stakes
- Juice / game feel
- La regla de colores con letras repetidas
- Dos listas de palabras
- El puzzle del día, igual para todos
- Compartir sin spoilers
- Modo difícil
- Accesibilidad
- Racha y estadísticas
- Baseline de parámetros
- Variantes, y qué parte del baseline reescribe cada una
- Definición de Terminado
- Aplicación
- Límites
- Fuentes

---

## Loop de experiencia

```txt
LOOP ATÓMICO    (≈5–20 s)       pensar una palabra → tipearla → enviar → leer cinco colores
LOOP DE PARTIDA (≈2–10 min)     hasta seis intentos: cada color descarta candidatas → se resuelve o se pierde
LOOP DE SESIÓN  (1 por día)     jugar → compartir la grilla → volver mañana
```

**El límite de una por día es el diseño, no una restricción técnica.** Wardle contó que lo tomó de la escasez del Spelling Bee del NYT, que deja con ganas de más, y que apuntó a unos tres minutos diarios, sin notificaciones, anuncios ni pedidos de dinero. `Boston.com / AP, 2022` El juego no compite por tiempo de pantalla: compite por **hábito**. La sesión no se extiende: se espera. Esto invierte `01_Loop_de_experiencia`: el "una más" no existe, el motor del regreso es el ritual del día siguiente y la comparación social del día de hoy. `12_Pacing_y_estructura`

**Qué lo hace juego:** el objetivo impuesto es hallar una palabra en seis intentos; el obstáculo aceptado es que cada intento da feedback y consume uno. **Dónde vive la tensión:** en la deducción, el jugador siempre sabe qué hacer (probar una palabra) y lo que no sabe es *cuál*; cada color angosta el espacio. Y en el último intento, donde la derrota es real. `15_Muerte_reintento_y_checkpoints`: acá el reintento está **prohibido por diseño** hasta mañana, y eso pone todo el peso en que la partida perdida se sienta justa (ver *Dos listas de palabras*).

---

## Table-stakes

| # | Table-stake | Por qué es obligatorio |
|---|-------------|------------------------|
| 1 | **Un solo puzzle por día, igual para todos** | Es la escasez y es lo que hace comparables los resultados. Sin eso es una app de palabras más. Ver *El puzzle del día* |
| 2 | **Feedback de tres estados por letra** (lugar correcto / está en otro lugar / no está) | Es el único canal de información del jugador. Tiene que ser correcto también con letras repetidas: ver sección propia |
| 3 | **Solo se aceptan palabras reales, y una palabra rechazada no gasta intento** | Sin validación el jugador tira letras para "mirar" los colores, y el juego deja de ser de palabras. Rechazar sin costo hace que un error de tipeo no cueste la partida |
| 4 | **Lista de respuestas corta y familiar, lista de permitidas larga** | La derrota solo se siente justa si la respuesta era una palabra que el jugador pudo conocer. Ver *Dos listas* |
| 5 | **Teclado físico y virtual, con el estado de cada letra pintado en las teclas** | El teclado es el segundo tablero: le ahorra al jugador llevar la cuenta de memoria. `10_Input_y_respuesta`, `14_UI_HUD_y_menus` |
| 6 | **Revelado en el orden de las letras, de izquierda a derecha, y el input bloqueado mientras dura** | El revelado es el momento del juego; si se salta o se superpone con el siguiente tipeo, se pierde |
| 7 | **El estado de la partida sobrevive a cerrar y reabrir** | Un puzzle por día no se puede perder por cerrar una pestaña: no hay reintento. Ver *Racha y estadísticas* |
| 8 | **Pantalla de fin con la respuesta, la grilla para compartir y las estadísticas** | Cierra el día. Si pierde, mostrar la palabra: es el único aprendizaje de la partida |
| 9 | **Compartir sin spoilers** | La grilla de colores cuenta cómo te fue sin decir qué palabra era. Ver sección propia |
| 10 | **Opción de alto contraste / daltonismo, y estado que no dependa solo del color** | El juego entero es una codificación por color. Ver *Accesibilidad* |
| 11 | **Aviso de "ya jugaste hoy" con cuenta regresiva al próximo puzzle** | El jugador que vuelve a las 10 de la mañana tiene que entender por qué no hay nada más, y cuándo vuelve el juego. `08_Progresion_y_recompensa` |
| 12 | **Instrucciones con un ejemplo resuelto, saltable** | La regla de colores se entiende en un ejemplo, no en un párrafo. `09_Onboarding_y_tutorial` |

---

## Juice / game feel

| Efecto | Qué comunica | Cuidado |
|--------|--------------|---------|
| **Revelado letra por letra con giro de la baldosa** | el momento de la verdad, una letra por vez | Es la suspensión del juego: escalonado corto (destilación propia: ≈100–300 ms entre letras, a calibrar). Demasiado lento irrita en el intento 6 al día 200 |
| **Temblor horizontal de la fila ante palabra inválida** | "no cuenta, no perdiste el intento" | Un temblor y un texto ("No está en la lista"); sin sonido agresivo. No debe parecer una penalidad |
| **Rebote de la baldosa al tipear una letra** | que la tecla entró | Más chico que el revelado. `02_Game_feel`, `10_Input_y_respuesta` |
| **Baile o salto de la fila ganadora** | resolviste | Es el cierre del día: el evento más grande, y corto |
| **Teclas que se pintan recién después del revelado** | no spoilear el color antes de terminar el giro | Si el teclado cambia antes, el revelado pierde su suspenso |

**Regla del género: nada se anima mientras el jugador piensa.** El tablero está quieto entre intentos; el juice vive en los dos momentos de cierre (revelado, fin del día). *Destilación propia.*

---

## La regla de colores con letras repetidas

Es el punto donde más implementaciones fallan. Las dos reglas, según el análisis consultado: **(1)** un verde le gana a un amarillo; **(2)** cada letra marcada como presente (verde o amarilla) tiene que corresponder a **una copia distinta** de esa letra en la respuesta. `wordle-boss, Algorithm Overview`

**Algoritmo de dos pasadas** (la forma estándar que cumple las dos reglas):

```txt
Entrada: respuesta, intento (misma longitud). Salida: un estado por posición.
0. disponibles = conteo de cada letra de la RESPUESTA
1. PASADA 1 (verdes): para cada posición i, si intento[i] == respuesta[i]:
        estado[i] = verde;  disponibles[letra] -= 1
2. PASADA 2 (amarillos): para cada posición i que NO es verde, de izquierda a derecha:
        si disponibles[intento[i]] > 0:  estado[i] = amarillo;  disponibles[letra] -= 1
        si no:                           estado[i] = gris
```

**El caso que rompen las implementaciones ingenuas.** La ingenua marca amarillo a toda letra del intento que *aparece en algún lugar* de la respuesta, en una sola pasada. Ejemplo de la fuente: respuesta con una sola E, intento con dos E. Correcto: la **primera E** del intento que no sea verde se pinta amarilla y la **segunda queda gris**, porque la respuesta no tiene una segunda E. La ingenua pinta las dos amarillas y le miente al jugador diciéndole que hay dos. Segundo caso, el inverso: si la **segunda** E del intento cae en su lugar exacto, tiene que ser **verde**, y la primera, que antes de la pasada 1 parecía candidata a amarilla, **queda gris**. Por eso los verdes se resuelven primero y consumen su copia: una sola pasada de izquierda a derecha le gasta la copia a la E equivocada.

Un caso de prueba hecho a mano para este libro (destilación propia): respuesta `PERRO`, intento `ERROR`. Pasada 1: solo la R de la posición 3 coincide, verde. Quedan disponibles P, E, O y una R. Pasada 2: E amarilla, R (posición 2) amarilla, O amarilla, y la R final **gris**, porque las dos R de la respuesta ya están usadas. Resultado: amarillo, amarillo, verde, amarillo, gris. La implementación ingenua pinta la última R amarilla (tres R marcadas contra dos que hay). Esa es la invariante que sirve de test, y se puede correr contra todas las parejas de una lista chica:

```txt
Invariante a testear:  para cada letra L:   #(verdes + amarillos de L en el intento)  ≤  #(L en la respuesta)
Y además:              toda posición donde intento[i] == respuesta[i] es verde (nunca amarilla ni gris)
```

---

## Dos listas de palabras

| Lista | Para qué | Tamaño en Wordle |
|-------|----------|------------------|
| **Respuestas** | de acá sale el puzzle del día | 2.315 originales; 2.309 hoy según Wikipedia (la misma página dice que hacia julio de 2022 se habían sacado siete, lo que daría 2.308: la fuente no concilia las cifras) |
| **Permitidas** | todo lo que se acepta como intento | 12.972 según una nota de análisis que cita la lista oficial (`That's Maths`); Wikipedia no da el número |

**Por qué separadas.** Si se aceptan solo las respuestas, el jugador puede *deducir* palabras por exclusión de la lista, y los intentos de exploración (palabras raras con letras útiles) quedan prohibidos. Si se usa una sola lista larga, la respuesta del día puede ser una palabra oscura y la derrota se siente injusta. La separación resuelve las dos cosas a la vez: **la respuesta es familiar, el intento es libre.** El proceso de Wardle fue ese: partió de unas 12.000 palabras de cinco letras y su pareja marcó las que conocía, lo que dejó unas 2.500 (según AP; Wikipedia dice que la lista original tenía «aproximadamente 13.000» y que se filtró a «unas 2.000»: las fuentes no coinciden en los redondeos). `Boston.com / AP`

Curaduría posterior: el NYT sacó palabras consideradas ofensivas o inoportunas y variantes de ortografía británica, y desde noviembre de 2022 una editora revisa cada palabra. `Wikipedia` **La lista de respuestas es contenido editorial, no un diccionario**: se cura.

**Aritmética, solo lo que se afirma:** log₂ 2.315 ≈ 11,18 bits para identificar la respuesta entre las del día; log₂ 12.972 ≈ 13,66 bits sobre la lista de permitidas. Que la lista de permitidas sea mayor que la de respuestas hace que *muchos intentos válidos no puedan ser la solución*: son intentos de pura información.

---

## El puzzle del día, igual para todos

**Sin servidor, el puzzle se deriva del día.** El Wordle original corría entero en JavaScript del lado del cliente (Wikipedia; un análisis de ingeniería inversa no encontró pedidos de red al adivinar o ganar). `Medium, re-hacking Wordle` La forma, según las dos fuentes que la describen: una **fecha de origen fija** (19 de junio de 2021) y la fecha de hoy dan un **número de día**, y ese número indexa la lista de respuestas. Cómo se calcula el índice exacto (módulo, orden) **no lo describe ninguna fuente leída**: es destilación propia que sirva `índice = días desde el origen, con el módulo del largo de la lista`.

```txt
número de día = días enteros entre la fecha de origen y hoy      (el mismo para todos los que comparten fecha)
respuesta     = lista_de_respuestas[ orden_fijo[ número de día mod largo ] ]
```

**Consecuencias de diseño:** (1) la lista y su orden son parte del producto: si cambian, cambian las palabras de días ya jugados; (2) la respuesta viaja en el código, así que cualquiera puede mirarla: es aceptable en un juego casual, no en uno con ranking; (3) el número de día es lo que se muestra al compartir ("Wordle 196", en el ejemplo de Wikipedia). Tras la compra, el NYT movió la correspondencia fecha→palabra a sus servidores. `dinogame.gg` Un clon sin backend hereda el problema (2) y lo declara.

---

## Compartir sin spoilers

Al principio no se podía compartir; hacia mediados de diciembre de 2021 Wardle agregó un botón que copia una grilla de cuadrados de color, sin la palabra y sin vínculo al juego, porque pensó que se veía menos atractivo y prefería el misterio de la grilla. `Boston.com / AP` Wikipedia agrega que el formato lo inspiró un grupo de Nueva Zelanda que ya compartía algo parecido.

```txt
Wordle 196 4/6        ← nombre, número de día, intentos usados / máximo ("X/6" si se perdió: convención, no verificada)
⬛🟨⬛⬛⬛
🟩⬛🟨⬛⬛             ← una fila por intento, un cuadrado por letra, sin letras
🟩🟩🟩⬛🟩
🟩🟩🟩🟩🟩
```

Qué cuenta: **la forma de la deducción, sin su contenido.** Es un texto plano (no una imagen), así que viaja por cualquier chat; el número de día permite comparar con otros que jugaron el mismo puzzle. 6 filas × 5 columnas = 30 cuadrados como máximo. Dos cuidados: el modo de alto contraste cambia los colores, y la grilla compartida tiene que cambiar con él para no confundir al lector daltónico (destilación propia); y copiar al portapapeles puede fallar sin permiso, así que hace falta un camino alternativo (texto seleccionable). `14_UI_HUD_y_menus`

---

## Modo difícil

La regla (Wikipedia): cada letra revelada, verde o amarilla, **tiene que usarse** en los intentos siguientes. Lo que implementa: las verdes, en su lugar; las amarillas, en cualquier posición de la palabra. Qué cambia: prohíbe el intento "de exploración" que descarta letras sin acertar ninguna. Queda un juego más estrecho, más cercano al puro razonamiento y con menos margen para el azar útil. `06_Dificultad_y_curva`

Reglas de implementación (destilación propia): es opcional y se elige **antes del primer intento** del día (cambiarlo a mitad de partida permitiría recibir ayuda y volver atrás); el error se dice con un mensaje que nombra la letra que falta ("La palabra tiene que usar la A") y, como la palabra inválida, **no gasta el intento**. No es "más difícil" en el sentido de un parámetro numérico: es otra restricción sobre el mismo juego.

---

## Accesibilidad

El juego codifica todo en dos colores que se distinguen mal: para un jugador daltónico, verde y amarillo pueden verse parecidos, y cuando aparece un solo color no se sabe cuál es. La crítica es que el modo de alto contraste existe (cambia verde y amarillo por naranja y azul, según Wikipedia) pero está escondido en los ajustes. `Bill Fischer, Substack` La lección de diseño es la del `14_UI_HUD_y_menus`: **el estado no puede vivir solo en el color.**

Mínimos (destilación propia, cruzados con `14_UI_HUD_y_menus`): paleta alternativa de alto contraste **a un toque, y visible en el tutorial**; una segunda señal en cada baldosa (un ícono o un patrón chico para "en lugar" y "en otro lugar"); y `aria-label` por baldosa ("A, correcta", "R, está en otro lugar") para lector de pantalla. Contraste mínimo de texto sobre baldosa: medirlo con la herramienta de contraste de `14_UI_HUD_y_menus`, no a ojo. Tema oscuro disponible (existe en el original, Wikipedia).

---

## Racha y estadísticas

Wordle conserva estadísticas entre días: Wikipedia confirma las rachas diarias y que las estadísticas se trasladaron en la migración; el resto del conjunto mínimo (partidas, porcentaje de victorias, racha máxima, distribución de en qué intento se resolvió) es destilación propia, no leído en una fuente. La racha es **la memoria del ritual**: castiga faltar un día, y eso es un arma de doble filo. Cuando el NYT migró el juego, algunos jugadores reportaron que sus rachas se reiniciaron (Wikipedia): perder una racha de cientos de días por un error técnico es lo peor que le puede pasar al ritual. `08_Progresion_y_recompensa`

```txt
Estado mínimo a persistir:  { partidas, victorias, rachaActual, rachaMax, distribución[1..N], últimoDíaJugado, intentosDeHoy[], resultadoDeHoy }
```

Reglas (destilación propia): la racha se corta si entre el último día jugado y hoy pasó **más de un número de día** (se saltó al menos un día), comparando números de día, no horas, y si la última partida se perdió (que perder también la corta en el original **no está verificado en fuente leída**: decisión propia); el estado de hoy y las estadísticas se guardan en cada intento, no al terminar; y el juego tiene que **vivir sin la persistencia** (modo privado, almacenamiento bloqueado): jugar sin guardar, avisando que la racha no se conserva.

---

## Baseline de parámetros

Relaciones, no números sueltos. El baseline original es **5 letras y 6 intentos** (la cantidad de intentos la da `That's Maths`).

| Parámetro | Relación | Baseline | Calibración |
|-----------|----------|----------|-------------|
| Largo de palabra `L` | resultados posibles por intento = `3^L` | 5 → 243 | 3⁵ = 243 (`That's Maths`; verificado) |
| Información máxima por intento | `log₂(3^L) = L · log₂ 3` | 5 letras → ≈7,92 bits | cota superior: ningún intento da más |
| Información necesaria `I` | `log₂(cantidad de respuestas posibles)` | 2.315 → ≈11,18 bits | aritmética sobre una cifra citada |
| Intentos mínimos teóricos | `⌈ I / (L · log₂ 3) ⌉` | 11,18 / 7,92 ≈ 1,41 → 2 | cota teórica: ningún jugador real llega |
| Intentos `N` ofrecidos | `N` sobre el mínimo teórico, con margen para el azar de la apertura | 6 (vs. 2 del mínimo) | Wordle; **el margen exacto es destilación propia, a calibrar** |
| Capacidad total contra necesidad | `N · L · log₂ 3 / I` | 6 · 7,92 / 11,18 ≈ 4,25 | aritmética: sobra capacidad; lo que limita es *qué intentos se pueden armar* |
| Respuestas contra permitidas | respuestas ⊂ permitidas | 2.315 en 12.972: ≈ 18% | aritmética sobre dos cifras citadas |
| Peso del azar | el primer intento da menos que la cota | un análisis mide ≈6,21 bits de información esperada para una buena apertura sobre **otra lista** (5.757 palabras) | `Towards Data Science`: la cifra **no es de la lista de Wordle**; sirve solo como orden de magnitud |
| Duración objetivo del día | sin notificaciones, sin sesión extendida | ≈3 minutos (intención de Wardle; el loop de partida admite 2–10 min, así que no es un tope) | Wardle (`AP`) |
| Revelado, ms por letra | ver *Juice* | ≈100–300 | destilación propia, a calibrar |

**La relación que ordena el libro:** `L`, la lista y `N` se eligen **juntos**. Más largo de palabra da más información por intento pero lista más grande; más intentos hacen más fácil y menos tenso. `06_Dificultad_y_curva`: la dificultad del puzzle diario no se ajusta por jugador: es fija, y la que sube y baja es la de cada palabra del día (una con letras repetidas o poco comunes es más difícil que una con letras frecuentes), que se cura al armar la lista. *Destilación propia.*

---

## Variantes, y qué parte del baseline reescribe cada una

Una variante no le agrega una fila al baseline: **lo pone entero bajo sospecha.**

| Variante | Qué reescribe |
|----------|---------------|
| **Español (tildes y ñ)** | La **normalización**: comparar sin tildes (`á`=`a`) pero **sin tocar la ñ**, que es otra letra: descomponer con Unicode y quitar todos los acentos combinantes la convierte en `n`. Decidir si la tilde cuenta como feedback o se ignora, y si el teclado la ofrece. La lista de respuestas se cura con otro criterio de "familiar" (rioplatense, voseo, verbos conjugados). No hay cifra verificada de tamaños en español: va en Límites |
| **Largo distinto** | `3^L` cambia: 4 letras → 81 resultados, ≈6,34 bits máximos; 6 letras → 729, ≈9,51 bits (aritmética). Cambia la lista, `N` y el ancho del tablero; con 6 letras en móvil, el tamaño de la baldosa |
| **Ilimitado / práctica** | **Rompe la escasez**: sin el límite diario desaparecen el ritual, la comparación y la racha como estaban. Pasa a ser un juego de sesión con `01_Loop_de_experiencia` común: hay "una más", y las estadísticas y la lista de respuestas se separan de las del día |
| **Multijugador** (misma palabra, quién la resuelve antes o en menos intentos) | Agrega **tiempo y presión**, que el original saca a propósito; reescribe el ritmo, el feedback (¿se ve el progreso del rival?) y el spoiler |
| **Quordle y similares** (varios tableros, un solo teclado) | Cada intento da feedback para **varias respuestas a la vez**: cambian `I`, `N` y el teclado (un estado por tablero en cada tecla). No leí fuente sobre sus reglas: ver Límites |

---

## Definición de Terminado

Checklist del género. Se corre **sobre el juego corriendo**.

```txt
REGLA DE COLORES
[ ] Con una letra repetida en el intento y una sola en la respuesta, solo una se pinta (la verde si hay verde)
[ ] Una letra verde nunca deja a otra copia de esa letra amarilla de más
[ ] Para toda letra: verdes + amarillas ≤ copias en la respuesta (probado con una tabla de casos)
[ ] El teclado muestra el mejor estado de cada letra (verde > amarilla > gris), sin pintar antes del revelado

PALABRAS
[ ] La respuesta del día sale de una lista curada, familiar; los intentos aceptan una lista más larga
[ ] Una palabra inexistente tiembla y NO gasta el intento
[ ] Con tildes y ñ (si es español) escribo la palabra natural y se compara bien; la ñ no se convierte en n

DÍA Y ESTADO
[ ] Hay un puzzle por día y es el mismo para todos los que juegan el mismo día
[ ] Si cierro y vuelvo, mi partida de hoy está como la dejé
[ ] Una vez terminada, veo cuándo hay otro puzzle y no puedo repetir hoy
[ ] Si el almacenamiento falla, el juego se puede jugar y avisa que no guarda
[ ] La racha se corta por días no jugados, no por horas

COMPARTIR Y ACCESIBILIDAD
[ ] La grilla copiada no contiene la palabra ni letras, y lleva el número de día
[ ] Si falla copiar, hay otra forma de sacar el texto
[ ] Hay modo de alto contraste, lo encuentro sin abrir ajustes escondidos, y cada baldosa tiene señal además del color
[ ] Se puede jugar entero con teclado físico y con teclado en pantalla

FEEL
[ ] El revelado es letra por letra, y no puedo tipear encima
[ ] Tipear una letra responde en el cuadro en que la aprieto
[ ] Ganar, perder y fin del día se sienten distintos
```

Un Wordle que revela colores pero falla el caso de letras repetidas o el estado tras recargar no está terminado: es la demo técnica que obliga a gastar prompts en trabajo remedial.

---

## Aplicación

- **Cuándo se abre este libro:** ante cualquier pedido de "un Wordle", juego de palabras diario, puzzle de una por día, o de "algo que se comparta con una grilla". Producción lo carga al escribir el `RQ`; Game Design lo cruza con el checklist de pilares; UI/UX diseña tablero, teclado y contraste.
- **Qué trae la IA por default sin que se lo pidan:** las 12 table-stakes, el algoritmo de dos pasadas con su invariante, las dos listas, el modo difícil como opción previa, la grilla sin spoilers y la Definición de Terminado.
- **Qué NO decide este libro:** el idioma ni el contenido de las listas, el nombre y el arte (que no pueden ser los de Wordle), si hay ranking, la monetización.

**Si va al portfolio web** (HTML + CSS + JS sin frameworks, sin motor):
- **Teclado físico + virtual**: `keydown` para letras, Enter y Retroceso, más botones en pantalla que disparan el mismo código. Un solo camino de entrada.
- **`localStorage` con try/catch** en cada lectura y escritura; si falla, se juega sin guardar y se avisa. Se guarda en cada intento.
- **Sin backend:** el puzzle sale del número de día y la lista va en el código. Costo declarado: **la respuesta es visible en el código fuente**, así que no hay ranking confiable y quien mire puede ver las respuestas de mañana. Para un portfolio es aceptable.
- **Zona horaria:** el "día" se define en **hora local del jugador** (cambia a la medianoche de su reloj). Costo declarado: dos jugadores en husos distintos pueden tener puzzles distintos durante unas horas, y un jugador que cambie la hora del dispositivo puede jugar de nuevo o saltear un día; la grilla compartida lleva el número de día justamente para saber si se comparó el mismo puzzle. El camino alternativo (UTC) elimina la divergencia pero hace que el puzzle cambie a una hora arbitraria para el jugador. La decisión de este libro es la local; destilación propia.
- **Nombre y lista propios:** un clon no se llama Wordle ni usa su lista.

## Límites

- Es un libro de **experiencia**. Cómo se arma el índice del día, la validación o la accesibilidad por ARIA es materia del `SOL`.
- **No verificado:** el cálculo exacto del índice diario del original (solo se leyó que usa una fecha de origen); si el original usaba la hora local del jugador (el libro lo toma como decisión propia); el formato "X/6" al perder; el reparto de colores exacto de cada cuadrado en cada modo; la cifra de 12.972 (viene de una nota que cita la lista, no de una lista que yo haya abierto); los tamaños de listas **en español** y las reglas, la cantidad de intentos y las listas de Quordle.
- **Las cifras de Wikipedia y AP no coinciden** en el tamaño de la lista filtrada (≈2.000 / ≈2.500, y ≈13.000 contra ≈12.000 de partida) ni en el de respuestas (2.309 / 2.315 − 7): se citan ambas.
- **No se leyó el video ni el texto de 3Blue1Brown**: la página consultada no traía el contenido y el análisis de información se apoya en dos notas que lo reseñan o lo replican con otra lista. Los bits de este libro son aritmética propia; la cifra de 6,21 bits es de otra lista.
- **No cubierto:** estrategia óptima de resolución (solvers), generación de listas en español, anti-trampa, y la historia de ingresos o de usuarios más allá de los números citados.
- **Ninguna table-stake se validó con jugadores ni con un clon propio.** El primer Wordle que pase por la cadena es la validación: si su `VE` encuentra un faltante, el libro se actualiza.

---

## Fuentes

Consultadas el 2026-10-13, sin ficha propia en la Biblioteca (a fichar):

- Wikipedia, *Wordle* — https://en.wikipedia.org/wiki/Wordle. Creador, historia, compra por el NYT (31 de enero de 2022, «siete cifras bajas»), lista de respuestas, curaduría, modo difícil, grilla, alto contraste, usuarios (90 el 1 de noviembre de 2021; más de 300.000 el 2 de enero de 2022)
- Associated Press vía Boston.com, *He made Wordle for his partner. Now it's an online hit* (2022-01-04) — https://www.boston.com/news/national-news/2022/01/04/he-made-wordle-for-his-partner-now-its-an-online-hit/. Wardle: origen, escasez, ≈3 minutos, listas, grilla de compartir
- wordle-boss, *Algorithm Overview* — https://wordle-boss.readthedocs.io/en/latest/algorithms.html. Las dos reglas de letras repetidas y sus ejemplos. La descripción de dos pasadas es inferencia del lector de la página, coincidente con la de `dinogame.gg`
- dinogame.gg, *How Wordle's Algorithm Actually Works* — https://dinogame.gg/blog/how-wordle-algorithm-works/. Dos pasadas, fecha de origen, traslado a servidores del NYT
- capJavert, *Re-hacking Wordle*, Medium — https://medium.com/@capJavert/re-hacking-wordle-114ba75d1344. Fecha de origen, lógica del lado del cliente
- That's Maths, *Why Waffle when One Wordle Do?* (2022-02-24) — https://thatsmaths.com/2022/02/24/why-waffle-when-one-wordle-do/. 2.315 y 12.972, 3⁵ = 243, seis intentos, reseña de 3Blue1Brown
- Towards Data Science, *Information Theory Applied to Wordle* — https://towardsdatascience.com/information-theory-applied-to-wordle-b63b34a6538e/. Bits y entropía sobre una lista de 5.757 palabras (no la de Wordle)
- Bill Fischer, *These 2 Wordle colors undermine color* (Substack) — https://billfischer.substack.com/p/these-2-wordle-colors-undermine-color. Verde y amarillo, daltonismo, alto contraste escondido
- 3Blue1Brown, *Solving Wordle using information theory* — https://www.3blue1brown.com/lessons/wordle. Citado como fuente de la teoría; **NO LEÍDA / a verificar**: la página consultada (Grant Sanderson, 2022-02-06) trae solo navegación y metadatos, sin el contenido (ver Límites)

No accesible: la nota del NYT sobre la compra (bloqueada). Del vault: `01_Loop_de_experiencia`, `02_Game_feel`, `03_Definicion_de_terminado`, `06_Dificultad_y_curva`, `08_Progresion_y_recompensa`, `09_Onboarding_y_tutorial`, `10_Input_y_respuesta`, `12_Pacing_y_estructura`, `14_UI_HUD_y_menus`, `15_Muerte_reintento_y_checkpoints`.

**Cobertura declarada:** de las 12 table-stakes, la 1, 4, 9 y 10 nombran calibración en una fuente externa; la 2 se apoya en la regla de colores; las demás (3, 5, 6, 7, 8, 11, 12) son **destilación propia**. Son también destilación propia: el algoritmo con su invariante, los parámetros de revelado, las reglas de modo difícil, racha y zona horaria, y la lectura de `N` contra `I`. **Ninguna se validó con jugadores.**

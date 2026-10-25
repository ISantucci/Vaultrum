---
tipo: medicina
estado: En la Biblioteca
mision: EST-024_Mision_Morfologia_del_movimiento
consume: Arte, solo al encargar, animar o revisar un salto, una caída desde altura o un aterrizaje de una persona o un humanoide
remite: RA-011_Locomocion_por_apoyos, 02_Plataformero_2D, Principios de animacion
cruza: 01_Anatomia_del_movimiento, 03_Masa_centro_de_masa_y_equilibrio
---

# Medicina 06 — Salto y aterrizaje

> Las fases de un salto real y cuánto dura cada una, cuánto se agacha el cuerpo, cuánto sube, cómo frena al aterrizar, y qué pasa con todo eso cuando el juego exagera la altura o la gravedad.
> **No cubre:** cuánto salta el personaje del jugador, con qué gravedad ni con qué demora: eso es diseño y lo fija el `GDS` (en un plataformero, `02_Plataformero_2D`). Tampoco perder el equilibrio y caerse al piso: eso es `03_Masa_centro_de_masa_y_equilibrio`. Este libro dice qué hace el cuerpo para que la física del juego se vea creíble.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Qué decisión sostiene

Arte, al escribir POSES, TIEMPO y JUGABILIDAD de un encargo de salto: preparación, despegue, ascenso, ápice, caída y aterrizaje (las fases de `RA-011`, regla 5). Hasta hoy la duración de la preparación y del amortiguado, la profundidad del agache y cuánto se dobla la rodilla al aterrizar iban a ojo. Las tres cosas chocan además con la física del juego, que exagera la altura y no tolera una preparación larga en el personaje del jugador.

---

## Modelo

**Convención.** Los ángulos son de flexión: 0° = articulación recta, crece al doblar (la de `01_Anatomia_del_movimiento`). Las alturas del salto son del centro de masa, que en el juego es lo que sube la raíz del personaje.

**La preparación tiene tres partes** (McMahon, Suchomel, Lake y Comfort 2018). En la **descarga** la fuerza contra el piso cae por debajo del peso y el cuerpo empieza a caer; en el **frenado** detiene esa caída hasta quedar en el punto más bajo; en la **propulsión** empuja hasta que los pies dejan el piso. Después viene el vuelo, balístico: en el cuerpo real nada de lo que haga cambia la trayectoria de su centro de masa.

**La bajada dura más que la subida.** Del primer movimiento al despegue pasan entre 0.75 y 0.81 s (McMahon, Rej y Comfort 2017); la descarga sola se lleva entre un tercio y la mitad de un total de 0.83–0.99 s, según dónde se marque el inicio (Williams 2024). Descarga más frenado suman ≈0.5–0.7 s, según el umbral que marca el inicio, contra una propulsión estimada en ≈0.3 s (derivado de Williams 2024 y McMahon, Rej y Comfort 2017).

**El agache se paga en tiempo.** El salto con contramovimiento sube 3–4 cm más que el mismo salto desde la sentadilla quieta, porque el músculo llega al empuje ya activado, no principalmente por energía elástica (Bobbert 1996); a cambio, alarga la fase previa al despegue entre 71 y 76% (Harman 1990). En el personaje del jugador es lo primero que se recorta.

**El cuerpo despega estirado.** Con las manos en la cadera, el centro de masa baja unos 0.28 m y después sube unos 0.38 m hasta el despegue: despega unos 10 cm por encima de su altura de pie, en punta de pie (derivado de McMahon, Rej y Comfort 2017). La velocidad máxima llega 0.03 s antes de que los pies se separen y cae un 6–7% hasta el despegue (Harman 1990).

**Los brazos pesan más que el agache.** Balancear los brazos suma unos 8.6 cm de altura; el 72% de esa mejora es velocidad de despegue y el 28%, un centro de masa más alto al despegar, con los brazos arriba (Lees, Vanrenterghem y De Clercq 2004). Su efecto es mayor que el del contramovimiento (Harman 1990).

**Lo que sube es el centro de masa, no los pies.** Los pies suben lo mismo más lo que el cuerpo se recoja en el aire, y el cuerpo aterriza más bajo de lo que despegó (Linthorne 2001).

**Aterrizar es frenar con las articulaciones.** Cayendo de 0.59 m, un aterrizaje blando flexiona la rodilla 117° y uno rígido 77°; el blando reparte el trabajo entre cadera y rodilla y genera menos fuerza contra el piso, el rígido carga más el tobillo (DeVita y Skelly 1992).

**Salto en largo.** Sin carrera, 5 varones activos saltaron 2.1–2.3 m y eligieron despegar a 31–39°, más empinado que el óptimo calculado de 19–27° (Wakai y Linthorne 2005). Con carrera, el ángulo de despegue ronda los 23° (Linthorne, Guzman y Bridgett 2005): nadie salta a 45°.

---

## Parámetros

| Parámetro | Valor | Rango | Condición | Fuente |
|---|---|---|---|---|
| Del primer movimiento al despegue | 0.78 s | 0.75–0.81 s | salto máximo, manos en la cadera, 14 y 14 deportistas | (McMahon, Rej y Comfort 2017) |
| Ídem, con otro umbral de inicio | 0.83 s | 0.83–0.99 s | 11 voleibolistas universitarias; resumen de congreso | (Williams 2024) |
| Descarga | 0.31 s | 0.31–0.47 s según el umbral | ídem | (Williams 2024) |
| Frenado + propulsión | 0.52 s | — | ídem | derivado de (Williams 2024) |
| Propulsión sola | ≈0.30 s | 0.30–0.32 s | estimación con aceleración constante | derivado de (McMahon, Rej y Comfort 2017) |
| Cuánto baja el centro de masa | 0.28 m | 0.25 (mujeres) – 0.31 m (varones) | profundidad elegida | (McMahon, Rej y Comfort 2017) |
| Cuánto sube hasta el despegue | 0.38 m | 0.34 – 0.42 m | ídem | (McMahon, Rej y Comfort 2017) |
| Velocidad máxima hacia arriba | 2.5 m/s | 2.3 – 2.7 m/s | 0.03 s antes del despegue | (McMahon, Rej y Comfort 2017; Harman 1990) |
| Velocidad de despegue | ≈2.3 m/s | 2.2 – 2.5 m/s | de las alturas medidas | derivado con h = v0²/(2g) de (McMahon, Rej y Comfort 2017) |
| Fuerza máxima contra el piso | 2.3–2.5 veces el peso | — | frenado y propulsión | (McMahon, Rej y Comfort 2017) |
| Ventaja del contramovimiento | +3.4 cm | +3.4 a +3.8 cm | misma postura inicial | (Bobbert 1996; Linthorne 2001) |
| Ganancia por balanceo de brazos | +8.6 cm | — | 20 varones | (Lees, Vanrenterghem y De Clercq 2004) |
| Altura de salto, mujeres entrenadas | 0.24 m | ± 0.05 m | netball regional | (McMahon, Rej y Comfort 2017) |
| Altura de salto, varones entrenados | 0.32–0.36 m | ± 0.05 m | rugby | (McMahon, Rej y Comfort 2017; McMahon, Ripley y Comfort 2022) |
| Altura de salto, velocistas de selección | 0.63 m (varones) · 0.48 m (mujeres) | ± 0.05–0.06 m | selección nacional noruega | (Haugen 2021) |
| Salto en largo sin carrera | 2.1–2.3 m | — | 5 varones activos | (Wakai y Linthorne 2005) |
| Ángulo de despegue sin carrera | 31–39° elegido | 19–27° óptimo calculado | ídem | (Wakai y Linthorne 2005) |
| Ángulo de despegue con carrera | ≈23° | — | saltadores experimentados | (Linthorne, Guzman y Bridgett 2005; actas de ISBS 2002) |
| Flexión de rodilla, aterrizaje blando / rígido | 117° / 77° | blando por encima de 90°, rígido por debajo | caída de 0.59 m, 8 atletas | (DeVita y Skelly 1992) |
| Aterrizaje en un pie | rodilla 9–14° de flexión al contacto, máximo ≈80°; cadera, máximo ≈50° | — | caída de 0.35 m, 15 varones, pierna dominante, calzado normal y biónico | (Xu 2021) |

---

## Relaciones

```txt
h  = v0² / (2g)           altura que sube el centro de masa desde el despegue       (Linthorne 2001)
h  = g · T² / 8           T = tiempo de vuelo, con gravedad igual al subir y al bajar (Linthorne 2001)
t_subida = √(2h / g_subida)    t_caída = √(2h_caída / g_caída)    cada tramo con su gravedad
t_empuje = 2d / v0        d = recorrido del centro de masa en la propulsión
fuerza media / peso = 1 + h / s       al aterrizar desde h, frenando en un recorrido s
t_amortiguado = 2s / v,   v = √(2 g h)
```

La g es la del juego, salvo en la tabla de gravedad real de abajo. `1 + h/s` no depende de g: vale igual con la gravedad del juego; T, v y t_amortiguado sí dependen. Las cuatro últimas relaciones son cinemática elemental derivada para este libro y se comprueban a mano. Con datos reales: d = 0.42 m y la velocidad máxima de 2.67 m/s dan un empuje de 0.32 s (derivado de McMahon, Rej y Comfort 2017).

**El amortiguado es un supuesto.** Si se supone que el centro de masa baja 0.30 m al frenar una caída de 0.59 m, la fuerza media es 3 veces el peso y el amortiguado dura 0.18 s; el pico es mayor que la media (supuesto de esta misión: DeVita y Skelly 1992 miden la rodilla, no el centro de masa).

**Tiempo en el aire con gravedad real y simétrica** (derivado de h = g · T² / 8):

```txt
altura    v0 (m/s)   en el aire (s)   cuadros a 60 fps   a 24 fps
0.25        2.2         0.45              27              11
0.40        2.8         0.57              34              14
0.60        3.4         0.70              42              17
2.00        6.3         1.28              77              31
```

**El juego decide la física al revés** (Pittman 2016): fija la altura h y el tiempo hasta el punto más alto t_h, y de ahí salen `v0 = 2h / t_h` y `g = 2h / t_h²`. Muchos juegos suben la gravedad después del ápice para que la caída sea más seca; en un plataformero la gravedad de la caída es 1.6–2.2 veces la de la subida (a igual altura, la caída dura 0.67–0.79 de la subida), hay corte de salto y apex hang (`02_Plataformero_2D`). Con eso, el vuelo deja de ser simétrico y su duración ya no sale de la tabla de arriba.

---

## Estilización

**Saltar más alto con gravedad real se ve flotante.** Dos metros con gravedad real son 1.28 s en el aire, más del doble que un salto humano (derivado de Linthorne 2001). Por eso los juegos suben la gravedad: 3 m en 0.35 s hasta el ápice piden unos 49 m/s² y despegar a 17 m/s, cuando una persona despega a 2.2–2.5 (derivado de Pittman 2016 y McMahon, Rej y Comfort 2017).

**La preparación real no entra en el control del jugador.** Los 0.8 s reales del primer movimiento al despegue serían 48 cuadros a 60 fps de demora entre el botón y el salto (derivado de McMahon, Rej y Comfort 2017). La demora la fija el `GDS`; en `02_Plataformero_2D` es cero, el salto responde en el cuadro del botón. Entonces el agache no se dibuja antes del despegue: la fuerza se vende con el estiramiento de los primeros cuadros de ascenso. Solo si el `GDS` acepta demora entra un empuje corto: con 0.4 m de empuje y v0 = 17 m/s, la física exagerada lo resuelve en 0.05 s, unos 3 cuadros a 60 fps (derivado de t_empuje = 2d/v0). Mostrar en esos pocos cuadros un agache más profundo que el real es estilización declarada: con la física real, más profundo es más largo. Que un enemigo use la preparación real como aviso lo decide el `GDS`; el criterio de anticipación del jugador y del enemigo es de `Principios de animacion`.

**Aterrizajes imposibles.** Agachado a fondo, el centro de masa baja como mucho ≈0.5 m (supuesto de esta misión). Para que un aterrizaje cargue lo mismo que el blando supuesto arriba, ≈3 veces el peso en media, el cuerpo tiene que frenar en la mitad de la altura de caída (derivado de fuerza/peso = 1 + h/s, con el supuesto de esta misión sobre la caída de DeVita y Skelly 1992): con ese tope, a partir de ~1 m de caída el cuerpo real rueda o se agacha a fondo. Caer 3 m frenando en 0.30 m es una fuerza media de 11 veces el peso. Un juego que no lo muestra elige una pose corta y estilizada, y lo declara.

---

## Medible y juicio

```txt
se mide (cuenta)        cuadros de ascenso y de caída contra la build o el GDS: t_subida y t_caída con
                        las gravedades del juego, más el apex hang, la velocidad terminal y el corte
                        de salto, si los hay; si no coinciden, manda la build
                        el cuadro de despegue: pies fuera del piso con el cuerpo estirado
                        recorrido del amortiguado contra la altura de caída (fuerza/peso = 1 + h/s)
se mide (animacion.py)  lienzo, alfa, escala, por clip. La línea de piso de la preparación y del
                        aterrizaje se revisa a mano, sin --in-place, en esos clips por separado; un salto no es un ciclo
                        in-place (RA-011, verificación)
se juzga (plancha)      si el despegue lee la fuerza; si el aterrizaje lee el peso
```

---

## Al encargo

```txt
POSES       preparación, despegue, ascenso, ápice, caída, aterrizaje; ascenso, caída y
            aterrizaje en clips separados, no un clip fijo (RA-011, regla 5). Agache con el
            centro de masa ≈0.16 · H abajo (≈0.28 m en un adulto); despegue estirado en punta de
            pie, brazos arriba si el estilo los usa; contacto con la rodilla casi recta (≈10° de
            flexión, en un pie desde 0.35 m, Xu 2021); amortiguado: blando ≈117° de flexión de
            rodilla, rígido ≈77°. Salto con carrera: el cuerpo despega inclinado hacia adelante
            (lectura de esta misión; la trayectoria la fija el juego)
TIEMPO      jugador: la demora botón → despegue la fija el GDS (en 02_Plataformero_2D, cero: el
            agache se vende en el estiramiento del ascenso). Con demora aceptada, empuje de
            2d/v0 con la v0 del juego (≈3 cuadros a 60 fps con 3 m en 0.35 s). Enemigo o cinemática: preparación real ≈0.8 s disponible.
            Ascenso y caída: los cuadros salen de la build o del GDS, cada tramo con su gravedad;
            √(8h/g) solo vale si la gravedad es la misma al subir y al bajar
ATERRIZAJE  jugador: pose corta y estilizada por defecto, del largo que fije el GDS (squash de
            60–100 ms en 02_Plataformero_2D). Cinemática o NPC: amortiguado proporcional
            (s ≈ h/2, supuesto de esta misión); más de ≈0.57 · H de caída (~1 m en un adulto): rodar o agacharse a fondo
JUGABILIDAD cuadro de despegue y cuadro de contacto marcados; el ascenso puede cortarse antes del
            ápice (RA-011, regla 5); cuándo vuelve el control lo fija el GDS
```

El 0.16 · H sale de 0.28 m sobre una estatura de 1.75 m (derivado de McMahon, Rej y Comfort 2017, supuesta esa estatura); para otra escala, proporcional a la estatura.

---

## Límites

- Saltos verticales y en largo de adultos sanos, y aterrizajes desde una altura. Saltos con giros, mortales, salto en alto, saltos de rebote (drop jump) y el detalle del salto en largo con carrera, más allá del ángulo de despegue, quedan afuera.
- **No verificados en esta misión:** la duración separada de frenado y propulsión medida en plataforma, el ángulo de rodilla en el punto más bajo del agache, las alturas de salto de adultos no entrenados, cuánto baja el centro de masa al aterrizar y las fuerzas de aterrizaje por técnica (de ahí que el amortiguado sea un supuesto), si el primer contacto es con el antepié, el penúltimo paso más largo en el salto en largo, y cifras de cuadros de anticipación en juegos.
- Referencia visual primaria: las láminas de salto de `83_Muybridge_Animal_Locomotion`.

---

## Fuentes

- McMahon, J. J., Rej, S. J. E. & Comfort, P. (2017). Sex differences in countermovement jump phase characteristics. *Sports* 5(1), 8. — `75_Countermovement_Jump_Phases`.
- McMahon, J. J., Suchomel, T. J., Lake, J. P. & Comfort, P. (2018). Understanding the key phases of the countermovement jump force-time curve. *Strength and Conditioning Journal* 40(4), 96–106. — `75_Countermovement_Jump_Phases`.
- McMahon, J. J., Ripley, N. J. & Comfort, P. (2022). Force plate-derived countermovement jump normative data and benchmarks for professional rugby league players. *Sensors* 22(22), 8669.
- Williams et al. (2024). Influence of onset movement threshold on phase duration during the countermovement jump. *International Journal of Exercise Science, Conference Proceedings* 16(3), 235. Resumen.
- Linthorne, N. P. (2001). Analysis of standing vertical jumps using a force platform. *American Journal of Physics* 69(11), 1198–1204. — `76_Standing_Vertical_Jump`.
- Bobbert, M. F., Gerritsen, K. G. M., Litjens, M. C. A. & Van Soest, A. J. (1996). Why is countermovement jump height greater than squat jump height? *Medicine & Science in Sports & Exercise* 28(11), 1402–1412. Resumen.
- Harman, E. A., Rosenstein, M. T., Frykman, P. N. & Rosenstein, R. M. (1990). The effects of arms and countermovement on vertical jumping. *Medicine & Science in Sports & Exercise* 22(6), 825–833. Resumen.
- Lees, A., Vanrenterghem, J. & De Clercq, D. (2004). Understanding how an arm swing enhances performance in the vertical jump. *Journal of Biomechanics* 37(12), 1929–1940. Resumen.
- Haugen, T., Breitschädel, F., Wiig, H. & Seiler, S. (2021). Countermovement jump height in national-team athletes of various sports. *International Journal of Sports Physiology and Performance* 16(2), 184–189. Resumen; solo los valores de velocistas.
- Wakai, M. & Linthorne, N. P. (2005). Optimum take-off angle in the standing long jump. *Human Movement Science* 24(1), 81–96.
- Linthorne, N. P., Guzman, M. S. & Bridgett, L. A. (2005). Optimum take-off angle in the long jump. *Journal of Sports Sciences* 23(7), 703–712. Resumen; el ≈23° se lee en el resumen de los mismos autores en las actas de ISBS (2002).
- DeVita, P. & Skelly, W. A. (1992). Effect of landing stiffness on joint kinetics and energetics in the lower extremity. *Medicine & Science in Sports & Exercise* 24(1), 108–115. Resumen.
- Xu, D., Zhou, H., Baker, J. S., István, B. & Gu, Y. (2021). An investigation of differences in lower extremity biomechanics during single-leg landing from height using bionic shoes and normal shoes. *Frontiers in Bioengineering and Biotechnology* 9, 679123.
- Pittman, K. (2016). *Math for Game Programmers: Building a Better Jump*. GDC. — `84_Building_a_Better_Jump`.

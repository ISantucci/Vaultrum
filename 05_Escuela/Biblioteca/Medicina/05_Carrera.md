---
tipo: medicina
estado: En la Biblioteca
mision: EST-024_Mision_Morfologia_del_movimiento
consume: Arte, solo al encargar, animar o revisar la carrera de una persona o un humanoide (trote, carrera, sprint, arranque)
remite: RA-011_Locomocion_por_apoyos, 02_Plataformero_2D
cruza: 04_Marcha_humana
---

# Medicina 05 — Carrera

> Qué hace que una carrera sea carrera y no una caminata rápida, cuánto dura su ciclo a cada velocidad, cuántos cuadros vuela y cómo arranca.
> **No cubre:** la caminata, el vocabulario (zancada, paso, I/D, in-place) ni la escala por número de Froude: están en `04_Marcha_humana` y acá se usan sin repetirse.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Qué decisión sostiene

`RA-011` dice que una carrera "no es la caminata reproducida más rápido", y nació de una caminata que parecía correr. Lo que la regla no tiene son los números: cuánto del ciclo apoya cada pie, cuántos cuadros sin apoyo hay, cuánto flexiona la rodilla, cómo crece la zancada con la velocidad. Hasta hoy Arte los ponía a ojo en POSES, TIEMPO y MOVIMIENTO del encargo, y no tenía con qué decidir cuántos ciclos distintos hace falta animar.

---

## Modelo

**Nombres que usa este libro.** Ciclo = zancada = dos pasos; N cuenta cuadros por zancada. **Trote** es 2.5 m/s, **carrera** 3.5–4.5 m/s y **sprint** la velocidad máxima de cada uno; son los nombres de la tabla de cuadros de abajo, y trote y carrera son las velocidades medidas por Fukuchi, Fukuchi y Duarte (2017).

**El apoyo se achica con la velocidad.** Cada pie apoya el 62% del ciclo al caminar, el 31% al correr y el 22% en un sprint (Mann y Hagy 1980). Con menos de la mitad del ciclo apoyado, los dos apoyos ya no se tocan: aparece una fase de **vuelo después de cada despegue**, dos por zancada. Al correr, el despegue cae cerca del 40% del ciclo (Novacheck 1998, vía Physiopedia); la fuente no da la velocidad y esta misión lo asigna al trote.

**Resorte, no péndulo.** Al correr el cuerpo rebota como una masa sobre un resorte; al caminar, pasa por encima de la pierna como un péndulo invertido (Farley y Ferris 1998). En el modelo de resorte la compresión máxima, y por eso el punto más bajo del cuerpo, cae en el apoyo medio, y el punto alto en el vuelo: lo contrario de la caminata, donde el apoyo medio es el punto alto (derivado del modelo de Farley y Ferris 1998; `04_Marcha_humana`). La rodilla lo muestra: toca el piso ya flexionada a 18° y llega a 46° en su pico del apoyo (Heiderscheit 2011).

**El cuerpo baja al ir más rápido.** Con la velocidad crecen la flexión de cadera y de rodilla y la flexión dorsal del tobillo, y el centro de masa baja (Mann y Hagy 1980). En el balanceo, el talón se acerca a la cola cuanto más rápido se corre (Fukuchi, Fukuchi y Duarte 2017).

**Más velocidad es más zancada, no más cadencia.** De 2.5 a 4.5 m/s la zancada crece 59% (de 1.86 a 2.96 m) y la cadencia 14% (derivado de Fukuchi, Fukuchi y Duarte 2017). En velocidad máxima tampoco gana quien mueve la pierna más rápido: el tiempo de balanceo no difiere entre rápidos y lentos, y los rápidos empujan el piso con más fuerza (Weyand 2000). Subir la velocidad de reproducción de un ciclo no lo convierte en una carrera más rápida: solo lo acelera.

**El arranque tiene su forma.** En velocistas que salen de tacos, el contacto con el piso es largo en los primeros pasos y se acorta rápido hasta el paso 4; la frecuencia sube hasta el paso 4 y después queda en meseta (máximo de 4.87 pasos por segundo en el paso 8), mientras el paso se sigue alargando hasta el 24; el tronco sale inclinado y se endereza hasta el paso 16 (Nagahara 2014).

---

## Parámetros

| Parámetro | Valor | Rango | Condición | Fuente |
|---|---|---|---|---|
| Apoyo de cada pie | 31% del ciclo | — | 5 trotadores y 6 fondistas de élite, velocidad no informada | (Mann y Hagy 1980) |
| Apoyo de cada pie, sprint | 22% del ciclo | — | 2 velocistas | (Mann y Hagy 1980) |
| Despegue en el trote | ≈40% del ciclo | — | al correr, velocidad no informada; asignado al trote por esta misión | (Novacheck 1998, vía Physiopedia) |
| Velocidad preferida de un corredor recreativo | 2.9 m/s | ± 0.5 m/s | cinta, 45 corredores, estatura media 1.76 m | (Heiderscheit 2011) |
| Cadencia preferida | 172.6 pasos/min | ± 8.8 | 2.9 m/s | (Heiderscheit 2011) |
| Largo de paso | 1.01 m | ± 0.17 m | 2.9 m/s | (Heiderscheit 2011) |
| Subida y bajada del centro de masa | 8.7 cm | 7.3 cm con +10% de cadencia | 2.9 m/s | (Heiderscheit 2011) |
| Rodilla al tocar el piso / pico en el apoyo | 18° / 46° de flexión | — | 2.9 m/s; 0° = pierna recta | (Heiderscheit 2011) |
| Zancada (dos pasos) | 1.86 / 2.46 / 2.96 m | — | 2.5 / 3.5 / 4.5 m/s, 28 corredores recreativos | (Fukuchi, Fukuchi y Duarte 2017) |
| Cadencia | 162 / 171 / 183 pasos/min | — | ídem; la fuente da 80.8 / 85.7 / 91.7 zancadas/min | derivado (× 2) de (Fukuchi, Fukuchi y Duarte 2017) |
| Duración de la zancada | 0.74 / 0.70 / 0.65 s | — | ídem | derivado de (Fukuchi, Fukuchi y Duarte 2017) |
| Flexión máxima de rodilla en el balanceo | 94° / 109° / 119° | — | ídem | (Fukuchi, Fukuchi y Duarte 2017) |
| Flexión máxima de cadera | 44° / 53° / 61° | — | ídem | (Fukuchi, Fukuchi y Duarte 2017) |
| Extensión de cadera al despegar | 4° / 8° / 12° | — | ídem | (Fukuchi, Fukuchi y Duarte 2017) |
| Flexión plantar máxima | 17° / 20° / 23° | — | ídem | (Fukuchi, Fukuchi y Duarte 2017) |
| Velocidad máxima de sprint | 6.2–11.1 m/s | — | 33 personas de distinto nivel | (Weyand 2000) |
| Velocidad máxima de élite | 12.34 m/s | — | Bolt, Berlín 2009, pico en el tramo 60–80 m | (Maćkała y Mero 2013) |
| Paso y frecuencia de élite | 2.77 m a 4.49 pasos/s | — | promedio del tramo 60–80 m (12.26 m/s) | (Maćkała y Mero 2013) |
| Contacto mínimo en sprint | 0.090 s | ± 0.006 s | 12 velocistas, aceleración de 50 m desde tacos | (Nagahara 2014) |
| Frecuencia máxima en la aceleración | 4.87 pasos/s | — | paso 8; sube hasta el paso 4 y queda en meseta | (Nagahara 2014) |
| Primer apoyo con el talón | 88.9% | — | 936 fondistas calzados, km 10 | (Larson 2011, vía el blog del autor) |

**"Stride" no dice siempre lo mismo.** Maćkała y Mero (2013) llaman *stride* al paso; Fukuchi (2017) llama *stride* a la zancada de dos pasos. En un encargo se escribe "paso" o "zancada", nunca "stride".

---

## Relaciones

```txt
velocidad = largo de zancada × zancadas por segundo = largo de paso × pasos por segundo
apoyo por pie   = apoyo × N                apoyo como fracción del ciclo
vuelo por paso  = (0.5 − apoyo) × N
```

**Cuadros por ciclo** (derivado de Fukuchi, Fukuchi y Duarte 2017, y de Maćkała y Mero 2013):

```txt
            velocidad   zancada   cuadros por zancada      cuadros por paso
                          (s)     24 fps  30 fps  12 fps       a 24 fps
trote        2.5 m/s     0.74       18      22       9            9
carrera      3.5 m/s     0.70       17      21       8            8
carrera      4.5 m/s     0.65       16      20       8            8
sprint élite 12.3 m/s    0.45       11      13       5            5
```

**Cuadros con y sin apoyo** (derivado con el apoyo de Novacheck 1998 para el trote y el de Mann y Hagy 1980 para carrera y sprint):

```txt
a 24 fps   trote    N ≈ 18, apoyo 0.40   ≈7 cuadros de apoyo por pie · ≈2 de vuelo por paso
           carrera  N ≈ 16–17, apoyo 0.31 ≈5 de apoyo · ≈3 de vuelo
           sprint   N ≈ 11, apoyo 0.22   ≈2.4 de apoyo · ≈3 de vuelo
a 12 fps   trote    N ≈ 9, apoyo 0.40    ≈3.6 de apoyo · ≈1 de vuelo
```

Un ciclo de 8 sprites reproducido a 12 fps tiene la cadencia de una carrera de unos 4 m/s; lo rápido que avanza en el juego depende de la zancada en px (derivado de Fukuchi, Fukuchi y Duarte 2017).

**Que no patine.** La relación in-place es la de `04_Marcha_humana`: `v_juego = zancada_px · fps / N`, con zancada_px en la escala del ART. Con vuelo hay cuadros en que ningún pie retrocede: el cuerpo avanza solo.

**Escala.** La transición a carrera y la escala para piernas cortas están en `04_Marcha_humana`, con L = 0.527 · H.

**Más cadencia, menos rebote.** A igual velocidad, subir la cadencia un 10% baja el rebote de 8.7 a 7.3 cm, acorta el paso de 1.01 a 0.92 m y baja el pico de la rodilla de 46° a 43° (Heiderscheit 2011).

---

## Estilización

**Cartoon.** La tradición de animación habla de carreras "en 8, en 6 y en 4" cuadros por paso a 24 fps (atribuido a Williams 2001; no se pudo leer en esta misión). Contra los datos: en 8 es una carrera de 3.5–4.5 m/s; en 6 son 4 pasos por segundo, un sprint que no es de élite; en 4 son 6 pasos por segundo, más que la frecuencia máxima medida de 4.87 (Nagahara 2014). Por debajo de unos 5 cuadros por paso a 24 fps ya es exageración, y se elige como tal.

**Ciclos distintos, no un ciclo acelerado.** Como la velocidad real crece sobre todo por la zancada, un rango amplio de velocidades se cubre con trote, carrera y sprint mezclados, no estirando la reproducción de uno (derivado de Fukuchi, Fukuchi y Duarte 2017). Un ciclo acelerado sin alargar la zancada se lee nervioso (juicio de esta misión). Cuánto se puede acelerar antes de que se note no tiene fuente: se mide en el juego.

**Piernas cortas a velocidad alta.** Si el juego le impone a un personaje de pierna corta una velocidad alta, su Froude sube, y por la similitud dinámica de `04_Marcha_humana` el resultado se lee como sprint: más vuelo, menos apoyo, más flexión (extrapolación a la carrera de una similitud medida al caminar por Donelan y Kram 1997).

**Arranque.** Dura lo que el juego tarda en llegar a la velocidad máxima, y eso lo fija el `GDS`. En `02_Plataformero_2D` son 0.1–0.2 s, menos de un paso: entra el ciclo, a lo sumo con una pose de impulso. Con ≈1 s o más de aceleración (NPC, cinemática), 3–4 pasos cortos, con contacto largo y el tronco adelante, comprimen una aceleración que en velocistas dura hasta el paso 14–24 (Nagahara 2014): es estilización, y para el arranque de un trote no hay dato.

**Lo que hace que se lea "carrera"**, todo medido: menos de la mitad del ciclo apoyado y cuadros de vuelo (Mann y Hagy 1980); rodilla flexionada durante todo el apoyo (Heiderscheit 2011); talón cerca de la cola en el balanceo (Fukuchi, Fukuchi y Duarte 2017); rebote de 8–9 cm a 2.9 m/s, el doble que caminando (Heiderscheit 2011; Orendurff 2004).

---

## Medible y juicio

```txt
se mide (animacion.py)   lienzo, alfa, escala. Una carrera no se mide con --in-place: tiene
                         fase aérea (RA-011, verificación)
se mide (cuenta)         cuadros sin ningún pie apoyado por paso, contra la tabla de su fps
                         cuadros por paso contra la velocidad del juego, convertida con la escala
                         del ART; v_juego contra zancada_px · fps / N
se juzga (plancha)       que el punto bajo del cuerpo caiga en el apoyo medio, no en el contacto;
                         que la rodilla de apoyo no se estire; que I y D se alternen; el enlace
                         del último cuadro con el primero
```

---

## Al encargo

```txt
MIEMBROS    I y D anatómicas; brazos en oposición a las piernas
POSES       cada pie apoya menos de la mitad del ciclo, y entre apoyos hay vuelo. La rodilla
            toca el piso flexionada y se flexiona más hasta el apoyo medio, que es el punto MÁS
            BAJO del cuerpo; el más alto está en el vuelo. Si se usa el esquema de ocho poses de
            RA-011, el apoyo medio (02–03) es el punto bajo, al revés que caminando. Balanceo con
            el talón alto: ≈95° de rodilla al trotar, ≈120° a 4.5 m/s. Trote de fondo: primer
            contacto con el talón
TIEMPO      a 24 fps: trote ≈0.74 s por zancada, 9 cuadros por paso y ≈2 de vuelo; carrera
            ≈0.65–0.70 s, 8 por paso y ≈3 de vuelo; sprint ≈5–6 por paso. Menos de 5 cuadros por
            paso (más de ≈5 pasos por segundo) ya es cartoon. A 12 fps, el trote son 9 cuadros
            por zancada con ≈1 de vuelo
MOVIMIENTO  in-place: v_juego = zancada_px · fps / N. Rebote vertical ≈5% de la estatura a
            2.9 m/s, de pico a pico. Para otra velocidad, otro ciclo: la zancada crece, la
            cadencia casi no. Un plataformero a 6–9 alturas por segundo (10.5–15.8 m/s para
            1.75 m) pide el ciclo de sprint
ARRANQUE    dura lo que el juego tarda en llegar a la velocidad máxima (GDS). En
            02_Plataformero_2D son 0.1–0.2 s, menos de un paso: entra el ciclo, a lo sumo con
            una pose de impulso. Con ≈1 s o más de aceleración (NPC, cinemática): 3–4 pasos
            cortos, con contacto largo y el tronco adelante; la cadencia sube hasta el paso 4;
            después el ciclo (estilización de una aceleración más larga)
```

El 5% sale de 8.7 cm sobre una estatura de 1.75 m (derivado de Heiderscheit 2011). Los 10.5–15.8 m/s salen de 6–9 alturas por segundo para 1.75 m (derivado de `02_Plataformero_2D`); los velocistas de Weyand van de 6.2 a 11.1 m/s (Weyand 2000) y el máximo medido es 12.34 m/s (Maćkała y Mero 2013): por encima, la zancada es estilizada. Los 95° y 120° son la flexión máxima de rodilla a 2.5 y 4.5 m/s (Fukuchi, Fukuchi y Duarte 2017).

---

## Límites

- Corredores adultos sanos, en cinta o pista. Correr en pendiente, girar, frenar y cambiar de dirección quedan afuera.
- **Asignación declarada:** usar 0.40 de apoyo para el trote y 0.31 para la carrera es una asignación por velocidad que esta misión hizo; las dos fuentes no informan la velocidad exacta.
- **No verificados en esta misión:** amplitud de brazos (el codo a 90° es práctica habitual sin fuente leída), inclinación del tronco a velocidad constante, tiempos de contacto en el trote, la rigidez de la pierna y cómo cambia el rebote con la velocidad, el cambio de zancada a cadencia por encima de ~7 m/s, el patrón de apoyo de los velocistas y el arranque de un trote. Para un encargo que los necesite, la referencia es primaria: `81_Datasets_de_marcha_y_carrera_Fukuchi`, `82_CMU_Motion_Capture_Database`, `83_Muybridge_Animal_Locomotion`.
- Las convenciones cartoon de cuadros por paso no se leyeron en su fuente; están contrastadas con datos, no confirmadas.

---

## Fuentes

- Mann, R. A. & Hagy, J. (1980). Biomechanics of walking, running, and sprinting. *American Journal of Sports Medicine* 8(5), 345–350. Resumen.
- Novacheck, T. F. (1998). The biomechanics of running. *Gait & Posture* 7(1), 77–95. Leído vía Physiopedia, *Running Biomechanics*.
- Farley, C. T. & Ferris, D. P. (1998). Biomechanics of walking and running: center of mass movements to muscle action. *Exercise and Sport Sciences Reviews* 26, 253–285. Resumen.
- Heiderscheit, B. C., Chumanov, E. S., Michalski, M. P., Wille, C. M. & Ryan, M. B. (2011). Effects of step rate manipulation on joint mechanics during running. *Medicine & Science in Sports & Exercise* 43(2), 296–302. https://pmc.ncbi.nlm.nih.gov/articles/PMC3022995/
- Fukuchi, R. K., Fukuchi, C. A. & Duarte, M. (2017). A public dataset of running biomechanics and the effects of running speed on lower extremity kinematics and kinetics. *PeerJ* 5, e3298. — `81_Datasets_de_marcha_y_carrera_Fukuchi`.
- Weyand, P. G., Sternlight, D. B., Bellizzi, M. J. & Wright, S. (2000). Faster top running speeds are achieved with greater ground forces not more rapid leg movements. *Journal of Applied Physiology* 89(5), 1991–1999. Resumen.
- Maćkała, K. & Mero, A. (2013). A kinematics analysis of three best 100 m performances ever. *Journal of Human Kinetics* 36, 149–160. https://pmc.ncbi.nlm.nih.gov/articles/PMC3661886/
- Nagahara, R., Matsubayashi, T., Matsuo, A. & Zushi, K. (2014). Kinematics of transition during human accelerated sprinting. *Biology Open* 3(8), 689–699. https://pmc.ncbi.nlm.nih.gov/articles/PMC4133722/
- Larson, P. et al. (2011). Foot strike patterns of recreational and sub-elite runners in a long-distance road race. *Journal of Sports Sciences*. Leído vía el blog del autor (runblogger.com).
- Donelan, J. M. & Kram, R. (1997) y Orendurff, M. S. et al. (2004): ver `04_Marcha_humana`.

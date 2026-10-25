---
tipo: medicina
estado: En la Biblioteca
mision: EST-024_Mision_Morfologia_del_movimiento
consume: Arte, solo al encargar, animar o revisar la caminata de una persona o un humanoide
remite: RA-011_Locomocion_por_apoyos, Principios de animacion
cruza: 02_Proporciones_del_cuerpo, 03_Masa_centro_de_masa_y_equilibrio, 05_Carrera
---

# Medicina 04 — Marcha humana

> Cómo camina una persona, con los números que un encargo de caminata necesita para no inventarlos: cuánto dura el ciclo, cuándo hay dos pies en el piso, cuánto sube y baja el cuerpo y a qué velocidad una persona elige dejar de caminar.
> **No cubre:** la regla de oficio para pedir y revisar una caminata (`RA-011_Locomocion_por_apoyos`) ni el criterio de animación (`Principios de animacion`). Este libro es el mecanismo que esas dos notas dan por sabido.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Qué decisión sostiene

En el modo Encargo de animación, Arte escribe POSES, TIEMPO y MOVIMIENTO de una caminata, y después la revisa sobre la plancha numerada. Hasta hoy esas líneas salían de memoria: `RA-011` nació de dos correcciones del owner, no de una fuente, y nadie sabía con número cuánto dura el doble apoyo, cuánto sube el cuerpo ni dónde está su punto más bajo. Este libro da esos valores y la relación entre la velocidad del personaje en el juego y su ciclo, que es lo que decide si el pie patina.

---

## Modelo

**Vocabulario.** Una **zancada** (o ciclo) va del contacto de un pie al siguiente contacto del mismo pie; un **paso**, de un pie al otro: una zancada son dos pasos, y el esquema de ocho poses de `RA-011` es una zancada. **I / D** son izquierda y derecha del personaje (`RA-011`, regla 1). **In-place**: el ciclo no se desplaza y lo mueve el juego (`RA-011`, regla 4). **fps**: cuadros por segundo de la animación, no del juego. **L**: largo de pierna funcional, la altura del trocánter de pie, 0.527 · H (`02_Proporciones_del_cuerpo`).

**Apoyo, balanceo y doble apoyo.** A velocidad cómoda cada pierna pasa cerca del 60% del ciclo apoyada y el 40% en el aire (Thompson, OUHSC, consultado en 2026); Mann y Hagy (1980) miden 62%. Como cada pie apoya más de la mitad del ciclo, los dos apoyos se superponen: hay **doble apoyo dos veces por zancada**, que a velocidad cómoda suman 20–24% (Thompson, OUHSC, consultado en 2026). Al caminar más rápido el apoyo se acorta, y el doble apoyo desaparece recién al correr (Mann y Hagy 1980; `05_Carrera`).

**Péndulo invertido.** Sobre la pierna apoyada el cuerpo sube hasta el apoyo medio y baja después. El centro de masa está más alto cuando el pie libre pasa junto al apoyado (cerca del 30% del ciclo) y más bajo en la carga, justo al contacto (cerca del 0%) (Orendurff 2004; Kuo y Donelan 2010). Lo caro no es ese arco sino pasar de un pie al otro: el impulso de la pierna de atrás empieza un poco antes del contacto de la de adelante y sigue durante el doble apoyo (Kuo y Donelan 2010). En una caminata dibujada, el impulso del pie de atrás y el contacto del de adelante se superponen: el de atrás empuja durante el doble apoyo y despega recién al final, en la pose 02.

**El rebote no se aplana.** La teoría clásica de los seis determinantes (Saunders, Inman y Eberhart 1953, citados por Kuo y Donelan 2010) sostenía que pelvis y rodilla aplanan la trayectoria del centro de masa para ahorrar energía. Caminar con el centro de masa plano cuesta más, no menos, y medidos uno por uno los determinantes aportan poco al aplanado (Kuo y Donelan 2010). Una caminata realista sube y baja; aplanarla la vuelve mecánica.

**La velocidad cambia la forma, no solo el tiempo.** Al caminar más rápido el rebote vertical crece y el vaivén lateral se achica (Orendurff 2004). Lento es más vaivén y menos rebote; rápido, al revés.

---

## Parámetros

| Parámetro | Valor | Rango | Condición | Fuente |
|---|---|---|---|---|
| Velocidad cómoda | 1.4 m/s | 1.31–1.43 m/s | adultos de 20 a 59 años, por década y sexo | (Bohannon y Andrews 2011) |
| Velocidad cómoda, 60 a 69 años | 1.3 m/s | 1.24–1.34 m/s | ídem | (Bohannon y Andrews 2011) |
| Velocidad cómoda, 70 a 79 años | 1.2 m/s | 1.13–1.26 m/s | ídem | (Bohannon y Andrews 2011) |
| Apoyo de cada pierna | 60% de la zancada | 62% en Mann y Hagy | velocidad cómoda | (Thompson, OUHSC, consultado en 2026; Mann y Hagy 1980) |
| Doble apoyo | 20–24% de la zancada, en dos tramos | — | velocidad cómoda | (Thompson, OUHSC, consultado en 2026) |
| Subida y bajada del centro de masa, de pico a pico | 4.1 cm a 1.2 m/s | 2.7 cm a 0.7 m/s – 4.8 cm a 1.6 m/s | 10 adultos de 21 a 45 años, estatura media 1.76 m, pasarela de 10 m | (Orendurff 2004) |
| Vaivén lateral del centro de masa, de pico a pico | 4.4 cm a 1.2 m/s | 7.0 cm a 0.7 m/s – 3.9 cm a 1.6 m/s | ídem | (Orendurff 2004) |
| Punto más alto del cuerpo | ≈30% de la zancada (y ≈80%) | — | apoyo simple | (Orendurff 2004) |
| Punto más bajo del cuerpo | ≈0% de la zancada (y ≈50%, por simetría) | — | carga, al contacto | (Orendurff 2004) |
| Talón de atrás arriba | desde ≈35% de la zancada | — | apoyo terminal | (Thompson, OUHSC, consultado en 2026) |
| Flexión máxima de rodilla | 60° | — | balanceo inicial; 0° = pierna recta | (Thompson, OUHSC, consultado en 2026) |
| Radio con que rueda el pie | 0.3 × L | — | — | (Kuo y Donelan 2010) |
| Velocidad de transición a la carrera | 2.0 m/s | 1.96 ± 0.17 m/s | adultos, cinta; la velocidad que la gente elige | (Neptune y Sasaki 2005) |
| Número de Froude en la transición | 0.5 | se sostiene en gravedad reducida | — | (Kram, Domingo y Ferris 1997) |
| Número de Froude de la caminata cómoda | ≈0.2 | — | 1.4 m/s con L = 0.92 m | derivado de (Bohannon y Andrews 2011; Fromuth y Parkinson 2008) |
| Duración de la zancada en animación | 1.0 s | 1.0–1.67 s | 24 cuadros a 24 fps natural · 32 paseo · 40 persona mayor o cansada | (Koning, Monmouth, consultado en 2026; cita a Williams 2001) |

---

## Relaciones

```txt
velocidad            = largo de zancada / duración de la zancada                    definición
duración de zancada  = 120 / cadencia            [s, con cadencia en pasos/min]     definición
```

**Que el pie no patine, en un ciclo in-place** (derivado de las definiciones; es la base numérica de la regla 4 de `RA-011`):

```txt
N           cuadros por zancada
zancada_px  lo que avanzaría el personaje en una zancada, en px (escala del ART)
v_juego     = zancada_px · fps / N                 si el ciclo ya existe
fps         = v_juego · N / zancada_px             si diseño fija la velocidad

en el sprite   el pie apoyado retrocede zancada_px / N por cuadro, igual en todos los
               cuadros de apoyo (0.6 · N cuadros). El pie en el aire avanza 0.6 · zancada_px
               en 0.4 · N cuadros: por cuadro, 1.5 veces lo que retrocede el apoyado; en
               total, los dos recorren 0.6 · zancada_px
en el mundo    el pie en el aire avanza una zancada entera mientras el cuerpo avanza 0.4:
               va a ≈2.5 veces la velocidad del juego
```

**Escala por número de Froude** (Donelan y Kram 1997): `Fr = v² / (g · L)`. Dos cuerpos de distinto tamaño caminan con forma parecida cuando caminan al mismo Fr:

```txt
v          = √(Fr · g · L)          cómoda con Fr ≈ 0.2; la gente elige correr cerca de Fr = 0.5
duración   ∝ √(L / g)               la zancada de una pierna más corta dura menos
cadencia   ∝ √(g / L)

adulto, L = 0.92 m:   cómoda √(0.2 · 9.81 · 0.92) ≈ 1.34 m/s · transición ≈ 2.1 m/s
L = 0.46 m (la mitad): cómoda ≈ 0.95 m/s · transición ≈ 1.50 m/s · duración de zancada ≈ 0.71 de la del adulto
```

La similitud es una guía, no una ley: a igual Fr el porcentaje de apoyo coincide (±2%), pero el largo relativo de la zancada no (Donelan y Kram 1997).

**Las ocho poses de `RA-011` sobre el ciclo real** (derivado: poses repartidas parejo, contra los eventos de Orendurff 2004 y de Thompson, OUHSC, consultado en 2026):

```txt
pose RA-011     reparto parejo   evento real cerca de esa pose
01 contacto I        0%          doble apoyo; centro de masa en su MÍNIMO (≈0%)
02 descenso I       12.5%        termina el doble apoyo: D acaba de despegar
03 paso D           25%          D pasa junto a I; el MÁXIMO real cae cerca del 30%
04 elevación I      37.5%        el talón de I se levanta (desde ≈35%); el cuerpo ya baja
05 contacto D       50%          el otro doble apoyo y el otro mínimo
06–08                            espejo de 02–04
```

En animación tradicional la pose de descenso (02) se dibuja más baja que el contacto (01) (Koning, Monmouth, consultado en 2026): es convención de oficio, no el cuerpo real, que toca su mínimo en la carga. Las dos lecturas valen; lo que no vale es no saber cuál se eligió.

Dos lecturas de `RA-011` que la biomecánica precisa. No la re-legislan: se elevan al owner como hallazgo.

1. `RA-011` dice que en la caminata "suele haber" doble apoyo. A velocidad cómoda se mide 20–24% de doble apoyo (Thompson, OUHSC, consultado en 2026), y como cada pie apoya más de la mitad del ciclo, en toda caminata los apoyos se superponen. Un ciclo sin ninguna pose con los dos pies en el piso es una carrera o un error.
2. "04 elevación" puede leerse como "el cuerpo en su punto más alto" o como "se eleva el talón". En el cuerpo real el punto alto queda cerca de 03 y en 04 sube el talón mientras el cuerpo baja (Orendurff 2004; Thompson, OUHSC, consultado en 2026). Un 04 más alto que 03 es una decisión de estilo, no realismo.

---

## Estilización

**Tiempos de animación** (24 fps, cuadros por zancada; Koning, Monmouth, consultado en 2026, citando a Williams 2001): 16 para una caminata cartoon o una carrera lenta (con los datos de `05_Carrera`, 16 cuadros por zancada a 24 fps son ≈4.2 m/s, la carrera, y el trote son 18), 24 para una caminata enérgica y natural, 32 para un paseo, 40 para una persona mayor o cansada, 48 para un paso lento. Una caminata de 16 cuadros son 180 pasos por minuto, muy por encima de una caminata cómoda: 130 pasos por minuto ya es caminata vigorosa (Tudor-Locke 2019). Es estilización, y se escribe como tal.

**Piernas cortas.** Por Froude, el mismo andar en un personaje de pierna corta va más lento y con más cadencia. Cerca de `√(0.5 · g · L)` una persona elige correr; un personaje que camina más rápido que eso se ve forzado (derivado de Kram, Domingo y Ferris 1997). Si el juego lo pide, es una carrera (`05_Carrera`) o hay que alargarle la pierna aparente.

**Carácter.** Pesado o cansado, *si camina más lento*: zancada más larga en tiempo, menos rebote y más vaivén lateral; enérgico y rápido: más rebote (derivado de Orendurff 2004, que mide ese cambio con la velocidad, no con el carácter).

**Sprites.** Ocho poses por zancada de 1 s quedan sostenidas 3 cuadros a 24 fps; doce poses, 2 cuadros (derivado de Koning, Monmouth, consultado en 2026).

---

## Medible y juicio

```txt
se mide (animacion.py --in-place)   lienzo, alfa, escala, línea de apoyo y enlace 08 → 01
se mide (cuenta)                    poses con los dos pies apoyados: en ocho poses, 01 y 05
                                    (2 de 8, lo más cercano al 20–24% que permiten 8 poses)
                                    rebote del cuerpo en px contra la escala del ART
                                    velocidad del juego contra zancada_px · fps / N
se juzga (plancha)                  que I y D se alternen (RA-011, regla 3); que 03 sea el punto
                                    alto salvo estilo declarado en el ART; que el impulso de atrás
                                    y el contacto de adelante se superpongan (el de atrás
                                    despega en 02)
```

---

## Al encargo

Líneas para el encargo de animación de Arte. Se copian, y el `ART` cita este libro.

```txt
MIEMBROS    I y D anatómicas: en 01 apoya I adelante y D termina atrás; en 05, al revés
POSES       01 y 05 con los dos pies en el piso. 01–02 es la ventana del punto más bajo (el
            cuerpo real toca el mínimo al contacto; dibujar 02 más bajo es convención); 03, el
            más alto; en 04 sube el talón de atrás y el cuerpo ya baja. Si el estilo pide un 04
            más alto, se escribe como decisión de estilo. La rodilla del pie que pasa (03, 07)
            cerca de su flexión máxima, ≈60°
TIEMPO      zancada de ≈1.0 s para una caminata natural: 24 cuadros a 24 fps, u 8 poses
            sostenidas 3 cuadros. Paseo: 32 cuadros (1.33 s). Mayor o cansado: 40 (1.67 s)
MOVIMIENTO  in-place: el pie apoyado retrocede lo mismo en cada cuadro de apoyo, y la velocidad
            del juego es zancada_px · fps / N. Rebote vertical del cuerpo ≈2–2.5% de la estatura,
            de pico a pico; vaivén lateral del mismo orden, mayor cuanto más lento.
            En 3D, el pie rueda talón → planta → punta como una rueda de radio 0.3 · L
ESCALA      L = 0.527 · H. Pierna corta: la misma caminata va más lenta y con más cadencia.
            Cerca de √(0.5 · g · L) la gente elige correr (05_Carrera)
```

El rebote del 2–2.5% sale de 4.1 cm a 1.2 m/s y de ≈4.5 cm a 1.4 m/s, sobre una estatura de 1.75 m (derivado de Orendurff 2004, cuyos sujetos miden 1.76 m de media).

---

## Límites

- Adulto sano a velocidad cómoda. Niños, mayores frágiles y marcha patológica quedan afuera.
- **No verificados en esta misión, y por eso fuera de la tabla:** la cadencia típica en pasos por minuto y el largo de paso relativo a la estatura; los porcentajes finos de las subfases; cuánto cambian el apoyo y el doble apoyo con la velocidad (la dirección es firme, los porcentajes no); la amplitud de la rotación y la oblicuidad de la pelvis, del balanceo de brazos y del tronco; los ángulos de cadera y tobillo por fase. Si un encargo los necesita, se miden sobre referencia primaria (`83_Muybridge_Animal_Locomotion`, `82_CMU_Motion_Capture_Database`, `81_Datasets_de_marcha_y_carrera_Fukuchi`) y no se inventan.
- Giros, pendientes, escaleras y caminar cargando: fuera. Cargar está en `03_Masa_centro_de_masa_y_equilibrio`.
- Cuándo la caminata pasa a carrera y cómo es la carrera: `05_Carrera`.

---

## Fuentes

- Kuo, A. D. & Donelan, J. M. (2010). Dynamic principles of gait and their clinical implications. *Physical Therapy* 90(2), 157–174. — `71_Dynamic_Principles_of_Gait`. Péndulo invertido, costo de la transición entre pasos, crítica a los seis determinantes de Saunders, Inman y Eberhart (1953).
- Orendurff, M. S., Segal, A. D., Klute, G. K., Berge, J. S., Rohr, E. S. & Kadel, N. J. (2004). The effect of walking speed on center of mass displacement. *Journal of Rehabilitation Research and Development* 41(6A), 829–834. https://www.rehab.research.va.gov/jour/04/41/6/orendurff.html
- Bohannon, R. W. & Andrews, A. W. (2011). Normal walking speed: a descriptive meta-analysis. *Physiotherapy* 97, 182–189. Tabla leída en el resumen normativo de la Universidad de Toronto: https://www.physicaltherapy.utoronto.ca/sites/default/files/assets/files/11walking-speed-age-and-sex-specific-normative-values-final.pdf
- Mann, R. A. & Hagy, J. (1980). Biomechanics of walking, running, and sprinting. *American Journal of Sports Medicine* 8(5), 345–350. Resumen: https://pubmed.ncbi.nlm.nih.gov/7416353/
- Thompson, D. *Gait cycle terminology*. OUHSC, terminología de Rancho Los Amigos. https://ouhsc.edu/bserdac/dthompso/web/gait/terms.htm
- Donelan, J. M. & Kram, R. (1997). The effect of reduced gravity on the kinematics of human walking: a test of the dynamic similarity hypothesis for locomotion. *Journal of Experimental Biology* 200, 3193–3201.
- Kram, R., Domingo, A. & Ferris, D. P. (1997). Effect of reduced gravity on the preferred walk-run transition speed. *Journal of Experimental Biology* 200, 821–826. Resumen: https://ntrs.nasa.gov/citations/20040173033
- Neptune, R. R. & Sasaki, K. (2005). Ankle plantar flexor force production is an important determinant of the preferred walk-to-run transition speed. *Journal of Experimental Biology* 208, 799–808.
- Tudor-Locke, C. et al. (2019). Walking cadence (steps/min) and intensity in 21–40 year olds: CADENCE-adults. *International Journal of Behavioral Nutrition and Physical Activity* 16, 8.
- Fromuth, R. C. & Parkinson, M. B. (2008). — `74_Predicting_Segment_Lengths_from_Stature`. Altura del trocánter como fracción de la estatura.
- Koning, W. F. *Movement: Walk Cycle*. Monmouth University. https://animation.monmouth.edu/instruct/?p=351 — cita a Williams, `60_The_Animators_Survival_Kit`.

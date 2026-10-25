---
tipo: medicina
estado: En la Biblioteca
mision: EST-024_Mision_Morfologia_del_movimiento
consume: Arte, solo al fijar la escala de una persona o un humanoide, al escribir su hoja de referencia, al modelarlo o al ubicar las articulaciones de su rig
remite: Proporcion y estilizacion, RA-005_Blueprint_sin_cotas
cruza: 03_Masa_centro_de_masa_y_equilibrio, 04_Marcha_humana, 05_Carrera
---

# Medicina 02 — Proporciones del cuerpo

> Dónde está cada parte del cuerpo como fracción de la estatura, cuánto varía entre personas y entre sexos, qué es hito óseo y qué es centro articular, y cómo se escriben esas proporciones cuando el personaje no es realista.
> **No cubre:** el criterio de proporción como identidad ni la escala de estilización del elenco (`Proporcion y estilizacion`). Esa nota decide qué proporción quiere el juego; este libro da los números del cuerpo real desde los que se parte.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Qué decisión sostiene

El Director de Escala fija la dimensión maestra; el Analista de Referencia lee una medida en dos vistas; la hoja de referencia pide líneas guía horizontales "a la altura de cada parte clave"; el Modelador construye y el rig ubica cada hueso. Hasta hoy esas alturas se ponían a ojo, y las líneas guía de la hoja eran una hipótesis sin números. Este libro las da como fracción de la estatura, con fuente, y separa lo que es medida de silueta de lo que es posición de una articulación.

---

## Modelo

**Una estatura y fracciones.** Cada altura de referencia del cuerpo es una fracción fija de la estatura H, y esa fracción varía poco entre personas: alrededor de la mediana, el rango del percentil 5 al 95 se aparta ±0.3–1.3% de H; el tobillo es lo que menos varía y el trocánter lo que más (Fromuth y Parkinson 2008). Se elige H y se multiplica.

**Los sexos se diferencian a lo ancho.** Las fracciones de altura de varones y mujeres difieren en menos de 0.008 de H; lo que cambia es el ancho: hombros más anchos en varones, caderas más anchas en mujeres (Gordon 2014; Fromuth y Parkinson 2008).

**Los percentiles no se suman.** Una persona del percentil 95 de estatura no está hecha de segmentos del percentil 95. Para un personaje se usan las fracciones medianas y se escala H; no se arma un cuerpo "grande" segmento por segmento (Fromuth y Parkinson 2008).

**Hito óseo no es centro articular.** Las alturas de la tabla son de hitos que se palpan: el acromion, el trocánter, el epicóndilo lateral de la rodilla, el maléolo lateral. Sirven para la silueta y las líneas guía, y aproximan dónde va el eje de una articulación, pero no son ese eje. "Cadera" en este libro nombra tres cosas distintas, y se dice cuál: el trocánter (hito lateral), el centro de la cabeza del fémur (centro articular) y el ancho de caderas (silueta, con tejido blando).

**Para adultos, esta tabla; para chicos, ninguna escalada.** Las fracciones clásicas de Drillis y Contini, que reproducen los manuales, nunca se validaron para una población concreta, y en chicos fallan: subestiman brazo y antebrazo y sobreestiman el ancho de hombros (OPEN Design Lab; Wisner 2006). Un adulto usa la tabla de este libro, que sale de ANSUR; un personaje infantil necesita datos con edad, y escalar cualquiera de las dos no los reemplaza.

---

## Parámetros

Fracciones de la estatura H. Alturas desde el piso, de pie. ANSUR II es la encuesta de 2012 (Gordon 2014, mediana); ANSUR 1988 es la que usan Fromuth y Parkinson (2008).

| Parte | Varón | Mujer | Rango (percentil 5–95) | Condición | Fuente |
|---|---|---|---|---|---|
| Estatura | 175.5 cm | 162.6 cm | civiles: 175.5 / 161.3 cm | mediana militar; civiles de 20 años o más | (Gordon 2014; Fryar 2021) |
| Ojos | 0.934 | 0.933 | — | ANSUR II | (Gordon 2014) |
| Hombro (acromion) | 0.820 | 0.819 | V 0.814–0.827 · M 0.814–0.823 | hito óseo; ANSUR II (rango de ANSUR 1988) | (Gordon 2014; Fromuth y Parkinson 2008) |
| Codo, de pie | 0.617 | 0.616 | — | línea de silueta: borde inferior del codo (inferido), no el eje | (Gordon 2014) |
| Trocánter mayor | 0.527 | 0.528 | V 0.518–0.540 · M 0.517–0.539 | hito lateral de la cadera; ANSUR 1988 | (Fromuth y Parkinson 2008) |
| Nudillos, brazo caído | 0.417 | 0.422 | — | ANSUR II | (Gordon 2014) |
| Rodilla (epicóndilo lateral) | 0.285 | 0.283 | V 0.280–0.292 · M 0.276–0.290 | hito óseo; ANSUR 1988 | (Fromuth y Parkinson 2008) |
| Tobillo (maléolo lateral) | 0.038 | 0.037 | V 0.036–0.041 · M 0.034–0.040 | hito óseo; ANSUR 1988 | (Fromuth y Parkinson 2008) |
| Brazo (acromion a radial) | 0.194 | 0.191 | — | ANSUR 1988 | (Fromuth y Parkinson 2008) |
| Antebrazo (radial a estiloides) | 0.153 | 0.149 | — | ANSUR 1988 | (Fromuth y Parkinson 2008) |
| Mano | 0.110 | 0.111 | 0.108–0.113 | ANSUR II y 1988 | (Gordon 2014; Fromuth y Parkinson 2008) |
| Muslo (trocánter a rodilla) | 0.242 | 0.245 | — | resta de hitos de ANSUR 1988 | derivado de (Fromuth y Parkinson 2008) |
| Segmento pierna (rodilla a tobillo) | 0.247 | 0.246 | — | ídem | derivado de (Fromuth y Parkinson 2008) |
| Pie | 0.154 | 0.150 | — | ANSUR II | (Gordon 2014) |
| Envergadura | 1.032 | 1.019 | — | ANSUR II | (Gordon 2014) |
| Hombros, ancho de hueso (biacromial) | 0.236 | 0.224 | — | esqueleto | (Gordon 2014) |
| Hombros, ancho con músculo (bideltoideo) | 0.290 | 0.277 | — | silueta | (Gordon 2014) |
| Caderas, ancho máximo | 0.196 | 0.217 | — | silueta, con tejido blando | (Gordon 2014) |
| Cabeza, largo (frente a nuca) | 0.114 | 0.117 | — | ANSUR II | (Gordon 2014) |
| Cabeza, ancho | 0.088 | 0.090 | — | ANSUR II | (Gordon 2014) |
| Cabeza, alto (coronilla a mentón) | ≈0.13 | ≈0.13 | — | 7.5 cabezas en la estatura | derivado de (Loomis 1943) |

---

## Relaciones

```txt
altura de una parte    y = f · H                     f de la tabla
largo de un segmento   resta de dos alturas, SOLO del mismo juego de datos
                       muslo = 0.527 − 0.285 = 0.242 · H   (trocánter y rodilla, ANSUR 1988)
unidad cabeza          h = H / N                     N = cabezas que mide el personaje
L (largo de pierna)    altura del trocánter = 0.527 · H   (la usan 03, 04 y 05)
```

La resta no se hace entre juegos distintos: hombro de ANSUR II menos codo de pie da 0.203 · H, porque el codo de pie es el borde inferior del codo, no su eje (derivado de Gordon 2014). Para el codo, acromion menos brazo dentro de ANSUR 1988 da la altura del radial, ≈0.627 · H, que aproxima el eje sin ser el eje (derivado de Fromuth y Parkinson 2008).

Ejemplos para un varón de 1.75 m: hombro a 1.435 m (derivado de Gordon 2014), trocánter a 0.922 m, rodilla a 0.499 m, tobillo a 0.067 m (derivado de Fromuth y Parkinson 2008).

**La mitad de la estatura** cae 0.027 · H, unos 5 cm, por debajo del trocánter (derivado de Fromuth y Parkinson 2008). La altura del pubis no se midió.

**Envergadura ≈ estatura**, con un 2–3% de más (Gordon 2014).

**Hombros contra caderas, en la silueta** (bideltoideo sobre ancho de caderas): 1.48 en varones y 1.27 en mujeres (derivado de Gordon 2014). Para el esqueleto se compararía el ancho de hueso de hombros con el de la pelvis, que no se leyó.

**Centro de la cadera para el rig** (Hara 2016). En milímetros, con origen en el punto medio entre las dos espinas ilíacas anterosuperiores, X hacia adelante, Y hacia afuera, Z hacia arriba —los ejes de Hara, no los del programa: en Blender lo lateral es X—, y LL = largo del miembro inferior, de la espina ilíaca al maléolo interno pasando por el epicóndilo interno de la rodilla (no el segmento pierna de la tabla):

```txt
X = 11 − 0.063 · LL        Y = 8 + 0.086 · LL        Z = −9 − 0.078 · LL
LL = 900 mm  →  (−46, ±85, −79) mm
```

Error absoluto medio de 3.8 a 5.2 mm según el eje (Hara 2016). Como la tabla no da la altura de las espinas ilíacas, al rig entra solo Y: con LL ≈ 900 mm, supuesto para un adulto de 1.75 m, cada centro queda a ≈0.05 · H de la línea media, y entre los dos hay ≈0.10 · H (derivado de Hara 2016; con LL entre 850 y 950 mm da 0.046–0.051 · H por lado).

---

## Estilización

**Cánones de dibujo** (Loomis 1943): 7.5 cabezas es la figura normal, que en dibujo se ve achaparrada; 8 es el ideal académico; 8.5 el de moda; 9 el heroico. El alargamiento es una decisión de estilo, no de anatomía.

**Por edad**, en el canon ideal de Loomis (adulto = 8): alrededor de 4 cabezas al año, 5 a los 3 años, 6⅜ a los 10 y 7¼ a los 15 (Loomis 1943, leído por reconocimiento de texto: confirmar en la lámina antes de usarlo como medida). Sirve como gradiente para que un personaje se lea más joven.

**Chibi**, de 2 a 4 cabezas (ArtRocket 2019, tutorial de Clip Studio): a 2 cabezas el cuello puede desaparecer, brazos y piernas se engrosan y la mano se simplifica en dos formas.

**En un estilizado, las alturas no salen de f · H.** Pasar las fracciones reales a cabezas pone el hombro de un chibi de 2 cabezas a 1.64 cabezas del piso, adentro de la cabeza (derivado de Gordon 2014). Las alturas de un estilizado las fija, en cabezas, la referencia aprobada del personaje (`Proporcion y estilizacion`); f · H vale para el realista.

**Qué se conserva al deformar** no tiene fuente encontrada, y por eso se decide en el encargo. Un ejemplo de lo que hay que decidir: en una persona real el brazo entero —brazo, antebrazo y mano— mide unos 0.45 de H y la cabeza 0.13; en un chibi de 2 cabezas, si el cuerpo conserva sus proporciones internas, el brazo mide un cuarto de H y no llega a la coronilla (derivado de Fromuth y Parkinson 2008, Gordon 2014 y Loomis 1943). Si el personaje tiene que poder tocarse la cabeza, se escribe antes de modelarlo.

---

## Medible y juicio

```txt
se mide     la altura de cada parte del modelo contra f · H, con el rango 5–95 de su sexo como
            tolerancia; donde no hay rango con fuente, se reporta la desviación sin umbral
            la misma medida en dos vistas de la referencia (Analista de Referencia, RA-005_Blueprint_sin_cotas)
            el alto total y la línea de piso con arte.malla() (ley 3: la medida es real)
se juzga    el canon: cuántas cabezas mide el personaje es dirección de arte, no anatomía
```

---

## Al encargo

```txt
ESCALA        estatura real del personaje en metros, y su canon en cabezas
LÍNEAS GUÍA   realista: horizontales a la altura de ojos 0.93 · hombro 0.82 · codo de silueta
              0.62 · trocánter 0.53 · nudillos 0.42 · rodilla 0.285 · tobillo 0.04 (fracciones
              de H). Los números ubican las líneas; en una hoja generada no se rotulan: sin cotas
              (RA-005_Blueprint_sin_cotas). Estilizado: las alturas salen, en cabezas, de la
              referencia aprobada
RIG           cadera: cada centro a ≈0.05 · H de la línea media; su altura no tiene número con
              fuente (el trocánter, 0.53, es un hito lateral, no el centro). Codo, rodilla y
              tobillo: a la altura del radial (≈0.63 · H de pie), del epicóndilo lateral (0.285)
              y del maléolo lateral (0.04 · H), que aproximan el eje sin ser el eje. Hombro: el
              acromion a 0.82 · H; el
              centro del hombro queda abajo y adentro, sin número con fuente
SILUETA       hombros con músculo contra caderas: 1.48 en varones, 1.27 en mujeres
ESTILIZADO    declarar qué alcances se conservan: ¿la mano llega a la cabeza, a la cintura, al
              suelo agachado?
```

Las fracciones del bloque son las de la tabla (Gordon 2014; Fromuth y Parkinson 2008); el 0.05 y el 0.63 son derivados de Relaciones (Hara 2016; Fromuth y Parkinson 2008).

---

## Límites

- Población adulta de Estados Unidos: militar en ANSUR II (2012) y ANSUR 1988, civil en NHANES. Otras poblaciones difieren en estatura más que en fracciones; no se midió en esta misión.
- **No verificados en esta misión:** el alto de la cabeza medido en población (el 0.13 es derivado), la altura del mentón y del pubis, la altura del centro de la cadera, el desplazamiento del centro del hombro respecto del acromion, la posición del eje del codo, de la rodilla y del tobillo respecto de sus hitos, el ancho de hueso de la pelvis, y las proporciones por edad en datos de crecimiento.
- Chicos: esta tabla no sirve. Mayores: cambian la postura y la estatura; tampoco se cubren.

---

## Fuentes

- Gordon, C. C. et al. (2014). *2012 Anthropometric Survey of U.S. Army Personnel: Methods and Summary Statistics* (ANSUR II). NATICK/TR-15/007. Leído en las tablas resumen de la Ergonomics Center de North Carolina State University (mediana). — `80_ANSUR_II`.
- Fromuth, R. C. & Parkinson, M. B. (2008). Predicting 5th and 95th percentile anthropometric segment lengths from population stature. ASME IDETC/CIE, DETC2008-50091. — `74_Predicting_Segment_Lengths_from_Stature`.
- Fryar, C. D. et al. (2021). Anthropometric reference data for children and adults: United States, 2015–2018. *Vital and Health Statistics* 3(46). NCHS.
- OPEN Design Lab, Penn State. *Design Tools: Proportionality Constants Guidelines*. https://www.openlab.psu.edu/design-tools-proportionality-constants/
- Wisner, D. M. et al. (2006). Upper body segment lengths as a proportion of height in children. ISBS 2006.
- Hara, R., McGinley, J., Briggs, C., Baker, R. & Sangeux, M. (2016). Predicting the location of the hip joint centres, impact of age group and sex. *Scientific Reports* 6, 37707. CC BY 4.0. Ecuaciones confirmadas en el manuscrito del repositorio de la Universidad de Salford.
- Loomis, A. (1943). *Figure Drawing for All It's Worth*. Viking Press. — `79_Figure_Drawing_for_All_Its_Worth`.
- ArtRocket (2019). *Easy steps to creating chibi characters*. Clip Studio Tips, Celsys. https://clipstudio.net/how-to-draw/archives/155423

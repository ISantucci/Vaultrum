---
tipo: medicina
estado: En la Biblioteca
mision: EST-024_Mision_Morfologia_del_movimiento
consume: Arte, solo al encargar, animar o revisar una pose con peso de una persona o un humanoide: quieto, en un pie, cargando, empujando, tirando o perdiendo el equilibrio
remite: Principios de animacion
cruza: 02_Proporciones_del_cuerpo, 04_Marcha_humana, 06_Salto_y_aterrizaje
---

# Medicina 03 — Masa, centro de masa y equilibrio

> Dónde está el peso del cuerpo, cuándo una pose se sostiene y cuándo se cae, y cómo se reacomoda el cuerpo para cargar, empujar o recuperar el equilibrio.
> **No cubre:** el peso como cualidad de animación —anticipación, compresión, timing—, que es de `Principios de animacion`. Tampoco caer desde una altura y aterrizar: eso es `06_Salto_y_aterrizaje`. Este libro da la física que hace que una pose "tenga peso" o no.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Qué decisión sostiene

Una pose de idle, un apoyo en una pierna, un personaje que carga una caja o empuja una puerta se ven bien o se ven a punto de caerse por una razón: dónde cae la vertical del centro de masa respecto de los pies. Hasta hoy Arte lo decidía a ojo en el encargo y en la revisión. Este libro da dónde está ese centro, cuánto margen tiene el cuerpo real y cómo se mueve el resto para compensar.

---

## Modelo

**El centro de masa es un promedio.** Cada segmento tiene su fracción de la masa total y su centro a una fracción fija de su largo, medida desde su extremo **proximal** —el más cercano al tronco: hombro, codo, muñeca, cadera, rodilla, tobillo—, sea cual sea la pose; el centro del cuerpo es el promedio ponderado (Duarte, BMClab, a partir de Winter 2009 y de Leva 1996). Cabeza, brazos y tronco juntos son el 68% de la masa (Winter 2009): mover el tronco es mover el centro de masa. Un miembro inferior entero es un 16–21%, así que levantarlo lo corre mucho. Un brazo entero es un 5%, pero no es despreciable: estirarlo corre el centro del cuerpo unos 1.5 cm: nada en dos pies; en uno, si va hacia el costado, todo el margen, porque hacia adelante el pie es largo (que el borde más cercano sea el costado es lectura de esta misión; derivado de Winter 2009, Fromuth y Parkinson 2008 y Hof 2005, para 1.75 m).

**Dos tablas, dos poblaciones.** La de Dempster salió de cadáveres de varones mayores; la de de Leva, de personas jóvenes vivas, y le da al muslo bastante más masa y al tronco y la cabeza menos (Duarte, BMClab). Para un personaje joven y atlético conviene de Leva. Las dos definen los segmentos entre puntos distintos, por eso se usa una tabla entera, con sus masas, sus centros y sus extremos, nunca filas de las dos.

**Equilibrio quieto.** Un cuerpo quieto está en equilibrio si la vertical de su centro de masa cae dentro de la base de sustentación, el polígono que encierran sus apoyos (Hof 2005). De pie, esa vertical cae 4–5 cm por delante de los tobillos: la persona está apenas inclinada hacia adelante (Hellebrandt, citado por Opala-Berdzik 2010).

**El margen real es chico.** Parado en dos pies, la menor distancia del cuerpo hasta el borde más cercano de su base es de unos 6 cm; en un pie, 1.5 cm; en un pie en puntas, ninguna: sale y vuelve con correcciones continuas (Hof 2005). En una pose en un pie, el centro de masa va prácticamente encima del pie de apoyo.

**En movimiento no alcanza con la posición.** Lo que tiene que quedar dentro de la base es el *centro de masa extrapolado*: la posición más la velocidad dividida por una frecuencia propia del cuerpo (Hof 2005). Un cuerpo que se mueve rápido hacia el borde ya tiene el extrapolado afuera aunque su centro de masa esté adentro. Si el extrapolado sale, la única salida es mover la base: dar un paso.

**Alto no es inestable; es más sensible.** Con el centro más alto, el péndulo equivalente es más largo y el mismo movimiento lleva el extrapolado más lejos: la pose sigue en equilibrio si está quieta, pero aguanta menos un empujón o un movimiento (derivado de Hof 2005). Y cuánto aguanta no es lo mismo que cuánto tarda en caer: eso lo da el tamaño (Relaciones).

**Recuperar el equilibrio** se hace con el tobillo (el cuerpo pivotea entero), con la cadera (tronco y piernas en contrafase) o con un paso (Horak y Nashner 1986, citado por Vlutters 2018).

**Caerse.** Desde que se pierde el equilibrio hasta el impacto pasan unos 0.7 s, como mucho 0.75 (Hsiao y Robinovitch 1998, citado por Le Goic 2018). Los músculos se activan desde los 0.06 s, pero no cambian la trayectoria hasta los 0.3 s: hasta ahí el cuerpo cae en bloque, sin reacción visible (Le Goic 2018). Un instante de rigidez antes de la reacción es fisiológico, no un error de animación.

**En una pierna.** Con casi todo el peso en una pierna, si los abductores de la cadera de apoyo no la sostienen, la pelvis cae del lado de la pierna libre y el tronco se inclina hacia la de apoyo para compensar (StatPearls, *Trendelenburg sign*). El contrapposto relajado se parece a esa postura hecha a propósito; la equivalencia es una lectura de esta misión, no una medición.

**Cargar.** El centro que tiene que caer en la base es el combinado: cuerpo más carga. Caminando con una carga en una mano, las piernas se inclinan hacia el lado libre, y el tronco no siempre hacia el lado opuesto a la carga, como pide la regla de dibujo (Zhang, Ye y Wang 2010). Con mochila el tronco se inclina hacia adelante, más caminando que parado (Singh y Koh 2009, en niños de 9 a 10 años).

**Empujar y tirar.** La fuerza horizontal sale del rozamiento entre suela y piso. Al empujar, el cuerpo se inclina pivoteando sobre el pie de atrás, y cuanto más cerca está lo que se empuja, más largo es el paso (Chen, Lee y Hsu 2011).

---

## Parámetros

**Tabla de Dempster** (Winter 2009, vía Duarte): masa como fracción del total; centro como fracción del largo desde el extremo proximal.

| Segmento | Masa | Centro | Extremos del segmento | Condición | Fuente |
|---|---|---|---|---|---|
| Cabeza y cuello | 0.081 | a la altura del conducto auditivo | de C7–T1 al conducto auditivo | varones mayores | (Winter 2009) |
| Tronco | 0.497 | 0.50 | del trocánter mayor al hombro | ídem | (Winter 2009) |
| Brazo | 0.028 | 0.436 | del hombro al codo | ídem | (Winter 2009) |
| Antebrazo | 0.016 | 0.430 | del codo a la muñeca | ídem | (Winter 2009) |
| Mano | 0.006 | 0.506 | de la muñeca al nudillo del índice | ídem | (Winter 2009) |
| Muslo | 0.100 | 0.433 | del trocánter mayor a la rodilla | ídem | (Winter 2009) |
| Pierna | 0.0465 | 0.433 | de la rodilla al maléolo interno | ídem | (Winter 2009) |
| Pie | 0.0145 | 0.50 | del maléolo lateral a la cabeza del 2º metatarsiano | ídem | (Winter 2009) |
| Cabeza + brazos + tronco | 0.678 | — | todo lo que está arriba de la cadera | ídem | (Winter 2009) |

**Tabla de de Leva** (de Leva 1996, vía Duarte; jóvenes: 100 varones y 15 mujeres, datos de Zatsiorsky y Seluyanov): varón / mujer; el centro se mide desde el extremo indicado.

| Segmento | Masa V / M | Centro V / M | Medido desde | Hasta | Fuente |
|---|---|---|---|---|---|
| Cabeza | 0.069 / 0.067 | 0.598 / 0.589 | la coronilla | el punto medio de los ángulos de la mandíbula | (de Leva 1996) |
| Tronco | 0.435 / 0.426 | 0.449 / 0.415 | el borde superior del esternón | el punto medio entre los dos centros de cadera | (de Leva 1996) |
| Brazo | 0.027 / 0.026 | 0.577 / 0.575 | el centro del hombro | el centro del codo | (de Leva 1996) |
| Antebrazo | 0.016 / 0.014 | 0.457 / 0.456 | el centro del codo | el centro de la muñeca | (de Leva 1996) |
| Mano | 0.006 / 0.006 | 0.790 / 0.747 | el centro de la muñeca | el nudillo del dedo medio (extremo distal del 3er metacarpiano) | (de Leva 1996) |
| Muslo | 0.142 / 0.148 | 0.410 / 0.361 | el centro de la cadera | el centro de la rodilla | (de Leva 1996) |
| Pierna | 0.043 / 0.048 | 0.440 / 0.435 | el centro de la rodilla | el centro del tobillo | (de Leva 1996) |
| Pie | 0.014 / 0.013 | 0.442 / 0.401 | el talón | la punta del dedo más largo | (de Leva 1996) |

En la fuente cada columna de masa suma 1 contando dos brazos y dos piernas; acá van redondeadas.

**Cuerpo entero:**

| Parámetro | Valor | Rango | Condición | Fuente |
|---|---|---|---|---|
| Altura del centro de masa, de pie | 0.567 · H (varones) · 0.561 · H (mujeres) | hasta 0.575 · H en adultos mayores | adultos | (Swearingen y Young 1965, citando a Cotton; Narciso 2010) |
| Vertical del centro de masa | 4–5 cm delante de los tobillos | — | de pie, quieto | (Hellebrandt, citado por Opala-Berdzik 2010) |
| Margen mínimo hasta el borde más cercano: dos pies | 64 mm | DE 8 mm | quieto, ojos abiertos | (Hof 2005) |
| Margen mínimo: un pie | 15.5 mm | DE 6 mm | ídem | (Hof 2005) |
| Margen mínimo: un pie en puntas | −9 mm: sale por momentos | DE 14 mm | ídem | (Hof 2005) |
| Margen al caminar | 2–3 cm | — | lateral | (Hof 2005) |
| Péndulo equivalente l, adelante–atrás | 1.20–1.24 × altura del trocánter | — | 1.20 con el tronco vertical, 1.24 con el tronco acompañando a las piernas | (Hof 2005) |
| Péndulo equivalente l, lateral | 1.34 × altura del trocánter | — | — | (Hof 2005) |
| Caída de pie hasta el impacto | ≈0.7 s | hasta 0.75 s | tras una perturbación | (Hsiao y Robinovitch 1998, citado por Le Goic 2018) |
| Caída sin reacción visible | 0.3 s | músculos activos desde 0.06 s | ídem | (Le Goic 2018) |
| Empuje / tracción máxima | 155–169 N / 135–148 N | — | isométrica, media por altura de manija, varones jóvenes de 70 kg de media, rozamiento 0.48 | (Chen, Lee y Hsu 2011) |
| Altura de máxima fuerza para empujar o tirar | 50–90 cm | entre rodilla y cadera | ídem | (Chen, Lee y Hsu 2011) |
| Efecto del rozamiento | +50% de empuje | de 0.3 a 0.6 de rozamiento | — | (Kroemer 1974, citado por Chen, Lee y Hsu 2011) |

---

## Relaciones

```txt
centro de un segmento     r = r_prox + k · (r_dist − r_prox)      k y extremos de UNA de las tablas
centro del cuerpo         r_CM = Σ(m_i · r_i) / Σ m_i              (Duarte, BMClab)
equilibrio quieto         la vertical de r_CM cae dentro de la base
centro extrapolado        ξ = x + v / ω0,   ω0 = √(g / l)           (Hof 2005)
equilibrio en movimiento  ξ dentro de la base; si sale, hace falta un paso
```

**l es un péndulo equivalente**, que incluye la inercia del cuerpo: es más largo que la altura del centro de masa y no es la L de `04_Marcha_humana`. Con 1.22 × el trocánter de 0.527 · H (`02_Proporciones_del_cuerpo`), l ≈ 0.64 · H, unas 1.13 veces la altura del centro de masa. Un adulto de 1.75 m tiene `1/ω0 ≈ 0.34 s`: es la escala de tiempo de su equilibrio (derivado de Hof 2005 y Fromuth y Parkinson 2008).

**Tamaño y tiempo** (derivado de ω0 = √(g/l)): la escala de tiempo crece con la raíz del tamaño. Un personaje de 1 m tiene `1/ω0 ≈ 0.26 s`; uno de 3 m, `≈ 0.44 s`. Si se escala también la caída medida, el impacto llega a `0.7 · √(H / 1.75)` s: unos 0.53 s para 1 m. Los 0.3 s sin reacción visible son latencia del sistema nervioso, no mecánica: escalarlos es una decisión que se declara. En un estilizado, l se toma como ≈1.13 × la altura de su centro de masa visual: convención de esta misión, con la razón del adulto (Hof 2005; Swearingen y Young 1965).

**Inclinarse para empujar** (derivado de un modelo rígido apoyado en el pie de atrás; θ es el ángulo de la recta pie de atrás–centro de masa respecto de la vertical, no del tronco):

```txt
tan θ ≈ (F / W) · (h_manos / h_CM)          F = fuerza horizontal, W = peso
θ máximo ≈ atan(μ · h_manos / h_CM)          μ = rozamiento suela–piso
manos a la altura del centro: μ 0.3 → 17°   μ 0.48 → 26°   μ 0.6 → 31°
empuje fuerte (160 N, 70 kg, F/W ≈ 0.23): manos a la altura del centro → θ ≈ 13°;
manos a 50–90 cm en un adulto de 1.75 m → θ ≈ 7–12°; manos a 1.3 m (una puerta a la altura
del pecho) → θ ≈ 17°, con tope de 32° para μ 0.48
```

Tirar es lo mismo hacia atrás.

**Cargar en una mano** (derivado): el centro combinado se corre `m_carga · d / (M + m_carga)`, con d la distancia de la mano a la línea media. Para recentrarlo, el cuerpo se corre hacia el otro lado unos `m_carga · d / M`: con la mano a 0.25 m, 2.5 cm para una carga del 10% del peso y 5 cm para una del 20%. Cuanto más cerca del cuerpo va la carga, menos hay que compensar.

---

## Estilización

**El equilibrio se juzga con la masa visual.** No hay fuente sobre dónde está el centro de masa de un personaje cabezón. La hipótesis de esta misión: el espectador juzga el equilibrio por la masa que ve, así que la vertical que tiene que caer en la base es la del centro de la masa aparente, cabeza grande incluida. Si la cabeza pesa lo que pesa en una persona, un chibi tiene el centro de masa más bajo que un adulto; si se le asigna peso en proporción a su tamaño, el centro sube y la pose se vuelve más sensible:

```txt
                    peso de la cabeza →   0.08 (real)   0.25    0.50
altura del centro, 3 cabezas                 0.44 H      0.51 H   0.62 H
altura del centro, 4 cabezas                 0.49 H      0.56 H   0.67 H
```

Cálculo de esta misión con la distribución humana para el cuerpo bajo el mentón (derivado de Winter 2009); es una hipótesis de diseño, no un hallazgo. Lo que dice para el encargo: un cabezón que tiene que verse estable necesita una base más ancha, pies más separados.

---

## Medible y juicio

```txt
se mide     el centro de masa de una pose 3D con UNA de las tablas, y su vertical contra el
            polígono de los pies. Hoy no hay instrumento del vault que lo haga: es un hueco, y el
            ART lo dice
            en un sprite, la vertical por el centro de la masa visible contra los pies
se juzga    si la pose se lee pesada, liviana o a punto de caerse
```

---

## Al encargo

```txt
MIEMBROS
  PIERNA        levantar un miembro inferior entero (16–21% de la masa) corre mucho el centro:
                el tronco y la pelvis van hacia el lado de apoyo
  BRAZO         un brazo entero es ≈5%: en dos pies no cambia nada; en un pie, estirado hacia el
                costado, se come el margen
POSES
  QUIETO        la vertical del centro de masa cae entre los pies, apenas delante de los tobillos
  UN PIE        el centro de masa encima del pie de apoyo: el margen real es de ≈1.5 cm
                (≈0.01 · H) hacia el borde más cercano, que en un pie es el costado (lectura de
                esta misión: hacia adelante el pie es largo)
  CONTRAPPOSTO  la pelvis cae del lado de la pierna libre; el tronco compensa hacia la de apoyo
                (lectura de esta misión)
  CARGA         el centro combinado, cuerpo más carga, vuelve sobre los pies. Caminando con una
                carga en una mano, las piernas se inclinan hacia el lado libre. Lo pesado, pegado
                al cuerpo (menos distancia, menos compensación)
  CABEZÓN       pies más separados para que se lea estable (hipótesis de esta misión)
TIEMPO
  CAERSE        desde parado, al perder el equilibrio: 0.3 s en bloque, sin reacción visible;
                impacto a los 0.7 s. Personaje de otro tamaño: impacto × √(H / 1.75); los 0.3 s
                no se escalan salvo que el ART lo declare. Caer desde una altura y aterrizar:
                06_Salto_y_aterrizaje
MOVIMIENTO
  EMPUJAR       la recta pie de atrás–centro de masa inclinada ≈ atan(fuerza / peso · h_manos /
                h_CM): unos 13° para un empujón fuerte con las manos a la altura del centro, unos
                17° con las manos a la altura del pecho; nunca más que atan(rozamiento · h_manos /
                h_CM). Pivotea sobre el pie de atrás
  TIRAR         igual, inclinado hacia atrás
  RECUPERAR     extrapolado adentro: tobillo (el cuerpo en bloque) o cadera (tronco y piernas en
                contrafase); extrapolado afuera: un paso
```

Los valores del bloque son los de las tablas y los derivados de Relaciones (Winter 2009; de Leva 1996; Hof 2005; Le Goic 2018; Chen, Lee y Hsu 2011).

## Límites

- Adultos. Las tablas segmentarias salen de pocas personas: varones mayores en Dempster, jóvenes en de Leva.
- **No verificados en esta misión:** que la vertical del centro de masa pase delante de la segunda vértebra sacra, la amplitud del balanceo en bipedestación tranquila, el ancho de pies preferido, los grados de inclinación de pelvis y hombros en el contrapposto, la inclinación del tronco con mochila en grados y los umbrales de las estrategias de tobillo y cadera.
- **Supuestos de la tabla de cabezones:** el conducto auditivo se tomó a la altura de los ojos, 0.93 · H (Gordon 2014, vía `02_Proporciones_del_cuerpo`), y el mentón humano a 0.87 · H, la fracción clásica de Drillis y Contini (1966) que esta misión no leyó en la fuente; se partió del centro del cuerpo entero a 0.56 · H (redondeo de 0.567 / 0.561, Swearingen y Young 1965) y se le restó la cabeza de Dempster.
- Las relaciones de empuje, carga y tamaño son física elemental derivada para este libro, no mediciones publicadas.

---

## Fuentes

- Duarte, M. *Body segment parameters* (cuaderno de BMClab, UFABC), con las tablas de Winter (2009, tabla 4.1, a partir de Dempster 1955) y de de Leva (1996). — `72_Body_Segment_Parameters`.
- Winter, D. A. (2009). *Biomechanics and Motor Control of Human Movement* (4ª ed.). Wiley. Leído vía Duarte.
- de Leva, P. (1996). Adjustments to Zatsiorsky-Seluyanov's segment inertia parameters. *Journal of Biomechanics* 29(9), 1223–1230. Leído vía Duarte.
- Hof, A. L., Gazendam, M. G. J. & Sinke, W. E. (2005). The condition for dynamic stability. *Journal of Biomechanics* 38, 1–8. — `73_Condition_for_Dynamic_Stability`.
- Fromuth, R. C. & Parkinson, M. B. (2008). — `74_Predicting_Segment_Lengths_from_Stature`. Altura del trocánter y largos de brazo.
- Swearingen, J. J. & Young, J. W. (1965). *Determination of centers of gravity of children, sitting and standing*. FAA Office of Aviation Medicine, AM 65-23. Cita los datos de adultos de Cotton.
- Narciso, F. V. et al. (2010). Center of gravity height and number of falls in active and sedentary older adults. *Revista Brasileira de Cineantropometria e Desempenho Humano* 12(4), 302. Resumen.
- Opala-Berdzik, A. et al. (2010). The influence of pregnancy on the location of the center of gravity in standing position. *Journal of Human Kinetics* 26. Cita a Hellebrandt.
- Le Goic, M. et al. (2018). An initial passive phase that limits the time to recover and emphasizes the role of proprioceptive information. *Frontiers in Neurology* 9, 986. Cita a Hsiao y Robinovitch (1998).
- Vlutters, M., van Asseldonk, E. H. F. & van der Kooij, H. (2018). Foot placement modulation diminishes for perturbations near foot contact. *Frontiers in Bioengineering and Biotechnology* 6, 48. Cita a Horak y Nashner (1986).
- Chen, Y. L., Lee, Y. C. & Hsu, T. C. (2011). Isometric push and pull strengths of young Taiwanese males. *Industrial Health* 49, 696–702.
- Zhang, X. A., Ye, M. & Wang, C. T. (2010). Effect of unilateral load carriage on postures and gait symmetry in ground reaction force during walking. *Computer Methods in Biomechanics and Biomedical Engineering* 13(3), 339–344. Resumen.
- Singh, T. & Koh, M. (2009). Effects of backpack load position on spatiotemporal parameters and trunk forward lean. *Gait & Posture* 29(1), 49–53. Resumen.
- StatPearls. *Trendelenburg sign*. NCBI Bookshelf.

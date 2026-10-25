---
tipo: medicina
estado: En la Biblioteca
mision: EST-024_Mision_Morfologia_del_movimiento
consume: Arte, solo al riggear una persona o un humanoide, al correr su prueba de poses o al revisar una pose extrema en un encargo
remite: Rigging y skinning, Huesos e influencias
cruza: 04_Marcha_humana, 05_Carrera, 07_Cadena_cinetica
---

# Medicina 01 — Anatomía del movimiento

> Cuánto se dobla cada articulación de una persona, cuáles se mueven juntas, cómo se pasa un ángulo anatómico a un hueso del rig y qué hacer cuando no hay número.
> **No cubre:** cuántos huesos entran en el presupuesto (`Huesos e influencias`) ni cómo se pesan los vértices (`Rigging y skinning`).
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Qué decisión sostiene

`Rigging y skinning` pide llevar al personaje a "las poses extremas que la animación va a pedir" antes de animar, con la rodilla al máximo como ejemplo, y no dice cuánto es el máximo. Hasta hoy ese máximo, y los límites de rotación de cada hueso, se ponían a ojo. Un rig sin límites deja que una animación —o un generador— doble una rodilla hacia atrás, y nadie lo ve hasta la plancha. Este libro da los rangos con fuente, los acoplamientos que un límite fijo no captura, y la regla para los huesos que no tienen número.

---

## Modelo

**Convención de ángulos.** 0° es la posición anatómica: de pie, brazos al costado, palmas hacia adelante, cada segmento alineado con el anterior; la flexión crece al doblar. La pronación y la supinación se cuentan desde el pulgar arriba (convención goniométrica estándar; el método de Soucie no se leyó). En "extensión más allá de recto", un valor negativo quiere decir que no llega a recto; Roaas y Andersson (1982) anotan la hiperextensión en negativo, al revés que Soucie (2011).

**Del ángulo anatómico al hueso del rig.** La tabla mide desde la posición anatómica; un límite de hueso se mide desde la pose de reposo del rig, que en un juego suele ser T o A. El límite del hueso es el valor de la tabla menos lo que el hueso ya tiene girado en reposo: en pose T el brazo ya está a unos 90° de elevación lateral. En un rig espejado, rotación interna y externa, y pronación y supinación, cambian de signo entre `.L` y `.R` (consecuencia de la simetría, no de una fuente).

**Grados de libertad que el rig tiene que respetar** (anatomía estándar; sin fuente leída en esta misión, salvo donde se cita):

```txt
hombro      complejo: la glenohumeral (3) más la escápula, que rota sobre el tórax al subir el brazo
codo        bisagra (1): flexión y extensión
antebrazo   (1) aparte del codo y de la muñeca: pronación y supinación, el radio gira sobre el cúbito
muñeca      (2): flexión y extensión, desviación radial y cubital. No rota: la mano gira porque
            gira el antebrazo
cadera      (3)
rodilla     (1) principal. Rota sobre su eje solo flexionada, y al terminar de extenderse la tibia
            rota sola hacia afuera (screw-home)
tobillo     flexión dorsal y plantar; la inversión y la eversión son del pie
```

De ahí, tres consecuencias de rig: un hueso de clavícula o escápula conducido por la elevación del brazo (Scibek y Carcia 2012); la rotación de la mano en el antebrazo, no en la muñeca; y la rotación axial de la rodilla bloqueada con la pierna estirada (Kim 2015).

**Un rango es un default, no un límite universal.** Casi todos los rangos bajan con la edad, las mujeres tienen más que los varones en la mayoría de los movimientos, y un chico de 2 a 8 años tiene bastante más extensión de cadera, flexión de rodilla y flexión dorsal que un adulto (Soucie 2011). Soucie midió movimiento pasivo en 674 personas (Soucie 2011): es el techo; un gesto voluntario queda por debajo.

---

## Parámetros

Adultos de 20 a 44 años salvo que se indique. Grados. Una celda "usar el de varón" es un dato que solo existe para varones. Para un humanoide sin sexo, la columna Varón, que es la de menor rango.

| Movimiento | Varón | Mujer | Rango (todas las edades o entre fuentes) | Condición | Fuente |
|---|---|---|---|---|---|
| Flexión de hombro (húmero contra tórax, con escápula) | 169° | 172° | 164–179° | pasivo | (Soucie 2011) |
| Flexión de codo | 145° | 150° | 144–153° | pasivo | (Soucie 2011) |
| Extensión de codo más allá de recto | 1° | 5° | −1 a 7° | negativo: no llega a recto | (Soucie 2011) |
| Pronación | 77° | 82° | 77–85° | desde el pulgar arriba | (Soucie 2011) |
| Supinación | 85° | 91° | 82–94° | ídem | (Soucie 2011) |
| Flexión de cadera | 130° | 134° | 113–134° | con la rodilla flexionada (inferido: Soucie no declara la posición; Roaas mide boca arriba con la otra cadera flexionada) | (Soucie 2011; Roaas y Andersson 1982, con la columna AAOS) |
| Extensión de cadera | 17° | 18° | 9–28° | la dispersión entre fuentes probablemente viene de cómo se fija la pelvis (no verificado) | (Soucie 2011; Roaas y Andersson 1982) |
| Abducción de cadera | 39° | usar el de varón | 39–48° | boca arriba, rodilla extendida, varones de 30 a 40 años | (Roaas y Andersson 1982) |
| Aducción de cadera | 31° | usar el de varón | 26–31° | ídem | (Roaas y Andersson 1982) |
| Rotación interna / externa de cadera | 33° / 34° | usar el de varón | interna 33–35°, externa 34–48° | boca abajo, rodilla flexionada | (Roaas y Andersson 1982) |
| Flexión de rodilla | 138° | 142° | 134–144° | — | (Soucie 2011; Roaas y Andersson 1982) |
| Hiperextensión de rodilla | 1° | 2° | hasta 10° en la tabla AAOS | — | (Soucie 2011; Roaas y Andersson 1982) |
| Flexión dorsal, pie apoyado: rodilla extendida / flexionada | 25° / 39° | 25° / 39° | DE 6–7° | ambos sexos, en estocada | (Baumbach 2014) |
| Flexión dorsal, pie en el aire: rodilla extendida / flexionada | 4° / 20° | 4° / 20° | DE 7–9° | ambos sexos | (Baumbach 2014) |
| Flexión dorsal, rodilla no declarada | 13° | 14° | 12–18° | no se usa como límite | (Soucie 2011; Roaas y Andersson 1982) |
| Flexión plantar | 55° | 62° | 40–62° | — | (Soucie 2011; Roaas y Andersson 1982) |
| Inversión / eversión del pie | 28° / 28° | usar el de varón | inversión 28–36°, eversión 19–28° | pasivo | (Roaas y Andersson 1982) |
| Ángulo de carga del codo | 11° | 13° | DE 4–5° | 1 a 18 años; crece hasta los 16 y se estabiliza | (Terra 2011) |
| Ritmo escapulohumeral global | 2.34 : 1 | 2.34 : 1 | por tramo, de 40 : 1 a 0.9 : 1 | ambos sexos, plano escapular, hasta 120° | (Scibek y Carcia 2012) |
| Screw-home de la tibia | 4–17° | 4–17° | según el método | ambos sexos, en los últimos 20° de extensión | (Kim 2015) |

**Niña o niño de 2 a 8 años** (Soucie 2011; varón / mujer): flexión de cadera 131 / 141° · extensión de cadera 28 / 26° · flexión de rodilla 148 / 153° · hiperextensión de rodilla 2 / 5° · flexión dorsal 23 / 25° · flexión plantar 56 / 67° · flexión de hombro 178 / 179° · flexión de codo 151 / 153° · extensión de codo 2 / 7° · pronación 80 / 85° · supinación 86 / 94°.

---

## Relaciones

**Escápula** (derivado de Scibek y Carcia 2012, medido en el plano escapular hasta 120°; la tabla de 170° es flexión sagital, así que el reparto es aproximado):

```txt
elevación total del brazo     30°     60°     90°    120°     170°
escápula acumulada           0.7°   11.7°   20.2°   36.0°    ≈51° (extrapolado)
hueso del brazo              29.3°  48.3°   69.8°   84.0°    ≈119° (extrapolado)
```

Por encima de 120° no hay dato: el reparto de 170° sale de la razón global, `170 · 2.34 / 3.34 ≈ 119°` al brazo y el resto a la escápula. El 2 : 1 constante de la literatura clásica (Inman 1944, citado por Scibek y Carcia 2012) es una aproximación.

**La flexión dorsal depende de la rodilla y de la carga** (Baumbach 2014). El gemelo cruza la rodilla y el tobillo; con la rodilla flexionada 20° ya no limita, y flexionar más no suma:

```txt
DF_max ≈ DF_ext + (DF_flex − DF_ext) · min(flexión de rodilla, 20°) / 20°
  pie apoyado (con carga):    DF_ext = 25°, DF_flex = 39°
  pie en el aire (sin carga): DF_ext = 4°,  DF_flex = 20°
```

La rampa lineal entre 0 y 20° es un supuesto de esta misión; los extremos son medidos. El tope del rig es el del pie apoyado: un agachado con los talones en el piso lo necesita.

**La flexión de cadera depende de la rodilla.** Los isquiotibiales cruzan la cadera y la rodilla: con la rodilla extendida la cadera flexiona bastante menos. Ese valor no se verificó en esta misión; los 130–134° de la tabla valen solo con la rodilla flexionada (Soucie 2011; Roaas y Andersson 1982).

**Screw-home** (derivado de Kim 2015), opcional:

```txt
rotación externa de la tibia = k · (20° − flexión de rodilla) / 20°   entre 0 y 20° de flexión
k entre 4° y 17° según el método de medición
```

**Ángulo de carga.** Con el codo extendido el antebrazo se abre 11–13° hacia afuera (Terra 2011): el eje de la bisagra del codo no es perpendicular al húmero.

**Pronación y supinación.** El arco total es de 162° en varones y 173° en mujeres adultos (derivado de Soucie 2011), repartido a lo largo del antebrazo. Cómo repartirlo entre huesos de torsión no tiene fuente encontrada.

---

## Estilización

**Los ángulos no escalan con el largo del segmento.** En un personaje de miembros cortos o cabeza grande cambian el alcance y las colisiones —el brazo contra la cabeza, el muslo contra la panza—, no el rango de la articulación. El límite efectivo es el menor entre el anatómico y el de colisión, medido en la pose extrema (inferencia de esta misión, sin fuente específica).

**Un personaje que se lee como chico** puede usar la fila de 2 a 8 años: más flexión de rodilla, más extensión de cadera y más flexión dorsal (Soucie 2011).

**Romper articulaciones a propósito** —un cuadro fuera de rango para que una pose se lea mejor— es práctica de animación cartoon que no se verificó en su fuente. Si se usa, se declara en el `ART` como decisión de estilo de ese clip, nunca como límite del rig.

---

## Medible y juicio

```txt
se mide      el ángulo de cada hueso en cada pose extrema, contado desde la pose de reposo,
             contra la tabla. Hoy no hay instrumento del vault que lo haga: es un hueco, y el
             ART lo dice
             las colisiones de la malla deformada en esas poses: arte.malla() (Rigging y skinning)
se juzga     si la pose se lee natural y si el volumen se sostiene, sobre el render de la pose;
             la pierna estirada al frente, que no tiene número
```

---

## Al encargo

```txt
RIG           límite del hueso = valor de la tabla − giro del hueso en la pose de reposo. En T el
              brazo ya tiene ≈90° de elevación: según la curva de Relaciones, ≈70° de brazo y ≈20°
              de escápula; del reposo al brazo arriba quedan ≈49° al hueso del brazo y ≈31° a la
              escápula, con el driver en cero en el reposo. La elevación lateral se aproxima con
              la flexión de la tabla. Signos de rotación axial espejados entre .L y .R.
              Columna del sexo del personaje; celda vacía: la de varón; sin sexo: Varón
HOMBRO        170° es el total húmero-tórax: hueso del brazo ≈119°, el resto a clavícula o
              escápula por driver con la curva de Relaciones, si el presupuesto (Huesos e
              influencias) admite ese hueso; si no, el ART lo declara
CODO          flexión V 145° / M 150°; hiperextensión V 1° / M 5°; eje de la bisagra inclinado
              para dar 11–13° de valgo con el brazo extendido
ANTEBRAZO     pronación V 77° / M 82°, supinación V 85° / M 91°; la muñeca sin rotación axial
RODILLA       flexión V 138° / M 142°; hiperextensión V 1° / M 2°; sin rotación axial con la
              pierna estirada (salvo el screw-home, si se usa)
TOBILLO       flexión dorsal con el tope del pie apoyado: 25° con la rodilla extendida → 39° con
              la rodilla flexionada 20° o más; flexión plantar V 55° / M 62°
CADERA        flexión 130–134° solo con la rodilla flexionada; extensión V 17° / M 18°. No usar
              el extremo bajo de un rango como límite (9° de extensión cortaría la carrera de
              05_Carrera, que llega a 12°)
PRUEBA DE POSES  cada articulación al límite de su rig: brazo arriba (≈170° húmero-tórax), codo,
              rodilla, cadera con la rodilla flexionada, pierna estirada al frente, pronación y
              supinación por separado, agachado con los talones apoyados, torso girado y muñeca
              al máximo hasta colisión, y las del encargo (Rigging y skinning). Si el personaje
              lanza por encima del hombro: rotación externa del hombro (no extensión) a
              165–175°, en el armado del lanzamiento. Si hace un swing con torsión:
              caderas–hombros ≈70° (medido en golfistas). Las dos son posiciones dinámicas de 07_Cadena_cinetica; para
              otros golpes, las del encargo. En cada una, arte.malla() sobre la malla deformada
ENCARGO 2D    ninguna rodilla ni ningún codo se dibuja doblado hacia atrás (los pocos grados de
              hiperextensión no se ven); la mano gira desde el antebrazo
SIN NÚMERO    muñeca, rotaciones del hombro, columna, flexión de cadera con la rodilla extendida,
              rotación de la rodilla flexionada y reparto de la pronosupinación entre huesos de
              torsión: se limitan por colisión y por la prueba de poses, y el ART lo declara
```

Los valores V / M del bloque son los de la tabla, adultos de 20 a 44 años (Soucie 2011); los 119° del brazo salen de Relaciones (derivado de Scibek y Carcia 2012).

---

## Límites

- Población adulta sana, mayormente de Estados Unidos (Soucie) y varones de 30 a 40 años (Roaas y Andersson).
- **No verificados en esta misión, y por eso fuera de la tabla:** muñeca, rotaciones del hombro, elevación lateral total del brazo, columna por regiones, rotación de la rodilla flexionada, flexión de cadera con la rodilla extendida, y cuánto rango se usa en las tareas cotidianas. De lo que se usa en movimiento: la rodilla al caminar está en `04_Marcha_humana`; cadera, rodilla y flexión plantar al correr, en `05_Carrera`; cadera y tobillo al caminar no se verificaron.
- **Los únicos números del estante para las rotaciones del hombro y del tronco son dinámicos** (rotación externa del hombro de 165–175° en el armado del lanzamiento —el «brazo atrás» de `07_Cadena_cinetica`, no una extensión— y caderas–hombros ≈70° en el swing): posiciones de un gesto que suma escápula, tronco y columna. No se usan como límite de un hueso; el rig tiene que permitirlas si el personaje las hace.
- Patologías, hiperlaxitud y deportistas de flexibilidad extrema: afuera.

---

## Fuentes

- Soucie, J. M. et al. (2011). Range of motion measurements: reference values and a database for comparison studies. *Haemophilia* 17(3), 500–507. Movimiento pasivo, 674 personas (resumen en Europe PMC). Tablas publicadas por el CDC: `79_Joint_Range_of_Motion_Study_CDC`.
- Roaas, A. & Andersson, G. B. J. (1982). Normal range of motion of the hip, knee and ankle joints in male subjects, 30–40 years of age. *Acta Orthopaedica Scandinavica* 53, 205–208. Su tabla 1 compara con la AAOS (1965) y con Boone y Azen (1979). https://actaorthop.org/actao/article/view/28654
- Baumbach, S. F. et al. (2014). The influence of knee position on ankle dorsiflexion — a biometric study. *BMC Musculoskeletal Disorders* 15, 246. https://pmc.ncbi.nlm.nih.gov/articles/PMC4118219/
- Kim, H. Y. et al. (2015). Screw-home movement of the tibiofemoral joint during normal gait: three-dimensional analysis. *Clinics in Orthopedic Surgery* 7(3), 303–309. https://pmc.ncbi.nlm.nih.gov/articles/PMC4553277/
- Scibek, J. S. & Carcia, C. R. (2012). Assessment of scapulohumeral rhythm for scapular plane shoulder elevation using a modified digital inclinometer. *World Journal of Orthopedics* 3(6), 87–94.
- Terra, B. B. et al. (2011). Evolution of the carrying angle of the elbow: a clinical and radiographic study. *Acta Ortopédica Brasileira* 19(2), 79–82.

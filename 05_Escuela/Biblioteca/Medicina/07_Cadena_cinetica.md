---
tipo: medicina
estado: En la Biblioteca
mision: EST-024_Mision_Morfologia_del_movimiento
consume: Arte, solo al encargar, animar o revisar un golpe, un lanzamiento, una patada o un blandir de una persona o un humanoide
remite: RA-011_Locomocion_por_apoyos, Principios de animacion, 02_Plataformero_2D, 61_Game_Anim
cruza: 01_Anatomia_del_movimiento
---

# Medicina 07 — Cadena cinética

> En qué orden se mueve el cuerpo cuando golpea, lanza o patea, cuánto dura la parte rápida y qué se puede comprimir en un juego sin que el golpe pierda peso.
> **No cubre:** el criterio de anticipación, continuación y arcos (`Principios de animacion`), ni el diseño del combate: preparación, actividad, recuperación, cancelaciones y el momento del daño se acuerdan con Game Design (`RA-011_Locomocion_por_apoyos`, regla 5). Este libro es el mecanismo que esos criterios imitan.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Qué decisión sostiene

Arte, al escribir POSES, TIEMPO y JUGABILIDAD de un encargo de ataque. Hasta hoy el orden en que se mueve el cuerpo, cuánto dura la parte rápida y qué se puede recortar para que el jugador sienta respuesta se decidían a ojo. Este libro responde con lo que el cuerpo real conserva y lo que cambia.

---

## Modelo

**Convención.** Los porcentajes del lanzamiento son de un intervalo fijo: del apoyo del pie delantero (0%) a soltar la pelota (100%), como los da Seroyer (2010). "Pico" es el máximo de **velocidad** de giro de un segmento, no su posición extrema; cuando se habla de una posición, se dice.

**Del centro a la punta.** En un lanzamiento, los giros llegan a su velocidad máxima en orden: primero la pelvis, después el tronco, después el codo, y la rotación interna del brazo apenas después de soltar; cada uno más rápido que el anterior (Seroyer 2010). La inclinación del tronco hacia adelante es otra cosa: llega a su pico tarde, al soltar (Seroyer 2010). En un dibujo, el pico de velocidad es el cuadro con el mayor espaciado de ese segmento.

**El segmento que hace pico primero frena mientras el siguiente acelera**, en parte porque el siguiente tira de él. En la patada, el muslo llega a su pico, frena, y la pierna sale despedida (Kellis y Katis 2007, citando a Putnam 1991). En el cuadro de impacto, la pelvis y el giro del tronco ya pasaron su pico.

**El pie de adelante arranca la parte rápida.** En el lanzamiento, todo lo anterior al apoyo del pie delantero es preparación lenta; desde ese apoyo hasta soltar pasan 0.145 s (Seroyer 2010, citando a Stodden 2008). Si el pie cae cerrado limita el giro de la pelvis; si cae abierto, la pelvis gira antes de tiempo y el brazo queda atrasado (Seroyer 2010).

**La preparación es una torsión.** Con el peso atrás, pelvis y hombros giran alejándose del objetivo, los hombros más que la pelvis; al arrancar, la pelvis gira primero hacia el objetivo y los hombros quedan atrás (Turner, Baker y Miller 2011). Esa separación entre caderas y hombros es la anticipación real del tronco; en golfistas hábiles llega a unos 70° (Cole y Grimshaw 2009, citando a Burden 1998).

**La forma no cambia con el nivel; la velocidad sí.** Comparando 231 lanzadores, de juveniles a profesionales, casi todas las posiciones y los seis parámetros de tiempo fueron iguales en todos los niveles, y las velocidades cambiaron con el nivel (Fleisig 1999). Lo que define el gesto es el orden y el tiempo relativo; lo que define la potencia, la magnitud.

**Un eslabón débil se paga en la punta.** Si cadera y tronco entregan 20% menos energía, el hombro tiene que girar 34% más rápido para la misma fuerza en la mano (Seroyer 2010, citando a Kibler y Chandler 1995). Un ataque animado solo con el brazo se lee débil, y esta es la razón mecánica (lectura de esta misión).

**Puño y patada.** El directo empieza en los pies, sigue con el giro del tronco y termina con el brazo, y cuanto más experto el boxeador más aportan las piernas (Turner, Baker y Miller 2011, citando a Filimonov 1985). En la patada de empeine hay aproximación en ángulo, pie de apoyo al costado de la pelota, armado con el muslo atrás (cadera extendida) y la rodilla doblada, y después el muslo lidera, frena, y la pierna latiguea (Kellis y Katis 2007).

**Después de soltar.** La desaceleración, de soltar hasta que el brazo llega a su máxima rotación interna, es la fase más cargada para el hombro; la continuación que sigue tiene fuerzas mínimas (Seroyer 2010). Que la continuación sirva para frenar en más tiempo y más recorrido es razonamiento mecánico de esta misión.

---

## Parámetros

**Momentos del lanzamiento** (intervalo: apoyo del pie delantero 0% → soltar 100%; béisbol; Seroyer 2010):

| Parámetro | Valor | Rango | Condición | Fuente |
|---|---|---|---|---|
| Duración del intervalo | 0.145 s | — | lanzadores | (Seroyer 2010, citando a Stodden 2008) |
| Pico de velocidad de giro de la pelvis | 25–39% | — | ídem | (Seroyer 2010) |
| Pico de velocidad de giro del tronco | 51–52% | — | ídem | (Seroyer 2010) |
| Brazo atrás: rotación externa máxima del hombro (posición) | 81% | — | ídem | (Seroyer 2010) |
| Pico de velocidad de extensión del codo | 90–95% | — | ídem | (Seroyer 2010) |
| Pico de velocidad de inclinación del tronco hacia adelante | 93–96% | — | ídem | (Seroyer 2010) |
| Pico de velocidad de rotación interna del hombro | 102–104% | — | después de soltar | (Seroyer 2010) |

**Magnitudes:**

| Parámetro | Valor | Rango | Condición | Fuente |
|---|---|---|---|---|
| Velocidad de giro de la pelvis | 400–700 °/s | — | lanzamiento | (Seroyer 2010) |
| Rotación externa máxima del hombro | 165–175° | — | posición dinámica del armado; no es un rango articular de rig | (Seroyer 2010) |
| Velocidad de extensión del codo | ≈2250 °/s | — | lanzamiento | (Seroyer 2010) |
| Velocidad de inclinación del tronco al soltar | 300–450 °/s | — | lanzamiento | (Seroyer 2010) |
| Velocidad de rotación interna del hombro | 7000–9000 °/s | — | lanzamiento | (Seroyer 2010) |
| Bateo: giro de cadera / de hombros | 714 °/s / 937 °/s | — | bateadores | (Welch 1995) |
| Bateo: velocidad del bate | 31 m/s | — | ídem | (Welch 1995) |
| Bateo: fuerza del pie delantero | 1.23 veces el peso | — | ídem | (Welch 1995) |
| Separación caderas–hombros | ≈70° | — | golfistas con hándicap menor a 10; posición dinámica | (Cole y Grimshaw 2009, citando a Burden 1998) |
| Velocidad del puño | 7.4 m/s (jab) · 8.2 (directo) · 9.0–9.2 (ganchos) | — | boxeadores de competencia, golpe único máximo; jab y ganchos sin confirmar en la revalidación | (Piorkowski, Lees y Barton 2011) |
| Velocidad del puño en combinaciones | 5.9 m/s | — | combinaciones | (Piorkowski, Lees y Barton 2011, citando a Whiting 1988) |
| Duración de un golpe de puño | ≈0.3 s o menos | — | del inicio al contacto, en general | (Turner, Baker y Miller 2011) |
| Patada: aproximación | hasta 45°, 2–3 pasos | — | la mejora por el ángulo puede no ser significativa; los pasos son la preferencia de la práctica | (Kellis y Katis 2007, citando a Isokawa y Lees 1988) |
| Patada: pie de apoyo | 5–10 cm detrás y 5–28 cm al costado de la pelota | — | recomendación sin confirmación experimental | (Kellis y Katis 2007, citando a Hay 1993) |
| Patada: pico del muslo / pierna en el impacto | 516–573 °/s / 1891 °/s | — | fútbol, empeine | (Kellis y Katis 2007, citando a Dörge 1999) |
| Patada: velocidad de la pelota | 18–35 m/s | 1.06–1.65 veces la del pie | fútbol, empeine | (Kellis y Katis 2007) |

---

## Relaciones

```txt
orden de los giros          pelvis → tronco → codo → rotación interna del brazo
tiempo de cada evento       t = t_apoyo + p · T            T ≈ 0.145 s en el lanzamiento  (Seroyer 2010)
  p: pelvis 0.25–0.39 · tronco 0.51–0.52 · brazo atrás 0.81 · codo 0.90–0.95 ·
     inclinación del tronco 0.93–0.96 · soltar 1.00 · rotación interna 1.02–1.04
velocidad de la punta       v = ω · r, sumada a lo largo de la cadena           física estándar
```

El principio clásico de suma de velocidades dice que cada segmento arranca cuando el anterior llega a su pico (Bunn 1972, no leído en esta misión). Lo observado alcanza para animar: el orden de la tabla.

**En cuadros** (derivado de Seroyer 2010 y de Turner, Baker y Miller 2011): los 0.145 s del apoyo al soltar son 9 cuadros a 60 fps y 4 a 30 fps. Con 0.145 s × 60 = 8.7 cuadros, cada evento cae en `p · 8.7` redondeado: pelvis en el cuadro 2–3, tronco en el 4–5, brazo atrás en el 7, codo en el 8, soltar en el 9. Un golpe de puño de 0.3 s son 18 cuadros a 60 fps.

---

## Estilización

**Lo real ya es rápido donde importa.** La parte explosiva dura 9 cuadros a 60 fps en un lanzamiento y hasta 18 en un puñetazo (derivado de Seroyer 2010 y de Turner, Baker y Miller 2011). En el cuerpo real lo largo es la preparación: el armado, la zancada, la torsión. Ahí está el margen para comprimir o alargar (lectura de esta misión).

**Jugador y enemigo.** El criterio —anticipación mínima en el jugador para que responda, larga en el enemigo para que se lea— es de `Principios de animacion`. Lo que agrega este libro: en el jugador se recorta la preparación, no la parte rápida, que ya es corta. Cooper (2019, `61_Game_Anim`) propone además marcar el cuadro desde el que el jugador recupera el control; dónde va lo acuerda Game Design (`RA-011`, regla 5).

**Hit-stop** (Sakurai, Famitsu 490–491, `85_Sakurai_Hitstop`): en el contacto, atacante y víctima se congelan un instante, más tiempo cuanto más fuerte el golpe y con un tope; en un plataformero, 2–5 cuadros a 60 fps (≈33–83 ms) y solo en golpes poco frecuentes: en algo que pasa cada segundo se lee como lag (`02_Plataformero_2D`). Que le devuelva al impacto el peso que la compresión le quitó es lectura de esta misión.

**Qué se conserva al comprimir.** Como el orden y el tiempo relativo son lo que no cambia entre un juvenil y un profesional (Fleisig 1999), al comprimir un ataque se conserva: el orden de los picos; la torsión de la preparación, con los hombros más atrás que la pelvis; la punta a su máxima velocidad en el cuadro de impacto; y la pelvis ya frenando en ese mismo cuadro. Si los cuadros alcanzan, cada evento va en su `p`; uno por cuadro solo cuando no entran. Se recorta la duración de la preparación, no el orden (inferencia de esta misión, apoyada en Fleisig 1999 y Seroyer 2010).

---

## Medible y juicio

```txt
se mide (cuenta)        cuadros de preparación, de parte rápida y de recuperación; cuadro de
                        impacto y cuadro de devolución del control, marcados en el ART como los
                        acordó Game Design
se juzga (plancha)      en qué cuadro tiene cada segmento su mayor espaciado (su pico de velocidad):
                        pelvis antes que tronco, tronco antes que codo
se juzga                si el golpe tiene peso; si el aviso del enemigo se lee a tiempo
```

---

## Al encargo

```txt
MIEMBROS    I o D: el brazo que golpea y el pie que se planta. En un lanzamiento o un directo,
            el pie delantero es el del lado contrario al brazo
POSES       preparación: hombros girados hacia atrás más que la pelvis, peso atrás. Al arrancar,
            la pelvis gira primero hacia el objetivo y los hombros quedan atrás. Impacto: la
            punta a su máxima velocidad (el mayor espaciado del ataque), antes de la extensión
            completa; pelvis y giro del tronco ya frenando; inclinación del tronco en su pico;
            pie delantero plantado. Recuperación: el brazo sigue girando después del impacto y
            frena en un arco amplio
ORDEN       pelvis → tronco → codo → mano o arma. Nunca solo el brazo. Con 0.145 s a 60 fps,
            cada evento en p · 8.7 redondeado (pelvis 2–3, tronco 4–5, brazo atrás 7, codo 8, soltar 9)
TIEMPO      lanzamiento por encima del hombro (béisbol): parte rápida ≈0.145 s, 9 cuadros a
            60 fps. Puño directo: del primer movimiento al contacto ≤0.3 s, 18 cuadros a 60 fps;
            la recuperación va aparte. Otro golpe de brazo, espada, arma pesada o patada: sin
            número en esta misión; se conserva el orden y se mide.
            Jugador: se recorta la preparación. Enemigo: la preparación larga se suma antes
JUGABILIDAD el cuadro de daño es un evento acordado con Game Design, no la pose de máximo
            alcance (RA-011, regla 5); igual la devolución del control y las cancelaciones.
            Hit-stop que crece con la fuerza, con tope: en un plataformero, 2–5 cuadros a 60 fps
            (≈33–83 ms) y solo en golpes poco frecuentes; en algo que pasa cada segundo se lee
            como lag (02_Plataformero_2D)
```

---

## Límites

- Gestos deportivos medidos: lanzamiento de béisbol, bateo, golf, boxeo y patada de fútbol. No hay biomecánica de espada ni de armas pesadas leída en esta misión: se extrapola el principio, no los números.
- **Posiciones dinámicas, no límites de rig:** los 165–175° del brazo atrás y los ≈70° entre caderas y hombros son posiciones del gesto, que suman escápula, tronco y columna. `01_Anatomia_del_movimiento` no tiene número para esas rotaciones; si el personaje lanza por encima del hombro o hace un swing con torsión, su rig tiene que permitirlas, y la prueba de poses de 01 las incluye.
- **No verificados en esta misión:** las velocidades de Fleisig por nivel, los porcentajes de aporte de piernas, tronco y brazo en el puño, la duración de cada tipo de golpe de puño por separado, la duración del swing de un bate o de una raqueta, la duración de la patada desde el apoyo al impacto, cuánto dura la continuación, y los datos de cuadros de juegos de pelea.
- El dataset abierto de lanzamientos y swings, `86_OpenBiomechanics_Driveline`, tiene licencia no comercial: **no es insumo de un juego comercial**.
- Referencia visual primaria: las láminas de lanzar y golpear de `83_Muybridge_Animal_Locomotion`, por título, no verificadas una por una.

---

## Fuentes

- Seroyer, S. T., Nho, S. J., Bach, B. R., Bush-Joseph, C. A., Nicholson, G. P. & Romeo, A. A. (2010). The kinetic chain in overhand pitching: its potential role for performance enhancement and injury prevention. *Sports Health* 2(2), 135–146. — `77_Kinetic_Chain_in_Overhand_Pitching`.
- Fleisig, G. S., Barrentine, S. W., Zheng, N., Escamilla, R. F. & Andrews, J. R. (1999). Kinematic and kinetic comparison of baseball pitching among various levels of development. *Journal of Biomechanics* 32(12), 1371–1375. Resumen.
- Kellis, E. & Katis, A. (2007). Biomechanical characteristics and determinants of instep soccer kick. *Journal of Sports Science and Medicine* 6(2), 154–165. — `78_Instep_Soccer_Kick`.
- Welch, C. M., Banks, S. A., Cook, F. F. & Draovitch, P. (1995). Hitting a baseball: a biomechanical description. *Journal of Orthopaedic & Sports Physical Therapy* 22(5), 193–201. Resumen.
- Cole, M. H. & Grimshaw, P. N. (2009). The X-Factor and its relationship to golfing performance. *Journal of Quantitative Analysis in Sports* 5(1).
- Piorkowski, B. A., Lees, A. & Barton, G. J. (2011). Single maximal versus combination punch kinematics. *Sports Biomechanics* 10(1), 1–11. Manuscrito del autor.
- Turner, A., Baker, E. & Miller, S. (2011). Increasing the impact force of the rear hand punch. *Strength and Conditioning Journal* 33(6), 2–9.
- Cooper, J. (2019). *Game Anim: Video Game Animation Explained*. CRC Press. — `61_Game_Anim`. Extracto leído en Game Developer, *The 12 principles of animation in video games*.
- Sakurai, M. Columna de Famitsu sobre el hit-stop, vol. 490–491, traducida por Source Gaming (2015). — `85_Sakurai_Hitstop`.

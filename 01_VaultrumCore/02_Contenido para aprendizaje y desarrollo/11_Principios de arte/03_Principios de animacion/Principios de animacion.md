## Propósito

Esta subsección reúne los doce principios de la animación con la **especificación que cada uno necesita para funcionar en un videojuego**, y las curvas de interpolación con las que se ajustan.

No existe para animar como en el cine: en el cine nadie interrumpe al personaje.
No existe para enseñar el editor de curvas de un programa: eso lo opera la IA desde `08_Operar el arte`.
No existe para medir lo que vuelve de un encargo: eso es `animacion.py` y las reglas `RA-010` a `RA-012` del Área de Arte.

Existe porque el control de juego de cada principio vivía en una tabla dentro de una regla de uso (`RA-010`), sacada de una página web y de las correcciones de Miles, sin fuente. Esa tabla se mudó acá, con fuente, y la regla ahora la nombra.

---

## Qué es animar

La animación es una **sucesión de imágenes** que, mostradas en el tiempo, producen la ilusión de movimiento.

```txt
clave (keyframe)    un momento relevante de la accion: una pose que la define
intermedio          lo que va entre dos claves (in-between)
pasaje (breakdown)  la pose que decide COMO se va de una clave a la otra
timing              cuanto dura cada cosa
spacing             como se reparte el movimiento dentro de ese tiempo
```

Los doce principios los ordenaron Frank Thomas y Ollie Johnston, animadores de Disney, en 1981. Son de cine: describen cómo hacer creíble un movimiento que **nadie interrumpe**.

---

## La especificación de videojuego

En un juego hay cinco cosas que el cine no tiene, y le ganan a cualquier principio cuando chocan:

```txt
1  el jugador tiene el control      la respuesta al input le gana a todo. Un principio
                                    que retrasa la respuesta, en una accion del jugador,
                                    se recorta o se muda a otra parte del movimiento
2  el dibujo no es el collider      deformar, exagerar o arquear el dibujo no mueve la
                                    hitbox. Lo que cuenta para el juego se acuerda aparte
3  el tiempo de gameplay manda      preparacion, actividad y recuperacion las fija Game
                                    Design en cuadros. El animador encaja poses en ese
                                    tiempo, no al reves
4  cuadros de animacion no son      ocho imagenes pueden durar 0.8 s en un juego que
   cuadros de simulacion            corre a 60. El juego avanza en ticks; la animacion,
                                    en dibujos
5  todo se lee a escala real        la camara no la elige el animador, y a veces la mueve
   y desde la camara real           el jugador. Una pose que solo se lee de frente no se lee
```

Cada nota de abajo dice cómo choca su principio con estas cinco, y qué gana.

---

## La tabla de control

Es la tabla que vivía en `RA-010`. Una línea por principio; el detalle, en su nota.

```txt
compresion y estiramiento   CONTROL: la deformacion vuelve al reposo; el collider no se deforma
anticipacion                CONTROL: corta en la accion del jugador; larga y legible en la
                            del enemigo, porque ahi ES el aviso
puesta en escena            CONTROL: una cosa reclama atencion por vez, leida en silueta y a
                            la camara real
pose a pose / directa       CONTROL: la locomocion y los contactos, pose a pose; los contactos
                            se aprueban antes de intercalar
continuacion y superposicion  CONTROL: lo accesorio sigue moviendose, pero el control vuelve
                            cuando lo dice el gameplay, no cuando termina la capa
entradas y salidas suaves   CONTROL: no todo se suaviza; el impacto llega abrupto y la
                            respuesta al input no arranca lenta
arcos                       CONTROL: un arco lindo no justifica atravesar el suelo ni que el
                            golpe conecte donde no se ve
accion secundaria           CONTROL: nunca protagonista; si informa estado, es un canal y se
                            acuerda con UI/UX
timing                      CONTROL: cuadros de animacion no son cuadros de simulacion
exageracion                 CONTROL: se exagera lo que comunica sin cambiar la categoria de
                            la accion
dibujo solido               CONTROL: articulaciones y masas se siguen aunque queden ocultas;
                            una pierna no cambia de identidad al cruzarse
atractivo                   CONTROL: no es embellecer ni adelgazar; sigue siendo el mismo
                            personaje
```

---

## Cómo debe usar esta subsección una IA

```txt
¿La accion es del JUGADOR, de un enemigo, de la UI o del ambiente?
¿Que fija el gameplay: cuadros de preparacion, de actividad, de recuperacion, eventos?
¿Que principio ayuda a comunicar la accion dentro de ese tiempo?
¿Choca con alguna de las cinco restricciones? Si choca, gana la restriccion.
¿Que parte se mide (animacion.py, el motor) y que parte se juzga contra la referencia?
```

---

## [[01 - Compresion y estiramiento]]

La deformación que da peso, material y velocidad, conservando el volumen. En juego: vuelve al reposo y no toca el collider.

---

## [[02 - Anticipacion]]

La preparación antes de la acción. Es el principio que más choca con un juego: en la acción del jugador es lag, y en la del enemigo es el aviso que hace justa la pelea.

---

## [[03 - Puesta en escena]]

Una idea por vez, inequívoca, leída en silueta. En juego, desde una cámara que no elige el animador; en UI, una sola cosa reclama la atención.

---

## [[04 - Pose a pose y accion directa]]

Los dos métodos de construir un movimiento, y el blocking. Incluye cuántas poses clave lleva cada acción de juego.

---

## [[05 - Continuacion y superposicion]]

Lo que sigue moviéndose después de que la acción paró, y las partes que no se detienen a la vez. En juego: no le quita el control al jugador.

---

## [[06 - Entradas y salidas suaves]]

La aceleración y la desaceleración cerca de las poses. En juego: no todo se suaviza, y el dibujo suave no cambia la física.

---

## [[07 - Arcos]]

Las trayectorias curvas de lo que se mueve con naturalidad. En juego: el arco del dibujo y el del golpe tienen que coincidir.

---

## [[08 - Accion secundaria]]

Lo que suma a la acción principal sin competir con ella. En juego: si informa estado, ya es un canal de comunicación.

---

## [[09 - Timing]]

Cuánto dura cada cosa y cómo se reparte el movimiento. En juego: el tiempo lo fija el gameplay y los cuadros de animación no son los de la simulación.

---

## [[10 - Exageracion]]

Llevar la pose más allá de lo real para que se lea. En juego: a la escala de pantalla, exagerar es legibilidad, y la dosis mínima suele alcanzar.

---

## [[11 - Dibujo solido]]

Volumen, peso y equilibrio. En juego: las masas se sostienen entre cuadros y las piernas no cambian de identidad.

---

## [[12 - Atractivo]]

El carisma del personaje. En juego: se lo mira miles de veces en el mismo idle, y corregirlo no puede cambiarlo de identidad.

---

## [[Curvas e interpolacion]]

Constante, lineal, Bézier y overshoot: cómo calcula el programa los intermedios, y cómo se ajustan timing y spacing con claves y manijas. Salió casi entera de la clase del 10 de agosto del owner.

---

## Fuentes de la subsección

- `59_The_Illusion_of_Life` — los doce principios, en su origen.
- `60_The_Animators_Survival_Kit` — timing, spacing, claves e intermedios.
- `61_Game_Anim` — la especificación de videojuego: respuesta, cancelación, raíz.
- `68_Apuntes_de_catedra_Animacion_2D_3D` — fuente propia del owner.
- Área de Arte: `RA-010`, `RA-011` y `RA-012`, de donde salió la tabla de control.

## Definición

**Anticipación**: un movimiento de preparación, casi siempre en sentido contrario, antes de la acción principal. Agacharse antes de saltar, llevar el brazo atrás antes de lanzar.

Prepara al espectador: le dice que algo va a pasar y hacia dónde.

---

## Idea central

**Es el principio que más choca con un juego**, porque en el cine la preparación no le cuesta nada a nadie, y en un juego le cuesta tiempo al jugador.

```txt
accion del JUGADOR   el jugador ya sabe que va a pasar: lo decidio el. La preparacion
                     no le informa nada y le retrasa la respuesta. Se siente como lag
accion del ENEMIGO   el jugador NO sabe que va a pasar. La preparacion es el aviso
                     (telegraph): la ventana para leer y reaccionar. Es lo que hace
                     justo un golpe
```

El mismo principio, en sentidos opuestos según de quién es la acción.

---

## Especificación para videojuegos

**En la acción del jugador:**

```txt
la respuesta primero     el input se tiene que ver respondido en el cuadro siguiente,
                         o en muy pocos. Toda preparacion larga es retraso percibido
la preparacion se acorta a uno o dos cuadros, o se muda: a la pose de espera
                         (un idle ya cargado) o al final de la accion
el peso se muda          lo que se le saca a la anticipacion se pone en la
                         continuacion: el movimiento "pesa" despues del input, no antes
```

**En la acción del enemigo:**

```txt
legible                  se distingue del idle y de las otras acciones del mismo enemigo
                         (Silueta legible, Puesta en escena)
suficiente               el aviso dura al menos el tiempo de reaccion humano —del orden
                         de un cuarto de segundo para algo simple— mas el tiempo de
                         ejecutar la respuesta. La duracion exacta es un parametro de
                         dificultad: la fija Game Design, no el animador
constante                la misma accion, la misma duracion de aviso. El jugador aprende
                         el ritmo; un aviso que cambia es injusto
```

**Preparación, actividad y recuperación.** Toda acción de combate se parte en tres tramos que se acuerdan con Game Design en cuadros (`RA-011`, regla 5). La anticipación es el primero. El momento de daño es un **evento** documentado, no la pose más extendida.

**En la UI:** los cambios son inmediatos, siempre con una animación de por medio (`68_Apuntes_de_catedra_Animacion_2D_3D`). La animación acompaña la respuesta, no la demora.

---

## Cómo se juzga

```txt
se mide     cuadros entre el input y el primer cambio visible, grabando en el motor a la
            frecuencia del juego. Los cuadros de preparacion los fija el GDS; el clip los
            cumple, y sus eventos se declaran en el manifiesto (RA-012)
se juzga    si el aviso se lee como aviso, a la distancia y camara de juego
```

---

## Errores comunes

```txt
Copiar la preparacion de una referencia de cine a un salto del jugador.
Un aviso de enemigo que se parece a su idle.
Avisos de duracion variable para la misma accion.
Deducir el momento de dano de la pose, en vez de declararlo como evento.
Alargar la preparacion para "dar peso" cuando el peso iba en la continuacion.
```

---

## Ejemplo en videojuegos

El salto de un plataformero: el personaje despega en el cuadro del input; el "agacharse antes" se reduce a un cuadro o desaparece, y el peso se muestra en el aterrizaje (compresión, polvo). El enemigo que embiste: baja la cabeza, raspa el piso, se queda quieto un instante —siempre lo mismo y siempre igual de largo— y recién después carga.

---

## Fuentes

- `59_The_Illusion_of_Life` — el principio.
- `61_Game_Anim` — respuesta contra fidelidad, y el peso mudado a la continuación.
- `05_Game_Feel` (Fuentes) y `02_Game_feel` (Fundamentos) — la respuesta como sensación.
- `68_Apuntes_de_catedra_Animacion_2D_3D` — cambios inmediatos con animación de por medio.
- `RA-010` (con su tabla previa a `TL-012`) y `RA-011` del Área de Arte — la preparación larga que se siente como retraso, y los tres tramos acordados con Game Design.

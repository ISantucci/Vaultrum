## Definición

**El input se interpreta a favor del jugador**: el juego hace lo que el jugador razonablemente quiso hacer. Perdona los errores de percepción y de timing que una persona comete siempre —el borde que vio tarde, el botón que apretó un poco antes, el apuntado que quedó cerca— y lo declara. Pero no juega por ella: el resultado tiene que seguir siendo suyo.

---

## Idea central

Es uno de los tres dominios del game feel, al lado del movimiento y de los efectos: la práctica lo llama **soporte**. Sin él, el jugador hace bien y pierde igual, y la culpa se siente del juego.

El límite es la **pertenencia**: si la asistencia decide por el jugador, el logro deja de ser suyo y el techo de habilidad desaparece. La regla que separa los dos lados:

```txt
se perdona    el error de PERCEPCION o de TIMING: vio el borde tarde, apreto un cuadro
              antes, apunto casi
no se perdona el error de DECISION: salto hacia el lado equivocado, eligio mal el objetivo
```

Así se consigue lo que Swink llama *fácil pero profundo*: el perdón baja el piso, y lo que no se perdona sostiene el techo.

---

## Especificación en Unity

```txt
coyote time    el salto sigue siendo valido ~100 ms (5-7 cuadros a 60 fps) despues de
               dejar el borde
buffer         la accion apretada poco antes de ser posible se ejecuta cuando lo es:
               100-133 ms (6-8 cuadros a 60 fps), y UNA sola accion en cola: la nueva
               pisa a la vieja. Mas de 200 ms produce acciones que nadie pidio
asistencias    magnetismo de apuntado, correccion de esquina, rango extra de agarre:
               declaradas con su radio, y apagables si el juego es de precision
donde vive     un componente de input guarda marcas de tiempo (ultimo pulsado, ultimo
               suelo) con Time.time, y el controlador las consulta. Los valores, en el
               ScriptableObject del avatar
```

El perdón que sale *sin querer* de un collider más grande que el sprite también es perdón: si existe, se declara. Si no está declarado, Level Design no puede contar con él.

---

## Quién lo aplica

```txt
Game Design    declara que se perdona y cuanto, y que no se perdona
Level Design   disena bordes y distancias contando con el perdon declarado, no con el ideal
Programacion   implementa con marcas de tiempo, no con colliders agrandados a ojo
Calidad        prueba los bordes: apretar un cuadro tarde, un cuadro antes, en el limite exacto
```

---

## Cómo se juzga

```txt
se mide     cada ventana de perdon, en ms, medida en el motor contra el GDS; la
            accion fantasma (buffer demasiado largo) provocada a proposito
se juzga    si el jugador siente que lo logro el
```

---

## Errores comunes

```txt
Perdon implicito, salido de un collider grande, que nadie declaro.
Un buffer tan largo que el personaje salta cuando el jugador ya no queria.
Asistencias que juegan solas.
Perdonar decisiones: el juego elige el objetivo por el jugador.
Disenar un nivel con el perdon "por las dudas" y otro sin el.
```

---

## Fuentes

- `10_Input_y_respuesta` (Fundamentos) — el perdón de input, sus ventanas y la línea de tiempo del salto.
- `69_Designing_Game_Feel_Survey` (Fuentes) — el soporte como tercer dominio del game feel.
- `05_Game_Feel` (Fuentes) — fácil pero profundo, y pertenencia (esta última, lectura Vaultrum sin confrontar con el capítulo 17).
- `05_Fundamentos_de_experiencia_ludica` (Fundamentos) — Pilar 5, justicia y control.

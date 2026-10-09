## Definición

Entre dos claves, el programa calcula los intermedios con una **interpolación**. La **curva** muestra el valor de un canal —posición en Z, rotación, escala, opacidad— a lo largo del tiempo, y es la herramienta con la que se ajustan timing y spacing en 3D y en UI.

Esta nota salió casi entera de la clase del 10 de agosto del owner (`68_Apuntes_de_catedra_Animacion_2D_3D`).

---

## Las interpolaciones

```txt
constante    el valor salta y se sostiene hasta la clave siguiente. Es el modo del
             blocking, de la animacion "en dos" y de un sprite: cada dibujo se queda
             quieto su tiempo. "Dos cuadros constantes, muevo, y asi"
lineal       el valor cambia lo mismo en cada cuadro: sin aceleracion. Mecanico. Sirve
             para lo que ES mecanico: una helice, una cinta, una barra que se llena a
             velocidad constante
curva        Bezier: aceleracion y desaceleracion, controladas por las manijas de cada
             clave. Es la que da masa
overshoot    la curva pasa el valor de destino y vuelve. En el ejemplo de la clase: en
             el tiempo 0 vale 0, en el tiempo 2 vale 2, y en el 1.5 ya vale 2.5. Es
             exageracion y rebote en una sola curva
```

---

## Las manijas, y la regla de los nombres

Cada clave de una curva Bézier tiene dos manijas que fijan la velocidad al llegar y al salir.

```txt
juntas y planas     la velocidad llega a cero en la clave: se frena y se arranca
alineadas           el movimiento pasa por la clave sin frenar
rotas (libres)      la velocidad cambia de golpe en la clave: un rebote, un impacto
```

La clase del 21 de septiembre dejó la técnica en una línea: **Bézier libre en un solo canal**. En un salto, el canal Z se edita con manijas rotas en el contacto con el piso —ahí la dirección cambia de golpe— mientras X sigue su curva propia. Cada canal tiene su curva.

**Los nombres se cruzan.** La clase describe el *ease in* como la mitad donde la velocidad aumenta y el *ease out* como la que desacelera: es el vocabulario de Unreal, de Blender y de CSS. La tradición dice *slow in* para frenar al **llegar** a una pose, que es lo contrario, y After Effects también: su *Easy Ease In* frena al llegar a la clave. Regla de Vaultrum:

```txt
se describe por la velocidad     "arranca lento"     "llega frenando"
el nombre del programa se usa    solo junto con el programa, porque cada uno
                                 llama distinto a lo mismo
```

---

## Menos claves

**A menos claves, más fácil de manipular** (cátedra). El ajuste se hace moviendo las claves en el tiempo —adelantar o retrasar— y las manijas para el reparto. Una animación con una clave en cada cuadro (horneada) no se puede editar: cualquier cambio es rehacer.

Del lado del costo, las claves guardadas son otra pregunta: `Claves por tipo de animacion`, en la rama Arte de Optimización.

---

## Especificación para videojuegos

```txt
la curva del dibujo no es   suavizar una curva no cambia la velocidad del controlador
la fisica                   que mueve al personaje (`RA-010`, antes de `TL-012`). Si no coinciden, patina
UI: se anima la transform   posicion, escala, rotacion y opacidad. NUNCA el tamano ni
                            los margenes del layout: la clase lo dejo como regla. En
                            Unreal (UMG), la transform de render no recalcula el layout;
                            el tamano y los margenes si. En Unity (uGUI), cualquier cambio
                            reconstruye el Canvas que lo contiene: lo animado va en un
                            Canvas propio (Canvas rebuild, Separar canvas por frecuencia
                            de cambio)
la respuesta no arranca     una curva que sale lenta de la pose de espera, en una
lenta                       accion del jugador, es lag
```

---

## Cómo se juzga

```txt
se mide     las curvas son datos del archivo: claves, valores, tipo de interpolacion y
            manijas se leen por script (Blender, Unreal). Overshoot no pedido, claves de
            mas y canales horneados se detectan sin mirar
se juzga    si el movimiento tiene la masa que pide la accion
```

---

## Errores comunes

```txt
Dejar las manijas automaticas y descubrir un overshoot que nadie pidio.
Curva en todo: el movimiento flota.
Hornear la animacion y despues querer ajustarla.
Animar el tamano de un widget en vez de su escala.
Nombrar "ease in" sin decir de que programa, y que el otro entienda lo contrario.
```

---

## Fuentes

- `68_Apuntes_de_catedra_Animacion_2D_3D` — las interpolaciones, el overshoot, menos claves, Bézier libre por canal y no animar el layout.
- `60_The_Animators_Survival_Kit` — spacing y el vocabulario tradicional.
- `71_Blender_Manual` y `74_Unreal_Animating_UMG_Widgets` — los editores de curvas.
- `Canvas rebuild` — el precio de animar el layout.

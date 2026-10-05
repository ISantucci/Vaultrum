## Definición

**Entradas y salidas suaves** (*slow in and slow out*): cerca de una pose extrema el movimiento se frena y al salir de ella arranca despacio. Se dibujan más cuadros cerca de las poses y menos en el medio.

En 3D y en UI no se dibuja: lo hace la **curva** de interpolación. El detalle está en `Curvas e interpolacion`.

---

## Idea central

```txt
sin suavizado   velocidad constante: mecanico, de maquina
con suavizado   acelera al salir, frena al llegar: tiene masa
```

**Cuidado con los nombres.** En la tradición, *slow in* es frenar al **llegar** a una pose, y After Effects usa *Easy Ease In* en ese mismo sentido. En Unreal, Blender y CSS, *ease in* es arrancar despacio y *ease out* llegar frenando. Los nombres se cruzan. En Vaultrum una curva se describe por lo que hace la velocidad —*arranca lento*, *llega frenando*— y el nombre del programa se usa solo junto con el programa.

---

## Especificación para videojuegos

```txt
no todo se suaviza        un impacto llega abrupto: suavizar la llegada de un golpe le
                          quita el golpe (`RA-010`, antes de `TL-012`)
la respuesta no arranca   la accion del jugador que arranca lenta se siente con lag: la
lenta                     salida de la pose de espera es corta
el dibujo no es la fisica suavizar el dibujo no cambia la velocidad del controlador. Si el
                          codigo mueve al personaje a velocidad constante y la animacion
                          acelera, los pies patinan
UI                        las transiciones casi siempre llevan suavizado; un texto puede
                          entrar por corte directo
```

---

## Cómo se juzga

```txt
se mide     la pendiente de la curva en cada clave, en el editor de curvas: es un dato
            del archivo y se puede leer por script. En 2D, la distancia entre cuadros
            consecutivos (spacing) en la plancha
se juzga    si el movimiento tiene masa sin flotar
```

---

## Errores comunes

```txt
Suavizar todo por defecto: el movimiento flota, nada pesa.
Arrancar lento la accion del jugador.
Suavizar el impacto.
Animar con curva una cosa que en el juego mueve el codigo a velocidad constante.
```

---

## Fuentes

- `59_The_Illusion_of_Life` — el principio.
- `60_The_Animators_Survival_Kit` — el reparto de los intermedios.
- `68_Apuntes_de_catedra_Animacion_2D_3D` — ease in, ease out y su descripción por velocidad.
- `RA-010_Animacion_identidad_y_movimiento`, con su tabla de control previa a `TL-012` — el impacto abrupto y la física del controlador.

## Definición

**Arcos**: lo que se mueve con naturalidad sigue trayectorias curvas. Una mano que saluda, una cabeza que gira, un pie que avanza: ninguno va en línea recta.

---

## Idea central

```txt
linea recta    mecanico. Es lo que produce una interpolacion lineal entre dos claves
arco           organico. Lo que se ve es la trayectoria, no solo las poses
```

El arco no está en las claves: está en **cómo se pasa de una a otra**. Por eso es el pasaje (breakdown) el que lo decide, y por eso un movimiento con buenas claves y sin pasajes viaja derecho.

---

## Especificación para videojuegos

```txt
el arco no atraviesa      un arco lindo no justifica atravesar el suelo, la pared o el
                          boton que se toca (`RA-010`, antes de `TL-012`)
el golpe sigue al dibujo  un ataque en arco barre un area. Si la hitbox se mueve en linea
                          recta o aparece entera en un cuadro, el golpe conecta donde no
                          se ve, o no conecta donde se ve
lo que mueve la fisica    la parabola de un proyectil la calcula el codigo. La animacion
no lo anima el animador   del lanzamiento tiene que soltar en el angulo que el codigo usa
el arco del ciclo         la cabeza en una caminata dibuja una onda; en un ciclo in-place
                          esa onda se ve sola, y delata un ciclo roto
```

---

## Cómo se juzga

```txt
se mide     la trayectoria de una parte (la mano, la cabeza) dibujada cuadro a cuadro:
            en 3D, la ruta de movimiento del hueso es un dato que el DCC traza; en 2D,
            el centro de la parte marcado sobre la plancha
se juzga    si el arco es el que pide la accion
```

---

## Errores comunes

```txt
Dos claves y nada en el medio: el movimiento viaja derecho.
Arcos que se rompen en un cuadro (la trayectoria hace un pico).
La hitbox que no sigue al arco.
Un arco que cruza el piso en el punto mas bajo.
```

---

## Fuentes

- `59_The_Illusion_of_Life` — el principio.
- `60_The_Animators_Survival_Kit` — el pasaje que dibuja el arco.
- `68_Apuntes_de_catedra_Animacion_2D_3D` — la clase de animación 2D avanzada.
- `RA-010_Animacion_identidad_y_movimiento`, con su tabla de control previa a `TL-012` — el arco que no atraviesa.

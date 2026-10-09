## Definición

**Continuación** (*follow through*): las partes que cuelgan o son flexibles siguen moviéndose después de que el cuerpo se detuvo —el pelo, la capa, la cola, la ropa— y se asientan de a poco.

**Superposición** (*overlapping action*): las partes de un cuerpo no arrancan ni frenan a la vez; cada una va con su desfase.

---

## Idea central

```txt
todo para a la vez        robot: se lee mecanico y sin peso
con continuacion          el cuerpo para, el pelo sigue, el pelo para despues
con superposicion         la cadera arranca, el torso la sigue, la cabeza llega ultima
```

Es lo que hace que un movimiento tenga masa. La clase de animación 2D avanzada del owner (31-08) lo trabajó junto con exageración, arcos y acción secundaria: los cuatro hacen que un personaje parezca vivo y no articulado.

---

## Especificación para videojuegos

```txt
el control vuelve cuando lo dice el gameplay   no cuando termina la capa. Lo accesorio
                                               puede seguir moviendose mientras el
                                               jugador ya actua (`RA-010`, antes de `TL-012`)
aca va el peso que perdio la anticipacion       en la accion del jugador, la continuacion
                                               es donde se muestra la fuerza
la recuperacion se puede cortar                el tramo de continuacion de un ataque es
                                               candidato natural a ventana de cancelacion:
                                               se acuerda con Game Design
en 3D, a menudo es simulacion                   pelo, capa, cola: huesos con resortes o
                                               fisica secundaria en vez de claves.
                                               Barato de autorear, cuesta CPU
```

---

## Cómo se juzga

```txt
se mide     en el motor: el cuadro en que vuelve el control contra el fin del clip. El
            cuadro de fin del bloqueo lo fija el GDS, y entra al manifiesto del clip
            como uno de sus eventos (RA-012)
se juzga    si el movimiento tiene masa sobre la plancha, y si lo accesorio no tapa la
            lectura de que el jugador ya puede actuar
```

---

## Errores comunes

```txt
Bloquear el input hasta que termine la ropa.
Superposicion excesiva: el personaje parece de gelatina.
Continuacion que no se asienta: el pelo sigue oscilando en el idle.
Animar a mano lo que un resorte resuelve, o simular lo que tenia que tener intencion.
```

---

## Fuentes

- `59_The_Illusion_of_Life` — el principio.
- `60_The_Animators_Survival_Kit` — desfase y arrastre.
- `61_Game_Anim` — el peso después del input, y las ventanas de cancelación.
- `68_Apuntes_de_catedra_Animacion_2D_3D` — la clase de animación 2D avanzada.

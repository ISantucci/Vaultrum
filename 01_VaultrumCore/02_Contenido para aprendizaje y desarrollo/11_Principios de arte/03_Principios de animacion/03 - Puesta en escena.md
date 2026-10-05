## Definición

**Puesta en escena** (*staging*): presentar una idea de modo que sea **inequívoca**. La pose, el encuadre y el momento se eligen para que se entienda una sola cosa, y la que importa.

---

## Idea central

```txt
una idea por vez       si dos cosas piden atencion a la vez, ninguna la recibe
la silueta lo dice     una pose bien puesta se entiende rellena de negro
la jerarquia           lo que importa se mueve primero, o mas, o solo
```

La cátedra del owner lo dejó como cinco preguntas que sirven para cualquier escena, animada o de interfaz:

```txt
¿que aparece?   ¿que desaparece?   ¿que se mueve?
¿que llama la atencion?   ¿que queda estatico?
```

---

## Especificación para videojuegos

```txt
la camara no la elige el animador   la pose se lee desde los angulos y distancias reales
                                    de juego: cenital, lateral, tres cuartos, lejos. Una
                                    pose que solo funciona de frente no funciona
se lee en silueta y a escala real   a 60 px de alto los detalles no existen: existe la
                                    forma rellena
lo jugable manda                    lo que el jugador necesita leer —el aviso, el objetivo,
                                    el peligro— tiene prioridad de movimiento sobre lo
                                    decorativo
UI: una cosa por vez                una tecla activa por estado (el tutorial WASD), los
                                    textos primero y por encima, y lo demas espera
```

---

## Cómo se juzga

```txt
se mide     la silueta rellena a la escala de pantalla real (Legibilidad, en IA Operativa);
            en una transicion de UI, cuantos elementos se mueven a la vez
se juzga    si la intencion se entiende sin contexto, en una sola mirada
```

---

## Errores comunes

```txt
Poses pensadas de frente para un juego de camara lateral o cenital.
Brazos dentro de la silueta del torso: la accion desaparece.
Todo se anima a la vez en una pantalla: nada destaca.
Lo decorativo se mueve mas que lo jugable.
```

---

## Ejemplo en videojuegos

El saludo de Miles: una sola mano arriba, separada del cuerpo, el otro brazo relajado. Rellena de negro, la silueta dice "saluda". Con las dos manos a la altura del pecho, dice "algo hace" y nada más.

---

## Fuentes

- `59_The_Illusion_of_Life` — el principio.
- `51_Understanding_Comics` — la lectura de una imagen que comunica.
- `61_Game_Anim` — la cámara de juego.
- `68_Apuntes_de_catedra_Animacion_2D_3D` — las cinco preguntas.
- `RA-010` (con su tabla previa a `TL-012`) y `RA-012` del Área de Arte — el saludo y el tutorial WASD.

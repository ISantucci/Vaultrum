## Definición

> *La personalidad de un personaje no comienza en el diseño, sino en la forma en que se mueve.*
> — apunte de la clase de animación 2D avanzada del owner, 31-08-2026

El mismo modelo, con dos caminatas distintas, son dos personajes distintos. El diseño dice quién podría ser; el movimiento dice quién es.

---

## Idea central

```txt
el timing        un personaje apurado y uno tranquilo, con la misma accion
las poses        hacia donde mira, como se para, que hace con las manos
la secundaria    lo que hace mientras hace otra cosa (Accion secundaria)
la continuacion  como se asienta lo que se mueve despues
```

Es la suma de los principios aplicada a una persona en particular.

---

## Especificación para videojuegos

```txt
la personalidad sobrevive al gameplay   el jugador necesita respuesta inmediata, y eso
                                        le quita preparacion a cada accion. La
                                        personalidad se muda a lo que el gameplay no
                                        mide: el idle, la secundaria, la continuacion,
                                        las transiciones
el idle es el retrato                   es lo que mas se ve del personaje
se escribe en la guia de estilo         como se mueve cada personaje: ritmo, amplitud,
                                        energia. Si no, cada clip lo interpreta distinto
```

---

## Cómo se juzga

```txt
se juzga    lo juzga el owner: es direccion. Que dos clips del mismo personaje se sientan
            del mismo personaje
se mide     solo la identidad (proporciones contra la referencia maestra)
```

---

## Errores comunes

```txt
Poner toda la personalidad en la preparacion de las acciones del jugador.
Un idle generico para un protagonista.
Clips del mismo personaje con energias distintas.
```

---

## Fuentes

- `68_Apuntes_de_catedra_Animacion_2D_3D` — la frase, y la clase donde salió.
- `59_The_Illusion_of_Life` — personalidad a través del movimiento.
- `64_Creating_Characters_with_Personality` — el carácter en el diseño y en la acción.

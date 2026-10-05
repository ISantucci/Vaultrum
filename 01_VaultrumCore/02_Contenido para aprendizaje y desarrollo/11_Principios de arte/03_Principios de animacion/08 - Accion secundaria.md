## Definición

**Acción secundaria**: un movimiento que acompaña a la acción principal y le suma sentido sin competir con ella. Silbar mientras se camina; mirar el botón antes de tocarlo.

---

## Idea central

```txt
la principal dice QUE hace     camina
la secundaria dice COMO es     camina mirando el piso: esta triste
```

La cátedra del owner lo dejó sin matiz: *las acciones secundarias siempre son importantes*. Son donde vive la personalidad (`Personalidad en el movimiento`).

---

## Especificación para videojuegos

```txt
nunca protagonista         si la secundaria tapa la lectura de la principal, sobra
                           (`RA-010`, antes de `TL-012`)
no cambia el timing        la secundaria no alarga ni corre la principal: el tiempo lo
                           fija el gameplay
si informa, es un canal    cojear con poca vida ya no es decoracion: es informacion de
                           estado. Entra al presupuesto de comunicacion y se acuerda con
                           UI/UX y Game Design
en 3D suele ser una capa   respirar, mirar hacia algo, una mano en la cadera: capas
                           aditivas sobre la locomocion, no clips nuevos. El mecanismo es
                           de la operacion (IA Operativa), el criterio es este
```

---

## Cómo se juzga

```txt
se juzga    si suma o compite: se mira la secuencia sin la secundaria y con ella
se mide     solo lo que la secundaria podria romper: que la duracion del clip no cambie
            y que la silueta de la accion principal siga leyendose
```

---

## Errores comunes

```txt
Una secundaria tan llamativa que el jugador mira eso y no el aviso.
Secundarias que informan estado sin que nadie las haya presupuestado.
Animar la secundaria dentro de cada clip en vez de como capa: se repite trabajo y se
desincroniza.
```

---

## Fuentes

- `59_The_Illusion_of_Life` — el principio.
- `61_Game_Anim` — capas y animación aditiva.
- `68_Apuntes_de_catedra_Animacion_2D_3D` — *siempre son importantes*.
- `RA-010_Animacion_identidad_y_movimiento`, con su tabla de control previa a `TL-012` — mirar el botón antes de tocarlo.

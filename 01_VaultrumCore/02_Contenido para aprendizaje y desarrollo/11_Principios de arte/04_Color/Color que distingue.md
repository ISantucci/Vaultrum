## Definición

Las **familias que el jugador tiene que distinguir** —aliado y enemigo, lo que se agarra y lo que decora, lo que hace daño y lo que no— se distinguen por **más de un canal a la vez**, y se siguen distinguiendo con las formas comunes de daltonismo.

---

## Idea central

```txt
un canal solo falla       si dos familias se distinguen solo por tono, el que no ve ese
                          tono no las distingue
redundancia               valor + tono + forma. Si uno falla, quedan dos
```

El caso que el Área de Arte probó como caso de su instrumento: **el rojo y el verde colapsan en deuteranopia**. Dos familias rojo y verde con el mismo valor son, para una parte de los jugadores, la misma familia.

---

## Especificación para videojuegos

```txt
el color no va solo           ninguna informacion jugable depende solo del color (es ley
                              de UI/UX, y vale igual para los assets)
la forma acompana             el enemigo peligroso no es solo rojo: tiene otra silueta
                              (Silueta legible)
se prueba con los tres        protanopia, deuteranopia, tritanopia, y en gris
la cantidad de senales        cuantas familias entran y por que canal lo dicta UI/UX
la dicta otro                 (presupuesto de comunicacion). Arte hace que las que
                              entraron se lean
```

---

## Cómo se juzga

```txt
se mide     distancia de color entre familias en simulacion de daltonismo y en gris
            (arte.paleta()); superposicion de siluetas entre familias
se juzga    si la diferencia se lee en movimiento, a la distancia de juego
```

---

## Errores comunes

```txt
Aliado verde, enemigo rojo, mismo valor y misma silueta.
Probar en color y dar por hecha la accesibilidad.
Agregar una familia nueva sin pasar por el presupuesto de comunicacion.
```

---

## Fuentes

- `63_Interaction_of_Color` — la relatividad que hace que dos colores se confundan.
- `42_Game_Accessibility_Guidelines` — el color que no va solo.
- Área de Arte: ley 5 y el caso rojo y verde de `probar_arte.py`.

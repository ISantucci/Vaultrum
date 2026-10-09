## Definición

**Dibujo sólido**: dar a lo que se anima volumen, peso y equilibrio. Las formas son tridimensionales aunque estén dibujadas en un plano, las masas se sostienen y la pose no se cae.

---

## Idea central

```txt
volumen      las formas tienen frente, costado y espalda, aunque se vea una sola
peso         el centro de masa esta sobre el apoyo; si no, la pose se cae
sin gemelos  los miembros no hacen exactamente lo mismo a la vez (twinning): se ve
             plano y artificial
```

---

## Especificación para videojuegos

```txt
en 3D el modelo da el volumen   y la pose lo puede romper: poses planas de cara a la
                                camara, brazos gemelos
en 2D la masa se sostiene       el torso no "respira" sin querer entre cuadros, la cabeza
                                no cambia de tamano
se siguen las articulaciones    aunque una pierna quede oculta (`RA-010`, antes de `TL-012`)
una pierna es la misma pierna   no se reasigna la identidad de las piernas al cruzarse
                                (RA-011): I sigue siendo I del otro lado
el equilibrio es jugable        un personaje que se ve desequilibrado en el idle parece
                                a punto de caer, y el jugador lo lee como estado
```

---

## Cómo se juzga

```txt
se mide     escala y area de la silueta estables entre cuadros (animacion.py); en 3D,
            que el volumen no colapse en las poses (Topologia para deformar)
se juzga    equilibrio y volumen, sobre la plancha numerada
```

---

## Errores comunes

```txt
Brazos y piernas gemelos.
Volumenes que cambian entre cuadros sin intencion.
Una pierna que cambia de lado en el cruce.
Poses de presentacion de frente en un juego que se ve de costado.
```

---

## Fuentes

- `59_The_Illusion_of_Life` — el principio.
- `60_The_Animators_Survival_Kit` — peso y equilibrio.
- `64_Creating_Characters_with_Personality` — volumen en el diseño.
- `RA-010` (con su tabla previa a `TL-012`) y `RA-011` del Área de Arte.

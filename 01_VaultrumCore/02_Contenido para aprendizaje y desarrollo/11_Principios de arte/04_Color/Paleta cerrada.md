## Definición

Una **paleta cerrada** es el conjunto limitado de colores del que sale todo color de un proyecto. Se decide antes del primer asset —mitad A del `ART`— y un color nuevo entra **por decisión**, no porque un asset lo trajo.

---

## Idea central

```txt
pocos colores, relacionados     se ven como un mundo
muchos colores, sueltos         se ven como una coleccion de assets de origenes distintos
```

Una paleta limitada no es pobreza: es lo que hace que el conjunto se vea hecho por la misma mano. Gurney lo trabaja como **gamut**: elegir de antemano una región del círculo de color y pintar solo desde adentro de ella.

---

## Cómo se arma

```txt
pocos tonos base          y sus rampas de valor, de oscuro a claro
rampas con corrimiento    al oscurecer, el tono se corre (por ejemplo hacia frio); al
de tono                   aclarar, hacia el otro lado. Una rampa que solo baja el brillo
                          se ve sucia. Es practica corriente del pixel art
un rol por color          cuales son de la figura, cuales del fondo, cuales del peligro,
                          cuales de la interfaz
lo que NO entra           se escribe tambien: el rojo de alerta, si el juego no tiene
                          alertas
```

---

## Especificación para videojuegos

```txt
se decide antes del primer asset    y vive en la guia de estilo del proyecto
cada asset se mide contra ella      el goblin trajo diez materiales nuevos contra los
                                    treinta que ya habia, y ningun instrumento los miro:
                                    es el caso que fundo al Guardian Visual
un color nuevo entra con razon      la razon se escribe: que familia distingue, que
                                    funcion cumple
```

---

## Cómo se juzga

```txt
se mide     censo de colores de los materiales, duplicados casi iguales, distancia entre
            colores (arte.paleta(), ley 5)
se juzga    si la paleta tiene el animo que pide la direccion de arte
```

---

## Errores comunes

```txt
Elegir colores asset por asset.
Diez variantes casi iguales del mismo verde.
Rampas que solo oscurecen.
Una paleta sin roles: todo compite.
```

---

## Fuentes

- `62_Color_and_Light` — gamut y paleta limitada.
- `67_Pixel_Logic` — paletas limitadas y corrimiento de tono en las rampas.
- Área de Arte: ley 5, Modo Escala, `05_Guardian_Visual`.

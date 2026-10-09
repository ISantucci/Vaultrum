## Definición

```txt
hard surface   objetos fabricados: maquinas, armas, edificios, muebles, torres
organico       objetos que crecieron: personajes, criaturas, rocas, troncos, telas
```

No es una categoría de estilo: es una diferencia de **cómo se construye, cómo se sombrea y cómo se deforma**.

---

## Idea central

```txt
                    hard surface                      organico
forma               planos, cortes, biseles           curvas continuas, masas
la arista           es informacion: una esquina       casi no existe: todo transita
                    viva dice "metal"
sombreado           aristas duras y biseles que       suave en todos lados
                    atrapan la luz
topologia           bucles de soporte junto a cada    flujo que sigue la forma y,
                    borde que tiene que quedar        si se deforma, la musculatura
                    nitido
deformacion         casi nunca: se mueve por piezas   siempre que es un personaje
                    rigidas emparentadas
```

Un error frecuente es tratar uno con las herramientas del otro: un personaje con aristas duras se ve de plástico facetado; una máquina toda suave se ve de goma.

---

## Lo que cambia para un juego

**Hard surface** se mueve por piezas: una torre que gira, una puerta, un cañón. Cada pieza es un objeto separado y nombrado, emparentado a la estructural (`RA-001`), y la animación es de transforms, no de deformación. Es barato de animar y caro de sombrear si cada bisel parte vértices.

**Orgánico** que se mueve necesita rig y topología para deformar. Lo que no se mueve —una roca— puede ser orgánico de forma y rígido de comportamiento.

---

## Cómo se juzga

```txt
se mide     aristas duras y vertices partidos (costo); solapes entre piezas rigidas
            (ley 1); en lo organico que se deforma, solapes en poses extremas
se juzga    si el sombreado dice el material correcto
```

---

## Errores comunes

```txt
Biselar todo "para que atrape la luz" y multiplicar los vertices.
Modelar un personaje con piezas rigidas que despues tienen que deformarse.
Unir en una sola malla piezas de una maquina que se mueven por separado.
Suavizar una esquina que tenia que leerse viva.
```

---

## Fuentes

- `65_Digital_Modeling` — los dos enfoques.
- Área de Arte: `RA-001_Organizacion_de_assets`, `RA-009_Personaje_y_accesorios`.

## Definición

Una malla que se dobla —un personaje, una criatura, una tela— necesita una topología pensada para el movimiento: bucles en las articulaciones, densidad donde la piel se estira y se comprime, y polos lejos de las zonas que se mueven.

---

## Idea central

**La deformación se prueba con poses, no con la malla quieta.** Una malla en reposo puede tener topología perfecta para reposo y colapsar al doblar el codo.

```txt
articulacion que dobla       bucles alrededor de ella, no a lo largo. Tres como minimo
(codo, rodilla, dedo)        es el punto de partida habitual: uno en el pliegue y uno a
                             cada lado, para que el volumen no se aplaste
articulacion que gira        hombro, cadera, cuello, muneca: el giro sobre el eje
                             retuerce la malla. Sin bucles suficientes colapsa como un
                             caramelo envuelto
cara                         bucles concentricos alrededor de ojos y boca: es donde la
                             expresion estira y comprime
```

El número de bucles es un punto de partida, no una ley: lo que decide es la prueba.

---

## La prueba de rango de movimiento

Antes de producir clips, la malla con su rig se lleva a las **poses extremas** que la animación va a pedir: brazo arriba, rodilla doblada al máximo, torso girado, el saludo de Miles con una mano.

```txt
se busca     volumen que se aplasta, caras que se cruzan, picos en el sombreado,
             accesorios que atraviesan el cuerpo
se corrige   topologia o pesos, ANTES de animar: un clip animado sobre un rig roto
             se rehace entero
```

Es la frase de `RA-012` —*el rig se valida con poses antes de producir los clips*— dicha del lado de la malla. Cómo se le pide a la IA esa prueba está en `Rigging y skinning` (IA Operativa).

---

## Cómo se juzga

```txt
se mide     solapes y espesor en cada pose extrema: arte.malla() corre sobre la malla
            deformada igual que sobre la quieta. Un accesorio que atraviesa en una pose
            es un solape real (RA-009)
se juzga    si el volumen se ve sostenido en la pose: se mira la plancha de poses
```

---

## Errores comunes

```txt
Probar la topologia en la pose A y darla por buena.
Densidad uniforme en todo el brazo y ninguna extra en el codo.
Polos en el hombro o en la rodilla.
Corregir con pesos lo que es un problema de topologia: el peso no crea volumen.
Esperar a ver el clip para descubrir que el codo colapsa.
```

---

## Fuentes

- `65_Digital_Modeling` — topología para personajes que se deforman.
- `61_Game_Anim` — el rig de juego y su prueba.
- Área de Arte: `RA-009_Personaje_y_accesorios`, `RA-012_Secuencia_alfa_y_entrega_de_animacion`.

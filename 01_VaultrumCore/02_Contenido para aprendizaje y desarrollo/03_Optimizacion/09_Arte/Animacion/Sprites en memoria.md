## Problema

La memoria de un juego 2D crece con cada animación nueva de cada personaje.

## Área

Memoria de video y tiempo de carga.

## Síntoma observable

```txt
cada personaje nuevo suma decenas de megas
la carga de un nivel tarda por las hojas de sprites
```

## Causa técnica

Una animación 2D por cuadros es una pila de imágenes. Su costo:

```txt
memoria  =  cuadros  x  ancho  x  alto  x  bytes por pixel  (+ relleno del atlas)

1 cuadro de 256 x 256, RGBA de 8 bits por canal, sin comprimir ni mipmaps   0.25 MB
1 animacion de 8 cuadros                 2 MB
10 animaciones de 8 cuadros              20 MB por personaje
las mismas, a 128 x 128                  5 MB
```

Tres cosas lo multiplican sin que se vea: animar con más dibujos por segundo de los que hacen falta (`09 - Timing`), un lienzo mucho más grande que la pose más amplia, y el espacio transparente que no se recorta al empaquetar.

## Detección

```txt
memoria de texturas por personaje en el motor
tamano de cada hoja y cuanto de ella es transparente
dibujos por segundo de cada animacion contra lo que pide el estilo
```

## Diagnóstico

Si el costo crece con la cantidad de animaciones y de cuadros, es esto. Si crece con la resolución de pantalla, es relleno de píxeles (`Overdraw y transparencias`).

## Solución

```txt
dibujos en dos                  la mitad de los cuadros donde el estilo lo permite
lienzo justo                    margen para la pose mas amplia, no el doble (RA-012)
empaquetado ajustado            recortar el transparente, compartir atlas
resolucion por distancia        el personaje que se ve chico no necesita 256
compresion donde no ensucie     el pixel art suele ir sin comprimir; la ilustracion
                                suavizada tolera compresion
reusar cuadros                  un idle que reusa el primer cuadro de la caminata
```

## Trade-off

```txt
menos dibujos      movimiento mas entrecortado
menos resolucion   menos detalle de cerca
recorte ajustado   el pivot se vuelve una coordenada a cuidar (RA-012: el pivot no se
                   mueve)
```

## Validación

Memoria por personaje antes y después, y la secuencia medida con `animacion.py`: mismo lienzo, mismo pivot, mismas siluetas.

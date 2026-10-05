## Problema

La memoria de texturas crece con cada asset, y el set se ve desparejo: unos nítidos, otros borrosos.

## Área

Memoria de video y ancho de banda.

## Síntoma observable

```txt
la memoria de texturas sube mas que la cantidad de assets
un asset chico tiene una textura enorme y uno grande una chica
al lado, uno se ve nitido y el otro borroso
```

## Causa técnica

Una textura cuesta su tamaño, no lo que muestra:

```txt
memoria  =  ancho x alto x bytes por pixel  (+ un tercio con mipmaps)

2048 x 2048, sin comprimir (4 bytes)     16 MB    con mipmaps  ~21 MB
2048 x 2048, comprimida a 1 byte         4 MB     con mipmaps  ~5.3 MB
```

La **densidad de textura** (texel density) es cuántos píxeles de textura caen en un metro de superficie. Si cada asset elige su textura por separado, la densidad varía: se gasta memoria donde no se ve y falta donde sí.

## Detección

```txt
memoria de texturas por asset en el motor
la densidad de cada asset: pixeles de textura por metro, medida sobre sus UV
espacio de UV sin usar: textura pagada que no se ve
```

## Diagnóstico

Si la memoria crece con el tamaño de las texturas y no con su cantidad, es tamaño. Si el set se ve desparejo, es densidad. El lado general —mipmaps, compresión, filtrado— es `Texturas y mipmaps`.

## Solución

```txt
una densidad para el proyecto    se fija en la guia de estilo, en pixeles por metro
la textura por lo que se ve      un objeto que se ve de lejos no necesita la densidad
                                 de lo que se ve de cerca
compresion                       la que el motor y la plataforma soporten; el pixel art
                                 suele ir sin comprimir para no ensuciar el pixel
UV aprovechadas                  sin espacio vacio en la textura
atlas                            texturas chicas juntas
```

## Trade-off

```txt
menos densidad    se ve borroso de cerca
compresion        artefactos en bordes y degradados
atlas             menos flexibilidad por pieza
```

## Validación

Memoria de texturas antes y después, y una alineación del set a la distancia de juego: misma nitidez en todos.

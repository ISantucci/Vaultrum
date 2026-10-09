## Problema

El motor procesa muchos más vértices de los que tiene la malla en el programa de modelado.

## Área

GPU (vértices y memoria de la malla).

## Síntoma observable

```txt
el DCC dice 1.200 vertices; el motor dice 3.400
un low poly facetado cuesta como una malla mucho mas densa
```

## Causa técnica

Para la GPU, un vértice es una **combinación única** de todos sus atributos: posición, normal, UV, color. Si dos caras que se tocan en un punto necesitan valores distintos de cualquier atributo en ese punto, el motor tiene que guardar **dos vértices**.

```txt
arista dura            dos normales en el mismo punto        -> se parte
costura de UV          dos coordenadas de textura             -> se parte
borde entre materiales cada material es una submalla aparte   -> se parte
```

El caso extremo es el sombreado facetado: cada cara tiene su normal, así que cada esquina de cada cara es un vértice propio. Un low poly facetado puede tener varias veces los vértices que el DCC cuenta.

No es un error: es el precio del aspecto. Lo que es error es no conocerlo.

## Detección

```txt
el conteo de vertices del motor despues de importar, contra el del DCC
en el DCC: cuantas aristas duras y cuantas costuras de UV tiene la malla
```

## Diagnóstico

Si el conteo del motor es mucho mayor que el del DCC y la malla tiene muchas aristas duras o muchas islas de UV, es esto. Si los dos conteos coinciden, el costo es la densidad real (`Caras en pantalla`).

## Solución

```txt
costuras donde ya hay aristas duras   si el vertice se parte igual por la normal, que la
                                      costura de UV vaya en el mismo lugar: se paga una vez
suave donde no hace falta duro        una arista dura que no se lee a la distancia de juego
                                      es costo sin lectura
el bisel en el mapa de normales       en vez de partir la geometria
menos islas de UV                     cada isla es un borde partido
```

## Trade-off

```txt
menos aristas duras   superficies que se ven mas blandas
costuras alineadas    menos libertad para acomodar la textura
facetado              es el estilo: se paga sabiendolo
```

## Validación

Conteo de vértices del motor antes y después, y la silueta y el sombreado a la distancia de juego sin cambios de lectura.

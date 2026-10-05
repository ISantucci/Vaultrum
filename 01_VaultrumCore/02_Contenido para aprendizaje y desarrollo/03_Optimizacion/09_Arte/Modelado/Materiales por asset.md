## Problema

Muchas llamadas de dibujo para pocos objetos.

## Área

CPU (preparación de las llamadas) y GPU (cambios de estado).

## Síntoma observable

```txt
el numero de llamadas de dibujo sube mucho con cada personaje en pantalla
el batching no agrupa objetos que parecen iguales
```

## Causa técnica

Un objeto con varios materiales es, para el motor, **varias submallas**: cada una se dibuja aparte, con su propio estado. Y dos objetos con materiales distintos no se agrupan en una misma llamada.

```txt
goblin con 10 materiales    10 llamadas por goblin
20 goblins                  200 llamadas, antes de las sombras
```

El goblin de TowerDefense trajo diez materiales nuevos. Ningún instrumento lo vio, porque las leyes que se corrían —la 1, la 2 y la 3— miden la malla: es el caso que hizo que la ley 5 mire los materiales.

## Detección

```txt
el depurador de cuadros del motor: cuantas llamadas por objeto
el censo de materiales del asset y del conjunto (arte.paleta())
```

## Diagnóstico

Si el costo crece con la cantidad de **materiales distintos** y no con las caras, es esto. Si crece con las caras, es `Caras en pantalla`. Para el lado general del problema, `Draw calls y batching`.

## Solución

```txt
un material por asset         cuando el estilo lo permite
atlas de textura              varias texturas en una, para que varias piezas compartan
                              material
color por vertice             en low poly de color plano, el color puede ir en la malla
                              y no en el material
materiales del conjunto       reusar los materiales del set en vez de crear uno por asset
                              (Paleta cerrada)
```

## Trade-off

```txt
atlas            menos resolucion por pieza, y una pieza no se cambia sola
un material      menos variedad de sombreado dentro del asset
```

## Validación

Llamadas de dibujo por instancia antes y después, y el censo de materiales del conjunto.

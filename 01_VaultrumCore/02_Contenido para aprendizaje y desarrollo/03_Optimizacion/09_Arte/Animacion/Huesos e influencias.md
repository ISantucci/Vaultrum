## Problema

El frame cae con muchos personajes animados en pantalla, aunque sus mallas sean livianas.

## Área

CPU (evaluar la pose del esqueleto) y GPU o CPU (deformar la malla, según dónde corra el skinning).

## Síntoma observable

```txt
el costo crece con cada personaje animado, no con las caras
el profiler muestra tiempo en animacion y en actualizar transforms
los personajes lejanos cuestan lo mismo que los cercanos
```

## Causa técnica

Un personaje animado se paga dos veces por cuadro:

```txt
evaluar la pose     cada hueso: leer la animacion, mezclar, resolver la jerarquia.
                    Crece con los HUESOS
deformar la malla   cada vertice: sumar la influencia de cada hueso que lo mueve.
                    Crece con VERTICES x INFLUENCIAS por vertice
```

```txt
costo por cuadro  ~  personajes animados  x  (huesos  +  vertices x influencias)
```

Los huesos secundarios —pelo, capa, cola, dedos— multiplican el primer término. Las influencias por vértice, el segundo. Muchos motores dejan fijar un tope: Unity, por ejemplo, ofrece 1, 2, 4 o ilimitadas influencias en su configuración de calidad.

## Detección

```txt
el profiler: tiempo de animacion y de skinning por cuadro
cuantos personajes animados hay a la vez, cuantos huesos tiene cada uno
cuantas influencias por vertice exporta el rig
```

## Diagnóstico

Si el costo crece con la cantidad de **personajes animados** y no baja al reducir caras, es esqueleto. Si baja al reducir caras, es `Caras en pantalla`.

## Solución

```txt
presupuesto de huesos por familia   un enemigo de oleada no lleva dedos animados
tope de influencias                 el que la plataforma pide, verificado en el rig
                                    antes de animar (Rigging y skinning)
niveles de detalle de esqueleto     menos huesos lejos: los secundarios se apagan
huesos secundarios por necesidad    pelo y capa por simulacion solo en lo que se ve cerca
animar menos seguido lo lejano      ver Animacion fuera de camara
```

## Trade-off

```txt
menos huesos          animacion menos expresiva
menos influencias     deformacion mas dura en las articulaciones
LOD de esqueleto      la continuacion y la superposicion desaparecen de lejos
```

## Validación

Tiempo de animación y skinning con la oleada completa, antes y después, y una prueba de poses extremas para ver que la deformación sigue sosteniendo el volumen.

# Texturizado, UV y materiales

## Qué hace Vaultrum acá

Despliega las UV de una malla, mide la densidad de textura, asigna materiales desde la paleta del proyecto y, si hace falta, hornea un mapa de normales de una versión detallada a una liviana.

## Con qué opera la IA

En Blender, por MCP, con Python:

```txt
UV           costuras marcadas donde ya hay aristas duras (se paga una vez el vertice
             partido) y despliegue; empaquetado de islas sin solapes
densidad     pixeles de textura por metro: area de cada cara en la UV contra su area en
             3D, por script, comparada con la de la guia de estilo
materiales   desde la paleta cerrada del proyecto, y los menos posibles por asset; en
             low poly de color plano, color por vertice en vez de un material por color
horneado     mapa de normales de la version densa a la liviana, cuando el estilo pide
             detalle que la geometria no puede pagar
```

## Lo que se verifica por script

```txt
islas de UV          cuantas, y que ninguna se solape ni salga del espacio 0-1 sin querer
densidad             la misma en todo el set, dentro de la tolerancia de la guia
materiales           cuantos por asset y si alguno no esta en la paleta (arte.paleta())
vertices partidos    cuanto suman las costuras al conteo que ve el motor
```

Una textura que viene de un generador de imagen pasa por lo mismo: se mide contra la paleta antes de aceptarla.

## Cómo pedírselo

```txt
"Desplegá y texturizá <asset> con la densidad de <proyecto>, materiales de la paleta.
 Reportame islas, densidad, materiales y vertices partidos."
```

## Lo que no hace

No elige la paleta: sale de la mitad A. No decide el estilo de la textura: dirección de arte.

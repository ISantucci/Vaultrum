## Definición

La **topología** es cómo están conectados los vértices y las caras de una malla, independiente de su forma. El **flujo de aristas** (edge flow) es la dirección en que corren los bucles de aristas sobre la superficie.

```txt
bucle de aristas (edge loop)   una cadena de aristas que da la vuelta a la forma
anillo de aristas (edge ring)  las aristas paralelas que cruzan un bucle
polo                           un vertice con distinto de cuatro aristas: 3 o 5
```

---

## Idea central

**La topología buena sigue la forma.** Los bucles corren por donde la forma cambia de dirección: alrededor de un ojo, a lo largo de un brazo, por el borde de un bisel.

```txt
quads           se subdividen limpios, se seleccionan por bucles, se deforman parejo
polos           son inevitables y necesarios: es donde el flujo cambia de direccion.
                Se ponen donde la superficie es plana o no se deforma
densidad pareja  caras de tamano parecido en la misma zona. Un salto brusco de
                densidad se ve en el sombreado y en la deformacion
```

La topología de una malla quieta y de baja densidad casi no importa: se triangula y nadie la ve. Importa cuando la malla se **subdivide**, se **deforma** o se **edita** después.

---

## Lo que cambia según el destino

```txt
asset estatico de juego     limpieza suficiente para que el sombreado no muestre
                            artefactos; triangulos y algun ngon plano son aceptables
malla que se subdivide      quads, sin ngons, polos lejos de las curvas
malla que se deforma        ver Topologia para deformar
malla para esculpir         densidad pareja; la topologia final sale de la retopologia
```

---

## Cómo se juzga

```txt
se mide     cantidad de ngons, de triangulos, de polos y su ubicacion: es conteo
            sobre la malla y se puede correr por script (bmesh)
se juzga    si el flujo sigue la forma: se mira con el wireframe sobre el sombreado
```

---

## Errores comunes

```txt
Polos en una articulacion o en el medio de una curva visible.
Ngons en zonas que se subdividen o se deforman.
Densidad altisima en una zona que no se ve y baja en la silueta.
Flujo que cruza la forma en diagonal: el sombreado muestra rayas.
Retopologia "a mano" sin mirar el flujo final: se termina con quads que no siguen nada.
```

---

## Fuentes

- `65_Digital_Modeling` — topología, flujo y polos.
- `71_Blender_Manual` — las herramientas de bucle y anillo.

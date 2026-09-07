# RA-004 — De blueprint a malla

**Insumo:** blueprint VW Voyage entregado por el owner (2026-09-01) con cuatro vistas y seis cotas.
**Estado:** Vigente.

## La regla

> Un blueprint no se calca: **se leen sus cotas y se construye contra ellas.** La imagen dice la forma; solo los numeros dicen el tamano, y hay que verificar cada uno con su delta en milimetros.

Calcar la silueta a ojo da algo que se parece. Construir contra las cotas da algo que **entra en el mundo del juego** al lado de otros assets.

## El metodo, en orden

```txt
1. Transcribir las cotas         y marcar cual falta y cual se contradice
2. Derivar lo que no esta dicho  voladizos, trocha, alturas intermedias
3. Elegir estaciones             sobre los quiebres del perfil, no equiespaciadas
4. Loftear                       un anillo de N puntos por estacion, N constante
5. Medir y declarar              cada cota contra el blueprint, con delta en mm
```

El paso 3 es el que decide si el modelo se parece: las estaciones van **donde la forma cambia** —cara delantera, eje, base del parabrisas, techo, base de la luneta, cola—, no cada 40 cm.

## Cotas: lo que el blueprint dice y lo que hay que derivar

```txt
DADO      largo 4218 · ancho 1664 · alto 1472 · entre ejes 2470
DERIVADO  voladizo delantero 800 · voladizo trasero 948
          -> ejes en x = +1309 y x = -1161  (suman 2470 y cierran 4218)
```

**Una cota del blueprint es imposible y hay que decirlo:** declara *ancho de via delantera 1664*, identico al *ancho total*. Una trocha nunca puede igualar el ancho: las ruedas tendrian que estar fuera de la carroceria. Se lee como **ancho de la carroceria medido en la vista frontal** (y 1652 en la trasera), y la trocha real se deriva del ancho del neumatico: 1436 adelante, 1424 atras.

**Anotar la contradiccion no es opcional.** Si se la modela literal, el auto sale con las ruedas afuera y nadie sabe por que.

## Cotas: que se mide y que se excluye

```txt
largo   incluye paragolpes           4218
ancho   EXCLUYE espejos              1664   (con espejos: 1890)
alto    EXCLUYE antena               1472   (con antena: 1627)
```

Las dos exclusiones no son licencia: son la convencion con la que el blueprint mismo esta acotado. Pero **todo lo demas entra**, y ahi aparecio el primer defecto real: las manijas sobresalian 27 mm y el ancho medido daba **1718**. Se resolvieron **embutidas** —se cala un hueco en la puerta y la pieza entra ahi— y el ancho volvio a 1664.

Ese es el criterio: si una pieza rompe la cota, se rehace la pieza, no se cambia la cota.

## La ley de la junta (separar en paneles sin cruces)

Un panel separado de una cascara cerrada es una superficie abierta. Para que sea solido hay que **solidificarlo** con espesor `t`, y para que no toque al vecino hay que **retraerlo** una luz `s`. Entre dos paneles perpendiculares, el solido de A invade el plano de B exactamente `t`. De ahi:

```txt
                    s > t
```

```txt
primer intento    t = 12 mm · s = 2.5 mm por escala uniforme  ->  46 pares cruzados
segundo intento   t =  3 mm · s = 4 mm por inset real         ->  0 pares
```

Y la escala uniforme **no sirve** como retraccion: en un panel largo (el piso, 3.9 m) mueve las puntas 4 mm y los costados 1.4 mm. Hay que usar un **inset real** (`bmesh.ops.inset_region` + borrar el aro), que retrae la misma distancia en todo el borde.

Efecto secundario util: esa luz **es la junta de chapa**. A 4.2 m, 4 mm entre paneles perpendiculares y 8 mm entre coplanares se leen como las lineas de un auto de verdad.

## Origenes: cada abertura gira sobre su bisagra

```txt
Capot        borde trasero, sobre la base del parabrisas
Baul         borde delantero
Puertas      su parante (A para las delanteras, B para las traseras)
Resto        centro geometrico
Asset        Piso, en (0,0,0) a nivel de suelo    <- ancla de RA-001
```

Una puerta con el origen en su centro no se puede abrir con una rotacion. Poner el origen en la bisagra convierte una animacion en un solo canal de rotacion.

## Lo que encontro el instrumento y no se veia

Cinco corridas de `verificar_malla` sobre el mismo auto:

```txt
46 pares cruzados        toda la adyacencia entre paneles: s < t
5 normales invertidas    las piezas espejadas con y0 > y1 -> escala negativa en Y
1 cruce escape-paragolpes
+11 mm de largo          el escape sobresalia del blueprint
+54 mm de ancho          las manijas
```

**Ninguno de los cinco se veia en el render.** El auto se veia bien en las tres vistas antes de correr el instrumento. Es el argumento entero de RA-002.

## Ampliacion de RA-001 — el prefijo del asset

Con mas de un asset en la escena, los nombres de pieza chocan: `Techo` ya existia en la torre de arqueras, `Puerta` iba a chocar con cualquier edificio. Blender resuelve el choque solo, agregando `.001`, y ahi se pierde la trazabilidad.

```txt
Voyage_Techo · Voyage_Puerta_DI · Torre_Techo
```

**El nombre de un objeto lleva el prefijo de su asset.** La collection agrupa; el prefijo desambigua.

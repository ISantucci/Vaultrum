# RA-005 — Blueprint sin cotas

**Insumo:** blueprint "Stylized Small Tower" entregado por el owner (2026-09-01): cinco vistas, cero medidas. El unico dato numerico es *Unit: Blender Unit (1.0)*.
**Estado:** Vigente.

## La regla

> Un blueprint sin cotas entrega **proporcion, no tamano**. La proporcion se mide sobre el dibujo; el tamano se fija aparte y **se declara**. Nunca se inventa una cota y se la presenta como si viniera del plano.

## Que dice y que no dice "Unit: Blender Unit (1.0)"

Dos lecturas posibles, y hay que elegir una a la vista:

```txt
A) el asset mide 1.0 unidad          -> una torre de 1 m: una maqueta
B) 1 unidad blender = 1.0 (metro)    -> declara el sistema, no el tamano
```

Se tomo **B**, que es la convencion habitual en una hoja de asset y la unica compatible con RA-003 (metros reales). **La eleccion se declara aca porque no la resuelve el plano.**

## Proporcion: se mide sobre el dibujo

```txt
alto total / huella           1.30  (medido en la vista frontal del blueprint)
reparto vertical              muro 70% · banda del parapeto 19% · almenas 11%
almenas                       12: 4 esquineras + 2 por lado  (contadas en la vista superior)
piso                          5 tablas paralelas             (contadas en la vista superior)
```

El modelo replica ese reparto: 2.09 / 0.56 / 0.34 sobre 3.00 m -> 70% / 19% / 11%.

## Cuando la proporcion y la funcion se contradicen

RA-003 dice: fijar primero la cota que la funcion exige y derivar el resto. **Aca eso no se puede**, y hay que decirlo en vez de disimularlo:

```txt
pasarela (piso de tablas)   2.656 m
coronamiento (almenas)      3.000 m
almena sobre la pasarela    0.344 m   <- a la rodilla
```

Una almena real cubre al defensor hasta el pecho: 1.2 a 1.8 m sobre la pasarela, o sea **el 45% de la altura**, no el 11%. La proporcion del blueprint es **estilizada**, no funcional. Derivar el tamano de la funcion habria dado una torre distinta a la dibujada.

**Decision: manda el dibujo, y la contradiccion se declara.**

```txt
El tamano se fija por ROL en la escena, no por funcion:
  "Small Tower" -> 3.00 m = 0.67x el arbol (4.50) y 0.46x la torre de arqueras (6.47)
  Es la mas chica de las tres. El nombre y la escena coinciden.
```

Si el owner quiere que un personaje se cubra ahi, hay dos caminos y ninguno es gratis: escalar x2.2 (y deja de ser "small"), o subir las almenas al 45% (y deja de ser este blueprint).

## Cierre de la pregunta abierta de RA-001 — el ancla

RA-001 dejaba abierto que hacer cuando **no hay una pieza central que toque el piso**. Se cierra con una regla, probada en dos assets:

```txt
Si hay una pieza que abarca la planta y toca el suelo    -> esa es el ancla
    torre de arqueras -> Cimiento     ·  Voyage -> Piso
Si no la hay                                             -> la PRIMERA pieza
    estructural, y su ORIGEN se lleva al origen del asset, no a su centroide
    torre chica -> Poste_01, con origen en (0,0,0) de la torre
```

El empty sigue descartado: una pieza real que ya existe cumple el rol sin agregar un objeto vacio al export.

## La trampa del emparentado (costo: 4 corridas)

Al llevar el origen del ancla y emparentar en el mismo bloque de codigo, `matrix_world` **todavia tiene el valor viejo**: Blender no lo recalcula hasta el proximo `view_layer.update()`. El `matrix_parent_inverse` sale mal y **todo el asset queda corrido** —en este caso 0.92 m en X e Y y 1.05 m en Z— con la malla intacta y el veredicto de RA-002 en verde.

```txt
Sintoma:  verificar_malla dice EN LEY y el bbox esta mal.
Causa:    matrix_world sin actualizar entre mover el origen y emparentar.
Arreglo:  hijos construidos en coordenadas del asset -> parent_inverse = IDENTIDAD
          y el origen del ancla se ubica por su bounding box local.
```

**Leccion mas grande:** `verificar_malla` prueba la MALLA, no el EMPLAZAMIENTO. Un asset puede estar perfecto y estar en el lugar equivocado. Por eso toda verificacion cierra tambien con **bbox, z_min y centro** — que fue lo unico que delato el error.


---

## Ampliacion - el blueprint generado por IA (2026-09-04)

Se le pidio a ChatGPT una hoja de referencia de un mortero estilizado con el prompt
escrito en esta sesion. **Salio buena: nueve vistas, objeto reconocible, barra de
specs.** Y sirve exactamente hasta donde dice esta nota: da proporcion, no cota.

**Lo que la hoja acerto** -y hay que decirlo, no solo criticar-: el cano aparece
VERTICAL en la vista Front y a ~40 grados en las vistas laterales. Eso no es una
contradiccion: es un cano inclinado puramente en Y, que de frente se ve derecho.
Las cinco ortograficas son coherentes entre si en la inclinacion.

**Donde se contradice:**

```txt
largo del cano deducido de la vista Front    ~2.15 m   (extension en Z / cos 40)
largo del cano medido en la vista Side       ~1.70 m
                                             -------
                                             26% de diferencia, mismo objeto,
                                             misma hoja
```

Se modelo **2.00 m**, entre las dos, y se declara. No hay forma de "resolver" la
contradiccion: no existe la cota, existen dos dibujos que no coinciden.

```txt
Un blueprint humano sin cotas   da proporcion, y sus vistas SI concuerdan.
Un blueprint generado por IA    da proporcion APROXIMADA, y sus vistas pueden
                                no concordar entre si.
```

**Consecuencia practica:** con una hoja generada por IA, antes de modelar hay que
**cruzar la misma medida en dos vistas distintas**. Si dan distinto, se elige un
valor, se declara la horquilla, y se sigue. Lo que no se puede hacer es tomar una
sola vista y llamarla cota.

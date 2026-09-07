# RA-006 — Relleno y espesor

**Insumo:** correccion del owner, 2026-09-01, sobre la torre bomba:
> *"no todo sea tan vacio como el auto, las cosas deben tener un relleno. La torre esta bien que por dentro este vacia ya que por ahi subiria la arquera, pero aca el piso debe ser solido, es roca. Los troncos tambien son rigidos, tienen relleno, pero las tablas mas finas."*

**Estado:** Vigente.

## La regla

> **Macizo por defecto. La cascara es la excepcion y hay que justificarla.**
> Una pieza es hueca solo cuando el hueco es un espacio que algo ocupa de verdad.

RA-002 pedia malla cerrada y sin caras interiores. Eso hace que una cascara de 3 mm **pase el mismo control** que un bloque de piedra: las dos son solidos topologicos. Faltaba la pregunta del material.

## La prueba del corte

```txt
Si la cortaras al medio, que verias?

  masa continua        -> MACIZO      roca, tronco, viga, tabla, ladrillo
  un espacio util      -> CASCARA     habitaculo de un auto, interior de una torre
                                      por la que sube alguien, un aro de soga
```

El hueco tiene que **servir para algo**. El interior de la torre de arqueras es hueco porque la arquera sube por ahi. El aro de una soga es hueco porque **por ahi pasa el tronco**. Un cimiento de piedra no tiene nada adentro: es piedra.

## Tabla de espesores

El espesor no se elige: lo dicta el material.

```txt
roca / mamposteria        macizo, la pieza ES la masa    150 mm +
tronco / poste / viga     macizo, seccion completa        80-200 mm
tabla de piso             fina pero maciza                40-80 mm
liston / travesano        fino pero macizo                20-40 mm
soga (seccion del cordon) tubo real                       20-30 mm
tela / venda / lona       piel                            10-25 mm
chapa de auto             cascara                          2-4 mm
```

Fino y hueco **no son lo mismo**. Una tabla de 55 mm es fina y maciza. Un capot de 3 mm es una cascara. La distincion es lo que se le escapaba al auto.

## El instrumento

No se juzga a ojo. `verificar_malla.relleno(objeto)`:

```txt
espesor equivalente = 2V/A
```

Para una chapa de espesor t da t. Para un cubo de lado L da L/3. Es el espesor real del material, medido, en milimetros.

```txt
razon = espesor_eq / dimension mas chica

  >= 0.28  macizo
  >= 0.12  intermedio
  <  0.12  cascara
```

**Limite declarado:** la razon falla en piezas casi planas. `Voyage_Techo` es una cascara de 3 mm y la razon la clasifica "intermedio" (0.13), porque el panel es tan chato que su bbox mas corto (22.9 mm) ya es casi el espesor. **El numero que se lee es `espesor_eq_mm`**; la clase es una ayuda, no el veredicto.

## Lo que midio sobre los seis assets

```txt
Bomba_Cimiento    roca      296.4 mm   macizo
TorreChica_Poste  tronco    162.0 mm   macizo
Bomba_Pata_01     tronco    108.6 mm   macizo
Bomba_Viga_01     viga       97.3 mm   macizo
Bomba_TablaPalco  tabla      54.4 mm   macizo    <- fina Y maciza
Bomba_Soga_01     soga       24.2 mm   cascara   <- a proposito: el aro rodea el tronco
Bomba_Venda       tela       19.6 mm   cascara   <- a proposito: la tela es piel
Voyage_Capot      chapa       3.0 mm   cascara
```

```txt
asset            macizo  intermedio  cascara
Torre_Bomba         29        0         5     las 5 son sogas y venda: correcto
Torre_Chica         30        0         0
Torre_Arqueras      13        1         0
Fogata              11        1         0
Arbol                4        1         0
Voyage              31        1        21     las 21 son la chapa: correcto
```

**Cero huecos no intencionales en los seis assets.** Las 26 cascaras del vault estan todas justificadas por material.

## Lo que esto habria cambiado en el auto

Nada, y eso es el punto: el Voyage esta bien como cascara —una carroceria **es** chapa sobre un espacio util. El defecto no era el auto: era **no tener escrito por que**. Sin esta nota, el proximo asset se modela hueco por costumbre y no por decision, y ahi si sale mal: una roca hueca se rompe al primer corte booleano, pesa lo mismo y se ve peor en cualquier corte de camara.


---

## Ampliacion - la razon falla en DOS casos mas (2026-09-04)

`RA-006` ya declaraba que la razon `espesor_eq / dimension_minima` se equivoca en
piezas casi planas. El mortero sumo dos casos mas, y los tres tienen la misma causa:
**la razon usa el bounding box alineado a los ejes, y el AABB miente.**

```txt
pieza INCLINADA     una viga de 130 x 110 x 766 girada en el espacio tiene un AABB
                    de 440 x 630 x 420. La dimension minima deja de ser el espesor
                    de la viga y pasa a ser una diagonal.
                    Puntal_01: espesor_eq 55.3 mm -> MACIZO, y la razon dice cascara.

objeto MULTI-ISLA   `Roblones` son 18 cabezas de 58 mm repartidas por todo el cano.
                    Su AABB abarca el cano entero. La razon da casi cero.
                    espesor_eq 16.4 mm -> es un roblon, y es macizo.
```

```txt
Se lee espesor_eq_mm. La CLASE es una ayuda que se rompe en tres casos:
pieza casi plana - pieza inclinada - objeto multi-isla.
```

En el mortero las 13 piezas dieron el espesor correcto y **solo dos huecos reales**
-`Bandas` y `Collar`, que abrazan el cano-, mas el anima del propio cano, que es
para lo que existe un mortero. Cero huecos no intencionales.

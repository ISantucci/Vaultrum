# RA-008 - Origen por funcion, y verificar el instrumento

**Insumo:** bala de mortero y flecha, 2026-09-04. Los dos primeros PROYECTILES del
registro, y los dos primeros assets con piezas de milimetros.
**Estado:** Vigente.

## Regla 1 - el origen sigue a la funcion

`RA-003` decia "origen del asset en el suelo". Eso vale para lo que se apoya. Un
proyectil no se apoya: vuela, y en el aire gira sobre su centro de masa.

```txt
lo que se APOYA   -> origen en el piso, centro de la planta      (edificios)
lo que VUELA      -> origen en el CENTRO DE MASA                 (proyectiles)
```

El centro de masa no se estima: se calcula por volumen x densidad de CADA material,
con el teorema de la divergencia sobre los triangulos. `centro_masa()` en
`primitivas.py`. Sirve igual para un solido hueco, que es justo el caso de la bala.

```txt
Bala    115.99 kg   residual del centro de masa: 0.000 mm en los tres ejes
Flecha   43.9 g     equilibrio al 65.3% desde el culatin
```

## Regla 2 - el instrumento tambien se verifica

`verificar_malla` venia reportando **normales invertidas donde no las habia**. La
causa estaba en mi propia herramienta:

```txt
_stats guardaba:  "vol": round(bm.calc_volume(signed=True), 5)
y el test hacia:  invertidas = [k for k,v in st.items() if v["vol"] <= 0]
```

Toda pieza de menos de ~1 cm3 redondeaba a `0.00000` y caia en `<= 0`.

```txt
Bala_Mecha        0.00000199 m3   -> round(.,5) = 0.00000  -> "invertida" (falso)
Flecha_Punta      0.00000263 m3
Flecha_Culatin    0.00000135 m3
```

**Seis assets pasaron por esta herramienta sin que apareciera**, porque todos median
entre 0.9 y 6.5 m. El primero con piezas de milimetros la rompio.

```txt
Una herramienta que verifica todo no esta verificada hasta que se la prueba
en el EXTREMO de su rango. Aca el extremo era el tamano.
```

Arreglo: el signo se prueba sobre el valor crudo; el redondeo queda solo para
mostrar.

## Regla 3 - un asset recentrado se reconstruye entero

Despues de recentrar la flecha sobre su centro de masa, se reconstruyeron **dos de
las cuatro piezas**. Las nuevas nacieron en el marco original y las viejas ya estaban
corridas: la flecha midio **1.1456 m** en vez de 0.69.

```txt
Recentrar mueve la MALLA, no el objeto. Cualquier pieza construida despues
nace en el marco viejo y el asset queda partido.
-> una vez recentrado: o se reconstruye COMPLETO, o no se toca.
```

Es primo del error de `RA-005` (el `matrix_world` sin actualizar): las dos veces el
veredicto de `RA-002` dio verde y **la cota fue lo unico que delato el problema**.

## Regla 4 - lo que interactua se verifica CONTRA lo otro

Una bala no se verifica contra su propia ficha: se verifica **metiendola en el canon
que ya existe**. Se bajo el proyectil por el anima del mortero ya modelado, con
BVHTree, en cuatro posiciones:

```txt
holgura radial        28.1 mm, constante en todo el recorrido
asiento minimo        s = 1.188 m  (mas abajo el anima se cierra: choca)
recorrido util        0.812 m
camara de polvora     24.65 L      (el hueco que queda debajo de la bala asentada)
```

El primer intento **choco a s = 1.10**. No era un defecto: es la camara. El
instrumento encontro donde apoya la bala sin que nadie se lo dijera.

## La masa como cota, otra vez

La flecha salio de **89.4 g** contra los 25-40 g de una flecha real: la punta sola
pesaba 62 g. Se afino a bodkin (radio maximo 6.2 mm) y quedo en **43.9 g**.

Es la regla 2 de `RA-007` -una especificacion medible se ajusta- aplicada cuando el
pedido **no trae la cota**: el objetivo salio del rango de referencia del objeto real.

---

## Adenda (Goblin) — el paso de jerarquía puede *introducir* la falla

Con el goblin entero construido, el diagnóstico dentro del build daba **0 pares
cruzados**. `verificar("Goblin")` daba **FUERA DE LEY: interpenetración**. Las
dos cosas eran ciertas: la interpenetración no estaba en la geometría, la creaba
el paso de armar la jerarquía.

`emparentar()` usa **parent inverse identidad**. Eso no es un detalle de
implementación: es un **contrato**. Exige que, al momento de emparentar,

1. la geometría de cada hijo ya esté en **coordenadas del asset**, y
2. la `location` de cada hijo sea **cero**.

Si se llega con la `location` sin hornear — y se llega, porque
`separar_dirigido()` y `relajar()` mueven `location` — o con el origen del ancla
fuera de cero, **cada hijo se corre el origen del ancla**. Acá fueron 29 mm en X
y 43 mm en Y: nada se cae, nada se ve raro, el bbox sigue siendo razonable y
`z_min` sigue dando 0. Lo único que se rompe es lo que tenía holgura menor a
ese corrimiento: los tirantes, que llevaban 6 mm.

Secuencia correcta, en este orden:

1. terminar **toda** la geometría;
2. calcular el origen del asset (acá, el centro entre los pies a nivel de piso);
3. **hornear**: `data.transform(Translation(location - origen))` y `location = 0`
   para **todos**, ancla incluida;
4. recién ahí `emparentar()` y mover el ancla a donde va el asset.

Es la cuarta vez que aparece la misma familia — torre chica corrida, agujas
hundidas, flecha partida en dos — pero es la primera en que el defecto **no
existía** hasta que lo introdujo el paso de colocación. De ahí la regla:

> **RA-008.5 — Verificar SIEMPRE después de emparentar, nunca antes.**
> Una verificación que corre sobre la geometría suelta no dice nada sobre el
> asset que se va a exportar.

## Propósito

Medir las leyes 1, 2 y 3 sobre la geometría, después de emparentar, y rebotar lo que encuentra sin tocarlo. Es el gate de malla del área.

---

## Entrada del flujo

- El asset que sale de `03_Modelador`, ya emparentado.
- El mismo asset otra vez, después de que `04` o `05` hayan tocado geometría o materiales.
- En modo Pasada, el set completo: `06` abre la pasada y `06` la cierra.

Corre siempre, en los tres modos. No es condicional.

---

## Transformación que realiza

- Corre `arte.malla()` con `06_Verificador_Malla`, después de emparentar.
- Ley 1, nada se atraviesa, todo mira afuera, todo cierra: `BVHTree.overlap`, signo de `calc_volume` sin redondear, aristas con cantidad de caras distinta de 2.
- Ley 2, relleno y espesor declarados: espesor equivalente `2V/A`. Se lee `espesor_eq_mm`, no la clase: el clasificador macizo/intermedio/cáscara es una razón contra el bbox, y el bbox miente en pieza casi plana, inclinada o con varias islas.
- Ley 3, la medida es real y la colocación se verifica después de emparentar: bbox, `z_min`, centro, transform. Corolario `RA-008.5`: *verificar prueba la MALLA, no la COLOCACIÓN*.

---

## Salida esperada / formato

```txt
## Corrida
   primera o segunda, y qué la disparó
## Ley 1
## Ley 2
   espesor_eq_mm por pieza
## Ley 3
   bbox, z_min, centro, transform
## Rebotes a 03
   un hallazgo concreto por línea
```

---

## Las dos corridas, y por qué no repara

En modo Producción corre dos veces: después de `03_Modelador`, y otra vez después de que `04` o `05` hayan tocado algo. La segunda no es ceremonia, es la consecuencia de haber modificado geometría o materiales. Lo medido antes del cambio no dice nada del asset que quedó.

No toca geometría, nunca. Rebota el hallazgo concreto a `03_Flujo_Construccion`. Si arreglara lo que encuentra, nadie revisaría el arreglo.

---

## Los cuatro defectos, y el límite del instrumento

Cuatro defectos que atrapó y que una inspección visual perfecta dejó pasar: la torre chica corrida 0.92 / 0.92 / 1.05 m en el bbox; dos agujas hundidas 109 y 113 mm en la roca, sobre 192 raycasts; la flecha en dos marcos de coordenadas, 1.14 m contra los 0.69 m declarados; el goblin con los tirantes dentro del torso, visible recién al verificar después de emparentar.

El verificador también tuvo su defecto: redondeaba el volumen antes de mirarle el signo, y seis assets pasaron porque medían entre 0.9 y 6.5 m. La flecha, el primer asset a escala de milímetros, lo rompió. *El instrumento también se verifica, en el extremo de su rango.*

---

## Criterios de aceptación

- La corrida es posterior a emparentar. Una anterior no cuenta.
- Se lee `espesor_eq_mm`, nunca la clase.
- El volumen se lee sin redondear.
- Cada hallazgo sale con su número y su pieza.
- Está declarado qué corrida es y qué la disparó.

---

## Condiciones para avanzar

Avanza a `07_Flujo_Entrega` si hay entrega en formato externo. Si no la hay, el `ART-XXX.n` cierra acá y la omisión de `07` se declara con su razón.

Vuelve a `03_Flujo_Construccion` con el hallazgo si alguna de las tres leyes está en rojo. Después de esa reparación no cierra nada: se corre `06` de nuevo.

---

## Qué debe evitar

No modela ni corrige. No verifica antes de emparentar. No lee la clase en lugar del espesor. No redondea. No da por buena una medida porque el asset se ve bien.

---

## Resultado final

El estado de las leyes 1, 2 y 3 con el número de cada falla, y el `ART-XXX.n` cerrado o rebotado a `03_Flujo_Construccion`.

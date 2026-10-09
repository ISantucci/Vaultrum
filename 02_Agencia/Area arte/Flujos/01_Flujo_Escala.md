## Propósito

Fijar el presupuesto de escala del proyecto antes del primer asset, y cerrar con eso la mitad A del `ART-XXX.n`.

---

## Entrada del flujo

- `LDS` cerrado: la grilla del espacio, el ancho del camino, la cámara.
- `GDS`: qué rol juega cada objeto y qué tiene que leerse como qué.
- `UXS` en su mitad A.

Corre una vez por proyecto. Se vuelve a correr sólo si cambia el espacio, la cámara o la plataforma.

---

## Transformación que realiza

- `01_Director_Escala` fija la dimensión maestra, la altura de referencia funcional, el presupuesto de caras por familia y el contrato de exportación.
- `05_Guardian_Visual` declara la paleta del proyecto.
- Con esas decisiones escritas se cierra la mitad A del `ART-XXX.n`.

Este flujo produce números y reglas, no geometría.

---

## Salida esperada / formato

```txt
## Dimensión maestra
   valor y línea del LDS de la que sale
## Altura de referencia funcional
## Presupuesto de caras por familia
   una línea por familia
## Contrato de exportación
   unidades, orientación, origen
## Paleta declarada
```

Se registra como mitad A del `ART-XXX.n`.

---

## Por qué existe, medido

En el proyecto en curso la celda de 3.00 m se decidió midiendo cuántos de los 8 assets ya construidos entraban: con 2.5 m entraban 4, con 3.0 m entraban 6, con 3.5 m entraban 7. Se eligió 3.0 porque la celda es también el ancho del camino, y un Gigante tiene que llenarlo para leerse como tanque.

Salió bien y salió al revés. La dimensión se dedujo de los assets en lugar de que los assets salieran de la dimensión. Con un asset más de los que había, no entraba ninguna. La dimensión maestra se decide una vez, antes del primer asset, y sale del `LDS`.

---

## Criterios de aceptación

- La dimensión maestra cita la línea del `LDS` de la que sale.
- La altura de referencia funcional está en metros y sirve para comparar cualquier asset.
- Cada familia tiene su presupuesto de caras. Ninguna queda sin número.
- El contrato de exportación dice unidades, orientación y origen.
- La paleta está declarada antes de que exista el primer material.
- Ningún asset se construyó para llegar a estos números.

---

## Condiciones para avanzar

Avanza a `02_Flujo_Referencia` con la mitad A cerrada.

No avanza si no hay `LDS`. Sin la grilla del espacio, la dimensión maestra sale de la nada y se termina corrigiendo contra assets ya construidos.

---

## Qué debe evitar

No modela. No mide assets existentes para deducir la dimensión. No deja una familia sin presupuesto hasta ver cómo sale. No elige la paleta por gusto del asset que toca primero.

---

## Resultado final

El presupuesto de escala del proyecto escrito y cerrado, antes de que exista geometría que lo condicione.

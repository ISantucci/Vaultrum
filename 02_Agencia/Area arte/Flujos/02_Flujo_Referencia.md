## Propósito

Convertir la referencia que trae el owner en una proporción derivada y verificada, apta para construir.

---

## Entrada del flujo

- La referencia tal como llega: blueprint, foto o descripción escrita.
- La mitad A del `ART-XXX.n` cerrada: dimensión maestra, altura de referencia funcional, presupuesto de la familia.

Sin la mitad A no hay contra qué medir, y la referencia queda flotando.

---

## Transformación que realiza

- `02_Analista_Referencia` lee la referencia y extrae la proporción.
- Toma la misma medida en dos vistas antes de que se modele nada.
- Cuando no hay cotas, deriva la escala del rol del objeto en el juego contra la altura de referencia funcional, nunca del dibujo.
- Declara lo que falta: qué no se ve, qué no se puede medir, qué queda a criterio del modelador.

---

## Salida esperada / formato

```txt
## Proporción derivada
   medida — vista 1 — vista 2 — diferencia
## Escala contra la referencia funcional
   rol del objeto y comparación
## Lo que falta
## Lo que decide el modelador
```

---

## La regla de las dos vistas

Un blueprint generado por IA da proporción aproximada, no medidas, y sus vistas no coinciden entre sí. En el mortero del proyecto en curso la misma pieza medía 2.15 m de frente y 1.70 m de lado: 26% de diferencia. Leída en una sola vista, esa medida habría entrado a construcción como si fuera un dato.

Evidencia de que la regla funciona en la otra dirección: el Ø 2.400 m exacto de la base de ese mismo mortero salió de un blueprint sin cotas, leído en dos vistas y anclado al rol del objeto.

---

## Criterios de aceptación

- Toda medida que pasa a construcción se leyó en dos vistas.
- Las discrepancias están escritas con su porcentaje, no promediadas en silencio.
- La escala final se justifica contra la altura de referencia funcional y el rol del objeto, no contra el dibujo.
- Lo que falta está declarado: una omisión declarada es criterio, una omisión silenciosa es un hueco.

---

## Condiciones para avanzar

Avanza a `03_Flujo_Construccion` con la proporción derivada y lo que falta declarado.

No avanza si las dos vistas discrepan y nadie decidió cuál manda. Una discrepancia sin dueño se resuelve sola dentro del script del modelador y se paga rehaciendo el asset.

---

## Qué debe evitar

No modela. No promedia dos vistas que no coinciden para sacarse el problema de encima. No trata un blueprint sin cotas como si fuera un plano cotado. No completa lo que no ve inventándolo en vez de declararlo. No toca la dimensión maestra: si la referencia no entra, eso vuelve a `01_Flujo_Escala`.

---

## Resultado final

Una proporción que se puede construir, con su origen medido y sus huecos escritos.

## Propósito

Bajar el costo en pantalla del asset o del set completo, sin perder la lectura.

---

## Entrada del flujo

- Un asset que excede el presupuesto de caras de su familia, con el número.
- O el set completo, en modo Pasada.

Es un paso condicional. Si ninguna de las dos condiciones se cumple, no corre y declara la omisión con su razón: una omisión declarada es criterio, una omisión silenciosa es un hueco.

---

## Transformación que realiza

- `04_Optimizador`, dueño de la ley 4, mide caras por instancias máximas simultáneas, no caras en el archivo.
- Aplica palancas: densidad de anillos, ngons cóncavos, islas, piezas que nadie ve, LOD.
- Declara la deuda técnica del arte que queda abierta.

Es el único paso del área que puede reducir geometría.

---

## Salida esperada / formato

```txt
## Medición
   caras — instancias máximas simultáneas — total en pantalla
## Palancas aplicadas
   cuál, y qué costó en lectura
## Resultado contra el presupuesto de la familia
## Deuda técnica declarada
## Omisión, si no corrió
```

---

## Qué número decide

El goblin cerró en 817 caras, y 817 no significa nada. El número que decide es 817 por 20 goblins simultáneos: 16.340 caras en pantalla. Un asset barato instanciado veinte veces sale caro; uno caro que aparece una vez puede no serlo. El presupuesto se lee contra el peor caso simultáneo, nunca contra el archivo abierto.

---

## Regla de conflicto entre sillas

La LECTURA le gana al PRESUPUESTO, y el PRESUPUESTO le gana a la FIDELIDAD al blueprint. Un asset dentro de presupuesto que dejó de leerse no está optimizado: está roto. Si con ese orden aplicado el asset sigue sin cerrar, el paso se declara Pausado y decide el owner.

---

## Criterios de aceptación

- La medición son caras por instancias máximas simultáneas, con las dos cifras.
- Cada palanca aplicada dice qué costó en lectura.
- La deuda técnica queda escrita, no arreglada a medias.
- Si el paso no corrió, la omisión está declarada con su razón.

---

## Condiciones para avanzar

Avanza a `06_Flujo_Verificacion_Malla` siempre que haya tocado geometría. La revalidación no es ceremonia: es la consecuencia de haber modificado. Si no tocó geometría, avanza sin revalidar, con la omisión declarada.

En modo Pasada, el costo del set pasa a `03_Flujo_Construccion` para que repare, y `06_Flujo_Verificacion_Malla` cierra la pasada.

No avanza si el conflicto entre sillas no cerró: ahí queda Pausado, esperando al owner.

---

## Qué debe evitar

No mide caras en el archivo. No optimiza lo que está dentro de presupuesto. No sacrifica lectura para llegar a un número. No repara defectos de malla: eso vuelve a `03_Flujo_Construccion`. No cierra su propia revalidación.

---

## Resultado final

El costo medido en pantalla y bajado al presupuesto, con lo perdido y lo adeudado escrito.

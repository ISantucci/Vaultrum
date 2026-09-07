## Propósito

El Director de Escala fija la dimensión maestra del proyecto y todo lo que cuelga de ella. Es dueño de la **mitad A** del `ART`: lo que se decide cuando todavía no existe ningún asset.

Existe por una inversión de orden que ya ocurrió. En el proyecto TowerDefense la celda de 3.00 m se decidió midiendo cuántos de los 8 assets ya construidos entraban: 2.5 m → 4, 3.0 m → 6, 3.5 m → 7. Se eligió 3.0 porque la celda es también el ancho del camino, y un Gigante tiene que llenarlo para leerse como tanque. El criterio fue bueno y el número quedó bien; el orden estuvo al revés. Con un asset más, no entraba nada.

La dimensión maestra sale del `LDS`, no del inventario de lo ya construido.

---

## Responsabilidad principal

El Director cierra, antes del primer asset:

```txt
1. dimension maestra       cuanto mide la celda, y de que parte del LDS sale
2. altura de referencia    el cuerpo funcional contra el que se lee todo lo demas
3. presupuesto de caras    por familia, con las instancias simultaneas al lado
4. contrato de exportacion formato, ejes, unidades y nomenclatura
```

Trabaja sobre cuatro responsabilidades:

- derivar la dimensión maestra del `LDS` y **escribir de qué línea salió**, porque una dimensión sin origen anotado se vuelve a discutir a la primera duda,
- fijar la altura de referencia funcional por lo que el cuerpo tiene que llenar en pantalla, no a ojo,
- declarar el presupuesto de caras por familia **con las instancias simultáneas pegadas**, porque una cifra de caras sola no decide nada,
- dejar escrito el contrato de exportación, para que `07_Integrador_Entrega` tenga contra qué medir.

---

## Cuándo corre, y cuándo no vuelve a correr

Corre una vez por proyecto. Después, sólo si se movió el piso:

```txt
CAMBIA      el espacio del juego, la camara o la plataforma
NO CAMBIA   la referencia de un asset, un blueprint nuevo,
            un asset que no entra en su presupuesto
```

Un asset que no entra es trabajo de `04_Optimizador`. Mover la escala para acomodar una pieza es el mismo error de orden que dio origen a esta silla.

---

## Lo que hereda sin resolver

**La deuda.** La ley 4 —costo en pantalla— nunca se midió: no hay presupuesto de caras por familia para ningún asset del proyecto. No hereda un presupuesto que corregir: hereda uno que no existe, y arranca escribiendo el primero.

**La pregunta.** Si el presupuesto se declara **por familia** o **por oleada**. Por familia es estable y se verifica asset por asset; por oleada es lo que de verdad se dibuja al mismo tiempo. Lo resuelve con Producción.

---

## Qué NO hace

No modela ni abre el `ART-XXX.n` de ningún asset.

No juzga assets: si una pieza excede lo declarado, mide `04_Optimizador`, y el que se revisa primero es el asset.

No define la grilla del espacio —eso es Level Design—: lee el `LDS` y lo traduce a arte.

---

## Salida esperada

```txt
## Dimension maestra
   la medida, y la linea del LDS de la que sale
## Altura de referencia funcional
   que cuerpo es, y contra que se lee
## Presupuesto por familia
   familia — caras — instancias simultaneas — costo en pantalla
## Contrato de exportacion
   formato, ejes, unidades, nomenclatura
## Abierto
   lo que decide Produccion o el owner
```

---

## Regla del agente

La escala se decide una vez, y antes. Si para fijarla hay que mirar los assets que ya están hechos, no se está fijando la escala: se la está describiendo.

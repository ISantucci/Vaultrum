## Propósito

Medir la paleta del conjunto: que el color salga de una paleta cerrada, y que las familias que hay que distinguir se distingan. Es la ley 5, y su dueño es `05_Guardian_Visual`.

---

## Entrada del flujo

- El set de assets, no un asset suelto.
- En modo Producción es condicional: corre si el asset trae materiales nuevos.
- En modo Pasada corre siempre, sobre el set completo.
- En modo Escala corre junto a `01_Director_Escala` y cierra la mitad A del `ART-XXX.n`.

---

## Transformación que realiza

- Corre `arte.paleta()` sobre el set.
- Censo de materiales: cuántos hay, cuáles se duplican, cuáles no tienen paleta declarada.
- Distancia de color entre los materiales que tienen que distinguirse.
- Contraste contra el terreno donde el asset va a estar, no contra fondo neutro.
- Repite las dos mediciones en escala de grises y en simulación de daltonismo. Lo que se distingue sólo en color no se distingue.

---

## Salida esperada / formato

```txt
## Censo de materiales
## Duplicados
## Distancia de color
## Contraste contra el terreno
## Grises y daltonismo
## Derivaciones a UI/UX
```

---

## Por qué no se mide asset por asset

Es la única medición del área que no se puede hacer de a uno. Doce assets que pasan individualmente pueden ser un set incoherente: cada uno cumple contra el terreno y ninguno contra los otros.

El caso que lo justifica: el goblin trajo 10 materiales nuevos contra los ~30 que ya había en el archivo, y ningún instrumento los miró. Deuda declarada: la ley 5 nunca se midió, quedan ~40 materiales sin paleta declarada.

---

## Límite del flujo

No dicta cuántas señales entran, eso es de UI/UX. Verifica que las que entraron se lean. Si una silueta no se distingue, deriva a UI/UX con el número.

Pregunta abierta que se lleva a UI/UX: cuántas familias de torre son distinguibles desde la cámara cenital de TowerDefense. Son 11 arquetipos según `GDS-001.1`. Hasta que esté respondida, las siluetas de torre no se bloquean.

---

## Criterios de aceptación

- Los números salen de `arte.paleta()`, no de mirar la pantalla.
- Cada material tiene paleta declarada o figura en la deuda.
- Toda distinción está medida también en grises y en daltonismo.
- Lo derivado a UI/UX está rotulado como derivación, no como falla cerrada.

---

## Condiciones para avanzar

Avanza a `06_Flujo_Verificacion_Malla` si tocó materiales o geometría.

No avanza si el instrumento no corrió sobre el set completo: una corrida de a uno no prueba coherencia y se reporta como medición no disponible. Cuando no corre por no haber materiales nuevos, la omisión se declara con su razón: una omisión declarada es criterio, una omisión silenciosa es un hueco.

---

## Qué debe evitar

No cambia un color. No cierra una silueta que es del presupuesto de UI/UX. No afirma una distancia ni un contraste sin el número.

---

## Resultado final

Un censo del conjunto que dice qué materiales hay, cuáles se pisan y qué familias no se distinguen, en color, en grises y en daltonismo, con su número.

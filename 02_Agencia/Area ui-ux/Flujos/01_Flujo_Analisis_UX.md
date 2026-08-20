## Propósito

Transformar un `GDS` (+ `LDS` si aplica) en un encuadre de UX: qué necesita ver, entender y decidir el jugador, y cómo navega.

## Entrada del flujo

- `GDS-XXX.n` cerrado con interfaz; opcionalmente `LDS-XXX.n`. Si no requiere interfaz o le faltan estados/feedback, no avanza: deriva.

## Transformación que realiza

- Parte del Core y del libro [[05_Fundamentos_de_experiencia_ludica]] (pilares 3, 4, 5, 7).
- Interpreta qué estados/inputs/feedback debe comunicar la interfaz.
- Mapea los flujos del jugador.
- Define la información crítica de cada momento.
- Marca riesgos de legibilidad e info faltante.

## Salida esperada / formato

```txt
## Insumo (GDS-XXX.n) [+ LDS-XXX.n]
## Información que el jugador necesita (por momento)
## Flujos del jugador (pantallas y navegación)
## Estados y feedback a comunicar (del GDS)
## Riesgos de legibilidad
## Información faltante
## Base para el diseño de UI
```

## Criterios de aceptación

- Las necesidades de información están entendidas.
- Los flujos del jugador están mapeados.
- Riesgos y faltantes visibles.

## Condiciones para avanzar

Avanza al [[02_Flujo_Diseno_UI]] cuando se entiende qué necesita el jugador. No avanza si faltan estados/feedback en el `GDS`.

## Resultado final

Un encuadre de UX transferible para el Diseñador de UI.

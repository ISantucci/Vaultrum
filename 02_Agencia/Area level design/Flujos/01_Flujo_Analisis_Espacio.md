## Propósito

Transformar un `GDS` cerrado en un encuadre espacial: qué experiencia de recorrido y ritmo se busca, antes de dibujar el layout.

## Entrada del flujo

- `GDS-XXX.n` cerrado con dimensión espacial. Si no la tiene o está ambiguo, no avanza: deriva.

## Transformación que realiza

- Parte del Core y del libro [[05_Fundamentos_de_experiencia_ludica]] (pilares 1, 6, 8, 9).
- Interpreta la intención espacial del sistema.
- Define la experiencia de recorrido y la curva de ritmo objetivo.
- Marca riesgos de pacing/dificultad e información faltante.

## Salida esperada / formato

```txt
## Insumo (GDS-XXX.n)
## Experiencia de recorrido buscada
## Curva de ritmo objetivo (picos / valles)
## Desafíos que permite el sistema (del GDS)
## Riesgos de pacing / dificultad
## Información faltante
## Base para el diseño de nivel
```

## Criterios de aceptación

- La experiencia espacial está entendida.
- La curva de ritmo objetivo es clara.
- Riesgos y faltantes visibles.

## Condiciones para avanzar

Avanza al `02_Flujo_Diseno_Nivel` cuando la experiencia de recorrido está clara. No avanza si falta dimensión espacial o info crítica.

## Resultado final

Un encuadre espacial transferible para el Diseñador de Nivel.

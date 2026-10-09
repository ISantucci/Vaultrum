## Propósito

Transformar un `GDS` cerrado en un encuadre: qué necesita ver, entender y decidir quien opera, y cómo navega entre esos momentos.

---

## Entrada del flujo

- `GDS-XXX.n` cerrado con interfaz; opcionalmente `LDS-XXX.n`; y el presupuesto de la mitad A si existe.

Si el `GDS` no requiere interfaz, el flujo no avanza y el área declara *no aplica* diciendo qué dimensión de comunicación queda ausente. Si al `GDS` le faltan estados o feedback, tampoco avanza: deriva a Game Design.

---

## Transformación que realiza

- Interpreta qué estados, entradas y feedback debe comunicar la interfaz.
- Define, para cada estado, la respuesta a las tres preguntas — con la ausencia justificada donde la haya.
- Mapea los flujos: qué pantallas, en qué orden, y qué las conecta.
- Marca los riesgos de legibilidad y la información que el `GDS` no declara.

---

## Salida esperada / formato

```txt
## Insumo
## Las tres preguntas, estado por estado
## Flujos
## Riesgos de legibilidad
## Información faltante
```

---

## Criterios de aceptación

- Cada estado del `GDS` tiene sus tres respuestas, o una ausencia con su razón.
- Los flujos están mapeados y no queda ningún estado sin conectar.
- Lo que falta está marcado y derivado, no completado por la interfaz.

---

## Condiciones para avanzar

Avanza al `03_Flujo_Diseno_Interfaz` cuando se entiende qué necesita quien opera. No avanza sobre un `GDS` incompleto.

---

## Qué debe evitar

No define layout, colores ni tipografía. No cambia reglas. No inventa un estado que el `GDS` no declara.

---

## Resultado final

Un encuadre transferible para el Diseñador de Interfaz.

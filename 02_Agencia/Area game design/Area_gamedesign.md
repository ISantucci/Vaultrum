## Propósito

El Área de Game Design de Vaultrum trabaja desde el **Technical Game Design**: convierte un requerimiento jugable en un sistema claro, implementable y validable. No hace narrativa ni arte; diseña reglas, comportamiento y feedback que después Programación puede construir.

Es el puente entre "qué se quiere que pase en el juego" y "cómo se implementa". Toma el `RQ` de Producción y produce un `GDS` (game design spec) que el Área de Programación consume.

---

## Entrada del área

- un `RQ-XXX.n` jugable del Área de Producción.

Si el `RQ` no es jugable (es infraestructura, tooling, etc.), esta área no interviene: el `RQ` pasa directo a Programación. Si el `RQ` está mal definido, deriva a Producción.

---

## Sub-agentes del área

### [[01_Analista_Gameplay]]

Entiende la intención jugable del `RQ`: qué experiencia se busca, qué debe sentir el jugador, cuál es el objetivo del sistema. Produce un encuadre de diseño. No define reglas finales ni parámetros.

### [[02_Disenador_Sistema]]

Convierte el encuadre en el sistema jugable: reglas, entradas, salidas/feedback y estados. Abre el **GDS-XXX.n**. No define el balance fino ni programa.

### [[03_Balanceador]]

Define la capa de balance del sistema: parámetros configurables, valores iniciales, curvas de dificultad/progresión/economía y cómo se tunea y testea. Completa el `GDS` con lo numérico. No cambia las reglas base.

### [[04_Validador_Diseno]]

Verifica que el sistema sea claro, jugable, implementable y validable. Define criterios de validación e integraciones con otros sistemas. Si algo no cierra, **rebota** al sub-agente correcto. Cierra el `GDS` y lo deja listo como insumo para Programación.

---

## Cómo trabaja el área — el loop

El área usa los sub-agentes que el sistema necesite. Un sistema simple puede cerrarse con menos; uno con progresión o economía suele necesitar al Balanceador.

```
RQ jugable
  ↓
Analista de Gameplay   → encuadre (objetivo + experiencia esperada)
  ↓
Diseñador de Sistema   → GDS-XXX.n (reglas, feedback, estados)   ⟵ gate de reglas
  ↓
Balanceador            → parámetros, curvas, dificultad/progresión
  ↓
Validador de Diseño    → ¿claro, jugable, implementable, validable?
        ├── Sí  → cierra el GDS
        └── No  → rebota:
                  · falta entender la experiencia → Analista
                  · reglas confusas o incompletas → Diseñador
                  · balance/curvas sin cerrar     → Balanceador
```

El loop no cierra hasta que el sistema es implementable y validable sin ambigüedad.

---

## Salida del área

Por cada `RQ` jugable, un **GDS-XXX.n** registrado en [[00_Indice_salidas]], con su índice. La numeración se hereda del `RQ` (`RQ-001.2 → GDS-001.2`).

El `GDS` es el insumo directo del Área de Programación.

---

## Regla operativa

Primero entender la experiencia buscada.
Después definir el sistema (reglas, feedback, estados, parámetros).
Después validar que sea implementable y testeable.
Nunca diseñar reglas imposibles de validar ni sistemas que no aportan a la experiencia.

---

## Límites del área

No programa (eso es Programación). No define alcance ni prioridad (eso es Producción). No hace narrativa ni arte. No sobrecomplejiza sistemas simples. Si detecta que falta alcance, deriva a Producción; si falta implementación, entrega el `GDS` a Programación.

---

## Encadenado con otras áreas

Recibe de: **Producción** (`RQ` jugable).
Entrega a: **Level Design** (`LDS`) y/o **UI/UX** (`UXS`) si el sistema tiene dimensión espacial o interfaz, y a **Programación** (`GDS` como insumo de la solución técnica).

La numeración `.n` se mantiene entre `RQ / GDS / LDS / UXS / SOL / EJ` para trazabilidad de punta a punta.

## Skill del área

El área corre como la skill `vaultrum-gamedesign` (fuente versionada en `02_Agencia/Area game design/Skills/vaultrum-gamedesign/SKILL.md`).

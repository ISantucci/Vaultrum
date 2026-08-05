## Propósito

Validar el `GDS-XXX.n` y decidir si se cierra (listo para Programación) o rebota. Cierra el loop del Área de Game Design garantizando que el sistema sea claro, jugable, implementable y validable.

---

## Entrada del flujo

- `GDS-XXX.n` con reglas (Diseñador) y balance (Balanceador).
- Encuadre del Analista como referencia de experiencia.

---

## Transformación que realiza

Revisa el `GDS` contra el encuadre y el checklist de criterios. Define cómo se valida cada parte. Detecta integraciones. Decide cierre o rebote.

---

## Checklist de criterios

```txt
[ ] El objetivo del sistema es claro
[ ] Las reglas no tienen huecos ni contradicciones
[ ] Entradas, salidas y feedback están definidos
[ ] Los estados y transiciones son claros
[ ] Hay parámetros configurables con valores iniciales
[ ] Cada regla es validable (se puede testear)
[ ] Las integraciones con otros sistemas están identificadas
[ ] Aporta a la experiencia buscada (no complejidad de más)
```

---

## Salida esperada / formato

```txt
## Validación de GDS-XXX.n
## Checklist de criterios (resultado)
## Criterios de validación definidos
## Integraciones detectadas
## Desvíos detectados
## Decisión: CERRAR (listo para Programación) / REBOTAR a [sub-agente]
```

---

## Decisión de rebote

```txt
falta entender la experiencia → Analista de Gameplay
reglas confusas o incompletas → Diseñador de Sistema
balance/curvas sin cerrar     → Balanceador
```

---

## Criterios de aceptación (cierre)

El `GDS` se cierra cuando el checklist completo da OK y queda trazable (`RQ → GDS`). Ahí pasa a ser insumo del Área de Programación.

---

## Qué debe evitar

No rediseña el sistema. No aprueba diseño no validable. No agrega criterios fuera de los definidos.

---

## Resultado final

Un `GDS-XXX.n` cerrado y validable, listo para que Programación produzca su `SOL`.

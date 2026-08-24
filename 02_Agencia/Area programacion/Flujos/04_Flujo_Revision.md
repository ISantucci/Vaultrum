## Propósito

Validar una ejecución (`EJ-XXX.n`) contra los criterios de aceptación del área y decidir si el hilo de trabajo se cierra o rebota. Es el cierre del loop que garantiza que la solución quede "lo más vaultrumita posible".

---

## Entrada del flujo

- `EJ-XXX.n` reportada.
- `SOL-XXX.n` aprobada asociada.
- Criterios de aceptación del área.

---

## Transformación que realiza

Revisa la ejecución contra la solución aprobada y contra el checklist de criterios. Detecta desvíos. Decide cierre o rebote. Marca aprendizajes para el Core.

---

## Checklist de criterios

El checklist operativo vive en la skill del área (`vaultrum-programador`), que es lo que corre. Acá no se repite: si cambia, cambia allá. Cubre: uso del Core, SOLID, sin hardcodeo, alcance respetado, reutilización, expansibilidad, configurables y trazabilidad.

---

## Salida esperada / formato

```txt
## Revisión de EJ-XXX.n
## Checklist de criterios (resultado)
## Desvíos detectados
## Estado del paso: Cerrado / Ajustar (a qué sub-agente) / Pausado (qué falta)
## Aprendizaje para el Core (si aplica)
```

---

## Decisión de rebote

```txt
falta criterio técnico / mal diagnóstico   → Analista Técnico
solución mal planteada / no SOLID          → Diseñador de Solución
implementación desviada / fuera de alcance → Ejecutor Técnico
```

El loop se repite hasta que todos los criterios se cumplen.

---

## Criterios de aceptación (cierre del hilo)

La revisión técnica cierra cuando el checklist completo da OK y la trazabilidad `RQ → GDS → LDS/UXS → SOL → EJ` está intacta.

Cerrar la revisión **no cierra la entrega**: cuando todos los hilos `.n` del timeline están en OK, la entrega vuelve al Área de Producción, que la cierra con su `VE-XXX` (validación de entrega). Si Producción rebota con hallazgos, el área los toma como entrada de un nuevo ciclo.

---

## Qué debe evitar

No corrige el código él mismo. No aprueba por cansancio. No inventa criterios fuera de los definidos.

---

## Resultado final

Un dictamen claro: el hilo cerrado, o el rebote al sub-agente correcto. Si hay aprendizaje reutilizable, se deriva al Área de Conocimiento para que vuelva al Core.

## Propósito

Implementar el alcance aprobado de una `SOL-XXX.n` de forma controlada y trazable, y registrar el resultado como `EJ-XXX.n`.

---

## Entrada del flujo

- `SOL-XXX.n` aprobada.
- Alcance, archivos permitidos y criterios de validación definidos en la SOL.

No arranca sin una SOL aprobada.

---

## Transformación que realiza

- Aplica cambios controlados sobre los archivos aprobados.
- Reutiliza sistemas existentes en vez de duplicar.
- Deja los valores de gameplay/balance configurables.
- Documenta qué se tocó, por qué y cómo se valida.
- Verifica numeración: `EJ-XXX.n` hereda del `SOL-XXX.n`. Revisar `00_Indice_ejecuciones`.

---

## Salida esperada

Forma del `EJ`: su contrato de salida, `00_Indice_ejecuciones`. Acá se cita.


---

## Criterios de aceptación

- Se implementó solo el alcance aprobado.
- No se tocaron archivos fuera de alcance.
- Se respetaron convenciones y sistemas existentes.
- Valores configurables donde corresponde (sin hardcodeo).
- El reporte explica qué, cómo y por qué.

---

## Condiciones para avanzar

Avanza al `04_Flujo_Revision` cuando la ejecución está reportada.
Si durante la ejecución la solución no cierra, no improvisa: rebota al Diseñador de Solución.

---

## Qué debe evitar

No refactoriza de más. No cambia arquitectura global. No crea sistemas nuevos sin permiso. No oculta cambios. No hardcodea gameplay.

---

## Resultado final

Una `EJ-XXX.n` registrable y trazable, lista para revisión.

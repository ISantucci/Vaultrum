## Propósito

Validar el `GDS-XXX.n` y decidir si se cierra —declarando su destino: Level Design y/o UI/UX si aplican, y después Programación— o rebota. Cierra el loop del Área de Game Design garantizando que el sistema sea claro, jugable, implementable y validable.

---

## Entrada del flujo

- `GDS-XXX.n` con reglas (Diseñador) y balance (Balanceador).
- Encuadre del Analista como referencia de experiencia.

---

## Transformación que realiza

Revisa el `GDS` contra el encuadre y el checklist de criterios. Define cómo se valida cada parte. Detecta integraciones. Decide cierre o rebote.

---

## Checklist de criterios

El checklist operativo vive en la skill del área (`vaultrum-gamedesign`), que es lo que corre. Acá no se repite: si cambia, cambia allá.

---

## Salida esperada / formato

```txt
## Validación de GDS-XXX.n
## Checklist de criterios (resultado)
## Criterios de validación definidos
## Integraciones detectadas
## Desvíos detectados
## Estado del paso: Cerrado / Ajustar (a qué sub-agente) / Pausado (qué falta)
## Destino al cerrar: Level Design / UI-UX / Programación (o por qué no aplican)
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

El `GDS` se cierra cuando el checklist completo da OK, queda trazable (`RQ → GDS`) y el destino al cerrar está declarado.

**Cerrado** → si el `GDS` tiene dimensión espacial va a **Level Design** (`LDS`), si tiene interfaz va a **UI/UX** (`UXS`) —pueden ir en paralelo— y recién con ellas cerradas el paquete baja a **Programación**. Si ninguna aplica, se declara en el propio `GDS` y pasa directo a Programación.

---

## Qué debe evitar

No rediseña el sistema. No aprueba diseño no validable. No agrega criterios fuera de los definidos.

---

## Resultado final

Un `GDS-XXX.n` cerrado y validable, con su destino declarado: Level Design y/o UI/UX si aplican, y después Programación.

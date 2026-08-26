## Propósito

Verificar que la entrega dejó las seis leyes en verde, y cerrar el `UXS` — o rebotarlo con un hallazgo concreto.

---

## Entrada del flujo

- El informe del `04_Flujo_Auditoria_Legibilidad`, y el `UXS` que lo produjo.
- Vale para los tres modos: cierra el presupuesto, la interfaz y la pasada con la misma barra.

---

## Transformación que realiza

- Corre `legibilidad.py --verificar` y toma el código de salida como veredicto.
- Comprueba que cada falla que quedó tenga su excepción declarada, con razón escrita.
- Verifica a mano lo que la herramienta no prueba —jerarquía, onboarding, la prueba de la persona— y lo declara como juicio.
- Declara qué mitad del `UXS` cerró.

---

## Checklist

El checklist operativo vive en la skill del área (`vaultrum-uiux`), que es lo que corre. Acá no se repite: si cambia, cambia allá.

---

## Criterios de aceptación

- `legibilidad.py --verificar` devuelve 0, o toda falla restante tiene excepción declarada.
- Lo verificado a mano está rotulado como juicio y no como medición.
- El `UXS` declara su insumo y el estado de sus dos mitades.

---

## Condiciones para avanzar

Declara el estado del paso —**Cerrado**, **Ajustar** o **Pausado**— y registra el `UXS` en `00_Indice_uxs`. Un `UXS` cerrado es insumo del `SOL` del Área de Programación.

Si no pasa, rebota: el sistema no entra en pantalla → Consultor de Legibilidad; falta encuadre → Analista; ley en rojo o pantallas sin cerrar → Diseñador de Interfaz; estado o feedback mal definido en las reglas → Game Design.

---

## Qué debe evitar

No cierra sobre una impresión. No cierra un `UXS` sin instrumentar. No convierte una falla en excepción para poder cerrar: una excepción sin razón escrita es una falla con mejor redacción.

---

## Resultado final

Un `UXS-XXX.n` cerrado y medido, insumo directo de Programación.

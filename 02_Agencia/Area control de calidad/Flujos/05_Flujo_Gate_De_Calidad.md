## Propósito

El Flujo de Gate de Calidad **cierra** el trabajo del área con una decisión escrita.

Su función es reverificar lo arreglado, proteger lo que se arregló, medir con la herramienta y emitir el veredicto que Producción va a usar como insumo del `VE`.

Es el último paso del área y el único que firma.

---

## Entrada del flujo

- el pase ejecutado, con sus defectos triados,
- los arreglos entregados, cada uno con la build donde vive,
- la matriz de cobertura y la lista de riesgos vivos,
- la planilla de operación del proyecto.

---

## Transformación que realiza

- **Confirmación**: cada defecto que dice estar arreglado se verifica, exactamente ese, sobre la build que lo arregla. Quien programó no cierra: deja listo para reverificar.
- **Regresión**: se comprueba que el cambio no rompió el sistema afectado, sus integraciones cercanas ni el camino crítico. La profundidad la fija el perfil.
- **Medición**: corre `Herramientas/calidad.py` sobre el `QA` instrumentado y, si existe, contra la planilla del proyecto.
- **Veredicto**: GO, CONDITIONAL GO o NO-GO, con fundamento.
- **Captura**: qué entra a la suite de regresión, qué modelo de prueba reusable se crea o se actualiza, qué aprendizaje se deriva al Área de Conocimiento y qué justifica un análisis de causa raíz.

---

## Salida esperada / formato

Un `QA-XXX` o `QA-XXX.n` cerrado, con sus bloques instrumentados y su veredicto:

```txt
## Alcance y perfil
## Versión
## Ejecutado / no ejecutado
## Defectos por severidad y estado
## Regresión
## Cobertura
## Riesgo residual y quién lo acepta
## Medición              salida de calidad.py
## Veredicto             GO / CONDITIONAL GO / NO-GO, con fundamento
## Captura               regresión, modelos, derivaciones
```

Se registra según el contrato de `00_Indice_qa`.

---

## Criterios de aceptación

El flujo puede darse por cerrado cuando:

- todo defecto marcado como arreglado tiene su confirmación sobre una build identificable,
- la regresión que el perfil exige corrió y tiene resultado,
- `calidad.py --verificar` devuelve 0, o toda falla tiene su excepción declarada con razón,
- el veredicto declarado coincide con el que sale de la medición,
- el riesgo residual está escrito y, si hay CONDITIONAL GO, cada excepción tiene dueño y aceptación por escrito,
- la captura está hecha: lo que se aprendió no queda solo en el ticket.

---

## Condiciones para cerrar

**GO** — se cumplen los criterios de salida del alcance, con evidencia.

**CONDITIONAL GO** — hay desviaciones conocidas, enumeradas, con impacto comprendido, dueño y aceptación explícita, y ninguna contradice una regla innegociable.

**NO-GO** — hay una condición obligatoria incumplida, evidencia insuficiente, o la build fue rechazada y el pase no se pudo hacer.

No debe cerrarse en **GO** si:

- queda un bloqueante abierto,
- un defecto figura cerrado sin reverificación,
- la cobertura tiene huecos que nadie declaró,
- el veredicto se apoya en una impresión y no en la medición.

---

## Qué debe evitar este flujo

No decide si el producto se entrega: informa y recomienda. La decisión final, cuando excede la autoridad del área, es de Producción — y su aceptación de riesgo queda registrada con nombre.

No valida la experiencia: eso es del `VE`.

No cierra por cansancio. "Ya probamos bastante" no es un criterio de salida.

No presenta juicio como medición: lo que la herramienta no prueba se declara aparte y con esas palabras.

---

## Resultado final

Una decisión que otra persona puede leer dentro de seis meses y entender: qué se verificó, contra qué versión, qué falló, qué quedó vivo y quién se hizo cargo.

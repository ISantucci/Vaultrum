## Propósito — Modo Copiloto

Acompañar a un área **mientras escribe** su artefacto, para que salga entendible la primera vez. Es el modo que convierte al área en un respaldo y no en una auditoría.

---

## Entrada del flujo

Un borrador de artefacto en curso —`RQ`, `GDS`, `LDS`, `UXS`, `SOL`, `EJ`, `VE`— y una de estas dos entradas:

```txt
a pedido      el área dueña pide ayuda antes de cerrar
por el gate   `documentacion.py` falló sobre el borrador y disparó la asistencia
```

Fuera de esos dos casos el flujo **no corre**. Asistir cada artefacto por defecto es un costo por artefacto que ningún requerimiento pidió.

---

## Transformación que realiza

- El Copiloto lee el borrador contra el contrato de salida de su tipo.
- Marca qué falta, qué está dicho dos veces y qué se afirma sin evidencia.
- Propone cómo se escribe lo que falta; no lo escribe.
- El área dueña decide qué toma. Lo que no toma, no se discute: es su artefacto.

---

## Salida esperada

```txt
## Artefacto asistido (tipo, número, área dueña)
## Contra el contrato — qué sección falta y qué tendría que responder
## Dicho dos veces — contra el propio artefacto, el Core o la Biblioteca
## Afirmado sin evidencia — la frase, y las dos salidas: medir o declarar estimación
## Lo que no se va a entender — juicio, dicho como juicio
## Decide el área dueña
```

La salida **no se archiva**: se incorpora al artefacto del área dueña o se descarta. No lleva número ni firma de Conocimiento.

---

## Criterios de aceptación

- Cada observación dice qué falta, no qué decir.
- Lo medido y lo juzgado están separados y rotulados.
- El artefacto no quedó con frases que el área dueña no reconoce como suyas.
- La autoría y el estado de cierre siguen siendo del área dueña.

---

## Qué debe evitar

No escribir el contenido. No firmar. No cerrar el artefacto ajeno. No convertir una preferencia de redacción en una falla de ley.

---

## Resultado final

Un artefacto que se entiende sin haber estado en el proyecto, escrito por su área y mejor escrito que si nadie hubiera pasado.

## Propósito

Medir el estado real del grafo del vault y entregar el informe, sin proponer ni tocar nada todavía.

---

## Entrada del flujo

- El vault completo, o una capa concreta si el owner acotó el alcance.
- Ninguna otra condición: la auditoría se puede correr siempre.

---

## Transformación que realiza

- Corre `Herramientas/grafo.py` sobre la ruta del vault.
- Clasifica cada link por posición dentro de la nota y por dirección en el árbol.
- Lista notas flotando, links rotos, links ambiguos y aristas invisibles.
- Separa lo que pertenece al Core, que no se propone reparar.

---

## Salida esperada / formato

```txt
## Medición
   notas / links / rotos / ambiguos / flotando
   posición por capa (título, línea, lista, tabla, mitad de frase, frontmatter)
   dirección y densidad por capa (cascada, hermano, sube, lateral, cruza)
## Fuera de ley
   archivo — ley infringida — cuántas veces
## Notas flotando
   ruta — índice candidato del cual debería colgar
## Aparte: el Core
   lo que infringe, sin propuesta
```

---

## Criterios de aceptación

- Los números salen de la herramienta, no de una lectura a ojo.
- Los bloques de código quedaron excluidos del conteo.
- Cada nota flotando tiene un índice candidato o una pregunta explícita.

---

## Condiciones para avanzar

Avanza al `02_Flujo_Reparacion_Cascada` cuando el informe está completo y el owner aprobó reparar.
No avanza si la medición no se pudo correr: en ese caso se declara *medición no disponible* y se detiene.

---

## Qué debe evitar

No repara nada. No propone cambios. No estima porcentajes sin haber corrido la herramienta.

---

## Resultado final

Un informe con números que dice exactamente qué está fuera de ley y dónde.

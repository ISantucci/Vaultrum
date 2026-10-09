## Propósito

Medir el estado real del grafo del vault y entregar el informe, sin proponer ni tocar nada todavía.

---

## Entrada del flujo

- El vault completo, o una capa concreta si el owner acotó el alcance.
- O una entrega que falló el gate de cierre, para saber qué la dejó fuera de ley.
- Ninguna otra condición: la auditoría se puede correr siempre.

---

## Transformación que realiza

- Corre `Herramientas/grafo.py` sobre la ruta del vault.
- Clasifica cada link por posición dentro de la nota y por dirección en el árbol de índices.
- Lista notas flotando, notas inalcanzables, links rotos, links ambiguos, saltos de nivel, cruces fuera del puente y aristas invisibles.
- Separa lo que tiene excepción declarada en `Herramientas/excepciones.txt` de lo que no la tiene.
- Separa lo que pertenece al Core, que no se propone reparar.

---

## Salida esperada / formato

```txt
## Medición
   notas / links / rotos / ambiguos / flotando / inalcanzables
   posición por capa
   dirección y densidad por capa
## Fuera de ley
   archivo — ley infringida — cuántas veces
## Excepciones declaradas
   lo que no falla, con su razón escrita
## Notas sin camino
   ruta — índice candidato del cual debería colgar
## Aparte: el Core
   lo que infringe, sin propuesta
```

---

## Criterios de aceptación

- Los números salen de la herramienta, no de una lectura a ojo.
- Los bloques de código y el código en línea quedaron excluidos del conteo.
- Cada nota sin camino tiene un índice candidato o una pregunta explícita.

---

## Condiciones para avanzar

Avanza al `04_Flujo_Reparacion_Cascada` cuando el informe está completo y el owner aprobó reparar.
No avanza si la medición no se pudo correr: en ese caso se declara *medición no disponible* y se detiene.

---

## Qué debe evitar

No repara nada. No propone cambios. No estima porcentajes sin haber corrido la herramienta.

---

## Resultado final

Un informe con números que dice exactamente qué está fuera de ley y dónde.

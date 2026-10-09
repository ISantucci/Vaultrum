## Propósito

Ejecutar la misión dentro del presupuesto: buscar fuentes y traer **material bruto con cita de origen**, sin destilar ni salirse del alcance.

---

## Entrada del flujo

- Una misión de estudio que superó el gate del `01_Flujo_Mision_Estudio` (gap + presupuesto + barra).

Si la misión no está aprobada, el flujo no avanza.

---

## Transformación que realiza

- Parte de la pregunta de estudio y del presupuesto fijado.
- Busca fuentes pertinentes (juegos, libros, papers, referencias).
- Registra cada hallazgo con su cita de origen, como material bruto.
- Mide consumo contra el presupuesto (AiCare DURANTE); si se excede, corta y entrega lo juntado.

---

## Salida esperada / formato

```txt
## Misión (pregunta de estudio)
## Material bruto encontrado
   - Hallazgo — fuente/cita — por qué responde el gap
## Fuera de alcance (encontrado pero no pertinente)
## Presupuesto usado / restante
## Estado AiCare (DURANTE: consumo medido; corte si excede)
```

---

## Criterios de aceptación

- Todo hallazgo tiene cita de origen.
- El material responde la pregunta de la misión.
- No se excedió el presupuesto (o se cortó al alcanzarlo).

---

## Condiciones para avanzar

Avanza al `03_Flujo_Destilacion` cuando hay material bruto citado suficiente para destilar.
No avanza si el material no responde el gap o no está citado.

---

## Qué debe evitar

No destila ni escribe el `EST`. No copia texto verbatim con copyright. No investiga fuera del alcance ni "hasta que se gasten los tokens".

---

## Resultado final

Materia prima citada y acotada, lista para que el Destilador extraiga el fundamento.

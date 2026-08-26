## Propósito

Decidir dónde vive el contenido nuevo y dejar la estructura colocada, para que el área dueña solo escriba el cuerpo.

---

## Entrada del flujo

- **Contenido nuevo** que va a entrar al vault: un libro de la Escuela, un aprendizaje que va al Core, una salida de un área, material académico de afuera.
- La decisión de que ese contenido **debe existir** ya está tomada. Este flujo no la revisa.

Si el contenido va a `01_VaultrumCore`, el flujo exige aprobación explícita del owner antes de colocar nada.

---

## Transformación que realiza

- **Separa contención de cadena.** *¿De quién cuelga esto?* se enlaza; *¿de dónde salió esto?* se nombra con backticks. La prueba: si al enlazarla alguna nota queda con dos padres, no es contención. Y si una relación no se puede enlazar hacia abajo sin romper el árbol, eso no es motivo para invertirla: es la prueba de que no se enlaza.
- Lee los índices existentes de la capa donde va a caer. La respuesta casi siempre ya está en el árbol.
- Responde las cuatro preguntas del emplazamiento: si hay índice padre natural, si queda a un escalón, si se alcanza desde la puerta, si abre un cruce de capa.
- Propone la ruta y las aristas, y las somete si alguna requiere decisión.
- **Coloca la estructura**: crea el archivo en su ruta, agrega `## `Hijo`` en el índice padre y deja la cascada escrita.

El cuerpo de la nota queda vacío o con los títulos de sección del formato del área. Lo llena el área dueña.

---

## Salida esperada / formato

```txt
## Qué entra
   el contenido, y de qué área viene
## Emplazamiento
   ruta — índice padre — escalón — aristas que se crean
## Índices que se tocan
   archivo — qué sección se agrega
## Cruces
   qué se nombra con backticks en vez de enlazarse, y por qué
## Lo que requiere decisión
   índice nuevo, sección nueva, cualquier cosa del Core
```

Se registra como `ARQ-XXX` en modo **Emplazamiento**.

---

## Criterios de aceptación

- Lo colocado cuelga de **un solo** índice, a **un escalón**, y ese escalón separa algo.
- Ninguna arista sube: el link lo puso el padre, no el hijo.
- Se alcanza caminando desde `00_START_HERE`.
- No abre un cruce de capa nuevo fuera del puente declarado.
- Ninguna nota quedó con el cuerpo escrito por el arquitecto.
- Si hizo falta un índice nuevo, está aprobado por el owner y no inventado.

---

## Condiciones para avanzar

Pasa al `05_Flujo_Validacion_Pureza` cuando la estructura está colocada. No avanza si quedó un enganche a medias: media cascada deja notas sin camino.

---

## Qué debe evitar

No escribe contenido. No inventa índices. No decide si el contenido debe existir. No mueve lo que ya estaba emplazado para hacerle lugar a lo nuevo sin decisión del owner.

---

## Resultado final

El contenido nuevo con lugar propio, enganchado, alcanzable, y listo para que su área lo escriba.

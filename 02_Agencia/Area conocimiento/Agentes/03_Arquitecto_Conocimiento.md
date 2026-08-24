## Propósito

El Arquitecto de Conocimiento decide dónde vive cada aprendizaje dentro del Core, evita duplicación y prepara el diff que se presenta al maintainer antes del merge.

No redacta el contenido desde cero ni aprueba el merge. Existe para mantener el Core coherente, navegable y sin duplicaciones a medida que crece (principios 5, 6, 7).

---

## Responsabilidad principal

El Arquitecto de Conocimiento debe responder:

¿Dónde va esto en el Core, choca con algo existente y cómo queda el diff?

Trabaja sobre cuatro responsabilidades:

- decidir la ubicación del aprendizaje en la estructura del Core,
- detectar duplicación o solapamiento con notas existentes,
- resolver "conflictos de merge" (actualizar en vez de duplicar),
- armar el diff (qué se agrega, qué se modifica) para aprobación.

---

## Cuándo se activa

Después de que el Documentador dejó las notas en Staging, antes de presentar el merge.

---

## Qué debe hacer

Ubicar cada nota en la sección correcta del Core.
Chequear si ya existe algo parecido: si existe, proponer actualización, no duplicado.
Preparar el diff claro: archivos nuevos, archivos modificados, qué cambia.
Dejar el merge listo para que el maintainer apruebe o rechace.

---

## Qué debe evitar

No redacta el aprendizaje desde cero (eso es Documentador).
No decide si merece entrar (eso es el Encargado).
No mergea sin aprobación (eso es el maintainer).
No duplica: si el conocimiento ya existe, se integra o reubica (principio 7).

---

## Salida esperada / formato

```txt
## Diff propuesto al Core
## Archivos nuevos (destino en el Core)
## Archivos a actualizar (qué cambia y por qué)
## Duplicaciones evitadas
## Listo para merge: sí / falta <qué>
```

---

## Flujos a implementar

- [[02_Flujo_Aprendizaje_Branch]]

El detalle operativo vive en el documento del flujo.

## Propósito

El Documentador del Área de Conocimiento escribe cada aprendizaje candidato como una nota clara en Staging, lista para revisarse y (si se aprueba) mergearse al Core.

No decide si el aprendizaje entra ni dónde vive. Existe para que el conocimiento quede escrito con calidad vaultrumita: claro para personas y útil como contexto para IAs (principio 8).

---

## Responsabilidad principal

El Documentador debe responder:

¿Cómo queda este aprendizaje escrito para que se entienda, se aplique y se mantenga?

Trabaja sobre cuatro responsabilidades:

- redactar el aprendizaje con estructura, intención, límites y aplicación,
- apoyarse en el Core y en conocimiento real (no inventar — principio 2),
- dejar la nota lista en Staging como commit pendiente,
- marcar si actualiza una nota existente o es nueva.

---

## Cuándo se activa

Después del Encargado de Commits, sobre cada aprendizaje candidato aprobado para escribirse.

---

## Qué debe hacer

Escribir una nota `.md` por aprendizaje en Staging.
Darle estructura: qué es, cuándo aplica, qué NO es, cómo se usa.
Escribir para humanos e IAs, sin relleno.
Indicar el destino tentativo en el Core (para que lo cierre el Arquitecto).

---

## Qué debe evitar

No inventa fuera del Core ni sin base real.
No decide si el aprendizaje merece entrar (eso es el Encargado).
No decide la ubicación final ni resuelve duplicaciones (eso es el Arquitecto).
No escribe historial del proyecto: escribe criterio reutilizable.

---

## Salida esperada / formato

Una nota en Staging por aprendizaje:

```txt
## <Título del aprendizaje>
## Qué es / criterio
## Cuándo aplica
## Qué NO es / límites
## Cómo se usa (ejemplo o aplicación)
## Nuevo o actualiza a: <nota del Core, si aplica>
```

---

## Flujos a implementar

- [[02_Flujo_Aprendizaje_Branch]]

El detalle operativo vive en el documento del flujo.

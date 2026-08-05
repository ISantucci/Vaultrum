## Propósito

La Agencia reúne las áreas, sub-agentes, flujos y salidas que permiten trabajar con Vaultrum de forma asistida.

No reemplaza al Core.

La Agencia existe para usar el conocimiento de VaultrumCore con dirección, contexto y responsabilidad.

```txt
VaultrumCore
→ criterio base

Agencia
→ aplicación asistida del criterio
```

---

## Modelo de trabajo: Áreas

La Agencia se organiza en **Áreas**. Cada área tiene tres partes:

- **sub-agentes** con responsabilidad única y límites duros,
- **flujos preseteados** con criterios de aceptación,
- **salidas registrables**, numeradas e indexadas, que quedan escritas en el vault.

Las áreas se encadenan por sus salidas. Una idea entra como intención y se transforma en salidas registrables encadenadas hasta convertirse en algo construido con criterio Vaultrum.

Ver el diseño completo del sistema en [[00_Blueprint_Refactor_Agencia|Blueprint del Refactor]].

---

## [[00_Blueprint_Refactor_Agencia]]

Documento base del refactor. Define el modelo canónico, la columna vertebral de numeración (`TL → RQ → GDS → SOL → EJ`) y el contrato de cada área.

---

## Áreas

### [[Area_produccion]]

Convierte una intención en roadmap y requerimientos. Produce `TL` (timeline) + `RQ` (requerimientos). Define qué se hace, por qué, con qué alcance y prioridad.

### [[Area_gamedesign]]

Technical Game Design. Consume un `RQ` jugable y lo convierte en un sistema jugable claro, implementable y validable. Produce `GDS` (game design spec): reglas, feedback, estados, parámetros configurables.

### [[Area_programacion]]

Convierte un `RQ` (+ `GDS`) en una solución técnica construida con criterio Vaultrum. Produce `SOL` (solución técnica) + `EJ` (ejecución). Sus sub-agentes iteran hasta cumplir los criterios de aceptación.

### [[Area_conocimiento]]

Capa de control de versiones del Core (no es producción). Modelo git: Core = `main`, proyecto = `branch`, aprendizaje = `commit`, entrar al Core = `merge` con aprobación. Gestiona qué conocimiento vuelve al Core, con criterio y sin acumular historial.

---

## [[Indice Agentes]] — capa legacy en migración

Los 7 "Agentes" son el modelo anterior (personas/modos). Se están **absorbiendo dentro de las áreas** que correspondan:

- Programador / Auditor → Área de Programación.
- Technical Game Designer → Área de Game Design.
- Productor → Área de Producción.
- Documentador / Arquitecto de Conocimiento → Área de Conocimiento.

Se conserva su criterio como referencia; lo obsoleto se elimina a medida que se migra.

---

## Regla final

La Agencia no dirige al Core.

La Agencia usa el Core.

Primero criterio. Después área. Después salida registrable.

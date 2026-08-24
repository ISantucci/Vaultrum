## Propósito

El Área de Level Design de Vaultrum toma un sistema jugable ya diseñado (`GDS`) y lo **acomoda en el espacio y el tiempo**: dónde y cuándo se le presentan al jugador los desafíos que las reglas permiten. No inventa reglas nuevas (eso es Game Design) ni diseña interfaces (eso es UI/UX): compone el nivel/escenario/pantalla jugable donde esas reglas cobran vida.

Es el puente entre "estas son las reglas del sistema" y "así se vive el sistema en un nivel concreto". Toma el `GDS` de Game Design y produce un `LDS` (level design spec) que el Área de Programación construye.

---

## Entrada del área

- un `GDS-XXX.n` cerrado del Área de Game Design (reglas, estados, parámetros de balance ya definidos).

Si el `GDS` no implica espacio ni progresión jugable (ej: un sistema puramente de UI o de backend), esta área no interviene. Si el `GDS` está incompleto o ambiguo, deriva a Game Design.

---

## Sub-agentes del área

### [[01_Analista_Espacio]]

Interpreta qué experiencia **espacial y de ritmo** busca el sistema: cómo debería sentirse recorrer y enfrentar esto. Encuadra con los pilares de **dificultad/flow (6)**, **pacing (8)** y **core loop (1)** del libro `05_Fundamentos_de_experiencia_ludica`. No define el layout final.

### [[02_Disenador_Nivel]]

Convierte el encuadre en el nivel: layout, colocación de desafíos y encuentros, puntos de descanso/checkpoint, progresión intra-nivel y **curva de dificultad aplicada** (usa los parámetros de balance del `GDS`, no los redefine). Abre el **LDS-XXX.n**. No cambia las reglas ni programa.

### [[03_Validador_Nivel]]

Verifica que el nivel sea jugable, legible en su recorrido, con pacing y dificultad que respeten la experiencia buscada, y construible. Si algo no cierra, **rebota** al sub-agente correcto. Cierra el `LDS` y lo deja como insumo para Programación.

---

## Cómo trabaja el área — el loop

```
GDS cerrado
  ↓
Analista de Espacio   → encuadre espacial (experiencia de recorrido + ritmo)
  ↓
Diseñador de Nivel    → LDS-XXX.n (layout, encuentros, pacing, dificultad aplicada)  ⟵ gate de nivel
  ↓
Validador de Nivel    → ¿jugable, legible, con buen pacing, construible?
        ├── Sí  → cierra el LDS
        └── No  → rebota:
                  · falta entender la experiencia espacial → Analista de Espacio
                  · layout/encuentros/pacing sin cerrar    → Diseñador de Nivel
                  · balance de reglas mal                  → deriva a Game Design
```

El loop no cierra hasta que el nivel es construible y respeta la experiencia buscada.

---

## Salida del área

Por cada `GDS` con dimensión espacial, un **LDS-XXX.n** registrado en `00_Indice_lds`, con su índice. La numeración se hereda del `GDS` (`GDS-001.2 → LDS-001.2`).

El `LDS` es insumo del Área de Programación (junto al `GDS` y, si existe, el `UXS`).

---

## Regla operativa

Primero entender la experiencia espacial y de ritmo buscada.
Después componer el nivel (layout, encuentros, pacing, dificultad aplicada).
Después validar que sea jugable, legible y construible.
Nunca inventar reglas nuevas (es Game Design) ni diseñar interfaces (es UI/UX).

---

## Límites del área

No define reglas ni balance base (Game Design). No diseña interfaces/HUD/menús (UI/UX). No programa (Programación). No define alcance ni prioridad (Producción). No hace arte final. Si falta regla o balance → Game Design; si falta implementación → entrega el `LDS` a Programación.

---

## Encadenado con otras áreas

Recibe de: **Game Design** (`GDS` cerrado).
Entrega a: **Programación** (`LDS` como insumo de la solución técnica).
Consulta on-demand: la Escuela (`05_Fundamentos_de_experiencia_ludica`), pilares 1, 6, 8, 9.

La numeración `.n` se mantiene entre `GDS / LDS / SOL / EJ` para trazabilidad de punta a punta.


## Flujos del área

Cada flujo es un paso del loop del área. Se entra por el flujo que corresponde al estado del trabajo, no por todos.

### [[01_Flujo_Analisis_Espacio|Flujo Analisis Espacio]]

### [[02_Flujo_Diseno_Nivel|Flujo Diseno Nivel]]

### [[03_Flujo_Validacion_Nivel|Flujo Validacion Nivel]]

---

## Salidas del área

El registro de lo que el área produjo. Cada índice lista sus propias entregas.

### [[02_Agencia/Area level design/Salidas/00_Indice_lds|Indice lds]]

---

## Skill del área

El área corre como la skill `vaultrum-leveldesign` (fuente versionada en `02_Agencia/Area level design/Skills/vaultrum-leveldesign/SKILL.md`).

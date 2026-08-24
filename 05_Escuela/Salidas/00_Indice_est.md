## Índice de Candidatos de Estudio (EST)

Registro de todas las salidas de la Escuela Vaultrum.

Cada `EST-XXX` es un fundamento destilado, citado y validado, listo para el handoff al Área de Conocimiento.

---

## Registro

| EST | Misión (gap) | Fundamento | Estado |
|-----|--------------|------------|--------|
| [[EST-001_Mision_Pong]] | Fundamentos de experiencia (Pong) | [[01_Pong]] + aporte a [[01_Loop_de_experiencia]] | **Handoff hecho** |
| [[EST-002_Mision_Catalogo_RulesOfPlay]] | Catalogar *Rules of Play* | fuente catalogada (sin destilar) | Catalogada |
| [[EST-003_Mision_Catalogo_Batch_Fundamentos]] | Catálogo batch de 28 fuentes del canon | 28 fuentes catalogadas (sin destilar) | Catalogada |
| [[EST-004_Mision_Destilacion_Playbook]] | Destilar 29 fuentes en playbook por función | [[04_Playbook_de_diseno]] (destilación de marco) | **Handoff hecho** |
| [[EST-005_Mision_Fundamentos_Experiencia_Ludica]] | Fundamentos de la buena experiencia lúdica (9 pilares + checklist por-GDS) | [[05_Fundamentos_de_experiencia_ludica]] | **Handoff hecho** |
| [[EST-006_Mision_Lote_Biblioteca_Agosto26]] | Cobertura de la Biblioteca: Fundamentos sin profundizar, estante de Juegos con un solo libro, cero documentación real | 12 Fundamentos (06–17) + 52 documentos del estante nuevo [[00_Indice_documentos]] | En estudio — **sin AiCare, sin handoff** |

---

## Regla

- Un `EST` cuelga siempre de una misión de estudio (gap + presupuesto + barra).
- Estados posibles: En investigación / En destilación / En validación / Listo para handoff / **Handoff hecho** / Catalogada / Descartado.
- Al registrar, linkear a la misión, dejar las citas y el resultado de AiCare.
- Un `EST` con handoff pasa a ser candidato de commit en el Área de Conocimiento; el merge a `main` lo aprueba el owner.
- **Un libro solo es insumo válido de producción cuando está *En la Biblioteca*.** Un libro *En estudio* o *En validación* es material en curso: Producción lo rechaza en su gate de insumo y deriva a Escuela.

---

## Handoff a Conocimiento — resultado

Los tres `EST` con handoff se resolvieron por **indexación**, no por copia: el Core guarda el puntero en [[Experiencia de juego]] y el contenido queda en la Biblioteca, cargándose on-demand.

```txt
EST-001 → 01_Pong (En la Biblioteca) + primer contenido de 01_Loop_de_experiencia
EST-004 → 04_Playbook_de_diseno       indexado
EST-005 → 05_Fundamentos_de_experiencia_ludica  indexado
```

Efecto secundario del handoff: `03_Definicion_de_terminado` pasó de *Reservado* a escrito, sintetizando 01/02/05 y el uso real en `VE-003`. La skill `vaultrum-produccion` ya no lleva el checklist inline como pendiente declarado: apunta al libro.

**Lo que NO se hizo:** promover ningún libro a criterio propio del Core. Indexar es que las áreas lo encuentren; promover es que pase a ser regla. Lo segundo requiere una decisión aparte del owner, caso por caso.

---

## EST-006 — qué falta para cerrarla

A diferencia de las cinco anteriores, esta misión **no está cerrada**. Lo que falta, en orden:

```txt
1. Decisión del owner sobre 02_Game_feel (escribir o deprecar)
2. Pass de AiCare  ← gate obligatorio, todavía no corrido
3. Validación (barra + dedup) libro por libro
4. Handoff a Conocimiento
5. Aprobación del owner → los libros pasan a En la Biblioteca
```

Hasta el paso 5, **ningún libro de este lote es insumo válido de un `RQ`**. El lote es material en curso, no criterio.

Pendiente fuera de esta corrida: los 13 libros de Juegos (02–14) quedaron escritos pero **no implementados**, a la espera de la decisión de nombres de archivo (nombre de género vs nombre del título).

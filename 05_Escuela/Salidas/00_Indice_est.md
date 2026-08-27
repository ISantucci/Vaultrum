## Índice de Candidatos de Estudio (EST)

Registro de todas las salidas de la Escuela Vaultrum.

Cada `EST-XXX` es un fundamento destilado, citado y validado, listo para el handoff al Área de Conocimiento.

---

## Registro

- [[EST-001_Mision_Pong|EST-001 Misión Pong]] — fundamentos de experiencia sobre Pong; produjo el libro de Pong y aportó al de Loop de experiencia. **Handoff hecho.**
- [[EST-002_Mision_Catalogo_RulesOfPlay|EST-002 Misión Rules of Play]] — catalogar la fuente, sin destilar. Catalogada.
- [[EST-003_Mision_Catalogo_Batch_Fundamentos|EST-003 Misión catálogo del canon]] — 28 fuentes del canon catalogadas, sin destilar. Catalogada.
- [[EST-004_Mision_Destilacion_Playbook|EST-004 Misión destilación del Playbook]] — destilar 29 fuentes en un playbook por función. **Handoff hecho.**
- [[EST-005_Mision_Fundamentos_Experiencia_Ludica|EST-005 Misión fundamentos de experiencia lúdica]] — los 9 pilares más el checklist por GDS. **Handoff hecho.**
- [[EST-006_Mision_Lote_Biblioteca_Agosto26|EST-006 Misión lote de Biblioteca]] — lote de agosto: fundamentos nuevos y el estante de documentación real. Pendiente de cierre.
- [[EST-007_Mision_Frameworks_Spec_Driven|EST-007 Misión frameworks spec-driven]] — relevamiento externo: cómo resuelven cuatro frameworks comparables la portabilidad multi-superficie y la economía de tokens. Produjo la fuente `30_Frameworks_spec_driven_multiagente`. **Cerrada con deuda declarada.**
- [[EST-008_Mision_Lote_Level_Design|EST-008 Misión lote de Level Design]] — hueco de estante: el Área de Level Design no tenía ni una fuente. Catalogó `31`–`36` en Fuentes. **Cerrada como misión de catálogo** (sin handoff: no destiló).
- [[EST-009_Mision_Fuentes_Huerfanas|EST-009 Misión fuentes huérfanas]] — el gap se midió leyendo qué cita cada libro *En estudio*: ninguno citaba una fuente de su propio tema. Catalogó `37`–`56` en Fuentes y `53`–`64` en Documentación real, y abrió una sección de estante. **Cerrada como misión de catálogo.**

---

## Regla

- Un `EST` cuelga siempre de una misión de estudio (gap + presupuesto + barra).
- Estados posibles: En investigación / En destilación / En validación / Listo para handoff / **Handoff hecho** / Catalogada / Descartado.
- El `EST` declara su misión en su propia ficha, con las citas y el resultado de AiCare. El índice la nombra.
- Un `EST` con handoff pasa a ser candidato de commit en el Área de Conocimiento; el merge a `main` lo aprueba el owner.
- **Un libro solo es insumo válido de producción cuando está *En la Biblioteca*.** Un libro *En estudio* o *En validación* es material en curso: Producción lo rechaza en su gate de insumo y deriva a Escuela.

---

## Handoff a Conocimiento — resultado

Los tres `EST` con handoff se resolvieron por **indexación**, no por copia: el Core guarda el puntero en `Experiencia de juego` y el contenido queda en la Biblioteca, cargándose on-demand.

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

---
tipo: mision
estado: En estudio — sin AiCare, sin handoff
fecha: 2026-08-24
alcance: Biblioteca — alta masiva de Fundamentos + apertura del estante de Documentación real
produjo: 12 Fundamentos (06–17), 52 documentos, 1 estante nuevo
---

# EST-006 — Lote Biblioteca agosto 2026

> Misión de **cobertura**, no de profundidad puntual. A diferencia de EST-001 a EST-005, esta corrida no estudió un tema: estudió **qué le faltaba a la Biblioteca entera** y llenó los huecos más caros.
> **Estado: abierta.** El material está en los estantes; el gate de AiCare y el handoff no corrieron.

## Índice

- Misión (gap estudiado)
- Presupuesto y barra
- Resultado
- Dedup
- Estado AiCare
- Deuda declarada
- Lo que quedó fuera
- Handoff

---

## Misión (gap estudiado)

La Biblioteca tenía un desbalance estructural que ninguna misión anterior había mirado de frente:

| Estante | Tenía | El hueco |
|---------|-------|----------|
| Fuentes | 29 fichas | Todas de teoría de diseño. Cero de programación, level design, UX aplicado, producción o negocio |
| Fundamentos | 5 libros | 05_Fundamentos_de_experiencia_ludica declaraba **nueve misiones de profundización** en su tabla final. Ninguna corrida |
| Juegos | **1 libro** | Solo 01_Pong. El estante existe para que "hacé un juego de género X" traiga baseline sin pedirlo, y cubría un solo género |
| Documentación real | no existía | Ni un GDD real, ni un postmortem, ni código liberado. Teoría sobre cómo *debería* escribirse un documento de diseño, y cero ejemplos de cómo se escribió uno |

**Pregunta de estudio:** ¿qué contenido le falta a la Biblioteca para que un pedido de "hacé un juego de género X" traiga un baseline sólido sin que el owner tenga que pedirlo?

---

## Presupuesto y barra

**Presupuesto.** Una corrida nocturna. Seis agentes de investigación en paralelo, seis de destilación. El presupuesto de búsqueda web se agotó (200/200) a mitad de la fase de investigación; la fase de destilación corrió sin búsqueda, que es lo correcto —destilar es criterio, no datos.

**Barra.**

- Cada libro con la anatomía completa de `01_Pong`: loop, table-stakes, juice, baseline numérico, Definición de Terminado, aplicación, límites, fuentes.
- Cada Fundamento declara en su frontmatter (`profundiza:`) qué pilar extiende, para no repetir el baseline del libro 05.
- Cada documento con cita verificable **o marca explícita de no verificado**. Nada inventado, nada borrado por no poder confirmarlo.
- Cero texto verbatim con copyright.

---

## Resultado

### Implementado en el vault

```txt
05_Escuela/Biblioteca/Fundamentos/   12 libros nuevos (06–17)      187 KB
05_Escuela/Biblioteca/Documentos/    estante nuevo + 52 fichas      112 KB
                                     ────────────────────────────────────
                                     64 notas nuevas + 5 índices actualizados
```

**Fundamentos 06–17.** Las nueve misiones de profundización declaradas por `05_Fundamentos_de_experiencia_ludica`, más tres áreas que no estaban en ningún estante:

| Libro | Profundiza |
|-------|------------|
| 06_Dificultad_y_curva | Pilar 6 |
| 07_Economia_y_balance | Pilares 6 y 9 |
| 08_Progresion_y_recompensa | Pilar 7 |
| 09_Onboarding_y_tutorial | Pilares 4 y 6 |
| 10_Input_y_respuesta | Pilares 3 y 5 |
| 11_Camara_y_encuadre | Pilares 4 y 5 |
| 12_Pacing_y_estructura | Pilar 8 |
| 13_Playtesting_y_validacion | Proceso — transversal |
| 14_UI_HUD_y_menus | Pilar 4 — **área nueva** |
| 15_Muerte_reintento_y_checkpoints | Pilares 2, 5 y 7 — **área nueva** |
| 16_Audio_como_gameplay | Pilares 3 y 4 — **área nueva** |
| 17_Scope_prototipado_y_cierre | Proceso — **área nueva** |

**Estante de Documentación real.** Cuarto estante de la Biblioteca, declarado en `00_Biblioteca` e indexado en `00_Indice_documentos`. 52 artefactos: 19 GDD y design bibles históricos, 8 colecciones, 9 repos de código liberado, 7 docs oficiales de motor, 4 registros de proceso, 5 hallazgos. Con **regla de licencia de tres niveles** (A explícita / B publicada sin licencia formal / C filtrada o decompilada) como norma del estante.

### Relevado pero no implementado

- 13 libros del estante de Juegos (02–14): arcade clásico y ocho géneros modernos, escritos completos.
- 152 fuentes candidatas con ficha (técnica, craft, producción y negocio).
- 41 postmortems y casos de éxito con lección destilada y cifras citadas.
- 111 recursos vivos (charlas de GDC, canales, wikis, papers con DOI, datasets, comunidades hispanohablantes).

---

## Dedup

Ningún libro duplica uno existente.

- Los Fundamentos 06–17 **profundizan** pilares del libro 05 y lo declaran en el frontmatter. No repiten el baseline: lo continúan.
- El estante de Documentación real no se solapa con Fuentes: Fuentes es bibliografía de estudio, Documentos es evidencia primaria. La misma obra podría aparecer en los dos solo si se estudia como libro *y* se consulta como artefacto — no ocurre en este lote.
- Los 13 libros de Juegos se apoyan en `01_Pong` para lo compartido de paleta-y-pelota en vez de reescribirlo.

---

## Estado AiCare

**Pendiente. Esta misión no puede cerrarse sin ese paso.**

Es exactamente el escenario contra el que AiCare existe: alta masiva de material en el estante más expuesto a intoxicarse. El lote agrega ~95.000 tokens de contenido a la Biblioteca, y el diseño de consulta on-demand implica que **nadie carga eso junto** — pero eso hay que medirlo, no suponerlo.

Lo que el pass tiene que verificar:

```txt
[ ] Peso real de una consulta típica (¿cuánto entra al contexto al abrir un GDS?)
[ ] Solapamiento entre los 12 Fundamentos nuevos y 04_Playbook_de_diseno
[ ] Solapamiento entre Fundamentos 10/16 y el reservado 02_Game_feel
[ ] Si el índice de Documentos alcanza para navegar sin abrir las 52 fichas
[ ] Poda: qué ficha de Documento no aporta y se descarta antes de que sea deuda
```

---

## Deuda declarada

**`02_Game_feel` sigue *Reservado* con 870 bytes,** y los libros nuevos `10_Input_y_respuesta` (la mitad entrante del lazo) y `16_Audio_como_gameplay` (parte de la saliente) lo rodean por los dos lados. Dos libros nuevos apoyándose en un estante vacío es deuda estructural, no un detalle.

Decisión pendiente del owner: **escribirlo de verdad** (y que 10 y 16 lo referencien) o **deprecarlo** repartiendo su contenido entre 10, 16 y `05_Fundamentos_de_experiencia_ludica`.

---

## Lo que quedó fuera

- **Los 13 libros de Juegos**, a la espera de la decisión de nombres de archivo: nombre de género (`07_Puzzle_de_caida`) o nombre del título (`07_Tetris`). Están escritos como género, así que el nombre genérico envejece mejor y no arrastra la marca — pero la decisión cambia el grafo y la toma el owner.
- **Las 152 fuentes candidatas**, que deben entrar por tandas y no de golpe: cada ficha que no se va a leer es peso muerto en el estante.
- **El Core.** No se tocó nada de `01_VaultrumCore`. La Escuela no mergea: indexar en `Experiencia de juego` es una acción del Área de Conocimiento con aprobación del owner.

---

## Handoff

**No solicitado.** Todo el lote entra como `En estudio`.

Por la regla de gobernanza vigente —la que se cerró tras el caso de `01_Pong` usándose en `TL-003` sin aprobar— **ningún libro de este lote es insumo válido de un `RQ`**. Producción lo rechaza en su gate de insumo y deriva a Escuela.

Secuencia para cerrar:

```txt
1. Decisión del owner sobre 02_Game_feel
2. Pass de AiCare              ← gate obligatorio
3. Validación (barra + dedup) libro por libro
4. Handoff a Conocimiento
5. Aprobación del owner → los libros pasan a En la Biblioteca
```

## Estante de Fundamentos

Lo **transversal** de la experiencia: sirve para cualquier género. Todo entregable jugable se apoya en estos libros como baseline, además del libro de su juego/género.

---

## Registro

### [[01_Loop_de_experiencia|Loop de experiencia]]

input → feedback → objetivo → victoria/derrota; loops anidados; juego vs juguete · EST-001 Mision Pong · En la Biblioteca

### [[02_Game_feel|Game feel]]

profundiza Pilar 3 — las tres capas del feel, vocabulario de efectos con sus ventanas de tiempo, juice que informa vs juice que decora · EST-010 Mision Plataformero 2D · En la Biblioteca

### [[03_Definicion_de_terminado|Definicion de terminado]]

checklist de "está hecho" (no "compila"); los dos modos de cierre · síntesis de 01/02/05 + uso en VE-003 Pong3D · En la Biblioteca

### [[04_Playbook_de_diseno|Playbook de diseno]]

principios accionables por función (mostrar, guiar, feel, decisiones, retener, sistemas, emoción, marco, producción, restricciones) · EST-004 Mision Destilacion Playbook · En la Biblioteca

### [[05_Fundamentos_de_experiencia_ludica|Fundamentos de experiencia ludica]]

los 9 pilares de que un sistema se *sienta bien* + CHECKLIST por-GDS + misiones de profundización · EST-005 Mision Fundamentos Experiencia Ludica · En la Biblioteca

### [[06_Dificultad_y_curva|Dificultad y curva]]

profundiza Pilar 6 — cuatro ejes de dificultad, curva escalonada, DDA, asistencias, economía de la muerte · EST-006 Mision Lote Biblioteca Agosto26 · En la Biblioteca

### [[07_Economia_y_balance|Economia y balance]]

profundiza Pilares 6 y 9 — fuentes/sumideros/stocks, bola de nieve y catch-up, inflación, dominancia, balance sin datos · EST-006 Mision Lote Biblioteca Agosto26 · En la Biblioteca

### [[08_Progresion_y_recompensa|Progresion y recompensa]]

profundiza Pilar 7 — las tres progresiones (personaje/jugador/contenido), vertical vs horizontal, meta-progresión · EST-006 Mision Lote Biblioteca Agosto26 · En la Biblioteca

### [[09_Onboarding_y_tutorial|Onboarding y tutorial]]

profundiza Pilares 4 y 6 — enseñar es diseño de niveles; presupuesto de atención 60s/5min/30min · EST-006 Mision Lote Biblioteca Agosto26 · En la Biblioteca

### [[10_Input_y_respuesta|Input y respuesta]]

profundiza Pilares 3 y 5 — cadena de latencia, perdón de input, curvas analógicas, remapeo · EST-006 Mision Lote Biblioteca Agosto26 · En la Biblioteca

### [[11_Camara_y_encuadre|Camara y encuadre]]

profundiza Pilares 4 y 5 — taxonomía de cámara, contrato de información, smoothing, presupuesto de screenshake · EST-006 Mision Lote Biblioteca Agosto26 · En la Biblioteca

### [[12_Pacing_y_estructura|Pacing y estructura]]

profundiza Pilar 8 — la curva de intensidad como objeto diseñable, unidades de pacing, densidad de novedad · EST-006 Mision Lote Biblioteca Agosto26 · En la Biblioteca

### [[13_Playtesting_y_validacion|Playtesting y validacion]]

proceso — tipos de playtest, protocolo, preguntas prohibidas, telemetría mínima, cuándo matar un prototipo · EST-006 Mision Lote Biblioteca Agosto26 · En la Biblioteca

### [[14_UI_HUD_y_menus|UI HUD y menus]]

profundiza Pilar 4 — jerarquía de información, cuatro superficies, estados de UI olvidados, gamepad · EST-006 Mision Lote Biblioteca Agosto26 · En la Biblioteca

### [[15_Muerte_reintento_y_checkpoints|Muerte reintento y checkpoints]]

profundiza Pilares 2, 5 y 7 — el costo de la muerte como perilla, checkpoints, permadeath, muerte instructiva · EST-006 Mision Lote Biblioteca Agosto26 · En la Biblioteca

### [[16_Audio_como_gameplay|Audio como gameplay]]

profundiza Pilares 3 y 4 — confirmar/advertir/ubicar, jerarquía de mezcla, fatiga auditiva, redundancia visual · EST-006 Mision Lote Biblioteca Agosto26 · En la Biblioteca

### [[17_Scope_prototipado_y_cierre|Scope prototipado y cierre]]

proceso — el verbo único, qué pregunta responde cada prototipo, presupuesto de contenido, feature freeze · EST-006 Mision Lote Biblioteca Agosto26 · En la Biblioteca


---

## Regla

- Numeración correlativa por estante (01, 02, ...).
- Estados: Reservado / En estudio / En destilación / En validación / En la Biblioteca / A actualizar.
- Los libros de Fundamentos **no** llevan `genero` (son transversales).
- Se **actualizan**, no se duplican.
- Los libros 06–17 son **misiones de profundización** de los pilares de [[05_Fundamentos_de_experiencia_ludica]]: cada uno declara en su frontmatter (`profundiza:`) qué pilar extiende. No repiten el baseline, lo continúan. Un caso concreto (ej: Pong) puede *aportar* a un fundamento sin crear uno nuevo.

---

## Indexados en el Core

Estos libros están indexados desde `Experiencia de juego` (`01_VaultrumCore/.../05_Experiencia de juego/`). El Core guarda el puntero; el peso vive acá y se carga on-demand.

Un libro **no** se copia al Core. Que un fundamento se promueva a criterio propio del Core lo decide el Área de Conocimiento con aprobación del owner — y en ese caso deja de ser referencia y pasa a ser regla.

---

## Lote EST-006 (agosto 2026) — cerrado

Los doce libros `06`–`17` entraron juntos en `EST-006_Mision_Lote_Biblioteca_Agosto26`. Cubren las nueve misiones de profundización que `05_Fundamentos_de_experiencia_ludica` dejaba declaradas en su tabla final, más tres áreas que no estaban en ningún estante: UI/HUD, audio y scope/cierre.

**Estado: cerrado.** Auditados libro por libro contra `14_UI_HUD_y_menus` como estándar, corregidos en dos pasadas y promovidos el 2026-08-28. `Fundamentos` pasó de *10 usables de 17* a **17 de 17**. La evidencia es `AUDITORIA_Lote_EST-006_20260828`, en `Area conocimiento/Staging`.

Esta sección decía lo contrario durante días. Decía *"Estado: En estudio"* y *"`02_Game_feel` sigue Reservado"* mientras las diecisiete líneas de registro de arriba —en esta misma nota— decían `En la Biblioteca`, y `02_Game_feel` estaba escrito desde `EST-010`. `--verificar` no lo veía: **lee la línea de registro, no la prosa.** Un índice puede contradecirse a sí mismo sin que ningún instrumento se entere, y el remedio no es otro contador — es que la prosa de un índice no repita un estado que la línea de registro ya declara.

```txt
la linea de registro   dice el estado    ← la mide el instrumento
la prosa del estante   dice el porque    ← no repite el estado, lo explica
```

**Lo que sí cambió el instrumento:** `biblioteca.py --verificar` ganó un tercer cruce. Antes comparaba la ficha con el estante; ahora además le pregunta a la **misión**. El lote tuvo 64 piezas cerradas mientras su misión declaraba *"En estudio — sin AiCare, sin handoff"*, y la herramienta contestaba EN NORMA porque ficha y estante coincidían. Ahora falla.

**Regla de carga, medida y no supuesta:** los doce libros juntos pesan **53.2k tokens = 133% de un presupuesto de 40k**. Un `GDS` real —`05` más los dos o tres pilares que toca— pesa 19.5k, el 49%. La consulta on-demand de `Experiencia de juego` no es una recomendación de estilo: es la única forma en que este estante entra.

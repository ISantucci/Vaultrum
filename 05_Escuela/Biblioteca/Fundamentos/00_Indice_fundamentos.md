## Estante de Fundamentos

Lo **transversal** de la experiencia: sirve para cualquier género. Todo entregable jugable se apoya en estos libros como baseline, además del libro de su juego/género.

---

## Registro

### [[01_Loop_de_experiencia|Loop de experiencia]]

input → feedback → objetivo → victoria/derrota; loops anidados; juego vs juguete · EST-001 Mision Pong · En la Biblioteca

### [[02_Game_feel|Game feel]]

juice, feedback, sensación de control · Reservado

### [[03_Definicion_de_terminado|Definicion de terminado]]

checklist de "está hecho" (no "compila"); los dos modos de cierre · síntesis de 01/02/05 + uso en VE-003 Pong3D · En la Biblioteca

### [[04_Playbook_de_diseno|Playbook de diseno]]

principios accionables por función (mostrar, guiar, feel, decisiones, retener, sistemas, emoción, marco, producción, restricciones) · EST-004 Mision Destilacion Playbook · En la Biblioteca

### [[05_Fundamentos_de_experiencia_ludica|Fundamentos de experiencia ludica]]

los 9 pilares de que un sistema se *sienta bien* + CHECKLIST por-GDS + misiones de profundización · EST-005 Mision Fundamentos Experiencia Ludica · En la Biblioteca

### [[06_Dificultad_y_curva|Dificultad y curva]]

profundiza Pilar 6 — cuatro ejes de dificultad, curva escalonada, DDA, asistencias, economía de la muerte · EST-006 Mision Lote Biblioteca Agosto26 · En estudio

### [[07_Economia_y_balance|Economia y balance]]

profundiza Pilares 6 y 9 — fuentes/sumideros/stocks, bola de nieve y catch-up, inflación, dominancia, balance sin datos · EST-006 Mision Lote Biblioteca Agosto26 · En estudio

### [[08_Progresion_y_recompensa|Progresion y recompensa]]

profundiza Pilar 7 — las tres progresiones (personaje/jugador/contenido), vertical vs horizontal, meta-progresión · EST-006 Mision Lote Biblioteca Agosto26 · En estudio

### [[09_Onboarding_y_tutorial|Onboarding y tutorial]]

profundiza Pilares 4 y 6 — enseñar es diseño de niveles; presupuesto de atención 60s/5min/30min · EST-006 Mision Lote Biblioteca Agosto26 · En estudio

### [[10_Input_y_respuesta|Input y respuesta]]

profundiza Pilares 3 y 5 — cadena de latencia, perdón de input, curvas analógicas, remapeo · EST-006 Mision Lote Biblioteca Agosto26 · En estudio

### [[11_Camara_y_encuadre|Camara y encuadre]]

profundiza Pilares 4 y 5 — taxonomía de cámara, contrato de información, smoothing, presupuesto de screenshake · EST-006 Mision Lote Biblioteca Agosto26 · En estudio

### [[12_Pacing_y_estructura|Pacing y estructura]]

profundiza Pilar 8 — la curva de intensidad como objeto diseñable, unidades de pacing, densidad de novedad · EST-006 Mision Lote Biblioteca Agosto26 · En estudio

### [[13_Playtesting_y_validacion|Playtesting y validacion]]

proceso — tipos de playtest, protocolo, preguntas prohibidas, telemetría mínima, cuándo matar un prototipo · EST-006 Mision Lote Biblioteca Agosto26 · En estudio

### [[14_UI_HUD_y_menus|UI HUD y menus]]

profundiza Pilar 4 — jerarquía de información, cuatro superficies, estados de UI olvidados, gamepad · EST-006 Mision Lote Biblioteca Agosto26 · En estudio

### [[15_Muerte_reintento_y_checkpoints|Muerte reintento y checkpoints]]

profundiza Pilares 2, 5 y 7 — el costo de la muerte como perilla, checkpoints, permadeath, muerte instructiva · EST-006 Mision Lote Biblioteca Agosto26 · En estudio

### [[16_Audio_como_gameplay|Audio como gameplay]]

profundiza Pilares 3 y 4 — confirmar/advertir/ubicar, jerarquía de mezcla, fatiga auditiva, redundancia visual · EST-006 Mision Lote Biblioteca Agosto26 · En estudio

### [[17_Scope_prototipado_y_cierre|Scope prototipado y cierre]]

proceso — el verbo único, qué pregunta responde cada prototipo, presupuesto de contenido, feature freeze · EST-006 Mision Lote Biblioteca Agosto26 · En estudio


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

## Lote EST-006 (agosto 2026)

Los doce libros 06–17 entraron juntos en la misión `EST-006_Mision_Lote_Biblioteca_Agosto26`. Cubren las nueve misiones de profundización que el propio `05_Fundamentos_de_experiencia_ludica` dejaba declaradas en su tabla final, más tres áreas que no estaban en ningún estante: UI/HUD, audio y scope/cierre.

**Estado: `En estudio`.** Ninguno pasó por validación, handoff ni AiCare. Por la misma regla de gobernanza que rige el estante de Juegos, **un libro *En estudio* no es insumo válido de un `RQ`**: Producción lo rechaza en su gate de insumo y deriva a Escuela.

**Deuda declarada:** `02_Game_feel` sigue *Reservado* y los libros `10_Input_y_respuesta` y `16_Audio_como_gameplay` lo rodean por los dos lados. Decisión pendiente del owner: escribirlo, o deprecarlo repartiendo su contenido entre 10 y 16.

---
tipo: fundamento
estado: En estudio
mision: [[EST-006_Mision_Lote_Biblioteca_Agosto26]]
profundiza: Pilares 3 — Feedback y game feel · 4 — Claridad y legibilidad
cruza: 05_Fundamentos_de_experiencia_ludica, 02_Game_feel, 14_UI_HUD_y_menus
---

# Fundamento 16 — Audio como gameplay

> Cubre el sonido como canal de información jugable: confirmar, advertir, ubicar, mezclar, variar y adaptar. **No** cubre composición musical, producción de assets, middleware específico ni diseño sonoro como disciplina artística. Tampoco cubre voces ni doblaje.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta
2. El modelo — tres funciones, jerarquía, telegrafiado, variación, capas, silencio
3. Baseline numérico
4. Patrones que funcionan
5. Antipatrones
6. Cómo se verifica
7. CHECKLIST
8. Aplicación · Límites · Fuentes

## Qué es y por qué se rompe si falta
El audio es el canal de información más barato y el más despreciado por el dev solo, que lo agenda para "el final" y termina pegando 15 sonidos gratuitos la semana del release. El resultado es un juego que se siente flojo sin que nadie sepa explicar por qué: los golpes no pegan, los saltos no pesan, los enemigos aparecen de la nada.

La razón técnica es que el oído resuelve tiempo mejor que el ojo. Un cue sonoro llega y se procesa aunque el jugador esté mirando otra parte de la pantalla, y llega con una precisión temporal que ninguna animación iguala. Por eso el audio no es decoración: es el sistema de notificaciones del juego. Un golpe sin sonido es un golpe que no ocurrió; un enemigo que carga un ataque sin cue es un enemigo injusto.

Se rompe también por el lado opuesto: audio que existe pero no está jerarquizado. Si todo suena al mismo volumen, el sonido que salva vidas queda enterrado bajo tres pasos, dos ambientes y la música.

## El modelo

**Capa 1 — Las tres funciones jugables.** Todo sonido que no cumple una de estas tres es ambiente, y el ambiente es lo último que se produce.

| Función | Pregunta que responde | Latencia crítica | Ejemplo | Si falta |
|---|---|---|---|---|
| **Confirmar** | ¿mi input entró? | ≤50 ms | click de salto, chasquido de recarga | El control se siente muerto |
| **Advertir** | ¿algo va a pasar? | 400–800 ms **antes** | gruñido de carga, beep de mina | El juego se siente injusto |
| **Ubicar** | ¿dónde está? | inmediata + espacial | pasos detrás, aleteo a la izquierda | El jugador gira la cámara todo el tiempo |

**Capa 2 — Jerarquía y mezcla.** Cuando dos sonidos compiten, uno tiene que ganar, y esa decisión se toma en el mixer, no en el momento.

```txt
  BUS               EJEMPLO                        NIVEL REL.   DUCKEA A
  ────────────────────────────────────────────────────────────────────────
  0 UI crítica      error, confirmación de menú     -6 dB       1,2,3,4
  1 Advertencia     carga de ataque, timer, alarma  -6 dB       2,3,4
  2 Acción jugador  golpe, salto, recarga, daño     -8 dB       3,4
  3 Mundo/enemigos  pasos, impactos lejanos         -14 dB      4
  4 Música/ambiente colchón, loop, viento           -18 dB      —

  Regla: un sonido nunca puede ser tapado por un bus de número mayor.
  Ducking: -4 a -6 dB, ataque 50 ms, release 300-500 ms.
```

**Capa 3 — El telegrafiado.** Un cue que suena junto con el impacto no es telegrafiado, es notificación de daño. El tiempo de reacción simple humano ronda los 250 ms; para que el jugador *decida* y *ejecute* hace falta más. Por eso el cue va 400–800 ms antes del golpe, y el ataque no puede tener un tiempo de carga menor que su propio cue.

```txt
  t = -0.8 s   ────▶ CUE (audio distintivo, direccional)
  t = -0.5 s   ────▶ anticipación visual (pose, tell)
  t =  0.0 s   ────▶ IMPACTO (sonido de bus 2, contundente)
  t = +0.1 s   ────▶ reacción del mundo (hitstop, shake, partículas)

  Si el cue y el impacto están a menos de 250 ms, el jugador no puede
  reaccionar: la muerte se lee como injusta aunque el balance esté bien.
```

**Capa 4 — Variación y fatiga.** Un sample sin variación deja de escucharse como información y empieza a escucharse como ruido. El mecanismo es adaptación perceptual: el cerebro filtra lo perfectamente repetido. Solución barata: round-robin de 4–8 samples + pitch aleatorio ±5–8% + volumen ±2 dB. Regla de detección: **si un sonido puede sonar más de 3 veces en 10 segundos, necesita variación.**

**Capa 5 — Audio adaptativo.** Dos modelos, y el barato alcanza.

| Modelo | Cómo funciona | Costo | Cuándo |
|---|---|---|---|
| Por capas (horizontal) | Stems que entran y salen sobre la misma base | Bajo si compusiste pensándolo | Exploración → tensión → combate |
| Por estado (vertical) | Pistas distintas con transición en compás | Medio | Cambios de zona o fase de jefe |
| Stinger | Frase corta encima de lo que suene | Muy bajo | Victoria, descubrimiento, muerte |

**Capa 6 — El silencio.** El silencio es el único recurso de audio que cuesta cero producir y funciona por contraste: un corte de 3–8 segundos antes de un pico convierte el pico en evento. Sin silencios, la música al 100% todo el tiempo es una planicie, y una planicie no tiene picos.

**Capa 7 — Lo mínimo, en orden.** Para un dev solo, este es el orden de producción. Cada línea vale más que todas las de abajo juntas.

```txt
  1  Confirmación del verbo principal (saltar / disparar / golpear)
  2  Impacto: dar daño y recibir daño (dos sonidos distintos)
  3  Advertencia de peligro (1 por arquetipo de enemigo)
  4  Recompensa / pickup
  5  UI: navegar, confirmar, cancelar, error
  6  Muerte y fin de nivel
  7  Loop ambiental de zona
  8  Música: 2 capas (base + combate)
```

**Capa 8 — Redundancia visual.** Todo lo que el audio comunica tiene que existir también en visual. No es solo accesibilidad para personas sordas o hipoacúsicas: es el jugador que juega en el colectivo, con la tele muda, o con el bebé durmiendo al lado. La lista de "qué información se pierde con el mute" es literalmente tu backlog de accesibilidad.

## Baseline numérico

| Parámetro / criterio | Baseline sugerido | Por qué |
|---|---|---|
| Latencia input → sonido | ≤50 ms (objetivo ≤30 ms) | Arriba de 100 ms se percibe desacoplado del control |
| Anticipación de un cue de advertencia | 400–800 ms antes del impacto | Reacción humana ~250 ms + margen de decisión |
| Variaciones por sonido de alta frecuencia | 4–8 samples + pitch ±5–8% + vol ±2 dB | Corta la fatiga por repetición |
| Umbral que exige variación | Sonido que suena >3 veces en 10 s | Punto donde el oído empieza a filtrar |
| Voces simultáneas | 24–32 totales; 2–4 por tipo de evento | Evita el barro sonoro en combate |
| Loudness integrado de la mezcla | -18 a -16 LUFS; picos ≤ -1 dBTP | Deja headroom y evita clipping en TV |
| Ducking de música bajo advertencia | -4 a -6 dB, ataque 50 ms, release 300–500 ms | Abre lugar sin que se note el bombeo |
| Rolloff 3D (min / max distance) | 3–5 m / 40–60 m, curva logarítmica | Ubicar sin que todo suene lejos |
| Sonidos mínimos para prototipo jugable | 12–20 | Con menos, el prototipo miente sobre el feel |
| Capas de música adaptativa | 3–4 | Más capas = costo de composición sin ganancia perceptible |
| Crossfade entre capas / estados | 0.5–2 s, alineado a compás | Transición que no se escucha como corte |
| Silencio antes de un pico | ≥1 corte de 3–8 s | El contraste crea el pico |
| Loop ambiental mínimo | ≥60 s, o 20 s con capas asincrónicas | Debajo de 30 s el loop se detecta |
| Duración de un sonido de UI | 60–150 ms | Más largo se solapa al navegar rápido |
| Sliders de volumen | 3 (master, música, SFX) + rango dinámico reducido | Piso de un juego terminado |
| Presupuesto de memoria de audio | 5–10% del budget; streaming para clips >5 s | Los WAV sin comprimir se comen el build |

## Patrones que funcionan

- **Triple confirmación.** Cada acción del jugador devuelve sonido + visual + haptic. *Cuándo:* el verbo principal, siempre. *Costo:* tres assets reutilizables; es la base del game feel.
- **Round-robin con pitch.** Pool de samples + variación aleatoria de tono y volumen. *Cuándo:* pasos, golpes, saltos, impactos. *Costo:* casi cero en código y es la mejor relación costo/beneficio de todo el libro.
- **Cue de dos tiempos.** Whoosh de anticipación + impacto seco, separados 400–800 ms. *Cuándo:* todo ataque telegrafiado. *Costo:* la animación tiene que respetar exactamente ese timing; si la animación cambia, el cue miente.
- **Firma sonora por arquetipo.** Cada tipo de enemigo tiene un timbre reconocible (grave/metálico/agudo) que se identifica sin verlo. *Cuándo:* ≥3 arquetipos de enemigos. *Costo:* un set de 3–5 sonidos por arquetipo.
- **Mezcla por prioridad.** Buses con ducking automático según la tabla de jerarquía, definidos una vez en el mixer. *Cuándo:* apenas tengas más de 20 sonidos. *Costo:* medio día de setup y deja de existir el problema "no escuché la alarma".
- **Capa de tensión por proximidad.** Un stem que sube cuando hay enemigos cerca. *Cuándo:* stealth, survival, exploración con peligro. *Costo:* un sistema de estado de amenaza que después reutilizás para música y para IA.
- **Sonido de estado con corte.** Loops de estado (veneno, poca vida) que se atenúan tras 20–30 s para no fatigar. *Cuándo:* estados persistentes. *Costo:* hay que reforzarlos visualmente porque el audio se retira.
- **Silencio antes del golpe.** Corte total 1–2 s antes de un evento mayor. *Cuándo:* jefes, revelaciones, fin de nivel. *Costo:* coordinación con animación y cámara.
- **Indicador direccional de sonido.** Flecha o arco en el borde de pantalla para sonidos importantes fuera de cámara. *Cuándo:* si el audio comunica posición. *Costo:* UI extra, y resuelve accesibilidad de una.

## Antipatrones

| Antipatrón | Síntoma observable |
|---|---|
| El sample único | El tester baja el volumen a los 10 minutos y sigue jugando |
| Todo en el mismo bus | En combate el sonido crítico existe pero nadie lo escucha |
| Música que tapa la advertencia | Muertes reportadas como injustas solo cuando hay música de combate |
| Audio en el último sprint | El juego se siente flojo y nadie sabe señalar por qué |
| El loop de 8 segundos | El jugador tararea el ambiente y después lo mutea |
| UI más fuerte que el gameplay | Navegar un menú es más contundente que matar un enemigo |
| Alerta solo auditiva | Jugando en mute, el jugador muere sin entender qué pasó |
| Reverb global | Interiores y exteriores suenan igual; se pierde la lectura de espacio |
| Cue que llega con el golpe | El tester dice "no me dio tiempo" con el balance correcto |
| Sonido de daño idéntico al de golpear | El jugador no distingue si pegó o le pegaron |

## Cómo se verifica

- **Test del mute.** Jugá 15 minutos con el sonido apagado y anotá cada información que perdés. Esa lista es, exactamente, tu deuda de accesibilidad y tu backlog de redundancia visual.
- **Test del solo-audio.** Al revés: que alguien escuche la sesión sin ver la pantalla y describa qué está pasando. Si acierta la mayoría de los eventos, tu audio informa.
- **Test de los 20 minutos.** Sesión larga sin interrupciones. El primer sonido que te empiece a molestar es el que necesita variación.
- **Test del parlante malo.** Escuchá la mezcla en el parlante de la notebook y en auriculares baratos. Si el cue de advertencia desaparece en el parlante chico, está en un rango de frecuencia equivocado.
- **Test mono.** Colapsá a mono. Los cues que dependían del paneo para distinguirse tienen que seguir siendo distinguibles por timbre.
- **Conteo de repeticiones.** Loggeá cuántas veces se dispara cada AudioClip por minuto. Todo lo que pase de 6/min sin variación va a la lista de arreglos.

## CHECKLIST

```txt
[ ] Cada sonido del juego esta clasificado: confirmar / advertir / ubicar / ambiente
[ ] El verbo principal tiene sonido de confirmacion con latencia <=50 ms
[ ] Dar daño y recibir daño suenan distinto y son inconfundibles
[ ] Todo ataque enemigo tiene cue >=400 ms antes del impacto
[ ] Ningun cue de advertencia esta a menos de 250 ms del golpe
[ ] Todo sonido que puede sonar >3 veces en 10 s tiene 4+ variaciones + pitch
[ ] Existe un mixer con buses jerarquizados y ducking configurado
[ ] La musica ducka bajo advertencias, no al reves
[ ] Limite de voces por evento configurado (2-4)
[ ] Loops ambientales >=60 s o construidos con capas asincronicas
[ ] Hay al menos 1 silencio deliberado antes de cada pico del juego
[ ] Musica adaptativa: minimo base + combate, transicion en compas
[ ] Rolloff 3D configurado por tipo de fuente, no global
[ ] Reverb por zona, no un reverb unico para todo el juego
[ ] Test del mute hecho: la lista de informacion perdida esta cerrada
[ ] Todo lo que el audio comunica tiene equivalente visual
[ ] 3 sliders de volumen + opcion de rango dinamico reducido
[ ] Mezcla verificada en parlante de notebook, auriculares y mono
[ ] Loudness integrado entre -18 y -16 LUFS, picos <= -1 dBTP
```

## Aplicación · Límites · Fuentes

**Aplicación (Unity, dev solo).** Un `AudioMixer` con los cinco buses de la tabla, y `Snapshots` para los estados globales (normal, pausa, combate, poca vida) resueltos con transiciones de 0.3–0.5 s. Encapsulá todo disparo en un `AudioService.Play(SoundId, position)` que resuelva pool, round-robin, pitch y límite de voces: si vas llamando `AudioSource.PlayOneShot` desde 40 scripts, no vas a poder cambiar la mezcla después. Los `SoundId` como ScriptableObject con su lista de variaciones te dan el round-robin gratis y te dejan intercambiar assets sin tocar código. Para música por capas alcanza con N `AudioSource` sincronizados por `PlayScheduled` y cross-fade de volumen: no hace falta middleware para 3 capas. Comprimí en Vorbis todo lo largo, dejá en PCM/ADPCM solo los sonidos cortos de alta frecuencia.

**Límites.** Este libro trata el audio como sistema de información, no como obra. No cubre composición, síntesis, grabación de foley ni mezcla profesional. Tampoco cubre audio espacial avanzado (HRTF, oclusión, propagación), que en la mayoría de los proyectos de un dev solo es sobre-ingeniería frente a un buen rolloff y un buen paneo. Los valores de loudness son baseline sugerido, no requisito de plataforma: verificá los de tu destino antes de certificar.

**Fuentes.** [[05_Game_Feel]] · [[08_Designing_Games]] · [[09_Gamers_Brain]] · [[11_How_Games_Move_Us]] · [[13_Elements_of_Game_Design]] · [[10_Game_Usability]] · [[29_Racing_the_Beam]]
**Cruces.** [[05_Fundamentos_de_experiencia_ludica]] (Pilares 3 y 4) · [[02_Game_feel]] (el audio como tercio del feel) · [[14_UI_HUD_y_menus]] (redundancia visual e indicadores direccionales) · [[15_Muerte_reintento_y_checkpoints]] (el cue que define si la muerte fue justa)

---

---
tipo: fundamento
estado: En estudio
mision: EST-006_Mision_Lote_Biblioteca_Agosto26
profundiza: Pilar 3 — Feedback y game feel · Pilar 5 — Justicia y control
cruza: 05_Fundamentos_de_experiencia_ludica, 02_Game_feel, 04_Playbook_de_diseno, 03_Definicion_de_terminado
---

# Fundamento 10 — Input y respuesta

> Profundiza la mitad **entrante** del lazo: qué pasa entre que el jugador aprieta y que el juego contesta. Cubre la cadena de latencia, el perdón de input como categoría de diseño, curvas analógicas y las consecuencias de diseño (no de binding) de teclado, gamepad y táctil.
> **No cubre:** el lado saliente del juice —animación, partículas, sonido de impacto— que vive en `02_Game_feel`; netcode y rollback; accesibilidad motriz completa; ergonomía de menús (eso es UI/UX).
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta · 2. El modelo · 3. Baseline numérico · 4. Patrones · 5. Antipatrones · 6. Playtest · 7. Checklist · 8. Aplicación, límites y fuentes.

## Qué es y por qué se rompe si falta
El input es el único canal por el que existe la agencia. Si la respuesta llega tarde, llega distinta o llega **a veces**, el jugador deja de creer que controla; y cuando deja de creer, deja de arriesgar. Un juego con input roto no se juega mal: se juega **defensivo**. El jugador reduce la ambición de sus intenciones hasta el nivel que el sistema le confirma de forma fiable, y eso aplana todo lo demás —dificultad, flow, expresión— sin que ninguna de esas cosas esté mal diseñada.

El síntoma social es peor todavía: el jugador **le pasa la culpa al juego**. Cruza una línea invisible y a partir de ahí toda muerte es injusta. Esa línea no está donde está el promedio de latencia, está donde está la inconsistencia.

## El modelo

**A. La cadena de latencia.** Nadie "tiene" latencia: se acumula en siete tramos y el dev sólo controla tres.

```txt
PULSACIÓN FÍSICA
   │  0.5–3 ms    debounce del switch, recorrido de la tecla
   ▼
DISPOSITIVO                                          [NO controlás]
   │  1–8 ms      polling USB (1000 Hz = 1 ms · 125 Hz = 8 ms)
   ▼              gamepad Bluetooth: +4–15 ms · dongle 2.4 GHz: +2–6 ms
SISTEMA OPERATIVO                                    [NO controlás]
   │  0–4 ms      cola de eventos
   ▼
MOTOR — LECTURA DE INPUT                             [ SÍ controlás ]
   │  0–16.7 ms   el evento espera al próximo tick (60 fps)
   ▼              si leés en FixedUpdate a 50 Hz: hasta 20 ms + pérdidas
LÓGICA DE JUEGO                                      [ SÍ controlás ]
   │  0–16.7 ms   orden de ejecución: un script mal ordenado = +1 frame
   ▼
RENDER + PRESENTACIÓN                                [ SÍ controlás ]
   │  16.7–50 ms  cola de GPU, VSync, triple buffer (1–3 frames)
   ▼
PANTALLA                                             [NO controlás]
   │  1–20 ms     respuesta de pixel + procesamiento del panel
   ▼
   OJO DEL JUGADOR
```

Total realista en PC a 60 fps con VSync doble: **55–90 ms**. Lo que el dev solo puede recortar sin tocar hardware está casi todo en los tres tramos centrales: leer input en `Update` y consumirlo en el `FixedUpdate` siguiente con marca de tiempo, ordenar la ejecución para que el frame de la pulsación sea el frame del cambio de estado, y no encadenar buffers de presentación innecesarios.

**B. Cómo se siente cada rango.** La percepción es por género y, sobre todo, por **consistencia**: un jitter de ±20 ms se siente peor que 85 ms estables.

| Latencia total | Qué siente el jugador | A quién culpa |
|---|---|---|
| < 30 ms | "Es mi mano" — no percibe intermediario | A nadie |
| 30–60 ms | Sólido, directo | A nadie |
| 60–100 ms | Pesado; se adapta bajando el riesgo | A sí mismo, sin saberlo |
| 100–150 ms | Notoriamente lento en acción rápida | **Al juego** |
| > 150 ms | "Está roto", "se traba" | Al juego, en voz alta |

Umbral por género (sugerido): rítmico ≤ 25 ms · fighting/plataformas de precisión ≤ 50 ms · acción general ≤ 70 ms · estrategia y gestión, irrelevante.

**C. Perdón de input como categoría de diseño.** No es un parche: es una capa con su propia taxonomía.

| Mecanismo | Qué corrige | Ventana baseline (60 fps) | Riesgo |
|---|---|---|---|
| Buffer de entrada | Pulsar 2 frames antes de que sea válido | 6–8 f (100–133 ms) | Acciones fantasma si es cola larga |
| Coyote time | Saltar tras dejar el borde | 4–7 f (66–116 ms) | "Flotar", perder lectura del borde |
| Ventana de cancelación | Quedar comprometido a un error | 20–40% del recovery | Combos degenerados |
| Corner correction / nudge | Rozar una esquina al saltar | 8–14 px (2D) | Colarse por huecos no previstos |
| Hurtbox reducida | Golpes "que no me tocaron" | 70–85% del sprite | El jugador aprende a abusar |
| Sticky targeting | Perder el lock al girar | histéresis 15–25° | Cuesta soltar el objetivo |
| Aim assist (fricción) | Micro-temblor del stick | −25 a −45% sensibilidad en el objetivo | Sensación de imán |
| Aim assist (magnetismo) | Puntería gruesa de stick | ≤ 2° de corrección/s | **Robo de agencia** |
| i-frames post-golpe | Encadenados injustos | 30–60 f | Abuso deliberado del daño |

**El eje perdón ↔ robo.** El perdón es legítimo cuando corrige la brecha entre la **intención expresada** y la lectura del sistema. Es robo cuando decide en lugar del jugador. Test de tres preguntas: (1) ¿ya expresó la intención antes de que el sistema ayudara? (2) ¿el resultado asistido es exactamente el que habría logrado con timing perfecto, ni más? (3) ¿puede señalarlo? Si puede señalarlo, se rompió. Un "sí, no, sí" es un bug de diseño.

```txt
BUFFER Y COYOTE — línea de tiempo del salto (1 frame = 16.7 ms)

  SUELO ██████████████████│ AIRE · · · · · · · · · · · · · · · ·
                          │
  coyote time             │←──── 6 f / 100 ms ────→│  salto aún válido
                          │
  buffer      │←─ 8 f / 133 ms ─→│
              apretó acá         toca suelo acá → salta en ese frame

  RIESGO  coyote > 10 f → el borde deja de leerse, el jugador "flota"
          buffer > 12 f → saltos que él no pidió, 200 ms tarde
          buffer en cola (2+ acciones) → tren de acciones fantasma
```

**D. Analógico: zona muerta y curvas.** Cuatro tipos de deadzone: **axial** (por eje: rompe las diagonales), **radial** (magnitud: salto de 0 a 0.15 al salir), **cruzada** (lo peor de ambas) y **radial escalada** — la única recomendable: descartás por magnitud y **re-normalizás** para que apenas salís de la zona muerta valgas 0.0 y en el borde valgas exactamente 1.0.

Curvas de respuesta: lineal (vehículos, cámaras), exponente 1.5–2.5 (puntería fina en el centro), dual-zone (precisión abajo, velocidad arriba, con codo declarado). Para cámara con stick: rampa de aceleración de 100–250 ms más *turn boost* al mantener el eje al máximo. Nunca apliques *lerp* al input crudo para "suavizar": eso se siente como patinar, no como suavidad.

**E. Dispositivos: qué cambia en el diseño.**

| Eje | Teclado + mouse | Gamepad | Táctil |
|---|---|---|---|
| Direcciones de movimiento | 8 discretas | 360° analógicas | 360° con drift |
| Puntería fina | Excelente | Pobre → exige asistencia estructural | Muy pobre + oclusión |
| Acciones simultáneas cómodas | 4–6 | 3–4 | **1–2** |
| Granularidad de intensidad | Nula (on/off) | Alta (gatillos) | Media (presión/duración) |
| Oclusión de pantalla | 0% | 0% | 15–30% (pulgares) |
| Perdón necesario | Bajo | Medio | **Alto** |

Consecuencia: en táctil recortás verbos antes que agrandar botones (objetivo mínimo 7–9 mm ≈ 44–48 px a 160 dpi, separación ≥ 8 px, HUD fuera del arco de los pulgares); en gamepad la precisión de puntería es una decisión de **diseño de encuentros**, no un slider; en teclado el movimiento debe ser divertido con sólo 8 ángulos.

**F. Remapeo como table-stake.** Mínimo no negociable: todas las acciones remapeables (menús incluidos), hold ↔ toggle para agacharse/apuntar/correr, inversión de X e Y por separado, sensibilidad separada por contexto (cadera vs. mira), ningún combo obligatorio de más de dos botones, y ninguna secuencia de *mashing* sin alternativa de mantener.

## Baseline numérico

| Parámetro / criterio | Baseline sugerido | Por qué |
|---|---|---|
| Latencia total objetivo (acción, 60 fps) | ≤ 65 ms; ideal ≤ 50 ms | Bajo 60 ms nadie culpa al juego |
| Jitter máximo tolerable | ±8 ms | La inconsistencia se percibe antes que el promedio |
| Acuse visual/sonoro tras pulsar | ≤ 2 frames (33 ms) | Confirma que el input entró aunque la acción tarde |
| Buffer de entrada | 6–8 frames, **1 sola acción** en cola | Cubre la anticipación humana sin generar fantasmas |
| Coyote time (plataformero) | 5–7 frames | Corrige el error de percepción del borde |
| Ventana de cancelación | 25–35% del recovery de la acción | Devuelve agencia sin borrar el compromiso |
| Deadzone interna (stick) | 8–12% del rango, radial escalada | Cubre el drift típico sin comer precisión |
| Deadzone externa | 92–95% | Garantiza alcanzar 1.0 en los bordes |
| Exponente de curva (puntería) | 1.8 (rango útil 1.5–2.5) | Precisión en el centro, velocidad en el borde |
| Corner correction (2D) | 8–14 px | Perdona el roce sin abrir atajos |
| Hurtbox del jugador | 75–85% del sprite visible | El jugador sobreestima su propio tamaño |
| Aim assist: fricción / magnetismo | −35% sens. / ≤ 2°·s⁻¹ | Fricción es invisible, magnetismo se nota |
| Polling objetivo | 1000 Hz cableado; ≥ 250 Hz gamepad | Cada escalón de polling es un ms real |
| Re-pulsación como señal de error | > 12% de las acciones | Indicador de acuse tardío |

## Patrones que funcionan
- **Lectura en Update / consumo con marca de tiempo.** Guardás `tiempoDePulsacion` y el sistema de física consulta la antigüedad. *Cuándo:* siempre que haya física. *Costo:* hay que decidir quién consume el evento y limpiarlo, o dos sistemas lo comen dos veces.
- **Acuse inmediato, resolución diferida.** Un destello y un click en el frame 1; el disparo resuelve en el 3. *Cuándo:* acciones que casi nunca fallan. *Costo:* si la resolución contradice el acuse, se lee como bug.
- **Perdón escalonado por dificultad.** Coyote 6 f en normal, 3 f en difícil. *Costo:* el timing deja de ser una sola verdad; el jugador que sube de dificultad re-aprende.
- **Cola de una sola acción.** El buffer nuevo pisa al viejo. *Costo:* pierde combos escritos con anticipación larga.
- **Asistencia en dos capas.** Fricción siempre, magnetismo sólo si el objetivo ya está dentro del cono. *Costo:* en PvP hay que exponerlo o se percibe como trampa.
- **Fade de compromiso.** En vez de animación bloqueante, la ventana de cancelación se cierra progresivamente. *Costo:* el balance de frames se vuelve difícil de comunicar.

## Antipatrones
| Antipatrón | Síntoma observable en playtest |
|---|---|
| Leer input en `FixedUpdate` | "A veces no salta"; el tester repite la pulsación y **se mira el dedo** |
| Buffer en cola larga | El personaje ejecuta 800 ms tarde; "yo no apreté eso" |
| Deadzone axial sin normalizar | En diagonal corre más rápido; el arranque salta de 0 a 0.3 |
| Suavizado del eje crudo | Dice "patina" aunque la aceleración esté bien |
| Animación bloqueante sin cancelación | Muere **mirando** una animación, sin tocar el control |
| Magnetismo que salta de objetivo | Micro-zigzag continuo: pelea contra su propia mano |
| Remapeo sólo en gameplay | Queda atrapado en un menú y te pide ayuda |
| Vibración larga y constante | No registra el golpe importante; apaga la vibración |
| Feedback en un solo canal | Con motion blur o sin audio, no sabe si el input entró |

## Cómo se mide en playtest
**Qué observar:** las manos y la cara, no la pantalla. Re-pulsación involuntaria = acuse tardío. Zigzag en la mira = asistencia mal calibrada. Soltar el stick antes de terminar el giro = curva mal. Pausa de medio segundo después de aterrizar = falta buffer y ya lo aprendió.
**Qué preguntar:** "contame qué intentabas hacer en ese salto", "¿en qué momento decidiste saltar?", "mostrame la última muerte que te pareció injusta".
**Qué NO preguntar:** "¿te gustó el control?", "¿notaste latencia?", "¿subimos el coyote time?". Ninguna de las tres tiene respuesta útil y las tres contaminan la sesión siguiente.
**Telemetría mínima:** delta pulsación→ejecución (p50/p95), % de saltos ejecutados dentro de la ventana de coyote, % de acciones servidas por el buffer, re-pulsaciones en < 150 ms, histograma de magnitud de stick (calibra la deadzone real), muertes por caída dentro de los 200 ms de un salto no ejecutado.
**Medición casera de latencia:** filmá pantalla y dedo con el celular a 240 fps y contá cuadros — cada uno son 4.17 ms. Tres tomas, tomá la mediana.

## CHECKLIST
```txt
INPUT Y RESPUESTA — pegar en el GDS

[ ] Latencia medida (240 fps, mediana de 3 tomas): ____ ms  · objetivo ≤65
[ ] El input se lee en Update y se consume con marca de tiempo
[ ] Acuse visual o sonoro dentro de 2 frames para TODA acción del jugador
[ ] Buffer de entrada: ____ frames · cola de 1 sola acción
[ ] Coyote time: ____ frames · declarado y probado en el borde
[ ] Ventana de cancelación definida para cada acción comprometida
[ ] Hurtbox del jugador ≤ 85% del sprite · hitbox ofensiva declarada
[ ] Deadzone radial escalada con re-normalización (0.0 al salir, 1.0 al borde)
[ ] Curva de respuesta declarada por contexto (mover / apuntar / cámara)
[ ] Test de perdón: ¿el jugador puede señalar la asistencia? → si sí, bajar
[ ] Remapeo completo, incluidos menús · hold↔toggle · inversión X e Y
[ ] Ningún combo obligatorio de 3+ botones · ningún mashing sin alternativa
[ ] Jugado con gamepad, teclado y (si aplica) táctil, no sólo con el tuyo
[ ] Vibración con slider y jugable en 0%
```

## Aplicación · Límites · Fuentes
**Aplicación.** En todo GDS de Vaultrum, "Input y respuesta" es una sección propia con la tabla de baselines completada con números reales del proyecto, no con los sugeridos. Ningún requerimiento de movimiento se cierra en `03_Definicion_de_terminado` sin latencia medida.
**Límites.** No aplica a multijugador en red (la predicción y el rollback cambian el modelo entero), ni a controles por movimiento o VR. Los números asumen 60 fps estables: a 30 fps recalculá todo en milisegundos, no en frames.
**Fuentes.** `05_Game_Feel` · `09_Gamers_Brain` · `10_Game_Usability` · `12_Design_of_Everyday_Things` · `02_Art_of_Game_Design` · `15_Game_Mechanics` · `29_Racing_the_Beam` · `01_Pong`.
**Cruces.** `05_Fundamentos_de_experiencia_ludica` (P3, P5) · `02_Game_feel` · `04_Playbook_de_diseno` · `11_Camara_y_encuadre`.

---

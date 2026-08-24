---
tipo: fundamento
estado: En estudio
mision: [[EST-006_Mision_Lote_Biblioteca_Agosto26]]
profundiza: Pilar 8 — Ritmo y pacing
cruza: 05_Fundamentos_de_experiencia_ludica, 01_Loop_de_experiencia, 04_Playbook_de_diseno
---

# Fundamento 12 — Pacing y estructura

> Profundiza la curva de intensidad como objeto diseñable, auditable y dibujable en papel antes de construir nada. Cubre unidades de pacing, alternancia, densidad de novedad, estructura de sesión y el diagnóstico de la repetición.
> **No cubre:** curva de dificultad y ajuste de números (eso es balance, en el GDS); narrativa y estructura dramática de guion; economía y monetización; pacing multijugador.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta · 2. El modelo · 3. Baseline numérico · 4. Patrones · 5. Antipatrones · 6. Playtest · 7. Checklist · 8. Aplicación, límites y fuentes.

## Qué es y por qué se rompe si falta
El pacing es la **derivada** de la experiencia: no importa cuánta intensidad hay, importa cómo cambia. Un juego puede tener buen loop, buen feel y buena cámara y aun así ser insoportable, porque el jugador no percibe valores absolutos: percibe **contrastes**. Un pico de 8/10 después de un valle de 3/10 se siente enorme; el mismo 8 después de un 7 sostenido durante veinte minutos se siente cansancio.

Cuando falta, el diagnóstico es engañoso. El tester dice "es muy difícil" en el minuto 25 y en realidad está fatigado: su tasa de acierto cayó sin que el contenido cambiara. El dev baja los números, arruina el balance, y el problema —una meseta de intensidad sin valles— sigue intacto.

## El modelo

**A. Qué es intensidad.** No es dificultad. Intensidad = amenaza percibida + densidad de decisiones + carga cognitiva + estímulo audiovisual + presión temporal. Un puzzle sin enemigos puede estar en 8. Una arena con 40 enemigos triviales puede estar en 4.

**B. Unidades de pacing.** Cada nivel de zoom tiene su propia curva y su propio modo de fallar.

| Unidad | Duración | Qué la abre | Qué la cierra | Falla típica |
|---|---|---|---|---|
| Beat | 2–10 s | Un estímulo | Su resolución | Beats idénticos en serie |
| Encuentro | 45–90 s | Una amenaza o problema | Victoria/derrota | Encuentros de 3+ min sin fases |
| Secuencia / sala | 3–8 min | Un espacio nuevo | Una puerta, un cofre, un checkpoint | Sala sin gancho de salida |
| Nivel | 8–20 min | Una premisa espacial | Clímax + bajada | Clímax que no es el máximo |
| Acto | 1–4 h | Una promesa nueva | Un giro de sistema | Acto 2 sin capa nueva |
| Sesión | 20–90 min | El jugador se sienta | El jugador elige irse | Sin punto de salida natural |
| Campaña | 6–40 h | La fantasía | El cierre | Último tercio de relleno |

**C. La forma: serrucho ascendente.**

```txt
CURVA DE INTENSIDAD — nivel de 15 min (escala 0–10, muestreo cada 30 s)

10 │                                                  ██
 9 │                                                  ██
 8 │          ██              ██          ██          ██
 7 │          ██              ██          ██          ██
 6 │      ██  ██          ██  ██      ██  ██          ██
 5 │  ██  ██  ██  ██      ██  ██  ██  ██  ██  ██      ██
 4 │  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██
 3 │  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██
 2 │  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██
 1 │  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██
   └──────────────────────────────────────────────────────────
      G   P1  V1  P2  V2  P3  V3  P4  V4  P5  V5  CLI  BAJ
     0'  1'  2'30 4'  5'30 7' 8'30 10' 11' 12'30    14'  15'

 G   gancho ≤45 s      P  pico 45–90 s      V  valle
 DELTA   cada pico supera al valle anterior en ≥3 puntos
 TECHO   el clímax es el único 10 del nivel
 BAJADA  20–40 s sin amenaza después del clímax
 PLANO   ningún tramo con variación <2 puntos durante más de 4 min
```

**D. El rol del valle.** Un valle no es tiempo perdido: hace tres trabajos simultáneos. (1) **Consolida** el aprendizaje del pico anterior —el cerebro no integra bajo carga—. (2) **Restaura** recursos y atención. (3) **Hace legible** el pico siguiente por contraste. Duración sugerida: 20–40% del pico previo, mínimo 20 s. Y un valle **nunca es una pantalla vacía**: es loot, ruta, decisión de build, una conversación, un rincón que premia mirar.

**E. Densidad de novedad.** La atención se paga con ideas nuevas, y la tolerancia baja con el tiempo invertido porque la habilidad sube.

| Fase | Idea nueva cada | Qué cuenta como idea |
|---|---|---|
| 0–10 min | 60–90 s | Verbo, enemigo, obstáculo, regla, giro visual |
| 10–60 min | 3–5 min | Lo anterior + combinación explícita de dos ideas viejas |
| 1–5 h | 8–15 min | Sobre todo recombinación; novedad pura reservada para los actos |
| 5 h+ | Por acto | Capa de sistema, no elemento suelto |

**Regla de recombinación 3:1.** Por cada mecánica nueva, tres encuentros que la crucen con mecánicas viejas. Sin esto, la novedad se convierte en un desfile de cosas que el jugador no recuerda.

**Introducción de una mecánica en 4 tiempos:** presentar en seguro (sin castigo, 15–30 s) → exigir en aislado (el fracaso cuesta poco, 1–2 min) → combinar con lo viejo (3 encuentros) → subvertir o invertir (1 encuentro). Saltarse el tiempo 1 produce la queja "no me explicaron"; saltarse el 3 produce "esa mecánica no servía para nada".

**F. El primer minuto.**

| Segundo | Qué tiene que haber pasado |
|---|---|
| 0–5 | Una imagen que promete el género. Sin logos, sin carga larga |
| 5–15 | El control ya está en la mano y algo responde |
| 15–30 | Primer verbo con feedback fuerte (el que vende el juego) |
| 30–60 | Primera decisión con consecuencia visible + objetivo nombrado |
| 60–90 | Primera amenaza real, telegrafiada |

**G. El minuto 30.** La pregunta del jugador cambia de "¿entiendo esto?" a "¿esto va a algún lado?". A esa altura tenés que haber entregado tres cosas: la segunda capa del sistema (o su promesa concreta), una meta de mediano plazo, y una razón para volver mañana. **Test del minuto 30:** pausá y preguntá "¿qué querés conseguir en la próxima hora?". Si no puede nombrarlo, el pacing macro está roto, no la dificultad.

**H. Estructura de sesión y punto de salida.** Definí una sesión objetivo (móvil 5–12 min · PC/consola 35–75 min) y diseñá **puntos de salida natural** cada 8–12 min: momentos donde el estado está guardado, hay cierre mecánico o narrativo, y hay un gancho abierto para la próxima. Un jugador que sale en un pico de satisfacción vuelve; uno que sale en un pozo de frustración —o que perdió progreso porque el autoguardado estaba a 25 minutos— no.

**I. Repetición buena vs. relleno.**

| Dimensión | Repetición de dominio | Repetición de relleno |
|---|---|---|
| ¿El resultado varía? | Sí, según la ejecución | No, sólo el tiempo |
| ¿Mejora la ejecución? | Sí, y se nota | No hay techo de habilidad |
| ¿El tiempo baja con la habilidad? | Sí | No |
| ¿El jugador elige repetir? | Sí | Lo obliga la economía |
| ¿Hay información nueva? | Sí (variación, lectura) | No |

**Prueba del asfalto:** si el jugador ya sabe el resultado antes de empezar y no puede hacerlo ni más rápido ni mejor, es relleno. Sacalo o dale techo de habilidad.

**J. Cómo se dibuja y audita en papel.** Siete pasos, antes de abrir el motor: (1) declarar la duración objetivo de la unidad; (2) listar los beats en una fila por minuto; (3) asignar intensidad prevista 0–10 a cada uno; (4) marcar tipo (pico / valle / meseta); (5) marcar si hay idea nueva; (6) anotar el recurso con el que el jugador entra (vida, munición, atención); (7) marcar los puntos de salida. Después, cinco chequeos de auditoría: ¿hay al menos 3 picos por cada 15 min? ¿ningún tramo plano de más de 4 min? ¿ningún pico sostenido de más de 90 s sin valle? ¿el clímax es el máximo absoluto? ¿la densidad de novedad respeta la fase? Cualquier "no" se arregla en la planilla, donde cuesta cinco minutos, no en el motor, donde cuesta cinco días.

## Baseline numérico

| Parámetro / criterio | Baseline sugerido | Por qué |
|---|---|---|
| Gancho inicial | ≤ 45 s hasta el primer verbo con feedback fuerte | Antes de eso se decide si sigue |
| Primera decisión con consecuencia | ≤ 60 s | Convierte al espectador en jugador |
| Duración de encuentro estándar | 45–90 s | Encima exige fases o se lee como esponja |
| Pico sostenido máximo | 90 s sin valle | La atención sostenida cae ahí |
| Duración del valle | 20–40% del pico previo, mín. 20 s | Consolida sin enfriar |
| Delta pico/valle mínimo | ≥ 3 puntos sobre 10 | El contraste es lo que se percibe |
| Tramo plano máximo | 4 min con variación < 2 puntos | Umbral típico de aburrimiento reportado |
| Duración de nivel | 8–20 min | Cabe en una sesión corta y en la memoria |
| Punto de salida natural | Cada 8–12 min | Respeta la vida del jugador |
| Bajada post-clímax | 20–40 s sin amenaza | Sin exhalación no hay recuerdo de victoria |
| Reintento tras muerte | ≤ 3 s hasta jugar de nuevo | Cada segundo extra convierte tensión en fastidio |
| Ratio de recombinación | 3 encuentros mixtos por mecánica nueva | Fija la idea sin autoría infinita |
| Tutorial | ≤ 10% del tiempo del acto 1 | Más allá, se lee como impuesto |
| Cinemática sin input | ≤ 45–90 s, siempre salteable | Umbral donde el jugador suelta el mando |
| Retención al minuto 30 | ≥ 60% de los testers llegan | Punto de abandono más frecuente |

## Patrones que funcionan
- **Serrucho ascendente.** Picos crecientes con valles entre medio. *Cuándo:* estructura por defecto de cualquier nivel. *Costo:* exige contenido de relleno de calidad para los valles — no es gratis.
- **Valle con trabajo liviano.** El respiro tiene una tarea de baja tensión (loot, ruta, build). *Costo:* si el trabajo liviano se vuelve obligatorio y largo, es relleno con otro nombre.
- **Bookend de sesión.** Abrí con un objetivo de sesión declarado y cerrá con su cierre. *Costo:* requiere un sistema de metas visible y persistente.
- **Regla de tres y quiebre.** Tres encuentros que enseñan la regla, el cuarto la rompe. *Costo:* el cuarto es autoría manual, nunca procedural.
- **Exhalación forzada.** 20–40 s post-clímax donde nada puede matarte. *Costo:* parece tiempo muerto en la planilla; defendelo.
- **Rampa de reingreso.** Los primeros 60 s tras cargar partida son de baja exigencia y recuerdan el objetivo. *Costo:* hay que persistir contexto, no sólo estado.
- **Falso final / doble clímax.** *Costo:* si el segundo pico no supera al primero, el nivel se lee como estirado.
- **Presupuesto de novedad por hora.** Se usa como herramienta de scope: si el acto 2 necesita 8 ideas y tenés presupuesto para 4, el acto 2 dura la mitad.
- **Micro-serrucho (móvil).** Ciclos pico/valle de 20–40 s dentro de sesiones de 6 min. *Costo:* imposible construir tensión larga.

## Antipatrones
| Antipatrón | Síntoma observable en playtest |
|---|---|
| Meseta alta ("todo a 11") | Juega **peor** en el minuto 20 que en el 5 con el mismo contenido; dice "es difícil" |
| Tutorial largo | Mueve el stick mientras lee; saltea el texto; te pregunta cosas que el texto explicaba |
| Valle vacío (pasillo sin nada) | Mira el celular, o te habla a vos sobre otro tema |
| Relleno por economía | Pregunta "¿cuánto falta?" |
| Novedad sin recombinación | No recuerda la mecánica 20 min después; no la usa cuando serviría |
| Clímax sin bajada | Se queda quieto tras ganar; no celebra; corta seco al menú |
| Sin punto de salida | Abandona a mitad de nivel, pierde progreso y no vuelve al día siguiente |
| Confundir dificultad con intensidad | Subiste los números y la curva percibida no se movió |
| Todos los niveles con la misma forma | Desde el nivel 4 predice la estructura y baja la atención visiblemente |
| Spike sin telegrafía en el minuto 30 | Pico de abandono justo ahí en la telemetría |

## Cómo se mide en playtest
**Qué observar:** sesión completa, sin interrupciones, con una **hoja de intensidad percibida** que llenás vos cada 2 minutos (0–10) mientras mirás. Anotá micro-conductas: cambio de postura, mirar el celular, suspirar, hablar del juego (bueno) vs. hablar de otra cosa (malo), la primera vez que pregunta cuánto falta.
**Qué preguntar después:** "contame el nivel de memoria, momento por momento" —lo que no recuerda, no existió—; "¿en qué momento pensaste en parar?"; "si mañana tuvieras 20 minutos, ¿qué harías primero?".
**Qué NO preguntar:** "¿fue muy largo?", "¿te aburriste?" (nadie lo admite en la cara del autor), "¿qué le sacarías?".
**Telemetría mínima:** tiempo por sala, gap entre acciones significativas (más de 8 s marca un valle no diseñado), muertes por minuto como curva, punto exacto de abandono de sesión, duración de sesión, % que llega al minuto 30, tiempo hasta el primer objetivo declarado. Superponé tu hoja de intensidad prevista con la curva real de muertes por minuto: donde no coinciden, ahí está el problema.

## CHECKLIST
```txt
PACING Y ESTRUCTURA — pegar en el GDS / LDS

[ ] Curva de intensidad dibujada en papel ANTES de construir la unidad
[ ] Duración objetivo declarada: beat/encuentro/nivel/sesión
[ ] Gancho ≤45 s · primera decisión con consecuencia ≤60 s
[ ] Ningún pico sostenido >90 s sin valle
[ ] Ningún tramo plano >4 min (variación <2 puntos)
[ ] Delta pico/valle ≥3 en cada transición
[ ] Cada valle tiene trabajo liviano; ninguno es pasillo vacío
[ ] Clímax = máximo absoluto del nivel · bajada de 20–40 s después
[ ] Densidad de novedad respetada según fase (60–90 s / 3–5 min / 8–15 min)
[ ] Recombinación 3:1 cumplida para cada mecánica nueva
[ ] Mecánicas introducidas en 4 tiempos (seguro → aislado → combinado → subvertido)
[ ] Punto de salida natural cada 8–12 min (guardado + cierre + gancho)
[ ] Test del minuto 30: el tester puede nombrar su objetivo de la próxima hora
[ ] Cada repetición pasa la prueba del asfalto (varía o tiene techo de habilidad)
[ ] Reintento tras muerte ≤3 s
[ ] Auditoría de 5 chequeos firmada antes de pasar a producción
```

## Aplicación · Límites · Fuentes
**Aplicación.** La planilla de curva es entregable del LDS: una fila por minuto, con intensidad prevista, tipo, novedad y punto de salida. La auditoría de cinco chequeos entra en [[03_Definicion_de_terminado]] como criterio de cierre de nivel.
**Límites.** No aplica tal cual a juegos sin narrativa espacial (puzzle infinito, roguelike puro, sandbox) donde el pacing lo genera el sistema: ahí se diseña la **distribución** de intensidad, no la curva. Tampoco cubre pacing de sesiones sociales, donde el grupo impone su propio ritmo.
**Fuentes.** [[08_Designing_Games]] · [[04_Theory_of_Fun]] · [[02_Art_of_Game_Design]] · [[03_Game_Design_Workshop]] · [[13_Elements_of_Game_Design]] · [[14_Fundamentals_of_Game_Design]] · [[16_Advanced_Game_Design]] · [[17_Uncertainty_in_Games]] · [[18_Art_of_Failure]] · [[11_How_Games_Move_Us]] · [[19_Playful_Production_Process]].
**Cruces.** [[05_Fundamentos_de_experiencia_ludica]] (P8, P6, P7) · [[01_Loop_de_experiencia]] · [[04_Playbook_de_diseno]] · [[13_Playtesting_y_validacion]].

---

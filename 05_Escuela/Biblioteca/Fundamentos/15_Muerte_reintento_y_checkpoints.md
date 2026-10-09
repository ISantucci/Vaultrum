---
tipo: fundamento
estado: En la Biblioteca
mision: EST-006_Mision_Lote_Biblioteca_Agosto26
profundiza: Pilares 2 — Victoria/derrota y estados de fin · 5 — Justicia y control · 7 — Recompensa y motivación
cruza: 05_Fundamentos_de_experiencia_ludica, 01_Loop_de_experiencia, 03_Definicion_de_terminado
---

# Fundamento 15 — Muerte, reintento y checkpoints

> Cubre el fracaso como sistema: qué cuesta morir, dónde se guarda el progreso, cuánto tarda el reintento y cómo se mide si tus muertes son justas. **No** cubre la curva de dificultad ni el balance de encuentros (eso es Pilar 6), ni la narrativa de la muerte, ni el diseño espacial de los niveles.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta
2. El modelo — costo, tolerancia, checkpoint, guardado, muerte instructiva
3. Baseline numérico
4. Patrones que funcionan
5. Antipatrones
6. Cómo se verifica
7. CHECKLIST
8. Aplicación · Límites · Fuentes

## Qué es y por qué se rompe si falta
La muerte no es el castigo del juego: es su mecanismo de enseñanza más barato. Un juego sin costo por fallar no tiene tensión, y un juego con costo mal calibrado no tiene jugadores. Entre esos dos extremos hay una perilla, y la mayoría de los devs solos nunca la giran a propósito: heredan el comportamiento del template y descubren en el playtest que la gente abandona en el minuto 12.

Se rompe de dos maneras opuestas. Con costo bajo, el jugador deja de pensar y empieza a hacer fuerza bruta: pierde la sensación de logro y el juego se vuelve trámite. Con costo alto, el jugador deja de experimentar: juega conservador, evita las mecánicas interesantes que le diseñaste, y cuando pierde una hora de progreso cierra el juego y no vuelve. El punto medio no es "dificultad media": es **costo bajo con causa clarísima**.

## El modelo

**Capa 1 — Taxonomía del costo.** Morir siempre cuesta algo. La pregunta de diseño es *qué* y *cuánto*.

| Tipo de costo | Qué se pierde | Perilla | Riesgo si se exagera |
|---|---|---|---|
| Tiempo | Segundos hasta volver al control | Distancia al checkpoint + carga + animación | El jugador mira pantallas, no juega |
| Progreso | Terreno, puzzles, cutscenes ya superados | Densidad de checkpoints | Repetición mecánica sin aprendizaje |
| Recursos | Munición, oro, consumibles, XP | % de pérdida, recuperabilidad | Espiral de la muerte: perdés porque perdiste |
| Información | Estado del mundo, plan, memoria de la sala | Reset determinista vs aleatorio | El jugador no puede formar hipótesis |
| Dignidad | Contador de muertes, ranking, testigos | Visibilidad del fracaso | Vergüenza → abandono, sobre todo en stream |

**Capa 2 — La ecuación de tolerancia.** No es una fórmula exacta: es una brújula para saber qué perilla tocar cuando el playtest se queja.

```txt
                 claridad de la causa  ×  velocidad del reintento
   TOLERANCIA ≈ ───────────────────────────────────────────────────
                              costo de la muerte

   claridad     0 = "¿qué pasó?"        1 = "pisé el pico, obvio"
   velocidad    0 = 20 s + menú          1 = <1.5 s, botón directo
   costo        1 = respawn en el lugar  10 = perdés 40 min

   Si baja la tolerancia, subí claridad o velocidad ANTES de bajar el costo.
   El costo es lo que le da valor al intento; los otros dos son gratis de mejorar.
```

**Capa 3 — El bucle de la muerte instructiva.** Una muerte que no enseña es tiempo robado.

```txt
   MUERTE ──▶ CAUSA LEGIBLE ──▶ REINTENTO ──▶ HIPÓTESIS ──▶ INTENTO
              (<=1 s, visible    (<=3 s, sin    ("esta vez     (aplica lo
               y sin ambigüedad)  menús)         salto antes")  aprendido)
      ▲                                                              │
      └──────────────────────────────────────────────────────────────┘

   Si el jugador no puede completar la casilla HIPÓTESIS, el bucle
   no es aprendizaje: es lotería. Ese es el bug, no la dificultad.
```

**Capa 4 — Checkpoint: dónde, qué y qué no.** El checkpoint va **inmediatamente antes del desafío nuevo**, nunca en el medio y nunca después de un tramo de tránsito. Regla operativa: si entre el checkpoint y la muerte hay más de 30 segundos de contenido ya dominado, el checkpoint está mal puesto.

| Qué guarda | Qué NO guarda | Motivo |
|---|---|---|
| Posición y estado del jugador | Munición gastada en el intento fallido | Evita la espiral de la muerte |
| Puertas abiertas, puzzles resueltos | Enemigos ya muertos en la sala del desafío | El desafío tiene que ser repetible completo |
| Recursos al momento de tocarlo | Estado de la cámara / cinemática | Nada de re-mirar lo mismo |
| Contador de intentos (interno) | — | Es tu telemetría de justicia |

**Capa 5 — Modelos de guardado.**

| Modelo | Cuándo conviene | Costo de diseño |
|---|---|---|
| Autosave por checkpoint | Acción, plataformas, aventura lineal | Bajo; exige checkpoints bien puestos |
| Save manual multi-slot | RPG, sim, juegos largos con builds | Medio; hay que serializar todo |
| Autosave + slot manual | Default seguro para un dev solo | Medio |
| Suspend save (guardar y salir) | Handheld, sesiones cortas | Alto si el estado es complejo |
| Permadeath por run | Roguelite, runs de 20–45 min | Alto: hay que balancear run **y** meta |

**Capa 6 — Permadeath.** Funciona cuando la run es corta, generada y el fracaso produce conocimiento transferible o meta-progresión. Falla en un plataformero autoral porque ahí el contenido es fijo: repetir el nivel 1 por décima vez no genera información nueva, genera resentimiento. Regla: **permadeath necesita variación entre runs; sin variación es solo castigo.**

**Capa 7 — El game over.** Es el peor lugar del juego para poner fricción, porque el jugador ya está en su momento de menor paciencia. Ideal: no existe como pantalla, el reintento es inmediato. Si existe, tiene una sola acción por defecto ya enfocada (Reintentar) y se puede saltear con cualquier botón después de 0.3 s.

## Baseline numérico

| Parámetro / criterio | Baseline sugerido | Por qué |
|---|---|---|
| Muerte → control recuperado (acción rápida) | ≤1.5 s | Mantiene el bucle de intento en flujo |
| Muerte → control recuperado (acción 3D / aventura) | ≤5 s | Techo antes de que el jugador suelte el mando |
| Muerte → control recuperado con carga | ≤8 s; >15 s = rediseñar | Arriba de eso el costo real es la carga, no el error |
| Contenido dominado a repetir antes del punto de muerte | ≤30 s | Umbral donde la repetición deja de enseñar |
| Distancia entre checkpoints (acción) | 45–90 s de juego limpio | Un desafío por checkpoint |
| Duración de la animación de muerte | ≤1.2 s, salteable tras 0.3 s | Es feedback, no espectáculo |
| Tasa de muerte en nivel calibrado (acción) | 1 cada 3–8 min | Debajo aburre, arriba frustra |
| Intentos esperados en un jefe | 3–8 | Suficiente para aprender el patrón |
| Alerta de injusticia | >25% de jugadores muere ≥6 veces en el mismo trigger | Es diseño, no habilidad |
| Pérdida de recursos por muerte (progresión larga) | ≤10%, recuperable | Evita la espiral de la muerte |
| Pérdida total de recursos | Aceptable solo si la run dura ≤25–45 min | El costo tiene que caber en una sesión |
| Meta-progresión en roguelite | ≥1 desbloqueo cada 2–3 runs fallidas | Convierte el fracaso en recompensa (Pilar 7) |
| Slots de guardado | ≥3 manuales + 2 autosave rotativos | Rotar evita perder todo por corrupción |
| Frecuencia de autosave (juego largo) | ≤3 min, nunca durante combate | El jugador nunca pierde más de una escena |
| Coyote time (plataformas) | 4–6 frames @60 fps | La mayoría de las muertes "injustas" viven acá |
| i-frames tras recibir daño | 0.5–1.0 s | Evita el doble golpe que se lee como bug |
| Acierto en "¿qué te mató?" post-partida | ≥90% de respuestas correctas | Métrica directa de claridad de la causa |

## Patrones que funcionan

- **Reintento instantáneo.** Un botón dedicado que resetea la escena sin pasar por menú ni pantalla. *Cuándo:* cualquier juego con muerte frecuente. *Costo:* obliga a que el reset del nivel sea determinista y barato; es un requisito de arquitectura, no un feature de UI.
- **Checkpoint respirado.** El punto de guardado va en el último lugar seguro antes del desafío, con 2–3 segundos de aire para reorientarse. *Cuándo:* siempre. *Costo:* le pone restricciones al level design, que ya no puede encadenar desafíos sin pausa.
- **La muerte que devuelve información.** Al morir, el juego muestra la causa: el proyectil que te pegó queda resaltado 0.5 s, o un texto de una línea ("Caída"), o un marcador en el mundo donde caíste. *Cuándo:* si el playtest pregunta "¿qué me mató?". *Costo:* pequeño sistema de "última fuente de daño"; es una de las mejores relaciones costo/beneficio del libro.
- **Costo escalonado.** La primera muerte en un desafío es gratis, la tercera empieza a costar. *Cuándo:* juegos con recursos y público mixto. *Costo:* hay que comunicarlo o parece un bug.
- **Moneda del cadáver.** Perdés los recursos al morir pero podés recuperarlos volviendo al lugar, una sola vez. *Cuándo:* progresión larga con tensión deseada. *Costo:* genera una minoría que abandona; es una decisión de identidad, no de balance.
- **Autosave sombra.** Guardado silencioso al entrar a cada sala, además del checkpoint visible. *Cuándo:* juegos donde un crash cuesta caro. *Costo:* espacio y bugs de estado parcial; probalo con crash forzado.
- **Modo asistido.** Opciones de accesibilidad de dificultad (vida extra, invulnerabilidad, saltear encuentro) sin bloquear contenido ni logros. *Cuándo:* al cerrar el juego. *Costo:* testear un segundo balance, pero amplía el público sin tocar el diseño base.
- **Permadeath con memoria.** La run se pierde, el conocimiento y los desbloqueos quedan. *Cuándo:* roguelite. *Costo:* dos economías paralelas para balancear.

## Antipatrones

| Antipatrón | Síntoma observable |
|---|---|
| Muerte por causa invisible | En playtest, "¿qué me mató?" aparece más de una vez cada 10 min |
| Cutscene no salteable antes del jefe | El tester comenta la cutscene, no el jefe |
| Pasillo de 90 s entre checkpoint y desafío | El jugador corre distraído y muere en el tránsito |
| Game over con menú de tres niveles | Baja el ritmo de intentos por minuto a menos de la mitad |
| Autosave en el peor momento | Guardado con 1 HP, sin recursos y sin salida: softlock |
| Pérdida total sin aviso | Reviews con la palabra "injusto"; abandono en la primera muerte grande |
| Muerte por carga | El tiempo muerto supera al tiempo jugado en tramos difíciles |
| Dificultad por repetición | El desafío real es la resistencia al tedio, no la habilidad |
| Contador de muertes obligatorio y visible | Jugadores que reinician la partida para "limpiar" el número |
| Enemigos ya muertos que reviven en el reintento | El jugador vuelve a pelear lo que ya resolvió |

## Cómo se verifica

- **Log de muerte.** Cada muerte escribe: posición, causa, tiempo desde el último checkpoint, número de intento en ese trigger, tiempo hasta recuperar el control. Con 5 testers y 2 horas ya tenés el mapa de calor de tu juego.
- **La pregunta de los tres segundos.** Justo después de morir, preguntá qué lo mató. Menos de 90% de aciertos = problema de telegrafiado o de legibilidad, no de dificultad.
- **Tiempo muerto.** Sumá todo el tiempo sin control (animación + carga + menú + tránsito repetido) y dividilo por el tiempo de sesión. Objetivo: <5%. Arriba de 15% el juego se siente lento aunque el gameplay sea rápido.
- **Curva de intentos.** Graficá intentos por trigger. Un pico aislado de 6+ intentos donde el resto está en 1–2 es un problema de diseño puntual, y casi siempre es un problema de comunicación, no de balance.
- **Test del crash.** Matá el proceso en cinco momentos distintos y verificá que el jugador nunca pierda más de una escena.

## CHECKLIST

```txt
[ ] Esta escrito que se pierde al morir: tiempo, progreso, recursos, informacion
[ ] La causa de la muerte es identificable en <=1 s sin explicacion externa
[ ] Muerte -> control recuperado dentro del baseline del genero
[ ] Existe reintento directo sin pasar por menu
[ ] Animacion de muerte <=1.2 s y salteable
[ ] Ningun checkpoint deja mas de 30 s de contenido dominado antes del desafio
[ ] El checkpoint guarda progreso pero no penaliza recursos del intento fallido
[ ] Autosave nunca ocurre en combate ni en estado insalvable
[ ] >=2 slots de autosave rotativos + guardado manual si el juego dura >2 h
[ ] Probado matar el proceso en 5 momentos: nunca se pierde mas de una escena
[ ] La pantalla de game over tiene 1 accion por defecto ya enfocada
[ ] Coyote time e i-frames medidos y anotados, no heredados del template
[ ] Log de muerte activo: causa, posicion, intento, tiempo desde checkpoint
[ ] Ningun trigger con >25% de jugadores muriendo 6+ veces
[ ] Si hay permadeath: la run dura <=45 min y hay variacion entre runs
[ ] Si hay permadeath: >=1 desbloqueo cada 2-3 runs fallidas
[ ] El contador de muertes es ocultable
[ ] Existe modo asistido sin bloquear contenido
```

## Aplicación · Límites · Fuentes

**Aplicación (Unity, dev solo).** Centralizá el reset en un `LevelResetService` que restaure la escena por estado y no por `LoadScene`: recargar la escena es el camino fácil y el que produce los 8 segundos de espera que arruinan el bucle. Guardá el `lastDamageSource` en el componente de vida y usalo tanto para el feedback de muerte como para el log. El checkpoint conviene modelarlo como un snapshot serializable explícito (una struct con lo que guarda, según la tabla de arriba) en vez de "todo el estado": así el "qué NO guarda" es una decisión visible en el código y no un accidente. Un `deaths.csv` en `Application.persistentDataPath` alcanza como telemetría casera.

**Límites.** Este libro asume fracaso frecuente y recuperable. No cubre juegos sin estado de derrota (sandbox, walking sims), ni fracaso económico de largo plazo en estrategia y management, donde la "muerte" son 40 horas de decisiones y el modelo de checkpoint no aplica. Tampoco cubre pérdidas de progreso en multijugador competitivo, donde el costo lo fija la comunidad y no vos.

**Fuentes.** `18_Art_of_Failure` · `17_Uncertainty_in_Games` · `08_Designing_Games` · `04_Theory_of_Fun` · `07_Characteristics_of_Games` · `03_Game_Design_Workshop` · `09_Gamers_Brain`
**Cruces.** `05_Fundamentos_de_experiencia_ludica` (Pilares 2, 5, 7) · `01_Loop_de_experiencia` (el fracaso como iteración del loop) · `03_Definicion_de_terminado` (guardado robusto como criterio de cierre) · `02_Game_feel`

---

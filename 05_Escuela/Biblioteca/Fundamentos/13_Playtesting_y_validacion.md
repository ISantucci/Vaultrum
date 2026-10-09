---
tipo: fundamento
estado: En la Biblioteca
mision: EST-006_Mision_Lote_Biblioteca_Agosto26
profundiza: Proceso — validación empírica (transversal a los 9 pilares)
cruza: 05_Fundamentos_de_experiencia_ludica, 03_Definicion_de_terminado, 04_Playbook_de_diseno
---

# Fundamento 13 — Playtesting y validación

> Profundiza el playtest como instrumento de medición: cómo se diseña, se conduce, se lee y se convierte en decisiones. Cubre tipos de test, protocolo, preguntas, sesgos, telemetría para un dev solo y criterios de muerte de prototipo.
> **No cubre:** QA formal y gestión de bugs; investigación de mercado y wishlists; testeo de accesibilidad especializado; estadística inferencial más allá de umbrales prácticos.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta · 2. El modelo · 3. Baseline numérico · 4. Patrones · 5. Antipatrones · 6. Cómo se audita el propio proceso · 7. Checklist · 8. Aplicación, límites y fuentes.

## Qué es y por qué se rompe si falta
Un playtest es un **instrumento de medición**, no una búsqueda de aprobación. La diferencia es operativa: un instrumento tiene una hipótesis, una métrica y un umbral de decisión definidos **antes** de encenderlo. Si no podés escribir la frase "si pasa X, cambio Y", no estás testeando: estás mostrando el juego.

Para un dev solo esto no es un lujo de estudio grande, es la única defensa contra el sesgo estructural del trabajo en soledad: sos la única persona del planeta que ya sabe cómo se juega, qué quisiste decir y qué va a pasar en el minuto 12. Cada hora sin testers frescos te aleja un poco más del jugador real, y el alejamiento no se siente: se siente exactamente igual que tener razón.

## El modelo

**A. La ficha de test.** Una página, antes del test, siempre:

| Campo | Ejemplo |
|---|---|
| Hipótesis | "Un jugador nuevo entiende el gancho sin texto" |
| Población | Nunca jugó esta build; juega plataformeros |
| n | 5 |
| Tarea | Primeros 10 min, sin ayuda |
| Métrica | Usa el gancho voluntariamente antes del min 4 |
| Umbral | ≥ 4 de 5 |
| Si falla | Agregar demostración pasiva en la sala 2 |
| Si pasa | Cerrar el tema; no volver a testearlo hasta cambio de build |

**B. Tipos de test.**

| Tipo | Pregunta que responde | n mínimo | Duración | Build |
|---|---|---|---|---|
| Feel | ¿El verbo central se siente bien solo? | 3–5 | 10–20 min | Caja gris |
| Comprensión | ¿Se entiende sin que yo hable? | 5–8 | Primeros 15 min | UI real |
| Dificultad / balance | ¿Los números están donde creo? | 8–15 | Sesión completa | Nivel completo |
| Retención | ¿Vuelve mañana? | 15+ | 3–7 días | Build jugable en casa |
| Bugs dirigidos | ¿Se rompe si lo empujo? | 2–4 | 30–60 min | La que sea |

**Principio de escala:** los problemas de **comprensión** aparecen casi todos con 5 testers frescos; los problemas de **números** necesitan muchos más, porque la varianza de habilidad entre personas es enorme. Comprensión escala con n chico; balance escala con n grande. Y "fresco" se es **una sola vez**: llevá registro de quién vio qué build.

**C. El protocolo.**

```txt
PROTOCOLO DE SESIÓN (45–70 min según cuánto dure el juego)

 T-1 día  │ confirmar · build limpia y probada · hoja de observación impresa
 00:00    │ ENCUADRE (3 min)
          │   decir:    "no te evalúo a vos, evalúo el juego"
          │             "pensá en voz alta" · "si te trabás, trabate"
          │   NO decir: cómo se juega · qué esperás · qué cambiaste
 00:03    │ CONSENTIMIENTO + grabación (pantalla + audio; manos si es de input)
 00:05    │ JUEGO (20–40 min)          ←  VOS: CALLADO
          │   sólo dos frases permitidas:
          │     "¿qué estás pensando?"   "¿qué estás intentando hacer?"
          │   rescate SÓLO tras 3 min trabado — y anotá minuto y motivo:
          │   ese rescate ES el hallazgo, no una interrupción del hallazgo
          │   -> termina entre 00:25 y 00:45, y de ahí en más el reloj es RELATIVO
 fin+0:00 │ ENTREVISTA (10–15 min) — de abierto a cerrado, nunca al revés
 +entrev. │ CIERRE: gracias · qué sigue · todavía NO le expliques el juego
          │   arranca cuando termina la entrevista, no a una hora fija
 +1 h     │ VOLCADO: notas crudas → SÍNTOMAS. El diagnóstico, mañana.

 El tramo posterior al juego NO tiene hora fija: si la agendás a las 00:45 y el
 tester terminó a las 00:25, tenés veinte minutos de nada — y el silencio
 posterior a una sesión es donde el diseñador empieza a explicar su juego.
```

El costo real de hablar durante el test: cada intervención compra un dato falso y destruye uno real. Si tenés que intervenir, ya encontraste el bug.

**D. Preguntas prohibidas y sus reemplazos.** La tabla más útil del libro.

| Prohibida | Por qué falla | Reemplazo |
|---|---|---|
| "¿Te gustó?" | Cortesía, no dato | "Contame qué hiciste" / "¿a quién se lo recomendarías?" |
| "¿Fue difícil?" | Orgullo | "¿En qué momento pensaste que no ibas a poder?" |
| "¿Entendiste X?" | Todos dicen que sí | "Explicame X como si yo no lo conociera" |
| "¿Agregarías Y?" | Convierte al tester en diseñador | "¿Qué te faltó poder hacer?" |
| "¿La cámara estaba bien?" | Sugestión | "¿Qué viste justo antes de morir?" |
| "¿Está claro el objetivo?" | Sí automático | "¿Qué estás tratando de conseguir ahora?" |
| "¿Volverías a jugar?" | Predicción sin valor | "¿Qué fue lo último que jugaste dos días seguidos?" |
| "¿Preferís A o B?" | Preferencia declarada ≠ conducta | Testear A y B con grupos distintos y medir |
| "¿No te parece que...?" | Es tu opinión con signo de pregunta | Nada. Callate. |

**E. Observación vs. opinión.** El tester es un **sensor confiable de síntomas** y un **consultor pésimo de soluciones**. Su propuesta de solución es un dato valioso sobre el síntoma, y ninguno sobre la solución.

| Lo que dijo (dato) | Síntoma observado (dato) | Diagnóstico (tuyo) | Cambio candidato (tuyo) |
|---|---|---|---|
| "El jefe es injusto" | Murió 6 veces, 5 por el área | Falta anticipación | Wind-up de 400 ms + audio |
| "Se traba" | Repitió la pulsación 14 veces | Acuse tardío | Feedback en ≤2 frames |
| "Me perdí" | Volvió 3 veces a la misma sala | Sin hito visual | Landmark en el eje de avance |
| "Agregá un mapa" | 4 min dando vueltas | Legibilidad espacial | Landmark antes que mapa |

**F. Feedback contradictorio, en cuatro pasos.** (1) Separá por perfil: habilidad, género favorito, horas jugadas. (2) Buscá el síntoma común detrás de las quejas opuestas —"muy fácil" y "muy difícil" en el mismo encuentro suele significar "no hay lectura de la dificultad", no "el número está mal"—. (3) Ponderá por frecuencia y severidad, nunca por elocuencia: el tester más articulado no es el más representativo. (4) Si después de eso sigue partido, dejó de ser una decisión de balance y pasó a ser una decisión de **público objetivo**: elegí conscientemente a quién le estás fallando.
Umbrales prácticos: 3 de 5 con el mismo síntoma → arreglar. 1 de 8 → anotar y esperar la próxima ocurrencia. 1 de 8 pero **bloqueante** → arreglar igual.

**G. Sesgos.**

| Sesgo | Síntoma | Contramedida |
|---|---|---|
| Del amigo (complacencia) | Elogia, minimiza, "está buenísimo" | Pedile 3 cosas que rompió, no 3 que le gustaron; usalo para bugs y feel, nunca para retención |
| Del creador (maldición del conocimiento) | Explicás sin darte cuenta; ves lo que quisiste hacer | Guion escrito de encuadre; mirá la grabación 48 h después |
| De demanda | El tester intuye qué querés oír | No digas qué cambiaste desde la última build |
| De novedad | La primera hora siempre divierte | Test multi-sesión antes de creerle a la diversión |
| De supervivencia | Sólo escuchás a los que terminaron | Perseguí a los que abandonaron: es el dato más caro y más valioso |
| De recencia | El último minuto tiñe todo el recuerdo | Preguntá por momentos específicos, no por el conjunto |

**H. Telemetría mínima para un dev solo.** Regla: **un evento por pregunta de diseño**. Si no tenés la pregunta, no loguees. CSV local, id de sesión anónimo, nada de nube hasta que la necesites.

> **Este libro es el dueño del territorio de playtest.** Los otros libros del estante —`07`, `08`, `09`, `12`— proponen eventos candidatos y protocolos de observación de **su** dominio, y está bien que lo hagan: saben qué preguntar sobre economía, progresión, onboarding y pacing. Lo que no hacen es **legislar**. El n de testers, el protocolo de sesión y el tope de ≤10 eventos activos se fijan acá, y ahí se dirime cualquier diferencia. Sin este párrafo, la unión de las cuatro listas da ~23 eventos y cada libro cree estar pidiendo poco.

| Evento | Responde |
|---|---|
| `session_start` (build, plataforma, config) | ¿Con qué jugaron? |
| `level_enter` / `level_exit` + tiempo | ¿Dónde se atasca el pacing? |
| `death` (causa, posición, t desde checkpoint) | ¿Qué mata y cuánto cuesta? |
| `objective_set` / `objective_complete` | ¿Sabe qué hacer? |
| `first_use` por verbo (tiempo) | ¿Descubre las mecánicas? |
| `retry_count` por encuentro | ¿Dónde está el muro real? |
| `idle > 8 s` (posición) | ¿Dónde se confunde o se aburre? |
| `setting_changed` | ¿Qué default está mal? |
| `quit` (posición, tiempo) | ¿Dónde se cae la sesión? |

**I. Decidir qué cambiar.** Matriz frecuencia × severidad: bloqueante y frecuente → arreglar ya · bloqueante y raro → arreglar ya · fricción frecuente → backlog alto · fricción rara → anotar · preferencia (aunque sea frecuente) → no tocar salvo que contradiga la intención declarada. Dos reglas duras: **24 horas** entre el test y la decisión (nunca decidas caliente ni delante del tester) y **un cambio por hipótesis** — si cambiás cinco cosas entre dos tests, el próximo test no te dice nada.

**J. Cuándo matar un prototipo.** Escribí estos criterios el día 1, cuando todavía no estás enamorado:
- El verbo central no divierte sin contenido después de **3 iteraciones** de test de feel con testers frescos.
- En 3 rondas, **ningún** tester pidió "una más".
- Tenés que explicarlo para que sea divertido, y ya reescribiste el onboarding dos veces.
- El costo de la próxima iteración supera el presupuesto de tiempo que declaraste al empezar.
- No podés nombrar la fantasía en una frase que un tester repita, con sus palabras, después de jugar.
Ritual de cierre: post-mortem de una página, código archivado, aprendizaje registrado. Un prototipo muerto con post-mortem es una inversión; uno muerto en silencio es una pérdida.

## Baseline numérico

| Parámetro / criterio | Baseline sugerido | Por qué |
|---|---|---|
| n para test de comprensión | 5 testers frescos | Cubre la mayoría de los problemas de usabilidad |
| n para test de balance | 8–15 | La varianza de habilidad exige volumen |
| n para retención | 15+, multi-sesión | Todo lo menor es anécdota |
| Intervenciones del facilitador | ≤ 2 por sesión de 40 min | Por encima, la sesión mide tu ayuda |
| Espera antes de rescatar | 3 min trabado | El atasco corto es diseño; el largo es defecto |
| Umbral de repetición de síntoma | 3 de 5 → arreglar | Deja de ser azar |
| Espera entre test y decisión | 24 h | Evita decidir con adrenalina |
| Cambios entre dos tests | 1 hipótesis por vez | Sin esto no hay atribución |
| Cadencia en prototipo | 1 test cada 1–2 semanas | Ritmo sostenible para dev solo |
| Volcado de notas | ≤ 2 h después de la sesión | La memoria de matices se evapora |
| Eventos de telemetría iniciales | ≤ 10 | Más es data que nunca vas a mirar |
| Primer objetivo alcanzado sin ayuda | ≥ 80% de testers, en < 5 min | Umbral de onboarding aceptable |
| Completado de nivel al 1.º intento (normal) | 60–80% | Fuera de ese rango, revisá dificultad |
| Grabación de sesión | Pantalla + audio siempre | Vas a ver cosas que no viste en vivo |

## Patrones que funcionan
- **Ficha de una página antes del test.** *Costo:* 20 min de preparación por sesión. Sin ella el test es entretenimiento.
- **Think-aloud de dos frases.** *Costo:* reduce inmersión ~10%; **no sirve** para medir tensión ni pacing — para eso, silencio total y observación pura.
- **Primer contacto de 5 minutos.** Sólo los primeros 5 min, n=5, en cualquier lado. *Costo:* no dice nada de retención ni de balance.
- **A/B secuencial con grupos distintos.** *Costo:* duplica el n necesario, pero elimina el sesgo de comparación.
- **Cámara a las manos** en tests de input. *Costo:* incomoda; avisá antes.
- **Diario de tres preguntas** para retención multi-día. *Costo:* tasa de respuesta baja; pagá con algo real.
- **Backlog de síntomas, no de soluciones**, con contador de ocurrencias. *Costo:* disciplina diaria; es el hábito que más rinde.
- **Kill criteria escritos el día 1.** *Costo:* incomodidad emocional, hoy, a cambio de meses después.

## Antipatrones
| Antipatrón | Síntoma observable |
|---|---|
| Testear con gente que ya jugó | Todos "entienden"; los nuevos no |
| Hablar durante el test | En el video, cada tramo difícil tiene tu voz encima |
| Ejecutar las soluciones que propone el tester | El juego se vuelve la suma de pedidos y pierde forma |
| Testear sin hipótesis | Terminás el test sin saber qué cambiar, y de mal humor |
| Testear recién con arte final | Los hallazgos son estructurales y ya no hay presupuesto |
| Contar lo que dijeron, no lo que hicieron | Tus notas no tienen ni un timestamp |
| Cambiar 6 cosas entre tests | Mejoró y no sabés por qué; empeoró y no sabés por qué |
| Ignorar al que abandonó | Tu build parece buenísima y nadie termina el nivel 2 |
| Confundir aplauso social con validación | En la jam todos festejan; en casa nadie abre el .exe |
| 60 eventos de telemetría | Nunca abriste el CSV |

## Cómo se mide en playtest (auditar el propio proceso)
El instrumento también se calibra. Cuatro métricas sobre vos mismo, una por sesión: **tasa de intervención** (veces que hablaste por hora — objetivo ≤ 3), **% de hallazgos con síntoma observable** anotado (objetivo ≥ 80%; el resto son opiniones disfrazadas), **tiempo entre test y build corregida** (objetivo ≤ 2 semanas, o el hallazgo se enfría), y **% de cambios revertidos** después (si supera 20%, estás decidiendo con n insuficiente o sin las 24 h de espera).
Mirá la grabación de una sesión de cada cinco **completa**, con 48 h de distancia. Vas a encontrar dos cosas que no viste en vivo: una intervención tuya que creíste inocente, y un momento de duda del jugador de 6 segundos que en el momento te pareció normal.
Lo que **no** hay que preguntarse al cerrar un test: "¿salió bien?". Un test no sale bien ni mal; confirma o refuta. El único test fallido es el que no tenía hipótesis.

## CHECKLIST
```txt
PLAYTESTING Y VALIDACIÓN — pegar en el GDS / plan de producción

ANTES
[ ] Ficha de una página: hipótesis · población · n · tarea · métrica · umbral
[ ] Escrito "si falla, cambio ___" y "si pasa, cierro el tema"
[ ] Tester fresco verificado contra el registro de quién vio qué build
[ ] Build limpia, probada de punta a punta hoy · guion de encuadre impreso
[ ] Telemetría activa: ≤10 eventos, cada uno atado a una pregunta

DURANTE
[ ] Encuadre dicho, no improvisado · consentimiento y grabación
[ ] Silencio · sólo "¿qué estás pensando?" / "¿qué estás intentando?"
[ ] Rescate sólo tras 3 min trabado, con minuto y motivo anotados
[ ] Intervenciones contadas: ____ (objetivo ≤2 en 40 min)

DESPUÉS
[ ] Volcado de notas crudas dentro de las 2 h · síntomas, no diagnósticos
[ ] Entrevista de abierto a cerrado · cero preguntas de la lista prohibida
[ ] Cada hallazgo tiene un síntoma observable con timestamp
[ ] Feedback contradictorio separado por perfil antes de promediar nada
[ ] 24 h de espera antes de decidir
[ ] Matriz frecuencia × severidad aplicada · UN cambio por hipótesis
[ ] Kill criteria del prototipo revisados: ¿alguno se cumplió?
```

## Aplicación · Límites · Fuentes
**Aplicación.** Ningún requerimiento de Vaultrum se cierra en `03_Definicion_de_terminado` sin al menos un test con ficha y umbral. Los checklists de los Fundamentos 10, 11 y 12 son las hipótesis; este libro es el instrumento con el que se verifican. El backlog de síntomas vive junto al proyecto y se lleva al Core sólo cuando el aprendizaje es reutilizable.
**Límites.** No sustituye QA formal ni testeo de accesibilidad con personas con discapacidad, que requieren protocolos propios. Los umbrales son heurísticas de trabajo, no estadística: con n=5 no hay significancia, hay señal. Para decisiones de plata (precio, plataforma, alcance) esto no alcanza.
**Fuentes.** `03_Game_Design_Workshop` · `19_Playful_Production_Process` · `09_Gamers_Brain` · `10_Game_Usability` · `02_Art_of_Game_Design` · `12_Design_of_Everyday_Things` · `08_Designing_Games` · `18_Art_of_Failure` · `04_Theory_of_Fun`.
**Cruces.** `05_Fundamentos_de_experiencia_ludica` (los 9 pilares) · `03_Definicion_de_terminado` · `04_Playbook_de_diseno` · `10_Input_y_respuesta` · `11_Camara_y_encuadre` · `12_Pacing_y_estructura`.

---
tipo: fundamento
estado: En la Biblioteca
mision: EST-010_Mision_Plataformero_2D
profundiza: Pilar 3 — Feedback y game feel
cruza: 05_Fundamentos_de_experiencia_ludica, 10_Input_y_respuesta, 11_Camara_y_encuadre, 16_Audio_como_gameplay, 03_Definicion_de_terminado
---

# Fundamento 02 — Game feel / Juice

> Profundiza la mitad **saliente** del lazo: qué hace el juego con lo que el jugador apretó, y por qué una misma mecánica se siente muerta o viva según cómo conteste. Cubre las tres capas del feel, el vocabulario de efectos con sus ventanas de tiempo, la diferencia entre juice que informa y juice que decora, y cómo se mide.
> **No cubre:** la mitad entrante —latencia, perdón de input, curvas— que vive en `10_Input_y_respuesta`; la cámara, que es tan grande que tiene libro propio en `11_Camara_y_encuadre`; el diseño sonoro como sistema, en `16_Audio_como_gameplay`.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta · 2. Las tres capas · 3. El vocabulario de efectos · 4. Baseline numérico · 5. La regla que separa juice de ruido · 6. Antipatrones · 7. Cómo se mide en playtest · 8. Checklist · 9. Aplicación, límites y fuentes.

## Qué es y por qué se rompe si falta

El *game feel* es la sensación de manejar algo. No es un efecto ni una lista de efectos: es lo que queda cuando el jugador puede **predecir** el resultado de su acción antes de terminarla, y el juego **confirma** que pasó. Sin la primera mitad hay sorpresa; sin la segunda, silencio. Las dos juntas producen la ilusión de que hay un objeto del otro lado del botón.

Lo que se rompe cuando falta no es la diversión: es la **causalidad**. Un juego mudo obliga al jugador a inferir el estado del sistema desde la lógica en vez de percibirlo, y esa inferencia consume la atención que debería ir al desafío. El síntoma es siempre el mismo y siempre se confunde con otra cosa: *"está bien pero le falta algo"*. Casi nunca le falta contenido. Le falta confirmación.

Hay una asimetría que conviene tener escrita porque decide prioridades: **la falta de feel se siente como un defecto del juego; el exceso, como un defecto del jugador.** Un juego mudo se percibe barato. Un juego con demasiado juice se percibe confuso, y el jugador cree que es él el que no entiende. El segundo error es más caro de detectar.

## Las tres capas

El feel se construye en tres capas que se pueden afinar por separado. Confundirlas es el motivo por el que "agregar juice" a veces no arregla nada. `05_Game_Feel`

**Capa 1 — Respuesta.** Que el sistema conteste, y conteste rápido. Es la mitad entrante y vive en `10_Input_y_respuesta`. Sin esta capa las otras dos no se perciben: un efecto glorioso 200 ms tarde no se lee como impacto, se lee como error.

**Capa 2 — Simulación.** Cómo se mueve la cosa que se maneja: aceleración, fricción, inercia, peso. Es la capa que produce **predicción**. Un objeto con aceleración se puede anticipar; uno con velocidad binaria, no. Esta capa es la que hace que un juego se sienta bien **sin un solo efecto encima** — y por eso es la primera que hay que afinar. Un plataformero con buena simulación y cero partículas se siente sólido; uno con mala simulación y partículas hermosas se siente resbaloso y caro.

**Capa 3 — Contexto y confirmación.** El resto: animación, partículas, sonido, sacudida, pausa de impacto, reacción del entorno. Es la capa que produce **contundencia**, y es la única que se puede agregar al final sin rehacer nada.

```txt
capa 1  respuesta     el sistema contesta        -> agencia
capa 2  simulacion    se puede anticipar         -> control
capa 3  confirmacion  se percibe que paso        -> contundencia
```

La regla de orden es dura: **no se compra contundencia con capa 3 lo que falta en capa 2.** Es el error más común y el más caro, porque la capa 3 es la barata de agregar y la que se ve en un video.

## El vocabulario de efectos

Cada efecto es una **oración** sobre el estado del sistema. Si no dice nada nuevo, es ruido.

| Efecto | Qué afirma | Ventana típica |
|--------|-----------|----------------|
| **Squash / stretch** | hubo impacto y tiene peso | 60–120 ms |
| **Anticipación** (frames antes de la acción) | esto va a pasar | 40–100 ms |
| **Hitstop / freeze frame** | el impacto fue fuerte | 2–6 frames (33–100 ms) |
| **Screenshake** | pasó algo grande, y a todo, no solo a vos | 100–250 ms, amplitud decreciente |
| **Partículas** | hubo contacto, acá | 3–10 partículas, 200–500 ms |
| **Flash / tinte** | este objeto es el que recibió | 50–150 ms |
| **Knockback** | hubo transferencia de fuerza | proporcional al daño |
| **Trail** | esto va rápido, y por acá | mientras dure la velocidad |
| **Sonido de impacto** | pasó, ahora | ataque < 20 ms |
| **Pitch variable en sonido repetido** | esto es otro evento, no el mismo | ±5–15% |
| **Pausa antes de la recompensa** | lo que viene importa | 150–400 ms |

**Los tres eventos que siempre necesitan efecto propio**, en cualquier género: el que el jugador causa más veces, el que le cuesta algo, y el que le da algo. Si esos tres suenan igual, el juego se siente plano por más efectos que tenga.

## Baseline numérico

Punto de partida, no dogma. Todo lo de abajo se afina jugando.

| Parámetro | Baseline | Por qué |
|-----------|----------|---------|
| Respuesta visible al input | ≤ 100 ms, ideal ≤ 50 ms | Arriba de 100 ms el jugador percibe demora aunque no sepa nombrarla. `10_Input_y_respuesta` |
| Duración de un efecto de confirmación | 60–150 ms | Debajo no se percibe; arriba se lee como lag |
| Hitstop en evento frecuente | 0–2 frames | En algo que pasa cada segundo, 5 frames es lag |
| Hitstop en evento raro y grande | 4–8 frames | Acá sí paga |
| Screenshake, amplitud | ≤ 1–2% del alto de pantalla | Más marea y tapa información |
| Screenshake, frecuencia de uso | eventos raros | Al saltar o al caminar se vuelve ruido. `59_The_Art_of_Screenshake` |
| Variación de pitch en sonido repetido | ±5–15% | Sin esto, diez repeticiones se vuelven una sola |
| Ataque del sonido de impacto | < 20 ms | Un ataque lento se percibe como retraso aunque el sonido arranque a tiempo |
| Curva de aceleración del avatar | llegar al 90% en 0.1–0.2 s | Peso sin patinaje. Capa 2 |
| Frenado | 0.08–0.15 s | Más largo se siente sobre hielo |

## La regla que separa juice de ruido

Una sola, y decide todos los casos dudosos:

> **Un efecto que no cambia lo que el jugador sabe, es ruido — y si además tapa algo, es un defecto.**

De ahí salen tres pruebas prácticas:

1. **La prueba de la oración.** Escribí en una línea qué afirma el efecto. Si no se puede, o si otro efecto ya lo afirma, sobra.
2. **La prueba de la oclusión.** ¿Tapa el objeto que el jugador necesita seguir mirando? En Pong, la pelota. En un plataformero, el próximo apoyo. En un shooter, el enemigo. Si lo tapa, no importa cuánto guste: se recorta.
3. **La prueba de la repetición.** Multiplicá el efecto por las veces que pasa en un minuto de juego real. Un hitstop precioso en algo que pasa 40 veces por minuto son 4 segundos de juego congelado por minuto.

La 3 es la que más rinde y la que casi nunca se hace, porque el juice se prueba de a un evento y se sufre en serie. `60_Juice_It_or_Lose_It`

## Antipatrones

- **Juice sobre simulación rota.** Agregar capa 3 a un movimiento que no se puede anticipar. Se siente caro y sigue sin controlarse.
- **El mismo efecto para todo.** Un solo sonido de impacto para golpear, recibir y recoger convierte tres eventos en cero información.
- **Screenshake como sinónimo de importante.** Se agota: si todo sacude, nada sacude.
- **Efecto sin límite superior.** Diez enemigos muriendo juntos disparan diez screenshakes sumados. Todo efecto acumulable necesita techo.
- **Juice que se come el frame budget.** Partículas por evento sin pool, en un juego que ya va justo. Es exactamente `Cuando NO optimizar` al revés: acá el costo sí tiene requerimiento detrás, y hay que medirlo.
- **Confirmar el input en vez del resultado.** Un efecto al apretar el botón, no al pasar la cosa. Enseña al jugador que apretar es suficiente.

## Cómo se mide en playtest

El feel es subjetivo y la medición no tiene por qué serlo.

- **Sin audio.** Jugar en silencio. Lo que se vuelve ilegible es lo que estaba sostenido solo por el sonido — y eso es una falla de accesibilidad, no un logro.
- **Sin capa 3.** Apagar partículas, shake y hitstop. Si el juego se vuelve incontrolable, el problema estaba en capa 2 y el juice lo estaba tapando.
- **La pregunta de las tres.** Después de un minuto: *¿qué está pasando? ¿qué podés hacer? ¿cómo vas?* Si alguna no se contesta, falta información, no efectos.
- **Video a 1/4 de velocidad.** Los efectos que se pisan entre sí sólo se ven acá.
- **Contar eventos por minuto.** El insumo de la prueba de la repetición.

## CHECKLIST

```txt
CAPA 1 — RESPUESTA
[ ] El sistema contesta a todo input, siempre, en menos de 100 ms
[ ] Ninguna acción del jugador queda sin respuesta perceptible

CAPA 2 — SIMULACION
[ ] Puedo anticipar donde va a terminar lo que estoy moviendo
[ ] Lo que manejo tiene peso: acelera y frena, no se prende y apaga
[ ] Apagando todos los efectos, el juego sigue siendo controlable

CAPA 3 — CONFIRMACION
[ ] Los tres eventos clave (el frecuente, el que cuesta, el que da) suenan y se ven distinto entre si
[ ] Ningun efecto tapa lo que tengo que seguir mirando
[ ] Ningun efecto acumulable puede sumarse sin techo
[ ] Los sonidos repetidos varian, no se vuelven uno solo

COSTO
[ ] Multiplicado por su frecuencia real, ningun efecto come tiempo de juego
[ ] El juice no baja el frame rate por debajo del objetivo declarado
```

## Aplicación · Límites · Fuentes

**Aplicación.** Game Design lo cruza al escribir la sección de feedback de un `GDS`; UI/UX lo consulta al decidir cuánta señal entra por el canal visual; Programación lo lee antes de resolver el movimiento del avatar, porque la capa 2 es una decisión técnica con consecuencia de diseño. Un `GDS` que dice *"que se sienta bien"* sin nombrar capa, efecto y ventana no declaró nada.

**Límites.** No cubre cámara (`11_Camara_y_encuadre`), input (`10_Input_y_respuesta`) ni audio como sistema (`16_Audio_como_gameplay`). No cubre animación como oficio: acá está qué tiene que comunicar, no cómo se anima. Y el baseline numérico está pensado para juegos de acción en tiempo real; un juego por turnos usa las mismas tres capas con otras ventanas.

**Fuentes.** `05_Game_Feel` (el marco de las tres capas), `59_The_Art_of_Screenshake`, `60_Juice_It_or_Lose_It`, `61_Juicing_Your_Cameras_With_Math`, `09_Gamers_Brain` (percepción y atención), `39_Game_Sound`, `11_How_Games_Move_Us`, `34_Celeste_codigo_fuente_del_juego_y_del_prototipo_PICO`.

**Nota de origen.** Este libro estuvo **Reservado** desde que se creó el estante: era el fundamento más citado de la Biblioteca —veinte archivos lo nombran— y estaba vacío. Lo detectó `EST-009` leyendo la bibliografía en vez del índice, y lo cerró `EST-010`, que lo necesitaba como insumo para el libro de plataformero. Es el caso testigo de la regla: **un hueco en una biblioteca no está donde falta un tema, está donde algo muy citado no tiene nada debajo.**

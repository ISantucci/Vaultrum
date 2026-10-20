---
tipo: fundamento
estado: En la Biblioteca
mision: EST-010_Mision_Plataformero_2D
actualizado: EST-023_Mision_Swink_Game_Feel
profundiza: Pilar 3 — Feedback y game feel
cruza: 05_Fundamentos_de_experiencia_ludica, 10_Input_y_respuesta, 11_Camara_y_encuadre, 16_Audio_como_gameplay, 03_Definicion_de_terminado
---

# Fundamento 02 — Game feel / Juice

> Profundiza la mitad **saliente** del lazo: qué hace el juego con lo que el jugador apretó, y por qué una misma mecánica se siente muerta o viva según cómo conteste. Cubre las tres capas del feel y el modelo de Swink del que salen —tres bloques, seis componentes, umbrales de percepción y el sobre de respuesta—, el vocabulario de efectos con sus ventanas de tiempo, la diferencia entre juice que informa y juice que decora, cómo se mide, y los ocho principios del capítulo 17 de Swink.
> **No cubre:** la mitad entrante —latencia, perdón de input, curvas— que vive en `10_Input_y_respuesta`; la cámara, que es tan grande que tiene libro propio en `11_Camara_y_encuadre`; el diseño sonoro como sistema, en `16_Audio_como_gameplay`.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta · 2. Las tres capas · 3. Los seis componentes de Swink · 4. Los umbrales de percepción · 5. El sobre de respuesta · 6. El vocabulario de efectos · 7. Baseline numérico · 8. La regla que separa juice de ruido · 9. Antipatrones · 10. Cómo se mide en playtest · 11. Los ocho principios · 12. Checklist · 13. Aplicación, límites y fuentes.

## Qué es y por qué se rompe si falta

El *game feel* es la sensación de manejar algo. No es un efecto ni una lista de efectos: es lo que queda cuando el jugador puede **predecir** el resultado de su acción antes de terminarla, y el juego **confirma** que pasó. Sin la primera mitad hay sorpresa; sin la segunda, silencio. Las dos juntas producen la ilusión de que hay un objeto del otro lado del botón.

Lo que se rompe cuando falta no es la diversión: es la **causalidad**. Un juego mudo obliga al jugador a inferir el estado del sistema desde la lógica en vez de percibirlo, y esa inferencia consume la atención que debería ir al desafío. El síntoma es siempre el mismo y siempre se confunde con otra cosa: *"está bien pero le falta algo"*. Casi nunca le falta contenido. Le falta confirmación.

Hay una asimetría que conviene tener escrita porque decide prioridades: **la falta de feel se siente como un defecto del juego; el exceso, como un defecto del jugador.** Un juego mudo se percibe barato. Un juego con demasiado juice se percibe confuso, y el jugador cree que es él el que no entiende. El segundo error es más caro de detectar.

## Las tres capas

El feel se construye en tres capas que se pueden afinar por separado. Confundirlas es el motivo por el que "agregar juice" a veces no arregla nada. Son una lectura propia de los tres bloques de Swink —tiempo real, espacio simulado, pulido—, no un término suyo. `05_Game_Feel`

**Capa 1 — Respuesta.** Que el sistema conteste, y conteste rápido. Es la mitad entrante y vive en `10_Input_y_respuesta`. Sin esta capa las otras dos no se perciben: un efecto glorioso 200 ms tarde no se lee como impacto, se lee como error.

**Capa 2 — Simulación.** Cómo se mueve la cosa que se maneja: aceleración, fricción, inercia, peso. Es la capa que produce **predicción**. Un objeto con aceleración se puede anticipar; uno con velocidad binaria, no. Esta capa es la que hace que un juego se sienta bien **sin un solo efecto encima** — y por eso es la primera que hay que afinar. Un plataformero con buena simulación y cero partículas se siente sólido; uno con mala simulación y partículas hermosas se siente resbaloso y caro.

**Capa 3 — Pulido y confirmación.** El resto: animación, partículas, sonido, sacudida, pausa de impacto, reacción del entorno. Es la capa que produce **contundencia**, y es la única que se puede agregar al final sin rehacer nada.

```txt
capa 1  respuesta     el sistema contesta        -> agencia
capa 2  simulacion    se puede anticipar         -> control
capa 3  pulido        se percibe que paso        -> contundencia
```

La regla de orden es dura: **no se compra contundencia con capa 3 lo que falta en capa 2.** Es el error más común y el más caro, porque la capa 3 es la barata de agregar y la que se ve en un video.

## Los seis componentes de Swink

Las tres capas son la lectura operativa; el modelo de origen es más ancho. Swink define el game feel como **control en tiempo real** de objetos virtuales en un **espacio simulado**, con las interacciones **enfatizadas por pulido**. Son tres bloques y tienen que estar los tres: sin tiempo real hay otra sensación —la del turno—, sin espacio simulado no hay nada que tocar, y sin pulido no hay confirmación. `05_Game_Feel`

Encima de los bloques, seis componentes que se afinan y se miden por separado:

```txt
componente   que es                                       donde se trabaja
input        el dispositivo y como expresa la intencion   10_Input_y_respuesta
respuesta    como el sistema procesa y contesta           capa 1 en 10_Input · capa 2 aca
contexto     el espacio que le da sentido al movimiento   Level Design · 11_Camara_y_encuadre
pulido       animacion, sonido y efectos                  capa 3 · 16_Audio_como_gameplay
metafora     lo que el jugador cree que esta moviendo     aca abajo
reglas       lo que esta en juego cuando se mueve         aca abajo
```

**Metáfora.** Lo que el objeto representa fija qué física espera el jugador antes de tocar el control. Un auto que frena como una nave se siente roto aunque frene perfecto; el mismo frenado en una nave se siente bien. Swink la gradúa en tres: **real, icónica, abstracta**. Cuanto más real la metáfora, más angosta la franja de comportamientos que el jugador acepta; un cuadrado puede moverse casi de cualquier forma. La metáfora no se elige al final: fija los parámetros de la capa 2. Un `GDS` que dice *"un caballo"* ya declaró una inercia. *(Los tres grados son de Swink; la lectura de la franja que se angosta es de Vaultrum.)*

**Reglas.** Lo que está en juego cuando el objeto se mueve. El mismo salto se siente distinto si caer cuesta una vida, si hay un reloj o si tocar a un enemigo resta. Swink las lee en tres alturas: **altas** (los objetivos de largo plazo), **medias** (los de un tramo o un encuentro) y **bajas** (las que cambian el movimiento de un momento a otro: daño, estados, invulnerabilidad). Las bajas son las que más tocan el feel y las que un `GDS` más seguido deja implícitas. *(Las tres alturas son de Swink; los ejemplos son de Vaultrum.)*

**Tres dominios.** La práctica posterior a Swink ordena el oficio en tres verbos, y cada uno cae en una capa: **tuning** de la fisicalidad (capa 2), **juicing** de la amplificación (capa 3) y **streamlining** del soporte —interpretar el input como lo que el jugador quiso hacer: coyote time, buffer, asistencia— (capa 1, con el perdón de `10_Input_y_respuesta`). El tercero es el que más se olvida: un `GDS` que declara física y efectos pero no declara qué perdona el input dejó uno de los tres dominios sin diseñar. `69_Designing_Game_Feel_Survey`

## Los umbrales de percepción

Las ventanas de este libro no son gusto. Salen de cuánto tarda una persona en percibir, decidir y moverse: el procesador humano tiene un ciclo de percepción de ~100 ms, uno de cognición de ~70 ms y uno motor de ~70 ms, y un lazo completo de corrección —ver, decidir, corregir— de **~240 ms**. Sobre eso Swink fija tres condiciones para que exista el control en tiempo real. `05_Game_Feel` · `70_Measuring_Game_Feel_Acceleration`

```txt
condicion                     umbral                       si se rompe
impresion de movimiento       mas de 10 cuadros/segundo    se ven fotos, no movimiento
respuesta instantanea         menos de 100 ms              100-240 ms: se siente pesada
continuidad de la respuesta   el lazo de ~240 ms           mas alla deja de sentirse control
                                                           y pasa a sentirse orden-y-espera
```

Y una consecuencia que decide cuándo se dispara cada efecto: dos estímulos dentro del mismo ciclo de percepción se funden, y el primero se lee como **causa** del segundo. Un efecto que llega dentro de los ~100 ms de su evento se percibe como su consecuencia; uno que llega después se percibe como otro evento.

La relación con el resto de la Biblioteca, escrita como relación y no como número suelto:

```txt
10_Input_y_respuesta   acuse en 2 frames y tope de 65 ms para la cadena. No contradice los
                       100 ms: Swink marca donde deja de existir el control; 10 marca como lo
                       juzga un jugador de accion, que ya siente pesado 60-100 ms. En accion
                       manda 10, y 100 ms es el borde, nunca el objetivo
inicio de un efecto    dentro de ~100 ms del evento que confirma: ahi se lee como su
                       consecuencia. Cuanto DURA cada efecto es otra cosa: la tabla de abajo
t_reaccion de 11       los ~250 ms de 11_Camara_y_encuadre son este lazo redondeado (ver,
                       decidir, arrancar); la maniobra de escape se suma aparte
aviso de un enemigo    parte del lazo de correccion: dura al menos lo que el jugador tarda en
                       ver, decidir y moverse (Anticipacion, en el Core)
```

## El sobre de respuesta

La capa 2 tiene vocabulario propio. Swink toma de la síntesis de sonido el **sobre ADSR** y lo aplica a la velocidad del avatar en el tiempo. `05_Game_Feel`

```txt
A  ataque        cuanto tarda en llegar a la velocidad maxima   -> aceleracion
D  decaimiento   si cae de un pico a una velocidad de crucero    -> en un avatar suele sobrar
S  sostenido     la velocidad mientras dura el input             -> velocidad maxima
R  liberacion    cuanto tarda en frenar al soltar                -> frenado
```

Con eso, *"se siente resbaloso"* deja de ser una opinión y pasa a ser un parámetro. **Un sobre corto se siente ajustado y responsivo; uno largo, suelto y fluido** —flotante si lo largo es el ataque, sobre hielo si es la liberación—. No hay uno correcto: la metáfora elige cuál se espera.

Medido con 274 jugadores en un plataformero 2D, las dos mitades del sobre no pesan igual: la sensación **flotante** la produce sobre todo un ataque largo (más de 1 s), la que los jugadores llamaron **rígida**, una liberación larga, y la respuesta se sigue percibiendo alta con un ataque más largo **mientras la liberación ronde 0.25 s o menos**. La liberación decide cuán responsivo se siente el control; el ataque, cuán flotante. Por eso el baseline le da al frenado una ventana propia y más corta. `70_Measuring_Game_Feel_Acceleration`

## El vocabulario de efectos

Cada efecto es una **oración** sobre el estado del sistema. Si no dice nada nuevo, es ruido.

| Efecto | Qué afirma | Ventana típica |
|--------|-----------|----------------|
| **Squash / stretch** | hubo impacto y tiene peso | 60–120 ms |
| **Anticipación** (frames antes de la acción) | esto va a pasar | acción propia: 0–2 frames (`02 - Anticipacion`, en el Core) · aviso de un enemigo: al menos el lazo de ~240 ms (`11_Camara_y_encuadre`) |
| **Hitstop / freeze frame** | el impacto fue fuerte | 0–8 frames según la frecuencia del evento (ver el baseline) |
| **Screenshake** | pasó algo grande, y a todo, no solo a vos | la duración la dan el trauma y el decay de `11_Camara_y_encuadre` |
| **Partículas** | hubo contacto, acá | 3–10 partículas, 200–500 ms |
| **Flash / tinte** | este objeto es el que recibió | 50–150 ms |
| **Knockback** | hubo transferencia de fuerza | proporcional al daño |
| **Trail** | esto va rápido, y por acá | mientras dure la velocidad |
| **Sonido de impacto** | pasó, ahora | ataque < 20 ms |
| **Pitch variable en sonido repetido** | esto es otro evento, no el mismo | ±5–15% |
| **Pausa antes de la recompensa** | lo que viene importa | 150–400 ms, con el acuse ya dado: va entre la confirmación y la recompensa, nunca entre el input y la confirmación |

**Los tres eventos que siempre necesitan efecto propio**, en cualquier género: el que el jugador causa más veces, el que le cuesta algo, y el que le da algo. Si esos tres suenan igual, el juego se siente plano por más efectos que tenga.

## Baseline numérico

Punto de partida, no dogma. Todo lo de abajo se afina jugando.

| Parámetro | Baseline | Por qué |
|-----------|----------|---------|
| Latencia del input (acción) | acuse ≤ 2 frames; cadena total ≤ 65 ms, ideal ≤ 50 ms | El dueño del número es `10_Input_y_respuesta`. Los 100 ms de Swink son el borde de la percepción, nunca el objetivo |
| Inicio de un efecto de confirmación | dentro de ~100 ms del evento | Dentro del ciclo de percepción se lee como consecuencia; después, como otro evento. La duración la da la tabla de efectos |
| Hitstop en evento frecuente | 0–2 frames | En algo que pasa cada segundo, 5 frames es lag |
| Hitstop en evento raro y grande | 4–8 frames | Acá sí paga |
| Screenshake, amplitud | la tabla de `11_Camara_y_encuadre`: liviano 0.2–0.4% · pesado 0.8–1.5% · excepcional 2–3%; techo duro 3% | Con el modelo de trauma no se fija la amplitud por evento: se declara cuánto trauma suma cada uno. Más marea y tapa información |
| Screenshake, frecuencia de uso | eventos raros; en uno frecuente, sólo la fila liviana de `11_Camara_y_encuadre` o nada | Al saltar o al caminar se vuelve ruido. `59_The_Art_of_Screenshake` |
| Variación de pitch en sonido repetido | ±5–15% | Sin esto, diez repeticiones se vuelven una sola |
| Ataque del sonido de impacto | < 20 ms | Un ataque lento se percibe como retraso aunque el sonido arranque a tiempo |
| Ataque del avatar (A del sobre) | llegar al 90% en 0.1–0.2 s | Peso sin patinaje. Un ataque de más de 1 s se percibe flotante (`70_Measuring_Game_Feel_Acceleration`). Capa 2 |
| Liberación del avatar (R del sobre) | hasta detenerse en 0.08–0.15 s, con la curva declarada | Más largo se siente sobre hielo. Es la perilla que más mueve la sensación de respuesta: se sostiene alta mientras ronde 0.25 s o menos (`70_Measuring_Game_Feel_Acceleration`) |

## La regla que separa juice de ruido

Una sola, y decide todos los casos dudosos:

> **Un efecto que no cambia lo que el jugador sabe, es ruido — y si además tapa algo, es un defecto.**

De ahí salen tres pruebas prácticas:

1. **La prueba de la oración.** Escribí en una línea qué afirma el efecto. Si no se puede, o si otro efecto ya lo afirma, sobra.
2. **La prueba de la oclusión.** ¿Tapa el objeto que el jugador necesita seguir mirando? En Pong, la pelota. En un plataformero, el próximo apoyo. En un shooter, el enemigo. Si lo tapa, no importa cuánto guste: se recorta.
3. **La prueba de la repetición.** Multiplicá el efecto por las veces que pasa en un minuto de juego real. Un hitstop precioso de 6 frames (100 ms) en algo que pasa 40 veces por minuto son 4 segundos de juego congelado por minuto.

La 3 es la que más rinde y la que casi nunca se hace, porque el juice se prueba de a un evento y se sufre en serie. `60_Juice_It_or_Lose_It`

## Antipatrones

- **Juice sobre simulación rota.** Agregar capa 3 a un movimiento que no se puede anticipar. Se siente caro y sigue sin controlarse.
- **El mismo efecto para todo.** Un solo sonido de impacto para golpear, recibir y recoger convierte tres eventos en cero información.
- **Screenshake como sinónimo de importante.** Se agota: si todo sacude, nada sacude.
- **Efecto sin límite superior.** Diez enemigos muriendo juntos disparan diez screenshakes sumados. Todo efecto acumulable necesita techo.
- **Juice que se come el frame budget.** Partículas por evento sin pool, en un juego que ya va justo. Es exactamente `Cuando NO optimizar` al revés: acá el costo sí tiene requerimiento detrás, y hay que medirlo.
- **Confirmar sólo el input.** El acuse al apretar es obligatorio (`10_Input_y_respuesta`: ≤ 2 frames), pero el efecto de impacto va cuando pasa la cosa. Un juego que confirma todo al apretar le enseña al jugador que apretar es suficiente.

## Cómo se mide en playtest

El feel es subjetivo y la medición no tiene por qué serlo.

- **Sin audio.** Jugar en silencio. Lo que se vuelve ilegible es lo que estaba sostenido solo por el sonido — y eso es una falla de accesibilidad, no un logro.
- **Sin capa 3.** Apagar partículas, shake y hitstop. Si el juego se vuelve incontrolable, el problema estaba en capa 2 y el juice lo estaba tapando.
- **La pregunta de las tres.** Después de un minuto: *¿qué está pasando? ¿qué podés hacer? ¿cómo vas?* Si alguna no se contesta, falta información, no efectos.
- **Video a 1/4 de velocidad.** Los efectos que se pisan entre sí sólo se ven acá.
- **Contar eventos por minuto.** El insumo de la prueba de la repetición.
- **Atar cada impresión a un número.** Es el método de Swink —métricas blandas contra métricas duras—: si el playtest dice *flotante*, se mide el ataque antes de tocar nada; si dice *rígido*, *resbaloso* o *sobre hielo*, la liberación; si dice *pesado*, primero la latencia medida (`10_Input_y_respuesta`) y después el ataque. Un adjetivo sin su parámetro no se puede afinar. `05_Game_Feel`
- **Leer los números del juego de referencia.** Antes de afinar, medir las métricas duras del juego al que el proyecto se quiere parecer. `58_Sonic_Physics_Guide` es el caso de un feel escrito entero en números; por su licencia sirve para calibrar el orden de magnitud, nunca para copiar valores.

## Los ocho principios

En el capítulo 17, Swink resume el libro en ocho principios. Son la fuente de los principios de game feel del Core, que los reescriben como regla de Vaultrum cruzados con la evidencia de los proyectos: acá van con la lectura de Swink. `05_Game_Feel`

```txt
principio                 lectura
resultados predecibles    el mismo input da un resultado que se puede anticipar. Mapeos
                          antinaturales, movimiento demasiado rapido o estados que se pisan
                          lo vuelven azar
respuesta instantanea     la respuesta llega antes del umbral de 100 ms
facil pero profundo       piso bajo y techo alto: se entiende enseguida y se domina tarde.
                          La sensibilidad del input y la de la respuesta dan la profundidad
novedad                   el mismo input no da exactamente lo mismo, para que la repeticion
                          no canse; la variacion queda debajo de lo que se lee como azar
respuesta atractiva       moverse es lindo aun en un cuarto vacio, sin contexto ni objetivo.
                          Y fallar tambien: es donde el jugador pasa mucho tiempo
movimiento organico       curvas, no saltos de valor: el movimiento acelera, frena y se asienta
armonia                   input, simulacion, pulido, metafora y reglas dicen lo mismo
pertenencia               el resultado es del jugador: lo explica su habilidad, no el sistema
```

**Verificación parcial declarada.** Los ocho títulos salen del índice del libro. Las lecturas de resultados predecibles, fácil pero profundo, novedad y respuesta atractiva salen del artículo de 2006 en el que Swink los adelantó; la de respuesta instantánea, de los umbrales. **Movimiento orgánico, armonía y pertenencia son destilación propia**, sin el capítulo a la vista. El detalle está en la ficha `05_Game_Feel`.

## CHECKLIST

```txt
CAPA 1 — RESPUESTA
[ ] Todo input tiene acuse en <= 2 frames y la cadena entra en el tope de su genero (10_Input)
[ ] Ninguna acción del jugador queda sin respuesta perceptible
[ ] Lo que el input perdona (coyote, buffer, asistencia) esta declarado: es el dominio de soporte
[ ] Durante un hitstop el input se sigue leyendo y entra al buffer: el congelado no consume la ventana

CAPA 2 — SIMULACION
[ ] Puedo anticipar donde va a terminar lo que estoy moviendo
[ ] Lo que manejo tiene peso: acelera y frena, no se prende y apaga
[ ] Apagando todos los efectos, el juego sigue siendo controlable
[ ] El sobre del avatar (ataque, sostenido, liberacion) esta declarado en numeros, no en adjetivos

CAPA 3 — PULIDO (CONFIRMACION)
[ ] Los tres eventos clave (el frecuente, el que cuesta, el que da) suenan y se ven distinto entre si
[ ] Ningun efecto tapa lo que tengo que seguir mirando
[ ] Ningun efecto acumulable puede sumarse sin techo
[ ] Los sonidos repetidos varian, no se vuelven uno solo

METAFORA Y REGLAS
[ ] La metafora esta declarada (real / iconica / abstracta) y la capa 2 se comporta como ella promete
[ ] Las reglas bajas que cambian el movimiento (dano, estados, invulnerabilidad) estan escritas
[ ] Input, simulacion, pulido, metafora y reglas dicen lo mismo: ninguno contradice a otro

COSTO
[ ] El tiempo congelado por minuto (hitstop x eventos por minuto) esta declarado en el GDS y queda bajo el techo que el GDS fija
[ ] El juice no baja el frame rate por debajo del objetivo declarado
```

## Aplicación · Límites · Fuentes

**Aplicación.** Game Design lo cruza al escribir la sección de feedback de un `GDS`; UI/UX lo consulta al decidir cuánta señal entra por el canal visual; Programación lo lee antes de resolver el movimiento del avatar, porque la capa 2 es una decisión técnica con consecuencia de diseño. Un `GDS` que dice *"que se sienta bien"* sin nombrar capa, efecto y ventana no declaró nada. Los principios que salen de este libro viven como regla en el Core, en `Principios de game feel`; este libro es su cómo, y el Core no lo copia.

**Límites.** No cubre cámara (`11_Camara_y_encuadre`), input (`10_Input_y_respuesta`) ni audio como sistema (`16_Audio_como_gameplay`). No cubre animación como oficio: acá está qué tiene que comunicar, no cómo se anima. Y el baseline numérico está pensado para juegos de acción en tiempo real; un juego por turnos no tiene control en tiempo real en el sentido de Swink: usa las capas 1 y 3 con otras ventanas, y no tiene capa 2. Los frames de este libro son a 60 fps; a otro framerate manda el valor en ms. El libro de Swink no se leyó entero en `EST-023`: qué se verificó contra qué está en la ficha `05_Game_Feel`, y tres de los ocho principios quedan como destilación propia hasta confrontarlos con el capítulo.

**Fuentes.** `05_Game_Feel` (los tres bloques de los que salen las tres capas, los seis componentes, los umbrales, el sobre ADSR y los ocho principios), `69_Designing_Game_Feel_Survey` (los tres dominios), `70_Measuring_Game_Feel_Acceleration` (el sobre medido con jugadores), `58_Sonic_Physics_Guide` (un feel escrito en números, para calibrar), `59_The_Art_of_Screenshake`, `60_Juice_It_or_Lose_It`, `61_Juicing_Your_Cameras_With_Math`, `09_Gamers_Brain` (percepción y atención), `39_Game_Sound`, `11_How_Games_Move_Us`, `34_Celeste_codigo_fuente_del_juego_y_del_prototipo_PICO`.

**Nota de origen.** Este libro estuvo **Reservado** desde que se creó el estante: era el fundamento más citado de la Biblioteca —veinte archivos lo nombran— y estaba vacío. Lo detectó `EST-009` leyendo la bibliografía en vez del índice, y lo cerró `EST-010`, que lo necesitaba como insumo para el libro de plataformero. Es el caso testigo de la regla: **un hueco en una biblioteca no está donde falta un tema, está donde algo muy citado no tiene nada debajo.**

**Actualización `EST-023`.** El libro se había escrito con el marco de Swink sin destilarlo: usaba cuatro de sus seis componentes y ninguno de sus umbrales. La misión lo completó y reparó las contradicciones que tenía con sus vecinos: con `11_Camara_y_encuadre` en la amplitud, la duración y la frecuencia del screenshake y en el hitstop, y con `10_Input_y_respuesta` en el acuse y el tope de latencia. Las encontró un validador independiente; ninguna la veía `--verificar`. Es el mismo caso testigo un nivel más abajo: **una fuente citada como marco no queda destilada por haber sido citada.**

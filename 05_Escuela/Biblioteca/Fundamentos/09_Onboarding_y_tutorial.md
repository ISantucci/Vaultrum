---
tipo: fundamento
estado: En la Biblioteca
mision: EST-006_Mision_Lote_Biblioteca_Agosto26
profundiza: Pilares 4 y 6 — Claridad/legibilidad y Dificultad/tensión
cruza: 05_Fundamentos_de_experiencia_ludica, 04_Playbook_de_diseno, 06_Dificultad_y_curva, 02_Game_feel
---

# Fundamento 09 — Onboarding y tutorial

> Este libro profundiza los **Pilares 4 y 6** de `05_Fundamentos_de_experiencia_ludica`. El baseline (que se entienda qué hacer, que el HUD sea legible, que la curva arranque suave) ya está ahí. Acá va lo que el pilar deja afuera: **enseñar como diseño de niveles**, el presupuesto de atención de los primeros 60 s / 5 min / 30 min, qué se puede asumir del vocabulario del género, el costo real de cada popup, y cómo testear un onboarding sin contaminarlo.
> Lo que NO cubre: el diseño del HUD y la jerarquía visual (UI/UX), la curva completa del juego (vive en `06_Dificultad_y_curva`), la respuesta táctil de los controles (vive en `02_Game_feel`).
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta
2. El modelo — enseñar es diseño de niveles
3. Baseline numérico
4. Patrones que funcionan
5. Antipatrones
6. Cómo se mide en playtest
7. CHECKLIST
8. Aplicación
9. Límites
10. Fuentes

## Qué es y por qué se rompe si falta
El onboarding es el tramo donde el jugador decide si tu juego vale su tiempo, y todavía no invirtió nada — así que el costo de irse es cero. Es el único tramo del juego donde competís contra el botón de cerrar. Si falta o está mal: el jugador no entiende el objetivo (abandona en 2 min), entiende pero no sabe operar (culpa a los controles), u opera pero no sabe por qué (juega sin intención y se aburre).

Y hay un fracaso silencioso, peor que el abandono: el jugador **atraviesa** el tutorial sin aprender. Aprieta lo que le señalan, la barra avanza, llega al juego y no sabe nada. El tutorial cumplió su trámite y no hizo su trabajo.

## El modelo — enseñar es diseño de niveles

La tesis central: **un buen tutorial no explica, construye una situación donde la respuesta correcta es la única evidente y el error es barato.** El texto es la última herramienta, no la primera.

Jerarquía de medios de enseñanza, del más barato al más caro para el jugador:

| Nivel | Medio | Cómo enseña | Costo cognitivo | Cuándo |
|---|---|---|---|---|
| 1 | **Affordance** | La forma dice la función (la saliente se agarra, lo rojo daña) | Casi nulo | Siempre que se pueda |
| 2 | **Restricción** | El espacio sólo permite la acción correcta | Nulo | Presentación de mecánicas |
| 3 | **Demostración** | Un NPC/enemigo hace lo que vos vas a hacer | Bajo | Mecánicas complejas |
| 4 | **Consecuencia barata** | Probás, fallás, entendés, reintentás en 2 s | Bajo, y se retiene mejor | Ejecución y timing |
| 5 | **Ícono / diegético** | Un símbolo en el mundo | Medio (hay que aprenderlo) | Convenciones y estados |
| 6 | **Prompt contextual** | "Mantené [E]" aparece en el momento justo | Medio | Inputs no adivinables |
| 7 | **Popup / texto** | Se detiene el juego y se lee | Alto | Último recurso |

```txt
       ENSEÑAR            PRACTICAR EN SEGURIDAD          EXAMINAR BAJO PRESIÓN
   ┌────────────────┐    ┌──────────────────────┐    ┌────────────────────────┐
   │ Mecánica sola  │    │ 3-5 usos, variación  │    │ Con costo real, tiempo │
   │ Espacio cerrado│───>│ menor, sin castigo   │───>│ o recursos en juego    │
   │ Error imposible│    │ Error barato (<3 s)  │    │ Error caro pero justo  │
   └────────────────┘    └──────────────────────┘    └────────────────────────┘
          ^                                                       │
          │                                                       │
          └──── si falla el examen, el bucle vuelve acá ──────────┘
                (no se avanza a la mecánica siguiente)

   REGLA: nunca se introduce la mecánica N+1 antes de que N pase su examen.
```

**El nivel-tutorial invisible.** Es el primer nivel real del juego, diseñado para que enseñe sin declararse tutorial. Sus reglas de construcción:

| Regla | Por qué |
|---|---|
| Espacio cerrado con una sola salida | El jugador no puede perderse; el error de navegación no existe |
| La primera acción posible es la mecánica central | Se aprende el verbo del juego antes que nada |
| Obstáculo imposible de ignorar y trivial de superar | Fuerza el uso sin frustrar |
| Cámara o iluminación que apunta a lo importante | Dirige la atención sin texto |
| El primer error no cuesta nada | Habilita la exploración |
| Un momento memorable en los primeros 3 min | Es lo que el jugador va a contar |

**Cuándo un tutorial explícito SÍ se justifica.** No es siempre pecado. Se justifica cuando: (a) el input no es adivinable ni convencional (combinaciones, mantener + dirección), (b) la mecánica no tiene representación visual posible (una regla económica abstracta), (c) el género es de alta complejidad y el jugador *espera* que le expliquen (estrategia, gestión, simulación), (d) hay riesgo de perder progreso permanente por no saber. Fuera de eso, es una confesión de que el nivel no enseña.

**Presupuesto de atención.**

| Ventana | Qué tiene que pasar sí o sí | Qué NO puede pasar |
|---|---|---|
| **0–60 s** | El jugador tiene el control y ejecuta el verbo central. Sabe qué es lo suyo en pantalla y hacia dónde va. | Logos largos, cinemática no salteable, elegir dificultad a ciegas, más de 1 popup |
| **1–5 min** | Ya usó la mecánica central 5+ veces, tuvo un primer éxito claro, y sabe cuál es su objetivo de sesión. | Presentar 2 mecánicas más sin consolidar la primera; primer muro real |
| **5–30 min** | Vio 2–3 mecánicas más —el total de los 30 minutos no pasa de 5—, tuvo un momento memorable, y entendió el loop completo (acción → consecuencia → recompensa → nueva acción). | Que todavía no haya aparecido el gancho; que el juego siga "explicando" |

El recurso escaso no es el tiempo, es la **atención**: en los primeros minutos el jugador está gastando casi toda su capacidad en operar los controles. Todo lo que le pidas leer compite directamente con eso. Por eso el texto llega mal en el minuto 1 y bien en el minuto 20.

**Vocabulario del género: qué se puede asumir y qué no.**

| Se puede asumir (casi siempre) | Se puede asumir sólo dentro del género | Nunca se asume |
|---|---|---|
| WASD/stick izquierdo mueve | Doble salto, dash con hombro | Cualquier combinación de 2+ botones |
| Barra roja = vida | Stamina, parry, iframes de rodada | Un ícono propio de tu juego |
| Rojo = daño / verde = cura | Loop de run + meta en roguelites | Reglas de economía propias |
| Interactuar con el botón sur / E | Crafteo desde inventario | Interacciones ocultas o contextuales raras |
| Cofre / brillo = recompensa | Fog of war, niebla de guerra en estrategia | Qué significa tu recurso morado |

Regla operativa: **usar la convención del género es la forma más barata de enseñar; romperla es un gasto que hay que pagar con una lección explícita.** Si rompés una convención, tenés que enseñarla como si fuera una mecánica nueva — porque para el jugador lo es, y encima tiene que desaprender primero.

**El coste de cada popup.** Un popup cuesta: la interrupción del flow, el reinicio del contexto motriz (soltó los controles), la probabilidad de que no se lea (alta: el jugador quiere volver a jugar), y la deuda de confianza — a partir del tercer popup el jugador empieza a cerrarlos sin leer, y ahí perdiste el canal para siempre. Baseline: **máximo 1 popup en los primeros 60 s, máximo 3 en los primeros 10 min**, y cada uno debe ser reconsultable después (glosario, pausa) para que su pérdida no sea fatal.

**Enseñar con la muerte barata.** El fracaso es el mejor profesor que tenés y es gratis de producir. Condiciones para que enseñe en vez de castigar: el jugador entiende qué lo mató (comprensión, ver `06_Dificultad_y_curva`), el reintento cuesta menos de 3 s, la muerte ocurre cerca del error (no 30 s después), y la situación se repite igual para poder probar la hipótesis. Con esas cuatro, el jugador prefiere morir a leer.

## Baseline numérico

| Parámetro / criterio | Baseline sugerido | Por qué |
|---|---|---|
| Tiempo hasta el primer input del jugador | < 30 s desde el arranque (idealmente < 15 s) | Cada segundo sin control gasta paciencia que no ganaste |
| Popups en los primeros 60 s | Máximo 1 | El segundo se lee a la mitad; el tercero no se lee |
| Popups en los primeros 10 min | Máximo 3 | A partir de ahí se cierran por reflejo |
| Palabras por popup | ≤ 15 | Encima de 15 se saltea |
| Mecánicas nuevas en los primeros 5 min | 1 (máximo 2) | Consolidar > presentar |
| Mecánicas nuevas en los primeros 30 min | 3–5 **en total, contando las de los primeros 5 min** | Deja espacio para practicar cada una. Es un total, no un adicional: 2 en los primeros 5 min dejan 3 para el resto |
| Usos de una mecánica antes de examinarla | 3–5 con variación | Menos y no se automatiza |
| Tiempo hasta el primer éxito claro del jugador | < 90 s | El primer éxito es lo que compra los 10 min siguientes |
| Tiempo hasta el momento memorable | < 3 min (nunca más de 10) | Es el gancho y lo que el jugador cuenta |
| Costo del primer error | 0 (ni tiempo ni recurso) | Habilita explorar en vez de temer |
| Duración total del tramo tutorial | ≤ 10 % del tiempo esperado de juego | Encima se lee como escuela |
| Testers necesarios que nunca vieron el juego | 5 frescos | El n canónico lo fija `13_Playtesting_y_validacion`; con 3 ya aparecen los bloqueos duros, pero los de comprensión necesitan 5 |
| Tiempo de silencio del observador durante el test | 100 % mientras la corrida sea válida | Cualquier ayuda la termina como dato de onboarding — ver el protocolo: el rescate a los 3 min es un hallazgo, no una excepción a esta regla |

## Patrones que funcionan

| Patrón | Cuándo usarlo | Costo |
|---|---|---|
| **Nivel-tutorial invisible** | Default para acción, plataformas, aventura | Caro: es diseño de nivel fino, muchas iteraciones |
| **Habitación de una sola salida** | Presentar cualquier mecánica nueva | Puede sentirse pasillo si se abusa |
| **Demostración por NPC** | Mecánicas con timing o secuencia | Requiere IA o scripting de la demo |
| **Prompt contextual efímero** | Inputs no adivinables, en el momento exacto | Debe desaparecer solo tras 2–3 usos correctos |
| **Muerte barata de escuela** | Enseñar peligros y timings | Exige checkpoint inmediato y telegrafiado |
| **Glosario reconsultable** | Todo lo enseñado por popup vive también en pausa | Trabajo de UI, poco de diseño |
| **Tutorial diferido** | Enseñar la mecánica recién cuando el jugador la necesita | Requiere detectar la necesidad; excelente retención |
| **Onboarding por dificultad implícita** | Los primeros enemigos son versiones lentas de los reales | Barato y muy efectivo: reusa assets |
| **Sandbox opcional** | Zona de práctica accesible desde el menú | No enseña solo; complementa |

## Antipatrones

| Antipatrón | Síntoma observable en playtest |
|---|---|
| **Muro de texto inicial** | El tester saltea sin leer y a los 2 min pregunta lo que decía el texto |
| **Tutorial que se atraviesa** | Completa todos los pasos y a los 5 min no usa ninguna mecánica enseñada |
| **Enseñar sin examinar** | La mecánica aparece una vez y no vuelve hasta 40 min después: ya se olvidó |
| **Manos en el volante** | El juego bloquea todo salvo el botón correcto: el tester aprende a apretar lo que brilla, no la mecánica |
| **Popup por cada cosa** | El tester cierra el cuarto popup sin leerlo (observable: <1 s en pantalla) |
| **Cinemática antes del control** | El tester mira el teléfono durante la intro |
| **Convención rota en silencio** | El tester intenta 3 veces la acción convencional y se frustra |
| **Todo enseñado, nada practicado** | 6 mecánicas en 5 min; el tester recuerda 2 |
| **Elegir dificultad a ciegas** | El tester pregunta "¿cuál me conviene?" antes de haber jugado nada |
| **Observador que habla** | El test da resultados buenísimos y el juego fracasa igual con jugadores reales |

## Cómo se mide en playtest

**Qué observar:** segundos hasta el primer input, cuántas veces mira los controles o el teclado, tiempo que cada popup permanece en pantalla (menos de 1 s = no se leyó), cuántos intentos hasta el primer éxito, si usa la mecánica enseñada la próxima vez que hace falta (la prueba real), en qué momento levanta la vista de la pantalla, y qué parte del HUD nunca mira.

**Qué preguntar** (después): "Contame qué estabas tratando de hacer" (mide intención), "¿Qué pensabas que iba a pasar cuando apretaste eso?" (mide modelo mental), "¿Cuál es tu objetivo ahora?" (mide claridad de meta), "¿Qué te sorprendió?", "¿Qué botón hace X?" (mide retención real).

**Qué NO preguntar:** "¿Se entendió el tutorial?" (nadie admite que no entendió). "¿Estuvo claro?" (respuesta social garantizada). "¿Sabías que podías hacer X?" (se lo estás enseñando ahí mismo y contaminás el resto del test).

**Por qué no podés estar en la sala hablando.** Cada aclaración que das es una corrección que el jugador real no va a tener. Un onboarding testeado con el diseñador al lado siempre parece funcionar: estás siendo el tutorial. Protocolo mínimo: presentás el juego en una frase, decís "no te voy a poder ayudar", y te callás. Si el tester se traba más de 3 min sin progreso, anotás el punto exacto y recién ahí intervenís — pero esa corrida ya terminó como dato de onboarding. Grabá pantalla y manos si podés; el silencio incómodo es el dato.

**Eventos candidatos de telemetría** (no una lista a implementar entera): tiempo hasta el primer input, tiempo hasta el primer éxito, tasa de abandono por minuto en los primeros 10, popups mostrados vs tiempo en pantalla de cada uno, primer uso de cada mecánica enseñada (y si hubo un segundo uso), y punto exacto del primer abandono.

> El **tope total** de eventos activos lo fija `13_Playtesting_y_validacion` en ≤10, uno por pregunta de diseño. Esta lista propone candidatos para el dominio del onboarding; no los suma al presupuesto por su cuenta. Cuatro libros proponiendo "su" telemetría mínima suman ~23 eventos, que es más del doble del tope.

## CHECKLIST

```txt
[ ] El jugador tiene el control en menos de 30 s desde el arranque
[ ] Toda cinemática es salteable desde el primer frame
[ ] Máximo 1 popup en los primeros 60 s, 3 en los primeros 10 min
[ ] Ningún popup supera las 15 palabras
[ ] Cada mecánica se enseña por affordance/restricción antes que por texto
[ ] Cada mecánica nueva tiene: presentación segura -> 3-5 prácticas -> examen
[ ] No se introduce la mecánica N+1 antes de que N pase su examen
[ ] El primer error del jugador no cuesta nada
[ ] Hay un momento memorable en los primeros 3 minutos
[ ] Toda convención de género rota se enseña explícitamente
[ ] Todo lo enseñado por popup es reconsultable en pausa/glosario
[ ] No se pide elegir dificultad antes de haber jugado
[ ] El tramo tutorial es <= 10 % del tiempo esperado de juego
[ ] Se testeó con 5 testers frescos, en silencio total (el n lo fija 13_Playtesting)
[ ] Cada mecánica enseñada vuelve a aparecer dentro de los 10 min siguientes
```

## Aplicación
**Game Design abre este libro cuando:** diseña el primer nivel de un GDS, define el orden de presentación de mecánicas, evalúa si hace falta tutorial explícito, prepara una demo o build de feria, o cuando el playtest muestra abandono en los primeros 10 minutos.

**Qué trae la IA por default:** la secuencia enseñar→practicar→examinar armada para cada mecánica del GDS, la propuesta de enseñar por affordance o restricción antes de aceptar cualquier texto, el conteo de popups y palabras contra el baseline, y el protocolo de test en silencio con las preguntas prohibidas listadas.

## Límites
No aplica igual en: juegos de complejidad deliberadamente alta cuyo público espera manual y curva empinada (simuladores, wargames — ahí el tutorial explícito y extenso es un feature), juegos de puzzle donde descubrir la regla *es* el juego (enseñar de más lo arruina), y secuelas cuyo público ya tiene el vocabulario (pero acordate del jugador nuevo: dale una vía rápida, no le saques la enseñanza).

**Tensiones:** con `06_Dificultad_y_curva` — el onboarding pide error barato y la curva pide que el error importe; la resolución es temporal, no de compromiso (barato primero, caro después). Con el Pilar 9 (agencia) — enseñar por restricción le saca libertad al jugador justo cuando quiere probar. Con el Pilar 8 (pacing) — un onboarding cuidadoso es lento, y la primera impresión pide velocidad: la salida es enseñar dentro de la acción, nunca antes de ella.

## Fuentes
`09_Gamers_Brain` · `10_Game_Usability` · `12_Design_of_Everyday_Things` · `04_Theory_of_Fun` · `03_Game_Design_Workshop` · `02_Art_of_Game_Design` · `13_Elements_of_Game_Design` · `19_Playful_Production_Process` · `14_Fundamentals_of_Game_Design`
Cruces: `05_Fundamentos_de_experiencia_ludica` (Pilares 4 y 6) · `04_Playbook_de_diseno` · `02_Game_feel` · `01_Loop_de_experiencia` · `06_Dificultad_y_curva` · `08_Progresion_y_recompensa`

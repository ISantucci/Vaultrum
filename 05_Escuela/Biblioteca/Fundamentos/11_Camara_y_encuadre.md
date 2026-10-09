---
tipo: fundamento
estado: En la Biblioteca
mision: EST-006_Mision_Lote_Biblioteca_Agosto26
profundiza: Pilar 4 — Claridad y legibilidad · Pilar 5 — Justicia y control
cruza: 05_Fundamentos_de_experiencia_ludica, 02_Game_feel, 10_Input_y_respuesta, 04_Playbook_de_diseno
---

# Fundamento 11 — Cámara y encuadre

> Profundiza la cámara como **decisión de diseño**: qué información existe para el jugador, con cuánta anticipación, y bajo qué contrato. Cubre taxonomía, pipeline, smoothing, screenshake y encuadre por género.
> **No cubre:** composición artística ni dirección de fotografía; cinemáticas narrativas y su guion; HUD y diegesis (eso es UI/UX); cámaras de VR.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta · 2. El modelo · 3. Baseline numérico · 4. Patrones · 5. Antipatrones · 6. Playtest · 7. Checklist · 8. Aplicación, límites y fuentes.

## Qué es y por qué se rompe si falta
La cámara no muestra el juego: **lo define**. Lo que no está en cuadro no existe para la decisión del jugador, y una decisión tomada sin información no es agencia, es lotería. Por eso la cámara pertenece a los pilares 4 y 5 y no al departamento técnico: es el mecanismo que reparte la información necesaria para no morir.

Cuando falta, el juego se vuelve injusto sin que ninguna regla sea injusta. Y hay un segundo costo, más silencioso: la cámara mala **cansa el cuerpo**. El jugador no dice "la cámara está mal", dice "no sé, me cansé" y se levanta a los 20 minutos. Ese abandono es indistinguible de un problema de contenido si no lo buscás específicamente.

## El modelo

**A. Taxonomía.**

| Tipo | Qué resuelve | Costo | Cuándo elegirla |
|---|---|---|---|
| Fija (por sala) | Composición perfecta, cero mareo | Cero look-ahead; el jugador entra a ciegas | Puzzle, terror, arcade de pantalla única |
| Seguimiento duro (lock) | Simple, predecible | Micro-temblor; ilegible al vibrar el personaje | Prototipos, top-down lento |
| Con zona muerta | Estabilidad + libertad de micro-movimiento | Dos parámetros más; bugs de re-entrada | Casi todo el 2D y el top-down |
| Con look-ahead | Anticipación en la dirección del movimiento | Oscila al zigzaguear | Plataformas, runners, shooters 2D |
| Con anclajes / regiones | Autoría por zona, encuadre garantizado | Autoría manual + blend entre regiones | Metroidvania, niveles curados |
| Cinemática / scripted | Dirige la atención | Roba control; interrumpe el flow | Sólo fuera de combate |
| Híbrida por estado | Cada estado su encuadre | Explosión de parámetros | Producción madura |

**B. El pipeline: el orden importa más que los valores.**

```txt
PIPELINE DE CÁMARA — orden fijo, una pasada por frame

 1  TARGET            jugador + offset de altura (1.2–1.6 m en 3ra persona)
 2  PUNTO COMPUESTO   promedio ponderado: jugador 0.7 · amenaza/objetivo 0.3
 3  LOOK-AHEAD        + intención (stick), NO velocidad · con damping propio
 4  DEADZONE          si el punto cae dentro del rectángulo muerto → no mover
 5  DAMPING           SmoothDamp por eje (X ≠ Y), críticamente amortiguado
 6  CONFINER          clamp a los límites de la región / volumen del nivel
 7  OCLUSIÓN          pull-in predictivo o fade del oclusor — nunca snap
 8  ENCUADRE          offset de composición (espacio jugable por delante)
 9  SHAKE             trauma² · techo global duro · decay
10  FOV               base + kick (dash / daño), retorno en 200–300 ms
    ▼
    SALIDA A RENDER

 ⚠  Invertir 4 y 5 (amortiguar antes de la zona muerta) = temblor clásico.
 ⚠  Aplicar 9 antes de 6 = el shake deja ver fuera del nivel.
 ⚠  Aplicar 3 sin damping propio = oscilación en cada cambio de dirección.
```

**C. El contrato de la cámara con el jugador.** Cinco cláusulas; romper una sola alcanza para que el juego se sienta tramposo.
1. **Nunca le saques información que necesita para no morir.** Toda amenaza capaz de matar en menos de T debe ser visible T antes.
2. **No te muevas sola durante el control activo**, salvo que el jugador haya causado el movimiento.
3. **Espacio por delante**, siempre, en la dirección del avance.
4. **Devolvé el control** en ≤ 300 ms al terminar cualquier movimiento scripted.
5. **Sé predecible**: la misma acción produce el mismo encuadre, siempre.

**D. Presupuesto de visión.** La cláusula 1 se calcula, no se estima:

`distancia visible por delante ≥ velocidad × (t_reacción + t_ejecución) × 1.5`

Con t_reacción ≈ 250 ms (percepción + decisión) y t_ejecución = duración real de la maniobra de escape. Ejemplo: personaje a 8 u/s, salto de 350 ms → (0.25 + 0.35) × 1.5 = 0.9 s → **7.2 unidades visibles por delante**. Ese número, no el gusto, define el look-ahead y el FOV. Si no entra en pantalla, la opción es bajar la velocidad o alejar la cámara: no hay tercera.

**E. Smoothing y el punto de mareo.**

| Técnica | Parámetro | Sensación | Riesgo |
|---|---|---|---|
| Lerp por frame | `t` fijo | Aceptable a 60 fps | Depende del framerate: a 30 fps es otro juego |
| Exponencial (frame-independent) | vida media | Suave y estable | Nunca llega del todo |
| Críticamente amortiguado | tiempo de asentamiento | Profesional, sin rebote | Requiere estado (velocidad) |
| Resorte con overshoot | rigidez + amortiguación | Vivo, "orgánico" | **Mareo** si hay overshoot en 2 ejes |

El punto donde el smoothing se vuelve mareo: tiempo de asentamiento por encima de **~250–300 ms**, u overshoot simultáneo en X e Y, o retardo tal que en carrera sostenida el personaje quede a más del 15% del ancho de pantalla del punto de encuadre. Regla dura: **el eje Y se trata distinto del X**. En plataformeros, al aterrizar el eje Y hace snap (o se asienta en ≤ 100 ms); de lo contrario cada salto es una ola.

**F. Screenshake con presupuesto.** Modelo de trauma: una sola variable `trauma ∈ [0,1]`; los eventos **suman** trauma con clamp a 1.0; el desplazamiento se calcula como `trauma²` (o `³`) por la amplitud máxima; el decay es lineal, 1.0–1.5 por segundo. Cuadrático porque hace que muchos eventos chicos no se conviertan en una licuadora, y que el evento grande siga sintiéndose grande.

| Evento | Amplitud (% alto de pantalla) | Duración | Nota |
|---|---|---|---|
| Golpe liviano | 0.2–0.4% | 60–100 ms | Casi subliminal |
| Golpe pesado / muerte de enemigo | 0.8–1.5% | 150–250 ms | Con hitstop de 2–5 f |
| Explosión cercana | 2–3% | 300–450 ms | Único evento que pisa el techo |
| Techo global (clamp) | **3% del alto** | — | No negociable |

Slider de intensidad 0–100% obligatorio, y el juego tiene que ser **completamente jugable en 0%**: si el shake transporta información, esa información falla en accesibilidad.

**G. Encuadre por género.**

| Género | Punto de encuadre | Deadzone típica | Look-ahead | Error clásico |
|---|---|---|---|---|
| Plataformero 2D | Jugador desplazado 5–10% hacia atrás | 12–18% ancho · 20–30% alto | 10–20% del ancho | Salto de fe: el destino no está en cuadro |
| Top-down | Entre jugador y cursor/mira | 8–12% radial | Hacia el cursor, 25% | Cámara centrada 1:1 que tiembla |
| Tercera persona | Hombro + offset de altura | Cono de 5–8° | Por intención del stick | Auto-recenter que pelea con el jugador |
| Isométrico | Centro con desplazamiento al frente | 10% | Bajo | Oclusión de edificios sin fade |

FOV sugerido: primera persona 90–103° horizontal en PC, 70–85° a distancia de sofá; tercera persona 55–70°. **Slider de FOV obligatorio en PC.** FOV kick en dash: +5 a +12° con retorno en 200–300 ms.

## Baseline numérico

| Parámetro / criterio | Baseline sugerido | Por qué |
|---|---|---|
| Deadzone horizontal | 12–18% del ancho | Absorbe micro-movimiento sin perder el centro |
| Deadzone vertical | 20–30% del alto | El eje Y varía más (saltos) y marea más |
| Look-ahead | 10–20% del ancho, aplicado en 300–500 ms | Cumple el presupuesto de visión sin oscilar |
| Tiempo de asentamiento (X) | 180–250 ms | Debajo se siente rígido, encima se siente ebrio |
| Tiempo de asentamiento (Y) | 100–150 ms; snap al aterrizar | Evita la ola vertical |
| Overshoot | 0% en Y; ≤ 3% en X | El rebote vertical es la causa n.º 1 de mareo |
| Techo de screenshake | 3% del alto de pantalla | Por encima se pierde la lectura de hitboxes |
| Decay de trauma | 1.0–1.5 · s⁻¹ | Deja el pico y limpia rápido |
| Offset vertical del target (3ra p.) | 1.2–1.6 m sobre el pie | Encuadra la amenaza, no el piso |
| Devolución de control post-cinemática | ≤ 300 ms | Más allá, el jugador ya intentó moverse |
| Velocidad de cámara manual | 90–180 °·s⁻¹, con slider | Rango habitual; sin slider, la mitad sufre |
| FOV kick en dash | +5 a +12°, retorno 200–300 ms | Vende velocidad sin desorientar |
| Blend entre regiones | 250–400 ms, con easing | Menos se lee como corte; más se lee como pérdida de control |
| Visión por delante | ≥ velocidad × 0.9 s | Cláusula 1 del contrato, calculada |

## Patrones que funcionan
- **Zona muerta con zona blanda (histéresis).** Rectángulo interior donde la cámara no se mueve, exterior donde acelera. *Costo:* un bug clásico de re-entrada oscilante en el borde; hay que probarlo caminando al ras.
- **Look-ahead por intención, no por velocidad.** Mirá hacia donde apunta el stick, no hacia donde va el cuerpo — anticipa 100–200 ms extra. *Costo:* con zigzag oscila; exige damping propio y zona muerta de stick.
- **Punto de interés compuesto.** Promedio ponderado jugador/objetivo. *Costo:* con 3+ focos se aleja demasiado; necesita clamp de zoom.
- **Cámara por volúmenes con blend.** Regiones de nivel con parámetros propios. *Costo:* autoría manual por sala; es tiempo de level design, no de código.
- **Snap vertical al aterrizar.** *Costo:* si el personaje rebota, el snap se lee como tirón; hay que amortiguarlo en 2–3 frames.
- **Fade de oclusores.** Disolver la pared en vez de meter la cámara. *Costo:* shader y orden de render; en pixel art no siempre es viable.
- **Peek manual barato.** Un botón adelanta la cámara. *Costo:* si es **necesario** para sobrevivir, es un impuesto y viola la cláusula 1 — sólo vale como comodidad opcional.

## Antipatrones
| Antipatrón | Síntoma observable en playtest |
|---|---|
| Seguimiento 1:1 sin deadzone | Temblor constante; el tester se aleja de la pantalla o se queja de cansancio a los 10 min |
| Look-ahead sin damping | Oscilación al cambiar de dirección → **el jugador deja de cambiar de dirección rápido** |
| Shake acumulativo lineal | En la oleada grande no sabe qué lo mató |
| Auto-recenter agresivo | Suelta el stick derecho y espera a que la cámara "se calme" |
| Salto de fe (destino fuera de cuadro) | Camina al borde y hace **saltitos de sondeo** |
| Alejarse para "mostrar" al jefe mientras ataca | Muere en la transición; dice "ni lo vi" |
| Colisión con snap en pasillos | Sale desorientado y camina para el lado equivocado |
| Cinemática que roba control en combate | Suelta el mando y se cruza de brazos |
| FOV fijo bajo en PC | Se levanta a los 20 min "a tomar aire" |
| Un solo set de parámetros para todos los estados | La cámara de caminar se usa en caída libre y se pierde el suelo |

## Cómo se mide en playtest
**Qué observar:** los saltitos de sondeo en los bordes (falta visión abajo), si el tester mueve la cabeza para "ver más", si retrocede antes de avanzar en cada sala nueva (falta look-ahead), y el minuto exacto en que empieza a cambiar de postura. Cronometrá el intervalo entre *la amenaza entra en cuadro* y *el jugador reacciona*: si es menor a 250 ms, no reaccionó, adivinó.
**Qué preguntar:** "¿qué viste justo antes de morir?", "¿qué había abajo cuando saltaste?", "dibujame de memoria la sala".
**Qué NO preguntar:** "¿la cámara está bien?", "¿te marea?" (la sugestión fabrica el síntoma), "¿preferís más zoom?".
**Prueba de mareo:** sesión continua de 20 min y, al final, una pregunta genérica de malestar físico **sin nombrar la cámara**. Si dos de cinco reportan algo, revisá overshoot y FOV antes que cualquier otra cosa.
**Telemetría mínima:** muertes por caída con la plataforma destino fuera del frustum (flag booleano al morir), % de tiempo con el jugador fuera de la deadzone, trauma acumulado por segundo (p95), % de sesión con oclusor activo, uso del control manual de cámara (si nadie lo toca: o la automática funciona, o el binding es invisible — averiguá cuál).

## CHECKLIST
```txt
CÁMARA Y ENCUADRE — pegar en el GDS

[ ] Tipo de cámara declarado por estado (caminar / correr / caer / combate)
[ ] Pipeline en el orden correcto: deadzone ANTES de damping, confiner ANTES de shake
[ ] Presupuesto de visión calculado: velocidad ___ × 0.9 s = ___ unidades por delante
[ ] Cláusula 1 verificada: ninguna amenaza letal aparece con menos de 250 ms de aviso
[ ] Deadzone X ___ % · Y ___ % · probada caminando al ras del borde
[ ] Asentamiento X ___ ms · Y ___ ms · overshoot vertical = 0
[ ] Snap o asentamiento rápido en Y al aterrizar
[ ] Shake con modelo de trauma², techo 3% del alto, decay declarado
[ ] Slider de shake 0–100% · el juego es jugable y legible en 0%
[ ] Slider de FOV (PC) · inversión de ejes · sensibilidad separada por contexto
[ ] Oclusión resuelta por fade o pull-in predictivo, nunca por snap
[ ] Toda cámara scripted devuelve el control en ≤300 ms y es salteable
[ ] Sesión de 20 min continua sin reporte de malestar en ≥4 de 5 testers
[ ] Cero saltos de fe: recorrido completo verificando destino visible
```

## Aplicación · Límites · Fuentes
**Aplicación.** La cámara se especifica en el GDS junto al movimiento, nunca después: los parámetros de cámara y los de locomoción se balancean juntos. En el LDS, cada sala declara su región de cámara y su verificación de "destino visible".
**Límites.** No aplica a VR (donde toda cámara no diegética es náusea garantizada) ni a cámaras de estrategia con control total del jugador, donde el contrato se invierte. Los porcentajes asumen 16:9; en ultrawide recalculá la deadzone en unidades de mundo, no de pantalla.
**Fuentes.** `05_Game_Feel` · `09_Gamers_Brain` · `10_Game_Usability` · `14_Fundamentals_of_Game_Design` · `13_Elements_of_Game_Design` · `12_Design_of_Everyday_Things` · `03_Game_Design_Workshop` · `29_Racing_the_Beam` · `01_Pong`.
**Cruces.** `05_Fundamentos_de_experiencia_ludica` (P4, P5) · `02_Game_feel` · `10_Input_y_respuesta` · `04_Playbook_de_diseno`.

---

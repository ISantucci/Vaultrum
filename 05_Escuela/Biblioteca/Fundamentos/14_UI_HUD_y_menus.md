---
tipo: fundamento
estado: En estudio
mision: EST-006_Mision_Lote_Biblioteca_Agosto26
profundiza: Pilar 4 — Claridad y legibilidad
cruza: 05_Fundamentos_de_experiencia_ludica, 02_Game_feel, 03_Definicion_de_terminado, 04_Playbook_de_diseno
---

# Fundamento 14 — UI, HUD y menús

> Cubre la capa donde el juego habla explícito: HUD, menús, navegación, estados de interfaz y legibilidad. **No** cubre estilo gráfico ni dirección de arte, ni economía de F2P, ni localización profunda, ni accesibilidad completa (solo el piso mínimo). Tampoco cubre el feedback dentro del mundo jugable: eso es `02_Game_feel`.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta
2. El modelo — cuatro superficies, tres cajones, dos presupuestos, cinco estados olvidados
3. Baseline numérico
4. Patrones que funcionan
5. Antipatrones
6. Cómo se verifica
7. CHECKLIST
8. Aplicación · Límites · Fuentes

## Qué es y por qué se rompe si falta
La UI es el único lugar del juego donde el sistema habla en su propio idioma, sin metáfora. Todo lo demás —animación, sonido, level design— comunica por inferencia. La UI comunica por declaración. Por eso es el último recurso y también el más caro en atención: cada píxel de HUD es un píxel que el jugador no está mirando del juego.

Cuando falta o está mal, no falla "la estética": falla la toma de decisiones. El jugador no sabe cuánta vida le queda, no sabe si el input entró, no sabe cómo salir de una pantalla. El síntoma clásico no es "se ve feo", es **el jugador aprieta el mismo botón tres veces**. Eso no es impaciencia, es ausencia de acuse de recibo.

Para un dev solo hay una trampa extra: la UI parece "lo que se hace al final" y en realidad es lo que define si el juego se puede jugar sin vos al lado explicando.

## El modelo

**Capa 1 — Las cuatro superficies.** Toda información se puede poner en uno de cuatro lugares. Elegir mal no es un error de gusto, es un error de costo.

```txt
                    ¿ESTÁ EN LA FICCIÓN?
                     SÍ                      NO
        ┌────────────────────────┬────────────────────────┐
   SÍ   │ DIEGÉTICO              │ ESPACIAL               │
 ¿ESTÁ  │ pantalla en el traje,  │ contorno de enemigo,   │
 EN EL  │ munición en el arma,   │ marcador 3D, arco de   │
 ESPACIO│ linterna que titila    │ trayectoria, decal     │
  3D?   ├────────────────────────┼────────────────────────┤
   NO   │ META                   │ NO DIEGÉTICO           │
        │ sangre en el borde,    │ barra de vida, minimapa│
        │ lente sucia, viñeta    │ contador, menú, tooltip│
        └────────────────────────┴────────────────────────┘
```

| Superficie | Fuerte en | Débil en | Costo de producción |
|---|---|---|---|
| Diegético | Inmersión, coherencia | Precisión numérica, lectura rápida | Alto (arte + animación + cámara) |
| Espacial | Ubicar en el mundo, targeting | Se pierde fuera de cámara | Medio (shader/billboard) |
| Meta | Estado urgente y emocional | Cantidad exacta, historial | Bajo (post-proceso) |
| No diegético | Precisión, densidad, escaneo | Rompe inmersión, come pantalla | Bajo (Canvas) |

**Capa 2 — Los tres cajones.** Cada dato del juego va exactamente a un cajón. Escribí la lista completa antes de dibujar nada.

| Cajón | Regla de admisión | Ejemplos |
|---|---|---|
| HUD permanente | Se consulta ≥1 vez cada 10 s **y** cambia una decisión inmediata | Vida, munición, cooldown activo, objetivo actual |
| A demanda | Se consulta ≤1 vez por minuto, o solo al planificar | Inventario, mapa completo, stats, log |
| No va (lo dice el mundo) | El mundo o el audio ya lo comunican | "Enemigo cerca" (audio), "puerta cerrada" (visual del candado) |

**Capa 3 — Los dos presupuestos.** El *presupuesto de píxeles* es finito y medible: cuánto del área de pantalla ocupa el HUD. El *presupuesto de atención* es más chico y no se ve: cuántos elementos puede monitorear el jugador mientras juega. Un jugador en combate sostiene 2–3 elementos de HUD, no 8. Cuando agregás el noveno widget no ganás información: perdés los tres primeros.

**Capa 4 — Los cinco estados que casi todos olvidan.** Cada pantalla tiene un estado feliz y cinco que nadie prototipa: **vacío** (inventario sin ítems, lista sin partidas), **cargando** (¿el juego colgó o está trabajando?), **error** (guardado falló, archivo corrupto), **primera vez** (el jugador nunca vio esta pantalla y no hay nada que le enseñe), y **cambio de dispositivo** (soltó el gamepad y agarró el teclado a mitad de menú). Los cinco son bugs de UX garantizados si no están en la lista de tareas desde el día uno.

**Capa 5 — El gamepad como restricción de diseño.** Si la UI se navega con stick y D-pad, no podés diseñar como si hubiera cursor. Foco siempre visible, orden de foco explícito (no automático), wrap definido, y `B`/`Círculo` vuelve **siempre**, desde cualquier profundidad. Diseñar primero para gamepad y después agregar mouse funciona; al revés, no.

**Capa 6 — La cadena de respuesta.** Un botón no "hace algo": acusa recibo, después hace algo.

```txt
 t=0      input registrado
 ≤16 ms   cambio visual (highlight, escala 1.00 → 1.04)
 ≤50 ms   sonido de confirmación
 ≤100 ms  el jugador lo percibe como "instantáneo"
 ≤200 ms  transición de pantalla completada
 >300 ms  sin feedback → el jugador vuelve a apretar
```

## Baseline numérico

| Parámetro / criterio | Baseline sugerido | Por qué |
|---|---|---|
| Área de pantalla ocupada por HUD permanente | ≤10–12% | Arriba de eso el jugador deja de mirar el mundo |
| Elementos permanentes en HUD | 3–5 | Límite práctico de monitoreo en combate |
| Latencia input → acuse visual | ≤100 ms (objetivo ≤50 ms) | Umbral de "instantáneo" percibido |
| Tipografía de cuerpo — TV a 2–3 m | ≥28 px @1080p (~2.6% de la altura) | Distancia de lectura de sala |
| Tipografía de cuerpo — monitor / handheld | ≥16–18 px @1080p / ≥22 px @720p | Densidad de píxeles y distancia |
| Contraste texto/fondo | ≥4.5:1 cuerpo · ≥3:1 títulos e íconos | Piso de legibilidad con luz ambiente |
| Safe area en TV | 5% de margen por lado | Overscan todavía existe |
| Blanco táctil / clic mínimo | ≥44 px @1x (~9 mm) | Precisión del dedo y del cursor |
| Transición entre pantallas | 120–200 ms | Más rápido se pierde, más lento molesta |
| Pasos hasta cualquier opción crítica | ≤3 | Volumen y rebind no pueden estar enterrados |
| Elementos con foco visibles sin scroll | ≤12 | Escaneo con stick se vuelve tedioso |
| Duración de toast / notificación | 2.5–4 s | Alcanza para leer 6–8 palabras |
| Delay de tooltip | 400–600 ms | Evita parpadeo al pasar de largo |
| Apertura de menú de pausa | ≤200 ms y congela la simulación | Es un table-stake, no un feature |
| Sliders de audio mínimos | 3 (master, música, SFX) | Piso de un juego terminado |
| Color como único canal de información | Nunca | ~8% de hombres tiene alguna deficiencia de color |

## Patrones que funcionan

- **Los tres cajones (proceso).** Antes de abrir Figma o el Canvas, listá cada dato del juego y asignale cajón. *Cuándo:* al arrancar el UXS. *Costo:* 2–3 horas de planilla; te obliga a discutir con vos mismo.
- **HUD que se desvanece.** El elemento aparece cuando cambia y se va tras 3–5 s de estabilidad (la barra de vida solo existe si perdiste vida). *Cuándo:* juegos de exploración o cámara cinematográfica. *Costo:* una máquina de estados por widget y riesgo real de esconder algo crítico; nunca lo apliques al recurso que se consume en combate.
- **Foco explícito con cursor virtual.** Definís a mano el vecino arriba/abajo/izq/der de cada elemento en vez de confiar en la navegación automática. *Cuándo:* siempre que haya gamepad. *Costo:* ~30 min por pantalla; se paga solo la primera vez que un menú deja de trabarse.
- **Respuesta en tres capas.** Cada botón devuelve visual + sonido + (si hay) haptic. *Cuándo:* todo botón, sin excepción. *Costo:* 3 assets reutilizables para todo el juego, no por botón.
- **Scrim duro bajo el texto.** Sombra dura, contorno de 2 px o rectángulo semitransparente al 40–60% detrás de todo texto sobre imagen. *Cuándo:* cualquier texto sobre gameplay. *Costo:* medio día; agrega algo de ruido visual y salva la legibilidad en escenas claras.
- **Prompt-agnóstico.** Los glifos de botón salen de un atlas indexado por dispositivo activo, nunca hardcodeados como "presioná X". *Cuándo:* si soportás teclado + gamepad. *Costo:* mantener el atlas y detectar el último dispositivo usado.
- **Opciones mínimas viables.** Video (resolución, pantalla completa, vsync), audio (3 sliders), controles (rebind + sensibilidad + invertir Y), accesibilidad (tamaño de texto, sacudida de cámara off, subtítulos), idioma. *Cuándo:* antes de la primera build pública. *Costo:* 1–2 semanas de dev solo; es la diferencia entre demo y juego.
- **Ensayo del primer minuto.** Prototipar la pantalla en estado "primera vez" antes que en estado lleno. *Cuándo:* toda pantalla con contenido acumulable. *Costo:* casi nulo, y elimina la pantalla vacía que parece bug.

## Antipatrones

| Antipatrón | Síntoma observable |
|---|---|
| HUD de simulador de vuelo | 9+ widgets; en el video del playtest el jugador nunca mira 6 de ellos |
| Botón sin acuse | El jugador aprieta 2–3 veces y después dice "se colgó" |
| Menú solo-mouse | Con gamepad no se puede cerrar un popup o no se ve qué está seleccionado |
| Pausa que no pausa | El jugador muere mientras mira el menú de opciones |
| Color como único canal | Con filtro de deuteranopía, dos estados distintos son el mismo gris |
| Texto sobre imagen sin scrim | En la zona nevada / al mediodía el texto desaparece |
| Confirmar para todo | Vender un ítem cuesta 3 confirmaciones; vender 20 cuesta 60 |
| Estado vacío no diseñado | Inventario recién empezado = panel negro, parece error de carga |
| Fuente de póster a 12 px | Los testers leen mal los números y culpan al balance |
| Opciones ausentes | Reviews que dicen "no hay rebind" antes de hablar del juego |

## Cómo se verifica

- **Test de la foto.** Sacá un screenshot de un momento de combate, mostralo 5 segundos y preguntá: ¿cuánta vida te queda? ¿qué tenés que hacer ahora? Si no lo responden, la jerarquía está rota.
- **Test del gamepad único.** Desconectá el mouse y jugá el juego entero desde el arranque hasta salir. Cada pantalla trabada es un bug bloqueante.
- **Test del televisor.** Escalá el juego al 50% y miralo a 2 m. Todo lo que no se lee está mal dimensionado para consola o handheld.
- **Test del filtro.** Pasá capturas por un simulador de deuteranopía/protanopía y verificá que cada estado siga siendo distinguible por forma, ícono o posición.
- **Conteo de miradas.** Grabá 10 minutos de gameplay y contá cuántas veces el jugador consulta cada widget. Todo lo que baja de 1 consulta cada 60 s se va del HUD permanente al cajón "a demanda".
- **Medición dura.** Loggeá el delta entre input y primer cambio visual del botón. Si supera 100 ms, el problema está en el layout o en la animación, no en la percepción del jugador.

## CHECKLIST

```txt
[ ] Cada dato del juego está asignado a un cajón: HUD / a demanda / no va
[ ] HUD permanente <= 5 elementos y <= 12% del area de pantalla
[ ] Cada elemento del HUD justifica su lugar con una decision que habilita
[ ] Todo boton responde con visual (<=100 ms) + sonido
[ ] Navegacion completa con gamepad: foco visible, wrap definido, B vuelve siempre
[ ] Menu de pausa: abre <=200 ms, congela simulacion, tiene Reanudar/Opciones/Salir
[ ] Los 5 estados existen y estan diseniados: vacio, cargando, error, primera vez, cambio de dispositivo
[ ] Ningun texto sobre imagen sin scrim, sombra dura o contorno
[ ] Tipografia de cuerpo >= 28 px @1080p si hay salida a TV / handheld
[ ] Contraste >= 4.5:1 en cuerpo, >= 3:1 en iconos y titulos
[ ] Ninguna informacion depende solo del color (hay forma, icono o posicion)
[ ] Safe area del 5% respetada en todas las pantallas
[ ] Opciones minimas: video, 3 sliders de audio, rebind, sensibilidad, invertir Y, subtitulos, idioma
[ ] Volumen y rebind alcanzables en <=3 pasos desde la pausa
[ ] Glifos de boton cambian solos segun teclado/gamepad
[ ] Confirmacion solo en acciones irreversibles
[ ] Test de la foto pasado con 3 personas distintas
[ ] Recorrido completo del juego hecho sin mouse
```

## Aplicación · Límites · Fuentes

**Aplicación (Unity, dev solo).** Un solo Canvas por capa lógica (HUD / menús / overlays), `Screen Space - Overlay` para HUD y `Camera` solo si necesitás efectos. Definí el orden de foco a mano con `Navigation: Explicit` en cada Selectable: la navegación automática funciona hasta que movés un botón dos píxeles. Un único `UIAudio` que dispara navegar/confirmar/cancelar/error, llamado desde un wrapper de botón, evita 40 llamadas duplicadas. Todo tamaño de fuente y padding sale de un ScriptableObject de tema, para que el slider de "tamaño de texto" sea una línea y no un refactor. La escala de referencia del CanvasScaler, fijada a 1920×1080 con `Match Width Or Height = 0.5`, es el default más seguro.

**Límites.** Este libro asume un juego single-player con pantalla completa. No cubre UI de multijugador local (split-screen cambia todos los presupuestos), ni interfaces de simulación densa (estrategia, management), donde el HUD *es* el juego y los baselines de 3–5 elementos no aplican. Tampoco reemplaza una auditoría de accesibilidad: acá hay piso, no techo.

**Fuentes.** `09_Gamers_Brain` · `10_Game_Usability` · `12_Design_of_Everyday_Things` · `14_Fundamentals_of_Game_Design` · `02_Art_of_Game_Design` · `13_Elements_of_Game_Design`
**Cruces.** `05_Fundamentos_de_experiencia_ludica` (Pilar 4) · `02_Game_feel` (feedback dentro del mundo) · `03_Definicion_de_terminado` (opciones mínimas como criterio de cierre) · `04_Playbook_de_diseno`

---

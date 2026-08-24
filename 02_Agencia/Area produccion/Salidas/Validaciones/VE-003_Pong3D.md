## Entrega validada

[[TL-003_Pong3D_Unity6_Cadena_Completa]] — Pong 3D para dos jugadores locales en Unity 6.

## Trazabilidad

```txt
TL-003
  RQ-003.1  (no jugable)                          -> SOL-003 -> EJ-003   [completo]
  RQ-003.2  -> GDS-003.2                          -> SOL-003 -> EJ-003   [completo]
  RQ-003.3  -> GDS-003.3                          -> SOL-003 -> EJ-003   [completo]
  RQ-003.4  -> GDS-003.4                          -> SOL-003 -> EJ-003   [completo]
  RQ-003.5  -> GDS-003.5 -> UXS-003.5             -> SOL-003 -> EJ-003   [completo]
  RQ-003.6  -> GDS-003.6                          -> SOL-003 -> EJ-003   [completo]
  RQ-003.7  -> GDS-003.7 -> UXS-003.7             -> SOL-003 -> EJ-003   [completo]
  GDS-003.0 (marco comun, sin RQ propio)                                 [completo]
```

Sin eslabones faltantes. `LDS` no aplica y está declarado en el `TL` y en el `GDS-003.0` con su motivo (no hay dimensión espacial que componer). `UXS` **sí** aplica, al revés que en [[VE-002_Pong3D]], y produjo las dos primeras salidas del Área de UI/UX del vault.

## Contra los insumos de la Biblioteca

Es la diferencia estructural con TL-002 y por eso se verifica primero.

| Table-stake del libro [[01_Pong]] | Cubierto en | Implementado |
|---|---|---|
| 1 · Dos paletas en un eje, con límites | `RQ-003.2` / `GDS-003.2` | `PaddleController` |
| 2 · Pelota que nunca atraviesa nada | `RQ-003.3` / `GDS-003.3` r.7 | Substepping + cruce de plano |
| 3 · Ángulo según punto de impacto | `GDS-003.3` r.3 | `BallController.Bounce` |
| 4 · Marcador visible siempre | `RQ-003.4` / `UXS-003.7` | `GameHud` franja superior |
| 5 · Condición de victoria y fin perceptible | `GDS-003.4` r.3, r.7 | `ScoreTracker` + pantalla de fin |
| 6 · Saque con pausa legible | `GDS-003.4` r.5, r.6 | `BeginServe`, 1.0 s |
| 7 · Reintento inmediato | `GDS-003.4` r.8 | `ENTER` sin recargar escena |
| 8 · Pausa y salida de cada pantalla | `RQ-003.5` / `UXS-003.5` | 6 estados, `ESC` siempre atrás |
| 9 · Controles comunicados | `RQ-003.7` / `UXS-003.7` | Bloques en el menú + hint del primer saque |

**Las nueve están cubiertas por un requerimiento explícito.** Ninguna quedó implícita ni apareció como intuición del programador — que es exactamente lo que la Ley candidata #1 pedía.

**Baseline de parámetros:** los diez valores del libro están traducidos en la tabla de `GDS-003.0` y los diez caen dentro del rango. Verificable línea por línea contra `PongConfig.cs`.

**CHECKLIST de 9 pilares:** corrido en los seis `GDS`. Los ítems marcados `N/A` llevan justificación escrita, ninguno quedó sin marcar.

## Contra los RQ

Los siete están implementados según el `EJ-003`. **Verificado leyendo el código y compilándolo fuera de Unity, no jugándolo.**

## Definición de Terminado

La checklist de 18 ítems del libro [[01_Pong]], que se corre **sobre el juego corriendo**:

```txt
LOOP
[ ] Muevo mi paleta y la pelota rebota siempre, a cualquier velocidad
[ ] Donde pego cambia hacia donde sale: puedo apuntar
[ ] La pelota nunca atraviesa una paleta ni una pared, ni se traba

PARTIDA
[ ] Hay marcador visible para los dos jugadores
[ ] Hay puntaje objetivo declarado y la partida termina al alcanzarlo
[ ] Se quien gano sin interpretar numeros
[ ] Puedo jugar de nuevo sin cerrar la aplicacion

ESTADOS
[ ] Puedo pausar y despausar
[ ] Toda pantalla tiene salida
[ ] Tras un gol hay un saque legible, no un reinicio instantaneo

CLARIDAD
[ ] Se que teclas uso yo y cuales el otro jugador, sin que me lo expliquen
[ ] Distingo mi lado del lado del rival de un vistazo
[ ] En todo momento puedo responder: que pasa / que puedo hacer / como voy

FEEL
[ ] El golpe contra la paleta se ve y se escucha como un evento
[ ] El gol se siente distinto (mas grande) que un rebote
[ ] La paleta responde al instante y frena con peso
[ ] Un rally largo sube de tension por si solo
[ ] El juice nunca me impide ver la pelota
```

**Ningún ítem se tilda.** Los dieciocho están implementados en código y ninguno fue verificado sobre el juego corriendo. Tildarlos desde el código sería el cierre en falso que este gate existe para evitar — y es literalmente el aprendizaje que dejó `VE-002`.

## Experiencia

No leída. Requiere jugar.

## Hallazgos

Ninguno confirmado. Riesgos abiertos, heredados del `EJ-003`:

1. El proyecto nunca se abrió en Unity: no está probado que la escena se genere ni que los recursos builtin (`Standard`, `LegacyRuntime.ttf`) resuelvan.
2. El balance está dentro del rango del libro, pero un rango no es un playtest.
3. El encuadre de cámara se calculó, no se miró.
4. Los caracteres `↑ ↓ ‹ › ▸` dependen de la fuente. Cosmético.

**Lo que sí cambió respecto de `VE-002`:** la implementación está en disco y compila. La entrega dejó de ser una promesa.

## Checklist de validación del owner (3 minutos)

Para pasar a **Cerrado**:

```txt
1. Unity Hub → Add project from disk → C:\Users\ControlEquipos\Desktop\a\vaultrumtest2
2. Abrir con Unity 6. Confirmar que compila sin errores.
3. Abrir Assets/Scenes/Pong.unity (deberia generarse sola; si no: menu Vaultrum → Regenerar escena Pong)
4. Play. Confirmar que la arena se ve completa y la pelota se lee contra el piso.
5. Jugar UNA partida a 5 puntos, de a dos, y correr los 18 items de arriba.
6. Si algo del feel no cierra: tocar el campo `config` del objeto Pong EN PLAY, sin recompilar.
```

## Aprendizaje para el Core

Dos candidatos, sin formalizar. Se derivan al Área de Conocimiento:

1. **Optimizar sin requerimiento de performance es scope no pedido.** Trabajo de calidad que nadie encargó, que consume el presupuesto que debía ir a la experiencia. La regla utilizable no es "no optimices" sino *"no enciendas maquinaria que ningún requerimiento pidió"* — que es una regla de alcance, no de rendimiento. Es la contracara técnica de la Ley candidata #1.
2. **Una entrega puede verificarse parcialmente sin el entorno de destino, y esa verificación parcial hay que declararla con su alcance.** Compilar fuera de Unity cerró una clase entera de errores (sintaxis, tipos, firmas) sin poder abrir el editor. No convierte un `PAUSADO` en `Cerrado`, pero convierte "no sabemos nada" en "sabemos esto y no aquello". `VE-002` no tenía esa distinción disponible.

## Playtest del owner (registrado)

El owner abrió el proyecto y jugó. Veredicto: **8/10**, *"el juego es divertido"*, con mejoras pendientes sin detallar todavía.

Lo que esto cierra, y es lo que TL-002 nunca pudo tener: el juego **corre, se juega y es divertido**. La entrega dejó de ser una promesa verificada en papel. El riesgo #1 del `TL-003` —no poder ejecutar Unity desde la Agencia— quedó cubierto por el checklist de 3 minutos, que funcionó como estaba previsto.

Lo que **no** cierra: los 18 ítems de la Definición de Terminado no se recorrieron uno por uno, y las mejoras pendientes no están declaradas como hallazgos concretos. Un 8/10 es un juicio global válido, pero no es el mismo instrumento que la checklist: dice que el conjunto funciona, no cuál de los dieciocho falla.

## Estado de la entrega

**CERRADO con observaciones abiertas.**

La entrega responde a la intención original: un Pong 3D para dos jugadores que se juega y es divertido (8/10 del owner). El `TL-003` queda entregado.

Las mejoras pendientes **no reabren este `VE`**: se recogen como intención nueva y entran por Producción como `TL-004` cuando el owner las declare. Cerrar una entrega que cumplió y abrir un timeline nuevo para lo que sigue es más limpio que dejar un `VE` abierto indefinidamente — un `VE` que no cierra nunca deja de ser un gate.

**Deuda declarada:** los 18 ítems no se recorrieron uno por uno. Si en la próxima iteración aparece un problema que la checklist habría atrapado, el aprendizaje es que el juicio global no reemplaza al instrumento.

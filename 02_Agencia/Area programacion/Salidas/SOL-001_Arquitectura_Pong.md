# SOL-001 — Arquitectura del Pong (Propuesta)

- **RQ:** TL-001 / RQ-001.1 … RQ-001.6 · **GDS:** GDS-001.1 … GDS-001.5
- **Estado:** Propuesta (⟵ requiere aprobación del maintainer antes de ejecutar)
- **Entorno:** Unity 2022.3 LTS, Built-in RP, Input Manager clásico.

## Diagnóstico (Analista Técnico)
El prototipo previo (`Ball`, `Paddle`, `GameManager`, `GameBootstrap`, `PongAutoSetup`) funciona pero **viola SRP**: `GameBootstrap` arma todo, `GameManager` mezcla estado+score+UI (OnGUI), valores hardcodeados y sin estados de juego, menú, pausa ni juice. Se reconstruye limpio sobre los GDS. Se conserva la idea buena del prototipo: **auto-setup por Editor** (evita YAML de escena a mano) y **física determinista** (sin Rigidbody peleando con control manual).

## Principios aplicados (Core)
SOLID (SRP: una responsabilidad por clase) · separación **estructura/algoritmo/consumidor** · **managers coordinan, no absorben** · **UI muestra, no decide** · **arquitectura por eventos** (evita `FindObjectsOfType`/cálculo inútil en Update) · **balance configurable** vía ScriptableObject (cero hardcodeo).

## Componentes propuestos

| Clase | Responsabilidad | RQ/GDS |
|---|---|---|
| `PongConfig` (ScriptableObject) | Todos los parámetros de balance y cancha. Fuente única de valores. | .1–.6 |
| `GameStateMachine` | Estados Menu/Playing/Paused/GameOver + `OnStateChanged`. Habilita/congela gameplay. No absorbe score ni UI. | .4 |
| `PaddleController` | Input por jugador (binding configurable) + movimiento con clamp. Lee velocidad de config. | .1 |
| `BallController` | Movimiento determinista, saque, aceleración; **emite eventos** `OnPaddleHit/OnWallHit/OnGoal/OnServe`. | .2 |
| `BounceService` (clase pura, sin Unity) | Cálculo de reflexión/ángulo por impacto. Testeable en aislamiento. | .2 |
| `ScoreManager` | Escucha `OnGoal`, lleva score, evalúa `targetScore`, emite `OnScoreChanged/OnVictory`. Coordina, no dibuja. | .3 |
| `HUD` / `MenuPanel` / `PausePanel` / `GameOverPanel` (uGUI) | Muestran y comunican; se suscriben a eventos. No deciden lógica. | .3/.4 |
| `FeedbackController` | Escucha eventos y dispara SFX + flash/escala + shake. Desacoplado y desactivable. | .5 |
| `CameraShake` | Utilitario de shake configurable. | .5 |
| `SceneBootstrap` + `PongSceneBuilder` (Editor) | Arma cámara, luz y **cancha contorneada** con dimensiones de `PongConfig`. Auto-setup robusto. | .6 |

## Flujo de datos (eventos, sin acoplar)
`BallController` emite → `ScoreManager` y `FeedbackController` escuchan. `ScoreManager` emite `OnVictory` → `GameStateMachine` va a GameOver. UI se suscribe a estado/score. Nadie busca a nadie por `Find`.

## Alternativas descartadas
- **Rigidbody dinámico** para la pelota → no determinista para Pong. Se usa movimiento manual + `BounceService`.
- **Todo en OnGUI** → no escala; se usa Canvas uGUI.
- **GameManager monolítico** → viola SRP; se separa en State + Score + Feedback.

## Configurables (desde Inspector/SO, nada hardcodeado)
Velocidades y límites de paleta; base/max/step de pelota; ángulo máximo; delay y jitter de saque; `targetScore`; volumen SFX; flash; shake (on/off, magnitud, duración); dimensiones de cancha.

## Riesgos
- Sin playtest, el balance puede requerir ajuste → todo expuesto en `PongConfig`.
- Construcción de escena → se mantiene auto-setup por Editor para no depender de YAML frágil.

## Alcance a aprobar
Implementar las 10 clases de la tabla + `PongConfig` + escena auto-armada + UI de menú/pausa/fin + SFX/juice, en `Desktop\a\vaultrumtest2` (reemplazando el prototipo). Salida: **EJ-001.1 … EJ-001.6**.

> **GATE:** ¿Apruebo este alcance para ejecutar? Si sí, paso al Ejecutor Técnico y construyo. Si querés recortar (ej. dejar juice para después), lo ajusto antes de tocar código.

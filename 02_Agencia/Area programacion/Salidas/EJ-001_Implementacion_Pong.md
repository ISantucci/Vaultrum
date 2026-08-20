# EJ-001 — Implementación del Pong

- **SOL:** [[SOL-001_Arquitectura_Pong]] · **RQ:** RQ-001.1..6 · **GDS:** GDS-001.1..5
- **Estado:** Reportada (revisión estática OK) · **Entorno:** Unity 2022.3 LTS
- **Ubicación:** `Desktop\a\vaultrumtest2` (reemplaza el prototipo)

## Ejecución
Aprobado por el owner saltar el gate ("que el programador se ponga de una"). Se implementó el alcance completo de SOL-001.

## Archivos creados
- `Assets/Scripts/PongConfig.cs` — ScriptableObject con todo el balance (RQ .1–.6).
- `Assets/Scripts/GameState.cs` — enum + `GameStateMachine` (RQ .4).
- `Assets/Scripts/BounceService.cs` — algoritmo de rebote puro (RQ .2).
- `Assets/Scripts/PaddleController.cs` — paletas (RQ .1).
- `Assets/Scripts/BallController.cs` — pelota + eventos (RQ .2).
- `Assets/Scripts/ScoreManager.cs` — score y victoria (RQ .3).
- `Assets/Scripts/FeedbackController.cs` — SFX + flash + shake (RQ .5).
- `Assets/Scripts/CameraShake.cs` — screen shake (RQ .5).
- `Assets/Scripts/UIController.cs` — Canvas/paneles por estado (RQ .3/.4).
- `Assets/Scripts/GameController.cs` — flujo/input de estados (RQ .4).
- `Assets/Scripts/PongBootstrap.cs` — arma escena y cablea eventos (RQ .6).
- `Assets/Editor/PongSceneBuilder.cs` — auto-setup de escena.
- `Packages/manifest.json`, `ProjectSettings/ProjectVersion.txt`, `README.md`.

## Archivos eliminados (prototipo)
`Ball.cs`, `Paddle.cs`, `GameManager.cs`, `GameBootstrap.cs`, `PongAutoSetup.cs`.

## Checklist de cierre (Revisor)
```
[x] Usa criterio del Core (SOLID, managers coordinan, UI muestra, eventos)
[x] SOLID / separación de responsabilidades (10 clases, 1 responsabilidad c/u)
[x] Sin hardcodeo: todo el balance en PongConfig (SO)
[x] Respetó el alcance aprobado (RQ .1–.6)
[x] Reutilizó lo bueno del prototipo (auto-setup, física determinista)
[x] Expansible y mantenible (config + eventos)
[x] Configurable desde Unity (ScriptableObject/Inspector)
[x] Trazable: TL → RQ → GDS → SOL → EJ
```
Revisión estática: llaves/paréntesis balanceados en los 12 scripts; tipos de eventos compatibles en el cableado.

## Pendiente / riesgo
- Falta prueba en Unity real (no se pudo compilar/ejecutar el editor desde acá). El balance puede requerir ajuste fino en playtest — todo expuesto en `PongConfig`.

## Aprendizaje reutilizable (a Conocimiento)
Patrón "Bootstrap arma escena + cablea eventos" y `BounceService` como algoritmo puro testeable son candidatos a volver al Core. Derivar a `vaultrum-conocimiento` al cerrar.

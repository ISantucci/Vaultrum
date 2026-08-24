## Solución ejecutada

[[SOL-003_Arquitectura_Pong3D]] — cubre `RQ-003.1` a `RQ-003.7` del [[TL-003_Pong3D_Unity6_Cadena_Completa]].

Destino: `C:\Users\ControlEquipos\Desktop\a\vaultrumtest2` (carpeta vacía; la implementación de `EJ-002` nunca había aterrizado ahí).

## Archivos creados

**17 scripts C# + 4 de proyecto.** Ninguno usa el módulo de física. Ningún asset binario.

| Capa | Archivos |
|------|----------|
| `Scripts/` | `PongBootstrap.cs` — único MonoBehaviour con `Update` |
| `Scripts/Config` | `PongConfig.cs` (balance + `PongPalette`) |
| `Scripts/Core` | `GameState.cs` · `SessionSettings.cs` · `ScoreTracker.cs` · `MatchDirector.cs` |
| `Scripts/Gameplay` | `PongKeys.cs` · `IPaddleInput.cs` (+ `KeyboardPaddleInput`) · `PaddleController.cs` · `BallController.cs` |
| `Scripts/Presentation` | `SceneBuilder.cs` · `UiFactory.cs` · `GameHud.cs` · `ScreenStack.cs` · `FeedbackDirector.cs` · `ProceduralAudio.cs` |
| `Editor` | `PongSceneBootstrap.cs` |
| Proyecto | `Packages/manifest.json` · `ProjectSettings/ProjectVersion.txt` · `README.md` · `.gitignore` |

## Qué se implementó por requerimiento

| RQ | Estado | Dónde |
|----|--------|-------|
| `003.1` Setup + arena | Implementado | `SceneBuilder`: piso, dos paredes, línea central de 11 tramos, **líneas de gol en el color de cada jugador** (criterio de aceptación "se distingue pared de gol"), cámara `(0,21,−16)` a 52° con FOV 46, una direccional, ambiente plano. `PongSceneBootstrap` genera la escena y la registra en Build Settings |
| `003.2` Paletas | Implementado | `PaddleController` + `KeyboardPaddleInput`. Rampa simétrica de 80 ms, clamp sobre la posición final, `W`+`S` simultáneas se cancelan, velocidad expuesta para el spin |
| `003.3` Pelota | Implementado | `BallController`. Dial de puntería por offset de impacto, spin de paleta al 25 %, aceleración lineal con techo, substepping + cruce de plano con Z interpolada, guardias de ángulo mín/máx |
| `003.4` Marcador / saque / victoria | Implementado | `ScoreTracker` + `PongBootstrap`. Saque hacia quien recibió el gol, pausa de 1 s, punto de partido expuesto, revancha sin recargar escena |
| `003.5` Estados y flujo | Implementado | `MatchDirector` (6 estados) + `ScreenStack` (menú, opciones, pausa, fin). Pausa por estado, `ESC` siempre atrás, opciones que se aplican en la partida siguiente |
| `003.6` Game feel | Implementado | `FeedbackDirector` + `ProceduralAudio` (5 clips sintetizados). Jerarquía pared < paleta < gol < victoria, hit-stop sin `timeScale`, sacudida con techo duro, tono del rally ascendente |
| `003.7` Onboarding | Implementado | `ScreenStack` (bloques de control por lado en el menú) + `GameHud` (hint de 2 s junto a cada paleta en el primer saque, color por jugador, jerarquía 5:1) |

## Desvíos respecto de la SOL (declarados)

**1. La estela va en un GameObject hijo de la pelota.** Un GameObject no admite dos `Renderer`, y la pelota ya tiene `MeshRenderer`. El hijo lleva una escala inversa para que el ancho del trail no herede la escala de la esfera. Detectado en verificación, no en runtime.

**2. La cuenta de saque muestra `SAQUE` en vez de un número descendente.** Con `serveDelay = 1.0 s` un contador de 3-2-1 no tiene tres segundos que contar, y un contador de un solo dígito parpadeando durante un segundo es ruido. El `UXS-003.5` pide "cuenta visible" y esto lo cumple; si `serveDelay` sube a 2 s o más, conviene volver al número. **Deuda declarada.**

**3. No se creó `ProjectSettings/ProjectSettings.asset`.** Se deja que Unity lo genere con sus defaults al abrir. Escribirlo a mano es la segunda forma más común de dejar un proyecto sin abrir, después de la escena. La contrapartida es que *Active Input Handling*, la resolución por defecto y el nombre del producto quedan en default — y por eso `PongKeys` no depende de esa casilla (decisión 6 del `SOL`).

## Verificación hecha

**Compilación verificada fuera de Unity.** Los 17 scripts se compilaron con `mcs` contra un stub de la API de Unity que se usa en el proyecto, en las dos configuraciones de defines:

```txt
[x] -define:ENABLE_LEGACY_INPUT_MANAGER                          → 0 errores
[x] -define:ENABLE_INPUT_SYSTEM;ENABLE_LEGACY_INPUT_MANAGER      → 0 errores
```

Esto **no** reemplaza abrir Unity: verifica sintaxis, tipos y firmas del código propio, no que la escena se genere, que los materiales resuelvan el shader `Standard` ni que el juego se sienta bien. Es exactamente la distinción que dejó `VE-002_Pong3D` en PAUSADO — *verificar el código no es verificar la entrega* — y por eso se declara acá con su alcance en vez de presentarse como validación.

**Revisión de contrato hecha leyendo el código:**

```txt
[x] Ningún Collider ni Rigidbody se crea en la escena (se destruyen los de los primitivos)
[x] Ningún GetComponent / Instantiate / Destroy / LINQ dentro del Update
[x] Las 4 suscripciones al FeedbackDirector están aisladas y son comentables en bloque
[x] El marcador solo se redibuja en ScoreChanged; el rally solo cuando cambia
[x] Todo el balance está en un único campo serializado (config), sin valores mágicos sueltos
[x] Las paletas se tickean siempre antes que la pelota, en un solo lugar
[x] Los seis estados tienen al menos una transición saliente (revisado contra la tabla del UXS)
```

## Riesgos abiertos (no hallazgos)

1. **El proyecto nunca se abrió en Unity.** No está probado que la escena se genere, que el shader `Standard` resuelva ni que `LegacyRuntime.ttf` esté disponible en esta versión.
2. **El balance se fijó sin jugar.** Todos los valores caen dentro del rango del libro [[01_Pong]] (tabla de traducción en `GDS-003.0`), pero un rango no es un playtest.
3. **El encuadre de cámara se calculó, no se miró.** `(0,21,−16)`, 52°, FOV 46 da margen sobre una arena de 26 × 15 en 16:9 según el cálculo. Hay que verlo.
4. **Los caracteres `↑ ↓ ‹ › ▸ ¡` dependen de que la fuente los tenga.** Si alguno sale como cuadrito, es cosmético y se reemplaza por texto.

## Estado

**Reportada.** Pasa a `VE-003` del Área de Producción.

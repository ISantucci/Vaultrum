## Requerimientos

`RQ-003.1` a `RQ-003.7` del `TL-003_Pong3D_Unity6_Cadena_Completa`, con `GDS-003.0_Marco_Comun`, `GDS-003.2` a `GDS-003.7`, `UXS-003.5_Flujo_De_Pantallas` y `UXS-003.7_HUD_Y_Onboarding` como insumos cerrados.

Destino: `C:\Users\ControlEquipos\Desktop\a\vaultrumtest2`.

## Criterio que ordena todas las decisiones

**Cada decisión técnica se justifica contra un requerimiento, no contra un principio.**

Esto es una corrección deliberada de rumbo. En una escena de veinte objetos es facilísimo aplicar criterio de ingeniería excelente —evitar el GC, apagar sistemas del motor, minimizar saltos managed↔native— a problemas que nadie tiene. Eso es *scope no pedido*: trabajo de calidad que consume el presupuesto que debía ir a la experiencia (riesgo #5 de TL-003).

La regla operativa que se aplica es más chica y más honesta: **no encender maquinaria que ningún requerimiento pidió.** Que es distinto de *optimizar por deporte*.

## Decisiones

### 1. Sin motor de física

**Requerimiento:** `RQ-003.3` — table-stake #2 del libro `01_Pong`: la pelota nunca atraviesa nada, y una pelota que atraviesa la paleta es una violación del pilar de justicia.

Un `Rigidbody` + `Collider` por objeto hace que PhysX corra broadphase, narrowphase, resolución de contactos y sincronización de transforms para una esfera y cuatro planos. Pero el argumento decisivo **no es el costo**: es que el rebote de Pong **no es físico**. El ángulo se deriva del punto de impacto (`GDS-003.3`, regla 3), no de la normal. Usar PhysX obligaría a pelearle su propia resolución de colisión para imponerle una regla de diseño.

**Consecuencia asumida:** sin colliders no hay CCD gratis, así que la continuidad hay que resolverla a mano (decisión 3).

### 2. Un solo `MonoBehaviour` con `Update`

**Requerimiento:** `GDS-003.3`, regla 4 — el spin lee la velocidad de la paleta **en el instante del golpe**. Si las paletas y la pelota fueran `MonoBehaviour` separados, el orden de ejecución quedaría a merced de la configuración de *execution order* del proyecto, y una inversión haría que el spin leyera la velocidad del frame anterior. Sería un bug de gameplay intermitente, no un problema de rendimiento.

`PongBootstrap` orquesta: paletas → pelota → HUD, siempre en ese orden y visible en once líneas. `PaddleController`, `BallController`, `ScoreTracker` y `MatchDirector` son clases normales, testeables sin abrir el editor.

**Nota:** el ahorro de saltos managed↔native es real pero es un efecto colateral, no la razón. Con veinte objetos no habría hecho falta.

### 3. Continuidad por cruce de plano + substepping

**Requerimiento:** `RQ-003.3`, criterio de aceptación *"a velocidad máxima, con la paleta quieta, la pelota nunca la atraviesa"*.

Dos mecanismos combinados:

- **Substepping:** el desplazamiento del frame se parte en pasos de largo máximo `min(radio, medioAncho) = 0.25 u`. A 23 u/s y 60 fps el paso es 0.383 u → dos sub-pasos.
- **Cruce de plano:** dentro de cada sub-paso, la pregunta no es *"¿la pelota está dentro de la paleta?"* sino *"¿cruzó el plano de la paleta este paso?"*, interpolando la Z exacta del cruce. Es continuo de verdad y cuesta dos multiplicaciones.

El orden importa: **paletas primero, paredes después**. Al revés, una pelota que rebota en la pared en el mismo sub-paso en que cruza el plano de la paleta calcularía el punto de impacto con la Z ya reflejada.

### 4. Todo por código, cero assets

**Requerimiento:** riesgo #2 de `TL-003` y el aprendizaje de `VE-002_Pong3D` (*la entrega nunca aterrizó*).

Ni prefabs, ni materiales, ni canvas cableado, ni clips de audio. La razón **no** es el peso del repositorio: es que un proyecto sin referencias no tiene referencias que se rompan. Ningún GUID que se desincronice, ningún `.wav` mal importado, ninguna escena YAML mal formada que impida abrir el proyecto.

**Contrapartida declarada:** un objeto que solo existe en código es más difícil de ajustar a ojo para alguien que trabaja en el editor. Se mitiga poniendo todo el balance en un solo campo del Inspector, editable en Play.

### 5. La escena la genera Unity, no nosotros

**Requerimiento:** riesgo #2 de `TL-003`.

`Assets/Editor/PongSceneBootstrap.cs` crea `Assets/Scenes/Pong.unity` con un único GameObject la primera vez que se abre el proyecto, y la registra en Build Settings. Una escena YAML escrita a mano que salga mal deja el proyecto **sin abrir**; que la genere Unity elimina esa clase de error entera.

**Contrapartida declarada:** es un script de editor que toca el proyecto al importar. Solo actúa si la escena no existe, y después no hace nada más. Hay además un `Vaultrum → Regenerar escena Pong` manual.

### 6. Entrada con doble camino por defines

**Requerimiento:** riesgo #3 de `TL-003`.

Si *Active Input Handling* quedara en "Input System only", `Input.GetKey` lanza excepción; si quedara en "Input Manager only", `Keyboard.current` es null. `PongKeys` implementa los dos caminos, prefiere el nuevo si está disponible y cae al viejo si no. Nueve teclas, treinta líneas, y el proyecto deja de depender de una casilla de configuración.

### 7. Feedback por eventos, desmontable entero

**Requerimiento:** `GDS-003.6`, regla 8 y su criterio de validación.

Ningún sistema de gameplay conoce cámara, audio ni interfaz. Cuatro suscripciones en `Awake` conectan el `FeedbackDirector`. Comentarlas deja el juego jugable, feo, y con exactamente las mismas trayectorias y puntajes. Esa propiedad es el criterio de validación, no una consecuencia agradable.

### 8. Hit-stop sin `timeScale`

**Requerimiento:** `GDS-003.5`, regla 4 y `GDS-003.6`, regla 2.

`timeScale = 0` es global: apaga también la interfaz y cualquier cosa que espere tiempo real, y es una fuente clásica de estados muertos. Acá el hit-stop es un contador en `PongBootstrap` que saltea el tick de gameplay; la presentación sigue corriendo en `unscaledDeltaTime`, así que la sacudida y el squash siguen vivos **durante** el congelamiento — que es justo lo que hace que se sienta un impacto y no un tirón.

### 9. Optimizaciones que sí tienen requerimiento (y las que no se hicieron)

| Se hizo | Requerimiento detrás |
|---------|---------------------|
| Marcador por evento, con tabla de strings precalculada | `GDS-003.4`: es texto grande y estático; redibujarlo 60 veces por segundo es trabajo que nadie pidió |
| Contador de rally solo cuando cambia | Igual que arriba |
| Materiales compartidos, sombras/probes apagadas por renderer | `RQ-003.1`: la pelota tiene que leerse contra el piso. Las sombras y las probes agregan ruido visual sin aportar a la legibilidad |
| Near/far clip ajustados al tamaño real | Precisión de z-buffer, gratis |

| **No se hizo** | **Por qué** |
|---|---|
| Pool de partículas | No hay partículas: `GDS-003.6` las descarta por competir con la legibilidad de la pelota |
| Loop de simulación a paso fijo con interpolación | Nadie pidió determinismo entre máquinas ni replays. La simulación es determinista *por frame* y eso alcanza para un juego local |
| Occlusion culling, batching manual, instancing explícito | Veinte objetos. Sería resolver un problema de escenas grandes |
| Presupuesto de asignaciones cero en todo el loop | Se cumple donde hay un motivo (marcador, rally). Perseguirlo por deporte sería scope no pedido |

La fila del loop a paso fijo es la más discutible y por eso está declarada: **si alguna vez se agrega red o replay, esa decisión se revisa.** Hoy no hay requerimiento que la pida.

## Arquitectura

```txt
PongBootstrap  (unico MonoBehaviour con Update)
├── SceneBuilder ─────────► arena, paletas, pelota, camara, luz     (RQ-003.1)
├── UiFactory ────────────► canvas 1920x1080, labels, paneles       (UXS-003.5)
│    ├── GameHud ────────► franjas, marcador, rally, hints          (UXS-003.7)
│    └── ScreenStack ────► menu, opciones, pausa, fin               (UXS-003.5)
├── MatchDirector ───────► 6 estados, transiciones explicitas       (GDS-003.5)
├── ScoreTracker ────────► puntajes, punto de partido, victoria     (GDS-003.4)
├── PaddleController x2 ─► rampa, clamp, velocidad expuesta         (GDS-003.2)
│    └── IPaddleInput ──► KeyboardPaddleInput ─► PongKeys
├── BallController ──────► dial de punteria, spin, continuo, rally  (GDS-003.3)
└── FeedbackDirector ────► hit-stop, shake, squash, flash           (GDS-003.6)
     └── ProceduralAudio ► 5 clips sintetizados
```

**Orden del `Update`, explícito y en un solo lugar:**

```txt
1. feedback.TickUnscaled(udt)      ← sigue vivo durante el hit-stop
2. hud.TickUnscaled(udt)
3. HandleUiInput()                  ← la interfaz responde siempre, aun congelado
4. si hay freeze pendiente → return
5. paletas.Tick(dt)                 ← SIEMPRE antes que la pelota
6. pelota.Tick(dt, paletaL, paletaR)
7. hud.SetRally(...) solo si cambio
```

## Trazabilidad

| Archivo | Cubre |
|---------|-------|
| `Scripts/Config/PongConfig.cs` | Balance completo + paleta de color (`GDS-003.0`) |
| `Scripts/Core/GameState.cs` · `MatchDirector.cs` | `GDS-003.5` |
| `Scripts/Core/ScoreTracker.cs` · `SessionSettings.cs` | `GDS-003.4`, `GDS-003.5` |
| `Scripts/Gameplay/PongKeys.cs` · `IPaddleInput.cs` | `GDS-003.2`, riesgo #3 |
| `Scripts/Gameplay/PaddleController.cs` | `GDS-003.2` |
| `Scripts/Gameplay/BallController.cs` | `GDS-003.3` |
| `Scripts/Presentation/SceneBuilder.cs` | `RQ-003.1` |
| `Scripts/Presentation/UiFactory.cs` · `GameHud.cs` | `UXS-003.7` |
| `Scripts/Presentation/ScreenStack.cs` | `UXS-003.5` |
| `Scripts/Presentation/FeedbackDirector.cs` · `ProceduralAudio.cs` | `GDS-003.6` |
| `Scripts/PongBootstrap.cs` | Orquestación, `RQ-003.4`, `RQ-003.5` |
| `Editor/PongSceneBootstrap.cs` | `RQ-003.1`, riesgo #2 |

## Criterios de aceptación técnicos

- El proyecto abre en Unity 6 y compila sin errores.
- Comentar las cuatro suscripciones al `FeedbackDirector` deja el juego funcionando idéntico.
- Ningún `GetComponent`, `Instantiate`, `Destroy` ni LINQ dentro del loop.
- Ningún `Collider` ni `Rigidbody` en la escena.
- Todo el balance accesible desde un único campo del Inspector, editable en Play.

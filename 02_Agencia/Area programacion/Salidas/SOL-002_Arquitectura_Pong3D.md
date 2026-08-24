## Requerimiento y specs

Cubre el hilo completo de [[TL-002_Pong3D_2_Jugadores_Unity6]]: `RQ-002.1` a `RQ-002.6`, con `GDS-002.2` a `GDS-002.6`.

Los seis requerimientos comparten una única arquitectura. Partirlos en seis soluciones técnicas sería sobrearquitecturar (principio 5): el sistema tiene tres objetos móviles.

## Entorno (dado por Producción, no se re-decide)

Unity **6000.0.81f1** · Built-in RP · Input Manager legacy · uGUI · sin assets externos.

---

## Diagnóstico

Proyecto nuevo, carpeta vacía. No hay nada que reutilizar ni convenciones previas que respetar. La restricción real no es técnica sino de verificación: **no puedo abrir el editor**, así que toda decisión que dependa de que yo acierte un archivo binario o un YAML de Unity es una decisión frágil.

Del Core aplican: SOLID (SRP en la separación de sistemas, DIP en la entrada), *Clases puras* y *MonoBehaviour como puente*, *Medir antes de optimizar*, *Evitar allocations por frame*, *UI orientada a eventos*, *Cuándo NO crear un Manager*.

---

## Decisiones técnicas y alternativas descartadas

### 1. Movimiento propio, sin motor de física

**Decisión:** pelota y paletas se mueven con matemática propia; sin `Rigidbody`, sin `Collider`, sin el módulo de física.

**Por qué:** el `GDS-002.3` exige determinismo total (pilar 5: perder siempre es culpa del jugador) y un ángulo de rebote calculado desde el punto de impacto, no reflejado. Con física del motor habría que **pelear contra ella** para conseguir eso: cancelar restitución, congelar rotaciones, corregir el vector después de cada colisión. Se termina con física activa y anulada, que es lo peor de los dos mundos.

**Alternativa descartada:** `Rigidbody` + `PhysicMaterial` bounciness 1. Más idiomático, pero introduce no-determinismo, coste de solver, riesgo de tunneling que igual hay que resolver a mano, y el ángulo por offset queda como una corrección peleando con el motor.

**Consecuencia:** el proyecto no usa el módulo de física en absoluto. Coste de física por frame: cero.

### 2. Un manager que tickea, no objetos que se auto-actualizan

**Decisión:** `GameManager` es el único `Update` del gameplay. Llama a `Tick(dt)` de paletas y pelota **solo en los estados donde corresponde**.

**Por qué:** el `GDS-002.5` regla 2 lo pide explícitamente. La alternativa habitual —cada objeto con su `Update` consultando `if (state != Playing) return;`— reparte la máquina de estados en todos los archivos y es la vía directa a bugs de pausa.

**Alternativa descartada:** `UpdateManager` genérico del Core (registro/desregistro, listas de suscriptores). Es la herramienta correcta para cientos de objetos; acá hay tres. Aplicarlo sería sobrearquitectura (principio 5, y *Cuándo NO crear un Manager*).

### 3. Configuración en ScriptableObject + copia de sesión

**Decisión:** `PongConfig` (ScriptableObject) contiene todo el balance. Al arrancar se copia a un `MatchSettings` mutable en memoria; el menú de opciones edita la copia.

**Por qué:** cero hardcodeo, y editar el asset en Play Mode dejaría cambios persistidos en disco sin que el owner lo pidiera. El asset es el default; la copia es la sesión.

### 4. Eventos C# tipados

**Decisión:** `event Action<...>` en C# plano. No `UnityEvent`, no `SendMessage`, no un event bus global.

**Por qué:** el `GDS-002.6` regla 1 exige que quitar todo el feedback no altere una trayectoria. Los `Action` son verificables en compilación, no asignan al invocarse y no requieren una capa de infraestructura. Un event bus global para 5 eventos es una capa sin necesidad real.

**Riesgo asumido:** hay que desuscribirse en `OnDisable`. Está cubierto en la implementación.

### 5. La escena se genera por script de editor

**Decisión:** un script en `Assets/Editor/` construye la escena con la API de Unity: arena, cámara, luces, paletas, pelota, canvas y el asset de configuración. Corre solo la primera vez que se abre el proyecto y queda como menú `Vaultrum ▸ Regenerar escena Pong`.

**Por qué:** es la mitigación del riesgo principal del `TL`. Un `.unity` escrito a mano es un YAML con GUIDs y `fileID` que no puedo validar sin abrir el editor; un script de generación usa la misma API que usaría una persona y es determinístico.

**Alternativa descartada:** escribir el `.unity` a mano. Alternativa descartada: crear todo en runtime desde un bootstrap — funcionaría, pero deja al owner sin nada que tocar en el Inspector, que es justo lo que un proyecto Unity tiene que ofrecer.

### 6. uGUI con texto legacy

**Decisión:** `UnityEngine.UI.Text` con la fuente incorporada `LegacyRuntime.ttf`.

**Por qué:** TextMeshPro requiere importar "TMP Essential Resources" desde un diálogo manual. Un proyecto que no abre y corre de una viola el criterio de entrega. Es deuda declarada: migrar a TMP es un cambio acotado si el owner lo quiere.

### 7. Audio generado por código y cacheado

**Decisión:** los `AudioClip` se sintetizan una vez en el arranque con `AudioClip.Create` + `SetData`, con envolvente ataque/caída. Se reproducen con `PlayOneShot` sobre un `AudioSource` fijo.

**Por qué:** sin archivos externos (restricción del `TL`) y sin asignación por evento.

### 8. Entrada detrás de una interfaz

**Decisión:** `IPaddleInput` con una sola operación: devolver la dirección en `[-1, 1]`. `KeyboardPaddleInput` la implementa con `KeyCode` configurables.

**Por qué:** DIP del Core. Sumar gamepad más adelante es una clase nueva, sin tocar el movimiento de la paleta.

---

## Estructura

```txt
Assets/
  Editor/
    PongSceneBuilder.cs        generación de escena + assets + auto-arranque
  Scripts/
    Config/
      PongConfig.cs            ScriptableObject: todo el balance
      MatchSettings.cs         copia mutable de sesión
    Core/
      GameState.cs             enum de estados
      GameEvents.cs            eventos tipados del gameplay
      ScoreTracker.cs          clase pura, sin MonoBehaviour
      Arena.cs                 struct de límites, cálculo de clamps
    Gameplay/
      GameManager.cs           máquina de estados + único Update
      PaddleController.cs      movimiento, clamp, escala base
      BallController.cs        movimiento por sub-pasos, rebotes, saque
      IPaddleInput.cs          abstracción de entrada
      KeyboardPaddleInput.cs   implementación por teclado
    Presentation/
      CameraShake.cs           sacudida sin deriva
      HitPunch.cs              estirón de escala no acumulativo
      ProceduralAudio.cs       síntesis y cache de clips
      GameHud.cs               marcador y cuenta regresiva, por evento
      MenuScreens.cs           menú, opciones, pausa, fin
```

Ningún archivo de gameplay referencia a `Presentation`. La dependencia va en un solo sentido.

---

## Parámetros configurables

Todos los del `GDS-002.2` al `GDS-002.6`, en `PongConfig`, con rangos declarados en el Inspector. **Cero valores de balance escritos en el código de gameplay.**

---

## Riesgos técnicos

| Riesgo | Mitigación |
|--------|------------|
| El proyecto no compila y no puedo verlo | Sin dependencias de paquetes opcionales; API estable desde 2019; sin `#if` de plataforma |
| La generación de escena falla a mitad | Es idempotente: borra y rehace. El menú permite regenerar |
| Balance a ciegas | Todo en el Inspector con rangos; el `VE` puede quedar en *Ajustar* |
| Deriva de cámara por sacudidas | La sacudida se aplica sobre una posición base guardada, nunca acumulando offsets |

---

## Gate de aprobación

Esta solución cubre los seis requerimientos con una sola arquitectura, sin física del motor, sin paquetes extra y sin assets externos. **Alcance a ejecutar:** los 13 archivos listados más la estructura de proyecto.

`EJ-002` registra lo efectivamente implementado.

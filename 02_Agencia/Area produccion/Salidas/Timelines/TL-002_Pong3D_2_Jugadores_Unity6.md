> **SUPERSEDIDO por `TL-003_Pong3D_Unity6_Cadena_Completa`** — su `VE-002` quedó PAUSADO y su implementación nunca aterrizó en disco. TL-003 rehace la cadena cargando el libro `01_Pong` (que en ese momento estaba vacío) y agregando `UXS` y onboarding. Este timeline queda como antecedente cerrado; no se reabre.

## Objetivo

Un **Pong 3D para dos jugadores locales**, completo y pulido, construido en Unity 6 con criterio Vaultrum: sin hardcodeo de balance, sin costo por frame evitable, y con una entrega que se sostenga sola frente a un jugador (no un MVP que compila).

Proyecto nuevo, carpeta vacía: `C:\Users\ControlEquipos\Desktop\a\vaultrumtest2`.

---

## Área afectada

Producción (dueña de la entrega) → Game Design → Programación → Producción (`VE`).

**Level Design:** no interviene. El sistema no tiene dimensión espacial que componer: la "cancha" es el propio sistema de reglas, no un nivel con recorrido, encuentros ni pacing intra-nivel. Declarado explícitamente (no es omisión silenciosa).

**UI/UX:** no se abre área propia. La interfaz es un HUD de marcador y tres pantallas de menú; el `GDS` de estados define la información y el feedback, y Programación la construye. Si la interfaz creciera (opciones anidadas, remapeo de controles), se abre `UXS`.

---

## Restricción de entorno (dada, no se re-decide)

| Ítem | Valor | Origen |
|------|-------|--------|
| Motor | Unity **6000.0.81f1** (Unity 6 LTS) | elegido por el owner entre 5 instaladas |
| Render pipeline | **Built-in** | elegido por el owner |
| Input | **Input Manager legacy** (`Input.GetKey`) | decisión de Producción: cero configuración, sin paquete extra, sin assets que no puedo validar sin abrir el editor. Intercambiable después por el `IPaddleInput` del diseño. |
| UI | **uGUI** (`com.unity.ugui`), texto legacy | evita el import manual de TMP Essential Resources |
| Assets externos | **ninguno** | audio procedural, materiales por código, primitivas |

---

## Criticidad

Alta. Es la primera corrida completa de la Agencia refactorizada (cadena `TL → RQ → GDS → SOL → EJ → VE`) sobre un proyecto real.

---

## Requerimientos asociados

| RQ | Título | Jugable |
|----|--------|---------|
| RQ-002.1_Setup_Proyecto_Arena3D | Setup de proyecto Unity 6 y arena 3D | No |
| RQ-002.2_Paletas_Controlables | Paletas controlables para dos jugadores | Sí |
| RQ-002.3_Pelota_Rebote_Aceleracion | Pelota: rebote, ángulo por impacto y aceleración | Sí |
| RQ-002.4_Score_Victoria_Reinicio | Marcador, condición de victoria y reinicio | Sí |
| RQ-002.5_Estados_Menus | Estados de juego, menús y opciones | Sí |
| RQ-002.6_Game_Feel_Audio | Game feel y audio procedural | Sí |

---

## Secuencia de trabajo

```txt
RQ-002.1  Setup + arena          → Programación (no jugable, directo)
RQ-002.2  Paletas               → GDS → Programación
RQ-002.3  Pelota                → GDS → Programación
RQ-002.4  Score / victoria      → GDS → Programación
RQ-002.5  Estados / menús       → GDS → Programación
RQ-002.6  Game feel / audio     → GDS → Programación
   ↓
SOL-002 (arquitectura única para el conjunto) → EJ-002 (implementación)
   ↓
VE-002  validación de entrega del TL
```

`SOL`/`EJ` se resuelven como un solo hilo: los seis requerimientos comparten una única arquitectura (config + máquina de estados + tick central). Partirlos en seis soluciones técnicas sería sobrearquitecturar (principio 5).

---

## Dependencias

- `RQ-002.2` y `RQ-002.3` dependen de la arena de `RQ-002.1` (límites de rebote y de movimiento).
- `RQ-002.4` depende de `RQ-002.3` (el punto se detecta cuando la pelota sale por un fondo).
- `RQ-002.5` envuelve a todos: la máquina de estados gobierna qué se actualiza.
- `RQ-002.6` se engancha sobre eventos de `002.3` y `002.4`; no los modifica.

---

## Riesgos

| Riesgo | Mitigación |
|--------|------------|
| No puedo abrir Unity para validar: escena, assets y compilación se generan a ciegas | La escena no se escribe a mano en YAML: la genera un script de editor con la API de Unity, que es determinística. Cero dependencias de paquetes que requieran import manual. |
| Tunneling de la pelota a alta velocidad | Movimiento por sub-pasos acotados por el objeto más fino de la arena. Definido en el `GDS` de pelota. |
| Balance a ciegas (no puedo playtestear) | Todo valor de balance queda en un ScriptableObject editable desde el Inspector, con rangos declarados. El `VE` va a quedar en **Ajustar** si el owner detecta que el feel no cierra. |
| Sobrearquitectura por "hacerlo bien" | Un solo manager, sin Service Locator, sin UpdateManager global, sin pooling: el juego tiene 3 objetos móviles. La optimización se juega en no gastar, no en agregar capas. |

---

## Criterios de cierre del timeline

- Los seis `RQ` tienen su `GDS` (los cinco jugables) y quedan cubiertos por `SOL-002` + `EJ-002`.
- El proyecto abre en Unity 6000.0.81f1 y entra a Play sin pasos manuales más allá de abrir la escena.
- La definición de terminado del `VE` se cumple sobre el juego corriendo.
- `VE-002` en estado **Cerrado**.

## Índice de UI/UX Specs (UXS)

Registro de todas las specs de interfaz del Área de UI/UX.

Cada `UXS-XXX.n` es la capa de comunicación jugador↔juego diseñada y validada para un `GDS-XXX.n`.

---

## Registro

### TL-003 — Pong 3D, cadena completa

- [[UXS-003.5_Flujo_De_Pantallas|UXS-003.5 Flujo de pantallas]] — seis pantallas, mapa de navegación y reglas de interacción por teclado, para `GDS-003.5`
- [[UXS-003.7_HUD_Y_Onboarding|UXS-003.7 HUD y onboarding]] — HUD de juego, jerarquía visual, código de color redundante y onboarding del primer saque, para `GDS-003.7`

Las dos cerradas.

---

## Regla

- Un `UXS` cuelga siempre de un `GDS` (hereda número base y subnumeración).
- Estados posibles: En análisis / En diseño / En validación / Cerrada / Rebotada.
- El `UXS` declara su `GDS` (y su `LDS` si aplica) en su propia ficha, y el índice lo nombra. El resultado de la validación queda en el `UXS`.
- Un `UXS` cerrado es insumo del `SOL` del Área de Programación (junto al `GDS` y, si existe, el `LDS`).

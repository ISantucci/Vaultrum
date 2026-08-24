## Índice de Game Design Specs (GDS)

Registro de todas las specs de diseño del Área de Game Design.

Cada `GDS-XXX.n` es un sistema jugable diseñado y validado para un `RQ-XXX.n`.

---

## Registro

### TL-001 — Pong 2 jugadores

- [[GDS-001.1_Paletas|GDS-001.1 Paletas]] — paletas controlables, para `RQ-001.1`
- [[GDS-001.2_Pelota|GDS-001.2 Pelota]] — rebote y aceleración, para `RQ-001.2`
- [[GDS-001.3_Score_Victoria|GDS-001.3 Score y victoria]] — para `RQ-001.3`
- [[GDS-001.4_Estados|GDS-001.4 Estados]] — menú, pausa y reinicio, para `RQ-001.4`
- [[GDS-001.5_Game_Feel|GDS-001.5 Game feel]] — feedback, para `RQ-001.5`

Las cinco cerradas.

### TL-002 — Pong 3D en Unity 6

- [[GDS-002.2_Paletas|GDS-002.2 Paletas]] — control directo y clamp, para `RQ-002.2`
- [[GDS-002.3_Pelota|GDS-002.3 Pelota]] — ángulo por impacto, aceleración y anti-tunneling, para `RQ-002.3`
- [[GDS-002.4_Score_Victoria|GDS-002.4 Score y victoria]] — con reinicio, para `RQ-002.4`
- [[GDS-002.5_Estados|GDS-002.5 Estados]] — menús y opciones, para `RQ-002.5`
- [[GDS-002.6_Game_Feel|GDS-002.6 Game feel]] — audio procedural, para `RQ-002.6`

Las cinco cerradas. El `RQ-002.1` (setup de proyecto) no tiene `GDS`: no hay sistema jugable que diseñar.

### TL-003 — Pong 3D, cadena completa

- [[GDS-003.0_Marco_Comun|GDS-003.0 Marco común]] — geometría, paleta de color, contrato de eventos y omisiones declaradas; cuelga del `TL-003`, no de un `RQ`
- [[GDS-003.2_Paletas|GDS-003.2 Paletas]] — rampa de aceleración y peso, para `RQ-003.2`
- [[GDS-003.3_Pelota|GDS-003.3 Pelota]] — dial de puntería, spin de paleta y continuo por cruce de plano, para `RQ-003.3`
- [[GDS-003.4_Score_Saque_Victoria|GDS-003.4 Score, saque y victoria]] — saque compensatorio y revancha, para `RQ-003.4`
- [[GDS-003.5_Estados|GDS-003.5 Estados]] — seis estados, transiciones explícitas, sin estados muertos, para `RQ-003.5`
- [[GDS-003.6_Game_Feel|GDS-003.6 Game feel]] — juice jerarquizado y pacing sonoro del rally, para `RQ-003.6`
- [[GDS-003.7_Onboarding_Legibilidad|GDS-003.7 Onboarding y legibilidad]] — redundancia color+lado y jerarquía del HUD, para `RQ-003.7`

Las siete cerradas. El `RQ-003.1` (setup de proyecto) no tiene `GDS`, por el mismo motivo.

---

## Regla

- Un `GDS` cuelga siempre de un `RQ` (hereda número base y subnumeración). **Única excepción: el `GDS-XXX.0`** (ver abajo).
- Un `GDS` declara si `LDS` y `UXS` aplican. Un "no aplica" dice **qué dimensión falta y por qué**; se comprueba al cerrar el `VE` con el test del "no aplica".
- Estados posibles: En diseño / En balance / En validación / Cerrada / Rebotada.
- El `GDS` declara su `RQ` en su propia ficha, y el índice lo nombra. El resultado de la validación queda en el `GDS`.
- Un `GDS` cerrado baja a **Level Design** (`LDS`) y/o **UI/UX** (`UXS`) cuando aplican, y de ahí —junto a ellos— al `SOL` del Área de Programación. Si ninguna aplica, el propio `GDS` lo declara y pasa directo a Programación.

---

## El marco común: `GDS-XXX.0`

Cuando **tres o más** `GDS` del mismo timeline comparten definiciones —geometría, paleta de color, contrato de eventos, convenciones de nombres, omisiones declaradas comunes— esas definiciones van a un `GDS-XXX.0` en vez de repetirse.

Es el único artefacto de la cadena que **no cuelga de un `RQ`**: cuelga del `TL`, igual que el `VE`. Por eso lleva `.0`.

```txt
GDS-XXX.0   marco común       cuelga de TL-XXX     (sin RQ propio)
GDS-XXX.n   spec del sistema  cuelga de RQ-XXX.n
```

Condiciones:

- Se abre **solo** con tres o más `GDS` que lo comparten. Con dos se repite y listo: un marco común para dos specs es sobrearquitectura (principio 5).
- Contiene **solo** lo compartido. Lo que usa un único `GDS` va en ese `GDS`.
- Los `GDS-XXX.n` lo referencian; no lo copian.
- No baja por su cuenta a Level Design ni UI/UX: viaja con los `GDS` que lo referencian.
- El `VE` lo verifica como parte de la entrega del timeline.

**Origen:** `GDS-003.0` se inventó durante el Pong 3D para no repetir seis veces la misma geometría y el mismo contrato de eventos. Funcionó, pero entró como excepción silenciosa a la columna vertebral de numeración — que es exactamente lo que el índice de la Agencia dice que no debe haber. Esta regla lo formaliza en vez de dejarlo como precedente tácito.

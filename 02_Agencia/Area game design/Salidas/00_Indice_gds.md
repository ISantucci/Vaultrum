## Índice de Game Design Specs (GDS)

Registro de todas las specs de diseño del Área de Game Design.

Cada `GDS-XXX.n` es un sistema jugable diseñado y validado para un `RQ-XXX.n`.

---

## Registro

| GDS | Requerimiento | Sistema | Estado |
|-----|---------------|---------|--------|
| [[GDS-001.1_Paletas]] | RQ-001.1 | Paletas controlables | Cerrada |
| [[GDS-001.2_Pelota]] | RQ-001.2 | Pelota: rebote y aceleración | Cerrada |
| [[GDS-001.3_Score_Victoria]] | RQ-001.3 | Score y victoria | Cerrada |
| [[GDS-001.4_Estados]] | RQ-001.4 | Estados: menú/pausa/reinicio | Cerrada |
| [[GDS-001.5_Game_Feel]] | RQ-001.5 | Game feel: feedback | Cerrada |
| [[GDS-002.2_Paletas]] | RQ-002.2 | Paletas: control directo y clamp | Cerrada |
| [[GDS-002.3_Pelota]] | RQ-002.3 | Pelota: angulo por impacto, aceleracion, anti-tunneling | Cerrada |
| [[GDS-002.4_Score_Victoria]] | RQ-002.4 | Score, victoria y reinicio | Cerrada |
| [[GDS-002.5_Estados]] | RQ-002.5 | Estados, menus y opciones | Cerrada |
| [[GDS-002.6_Game_Feel]] | RQ-002.6 | Game feel y audio procedural | Cerrada |
| [[GDS-003.0_Marco_Comun]] | TL-003 (marco) | Geometria, paleta de color, contrato de eventos, omisiones declaradas | Cerrada |
| [[GDS-003.2_Paletas]] | RQ-003.2 | Paletas con rampa de aceleracion y peso | Cerrada |
| [[GDS-003.3_Pelota]] | RQ-003.3 | Pelota: dial de punteria, spin de paleta, continuo por cruce de plano | Cerrada |
| [[GDS-003.4_Score_Saque_Victoria]] | RQ-003.4 | Marcador, saque compensatorio, victoria y revancha | Cerrada |
| [[GDS-003.5_Estados]] | RQ-003.5 | Seis estados, transiciones explicitas, sin estados muertos | Cerrada |
| [[GDS-003.6_Game_Feel]] | RQ-003.6 | Juice jerarquizado y pacing sonoro del rally | Cerrada |
| [[GDS-003.7_Onboarding_Legibilidad]] | RQ-003.7 | Onboarding, redundancia color+lado, jerarquia del HUD | Cerrada |

---

## Regla

- Un `GDS` cuelga siempre de un `RQ` (hereda número base y subnumeración). **Única excepción: el `GDS-XXX.0`** (ver abajo).
- Un `GDS` declara si `LDS` y `UXS` aplican. Un "no aplica" dice **qué dimensión falta y por qué**; se comprueba al cerrar el `VE` con el test del "no aplica".
- Estados posibles: En diseño / En balance / En validación / Cerrada / Rebotada.
- Al registrar, linkear al `RQ` y dejar el resultado de la validación.
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

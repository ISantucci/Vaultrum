## Índice de Game Design Specs (GDS)

Registro de todas las specs de diseño del Área de Game Design.

Cada `GDS-XXX.n` es un sistema jugable diseñado y validado para un `RQ-XXX.n`.

---

## Registro

Los artefactos de un proyecto **no se registran acá**. Viven en la carpeta del proyecto, en `06_Proyectos/<Proyecto>/02_GameDesign/`, y se listan en el cuaderno de ese proyecto.

Este índice es el **contrato de salida** del área: qué produce, qué forma tiene, cómo se numera y cuándo está cerrado. No es un archivo.

> Entrada a los proyectos: `00_Proyectos`. Por qué dejaron de vivir acá: `TL-008_La_Agencia_Es_La_Empresa`.

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

## Objetivo

Un **Pong 3D para dos jugadores locales en Unity 6**, entregado en `C:\Users\ControlEquipos\Desktop\a\vaultrumtest2`, que cumpla la Definición de Terminado del libro `01_Pong` — no que compile.

Este timeline existe por una razón declarada: **`TL-002_Pong3D_2_Jugadores_Unity6` quedó en `VE-002_Pong3D` = PAUSADO y su implementación no está en disco** (la carpeta destino está vacía). TL-002 no fue un mal timeline: sus `RQ` y `GDS` son sólidos. Falló en el borde: nunca se pudo validar y nunca aterrizó. TL-003 rehace la cadena **cargando primero el insumo que TL-002 no tenía** —el libro `01_Pong`, que en ese momento estaba vacío— y agrega los dos eslabones que faltaron.

## Antecedente y delta contra TL-002

| Dimensión | TL-002 | TL-003 |
|-----------|--------|--------|
| Libro de género (01_Pong) | Vacío (molde de EST-001). No se pudo consultar | **Llenado por EST-001 y cargado como insumo obligatorio del `RQ`** |
| `UXS` | Declarado *no aplica* | **Aplica.** La interfaz se diseña antes de codearse, no se improvisa en `Awake` (desvío #1 del `EJ-002`) |
| Onboarding / controles | Implícito | `RQ-003.7` propio (table-stake #9 del libro) |
| Estado en disco | Nunca aterrizó | Entrega verificable en la ruta destino |
| Cierre | PAUSADO sin poder validar | Cierre con checklist ejecutable por el owner en una sola partida |

TL-002 queda como **antecedente cerrado como PAUSADO**. No se reabre: se supersede.

## Área afectada

Producción (dueña) → Game Design → UI/UX → Programación → Producción (validación).

## Criticidad

Alta. Es la entrega que cierra el loop que originó la Ley candidata #1 (fricción mínima / baseline competente).

## Insumos cargados

| Insumo | Qué aporta | Dónde se usa |
|--------|-----------|--------------|
| 01_Pong | 9 table-stakes, baseline de parámetros, Definición de Terminado del género | Redacción de los `RQ` y validación final |
| 05_Fundamentos_de_experiencia_ludica | 9 pilares + CHECKLIST por-GDS | Gate de cada `GDS` |
| TL-002_Pong3D_2_Jugadores_Unity6 | Diseño previo del mismo sistema | Reutilizado donde sigue siendo válido; se declara qué se hereda |
| VaultrumCore (SOLID, patrones, optimización) | Criterio técnico | `SOL-003` |

## Supuestos declarados

1. **Versión de Unity:** se escribe `ProjectVersion.txt` con `6000.0.81f1` (la versión que el owner relevó en TL-002). Si el Hub tiene una 6.x más nueva instalada, Unity ofrece migrar al abrir y el proyecto no depende de nada específico de la versión. **A confirmar por el owner al abrir.**
2. **Render pipeline:** Built-in. Sin URP/HDRP: evita depender de assets de pipeline y de la migración de materiales.
3. **Input:** el código soporta Input System *y* el manager legacy mediante defines, para no depender de cómo quede configurado *Active Input Handling*.

## Requerimientos asociados

| RQ | Título | Jugable | Cadena |
|----|--------|---------|--------|
| RQ-003.1_Setup_Proyecto_Arena | Setup de proyecto, escena y arena 3D | No | → `SOL` |
| RQ-003.2_Paletas_Controlables | Dos paletas por teclado, con peso | Sí | → `GDS` → `SOL` |
| RQ-003.3_Pelota_Rebote_Aceleracion | Pelota: ángulo por impacto, aceleración, anti-tunneling | Sí | → `GDS` → `SOL` |
| RQ-003.4_Score_Saque_Victoria | Marcador, saque justo, condición de victoria | Sí | → `GDS` → `SOL` |
| RQ-003.5_Estados_Y_Flujo_De_Pantallas | Máquina de estados y flujo sin estados muertos | Sí | → `GDS` → `UXS` → `SOL` |
| RQ-003.6_Game_Feel_Y_Audio | Juice del impacto, del gol y del rally | Sí | → `GDS` → `SOL` |
| RQ-003.7_Onboarding_Y_Legibilidad | Controles comunicados, lados distinguibles, HUD legible | Sí | → `GDS` → `UXS` → `SOL` |

## Secuencia de trabajo

```txt
RQ-003.1 ─────────────────────────────────► SOL-003 ► EJ-003
RQ-003.2 ► GDS-003.2 ──────────────────────►
RQ-003.3 ► GDS-003.3 ──────────────────────►
RQ-003.4 ► GDS-003.4 ──────────────────────►
RQ-003.5 ► GDS-003.5 ► UXS-003.5 ──────────►
RQ-003.6 ► GDS-003.6 ──────────────────────►
RQ-003.7 ► GDS-003.7 ► UXS-003.7 ──────────►
                                             ↓
                                          VE-003
```

`LDS` **no aplica** y queda declarado: el sistema no tiene dimensión espacial que componer — la arena es un rectángulo fijo, no hay layout, encuentros ni progresión intra-nivel. Es una omisión declarada, no un hueco.

`UXS` **sí aplica**, al revés que en TL-002: hay tres pantallas, un HUD y un flujo de navegación. En TL-002 esto se resolvió dentro del `EJ` como desvío declarado; acá se diseña antes.

## Dependencias

- `GDS-003.3` (pelota) depende de `GDS-003.2` (paletas): necesita medio-alto y posición.
- `GDS-003.6` (feel) depende de que 003.2/003.3/003.4 declaren sus eventos.
- `UXS-003.5` y `UXS-003.7` dependen de sus `GDS` cerrados.
- `SOL-003` depende de los siete hilos.
- `VE-003` depende de que el owner pueda **abrir el proyecto y jugar una partida**. Es la dependencia que hundió a TL-002 y está declarada desde el arranque.

## Riesgos

| # | Riesgo | Mitigación |
|---|--------|-----------|
| 1 | **No se puede ejecutar Unity desde la Agencia.** Es el riesgo que dejó TL-002 en PAUSADO | Se asume desde el inicio: la entrega incluye un checklist de validación de 3 minutos que el owner corre. `VE-003` queda PAUSADO por diseño hasta esa corrida, no por sorpresa |
| 2 | Escena Unity generada a mano en YAML: si está mal formada, el proyecto no abre | La escena contiene **un solo GameObject** con el bootstrap. Todo lo demás se construye en runtime. Menos YAML, menos superficie de error |
| 3 | *Active Input Handling* en modo "solo Input System" rompe `Input.GetKey` | Código con doble camino por defines (`ENABLE_INPUT_SYSTEM` / `ENABLE_LEGACY_INPUT_MANAGER`) |
| 4 | Balance fijado sin jugar (riesgo heredado de TL-002) | Todos los parámetros expuestos en el Inspector, en un solo lugar, editables en Play sin recompilar |
| 5 | Sobre-ingeniería: resolver problemas de escenas grandes en una escena de 20 objetos | El `SOL` justifica cada decisión técnica **contra un requerimiento**, no contra un principio. Optimizar sin requerimiento de performance es scope no pedido |

## Criterios de cierre

`VE-003` pasa a **Cerrado** solo si, **con el juego corriendo**, se tildan los 18 ítems de la Definición de Terminado de `01_Pong`. Verificar el código no es verificar la entrega (aprendizaje declarado en `VE-002_Pong3D`).

Si el feel no cierra, el estado es **Ajustar** con hallazgo concreto y el balance se toca en el Inspector, sin recompilar.

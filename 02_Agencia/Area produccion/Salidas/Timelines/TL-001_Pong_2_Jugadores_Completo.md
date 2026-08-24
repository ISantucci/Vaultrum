# TL-001 — Pong 2 jugadores completo y divertido

## Objetivo

Construir un Pong local para 2 jugadores en Unity 3D, jugable de punta a punta y con buen game feel: cancha, paletas controlables, pelota con rebote y aceleración, score con condición de victoria, menú de inicio, pausa y reinicio, y feedback visual/sonoro.

## Área afectada

Producción (este TL) → Game Design (reglas) → Programación (implementación). Sin narrativa ni arte pesado.

## Criticidad

Media. Es un proyecto de referencia para validar el flujo completo de la Agencia end-to-end.

## Restricción de entorno (dada, no se re-decide)

- Motor: **Unity 2022.3 LTS** (elegida por el owner).
- Render: Built-in RP (sin URP), para materiales estándar simples.
- Proyecto: **de cero**, carpeta `Desktop\a\vaultrumtest2` (se reemplaza el prototipo previo).
- Plataforma: PC, teclado. 2 jugadores locales.

## Requerimientos asociados

- **RQ-001.1** Paletas controlables (2 jugadores) — jugable
- **RQ-001.2** Pelota con rebote y aceleración — jugable
- **RQ-001.3** Score y condición de victoria — jugable
- **RQ-001.4** Estados de juego: menú, pausa y reinicio — jugable
- **RQ-001.5** Game feel: feedback visual y sonoro — jugable
- **RQ-001.6** Setup de proyecto, escena y cancha — no jugable (técnico)

## Secuencia de trabajo

1. RQ-001.6 (setup base) habilita todo lo demás.
2. RQ-001.1 y RQ-001.2 (core jugable) en paralelo sobre el setup.
3. RQ-001.3 (score/victoria) sobre el core.
4. RQ-001.4 (estados/menú/pausa) envuelve el loop.
5. RQ-001.5 (juice) al final, sobre lo ya jugable.

## Dependencias

- Todo depende de RQ-001.6.
- RQ-001.3 depende de RQ-001.1 + RQ-001.2.
- RQ-001.4 depende de RQ-001.3 (necesita saber cuándo hay victoria).
- RQ-001.5 depende de que el evento (gol/rebote/saque) ya exista.

## Riesgos

- Física del rebote inconsistente si se mezcla Rigidbody con movimiento manual → definir en GDS.
- Estados de juego mal separados (menú/juego/pausa/fin) → máquina de estados clara.
- Hardcodeo de balance (velocidad, aceleración, puntaje objetivo) → configurable.

## Criterios de cierre

- Se puede jugar una partida completa 2 jugadores: sacar, rebotar, puntuar, ganar, reiniciar.
- Menú de inicio y pausa funcionales; victoria con reinicio.
- Feedback de rebote/gol presente.
- Valores de balance configurables desde el Inspector.
- Trazabilidad TL → RQ → GDS → SOL → EJ completa.

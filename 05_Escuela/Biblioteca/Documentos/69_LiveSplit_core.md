---
tipo: documento
familia: Código fuente liberado
autor: LiveSplit (comunidad de speedrunning)
anio: vivo (consultado 2026-10-02)
formato: Código fuente (Rust) y documentación de componentes
acceso: Libre
licencia: nivel A — MIT o Apache-2.0, a elección
prioridad: media
estado: Estudiado
mision: EST-019_Mision_Endless_runner_y_contrarreloj
url: https://github.com/LiveSplit/livesplit-core
---

# Documento 69 — LiveSplit (livesplit-core)

> El cronómetro de referencia del speedrun: es como la comunidad que más mide tiempos decidió mostrarlos.
> **IP:** ficha + referencia. La Biblioteca no aloja el código.

---

- **Autor y año:** proyecto LiveSplit, en desarrollo continuo
- **Tipo:** código fuente del motor del cronómetro y documentación de sus componentes (https://github.com/LiveSplit/LiveSplit.github.io/blob/master/components.md)
- **URL:** https://github.com/LiveSplit/livesplit-core — `src/timing/timing_method.rs`, `src/settings/semantic_color.rs`
- **Estado de acceso:** **Libre.** Nivel A.
- **Qué se aprende:**
  - Dos métodos de tiempo: tiempo real, sin modificar, y tiempo de juego, el que informa el juego, con o sin cargas.
  - Cuatro estados de delta con color semántico —adelante ganando, adelante perdiendo, atrás recuperando, atrás perdiendo—, más dorado para el mejor segmento y otro color para el récord nuevo.
  - La suma de los mejores segmentos como carrera perfecta, y el ahorro posible por segmento.
- **Gap de Vaultrum que cubre:** las table-stakes de reloj, delta y récord de `06_Contrarreloj`.
- **Prioridad:** **Media**

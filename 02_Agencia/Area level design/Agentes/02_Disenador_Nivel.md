## Propósito

El Diseñador de Nivel convierte el encuadre espacial en el nivel concreto: layout, colocación de desafíos y ritmo. Abre el `LDS`.

---

## Responsabilidad principal

¿Cómo se acomodan en el espacio y el tiempo los desafíos que el sistema permite?

- diseñar el layout del nivel/escenario/pantalla jugable,
- colocar encuentros, obstáculos y objetivos según la curva de ritmo del encuadre,
- definir puntos de descanso, checkpoints y progresión intra-nivel,
- aplicar la curva de dificultad usando los **parámetros de balance del `GDS`** (no los redefine),
- señalar integraciones con otros niveles/sistemas.

---

## Cuándo se activa

Después del Analista de Espacio, con el encuadre listo.

---

## Qué debe hacer

Componer el nivel sobre la experiencia encuadrada. Colocar desafíos con intención de pacing (variar picos y valles, dosificar novedad). Aplicar dificultad con los parámetros del `GDS`. Abrir y completar el `LDS-XXX.n`.

---

## Qué debe evitar

No inventa reglas nuevas ni cambia balance base (Game Design). No diseña HUD/menús (UI/UX). No programa. No sobrecarga el nivel con contenido que no aporta a la experiencia.

---

## Salida esperada / formato

```txt
## Insumo (GDS-XXX.n) + encuadre
## Layout del nivel (estructura espacial)
## Colocación de desafíos / encuentros
## Pacing (secuencia de picos y valles)
## Dificultad aplicada (parámetros del GDS usados)
## Checkpoints / descansos / progresión intra-nivel
## Integraciones
## Criterios de validación
```

---

## Flujos a implementar

- [[02_Flujo_Diseno_Nivel]]

---
plantilla: Plan de prueba
alcance: una épica (hilo o entrega)
---

# Plan de prueba — <Épica>

## Identificación

- Épica / insumo (`EJ-XXX.n` o `TL-XXX`):
- Dueño de la épica:
- Build / rama / commit:
- Plataformas objetivo:
- Perfil elegido: Ligero / Estándar / Completo
- Justificación del perfil:

## Intención

Qué tiene que poder hacer el jugador o el sistema cuando esto funciona.

## Criterio de comparación

- Requerimientos:
- Specs:
- Criterios de aceptación:

## Modos de falla

| Modo de falla concreto | Impacto en el jugador | Prob. | Detección | Prioridad |
|---|---|---:|---:|---|

## Sistemas afectados

Directos e indirectos. Los indirectos son los que rompen sin que nadie los mire.

## Modelo de cobertura

Qué dimensiones se van a examinar y cuáles no aplican, con razón:

```txt
camino feliz · negativos · límites · estados y transiciones · persistencia
entrada · interfaz y feedback · rendimiento · accesibilidad · idioma · plataforma
```

## Casos dirigidos

Uno por línea, con la técnica que lo genera (límite, partición, estado, tabla, pares).

## Charters exploratorios

## Impacto en regresión

Qué comportamiento ya validado puede romper este cambio.

## Candidatos a automatización

## Datos y preparación

Partidas guardadas, semillas, configuraciones, atajos de estado que hacen falta.

## Criterios de entrada

## Criterios de salida

## Evidencia esperada

## Fuera de alcance

Qué no se va a verificar en este pase y qué riesgo queda vivo.

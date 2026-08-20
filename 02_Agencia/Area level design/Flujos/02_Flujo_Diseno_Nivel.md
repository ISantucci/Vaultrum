## Propósito

Convertir el encuadre espacial en un `LDS`: layout, encuentros, pacing y dificultad aplicada.

## Entrada del flujo

- Encuadre del [[01_Flujo_Analisis_Espacio]] + `GDS-XXX.n`.

## Transformación que realiza

- Diseña el layout del nivel.
- Coloca desafíos/encuentros según la curva de ritmo.
- Define checkpoints, descansos y progresión intra-nivel.
- Aplica la curva de dificultad con los parámetros de balance del `GDS` (no los redefine).
- Abre el `LDS-XXX.n`.

## Salida esperada / formato

```txt
## Insumo (GDS-XXX.n) + encuadre
## Layout del nivel
## Colocación de desafíos / encuentros
## Pacing (picos y valles)
## Dificultad aplicada (parámetros del GDS)
## Checkpoints / descansos / progresión
## Integraciones
## Criterios de validación
```

## Criterios de aceptación

- Layout y encuentros definidos con intención de pacing.
- Dificultad aplicada sin redefinir balance.
- Progresión intra-nivel clara.

## Condiciones para avanzar

Avanza al [[03_Flujo_Validacion_Nivel]] con el `LDS` abierto y completo.

## Qué debe evitar

No inventa reglas ni diseña interfaces. No programa.

## Resultado final

Un `LDS-XXX.n` listo para validación.

## Propósito

Esta carpeta contiene los timelines generados por el Área de Producción.

Cada timeline organiza una planificación general y agrupa los requerimientos necesarios para concretarla.

---

## Formato obligatorio

Cada timeline debe ordenar:

- objetivo,
- área afectada,
- criticidad,
- requerimientos asociados,
- secuencia de trabajo,
- dependencias,
- riesgos,
- criterios de cierre.

---

## Regla de numeración

Cada timeline usa un número base incremental.

Ejemplo:

TL-001  
TL-002  
TL-003

Los requerimientos asociados deben usar el mismo número base.

---

## Patron de archivo

Cada timeline debe usar este patron:

TL-XXX_Nombre_Descriptivo.md

Ejemplo:

TL-001_Pong_2_Jugadores_Completo.md

---

## Timelines registrados

Formato de registro:

```
- [[TL-XXX_Nombre_Descriptivo]] - objetivo breve
```

Registros:

- [[TL-001_Pong_2_Jugadores_Completo]] - Pong 2 jugadores completo (cancha, paletas, pelota, score, estados, juice)
- [[TL-002_Pong3D_2_Jugadores_Unity6]] - Pong 3D 2 jugadores en Unity 6 (arena, paletas, pelota, score, estados, opciones, game feel)
- [[TL-003_Pong3D_Unity6_Cadena_Completa]] - Pong 3D 2 jugadores en Unity 6 con cadena completa (supersede TL-002): carga el libro de Pong, agrega UXS y onboarding

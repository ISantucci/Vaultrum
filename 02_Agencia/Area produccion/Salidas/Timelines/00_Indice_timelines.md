## Propósito

Esta carpeta contiene los timelines generados por el Área de Producción.

Cada timeline organiza una planificación general y agrupa los requerimientos necesarios para concretarla.

---

## Formato obligatorio

Cada timeline ordena:

```txt
objetivo
área afectada
criticidad
requerimientos asociados
secuencia de trabajo
dependencias
riesgos
criterios de cierre
```

---

## Regla de numeración y nombre de archivo

Cada timeline usa un número base incremental, y sus requerimientos heredan ese número:

```txt
TL-001
TL-002
TL-003
```

El archivo se nombra con el código, el separador y el nombre descriptivo:

```txt
TL-XXX_Nombre_Descriptivo.md
TL-001_Pong_2_Jugadores_Completo.md
```

---

## Timelines registrados

- [[TL-001_Pong_2_Jugadores_Completo|TL-001 Pong 2 jugadores]] — cancha, paletas, pelota, score, estados y juice
- [[TL-002_Pong3D_2_Jugadores_Unity6|TL-002 Pong 3D en Unity 6]] — arena, paletas, pelota, score, estados, opciones y game feel
- [[TL-003_Pong3D_Unity6_Cadena_Completa|TL-003 Pong 3D, cadena completa]] — supersede al TL-002: carga el libro de Pong y agrega UI/UX y onboarding

---


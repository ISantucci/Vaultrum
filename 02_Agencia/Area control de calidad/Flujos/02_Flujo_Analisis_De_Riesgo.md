## Propósito

El Flujo de Análisis de Riesgo decide **dónde se gasta el esfuerzo** del pase.

Su función es convertir "hay que probar esto" en un orden de trabajo con criterio: qué se prueba primero, con qué profundidad, con qué técnica, y qué se deja explícitamente afuera.

Existe porque el tiempo de verificación siempre es menor que la superficie a verificar, y sin este paso el pase cubre lo cómodo en vez de lo caro.

---

## Entrada del flujo

- una entrada en estado LISTO PARA QA,
- lo que cambió y los sistemas que toca,
- el historial de defectos de esos sistemas, si existe,
- el modelo de prueba reusable del sistema, si existe.

---

## Transformación que realiza

- Lista **modos de falla**, no sistemas: qué podría pasar en concreto, no qué área podría fallar.
- Estima por modo: probabilidad, impacto, dificultad de detección y exposición.
- Ordena por prioridad de riesgo.
- Elige el perfil —Ligero, Estándar o Completo— y lo justifica contra el riesgo, no contra el tiempo.
- Asigna técnicas a los riesgos altos: límites, particiones, tabla de decisión, estados, pares, exploratorio dirigido.
- Declara qué queda fuera de alcance y qué riesgo vivo deja.

El criterio de fondo vive en el Core, en `Testing basado en riesgo`: este flujo lo aplica, no lo repite.

---

## Salida esperada / formato

```txt
## Riesgos            sistema · modo de falla · prob · impacto · detección · exposición · prioridad
## Perfil             Ligero / Estándar / Completo, con justificación
## Técnicas           qué se le aplica a cada riesgo alto
## Fuera de alcance   qué NO se verifica y qué riesgo queda vivo
```

Queda como el bloque instrumentado de riesgo del `QA`.

---

## Criterios de aceptación

El flujo puede darse por cerrado cuando:

- cada riesgo está escrito como modo de falla concreto y no como nombre de sistema,
- cada uno tiene sus cuatro estimaciones,
- el perfil está elegido y justificado,
- cada riesgo alto tiene al menos una técnica asignada,
- lo que queda fuera de alcance está escrito.

---

## Condiciones para avanzar

Avanza cuando el orden de trabajo puede ejecutarse sin volver a preguntar qué es lo importante.

Queda **Pausado** cuando el riesgo no se puede estimar sin información que nadie tiene —un sistema que nadie entiende, un cambio que nadie puede describir— y esa información es condición para saber dónde mirar.

No debe avanzar si:

- el perfil se eligió por el tiempo disponible en vez de por el riesgo,
- la lista de riesgos es una lista de sistemas,
- no hay nada declarado fuera de alcance en un pase que no es Completo.

---

## Qué debe evitar este flujo

No estima solo. La probabilidad la conoce mejor quien construyó el sistema; el impacto, quien conoce al jugador. Una estimación de una sola cabeza hereda sus puntos ciegos.

No baja el perfil en silencio. Si el tiempo no alcanza, lo que se declara es qué queda sin verificar.

No convierte el análisis en un documento largo. Ordenar es el objetivo; el número exacto no importa mientras separe lo primero de lo último.

---

## Resultado final

Un pase que empieza sabiendo dónde duele, y un registro de lo que se decidió no mirar.

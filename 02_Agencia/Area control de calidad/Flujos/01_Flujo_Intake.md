## Propósito

El Flujo de Intake decide si una épica **entra** al control de calidad.

Su función es fijar por escrito qué se va a verificar, sobre qué versión y contra qué criterio, antes de que alguien ejecute la primera prueba. Es el gate de entrada del área y el único paso que puede terminar sin haber probado nada.

Existe porque un resultado de prueba sin versión, sin alcance y sin criterio de comparación no es información: es una anécdota.

---

## Entrada del flujo

- una épica terminada: un hilo con su `EJ-XXX.n` en revisión técnica OK, o un `TL-XXX` con todos sus hilos cerrados;
- la build, rama o commit donde vive lo construido;
- los `RQ` del alcance, y los `GDS`, `LDS` o `UXS` que definen el comportamiento esperado;
- lo que cambió, los sistemas que toca y las limitaciones conocidas.

Si la épica no está terminada, el flujo no arranca: el área no verifica trabajo en curso.

---

## Transformación que realiza

- Congela la versión: build, commit o rama, plataforma y entorno, escritos antes de empezar.
- Fija el alcance: qué entra en este gate y qué queda afuera.
- Reúne el criterio de comparación y comprueba que exista: sin criterios de aceptación no hay resultado esperado, y sin resultado esperado no hay prueba.
- Declara el tipo de gate: de hilo (`QA-XXX.n`) o de entrega (`QA-XXX`).
- Corre la definición de listo para QA y decide si la entrada se acepta.

El checklist operativo vive en la skill del área (`vaultrum-calidad`, Paso 1). Este flujo no lo repite: define cuándo el paso puede darse por cerrado.

---

## Salida esperada / formato

```txt
## Entrada           épica · tipo de gate · insumo declarado
## Versión           build · commit o rama · plataforma · entorno · congelada
## Alcance           qué entra · qué no entra
## Criterio          artefactos contra los que se compara
## Contexto          qué cambió · sistemas tocados · limitaciones conocidas
## Estado            LISTO PARA QA · NO LISTO PARA QA (con lo que falta y a quién se le pide)
```

Queda como la primera sección del `QA` y como el bloque instrumentado de versión.

---

## Criterios de aceptación

El flujo puede darse por cerrado cuando:

- la versión está identificada y declarada congelada,
- el alcance dice qué entra y qué no,
- existe al menos un artefacto contra el cual comparar el comportamiento,
- el dueño de la épica está identificado,
- el entorno para ejecutar está disponible.

---

## Condiciones para avanzar

Avanza como **LISTO PARA QA** cuando se cumplen los cinco criterios de arriba.

Se detiene como **NO LISTO PARA QA** cuando falta algo imprescindible. No es un rechazo del trabajo: es la declaración de que el pase todavía no puede significar nada. Se dice exactamente qué falta y a quién se le pide.

No debe avanzar si:

- la build se puede recompilar y ser otra durante el pase,
- no hay criterios de aceptación ni specs contra las cuales comparar,
- el alcance es "lo último que se hizo",
- el entorno de ejecución no está disponible y no hay fecha.

---

## Qué debe evitar este flujo

No completa por su cuenta lo que falta. Preguntar es el trabajo; suponer es el defecto.

No rechaza por prolijidad: un documento mal escrito no bloquea el gate, una versión que no se puede identificar sí.

No empieza a probar "para ir adelantando". Un pase sobre una entrada incompleta produce defectos que después resultan ser malentendidos de alcance, y esos cuestan dos veces.

---

## Resultado final

Una entrada sobre la que el resultado de una prueba va a significar algo — o una lista corta y concreta de lo que falta para que lo signifique.

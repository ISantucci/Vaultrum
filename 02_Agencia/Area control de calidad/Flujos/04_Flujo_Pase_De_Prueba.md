## Propósito

El Flujo de Pase de Prueba es donde el área **ejecuta**: corre los casos, explora, encuentra, reporta y clasifica.

Su función es producir la materia prima del veredicto — defectos reproducibles con evidencia, y un registro honesto de qué se ejecutó y qué no.

---

## Entrada del flujo

- una build **Aceptada** o Condicional por el flujo de verificación,
- el orden de trabajo del análisis de riesgo, con su perfil y sus técnicas,
- los criterios de aceptación del alcance,
- la planilla de operación del proyecto, donde se registra lo que va apareciendo.

---

## Transformación que realiza

Corre en tres capas, y ninguna reemplaza a las otras:

```txt
casos dirigidos   contra los criterios de aceptación, con las técnicas asignadas por riesgo
exploratorio      charter, tiempo acotado, notas — para lo que ninguna lista contenía
automatizado      lo repetible, lo masivo y lo sensible a regresión, si existe
```

Después clasifica lo encontrado: validez, severidad, urgencia propuesta, dueño, decisión, si bloquea, si necesita regresión, si necesita análisis de causa raíz.

Las técnicas viven en el Core (`Tecnicas de diseno de pruebas`) y el checklist operativo en la skill (`vaultrum-calidad`, Paso 4). Este flujo no los repite.

---

## Salida esperada / formato

```txt
## Ejecutado          qué corrió, sobre qué versión, con qué resultado
## No ejecutado       qué quedó sin correr y por qué
## Defectos           uno por hallazgo: pasos, esperado, obtenido, evidencia, reproducibilidad
## Observaciones      fricción observable y lo que no es defecto, dicho como observación
## Triage             severidad · urgencia · dueño · decisión · bloquea · regresión · RCA
## Cobertura          la matriz de dimensiones, sin celdas vacías
```

Los defectos se registran en la planilla del proyecto; el `QA` lleva el resumen y los bloques instrumentados.

---

## Criterios de aceptación

El flujo puede darse por cerrado cuando:

- cada riesgo alto del análisis tiene al menos una ejecución asociada,
- cada defecto tiene versión, pasos, resultado esperado, resultado obtenido y evidencia — o está declarado intermitente con su frecuencia,
- cada defecto tiene severidad, dueño y decisión,
- la matriz de cobertura no tiene celdas vacías y cada "no aplica" tiene razón,
- lo que no se ejecutó está escrito.

---

## Condiciones para avanzar

Avanza al gate cuando el pase terminó o cuando se detuvo por una razón declarada.

Se detiene y devuelve cuando aparece un **bloqueante** que impide seguir probando: no tiene sentido acumular hallazgos sobre un sistema que no se puede recorrer. Se devuelve con el bloqueante, y el pase se retoma sobre la build del arreglo.

No debe avanzar si:

- hay defectos sin pasos ni evidencia,
- hay impresiones registradas como defectos,
- la cobertura quedó con celdas vacías,
- el exploratorio se declaró hecho sin notas ni charter.

---

## Qué debe evitar este flujo

No arregla lo que encuentra. Un área que encuentra y arregla deja de ser independiente.

No prueba lo cómodo. Si el análisis dijo dónde estaba el riesgo, ahí va el tiempo.

No infla la lista. Un duplicado y una observación convertida en defecto ensucian la única lista que después se usa para decidir.

No presenta una verificación parcial como completa: si algo se probó en el editor y no en la build de destino, se declara con esas palabras.

---

## Resultado final

Un conjunto de hallazgos que otro puede reproducir, clasificados, con dueño — y un registro honesto de la superficie que quedó sin mirar.

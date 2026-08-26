## Plantillas del Área de Control de Calidad

Los formularios operativos del área. Se copian al proyecto y se llenan ahí; acá viven vacíos, como contrato de forma.

Una plantilla existe para que quien la usa **no tenga que acordarse de qué preguntar**. Si un campo no se puede fallar, no es un campo: es decoración, y se saca.

---

## Qué plantilla para qué momento

```txt
al abrir un proyecto o un hito   → Estrategia de QA
al abrir el gate de una épica    → Plan de prueba
antes del pase profundo          → Verificación de build
durante el pase                  → Charter exploratorio · Reporte de defecto
al terminar el pase              → Resumen de pase
al cerrar                        → Gate de calidad · Problemas conocidos
después de un fallo significativo → Análisis de causa raíz
cuando un sistema ya se conoce   → Modelo de prueba reusable
```

---

## [[Plantilla_Estrategia_QA]]

Define, por proyecto o por hito, el alcance de calidad: qué entra, qué no, qué niveles y tipos aplican, qué plataformas, qué política de defectos y quién tiene autoridad de gate.

---

## [[Plantilla_Plan_De_Prueba]]

Traduce una épica en un pase ejecutable: intención, criterio de comparación, modos de falla, modelo de cobertura, casos dirigidos, charters, impacto en regresión y criterios de entrada y salida.

---

## [[Plantilla_Verificacion_De_Build]]

El registro del humo: identidad de la build, los checks con su resultado, los bloqueantes y la decisión de aceptar, aceptar condicionalmente o rechazar.

---

## [[Plantilla_Charter_Exploratorio]]

La sesión exploratoria con método: misión, tiempo acotado, componentes, datos de partida, heurísticas, notas, hallazgos y seguimiento.

---

## [[Plantilla_Reporte_De_Defecto]]

El defecto escrito para que otro pueda reproducirlo, estimar su impacto y verificar el arreglo.

---

## [[Plantilla_Resumen_De_Pase]]

Qué se ejecutó, qué no, qué falló por severidad, qué quedó sin cubrir y qué riesgo residual deja el pase.

---

## [[Plantilla_Gate_De_Calidad]]

El artefacto `QA`: alcance, versión, criterios obligatorios, estado de defectos, regresión, cobertura, riesgos aceptados con dueño, medición y veredicto.

---

## [[Plantilla_Problemas_Conocidos]]

Las desviaciones aceptadas que viajan con la entrega: qué es, a quién afecta, si hay alternativa, quién lo aceptó y qué pasa después.

---

## [[Plantilla_RCA]]

El análisis de causa raíz: qué ocurrió, por qué el producto lo permitió, por qué el proceso no lo detectó antes y qué queda funcionando para que no vuelva.

---

## [[Plantilla_Modelo_De_Prueba_Reusable]]

El conocimiento acumulado de un sistema: componentes, estados, integraciones, modos de falla, defectos históricos, límites, combinaciones de alto valor, charters estándar y candidatos a regresión y automatización.

Los modelos completados viven en `Modelos/`, que se crea cuando existe el primero.

---

## Regla

Una plantilla se completa con lo que se sabe y declara lo que no se sabe. Un campo vacío sin explicación es un hueco; un campo con "no aplica" y su razón es criterio.

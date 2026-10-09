## Propósito

Registro del contrato de salida del Área de Métricas.

Cada `MET` declara **qué se quiere saber, con qué se mide y qué se puede afirmar con lo medido**. No es un tablero ni un informe de números: es el documento contra el cual Programación implementa eventos, Control de Calidad los verifica y Producción decide.

---

## Los dos cortes

| Artefacto | Qué es | Cuelga de | Cuándo |
|---|---|---|---|
| `MET-XXX.n` | el **plan de medición** del hilo: objetivo, KPI, guardrails, tracking plan | `RQ-XXX.n` + `GDS-XXX.n` | con el `GDS` cerrado, antes del `SOL` |
| `MET-XXX` | la **lectura** de la entrega: el dato validado, leído contra los planes | `TL-XXX` + sus `MET-XXX.n` | con datos de la build jugada, antes del `VE` |

Es el mismo corte que `ART` y `QA`, y por una razón propia: **el plan se escribe por pregunta, y la lectura se hace sobre la build entera.** Un playtest no juega un hilo: juega la entrega, y lo que un hilo mide lo puede explicar otro.

El Modo Salud —un producto con jugadores, sin problema específico— produce también un `MET-XXX`, colgado del `TL` de operación que Producción abra para eso.

---

## Numeración

La subnumeración `.n` se hereda del hilo, igual que el resto de la cadena:

```txt
RQ-001.3  ->  GDS-001.3  ->  MET-001.3  ->  SOL-001  ->  EJ-001  ->  QA-001  ->  MET-001  ->  VE-001
```

`MET-XXX` **no lleva `.n`**, igual que `QA-XXX`, `ART-XXX` y `VE-XXX`: la lectura es de la entrega y no de la pieza.

---

## Contenido mínimo del plan — `MET-XXX.n`

```txt
## Insumo                 RQ-XXX.n · GDS-XXX.n
## Fase y modelo          fase: <una de las ocho> · modelo: <o "no aplica — por qué">
                          tope: N — <razón>   (solo si se pasa el presupuesto de la fase)
## Objetivo
## Comportamiento esperado
## KPI primario           nombre · formula · poblacion · ventana · fuente · baseline · objetivo
## Métricas diagnósticas
## Guardrails
## Segmentos              solo si la pregunta los pide
## Tracking plan          | Evento | Disparo | Parametros | Pregunta | KPI |
## QA de eventos          lo que Control de Calidad verifica, evento por evento
## Privacidad
## Decisión que habilita
## Lo que no se mide
## Estado
```

Las claves del KPI se escriben como `clave: valor`, una por línea: son lo que lee el instrumento, y lo que impide que dos personas lean dos métricas distintas con el mismo nombre.

## Contenido mínimo de la lectura — `MET-XXX`

```txt
## Insumo                 MET-XXX.n (todos los que lee) · TL-XXX · archivo de datos
## KPI primario           nombre: <el mismo que congeló el plan>
## Calidad del dato       lo que dijo metricas.py datos, citado
## Hechos
## Interpretaciones
## Hipótesis
## Recomendación          y quién decide
## Próxima medición
## Estado
```

---

## Dónde aterriza

```txt
la ficha      <Proyecto>/08_Metricas/MET-XXX.n_<Nombre>.md
              <Proyecto>/08_Metricas/MET-XXX_<Nombre>.md
el dato       <Proyecto>/08_Metricas/datos/<build>.csv   (si el owner decide guardarlo)
```

El plan y su lectura viven en la misma carpeta a propósito: el instrumento busca ahí el plan que la lectura cita para comprobar que el KPI no cambió.

Rige el **gate de existencia en disco**: lo que el `MET` afirma haber medido tiene que poder volver a medirse con el archivo que nombra.

---

## Cuándo un `MET` no cierra

```txt
el plan no está en ley                  rebota al 01 o al 02, según la ley
el dato no es legible                   Pausado: se declara qué haría falta
la lectura cambió el KPI                metric shopping: rebota al 03
un paso condicional no corrió y         es un hueco, no una omisión
NO declaró su omisión
un número sin instrumento               el área estaría estimando
```

Un `MET-XXX.n` cerrado es insumo del `SOL` y de la QA de eventos. Un `MET-XXX` cerrado es insumo del `VE`.

---

## Registro

Los artefactos de un proyecto **no se registran acá**. Viven en `06_Proyectos/<Proyecto>/08_Metricas/` y se listan en el cuaderno de ese proyecto.

Este índice es el **contrato de salida** del área: qué produce, qué forma tiene, cómo se numera y cuándo está cerrado. No es un archivo.

---

## Regla

- Un `MET` no cierra sin estar medido por `metricas.py`.
- El KPI primario se congela en el plan y la lectura no lo toca.
- El dato se valida antes de leerse.
- Todo paso condicional que no corre **declara su omisión con su razón**.
- Una excepción a una ley se escribe **en el propio `MET`**, con su razón. La del presupuesto de eventos ya tiene su forma —`tope: N — <razón>`— y el instrumento la lee.

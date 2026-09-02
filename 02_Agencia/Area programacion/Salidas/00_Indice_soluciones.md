## Índice de Soluciones Técnicas (SOL)

Contrato de salida del Área de Programación para el artefacto `SOL`. Responde las cinco preguntas de `RQ-008.1` y nada más. **No es un archivo:** los artefactos de un proyecto no se registran acá.

---

## 1 · Qué produce el área

Un `SOL-XXX.n` es la **solución técnica** de un `RQ-XXX.n`: dónde vive la arquitectura antes de que exista una línea de código. Decide, no implementa. Lo que se construye después es el `EJ`.

## 2 · Qué forma tiene

Ocho secciones, en este orden. Las cinco primeras salen de **medir los `SOL` reales**; las tres últimas están marcadas con su origen porque no salen de ahí.

| # | Sección | Qué tiene que decir | Origen |
|---|---------|---------------------|--------|
| 1 | **Insumo** | el `RQ`, y el `GDS` / `LDS` / `UXS` si aplican, cada uno en su línea rotulada | medido 4/5 |
| 2 | **Diagnóstico** | qué problema técnico hay que resolver, leído del insumo y no del gusto | medido 4/5 |
| 3 | **Decisiones** | cada decisión contra **su** `RQ` o su presupuesto, con las alternativas descartadas y por qué | medido 5/5 |
| 4 | **Lo que deliberadamente NO se hizo** | tabla de dos columnas: qué no se hizo, y el motivo | ley del Core |
| 5 | **Arquitectura** | componentes, responsabilidades y flujo de datos. La forma, no el código | medido 5/5 |
| 6 | **Contrato de ejecución** | qué archivos, qué interfaces, qué invariantes y qué queda prohibido | diseñada |
| 7 | **Verificación** | cómo se prueba que esto se sostiene, y qué **no** cubre esa prueba | medido 5/5 |
| 8 | **Estado** | Propuesta / Aprobada / Ejecutada / Cerrada / Rebotada | corolario |

**Sección 4 — ley del Core, no invención.** `Baseline de entregable` (mitad 2) declara obligatoria en toda `SOL` la tabla de *lo que se hizo* / *lo que deliberadamente no se hizo*. Medido: aparece en 2 de 5, siempre como `###` colgando de otra sección. Sube a `##` para que el gate la vea. La segunda columna es la que suele faltar, y es la que demuestra que hubo criterio y no olvido.

**Sección 6 — diseñada, con su requerimiento detrás.** Es la única que no sale de medir ni de una ley previa, y existe porque el owner pidió poder **rutear la ejecución a un ejecutor barato**. Un `EJ` solo se puede delegar si el `SOL` cerró la spec: qué archivos toca, qué interfaces expone, qué invariantes no se pueden romper y qué queda explícitamente fuera. Sin esa sección, quien ejecuta tiene que decidir — y decidir es justo lo que no se delega.

```txt
Archivos      rutas exactas que se crean o se tocan
Interfaces    firmas publicas: que llama a que, y con que
Invariantes   lo que tiene que seguir siendo cierto despues del cambio
Prohibido     lo que no se toca, con el motivo
```

**Punto de quiebre** —*a qué carga se rompe esta arquitectura*— **no entra al contrato todavía**, a propósito. Sin presupuesto de rendimiento declarado en el `RQ`, la sección se llenaría de `n/a` — que es exactamente el defecto que QA arrastró en dos entregas. Entra el día que exista la pregunta de plataforma y rendimiento en el relevamiento; hasta entonces se escribe **solo cuando hay presupuesto contra el cual medirla**.

## 3 · Cómo se numera

Un `SOL` cuelga siempre de **uno o varios** `RQ` del mismo timeline y hereda su número base. Lleva `.n` si cubre un solo hilo y no lo lleva si cubre el timeline entero; cuando cubre varios, **los enumera en su `Insumo`** y la Ley 1b de `documentacion.py` comprueba que ninguno quede afuera. La columna vertebral de numeración vive en `02_Indice Agencia` y este contrato la referencia, no la copia — hasta el 2026-09-01 esta línea decía 1:1 y era una copia que ya había derivado.

## 4 · Dónde aterriza

`06_Proyectos/<Proyecto>/05_Programacion/`. Nunca en las capas de sistema. Regla completa: **Dónde aterriza cada salida**, en `02_Indice Agencia`.

## 5 · Cuándo está cerrado

- Las ocho secciones existen, o la ausente está declarada con su motivo (test del *no aplica*).
- Cada decisión de la sección 3 nombra el `RQ` o el presupuesto que la pide. Una decisión justificada contra un principio y no contra un pedido es alcance no pedido.
- El `Contrato de ejecución` alcanza para que otro ejecute sin volver a decidir.
- La `Verificación` declara qué cubre **y qué no**.
- El estado es uno de los cinco del vocabulario.

```bash
python3 "02_Agencia/Area conocimiento/Herramientas/documentacion.py" "06_Proyectos/<Proyecto>" --verificar
```

---

## Registro

Los artefactos de un proyecto **no se registran acá**. Viven en `06_Proyectos/<Proyecto>/05_Programacion/` y se listan en el cuaderno de ese proyecto.

> Entrada a los proyectos: `00_Proyectos`. Por qué dejaron de vivir acá: `TL-008_La_Agencia_Es_La_Empresa`.

## De dónde salió esta forma

Medición sobre los cinco `SOL` reales del vault (2026-08-28), **agrupando por lo que cada sección hace y no por cómo se llama**. Era el paso que faltaba: los cinco decían las mismas cosas con títulos distintos —la arquitectura aparecía como *Arquitectura*, *Estructura*, *Componentes propuestos* y *Decisión de arquitectura*— y `documentacion.py` compara nombres literales, así que medía cero coincidencias y `contratos.txt` concluyó *"sin forma estable"*.

No era falta de forma. Era falta de vocabulario común.

```txt
                      agrupado por funcion, sobre 5 SOL reales
  Decisiones          5/5   100%
  Arquitectura        5/5   100%
  Verificacion        5/5   100%
  Diagnostico         4/5    80%
  Insumo              4/5    80%
  ---- umbral 75% ----
  Parametros          2/5    40%
  Riesgos             2/5    40%
  Trazabilidad        2/5    40%
  Estado              2/5    40%   <- entra igual, por el corolario
```

La tabla de equivalencias usada queda en el mismo lugar que esta medición, para que la próxima pasada mida lo mismo y no otra cosa.

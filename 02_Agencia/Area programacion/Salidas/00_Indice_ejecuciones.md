## Índice de Ejecuciones (EJ)

Contrato de salida del Área de Programación para el artefacto `EJ`. Responde las cinco preguntas de `RQ-008.1` y nada más. **No es un archivo:** los artefactos de un proyecto no se registran acá.

---

## 1 · Qué produce el área

Un `EJ-XXX.n` es la **implementación real** de un `SOL-XXX.n`, más el reporte de lo que pasó al construirla. El `SOL` decide; el `EJ` construye y cuenta. Si el `EJ` decide algo, eso es un **desvío** y se declara.

## 2 · Qué forma tiene

Siete secciones, en este orden. **Las siete salen de medir los `EJ` reales** — este contrato no diseñó ninguna.

| # | Sección | Qué tiene que decir | Origen |
|---|---------|---------------------|--------|
| 1 | **Insumo** | de qué `SOL` cuelga, en su línea rotulada | medido 4/5 |
| 2 | **Lo que se implementó** | por requerimiento o por hilo, no una lista suelta de tareas | medido 5/5 |
| 3 | **Archivos creados** | rutas reales, verificadas contra disco | medido 5/5 |
| 4 | **Desvíos declarados** | dónde la implementación se apartó del `SOL`, y por qué | medido 4/5 |
| 5 | **Verificación** | en formato de `Verificacion parcial declarada` | medido 5/5 |
| 6 | **Riesgos abiertos** | lo que queda frágil, sin confundirlo con hallazgos de QA | medido 4/5 |
| 7 | **Estado** | En ejecución / Reportada / En revisión / Cerrada / Rebotada | medido 4/5 |

**Sección 5 — el formato es obligatorio, no libre.** `Verificacion parcial declarada` (Core) fija cuatro campos y los cuatro se escriben:

```txt
Metodo        con que se verifico
Cubre         que clase de error queda cerrada
No cubre      que clase de error sigue abierta
Consecuencia  que significa eso para el estado de la entrega
```

Una verificación sin alcance declarado se lee como cierre, y produce el falso *Cerrado* que los `VE` existen para evitar.

**Sección 3 — se verifica contra disco, no contra memoria.** Ley 5 de la documentación: *lo terminado existe en disco*. Un archivo listado que no existe es una falla del gate, no una errata.

**Lo que quedó afuera:** `Aprendizaje reutilizable` aparece en 1 de 5. No entra al contrato — el aprendizaje se cosecha al cerrar la entrega, y su lugar es el `VE` y el commit al Core, no cada `EJ`.

## 3 · Cómo se numera

Un `EJ` cuelga siempre de un `SOL` y usa **su mismo número**, con `.n` o sin `.n` según lo tenga el `SOL`. La numeración vive en `02_Indice Agencia`; este contrato la referencia y no la repite — hasta el 2026-09-01 la repetía, diciendo 1:1.

## 4 · Dónde aterriza

`06_Proyectos/<Proyecto>/05_Programacion/`. El **código** no: el código va dentro del proyecto del motor, en su `Assets/`. El `EJ` cuenta lo que se escribió y dónde; no lo contiene.

## 5 · Cuándo está cerrado

- Las siete secciones existen, o la ausente está declarada con su motivo.
- Cada archivo listado en la sección 3 existe en disco.
- La `Verificación` trae los cuatro campos, y el campo *No cubre* no está vacío.
- Todo desvío respecto del `SOL` está en la sección 4. Un desvío no declarado no es un atajo: es una decisión tomada en el lugar equivocado.
- El estado es uno de los cinco del vocabulario.

```bash
python3 "02_Agencia/Area conocimiento/Herramientas/documentacion.py" "06_Proyectos/<Proyecto>" --verificar
```

---

## Registro

Los artefactos de un proyecto **no se registran acá**. Viven en `06_Proyectos/<Proyecto>/05_Programacion/` y se listan en el cuaderno de ese proyecto.

> Entrada a los proyectos: `00_Proyectos`. Por qué dejaron de vivir acá: `TL-008_La_Agencia_Es_La_Empresa`.

## De dónde salió esta forma

Medición sobre los cinco `EJ` reales del vault (2026-08-28), agrupando por lo que cada sección **hace** y no por cómo se llama. El `EJ` resultó tener forma más estable que el `SOL`: las siete funciones llegan al umbral sin que haga falta diseñar ninguna.

```txt
  Lo que se implemento   5/5   100%
  Archivos creados       5/5   100%
  Verificacion           5/5   100%
  Insumo                 4/5    80%
  Desvios declarados     4/5    80%
  Riesgos abiertos       4/5    80%
  Estado                 4/5    80%
  ---- umbral 75% ----
  Aprendizaje            1/5    20%
```

## Propósito

El Flujo de Lectura convierte un dato validado en **la lectura de la entrega**, el `MET-XXX`, que Producción usa para cerrar el `VE` y Game Design para decidir si el diseño se mueve.

Existe porque entre un número y una decisión hay una interpretación, y la interpretación sin rótulos es la forma más común de convertir una sospecha en un hecho.

---

## Entrada del flujo

- el o los `MET-XXX.n` del timeline, con su KPI congelado;
- el CSV de eventos de la build jugada, declarado **legible** —o legible con salvedades— por el `04_Flujo_Validacion_Medicion`;
- el informe de `metricas.py datos`, que es la fuente de todos los hechos;
- el `QA-XXX` de la entrega, si existe: una falla conocida explica comportamientos que de otro modo parecerían de diseño.

---

## Transformación que realiza

- Toma el KPI primario **tal como lo congeló el plan** y lo compara contra baseline, objetivo, control o cohorte anterior, y contra la expectativa de diseño.
- Busca el drop-off relativo, no el número más chico.
- Segmenta solo si la pregunta lo pide; en distribuciones sesgadas usa mediana y percentiles.
- Escribe hechos, interpretaciones, hipótesis y recomendación en secciones separadas.
- Nombra los confounders que pudieron mover el dato: una versión, un cambio de balance, una falla del `QA`.
- Escribe la próxima medición.

---

## Salida esperada / formato

```txt
## Insumo                MET-XXX.n · TL-XXX · el archivo de datos
## KPI primario          nombre: <el del plan, sin cambios>
## Calidad del dato      lo que dijo el instrumento
## Hechos
## Interpretaciones
## Hipótesis
## Recomendación
## Próxima medición
## Estado
```

Se mide con:

```txt
python3 "02_Agencia/Area metricas/Herramientas/metricas.py" lectura <MET-XXX.md> --verificar
```

---

## Criterios de aceptación

- el KPI de la lectura es el mismo que el del plan,
- cada hecho sale del instrumento o se declara estimación,
- ninguna hipótesis aparece en la sección de hechos,
- la recomendación dice quién decide,
- la próxima medición está escrita,
- `metricas.py lectura` devuelve EN LEY.

---

## Condiciones para avanzar

Avanza cuando Producción puede leer el `MET-XXX` en el `VE` sin tener que reinterpretar el dato.

Queda **Pausado** cuando el dato no alcanza para ninguna conclusión —pocos jugadores, ventana sin cerrar— y se declara qué faltaría. Una lectura que dice *"con esto no se puede afirmar nada"* es un cierre válido.

No debe avanzar si:

- el KPI cambió respecto del plan,
- se declaró una causa con un antes/después sin control,
- la lectura depende de un dato que el validador no declaró legible.

---

## Qué debe evitar este flujo

No busca la métrica que "dio positiva". No lee solo el agregado. No recomienda monetización agresiva porque sube un número.

---

## Resultado final

Una lectura que separa lo que se sabe de lo que se sospecha, con el mismo KPI que se eligió antes de mirar, y con la próxima pregunta escrita.

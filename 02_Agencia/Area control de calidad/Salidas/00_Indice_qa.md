## Índice de gates de calidad (QA)

Registro del contrato de salida del Área de Control de Calidad.

Cada `QA` es el gate que decide si una épica terminada **se sostiene**: qué se verificó, sobre qué versión, con qué evidencia, qué riesgo queda vivo y quién se hace cargo.

---

## Los dos cortes

| Artefacto | Cierra | Cuelga de | Cuándo |
|---|---|---|---|
| `QA-XXX.n` | un hilo de trabajo | `EJ-XXX.n` | una implementación específica terminó su revisión técnica |
| `QA-XXX` | la entrega del timeline | `TL-XXX` | todos los hilos cerraron y la épica va a cerrarse |

Es el mismo corte que la Agencia ya tenía: el hilo `.n` y la entrega. El `QA` de entrega **no lleva `.n`**, igual que el `VE`, porque la decisión de calidad es del entregable y no de la pieza.

Un `QA-XXX` de entrega no repite los `QA-XXX.n` de sus hilos: los cita, y verifica lo que solo se ve en conjunto — regresión cruzada, build candidata, cobertura del entregable y riesgo acumulado.

---

## Los tres perfiles

| Perfil | Cuándo | Qué corre |
|---|---|---|
| Ligero | hilo de riesgo bajo, sin datos persistentes ni camino crítico | intake, riesgo, humo del camino afectado, casos dirigidos, cobertura |
| Estándar | por defecto | lo anterior + exploratorio con charter + regresión del sistema afectado |
| Completo | entrega, build candidata, o algo que toque guardado, economía o plataforma | lo anterior + compatibilidad + rendimiento + regresión completa + conocidos |

El perfil se declara y se justifica contra el riesgo. Bajar de perfil es declarable; saltear el gate no lo es.

---

## Los tres veredictos

```txt
GO               se cumplen los criterios de salida del alcance, con evidencia
CONDITIONAL GO   hay desviaciones enumeradas, con impacto comprendido, dueño y aceptación escrita
NO-GO            hay una condición obligatoria incumplida, o no hay evidencia suficiente
```

Un `QA` en NO-GO no es un fracaso del área: es su producto. La alternativa —cerrar sin evidencia— es la que cuesta.

---

## El instrumento

Un `QA` no cierra sin estar **instrumentado y medido**. Los bloques van dentro de bloques de código cercados, con la etiqueta en el info-string, para que no agreguen una sola arista al grafo del vault:

````txt
```qa-alcance
tipo     hilo               (o: entrega)
insumo   EJ-004.2           (o: TL-004)
perfil   estandar           (ligero | estandar | completo)
```
```qa-build
build       0.9.4-rc1
commit      abc1234
plataforma  Windows
entorno     build de destino
congelada   si
```
```qa-humo
instalacion ok | arranque ok | pantalla principal ok | entrada ok
bucle ok | camino critico ok | caidas ok | logs ok | guardado ok
resultado   aceptada        (aceptada | condicional | rechazada)
```
```qa-riesgo
Guardado | 3 | 5 | 4 | 2 | una partida de la version anterior no abre tras actualizar
```
```qa-defectos
BUG-012 | mayor | cerrado | reverificado en 0.9.4-rc2
BUG-013 | menor | diferido | alternativa disponible
```
```qa-regresion
suite bloqueante | 0.9.4-rc2 | ok
suite esencial   | 0.9.4-rc2 | ok
```
```qa-cobertura
sistema | feliz | negativo | limite | estados | guardado | rendimiento | accesibilidad | idioma | plataforma
Descarte de item | si | si | si | si | na:no persiste | na:sin presupuesto declarado | si | si | Windows
```
```qa-aceptado
BUG-013 | menor | Ignacio | se difiere a TL-005: no toca el camino critico
```
```qa-decision
CONDITIONAL GO
```
````

Los campos de cada fila, en orden:

```txt
qa-riesgo     sistema | probabilidad | impacto | deteccion | exposicion | modo de falla   (los cuatro números, 1 a 5)
qa-defectos   id | severidad | estado | reverificación         (el cuarto campo es obligatorio si el estado es cerrado)
qa-regresion  suite | build | resultado
qa-cobertura  cabecera con las dimensiones, y una fila por sistema: si | no | na:razón
qa-aceptado   id | severidad | quién acepta | razón y qué pasa después
```

Severidades: `bloqueante` `critico` `mayor` `menor` `trivial`. Estados: `abierto` `diferido` `cerrado`.

La medición la corre `Herramientas/calidad.py`. **El veredicto declarado tiene que coincidir con el que sale de la medición**, o el `QA` no cierra. Una anotación entre paréntesis al final de un valor es documentación del formato y la herramienta la ignora.

---

## La planilla de operación

El detalle operativo no vive en el `QA`: vive en `Vaultrum_QA_Operations.xlsx`, con sus hojas de defectos, casos, regresión, verificación de build, riesgos, cobertura, gate y sesiones exploratorias.

```txt
plantilla vacía   02_Agencia/Area control de calidad/Herramientas/    se versiona, no se llena
copia del proyecto 06_Proyectos/<Proyecto>/06_Calidad/                se llena, no se versiona
```

La copia del proyecto se crea al abrir el primer `QA` de ese proyecto y se sigue usando en todos los siguientes: el registro de defectos es acumulativo, el `QA` es por épica.

---

## Registro

Los artefactos de un proyecto **no se registran acá**. Viven en la carpeta del proyecto, en `06_Proyectos/<Proyecto>/06_Calidad/`, y se listan en el cuaderno de ese proyecto.

Este índice es el **contrato de salida** del área: qué produce, qué forma tiene, cómo se numera y cuándo está cerrado. No es un archivo.

> Entrada a los proyectos: `00_Proyectos`. Por qué dejaron de vivir acá: `TL-008_La_Agencia_Es_La_Empresa`.

---

## Regla

- Un `QA-XXX.n` cuelga de su `EJ-XXX.n`; un `QA-XXX` cuelga de su `TL-XXX`. Cada uno declara su insumo en una línea rotulada.
- La numeración se hereda del hilo: `RQ-004.2 → GDS-004.2 → SOL-004.2 → EJ-004.2 → QA-004.2`.
- Estados del artefacto en el índice: En intake / En análisis / En pase / En reverificación / Cerrado / Devuelto. El **estado del paso** —Cerrado, Ajustar, Pausado— es el vocabulario común de la Agencia y se declara aparte: son dos ejes distintos.
- **No listo para QA** es un estado de la entrada, no del `QA`: significa que el gate todavía no abrió.
- Un `QA` no cierra sin estar instrumentado: un gate que no se puede medir no se puede validar.
- El veredicto lo confirma `calidad.py --verificar`, no una lectura.
- Toda excepción vive en `Herramientas/excepciones.txt` con su razón escrita.
- Un `QA` cerrado es **insumo obligatorio del `VE`** de Producción: un `VE` no cierra en Cerrado con un `QA` en NO-GO.

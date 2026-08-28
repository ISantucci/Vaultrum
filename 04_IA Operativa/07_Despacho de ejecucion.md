# Despacho de ejecución

El segundo presupuesto de esta capa. `01_Cuidado de tokens` y `04_Pass GC de contexto` cuidan **lo que entra**: qué material del vault se carga. Esta nota cuida **lo que sale**: dónde corre el trabajo y qué cuesta hacerlo correr.

```txt
AiCare     costo de ENTRADA     que contexto se carga        ya medido, contar_contexto.py
Despacho   costo de EJECUCION   que superficie y que modelo  esta nota
```

Son dos presupuestos distintos y se confunden fácil. Podar contexto y elegir un modelo barato bajan la misma factura por caminos que no se tocan: uno reduce lo que la IA tiene que leer, el otro reduce lo que cuesta cada cosa que hace.

---

## La ley del subagente

> **El subagente escribe el archivo y devuelve un resumen corto. El padre nunca sostiene el texto completo.**

Es la única ley de esta nota, y no salió de una intuición.

**El contraejemplo, medido.** `spec-kit` implementó lo contrario —forkear un comando y devolver su informe entero al padre— y **lo revirtió**. El motivo es aritmético: si el resultado no es compacto, el informe completo vuelve al padre, cada fork siguiente lo hereda, y el contexto crece hasta congelar la sesión. Delegar para ahorrar termina costando más que no delegar. `BMAD` resolvió lo mismo con la regla de arriba. Ver `30_Frameworks_spec_driven_multiagente` en la Biblioteca, y `RQ-007.7`.

**Dónde muerde hoy.** El comando `rescue` del plugin de Codex declara en su propia definición que *la respuesta final al usuario debe ser la salida de Codex, textual*. Enchufado crudo, para una tarea larga hace exactamente lo contrario de ahorrar. Por eso el pedido lleva las dos instrucciones adentro: dónde escribir, y qué devolver.

```txt
1. escribi el resultado en <ruta exacta>
2. devolveme SOLO: que archivos tocaste, que quedo sin hacer, y una linea de estado
```

---

## El criterio de reparto

Una sola línea, y vale para cualquier ejecutor barato, no solo para Codex:

```txt
el artefacto YA TIENE contrato escrito  ->  ejecutar es mecanico   ->  ejecutor barato
el artefacto es DONDE SE DECIDE         ->  modelo fuerte, con el vault cargado
```

De ahí sale un corolario que ordena el trabajo del sistema entero: **un artefacto sin contrato no se puede abaratar.** Mientras el `SOL` no tuvo forma medida, el `EJ` no se podía delegar — no porque faltara una herramienta, sino porque no había spec cerrada contra la cual ejecutar. Escribir contratos no es burocracia: es lo que habilita el ahorro.

**Esta nota es la autoridad del criterio y de la ley de arriba.** La tabla concreta de qué fase va a qué ejecutor —y con qué comandos -- vive en la skill del área que ejecuta, `vaultrum-programador`, que la cita en vez de repetirla.

La regla de capas no se cumple sola: la primera versión de estas dos piezas repetía el criterio en las dos, y **las copias ya diferían** —una hablaba de *cualquier ejecutor barato* y la otra fijaba Codex con esfuerzo bajo—. Lo detectó un review adversarial el mismo día que se escribieron. Dos textos que dicen lo mismo empiezan a diferir en cuanto uno se edita, y nadie se entera hasta que chocan.

---

## Lo que el ahorro no puede costar

```txt
trazabilidad   un EJ ejecutado por un tercero se registra igual, con el mismo contrato
               y el mismo gate de existencia en disco
decision       lo que se delega es ejecutar, nunca decidir
evidencia      los instrumentos son scripts: no necesitan modelo, y su salida ES la prueba
```

Un ahorro que rompe cualquiera de las tres no es un ahorro: es una entrega peor que salió más barata.

---

## Lo que esta nota todavía no mide

`contar_contexto.py` mide el material del vault que se carga. **No mide** lo que cuesta una ejecución delegada, ni cuántas veces se delegó, ni si el ahorro fue real. Hoy el despacho es criterio escrito y no medición.

Es la misma deuda que esta capa ya tuvo una vez —decía *medir* y estimaba— y se declara igual: **el reparto se aplica, no se afirma que ahorra.** El día que haya un contador de ejecuciones, se mide y se corrige si difiere.

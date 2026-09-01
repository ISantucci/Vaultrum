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

### La ley corre sobre ejecución, no sobre juicio

La ley de arriba está bien y su dominio estaba sin declarar. La primera corrida real la rompió con razón: se pidió un review adversarial con las tres líneas de vuelta de siempre, y volvieron **siete hallazgos completos**. No fue un incumplimiento del ejecutor: fue un error de la regla.

```txt
delegar EJECUCION   el producto es un archivo en disco   -> resumen corto, y el archivo
                    el trabajo queda fuera del contexto     se verifica con el gate
                    y el resumen alcanza

delegar JUICIO      el producto ES el texto que vuelve   -> NO se comprime.
                    comprimirlo destruye exactamente        Se acota el ALCANCE, antes.
                    lo que se fue a buscar
```

**Acotar un juicio se hace antes —qué se revisa y contra qué— no después recortando la salida.** Un review con alcance abierto y salida recortada es lo peor de las dos cosas: se paga entero y vuelve mutilado.

De ahí la forma general, que es lo que faltaba: **toda ley de compresión de respuesta declara sobre qué tipo de trabajo corre.** Una ley sin dominio declarado se aplica donde no corresponde la primera vez que alguien la respeta.

**Y una tercera cosa que ninguna de las dos ramas cubre.** Un ejecutor que no pudo escribir el archivo —sin permiso, sin la herramienta, sin la ruta— tiene que reportarlo como **fallo**, no como nota al final. En un review se nota porque los hallazgos vuelven igual; en un `EJ` el pedido volvería *cumplido* con el artefacto inexistente. Criterio del Core: `La superficie del ejecutor`.

---

## El criterio de reparto

Una sola línea, y vale para cualquier ejecutor barato, no solo para Codex:

```txt
el artefacto YA TIENE contrato escrito  ->  ejecutar es mecanico   ->  ejecutor barato
el artefacto es DONDE SE DECIDE         ->  modelo fuerte, con el vault cargado
```

De ahí sale un corolario que ordena el trabajo del sistema entero: **un artefacto sin contrato no se puede abaratar.** Mientras el `SOL` no tuvo forma medida, el `EJ` no se podía delegar — no porque faltara una herramienta, sino porque no había spec cerrada contra la cual ejecutar. Escribir contratos no es burocracia: es lo que habilita el ahorro.

**Esta nota es la autoridad del criterio y de la ley de arriba, y desde el 2026-09-01 tiene ejecutable y responsable.** El procedimiento vive en la skill `vaultrum-despacho` de esta capa; quien la usa es el `05_Despachante`, agente del Área de Producción. La nota dicta, la skill ejecuta y el agente responde — y ninguno de los tres repite lo que dice otro.

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

## Lo que esta nota mide, y lo que todavía no

`contar_contexto.py` mide el material del vault que se carga. Durante un tiempo, de este lado no había nada: el despacho era criterio escrito y no medición, y se declaró como deuda con la misma frase que esta capa ya había usado una vez.

**Desde el 2026-09-01 hay instrumento.** `Herramientas/despacho.py` cuenta sobre el log de la bandeja cuántas ejecuciones se delegaron, a qué ejecutor, cuánto tardó cada una y cuántas volvieron en fallo. Es un hecho leído de un archivo, no una estimación.

Lo que sigue sin medirse, declarado para que no se confunda con lo anterior:

```txt
tokens y plata     haría falta que el ejecutor devuelva su consumo, y hoy no lo devuelve.
                   Una ejecucion corta pudo ser cara y una larga barata.
el ahorro real     comparar contra el costo de no haber delegado exige una corrida
                   gemela que nadie hizo. Se sabe cuanto se delego, no cuanto se ahorro.
lo que no pasa     un comando disparado a mano dentro de una sesion no deja linea en
por la bandeja     el log. Si el numero parece bajo, esa es la primera sospecha.
```

**El reparto se aplica, no se afirma que ahorra.** La regla no cambió: cambió que ahora la mitad contable tiene número, y la mitad que no se puede contar está escrita como lo que es.

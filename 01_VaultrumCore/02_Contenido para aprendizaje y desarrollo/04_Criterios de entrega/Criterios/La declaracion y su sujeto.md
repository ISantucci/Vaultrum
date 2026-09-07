## Que es

Una declaracion es cualquier cosa que se escribe **sobre** un artefacto sin ser el artefacto: una excepcion que lo exime de una regla, un manifiesto que congela su version, un permiso, una cita que lo usa como evidencia.

Toda declaracion necesita nombrar a su sujeto. Hay dos formas de nombrarlo y una es fragil.

> **Una declaracion sobre algo nombra ese algo, no donde esta guardado.**

```txt
por RUTA        carpeta/subcarpeta/artefacto.md
                funciona hasta la primera mudanza

por IDENTIDAD   artefacto
                el nombre, el numero, lo que no cambia cuando cambia el lugar
```

## Por que existe

Porque el modo de falla de la primera forma no se parece a un error de puntero: se parece a deuda nueva.

Cuando un artefacto se mueve, su declaracion por ruta deja de aplicar. El artefacto vuelve a fallar la regla de la que estaba eximido, **como si nadie lo hubiera declarado nunca**. Quien mira el conteo ve que el sistema empeoro y sale a buscar que se rompio en el contenido. No se rompio nada del contenido: se rompio el puntero.

```txt
lo que pasa      un archivo cambia de carpeta
lo que se ve     el conteo de fallas sube
lo que se busca  que empeoro en el contenido
lo que paso      nada del contenido: la declaracion apunta a donde ya no esta
```

Es caro por asimetria. La causa real —repuntar una linea— es la reparacion mas barata que existe, y es la ultima que alguien va a probar, porque el sintoma sugiere cualquier otra cosa.

## La regla

> Una declaracion se ata a la **identidad** de su sujeto.
> Y el instrumento que lee declaraciones **avisa** cuando una no aplica a nada.

Las dos mitades hacen falta y hacen cosas distintas.

La primera reduce la rotura: un artefacto que se archiva, se reordena o cambia de estante sigue siendo el mismo artefacto, y su declaracion lo sigue.

La segunda cubre lo que la primera no puede: un artefacto se puede renombrar, borrar o reemplazar. Ahi la identidad tambien queda huerfana — y lo unico que separa un fallo silencioso de una decision es que alguien lo diga.

> **Lo que convierte el fallo silencioso en decision no es la identidad: es el aviso.**

El aviso no falla. Reparar una declaracion huerfana es juicio del area duena, y un instrumento que frena por eso frena por algo que no puede resolver solo. Nombra, y sigue.

## El precio, y que se hace con el

La identidad no es gratis: **puede ser ambigua**. Dos proyectos pueden tener cada uno su `QA-001`, su `GDS-001.0` o su marco comun, y una declaracion por identidad los cubriria a los dos cuando solo uno fue declarado.

Eso no invalida la regla. Pide una tercera cosa del instrumento:

```txt
identidad que corresponde a UN archivo      se usa
identidad que corresponde a VARIOS          se avisa, y para ese caso se vuelve
                                            a la ruta -- que es lo unico que
                                            los distingue
```

Un instrumento que resuelve la ambiguedad adivinando es peor que uno que exige la ruta: elige un sujeto sin decir que eligio.

## Como se aplica

Al escribir cualquier mecanismo que lea declaraciones:

```txt
1. ¿Que identifica al sujeto sin depender de donde esta?
   Un numero de la cadena, un nombre, un id. Si no hay ninguno, el sujeto no
   esta bien definido -- y ese es el hallazgo, no la ruta.

2. ¿El instrumento reporta las declaraciones que no aplicaron a nada?
   Si no, cada mudanza futura va a producir deuda aparente.

3. ¿Reporta cuando una identidad corresponde a mas de un sujeto?
   Si no, la declaracion mas comoda es la mas peligrosa.
```

Y al mover, renombrar o archivar cualquier cosa: **la mudanza incluye repuntar lo que hablaba de ella**. Correr el instrumento antes y despues no es prolijidad; es la unica forma de ver la diferencia entre lo que rompio la mudanza y lo que ya estaba roto.

## Cuando NO aplica

No aplica a un link. Un wikilink de Obsidian ya resuelve por nombre y sobrevive la mudanza solo: ahi el problema es el inverso —la ambiguedad— y lo resuelve calificar la ruta.

No aplica cuando el sujeto **es** un lugar. Una regla que exime a una carpeta entera se declara por carpeta, y esta bien: el sujeto no es el archivo que hoy vive ahi, es el subarbol.

No aplica a una declaracion de una sola vez, que se escribe, se usa y se tira en la misma corrida. Nada la va a leer despues de una mudanza.

## Regla final

> Si borrar una carpeta puede hacer que una regla del sistema deje de aplicarse sin que nadie se entere, la regla no estaba declarada sobre lo que creias.

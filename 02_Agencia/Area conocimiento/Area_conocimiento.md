## Propósito

El Área de Conocimiento es **la memoria de la Agencia**.

No produce proyecto. Hace dos cosas que ninguna otra área hace: cuida que lo que se trabaja **quede escrito y se entienda**, y decide qué de lo trabajado **vuelve al Core** como criterio.

```txt
Un área que no escribe lo que hizo, lo vuelve a hacer.
Un sistema que no absorbe lo que aprendió, no aprende: acumula.
```

Las dos mitades son la misma: sin documentación no hay de dónde cosechar, y sin cosecha la documentación es archivo muerto. Esta área existe para que Vaultrum se nutra de su propio trabajo.

---

## Dónde está parada

**No está al final de la cadena.** Está debajo, junto a Arquitectura. Las dos sostienen a las demás sin producir proyecto, y ninguna aparece en la columna vertebral de numeración.

```txt
Arquitectura   la forma del VAULT   dónde vive, de qué índice cuelga, con qué aristas
Conocimiento   la forma del TEXTO   si se entiende, si falta algo, si está dicho dos veces
               y la PERTENENCIA     a qué cuerpo de conocimiento pertenece lo nuevo
```

La frontera es dura y se lee en una línea: **el arquitecto decide dónde vive una nota; Conocimiento decide a qué pertenece y cómo está escrita.** Cuando el área necesita colocar algo en el vault, no lo coloca: le pide el emplazamiento al arquitecto y lo cita. Cuando el arquitecto necesita saber si una nota nueva duplica criterio existente, no lo decide: pregunta acá.

---

## Los tres servicios

Cada uno declara su momento de entrada. Un área que solo puede entrar cuando otra ya cerró está condenada a acomodar, no a decidir — por eso esta entra tres veces y no una.

### Modo Copiloto — durante

Un área está escribiendo su artefacto y Conocimiento la acompaña: qué falta, qué está dicho dos veces, qué se afirma sin evidencia, qué no se va a entender dentro de tres meses.

**Asiste, no firma.** El `GDS` sigue siendo de Game Design aunque Conocimiento lo haya ayudado a escribir. Si Conocimiento firmara, la trazabilidad diría que el diseño lo hizo el bibliotecario.

### Modo Gate — al cerrar un artefacto

Verificación **mecánica** contra el contrato de salida del tipo: `documentacion.py` corre solo y devuelve un número. Si pasa, el artefacto cierra. Si falla, y solo entonces, se llama al Copiloto.

Este modo existe por una razón concreta: el que se olvida de documentar se olvida de pedir ayuda para documentar. Un copiloto que solo entra cuando lo llaman no evita el olvido; un gate que corre solo, sí.

### Modo Cosecha — al cerrar una entrega

Qué de lo que se trabajó merece volver al Core. Es la autonutrición del sistema, y es lo único que esta área firma.

---

## El instrumento

El área no evalúa documentación a ojo. La medición la hace `Herramientas/documentacion.py`:

```txt
python3 "02_Agencia/Area conocimiento/Herramientas/documentacion.py" <ruta>
python3 "02_Agencia/Area conocimiento/Herramientas/documentacion.py" <ruta> --verificar
python3 "02_Agencia/Area conocimiento/Herramientas/documentacion.py" <ruta> --cosecha
```

`--verificar` devuelve código 1 si un artefacto no nombra su insumo, le falta una sección de su contrato, declara un "no aplica" sin decir qué queda ausente, afirma un número sin fuente, nombra un archivo del vault que no está en disco, repite un párrafo que ya vive en otro lado, o cierra sin declarar su estado.

`--cosecha` no opina: junta la evidencia de lo trabajado —la traza de operación, los remediales declarados en los `VE`, lo que ya espera en Staging— para que el Cosechador decida sobre hechos y no sobre memoria.

**La autoridad para condicionar el trabajo de otra área se sostiene en poder probar lo que se afirma.** Lo que la herramienta no prueba —si el texto se entiende, si el criterio es correcto, si el aprendizaje vale— se sigue verificando a mano y **se declara como juicio**, nunca como medición.

---

## Las seis leyes de la documentación

Ninguna se inventó acá. Las seis ya estaban escritas en el vault, sueltas, sin nadie que las midiera.

### Ley 1 — El artefacto declara su insumo

Un artefacto downstream no existe sin su insumo upstream. Si un `GDS` no nombra su `RQ`, la cadena se lee entera y no se puede recorrer hacia atrás.

### Ley 2 — La forma del contrato está completa

Cada tipo tiene secciones obligatorias. No se deducen abriendo un artefacto: se leen en el contrato de salida del área. Lo que hoy hay en `Herramientas/contratos.txt` es una **semilla medida** sobre los artefactos reales, y se reemplaza cuando los contratos existan.

### Ley 3 — Una omisión declarada es criterio; una silenciosa es un hueco

Un "no aplica" es una afirmación verificable, no un atajo: dice **qué dimensión del entregable queda ausente**. Un "no aplica" pelado es un hueco con buena letra.

### Ley 4 — Ningún número sin fuente

Una afirmación con número y sin instrumento ni fuente es una estimación disfrazada de medición. Se arregla midiendo o **declarándola como estimación**. Las dos salidas son válidas; disfrazarla no.

### Ley 5 — Lo que se afirma terminado existe en disco

Un artefacto no está reportado si lo que dice que produjo no está donde dice. Es el borde de salida de la cadena, y es donde más se rompe.

### Ley 6 — No se dice dos veces

Si el mismo párrafo vive en dos archivos, uno de los dos sobra o los dos están mal ubicados. Repetir el Core es la forma más cara de citarlo.

### Corolario — El artefacto declara su estado

`Cerrado`, `Ajustar` o `Pausado`. Vale para lo que cierra algo: un `TL`, un `EJ`, un `VE`. El estado de un `GDS` o un `SOL` vive en el índice de su área, no adentro del artefacto, y pedírselo sería inventar una regla que el vault no tiene.

---

## Sub-agentes del área

### [[01_Copiloto_Documentacion]]

Rol ancla. Acompaña a un área mientras escribe: devuelve observaciones sobre la forma del texto, nunca una reescritura. Asiste, no firma.

### [[02_Cosechador]]

Decide **con criterio qué merece volver al Core**, sobre la evidencia que junta el instrumento y no sobre memoria. No todo entra. Clasifica el caso y prepara los candidatos.

### [[03_Documentador]]

Escribe cada aprendizaje candidato como un `.md` claro en Staging, útil para humanos e IAs: qué es, cuándo aplica, qué NO es, cómo se usa.

### [[04_Bibliotecario_Pertenencia]]

Decide **a qué cuerpo de conocimiento pertenece** lo nuevo, detecta duplicación, resuelve conflictos —si ya existe algo parecido se actualiza en vez de duplicar— y arma el diff. Pide el emplazamiento al arquitecto y lo cita; no coloca la nota por su cuenta.

### [[05_Validador_Documentacion]]

Corre el instrumento y **cierra los tres modos**. Falla la entrega si un artefacto queda fuera de ley, si una observación del Copiloto se presentó como medición, o si un candidato llega a Staging sin destino ni criterio.

---

## Flujos del área

Cada flujo es un paso del loop. Se entra por el que corresponde al estado del trabajo, no por todos.

### [[01_Flujo_Copiloto]]

Acompañar a un área mientras escribe su artefacto.

### [[02_Flujo_Gate_Documentacion]]

Medir un artefacto contra su contrato y cerrarlo o rebotarlo.

### [[03_Flujo_Cosecha]]

Juntar la evidencia de lo trabajado, clasificar el caso y decidir qué se absorbe.

### [[04_Flujo_Retrospectiva]]

Caso 1 — el desarrollo salió del Core: se revisa por fricciones y `main` casi no cambia.

### [[05_Flujo_Aprendizaje_Branch]]

Caso 2 — hubo conocimiento nuevo real: detectar, escribir, ubicar, presentar el diff y mergear con aprobación.

### [[06_Flujo_Experimento]]

Caso 3 — una idea que quizás sirve: se evalúa, y si no sirve se descarta sin tocar el Core.

---

## Modelo de versiones del Core

El área sigue siendo la única que propone cambios a `main`, y lo hace con el modelo de siempre:

```txt
VaultrumCore        = main            (fuente de verdad, curada)
Proyecto / idea     = branch          (el trabajo de las áreas de producción)
Aprendizaje útil    = commit          (propuesta de cambio al Core)
Entrar al Core      = merge a main    (requiere revisión + aprobación del maintainer)
Descartar           = branch tirada   (no toca el Core)
```

**Es una metáfora de versionado, no la operación de git.** Un `COMMIT-XXX` es una propuesta de conocimiento; el commit del repositorio es otra cosa y no es de esta área. Ver *Lo que esta área ya no hace*.

---

## Staging (y por qué esta área no tiene `Salidas/`)

La carpeta `Staging` es la pizarra de **commits pendientes**: aprendizajes escritos que esperan aprobación. Es **transitoria**: cuando un aprendizaje se mergea al Core, se limpia; si se descarta, también.

La zona de trabajo es:

- [[00_Staging|Staging]] — lo que está ahí es candidato, no criterio

**Excepción declarada a la estructura de área.** Las otras áreas tienen `Salidas/`. Esta tiene `Staging/` en su lugar, y es deliberado por dos razones:

- su salida registrable es el **commit al Core**, que por definición vive en el Core y no acá — guardar además una copia sería duplicar `main`;
- lo que produce asistiendo **no es una salida suya**: se incorpora al artefacto del área dueña y no lleva su firma. Un informe de gate que quedara archivado sería historial de un trabajo ajeno.

Se declara porque una omisión declarada es criterio y una omisión silenciosa es un hueco.

---

## Lo que esta área ya no hace

**El commit de git salió del área.** Estaba acá por un accidente de la metáfora: el área se llamó *control de versiones* y se le colgó el control de versiones literal. Nada de eso es conocimiento.

```txt
la política del repositorio        →  `04_IA Operativa/03_Operar Vaultrum`
cuándo se commitea un proyecto     →  Producción, atado al `VE` en Cerrado
la verificación previa al commit   →  Área de Control de Calidad, con su `QA`
el gate de forma del pre-commit    →  Arquitectura, que ya era dueña del hook
```

El servicio real que esto prestaba —**seguro de vida para no perder trabajo**— no se borró: se movió con él, y lo declara `03_Operar Vaultrum`.

---

## Encadenado con las otras áreas

Recibe de: **todas las áreas**, en dos momentos distintos — mientras escriben (Copiloto) y al cerrar (Gate y Cosecha). Y de la **Escuela**, que entrega candidatos `EST` desde su Biblioteca.

Entrega a: **el artefacto del área dueña** (observaciones, sin firma) y a **VaultrumCore** (merge aprobado).

Puente con la Escuela: la Escuela mira **afuera** y no mergea al Core; Conocimiento mira **adentro** y es el único que propone a `main`. Toma el `EST`, hace dedup, pertenencia y diff, y lo presenta al owner. Decide qué se vuelve criterio indexado del Core y qué queda como libro de referencia en la Biblioteca.

---

## Regla operativa

Primero medir, después opinar.
Primero criterio, después redacción.
Después pertenencia, sin duplicar.
Después el diff.
Recién con tu aprobación, merge al Core.

Ningún aprendizaje entra al Core sin pasar por criterio y aprobación.

---

## Límites del área

No hace trabajo de producción: no arma `RQ`, `GDS`, `SOL` ni `EJ`. **No firma el artefacto de otra área** ni decide su contenido: dice qué falta, no qué decir. No coloca notas en el vault por su cuenta. No mergea sin aprobación. No acumula historial. No infla el Core "por las dudas": si un aprendizaje no es claro y reutilizable, no entra.

Y no presenta juicio como medición. Un informe que hace eso vale menos que uno que no mide nada, porque el segundo por lo menos no engaña.

---

## Skill del área

El área corre como la skill `vaultrum-conocimiento` (fuente versionada en `02_Agencia/Area conocimiento/Skills/vaultrum-conocimiento/SKILL.md`).

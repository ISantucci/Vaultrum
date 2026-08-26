## Propósito

El Área de Arquitectura cuida **la forma del vault**, no su contenido.

Ninguna otra área se ocupa de esto: Producción decide qué se hace, Game Design cómo se juega, Programación cómo se implementa, Conocimiento qué vuelve al Core. Todas escriben notas. Nadie, hasta ahora, se ocupaba de que esas notas **se puedan recorrer**.

El Área de Arquitectura existe para una sola pregunta:

```txt
¿Se puede entrar por un índice y llegar caminando a cualquier nota,
sin que el mapa se convierta en una telaraña?
```

Pero no la responde limpiando. La responde **antes**.

---

## El área no repara: dicta la forma

El arquitecto de un edificio no pasa el trapo cuando la obra quedó sucia. Dice cómo se construye y dónde va cada cosa, y por eso después no hay nada que limpiar.

Este área funciona igual. Cuando otra área va a tocar la forma del vault —crear una nota, abrir un índice, meter contenido nuevo, purgar links— **no ejecuta por su cuenta: le pide el plano al arquitecto**, y el arquitecto le explica cómo se hace eso en Vaultrum sin romper ninguna ley.

La razón es económica, no estética:

```txt
932 links de más entraron uno por uno, cada uno razonable.
Sacarlos costó una pasada entera y no produjo nada nuevo.
Dictar la forma antes cuesta un plano.
```

Ese es el fin del área. **La pureza no se consigue limpiando seguido: se consigue no ensuciando.** Cuando el arquitecto trabaja bien, las ejecuciones de las demás áreas salen más limpias y más baratas, y las pasadas de reparación dejan de hacer falta.

---

## Los tres modos

El área presta tres servicios. Cada uno se declara en su salida.

### Modo Plano

Un área va a hacer algo que toca la forma y **no sabe cómo hacerlo sin romper nada**. El arquitecto no ejecuta: entrega el procedimiento **en cascada**, paso por paso, con las leyes que aplican a cada uno, qué se mide entre paso y paso y qué gate cierra cada etapa. El área ejecuta con el plano en la mano.

Ejemplo: *"vamos a purgar los links de la Biblioteca"*. El plano dice qué ley se aplica primero, por qué el frontmatter va antes que las tablas, por qué las notas flotando se cuelgan al final y no al principio, y qué medición corre entre cada paso.

### Modo Emplazamiento

Entra **contenido nuevo** al vault y hay que decidir dónde vive. El arquitecto lee los índices existentes, evalúa de cuál debería colgar, en qué escalón, con qué aristas y qué índices hay que tocar — y **coloca la estructura**: crea la ruta, engancha la nota a su índice y escribe la cascada.

El **cuerpo** de la nota lo escribe el área dueña del contenido. El **lugar** lo decide el arquitecto. Esa es la división: fondo del área, forma del arquitecto.

Ejemplo: entran tres papers de estructuras de datos al Core. El arquitecto decide si cuelgan de `06_Estructuras de datos` o abren una sección nueva, si necesitan un índice intermedio, y deja los enganches escritos para que el área solo llene el contenido.

### Modo Pasada

El modo residual: medir lo que ya existe, repararlo y verificarlo. Es lo que las tres pasadas anteriores hicieron. **Sigue existiendo, pero deja de ser el propósito del área**: si el modo Plano y el modo Emplazamiento funcionan, una pasada solo debería hacer falta cuando entra material viejo de afuera o cuando el owner quiere una revisión completa.

---

## Las seis leyes del grafo

Las seis leyes no se inventaron acá: se **leyeron midiendo el Core**, que ya las cumplía sin tenerlas escritas. Son descripción del sistema que el owner construyó, formalizada para que el resto del vault pueda cumplirla.

### Ley 1 — El link es el título de la sección

Un índice enlaza a sus hijos desde el título: `## [[Hijo]]`. Debajo, prosa que dice qué contiene y cuándo consultarlo.

El link no se lee: se navega. La explicación no compite con él.

### Ley 2 — Cascada de un solo escalón

Un índice enlaza a sus **hijos directos** y a nadie más. No hay saltos de nivel ni links de vuelta al padre: para volver está la carpeta.

El escalón se mide **entre índices, no entre carpetas**. Una carpeta contenedora que no tiene índice propio no agrega un escalón: sus notas siguen siendo hijas directas del índice de arriba.

### Ley 3 — La hoja no linkea: sale

Una nota terminal no enlaza en el medio del contenido. Si tiene que continuar, cierra con `## Hacia donde seguir` y una línea por salida:

```txt
→ [[Índice de la sección que sigue]]
```

Y puede no tener ninguna. **Los caminos tienen su fin**: que una nota no lleve a ninguna otra no es un defecto, es el final del recorrido.

La salida va **hacia adelante**: al índice de la sección que sigue, nunca al índice del que la nota ya cuelga. Escribir el encabezado arriba de un link de vuelta al padre no lo convierte en salida — es un retorno, y lo prohíbe la Ley 2. `grafo.py` lo mide por dónde aterriza la arista, no por el rótulo de la sección (`ARQ-013`).

### Ley 4 — La prosa nombra con backticks

Mencionar no es enlazar. Cuando el texto necesita nombrar otro lugar sin invitar a ir, escribe la ruta o el nombre entre backticks:

```txt
El peso vive en `05_Escuela/Biblioteca/` y se carga on-demand.
```

La bibliografía, los cruces y las referencias **se nombran, no se enlazan**. Un libro que cita treinta fuentes no puede aportar treinta aristas al mapa.

### Ley 5 — Un puente por capa, y declarado

Una capa enlaza a otra desde **una sola nota**, y esa nota **dice en su cuerpo que es el puente**. Las dos mitades cuentan: una capa con un solo cruce que no se declara está tan fuera de ley como una con nueve.

Los dos puentes vivos del vault son `Experiencia de juego`, del Core hacia la Biblioteca, y `02_Indice Agencia`, de la Agencia hacia la Escuela.

### Ley 6 — Cero aristas invisibles

Ningún link en frontmatter. Ningún link adentro de una celda de tabla. Un link que no se ve al leer la nota pero pesa en el mapa es ruido puro: no ayuda a quien lee y ensucia a quien navega.

---

## Tres corolarios operativos

### Nada flota, y todo se alcanza

Toda nota cuelga de un índice. Si una nota existe y ningún índice la enlaza, o le falta el índice o le sobra la nota. No hay tercera opción.

Y colgar no alcanza: la nota tiene que ser **alcanzable caminando desde `00_START_HERE`**. Un racimo de notas que se enlazan entre sí y no cuelga de ningún camino real no flota según el conteo, y sin embargo no se llega.

### El padre apunta al hijo, y el hijo nunca al padre

Un link responde **una sola pregunta**: *¿de quién cuelga esto?* Nunca *¿de dónde salió?* De ahí salen tres cosas que se verifican sin discutir:

```txt
toda nota tiene exactamente un padre
todo link baja
para volver esta la carpeta
```

**El que sabe primero es el que enlaza.** Cuando Producción define un timeline, ahí mismo sabe en qué requerimientos se parte: el `TL` enlaza sus `RQ`, y el `RQ` nombra su timeline con backticks. Aplicado a cualquier par: si el padre puede nombrar al hijo en el momento en que lo crea, el link vive en el padre.

Y su corolario de forma, que evita el descanso vacío: **un escalón existe si separa algo.** Un índice que solo reenvía no es un escalón.

### La cadena se nombra, no se enlaza

La contención es un árbol. La **cadena** —`RQ` → `GDS` → `UXS` → `SOL` → `EJ`— no lo es: converge (siete requerimientos entran en una sola solución técnica) y cruza carpetas. No entra en un árbol en ninguna de las dos direcciones:

| Si la cadena se enlaza… | Qué rompe |
|---|---|
| hacia abajo (`RQ` → su `GDS`) | el `GDS` queda con dos padres, y el `SOL` con siete |
| hacia arriba (`GDS` → su `RQ`) | el hijo apunta al padre |

Por eso se **nombra con backticks** (Ley 4). No se pierde trazabilidad: vive dibujada en la *secuencia de trabajo* del timeline y en la trazabilidad del `VE`, que son bloques de texto y no aristas.

Y de acá sale la prueba que vuelve decidible cualquier caso nuevo:

```txt
si al enlazar una relacion alguna nota queda con dos padres,
esa relacion no es contencion: se nombra, no se enlaza.
```

**Esto corrige el corolario anterior** —*"la cadena sí puede cruzar de rama: una salida declara su insumo directo, en una línea rotulada"*—, que era el permiso bajo el cual entraban 33 aristas laterales solo en el cuaderno de un proyecto. Origen: `ARQ-014`; el aprendizaje sube por `COMMIT-006`.

Todo lo demás que cruce de rama es telaraña.

---

## Sub-agentes del área

### [[01_Consultor_Forma]]

Entrega el plano. Traduce lo que otra área va a hacer en un procedimiento en cascada con sus leyes, su orden y sus gates. No ejecuta.

### [[02_Emplazador]]

Ubica lo que entra. Lee los índices, decide de cuál cuelga el contenido nuevo y coloca la estructura. No escribe el cuerpo de la nota.

### [[03_Auditor_Grafo]]

Mide. Corre la herramienta, clasifica cada link por posición y dirección, y entrega el estado real del grafo sin proponer nada todavía.

### [[04_Reparador_Cascada]]

Repara. Toma el informe del Auditor y propone la corrección mínima: qué link se convierte en backtick, qué nota le falta a qué índice, qué tabla se vuelve cascada.

### [[05_Validador_Pureza]]

Valida y cierra **los tres modos**. Vuelve a medir y falla la entrega si algo quedó flotando, roto, ambiguo, escondido, salteando niveles o cruzando fuera del puente.

---

## Flujos del área

### [[01_Flujo_Plano]]

Convertir la intención de otra área en un procedimiento en cascada que se pueda ejecutar sin romper ley.

### [[02_Flujo_Emplazamiento]]

Decidir dónde vive el contenido nuevo y dejar la estructura colocada.

### [[03_Flujo_Auditoria_Grafo]]

Medir el estado del grafo y entregar el informe.

### [[04_Flujo_Reparacion_Cascada]]

Proponer y aplicar la corrección mínima sobre lo que el informe marcó.

### [[05_Flujo_Validacion_Pureza]]

Verificar que lo entregado dejó el grafo en ley, y registrar el `ARQ`.

---

## Los cuatro gates del área

Un gate que no se puede verificar mecánicamente no es un gate, es una intención. Los cuatro corren, no se piden.

| Gate | Cuándo | Qué exige | Cómo se verifica |
|------|--------|-----------|------------------|
| Forma | antes de crear, mover o purgar notas, índices o carpetas | plano o emplazamiento del arquitecto, citado en la salida del área | el `ARQ` existe y la salida lo nombra |
| Emplazamiento | contenido nuevo entrando al vault | índice padre declarado antes de escribir el cuerpo | el verificador: nada flota, nada inalcanzable |
| Cierre | toda entrega que escribió notas | grafo en ley | `grafo.py --verificar` devuelve 0 |
| Core | contenido nuevo entrando a `01_VaultrumCore` | emplazamiento más aprobación explícita del owner | excepciones nota por nota en `Herramientas/excepciones.txt` |

El gate de Cierre corre además en `.git/hooks/pre-commit`: un commit que deja el grafo fuera de ley no entra. Se puede saltear con `git commit --no-verify`, y saltearlo es una decisión declarable, no un descuido.

Editar el cuerpo de una nota que ya existe **no** dispara ningún gate. El área se activa cuando cambia la forma, no cuando cambia el texto.

---

## Salidas del área

### [[00_Indice_arq]]

El registro de las intervenciones de arquitectura. Cada `ARQ-XXX` declara su **modo** — Plano, Emplazamiento o Pasada — y queda con lo que se midió, lo que se hizo y cómo quedó.

---

## Herramienta del área

El área no audita a ojo. La medición la hace `Herramientas/grafo.py`, que recorre el vault y clasifica cada link por posición y dirección:

```txt
python3 "02_Agencia/Area arquitectura/Herramientas/grafo.py" .
python3 "02_Agencia/Area arquitectura/Herramientas/grafo.py" . --verificar
```

`--verificar` devuelve código 1 si algo quedó flotando, inalcanzable, roto, ambiguo, escondido, salteando niveles o cruzando de capa fuera del puente declarado. Es el gate de cierre de cualquier entrega que haya tocado notas.

La herramienta ignora los bloques de código y el código en línea: un nombre entre backticks no es una arista. Las excepciones se declaran una por una en `Herramientas/excepciones.txt`, con su razón escrita; una capa entera fuera del veredicto no es una excepción, es un agujero.

---

## Regla operativa

El área **dicta antes de que se construya, y mide antes de tocar**. Nunca propone una reparación sobre una impresión: primero corre la herramienta, después propone, y recién con aprobación aplica.

Y **no toca el Core sin el owner**. El Core es la fuente de la ley: si el Core la infringe, eso es una decisión del owner, no una corrección del área.

---

## Límites del área

**No escribe contenido.** El cuerpo de una nota es del área que la pide. El arquitecto puede crear el archivo vacío en su lugar y dejar los enganches escritos, pero lo que la nota dice no es suyo.

**No decide qué debe existir; decide dónde vive.** Si un área pregunta si una nota hace falta, la respuesta no es del arquitecto. Si pregunta dónde poner una nota que ya decidió que hace falta, la respuesta es suya y es vinculante.

**No renombra archivos por su cuenta.** Cuando un nombre repetido vuelve ambiguo un link, usa la ruta completa en el wikilink y deja el renombre como decisión del owner.

**No borra notas. No mergea al Core.**

Si una nota no tiene índice del cual colgar, el área **no inventa el índice**: lo reporta y pregunta de qué debería colgar. Un índice nuevo cambia la forma del vault y eso lo aprueba el owner.

---

## Encadenado con otras áreas

El área **no está al final de la cadena: está debajo de todas**. No recibe el trabajo de nadie y no se lo entrega a nadie; le presta forma a quien la va a necesitar.

```txt
        cualquier área va a tocar la forma
                    ↓
        Área de Arquitectura  →  ARQ modo Plano o Emplazamiento
                    ↓
        el área ejecuta con el plano
                    ↓
        gate de cierre: grafo.py --verificar
                    ↓
        si falla → ARQ modo Pasada
```

Producción la consulta al abrir un timeline que va a generar salidas nuevas. La Escuela la consulta cada vez que entra un libro a la Biblioteca. Conocimiento la consulta antes de mergear al Core, porque un merge es contenido nuevo entrando a la capa más protegida.

Lo que el área aprende sobre la forma del vault puede volver al Core como criterio, por la vía de siempre: `Area conocimiento/Staging/` y aprobación del owner. Las seis leyes viven acá hasta que el owner decida promoverlas.

---

## Skill del área

La skill ejecutable del área es `vaultrum-arquitecto`, en `Skills/vaultrum-arquitecto/`.

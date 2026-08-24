## Propósito

El Área de Arquitectura cuida **la forma del vault**, no su contenido.

Ninguna otra área se ocupa de esto: Producción decide qué se hace, Game Design cómo se juega, Programación cómo se implementa, Conocimiento qué vuelve al Core. Todas escriben notas. Nadie, hasta ahora, se ocupaba de que esas notas **se puedan recorrer**.

El Área de Arquitectura existe para una sola pregunta:

```txt
¿Se puede entrar por un índice y llegar caminando a cualquier nota,
sin que el mapa se convierta en una telaraña?
```

No corrige redacción, no discute criterio y no toca lo que una nota dice. Solo dónde caen sus links y de qué índice cuelga.

---

## Las seis leyes del grafo

Las seis leyes no se inventaron acá: se **leyeron midiendo el Core**, que ya las cumplía sin tenerlas escritas. Son descripción del sistema que el owner construyó, formalizada para que el resto del vault pueda cumplirla.

### Ley 1 — El link es el título de la sección

Un índice enlaza a sus hijos desde el título: `## [[Hijo]]`. Debajo, prosa que dice qué contiene y cuándo consultarlo.

El link no se lee: se navega. La explicación no compite con él.

### Ley 2 — Cascada de un solo escalón

Un índice enlaza a sus **hijos directos** y a nadie más. No hay saltos de nivel ni links de vuelta al padre: para volver está la carpeta.

### Ley 3 — La hoja no linkea: sale

Una nota terminal no enlaza en el medio del contenido. Si tiene que continuar, cierra con `## Hacia donde seguir` y una línea por salida:

```txt
→ [[Índice de la sección que sigue]]
```

Y puede no tener ninguna. **Los caminos tienen su fin**: que una nota no lleve a ninguna otra no es un defecto, es el final del recorrido.

### Ley 4 — La prosa nombra con backticks

Mencionar no es enlazar. Cuando el texto necesita nombrar otro lugar sin invitar a ir, escribe la ruta o el nombre entre backticks:

```txt
El peso vive en `05_Escuela/Biblioteca/` y se carga on-demand.
```

La bibliografía, los cruces y las referencias **se nombran, no se enlazan**. Un libro que cita treinta fuentes no puede aportar treinta aristas al mapa.

### Ley 5 — Un puente por capa, y declarado

Una capa enlaza a otra desde **una sola nota**, y esa nota dice en su cuerpo que es el puente. El ejemplo original es `Experiencia de juego` en el Core: indexa la Biblioteca y declara que es la única dirección en la que el Core enlaza hacia afuera.

### Ley 6 — Cero aristas invisibles

Ningún link en frontmatter. Ningún link adentro de una celda de tabla. Un link que no se ve al leer la nota pero pesa en el mapa es ruido puro: no ayuda a quien lee y ensucia a quien navega.

---

## Dos corolarios operativos

### Nada flota

Toda nota cuelga de un índice. Si una nota existe y ningún índice la enlaza, o le falta el índice o le sobra la nota. No hay tercera opción.

### La cadena sí puede cruzar de rama

Una salida puede declarar **su insumo directo** — un `GDS` apuntando a su `RQ`, un `EJ` a su `SOL`, un `VE` a su `TL` — en una línea rotulada, **una sola por documento**. Es la única arista lateral legal del vault, porque no es navegación: es trazabilidad de la cadena.

Todo lo demás que cruce de rama es telaraña.

---

## Sub-agentes del área

### [[01_Auditor_Grafo]]

Mide. Corre la herramienta, clasifica cada link por posición y dirección, y entrega el estado real del grafo sin proponer nada todavía.

### [[02_Reparador_Cascada]]

Repara. Toma el informe del Auditor y propone la corrección mínima: qué link se convierte en backtick, qué nota le falta a qué índice, qué tabla se vuelve cascada.

### [[03_Validador_Pureza]]

Valida. Vuelve a correr la medición después de la reparación y falla la entrega si algo quedó flotando, roto, ambiguo o escondido.

---

## Flujos del área

### [[01_Flujo_Auditoria_Grafo]]

Medir el estado del grafo y entregar el informe.

### [[02_Flujo_Reparacion_Cascada]]

Proponer y aplicar la corrección mínima sobre lo que el informe marcó.

### [[03_Flujo_Validacion_Pureza]]

Verificar que la reparación dejó el grafo en ley, y registrar el `ARQ`.

---

## Salidas del área

### [[00_Indice_arq]]

El registro de las pasadas de arquitectura. Cada `ARQ-XXX` es una auditoría con su reparación y su verificación.

---

## Herramienta del área

El área no audita a ojo. La medición la hace `Herramientas/grafo.py`, que recorre el vault y clasifica cada link por posición y dirección:

```txt
python3 "02_Agencia/Area arquitectura/Herramientas/grafo.py" .
python3 "02_Agencia/Area arquitectura/Herramientas/grafo.py" . --verificar
```

`--verificar` devuelve código 1 si algo quedó flotando, roto, ambiguo o escondido. Sirve como gate antes de cerrar cualquier entrega que haya tocado notas.

La herramienta ignora los bloques de código: un link adentro de un bloque ```` ``` ```` no es una arista y no debe contarse como tal.

---

## Regla operativa

El área **mide antes de tocar**. Nunca propone una reparación sobre una impresión: primero corre la herramienta, después propone, y recién con aprobación aplica.

Y **no toca el Core sin el owner**. El Core es la fuente de la ley: si el Core la infringe, eso es una decisión del owner, no una corrección del área. El Auditor lo reporta aparte y ahí se detiene.

---

## Límites del área

No escribe contenido. No decide qué nota debe existir. No renombra archivos por su cuenta. No mergea al Core.

Si una nota no tiene índice del cual colgar, el área **no inventa el índice**: lo reporta y pregunta de qué debería colgar.

---

## Encadenado con otras áreas

Cualquier área que escriba notas deja trabajo para ésta. La forma sana de encadenar es que el área que escribió corra el `--verificar` antes de cerrar, y que el Área de Arquitectura entre solo cuando falla o cuando el owner pide una pasada completa.

Lo que el área aprende sobre la forma del vault puede volver al Core como criterio, por la vía de siempre: `Area conocimiento/Staging/` y aprobación del owner. Las seis leyes viven acá hasta que el owner decida promoverlas.

---

## Skill del área

La skill ejecutable del área es `vaultrum-arquitecto`, en `Skills/vaultrum-arquitecto/`.

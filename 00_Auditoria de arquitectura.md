# Auditoría de arquitectura del vault — AUD-001

> **Registro fechado.** Ésta fue la primera auditoría del vault, hecha a mano. La serie continúa como `ARQ` en el Área de Arquitectura (`02_Agencia/Area arquitectura/Salidas/`), que además dejó la medición automatizada. Lo de abajo describe el estado de ese momento, no el de hoy.

> Cierra el ítem 11 del backlog de `00_Leyes de Vaultrum (bitacora)`: *"la cadena se probó de punta a punta produciendo un entregable, pero no se auditó la arquitectura del vault en sí"*.
>
> Alcance auditado: 351 notas en disco; 125 leídas en detalle (todas las estructurales: índices, `Area_*.md`, `Agentes/`, `Flujos/`, `Skills/`, capas 03/04/05 y raíz). Las ~226 notas de contenido profundo del Core —patrones, managers, optimización, VaultrumAi— **no** se auditaron nota por nota: se auditó su indexación, no su contenido.
>
> Método: verificación mecánica (resolución de wikilinks, sincronía índice↔disco, detección de duplicación literal, ubicación de checklists) más lectura de las capas estructurales. Lo mecánico está contado; lo cualitativo está argumentado y marcado como tal.

---

## Resumen

El vault está en mejor estado del que su propio backlog sugería. La sospecha de partida —duplicación entre `Area_*.md` / `Agentes/` / `Flujos/` / `Skills/`— **no se confirmó**: la regla de capas se cumple casi perfecto en la Agencia.

Lo que sí apareció son huecos de otro tipo: una capa que no cumple la regla que la Agencia sí cumple, una contradicción entre dos documentos sobre si el Core enlaza hacia abajo, y un ciclo de conocimiento que estaba escrito y nunca había corrido.

| Dimensión | Resultado | Estado |
|-----------|-----------|--------|
| Wikilinks que resuelven | 4 no resuelven, **las 4 son plantillas** (`TL-XXX_Nombre_Descriptivo`) | correcto |
| Índices ↔ disco (salidas) | 54 de 54 salidas indexadas | correcto |
| Duplicación literal entre capas | 9 frases en 24 archivos de área | correcto |
| Checklists solo en la Skill (Agencia) | 6 de 6 | correcto |
| Checklists solo en la Skill (Escuela) | 3 archivos fuera de la Skill, 15 ítems | **hallazgo** |
| Estructura de área completa | 5 de 6 áreas; Conocimiento sin `Salidas/` | **hallazgo** |
| Índice de capa ↔ disco | `04_Indice IA Operativa` no listaba `05_Modo_Operacion` | **corregido** |
| Coherencia Core ↔ Biblioteca | contradicción declarada entre dos documentos | **corregido** |
| Ciclo de conocimiento | 3 commits en Staging, 0 mergeados; 2 `EST` sin handoff | **corregido** |

---

## Lo que está bien (y conviene no tocar)

**1. La regla de capas se cumple.** Era la sospecha principal del backlog y no se confirmó.

```txt
frases (>=55 chars) repetidas entre Area_*.md / Agentes/ / Flujos/ / SKILL.md

Area produccion        2      Area ui-ux          1
Area game design       3      Area programacion   1
Area level design      2      Area conocimiento   0
                                          total   9
```

Nueve frases en 24 archivos. La mayoría son pares `Agentes/ ~ Flujos/`, que es el solapamiento más natural y el menos dañino. No hay nada que podar.

**2. Los checklists operativos viven donde el índice dice.** En la Agencia, los 6 checklists están en los 6 `SKILL.md` y en ningún otro lado. La regla *"ante divergencia manda la Skill"* no tiene divergencias que resolver.

**3. Los índices están sincronizados con el disco.** Las 54 salidas registradas (3 `TL`, 19 `RQ`, 17 `GDS`, 2 `UXS`, 3 `SOL`, 3 `EJ`, 2 `VE`, 5 `EST`) están todas indexadas. No hay salidas huérfanas ni entradas fantasma.

**4. Los wikilinks resuelven.** Sobre 125 archivos estructurales, los únicos cuatro que no resuelven son plantillas de ejemplo dentro de índices y del README. Ninguno es un link roto real.

Vale decirlo porque el instinto al auditar es buscar problemas: **la higiene estructural de este vault es buena.** Los hallazgos de abajo son huecos puntuales, no deuda acumulada.

---

## Hallazgos

### H1 — La Escuela no cumple la regla de capas que la Agencia sí cumple

**Evidencia:**

```txt
05_Escuela/Agentes/01_Bibliotecario.md            6 items [ ]
05_Escuela/Agentes/04_Validador_Estudio.md        6 items [ ]
05_Escuela/Flujos/04_Flujo_Validacion_Estudio.md  3 items [ ]
```

Quince ítems de checklist operativo fuera de `Skills/vaultrum-escuela/SKILL.md`.

**Por qué importa.** La regla existe porque *lo que corre tiene que ser autosuficiente*: si la Skill no trae el checklist, la misión corre sin él. Y si lo trae **además** de las fichas, hay dos fuentes que van a divergir. Hoy la Escuela está en el peor de los dos casos posibles según cuál sea: o la Skill está incompleta, o hay duplicación esperando divergir.

**Causa probable.** La Escuela se diseñó después de la refactorización a Áreas, tomando prestada su estructura (`Agentes/`, `Flujos/`, `Salidas/`, `Skills/`) sin heredar la regla de capas, que vive en `02_Indice Agencia.md` — un documento de otra capa. La regla está escrita donde la Escuela no la lee.

**Corrección propuesta:** mover los checklists a `SKILL.md`, dejar la referencia en las fichas, y **promover la regla de capas a un lugar que aplique a todo el vault** en vez de al índice de la Agencia. Mientras viva ahí, cada capa nueva la va a volver a incumplir.

*No aplicada en esta pasada:* toca el contenido operativo de la Escuela y merece su propio paso, no un arreglo de auditoría.

### H2 — El Área de Conocimiento no tiene `Salidas/`

Las otras cinco áreas tienen las cuatro carpetas. Conocimiento tiene `Agentes/`, `Flujos/`, `Skills/` y `Staging/`.

**Es defendible:** su producto no es un artefacto propio, es un merge al Core; y `Staging/` es transitorio por diseño. Pero el índice de la Agencia dice que un área *"nunca termina solo en una charla, termina depositando una salida registrable"*, sin declarar la excepción.

**Corrección propuesta:** declararla explícitamente en `Area_conocimiento.md` — *"esta área no tiene `Salidas/`: su salida registrable es el commit al Core, y su zona de trabajo es `Staging/`"*. Es una excepción legítima; lo que no puede ser es silenciosa, por el mismo criterio que aplica a los `no aplica` de `LDS`/`UXS`.

### H3 — Contradicción sobre si el Core enlaza hacia la Biblioteca — **corregida**

```txt
01_Indice VaultrumCore    decía: "El Core no enlaza hacia abajo"
00_Escuela                decía: "vía el índice por género del Core"
02_Indice Agencia         decía: "vía el índice por género del Core"
```

Dos capas asumían la existencia de un índice que la tercera declaraba inexistente por principio. En la práctica ganó la versión de la Escuela —el libro de Pong se consultó igual— pero por costumbre, no por diseño.

**Corregido:** el Core ahora tiene `Experiencia de juego`, un índice liviano hacia la Biblioteca, y `01_Indice VaultrumCore` explica la dirección del enlace en vez de negarla. El criterio queda: *el Core indexa, la Biblioteca pesa, el Core no depende*.

### H4 — El índice de IA Operativa no listaba `05_Modo_Operacion` — **corregido**

El documento que define los modos de operación (el switch Vaultrum/Owner, la pieza más sensible de esa capa) existía en disco y no figuraba en el índice de su propia capa. Un lector que entraba por el índice no lo encontraba.

**Corregido:** listado, junto con `06_Medicion de friccion` y la carpeta `Herramientas/`.

### H5 — El ciclo de conocimiento nunca había cerrado — **corregido**

Al momento de la auditoría: 3 commits en `Staging/`, 0 mergeados al Core. 2 `EST` *listos para handoff*, 0 entregados. El libro `01_Pong` en estado *En validación* y **ya usado como insumo de producción** en `TL-003`.

**Por qué es el hallazgo estructural más importante.** Toda la arquitectura se justifica en un ciclo `Core → Agencia → Conocimiento → Core`. Ese ciclo estaba escrito, tenía área, flujos, agentes y skill, y **nunca había corrido una vuelta completa**. Un ciclo que no cierra convierte al Core en biblioteca estática y a Conocimiento y Escuela en decorativas.

**Corregido:** los tres commits mergeados a la nueva sección `04_Criterios de entrega`, los tres `EST` con handoff hecho por indexación en `05_Experiencia de juego`, `01_Pong` promovido a *En la Biblioteca* con la regla de gobernanza que faltaba (*un libro solo es insumo válido si está En la Biblioteca*).

### H6 — El baseline dependía de un libro que no existía

`vaultrum-produccion` corría su definición de terminado con un checklist inline y una nota que decía *"fuente canónica futura: el libro `03_Definicion_de_terminado`, hoy Reservado"*.

Es exactamente el patrón que `COMMIT-003` describe: un insumo declarado que no existe, suplido por criterio propio. El pendiente estaba **declarado**, que es lo correcto — pero llevaba tres timelines declarado.

**Corregido:** el libro está escrito, sintetizando los Fundamentos 01/02/05 y el uso real en `VE-003`, y la skill apunta a él.

---

## Observaciones que no son hallazgos

No requieren acción. Se dejan escritas para que la próxima auditoría no las redescubra como si fueran problemas.

**El peso está donde no está el diferencial.** El Core concentra el 65% de la masa del vault (158 notas, ~1,2 MB) y es la parte más reemplazable: SOLID, patrones y algoritmos existen en cualquier bibliografía. La Agencia —la cadena con gates, que es lo que Vaultrum tiene y otros flujos de trabajo con IA no— es el 22%. No es un defecto: es una consecuencia de que el Core se escribió primero. Pero indica dónde conviene invertir de acá en adelante, y es lo que motivó reposicionar `README` y `00_START_HERE`.

**La gobernanza está escrita antes de tiempo.** `GOVERNANCE`, `CONTRIBUTING`, `Trademark`, `Sistema de contribucion` y un scoreboard, con `CONTRIBUTORS.md` de 408 bytes. No está mal escrita y no molesta; simplemente todavía no paga. Conviven además con un `Modo Owner` protegido por passphrase, que es un diseño explícitamente monousuario. La tensión entre *proyecto abierto* y *herramienta de una persona* está sin resolver — y es una decisión de dirección, no un defecto de arquitectura.

**Una sola muestra.** Todo lo que se validó de la cadena se validó sobre Pong, tres veces. `LDS` nunca corrió. No hay evidencia sobre géneros con dimensión espacial, persistencia, contenido o red, ni sobre entregables que no sean videojuegos. La cadena ya crujió una vez en esa única muestra (`GDS-003.0`), lo que sugiere que hay más por descubrir, no menos.

**La bitácora vive en la raíz.** `00_Leyes de Vaultrum (bitacora).md` es un documento de trabajo del owner —ideas sin formalizar, backlog abierto— sentado junto a `README.md` y `00_START_HERE.md`, que son la puerta pública. Funciona, pero mezcla dos audiencias en el mismo nivel.

---

## Qué queda abierto

```txt
H1  checklists de la Escuela fuera de su Skill        → paso propio
    promover la regla de capas fuera del índice de la Agencia
    (mientras viva ahí, cada capa nueva la va a incumplir)
    segunda muestra en un dominio distinto             → decisión del owner
    resolver la tensión abierto / monousuario          → decisión del owner
```

`H2` quedó cerrado: `Area_conocimiento` declara la excepción en su propia sección de Staging.

---

## Método

Los pasos mecánicos de esta auditoría —inventario, resolución de wikilinks, sincronía índice↔disco, cobertura de cada índice de capa— **ya no se hacen a mano**: los corre el Área de Arquitectura.

```txt
python3 "02_Agencia/Area arquitectura/Herramientas/grafo.py" .
python3 "02_Agencia/Area arquitectura/Herramientas/grafo.py" . --verificar
```

Quedan dos pasos que la herramienta no cubre y siguen siendo manuales:

```txt
- contar ítems de checklist fuera de los SKILL.md
- buscar frases largas repetidas entre Area_*.md / Agentes/ / Flujos/ / SKILL.md
```

El segundo es el que más ruido produce y el que menos encontró.

Para el peso y la carga de contexto, el instrumento es `04_IA Operativa/Herramientas/contar_contexto.py`.

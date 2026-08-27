## Índice de intervenciones de arquitectura (ARQ)

Registro de todo lo que el Área de Arquitectura hace sobre la forma del vault.

Cada `ARQ-XXX` declara su **modo** y queda con lo que se midió, lo que se hizo y en qué estado quedó el grafo.

---

## Los tres modos

| Modo | Qué registra | Cuándo |
|------|--------------|--------|
| Plano | el procedimiento en cascada que se le entregó a otra área | antes de que esa área toque la forma |
| Emplazamiento | dónde se ubicó contenido nuevo y qué índices se tocaron | cuando entra material al vault |
| Pasada | una medición con su reparación y su verificación | cuando hay que corregir lo que ya está |

Un `ARQ` declara un solo modo. Si una intervención empezó como plano y terminó reparando, son dos `ARQ`: el plano falló o la ejecución se desvió, y eso hay que poder leerlo separado.

---

## Regla de numeración

`ARQ-001`, `ARQ-002`, … en orden de ejecución. Una intervención por número, sin subíndices: la arquitectura no se fracciona por sistema. Un `ARQ` se corre entero o acotado a una capa, y eso se declara adentro.

Los `ARQ` **no cuelgan de la columna vertebral de numeración de la Agencia**: no son un eslabón de la cadena de producción, son intervenciones sobre el vault mismo.

---

## Registro

### [[ARQ-000_Auditoria_de_arquitectura|ARQ-000 — La primera auditoría del vault]]

Hecha a mano y fechada, antes de que el área existiera: qué está construido, qué está a medias y qué se prometió sin construir. Vivía en la raíz del vault, colgando de `00_START_HERE`; se trajo acá el 2026-08-25 porque una puerta no abre a un registro fechado. Es el `ARQ` cero de la serie.

### [[ARQ-001_Purga_Escuela_Agencia|ARQ-001 — Purga de Escuela y Agencia]]

Modo Pasada. Primera intervención. Formalización de las seis leyes leídas del Core y aplicación a `05_Escuela`, `02_Agencia` y la raíz. 1.504 links → 572, cero notas flotando.

### [[ARQ-002_Limpieza_del_Core|ARQ-002 — Limpieza del Core]]

Modo Pasada, sobre `01_VaultrumCore`. 82 wikilinks encerrados en bloques de código y 21 aristas de más. Quedó en 90% cascada y cero links fuera de posición.

### [[ARQ-003_Purga_de_lo_viejo|ARQ-003 — Purga de lo viejo]]

Modo Pasada. No sobre links: sobre texto que describía un vault que ya no existe. Restos de tabla en los ocho índices de Salidas, reglas de la forma vieja, secciones dobles y la auditoría de la raíz.

### [[ARQ-004_Las_leyes_sin_medir|ARQ-004 — Las leyes que no se medían]]

Modo Pasada. No sobre el vault: sobre la herramienta que lo mide. De las seis leyes, el verificador solo podía probar tres. Ley 2 y Ley 5 quedaron implementadas, la alcanzabilidad se camina de verdad y el Core deja de estar exento en bloque. 21 fallas que el gate anterior no veía, reparadas.

### [[ARQ-005_El_area_que_dicta|ARQ-005 — El área que dicta]]

Modo Pasada, sobre el área misma. El charter se invirtió: de reparar después a dictar antes. Tres modos declarados, dos agentes y dos flujos nuevos, cuatro gates y el hook de pre-commit que hace que el gate de cierre corra solo.

### [[ARQ-006_La_herramienta_de_Comunidad|ARQ-006 — La herramienta de Comunidad]]

Modo Emplazamiento, el primero. La capa de Comunidad necesitaba un verificador de formato para sus publicaciones y pasó por el arquitecto antes de crearlo. `Herramientas/post.py` quedó a un escalón de su capa, sin una sola arista nueva en el grafo.

### [[ARQ-007_La_purga_que_casi_no_hay|ARQ-007 — La purga que casi no hay]]

Modo Plano, el primero. El owner pidió limpiar lo viejo y lo repetido; la medición devolvió una sola edición aplicable, tres preguntas para el owner y doce repeticiones que resultaron deliberadas. El plano vale por lo que evitó borrar.

### [[ARQ-008_El_espejo_que_coincidia|ARQ-008 — El espejo que coincidía con el espejo]]

Modo Pasada, sobre la Biblioteca. El catálogo era un espejo exacto de 19 KB con cero entradas en cascada. Al derivar la vista de las fichas apareció lo que el espejo tapaba: `01_Pong` cerrado en el estante y *En validación* en su ficha. Los índices bajaron 35% y el desacuerdo ficha–estante pasó a ser un gate.

### [[ARQ-009_La_segunda_area_que_entraba_tarde|ARQ-009 — La segunda área que entraba tarde]]

Modo Plano, el segundo, y el primero entregado a otra área para que reescriba su propio charter. El Área de UI/UX tenía el mismo defecto que ésta antes de `ARQ-005` —entrar cuando el otro ya cerró— y además ningún instrumento. El plano ordenó los nueve pasos, midió el grafo antes de tocar y cerró con delta cero sobre 49 fallas preexistentes que no son suyas.

---

## Regla del índice

Una intervención entra acá recién cuando pasó por el `05_Flujo_Validacion_Pureza`. Una reparación sin verificación no es una intervención: es un cambio suelto.

### [[ARQ-010_La_puerta_que_abria_al_pasado|ARQ-010 — La puerta que abría al pasado]]

Pasada posterior a la mudanza de los proyectos: la puerta llevaba a un registro fechado, cuatro archivos compartían nombre, un índice estaba huérfano por una mayúscula y los artefactos mudados cruzaban de capa sin declarar. De 105 fallas a 2, las dos del Core y previas.

### [[ARQ-011_El_area_que_versionaba_lo_que_no_era_suyo|ARQ-011 — El área que versionaba lo que no era suyo]]

Pasada sobre el Área de Conocimiento, la tercera con el defecto de `ARQ-005` y `ARQ-009`, y la primera con un trabajo que no era suyo: el commit de git salió a tres dueños declarados. El área pasó de un servicio a tres —Copiloto, Gate y Cosecha—, estrenó `documentacion.py` y ganó el validador que era la única de las ocho en no tener. Cinco notas más, tres aristas menos, delta cero.

### [[ARQ-012_El_area_que_cierra|ARQ-012 — El área que cierra]]

Modo Emplazamiento, el más grande hasta ahora: una sección nueva al Core y un área nueva a la Agencia, las dos sobre control de calidad, con la frontera criterio/procedimiento como decisión principal. 34 notas, cero excepciones nuevas. De paso apareció el Core fuera de ley —el puente hacia la Biblioteca había quedado huérfano por un borrado accidental— y se restauró.

### [[ARQ-013_El_estante_que_volvia_sobre_si_mismo|ARQ-013 — El estante que volvía sobre sí mismo]]

Modo Pasada, disparada por un reporte del owner: un nido raro entre la Escuela y sus áreas. Las 52 fichas de un estante cerraban con un link de vuelta a su propio índice —105 aristas en un nodo, el único caso del vault— y el verificador decía EN LEY mientras pasaba, porque la etiqueta `salida` se reconocía por su rótulo y no por su efecto. Ocho hallazgos. La Escuela pasó de 184 a 130 links y de 67% a 95% de cascada; `grafo.py` mide la Ley 2 por primera vez, con test de fixture en los dos sentidos. Queda abierto el hallazgo 8: el gate corre sobre la copia de trabajo y el vault **publicado** tiene 33 links rotos que nadie midió nunca.

### [[ARQ-014_El_hijo_que_senalaba_al_padre|ARQ-014 — El hijo que señalaba al padre]]

Modo Emplazamiento sobre el cuaderno de un proyecto. El cuaderno enlazaba 49 artefactos al mismo escalón y 33 de ellos devolvían la arista hacia arriba. Quedó en 4 links, 54 notas con un padre cada una y cero links que suban. La decisión de fondo: en un proyecto conviven **contención** —que es un árbol y se enlaza— y **cadena** —que converge, cruza carpetas y por eso se nombra con backticks—. Contradice el corolario vigente de la cadena, que sube por `COMMIT-006`.

### [[ARQ-015_La_regla_escrita_y_el_segundo_proyecto|ARQ-015 — La regla escrita, y el segundo proyecto]]

El owner pidió los dos movimientos en orden: anotar el aprendizaje en el área y recién después aplicarlo. La regla —y el error de razonamiento que costó dos pasadas— quedó en el charter, la skill, el Emplazador y su flujo; el corolario viejo de la cadena quedó corregido. Después, `VaultrumWorld` con el mismo molde: 15 links en el cuaderno a 2, 14 aristas que subían a cero. Al haber un segundo proyecto apareció lo que uno solo no podía mostrar: los índices de área necesitaban nombre único por proyecto. La capa entera quedó en 100% de links en título de sección y cero laterales.

### [[ARQ-016_Las_cincuenta_aristas_que_no_bajaban|ARQ-016 — Las cincuenta aristas que no bajaban]]

Modo Pasada sobre todo el vault menos el Core. Las 51 aristas que no bajaban caían en cinco patrones y los cinco pasaron el mismo test: cada destino ya tenía exactamente un padre, así que ninguna era contención. 50 a backticks; queda una, el README hacia la puerta, que no es un padre sino la entrada. Agencia 76% → 99% de cascada, Escuela y Comunidad al 100%. Incluye la corrección de una cifra que esta área publicó mal en `ARQ-014` y `ARQ-015`: los 44 links del Core eran 16, y 15 de ellos son salidas legales de la Ley 3.

### [[ARQ-017_El_area_que_no_sabia_para_que_estaba|ARQ-017 — El área que no sabía para qué estaba]]

Pasada de diagnóstico sobre el charter del Área de Conocimiento: siete hallazgos, un charter propuesto y cinco decisiones que son del owner. Corrida el 2026-08-25 y entregada como `.txt` suelto en la raíz; registrada acá el 2026-08-26 sin editar una coma. **Diagnóstico, no intervención** — la reescritura del charter necesita su propio plano y su propia aprobación.

### [[ARQ-018_La_puerta_que_faltaba|ARQ-018 — La puerta que faltaba]]

Emplazamiento de la raíz: entran `CLAUDE.md`, `AGENTS.md` y `skills.bat`; salen los dos `.txt` sueltos, el `__pycache__` y un lock huérfano. Deja escrita la distinción que faltaba: **el vault tiene dos entradas** —`00_START_HERE` para el humano, `CLAUDE.md` para la máquina— y la segunda no se enlaza porque no se navega. Desvío declarado: se colocó antes de pedir el plano.

### [[ARQ-019_La_rama_que_no_existia|ARQ-019 — La rama que no existía]]

Emplazamiento sobre el Core: la sección de Optimización pasa de cuatro bloques por fase del método a ocho ramas por recurso, con el diagnóstico por encima de todas. El material académico del owner entró completo y cerró el hueco que la medición mostró: GPU era el 3% de una sección de 250 KB, no existía `GPU Bound` teniendo `CPU Bound`, y dos notas de herramientas apuntaban a ocho notas de GPU que nadie había escrito. De 40 notas a 79, sin borrar ninguna hoja: las carpetas se renombraron en vez de vaciarse. Tres índices retirados con su contenido absorbido y declarado. Cero excepciones nuevas. Desvío declarado: se colocó y se escribió en la misma corrida, y el cuerpo de las notas no lo puso el área dueña.


### [[ARQ-020_Las_treinta_y_ocho_fichas_que_entraron|ARQ-020 — Las treinta y ocho fichas que entraron]]

Emplazamiento sobre la Biblioteca: entran 38 fichas de los lotes `EST-008` y `EST-009`, y los estantes de Fuentes y Documentación real pasan de 30 y 52 a 56 y 64. Tres decisiones de forma: **sin índice intermedio** aunque el registro crezca —agregaría un escalón y rompería la Ley 2—, **una sección de registro nueva** para los cuatro documentos que reconstruyen en vez de registrar, y **la bibliografía entre backticks**, que evitó más de sesenta aristas laterales. La medición intermedia mostró la Ley 2 en vivo: tres fichas escritas y sin entrada en su índice aparecieron como flotando. Cero notas movidas, cero excepciones nuevas, grafo en ley. Desvío declarado: se colocó antes de pedir el plano — **la tercera seguida**, y queda abierto el hallazgo de que las otras áreas no tienen el pedido de plano en su flujo.
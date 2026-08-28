## Índice de Candidatos de Estudio (EST)

Registro de todas las salidas de la Escuela Vaultrum.

Cada `EST-XXX` es un fundamento destilado, citado y validado, listo para el handoff al Área de Conocimiento.

---

## Registro

El listado de misiones vive en `00_Registro_est`, que no se versiona.

---

## Regla

- Un `EST` cuelga siempre de una misión de estudio (gap + presupuesto + barra).
- Estados posibles: En investigación / En destilación / En validación / Listo para handoff / **Handoff hecho** / Cerrada / Catalogada / Descartado.
- **Toda misión declara `estado` en su frontmatter.** No es adorno: `biblioteca.py --verificar` cruza el estado de cada ficha contra el de su misión, y una pieza cerrada colgando de una misión abierta es una falla. Una misión sin `estado` declarado no se puede consultar, y ese cruce no corre.
- El `EST` declara su misión en su propia ficha, con las citas y el resultado de AiCare. El índice la nombra.
- Un `EST` con handoff pasa a ser candidato de commit en el Área de Conocimiento; el merge a `main` lo aprueba el owner.
- **Un libro solo es insumo válido de producción cuando está *En la Biblioteca*.** Un libro *En estudio* o *En validación* es material en curso: Producción lo rechaza en su gate de insumo y deriva a Escuela.

---

## Handoff a Conocimiento — resultado

**Todos los handoff se resolvieron por indexación, no por copia**: el Core guarda el puntero en `Experiencia de juego` y el contenido queda en la Biblioteca, cargándose on-demand. Ningún libro fue copiado al Core y **ninguno fue promovido a criterio propio** — promover es una decisión aparte del owner, caso por caso.

```txt
EST-001 → 01_Pong  +  primer contenido de 01_Loop_de_experiencia
EST-004 → 04_Playbook_de_diseno
EST-005 → 05_Fundamentos_de_experiencia_ludica
EST-006 → los 12 Fundamentos 06–17  +  52 documentos
EST-010 → 02_Game_feel  +  02_Plataformero_2D
EST-012/013/014 → el estante de Construccion entero, por una tercera tabla del puente
```

**El puente estuvo atrasado tres misiones y nadie lo medía.** Al abrir esta pasada, `Experiencia de juego` indexaba **5 de 17** Fundamentos y **1 de 2** Juegos, mientras su propia regla decía que *"lo único que puede crecer en esta sección es la tabla"*. Un libro escrito, promovido y no indexado **no está disponible**: Producción parte del Core, y lo que el Core no nombra, para Producción no existe. El faltante nunca fue de la Escuela — era del handoff, que se daba por hecho al escribir el libro.

Hoy el puente indexa las tres tablas completas: 17 Fundamentos, 2 Juegos, 3 de Construcción.

Efecto secundario del handoff: `03_Definicion_de_terminado` pasó de *Reservado* a escrito, sintetizando 01/02/05 y el uso real en `VE-003`. La skill `vaultrum-produccion` ya no lleva el checklist inline como pendiente declarado: apunta al libro.

**Lo que NO se hizo:** promover ningún libro a criterio propio del Core. Indexar es que las áreas lo encuentren; promover es que pase a ser regla. Lo segundo requiere una decisión aparte del owner, caso por caso.

---

## EST-006 — cerrada

Los cinco pasos que esta sección listaba como pendientes se corrieron:

```txt
1. Decision del owner sobre 02_Game_feel   → escrito en EST-010
2. Pass de AiCare                          → corrido 2026-08-28: los 12 libros juntos
                                             dan 53.2k = 133% de 40k. EXCEDIDO.
                                             Un GDS real (05 + 3 pilares) da 19.5k = 49%.
                                             Poda: ninguna. Los doce son insumo de gate.
3. Validacion libro por libro               → auditoria completa + segunda pasada:
                                             8 residuales encontrados y reparados
4. Handoff a Conocimiento                   → por INDEXACION, como EST-001/004/005
5. Aprobacion del owner                     → los 17 libros En la Biblioteca
```

**Lo que enseñó, y quedó en el instrumento.** Esta ficha declaró `En estudio — sin AiCare, sin handoff` mientras sus 64 piezas declaraban cerrado, y `--verificar` contestaba EN NORMA porque comparaba la ficha con el estante y los dos coincidían. Es el defecto de `01_Pong` un nivel más arriba: **el acuerdo entre dos espejos no dice nada del original.** `biblioteca.py --verificar` tiene ahora un tercer cruce que le pregunta a la misión, y por eso todas las misiones declaran `estado` en su frontmatter.

Deudas que la misión dejó abiertas y siguen abiertas: los dos esqueletos de libro que conviven (forma, no defecto), los 13 libros de Juegos escritos y sin implementar a la espera de la decisión de nombres, y el backlog de fuentes sin destilar — que `EST-011` ordenó por prioridad y `EST-012`/`013`/`014` empezaron a bajar.

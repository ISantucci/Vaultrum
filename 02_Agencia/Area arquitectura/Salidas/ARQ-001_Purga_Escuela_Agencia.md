---
tipo: pasada de arquitectura
alcance: 05_Escuela, 02_Agencia, 04_IA Operativa, raíz del vault
core: no modificado salvo una nota huérfana enganchada, con aprobación
estado: cerrada
---

# ARQ-001 — Purga de Escuela y Agencia

Primera pasada del Área de Arquitectura. Nació de una observación del owner: el Core se navega por índices en cascada y el resto del vault, no. El grafo de la Biblioteca era una telaraña.

---

## Qué se midió antes de tocar

La medición se corrió sobre `HEAD` con `Herramientas/grafo.py`, clasificando cada link por posición dentro de la nota y por dirección en el árbol, e ignorando los bloques de código.

| Capa | Notas | Links | Título | Tabla | Mitad de frase | Frontmatter | Lateral | Links/KB |
|------|-------|-------|--------|-------|----------------|-------------|---------|----------|
| 01_VaultrumCore | 164 | 186 | 70% | 3% | 6% | 0% | 4% | 0,16 |
| 02_Agencia | 116 | 293 | 9% | 18% | 29% | 0% | 34% | 0,76 |
| 05_Escuela | 123 | 972 | 1% | 34% | 43% | 10% | 48% | 1,98 |
| Raíz | 4 | 37 | 0% | 14% | 62% | 0% | 0% | 0,88 |

Totales: **422 notas, 1.504 links, 2 links ambiguos, 30 notas flotando.**

El diagnóstico en una línea: **el Core enlazaba desde estructuras y bajaba en cascada; la Escuela enlazaba desde el contenido y cruzaba de costado.** La Escuela era el 29% de las notas y el 64% de los links, con una densidad 12 veces mayor que la del Core.

Dato que habilitó la purga: **ninguna de las 8 skills del vault navega por wikilink.** Contienen 15 wikilinks decorativos contra 48 referencias por ruta. Las skills abren archivos por path; el grafo es para el owner.

---

## Qué se hizo

Seis pasos, de menor a mayor riesgo, midiendo entre cada uno.

| Paso | Alcance | Links afectados |
|------|---------|-----------------|
| Frontmatter → texto plano | 96 notas | −100 |
| Celdas de tabla → texto plano | índices y catálogos | −386 |
| Mitad de frase → backticks | ~90 notas | −530 |
| Tablas-registro → cascada `## `Hijo`` | 11 índices | +147 secciones |
| Bibliografía de los libros → backticks | 6 libros de Fundamentos | −84 |
| Registros de misión dejan de navegar | 7 notas `EST` | −18 |

Y el enganche de lo que flotaba: 16 bloques de índice insertados (flujos y salidas de las seis áreas, flujos y salidas de la Escuela, portada de la Biblioteca), los títulos de capa de `00_START_HERE` convertidos en links, y una nota del Core que no colgaba de ningún índice enganchada a `Managers`.

---

## Cómo quedó

| Capa | Notas | Links | Título | Tabla | Mitad de frase | Frontmatter | Lateral | Links/KB |
|------|-------|-------|--------|-------|----------------|-------------|---------|----------|
| 01_VaultrumCore | 164 | 187 | 70% | 3% | 6% | 0% | 4% | 0,16 |
| 02_Agencia | 126 | 220 | 44% | 0% | 0% | 0% | 30% | 0,53 |
| 05_Escuela | 123 | 138 | 91% | 0% | 0% | 0% | 3% | 0,29 |
| Raíz | 4 | 14 | 36% | 0% | 0% | 0% | 0% | 0,33 |

Totales: **1.504 links → 572**, cero notas flotando, cero links rotos, cero links ambiguos, cero aristas invisibles fuera del Core. Las 432 notas incluyen las 10 que suma esta área.

La Escuela pasó de 7,9 a 1,1 links por nota y de 1,98 a 0,29 links por KB: la densidad del Core.

Las aristas laterales que quedan en la Agencia no son telaraña: son la cadena. Un `GDS` declara su `RQ`, un `EJ` su `SOL`, un `VE` su `TL` — una línea rotulada por documento. Es la única lateral legal del vault.

---

## Lo que no se tocó

**El Core.** Conserva 19 links en prosa y en la tabla de su nota puente (`Experiencia de juego`). Son del owner y son deliberados: la Ley 4 admite la mención enlazada cuando es una decisión, y la Ley 5 define esa nota como el único puente del Core hacia otra capa. Queda como decisión del owner, no como corrección pendiente.

**Los nombres repetidos.** Cuatro archivos se llaman `00_Indice_salidas.md` en cuatro áreas distintas. Los links que apuntaban ahí quedaban ambiguos; se resolvieron escribiendo la ruta completa en el wikilink. El renombre sigue siendo la solución de fondo y es decisión del owner.

---

## Verificación

```txt
python3 "02_Agencia/Area arquitectura/Herramientas/grafo.py" . --verificar
```

Camino verificado a mano: `00_START_HERE` → `05_Escuela` → `La Biblioteca` → `Documentación real` → `DOOM — source release`. Cuatro escalones, sin búsqueda, sin pasar por ninguna arista lateral.

---

## Qué dejó como aprendizaje

Las seis leyes del grafo, escritas en `Area_arquitectura`. Salieron de medir el Core: no son criterio nuevo, son el criterio que ya estaba funcionando sin estar enunciado.

Candidato a promoción al Core por la vía del Área de Conocimiento, con aprobación del owner.

---
tipo: pasada de arquitectura
alcance: 01_VaultrumCore
estado: cerrada
modelo: Managers.md
---

# ARQ-002 — Limpieza del Core

Segunda pasada. El Core ya era el más sano del vault: 89% de sus aristas bajaban en cascada y no tenía una sola nota flotando. La pasada buscó lo que quedaba de más, con la nota `Managers` como modelo — es la que ya cumplía la ley entera sin excepciones.

---

## Lo que se encontró

**187 aristas reales y 82 wikilinks encerrados en bloques de código.**

Los 82 no eran links: Obsidian los muestra como texto, no se pueden clickear y no existen en el grafo. El caso extremo era `NPC`, la nota más grande de su sección, con **cero aristas propias**: sus 27 links estaban todos adentro de bloques.

Y ninguno de los 82 abría un camino nuevo: **los 82 apuntaban a una nota que ya era alcanzable por otra vía.**

El propio Core tenía la regla escrita. `Comportamientos` dice, textual:

```txt
Los comportamientos
→ no deben linkear hermanos por cercania.
```

---

## Qué se hizo

### Un bloque de código nunca contiene un link

Es el criterio de `Managers`: los links viven en listas y en títulos, y el bloque de código es para texto. Aplicado a los 82:

| Caso | Cuántos | Qué se hizo |
|------|---------|-------------|
| Salida declarada hacia un índice de sección, en `## Hacia donde seguir` | 15 | sale del bloque y pasa a ser link real (Ley 3) |
| Duplica la cascada `## `Hijo`` que ya está en la misma nota | 37 | pierde los corchetes |
| Hermano por cercanía, o mención lateral | 30 | pierde los corchetes |

Las 15 liberadas son las únicas que agregan alcance: desde una hoja de Fundamentos se salta al índice de la sección que sigue, que es exactamente lo que la nota ofrece cuando dice *"si ya hay un síntoma concreto"*.

### Veintiuna aristas de más

| Caso | Cuántas | Detalle |
|------|---------|---------|
| Salto de nivel | 4 | `01_Indice VaultrumCore` y `02_Contenido VaultrumCore` enlazaban nietos que el índice hijo ya enlaza |
| Duplicado exacto | 4 | el mismo destino enlazado dos veces en la misma nota |
| Par recíproco | 4 | dos pares A↔B entre hermanos que su índice ya conecta |
| Tabla de la nota puente | 6 | `Experiencia de juego` enlazaba seis libros sueltos de la Biblioteca |
| Mención en prosa | 3 | referencias a notas ya alcanzables, ahora nombradas con backticks |

La nota puente conserva sus dos aristas hacia la Biblioteca, ahora como títulos de sección: `## `00_Indice_fundamentos`` y `## `00_Indice_juegos``. Los seis libros los cascadea cada estante. Las tablas siguen ahí y se leen igual — dejaron de tejer.

---

## Cómo quedó

| | Antes | Después |
|---|-------|---------|
| Aristas reales | 187 | **181** |
| Wikilinks encerrados en bloques | 82 | **0** |
| Cascada | 89% | **90%** |
| Salida declarada | — | **8%** |
| Lateral | 4% | **0%** |
| En tabla / mitad de frase / frontmatter | 17 | **0** |
| Links por KB | 0,16 | **0,15** |

Todo lo que no es cascada en el Core son ahora tres cosas nombrables: **15 salidas declaradas** hacia los índices de sección de Optimización, **1 hermano** (la frase con la que `Cuando NO optimizar` se contrasta con `Medir antes de optimizar`) y **2 cruces de capa**, los dos desde la nota puente y los dos hacia un índice de estante.

---

## Qué cambió en la herramienta

Tres correcciones, todas por medir mal notas del Core:

- ignora el **código en línea**, además de los bloques: un nombre entre backticks no es una arista;
- reconoce `03_Optimizacion/Optimizacion.md` como índice — antes solo veía índices cuando el nombre de la carpeta no tenía prefijo numérico;
- **`salida` es una dirección propia**: un link desde `## Hacia donde seguir` hacia un índice no es una lateral, es la Ley 3 funcionando.

---

## Lo que no se tocó

El contenido. Ninguna nota cambió lo que dice: cambió dónde caen sus links y qué se lee como nombre en vez de como link.

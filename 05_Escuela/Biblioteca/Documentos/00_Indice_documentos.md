## Estante de Documentación real

**Artefactos** de la industria: documentos de diseño que se usaron de verdad, código fuente liberado, documentación oficial de motor y registros de proceso. No son libros destilados de Vaultrum (eso son [[00_Indice_fundamentos\|Fundamentos]] y [[00_Indice_juegos\|Juegos]]) ni bibliografía de estudio (eso es [[00_Indice_fuentes\|Fuentes]]): son **evidencia primaria**.

Existe para una cosa concreta: que **Producción y Game Design puedan mirar cómo lo resolvió alguien que ya lo hizo**, en vez de discutirlo en abstracto.

> **Regla de la casa:** la Biblioteca **no aloja** ninguno de estos documentos. Guarda la ficha, la referencia y la URL. Se estudia y se cita; no se copia.

---

## Consulta rápida — qué abrir según qué necesitás

| Necesito… | Abrí |
|-----------|------|
| Ver cómo se escribe un GDD real, de punta a punta | [[02_Shooter_Majestic_Revelations_design_doc_original_de\||Deus Ex — Majestic Revelations]] · [[01_Doom_Bible\|Doom Bible]] · [[10_Grand_Theft_Auto_Race_n_Chase_design_document\|GTA — Race'n'Chase]] |
| Justificar un **recorte de alcance** con evidencia histórica | [[01_Doom_Bible\|Doom Bible]] (lo que se planeó vs. lo que salió) · [[19_Star_Fox_2_documentos_de_diseno_y_manual\|Star Fox 2]] |
| Escribir un **pitch** corto y convincente | [[04_Diablo_pitch_original\|Diablo]] · [[05_BioShock_pitch_document\|BioShock]] · [[17_Guacamelee_design_pitch\|Guacamelee!]] |
| Fijar la **visión** de un proyecto en una página | [[06_Planescape_Torment_Vision_Statement\|Planescape: Torment]] · [[13_Wasteland_2_Vision_Document\|Wasteland 2]] |
| Diseñar **puzzles** y documentarlos | [[03_Grim_Fandango_Puzzle_Document\|Grim Fandango]] · [[48_ZACH_LIKE_los_cuadernos_de_diseno_de_Zachtronics\|ZACH-LIKE]] |
| Ver documentación de un estudio **de tamaño realista** (no AAA) | [[16_Rogue_Legacy_Design_Notes\|Rogue Legacy]] · [[51_Documentos_de_Double_Fine_via_Lee_Petty_y_de_Ninja_T\||Double Fine / Ninja Theory]] · [[15_Narbacular_Drop_documentos_el_predecesor_de_Portal\|Narbacular Drop]] |
| Arrancar un GDD **hoy** con una plantilla usable | [[43_Plantilla_oficial_de_GDD_de_Unity\|Plantilla oficial de GDD de Unity]] |
| Resolver **arquitectura de código** en Unity | [[37_Level_up_your_code_with_game_programming_patterns_Un\|Level up your code]] · [[38_Create_modular_game_architecture_with_ScriptableObje\|ScriptableObjects]] · [[42_Game_Programming_Patterns_Robert_Nystrom\|Game Programming Patterns]] |
| Leer **código real** de un juego terminado | [[30_DOOM_source_release\|DOOM]] · [[34_Celeste_codigo_fuente_del_juego_y_del_prototipo_PICO\|Celeste]] · [[31_Prince_of_Persia_Apple_II_codigo_fuente_original\|Prince of Persia]] |
| Entender **qué hace cada rol** en un equipo | [[47_The_Door_Problem_Liz_England\|The Door Problem]] |
| Ver **UX/UI de producción AAA** | [[49_Disenos_de_UX_UI_de_Destiny_y_Halo\|Destiny y Halo — UX/UI]] |
| Estudiar **diseño bajo restricción técnica extrema** | [[52_It_s_Behind_You_el_making_of_de_R_Type_para_ZX_Spect\||It's Behind You (R-Type)]] · [[29_Quake_GPL_source_release\|Quake]] |

---

## La unidad didáctica destacada: DOOM

Es el único caso del corpus donde están disponibles **la intención documentada y la implementación real del mismo proyecto**:

```txt
[[01_Doom_Bible]]        →  lo que se planeó y se descartó
[[30_DOOM_source_release]] →  lo que efectivamente se construyó
                    ↓
        leer los dos y ver dónde divergieron
```

Se consulta como **una sola unidad**, no como dos fichas sueltas. El segundo mejor ejemplar de esta clase es Prince of Persia ([[31_Prince_of_Persia_Apple_II_codigo_fuente_original|código]] + [[08_Prince_of_Persia_2_Design_Bible|design bible del 2]]).

---

## Regla de licencia — tres niveles

Todo documento de este estante entra clasificado en uno de tres niveles. **El nivel manda sobre qué se puede hacer con él.**

| Nivel | Qué es | Qué se puede hacer | Ejemplos |
|-------|--------|--------------------|----------|
| **A — licencia explícita** | Liberado formalmente por el titular (GPL, MIT, CC, publicación oficial) | Estudiar, citar, adaptar código según la licencia | id Software, Command & Conquer, OpenDUNE, OpenRA, docs de Unity/Unreal/Godot, Game Programming Patterns |
| **B — publicado sin licencia formal** | El autor lo puso a disposición, pero sin liberación explícita | Estudiar y citar. **No** copiar, no redistribuir, no alojar | Diablo (Brevik), Prince of Persia (Mechner), BioShock (Irrational), Al Lowe |
| **C — filtrado o decompilado** | Documento interno filtrado o ingeniería inversa de un producto comercial activo | Referenciar la existencia. **No** alojar, no distribuir, no basar producción en él | Deus Ex, Metal Gear Solid 2, CSE2 (bloqueado por HTTP 451) |

El caso CSE2 es el precedente: al intentar acceder devolvió un **HTTP 451 — Unavailable For Legal Reasons**. Queda fichado como precedente de política, no como material de consulta.

Ante la duda, el nivel es C y se frena para consultar al owner (regla de la Escuela: *si una fuente no tiene licencia clara, se resuelve con el owner antes de usarla*).

---

## Registro por familia

### Documentos de diseño reales

Los GDD, design bibles y pitches que efectivamente se usaron para construir un juego. Es el estante que responde "¿cómo se escribe esto de verdad?" — y, más útil todavía, "¿qué se descartó y por qué?".

| # | Documento | Autor / estudio | Año | Prioridad | Licencia |
|---|---|---|---|---|---|
| 01 | [[01_Doom_Bible\|Doom Bible]] | Tom Hall — id Software | 1992 | alta | incierta |
| 02 | [[02_Shooter_Majestic_Revelations_design_doc_original_de\|Shooter: Majestic Revelations (design doc original de Deus Ex)]] | Warren Spector y equipo — Ion Storm Austin | 1997 | alta | incierta |
| 03 | [[03_Grim_Fandango_Puzzle_Document\|Grim Fandango — Puzzle Document]] | Tim Schafer, Peter Tsacle, Eric Ingerson, Bret Mogilefsky, Peter Chan — LucasArts, abril | 1996 | alta | incierta |
| 04 | [[04_Diablo_pitch_original\|Diablo — pitch original]] | David Brevik — Condor, Inc. | 1994 | alta | a confirmar |
| 05 | [[05_BioShock_pitch_document\|BioShock — pitch document]] | Ken Levine y equipo — Irrational Games | 2002 | alta | a confirmar |
| 06 | [[06_Planescape_Torment_Vision_Statement\|Planescape: Torment — Vision Statement]] | Chris Avellone — Black Isle Studios | 1997 | alta | incierta |
| 07 | [[07_Fallout_Bible\|Fallout Bible]] | Chris Avellone — Black Isle / Interplay | 2002 | media | incierta |
| 08 | [[08_Prince_of_Persia_2_Design_Bible\|Prince of Persia 2 — Design Bible]] | Jordan Mechner / Brøderbund, 08/08/ | 1991 | media | incierta |
| 09 | [[09_Metal_Gear_Solid_2_Grand_Game_Plan\|Metal Gear Solid 2 — Grand Game Plan]] | Hideo Kojima — Konami | 2018 | media | incierta |
| 10 | [[10_Grand_Theft_Auto_Race_n_Chase_design_document\|Grand Theft Auto — "Race'n'Chase" design document]] | DMA Design | 1995 | alta | incierta |
| 11 | [[11_Coleccion_de_documentos_de_Al_Lowe_Leisure_Suit_Larr\|Colección de documentos de Al Lowe (Leisure Suit Larry y otros)]] | Al Lowe — Sierra On-Line | 1991 | media | incierta |
| 12 | [[12_Marble_Madness_design_document\|Marble Madness — design document]] | Mark Cerny — Atari Games | 1984 | baja | incierta |
| 13 | [[13_Wasteland_2_Vision_Document\|Wasteland 2 — Vision Document]] | inXile Entertainment, ~ | 2012 | media | incierta |
| 14 | [[14_What_Remains_of_Edith_Finch_documentos_de_concepto_t\|What Remains of Edith Finch — documentos de concepto tempranos]] | Giant Sparrow, ~ | 2014 | media | incierta |
| 15 | [[15_Narbacular_Drop_documentos_el_predecesor_de_Portal\|Narbacular Drop — documentos (el predecesor de Portal)]] | Nuclear Monkey Software | 2005 | alta | incierta |
| 16 | [[16_Rogue_Legacy_Design_Notes\|Rogue Legacy — Design Notes]] | Cellar Door Games, ~ | 2013 | alta | incierta |
| 17 | [[17_Guacamelee_design_pitch\|Guacamelee! — design pitch]] | DrinkBox Studios, ~ | 2012 | media | incierta |
| 18 | [[18_Sam_Max_Hit_the_Road_design_document\|Sam & Max: Hit the Road — design document]] | LucasArts | 1993 | baja | incierta |
| 19 | [[19_Star_Fox_2_documentos_de_diseno_y_manual\|Star Fox 2 — documentos de diseño y manual]] | Nintendo / Argonaut, ~ | 1995 | baja | incierta |

### Colecciones y repositorios

Agregadores. Cuando el documento puntual no está fichado acá, se busca primero en estos.

| # | Documento | Autor / estudio | Año | Prioridad | Licencia |
|---|---|---|---|---|---|
| 20 | [[20_Game_Documents_gamedocs_org\|Game Documents (gamedocs.org)]] | curador independiente, activo desde ~ | 2015 | alta | incierta |
| 21 | [[21_Video_Game_History_Foundation_Game_Design_Document_A\|Video Game History Foundation — Game Design Document Archive]] | Video Game History Foundation, colección en curso | — | alta | incierta |
| 22 | [[22_Computer_Game_Design_Documents_coleccion_Aric_Wilmun\|Computer Game Design Documents — colección Aric Wilmunder (LucasArts)]] | Aric Wilmunder — LucasArts, documentos de ~ | 1986 | alta | incierta |
| 23 | [[23_awesome_game_design_Roobyx\|awesome-game-design (Roobyx)]] | comunidad GitHub, mantenido | — | alta | explícita |
| 24 | [[24_Game_Design_Document_Resources_mikewesthad\|Game-Design-Document-Resources (mikewesthad)]] | Mike Hadley, comunidad GitHub | — | alta | incierta |
| 25 | [[25_Propuesta_de_Super_Smash_Bros_for_Wii_U_3DS_traducid\|Propuesta de Super Smash Bros. for Wii U / 3DS (traducida)]] | Masahiro Sakurai — Sora Ltd. / Bandai Namco, ~ | 2012 | media | incierta |
| 26 | [[26_Sloperama_Tom_Sloper_archivo_de_consejos_de_industri\|Sloperama — Tom Sloper, archivo de consejos de industria]] | Tom Sloper, desde ~ | 1999 | baja | incierta |
| 27 | [[27_GitHub_topic_game_design_document\|GitHub topic: game-design-document]] | GitHub, continuo | — | media | explícita |

### Código fuente liberado

La contraparte de los GDD: lo que efectivamente se construyó. Sirve para contrastar intención documentada contra implementación real.

| # | Documento | Autor / estudio | Año | Prioridad | Licencia |
|---|---|---|---|---|---|
| 28 | [[28_id_Software_organizacion_completa_en_GitHub_20_repos\|id Software — organización completa en GitHub (20 repos)]] | id Software, liberaciones entre | 1997 | alta | explícita |
| 29 | [[29_Quake_GPL_source_release\|Quake — GPL source release]] | John Carmack — id Software, código de | 1996 | alta | explícita |
| 30 | [[30_DOOM_source_release\|DOOM — source release]] | id Software, código de | 1993 | alta | explícita |
| 31 | [[31_Prince_of_Persia_Apple_II_codigo_fuente_original\|Prince of Persia (Apple II) — código fuente original]] | Jordan Mechner — Brøderbund, código | 1985 | alta | a confirmar |
| 32 | [[32_Command_Conquer_Remastered_Collection_codigo_fuente\|Command & Conquer Remastered Collection — código fuente (EA)]] | Westwood Studios / Electronic Arts, código de | 1995 | media | explícita |
| 33 | [[33_OpenDUNE_reimplementacion_de_Dune_II\|OpenDUNE — reimplementación de Dune II]] | proyecto comunitario OpenDUNE, sobre el original de Westwood de | 1992 | media | explícita |
| 34 | [[34_Celeste_codigo_fuente_del_juego_y_del_prototipo_PICO\|Celeste — código fuente del juego y del prototipo PICO-8]] | Maddy Thorson y Noel Berry — Extremely OK Games | 2018 | alta | incierta |
| 35 | [[35_CSE2_decompilacion_de_Cave_Story\|CSE2 — decompilación de Cave Story]] | Clownacy y colaboradores, decompilación de Cave Story v1.0.0.6 | 2004 | baja | bloqueada |
| 36 | [[36_OpenRA_reimplementacion_moderna_de_RTS_clasicos\|OpenRA — reimplementación moderna de RTS clásicos]] | proyecto comunitario OpenRA, activo desde | 2007 | media | explícita |

### Documentación oficial de motor

Material de estudio publicado por Unity, Unreal y Godot. Licencia limpia y aplicable directo a un proyecto en curso.

| # | Documento | Autor / estudio | Año | Prioridad | Licencia |
|---|---|---|---|---|---|
| 37 | [[37_Level_up_your_code_with_game_programming_patterns_Un\|Level up your code with game programming patterns (Unity)]] | Unity Technologies, con aportes de Wilmer Lin; edición ampliada reciente | — | alta | a confirmar |
| 38 | [[38_Create_modular_game_architecture_with_ScriptableObje\|Create modular game architecture with ScriptableObjects (Unity)]] | Unity Technologies; hay edición Unity 6 y edición previa | — | alta | a confirmar |
| 39 | [[39_Unity_Best_practice_guides_manual_oficial\|Unity — Best practice guides (manual oficial)]] | Unity Technologies, documentación viva | — | alta | a confirmar |
| 40 | [[40_Unreal_Engine_Gameplay_Framework\|Unreal Engine — Gameplay Framework]] | Epic Games, documentación viva | — | alta | a confirmar |
| 41 | [[41_Godot_Engine_documentacion_oficial\|Godot Engine — documentación oficial]] | Godot Engine community, documentación viva | — | media | explícita |
| 42 | [[42_Game_Programming_Patterns_Robert_Nystrom\|Game Programming Patterns — Robert Nystrom]] | Robert Nystrom | 2009 | alta | a confirmar |
| 43 | [[43_Plantilla_oficial_de_GDD_de_Unity\|Plantilla oficial de GDD de Unity]] | Unity Technologies, ~ | 2020 | baja | a confirmar |

### Postmortems técnicos y documentación abierta de desarrollo

Registros de proceso: bitácoras de desarrollo, wikis de patrones, ensayos de rol.

| # | Documento | Autor / estudio | Año | Prioridad | Licencia |
|---|---|---|---|---|---|
| 44 | [[44_Archivo_de_los_plan_files_de_John_Carmack\|Archivo de los .plan files de John Carmack]] | John Carmack — id Software, ~ | 1996 | alta | incierta |
| 45 | [[45_Archivo_de_postmortems_por_ano_dentro_de_awesome_gam\|Archivo de postmortems por año (dentro de awesome-game-design)]] | curación comunitaria; cubre | 1998 | alta | a confirmar |
| 46 | [[46_Game_Design_Patterns_Wiki_Chalmers_University\|Game Design Patterns Wiki (Chalmers University)]] | Staffan Björk y colaboradores — Chalmers University of Technology, en curso desde ~ | 2005 | media | incierta |
| 47 | [[47_The_Door_Problem_Liz_England\|The Door Problem — Liz England]] | Liz England | 2014 | alta | incierta |

### Hallazgos del relevamiento

Material que no estaba en el pedido y apareció buscando. Ficha mínima: verificar antes de apoyarse fuerte en ellos.

| # | Documento | Autor / estudio | Año | Prioridad | Licencia |
|---|---|---|---|---|---|
| 48 | [[48_ZACH_LIKE_los_cuadernos_de_diseno_de_Zachtronics\|ZACH-LIKE — los cuadernos de diseño de Zachtronics]] | — | — | alta | a confirmar |
| 49 | [[49_Disenos_de_UX_UI_de_Destiny_y_Halo\|Diseños de UX/UI de Destiny y Halo]] | — | — | alta | a confirmar |
| 50 | [[50_Pitch_y_fragmentos_de_codigo_de_Transport_Tycoon_Chr\|Pitch y fragmentos de código de Transport Tycoon (Chris Sawyer)]] | — | — | media | a confirmar |
| 51 | [[51_Documentos_de_Double_Fine_via_Lee_Petty_y_de_Ninja_T\|Documentos de Double Fine (vía Lee Petty) y de Ninja Theory]] | — | — | media | a confirmar |
| 52 | [[52_It_s_Behind_You_el_making_of_de_R_Type_para_ZX_Spect\|It's Behind You — el making of de R-Type para ZX Spectrum]] | — | — | baja | a confirmar |

---

## Regla del estante

- Numeración correlativa (01, 02, …). Un documento se **actualiza**, no se duplica.
- **Metadata obligatoria:** `familia`, `autor`, `anio`, `formato`, `acceso`, `licencia`, `prioridad`, `url`. La licencia es la clave: sin nivel declarado, el documento no se usa.
- Estados: Catalogado / Estudiado (alimentó libro X) / Inaccesible / Descartado.
- **Este estante no destila.** Un documento se convierte en criterio solo pasando por una misión de Escuela (Investigador → Destilador → Validador) que produzca un `EST`. Fichar no es aprender.
- **Consumidores primarios:** Producción (al escribir `TL`/`RQ`, para calibrar alcance y formato de documento) y Game Design (al escribir un `GDS`, para contrastar contra cómo lo resolvió alguien más).

---

## Cobertura pendiente

Del relevamiento quedaron pistas sin verificar por agotamiento del presupuesto de búsqueda. Se registran para no volver a buscarlas desde cero:

- **Half-Life / Half-Life 2 — Raising the Bar** (Valve, 2004): existe como libro comercial; falta confirmar si hay versión consultable en línea.
- **Rime GDD (Tequila Works):** no aparece ningún GDD publicado. **Probablemente la premisa sea falsa** — confirmar el origen del dato antes de volver a buscar.
- **System Shock — design doc de Looking Glass:** no relevado. Pista: el pitch de BioShock está alojado en systemshock.org, así que esa comunidad podría tener material propio.
- **Baldur's Gate, Dead Space, Doom 3, Braid, Sonic bible, Star Control:** no relevados.
- **E-books de Unity:** las landing pages no exponen contenido a fetch (formulario de por medio). Excepción: el PDF de ScriptableObjects está directo en el CDN de brandfolder — vale explorar si los demás también.

---

## Estado

Estante **abierto en la misión** [[EST-006_Mision_Lote_Biblioteca_Agosto26]]. 52 documentos catalogados, ninguno destilado todavía. Registrado en [[00_Catalogo_Biblioteca]] y declarado como cuarto estante en [[00_Biblioteca]].

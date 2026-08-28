## Estante de Documentación real

**Artefactos** de la industria: documentos de diseño que se usaron de verdad, código fuente liberado, documentación oficial de motor y registros de proceso.

No son libros destilados de Vaultrum (eso son `00_Indice_fundamentos` y `00_Indice_juegos`) ni bibliografía de estudio (eso es `00_Indice_fuentes`): son **evidencia primaria**.

Existe para una cosa concreta: que Producción y Game Design puedan mirar cómo lo resolvió alguien que ya lo hizo, en vez de discutirlo en abstracto.

La regla que gobierna el estante:

```txt
La Biblioteca no aloja ninguno de estos documentos.
Guarda la ficha, la referencia y la URL.
Se estudia y se cita. No se copia.
```

Este estante **no destila**. Un documento se vuelve criterio solo pasando por una misión de Escuela que produzca un `EST`. Fichar no es aprender.

---

## Consulta rapida

Qué abrir según qué se necesita. Los nombres apuntan a las fichas del Registro.

```txt
Ver como se escribe un GDD real, de punta a punta
→ Shooter: Majestic Revelations (Deus Ex), Doom Bible, GTA Race'n'Chase

Justificar un recorte de alcance con evidencia historica
→ Doom Bible (lo planeado vs lo que salio), Star Fox 2

Escribir un pitch corto y convincente
→ Diablo, BioShock, Guacamelee!

Fijar la vision de un proyecto en una pagina
→ Planescape: Torment, Wasteland 2

Disenar puzzles y documentarlos
→ Grim Fandango, ZACH-LIKE

Ver documentacion de un estudio de tamano realista, no AAA
→ Rogue Legacy, Double Fine / Ninja Theory, Narbacular Drop

Arrancar un GDD hoy con una plantilla usable
→ Plantilla oficial de GDD de Unity

Resolver arquitectura de codigo en Unity
→ Level up your code, ScriptableObjects, Game Programming Patterns

Leer codigo real de un juego terminado
→ DOOM, Celeste, Prince of Persia

Entender que hace cada rol en un equipo
→ The Door Problem

Ver UX/UI de produccion AAA
→ Destiny y Halo

Estudiar diseno bajo restriccion tecnica extrema
→ It's Behind You (R-Type), Quake
```

---

## La unidad didactica DOOM

Es el único caso del corpus donde están disponibles la intención documentada y la implementación real del mismo proyecto.

```txt
Doom Bible        → lo que se planeo y se descarto
DOOM source       → lo que efectivamente se construyo
                  ↓
        leer los dos y ver donde divergieron
```

Se consulta como **una sola unidad**, no como dos fichas sueltas. El segundo mejor ejemplar de esta clase es Prince of Persia: código original más el design bible del 2.

---

## Regla de licencia — tres niveles

Todo documento entra clasificado en un nivel, y el nivel manda sobre qué se puede hacer con él.

| Nivel | Qué es | Qué se puede hacer |
|-------|--------|--------------------|
| **A — explícita** | Liberado formalmente (GPL, MIT, CC, publicación oficial) | Estudiar, citar, adaptar según la licencia |
| **B — incierta** | El autor lo puso a disposición, sin liberación formal | Estudiar y citar. No copiar, no redistribuir, no alojar |
| **C — bloqueada** | Filtrado o decompilado de un producto comercial activo | Referenciar la existencia. No alojar, no distribuir, no usar como insumo |

El caso `35_CSE2_decompilacion_de_Cave_Story` es el precedente: al intentar acceder devolvió un HTTP 451, *Unavailable For Legal Reasons*. Queda fichado como precedente de política, no como material de consulta.

Ante la duda el nivel es C y se frena para consultar al owner, por la regla de la Escuela: si una fuente no tiene licencia clara, se resuelve con el owner antes de usarla.

---

## Registro — GDD y design bibles históricos

Los documentos que efectivamente se usaron para construir un juego. Responden "cómo se escribe esto de verdad" y, más útil todavía, "qué se descartó y por qué".

### [[01_Doom_Bible|Doom Bible]]

Design bible · Tom Hall — id Software, 1992 · licencia incierta · prioridad alta

### [[02_Shooter_Majestic_Revelations_design_doc_original_de|Shooter: Majestic Revelations (design doc original de Deus Ex)]]

GDD · Warren Spector y equipo — Ion Storm Austin, 1997 · licencia incierta · prioridad alta

### [[03_Grim_Fandango_Puzzle_Document|Grim Fandango — Puzzle Document]]

Design doc especializado (documento de puzzles) · Tim Schafer, Peter Tsacle, Eric Ingerson, Bret Mogilefsky, Peter Chan — LucasArts, abril, 1996 · licencia incierta · prioridad alta

### [[04_Diablo_pitch_original|Diablo — pitch original]]

Pitch · David Brevik — Condor, Inc., 1994 · licencia a confirmar · prioridad alta

### [[05_BioShock_pitch_document|BioShock — pitch document]]

Pitch · Ken Levine y equipo — Irrational Games, 2002 · licencia a confirmar · prioridad alta

### [[06_Planescape_Torment_Vision_Statement|Planescape: Torment — Vision Statement]]

Pitch / documento de visión · Chris Avellone — Black Isle Studios, 1997 · licencia incierta · prioridad alta

### [[07_Fallout_Bible|Fallout Bible]]

Design bible / biblia narrativa y de continuidad · Chris Avellone — Black Isle / Interplay, 2002 · licencia incierta · prioridad media

### [[08_Prince_of_Persia_2_Design_Bible|Prince of Persia 2 — Design Bible]]

Design bible · Jordan Mechner / Brøderbund, 08/08/, 1991 · licencia incierta · prioridad media

### [[09_Metal_Gear_Solid_2_Grand_Game_Plan|Metal Gear Solid 2 — Grand Game Plan]]

Pitch / plan maestro · Hideo Kojima — Konami, 2018 · licencia incierta · prioridad media

### [[10_Grand_Theft_Auto_Race_n_Chase_design_document|Grand Theft Auto — "Race'n'Chase" design document]]

GDD · DMA Design, 1995 · licencia incierta · prioridad alta

### [[11_Coleccion_de_documentos_de_Al_Lowe_Leisure_Suit_Larr|Colección de documentos de Al Lowe (Leisure Suit Larry y otros)]]

GDDs / design docs (varios) · Al Lowe — Sierra On-Line, 1991 · licencia incierta · prioridad media

### [[12_Marble_Madness_design_document|Marble Madness — design document]]

GDD · Mark Cerny — Atari Games, 1984 · licencia incierta · prioridad baja

### [[13_Wasteland_2_Vision_Document|Wasteland 2 — Vision Document]]

Documento de visión · inXile Entertainment, ~, 2012 · licencia incierta · prioridad media

### [[14_What_Remains_of_Edith_Finch_documentos_de_concepto_t|What Remains of Edith Finch — documentos de concepto tempranos]]

Docs de concepto · Giant Sparrow, ~, 2014 · licencia incierta · prioridad media

### [[15_Narbacular_Drop_documentos_el_predecesor_de_Portal|Narbacular Drop — documentos (el predecesor de Portal)]]

GDD / docs de proyecto estudiantil · Nuclear Monkey Software, 2005 · licencia incierta · prioridad alta

### [[16_Rogue_Legacy_Design_Notes|Rogue Legacy — Design Notes]]

Notas de diseño · Cellar Door Games, ~, 2013 · licencia incierta · prioridad alta

### [[17_Guacamelee_design_pitch|Guacamelee! — design pitch]]

Pitch · DrinkBox Studios, ~, 2012 · licencia incierta · prioridad media

### [[18_Sam_Max_Hit_the_Road_design_document|Sam & Max: Hit the Road — design document]]

GDD · LucasArts, 1993 · licencia incierta · prioridad baja

### [[19_Star_Fox_2_documentos_de_diseno_y_manual|Star Fox 2 — documentos de diseño y manual]]

GDD + manual · Nintendo / Argonaut, ~, 1995 · licencia incierta · prioridad baja


## Registro — Colecciones y repositorios

Agregadores. Cuando el documento puntual no está fichado acá, se busca primero en estos.

### [[20_Game_Documents_gamedocs_org|Game Documents (gamedocs.org)]]

Colección · curador independiente, activo desde ~, 2015 · licencia incierta · prioridad alta

### [[21_Video_Game_History_Foundation_Game_Design_Document_A|Video Game History Foundation — Game Design Document Archive]]

Colección / archivo institucional · Video Game History Foundation, colección en curso, — · licencia incierta · prioridad alta

### [[22_Computer_Game_Design_Documents_coleccion_Aric_Wilmun|Computer Game Design Documents — colección Aric Wilmunder (LucasArts)]]

Colección · Aric Wilmunder — LucasArts, documentos de ~, 1986 · licencia incierta · prioridad alta

### [[23_awesome_game_design_Roobyx|awesome-game-design (Roobyx)]]

Colección / awesome list · comunidad GitHub, mantenido, — · licencia explícita · prioridad alta

### [[24_Game_Design_Document_Resources_mikewesthad|Game-Design-Document-Resources (mikewesthad)]]

Colección · Mike Hadley, comunidad GitHub, — · licencia incierta · prioridad alta

### [[25_Propuesta_de_Super_Smash_Bros_for_Wii_U_3DS_traducid|Propuesta de Super Smash Bros. for Wii U / 3DS (traducida)]]

Pitch / propuesta de proyecto (slides) · Masahiro Sakurai — Sora Ltd. / Bandai Namco, ~, 2012 · licencia incierta · prioridad media

### [[26_Sloperama_Tom_Sloper_archivo_de_consejos_de_industri|Sloperama — Tom Sloper, archivo de consejos de industria]]

Colección / recurso de carrera y práctica profesional · Tom Sloper, desde ~, 1999 · licencia incierta · prioridad baja

### [[27_GitHub_topic_game_design_document|GitHub topic: game-design-document]]

Colección / índice vivo · GitHub, continuo, — · licencia explícita · prioridad media


## Registro — Código fuente liberado

La contraparte de los GDD: lo que efectivamente se construyó. Sirve para contrastar intención documentada contra implementación real.

### [[28_id_Software_organizacion_completa_en_GitHub_20_repos|id Software — organización completa en GitHub (20 repos)]]

Código fuente · id Software, liberaciones entre, 1997 · licencia explícita · prioridad alta

### [[29_Quake_GPL_source_release|Quake — GPL source release]]

Código fuente · John Carmack — id Software, código de, 1996 · licencia explícita · prioridad alta

### [[30_DOOM_source_release|DOOM — source release]]

Código fuente · id Software, código de, 1993 · licencia explícita · prioridad alta

### [[31_Prince_of_Persia_Apple_II_codigo_fuente_original|Prince of Persia (Apple II) — código fuente original]]

Código fuente + documentación técnica de época · Jordan Mechner — Brøderbund, código, 1985 · licencia a confirmar · prioridad alta

### [[32_Command_Conquer_Remastered_Collection_codigo_fuente|Command & Conquer Remastered Collection — código fuente (EA)]]

Código fuente · Westwood Studios / Electronic Arts, código de, 1995 · licencia explícita · prioridad media

### [[33_OpenDUNE_reimplementacion_de_Dune_II|OpenDUNE — reimplementación de Dune II]]

Código fuente (reimplementación) · proyecto comunitario OpenDUNE, sobre el original de Westwood de, 1992 · licencia explícita · prioridad media

### [[34_Celeste_codigo_fuente_del_juego_y_del_prototipo_PICO|Celeste — código fuente del juego y del prototipo PICO-8]]

Código fuente · Maddy Thorson y Noel Berry — Extremely OK Games, 2018 · licencia incierta · prioridad alta

### [[35_CSE2_decompilacion_de_Cave_Story|CSE2 — decompilación de Cave Story]]

Código fuente (decompilación) · Clownacy y colaboradores, decompilación de Cave Story v1.0.0.6, 2004 · licencia bloqueada · prioridad baja

### [[36_OpenRA_reimplementacion_moderna_de_RTS_clasicos|OpenRA — reimplementación moderna de RTS clásicos]]

Código fuente · proyecto comunitario OpenRA, activo desde, 2007 · licencia explícita · prioridad media


## Registro — Documentación oficial de motor

Material publicado por Unity, Unreal y Godot. Licencia limpia y aplicable directo a un proyecto en curso.

### [[37_Level_up_your_code_with_game_programming_patterns_Un|Level up your code with game programming patterns (Unity)]]

Doc técnica oficial / e-book · Unity Technologies, con aportes de Wilmer Lin; edición ampliada reciente, — · licencia a confirmar · prioridad alta

### [[38_Create_modular_game_architecture_with_ScriptableObje|Create modular game architecture with ScriptableObjects (Unity)]]

Doc técnica oficial / e-book · Unity Technologies; hay edición Unity 6 y edición previa, — · licencia a confirmar · prioridad alta

### [[39_Unity_Best_practice_guides_manual_oficial|Unity — Best practice guides (manual oficial)]]

Doc técnica oficial · Unity Technologies, documentación viva, — · licencia a confirmar · prioridad alta

### [[40_Unreal_Engine_Gameplay_Framework|Unreal Engine — Gameplay Framework]]

Doc técnica oficial · Epic Games, documentación viva, — · licencia a confirmar · prioridad alta

### [[41_Godot_Engine_documentacion_oficial|Godot Engine — documentación oficial]]

Doc técnica oficial · Godot Engine community, documentación viva, — · licencia explícita · prioridad media

### [[42_Game_Programming_Patterns_Robert_Nystrom|Game Programming Patterns — Robert Nystrom]]

Libro técnico / doc de referencia · Robert Nystrom, 2009 · licencia a confirmar · prioridad alta

### [[43_Plantilla_oficial_de_GDD_de_Unity|Plantilla oficial de GDD de Unity]]

Plantilla / doc oficial · Unity Technologies, ~, 2020 · licencia a confirmar · prioridad baja

### [[65_Fix_Your_Timestep|Fix Your Timestep! — Glenn Fiedler]]

Artículo técnico de referencia · Glenn Fiedler, 2004 rev. 2018 · licencia nivel B · prioridad alta · **Estudiado** — destilado en `01_Bucle_de_simulacion`

### [[56_Valve_Developer_Community_Level_Design|Valve Developer Community — Level design]]

Wiki oficial de desarrollo · Valve Corporation y comunidad, desde 2005 · licencia nivel B · prioridad media


## Registro — Postmortems técnicos y registros de proceso

Bitácoras de desarrollo, wikis de patrones y ensayos de rol.

### [[44_Archivo_de_los_plan_files_de_John_Carmack|Archivo de los .plan files de John Carmack]]

Doc técnica / bitácora de desarrollo · John Carmack — id Software, ~, 1996 · licencia incierta · prioridad alta

### [[45_Archivo_de_postmortems_por_ano_dentro_de_awesome_gam|Archivo de postmortems por año (dentro de awesome-game-design)]]

Colección de postmortems · curación comunitaria; cubre, 1998 · licencia a confirmar · prioridad alta

### [[46_Game_Design_Patterns_Wiki_Chalmers_University|Game Design Patterns Wiki (Chalmers University)]]

Colección académica / wiki de patrones · Staffan Björk y colaboradores — Chalmers University of Technology, en curso desde ~, 2005 · licencia incierta · prioridad media

### [[47_The_Door_Problem_Liz_England|The Door Problem — Liz England]]

Ensayo / doc de práctica profesional · Liz England, 2014 · licencia incierta · prioridad alta

### [[54_Iwata_Asks|Iwata Asks]]

Archivo oficial de entrevistas de desarrollo · Nintendo, 2006-2015 · licencia nivel A · prioridad alta

### [[55_Making_of_Prince_of_Persia|The Making of Prince of Persia — Journals 1985-1993]]

Diario de desarrollo publicado · Jordan Mechner, 2011/2020 · licencia nivel A · prioridad alta

### [[57_GDC_Level_Design_Workshop|GDC Level Design Workshop]]

Serie anual de charlas con slides · GDC, desde 2016 · licencia nivel B · prioridad alta

### [[59_The_Art_of_Screenshake|The Art of Screenshake]]

Charla con demo en vivo · Jan Willem Nijman (Vlambeer), 2013 · licencia nivel B · prioridad alta

### [[60_Juice_It_or_Lose_It|Juice it or lose it]]

Charla con demo en vivo · Martin Jonasson & Petri Purho, 2012 · licencia nivel B · prioridad alta

### [[61_Juicing_Your_Cameras_With_Math|Math for Game Programmers: Juicing Your Cameras With Math]]

Charla técnica con slides en PDF · Squirrel Eiserloh, 2016 · licencia nivel B · prioridad alta

### [[62_Playing_to_Win|Playing to Win]]

Libro completo publicado por su autor · David Sirlin, 2000-2006 · licencia nivel A · prioridad media


## Registro — Hallazgos del relevamiento

Material que no estaba en el pedido y apareció buscando. Ficha mínima: verificar antes de apoyarse fuerte en ellos.

### [[48_ZACH_LIKE_los_cuadernos_de_diseno_de_Zachtronics|ZACH-LIKE — los cuadernos de diseño de Zachtronics]]

Hallazgo — ficha mínima · —, — · licencia a confirmar · prioridad alta

### [[49_Disenos_de_UX_UI_de_Destiny_y_Halo|Diseños de UX/UI de Destiny y Halo]]

Hallazgo — ficha mínima · —, — · licencia a confirmar · prioridad alta

### [[50_Pitch_y_fragmentos_de_codigo_de_Transport_Tycoon_Chr|Pitch y fragmentos de código de Transport Tycoon (Chris Sawyer)]]

Hallazgo — ficha mínima · —, — · licencia a confirmar · prioridad media

### [[51_Documentos_de_Double_Fine_via_Lee_Petty_y_de_Ninja_T|Documentos de Double Fine (vía Lee Petty) y de Ninja Theory]]

Hallazgo — ficha mínima · —, — · licencia a confirmar · prioridad media

### [[52_It_s_Behind_You_el_making_of_de_R_Type_para_ZX_Spect|It's Behind You — el making of de R-Type para ZX Spectrum]]

Hallazgo — ficha mínima · —, — · licencia a confirmar · prioridad baja


## Registro — Referencia y especificación reconstruida

Material que **no registra un desarrollo**: cataloga o reconstruye. Un catálogo de pantallas reales, una física deducida por ingeniería inversa, una estructura de nivel reducida a grafo, un género definido por factores. Se consultan por su **método y su forma**, no por su historia.

### [[53_Game_UI_Database|Game UI Database]]

Base de datos de referencia visual · Edd Coates, desde 2020 · licencia nivel B · prioridad alta

### [[58_Sonic_Physics_Guide|Sonic Physics Guide]]

Especificación reconstruida por ingeniería inversa · comunidad de Sonic Retro, desde 2005 · **licencia nivel C — se referencia, no se usa de insumo** · prioridad media

### [[63_Boss_Keys|Boss Keys]]

Análisis de estructura con notación de grafo · Mark Brown (GMTK), 2016-2020 · licencia nivel B · prioridad alta

### [[64_Berlin_Interpretation|The Berlin Interpretation]]

Definición de género por factores · International Roguelike Development Conference, 2008 · licencia nivel B · prioridad media


---

## Regla del estante

- Numeración correlativa (01, 02, ...). Un documento se **actualiza**, no se duplica.
- Metadata obligatoria: `familia`, `autor`, `anio`, `formato`, `acceso`, `licencia`, `prioridad`, `url`. **Sin nivel de licencia declarado, el documento no se usa.**
- Estados: Catalogado / Estudiado (alimentó libro X) / Inaccesible / Descartado.
- Consumidor primario: **Producción**, al escribir un `TL` o un `RQ`, para calibrar alcance y formato de documento. Secundario: **Game Design**, al escribir un `GDS`.
- Una ficha nunca linkea a otra ficha. La navegación es por este índice.

---

## Cobertura pendiente

Pistas que quedaron sin verificar por agotamiento del presupuesto de búsqueda. Se registran para no volver a buscarlas desde cero.

```txt
Half-Life / Half-Life 2 (Raising the Bar)
→ existe como libro comercial; falta confirmar si hay version consultable en linea

Rime GDD (Tequila Works)
→ no aparece ningun GDD publicado; probablemente la premisa sea falsa

System Shock (design doc de Looking Glass)
→ no relevado; el pitch de BioShock esta en systemshock.org, esa comunidad podria tener material propio

Baldur's Gate, Dead Space, Doom 3, Braid, Sonic bible, Star Control
→ no relevados

E-books de Unity
→ las landing pages no exponen contenido; el PDF de ScriptableObjects si esta directo en el CDN
```

---

## Estado

Estante abierto en la misión `EST-006_Mision_Lote_Biblioteca_Agosto26` con 52 documentos. La misión `EST-009_Mision_Fuentes_Huerfanas` sumó doce más (53-64) y abrió la sección **Referencia y especificación reconstruida**, una familia que el estante no tenía: material que cataloga o reconstruye en vez de registrar.

Tres de esos doce entraron juntos y por un motivo declarado: `59`, `60` y `61` son el material que le faltaba a `02_Game_feel`, el libro de Fundamentos que sigue *Reservado*. Con ellos, escribirlo deja de estar bloqueado por falta de material y pasa a ser una decisión del owner.

64 documentos catalogados, ninguno destilado. Declarado como cuarto estante en `00_Biblioteca`. El conteo y el estado del estante se calculan con `Herramientas/biblioteca.py`.

# Vaultrum

**Vaultrum** es un sistema de desarrollo asistido por IA con **trazabilidad obligatoria**: convierte una intención en un entregable pasando por una cadena de pasos donde ninguno avanza sin su insumo anterior, y donde cada paso deja un documento escrito en disco.

Está orientado al desarrollo de videojuegos, software y sistemas creativos, y se abre como vault de **Obsidian**.

**Versión 1.0** — la primera pensada para que la use alguien que no es su autor.

---

## Qué problema resuelve

Trabajar con una IA sin estructura produce dos fallas al mismo tiempo:

```txt
entrega lo mínimo funcional      → falta el menú, el fin de partida, la forma de volver a jugar
y sobre-construye lo que nadie pidió → optimización, arquitectura y maquinaria sin requerimiento
```

Y produce una tercera, más silenciosa: **al terminar la conversación no queda nada.** Ni por qué se decidió lo que se decidió, ni qué se descartó, ni qué quedó pendiente.

Vaultrum ataca las tres con una regla y una cadena.

La regla:

> **Completo en experiencia, mínimo en maquinaria.**

La cadena:

```txt
Intención
  → TL + RQ      (Producción)      qué se hace, con qué alcance
  → GDS          (Game Design)     reglas, estados, feedback, balance
  → LDS / UXS / ART / MET   (Level Design / UI-UX / Arte / Métricas, si aplican)
  → SOL + EJ     (Programación)    solución técnica + implementación
  → QA           (Control de Calidad)  ¿se sostiene? GO / CONDITIONAL GO / NO-GO
  → VE           (Producción)      ¿lo entregado es lo prometido?
  → revisión de fase (Producción)  ¿la fase respondió su pregunta? avanzar · seguir · volver · cortar
  → commit al Core (Conocimiento)  ¿qué aprendizaje vuelve al sistema?
```

Las siglas, en una línea cada una:

```txt
TL   timeline: la entrega, con su alcance          GDS  game design spec: reglas y balance
RQ   requerimiento: un hilo de la entrega          LDS  level design spec: espacio y pacing
SOL  solución técnica: cómo se implementa          UXS  UI/UX spec: pantallas y legibilidad
EJ   ejecución: qué se implementó                  ART  arte: assets medidos por instrumento
QA   control de calidad: ¿se sostiene?             MET  métricas: ¿el jugador hizo lo esperado?
VE   validación de entrega: ¿es lo prometido?
```

**Productor** es como se presenta el asistente al arrancar: la puerta de entrada, que pivotea entre las diez áreas. Las **table-stakes** son lo que un entregable trae sin que se lo pidan (en un juego: menú, pausa, fin de partida, volver a jugar). El **gate de cierre** es el conjunto de mediciones que corre antes de cada commit.

Cada artefacto está numerado, linkea hacia atrás a su insumo, y **no existe si su insumo no existe**. Eso es lo que impide que la IA se saltee pasos y que una entrega se dé por terminada porque compila. Y antes de abrir cada timeline, nueve **señales de parada** —fase sin declarar, deuda arrastrada entre entregas, dos entregas sin que el juego arranque, código sin diseño, entre otras— impiden apilar trabajo nuevo sobre deuda que nadie mira.

---

## Antes de empezar: el entorno que necesitás

**Vaultrum no es una aplicación.** Es un vault —notas, skills e instrumentos— que opera un asistente de IA. Sin el asistente, se lee como documentación. Con el asistente, te atiende: el primer mensaje abre el Productor, y desde ahí la cadena corre sola.

Por eso, antes de clonar, tené armado esto:

| | Qué | Para qué |
|---|-----|----------|
| **Obligatorio** | un asistente que lea `CLAUDE.md` o `AGENTS.md` y use skills: **Claude Code** (en la terminal, o la app de escritorio de Claude abriendo la carpeta) o **Codex** | es quien opera el sistema. Necesitás tu propia cuenta |
| **Obligatorio** | **Python 3.10 o superior** | los instrumentos son scripts y su salida *es* la evidencia. En Windows, instalalo desde python.org y marcá *Add python.exe to PATH* |
| **Obligatorio** | **Git** | para clonar, y para que el gate de cierre mida tus commits |
| Recomendado | **Obsidian** | para navegar el vault y ver el grafo |
| Según tu proyecto | el motor (Unity, Godot, web…) | Vaultrum no lo trae ni lo elige por vos: te pregunta cuál usás |
| Según tu proyecto | Blender con su MCP | solo si vas a usar el Área de Arte |
| Opcional | Codex en el PATH y la bandeja de órdenes | solo si querés despachar ejecución a Codex (`04_IA Operativa`) |

---

## Empezar en cinco pasos

1. **Clonar.**
   ```bash
   git clone https://github.com/ISantucci/Vaultrum.git
   ```
2. **Correr el instalador** desde la raíz: `skills.bat` en Windows, `sh skills.sh` en macOS o Linux. Copia las skills donde el asistente las busca, instala el gate de cierre y verifica el entorno. Termina con un **veredicto**: `LISTO PARA TRABAJAR`, o la lista de lo obligatorio que falta. Lo que aparece como *opcional* no te frena.
3. **Abrir la carpeta con tu asistente**: `claude` parado en la carpeta, la app de escritorio de Claude con la carpeta abierta, o `codex`.
4. **Escribir cualquier cosa** —un "hola" alcanza—. Te contesta el **Productor** con una sola pregunta: *¿proyecto de cero o uno ya empezado?*
5. **Responder el seteo.** Al cerrarlo, Producción crea `06_Proyectos/<TuProyecto>/` con su cuaderno, y desde ahí cada artefacto aterriza en esa carpeta.

**Dónde vive el código.** En `06_Proyectos/<TuProyecto>/` viven los documentos de la cadena. El proyecto del motor —la carpeta de Unity, de Godot, el repo web— vive donde quieras, fuera del vault: el Productor te pregunta la ruta y la anota en el cuaderno. Tu asistente tiene que poder abrir las dos carpetas.

Para **retomar** otro día: abrí la carpeta y saludá. El Productor encuentra el cuaderno y te dice dónde quedaste y qué sigue.

Para **actualizar** Vaultrum: `git pull` y volvé a correr el instalador.

---

## Tus proyectos son tuyos

`06_Proyectos/` **no se versiona**: está en el `.gitignore`, y lo que hacés ahí no viaja aunque hagas push.

Pero un archivo ignorado no alcanza, porque lo que pasa dentro de un proyecto también se puede filtrar *contado* en las notas del sistema. Por eso el gate de cierre trae **`privacidad.py`**: lee los nombres de tus proyectos desde tu disco y frena cualquier commit que los nombre fuera de `06_Proyectos/`. Lo que el sistema aprende de tu proyecto puede volver al Core como lección, sin el nombre del proyecto.

`06_Proyectos/privado.txt` sirve para dos cosas, y también vive en tu carpeta y tampoco viaja:

```txt
NombreComercial                                   un término privado más (una línea, sin |):
                                                  el nombre de venta de un juego, un cliente
05_Escuela/Biblioteca/.../nota.md | Rayo | razón  un falso positivo: una palabra común que
                                                  coincide con tu proyecto, en ESA nota
```

Un consejo: no le pongas a tu proyecto el nombre de un género que la Biblioteca ya trata (*Pong*, *Dino*, *Runner*). Aparece en decenas de notas, y cada una sería un falso positivo que declarar.

---

## Si lo usás, nombralo

Vaultrum es libre y lo va a seguir siendo. Lo único que te pedimos a cambio es el crédito:

```txt
Hecho con Vaultrum — github.com/ISantucci/Vaultrum
```

En los créditos o en el "Acerca de" de lo que hagas, y en el README de tu proyecto con este badge:

[![Hecho con Vaultrum](https://img.shields.io/badge/hecho%20con-Vaultrum-5A3E8C)](https://github.com/ISantucci/Vaultrum)

```markdown
[![Hecho con Vaultrum](https://img.shields.io/badge/hecho%20con-Vaultrum-5A3E8C)](https://github.com/ISantucci/Vaultrum)
```

No es una obligación legal: la licencia cubre a Vaultrum, no lo que hacés con él. El Productor te lo pregunta una sola vez, cuando un proyecto se va a mostrar o publicar, y si decís que no, no insiste. Los detalles están en `03_Comunidad/Gestion/Trademark.md`, y para citarlo en un trabajo está `CITATION.cff` (GitHub lo muestra como *Cite this repository*).

---

## Qué hay adentro

**Este README describe lo que recibís al clonar.** El sistema viaja; los proyectos y el historial de uso de quien lo trabaja, no.

| Capa | Qué es |
|------|--------|
| **01_VaultrumCore** | la base de conocimiento: SOLID, patrones, optimización, estructuras, algoritmos, managers, IA para juegos, calidad y testing, métricas de producto, y los criterios de entrega |
| **02_Agencia** | las diez áreas que ejecutan y sostienen la cadena, cada una con sus agentes, flujos, salidas y su skill ejecutable |
| **03_Comunidad** | gobernanza, contribución, licencia y marca, y la preparación de lo que el sistema publica |
| **04_IA Operativa** | cómo una IA opera el vault sin inflarlo: tokens, prompteo, el pass GC y sus herramientas de medición |
| **05_Escuela** | aprendizaje proactivo y la Biblioteca: fundamentos de experiencia y análisis de juegos por género |
| `06_Proyectos` | **no viaja.** Es tu workspace: lo crea Producción al cerrar el seteo de tu primer proyecto |

Catorce **skills ejecutables** —una por cada una de las diez áreas, más la Escuela, la Comunidad, AiCare y el Despacho— son lo que hace que la cadena corra en vez de quedarse en documentación.

**Seis se registran y ocho se alcanzan.** Un asistente carga por adelantado el nombre y la descripción de cada skill registrada —la use o no— y ese presupuesto tiene tope. Vaultrum registra las áreas por donde el trabajo entra en frío (Producción, Arquitectura, Escuela, Comunidad, AiCare, Despacho) y deja las ocho de la cadena —Game Design, Level Design, UI/UX, Arte, Métricas, Programación, Calidad y Conocimiento— viviendo en su área, alcanzables por ruta desde el índice de la puerta. Existen igual y se usan igual: **descubrir cuesta presupuesto, alcanzar no cuesta nada**. El instalador verifica que ninguna quede sin camino.

Los instrumentos son 32 scripts versionados. El **gate de cierre** que corre antes de cada commit son seis mediciones hechas con cinco de ellos —`privacidad.py` corre siempre; las otras cinco, cuando el commit toca notas—: `grafo.py` y `grafo.py --paquete` (la forma del vault, en tu disco y en lo que se clona), `gemelos.py` (las copias que deben ser idénticas), `documentacion.py` (la forma del texto), `requerimientos.py` (lo entregado está archivado y lo pendiente, a la vista) y `privacidad.py` (el paquete no nombra tus proyectos).

---

## Lo que hace el instalador

```txt
sincroniza   las skills RESIDENTES a .claude/skills/ y .agents/skills/, que son
             las rutas que Claude Code y Codex escanean solos en el repo. Las
             referenciadas se quedan en su area: se abren por ruta, no se copian
mide         el presupuesto residente (name + description, contra el tope de
             8000 de Codex) y el ALCANCE: que ninguna referenciada quede sin
             camino en el indice de la puerta
instala      el gate de cierre en .git/hooks/pre-commit
prepara      la bandeja de ordenes de la capa IA Operativa
verifica     que el entorno pueda trabajar, y separa lo OBLIGATORIO (las puertas,
             el gate, las skills) de lo OPCIONAL (Codex, la bandeja)
```

`CLAUDE.md` y `AGENTS.md` en la raíz son la puerta: declaran el Modo Vaultrum y mandan al Productor. Por eso el primer mensaje —sea cual sea— abre el seteo del proyecto.

El repo trae además `.claude/settings.json` con un hook de Claude Code: en cada lectura o escritura del asistente corre `vaultrum_trace.py`, que anota en `.vaultrum/` qué hizo la sesión. Es local, no viaja y no manda nada a ningún lado; sirve para medir la fricción de una entrega.

---

## Modificar el sistema en tu copia (Modo Owner)

El asistente arranca en **Modo Vaultrum**: usa el sistema para tu proyecto, pero no toca sus skills, flujos ni índices. Para modificar el sistema —adaptarlo, o preparar una mejora para proponer— hace falta el **Modo Owner**, que se habilita pedido por pedido con una passphrase.

La que viaja en el repo (`04_IA Operativa/owner.json`) es la del maintainer. Creá la tuya una vez:

```bash
python "04_IA Operativa/Herramientas/owner.py"
```

Te pide una frase de tres palabras o más y escribe `owner.local.json`, que no se versiona. Desde ahí, en tu copia, el asistente verifica contra tu frase. El procedimiento completo está en `04_IA Operativa/05_Modo_Operacion.md`.

---

## Leerlo sin instalar nada

Si solo querés estudiar el criterio, revisar patrones o usar la Biblioteca, no hace falta nada más que Obsidian:

1. Obsidian → **Open folder as vault** → la carpeta de Vaultrum.
2. Abrí [00_START_HERE](00_START_HERE.md).

---

## Problemas comunes

**"No encontré Python" o el gate dice "no encuentro Python 3".** En Windows, instalá Python desde python.org con *Add python.exe to PATH*. Si igual falla, desactivá los alias de la Microsoft Store: *Configuración → Aplicaciones → Configuración avanzada de aplicaciones → Alias de ejecución de aplicaciones*, y apagá `python.exe` y `python3.exe`.

**El asistente no usa las skills.** Corré el instalador otra vez y abrí una sesión **nueva**: las skills se descubren al arrancar.

**Un commit frenado por el gate.** El mensaje dice qué medición falló y cómo ver su informe completo. Si fue `privacidad.py`, una nota del sistema nombra uno de tus proyectos: reescribila sin el nombre, o, si es una palabra común que coincide, declarala en `06_Proyectos/privado.txt` con la forma `ruta | término | razón`.

**El asistente me pide una passphrase.** Es el Modo Owner: ver *Modificar el sistema en tu copia*, más abajo.

**Bajé el .zip en vez de clonar.** Funciona, pero sin git no hay gate de cierre. El instalador te lo avisa como opcional.

**El veredicto dice "opcional" sobre Codex o la bandeja.** Si no usás Codex, ignoralo.

---

## Estado actual

**Versión 1.0.** Tres proyectos reales, de tres géneros distintos, corrieron la cadena de punta a punta, con seis validaciones de entrega cerradas.

Lo que eso probó: la cadena produce un entregable que se juega, con trazabilidad completa; las table-stakes entran como requerimiento explícito y no como intuición; y lo aprendido vuelve al Core. Resumen honesto: **la cadena funciona en el medio y falla en los bordes**, y las tres reglas de borde que lo corrigen ya son pasos ejecutables de las skills.

Lo que falta es **salir del dominio**: tres muestras, tres videojuegos. Sigue sin probarse que la cadena sirva fuera de los juegos. Y falta lo que esta versión viene a buscar: **gente que no es el autor usándolo.**

---

## Proponer mejoras

Las propuestas son bienvenidas: abrí un *issue* con el problema, dónde vive y qué proponés, o directamente un *pull request* (`git commit -s`). Para preparar el cambio con el asistente, creá antes tu passphrase (Modo Owner, arriba). El gate de cierre va a medir tu cambio igual que mide los del autor.

Cómo contribuir y qué implica: `03_Comunidad/Contribuciones/CONTRIBUTING.md` (GitHub lo encuentra por `.github/CONTRIBUTING.md`, que solo lo señala).

---

## Licencia

Copyright (C) 2026 Ignacio Santucci.

Vaultrum es software libre: podés redistribuirlo y modificarlo bajo los términos de la **GNU General Public License** publicada por la Free Software Foundation, versión 3 o (a tu elección) cualquier versión posterior (`GPL-3.0-or-later`). Se distribuye con la esperanza de que sea útil, pero **SIN NINGUNA GARANTÍA** — ni siquiera la garantía implícita de comerciabilidad o adecuación a un propósito particular. El texto oficial está en el archivo `LICENSE` de la raíz.

La marca es otra cosa que la licencia: la GPL licencia el código, no el nombre. El nombre y la identidad **Vaultrum** tienen su propia política en `03_Comunidad/Gestion/Trademark.md`.

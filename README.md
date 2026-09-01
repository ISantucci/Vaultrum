# Vaultrum

**Vaultrum** es un sistema de desarrollo asistido por IA con **trazabilidad obligatoria**: convierte una intención en un entregable pasando por una cadena de pasos donde ninguno avanza sin su insumo anterior, y donde cada paso deja un documento escrito en disco.

Está orientado al desarrollo de videojuegos, software y sistemas creativos, y se abre como vault de **Obsidian**.

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
  → LDS / UXS    (Level Design / UI-UX, si aplican)
  → SOL + EJ     (Programación)    solución técnica + implementación
  → QA           (Control de Calidad)  ¿se sostiene? GO / CONDITIONAL GO / NO-GO
  → VE           (Producción)      ¿lo entregado es lo prometido?
  → commit al Core (Conocimiento)  ¿qué aprendizaje vuelve al sistema?
```

Cada artefacto está numerado, linkea hacia atrás a su insumo, y **no existe si su insumo no existe**. Eso es lo que impide que la IA se saltee pasos y que una entrega se dé por terminada porque compila.

---

## Qué hay adentro

Cinco capas:

| Capa | Qué es |
|------|--------|
| **01_VaultrumCore** | la base de conocimiento: SOLID, patrones, optimización, estructuras, algoritmos, managers, IA para juegos, y los criterios de entrega |
| **02_Agencia** | las ocho áreas que ejecutan y sostienen la cadena, cada una con sus agentes, flujos, salidas y su skill ejecutable |
| **03_Comunidad** | gobernanza, contribución, licencia y marca — y la preparación de lo que el sistema publica, con su Archivo |
| **04_IA Operativa** | cómo una IA opera el vault sin inflarlo: tokens, prompteo, el pass GC y sus herramientas de medición |
| **05_Escuela** | aprendizaje proactivo y la Biblioteca: fundamentos de experiencia y análisis de juegos por género |

Once **skills ejecutables** (una por área, más la Escuela, la Comunidad y AiCare) son lo que hace que la cadena corra en vez de quedarse en documentación.

---

## Entorno recomendado

- **Obsidian**, para abrir y navegar el vault (la navegación usa wikilinks en cascada).
- **Git**, para clonar o versionar.
- Cualquier herramienta de IA capaz de leer archivos Markdown y usar el vault como contexto. Las skills están escritas en el formato de skills de Claude, y su contenido es portable a cualquier agente que lea instrucciones en Markdown.
- **Python 3** (opcional), solo para las herramientas de medición de `04_IA Operativa`.

---

## Cómo abrir Vaultrum

Hay dos formas de tener Vaultrum, y son distintas.

### Leerlo — como vault de Obsidian

1. Clonar o descargar este repositorio.
2. Abrir Obsidian → **Open folder as vault** → la carpeta raíz de Vaultrum.
3. Abrir [[00_START_HERE]].

Sirve para estudiar el criterio, revisar patrones y usar la Biblioteca. No hace falta nada más.

### Instalarlo — para que te atienda

1. Clonar el repositorio.
2. Correr **`skills.bat`** (Windows) o **`skills.sh`** (macOS/Linux) desde la raíz. No es solo copiar skills: deja el entorno de trabajo armado y **te dice si quedó armado o no**.
3. Abrir una sesión de IA con esa carpeta como contexto.

Lo que el instalador deja listo, y lo que verifica:

```txt
sincroniza   las skills a .claude/skills/ y .agents/skills/, que son las rutas
             que Claude Code y Codex escanean solos en el repo
instala      el gate de cierre en .git/hooks/pre-commit
prepara      la bandeja de ordenes de la capa IA Operativa
verifica     que cada harness pueda usarse de verdad: el binario en el PATH, su
             puerta (CLAUDE.md / AGENTS.md), su config, y que la bandeja sepa
             contra que proyecto despachar
```

Termina con un **veredicto**: entorno listo, o la lista de lo que falta. Nada de lo que falte rompe el vault —son datos de cada máquina— pero el instalador no dice "Listo" sobre un entorno que no puede trabajar.

`CLAUDE.md` y `AGENTS.md` en la raíz son la puerta: declaran el Modo Vaultrum y mandan al Productor. Con eso, el primer mensaje —sea cual sea— abre el seteo del proyecto.

---

## Cómo se usa

**Uso libre.** Entrar al Core, leer, tomar criterio y aplicarlo en un proyecto propio. No hace falta pasar por ningún flujo.

**Uso asistido.** Dar el vault como contexto a una IA y arrancar por Producción. La IA se convierte en el Productor, releva lo mínimo, produce el timeline y los requerimientos, y pivotea entre áreas hasta la entrega validada.

Los dos son válidos. El segundo es el que deja rastro.

---

## Estado actual

Etapa de apertura inicial, con dos entregas reales completas: un Pong 3D en Unity 6 y un plataformero 2D de precisión en web, las dos con la cadena corrida de punta a punta y su validación cerrada. Con la segunda corrieron por primera vez las dos áreas que faltaban, Level Design y Control de Calidad.

Lo que eso probó y lo que no está escrito sin maquillaje en `ARQ-000_Auditoria_de_arquitectura` y en el backlog de `00_Leyes_en_antesala`. Resumen honesto: **la cadena funciona en el medio y falla en los bordes**, y las tres reglas de borde que lo corrigen ya son pasos ejecutables de las skills.

Lo que falta ya no es la segunda muestra: es **salir del dominio.** Dos entregas, dos videojuegos. Y la segunda está probada como sistema y sin probar como experiencia — el owner todavía no la jugó, y eso está declarado como deuda en su `VE`, no tapado.

---

## Licencia

GPL-3.0. El texto oficial está en el archivo `LICENSE` de la raíz.

El nombre y la identidad **Vaultrum** tienen su propia política: ver `03_Comunidad/Gestion/Trademark.md`.

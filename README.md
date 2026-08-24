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
| **02_Agencia** | las seis áreas que ejecutan la cadena, cada una con sus agentes, flujos, salidas y su skill ejecutable |
| **03_Comunidad** | gobernanza, contribución, licencia y marca |
| **04_IA Operativa** | cómo una IA opera el vault sin inflarlo: tokens, prompteo, el pass GC y sus herramientas de medición |
| **05_Escuela** | aprendizaje proactivo y la Biblioteca: fundamentos de experiencia y análisis de juegos por género |

Ocho **skills ejecutables** (una por área, más la Escuela y AiCare) son lo que hace que la cadena corra en vez de quedarse en documentación.

---

## Entorno recomendado

- **Obsidian**, para abrir y navegar el vault (la navegación usa wikilinks `[[...]]`).
- **Git**, para clonar o versionar.
- Cualquier herramienta de IA capaz de leer archivos Markdown y usar el vault como contexto. Las skills están escritas en el formato de skills de Claude, y su contenido es portable a cualquier agente que lea instrucciones en Markdown.
- **Python 3** (opcional), solo para las herramientas de medición de `04_IA Operativa`.

---

## Cómo abrir Vaultrum

1. Clonar o descargar este repositorio.
2. Abrir Obsidian → **Open folder as vault** → la carpeta raíz de Vaultrum.
3. Abrir [[00_START_HERE]].

El repositorio se puede leer desde GitHub, pero la experiencia está pensada para Obsidian.

---

## Cómo se usa

**Uso libre.** Entrar al Core, leer, tomar criterio y aplicarlo en un proyecto propio. No hace falta pasar por ningún flujo.

**Uso asistido.** Dar el vault como contexto a una IA y arrancar por Producción. La IA se convierte en el Productor, releva lo mínimo, produce el timeline y los requerimientos, y pivotea entre áreas hasta la entrega validada.

Los dos son válidos. El segundo es el que deja rastro.

---

## Estado actual

Etapa de apertura inicial, con una entrega real completa: la cadena se corrió de punta a punta produciendo un Pong 3D en Unity 6, jugable y jugado.

Lo que eso probó y lo que no está escrito sin maquillaje en [[00_Auditoria de arquitectura]] y en el backlog de [[00_Leyes de Vaultrum (bitacora)]]. Resumen honesto: **la cadena funciona en el medio y falla en los bordes**, y las tres reglas de borde que lo corrigen ya son pasos ejecutables de las skills.

Falta la segunda muestra. Todo lo validado se validó sobre un mismo género.

---

## Licencia

GPL-3.0. El texto oficial está en el archivo `LICENSE` de la raíz.

El nombre y la identidad **Vaultrum** tienen su propia política: ver `03_Comunidad/Gestion/Trademark.md`.

## Qué es VaultrumCore

**VaultrumCore** es la base de conocimiento de Vaultrum.

Contiene principios, criterios, conceptos, estructuras, patrones, algoritmos, aprendizajes y material reutilizable orientado al desarrollo de videojuegos, software y sistemas creativos.

Su función es ordenar conocimiento útil para que pueda ser consultado, aplicado y reutilizado por personas y por la Agencia.

---

## [[01_Identidad y principios de Vaultrum]]

Sección dedicada a la identidad y los principios centrales de Vaultrum.

Define el criterio base del sistema:

- qué tipo de herramienta es Vaultrum;
- qué conocimiento busca preservar;
- desde dónde trabaja;
- qué principios guían su crecimiento;
- qué forma de trabajo intenta sostener;
- qué relación existe entre conocimiento, criterio y acción.

Esta sección funciona como base conceptual del Core.  

---

## [[02_Contenido VaultrumCore]]

Carpeta principal de conocimiento técnico y práctico de VaultrumCore.

Contiene material sobre:

- SOLID;
- patrones de diseño;
- optimización;
- criterios de entrega;
- calidad y testing;
- experiencia de juego (índice hacia la Biblioteca);
- estructuras de datos;
- algoritmos;
- managers;
- arquitectura;
- buenas prácticas.

Esta sección sirve para estudiar conceptos, consultar criterios y aplicar conocimiento en proyectos reales.

---

## [[03_VaultrumAi]]

Carpeta dedicada al uso de inteligencia artificial dentro de Vaultrum.

Contiene material relacionado con:

- IA para desarrollo de mapas;
- IA para NPC;
- asistencia con flujos de trabajo;
- uso de agentes;
- prompts operativos;
- integración entre conocimiento humano e inteligencia artificial.

---

## Qué vive en el Core y qué vive en la Biblioteca

Los **fundamentos de experiencia**, los **análisis de juegos por género** y el **mecanismo técnico** —cómo funciona un paso fijo, una colisión, un shader— no viven en el Core: viven en la Biblioteca de la Escuela (`05_Escuela/Biblioteca/`) y se consultan **on-demand**.

La frontera, medida en `ARQ-022` y en una línea:

```txt
el Core tiene el PRECIO de todo y el MECANISMO de nada
```

`Física costosa` dice cuánto sale la física por frame; ninguna nota del Core dice qué es un integrador. `Game loop` lo declara en su propio cuerpo: *"no existe para documentar el orden interno del motor"*. Las dos caras se necesitan y no se pisan — la de la Biblioteca es lo que la del Core da por sabido.

Lo que sí vive en el Core es el **índice** hacia esos libros: `Experiencia de juego`. Es un puntero liviano, no una copia, y cubre las dos mitades: experiencia (para Producción, Game Design, Level Design y UI/UX, antes de cerrar el `GDS`) y construcción (para Programación, después, al escribir el `SOL`).

```txt
el Core indexa   → liviano, siempre disponible
la Biblioteca    → el peso, se carga solo cuando hace falta
```

Esa es la única dirección en la que el Core enlaza hacia otra capa, y es deliberada: el Core sigue siendo la fuente de criterio, y parte del criterio es saber dónde está el resto. Lo que el Core **no** hace es depender de la Biblioteca para existir — si un libro falta, el Core lo dice y eso dispara una misión de Escuela.

Qué se promueve de la Biblioteca a criterio propio del Core lo decide el Área de Conocimiento con aprobación del owner.

---

## Uso del Core

VaultrumCore puede usarse de forma directa como fuente de consulta.

Una persona puede entrar a una carpeta, leer un concepto, tomar un criterio y aplicarlo en su propio proyecto.

La Agencia también usa VaultrumCore como base de conocimiento para trabajar sobre problemas, ideas, proyectos o tareas.

---

## Relación con la Agencia

La Agencia trabaja sobre proyectos, problemas, ideas y necesidades usando el conocimiento disponible en VaultrumCore.

VaultrumCore es la fuente de conocimiento.

La Agencia es la capa operativa que aplica ese conocimiento en situaciones concretas.

Cuando una experiencia genera un aprendizaje útil y reutilizable, ese aprendizaje puede volver al Core como mejora, corrección o nuevo contenido.

---

## Relación con la Comunidad

La Comunidad puede usar VaultrumCore para estudiar, construir, documentar o mejorar sus propios proyectos.

También puede proponer mejoras al Core mediante correcciones, nuevos contenidos, ejemplos, aclaraciones o reorganización de material existente.

Los aportes al Core deben mejorar al menos una de estas cosas:

- claridad;
- utilidad;
- criterio;
- aplicación práctica;
- navegación;
- coherencia;
- valor para personas;
- valor para la Agencia.

---

## Regla de VaultrumCore

VaultrumCore no existe para acumular información.

Existe para preservar conocimiento útil, claro y aplicable.
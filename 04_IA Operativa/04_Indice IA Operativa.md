# IA Operativa

Cuarta capa de Vaultrum. No es conocimiento de dominio (eso es el Core), ni trabajo asistido (eso es la Agencia): es la capa que cuida **cómo una IA opera Vaultrum**.

Vaultrum se da de contexto a una IA con ventana y tokens limitados. Esta capa existe para que esa operación sea eficiente, clara y sostenible: gastar bien los tokens, promptear con criterio y operar el vault sin romperlo.

---

## Por qué es una capa aparte

Hay dos sentidos de "IA" en Vaultrum, y conviene no mezclarlos:

- **IA para el juego** — pathfinding, NPCs, percepción. Vive en el Core (`03_VaultrumAi`). Es conocimiento de dominio.
- **IA que opera Vaultrum** — la que lee el vault, gasta tokens, sigue prompts. Es *esta* capa. Es conocimiento meta, sobre la operación del sistema.

Esta capa operacionaliza el **principio 8** ("escribirás para personas e IAs"): hasta ahora enunciado, acá desarrollado.

---

## Contenido

### [[01_Cuidado de tokens]]
El Token Budget como Frame Budget del contexto. Medir antes de podar. La fórmula costo × cantidad × frecuencia aplicada al contexto. Problemas típicos (acumulación, recarga, duplicación).

### [[02_Prompteo]]
Anatomía de un prompt operativo vaultrumita. Cómo dar Vaultrum de contexto sin saturar. Las skills de las áreas *son* prompts.

### [[03_Operar Vaultrum]]
Cómo una IA debe operar el vault: cargar por índices, partir del Core, declarar límites, no inventar.

### [[04_Pass GC de contexto]]
El pass tipo garbage collector que corre **en cada commit** para mantener la operación liviana. Su cadencia es el `Reducir frecuencia de actualización` del Core aplicado a tokens.

### [[05_Modo_Operacion]]
Los dos modos en que la IA opera el vault: **Modo Vaultrum** (usar el sistema para construir el proyecto del usuario) y **Modo Owner** (modificar el sistema mismo, protegido).

### [[06_Medicion de friccion]]
El instrumento que mide el **costo del owner en prompts** y lo separa en visión / aclaración / remedial. Es lo que vuelve falsable la Ley del baseline. No confundir con el conteo de tokens: son dos presupuestos distintos.

### [[07_Despacho de ejecucion]]
El segundo presupuesto de la capa: no qué contexto se carga, sino **dónde corre el trabajo y qué cuesta**. La ley del subagente —escribe el archivo, devuelve un resumen— con su contraejemplo medido, y el criterio de reparto entre ejecutor barato y modelo fuerte.

### Herramientas/

`contar_contexto.py` — el contador real de contexto. Mapa del vault por capa, archivos más pesados, costo de una carga concreta contra un presupuesto, y diff antes/después de podar. Es el Profiler de esta capa.

`bandeja/` — el canal entre el productor y los ejecutores que tienen manos: una orden `.md` entra, el observer la ejecuta parado en el proyecto, y el resultado vuelve con su estado. Es `07_Despacho de ejecucion` con una herramienta atrás. Cómo se arranca y qué se versiona: `bandeja/README.md`.

---

## Relación con la optimización del Core

Esta capa es la **optimización del Core aplicada a la IA en vez de al juego**. El mismo criterio: primero medir, después optimizar; no optimizar por intuición; no sobrearquitecturar.

```
Frame Budget           → Token Budget (ventana de contexto)
costo×cantidad×frecuencia → costo de cargar × cuánto × cada cuánto
GC Alloc / Memory Leak → contexto que se acumula y no se libera
Reducir frecuencia     → correr el pass en cada commit, no cada turno
Cacheo de referencias  → referenciar por índice/wikilink, no recargar
Medir antes de optimizar → medir tokens antes de podar
```

---

## Relación con las áreas

El Core alimenta todas las áreas; la Agencia produce; el Área de Conocimiento gestiona qué vuelve al Core. Esta capa cuida el *cómo* de la IA a lo largo de todo eso.

El **Pass GC** y el **Área de Conocimiento** comparten cadencia (ambos corren en cada commit), pero hacen cosas distintas: Conocimiento decide qué aprendizaje entra al Core; el Pass GC mantiene liviano el contexto de la IA.

---

## Regla de la capa

Esta capa debe practicar lo que predica: ser breve, clara y token-eficiente. Una capa sobre cuidar tokens no puede inflarse.

Y debe practicar lo que predica **también en el medir**: durante un tiempo esta capa decía "medir" y estimaba a ojo. Un pass de optimización sin instrumento es lo que el Core le prohíbe a cualquier optimización de rendimiento. El instrumento ahora existe (`Herramientas/contar_contexto.py`) y declara su propio margen de error.

Primero medir —contando, no estimando—. Después podar. Nunca podar de más.

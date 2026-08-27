# Plantilla — Cuaderno de proyecto

El cuaderno es **la memoria del proyecto**, no un log. Lo escribe Producción al cerrar el seteo y **es lo primero que se lee al abrir una sesión**: si existe, el Productor retoma en vez de preguntar de nuevo.

```txt
nombre     <Proyecto>.md, derivado del nombre de la carpeta
ubicacion  06_Proyectos/<Proyecto>/<Proyecto>.md   (raiz de la carpeta del proyecto)
techo      1.500 palabras. Al pasarlo, se parte (ver abajo).
```

**Se edita, no se acumula.** Un cuaderno con append infinito es contexto que se recarga entero en cada sesión — el costo exacto que `01_Cuidado de tokens` existe para evitar. Cada sección se reescribe; lo que dejó de ser cierto se saca.

Ley que lo sostiene: **Vaultrum no se escribe a sí mismo mientras trabaja** (`00_Leyes_en_antesala`).

---

## La plantilla

```markdown
# <Proyecto> — cuaderno de proyecto

> actualizado: AAAA-MM-DD · por: <area>

## 1. Identidad

| # | Pregunta | Respuesta | Origen |
|---|----------|-----------|--------|
| 1 | Qué es | … | declarado / inferido / **faltante** |
| … | (las quince del relevamiento de apertura) | | |

## 2. Entorno

motor · version elegida · plataforma · ruta del proyecto del motor

## 3. Estado

En qué punto de la cadena está el proyecto **hoy**, en dos o tres frases.
Qué está entregado, qué está abierto, qué está pausado y por qué.

## 4. Cadena

El índice de los artefactos del proyecto, por área.
Es la única sección que crece con el trabajo.

## 5. Decisiones

Qué se decidió, por qué, y **qué se descartó**. Una línea cada una.
Lo descartado vale tanto como lo elegido: evita rediscutirlo en la sesión doce.

## 6. Pendientes

Faltantes declarados, incluidos los que dejó la palabra de salteo.
Cada uno dice qué falta, no solo que falta.
```

---

## La fecha no es decorativa

El cuaderno **se desincroniza en silencio**: afirma un estado que el disco ya cambió, y nadie avisa. Pasó en la primera prueba real — el cuaderno de un proyecto declaraba un bloqueo que se había levantado el día anterior, y el Productor casi le dice al owner que no se podía avanzar.

Por eso:

```txt
1. Toda escritura del cuaderno actualiza la fecha. Sin excepcion.
2. Al RETOMAR, el Productor compara la fecha contra el disco antes de
   creerle a la seccion 3. Si el disco cambio despues, el cuaderno
   NO es la fuente: se corrige primero y se responde despues.
3. Un cuaderno mas viejo que su ultimo artefacto es un hallazgo,
   no un detalle.
```

**El cuaderno es memoria, no autoridad.** Ante divergencia manda el disco.

---

## Las tres marcas de origen

Cada dato de la sección 1 lleva de dónde salió, y **el `VE` los trata distinto**:

```txt
declarado   lo dijo el owner            vale como intención
inferido    salió del disco             vale como hecho verificable, no como intención
faltante    nadie lo respondió          es una deuda, no un hueco silencioso
```

Un dato inferido **no** es una respuesta del owner. Confundirlos es cómo un `VE` termina validando contra el papel del Productor en vez de contra lo que el owner quería.

## Cuando pasa el techo

No se borra: **se parte**. Las secciones pesadas salen a archivos hermanos y el cuaderno queda como índice.

```txt
<Proyecto>.md              identidad, entorno, estado — y links a lo demas
<Proyecto>_Decisiones.md   la seccion 5 cuando crece
<Proyecto>_Cadena.md       la seccion 4 cuando crece
```

Que sea una decisión medida y no un desborde.

## Hacia dónde seguir

- El procedimiento que lo genera y lo lee: `vaultrum-produccion`, Pasos 0 y 5.
- Dónde vive: **Dónde aterriza cada salida**, en `02_Indice Agencia`.

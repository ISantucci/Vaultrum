# Medición de fricción

La `Ley del baseline` dice que **el costo del owner se mide en prompts**. Durante un tiempo eso fue una afirmación sin instrumento: se comparaba `TL-002` contra `TL-003` a ojo (*"el desarrollo saca 4/10"*, *"esta vez fue mejor"*), que es exactamente el tipo de juicio que Vaultrum le prohíbe a una optimización de rendimiento.

Esta nota define el instrumento. Es corta a propósito: una métrica que necesita explicación larga no se registra.

---

## Por qué importa

Sin número, la Ley del baseline **no es falsable**. Se puede creer que el sistema mejora y estar equivocado, o mejorar y no poder demostrarlo. Las dos son formas de no saber.

Con número, cada entrega responde una pregunta concreta:

```txt
¿esta entrega costó más o menos prompts que la anterior comparable?
```

Esa es la única métrica que mide si Vaultrum está cumpliendo su promesa.

---

## Qué se cuenta

Un **prompt** es un mensaje del owner que pide o corrige algo. No cuenta cada mensaje: cuenta lo que costó llegar a la entrega.

Se clasifica en tres, porque la mezcla importa más que el total:

| Tipo | Qué es | Qué significa que suba |
|------|--------|------------------------|
| **Visión** | el owner aporta su idea, su criterio, una decisión que solo él puede tomar | **bien.** Es el gasto que Vaultrum existe para permitir |
| **Aclaración** | el owner responde algo que el sistema no pudo inferir | neutro. Algo de esto siempre hay |
| **Remedial** | el owner pide algo que un baseline competente debía traer, o corrige un desvío | **mal.** Es fricción pura: la Ley del baseline se está rompiendo |

```txt
Fricción = prompts remediales / prompts totales
```

El objetivo no es bajar el total. Es bajar **la proporción remedial**. Una entrega ambiciosa con muchos prompts de visión y ninguno remedial es un éxito, no un costo.

---

## Dónde se registra

En el `VE` de cada entrega, en un bloque de cuatro líneas:

```txt
FRICCION
  visión:     N
  aclaración: N
  remedial:   N   → <qué pidió, en una línea, por cada uno>
  fricción:   NN%
```

Los remediales se listan uno por uno. Sin la lista, el número no sirve para arreglar nada: el valor está en ver *qué* hubo que pedir dos veces.

El índice `00_Indice_ve` acumula la serie, que es lo único que permite ver tendencia.

---

## Cómo se cuenta sin volverlo una carga

La regla es que **el contador no puede costar un prompt**. Si registrar la métrica agrega fricción, la métrica se come a sí misma.

```txt
La IA lleva la cuenta durante la entrega, no el owner.
Al cerrar el VE, propone la clasificación.
El owner corrige lo que esté mal clasificado (eso sí es un prompt, y es barato).
```

Ante duda entre *aclaración* y *remedial*, se clasifica como **remedial**. Subestimar la fricción es el error caro: hace creer que el sistema anda mejor de lo que anda.

---

## Qué NO es esta métrica

- **No mide calidad de la entrega.** Un juego malo hecho en tres prompts sigue siendo un juego malo. La calidad la mide el `VE`; esto mide el costo.
- **No es comparable entre entregas de tamaño distinto.** Comparar un Pong contra un plataformero por número absoluto no dice nada. Lo comparable es la **proporción remedial**, y la serie de una misma clase de entregable.
- **No mide tokens.** Los tokens los mide AiCare con `contar_contexto.py`, y son el costo de la IA. Los prompts son el costo del owner. Son dos presupuestos distintos y se optimizan distinto.

```txt
tokens  → costo de la IA    → lo cuida AiCare
prompts → costo del owner   → lo cuida esta métrica
```

---

## Línea de base

La primera serie disponible, reconstruida a ojo y **declarada como estimación**, no como medición:

```txt
TL-002   fricción alta   — el owner puntuó el desarrollo 4/10 por cantidad de prompts
TL-003   fricción menor  — libro de género cargado antes del RQ, 9 table-stakes
                            como requerimiento explícito. Sin conteo formal.
```

Ninguno de los dos está medido con este instrumento: es anterior a él. **`TL-004` es la primera entrega que puede tener un número real**, y la primera comparación honesta va a ser `TL-004` contra `TL-005`.

Hasta entonces, cualquier afirmación sobre si Vaultrum bajó la fricción es una impresión. Vale como impresión y no vale como evidencia.

---

## Regla final

```txt
El owner gasta prompts en su visión.
Todo lo demás que tenga que pedir es una falla del sistema, y se cuenta.
```

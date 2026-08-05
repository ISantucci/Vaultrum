# Pass GC de contexto

La skill que ejecuta este pass se llama **AiCare**.

Un pass tipo **garbage collector** que corre **en cada commit** para mantener liviana la operación de la IA: liberar contexto que ya no aporta, detectar acumulación y confirmar que el trabajo sigue dentro del Token Budget.

No corre todo el tiempo (sería caro, como lógica costosa cada frame). No se deja para el final (el contexto se acumula como un memory leak y revienta el presupuesto en medio del desarrollo). El **commit es el intervalo sano** — es el `Reducir frecuencia de actualización` del Core aplicado a tokens.

---

## Por qué en cada commit

```
Cada turno   → demasiado frecuente, caro (como recalcular cada frame)
Al final     → demasiado tarde, el contexto ya se infló (leak)
Cada commit  → intervalo justo: hay un punto de corte natural y algo implementado que revisar
```

Comparte cadencia con el Área de Conocimiento (que también corre por commit), pero hace otra cosa: Conocimiento decide qué aprendizaje va al Core; el Pass GC limpia el contexto de trabajo de la IA.

---

## Qué revisa el pass

```
Acumulación   → ¿hay contexto arrastrado que ya no se usa?
Duplicación   → ¿se está cargando algo que ya vive en el Core?
Recarga       → ¿se recarga lo que no cambió?
Carga total   → ¿se leyó de más cuando alcanzaba un índice?
Presupuesto   → ¿el contexto actual está cómodo dentro del Token Budget?
```

---

## Flujo del pass (calcado de la optimización del Core)

```
Síntoma        → contexto pesado, se pierde el hilo, respuestas genéricas
→ Medir        → qué está cargado y cuánto pesa (no podar por intuición)
→ Diagnóstico  → qué es acumulación, duplicación o recarga
→ Podar        → liberar lo que no aporta; referenciar en vez de duplicar
→ Validar      → confirmar que no se perdió contexto necesario
```

Si no se puede medir, se declara y se propone cómo validar la hipótesis — nunca podar a ciegas.

---

## Qué NO debe hacer el pass

```
Podar de más (perder contexto necesario por ahorrar tokens)
Correr en cada turno (optimización prematura y cara)
Optimizar sin medir
Tocar el Core o las salidas (solo gestiona el contexto de operación)
```

Una nota o un contexto claro pero algo largo no es un problema hasta medirlo como problema (principio: no sobrearquitectura).

---

## Salida del pass

```
## Pass GC — <commit>
## Medición: qué había cargado (aprox.)
## Detectado: acumulación / duplicación / recarga
## Podado: qué se liberó y por qué
## Validación: contexto necesario intacto
## Estado del Token Budget: cómodo / ajustado
```

---

## Regla final

El Pass GC cuida que la IA siga operando barato y claro a lo largo del desarrollo. Libera lo que no aporta, en el momento justo, sin romper lo que sí sirve.

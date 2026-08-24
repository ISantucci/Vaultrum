# Cuidado de tokens

Cuidar tokens es tratar la ventana de contexto de la IA como un recurso limitado con presupuesto, igual que el Frame Budget trata el tiempo de cada frame.

Regla base, prestada del Core:

```
Primero medir.
Después optimizar.
Optimizar sin medir es adivinar.
```

---

## Token Budget

La ventana de contexto es el presupuesto por turno. Todo lo cargado —vault, historial, instrucciones, salidas— compite por ese presupuesto, igual que todos los sistemas de un frame compiten por 16.66 ms.

Preguntas base:

```
¿Cuánto presupuesto tengo?
¿Cuánto estoy usando?
¿Qué parte se está pasando?
¿Qué puedo no cargar?
```

Como el Frame Budget: no importa solo que algo "entre", importa cuánto cuesta, cuántas veces se carga y si escala.

---

## Costo × cantidad × frecuencia

La misma fórmula del Core, aplicada al contexto:

```
Costo total
=
costo de cargar algo
× cantidad que se carga
× frecuencia con que se recarga
```

Optimizar ataca una de las tres:

```
Reducir costo    → notas más breves y autocontenidas
Reducir cantidad → cargar por índices, solo lo que aplica
Reducir frecuencia → no recargar lo que no cambió; correr el pass por commit
```

Ejemplo: releer el vault entero en cada turno es como recalcular pathfinding cada frame para todos los NPCs. Barato una vez, caro por acumulación.

---

## Medir antes de podar

No se poda contexto por intuición. Igual que no se optimiza un juego sin Profiler.

```
Síntoma (contexto pesado / respuestas lentas / se pierde el hilo)
→ medir qué está cargado y cuánto pesa
→ diagnosticar qué sobra
→ podar puntual
→ validar que no se perdió nada necesario
```

### El Profiler del contexto

Durante un tiempo esta capa predicaba medir y en la práctica estimaba. Ahora hay contador: `Herramientas/contar_contexto.py`.

```bash
python "04_IA Operativa/Herramientas/contar_contexto.py" mapa
python "04_IA Operativa/Herramientas/contar_contexto.py" pesados --top 20
python "04_IA Operativa/Herramientas/contar_contexto.py" carga --manifiesto .aicare/carga-actual.txt --presupuesto 40000
python "04_IA Operativa/Herramientas/contar_contexto.py" diff .aicare/antes.txt .aicare/despues.txt
```

Cuenta bytes y caracteres de forma exacta, y tokens de forma exacta si hay un tokenizador instalado o aproximada (±12%) si no. **Declara siempre en qué modo contó** — una estimación presentada como conteo es el mismo error que un `Cerrado` en falso.

Lo que el contador **no** mide, y no se finge que mida: el consumo real de la ventana del modelo, el historial de conversación y las salidas generadas. Mide el costo del material del vault que se carga, que es la parte que Vaultrum controla.

Una nota clara pero un poco larga **no es un problema hasta que se mide como problema**. Podar de más rompe utilidad, como bajar calidad visual sin diagnóstico.

---

## Problemas típicos de contexto

Fichas de diagnóstico, al estilo de los Problemas de rendimiento del Core:

```
Acumulación / leak   → contexto que se arrastra turno a turno sin liberarse
Recarga innecesaria  → volver a cargar algo que no cambió
Duplicación          → incluir texto que ya vive en el Core en vez de referenciarlo
Carga total          → leer el vault entero cuando alcanzaba un índice
Historial inflado    → arrastrar toda la conversación cuando importa el estado actual
```

---

## Soluciones

Prestadas del Core (Cacheo, Reducir frecuencia, Object Pool):

```
Cargar por índices/MOCs   → como cachear referencias: se apunta, no se recarga
Referenciar con wikilink  → incluir el link, no el contenido
Escribir autocontenido    → cada nota se entiende sola, sin arrastrar diez más
Podar por commit          → el Pass GC, no cada turno
```

---

## Dos presupuestos, no uno

Conviene no mezclarlos, porque se optimizan distinto:

```
tokens  → costo de la IA     → lo cuida AiCare con contar_contexto.py
prompts → costo del owner    → lo cuida [[06_Medicion de friccion]]
```

Bajar tokens a costa de que el owner tenga que pedir tres veces lo mismo es un mal negocio: se ahorra en el presupuesto barato y se gasta en el caro.

---

## Regla final

El vault ya está diseñado para esto: los índices existen para cargar selectivamente. Cuidar tokens es usar esa estructura, no pelearla.

No hacer trabajo de contexto innecesario suele ser mejor que hacerlo rápido.

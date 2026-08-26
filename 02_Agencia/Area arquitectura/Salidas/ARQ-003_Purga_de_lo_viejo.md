---
tipo: pasada de arquitectura
alcance: índices de Salidas, raíz del vault, restos de las dos pasadas anteriores
estado: cerrada
---

# ARQ-003 — Purga de lo viejo

Tercera pasada. No buscó links: buscó **texto que describía un vault que ya no existe**. Las dos pasadas anteriores cambiaron la forma del grafo y dejaron reglas, notas y descripciones hablando de la forma vieja.

---

## Restos de tabla en los índices de Salidas

Los ocho índices de Salidas venían de una conversión automática de tabla a cascada, y se notaba:

- **el alias repetía el nombre del archivo** — ``GDS-001.1_Paletas``, ``UXS-003.5_Flujo_De_Pantallas``, con Title Case mal puesto;
- **la metadata venía en tira de puntos medios** — `RQ-001.1 · Paletas controlables · Cerrada`, que es una fila de tabla sin celdas;
- **la columna de estado repetía el mismo valor** diecisiete veces. Una columna con un solo valor no es información;
- **los tres proyectos estaban en una lista plana**, sin decir dónde termina uno y empieza el otro.

Ahora los ocho agrupan por timeline, el alias es el nombre legible, la descripción es prosa y el estado va una vez por grupo — solo se marca la excepción. Y queda dicho lo que antes había que deducir: el `RQ-XXX.1` de setup no tiene `GDS` porque no hay sistema jugable que diseñar.

---

## Reglas que describían la forma vieja

Seis índices decían **"al registrar, linkear al `RQ`/`GDS`/`SOL`"**. Después de ARQ-001 el índice ya no enlaza el insumo: lo nombra, y quien lo declara es la ficha. La regla quedó reescrita en los seis: *"el `X` declara su insumo en su propia ficha, y el índice lo nombra"*.

También se fue el `(columna *Modo*)` del índice de `VE`, que apuntaba a una columna que ya no existe.

---

## Secciones que quedaron dobles

ARQ-001 enganchó los índices de Salidas desde cada `Area_*.md` agregando una sección nueva, sin ver que cinco áreas ya tenían una sección que explicaba su salida. Quedaron `## Salida del área` y `## Salidas del área`, una al lado de la otra.

Fusionadas: el link vive ahora al final de la sección que ya explicaba el concepto. Lo mismo en Conocimiento (`Staging`) y en la Escuela, donde el registro que se agregó repetía un `## Índice interno` que ya estaba.

---

## Restos en la raíz

- **`ARQ-000_Auditoria_de_arquitectura` (AUD-001)** se presentaba como *"el estado real del sistema"* y describe el estado de un momento anterior a las dos pasadas. Queda marcada como registro fechado, con la serie continuando en `ARQ`. Su sección de **Método** describía a mano seis pasos que hoy corre `grafo.py`: quedaron los dos que la herramienta no cubre.
- **`H2`** del backlog de esa auditoría estaba abierto y ya estaba cerrado en `Area_conocimiento`.
- **La nota de agentes legacy** del índice de la Agencia listaba siete roles absorbidos hace tres semanas. Queda la regla, se fue el inventario de nombres muertos.
- **La bitácora** suma la ley candidata #6: las seis leyes del grafo, con el dato que habilitó aplicarlas (ninguna skill navega por wikilink).

---

## Archivos

`_to_delete/` juntó lo que no sirve y no se puede borrar desde acá: el zip del lote `EST-006`, dos lock files vacíos de AiCare y un `__pycache__`. Se borra a mano desde el explorador. Quedó en `.gitignore` para que no entre a un commit por accidente.

---

## Cómo quedó

```txt
433 notas · 617 links · 0 rotos · 0 ambiguos · 0 flotando
```

Ninguna nota cambió lo que dice sobre su tema. Lo que cambió es que ninguna sigue describiendo un vault que ya no existe.

# RA-001 — Organizacion de assets en la escena

**Insumo:** dictado directo del owner, sesion 2026-09-01, sobre el arbol low poly ya construido.
**Estado:** Vigente.

## La regla

> Un asset **no es un objeto suelto en la escena**. Es una carpeta con nombre propio, y adentro sus partes separadas, cada una con su nombre.

```txt
Scene Collection
└── Arbol                 <- collection con el nombre del asset
    ├── Tronco
    ├── Hoja_01
    ├── Hoja_02
    ├── Hoja_03
    └── Hoja_04
```

## Que responde

Cuando el asset esta fusionado en un solo objeto, tocar una parte obliga a entrar a Edit Mode y seleccionar a mano. Cuando esta separado pero suelto en la raiz de la escena, dos assets se pisan y el Outliner deja de ser navegable. La carpeta resuelve las dos: **cada parte se toca sola, y el asset se mueve entero.**

## Como se aplica

```txt
1. Una collection por asset, nombrada como el asset      Arbol, Fogata
2. Cada parte, un objeto propio con nombre descriptivo   Tronco, Hoja_01, Roca_03
3. Numeracion con dos digitos y cero a la izquierda      _01, no _1
4. Las partes se emparentan a la pieza estructural       hojas -> Tronco
5. El nombre del objeto y el de su malla coinciden
```

El paso 4 es lo que hace que mover el asset no lo desarme: se agarra la pieza padre y va todo.

## Que NO es

No es agrupar con `Ctrl+J`: eso fusiona y pierde el control por pieza, que es justo lo que la regla busca. No es un empty como padre: la pieza estructural real (el tronco) ya cumple ese rol y ademas es geometria util.

## Evidencia

Sesion 2026-09-01. El arbol se construyo primero como **un solo objeto fusionado** (100 caras, boolean union), y el owner lo rechazo pidiendo las partes separadas. Al entregarlas separadas pero sueltas en `Collection`, corrigio otra vez: faltaba la carpeta. La regla salio de las dos correcciones, no de una preferencia declarada de entrada.

## Verificacion

Se comprueba mirando el Outliner, o por script:

```python
col = bpy.data.collections["Arbol"]
assert len(col.objects) > 1                       # esta separado
assert all(o.parent for o in col.objects if o.name != "Tronco")   # esta emparentado
```

## Limite encontrado al aplicarla (2026-09-01, fogata)

El paso 4 —emparentar a la pieza estructural— **supone que hay una pieza estructural**. En el arbol la hay: el tronco. En la fogata no: nueve rocas en anillo y tres troncos apoyados, ninguno mas estructural que otro.

Se resolvio anclando a `Tronco_01`, que funciona pero es arbitrario. La alternativa natural —un empty como padre— esta prohibida por esta misma nota, y esa prohibicion se escribio pensando en el arbol.

**Queda abierto para el owner:** o se admite el empty cuando no hay pieza estructural, o se declara que el ancla es "la primera pieza de la parte central". No se decide por defecto.

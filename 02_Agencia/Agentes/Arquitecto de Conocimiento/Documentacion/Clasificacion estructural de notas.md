# Clasificación Estructural de Notas

## Propósito

Antes de modificar, crear, mover o validar una nota, el Modo Arquitecto debe identificar qué tipo de documento está trabajando.

Una nota puede funcionar como:

```txt
índice
nota base
nota consumidora
algoritmo
aplicación
prompt operativo
flujo de trabajo
reporte
registro de aprendizaje
```

Esta clasificación define qué puede y qué no puede hacer la nota.

No todas las notas tienen la misma responsabilidad.

---

## Índice

Un índice orienta.

Debe mostrar:

```txt
propósito de la carpeta
organización general
notas incluidas
criterio de uso
relación entre secciones
```

Un índice no debe desarrollar en profundidad cada tema.

**Ejemplo**:

```txt
Navegación y pathfinding.md
→ orienta la carpeta.

Pathfinding.md
→ desarrolla el concepto.
```

---

## Nota Base o Proveedora

Una nota base define contrato.

Debe explicar:

```txt
qué es
qué representa
qué datos puede contener
qué responsabilidad tiene
qué NO debe hacer
cómo se valida
errores comunes
regla final
```

No debe explicar todos sus consumidores.

**Ejemplo**:

```txt
Nodos.md
→ define nodo, datos, vecinos, estado, costo y límites.
```

NO debe convertirse en:

```txt
Nodos.md
→ explicación completa de Pathfinding, NPC, Rutas alternativas y Algoritmos.
```

---

## Nota Consumidora

Una nota consumidora explica cómo usa una estructura, regla o algoritmo existente.

Puede llamar a notas proveedoras cuando las necesita.

**Ejemplo**:

```txt
Pathfinding.md
→ puede explicar cómo consume nodos, grillas o costos.
```

Pero no debe redefinir esas notas base.

---

## Algoritmo

Una nota de algoritmo explica procedimiento.

Debe responder:

```txt
qué problema resuelve
qué datos necesita
cómo funciona
qué resultado devuelve
cuándo conviene usarlo
cuándo no conviene usarlo
costos de implementación
costos de optimización
```

**Ejemplo**:

```txt
A Star
→ vive en Algoritmos.

Theta Star
→ vive en Algoritmos.
```

Un algoritmo puede ser consumido por mapas, NPCs u otros sistemas, pero no debe quedar encerrado en una carpeta consumidora si su naturaleza es general.

---

## Aplicación

Una nota de aplicación decide con criterio cuándo conviene usar una técnica, estructura o algoritmo en un caso real.

Debe responder:

```txt
cuándo conviene
cuándo no conviene
qué problema resuelve
qué costo tiene
qué riesgos tiene
cómo se valida
qué queda fuera
```

**Ejemplo**:

```txt
IA aplicada al diseño de mapas
→ decide cómo usar estructuras de mapa según el juego.
```

---

## Reporte o Registro de Aprendizaje

Un reporte no debe reabrir toda la arquitectura.

Debe registrar:

```txt
qué se hizo
qué agentes participaron
qué aprendió cada área
qué reglas nuevas surgieron
qué debería integrarse a futuro
```

Si el reporte detecta una regla repetible, el Arquitecto debe proponer dónde integrarla.

---

## Regla Proveedor-Consumidor

El Modo Arquitecto debe proteger esta dirección:

```txt
Proveedor
→ define contrato.

Consumidor
→ explica uso.

Índice
→ orienta.

Algoritmo
→ procesa.

Aplicación
→ decide con criterio.
```

**Error a evitar**:

```txt
El hijo se vuelve padre del padre.
```

**Ejemplo incorrecto**:

```txt
Nodos.md explica todo Pathfinding.
```

**Ejemplo correcto**:

```txt
Nodos.md define contrato.
Pathfinding.md explica cómo consume nodos.
```

---

## Criterio de Reubicación

Cuando un contenido parece estar en la carpeta equivocada, el Modo Arquitecto debe evaluar su naturaleza.

**Ejemplos**:

```txt
A Star
→ algoritmo
→ debe vivir en Algoritmos.

Theta Star
→ algoritmo
→ debe vivir en Algoritmos.

Line of Sight
→ técnica transversal
→ no debe encerrarse automáticamente en mapas o NPC.

Pathfinding
→ proceso de navegación
→ puede vivir en IA para mapas si se aplica al espacio.
```

La ubicación debe responder a la responsabilidad del concepto, no a dónde apareció primero.

---

## Regla Final

```txt
Antes de ordenar contenido,
ordena responsabilidades.

Antes de crear una nota,
define si orienta, provee, consume, procesa, aplica o registra.
```

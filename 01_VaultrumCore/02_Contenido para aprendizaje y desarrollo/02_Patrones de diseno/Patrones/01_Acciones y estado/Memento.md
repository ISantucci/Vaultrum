## Definicion

Memento es un patron que permite guardar y restaurar el estado de un objeto sin exponer todos sus detalles internos.

```txt
Objeto
→ crea snapshot

Memento
→ guarda estado

Objeto
→ restaura estado
```

---

## Idea central

Memento separa el guardado de estado de la manipulacion directa de los datos internos.

El objetivo es poder volver a un estado anterior de forma controlada.

---

## Que problema resuelve

Memento ayuda cuando se necesita restaurar estados sin romper encapsulamiento.

Problemas comunes:

- undo necesita recuperar estado anterior,
- checkpoint debe restaurar datos,
- se quieren snapshots,
- guardar estado expone demasiados detalles,
- revertir cambios se vuelve manual y fragil.

---

## Cuando conviene usarlo

Conviene considerar Memento cuando:

- se necesita restaurar estado,
- hay checkpoints,
- hay undo de cambios complejos,
- se requiere snapshot antes de modificar,
- el estado interno no deberia exponerse,
- se necesita volver a una version previa.

Ejemplos posibles:

```txt
estado de una torre
estado de inventario
estado de nivel
checkpoint
configuracion previa
accion editable
```

---

## Cuando NO conviene usarlo

No conviene usar Memento si:

- el estado es trivial,
- no hace falta restaurar,
- guardar estado completo es demasiado costoso,
- una copia simple alcanza,
- exponer todo el estado generaria mas problemas,
- no hay flujo real de undo o restauracion.

---

## Como decidir si aplica

Antes de proponer Memento, la IA debe responder:

```txt
¿Que estado necesita guardarse?
¿Para que se restaura?
¿Que datos son necesarios?
¿El estado es costoso?
¿El objeto deberia exponer esos datos?
¿Existe ya un sistema de guardado o snapshot?
¿Una solucion simple alcanza?
```

---

## Estructura conceptual

```txt
Originator
→ objeto que tiene estado

Memento
→ snapshot del estado

Caretaker
→ guarda mementos sin conocer detalles internos
```

La estructura puede simplificarse segun el proyecto.

---

## Ejemplo conceptual breve

Sin Memento:

```txt
Undo
→ accede a muchos campos internos
→ intenta reconstruir estado manualmente
```

Problema:

```txt
El sistema externo conoce demasiado.
Restaurar se vuelve fragil.
```

Con Memento:

```txt
Objeto
→ entrega snapshot

Sistema externo
→ guarda snapshot

Objeto
→ restaura desde snapshot
```

---

## Como debe usarlo una IA

Una IA debe considerar Memento cuando hay restauracion de estado no trivial.

Debe razonar asi:

```txt
Se necesita volver atras
→ identifico estado necesario
→ reviso si puede guardarse sin exponer internals
→ reviso sistema existente
```

Antes de implementar, debe presentar:

```txt
Estado a guardar
Motivo de restauracion
Datos incluidos
Datos excluidos
Sistema existente
Alternativa simple
Riesgos
Validacion esperada
```

---

## Como NO debe usarlo una IA

Una IA no debe usar Memento para cualquier variable.

No debe:

- guardar snapshots enormes sin necesidad,
- duplicar sistemas de guardado,
- exponer internals que deberian estar protegidos,
- usarlo si no hay restauracion real,
- agregar historial infinito sin control,
- mezclar Memento con persistencia completa sin analizarlo.

Ejemplo de mal uso:

```txt
Problema:
Guardar un booleano de abierto/cerrado.

Mala decision:
Crear Memento completo.

Motivo:
Una variable o estado simple alcanza.
```

---

## Reutilizacion antes que invencion

Si ya existe un sistema de guardado, undo o snapshot, la IA debe revisarlo antes de proponer Memento.

---

## Senales de que Memento puede servir

Puede valer la pena analizar Memento si:

- se necesita restaurar estado anterior,
- el undo requiere varios datos,
- un checkpoint debe recuperar configuracion,
- un sistema externo conoce demasiados campos internos,
- revertir manualmente genera bugs.

---

## Senales de Memento mal aplicado

Memento probablemente esta mal aplicado si:

- guarda mas datos de los necesarios,
- no hay restauracion real,
- consume demasiada memoria,
- duplica persistencia,
- expone detalles internos,
- complica un estado simple.

---

## Preguntas antes de implementar

```txt
¿Que estado debe guardarse?
¿Cuando se crea el snapshot?
¿Cuando se restaura?
¿Quien guarda el memento?
¿Que datos quedan fuera?
¿Cuanto cuesta en memoria?
¿Como se valida?
```

---

## Formato de propuesta esperado

```txt
Patron:
Memento

Estado a guardar:
...

Motivo:
...

Datos incluidos:
...

Sistema existente:
...

Alternativa simple:
...

Riesgos:
...

Validacion:
...
```

---

## Resultado esperado

Aplicar bien Memento deberia permitir:

- restaurar estados,
- proteger detalles internos,
- implementar snapshots,
- facilitar undo complejo,
- reducir errores al revertir,
- mantener estado controlado.

---

## Regla final

```txt
Memento no existe para guardar todo.
Existe para restaurar estado necesario sin exponer detalles internos innecesarios.
```
## Proposito

Esta seccion reune los principios SOLID como base de criterio para diseñar sistemas mas claros, mantenibles y extensibles.

No existe para aplicar reglas de forma automatica.
No existe para llenar el codigo de abstracciones.
No existe para sobrearquitecturar proyectos simples.

Existe para ayudar a detectar responsabilidades mezcladas, dependencias fragiles, herencias mal usadas, interfaces innecesarias y sistemas dificiles de modificar.

---

## Idea central

SOLID dentro de Vaultrum se entiende como criterio de diseño.

```txt
Problema de arquitectura
→ responsabilidad
→ dependencia
→ extension
→ mantenibilidad
→ decision tecnica
```

El objetivo no es demostrar tecnica.

El objetivo es tomar mejores decisiones al diseñar clases, componentes, managers, sistemas de gameplay, UI, IA, herramientas o cualquier estructura de software.

---

## Cuando usar esta seccion

Consultar esta seccion cuando haga falta:

- revisar responsabilidades de una clase,
- detectar clases demasiado grandes,
- evaluar acoplamiento,
- diseñar sistemas extensibles,
- separar logica de UI,
- revisar managers,
- preparar una implementacion,
- auditar codigo,
- decidir si una abstraccion tiene sentido,
- evitar que un cambio rompa partes no relacionadas,
- validar si una solucion tecnica respeta Vaultrum.

---

## Como debe usar esta seccion una IA

Una IA debe usar esta seccion como base de criterio antes de proponer o ejecutar cambios tecnicos.

Antes de aplicar una solucion, debe preguntarse:

```txt
¿Que responsabilidad tiene cada clase?
¿Hay una clase haciendo demasiado?
¿El sistema puede extenderse sin modificar todo?
¿La herencia representa una relacion real?
¿La interfaz obliga a implementar cosas innecesarias?
¿Las dependencias estan demasiado atadas a implementaciones concretas?
¿Aplicar SOLID aca mejora el sistema o lo complica sin necesidad?
```

La IA no debe usar SOLID como excusa para crear capas, interfaces o patrones innecesarios.

Debe usarlo para justificar decisiones tecnicas con criterio.

---

## Como recorrer esta seccion

El recorrido recomendado es:

```txt
1. Entender el problema tecnico.
2. Identificar que principio puede estar relacionado.
3. Leer la nota del principio correspondiente.
4. Comparar el caso real contra el criterio del principio.
5. Proponer una mejora minima y justificada.
6. Validar antes de ejecutar.
```

No hace falta leer todos los principios para cada tarea.

Se consulta el principio que ayude a resolver el problema real.

---

## Principios incluidos

## [[S - Single Responsibility Principle]]

Se enfoca en que una clase, componente o sistema tenga una responsabilidad clara y una razon principal para cambiar.

Sirve para detectar clases que mezclan logica, UI, datos, audio, validaciones o coordinacion en un solo lugar.

---

## [[O - OpenClosed Principle]]

Se enfoca en permitir que un sistema pueda extenderse sin modificar constantemente codigo existente.

Sirve para pensar variantes, nuevos comportamientos, nuevos tipos de objetos o nuevas reglas sin romper lo que ya funciona.

---

## [[L - Liskov Substitution Principle]]

Se enfoca en que una clase derivada pueda reemplazar a su clase base sin romper el comportamiento esperado.

Sirve para revisar si una herencia representa una relacion real o si se esta forzando una jerarquia incorrecta.

---

## [[I - Interface Segregation Principle]]

Se enfoca en evitar interfaces demasiado grandes o genericas.

Sirve para que una clase no tenga que implementar metodos que no necesita.

---

## [[D - Dependency Inversion Principle]]

Se enfoca en que los sistemas importantes dependan de abstracciones cuando eso reduzca fragilidad y mejore flexibilidad.

Sirve para evitar que la logica principal quede atada innecesariamente a implementaciones concretas.

---

## Criterio de uso

SOLID debe aplicarse cuando mejora:

- claridad,
- mantenimiento,
- extension,
- separacion de responsabilidades,
- testeo,
- integracion,
- escalabilidad razonable,
- reduccion de dependencias fragiles.

SOLID no debe aplicarse cuando solo agrega:

- capas innecesarias,
- interfaces sin uso real,
- abstracciones prematuras,
- complejidad accidental,
- codigo mas dificil de entender,
- soluciones mas grandes que el problema.

---

## Errores que esta seccion ayuda a evitar

Esta seccion ayuda a detectar problemas como:

- clases dios,
- managers que absorben todo,
- UI decidiendo logica de gameplay,
- herencias forzadas,
- interfaces gigantes,
- codigo dificil de extender,
- dependencias rigidas,
- cambios que rompen sistemas no relacionados,
- patrones aplicados sin necesidad,
- refactors sin criterio.

---

## Uso correcto dentro de Vaultrum

El uso correcto de esta seccion es:

```txt
Problema real
→ principio relacionado
→ lectura puntual
→ decision tecnica
→ validacion
```

No es:

```txt
Quiero usar SOLID
→ creo interfaces y abstracciones
→ complico el sistema
→ justifico la complejidad despues
```

SOLID debe funcionar como criterio base de diseño.

Otras secciones pueden apoyarse en estos principios cuando necesiten evaluar responsabilidades, dependencias, extension o mantenibilidad.

Esta seccion no necesita listar todas las partes de Vaultrum que pueden relacionarse con SOLID.

Cada seccion del vault puede referenciar SOLID cuando lo necesite.

El objetivo es mantener esta seccion estable, clara y sin dependencias innecesarias hacia documentos que pueden cambiar en el futuro.

SOLID debe sostener la arquitectura.

No debe reemplazar el criterio.

---

## Regla final

```txt
SOLID no existe para hacer codigo mas complejo.
Existe para hacer sistemas mas claros, mantenibles y dificiles de romper.
```
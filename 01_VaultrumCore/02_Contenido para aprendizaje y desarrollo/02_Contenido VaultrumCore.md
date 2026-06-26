## Qué es esta sección

Esta sección reúne el contenido técnico y práctico principal de VaultrumCore.

Contiene conocimiento orientado a programación, arquitectura, patrones, optimización, estructuras de datos, algoritmos y managers aplicados al desarrollo de videojuegos, software y sistemas creativos.

Su función es servir como base de consulta para personas y como base de conocimiento obligatoria para la Agencia.

No está pensada como una lista de temas aislados.

Está pensada como una base ordenada de conceptos que ayudan a pensar, decidir, construir y mejorar proyectos reales.

---

## [[Principios SOLID]]

Sección dedicada a los principios SOLID.

Estos principios sirven para pensar responsabilidades, dependencias, extensibilidad y mantenimiento del código.

Incluye:

- Single Responsibility Principle;
- Open/Closed Principle;
- Liskov Substitution Principle;
- Interface Segregation Principle;
- Dependency Inversion Principle.

Usar esta sección cuando el problema esté relacionado con:

- clases con demasiadas responsabilidades;
- código difícil de modificar;
- dependencias rígidas;
- herencia mal aplicada;
- interfaces demasiado grandes;
- arquitectura difícil de mantener;
- necesidad de separar responsabilidades.

SOLID no se usa para decorar arquitectura.

Se usa para tomar mejores decisiones de diseño.

---

## [[Patrones de diseno]]

Sección dedicada a patrones de diseño aplicados a videojuegos y software.

Los patrones no son soluciones obligatorias.

Son herramientas conceptuales para resolver problemas recurrentes de diseño, comunicación, creación, comportamiento, acceso, coordinación u optimización.

Incluye grupos como:

- acciones y estado;
- creación y datos;
- comunicación y flujo;
- comportamiento;
- acceso y coordinación;
- optimización práctica.

Usar esta sección cuando se repite un problema de estructura y conviene resolverlo con una solución conocida, mantenible y adaptable.

La regla base es no aplicar patrones por costumbre.

Primero se entiende el problema.

Después se elige el patrón si realmente aporta claridad, flexibilidad o mantenimiento.

---

## [[Optimizacion]]

Sección dedicada a rendimiento, diagnóstico y mejora de sistemas.

Incluye fundamentos, problemas frecuentes, herramientas de detección, metodologías y soluciones prácticas.

Sirve para entender:

- bottlenecks;
- frame budget;
- CPU bound;
- game loop;
- allocations;
- problemas por frame;
- uso de profiler;
- memory profiler;
- update managers;
- object pools;
- cacheo de referencias;
- separación entre lógica pura y MonoBehaviour.

Usar esta sección cuando el problema esté relacionado con rendimiento, consumo de memoria, frecuencia de actualización, uso innecesario de recursos o arquitectura poco eficiente.

La regla base es medir antes de optimizar.

---

## [[Estructuras de datos]]

Sección dedicada a estructuras de datos útiles para organizar, consultar, recorrer o priorizar información.

Sirve para entender cuándo conviene usar una estructura sobre otra según el problema.

Usar esta sección cuando haya que trabajar con:

- colecciones;
- búsqueda;
- ordenamiento;
- prioridad;
- relaciones entre elementos;
- recorrido de datos;
- representación de estados;
- organización de entidades;
- acceso eficiente a información.

Una estructura de datos no se elige porque sea avanzada.

Se elige porque representa bien el problema y mejora la forma de resolverlo.

---

## [[Algoritmos]]

Sección dedicada a procesos, métodos y pasos reutilizables para resolver problemas.

Incluye conocimiento aplicable a búsqueda, ordenamiento, recorrido, toma de decisiones, cálculo de caminos y resolución de sistemas.

Usar esta sección cuando el problema no sea solo “qué datos guardar”, sino “cómo procesarlos”.

Los algoritmos ayudan a transformar información en resultado.

La clave es entender:

- qué problema resuelven;
- qué datos necesitan;
- qué costo tienen;
- cuándo conviene usarlos;
- cuándo son innecesarios;
- cómo aplicarlos en videojuegos o software.

---

## [[Managers]]

Sección dedicada al uso, diseño, auditoría y refactorización de managers.

Los managers sirven para coordinar responsabilidades de sistema, pero pueden convertirse fácilmente en clases dios si no se diseñan con criterio.

Usar esta sección cuando el problema esté relacionado con:

- coordinación de sistemas;
- acceso a servicios;
- actualización centralizada;
- pooling;
- audio;
- UI;
- escenas;
- guardado;
- eventos;
- configuración;
- managers innecesarios;
- managers con demasiadas responsabilidades.

La regla base es que un manager debe coordinar una responsabilidad clara.

No debe absorber lógica que pertenece a otros sistemas.

---

## Cómo usar esta sección

Esta sección puede recorrerse de forma libre.

Una persona puede entrar directamente al tema que necesita y usarlo como referencia para su proyecto.

También puede ser usada por la Agencia como base de conocimiento para asistir en tareas de arquitectura, programación, documentación, optimización o diseño técnico.

El contenido no debe aplicarse de forma automática.

Debe usarse con criterio según el problema real.

---

## Relación con VaultrumCore

Esta sección forma parte de VaultrumCore porque concentra conocimiento reutilizable.

Cada tema debe aportar al menos una de estas cosas:

- claridad conceptual;
- criterio técnico;
- mejora de arquitectura;
- capacidad de decisión;
- prevención de errores;
- aplicación práctica;
- utilidad para personas;
- utilidad para la Agencia.

---

## Regla de esta sección

No se agrega contenido para completar una lista.

Se agrega contenido cuando ayuda a pensar, decidir, construir o mejorar.
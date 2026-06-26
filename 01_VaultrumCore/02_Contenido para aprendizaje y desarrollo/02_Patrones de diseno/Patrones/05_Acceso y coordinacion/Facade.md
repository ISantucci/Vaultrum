## Definicion

Facade es un patron de diseno que ofrece una entrada simple para interactuar con uno o varios subsistemas.

En lugar de que un sistema externo conozca muchos detalles internos, se comunica con una fachada.

```txt
Sistema externo
→ Facade
→ subsistemas internos
```

La fachada simplifica el acceso, pero no reemplaza la logica interna.

---

## Idea central

Facade reduce la complejidad visible desde afuera.

```txt
Muchos subsistemas
→ una entrada clara
→ menor acoplamiento externo
```

El objetivo no es esconder desorden.

El objetivo es ofrecer una interfaz de uso clara hacia una parte compleja del sistema.

---

## Que problema resuelve

Facade ayuda cuando un sistema necesita usar varios subsistemas y empieza a conocer demasiados detalles internos.

Problemas comunes:

- una clase externa llama a muchos sistemas distintos,
- la logica de uso queda repetida en varios lugares,
- usar un sistema requiere demasiados pasos,
- los detalles internos se filtran hacia afuera,
- cambiar un subsistema obliga a modificar muchos clientes,
- la integracion se vuelve dificil de entender.

---

## Cuando conviene usarlo

Conviene considerar Facade cuando:

- hay varios subsistemas que trabajan juntos,
- se necesita una entrada simple,
- muchos clientes repiten el mismo flujo,
- se quiere reducir acoplamiento externo,
- se necesita ocultar detalles de coordinacion,
- el uso correcto del sistema tiene varios pasos.

Ejemplos posibles:

```txt
sistema de construccion
sistema de inventario
sistema de misiones
sistema de guardado
sistema de economia
sistema de upgrades
```

---

## Cuando NO conviene usarlo

No conviene usar Facade si:

- solo hay un sistema simple,
- la fachada solo reenvia llamadas sin aportar claridad,
- se usa para esconder mala arquitectura,
- termina acumulando demasiadas responsabilidades,
- duplica logica que deberia vivir en los subsistemas,
- agrega una capa que nadie necesita.

Facade no debe convertirse en una clase dios.

---

## Como decidir si aplica

Antes de proponer Facade, la IA debe responder:

```txt
¿Que subsistemas se quieren simplificar?
¿Quien esta usando demasiados detalles internos?
¿El flujo se repite en varios lugares?
¿La fachada reduciria acoplamiento real?
¿La fachada tendria una responsabilidad clara?
¿Existe ya una entrada equivalente en el proyecto?
¿Una llamada directa alcanza?
```

Si la fachada no simplifica un uso real, no hace falta.

---

## Estructura conceptual

Una estructura simple puede ser:

```txt
Cliente
→ llama a Facade

Facade
→ coordina llamadas necesarias

Subsistemas
→ ejecutan responsabilidades reales
```

La fachada debe coordinar acceso.

No debe absorber la logica principal de todos los subsistemas.

---

## Ejemplo conceptual breve

Sin Facade:

```txt
UI de construccion
→ consulta recursos
→ valida terreno
→ consulta inventario
→ crea estructura
→ actualiza mision
→ dispara feedback
```

Problema:

```txt
La UI conoce demasiados detalles.
El flujo puede duplicarse.
Cambiar un paso interno rompe varios lugares.
```

Con Facade:

```txt
UI de construccion
→ solicita construir a ConstructionFacade

ConstructionFacade
→ coordina validaciones y sistemas necesarios
```

La UI pide una accion de alto nivel sin conocer todos los detalles internos.

---

## Como debe usarlo una IA

Una IA debe usar Facade cuando detecta que un sistema externo esta coordinando demasiados detalles internos.

Debe razonar asi:

```txt
Hay demasiadas dependencias externas
→ identifico el flujo comun
→ reviso si ya existe una entrada
→ propongo una fachada solo si simplifica
```

Antes de implementar, debe presentar:

```txt
Flujo complejo detectado
Sistemas involucrados
Cliente que conoce demasiado
Responsabilidad propuesta para la Facade
Alternativa simple
Riesgos
Validacion esperada
```

---

## Como NO debe usarlo una IA

Una IA no debe usar Facade como forma de tapar desorden.

No debe:

- crear una fachada para cualquier sistema,
- meter toda la logica dentro de la fachada,
- convertirla en manager global,
- esconder dependencias importantes,
- crear una fachada que solo reenvia metodos sin aportar claridad,
- usarla para evitar ordenar responsabilidades reales,
- crear una nueva entrada si ya existe una compatible.

Ejemplo de mal uso:

```txt
Problema:
Hay una clase con responsabilidades mezcladas.

Mala decision:
Crear GameFacade y mover todo ahi.

Motivo:
No se soluciono el problema. Solo se movio el desorden.
```

---

## Reutilizacion antes que invencion

Si ya existe un sistema central que coordina ese flujo, la IA debe analizar si puede extenderlo antes de crear una Facade nueva.

```txt
Primero revisar entrada existente.
Despues decidir si hace falta una fachada.
```

---

## Senales de que Facade puede servir

Puede valer la pena analizar Facade si:

- una clase externa conoce muchos subsistemas,
- varias partes repiten el mismo flujo,
- usar un sistema requiere demasiados pasos,
- los detalles internos se filtraron hacia UI o input,
- una integracion simple se volvio dificil de leer.

---

## Senales de Facade mal aplicada

Facade probablemente esta mal aplicada si:

- absorbe toda la logica,
- se convierte en clase gigante,
- no reduce complejidad real,
- oculta errores de arquitectura,
- duplica responsabilidades,
- nadie sabe si llamar a la fachada o al subsistema,
- agrega una capa sin beneficio claro.

---

## Preguntas antes de implementar

```txt
¿Que flujo quiero simplificar?
¿Quien lo usa?
¿Que subsistemas participan?
¿Que detalle interno quiero ocultar?
¿Que responsabilidad tendria la Facade?
¿Hay algo existente que ya cumple esta funcion?
¿Como se valida que simplifico y no complique?
```

---

## Formato de propuesta esperado

```txt
Patron:
Facade

Flujo a simplificar:
...

Sistemas involucrados:
...

Problema actual:
...

Por que aplica:
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

Aplicar bien Facade deberia permitir:

- simplificar el uso de sistemas complejos,
- reducir acoplamiento externo,
- evitar duplicacion de flujos,
- proteger detalles internos,
- mejorar legibilidad,
- facilitar integraciones.

---

## Regla final

```txt
Facade no existe para esconder desorden.
Existe para ofrecer una entrada clara hacia una complejidad real.
```
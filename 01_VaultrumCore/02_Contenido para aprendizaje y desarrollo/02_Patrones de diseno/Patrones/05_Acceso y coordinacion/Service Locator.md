## Definicion

Service Locator es un patron que centraliza la forma de encontrar servicios o dependencias.

```txt
Cliente
→ pide servicio al locator
→ recibe implementacion registrada
```

---

## Idea central

Service Locator ofrece acceso controlado a servicios comunes.

El riesgo es que puede ocultar dependencias si se usa sin criterio.

---

## Que problema resuelve

Service Locator ayuda cuando varios sistemas necesitan acceder a servicios comunes sin crear referencias manuales en todos lados.

Problemas posibles:

- muchas referencias repetidas,
- servicios compartidos dificiles de ubicar,
- necesidad de registrar implementaciones,
- acceso controlado a sistemas comunes,
- reemplazo de servicios en ciertos contextos.

---

## Cuando conviene usarlo

Conviene considerar Service Locator cuando:

- hay servicios compartidos,
- el acceso necesita centralizarse,
- se quiere registrar o reemplazar servicios,
- las dependencias estan controladas,
- no se quiere crear un Singleton por cada servicio,
- el proyecto ya usa este enfoque.

Ejemplos posibles:

```txt
servicio de audio
servicio de guardado
servicio de analytics
servicio de input
servicio de localizacion
servicio de economia
```

---

## Cuando NO conviene usarlo

No conviene usar Service Locator si:

- se usa solo para evitar pasar referencias,
- oculta dependencias importantes,
- cualquier clase puede pedir cualquier cosa,
- vuelve dificil saber que necesita cada sistema,
- reemplaza arquitectura clara,
- genera acceso global descontrolado.

---

## Como decidir si aplica

Antes de proponer Service Locator, la IA debe responder:

```txt
¿Que servicios se necesitan localizar?
¿Quienes los usan?
¿Las dependencias quedarian ocultas?
¿Existe una forma mas explicita?
¿El proyecto ya usa locator?
¿Hay necesidad de reemplazar implementaciones?
¿El acceso centralizado esta justificado?
```

---

## Estructura conceptual

```txt
ServiceLocator
→ registra servicios
→ entrega servicios

Cliente
→ solicita servicio
→ usa servicio
```

El registro y el ciclo de vida deben ser claros.

---

## Ejemplo conceptual breve

Uso posible:

```txt
AudioService
SaveService
InputService

ServiceLocator
→ registra servicios disponibles
```

Un sistema puede pedir un servicio sin conocer su implementacion concreta.

Problema si se abusa:

```txt
Cualquier clase pide cualquier servicio.
Las dependencias desaparecen del constructor o inspector.
El flujo se vuelve dificil de rastrear.
```

---

## Como debe usarlo una IA

Una IA debe tratar Service Locator con cuidado.

Debe razonar asi:

```txt
Hay servicios compartidos
→ reviso si acceso centralizado aporta valor
→ reviso riesgo de dependencias ocultas
→ reviso si ya existe mecanismo
```

Antes de implementar, debe presentar:

```txt
Servicios involucrados
Clientes
Motivo para localizar
Alternativa explicita
Riesgos
Validacion esperada
```

---

## Como NO debe usarlo una IA

Una IA no debe usar Service Locator como acceso global a todo.

No debe:

- registrar cualquier objeto,
- ocultar dependencias por comodidad,
- reemplazar referencias claras sin motivo,
- crear un locator si no hay servicios reales,
- duplicar Singletons o managers existentes,
- permitir que cualquier sistema pida cualquier cosa sin control,
- usarlo para evitar diseñar dependencias.

Ejemplo de mal uso:

```txt
Problema:
Un componente necesita una referencia clara a su sistema padre.

Mala decision:
Pedirlo al Service Locator.

Motivo:
La dependencia deberia ser explicita, no global.
```

---

## Reutilizacion antes que invencion

Si el proyecto ya tiene managers, singletons, inyeccion manual o un locator, la IA debe revisar ese flujo antes de crear uno nuevo.

---

## Senales de que Service Locator puede servir

Puede valer la pena analizar Service Locator si:

- hay servicios compartidos y reemplazables,
- se necesita registrar implementaciones,
- el proyecto ya tiene arquitectura de servicios,
- pasar referencias manuales genera ruido real,
- se quiere evitar multiples accesos globales independientes.

---

## Senales de Service Locator mal aplicado

Service Locator probablemente esta mal aplicado si:

- las dependencias son invisibles,
- todo se pide desde cualquier lado,
- se vuelve dificil testear,
- se usa como Singleton disfrazado,
- registra objetos que no son servicios,
- no hay control de ciclo de vida,
- nadie sabe que sistema depende de que.

---

## Preguntas antes de implementar

```txt
¿Que servicio se quiere localizar?
¿Quien lo necesita?
¿Debe ser reemplazable?
¿Como se registra?
¿Como se controla ciclo de vida?
¿Hay alternativa mas explicita?
¿Como se valida?
```

---

## Formato de propuesta esperado

```txt
Patron:
Service Locator

Servicios:
...

Clientes:
...

Motivo:
...

Alternativa explicita:
...

Riesgos:
...

Validacion:
...
```

---

## Resultado esperado

Aplicar bien Service Locator deberia permitir:

- centralizar acceso a servicios,
- controlar registro de dependencias,
- evitar accesos globales dispersos,
- reemplazar implementaciones cuando corresponda,
- mantener servicios compartidos ordenados.

---

## Regla final

```txt
Service Locator no existe para esconder dependencias.
Existe para localizar servicios compartidos cuando el acceso centralizado esta realmente justificado.
```
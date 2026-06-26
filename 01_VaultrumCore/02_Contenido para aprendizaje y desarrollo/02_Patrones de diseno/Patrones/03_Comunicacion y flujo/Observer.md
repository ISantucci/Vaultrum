## Definicion

Observer es un patron que permite que un objeto notifique cambios a otros sin conocer directamente quienes reaccionan.

```txt
Sujeto
→ emite cambio

Observadores
→ reaccionan
```

---

## Idea central

Observer separa quien produce un evento de quienes lo escuchan.

```txt
Cambio ocurrido
→ notificacion
→ sistemas interesados reaccionan
```

El objetivo es evitar dependencias directas innecesarias entre sistemas.

---

## Que problema resuelve

Observer ayuda cuando varios sistemas necesitan reaccionar a un mismo cambio.

Problemas comunes:

- un sistema llama directamente a muchos otros,
- la UI depende demasiado de gameplay,
- sistemas quedan acoplados por eventos,
- agregar una reaccion nueva obliga a modificar el emisor,
- el emisor conoce detalles de quienes escuchan.

---

## Cuando conviene usarlo

Conviene considerar Observer cuando:

- varios sistemas reaccionan al mismo cambio,
- el emisor no deberia conocer receptores,
- se necesita desacoplar gameplay y UI,
- se quiere agregar reacciones sin modificar el emisor,
- hay eventos claros de dominio.

Ejemplos posibles:

```txt
vida cambio
monedas cambiaron
mision completada
enemigo murio
torre mejorada
oleada iniciada
item recogido
```

---

## Cuando NO conviene usarlo

No conviene usar Observer si:

- solo hay una llamada simple,
- el flujo directo es mas claro,
- el evento oculta demasiado el comportamiento,
- se vuelve dificil saber quien escucha,
- hay riesgo de suscripciones olvidadas,
- se usa para todo sin criterio.

---

## Como decidir si aplica

Antes de proponer Observer, la IA debe responder:

```txt
¿Que cambio se quiere notificar?
¿Quien lo emite?
¿Quienes necesitan reaccionar?
¿El emisor deberia conocerlos?
¿Hay mas de un receptor?
¿Una llamada directa alcanza?
¿Existe un sistema de eventos ya usado?
```

---

## Estructura conceptual

```txt
Subject
→ mantiene observadores
→ notifica cambios

Observer
→ recibe notificacion
→ reacciona
```

En Unity puede implementarse con eventos de C#, UnityEvents u otro mecanismo existente.

---

## Ejemplo conceptual breve

Sin Observer:

```txt
PlayerHealth
→ actualiza barra de vida
→ reproduce sonido
→ avisa al GameManager
→ actualiza log
```

Problema:

```txt
PlayerHealth conoce demasiados sistemas.
```

Con Observer:

```txt
PlayerHealth
→ emite OnHealthChanged

UI, audio, game flow
→ escuchan y reaccionan
```

---

## Como debe usarlo una IA

Una IA debe considerar Observer cuando detecta que un sistema esta notificando manualmente a muchos otros.

Debe razonar asi:

```txt
Hay un cambio
→ reviso quienes reaccionan
→ reviso si el emisor debe conocerlos
→ uso mecanismo existente si existe
```

Antes de implementar, debe presentar:

```txt
Evento detectado
Emisor
Receptores
Motivo para desacoplar
Mecanismo existente
Riesgos
Validacion esperada
```

---

## Como NO debe usarlo una IA

Una IA no debe usar Observer para ocultar todo flujo.

No debe:

- convertir cada llamada en evento,
- crear eventos dificiles de rastrear,
- ignorar suscripciones y desuscripciones,
- duplicar sistemas de eventos,
- usar Observer si una llamada directa es mas clara,
- hacer que el orden de ejecucion sea impredecible,
- emitir eventos demasiado genericos.

Ejemplo de mal uso:

```txt
Problema:
Un boton llama a una funcion local simple.

Mala decision:
Crear evento global para eso.

Motivo:
No hay desacoplamiento necesario ni multiples interesados.
```

---

## Reutilizacion antes que invencion

Si el proyecto ya usa un sistema de eventos, la IA debe revisar si corresponde integrarse ahi antes de crear otro flujo.

---

## Senales de que Observer puede servir

Puede valer la pena analizar Observer si:

- un sistema llama a muchos otros,
- hay UI reaccionando a gameplay,
- hay varios interesados en un cambio,
- agregar reacciones modifica el emisor,
- el emisor conoce demasiados detalles externos.

---

## Senales de Observer mal aplicado

Observer probablemente esta mal aplicado si:

- nadie sabe quien escucha,
- los eventos son demasiado genericos,
- hay listeners que nunca se desuscriben,
- el orden importa pero no esta controlado,
- se usa para ocultar dependencias,
- se crean eventos para todo.

---

## Preguntas antes de implementar

```txt
¿Que evento existe?
¿Quien lo emite?
¿Quien lo escucha?
¿Hace falta desacoplar?
¿Como se suscriben y desuscriben?
¿Existe sistema de eventos?
¿Como se valida?
```

---

## Formato de propuesta esperado

```txt
Patron:
Observer

Evento:
...

Emisor:
...

Observadores:
...

Problema actual:
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

Aplicar bien Observer deberia permitir:

- desacoplar sistemas,
- agregar reacciones sin modificar emisor,
- separar UI de logica,
- reducir dependencias directas,
- mejorar extensibilidad controlada.

---

## Regla final

```txt
Observer no existe para ocultar llamadas.
Existe para notificar cambios reales sin acoplar al emisor con todos los interesados.
```
## Definicion

Un trade-off es el recurso que se gasta para ahorrar otro.

Toda optimizacion intercambia algo: optimizar no es eliminar costo, es moverlo hacia donde molesta menos.

Por eso el trade-off es un paso obligatorio de la metodologia, no un comentario al final.

```txt
Sintoma
→ hipotesis
→ medicion
→ diagnostico
→ solucion
→ trade-off
→ nueva medicion
→ validacion
```

El criterio central de esta nota es:

```txt
Una optimizacion que no declara que gasta
no esta terminada de pensar.
```

---

## Responsabilidad de esta nota

Esta nota no existe para desalentar la optimizacion.

Esta nota no existe para elegir cual intercambio es el correcto.

Esta nota no existe para listar tecnicas.

Esta nota no existe para reemplazar la medicion posterior.

Existe para obligar a nombrar el precio de cada solucion antes de aplicarla.

Su responsabilidad es ayudar a responder:

```txt
Esta solucion baja el costo aca.
¿Donde lo sube?
```

---

## Que problema ayuda a entender

Ayuda a entender por que una optimizacion puede mejorar un numero y empeorar el juego: la CPU baja, la memoria sube, el frame time queda igual y la carga se alarga.

Si solo se mira el numero que se queria bajar, ese resultado se reporta como exito.

Tambien ayuda a entender por que dos equipos pueden decidir al reves y los dos tener razon: con memoria abundante conviene precalcular, y con memoria limitada conviene recalcular.

El intercambio es el mismo. El presupuesto es distinto.

```txt
No hay soluciones universalmente correctas.
Hay soluciones correctas para un presupuesto.
```

---

## Como funciona

Los seis intercambios que aparecen con mas frecuencia son:

```txt
1. CPU ↔ Memoria
2. CPU ↔ GPU
3. Calidad ↔ GPU
4. Precision ↔ CPU
5. Loading ↔ Memoria
6. Complejidad ↔ Performance
```

CPU contra memoria: caching, pooling y precomputacion gastan memoria para ahorrar CPU.

CPU contra GPU: algunas estrategias no eliminan trabajo, lo mueven de un procesador al otro. Por eso no alcanza con decir que la CPU bajo; hay que mirar el frame completo.

Calidad contra GPU:

```txt
Sombras
Resolucion
LOD
Post processing
Iluminacion
→ intercambian fidelidad visual por tiempo de GPU
```

Precision contra CPU:

```txt
Timestep de fisica
Frecuencia de IA, pathfinding y sensores
→ intercambian exactitud por tiempo de CPU
```

Loading contra memoria: precargar mejora las transiciones y aumenta la memoria residente.

Y el sexto, que casi nunca se cuenta:

```txt
Complejidad ↔ Performance

Una solucion sofisticada puede ganar rendimiento
y aumentar bugs, onboarding, mantenimiento
y tiempo de desarrollo
```

Ese costo no aparece en el profiler, pero se paga igual durante meses: el costo de runtime es visible y medible, el de complejidad es invisible y acumulativo.

---

## Como aplicarlo en videojuegos

Ejemplo inspirado en Tower Defense.

Sintoma:

```txt
Spikes cuando las torres disparan mucho.
Medicion: Instantiate y Destroy de proyectiles.
Solucion candidata: object pool.
```

Trade-off declarado:

```txt
Se gana
→ menos allocations
→ menos picos de recoleccion

Se gasta
→ memoria residente permanente
→ logica de reset por proyectil
→ lifecycle mas complejo
```

Un pool enorme resuelve un problema de CPU y crea uno de memoria.

Otro caso del mismo juego:

```txt
Las oleadas grandes bajan el frame por targeting.
Solucion candidata: reevaluar objetivo 10 veces por segundo.
```

Trade-off declarado:

```txt
Se gana
→ menos evaluaciones por segundo

Se gasta
→ hasta 100 ms de latencia para cambiar de objetivo
→ torres que siguen apuntando a un enemigo ya muerto
```

Ahi el precio no es memoria. Es precision percibida.

La forma correcta de escribir cada decision es siempre la misma:

```txt
Se gana: ...
Se gasta: ...
Se acepta porque: ...
```

Criterio consolidado en Capsule Survivor.

---

## Como guia el diagnostico

El trade-off no orienta la busqueda de la causa. El diagnostico dice donde esta el costo; el trade-off dice cual solucion conviene pagar.

Cuando hay varias soluciones candidatas, se comparan por lo que gastan.

```txt
Solucion A
→ gana 3 ms
→ gasta 40 MB

Solucion B
→ gana 2,5 ms
→ gasta 20 lineas de complejidad

Solucion C
→ gana 3 ms
→ gasta calidad visual perceptible
```

Flujo recomendado:

```txt
Causa confirmada
→ listar soluciones posibles
→ declarar que gana y que gasta cada una
→ comparar contra el presupuesto real de la plataforma
→ elegir
→ medir de nuevo, incluido el recurso que se gasto
```

Ese ultimo paso es el que mas se saltea: se mide lo que se queria bajar y no lo que se acepto subir.

---

## Cuando conviene consultarlo

Conviene declarar trade-offs cuando:

```txt
Hay que elegir entre varias soluciones.
Una optimizacion se va a incorporar de forma permanente.
La solucion agrega un sistema nuevo.
La solucion toca calidad visual o feedback.
El proyecto tiene plataformas con presupuestos distintos.
```

Tambien conviene consultarlo cuando una IA propone una optimizacion sin mencionar costo, como cachear todo sin hablar de invalidacion, memoria ni datos obsoletos.

Una propuesta sin trade-off declarado esta incompleta, aunque la tecnica sea correcta.

---

## Cuando NO conviene forzarlo

No conviene convertir el trade-off en una excusa para no optimizar: "todo tiene un costo" no es un argumento para dejar el frame en 40 ms.

Declarar el precio sirve para pagarlo con criterio, no para esquivar la decision.

Tampoco conviene documentar intercambios en cambios triviales y reversibles, como sacar un log de un Update.

Ahi no hay nada que intercambiar. Es trabajo eliminado.

Tampoco conviene decidir sobre presupuestos imaginarios: sin conocer la plataforma objetivo, "gastar memoria no importa" no es una decision sino una suposicion.

---

## Errores que ayuda a evitar

Pensar en trade-offs ayuda a evitar:

- Reportar una mejora mirando un solo contador.
- Aplicar pooling sin contar la memoria residente.
- Cachear sin resolver invalidacion ni datos obsoletos.
- Mover trabajo de CPU a GPU en un juego ya limitado por GPU.
- Bajar precision hasta romper comportamiento de gameplay.
- Precargar todo y provocar problemas de memoria.
- Olvidar que mantenimiento y bugs tambien son costo.

La idea clave es:

```txt
Toda optimizacion gasta algo.
Si no se sabe que gasta, todavia no se entendio.
```

---

## Riesgos de interpretarlo mal

Un riesgo comun es creer que un intercambio favorable lo es siempre: cambiar memoria por CPU puede ser excelente en PC y un problema en mobile.

El mismo intercambio cambia de signo segun la plataforma.

Otro riesgo es no notar que el cuello de botella se traslado.

```txt
Antes:
CPU = 20 ms
GPU = 12 ms

Despues:
CPU = 10 ms
GPU = 12 ms
```

El frame mejoro, pero ahora limita la GPU.

Eso no significa que la optimizacion fallo. Significa que hay un cuello nuevo y hay que volver a medir.

Otro riesgo es subestimar el sexto intercambio: una solucion que gana 0,3 ms y agrega un subsistema que nadie mas entiende.

Una optimizacion que ahorra una cantidad despreciable y destruye mantenibilidad normalmente es mala ingenieria.

Otro riesgo es no validar la experiencia: profiler mejor, gameplay peor.

Un buen resultado de profiler no justifica romper feedback, comportamiento ni estabilidad.

---

## Hacia donde seguir

Esta nota pertenece a Fundamentos.

Si hace falta saber contra que presupuesto se compara:

```txt
→ Frame Budget
→ Frame time y estabilidad
```

Si hay soluciones que eliminan trabajo en vez de moverlo:

```txt
→ Reducir trabajo antes que acelerarlo
```

Si el intercambio toca lo que percibe el jugador:

```txt
→ Valor perceptual por costo
```

Si hace falta medir el recurso que se acepto gastar:

→ [[Diagnostico]]

Si se paga en tiempo de logica o simulacion:

→ [[CPU]]

Si se paga en calidad visual o tiempo grafico:

→ [[GPU]]

Si se paga en memoria residente:

→ [[Memoria]]

Si se paga en tiempos de carga:

→ [[Carga e IO]]

Si se paga en claridad de interfaz:

→ [[UI]]

Si hace falta el patron y su costo tipico:

→ [[Patrones transversales]]

---

## Checklist de diagnostico

Antes de dar una optimizacion por terminada, revisar:

```txt
¿Que recurso se ahorra?
¿Que recurso se gasta?
¿Cuanto se gasta, en numeros?
¿Ese gasto entra en el presupuesto de la plataforma objetivo?
¿El cuello de botella se traslado a otro recurso?
¿Se midio tambien el recurso que subio?
¿La solucion agrega complejidad permanente?
¿Alguien mas del equipo va a poder mantenerla?
¿El jugador percibe lo que se sacrifico?
¿El trade-off quedo escrito junto a la decision?
```

---

## Regla final

Una optimizacion no se describe por lo que mejora.

Se describe por lo que mejora y por lo que cuesta.

```txt
Se gana: ...
Se gasta: ...
Se acepta porque: ...

Si falta alguna de las tres lineas, la decision no esta cerrada.
```

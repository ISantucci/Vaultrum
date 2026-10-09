## Definicion

Valor perceptual por costo es el criterio que relaciona lo que un sistema consume con lo que el jugador percibe de el.

```txt
Costo computacional
vs
Valor perceptual
```

De ese cruce salen cuatro situaciones:

```txt
Barato y muy percibido
→ se conserva

Caro y muy percibido
→ se optimiza sin perder la informacion

Barato y apenas percibido
→ no es prioridad

Caro y apenas percibido
→ candidato fuerte a optimizacion
```

El criterio ordena por relacion, no por costo absoluto: un sistema caro no es automaticamente un problema, ni uno barato es automaticamente seguro.

```txt
La pregunta no es "¿cuanto cuesta?".
La pregunta es "¿cuanto cuesta en relacion con lo que aporta?".
```

---

## Responsabilidad de esta nota

Esta nota no existe para medir costos.

Esta nota no existe para elegir tecnicas de optimizacion.

Esta nota no existe para reemplazar el diagnostico.

Existe para meter al jugador dentro de la decision tecnica, de modo que la prioridad no se defina solo por milisegundos.

Su responsabilidad es ayudar a responder:

```txt
De todo lo que cuesta caro,
¿que es lo que el jugador menos va a extrañar?
```

---

## Que problema ayuda a entender

La finalidad de la performance es sostener la experiencia, no conseguir numeros bonitos.

Una optimizacion que mejora el frame y arruina el feedback no cumplio su funcion.

```txt
Se gana: +20% de performance
Se pierde: el jugador ya no entiende si pego
```

Eso no es una optimizacion exitosa con un efecto lateral: es una implementacion incorrecta.

Tambien ayuda a entender por que dos sistemas con el mismo costo no tienen la misma prioridad.

```txt
Sistema A: 3 ms, el jugador lo mira en cada disparo.
Sistema B: 3 ms, ocurre detras de la camara.
```

El costo es identico. La decision no.

---

## Como funciona

El caso de referencia es el de las particulas de impacto, cuando la medicion confirma que son costosas.

La solucion pobre es eliminarlas.

El costo baja de inmediato y el jugador pierde feedback: deja de recibir la informacion de que su disparo conecto.

Lo que se elimino no era un efecto visual. Era una respuesta del juego a una accion del jugador.

Proceso correcto:

```txt
medir el costo
↓
identificar la causa
↓
reducir cantidad / tamaño / lifetime / complejidad
↓
mantener la informacion perceptual
```

Un camino pregunta "¿cuanto cuesta?". El otro pregunta "¿que parte de esto es la que comunica?".

```txt
Efecto de impacto
= cantidad de particulas
+ tamaño
+ duracion
+ shader
+ el hecho de que aparezca al impactar
```

Los primeros cuatro son costo negociable. El ultimo es la informacion, y no se negocia.

```txt
Se puede reducir el efecto.
No se puede borrar la respuesta.
```

El mismo razonamiento se aplica al reves: con un sistema muy caro que el jugador nunca mira, conviene ser agresivo.

---

## Como aplicarlo en videojuegos

Ejemplo inspirado en Tower Defense.

Sintoma: el frame se cae cuando muchas torres impactan a la vez, y la medicion apunta al fill rate de las particulas de impacto.

Camino incorrecto:

```csharp
// Camino pobre: se apaga el feedback
impactVfx.SetActive(false);
```

Camino correcto:

```csharp
// Se conserva el evento perceptual, se reduce el costo
var emission = impactVfx.emission;
emission.rateOverTime = 8;      // antes 40

var main = impactVfx.main;
main.startLifetime = 0.25f;      // antes 1.2f
main.startSize = 0.4f;           // antes 1.0f
```

El impacto sigue existiendo y cuesta una fraccion.

El mismo juego, ordenado por valor perceptual:

```txt
HUD de vida
→ barato y consultado constantemente
→ se conserva

Feedback de impacto
→ el jugador lo necesita para leer el combate
→ se optimiza, no se elimina

Particulas ambientales de fondo
→ el jugador nunca las mira en una oleada
→ candidato fuerte

Animacion detallada fuera de camara
→ valor perceptual nulo
→ se apaga sin discusion
```

La lista no se ordena por milisegundos, sino por milisegundos divididos por atencion del jugador.

---

## Como guia el diagnostico

Este criterio entra despues de la medicion y antes de elegir la solucion: la medicion dice que sistemas son caros y el valor perceptual dice en que orden conviene tocarlos.

Preguntas utiles frente a cada sistema caro:

```txt
¿El jugador nota este sistema?
¿Que informacion le da?
¿Hay otra fuente que le de lo mismo?
¿Que pasa si se reduce a la mitad?
¿En que momento del juego lo mira?
```

Flujo recomendado:

```txt
Sistemas caros identificados
→ estimar el valor perceptual de cada uno
→ empezar por caro y poco percibido
→ reducir parametros antes que eliminar
→ validar frame y experiencia
```

Las dos ultimas lineas son validaciones distintas: la tecnica confirma que el frame mejoro, la perceptual confirma que el juego sigue comunicando lo mismo.

Sin la segunda, la optimizacion no esta cerrada.

---

## Cuando conviene consultarlo

Conviene aplicar este criterio cuando:

```txt
Hay varios sistemas caros y hay que priorizar.
La solucion propuesta implica sacar algo visible.
El costo esta en efectos, particulas, audio o UI.
Hay que recortar para llegar a una plataforma mas debil.
La optimizacion toca feedback de combate.
```

Tambien conviene consultarlo cuando una IA propone desactivar un efecto.

```txt
La IA propone apagar las particulas.
No pregunto que le comunicaban al jugador.
```

Eliminar es lo mas barato de escribir y lo mas caro de revertir.

---

## Cuando NO conviene forzarlo

No conviene usar valor perceptual para defender cualquier efecto costoso: "se ve lindo" no es un presupuesto.

Si el frame no cierra, algo se recorta: el criterio ayuda a elegir que, no a evitarlo.

Tampoco conviene aplicarlo sin medicion previa: un sistema que parece caro puede no estar en el bottleneck.

Recortar calidad de algo que no limitaba el frame empeora el juego sin ganar nada.

Tampoco conviene tratar el juicio perceptual como opinion individual: la percepcion se valida jugando y observando, no discutiendo.

---

## Errores que ayuda a evitar

Pensar en valor perceptual por costo ayuda a evitar:

- Eliminar feedback en lugar de reducir su costo.
- Optimizar primero lo mas visible del juego.
- Recortar efectos que el jugador usa para leer el combate.
- Conservar sistemas caros que nadie percibe.
- Confundir efecto visual con informacion de gameplay.

La idea clave es:

```txt
Se puede reducir la forma.
No se puede borrar el mensaje.
```

---

## Riesgos de interpretarlo mal

Un riesgo comun es usar el criterio para bloquear toda optimizacion visual.

Si todo aporta al game feel y todo es imprescindible, no hay decision posible y el frame no mejora.

Otro riesgo es el opuesto: tratar cualquier sistema caro como prescindible. Ese atajo produce juegos rapidos que se sienten muertos.

Otro riesgo es evaluar la percepcion en el editor, con la escena pausada y sin combate.

El valor perceptual se juzga en la situacion real de juego, con el jugador ocupado en otra cosa.

Otro riesgo es olvidar el audio y la UI: si se recorta la particula y queda el sonido, el impacto todavia se lee.

La informacion perceptual esta repartida entre varios canales, y antes de recortar uno conviene saber cuales sostienen el mensaje.

---

## Hacia donde seguir

Esta nota pertenece a Fundamentos.

Si hace falta saber cuanto margen hay disponible:

```txt
→ Frame Budget
→ Frame time y estabilidad
```

Si hace falta declarar que se sacrifica:

```txt
→ Trade-offs de optimizacion
```

Si hace falta reducir en vez de eliminar:

```txt
→ Reducir trabajo antes que acelerarlo
```

Si hace falta confirmar que ese sistema era el costoso:

→ [[Diagnostico]]

Si el costo viene de simulacion, IA o animacion:

→ [[CPU]]

Si viene de particulas, transparencias o efectos:

→ [[GPU]]

Si el recorte se paga en memoria residente:

→ [[Memoria]]

Si afecta lo que se precarga:

→ [[Carga e IO]]

Si el feedback afectado vive en la UI:

→ [[UI]]

Si hace falta un patron para escalar detalle:

→ [[Patrones transversales]]

---

## Checklist de diagnostico

Antes de recortar algo que el jugador ve, revisar:

```txt
¿Ese sistema aparece en la medicion como costoso?
¿Cuanto cuesta, en ms?
¿Que informacion le comunica al jugador?
¿En que momento la necesita?
¿Hay otro canal que comunique lo mismo?
¿Se puede reducir cantidad, tamaño, duracion o complejidad?
¿Cuanto se ahorra reduciendo en vez de eliminando?
¿Se probo jugando, no solo mirando?
¿El juego sigue comunicando lo mismo despues del cambio?
¿El frame mejoro lo suficiente como para justificar la perdida?
```

---

## Regla final

La performance existe para sostener la experiencia, no para reemplazarla.

```txt
Barato y percibido: se queda.
Caro y percibido: se reduce, no se borra.
Caro y no percibido: ahi se empieza.
```

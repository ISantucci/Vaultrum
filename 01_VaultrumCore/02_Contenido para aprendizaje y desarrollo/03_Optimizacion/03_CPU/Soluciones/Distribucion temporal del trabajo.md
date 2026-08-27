## Definicion

Distribucion temporal del trabajo consiste en repartir entre varios frames un conjunto de operaciones que podrian resolverse todas en el mismo frame.

La idea principal es:

```txt
No siempre se puede hacer menos trabajo.
A veces se puede hacer el mismo trabajo mejor repartido.
```

Si 300 agentes realizan una operacion costosa por segundo, hay una diferencia entre:

```txt
Frame X:
300 agentes
```

y:

```txt
Frame X:    50
Frame X+1:  50
Frame X+2:  50
Frame X+3:  50
Frame X+4:  50
Frame X+5:  50
```

El trabajo total puede seguir siendo el mismo. Los spikes desaparecen.

Esto introduce una distincion fundamental:

```txt
Optimizar no siempre significa reducir trabajo total.
Tambien puede significar distribuirlo mejor en el tiempo.
```

---

## Que problema ayuda a prevenir

Ayuda con:

```txt
Spikes de frame time
Stutter al aparecer una oleada
Muchos update activos
Fisica costosa
IA que piensa de mas
Pathfinding recalculado demasiado seguido
Freezes por trabajo de carga sincronico
```

No ataca el costo total. Ataca la concentracion.

```txt
El problema no es cuanto cuesta.
Es que todo cuesta en el mismo frame.
```

Un promedio sano puede convivir con frames rotos:

```txt
16 ms
16 ms
16 ms
72 ms
16 ms
```

Ese frame de 72 ms se percibe como tiron aunque el promedio parezca correcto.

---

## Como funciona

El trabajo se corta en porciones y se reparte por frames o por grupos.

Formas habituales:

```txt
Por grupos: el conjunto se divide en N grupos y cada frame corre uno.
Por indice: el agente actua cuando su indice coincide con el frame.
Por presupuesto: se procesa hasta agotar una cantidad o un tiempo por frame.
Por cola: se encolan pedidos y se atienden de a poco.
```

Version concentrada:

```csharp
private void OnWaveStart()
{
    for (int i = 0; i < agents.Count; i++)
    {
        agents[i].RecalculatePath();
    }
}
```

Version distribuida:

```csharp
private int cursor;

private void Tick()
{
    int budget = Mathf.Min(agentsPerFrame, agents.Count);

    for (int i = 0; i < budget; i++)
    {
        agents[cursor].RecalculatePath();
        cursor = (cursor + 1) % agents.Count;
    }
}
```

El algoritmo no cambio. Cambio cuando corre cada parte.

---

## Como aplicarlo en videojuegos

Sistemas candidatos:

```txt
Recalculo de rutas.
Percepcion de NPC.
Busqueda de objetivos.
Sensores de evasion.
Actualizacion de agentes lejanos.
Instanciacion o activacion de entidades.
Preparacion de datos al entrar a una escena.
```

En Tower Defense:

```txt
Oleada de 300 enemigos
→ activarlos repartidos en varios frames.

Torres
→ evaluar objetivo por grupos, no todas el mismo frame.

Enemigos
→ recalcular ruta por turnos.

HUD de dinero, vida y wave
→ actualizar por evento.
```

Ejemplo concreto:

```txt
Antes:
al empezar la wave, los 300 enemigos piden path.

Despues:
la wave entrega paths a razon de 20 por frame.
```

El jugador ve la misma oleada. No ve el tiron.

Tambien aplica a la carga, donde el sintoma es un freeze en vez de un spike:

```txt
Operacion pesada de golpe
→ frame normal, carga, freeze, frame normal.

Operacion repartida
→ varios frames algo mas caros, sin corte.
```

---

## Relacion con arquitectura

Se relaciona con:

```txt
Update Manager
Game Loop
Frame Budget
Object Pooling
Reducir frecuencia de actualizacion
```

Distribuir es mucho mas facil cuando existe un punto central que sabe quien esta registrado.

```txt
Sistemas dispersos con Update propio
→ dificil repartir.

Sistema central con lista de agentes
→ repartir es trivial.
```

Conviene distinguirla de reducir frecuencia:

```txt
Reducir frecuencia
→ hacer la operacion menos veces.

Distribuir
→ hacerla las mismas veces, pero no todas juntas.
```

Se pueden combinar. No son lo mismo.

Tambien conviene distinguirla de precarga y carga distribuida. Las dos reparten trabajo en varios frames, las dos usan el mismo diagrama de tandas y las dos cargan la misma advertencia: distribuir no elimina trabajo. Lo que cambia es que trabajo se reparte.

```txt
Distribucion temporal del trabajo
→ trabajo recurrente de simulacion: rutas, percepcion, targeting, sensores.

Precarga y carga distribuida
→ trabajo de carga de contenido: assets, instanciacion, preparacion de escena.
```

La regla practica: si el trabajo va a volver a aparecer todos los frames mientras el sistema exista, es distribucion temporal. Si aparece una vez, al traer contenido que todavia no estaba, es carga.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
CPU
Frame Budget
Estabilidad del frame time
```

No reduce el trabajo total del sistema. Solo modifica:

```txt
cuando se realiza
durante cuanto tiempo
como afecta la experiencia
```

Tambien puede aliviar al Garbage Collector si evita que muchas allocations se concentren en el mismo instante.

---

## Cuando conviene usarlo

El disparador tipico es un evento que junta mucho trabajo en un instante.

Conviene cuando:

```txt
El costo total es aceptable pero llega concentrado.
Hay spikes visibles en el Profiler.
Muchas entidades hacen lo mismo al mismo tiempo.
El trabajo es divisible.
El resultado tolera unos frames de espera.
El disparador es puntual: spawn, wave, carga, cambio de escena.
```

Sintoma clasico que lo justifica:

```txt
Frame time promedio sano
+
picos periodicos
→
candidato a distribucion.
```

---

## Cuando NO conviene usarlo

No conviene cuando el problema es el trabajo total.

```txt
Si el sistema no entra en el frame budget ni repartido,
distribuir solo cambia la forma de la caida.
```

Tampoco conviene en sistemas que exigen respuesta inmediata:

```txt
Input del jugador.
Movimiento principal.
Deteccion de impacto.
Feedback de disparo.
Resolucion de daño en el frame en que ocurre.
```

Y no conviene cuando la coherencia entre agentes importa:

```txt
Si media oleada reacciona un frame antes que la otra
y eso se nota,
la distribucion esta mal ubicada.
```

---

## Trade-offs

Ventajas:

```txt
Frame time mas estable.
Menos spikes.
Menos stutter percibido.
Mejor escalabilidad ante picos de entidades.
```

Costos:

```txt
Latencia de reaccion.
Comportamiento desfasado entre agentes.
Mas estado que mantener: cursores, colas, indices.
Diagnostico mas dificil, porque el costo queda repartido.
El trabajo total sigue existiendo.
```

El intercambio central es:

```txt
pico de costo ↔ latencia de respuesta
```

Por eso la validacion no termina en el Profiler. Termina jugando.

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Repartir un trabajo que en realidad habia que eliminar.
Repartir tanto que la reaccion se vuelve visible.
Colas que crecen mas rapido de lo que se atienden.
Agentes que nunca reciben su turno porque el cursor no llega.
Grupos desbalanceados donde uno concentra lo caro.
Distribuir sin medir y creer que se redujo costo.
```

Ejemplo:

```txt
Percepcion repartida en 30 frames.
El Profiler mejora.
El enemigo tarda medio segundo en ver al jugador.
El combate se siente roto.
```

Este es el riesgo propio de esta solucion: no se paga en CPU, se paga en respuesta.

Hay sistemas donde ese medio segundo rompe el feeling y no hay ganancia de frame que lo justifique.

---

## Checklist de implementacion

```txt
¿Se midio que el problema es el pico y no el total?
¿El trabajo es divisible sin romper la logica?
¿Cuanta latencia tolera este sistema?
¿Cuantos elementos se procesan por frame?
¿El presupuesto por frame es fijo o adaptativo?
¿Todos los elementos reciben su turno?
¿Que pasa si la cantidad crece de golpe?
¿La cola puede crecer sin control?
¿Los grupos estan balanceados?
¿Se comparo frame time antes y despues?
¿Se valido el feeling despues del cambio?
```

---

## Regla final

Distribuir no hace desaparecer el trabajo. Lo acomoda.

```txt
Mismo costo total,
repartido en el tiempo,
se siente completamente distinto.
```

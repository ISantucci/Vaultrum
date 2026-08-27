## Definicion

Particionado espacial consiste en dividir el mundo en regiones para que un agente consulte solamente las que pueden contener candidatos relevantes.

En lugar de:

```txt
Agente
↓
comparar con todos los agentes
```

se divide el espacio y se pregunta primero donde esta cada uno.

```txt
Grid

┌─────┬─────┬─────┐
│     │ X X │     │
├─────┼─────┼─────┤
│ X   │ NPC │ X   │
├─────┼─────┼─────┤
│     │ X   │     │
└─────┴─────┴─────┘
```

El NPC consulta solo:

```txt
su celda
las celdas vecinas relevantes
```

El objetivo es reducir muchisimo la cantidad de candidatos antes de ejecutar el calculo caro.

---

## Que problema ayuda a prevenir

Ayuda con:

```txt
IA que piensa de mas
Flocking que escala mal
Busqueda de objetivos sobre listas completas
Fisica costosa por queries de area
Chequeos de distancia contra todo
```

El problema que ataca es de escala.

```txt
100 agentes
cada uno compara contra otros 100
→ 100 × 100 = 10.000 comparaciones
```

Con mas agentes:

```txt
1.000 × 1.000 = 1.000.000
```

Es el problema clasico de un comportamiento cercano a:

```txt
O(n²)
```

Optimizar una multiplicacion dentro del loop impacta mucho menos que cambiar como se buscan los vecinos.

Por eso el particionado se elige antes que la microoptimizacion, no despues.

---

## Como funciona

El mundo se divide en celdas y cada agente se registra en la celda que le corresponde.

Flujo:

```txt
El agente se mueve
↓
se actualiza su celda
↓
la consulta pide celda propia + vecinas
↓
queda un conjunto reducido de candidatos
↓
recien ahi se hace el calculo caro
```

Version ingenua:

```csharp
foreach (Boid boid in boids)
{
    foreach (Boid other in boids)
    {
        Accumulate(boid, other);
    }
}
```

Version particionada:

```csharp
foreach (Boid boid in boids)
{
    foreach (Boid neighbour in grid.QueryNeighbours(boid.Position, radius))
    {
        Accumulate(boid, neighbour);
    }
}
```

El calculo por par no cambio. Cambio cuantos pares existen.

Es una aplicacion directa del principio:

```txt
filtrar barato antes de calcular caro
```

---

## Como aplicarlo en videojuegos

Sistemas candidatos:

```txt
Flocking y separacion entre agentes.
Percepcion de NPC.
Busqueda de objetivos.
Deteccion de area y explosiones.
Spawns que evitan superposicion.
Culling logico de entidades lejanas.
```

En flocking transforma la pregunta:

```txt
¿Cuales son todos los boids?
→
¿Cuales son los boids cercanos que pueden afectarme?
```

Separation, Cohesion y Alignment no cambian. Cambia a quienes se consultan.

En Tower Defense:

```txt
30 torres × 300 enemigos
→ 9.000 comparaciones por evaluacion si se recorre todo.

Con grid:
cada torre consulta solo las celdas que cubre su rango.
```

Ejemplo:

```txt
Antes:
la torre recorre la lista completa de enemigos.

Despues:
la torre pide los enemigos de las celdas dentro de su radio.
```

El grid tampoco reemplaza a los filtros posteriores. Los alimenta:

```txt
Celdas vecinas
→ candidatos
→ distancia exacta
→ angulo
→ raycast
```

---

## Relacion con arquitectura

Se relaciona con:

```txt
Broad phase y narrow phase
Cascada de filtros
Active Set
Update Manager
Distribucion temporal del trabajo
```

Necesita un dueño claro de la estructura:

```txt
Quien crea el grid.
Quien inserta y remueve agentes.
Quien lo actualiza cuando algo se mueve.
Quien responde las consultas.
```

Repartir esa responsabilidad entre los propios agentes suele terminar mal. Conviene un sistema que administre la estructura y exponga consultas.

Tambien encaja con la separacion entre modelo y vista: la estructura vive del lado de los datos, no del GameObject.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
CPU
Frame Budget
```

Tambien toca memoria:

```txt
mas estructura residente
↔
menos comparaciones
```

Suele mejorar el comportamiento de cache, porque agrupa datos que se consultan juntos.

Pero la estructura se paga:

```txt
insercion
remocion
actualizacion por movimiento
consulta
```

---

## Cuando conviene usarlo

Conviene cuando:

```txt
Hay muchas entidades consultandose entre si.
Las consultas son por proximidad.
El costo crece de forma cuadratica con la cantidad.
Las entidades estan repartidas en el espacio.
La escena es grande respecto del radio de consulta.
Se midio que la busqueda de vecinos domina el costo.
```

Sintoma que lo justifica:

```txt
El costo por agente es razonable
+
el costo total explota al sumar agentes
→
el problema esta en la busqueda, no en la formula.
```

---

## Cuando NO conviene usarlo

No conviene con pocas entidades.

```txt
Con 20 agentes,
mantener el grid puede costar mas
de lo que ahorra recorrer la lista.
```

Tampoco conviene cuando:

```txt
El radio de consulta cubre casi toda la escena.
Todas las entidades estan amontonadas en la misma celda.
Las consultas no son espaciales.
Las entidades se mueven tanto que la estructura se rehace siempre.
La cantidad de entidades es fija, chica y conocida.
```

Si todos los candidatos caen igual en la misma celda, el particionado no filtro nada y ademas se pago.

---

## Trade-offs

Ventajas:

```txt
Muchisimas menos comparaciones.
Escalabilidad ante crecimiento de entidades.
Consultas de proximidad baratas.
Base para aplicar otros filtros despues.
```

Costos:

```txt
Estructura que hay que mantener actualizada.
Memoria adicional.
Mas complejidad de codigo.
Costo de insercion y remocion por movimiento.
Tamaño de celda que hay que elegir y ajustar.
Resultado dependiente de como esten distribuidos los agentes.
```

El intercambio central es:

```txt
costo de mantener la estructura ↔ costo de comparar contra todos
```

Elegir el tamaño de celda es parte del trade-off:

```txt
Celdas muy chicas
→ muchas celdas que consultar.

Celdas muy grandes
→ demasiados candidatos por celda.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Agentes registrados en una celda que ya no ocupan.
Agentes duplicados en varias celdas.
Olvidar removerlos al desactivarlos o devolverlos al pool.
Consultar solo la celda propia y perder vecinos del borde.
Elegir tamaño de celda sin relacion con el radio de consulta.
Introducir particionado sin haber medido que la busqueda era el cuello.
```

Ejemplo:

```txt
Grid implementado.
Se consulta unicamente la celda propia.
Dos boids a diez centimetros, en celdas distintas,
dejan de verse.
El flocking se rompe y el Profiler no avisa.
```

Un error de particionado no aparece como caida de FPS. Aparece como comportamiento raro.

---

## Checklist de implementacion

```txt
¿Se midio que la busqueda de vecinos domina el costo?
¿Cuantas entidades participan realmente?
¿Las consultas son por proximidad?
¿Que radio necesita cada consulta?
¿El tamaño de celda esta relacionado con ese radio?
¿Se consultan tambien las celdas vecinas?
¿Quien es el dueño de la estructura?
¿Cuando se inserta y cuando se remueve cada agente?
¿Que pasa al desactivar o poolear una entidad?
¿Que pasa si todos los agentes caen en la misma celda?
¿Se comparo el costo antes y despues?
¿Se valido que el comportamiento no cambio?
```

---

## Regla final

El particionado no acelera el calculo. Reduce cuantas veces hay que hacerlo.

```txt
Antes de calcular contra todos,
preguntar quien puede llegar a importar.
```

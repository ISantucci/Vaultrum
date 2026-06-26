## Definicion

Una ruta alternativa es un camino posible distinto para llegar desde un punto hacia otro dentro del mapa.

No es automaticamente mejor.

No es automaticamente peor.

No es necesariamente una ruta calculada por algoritmo.

Una ruta alternativa existe cuando el mapa ofrece mas de una posibilidad real de recorrido.

```txt
Origen
→ camino A
→ destino

Origen
→ camino B
→ destino
```

---

## Responsabilidad de esta nota

Esta nota define que son rutas alternativas dentro de reglas de mapa.

Su responsabilidad es explicar:

```txt
que representa una ruta alternativa
cuando existe realmente
que datos puede necesitar
como puede afectar decisiones espaciales
cuando conviene implementarlas
cuando no conviene implementarlas
que costo tienen
como validarlas
```

Esta nota no debe explicar todo pathfinding, A Star, Dijkstra, NPCs o movimiento.

Los sistemas consumidores deben explicar como eligen o usan esas rutas.

---

## Problema que resuelve

Las rutas alternativas resuelven el problema de que el mapa no tenga un unico recorrido posible.

Pregunta principal:

```txt
¿Existen varios caminos posibles entre puntos importantes?
```

Ejemplo:

```txt
Camino corto
→ mas peligroso

Camino largo
→ mas seguro

Camino bloqueado
→ se habilita despues
```

La ruta alternativa debe tener una razon de diseño o sistema.

---

## Que puede representar una ruta alternativa

Una ruta alternativa puede representar:

```txt
camino secundario
atajo
desvio
ruta segura
ruta peligrosa
ruta desbloqueable
ruta mas cara
ruta mas larga
ruta tactica
ruta para otro tipo de agente
```

Ejemplo:

```txt
Ruta principal
→ facil de leer

Ruta secundaria
→ mas rapida pero bloqueada al inicio
```

---

## Datos que puede necesitar

Una ruta alternativa puede necesitar:

```txt
puntos de inicio y fin
nodos o conexiones que la componen
estado disponible/bloqueado
costo
condicion de desbloqueo
tipo de ruta
restricciones de uso
debug visual
```

No todas las rutas necesitan todos estos datos.

La informacion depende del uso real.

---

## Ruta alternativa no es decision

Una ruta alternativa ofrece una posibilidad.

No decide por si misma que camino tomar.

```txt
Ruta alternativa
→ existe como opcion.

Sistema consumidor
→ decide si la usa.
```

Ejemplo:

```txt
El mapa tiene dos rutas.

El pathfinding puede elegir segun costos.

Un sistema de oleadas puede habilitar una ruta.

Un diseñador puede forzar una ruta para tutorial.
```

La ruta no debe conocer todos sus consumidores.

---

## Ruta alternativa y costo

Una ruta alternativa puede tener costos distintos.

Ejemplo:

```txt
Ruta A
→ corta
→ costo alto

Ruta B
→ larga
→ costo bajo
```

Pero una ruta alternativa no necesita costos siempre.

Si el diseño solo necesita que exista otro camino, el costo puede no ser necesario.

---

## Ruta alternativa y bloqueo

Una ruta alternativa puede estar bloqueada o disponible.

Ejemplo:

```txt
Ruta B
→ bloqueada al inicio

Evento de progreso
→ Ruta B disponible
```

Bloqueo y costo no son lo mismo.

```txt
Bloqueada
→ no se puede usar.

Cara
→ se puede usar, pero no conviene.
```

---

## Que NO debe hacer una ruta alternativa

Una ruta alternativa no debe asumir responsabilidades que no le corresponden.

No debe:

```txt
decidir comportamiento de NPC
mover entidades
calcular pathfinding completo
resolver combate
controlar estados de IA
actualizar UI por si misma
funcionar como manager global
```

Debe existir como informacion de mapa.

Los sistemas consumidores deciden.

---

## Rutas alternativas como contrato de informacion

Una ruta alternativa puede pensarse como contrato.

```txt
Yo represento un camino posible.
Puedo estar disponible o bloqueada.
Puedo tener costo.
Puedo tener condiciones.
Puedo ser consultada por otros sistemas.
```

Ese contrato permite que el mapa ofrezca opciones sin decidir por los consumidores.

---

## Ejemplo conceptual en codigo

```csharp
using System.Collections.Generic;

public class AlternativeRoute<TNode>
{
    public string Id { get; }
    public IReadOnlyList<TNode> Nodes => _nodes;
    public bool IsAvailable { get; private set; }
    public float BaseCost { get; private set; }

    private readonly List<TNode> _nodes = new();

    public AlternativeRoute(string id, IEnumerable<TNode> nodes, float baseCost = 1f)
    {
        Id = id;
        _nodes.AddRange(nodes);
        BaseCost = baseCost;
        IsAvailable = true;
    }

    public void SetAvailable(bool isAvailable)
    {
        IsAvailable = isAvailable;
    }

    public void SetBaseCost(float baseCost)
    {
        BaseCost = baseCost;
    }
}
```

Este ejemplo representa una ruta alternativa como dato.

No calcula por si misma el comportamiento.

No mueve entidades.

No decide que sistema la usa.

---

## Cuando implementar rutas alternativas

Conviene implementarlas cuando:

```txt
el mapa ofrece mas de un camino real
las rutas afectan gameplay
hay atajos
hay decisiones tacticas
hay rutas desbloqueables
hay caminos con distintos riesgos
hay caminos con distintos costos
el diseño necesita variedad o progresion
```

Ejemplo correcto:

```txt
Tower defense con una ruta principal
y una ruta secundaria que se desbloquea en cierta oleada.

→ Rutas alternativas tienen sentido.
```

---

## Cuando NO implementarlas

No conviene implementarlas cuando:

```txt
el recorrido es unico
las rutas no cambian decisiones
los caminos alternativos son decorativos
no hay sistema que los use
una ruta fija alcanza
el costo de mantenerlas no se justifica
```

Ejemplo:

```txt
Un enemigo siempre va por el mismo camino
y no existe ninguna bifurcacion real.

→ No hay ruta alternativa que modelar.
```

---

## Por que no implementarlas de mas

Agregar rutas alternativas sin necesidad puede generar:

```txt
mas datos que mantener
mas testing
mas debug
rutas que nadie usa
balance mas dificil
comportamientos inesperados
confusion en el diseño del mapa
```

Regla:

```txt
Una ruta alternativa debe cambiar algo real.
```

---

## Mala practica al implementarlas

Malas practicas comunes:

```txt
crear rutas alternativas decorativas
no definir cuando estan disponibles
no validar que conecten correctamente
no mostrar debug visual
duplicar rutas en varios sistemas
hacer que la ruta decida comportamiento
mezclar ruta alternativa con IA del NPC
usar rutas alternativas sin criterio de gameplay
```

Ejemplo de mala practica:

```txt
Crear tres rutas distintas
pero todas tienen el mismo costo,
misma distancia,
mismo riesgo
y ningun sistema las diferencia.

→ Complejidad sin valor.
```

---

## Costos de implementacion

Implementar rutas alternativas requiere:

```txt
definir puntos de conexion
definir estado disponible/bloqueado
definir condiciones si existen
definir costos si existen
validar continuidad
integrar con sistemas consumidores
debuggear rutas
probar cambios de estado
```

No es solo dibujar otro camino.

Debe estar integrado al mapa logico.

---

## Costos de optimizacion

Las rutas alternativas pueden afectar rendimiento si aumentan demasiado las opciones de busqueda.

Costos posibles:

```txt
mas nodos o conexiones
mas vecinos por nodo
mas caminos posibles a evaluar
mas recalculos cuando cambian estados
mas debug visual
mas datos en memoria
```

Problemas frecuentes:

```txt
agregar muchas conexiones innecesarias
recalcular todas las rutas cuando cambia una sola
no cachear estados de disponibilidad
debuggear todas las rutas todo el tiempo
```

---

## Criterio de optimizacion

Opciones para reducir costo:

```txt
habilitar rutas solo cuando corresponde
actualizar solo conexiones afectadas
cachear disponibilidad
limitar recalculos
separar debug de runtime
evitar rutas alternativas que no cambian decisiones
mantener conexiones claras y necesarias
```

Ejemplo:

```txt
Mala practica:
cada frame revisar si todas las rutas alternativas estan disponibles.

Mejor:
actualizar disponibilidad por evento.
```

---

## Preguntas antes de implementar

Antes de implementar rutas alternativas, una IA debe responder:

```txt
¿Existe mas de un camino real?
¿Que diferencia una ruta de otra?
¿La diferencia afecta gameplay?
¿Las rutas tienen costos?
¿Las rutas pueden bloquearse?
¿Quien habilita o deshabilita rutas?
¿Quien consume esas rutas?
¿Como se validan?
¿Que costo tecnico agregan?
```

Si no hay diferencia real, no conviene modelarlas.

---

## Validacion visual

Las rutas alternativas deben poder verse.

Se puede mostrar:

```txt
ruta principal
ruta alternativa
estado disponible/bloqueado
costo
condicion de desbloqueo
puntos de conexion
direccion
```

Esto permite detectar:

```txt
rutas cortadas
rutas duplicadas
rutas que no conectan
rutas que nunca se usan
rutas disponibles antes de tiempo
rutas bloqueadas que siguen siendo usadas
```

---

## Errores comunes

```txt
crear alternativas sin impacto
duplicar rutas en varios sistemas
no definir estado
no definir condiciones
no validar conexion
no debuggear visualmente
mezclar ruta con comportamiento
no actualizar pathfinding cuando cambia una ruta
```

---

## Criterio para una IA

Cuando una IA proponga rutas alternativas, debe justificar:

```txt
por que el mapa necesita alternativas
que diferencia cada ruta
como se representan
quien las consume
si tienen costo o bloqueo
si cambian por eventos
que costo tecnico tienen
como se validan
```

No alcanza con decir:

```txt
Agregar rutas alternativas.
```

Debe explicar que decision o experiencia mejoran.

---

## Checklist

Antes de usar rutas alternativas, revisar:

```txt
¿Hay mas de un camino real?
¿Cada ruta tiene una razon para existir?
¿Las rutas afectan decisiones?
¿Hay costos, bloqueos o condiciones?
¿Las rutas conectan correctamente?
¿Hay un sistema consumidor?
¿Se actualizan cuando cambia el mapa?
¿Se evita complejidad decorativa?
¿Se puede debuggear visualmente?
```

---

## Regla final

Una ruta alternativa no es mejor por existir.

Tiene valor si cambia una decision, una estrategia o una experiencia.

```txt
Ruta alternativa
→ opcion espacial

Sistema consumidor
→ decide si la usa
```
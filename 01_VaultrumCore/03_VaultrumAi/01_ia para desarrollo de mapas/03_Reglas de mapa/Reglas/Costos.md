## Definicion

Un costo es un valor que representa cuanto cuesta, conviene o penaliza usar una parte del mapa.

Puede aplicarse a:

```txt
nodos
conexiones
celdas
zonas
rutas
terrenos
```

No es necesariamente distancia.

No es necesariamente tiempo.

No es necesariamente dificultad real.

El costo es una representacion numerica de una condicion que un sistema consumidor puede interpretar.

```txt
Costo
→ valor asociado al uso de una parte del mapa
```

---

## Responsabilidad de esta nota

Esta nota define que es un costo dentro de reglas de mapa.

Su responsabilidad es explicar:

```txt
que representa un costo
donde puede aplicarse
que datos necesita
que NO debe hacer
cuando conviene usarlo
cuando no conviene usarlo
que riesgos tiene
como validarlo
```

Esta nota no debe explicar por completo pathfinding, NPCs o algoritmos.

Los sistemas que consumen costos deben explicar desde su propio contexto como los usan.

---

## Responsabilidad de un costo

Un costo debe expresar una diferencia de conveniencia, dificultad o penalizacion.

Puede responder preguntas como:

```txt
¿Este camino deberia ser mas caro?
¿Esta zona deberia evitarse si hay otra opcion?
¿Este terreno deberia penalizarse?
¿Esta conexion deberia ser menos conveniente?
```

Un costo no deberia decidir comportamientos.

Un costo no deberia mover entidades.

Un costo no deberia calcular rutas por si mismo.

Un costo no deberia conocer todos los sistemas que lo consumen.

---

## Que puede representar un costo

Un costo puede representar:

```txt
distancia
dificultad
riesgo
penalizacion
preferencia
tiempo estimado
terreno lento
zona peligrosa
consumo de recurso
peso tactico
```

Ejemplo:

```txt
Camino normal
→ costo 1

Camino con barro
→ costo 3

Camino peligroso
→ costo 5
```

El significado del costo debe estar documentado.

No alcanza con poner numeros.

---

## Donde puede aplicarse

Un costo puede aplicarse sobre distintas partes del mapa.

Ejemplos:

```txt
Nodo
→ entrar a este nodo cuesta 2.

Conexion
→ moverse de A a B cuesta 5.

Celda
→ atravesar esta celda cuesta 3.

Zona
→ toda esta zona tiene penalizacion.

Ruta
→ esta ruta completa es menos conveniente.
```

La ubicacion del costo debe responder a la estructura del mapa.

---

## Costo base y costo dinamico

Un costo puede ser fijo o variable.

Costo base:

```txt
terreno normal = 1
barro = 3
agua = 5
```

Costo dinamico:

```txt
zona en peligro = +10
camino congestionado = +5
ruta bloqueada temporalmente = infinito o invalida
```

La diferencia es importante.

```txt
Costo base
→ pertenece al mapa o terreno.

Costo dinamico
→ cambia por estado de juego.
```

---

## Valor alto no es lo mismo que bloqueado

Un costo alto no siempre significa que una zona esta bloqueada.

```txt
Costo alto
→ se puede pasar, pero no conviene.

Bloqueado
→ no se puede pasar.
```

Ejemplo:

```txt
Pantano
→ costo alto.

Pared
→ bloqueado.
```

Confundir estas dos cosas puede generar rutas incorrectas.

---

## Que NO debe hacer un costo

Un costo no debe asumir responsabilidades que no le corresponden.

No debe:

```txt
decidir que ruta tomar
mover al agente
calcular pathfinding completo
decidir comportamiento de NPC
actualizar UI
controlar estados de juego
conocer todos los sistemas que lo usan
```

El costo debe mantenerse como dato interpretable.

---

## Costos como contrato de informacion

Un costo puede pensarse como contrato simple.

```txt
Yo represento cuanto penaliza o conviene usar esta parte del mapa.
Tengo un valor.
Tengo un significado.
Puedo ser consultado por otros sistemas.
```

Ese contrato permite que sistemas de navegacion, decision o gameplay usen costos sin mezclar responsabilidades.

---

## Ejemplo conceptual en codigo

```csharp
public class MapCost
{
    public float Value { get; private set; }
    public string Reason { get; private set; }

    public MapCost(float value, string reason)
    {
        Value = value;
        Reason = reason;
    }

    public void SetValue(float value)
    {
        Value = value;
    }

    public void SetReason(string reason)
    {
        Reason = reason;
    }
}
```

Ejemplo aplicado a una conexion:

```csharp
public class MapConnection
{
    public MapNode From { get; }
    public MapNode To { get; }
    public float BaseCost { get; private set; }
    public bool IsBlocked { get; private set; }

    public MapConnection(MapNode from, MapNode to, float baseCost)
    {
        From = from;
        To = to;
        BaseCost = baseCost;
    }

    public void SetBlocked(bool isBlocked)
    {
        IsBlocked = isBlocked;
    }

    public void SetBaseCost(float baseCost)
    {
        BaseCost = baseCost;
    }
}
```

Este ejemplo muestra el costo como dato.

No calcula rutas.

No mueve agentes.

No decide comportamientos.

---

## Cuando implementar costos

Conviene implementar costos cuando:

```txt
no todos los caminos tienen la misma conveniencia
hay terrenos con penalizaciones
hay zonas peligrosas
hay rutas que deben evitarse salvo necesidad
hay decisiones tacticas de navegacion
hay caminos mas largos pero mas seguros
hay rutas cortas pero caras
```

Ejemplo correcto:

```txt
Un enemigo puede ir por un camino corto peligroso
o por un camino largo seguro.

→ Costos permiten representar esa diferencia.
```

---

## Cuando NO implementar costos

No conviene implementar costos cuando:

```txt
todos los caminos son equivalentes
solo importa si se puede pasar o no
el recorrido es fijo
no hay decisiones espaciales reales
el costo no cambia ninguna decision
el sistema no tiene quien interprete esos costos
```

Ejemplo:

```txt
Un enemigo siempre sigue una unica ruta fija.

→ Agregar costos no cambia nada.
→ Es complejidad innecesaria.
```

---

## Por que no implementarlos de mas

Los costos agregan otra capa de lectura del mapa.

Implementarlos sin necesidad puede generar:

```txt
balance mas dificil
rutas inesperadas
debug mas complejo
numeros magicos
problemas de tuning
dependencias innecesarias
confusion entre costo y bloqueo
```

Regla:

```txt
Si el costo no modifica ninguna decision,
no aporta valor.
```

---

## Mala practica al implementar costos

Malas practicas comunes:

```txt
poner costos sin significado claro
usar numeros magicos
confundir costo alto con bloqueo
mezclar costos de mapa con decision de NPC
hacer que cada sistema interprete el costo distinto
no documentar escala
no debuggear valores
modificar costos dinamicos sin avisar a sistemas consumidores
```

Ejemplo de mala practica:

```txt
Nodo A costo 7
Nodo B costo 12
Nodo C costo 3
```

sin explicar que significa esa escala.

---

## Costos de implementacion

Implementar costos requiere:

```txt
definir escala
definir significado
decidir donde se aplican
integrarlos con estructura de mapa
integrarlos con sistemas consumidores
validar si modifican decisiones
debuggear valores
probar casos borde
```

No es solo agregar un `float`.

Es definir que representa ese valor.

---

## Costos de optimizacion

Los costos pueden afectar rendimiento si se recalculan o consultan mal.

Costos posibles:

```txt
CPU por recalcular costos dinamicos
CPU por consultar costos en cada expansion de ruta
allocations si se generan estructuras temporales
picos si muchos costos cambian al mismo tiempo
costo extra si dependen de consultas fisicas o raycasts
```

Problemas frecuentes:

```txt
recalcular costos cada frame
usar LINQ para filtrar costos en loops criticos
buscar costos por nombre o FindObjectsOfType
no cachear costos base
mezclar costos dinamicos con calculos pesados
```

---

## Criterio de optimizacion

Opciones para reducir costo:

```txt
separar costo base y costo dinamico
cachear costos base
actualizar costos dinamicos solo cuando cambia el estado
evitar recalcular en Update
usar eventos para notificar cambios
evitar allocations en consultas frecuentes
usar estructuras simples para lectura rapida
debug visual activable/desactivable
```

Ejemplo:

```txt
Mala practica:
cada nodo recalcula su costo completo en cada frame.

Mejor:
el costo base queda guardado,
el costo dinamico cambia solo cuando ocurre un evento.
```

---

## Preguntas antes de implementar

Antes de implementar costos, una IA debe responder:

```txt
¿Que representa el costo?
¿Donde se aplica?
¿Que escala usa?
¿Quien lo modifica?
¿Quien lo consume?
¿Es fijo o dinamico?
¿Que pasa con costo alto?
¿Que diferencia hay con bloqueado?
¿Como se debuggea?
¿El costo cambia alguna decision real?
```

Si no hay respuesta clara, no conviene implementarlo todavia.

---

## Validacion visual

Los costos deben poder validarse visualmente.

Se puede mostrar:

```txt
color por costo
numero sobre nodo o celda
grosor de conexion
zonas segun penalizacion
costo base
costo dinamico
costo total
```

Esto permite detectar:

```txt
costos invertidos
costos demasiado altos
costos que no afectan rutas
costos mal ubicados
costo usado como bloqueo por error
```

---

## Errores comunes

```txt
usar costos sin necesidad
no definir escala
confundir costo con bloqueo
guardar costos en el sistema equivocado
hacer que el costo decida comportamiento
no actualizar consumidores cuando cambian costos
no validar visualmente
usar numeros magicos
```

---

## Criterio para una IA

Cuando una IA proponga costos, debe justificar:

```txt
por que el mapa necesita costos
que representa el costo
donde vive el costo
quien lo consume
si es fijo o dinamico
como afecta decisiones
que costo tecnico tiene
como se valida
```

No alcanza con decir:

```txt
Agregar costos al mapa.
```

Debe explicar que problema resuelve.

---

## Checklist

Antes de usar costos, revisar:

```txt
¿Hay caminos o zonas con distinta conveniencia?
¿El costo tiene significado claro?
¿La escala esta definida?
¿El costo no se confunde con bloqueo?
¿El costo vive en la estructura correcta?
¿Hay un sistema consumidor?
¿El costo cambia decisiones reales?
¿Los costos dinamicos se actualizan con control?
¿Se evita recalcular cada frame?
¿Se puede debuggear visualmente?
```

---

## Regla final

Un costo no decide.

Un costo informa.

```txt
Costo
→ dato de conveniencia o penalizacion

Sistema consumidor
→ interpreta ese dato
```
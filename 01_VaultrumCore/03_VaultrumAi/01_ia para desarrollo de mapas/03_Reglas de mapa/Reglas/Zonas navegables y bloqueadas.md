## Definicion

Las zonas navegables y bloqueadas son una forma de clasificar partes del mapa segun si pueden ser usadas o no por sistemas de navegacion.

Una zona navegable es una parte valida del mapa.

Una zona bloqueada es una parte invalida o inaccesible.

No son comportamiento de NPC.

No son pathfinding completo.

No son movimiento fisico.

Son reglas espaciales que indican disponibilidad.

```txt
Zona navegable
→ se puede usar

Zona bloqueada
→ no se puede usar
```

---

## Responsabilidad de esta nota

Esta nota define como distinguir zonas validas e invalidas dentro de un mapa.

Su responsabilidad es explicar:

```txt
que significa navegable
que significa bloqueado
donde puede aplicarse
que datos necesita
cuando conviene implementarlo
cuando no conviene implementarlo
que costo tecnico tiene
como validarlo
```

Esta nota no debe explicar completo algoritmos, NPCs o movimiento.

Los sistemas consumidores deben interpretar esta informacion desde su propio contexto.

---

## Problema que resuelve

Esta clasificacion resuelve el problema de saber que partes del mapa pueden ser usadas.

Pregunta principal:

```txt
¿Que partes del mapa son validas para navegar y cuales no?
```

Ejemplo:

```txt
Suelo
→ navegable

Pared
→ bloqueada

Puerta cerrada
→ bloqueada temporalmente

Puerta abierta
→ navegable
```

---

## Datos que necesita

Una zona navegable o bloqueada puede necesitar:

```txt
identificador
area o limites
estado disponible/bloqueado
tipo de bloqueo
condicion de cambio
referencia visual
estructura asociada
```

Puede aplicarse sobre:

```txt
nodos
conexiones
celdas
zonas
colliders
tiles
sectores
```

La estructura depende del mapa.

---

## Navegable

Algo navegable es algo que el sistema puede usar como parte valida del recorrido.

Puede significar:

```txt
se puede pisar
se puede atravesar
se puede conectar
se puede considerar para ruta
se puede ocupar
```

Pero el significado exacto debe definirse segun el juego.

Ejemplo:

```txt
Una celda puede ser navegable para un soldado,
pero no para un vehiculo grande.
```

---

## Bloqueado

Algo bloqueado es algo que el sistema no debe usar como parte valida del recorrido.

Puede representar:

```txt
pared
obstaculo
puerta cerrada
zona fuera del mapa
zona peligrosa prohibida
camino deshabilitado
celda ocupada
conexion cortada
```

Bloqueado no es lo mismo que costoso.

```txt
Costoso
→ se puede pasar, pero no conviene.

Bloqueado
→ no se puede pasar.
```

---

## Bloqueo fijo y bloqueo dinamico

Un bloqueo puede ser fijo o dinamico.

Bloqueo fijo:

```txt
pared
borde del mapa
hueco
obstaculo permanente
```

Bloqueo dinamico:

```txt
puerta cerrada
camino destruido
objeto que se mueve
zona ocupada
evento temporal
```

La diferencia importa porque los bloqueos dinamicos deben notificar o actualizar sistemas consumidores.

---

## Que NO debe hacer una zona bloqueada

Una zona bloqueada no debe asumir responsabilidades que no le corresponden.

No debe:

```txt
calcular pathfinding completo
mover agentes
decidir comportamiento de NPC
actualizar estados de IA
resolver combate
funcionar como manager global
```

Debe exponer estado.

El sistema consumidor interpreta ese estado.

---

## Zonas como contrato de informacion

Una zona navegable o bloqueada puede pensarse como contrato.

```txt
Yo represento una parte del espacio.
Puedo decir si esta disponible.
Puedo decir si esta bloqueada.
Puedo cambiar de estado si corresponde.
Puedo ser consultada por otros sistemas.
```

Ese contrato permite separar disponibilidad del mapa y decision del sistema.

---

## Ejemplo conceptual en codigo

```csharp
public class NavigationZone
{
    public string Id { get; }
    public bool IsBlocked { get; private set; }
    public string BlockReason { get; private set; }

    public NavigationZone(string id)
    {
        Id = id;
        IsBlocked = false;
        BlockReason = string.Empty;
    }

    public void SetBlocked(bool isBlocked, string reason = "")
    {
        IsBlocked = isBlocked;
        BlockReason = reason;
    }

    public bool IsNavigable()
    {
        return !IsBlocked;
    }
}
```

Este ejemplo muestra estado de navegabilidad.

No calcula rutas.

No mueve agentes.

No decide comportamiento.

---

## Cuando implementar zonas navegables y bloqueadas

Conviene implementarlas cuando:

```txt
el mapa tiene areas validas e invalidas
hay obstaculos relevantes
hay zonas que cambian de estado
hay puertas, bloqueos o barreras
el pathfinding debe evitar ciertas partes
el jugador o NPC no deben atravesar todo
```

Ejemplo correcto:

```txt
Un mapa tiene puertas que se abren y cierran.

→ Zonas o conexiones bloqueadas permiten representar ese cambio.
```

---

## Cuando NO implementarlas

No conviene implementarlas como sistema separado cuando:

```txt
el mapa no tiene obstaculos
todo el espacio es valido
el recorrido es fijo
los bloqueos ya estan resueltos por otra estructura
una ruta manual alcanza
no hay sistemas consumidores
```

Ejemplo:

```txt
Un enemigo sigue siempre la misma spline.

→ No hace falta clasificar todo el mapa como navegable o bloqueado.
```

---

## Por que no implementarlas de mas

Clasificar zonas sin necesidad puede generar:

```txt
datos extra
debug extra
confusion con colliders fisicos
reglas duplicadas
estado inconsistente
costos de actualizacion
```

Regla:

```txt
Si nadie necesita consultar la navegabilidad,
no hace falta modelarla como sistema.
```

---

## Mala practica al implementarlas

Malas practicas comunes:

```txt
bloquear zonas sin criterio claro
confundir bloqueo con costo alto
duplicar bloqueo en varias clases
no notificar cambios dinamicos
no validar visualmente
hacer que la zona bloqueada mueva agentes
hacer que el bloqueo decida comportamiento
actualizar bloqueos cada frame sin necesidad
```

Ejemplo de mala practica:

```txt
Una puerta cerrada se marca como costo 9999
en vez de bloquear la conexion.

Resultado:
el sistema puede seguir considerandola transitable.
```

---

## Costos de implementacion

Implementar zonas navegables y bloqueadas requiere:

```txt
definir que significa navegable
definir que significa bloqueado
decidir sobre que estructura aplica
definir estado inicial
definir cambios dinamicos
notificar o actualizar consumidores
debuggear estado
probar casos de borde
```

No es solo poner un booleano.

El booleano necesita contexto.

---

## Costos de optimizacion

Los bloqueos pueden afectar rendimiento si se actualizan o consultan mal.

Costos posibles:

```txt
CPU por validar zonas
CPU por actualizar estados dinamicos
CPU por recalcular rutas afectadas
allocations por listas temporales
picos cuando cambian muchas zonas
costo de debug visual
```

Problemas frecuentes:

```txt
revisar todos los bloqueos cada frame
recalcular todo el mapa por un bloqueo local
consultar colliders fisicos sin control
usar busquedas globales para encontrar zonas
no cachear zonas afectadas
```

---

## Criterio de optimizacion

Opciones para reducir costo:

```txt
actualizar bloqueos por eventos
recalcular solo rutas afectadas
cachear estado navegable
separar bloqueo fijo y dinamico
evitar validar todo el mapa cada frame
usar estructuras simples para consulta
activar debug solo cuando se necesita
```

Ejemplo:

```txt
Mala practica:
cada NPC pregunta cada frame si todas las zonas estan bloqueadas.

Mejor:
el mapa notifica cuando una zona cambia,
y cada sistema consumidor decide si necesita recalcular.
```

---

## Preguntas antes de implementar

Antes de implementar zonas navegables y bloqueadas, una IA debe responder:

```txt
¿Que significa navegable en este juego?
¿Que significa bloqueado?
¿Sobre que estructura aplica?
¿El bloqueo es fijo o dinamico?
¿Quien cambia el estado?
¿Quien consume el estado?
¿Que pasa cuando cambia?
¿Como se debuggea?
¿El sistema realmente necesita consultarlo?
```

---

## Validacion visual

Debe poder verse:

```txt
zonas navegables
zonas bloqueadas
bloqueos fijos
bloqueos dinamicos
conexiones cortadas
estado actual
motivo del bloqueo
```

Esto permite detectar:

```txt
zonas mal marcadas
bloqueos que no se actualizan
rutas usando zonas bloqueadas
zonas navegables inaccesibles
confusion entre costo y bloqueo
```

---

## Errores comunes

```txt
confundir bloqueo con costo alto
marcar todo el mapa sin necesidad
no diferenciar fijo y dinamico
no notificar cambios
no validar visualmente
guardar bloqueo en el sistema equivocado
mezclar navegabilidad con comportamiento
recalcular demasiado
```

---

## Criterio para una IA

Cuando una IA proponga zonas navegables y bloqueadas, debe justificar:

```txt
por que el mapa necesita esa clasificacion
que significa navegable
que significa bloqueado
donde vive el estado
quien lo cambia
quien lo consume
que costo tecnico tiene
como se valida
```

No alcanza con decir:

```txt
Marcar zonas bloqueadas.
```

Debe explicar para que sistema y con que criterio.

---

## Checklist

Antes de usar zonas navegables y bloqueadas, revisar:

```txt
¿Hay partes validas e invalidas?
¿Navegable esta definido?
¿Bloqueado esta definido?
¿No se confunde bloqueo con costo?
¿Aplica a nodos, celdas, zonas o conexiones?
¿Hay bloqueos dinamicos?
¿Los consumidores se actualizan correctamente?
¿Se evita recalcular todo cada frame?
¿Se puede debuggear visualmente?
```

---

## Regla final

Una zona bloqueada no decide.

Una zona navegable no mueve.

Exponen disponibilidad espacial.

```txt
Zona
→ estado de disponibilidad

Sistema consumidor
→ interpreta y actua
```
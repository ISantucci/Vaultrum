## Definicion

Un mapa con costos es una representacion del espacio donde distintas partes del mapa tienen valores asociados que indican conveniencia, dificultad, riesgo o penalizacion.

No es un algoritmo.

No es pathfinding por si mismo.

No es comportamiento de NPC.

Es una estructura de mapa enriquecida con informacion numerica interpretable.

```txt
Mapa
→ estructura espacial

Costos
→ valores sobre partes del mapa

Mapa con costos
→ estructura espacial con valores interpretables
```

---

## Responsabilidad de esta nota

Esta nota explica como representar costos dentro de un mapa.

Su responsabilidad es definir:

```txt
que es un mapa con costos
donde pueden vivir los costos
que datos necesita
que sistemas puede alimentar
cuando conviene implementarlo
cuando no conviene implementarlo
que costo tecnico tiene
como validarlo
```

Esta nota no debe explicar completo A Star, Dijkstra, NPCs o movimiento.

Los sistemas consumidores deben explicar como interpretan el mapa con costos.

---

## Problema que resuelve

Un mapa con costos resuelve el problema de representar que no todos los caminos o zonas valen lo mismo.

Pregunta principal:

```txt
¿Como represento un mapa donde pasar por distintas partes tiene distinto valor?
```

Ejemplo:

```txt
Camino corto
→ peligroso
→ costo alto

Camino largo
→ seguro
→ costo bajo
```

El mapa con costos permite que otros sistemas usen esa informacion.

---

## Datos que necesita

Un mapa con costos puede necesitar:

```txt
estructura base del mapa
nodos, conexiones, celdas o zonas
costo base
costo dinamico
estado bloqueado/disponible
tipo de terreno
criterio de actualizacion
debug visual
```

Los costos deben tener significado claro.

No deben ser numeros sueltos sin escala.

---

## Donde pueden vivir los costos

Los costos pueden vivir en distintas partes de la estructura.

### En nodos

```txt
Entrar a este nodo cuesta 3.
```

### En conexiones

```txt
Moverse de A a B cuesta 5.
```

### En celdas

```txt
Atravesar esta celda cuesta 2.
```

### En zonas

```txt
Toda esta zona agrega +4 de penalizacion.
```

La eleccion depende del diseño del mapa.

---

## Costo base y costo total

Un mapa con costos puede separar:

```txt
costo base
→ valor propio del mapa o terreno.

costo dinamico
→ valor agregado por estado de juego.

costo total
→ resultado usado por el sistema consumidor.
```

Ejemplo:

```txt
Barro
→ costo base 3

Zona en peligro
→ costo dinamico +5

Costo total
→ 8
```

Separar estos valores ayuda a mantener claridad.

---

## Que NO debe hacer un mapa con costos

Un mapa con costos no debe asumir responsabilidades que pertenecen a otros sistemas.

No debe:

```txt
decidir comportamiento de NPC
mover entidades
calcular todas las rutas por si mismo
resolver combate
actualizar UI
funcionar como GameManager
mezclar costos con estados de IA
```

El mapa con costos debe exponer informacion.

El sistema consumidor interpreta.

---

## Mapa con costos como contrato de informacion

Un mapa con costos puede pensarse como contrato.

```txt
Yo represento el espacio.
Algunas partes tienen costos.
Puedo exponer esos costos.
Puedo actualizar esos costos si cambia el estado.
Puedo ser consultado por sistemas consumidores.
```

Ese contrato evita mezclar datos de mapa con decisiones de gameplay o comportamiento.

---

## Ejemplo conceptual en codigo

```csharp
public interface ICostProvider<TNode>
{
    float GetCost(TNode from, TNode to);
}
```

Ejemplo sobre conexiones:

```csharp
public class ConnectionCostProvider : ICostProvider<MapConnection>
{
    public float GetCost(MapConnection from, MapConnection to)
    {
        if (to.IsBlocked)
            return float.PositiveInfinity;

        return to.BaseCost;
    }
}
```

Ejemplo mas simple sobre nodos:

```csharp
public class NodeCostProvider
{
    public float GetCost(MapNode node)
    {
        if (node.IsBlocked)
            return float.PositiveInfinity;

        return node.BaseCost;
    }
}
```

Estos ejemplos muestran proveedores de costo.

No deciden comportamientos.

No mueven entidades.

No calculan por si solos toda la ruta.

---

## Cuando implementar mapas con costos

Conviene implementar mapas con costos cuando:

```txt
el mapa tiene terrenos distintos
hay zonas mas dificiles o peligrosas
hay caminos mas o menos convenientes
hay rutas alternativas con diferencias reales
el sistema debe elegir segun algo mas que distancia
hay condiciones dinamicas que modifican rutas
```

Ejemplo correcto:

```txt
Un mapa tiene dos caminos:

camino corto
→ pasa por zona peligrosa

camino largo
→ es seguro

→ Un mapa con costos permite representar esa diferencia.
```

---

## Cuando NO implementar mapas con costos

No conviene implementarlos cuando:

```txt
todos los caminos son equivalentes
solo importa bloqueado o disponible
el recorrido es fijo
no existe sistema que interprete costos
los costos no cambian ninguna decision
una estructura simple alcanza
```

Ejemplo:

```txt
Un enemigo sigue una ruta fija.

No elige entre rutas.
No hay decisiones de costo.

→ Un mapa con costos no aporta valor.
```

---

## Por que no implementarlo de mas

Un mapa con costos agrega complejidad de diseño y tecnica.

Puede generar:

```txt
tuning dificil
rutas inesperadas
necesidad de debug visual
mas datos que mantener
mas reglas que validar
mas errores por costos mal seteados
confusion entre costo y bloqueo
```

Regla:

```txt
Si los costos no cambian decisiones,
son ruido.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
poner costos en todos lados sin criterio
usar numeros magicos
no definir escala
hacer que cada sistema interprete costos distinto
actualizar costos dinamicos cada frame sin necesidad
no separar costo base y dinamico
usar costo infinito como parche sin documentarlo
no debuggear visualmente
```

Ejemplo de mala practica:

```txt
Nodo A costo 20 porque se ve peligroso,
pero ningun sistema usa ese dato.

→ Dato inutil.
```

---

## Costos de implementacion

Implementar mapas con costos requiere:

```txt
definir estructura base
decidir donde viven los costos
definir escala
definir costo base
definir costo dinamico si existe
definir quien modifica costos
definir quien consume costos
crear debug visual
probar rutas resultantes
```

No es solamente agregar una variable.

Es diseñar como el mapa comunica informacion.

---

## Costos de optimizacion

Los mapas con costos pueden afectar rendimiento si el sistema consulta o recalcula costos con mucha frecuencia.

Costos posibles:

```txt
CPU por consulta de costos
CPU por recalculo de costos dinamicos
CPU por actualizar muchas zonas
allocations por estructuras temporales
picos si se actualizan muchos nodos juntos
costo de pathfinding mas alto si hay muchas variaciones
```

Problemas frecuentes:

```txt
recalcular todos los costos cada frame
actualizar todo el mapa por un cambio local
consultar costos con busquedas globales
usar LINQ en loops de pathfinding
crear objetos de costo durante la busqueda
```

---

## Criterio de optimizacion

Opciones para reducir costo:

```txt
cachear costo base
actualizar costo dinamico solo por eventos
limitar actualizaciones a zonas afectadas
evitar recalcular todo el mapa
usar estructuras simples para lectura rapida
separar debug de runtime
evitar allocations en consultas
precalcular costos si el mapa es estatico
```

Ejemplo:

```txt
Mala practica:
cuando se abre una puerta, recalcular todos los costos del mapa.

Mejor:
actualizar solo nodos, conexiones o zonas afectadas por esa puerta.
```

---

## Preguntas antes de implementar

Antes de implementar mapas con costos, una IA debe responder:

```txt
¿Que diferencia representa el costo?
¿Donde vive el costo?
¿Que escala se usa?
¿El costo es fijo o dinamico?
¿Quien actualiza costos?
¿Quien consume costos?
¿Los costos cambian decisiones reales?
¿Como se debuggean?
¿Que pasa si un costo cambia?
¿El costo tecnico se justifica?
```

---

## Validacion visual

Un mapa con costos debe poder validarse visualmente.

Se puede mostrar:

```txt
color por costo
numero de costo
zonas con penalizacion
conexiones caras
nodos bloqueados
costo base
costo dinamico
costo total
```

Esto permite detectar:

```txt
costos invertidos
zonas mal configuradas
costos que no afectan rutas
costos demasiado altos
costos demasiado bajos
rutas incoherentes
```

---

## Errores comunes

```txt
crear mapa con costos sin necesidad
no definir escala
mezclar costos con bloqueos
mezclar costos con comportamiento de NPC
no separar costo base y dinamico
no actualizar consumidores
no validar visualmente
usar costos como parche de diseño
```

---

## Criterio para una IA

Cuando una IA proponga mapas con costos, debe justificar:

```txt
por que el mapa necesita costos
que estructura base usa
donde viven los costos
que significan los valores
quien los consume
quien los actualiza
que costo tecnico tienen
como se validan
```

No alcanza con decir:

```txt
Hacer un mapa con costos.
```

Debe explicar que decision mejora.

---

## Checklist

Antes de usar mapas con costos, revisar:

```txt
¿El mapa tiene diferencias reales de conveniencia?
¿La estructura base esta definida?
¿Los costos tienen significado?
¿La escala esta documentada?
¿Se separa costo base y dinamico?
¿Hay sistema consumidor?
¿Los costos modifican decisiones reales?
¿La actualizacion esta controlada?
¿Se evita recalcular todo cada frame?
¿Se puede debuggear visualmente?
```

---

## Regla final

Un mapa con costos no decide.

Expone informacion ponderada.

```txt
Mapa
→ estructura

Costos
→ valores

Sistema consumidor
→ interpreta
```
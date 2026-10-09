## Definicion

ABB significa Arbol Binario de Busqueda.

Es una estructura de datos en forma de arbol donde cada nodo puede tener hasta dos hijos.

La regla principal es:

```txt
hijo izquierdo
→ valores menores

hijo derecho
→ valores mayores
```

Ejemplo conceptual:

```txt
        50
       /  \
     30    70
    / \    / \
  20  40  60  80
```

Si se busca un valor:

```txt
valor menor que nodo actual
→ ir a izquierda

valor mayor que nodo actual
→ ir a derecha
```

Un ABB sirve para mantener datos ordenados por un criterio de busqueda.

---

## Responsabilidad

La responsabilidad de un ABB es organizar elementos comparables para permitir busqueda, insercion y recorrido ordenado.

Debe responder:

```txt
¿Donde insertar un valor?
¿Existe este valor?
¿Cual es el menor valor?
¿Cual es el mayor valor?
¿Como recorrer elementos en orden?
```

Un ABB organiza orden.

No decide por si solo que significa ese orden para el gameplay.

Ejemplo:

```txt
ABB
→ guarda enemigos ordenados por distancia a la base.

Sistema de targeting
→ consulta el enemigo prioritario.

Torre
→ ataca segun regla definida.
```

---

## Que NO debe hacer

Un ABB no debe absorber responsabilidades del sistema que lo usa.

No debe:

```txt
decidir gameplay por si solo
atacar enemigos
calcular daño
mover entidades
actualizar UI
definir dificultad
crear enemigos
resolver pathfinding
representar conexiones de mapa
```

Ejemplo incorrecto:

```txt
ABB
→ ordena enemigos
→ decide objetivo
→ dispara
→ aplica daño
→ actualiza UI
```

Ejemplo correcto:

```txt
EnemyPriorityTree
→ usa ABB para ordenar enemigos.

TargetingSystem
→ consulta prioridad.

TowerAttack
→ ejecuta ataque.

HealthSystem
→ aplica daño.
```

Regla:

```txt
ABB organiza por criterio.
No ejecuta gameplay.
```

---

## Que problema resuelve

Un ABB resuelve problemas donde importa mantener datos ordenados por un valor comparable.

Casos que puede resolver:

```txt
buscar valores rapidamente
mantener prioridades ordenadas
consultar minimo
consultar maximo
recorrer elementos en orden
ordenar enemigos por progreso
ordenar recursos por cantidad
ordenar eventos por tiempo
```

Ejemplo:

```txt
En Tower Defense, una torre quiere atacar al enemigo mas avanzado.

Cada enemigo tiene progreso en el camino.

Enemy A → 10
Enemy B → 60
Enemy C → 35

El sistema puede ordenar por progreso
y consultar el mayor valor.
```

Idea central:

```txt
Si el sistema necesita mantener elementos ordenados por un criterio,
un ABB puede ser una opcion.
```

---

## Datos que necesita

Un ABB necesita elementos comparables.

Puede ordenar por:

```txt
numero
distancia
progreso
tiempo
prioridad
puntuacion
costo
nivel
```

Ejemplos:

```txt
EnemyProgress
→ progreso del enemigo en el camino.

EventTime
→ tiempo en que debe ocurrir un evento.

ResourceAmount
→ cantidad de recurso.

ThreatScore
→ nivel de amenaza.
```

Tambien necesita una regla de comparacion.

```txt
menor que
mayor que
igual
```

Si el criterio no es claro, el ABB no es buena opcion.

---

## Que produce

Un ABB puede producir:

```txt
valor encontrado
valor minimo
valor maximo
recorrido ordenado
subarbol izquierdo
subarbol derecho
cantidad de elementos si se trackea
```

Operaciones comunes:

```txt
Insert
→ agrega elemento respetando orden.

Search
→ busca elemento.

Min
→ devuelve menor valor.

Max
→ devuelve mayor valor.

InOrder
→ recorre elementos de menor a mayor.
```

La salida debe ser interpretada por el sistema consumidor.

Ejemplo:

```txt
Max
→ devuelve enemigo mas avanzado.

TargetingSystem
→ decide si es objetivo valido.

TowerAttack
→ dispara.
```

---

## Como funciona

Un ABB compara cada valor con el nodo actual.

```txt
Si el valor es menor
→ va a izquierda.

Si el valor es mayor
→ va a derecha.
```

Ejemplo basico en C#:

```csharp
public class BinarySearchTreeNode
{
    public int Value;
    public BinarySearchTreeNode Left;
    public BinarySearchTreeNode Right;

    public BinarySearchTreeNode(int value)
    {
        Value = value;
    }
}
```

```csharp
public class BinarySearchTree
{
    private BinarySearchTreeNode root;

    public void Insert(int value)
    {
        root = InsertRecursive(root, value);
    }

    private BinarySearchTreeNode InsertRecursive(BinarySearchTreeNode node, int value)
    {
        if (node == null)
        {
            return new BinarySearchTreeNode(value);
        }

        if (value < node.Value)
        {
            node.Left = InsertRecursive(node.Left, value);
        }
        else if (value > node.Value)
        {
            node.Right = InsertRecursive(node.Right, value);
        }

        return node;
    }

    public bool Contains(int value)
    {
        return ContainsRecursive(root, value);
    }

    private bool ContainsRecursive(BinarySearchTreeNode node, int value)
    {
        if (node == null)
        {
            return false;
        }

        if (node.Value == value)
        {
            return true;
        }

        if (value < node.Value)
        {
            return ContainsRecursive(node.Left, value);
        }

        return ContainsRecursive(node.Right, value);
    }
}
```

Este ejemplo ordena enteros.

No sabe nada de enemigos, torres ni gameplay.

---

## Recorrido ordenado

Un ABB permite recorrer valores en orden usando recorrido in-order.

```txt
izquierda
→ nodo actual
→ derecha
```

Ejemplo:

```txt
        50
       /  \
     30    70
    / \    / \
  20  40  60  80
```

Recorrido in-order:

```txt
20
30
40
50
60
70
80
```

Esto sirve cuando el sistema necesita procesar datos ordenados.

---

## Sistemas consumidores comunes

Un ABB suele aparecer como soporte de sistemas que necesitan orden por criterio.

Ejemplos:

```txt
Targeting por prioridad
→ consultar enemigo mas avanzado.

Eventos por tiempo
→ consultar evento mas cercano.

Ranking
→ mantener valores ordenados.

Recursos por cantidad
→ consultar menor o mayor.

Amenazas
→ ordenar por threat score.
```

El ABB no implementa esos sistemas por si solo.

Solo ofrece la estructura de ordenamiento y busqueda.

Regla:

```txt
ABB sirve cuando el sistema consumidor necesita orden por comparacion.

Si el sistema necesita conexiones,
historial inverso u orden de llegada,
ABB no es la estructura correcta.
```

---

## Ejemplo aplicado: enemigo mas avanzado

Un ABB puede usarse para ordenar enemigos por progreso.

Flujo:

```txt
Enemigo actualiza progreso.
Sistema registra progreso.
ABB mantiene orden.
Targeting consulta maximo.
Torre ataca objetivo elegido.
```

Ejemplo conceptual:

```csharp
public class EnemyTargetData
{
    public string EnemyId { get; }
    public float Progress { get; }

    public EnemyTargetData(string enemyId, float progress)
    {
        EnemyId = enemyId;
        Progress = progress;
    }
}
```

Para un caso real, habria que definir una comparacion por `Progress`.

Separacion de responsabilidades:

```txt
ABB
→ ordena por progreso.

TargetingSystem
→ decide regla de objetivo.

TowerAttack
→ ejecuta disparo.

Enemy
→ informa su progreso.
```

El ABB no decide atacar.

Solo permite consultar orden.

---

## Como aplicarlo en videojuegos

En videojuegos, un ABB puede usarse cuando hace falta mantener datos ordenados por un criterio.

Casos tipicos:

```txt
enemigos por progreso
eventos por tiempo
objetivos por prioridad
amenazas por puntaje
items por valor
recursos por cantidad
ranking interno
```

Ejemplo en Tower Defense:

```txt
Torre prioriza enemigo mas avanzado.

ABB
→ mantiene enemigos ordenados por progreso.

Targeting
→ consulta maximo.

Ataque
→ dispara al objetivo.
```

Esto puede ser util si la consulta de prioridad ocurre frecuentemente y el conjunto cambia de forma controlada.

---

## Cuando conviene usar ABB

Conviene usar ABB cuando:

```txt
necesitas mantener elementos ordenados
necesitas buscar por valor
necesitas consultar minimo o maximo
necesitas recorrido ordenado
el criterio de comparacion es claro
```

Preguntas utiles:

```txt
¿Hay un valor por el cual ordenar?
¿Necesito consultar minimo o maximo?
¿Necesito buscar rapido?
¿Necesito recorrido ordenado?
¿La lista cambia con frecuencia?
```

Si la respuesta es si, ABB puede ser una opcion.

---

## Cuando NO conviene usar ABB

No conviene usar ABB si:

```txt
no hay criterio claro de orden
necesitas procesar en orden de llegada
necesitas acceder al ultimo elemento
necesitas representar conexiones
hay pocos elementos y una lista alcanza
el arbol puede desbalancearse mucho
```

Ejemplos:

```txt
deshacer ultima accion
→ Stack.

procesar oleada en orden
→ Queue.

representar mapa conectado
→ Grafo.

pocos enemigos activos
→ List puede alcanzar.
```

Regla:

```txt
No usar ABB si no hay una comparacion clara.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
usar ABB con pocos elementos sin necesidad
no definir criterio de comparacion
ignorar valores duplicados
hacer que el ABB ejecute gameplay
no controlar desbalance
usar ABB cuando se necesita prioridad dinamica muy cambiante
actualizar valores sin reordenar
```

Ejemplo de mala practica:

```txt
Un enemigo cambia su progreso,
pero queda en la misma posicion del ABB.
```

Problema:

```txt
El arbol deja de representar el orden real.
```

Si el valor usado para ordenar cambia, hay que actualizar la estructura correctamente.

---

## Costos de implementacion

Implementar un ABB requiere mas cuidado que Stack o Queue.

Puede requerir:

```txt
nodos
comparacion
insercion
busqueda
eliminacion
manejo de duplicados
recorrido
debug de arbol
actualizacion si cambia el valor ordenado
```

El costo aumenta si:

```txt
hay eliminaciones frecuentes
hay valores duplicados
el arbol se desbalancea
el criterio cambia en runtime
```

---

## Costos de optimizacion

Un ABB puede ser eficiente si esta razonablemente balanceado.

Riesgos posibles:

```txt
arbol desbalanceado
muchas inserciones ordenadas
actualizaciones frecuentes de valores
eliminaciones complejas
duplicados mal manejados
recorridos completos innecesarios
```

Criterio:

```txt
ABB balanceado
→ busqueda eficiente.

ABB desbalanceado
→ puede comportarse como una lista.
```

Ejemplo de desbalance:

```txt
Insertar:
10
20
30
40
50
```

Puede terminar como:

```txt
10
  \
   20
     \
      30
        \
         40
           \
            50
```

En ese caso, la busqueda pierde ventaja.

---

## Validacion

Validar un ABB implica revisar que el orden se mantenga correctamente.

Validar:

```txt
si los menores quedan a la izquierda
si los mayores quedan a la derecha
si Search encuentra valores existentes
si Search falla con valores inexistentes
si Min y Max devuelven lo correcto
si el recorrido in-order sale ordenado
si los valores actualizados se reubican
si los duplicados se manejan con criterio
```

Debug util:

```txt
imprimir recorrido in-order
mostrar raiz
mostrar hijos
logs de insercion
logs de busqueda
visualizacion del arbol
```

---

## Preguntas antes de implementarlo

Antes de usar ABB, preguntar:

```txt
¿Necesito mantener orden?
¿Cual es el criterio de comparacion?
¿Necesito minimo o maximo?
¿Necesito busqueda frecuente?
¿Hay duplicados?
¿Los valores cambian en runtime?
¿Que pasa si el arbol se desbalancea?
¿Una lista ordenada alcanza?
¿Necesito una estructura balanceada en vez de ABB simple?
```

---

## Errores comunes

Errores comunes:

```txt
usar ABB sin criterio de orden
ignorar duplicados
no reordenar al cambiar valor
no implementar eliminacion correctamente
confundir ABB con grafo
hacer que el ABB decida gameplay
no validar recorrido ordenado
usar ABB simple cuando se necesita balanceo
```

---

## Criterio para una IA

Cuando una IA trabaje con ABB debe:

```txt
identificar si el problema requiere orden por comparacion
definir claramente el criterio de comparacion
separar ABB del sistema consumidor
no hacer que el ABB ejecute gameplay
explicar Min, Max, Search e InOrder si aplica
advertir sobre duplicados
advertir sobre desbalance
comparar con List, Queue, Stack o Grafo si hay duda
```

Regla operativa:

```txt
Si hay que mantener elementos ordenados por un criterio claro,
ABB puede tener sentido.

Si no hay criterio de orden,
no corresponde usarlo.
```

---

## Checklist

Antes de cerrar una implementacion con ABB, revisar:

```txt
¿El problema realmente necesita orden?
¿El criterio de comparacion esta claro?
¿Los menores van a la izquierda?
¿Los mayores van a la derecha?
¿Se manejan duplicados?
¿Se actualiza la estructura si cambia el valor?
¿Min y Max funcionan?
¿InOrder devuelve valores ordenados?
¿El ABB esta separado del sistema consumidor?
¿Una List ordenada alcanzaba?
```

---

## Regla final

```txt
ABB no es una estructura para complicar el sistema.

Es util cuando el orden por comparacion realmente mejora busqueda, prioridad o recorrido.
```
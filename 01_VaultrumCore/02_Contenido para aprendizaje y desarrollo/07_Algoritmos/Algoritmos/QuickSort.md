## Definicion

QuickSort es un algoritmo de ordenamiento que organiza una coleccion usando pivotes y particiones.

Sirve para ordenar datos segun un criterio.

No crea la coleccion.

No decide que datos son importantes.

No reemplaza al sistema que usa los datos ordenados.

QuickSort procesa una coleccion y devuelve o deja esa coleccion ordenada.

```txt
Coleccion desordenada
→ QuickSort
→ coleccion ordenada
```

---

## Responsabilidad de esta nota

Esta nota explica QuickSort como algoritmo.

Su responsabilidad es definir:

```txt
que problema resuelve
que datos necesita
como funciona
que resultado devuelve
cuando conviene usarlo
cuando no conviene usarlo
que errores evita
que riesgos tiene
```

Esta nota no debe explicar todas las estructuras de datos ni todos los sistemas que pueden ordenar informacion.

Los sistemas que necesiten ordenamiento deben referenciar el algoritmo desde su propio contexto.

---

## Problema que resuelve

QuickSort resuelve el problema de ordenar una coleccion.

Pregunta principal:

```txt
¿Como ordeno estos datos segun un criterio?
```

Ejemplos:

```txt
ordenar puntuaciones
ordenar rankings
ordenar distancias
ordenar prioridades
ordenar resultados
ordenar estadisticas
```

El criterio de ordenamiento puede ser:

```txt
menor a mayor
mayor a menor
distancia
score
tiempo
prioridad
costo
```

---

## Datos que necesita

QuickSort necesita:

```txt
una coleccion
un rango a ordenar
un criterio de comparacion
```

La coleccion puede ser:

```txt
array
lista
coleccion de objetos
```

El algoritmo no deberia decidir por si mismo que significa “mejor” o “peor”.

Ese criterio debe venir del sistema consumidor.

---

## Resultado que devuelve

QuickSort produce:

```txt
coleccion ordenada
```

Ejemplo:

```txt
Entrada:
[8, 3, 5, 1, 9]

Salida:
[1, 3, 5, 8, 9]
```

El resultado puede ser usado por otro sistema.

Por ejemplo:

```txt
ranking
tabla
prioridad de objetivos
lista de resultados
```

---

## Como funciona

QuickSort usa una estrategia de division.

Flujo conceptual:

```txt
1. Elegir un pivote.
2. Separar elementos menores que el pivote.
3. Separar elementos mayores que el pivote.
4. Aplicar el mismo proceso a cada parte.
5. Repetir hasta que la coleccion quede ordenada.
```

Ejemplo:

```txt
Lista:
[8, 3, 5, 1, 9]

Pivote:
5

Menores:
[3, 1]

Mayores:
[8, 9]

Resultado final:
[1, 3, 5, 8, 9]
```

---

## Pivote

El pivote es el elemento usado como referencia para dividir la coleccion.

Una mala eleccion del pivote puede empeorar el rendimiento.

Estrategias comunes:

```txt
ultimo elemento
primer elemento
elemento central
pivote aleatorio
mediana aproximada
```

Para aprendizaje, usar el ultimo elemento es simple.

Para sistemas reales, conviene considerar el caso de uso.

---

## Ejemplo conceptual en codigo

```csharp
public static class QuickSort
{
    public static void Sort(int[] values, int low, int high)
    {
        if (low >= high) return;

        int pivotIndex = Partition(values, low, high);

        Sort(values, low, pivotIndex - 1);
        Sort(values, pivotIndex + 1, high);
    }

    private static int Partition(int[] values, int low, int high)
    {
        int pivot = values[high];
        int smallerIndex = low - 1;

        for (int current = low; current < high; current++)
        {
            if (values[current] <= pivot)
            {
                smallerIndex++;
                Swap(values, smallerIndex, current);
            }
        }

        Swap(values, smallerIndex + 1, high);

        return smallerIndex + 1;
    }

    private static void Swap(int[] values, int a, int b)
    {
        if (a == b) return;

        int temp = values[a];
        values[a] = values[b];
        values[b] = temp;
    }
}
```

Este ejemplo muestra el procedimiento basico.

No decide que datos ordenar.

No decide cuando mostrar resultados.

Solo ordena.

---

## Aplicacion en videojuegos

QuickSort puede servir para ordenar:

```txt
scores
rankings
tiempos de carrera
enemigos por distancia
objetivos por prioridad
resultados de partida
estadisticas
oleadas por dificultad
```

Ejemplo conceptual:

```txt
Lista de jugadores
→ criterio: score descendente
→ ranking ordenado
```

El algoritmo ordena.

El sistema de ranking decide que hacer con ese orden.

---

## Cuando conviene usarlo

Conviene usar QuickSort cuando:

```txt
hay una coleccion desordenada
se necesita ordenar por criterio
la cantidad de datos justifica usar un algoritmo eficiente
se quiere entender o controlar el ordenamiento
```

Ejemplos:

```txt
ranking de jugadores
lista de resultados
orden de prioridades
ordenamiento de metricas
```

---

## Cuando NO conviene usarlo

No conviene usar QuickSort cuando:

```txt
la coleccion es muy pequeña
el lenguaje ya provee un sort suficiente
el ordenamiento ocurre una sola vez y no es critico
se necesita estabilidad garantizada
el costo de implementarlo no aporta valor
```

En proyectos reales, muchas veces conviene usar el ordenamiento del lenguaje.

QuickSort debe entenderse como algoritmo, no como obligacion.

---

## Errores comunes

```txt
usar QuickSort cuando un sort nativo alcanza
ordenar cada frame sin necesidad
confundir criterio de ordenamiento con algoritmo
mezclar ordenamiento con UI
usar mal los indices
no controlar casos base
elegir pivotes malos para datos ya ordenados
usar QuickSort cuando se necesita estabilidad
```

---

## Criterio para una IA

Cuando una IA proponga QuickSort, debe justificar:

```txt
que coleccion se ordena
por que necesita ordenarse
cual es el criterio de comparacion
cada cuanto se ordena
si el sort nativo alcanza
que sistema consume el resultado
```

No alcanza con decir:

```txt
Usar QuickSort para ordenar.
```

Debe explicar por que ese ordenamiento es necesario.

---

## Checklist

Antes de usar QuickSort, revisar:

```txt
¿Hay una coleccion que necesita orden?
¿El criterio esta definido?
¿La coleccion justifica ordenar?
¿El sort nativo alcanza?
¿Se esta ordenando demasiado seguido?
¿La UI esta separada del algoritmo?
¿El sistema consumidor esta separado?
¿Se necesita estabilidad?
```

---

## Regla final

QuickSort no decide prioridades.

QuickSort ordena datos segun un criterio.

```txt
Coleccion
→ criterio
→ QuickSort
→ coleccion ordenada
→ sistema consumidor
```
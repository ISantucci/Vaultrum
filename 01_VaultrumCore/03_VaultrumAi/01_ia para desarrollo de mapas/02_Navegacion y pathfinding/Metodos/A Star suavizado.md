## Definicion

A Star suavizado es una tecnica aplicada sobre una ruta calculada con A Star para reducir puntos innecesarios, mejorar la naturalidad del recorrido o evitar movimientos demasiado angulares.

No reemplaza a A Star.

No es un algoritmo de busqueda completo por si mismo.

No decide comportamientos.

No mueve entidades.

Existe para mejorar una ruta ya calculada cuando esa ruta es valida, pero poco natural o demasiado quebrada.

```txt
A Star
→ calcula ruta

Suavizado
→ mejora la forma de esa ruta
```

---

## Responsabilidad de esta nota

Esta nota explica el suavizado de rutas dentro de un sistema de navegacion.

Su responsabilidad es definir:

```txt
que problema resuelve
que datos necesita
que resultado devuelve
cuando conviene aplicarlo
cuando no conviene aplicarlo
que costo tiene
como validarlo
```

Esta nota no debe reexplicar A Star completo.

A Star vive en la seccion de Algoritmos.

---

## Problema que resuelve

A Star puede devolver rutas correctas pero visualmente poco naturales.

Esto puede pasar cuando la ruta sigue demasiados nodos, celdas o quiebres.

Ejemplo:

```txt
Ruta original:
A → B → C → D → E

Ruta suavizada:
A → C → E
```

La ruta original puede ser valida.

Pero puede generar movimiento artificial.

Pregunta principal:

```txt
¿La ruta funciona, pero tiene puntos innecesarios?
```

---

## Datos que necesita

El suavizado necesita:

```txt
ruta original
lista de nodos o posiciones
criterio para saber si se puede saltear un punto
validacion de obstaculos
validacion de zonas bloqueadas
opcionalmente line of sight
```

El suavizado no debe inventar la ruta.

Debe recibir una ruta previa.

---

## Que devuelve

El suavizado devuelve una ruta modificada.

Puede devolver:

```txt
lista de posiciones simplificada
lista de nodos reducida
ruta igual a la original si no se puede mejorar
ruta invalida si se aplica mal
```

El resultado debe seguir siendo transitable.

No alcanza con que sea mas corta.

Debe respetar las reglas del mapa.

---

## Como funciona

Una forma comun de suavizar es revisar si se pueden saltear puntos intermedios.

Flujo conceptual:

```txt
1. Recibir ruta original.
2. Tomar un punto inicial.
3. Buscar el punto mas lejano alcanzable directamente.
4. Eliminar puntos intermedios innecesarios.
5. Repetir hasta llegar al final.
6. Devolver ruta simplificada.
```

Ejemplo:

```txt
A → B → C → D

Si A puede llegar directo a C:
A → C → D

Si C puede llegar directo a D:
A → C → D
```

---

## Relacion con A Star

A Star calcula la ruta.

El suavizado mejora la ruta.

```txt
A Star
→ ruta valida

Suavizado
→ ruta mas limpia
```

La dependencia correcta es:

```txt
A Star suavizado
→ consume una ruta generada por A Star
```

No al reves.

---

## Relacion con Line of Sight

Line of Sight puede usarse para validar si dos puntos de la ruta pueden conectarse directamente.

Ejemplo:

```txt
¿Puedo ir de A a C sin atravesar obstaculos?

Si
→ puedo saltear B.

No
→ debo conservar B.
```

Line of Sight no pertenece exclusivamente a esta nota.

Es una tecnica transversal que puede ser usada por varios sistemas.

---

## Ejemplo conceptual en pseudocodigo

```txt
rutaSuavizada = []

actual = primer punto

mientras actual no sea el final:
    buscar el punto mas lejano visible desde actual
    agregar ese punto a rutaSuavizada
    actual = ese punto

devolver rutaSuavizada
```

La idea es reducir puntos sin romper la validez de la ruta.

---

## Ejemplo conceptual en codigo

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;

public static class PathSmoother
{
    public static List<Vector3> SmoothPath(
        IReadOnlyList<Vector3> originalPath,
        Func<Vector3, Vector3, bool> hasLineOfSight)
    {
        List<Vector3> smoothedPath = new();

        if (originalPath == null || originalPath.Count == 0)
            return smoothedPath;

        int currentIndex = 0;
        smoothedPath.Add(originalPath[currentIndex]);

        while (currentIndex < originalPath.Count - 1)
        {
            int furthestVisibleIndex = currentIndex + 1;

            for (int i = originalPath.Count - 1; i > currentIndex; i--)
            {
                if (hasLineOfSight(originalPath[currentIndex], originalPath[i]))
                {
                    furthestVisibleIndex = i;
                    break;
                }
            }

            smoothedPath.Add(originalPath[furthestVisibleIndex]);
            currentIndex = furthestVisibleIndex;
        }

        return smoothedPath;
    }
}
```

Este ejemplo no calcula A Star.

Solo recibe una ruta y una funcion de validacion.

Eso mantiene separadas las responsabilidades.

---

## Cuando implementar A Star suavizado

Conviene implementar suavizado cuando:

```txt
A Star ya devuelve rutas validas
la ruta tiene demasiados quiebres
el movimiento se ve artificial
el agente deberia moverse de forma mas natural
el mapa permite conexiones directas entre puntos
existe una validacion confiable entre puntos
la mejora visual justifica el costo
```

Ejemplo correcto:

```txt
Un NPC calcula ruta por nodos.

La ruta funciona, pero el personaje dobla en cada nodo y se ve robotico.

→ A Star suavizado puede tener sentido.
```

---

## Cuando NO implementar A Star suavizado

No conviene implementar suavizado cuando:

```txt
la ruta ya se ve bien
el movimiento debe respetar estrictamente la grilla
los puntos intermedios representan decisiones obligatorias
no hay validacion confiable de obstaculos
el agente debe pasar si o si por ciertos nodos
el costo tecnico no aporta valor
```

Ejemplo:

```txt
Juego tactico por turnos donde la unidad debe moverse celda por celda.

→ Suavizar la ruta podria romper la lectura del sistema.
```

---

## Por que no implementarlo de mas

El suavizado agrega otra capa de validacion.

Puede generar problemas si se aplica sin criterio:

```txt
rutas que atraviesan paredes
saltos sobre zonas bloqueadas
agentes que ignoran puntos importantes
inconsistencias entre ruta logica y movimiento visual
debug mas dificil
mayor costo de CPU
```

Regla:

```txt
Una ruta mas corta no siempre es una ruta mejor.
```

---

## Mala practica al implementar suavizado

Malas practicas comunes:

```txt
suavizar sin validar obstaculos
eliminar puntos obligatorios
aplicar suavizado siempre aunque no haga falta
hacer line of sight cada frame sin control
mezclar suavizado con movimiento
mezclar suavizado con decision de NPC
no comparar ruta original contra ruta suavizada
no debuggear puntos eliminados
```

Ejemplo de mala practica:

```txt
A Star devuelve:
A → B → C

B representa una puerta obligatoria.

El suavizado elimina B.

Resultado:
A → C atravesando una pared.
```

---

## Costos de implementacion

Implementar suavizado requiere:

```txt
tener una ruta previa
definir criterio para saltear puntos
validar obstaculos
validar reglas de mapa
comparar ruta original y ruta final
debuggear puntos eliminados
probar casos borde
```

No es solamente borrar nodos intermedios.

Cada punto eliminado debe seguir produciendo una ruta valida.

---

## Costos de optimizacion

El suavizado puede tener costo si se ejecuta muchas veces.

Costos posibles:

```txt
CPU por validaciones entre puntos
CPU por line of sight
allocations si se crean listas nuevas
costo extra si se suavizan rutas largas
picos si muchos agentes suavizan al mismo tiempo
```

Problemas frecuentes:

```txt
suavizar cada frame
validar demasiados pares de puntos
usar raycasts sin control
crear nuevas listas constantemente
suavizar rutas que no cambiaron
```

---

## Criterio de optimizacion

Opciones para reducir costo:

```txt
suavizar solo cuando se calcula una ruta nueva
cachear la ruta suavizada
limitar la cantidad de puntos evaluados
reutilizar listas internas
evitar suavizar rutas cortas
distribuir calculos si hay muchos agentes
usar suavizado solo en agentes donde aporta valor visible
```

Ejemplo:

```txt
Mala practica:
cada NPC recalcula y suaviza ruta en Update.

Mejor:
recalcular y suavizar solo cuando cambia el destino,
cuando la ruta queda invalida,
o en intervalos controlados.
```

---

## Preguntas antes de implementar

Antes de implementar suavizado, una IA debe responder:

```txt
¿La ruta actual es valida?
¿El problema es visual o funcional?
¿La ruta tiene demasiados quiebres?
¿Los puntos intermedios son opcionales?
¿Existe validacion confiable entre puntos?
¿Line of Sight es necesario?
¿La ruta suavizada respeta obstaculos?
¿Cuantos agentes lo usan?
¿Cada cuanto se suaviza?
¿El costo se justifica?
¿Como se va a debuggear?
```

Si estas preguntas no tienen respuesta, todavia no conviene implementarlo.

---

## Errores comunes

```txt
tratar suavizado como pathfinding completo
suavizar rutas invalidas
eliminar puntos obligatorios
no validar obstaculos
no validar reglas de mapa
hacer demasiadas validaciones
confundir naturalidad visual con ruta correcta
no mostrar debug visual
```

---

## Criterio para una IA

Cuando una IA proponga A Star suavizado, debe justificar:

```txt
por que A Star simple no alcanza
que problema genera la ruta actual
que puntos pueden eliminarse
como se valida el salto entre puntos
que costo tiene
que sistema consume la ruta suavizada
como se compara antes y despues
```

No alcanza con decir:

```txt
Suavizar la ruta.
```

Debe explicar por que el suavizado aporta valor real.

---

## Checklist

Antes de implementar A Star suavizado, revisar:

```txt
¿Existe una ruta previa?
¿La ruta previa es valida?
¿La ruta tiene quiebres innecesarios?
¿Los puntos intermedios son opcionales?
¿Existe validacion de obstaculos?
¿La ruta suavizada respeta reglas del mapa?
¿El suavizado se calcula con frecuencia controlada?
¿Puede generar allocations frecuentes?
¿Se compara ruta original contra ruta suavizada?
¿Se puede debuggear visualmente?
```

---

## Regla final

A Star suavizado no calcula la intencion.

No reemplaza el algoritmo.

No mueve al agente.

```txt
Ruta valida
→ suavizado
→ ruta mas limpia
→ sistema consumidor
```
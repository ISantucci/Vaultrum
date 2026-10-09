## Definicion

La seleccion ponderada es una tecnica de decision que permite elegir entre varias opciones usando pesos, prioridades o probabilidades relativas.

En IA para NPCs, sirve cuando varias acciones posibles compiten entre si y no alcanza con una condicion fija.

```txt
Opcion A
→ peso 10

Opcion B
→ peso 30

Opcion C
→ peso 60
```

Cuanto mayor es el peso, mayor probabilidad o prioridad tiene una opcion.

La seleccion ponderada no implica azar obligatorio.

Puede usarse para probabilidad, utilidad o prioridad.

---

## Responsabilidad

La responsabilidad de la seleccion ponderada es elegir una opcion entre varias candidatas considerando su peso.

Debe responder:

```txt
¿Que opcion conviene elegir entre varias posibilidades?
```

Puede usarse para:

```txt
elegir comportamiento
elegir ataque
elegir punto de patrulla
elegir objetivo
elegir reaccion
elegir dialogo
elegir tactica
```

No debe ejecutar directamente la accion elegida.

---

## Que NO debe hacer

La seleccion ponderada no debe:

```txt
mover al NPC
aplicar daño
detectar objetivos
calcular rutas
ejecutar comportamiento completo
modificar UI
resolver toda la IA
```

Ejemplo incorrecto:

```txt
WeightedSelector
→ calcula pesos
→ mueve NPC
→ ataca
→ cambia animacion
```

Ejemplo correcto:

```txt
WeightedSelector
→ devuelve opcion elegida.

Sistema de decision
→ interpreta la opcion.

Comportamiento
→ ejecuta la accion.
```

Regla:

```txt
Seleccion ponderada elige.
No ejecuta.
```

---

## Que problema resuelve

La seleccion ponderada ayuda cuando una decision no deberia ser completamente fija.

Ejemplos:

```txt
enemigo puede atacar, reposicionarse o defender
animal puede huir o investigar
NPC puede elegir punto de patrulla
boss puede elegir entre varios ataques
aliado puede elegir a quien asistir
```

Sin ponderacion, la IA puede volverse demasiado predecible.

Con ponderacion, se puede generar variedad controlada.

---

## Datos que necesita

La seleccion ponderada puede necesitar:

```txt
lista de opciones
peso de cada opcion
condiciones de validez
contexto actual
random si se usa probabilidad
prioridades dinamicas
```

Ejemplo:

```txt
Ataque rapido
→ peso 50

Ataque fuerte
→ peso 20

Reposicionarse
→ peso 30
```

Los pesos pueden ser fijos o calculados segun contexto.

---

## Que produce

La seleccion ponderada puede producir:

```txt
opcion elegida
peso total
lista de opciones validas
motivo o contexto de eleccion
```

Ejemplo:

```txt
SelectedOption = HeavyAttack
Weight = 20
```

Eso no significa que la seleccion ejecute el ataque.

Solo indica que esa opcion fue elegida.

---

## Como funciona

Un selector ponderado simple:

```txt
1. Recibir opciones con peso.
2. Filtrar opciones invalidas.
3. Sumar pesos.
4. Elegir un valor entre 0 y peso total.
5. Recorrer opciones hasta encontrar la seleccionada.
6. Devolver opcion.
```

Ejemplo conceptual:

```csharp
using System;
using System.Collections.Generic;

public class WeightedOption<T>
{
    public T Value { get; }
    public int Weight { get; }

    public WeightedOption(T value, int weight)
    {
        Value = value;
        Weight = weight;
    }
}

public class WeightedSelector<T>
{
    private readonly Random random = new Random();

    public T Select(IReadOnlyList<WeightedOption<T>> options)
    {
        int totalWeight = 0;

        foreach (var option in options)
        {
            if (option.Weight > 0)
            {
                totalWeight += option.Weight;
            }
        }

        if (totalWeight <= 0)
        {
            throw new InvalidOperationException("No valid weighted options.");
        }

        int roll = random.Next(0, totalWeight);
        int current = 0;

        foreach (var option in options)
        {
            if (option.Weight <= 0)
            {
                continue;
            }

            current += option.Weight;

            if (roll < current)
            {
                return option.Value;
            }
        }

        return options[0].Value;
    }
}
```

Este selector solo devuelve una opcion.

No sabe si la opcion es ataque, patrulla o dialogo.

---

## Como aplicarlo en videojuegos

La seleccion ponderada puede aplicarse para:

```txt
elegir ataque de boss
elegir punto de patrulla
elegir reaccion de NPC
elegir objetivo prioritario
elegir comportamiento secundario
elegir frase de dialogo
elegir tactica enemiga
```

Ejemplo:

```txt
Boss con tres ataques:

Ataque rapido
→ peso 50

Ataque pesado
→ peso 20

Ataque de area
→ peso 30
```

Esto genera variedad sin perder control.

---

## Cuando conviene implementarlo

Conviene usar seleccion ponderada cuando:

```txt
hay varias opciones validas
se busca variedad controlada
no conviene elegir siempre lo mismo
las opciones tienen distinta prioridad
el diseño necesita comportamiento menos predecible
```

Pregunta clave:

```txt
¿Hay varias opciones correctas, pero algunas deben ser mas probables que otras?
```

Si la respuesta es si, seleccion ponderada puede aportar valor.

---

## Cuando NO conviene implementarlo

No conviene usar seleccion ponderada si:

```txt
hay una decision claramente correcta
el NPC debe ser completamente predecible
el jugador necesita leer un patron fijo
una condicion simple alcanza
un arbol de decision es mas claro
el azar puede volver injusta la experiencia
```

Ejemplos:

```txt
si el jugador esta en rango de ataque melee
→ atacar puede ser decision directa.

si el NPC tiene 5% de vida
→ huir puede ser prioridad fija.
```

Regla:

```txt
No usar azar donde el diseño necesita claridad.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
usar pesos sin criterio
hacer todo aleatorio
no filtrar opciones invalidas
permitir ataques imposibles
elegir una opcion sin feedback
no poder explicar por que salio una opcion
usar seleccion ponderada para ocultar mala decision
```

Ejemplo de mala practica:

```txt
El boss elige ataque de area aunque el jugador esta lejisimos y no puede impactar.
```

Problema:

```txt
La opcion era invalida, pero el selector no lo sabia.
```

---

## Costos de implementacion

La seleccion ponderada puede requerir:

```txt
estructura de opciones
pesos
filtros de validez
random o funcion de utilidad
debug de seleccion
balance de valores
```

El mayor costo suele ser de diseño, no tecnico.

Hay que ajustar pesos hasta que el comportamiento se sienta bien.

---

## Costos de optimizacion

Normalmente es barata.

Puede volverse costosa si:

```txt
hay muchisimas opciones
los pesos se calculan con consultas caras
se recalcula todo cada frame
cada opcion evalua sensores o pathfinding
```

Alternativas:

```txt
precalcular pesos
actualizar por eventos
filtrar opciones antes
evaluar por intervalos
cachear contexto
```

---

## Criterio de optimizacion

Antes de optimizar seleccion ponderada, revisar:

```txt
cantidad de opciones
frecuencia de seleccion
costo de calcular cada peso
si las opciones se filtran antes
si el contexto ya esta preparado
```

Criterio:

```txt
pocas opciones con pesos fijos
→ costo bajo.

muchas opciones con pesos dinamicos caros
→ posible problema.
```

---

## Validacion

La seleccion ponderada se valida revisando:

```txt
si las opciones invalidas quedan fuera
si los pesos reflejan la intencion de diseño
si la distribucion real coincide con lo esperado
si no hay una opcion dominante por error
si el jugador entiende el resultado
si el comportamiento no se siente injusto
```

Debug util:

```txt
mostrar opciones candidatas
mostrar pesos
mostrar roll elegido
registrar opcion final
probar muchas selecciones y contar resultados
```

---

## Preguntas antes de implementarlo

Antes de implementar seleccion ponderada, preguntar:

```txt
¿Hay varias opciones validas?
¿Los pesos tienen criterio de diseño?
¿Las opciones invalidas se filtran?
¿El azar mejora la experiencia?
¿El jugador necesita previsibilidad?
¿La seleccion debe ser probabilistica o por utilidad?
¿Cada cuanto se recalcula?
¿Se puede debuggear el resultado?
```

---

## Errores comunes

Errores comunes:

```txt
usar pesos arbitrarios
no filtrar opciones invalidas
convertir decisiones claras en azar
hacer comportamiento injusto
no validar distribucion
no poder reproducir o debuggear decisiones
recalcular pesos caros cada frame
usar seleccion ponderada donde un arbol era mas claro
```

---

## Criterio para una IA

Cuando una IA trabaje con seleccion ponderada debe:

```txt
mantenerla como tecnica de decision
no convertirla en ejecucion completa
separar opcion, peso y accion
explicar si se usa probabilidad, prioridad o utilidad
filtrar opciones invalidas
marcar cuando conviene y cuando no
considerar balance y validacion
respetar navegacion waterfall
```

Regla operativa:

```txt
La seleccion ponderada sirve para variedad controlada.
No para reemplazar criterio de diseño.
```

---

## Checklist

Antes de implementar seleccion ponderada, revisar:

```txt
¿Hay varias opciones validas?
¿Cada opcion tiene peso claro?
¿Los pesos responden al diseño?
¿Se filtran opciones invalidas?
¿El resultado puede debuggearse?
¿La distribucion se puede validar?
¿El azar aporta valor?
¿La decision necesita ser predecible?
¿Una condicion simple alcanza?
```

---

## Regla final

```txt
Seleccion ponderada no significa elegir al azar sin criterio.

Significa controlar la probabilidad o prioridad de opciones validas.
```
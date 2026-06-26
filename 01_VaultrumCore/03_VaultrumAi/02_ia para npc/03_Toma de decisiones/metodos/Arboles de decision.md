## Definicion

Un arbol de decision es una estructura que permite elegir una accion evaluando condiciones en forma ordenada.

En IA para NPCs, sirve para decidir que hacer segun informacion disponible.

```txt
Condicion
→ pregunta sobre el contexto.

Rama
→ camino segun resultado.

Hoja
→ accion o decision final.
```

Ejemplo:

```txt
¿Veo al jugador?
├── si → ¿Esta en rango de ataque?
│   ├── si → atacar
│   └── no → perseguir
└── no → patrullar
```

Un arbol de decision decide.

No ejecuta por si solo todo el comportamiento.

---

## Responsabilidad

La responsabilidad de un arbol de decision es elegir una salida a partir de condiciones.

Debe responder:

```txt
¿Que accion conviene segun el estado actual del contexto?
```

Puede evaluar:

```txt
si el jugador fue detectado
distancia al objetivo
vida actual
amenaza cercana
cooldown disponible
ultima posicion conocida
prioridad actual
```

Su salida deberia ser clara:

```txt
patrullar
perseguir
atacar
huir
investigar
esperar
```

---

## Que NO debe hacer

Un arbol de decision no debe:

```txt
mover al NPC directamente
aplicar daño
calcular rutas
detectar sensores por si mismo
contener toda la implementacion de cada accion
actualizar UI
resolver animaciones completas
```

Ejemplo incorrecto:

```txt
DecisionTree
→ detecta jugador
→ mueve NPC
→ calcula ruta
→ aplica daño
→ reproduce animacion
```

Ejemplo correcto:

```txt
DecisionTree
→ evalua condiciones
→ devuelve accion recomendada

Sistema de comportamiento
→ ejecuta accion elegida
```

Regla:

```txt
El arbol decide.
No ejecuta todo.
```

---

## Que problema resuelve

Los arboles de decision ayudan a ordenar decisiones con condiciones claras.

Sin una estructura, la decision puede quedar como condicionales mezclados.

Ejemplo debil:

```txt
if jugador
if vida
if rango
if cooldown
if patrulla
```

Con arbol:

```txt
¿Estoy muerto?
→ muerto

¿Tengo poca vida?
→ huir

¿Veo jugador?
→ atacar o perseguir

Si no
→ patrullar
```

Esto mejora lectura, depuracion y diseño.

---

## Datos que necesita

Un arbol de decision puede necesitar un contexto con datos como:

```txt
jugador detectado
distancia al jugador
vida actual
vida maxima
cooldown de ataque
ultima posicion conocida
amenaza cercana
estado actual
```

El arbol no deberia buscar todos esos datos por si mismo.

Lo ideal es recibir un contexto preparado.

---

## Que produce

Un arbol de decision puede producir:

```txt
accion elegida
estado sugerido
prioridad resultante
motivo de decision
```

Ejemplo:

```txt
Decision = Attack
Reason = Player in range and attack ready
```

La salida puede alimentar estados, comportamientos o sistemas de accion.

---

## Como funciona

Un arbol de decision evalua condiciones hasta llegar a una hoja.

Ejemplo conceptual:

```csharp
public enum NPCAction
{
    Patrol,
    Chase,
    Attack,
    Flee
}

public class NPCDecisionContext
{
    public bool PlayerDetected { get; set; }
    public bool PlayerInAttackRange { get; set; }
    public bool LowHealth { get; set; }
}

public class SimpleDecisionTree
{
    public NPCAction Evaluate(NPCDecisionContext context)
    {
        if (context.LowHealth)
        {
            return NPCAction.Flee;
        }

        if (context.PlayerDetected)
        {
            if (context.PlayerInAttackRange)
            {
                return NPCAction.Attack;
            }

            return NPCAction.Chase;
        }

        return NPCAction.Patrol;
    }
}
```

Este ejemplo decide una accion.

No ejecuta la accion.

---

## Como aplicarlo en videojuegos

Los arboles de decision convienen cuando las decisiones pueden organizarse como preguntas claras.

Ejemplos:

```txt
enemigo basico
guardia
animal reactivo
boss con fases simples
NPC aliado con prioridades
```

Ejemplo:

```txt
¿Tengo poca vida?
→ huir

¿Veo jugador?
→ atacar o perseguir

¿Escuche ruido?
→ investigar

Si no
→ patrullar
```

---

## Cuando conviene implementarlo

Conviene usar arboles de decision cuando:

```txt
hay condiciones claras
hay varias acciones posibles
se busca decision legible
se quiere debuggear por que se eligio algo
el comportamiento no necesita aprendizaje ni planificacion compleja
```

Pregunta clave:

```txt
¿Puedo expresar la decision como una secuencia de preguntas?
```

Si la respuesta es si, un arbol de decision puede ser una buena solucion.

---

## Cuando NO conviene implementarlo

No conviene usar arboles de decision si:

```txt
el NPC tiene una unica accion simple
las decisiones son demasiado dinamicas o ponderadas
hay muchas prioridades que cambian continuamente
el arbol se vuelve enorme y dificil de mantener
la seleccion por peso seria mas adecuada
```

Ejemplos:

```txt
NPC que solo abre dialogo
enemigo que solo avanza
sistema donde muchas opciones compiten por utilidad
```

Regla:

```txt
No usar arbol de decision si la decision no se puede leer como preguntas claras.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
arboles gigantes imposibles de leer
condiciones duplicadas
hojas que ejecutan demasiada logica
mezclar decision con accion
no poder explicar por que se eligio una rama
actualizar el arbol con datos que el NPC no deberia saber
```

Ejemplo de mala practica:

```txt
La hoja Attack mueve, rota, aplica daño y cambia animaciones.
```

Problema:

```txt
La decision queda acoplada a la ejecucion.
```

---

## Costos de implementacion

Un arbol de decision puede requerir:

```txt
contexto de decision
nodos de condicion
nodos de accion
estructura del arbol
debug de ramas
validacion de condiciones
```

Puede implementarse simple con condicionales o mas formal con nodos.

No siempre hace falta una estructura compleja.

---

## Costos de optimizacion

Los arboles suelen ser baratos, pero pueden generar costo si:

```txt
se evaluan muchas veces por frame
cada condicion hace busquedas caras
cada nodo consulta fisica, sensores o pathfinding
se recrea el arbol constantemente
```

Alternativas:

```txt
evaluar por intervalos
preparar contexto antes de evaluar
cachear datos
separar sensores de decision
reutilizar estructura del arbol
```

---

## Criterio de optimizacion

Antes de optimizar arboles de decision, revisar:

```txt
cantidad de NPCs
frecuencia de evaluacion
cantidad de condiciones
costo de cada condicion
si el contexto ya esta preparado
si se recrean nodos innecesariamente
```

Criterio:

```txt
arbol chico con contexto preparado
→ costo bajo.

arbol grande con sensores caros en cada nodo
→ riesgo alto.
```

---

## Validacion

Un arbol de decision se valida revisando:

```txt
si cada condicion responde lo esperado
si las ramas estan ordenadas correctamente
si las acciones elegidas tienen sentido
si no hay ramas imposibles
si no hay condiciones duplicadas
si se puede explicar por que eligio una accion
```

Debug util:

```txt
mostrar accion elegida
mostrar ultima condicion evaluada
logs temporales de ruta tomada
visualizacion del arbol
colores por decision
```

---

## Preguntas antes de implementarlo

Antes de implementar un arbol de decision, preguntar:

```txt
¿Que acciones puede elegir el NPC?
¿Que datos necesita para decidir?
¿Las condiciones son claras?
¿Hay prioridades entre condiciones?
¿La decision puede expresarse como preguntas?
¿Cada hoja devuelve una accion clara?
¿La ejecucion esta separada?
¿El arbol puede crecer demasiado?
¿Una maquina de estados alcanza?
¿Una seleccion ponderada seria mejor?
```

---

## Errores comunes

Errores comunes:

```txt
arbol demasiado grande
condiciones mal ordenadas
mezclar decision con ejecucion
usar datos que el NPC no deberia conocer
duplicar condiciones
no validar ramas
hacer que cada hoja tenga comportamiento completo
evaluar demasiado seguido sin necesidad
```

---

## Criterio para una IA

Cuando una IA trabaje con arboles de decision debe:

```txt
mantenerlos como sistema de decision
no convertirlos en ejecucion completa
separar contexto, condicion y accion resultante
no duplicar sensores
no duplicar comportamientos
explicar entradas y salidas
marcar cuando conviene y cuando no
proponer validacion de ramas
respetar navegacion waterfall
```

Regla operativa:

```txt
Un arbol de decision debe poder leerse como una serie de preguntas.
```

---

## Checklist

Antes de implementar arboles de decision, revisar:

```txt
¿Hay varias acciones posibles?
¿Las condiciones son claras?
¿El contexto esta definido?
¿Las hojas devuelven acciones concretas?
¿La ejecucion esta separada?
¿El arbol se puede explicar?
¿Hay riesgo de arbol gigante?
¿Se puede validar que rama tomo?
¿La solucion simple alcanza?
```

---

## Regla final

```txt
Un arbol de decision no hace cosas.

Elige que cosa conviene hacer.
```
## Definicion

NPC tactico simple es un preset para personajes que eligen entre varias acciones segun contexto, pero sin llegar a una IA compleja o sobrearquitecturada.

```txt
NPC tactico simple
→ evalua contexto
→ elige accion
→ ejecuta comportamiento
```

Sirve cuando el NPC necesita algo mas que atacar directo, pero no necesita un sistema avanzado.

---

## Rol de gameplay

Sirve para NPCs que deben tomar decisiones simples pero relevantes.

Ejemplos:

```txt
enemigo que alterna atacar y cubrirse
aliado que ayuda o se retira
enemigo que evalua distancia
enemigo que persigue si conviene y huye si esta debil
```

---

## Cuando usarlo

Usar este preset cuando:

```txt
hay varias acciones posibles
las decisiones dependen de contexto
las condiciones son claras
el NPC necesita parecer reactivo
se quiere evitar comportamiento monolitico
```

Pregunta clave:

```txt
¿El NPC necesita elegir entre acciones claras segun situacion?
```

---

## Cuando no usarlo

No usarlo si:

```txt
el NPC tiene una sola accion
el NPC necesita IA muy avanzada
el comportamiento se resuelve con un trigger
la decision ponderada seria mas adecuada
el preset agresivo directo alcanza
```

---

## Sistemas necesarios

```txt
arbol de decision o condiciones ordenadas
estados
comportamientos
deteccion basica
movimiento
feedback
```

---

## Sistemas opcionales

```txt
seleccion ponderada
pathfinding
huida
ataque
persecucion
puntos de cobertura
cooldowns
```

---

## Sistemas que NO necesita

Normalmente no necesita:

```txt
planificacion avanzada
behavior tree complejo
IA grupal compleja
aprendizaje automatico
seleccion aleatoria sin criterio
```

---

## Flujo de comportamiento

```txt
1. NPC recibe informacion del contexto.
2. Decision evalua condiciones.
3. Si vida baja, huye o se cubre.
4. Si jugador en rango, ataca.
5. Si jugador detectado pero lejos, persigue.
6. Si no hay objetivo, patrulla o espera.
7. Se ejecuta el comportamiento elegido.
```

---

## Estructura recomendada

```txt
NPCDecisionContext
→ datos actuales.

SimpleDecisionTree
→ elige accion.

NPCStateMachine
→ organiza accion activa.

Behaviours
→ ejecutan patrullaje, persecucion, ataque o huida.

MovementController
→ resuelve desplazamiento.
```

---

## Datos necesarios

```txt
vida actual
jugador detectado
distancia al jugador
rango de ataque
cooldown de ataque
amenaza actual
estado actual
ultima posicion conocida
```

---

## Variantes posibles

```txt
enemigo que huye con poca vida
enemigo que se cubre si esta lejos
aliado que ayuda al jugador
enemigo que persigue o ataca segun distancia
enemigo que alterna entre presion y retirada
```

---

## Costos de implementacion

Costo medio.

Puede requerir:

```txt
contexto de decision
condiciones
estado actual
varios comportamientos
validacion de transiciones
debug de decision
```

El costo aumenta si:

```txt
hay muchas acciones
hay cobertura
hay pathfinding
hay seleccion ponderada
hay grupos
```

---

## Costos de optimizacion

Riesgos:

```txt
evaluar condiciones caras cada frame
consultar sensores desde decision
recalcular rutas sin necesidad
muchos NPCs tacticos activos
```

Alternativas:

```txt
preparar contexto
evaluar por intervalos
separar sensores de decision
limitar pathfinding
cachear referencias
```

---

## Validacion

Validar:

```txt
si elige acciones coherentes
si no cambia de estado todo el tiempo
si las prioridades son correctas
si no usa informacion injusta
si el jugador entiende la reaccion
```

Debug util:

```txt
accion elegida
razon de decision
estado actual
contexto visible
logs de transicion
```

---

## Errores comunes

```txt
hacer decision demasiado compleja
meter percepcion dentro del arbol
mezclar decision con ejecucion
crear estados gigantes
no definir prioridades
cambiar de accion cada frame
```

---

## Criterio para una IA

Cuando una IA use este preset debe:

```txt
mantener decisiones simples
usar contexto preparado
separar decision y comportamiento
definir prioridades claras
evitar estados gigantes
validar razones de decision
```

---

## Checklist

```txt
¿Hay varias acciones posibles?
¿Las condiciones son claras?
¿Hay prioridad definida?
¿La decision esta separada de la ejecucion?
¿El contexto esta preparado?
¿Hay debug de razon de decision?
¿La solucion simple alcanza?
```

---

## Regla final

```txt
Un NPC tactico simple no necesita pensar mucho.

Necesita elegir bien entre pocas opciones claras.
```
## Definicion

NPC agresivo directo es un preset para enemigos que detectan al jugador y lo presionan de forma clara mediante persecucion y ataque.

```txt
NPC agresivo
→ detecta
→ persigue
→ ataca
```

No busca sutileza.

Busca presion directa.

---

## Rol de gameplay

Sirve para enemigos simples, criaturas hostiles o amenazas de accion.

Ejemplos:

```txt
zombie
enemigo melee simple
criatura salvaje
enemigo de arena
minion hostil
```

---

## Cuando usarlo

Usar este preset cuando:

```txt
el NPC debe atacar al jugador
la respuesta debe ser rapida
el combate es directo
la deteccion por rango alcanza
el jugador no necesita sigilo avanzado
```

Pregunta clave:

```txt
¿El NPC debe presionar al jugador de forma simple y clara?
```

---

## Cuando no usarlo

No usarlo si:

```txt
el NPC debe ser tactico
el NPC debe patrullar de forma compleja
el NPC debe tener sigilo justo
el NPC debe elegir ataques variados
el NPC debe huir o conservar vida
```

---

## Sistemas necesarios

```txt
deteccion por rango
persecucion
ataque
movimiento
cooldown de ataque
estado simple
```

---

## Sistemas opcionales

```txt
pathfinding
obstacle avoidance
Field of View
steering
animacion de ataque
feedback de alerta
```

---

## Sistemas que NO necesita

Normalmente no necesita:

```txt
seleccion ponderada
arbol de decision complejo
sospecha progresiva
patrullaje elaborado
huida
memoria compleja
```

---

## Flujo de comportamiento

```txt
1. NPC espera o deambula.
2. Jugador entra en rango de deteccion.
3. NPC persigue al jugador.
4. Si entra en rango de ataque, ataca.
5. Si jugador sale de rango, abandona o vuelve.
6. Repite mientras el objetivo sea valido.
```

---

## Estructura recomendada

```txt
RangeDetector
→ detecta jugador por distancia.

ChaseBehaviour
→ acerca al NPC.

AttackBehaviour
→ ejecuta ataque.

SimpleStateMachine
→ Idle / Chase / Attack.
```

---

## Datos necesarios

```txt
rango de deteccion
velocidad
rango de ataque
daño
cooldown
distancia de abandono
referencia al jugador
```

---

## Variantes posibles

```txt
enemigo melee
enemigo que corre en linea recta
enemigo que usa pathfinding
enemigo que abandona si el jugador se aleja
enemigo que no abandona hasta morir
```

---

## Costos de implementacion

Costo bajo a medio.

Aumenta si:

```txt
requiere pathfinding
hay muchos enemigos
hay ataques con animacion precisa
hay avoidance entre enemigos
```

---

## Costos de optimizacion

Riesgos:

```txt
muchos enemigos recalculando ruta
chequeos de rango por frame en masa
ataques con hitboxes mal controladas
instanciacion de efectos
```

Alternativas:

```txt
chequeos por intervalo
pooling
pathfinding limitado
cache de objetivo
LOD de IA
```

---

## Validacion

Validar:

```txt
si detecta en rango correcto
si persigue al objetivo correcto
si ataca solo en rango
si respeta cooldown
si abandona cuando corresponde
si no se traba con obstaculos
```

---

## Errores comunes

```txt
atacar fuera de rango
perseguir para siempre sin regla
recalcular ruta cada frame
mezclar deteccion, persecucion y ataque en una sola clase
no dar feedback de ataque
```

---

## Criterio para una IA

Cuando una IA use este preset debe:

```txt
mantenerlo simple
priorizar claridad de combate
no agregar sigilo si no aporta
no agregar decision compleja si no hace falta
separar detectar, perseguir y atacar
```

---

## Checklist

```txt
¿Tiene rango de deteccion?
¿Tiene rango de ataque?
¿Tiene cooldown?
¿Tiene condicion de abandono?
¿Necesita pathfinding?
¿Necesita feedback?
¿La persecucion esta separada del ataque?
```

---

## Regla final

```txt
Un NPC agresivo directo debe ser claro, no sofisticado.
```
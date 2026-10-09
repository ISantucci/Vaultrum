## Definicion

NPC de sigilo es un preset para personajes que deben detectar al jugador de forma justa, legible y dependiente de informacion perceptible.

```txt
NPC de sigilo
→ patrulla
→ percibe
→ sospecha o detecta
→ investiga, persigue o alerta
```

Su objetivo no es saber todo.

Su objetivo es reaccionar segun lo que puede percibir.

---

## Rol de gameplay

Sirve para crear tension, riesgo y lectura espacial.

Ejemplos:

```txt
guardia de stealth
camara de seguridad
enemigo que investiga ruidos
vigilante de zona restringida
```

---

## Cuando usarlo

Usar este preset cuando:

```txt
el jugador puede esconderse
la vision direccional importa
la deteccion debe ser justa
la posicion y cobertura importan
el NPC debe investigar o perseguir
el jugador debe entender el riesgo
```

Pregunta clave:

```txt
¿El jugador necesita poder evitar ser detectado mediante posicion, cobertura o timing?
```

---

## Cuando no usarlo

No usar este preset si:

```txt
el NPC siempre debe conocer al jugador
el juego es de accion directa
la vision direccional no aporta
la deteccion por rango alcanza
no hay cobertura ni sigilo
```

---

## Sistemas necesarios

```txt
Field of View
deteccion del jugador
patrullaje
estados
persecucion
feedback de alerta
memoria de ultima posicion
```

---

## Sistemas opcionales

```txt
sospecha progresiva
investigacion
ataque
pathfinding
sonido
zonas de alerta
line of sight
```

---

## Sistemas que NO necesita

Normalmente no necesita:

```txt
seleccion ponderada
ataques variados
steering avanzado
huida
IA grupal compleja
```

Regla:

```txt
En sigilo, la justicia y la legibilidad pesan mas que la complejidad.
```

---

## Flujo de comportamiento

```txt
1. NPC patrulla.
2. Field of View revisa si el jugador es visible.
3. Deteccion confirma o incrementa sospecha.
4. Si la deteccion se confirma, cambia a persecucion o alerta.
5. Si pierde al jugador, guarda ultima posicion conocida.
6. Puede investigar esa posicion.
7. Si no encuentra nada, vuelve a patrullar.
8. Si entra en rango, puede atacar o alertar.
```

---

## Estructura recomendada

```txt
VisionSensor
→ detecta visibilidad.

PlayerDetector
→ combina vision, rango, ruido o memoria.

NPCStateMachine
→ organiza Patrol, Suspicious, Investigate, Chase, Attack.

PatrolBehaviour
→ rutina base.

ChaseBehaviour
→ seguimiento del jugador o ultima posicion.

AlertFeedback
→ comunica sospecha o deteccion.
```

---

## Datos necesarios

```txt
rango de vision
angulo de vision
mascara de obstaculos
tiempo de sospecha
tiempo de memoria
ultima posicion conocida
rango de ataque o alerta
puntos de patrulla
feedback visual o sonoro
```

---

## Variantes posibles

```txt
guardia con deteccion instantanea
guardia con sospecha progresiva
camara fija con cono de vision
enemigo que investiga ruidos
guardia que alerta a otros
guardia que vuelve a patrullar
```

---

## Costos de implementacion

Costo medio a alto.

Puede requerir:

```txt
FOV
raycasts
estados
memoria
feedback
patrullaje
persecucion
validacion con obstaculos
```

El costo aumenta si:

```txt
hay sonido
hay sospecha progresiva
hay alertas grupales
hay pathfinding
hay varios guardias
```

---

## Costos de optimizacion

Riesgos:

```txt
raycasts frecuentes
muchos NPCs con FOV activo
pathfinding al perseguir
debug visual permanente
sistemas de alerta global mal controlados
```

Alternativas:

```txt
actualizar sensores por intervalos
filtrar por distancia antes de raycast
usar LOD de IA
activar FOV solo en zonas relevantes
limitar recalculos de ruta
```

---

## Validacion

Validar:

```txt
si no detecta a traves de paredes
si respeta angulo
si respeta distancia
si el jugador entiende cuando esta en riesgo
si la sospecha sube y baja correctamente
si la ultima posicion conocida funciona
si vuelve a patrullar
```

Debug util:

```txt
cono de vision
linea de raycast
estado actual
nivel de sospecha
ultima posicion conocida
ruta actual
```

---

## Errores comunes

```txt
deteccion instantanea sin feedback
detectar a traves de paredes
saber magicamente donde esta el jugador
mezclar FOV con ataque
no guardar ultima posicion
no definir retorno a patrulla
hacer sistemas de alerta imposibles de depurar
```

---

## Criterio para una IA

Cuando una IA use este preset debe:

```txt
priorizar justicia y legibilidad
separar percepcion y decision
usar FOV solo si la vision importa
no hacer que el NPC sepa todo
incluir feedback de alerta
validar con gizmos
considerar costos de raycasts
```

---

## Checklist

```txt
¿Hay sigilo real?
¿El jugador puede esconderse?
¿El FOV esta definido?
¿Hay obstaculos que bloquean vision?
¿Hay feedback de sospecha o alerta?
¿Hay ultima posicion conocida?
¿Hay retorno a patrulla?
¿La deteccion se siente justa?
```

---

## Regla final

```txt
Un NPC de sigilo no debe ser omnisciente.

Debe ser justo, legible y consistente.
```
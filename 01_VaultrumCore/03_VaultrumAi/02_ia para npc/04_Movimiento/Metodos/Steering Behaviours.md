## Definición

**Steering Behaviours** son técnicas de movimiento que permiten dirigir un agente mediante fuerzas, direcciones o tendencias de desplazamiento.

Se usan para producir movimientos más suaves, reactivos u orgánicos que un desplazamiento directo.

```txt
Steering
→ recibe una intención de movimiento
→ calcula una dirección, velocidad o fuerza deseada
→ entrega una salida para que el movimiento la ejecute
```

Steering no decide por qué el NPC se mueve.

Steering define cómo debería moverse una vez que ya existe una intención.

---

## Responsabilidad

La responsabilidad de Steering Behaviours es transformar una intención de movimiento en una salida utilizable por el sistema de movimiento.

Debe responder:

```txt
¿Hacia dónde debería moverse el agente?
¿Con qué intensidad?
¿Debe llegar suavemente?
¿Debe alejarse?
¿Debe seguir algo?
¿Debe evitar algo?
¿Debe combinar varias tendencias de movimiento?
```

Su salida puede ser:

```txt
dirección deseada
velocidad deseada
fuerza de steering
aceleración sugerida
rotación sugerida
```

La salida de steering no es una decisión completa.

Es una sugerencia de movimiento.

---

## Capas de movimiento

Una forma sana de entender steering es separarlo en capas:

```txt
Selección de acción
→ define qué quiere hacer el agente.

Steering
→ calcula cómo debería moverse para cumplir esa intención.

Locomoción
→ ejecuta físicamente el movimiento.
```

Ejemplo:

```txt
Toma de decisiones
→ decide perseguir al jugador.

Comportamiento
→ solicita moverse hacia el jugador.

Steering
→ calcula una dirección deseada hacia el jugador.

Movimiento / locomoción
→ aplica desplazamiento, velocidad, rotación o animación.
```

Esta separación evita que steering absorba responsabilidades que no le corresponden.

---

## Qué NO debe hacer

Steering no debe:

```txt
decidir comportamiento
detectar jugador
elegir estado
calcular pathfinding completo
aplicar daño
resolver combate
controlar toda la animación
reemplazar locomoción
```

Ejemplo incorrecto:

```txt
SteeringBehaviour
→ detecta jugador
→ decide perseguir
→ calcula ruta completa
→ mueve
→ ataca
```

Ejemplo correcto:

```txt
Comportamiento
→ pide moverse hacia un objetivo.

Steering
→ calcula dirección o fuerza deseada.

Movimiento
→ aplica desplazamiento.
```

Regla:

```txt
Steering resuelve cómo moverse.

No resuelve por qué moverse.
```

---

## Qué problema resuelve

Steering ayuda a evitar movimientos rígidos, secos o artificiales.

Puede aportar cuando un NPC necesita:

```txt
seguir un objetivo suavemente
llegar sin pasarse
huir de una amenaza
vagar por el escenario
perseguir objetivos en movimiento
evitar amontonamiento
moverse en grupo
ajustar trayectoria de forma reactiva
```

Sin steering, muchos movimientos quedan como:

```txt
ir en línea recta
frenar de golpe
girar instantáneamente
chocar con otros agentes
moverse de forma poco natural
```

---

## Datos que necesita

Steering puede necesitar:

```txt
posición actual
velocidad actual
velocidad máxima
aceleración máxima
objetivo
distancia de frenado
masa o peso
delta time
vecinos cercanos
obstáculos cercanos
```

Depende del tipo de steering usado.

Ejemplos:

```txt
Seek
→ posición actual
→ posición objetivo
→ velocidad máxima

Arrive
→ posición actual
→ posición objetivo
→ radio de frenado

Separation
→ vecinos cercanos
→ distancia mínima
```

---

## Qué produce

Steering puede producir:

```txt
dirección deseada
velocidad deseada
fuerza de movimiento
aceleración
rotación sugerida
```

Ejemplo conceptual:

```txt
DesiredVelocity = dirección hacia objetivo * velocidad máxima
```

Eso no significa que el NPC haya decidido perseguir.

Solo significa que el sistema de movimiento sabe hacia dónde convendría desplazarse.

---

## Tipos comunes

### Seek

Busca moverse hacia un objetivo.

Uso común:

```txt
perseguir una posición
seguir un punto de ruta
acercarse a un aliado
ir hacia un objetivo seleccionado
```

---

### Flee

Busca alejarse de una amenaza.

Uso común:

```txt
huida
evasión de peligro
mantener distancia
alejarse del jugador
```

---

### Arrive

Busca acercarse a un objetivo y frenar suavemente al llegar.

Uso común:

```txt
llegar sin pasarse
detenerse cerca del jugador
estacionarse en una posición
seguir puntos de ruta con llegada controlada
```

---

### Wander

Busca generar movimiento semi-aleatorio o exploratorio.

Uso común:

```txt
animales
civiles
NPCs ambientales
enemigos en estado de búsqueda
```

---

### Pursuit

Busca perseguir un objetivo considerando su movimiento.

Uso común:

```txt
enemigos que persiguen objetivos móviles
misiles simples
criaturas rápidas
unidades que interceptan
```

---

### Evade

Busca escapar de un perseguidor considerando su movimiento.

Uso común:

```txt
NPCs evasivos
enemigos débiles
unidades que mantienen distancia
```

---

### Separation

Busca alejarse de vecinos cercanos.

Uso común:

```txt
evitar amontonamiento
grupos de enemigos
multitudes
unidades que no deben superponerse
```

---

### Alignment

Busca orientar o mover al agente en una dirección similar a la de sus vecinos.

Uso común:

```txt
grupos
bandadas
formaciones orgánicas
movimiento colectivo
```

---

### Cohesion

Busca acercar al agente al centro del grupo.

Uso común:

```txt
bandadas
enjambres
grupos de criaturas
unidades que se mantienen juntas
```

---

## Relación con Flocking

Flocking puede entenderse como una aplicación grupal de Steering Behaviours.

Combina tendencias como:

```txt
Separation
Alignment
Cohesion
```

para coordinar movimiento entre varios agentes.

Steering Behaviours explica las técnicas generales de movimiento.

Flocking desarrolla el caso específico de movimiento grupal.

No hace falta duplicar Flocking dentro de esta nota.

---

## Relación con pathfinding

Steering y pathfinding pueden complementarse, pero no son lo mismo.

```txt
Pathfinding
→ calcula una ruta.

Steering
→ ajusta el movimiento hacia el siguiente objetivo o punto de ruta.

Movimiento
→ ejecuta el desplazamiento.
```

Ejemplo:

```txt
Pathfinding devuelve una lista de puntos.

Steering calcula cómo avanzar hacia el próximo punto de forma suave.

Movimiento aplica velocidad, rotación o desplazamiento.
```

Steering no debería calcular toda la ruta.

Pathfinding no debería encargarse del movimiento físico fino.

---

## Cuándo conviene usarlo

Conviene usar Steering Behaviours cuando:

```txt
el movimiento directo se ve rígido
el agente debe ajustar trayectoria suavemente
hay objetivos en movimiento
se necesita llegada suave
se necesita movimiento orgánico
hay varios agentes cerca
se quiere evitar superposición entre agentes
```

Pregunta clave:

```txt
¿El problema es cómo se mueve el NPC, no qué decisión toma?
```

Si la respuesta es sí, steering puede aportar valor.

---

## Cuándo NO conviene usarlo

No conviene usar steering si:

```txt
el movimiento simple alcanza
el NPC no se desplaza
el movimiento es por grilla estricta
el juego necesita movimiento exacto por casillas
el costo no se justifica
el movimiento orgánico no aporta al gameplay
```

Ejemplos:

```txt
comerciante estático
NPC de diálogo
torreta fija
enemigo que sigue waypoints simples
juego por turnos en grilla estricta
```

Regla:

```txt
No agregar steering si el movimiento básico ya cumple el rol.
```

---

## Riesgos comunes

Riesgos comunes al implementar steering:

```txt
usar steering para decidir estados
mezclar steering con pathfinding completo
aplicar muchas fuerzas sin control
no limitar velocidad
no controlar aceleración
ignorar delta time
sumar comportamientos incompatibles
no depurar la dirección resultante
calcular vecinos de forma costosa
```

El riesgo crece cuando se combinan muchos steering behaviours al mismo tiempo.

Ejemplo:

```txt
Seek solo
→ bajo costo.

Seek + avoidance + separation + arrive
→ más complejo.
```

---

## Validación

Steering se valida revisando:

```txt
si el NPC se mueve hacia donde corresponde
si la velocidad está controlada
si no vibra
si no se pasa del objetivo
si no se queda trabado
si los vectores tienen sentido
si el movimiento se entiende desde gameplay
```

Debug útil:

```txt
vector de velocidad
vector deseado
vector final
radio de llegada
vecinos detectados
dirección resultante
```

---

## Regla final

Steering no decide.

Steering transforma una intención de movimiento en una dirección, velocidad o fuerza más orgánica.

Primero intención.

Después steering.

Después movimiento.
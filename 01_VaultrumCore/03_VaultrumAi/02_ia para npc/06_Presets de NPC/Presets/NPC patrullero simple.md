## Definicion

NPC patrullero simple es un preset para personajes que recorren puntos, rutas o zonas con un patron claro y predecible.

```txt
NPC patrullero simple
→ sigue ruta
→ espera si corresponde
→ repite
```

Puede reaccionar al jugador, pero su base es una rutina de patrullaje entendible.

---

## Rol de gameplay

Sirve para crear presencia, vigilancia, ritmo o lectura espacial.

Ejemplos:

```txt
guardia basico
enemigo de pasillo
camara movil
NPC que recorre una zona
```

El jugador puede observar el patron y actuar en consecuencia.

---

## Cuando usarlo

Usar este preset cuando:

```txt
el NPC debe moverse por una ruta clara
el jugador debe poder leer el recorrido
la vigilancia importa
el mapa necesita actividad
el comportamiento debe ser simple y mantenible
```

Pregunta clave:

```txt
¿El recorrido del NPC aporta gameplay o lectura del espacio?
```

---

## Cuando no usarlo

No usar este preset si:

```txt
el NPC debe quedarse fijo
el NPC necesita variedad fuerte
el NPC necesita decisiones tacticas
el NPC debe navegar libremente zonas complejas
el patrullaje no aporta al gameplay
```

---

## Sistemas necesarios

```txt
patrullaje
waypoints
movimiento simple
estado actual
tiempo de espera opcional
debug de ruta
```

---

## Sistemas opcionales

```txt
deteccion del jugador
Field of View
persecucion
ataque
estado Patrol / Chase / Attack
pathfinding si los puntos no son directos
```

---

## Sistemas que NO necesita

Normalmente no necesita:

```txt
seleccion ponderada
arbol de decision complejo
steering avanzado
huida
ataques variados
memoria compleja
```

Regla:

```txt
Si la ruta debe ser clara, no agregar variedad innecesaria.
```

---

## Flujo de comportamiento

```txt
1. NPC inicia en primer punto.
2. Se mueve hacia el waypoint actual.
3. Al llegar, espera si corresponde.
4. Avanza al siguiente waypoint.
5. Repite el recorrido.
6. Si hay deteccion, puede interrumpir patrullaje.
7. Si termina interrupcion, puede volver a patrullar.
```

---

## Estructura recomendada

```txt
PatrolRoute
→ contiene puntos.

PatrolBehaviour
→ administra punto actual y avance.

MovementController
→ mueve al NPC.

NPCStateMachine
→ opcional si hay interrupciones.
```

Separacion esperada:

```txt
ruta
→ define puntos.

patrullaje
→ decide siguiente punto.

movimiento
→ desplaza al NPC.

decision
→ decide si interrumpir patrullaje.
```

---

## Datos necesarios

```txt
lista de waypoints
indice actual
velocidad
distancia de llegada
tiempo de espera
modo de ruta
```

Modos posibles:

```txt
circular
ida y vuelta
una sola vuelta
```

---

## Variantes posibles

```txt
patrullaje circular
patrullaje ida y vuelta
patrullaje con espera
patrullaje con rotacion en puntos
patrullaje interrumpible por deteccion
```

---

## Costos de implementacion

Costo bajo.

Puede requerir:

```txt
colocar waypoints
crear comportamiento de patrulla
integrar movimiento
validar llegada a puntos
debug visual
```

El costo aumenta si:

```txt
hay interrupciones
hay retorno a ruta
hay deteccion visual
hay pathfinding entre puntos
```

---

## Costos de optimizacion

Normalmente bajo.

Riesgos:

```txt
chequeos innecesarios cada frame
pathfinding recalculado entre puntos fijos
muchos NPCs con debug activo
```

Alternativas:

```txt
waypoints predefinidos
debug solo en editor
pathfinding solo si hace falta
distancia de llegada simple
```

---

## Validacion

Validar:

```txt
si sigue todos los puntos
si respeta el orden
si espera correctamente
si no se traba
si se interrumpe bien
si vuelve a la ruta si corresponde
```

Debug util:

```txt
gizmos de waypoints
lineas de ruta
punto actual visible
logs al cambiar de punto
```

---

## Errores comunes

```txt
no validar lista vacia
mezclar patrullaje con deteccion
hacer ruta imposible
no definir retorno luego de interrupcion
usar pathfinding donde alcanzan waypoints
```

---

## Criterio para una IA

Cuando una IA use este preset debe:

```txt
mantener patrullaje como rutina
no agregar variedad si no aporta
separar ruta y movimiento
definir si puede ser interrumpido
validar visualmente la ruta
```

---

## Checklist

```txt
¿Hay puntos de patrulla?
¿El orden esta claro?
¿Debe esperar?
¿Debe repetir?
¿Debe ser interrumpible?
¿Necesita deteccion?
¿Necesita pathfinding?
¿La ruta aporta al gameplay?
```

---

## Regla final

```txt
Un patrullero simple debe ser legible antes que sorprendente.
```
## Definicion

NPC patrullero con variedad es un preset para personajes que recorren puntos o zonas sin repetir siempre el mismo patron.

Usa variedad controlada mediante seleccion ponderada, memoria o condiciones de validez.

```txt
Patrullaje
→ puntos candidatos
→ pesos
→ memoria
→ siguiente destino
```

No es movimiento aleatorio sin criterio.

---

## Rol de gameplay

Sirve para NPCs que deben sentirse menos mecanicos sin volverse impredecibles o injustos.

Ejemplos:

```txt
guardia que revisa zonas
enemigo que alterna puntos de interes
NPC con rutina variable
personaje que inspecciona areas
```

---

## Cuando usarlo

Usar este preset cuando:

```txt
el patrullaje simple se siente repetitivo
el NPC debe revisar varias zonas
se busca variedad controlada
el jugador no debe memorizar facilmente una ruta exacta
hay puntos de interes con distinta prioridad
```

Pregunta clave:

```txt
¿El NPC necesita variar sin perder intencion de diseño?
```

---

## Cuando no usarlo

No usar este preset si:

```txt
el recorrido debe ser completamente predecible
el jugador necesita leer un patron fijo
hay pocos puntos de patrulla
la variedad no aporta gameplay
un patrullaje simple alcanza
```

---

## Sistemas necesarios

```txt
patrullaje
seleccion ponderada
puntos de interes
memoria de puntos recientes
condiciones de validez
movimiento
```

---

## Sistemas opcionales

```txt
estados
deteccion del jugador
Field of View
pathfinding
tiempos de espera variables
pesos dinamicos
zonas de prioridad
```

---

## Sistemas que NO necesita

Normalmente no necesita:

```txt
arbol de decision complejo
ataques variados
steering avanzado
huida
combate completo
```

Regla:

```txt
La variedad debe estar en la eleccion de destino, no en mezclar toda la IA.
```

---

## Flujo de comportamiento

```txt
1. NPC entra en patrullaje.
2. Se obtienen puntos candidatos.
3. Se descartan puntos invalidos.
4. Se ajustan pesos segun importancia, distancia o repeticion.
5. Se penalizan puntos visitados recientemente.
6. Se elige destino por seleccion ponderada.
7. Movimiento lleva al NPC al punto elegido.
8. Al llegar, espera un tiempo definido o variable.
9. Se registra el punto visitado.
10. Se repite el proceso.
```

---

## Estructura recomendada

```txt
PatrolPoint
→ define punto, peso base e importancia.

PatrolMemory
→ recuerda puntos recientes.

WeightedPatrolSelector
→ elige siguiente punto.

PatrolBehaviour
→ coordina la rutina.

MovementController
→ mueve al NPC.
```

Separacion esperada:

```txt
puntos
→ datos.

selector
→ decide siguiente destino.

memoria
→ evita repeticion.

patrullaje
→ coordina flujo.

movimiento
→ ejecuta desplazamiento.
```

---

## Datos necesarios

```txt
lista de puntos
peso base por punto
peso por importancia
penalizacion por repeticion
cantidad de puntos recordados
tiempo de espera minimo
tiempo de espera maximo
distancia de llegada
```

Ejemplo de pesos:

```txt
punto cercano
→ peso 40

punto importante
→ peso 60

punto visitado recientemente
→ peso 5

punto bloqueado
→ peso 0
```

---

## Variantes posibles

```txt
patrullaje por puntos ponderados
patrullaje por zonas
patrullaje con memoria corta
patrullaje con prioridades dinamicas
patrullaje con eventos del mundo
patrullaje con puntos bloqueados temporalmente
```

---

## Costos de implementacion

Costo medio.

Puede requerir:

```txt
datos por punto
selector ponderado
memoria de visitas
validacion de puntos
debug de pesos
integracion con movimiento
```

El costo aumenta si:

```txt
los pesos son dinamicos
hay eventos que cambian prioridades
hay pathfinding entre puntos
hay multiples NPCs compartiendo zonas
```

---

## Costos de optimizacion

Riesgos:

```txt
recalcular pesos cada frame
evaluar demasiados puntos
hacer pathfinding para todos los candidatos
no cachear datos
usar seleccion ponderada sin filtrar
```

Alternativas:

```txt
elegir nuevo punto solo al llegar
precalcular pesos base
filtrar antes de ponderar
limitar candidatos
recalcular solo cuando cambia el contexto
```

---

## Validacion

Validar:

```txt
si no repite siempre el mismo punto
si no elige puntos invalidos
si respeta prioridades
si el movimiento sigue teniendo sentido
si el jugador percibe variedad
si la variedad no rompe el diseño
```

Debug util:

```txt
mostrar pesos actuales
mostrar punto elegido
historial de puntos visitados
gizmos por prioridad
logs de seleccion
```

---

## Errores comunes

```txt
usar azar puro
no filtrar puntos invalidos
permitir repetir siempre el mismo punto
hacer pesos arbitrarios
no poder debuggear por que eligio un punto
usar variedad donde se necesitaba patron fijo
```

---

## Criterio para una IA

Cuando una IA use este preset debe:

```txt
mantener variedad controlada
usar pesos con criterio
evitar azar puro
incluir memoria si hay repeticion evidente
filtrar puntos invalidos
separar seleccion y movimiento
validar distribucion de elecciones
```

---

## Checklist

```txt
¿Hay varios puntos candidatos?
¿Cada punto tiene peso?
¿Hay condiciones de validez?
¿Se penalizan puntos recientes?
¿La variedad aporta gameplay?
¿El jugador puede entender el comportamiento?
¿Se puede debuggear la eleccion?
¿Un patrullaje simple alcanzaba?
```

---

## Regla final

```txt
La variedad buena no es azar.

Es repeticion controlada con criterio de diseño.
```
## Definicion

NPC evasivo es un preset para personajes que evitan peligro, huyen de amenazas o buscan una posicion segura.

```txt
NPC evasivo
→ detecta amenaza
→ elige escape
→ huye
→ alcanza seguridad
```

No esta pensado para enfrentar al jugador.

---

## Rol de gameplay

Sirve para NPCs que deben preservar su vida o reaccionar con miedo.

Ejemplos:

```txt
civil
animal
enemigo debil
NPC que busca refugio
aliado herido
```

---

## Cuando usarlo

Usar este preset cuando:

```txt
el NPC debe evitar peligro
la amenaza no debe resolverse con combate
el comportamiento de supervivencia aporta gameplay
el mundo debe sentirse reactivo
```

Pregunta clave:

```txt
¿Este NPC deberia escapar en vez de pelear?
```

---

## Cuando no usarlo

No usarlo si:

```txt
el NPC debe ser agresivo siempre
el NPC es una torreta fija
el boss debe sostener combate
la huida confundiria al jugador
no hay espacio para huir
```

---

## Sistemas necesarios

```txt
deteccion de amenaza
huida
movimiento
distancia segura
condicion de salida
feedback de miedo o alerta
```

---

## Sistemas opcionales

```txt
puntos seguros
seleccion ponderada de refugios
pathfinding
obstacle avoidance
estado Flee
memoria de amenaza
```

---

## Sistemas que NO necesita

Normalmente no necesita:

```txt
ataque
patrullaje complejo
Field of View avanzado
ataques variados
arbol de decision grande
```

---

## Flujo de comportamiento

```txt
1. NPC esta idle, deambulando o cumpliendo rutina.
2. Detecta amenaza.
3. Decision activa huida.
4. Huida elige direccion o punto seguro.
5. Movimiento ejecuta escape.
6. Al alcanzar distancia segura, se detiene, se esconde o desaparece.
```

---

## Estructura recomendada

```txt
ThreatDetector
→ detecta peligro.

FleeBehaviour
→ calcula escape.

SafePointSelector
→ opcional, elige refugio.

MovementController
→ mueve al NPC.

FleeState
→ organiza inicio y fin de huida.
```

---

## Datos necesarios

```txt
amenaza actual
posicion de amenaza
velocidad de huida
distancia segura
tiempo maximo de huida
puntos seguros opcionales
feedback visual o sonoro
```

---

## Variantes posibles

```txt
huida en direccion opuesta
huida hacia punto seguro
huida hacia zona aliada
huida con desaparicion
huida con llamado de ayuda
animal que huye y vuelve
```

---

## Costos de implementacion

Costo bajo a medio.

Aumenta si:

```txt
busca refugios
usa pathfinding
evalua multiples amenazas
usa seleccion ponderada para puntos seguros
```

---

## Costos de optimizacion

Riesgos:

```txt
buscar puntos seguros cada frame
recalcular rutas constantemente
evaluar demasiadas amenazas
raycasts para cobertura en muchos NPCs
```

Alternativas:

```txt
puntos seguros predefinidos
actualizacion por eventos
cache de amenaza
limitar recalculo
usar heuristicas simples
```

---

## Validacion

Validar:

```txt
si huye en direccion razonable
si no corre hacia peligro
si no se queda trabado
si termina la huida
si el jugador entiende la reaccion
```

Debug util:

```txt
direccion de huida
amenaza actual
punto seguro elegido
distancia segura
estado de huida
```

---

## Errores comunes

```txt
huir para siempre
correr contra una pared
correr hacia otra amenaza
no definir condicion de salida
usar pathfinding complejo sin necesidad
no dar feedback de miedo
```

---

## Criterio para una IA

Cuando una IA use este preset debe:

```txt
definir amenaza claramente
definir salida de huida
no agregar combate si no aporta
separar deteccion, decision y movimiento
elegir punto seguro solo si hace falta
validar con gameplay
```

---

## Checklist

```txt
¿Que amenaza activa la huida?
¿Debe huir directo o a punto seguro?
¿Tiene distancia segura?
¿Tiene condicion de salida?
¿Necesita pathfinding?
¿Puede quedar atrapado?
¿Hay feedback?
```

---

## Regla final

```txt
Huir no es un comportamiento menor.

Es una respuesta valida cuando protege el rol del NPC.
```
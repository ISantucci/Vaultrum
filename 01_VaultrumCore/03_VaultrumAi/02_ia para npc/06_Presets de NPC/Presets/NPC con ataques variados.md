
## Definicion

NPC con ataques variados es un preset para personajes que alternan entre distintas acciones ofensivas sin perder control de diseño.

```txt
NPC ofensivo avanzado
→ evalua ataques disponibles
→ filtra ataques invalidos
→ pondera opciones
→ ejecuta ataque
```

No significa atacar al azar.

Significa variar con reglas.

---

## Rol de gameplay

Sirve para enemigos que necesitan variedad ofensiva.

Ejemplos:

```txt
boss
enemigo elite
mago
enemigo tactico ofensivo
miniboss
```

---

## Cuando usarlo

Usar este preset cuando:

```txt
el NPC tiene varios ataques
la repeticion se siente pobre
el jugador necesita leer patrones
la variedad debe estar controlada
hay cooldowns o fases
```

Pregunta clave:

```txt
¿El NPC tiene varias opciones ofensivas validas?
```

---

## Cuando no usarlo

No usarlo si:

```txt
el NPC tiene un solo ataque
el combate debe ser muy simple
el azar volveria injusta la experiencia
no hay feedback claro
un ataque basico alcanza
```

---

## Sistemas necesarios

```txt
ataques definidos
cooldowns
condiciones de validez
seleccion ponderada
feedback de anticipacion
validacion de rango
```

---

## Sistemas opcionales

```txt
estados
fases
arbol de decision
pathfinding
reposicionamiento
memoria de ultimo ataque
telegraphs
```

---

## Sistemas que NO necesita

Normalmente no necesita:

```txt
patrullaje
Field of View realista
huida comun
sospecha progresiva
seleccion aleatoria sin condiciones
```

---

## Flujo de comportamiento

```txt
1. NPC esta listo para atacar.
2. Se revisan ataques disponibles.
3. Se descartan ataques en cooldown.
4. Se descartan ataques invalidos por distancia o contexto.
5. Se ajustan pesos.
6. Se elige ataque por seleccion ponderada.
7. Se muestra anticipacion.
8. Se ejecuta ataque.
9. Se aplica cooldown.
10. Se vuelve a evaluar.
```

---

## Estructura recomendada

```txt
AttackDefinition
→ datos de ataque.

AttackValidator
→ valida rango, cooldown y contexto.

WeightedAttackSelector
→ elige ataque valido.

AttackExecutor
→ ejecuta ataque.

AttackFeedback
→ muestra anticipacion e impacto.
```

---

## Datos necesarios

```txt
lista de ataques
rango por ataque
cooldown por ataque
peso base
condiciones de validez
duracion
daño
feedback visual
ultimo ataque usado
```

Ejemplo:

```txt
ataque rapido
→ peso 50
→ rango corto
→ cooldown bajo

ataque pesado
→ peso 20
→ rango medio
→ cooldown alto

ataque de area
→ peso 30
→ valido si jugador esta en zona
```

---

## Variantes posibles

```txt
boss por fases
mago con hechizos
enemigo melee con combos
enemigo que alterna ataque y reposicionamiento
enemigo que evita repetir ultimo ataque
```

---

## Costos de implementacion

Costo medio a alto.

Puede requerir:

```txt
varios ataques
validadores
cooldowns
feedback
animaciones
hitboxes
proyectiles
balance
seleccion ponderada
```

---

## Costos de optimizacion

Riesgos:

```txt
spawnear proyectiles sin pooling
chequear muchos ataques cada frame
efectos visuales pesados
hitboxes activas demasiado tiempo
recalcular pesos constantemente
```

Alternativas:

```txt
pooling
evaluar ataques solo al decidir
cooldowns claros
filtrar antes de ponderar
eventos de animacion
```

---

## Validacion

Validar:

```txt
si no elige ataques invalidos
si respeta cooldowns
si no repite demasiado
si el jugador entiende el ataque
si el feedback aparece antes del daño
si la variedad no se siente injusta
```

Debug util:

```txt
ataques disponibles
pesos actuales
ataque elegido
cooldowns
ultimo ataque usado
```

---

## Errores comunes

```txt
usar azar puro
no filtrar ataques invalidos
repetir siempre el mismo ataque
no dar anticipacion
hacer daño sin feedback
ignorar cooldowns
hacer ataques imposibles de esquivar
```

---

## Criterio para una IA

Cuando una IA use este preset debe:

```txt
mantener variedad controlada
filtrar ataques invalidos
usar pesos con intencion
dar feedback claro
respetar cooldowns
evitar azar injusto
validar con gameplay
```

---

## Checklist

```txt
¿Hay mas de un ataque?
¿Cada ataque tiene condicion?
¿Cada ataque tiene cooldown?
¿Hay pesos definidos?
¿Se filtran ataques invalidos?
¿Hay anticipacion?
¿Se evita repetir siempre lo mismo?
¿La variedad es justa?
```

---

## Regla final

```txt
Un ataque variado no es un ataque aleatorio.

Es una opcion ofensiva valida elegida con criterio.
```
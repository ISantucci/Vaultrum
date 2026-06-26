## Definición

GOAP significa Goal-Oriented Action Planning.

Es un enfoque de toma de decisiones donde un NPC elige un objetivo y construye un plan de acciones para alcanzarlo.

```txt
Estado actual del mundo
→ objetivo
→ acciones disponibles
→ plan
→ ejecución
```

GOAP no decide una acción aislada.

Decide una secuencia posible de acciones.

Ejemplo:

```txt
Objetivo:
sobrevivir

Estado actual:
tengo poca vida
no tengo botiquín
hay botiquín en otra sala

Plan:
ir a la sala
recoger botiquín
usar botiquín
```

GOAP pertenece a toma de decisiones.

No pertenece a movimiento, percepción ni pathfinding.

---

## Responsabilidad

La responsabilidad de GOAP es construir un plan para alcanzar un objetivo.

Debe responder:

```txt
¿Qué quiere lograr el NPC?
¿Qué acciones existen?
¿Qué condiciones necesita cada acción?
Qué cambia cada acción?
¿Qué secuencia de acciones permite llegar al objetivo?
```

GOAP no debe ejecutar todos los sistemas del NPC.

Debe elegir un plan.

Luego otros sistemas ejecutan las acciones del plan.

---

## Componentes principales

GOAP suele trabajar con cuatro piezas principales:

```txt
Estado del mundo
Objetivo
Acciones
Planificador
```

Cada pieza debe tener una responsabilidad clara.

---

## Estado del mundo

El estado del mundo representa información relevante para planificar.

Ejemplos:

```txt
tiene arma
tiene munición
jugador visible
vida baja
hay cobertura cerca
puerta abierta
enemigo en rango
tiene botiquín
```

No debería ser una copia completa del juego.

Solo debe contener datos útiles para decidir.

Regla:

```txt
El estado del mundo debe ser suficiente para planificar.

No debe convertirse en todo el juego.
```

---

## Objetivo

El objetivo representa qué quiere lograr el NPC.

Ejemplos:

```txt
eliminar enemigo
sobrevivir
conseguir arma
curarse
llegar a una zona
proteger aliado
escapar
```

Un objetivo no es una acción.

Es un resultado deseado.

Ejemplo incorrecto:

```txt
Objetivo:
recargar arma
```

Ejemplo más claro:

```txt
Objetivo:
estar listo para atacar

Acción posible:
recargar arma
```

La diferencia importa porque GOAP planifica acciones para alcanzar resultados.

---

## Acción

Una acción representa algo que el NPC puede hacer dentro de un plan.

Cada acción suele tener:

```txt
precondiciones
efectos
costo
ejecución
```

Ejemplo:

```txt
Acción:
Recoger arma

Precondiciones:
arma visible
arma alcanzable

Efectos:
tiene arma = true

Costo:
distancia hasta el arma
```

Otro ejemplo:

```txt
Acción:
Atacar jugador

Precondiciones:
tiene arma
jugador visible
jugador en rango

Efectos:
jugador dañado

Costo:
riesgo o tiempo de ataque
```

La acción define qué necesita y qué cambia.

No debería decidir todo el comportamiento del NPC por sí sola.

---

## Planificador

El planificador busca una secuencia de acciones que transforme el estado actual en un estado que cumpla el objetivo.

```txt
Estado actual
→ aplicar acción posible
→ nuevo estado simulado
→ aplicar otra acción
→ objetivo alcanzado
```

El planificador no debería mover físicamente al NPC.

Tampoco debería detectar al jugador.

Solo evalúa acciones posibles, precondiciones, efectos y costos.

---

## Flujo general

Un flujo simple de GOAP puede ser:

```txt
1. Leer estado actual del mundo.
2. Elegir o recibir objetivo.
3. Revisar acciones disponibles.
4. Filtrar acciones cuyas precondiciones se cumplen.
5. Simular efectos.
6. Buscar una secuencia que alcance el objetivo.
7. Elegir el plan más conveniente.
8. Entregar el plan al ejecutor.
9. Ejecutar acciones una por una.
10. Replanificar si el mundo cambia.
```

La ejecución del plan debe estar separada del cálculo del plan.

---

## Ejemplo conceptual

Situación:

```txt
NPC tiene poca vida.
NPC no tiene botiquín.
Hay botiquín en una habitación cercana.
```

Objetivo:

```txt
vida segura
```

Acciones disponibles:

```txt
Moverse a botiquín
Recoger botiquín
Usar botiquín
Buscar cobertura
Atacar
```

Plan posible:

```txt
Moverse a botiquín
→ Recoger botiquín
→ Usar botiquín
```

Ese plan no significa que GOAP mueva al NPC.

GOAP decide la secuencia.

Movimiento ejecuta desplazamiento.

Comportamientos ejecutan acciones concretas.

---

## Relación con estados de NPC

GOAP y estados pueden convivir.

Una máquina de estados puede definir el modo general del NPC.

GOAP puede planificar dentro de un modo específico.

Ejemplo:

```txt
Estado Combat
→ usa GOAP para decidir cómo resolver el combate.

Estado Flee
→ usa una acción simple de escape.

Estado Patrol
→ no necesita GOAP.
```

También puede pasar lo inverso:

```txt
GOAP decide ejecutar acción Atacar
→ esa acción activa comportamiento o estado de ataque.
```

No hay que forzar ambos sistemas si uno solo alcanza.

---

## Relación con árboles de decisión

Un árbol de decisión elige una acción evaluando condiciones ordenadas.

GOAP construye una secuencia de acciones.

```txt
Árbol de decisión
→ elige qué hacer ahora.

GOAP
→ planifica varios pasos para alcanzar un objetivo.
```

Ejemplo:

```txt
Árbol:
¿Veo al jugador?
→ atacar

GOAP:
Quiero atacar al jugador.
No tengo arma.
Hay arma cerca.
Plan:
ir al arma
recoger arma
acercarse
atacar
```

GOAP conviene cuando la solución no es una sola decisión inmediata.

---

## Relación con selección ponderada

La selección ponderada elige entre opciones usando pesos o prioridades relativas.

GOAP puede usar costos para elegir entre planes posibles.

```txt
Selección ponderada
→ elige una opción entre varias.

GOAP
→ construye y evalúa secuencias de acciones.
```

Ejemplo:

```txt
Selección ponderada:
elegir patrullar, investigar o esperar.

GOAP:
planificar cómo conseguir munición y volver a atacar.
```

---

## Qué NO debe hacer

GOAP no debe:

```txt
detectar jugador directamente
mover al NPC directamente
calcular pathfinding completo dentro del planificador
aplicar daño directamente desde el planificador
mezclar todas las acciones en una clase gigante
convertir cada problema simple en planificación compleja
replanificar cada frame sin necesidad
guardar todo el estado del juego sin criterio
```

Ejemplo incorrecto:

```txt
GOAPSystem
→ detecta jugador
→ calcula ruta
→ mueve
→ ataca
→ aplica daño
→ reproduce animación
→ decide siguiente objetivo
```

Ejemplo correcto:

```txt
Percepción
→ informa estado del mundo.

GOAP
→ calcula plan.

Ejecutor de acciones
→ ejecuta acción actual.

Movimiento
→ desplaza si la acción lo necesita.

Combate
→ resuelve daño si la acción lo necesita.
```

Regla:

```txt
GOAP planifica.

No ejecuta todo el NPC.
```

---

## Cuándo conviene usarlo

Conviene usar GOAP cuando:

```txt
el NPC tiene varios objetivos posibles
hay muchas acciones combinables
el orden de acciones importa
el mundo puede cambiar
el NPC debe resolver problemas de forma flexible
una decisión inmediata no alcanza
se busca comportamiento emergente controlado
```

Ejemplos:

```txt
enemigo que busca arma antes de atacar
NPC que busca comida, refugio o descanso
soldado que elige cubrirse, recargar y atacar
agente que resuelve objetivos con recursos del entorno
```

Pregunta clave:

```txt
¿El NPC necesita planificar pasos, no solo elegir una acción?
```

Si la respuesta es sí, GOAP puede aportar valor.

---

## Cuándo NO conviene usarlo

No conviene usar GOAP si:

```txt
el NPC tiene comportamiento simple
una máquina de estados alcanza
un árbol de decisión alcanza
la selección ponderada alcanza
hay pocas acciones posibles
no hay objetivos complejos
el costo de planificación no aporta gameplay
```

Ejemplos:

```txt
enemigo básico que patrulla y persigue
NPC de diálogo
comerciante
torreta
animal simple que huye si ve al jugador
```

Regla:

```txt
No usar GOAP si una solución más simple resuelve el problema.
```

---

## Riesgos comunes

Riesgos comunes al implementar GOAP:

```txt
sobrearquitecturar NPCs simples
crear demasiadas acciones abstractas
mezclar planificación con ejecución
no separar estado real y estado simulado
replanificar demasiado seguido
no manejar planes inválidos
no manejar cambios del mundo
costos mal definidos
precondiciones ambiguas
efectos inconsistentes
debug difícil
```

GOAP puede volverse costoso y difícil de depurar si no se mantiene acotado.

---

## Validación

GOAP se valida revisando:

```txt
objetivo elegido
estado inicial leído
acciones disponibles
precondiciones evaluadas
efectos simulados
plan generado
costo del plan
acción actual
motivo de fallo si no hay plan
momento de replanificación
```

Debug útil:

```txt
mostrar objetivo actual
mostrar plan completo
mostrar acción actual
mostrar acciones descartadas
mostrar precondiciones fallidas
mostrar costo total
logs de replanificación
```

Sin debug, GOAP puede parecer magia o comportamiento aleatorio.

---

## Regla final

GOAP no es comportamiento completo.

GOAP no es movimiento.

GOAP no es percepción.

GOAP es planificación orientada a objetivos.

```txt
Objetivo
→ acciones posibles
→ plan
→ ejecución separada
```

Primero objetivo.

Después plan.

Después ejecución.
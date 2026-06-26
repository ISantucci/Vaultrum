## Definicion

Un NPC, o Non-Playable Character, es una entidad del juego que no es controlada directamente por el jugador, pero que cumple un rol dentro del gameplay, la narrativa o el mundo.

Puede ser activo o pasivo.

Puede tener inteligencia compleja o comportamiento minimo.

```txt
NPC
→ entidad no controlada directamente por el jugador
→ cumple un rol dentro de la experiencia
```

Un NPC no debe pensarse automaticamente como “un personaje con IA avanzada”.

Primero debe pensarse como una pieza de diseño.

Despues se decide que comportamiento necesita.

---

## Responsabilidad

La responsabilidad de un NPC es representar una entidad del mundo que cumple una funcion clara.

Puede servir para:

```txt
crear conflicto
dar informacion
guiar al jugador
ofrecer interaccion
vender objetos
entregar misiones
defender una zona
atacar al jugador
huir de una amenaza
acompañar al jugador
simular vida
construir narrativa
generar presion
```

Desde diseño, la pregunta principal es:

```txt
¿Que rol cumple esta entidad en la experiencia del jugador?
```

Desde implementacion, la pregunta principal es:

```txt
¿Que sistemas necesita esta entidad para cumplir ese rol?
```

---

## Que problema resuelve

Los NPCs ayudan a que el mundo tenga presencia, interaccion, oposicion o estructura.

Un NPC puede resolver necesidades distintas segun el juego.

Ejemplos:

```txt
Guardia
→ controla una zona.

Enemigo agresivo
→ presiona al jugador.

Scout
→ detecta, escapa o pide ayuda.

Civil
→ da vida al mundo y reacciona al peligro.

Comerciante
→ permite intercambio de recursos.

Boss
→ genera un desafio memorable.

Aliado
→ acompaña o asiste al jugador.
```

El problema no es “hacer un NPC inteligente”.

El problema es definir que necesita hacer para cumplir bien su funcion.

---

## Que NO debe hacer un NPC

Un NPC no debe absorber todas las responsabilidades del juego.

No deberia contener internamente toda la logica de:

```txt
percepcion
decision
movimiento
pathfinding
combate
animacion
audio
UI
misiones
inventario
guardado
spawning
drops
mapa logico
```

Puede coordinar o consumir sistemas, pero no deberia reemplazarlos.

Ejemplo incorrecto:

```txt
Enemy.cs
→ detecta jugador
→ decide estado
→ calcula pathfinding
→ mueve al NPC
→ ataca
→ huye
→ anima
→ reproduce sonidos
→ actualiza UI
→ maneja drops
→ guarda estado
```

Ejemplo mas sano:

```txt
NPC / Enemy
→ representa la entidad y coordina responsabilidades necesarias.

Perception
→ detecta informacion.

Decision
→ elige intencion.

State Machine
→ organiza estados.

Movement
→ ejecuta desplazamiento.

Attack
→ ejecuta ataque.

Health
→ maneja vida.

Animation
→ muestra feedback.

Pathfinding
→ calcula rutas si hace falta.
```

Regla:

```txt
El NPC puede usar sistemas.
No debe convertirse en todos los sistemas.
```

---

## Datos que puede tener

Un NPC puede tener datos propios como:

```txt
identidad
rol
vida
velocidad
rango de deteccion
rango de ataque
daño
faccion
estado actual
objetivo actual
configuracion de comportamiento
referencias a sistemas necesarios
```

No todos los NPCs necesitan todos estos datos.

La configuracion debe responder al rol.

Ejemplo:

```txt
Comerciante
→ datos de dialogo e inventario.

Guardia
→ datos de percepcion, patrullaje, persecucion y ataque.

Civil
→ datos de rutina y reaccion al peligro.

Boss
→ datos de fases, ataques, patrones y feedback.
```

---

## Sistemas que puede consumir

Un NPC puede consumir sistemas segun su necesidad.

Ejemplos:

```txt
[[Percepcion]]
[[Field of View]]
[[Deteccion del jugador]]
[[Estados de NPC]]
[[Arboles de decision]]
[[Seleccion ponderada]]
[[Patrullaje]]
[[Persecucion]]
[[Ataque]]
[[Huida]]
[[Steering Behaviours]]
[[Obstacle Avoidance]]
[[Integracion con Pathfinding]]
```

Tambien puede relacionarse con sistemas externos a esta carpeta:

```txt
[[IA para desarrollo de mapas]]
[[Pathfinding]]
[[State]]
[[Strategy]]
[[Observer]]
[[Command]]
[[Event Queue]]
```

Pero consumir un sistema no significa redefinirlo.

Ejemplo:

```txt
NPC
→ puede necesitar una ruta.

Pathfinding
→ calcula la ruta.

Movimiento
→ ejecuta el desplazamiento.
```

El NPC no deberia explicar internamente como funciona todo el algoritmo de pathfinding.

---

## Flujo conceptual

Un NPC con comportamiento puede organizarse asi:

```txt
Rol
→ percepcion
→ decision
→ comportamiento
→ movimiento o accion
→ feedback
→ validacion
```

Ejemplo:

```txt
Guardia patrullero

Rol:
controlar una zona.

Percepcion:
detectar jugador.

Decision:
si ve al jugador, perseguir.

Comportamiento:
patrullaje, persecucion, ataque.

Movimiento:
waypoints o pathfinding.

Feedback:
animacion, sonido, alerta visual.

Validacion:
el jugador entiende cuando fue detectado y por que.
```

Ejemplo simple:

```txt
Comerciante

Rol:
permitir intercambio.

Percepcion:
interaccion del jugador.

Decision:
abrir dialogo o tienda.

Comportamiento:
esperar, conversar, vender.

Movimiento:
no necesita.

Validacion:
el jugador entiende que puede interactuar.
```

---

## Como aplicarlo en videojuegos

Para aplicar bien el concepto de NPC, primero se define su rol.

Preguntas utiles:

```txt
¿Que experiencia debe generar?
¿Es enemigo, aliado, civil, comerciante, jefe, guia o ambientacion?
¿Tiene que moverse?
¿Tiene que detectar al jugador?
¿Tiene que tomar decisiones?
¿Tiene que atacar o huir?
¿Tiene que reaccionar al entorno?
¿Debe tener feedback claro?
¿El jugador debe entender sus intenciones?
¿Debe ser reutilizable?
```

Luego se eligen los sistemas necesarios.

Ejemplo:

```txt
Enemigo simple

Necesita:
- deteccion basica
- persecucion
- ataque
- vida
- feedback
```

Ejemplo:

```txt
Guardia patrullero

Necesita:
- [[Percepcion]]
- [[Field of View]]
- [[Patrullaje]]
- [[Persecucion]]
- [[Ataque]]
- [[Estados de NPC]]
- [[Integracion con Pathfinding]] si el mapa lo requiere
```

Ejemplo:

```txt
Comerciante

Necesita:
- interaccion
- dialogo
- inventario
- feedback visual
```

No tiene sentido darle A Star, Obstacle Avoidance o Seleccion ponderada a un NPC que solo abre una tienda.

---

## Cuando conviene usar NPCs

Conviene usar NPCs cuando el juego necesita entidades que cumplan roles dentro del mundo o del gameplay.

Por ejemplo:

```txt
crear enemigos
crear aliados
agregar personajes narrativos
poblar un mundo
dar misiones
crear comerciantes
generar peligro
crear desafios
simular vida
guiar al jugador
defender zonas
crear interaccion
generar variedad de situaciones
```

La pregunta clave es:

```txt
¿Que cambia en el juego si este NPC existe?
```

Si la respuesta es clara, el NPC probablemente tiene una funcion.

---

## Cuando NO conviene usar NPCs

No conviene agregar NPCs si no cumplen una funcion clara.

Un NPC que no aporta gameplay, narrativa, ambientacion o interaccion puede convertirse en ruido.

Tampoco conviene llamar NPC a cualquier cosa que se mueve.

Ejemplos:

```txt
Objeto decorativo
→ no necesita ser NPC.

Torre automatica
→ puede ser entidad de gameplay, pero no necesariamente NPC.

Trampa
→ ejecuta logica, pero no necesariamente es NPC.

Proyectil
→ se mueve y causa daño, pero no es NPC.

Spawner
→ crea entidades, pero no es NPC.
```

Pregunta clave:

```txt
¿Esta entidad necesita comportarse como personaje, agente o entidad del mundo?
```

Si no necesita rol, decision, percepcion o interaccion como entidad, quizas no conviene tratarla como NPC.

---

## Costos de implementacion

Agregar NPCs puede implicar costos como:

```txt
diseño de rol
definicion de comportamientos
configuracion de datos
animaciones
feedback
integracion con vida, daño o interaccion
integracion con movimiento
integracion con pathfinding si aplica
debug de estados
validacion de gameplay
```

El costo aumenta cuando el NPC necesita:

```txt
percepcion avanzada
multiples estados
decisiones complejas
movimiento dinamico
reaccion al entorno
coordinacion con otros NPCs
uso de mapa logico
```

Regla:

```txt
Cada sistema agregado debe justificar su costo.
```

---

## Costos de optimizacion

Los NPCs pueden afectar rendimiento si se implementan sin criterio.

Riesgos comunes:

```txt
calcular percepcion cada frame sin necesidad
recalcular rutas constantemente
usar raycasts masivos sin control
actualizar muchos NPCs al mismo tiempo
crear listas temporales en loops frecuentes
usar busquedas globales para encontrar objetivos
dejar debug visual siempre activo
mezclar animacion, logica y pathfinding en Update
```

Alternativas posibles:

```txt
actualizacion por intervalos
eventos
cache de referencias
niveles de detalle para IA
limite de chequeos por frame
pooling cuando aplica
debug activable
separacion entre runtime y herramientas de editor
```

No todos los juegos necesitan optimizacion avanzada de NPCs.

Pero si hay muchos agentes o sistemas frecuentes, el costo debe considerarse temprano.

---

## Errores que ayuda a evitar

Definir bien que es un NPC ayuda a evitar:

```txt
llamar NPC a cualquier objeto con movimiento
crear IA compleja para entidades que no la necesitan
diseñar enemigos sin rol claro
crear personajes que no aportan al gameplay
mezclar comportamiento, movimiento, percepcion y combate en una sola clase
usar pathfinding donde alcanzan waypoints
usar estados donde alcanza una accion simple
crear sistemas genericos antes de entender el rol del personaje
hacer NPCs inteligentes pero poco utiles para el diseño
repetir logica entre muchos enemigos o personajes
no diferenciar entidad, agente, enemigo, aliado y objeto interactivo
```

---

## Riesgos de aplicarlo mal

El primer riesgo es pensar que todo NPC necesita IA avanzada.

Eso lleva a sobrearquitectura.

Ejemplo:

```txt
Comerciante
→ no necesita Field of View, A Star ni seleccion ponderada si solo abre una tienda.
```

Otro riesgo es diseñar NPCs sin rol.

Ejemplo debil:

```txt
Quiero un enemigo inteligente.
```

Mejor:

```txt
Quiero un enemigo que patrulle una zona,
detecte al jugador,
lo persiga
y ataque si esta cerca.
```

Otro riesgo es crear un NPC monolitico.

Problemas comunes:

```txt
cada nuevo comportamiento agrega mas condicionales
cambiar un estado rompe otro
la percepcion queda acoplada al movimiento
el ataque depende directamente del pathfinding
la animacion queda mezclada con decision
no se pueden reutilizar comportamientos
es dificil depurar que esta haciendo el NPC
```

---

## Criterio para una IA

Cuando una IA trabaje con el concepto de NPC, debe recordar:

```txt
NPC es nota base.
No debe explicar todos sus consumidores.

Percepcion, decision, comportamiento y movimiento
son sistemas o notas consumidoras.

Pathfinding, mapas y algoritmos
son proveedores externos cuando el NPC necesita navegar.
```

La IA debe evitar:

```txt
convertir NPC.md en hub de toda la IA
duplicar pathfinding dentro del concepto NPC
meter algoritmos dentro de la definicion de NPC
agregar sistemas que el rol no necesita
confundir entidad con comportamiento
```

Regla:

```txt
El NPC define la entidad y su rol.
Los sistemas explican como esa entidad percibe, decide y actua.
```

---

## Checklist

Antes de diseñar o implementar un NPC, revisar:

```txt
¿Tiene rol claro?
¿Aporta a gameplay, narrativa, mundo o interaccion?
¿Necesita IA o alcanza con interaccion simple?
¿Necesita percepcion?
¿Necesita toma de decisiones?
¿Necesita movimiento?
¿Necesita pathfinding?
¿Necesita estados?
¿La complejidad esta justificada?
¿Se puede validar su comportamiento?
¿El jugador entiende que hace?
¿Hay sistemas que se estan agregando por ansiedad tecnica?
```

---

## Regla final

```txt
Un NPC no es una bolsa de sistemas.

Es una entidad con un rol claro,
que consume solo los sistemas que necesita para cumplirlo.
```
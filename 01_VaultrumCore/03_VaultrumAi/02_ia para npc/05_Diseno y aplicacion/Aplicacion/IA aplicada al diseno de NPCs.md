## Definicion

IA aplicada al diseño de NPCs es el criterio para crear, evaluar y ajustar moldes de IA reutilizables.

No se enfoca en desarrollar un NPC completo dentro de esta nota.

Se enfoca en definir como pensar, combinar y validar sistemas antes de crear un preset concreto.

```txt
Rol del NPC
→ necesidad de gameplay
→ informacion necesaria
→ decision necesaria
→ comportamiento necesario
→ movimiento necesario
→ tecnica adecuada
→ preset reutilizable
→ validacion en juego
```

Esta nota funciona como puente entre las piezas tecnicas y los presets.

---

## Responsabilidad

La responsabilidad de esta nota es definir reglas para crear buenos presets de NPCs.

Debe ayudar a responder:

```txt
como se diseña un NPC desde cero
que sistemas necesita
que sistemas no necesita
como se combinan las piezas
cuando usar estados
cuando usar arboles de decision
cuando usar seleccion ponderada
cuando usar pathfinding
cuando usar steering
como evitar patrones repetitivos
como evitar sobrearquitectura
como validar si el preset sirve
cuando convertir una solucion real en preset
```

Esta nota no debe contener todas las recetas completas.

Las recetas concretas viven en `[[NPC Presets]]`.

---

## Que NO debe hacer

Esta nota no debe:

```txt
desarrollar todos los presets en profundidad
duplicar cada tecnica completa
duplicar cada comportamiento
duplicar algoritmos
convertirse en una lista gigante de NPCs
obligar a usar IA compleja en todos los casos
prometer una arquitectura universal
```

Ejemplo incorrecto:

```txt
Todo NPC debe tener:
Field of View
State Machine
Arbol de decision
Pathfinding
Steering
Obstacle Avoidance
Seleccion ponderada
```

Ejemplo correcto:

```txt
Cada NPC necesita solo la combinacion de sistemas que justifica su rol.
```

Regla:

```txt
Esta nota enseña a crear moldes.
Los presets guardan moldes concretos.
```

---

## Flujo general para crear un NPC

Antes de elegir tecnicas, definir el rol.

```txt
1. Definir rol del NPC.
2. Definir experiencia que debe generar.
3. Definir informacion que necesita percibir.
4. Definir decisiones que debe tomar.
5. Definir comportamientos posibles.
6. Definir movimiento necesario.
7. Definir si necesita navegacion.
8. Definir si necesita variedad.
9. Definir feedback.
10. Definir validacion.
11. Revisar costos.
12. Eliminar complejidad innecesaria.
13. Decidir si corresponde crear o actualizar un preset.
```

Regla:

```txt
Primero diseño.
Despues tecnica.
Despues preset.
```

---

## Formula base de una IA de NPC

Una IA de NPC puede pensarse como una cadena de responsabilidades.

```txt
Entrada
→ interpretacion
→ decision
→ comportamiento
→ movimiento / accion
→ feedback
→ validacion
```

Ejemplo:

```txt
Percepcion detecta jugador
→ decision interpreta amenaza
→ comportamiento elige persecucion
→ movimiento sigue ruta
→ feedback muestra alerta
→ gameplay valida si se entiende
```

Cada parte debe tener una responsabilidad clara.

---

## Capas de una IA de NPC

## Capa de informacion

Define que sabe el NPC.

Puede incluir:

```txt
deteccion por distancia
vision
sonido
daño recibido
eventos
zonas
memoria
ultima posicion conocida
```

Pregunta:

```txt
¿Que informacion necesita el NPC para cumplir su rol?
```

---

## Capa de decision

Define como el NPC elige que hacer.

Puede incluir:

```txt
condiciones simples
estados
arboles de decision
seleccion ponderada
prioridades
cooldowns
memoria de acciones recientes
```

Pregunta:

```txt
¿Como decide el NPC entre sus opciones?
```

---

## Capa de comportamiento

Define que acciones puede ejecutar.

Puede incluir:

```txt
patrullar
perseguir
atacar
huir
investigar
esperar
proteger
buscar
reposicionarse
interactuar
```

Pregunta:

```txt
¿Que acciones reales necesita ejecutar?
```

---

## Capa de movimiento

Define como se desplaza.

Puede incluir:

```txt
movimiento directo
waypoints
pathfinding
steering
obstacle avoidance
seguimiento de ruta
```

Pregunta:

```txt
¿Como llega o se mueve hacia donde necesita?
```

---

## Capa de feedback

Define como el jugador entiende la IA.

Puede incluir:

```txt
animaciones
sonidos
iconos de alerta
cambios de postura
lineas de vision visibles
telegraphs
efectos
logs de debug en desarrollo
```

Pregunta:

```txt
¿El jugador entiende que esta haciendo el NPC y por que?
```

---

## Como elegir tecnica segun problema

## Si el problema es detectar

Usar:

```txt
distancia
Field of View
sonido
eventos
zonas
memoria
```

Evitar resolver deteccion dentro de:

```txt
ataque
movimiento
pathfinding
seleccion ponderada
```

Pregunta:

```txt
¿Que necesita saber el NPC?
```

---

## Si el problema es decidir

Usar:

```txt
condiciones simples
estados
arboles de decision
seleccion ponderada
prioridades
```

Evitar resolver decision dentro de:

```txt
percepcion
ataque
movimiento
pathfinding
```

Pregunta:

```txt
¿Como elige entre acciones posibles?
```

---

## Si el problema es ejecutar una accion

Usar:

```txt
comportamientos
ataque
patrullaje
persecucion
huida
interaccion
```

Evitar meter toda la decision dentro del comportamiento.

Pregunta:

```txt
¿Que accion concreta debe ejecutar?
```

---

## Si el problema es moverse

Usar:

```txt
movimiento directo
waypoints
pathfinding
steering
obstacle avoidance
```

Evitar usar movimiento para decidir comportamiento.

Pregunta:

```txt
¿El problema es llegar, esquivar, suavizar o seguir una ruta?
```

---

## Si el problema es variar patrones

Usar:

```txt
seleccion ponderada
memoria de acciones recientes
condiciones de validez
cooldowns
pesos dinamicos
tiempos variables
```

Evitar:

```txt
azar puro sin restricciones
```

Pregunta:

```txt
¿La variedad tiene criterio o solo agrega ruido?
```

---

## Si el problema es navegar un mapa

Usar:

```txt
pathfinding
waypoints
rutas
mapa navegable
costos
zonas bloqueadas
```

Evitar implementar el algoritmo dentro del NPC.

Pregunta:

```txt
¿El NPC necesita planificar por donde moverse?
```

---

## Como elegir entre estados, arboles y seleccion ponderada

## Usar estados cuando

```txt
el NPC tiene modos claros
cada modo tiene comportamiento propio
hay transiciones importantes
se necesita saber que esta haciendo ahora
```

Ejemplo:

```txt
Patrol
Chase
Attack
Flee
```

---

## Usar arboles de decision cuando

```txt
la decision se puede expresar como preguntas
hay condiciones claras
se quiere legibilidad
hay prioridades ordenadas
```

Ejemplo:

```txt
¿Vida baja?
→ huir

¿Jugador en rango?
→ atacar

¿Jugador detectado?
→ perseguir

Si no
→ patrullar
```

---

## Usar seleccion ponderada cuando

```txt
hay varias opciones validas
se busca variedad controlada
los pesos responden al diseño
no hay una unica respuesta correcta
```

Ejemplo:

```txt
elegir siguiente punto de patrulla
elegir ataque de boss
elegir reaccion secundaria
elegir punto seguro
```

---

## Combinar tecnicas

Se pueden combinar tecnicas si cada una mantiene su responsabilidad.

Ejemplo:

```txt
Estado Attack
→ usa seleccion ponderada para elegir ataque.
```

Ejemplo:

```txt
Estado Patrol
→ usa seleccion ponderada para elegir siguiente punto.
```

Ejemplo:

```txt
Arbol de decision
→ decide que debe atacar.

Seleccion ponderada
→ decide que ataque usar.
```

Regla:

```txt
La tecnica de alto nivel decide el modo.
La tecnica interna puede variar la ejecucion.
```

---

## Reglas para crear un preset de NPC

Un preset debe documentar una solucion reutilizable.

No debe ser solo una descripcion narrativa.

Debe tener estructura operativa.

Formato recomendado:

```txt
Definicion
Rol de gameplay
Cuando usarlo
Cuando no usarlo
Sistemas necesarios
Sistemas opcionales
Sistemas que NO necesita
Flujo de comportamiento
Estructura recomendada
Datos necesarios
Variantes posibles
Costos de implementacion
Costos de optimizacion
Validacion
Errores comunes
Criterio para una IA
Checklist
Regla final
```

---

## Que debe incluir un preset

Un buen preset debe decir:

```txt
que problema resuelve
que tipo de NPC representa
que piezas usa
por que usa esas piezas
que piezas descarta
como se comporta
como se valida
que se puede copiar
que se debe adaptar
```

Ejemplo de sistema necesario:

```txt
NPC patrullero con variedad
→ patrullaje
→ seleccion ponderada
→ memoria de ultimos puntos
→ waypoints
```

Ejemplo de sistema descartado:

```txt
No necesita Field of View si no reacciona visualmente al jugador.
```

---

## Que NO debe incluir un preset

Un preset no debe:

```txt
obligar a usar todos los sistemas
mezclar responsabilidades
duplicar teoria completa de cada tecnica
copiar algoritmos enteros innecesariamente
ser tan especifico que no pueda reutilizarse
ser tan generico que no sirva como molde
```

Regla:

```txt
Un preset debe ser reutilizable, no universal.
```

---

## Cuando crear un nuevo preset

Crear un nuevo preset cuando:

```txt
aparece un tipo de NPC repetible
la combinacion de sistemas puede reutilizarse
la solucion ya fue validada o tiene criterio claro
el NPC representa un caso comun
el preset ahorraria decisiones futuras
```

Ejemplos:

```txt
guardia de sigilo
boss con ataques variados
civil que huye
NPC patrullero con variedad
enemigo agresivo directo
```

---

## Cuando NO crear un nuevo preset

No crear preset cuando:

```txt
el caso es demasiado especifico
todavia no se valido
solo cambia un valor menor
ya existe un preset parecido
la diferencia es solo estetica
la solucion no se repetiria
```

Ejemplo:

```txt
Guardia rojo con velocidad 4
```

Eso probablemente es una variante de guardia, no un preset nuevo.

---

## Como autonutrir la carpeta de presets

La carpeta de presets puede crecer con proyectos reales.

Flujo de autonutricion:

```txt
1. Se desarrolla un NPC real.
2. Se valida en gameplay.
3. Se identifica si la solucion es reutilizable.
4. Se compara con presets existentes.
5. Si encaja, se agrega como variante.
6. Si no encaja y es reutilizable, se crea nuevo preset.
7. Se documenta que sistemas usa y que problemas resolvio.
```

Regla:

```txt
No todo NPC real se convierte en preset.

Solo los moldes reutilizables alimentan la carpeta.
```

---

## Como usar un preset existente

Cuando se necesite crear un NPC, primero revisar `[[NPC Presets]]`.

Flujo:

```txt
1. Buscar el preset mas parecido.
2. Leer rol y cuando usarlo.
3. Revisar sistemas necesarios.
4. Revisar sistemas opcionales.
5. Descartar sistemas que no aplican.
6. Adaptar datos al juego.
7. Implementar solo lo necesario.
8. Validar en gameplay.
9. Registrar variante si aporta valor.
```

Regla:

```txt
Primero buscar molde existente.
Despues adaptar.
Recien despues crear algo nuevo.
```

---

## Como evitar patrones repetitivos

Para evitar que un NPC se sienta mecanico, se pueden usar varias estrategias.

## Variar destinos

```txt
patrullaje con puntos ponderados
zonas de interes
puntos bloqueados temporalmente
memoria de ultimos destinos
```

Ejemplo:

```txt
No elegir el ultimo punto visitado salvo que sea necesario.
```

---

## Variar tiempos

```txt
tiempos de espera variables
pausas entre acciones
cooldowns distintos
delay antes de reaccionar
```

Ejemplo:

```txt
Esperar entre 1 y 3 segundos en un punto de patrulla.
```

---

## Variar acciones

```txt
seleccion ponderada de ataques
acciones alternativas
comportamientos secundarios
respuestas segun contexto
```

Ejemplo:

```txt
Si el jugador esta cerca:
→ ataque rapido
→ empuje
→ retroceso
```

---

## Usar memoria

```txt
ultimo punto visitado
ultima accion ejecutada
ultima posicion conocida
ultimo ataque usado
tiempo desde ultima reaccion
```

Memoria evita repeticiones evidentes.

---

## Usar condiciones de validez

No alcanza con variedad.

Cada opcion debe tener sentido.

Ejemplo:

```txt
Ataque lejano
→ valido si jugador esta lejos.

Ataque melee
→ valido si jugador esta cerca.

Huida
→ valida si vida baja o amenaza alta.
```

Regla:

```txt
Variedad sin condiciones produce caos.
Condiciones sin variedad producen rigidez.
```

---

## Costos de implementacion

Crear IA aplicada puede requerir:

```txt
definir rol
elegir sistemas
conectar datos
crear comportamientos
crear decision
configurar valores
integrar movimiento
integrar feedback
crear debug
validar gameplay
documentar preset si aplica
```

El costo aumenta con:

```txt
cantidad de comportamientos
cantidad de estados
percepcion avanzada
pathfinding
seleccion ponderada
grupos de NPCs
bosses
feedback complejo
```

---

## Costos de optimizacion

La IA puede afectar rendimiento por:

```txt
sensores frecuentes
raycasts
pathfinding
busqueda de objetivos
actualizaciones por frame
muchos agentes activos
instanciacion de proyectiles
debug visual
allocations
```

Estrategias:

```txt
actualizar por intervalos
usar eventos
cachear referencias
limitar NPCs activos
usar LOD de IA
limitar pathfinding por frame
usar pooling cuando aplica
desactivar debug en runtime
```

---

## Validacion general

Un NPC se valida en gameplay, no solo por codigo.

Validar:

```txt
si cumple su rol
si el jugador entiende que hace
si reacciona cuando corresponde
si no sabe cosas injustas
si no se traba
si no hace acciones incoherentes
si el feedback es claro
si la complejidad se justifica
si el molde puede reutilizarse
```

Debug util:

```txt
estado actual
objetivo actual
deteccion actual
ruta actual
comportamiento activo
cooldown
ultima posicion conocida
logs temporales
gizmos
```

---

## Preguntas antes de diseñar un NPC

Antes de diseñar o implementar IA para un NPC, preguntar:

```txt
¿Que rol cumple?
¿Que experiencia debe generar?
¿Que debe saber?
¿Que no deberia saber?
¿Que decisiones toma?
¿Que comportamientos ejecuta?
¿Como se mueve?
¿Necesita pathfinding?
¿Necesita percepcion avanzada?
¿Necesita ataques?
¿Necesita huida?
¿Necesita variedad?
¿Necesita memoria?
¿Que feedback necesita?
¿Como se valida?
¿Existe un preset parecido?
¿Conviene adaptar un preset?
¿Conviene crear uno nuevo?
¿Que sistema seria sobrearquitectura?
```

---

## Errores comunes

Errores comunes:

```txt
partir desde la tecnica
no definir rol
agregar sistemas por ansiedad
hacer NPCs monoliticos
duplicar responsabilidades
no separar percepcion y decision
no separar decision y comportamiento
no separar movimiento y pathfinding
usar azar sin condiciones
usar seleccion ponderada sin pesos con sentido
usar estados para todo
crear presets para casos demasiado especificos
no revisar presets existentes
no validar con gameplay
no considerar costos
```

---

## Criterio para una IA

Cuando una IA trabaje en diseño de NPCs debe:

```txt
empezar por rol y experiencia
buscar presets existentes antes de inventar
no proponer sistemas sin necesidad
separar percepcion, decision, comportamiento y movimiento
no duplicar algoritmos ni mapas
indicar que tecnicas entran y cuales no
explicar cuando implementar y cuando no
considerar costos de implementacion
considerar costos de optimizacion
proponer validacion concreta
detectar si una solucion merece volverse preset
respetar navegacion waterfall
```

Regla operativa:

```txt
La IA no debe diseñar NPCs para demostrar tecnica.
Debe diseñarlos para cumplir una funcion en el juego.
```

---

## Checklist

Antes de cerrar el diseño de un NPC, revisar:

```txt
¿El rol esta claro?
¿La experiencia esperada esta clara?
¿La informacion que percibe esta definida?
¿Las decisiones estan definidas?
¿Los comportamientos estan definidos?
¿El movimiento esta definido?
¿La variedad es necesaria?
¿La memoria es necesaria?
¿Las tecnicas elegidas se justifican?
¿Hay tecnicas descartadas?
¿Hay feedback para el jugador?
¿Hay validacion posible?
¿Existe preset reutilizable?
¿La solucion deberia alimentar presets?
¿El costo es razonable?
¿La solucion simple alcanza?
```

---

## Regla final

```txt
IA aplicada al diseño de NPCs no guarda todas las recetas.

Define como crear buenos moldes,
como elegir sistemas
y como decidir si una solucion merece convertirse en preset.
```
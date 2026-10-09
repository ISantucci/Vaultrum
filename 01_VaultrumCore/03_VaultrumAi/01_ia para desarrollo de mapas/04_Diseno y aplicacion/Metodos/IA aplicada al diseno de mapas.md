# IA aplicada al diseno de mapas

## Definicion

IA aplicada al diseño de mapas es el criterio para usar estructuras espaciales, reglas de mapa y navegacion como soporte para gameplay, agentes y sistemas inteligentes.

No es una nota de algoritmos.

No es una nota de NPC.

No es una nota de movimiento.

No reemplaza a las notas tecnicas de representacion, reglas o pathfinding.

Existe para conectar el diseño del mapa con el uso real que hara el juego de esa informacion.

```txt
Mapa visual
→ mapa logico
→ sistemas que interpretan
→ experiencia jugable
```

---

## Responsabilidad de esta nota

Esta nota funciona como integradora de criterio.

Su responsabilidad es explicar:

```txt
como pensar mapas para IA y gameplay
como evitar sobrearquitectura espacial
como decidir estructura segun el juego
como conectar mapa logico con sistemas consumidores
como validar que el mapa realmente aporta valor
```

Esta nota no debe explicar en profundidad todos los conceptos tecnicos.

Debe indicar como aplicarlos con criterio.

---

## Problema que resuelve

El problema aparece cuando se diseña el mapa visual por un lado y la IA por otro, sin una estructura intermedia clara.

Ejemplo:

```txt
El escenario existe visualmente.
El NPC necesita moverse.
El pathfinding necesita datos.
El diseñador necesita controlar progresion.
Pero no hay mapa logico claro.
```

Esta nota ayuda a pensar:

```txt
¿Que informacion del mapa necesita el sistema para funcionar bien?
```

---

## Idea central

El mapa puede ser mucho mas que decorado.

Puede funcionar como una capa de informacion para sistemas.

Puede responder:

```txt
por donde se puede pasar
por donde conviene pasar
que zonas estan bloqueadas
que caminos se desbloquean
que puntos son importantes
que rutas existen
que zonas tienen riesgo
que partes del mapa deben guiar al jugador o agente
```

Pero esa informacion debe tener una razon.

No todo mapa necesita IA compleja.

---

## Mapa visual y mapa logico

El mapa visual es lo que ve el jugador.

El mapa logico es lo que interpreta el sistema.

```txt
Mapa visual
→ casas, caminos, paredes, puertas, rios, pasillos.

Mapa logico
→ nodos, conexiones, zonas, costos, bloqueos, rutas.
```

Ambos deben coincidir lo suficiente para que el comportamiento sea creible.

Si el mapa logico contradice al mapa visual, aparecen errores de lectura.

Ejemplo:

```txt
Visualmente hay una pared.
Logicamente el sistema cree que se puede pasar.

Resultado:
el agente atraviesa la pared.
```

---

## Mapa como proveedor de informacion

El mapa no deberia decidir todo.

Debe ofrecer informacion.

Ejemplo de informacion que puede proveer:

```txt
posiciones importantes
vecinos
conexiones
costos
bloqueos
zonas
rutas
estado de disponibilidad
```

Otros sistemas consumen esa informacion.

```txt
Pathfinding
→ consume estructura.

NPC
→ consume rutas o resultados, no todo el mapa.

Gameplay
→ puede modificar bloqueos o rutas.

Debug
→ visualiza datos.
```

La direccion de dependencia debe mantenerse limpia.

---

## Como decidir que necesita el mapa

Antes de diseñar el mapa logico, preguntar:

```txt
¿Que entidades usan el mapa?
¿Que necesitan saber?
¿Deben elegir ruta?
¿Deben evitar obstaculos?
¿Deben responder a cambios?
¿Deben preferir zonas?
¿El jugador debe entender esos caminos?
¿El mapa cambia por progreso?
¿Hay rutas alternativas?
¿Hay costos?
```

La estructura nace de estas respuestas.

No del deseo de usar una tecnica.

---

## Casos de aplicacion

### Ruta fija

Si una entidad siempre sigue el mismo camino:

```txt
Waypoints
→ probablemente alcanzan.
```

No hace falta pathfinding si no hay decision de ruta.

---

### Destino variable

Si una entidad debe llegar a distintos objetivos:

```txt
Representacion navegable
→ pathfinding
→ ruta
```

Puede requerir nodos, grilla o grafos segun el mapa.

---

### Mapa con zonas bloqueadas

Si algunas partes no pueden usarse:

```txt
zonas bloqueadas
→ reglas de mapa
→ consumidores evitan esas zonas
```

El bloqueo debe estar representado logicamente, no solo visualmente.

---

### Mapa con rutas alternativas

Si hay varios caminos posibles:

```txt
rutas alternativas
→ costos o condiciones
→ sistema consumidor elige o valida
```

La alternativa debe cambiar algo real.

---

### Mapa con progresion

Si el mapa cambia durante la partida:

```txt
desbloqueo de caminos
→ actualizacion del mapa logico
→ consumidores informados
```

No alcanza con abrir visualmente una puerta.

Debe cambiar la disponibilidad logica.

---

## Cuando implementar IA aplicada al diseño de mapas

Conviene trabajar esta capa cuando:

```txt
el mapa afecta decisiones
el mapa afecta navegacion
el mapa cambia durante la partida
hay agentes que deben interpretar el espacio
hay rutas alternativas
hay costos o bloqueos
hay progresion espacial
hay necesidad de debug visual
```

Ejemplo correcto:

```txt
Tower defense con caminos que se desbloquean por oleada
y enemigos que pueden tomar rutas distintas.

→ El mapa necesita una capa logica clara.
```

---

## Cuando NO implementarla

No conviene crear una capa compleja de mapa logico cuando:

```txt
el mapa es decorativo
el recorrido es completamente fijo
no hay decisiones espaciales
no hay sistemas consumidores
una ruta manual alcanza
la complejidad no cambia gameplay
```

Ejemplo:

```txt
Una cinemática donde un personaje camina siempre por el mismo sendero.

→ No necesita IA aplicada al diseño de mapas.
```

---

## Por que no implementarla de mas

Una capa de IA aplicada al mapa agrega costo.

Puede generar:

```txt
mas documentos
mas sistemas
mas datos
mas debug
mas puntos de fallo
mas tiempo de tuning
mas riesgo de desalineacion visual/logica
```

Regla:

```txt
Si el mapa logico no cambia decisiones ni comportamiento,
probablemente no hace falta.
```

---

## Mala practica al aplicarla

Malas practicas comunes:

```txt
diseñar mapas logicos sin necesidad
usar grillas, nodos y costos todos juntos por completismo
hacer que el mapa conozca estados de NPC
hacer que el NPC reconstruya el mapa
hacer que cada nota tecnica explique todo el sistema
crear rutas alternativas que nadie usa
crear costos que no modifican decisiones
no validar visualmente
no alinear mapa visual y mapa logico
```

Ejemplo de mala practica:

```txt
El mapa tiene nodos, grilla, costos, rutas alternativas y desbloqueos,
pero el juego solo tiene enemigos siguiendo una ruta fija.

→ Sobrearquitectura.
```

---

## Costos de implementacion

Aplicar IA al diseño de mapas puede requerir:

```txt
definir estructura logica
cargar datos de mapa
definir reglas
definir consumidores
crear debug visual
validar con gameplay
documentar decisiones
mantener consistencia visual/logica
integrar cambios de estado
```

No es solo agregar scripts.

Es crear una capa de lectura espacial.

---

## Costos de optimizacion

El costo depende de la estructura elegida.

Posibles costos:

```txt
cantidad de nodos o celdas
cantidad de conexiones
frecuencia de consultas
frecuencia de recalculo
actualizacion de costos dinamicos
cambios de rutas
validaciones de visibilidad
debug visual
allocations por consultas
```

Problemas frecuentes:

```txt
mapas demasiado densos
recalculos innecesarios
validaciones por frame
debug siempre activo
sistemas consumidores consultando todo el mapa
falta de cache
falta de eventos para cambios
```

---

## Criterio de optimizacion

Opciones para controlar costo:

```txt
usar la estructura minima suficiente
limitar densidad de nodos o celdas
actualizar por eventos
cachear datos estaticos
recalcular solo cuando cambia algo relevante
separar debug de runtime
evitar consultas globales frecuentes
distribuir calculos si hay muchos agentes
```

Ejemplo:

```txt
Mala practica:
todos los NPC consultan todo el mapa cada frame.

Mejor:
cada sistema consulta solo lo necesario,
con frecuencia controlada,
y usando eventos cuando cambia el mapa.
```

---

## Relacion con VaultrumAI

Dentro de VaultrumAI, esta nota debe funcionar como punto de criterio aplicado.

No debe reemplazar a:

```txt
Representacion de mapa
Navegacion y pathfinding
Reglas de mapa
IA para NPC
Algoritmos
```

Debe ayudar a decidir como usar esas partes juntas sin mezclarlas.

La direccion sana es:

```txt
Conceptos base
→ proveen informacion.

Reglas
→ agregan condiciones.

Algoritmos
→ procesan.

Sistemas consumidores
→ interpretan.

Diseño aplicado
→ decide si todo eso aporta valor al juego.
```

---

## Relacion con IA para NPC

La IA aplicada al diseño de mapas puede alimentar sistemas de NPC, pero no debe absorberlos.

Ejemplo:

```txt
Mapa
→ expone rutas y zonas.

NPC
→ decide objetivo.

Pathfinding
→ calcula ruta.

Movimiento
→ ejecuta.
```

El mapa no debe decidir que el NPC persigue.

El NPC no debe contener toda la estructura del mapa.

---

## Preguntas antes de aplicar esta capa

Antes de aplicar IA al diseño de mapas, una IA debe responder:

```txt
¿Que problema de diseño resuelve?
¿Que informacion necesita el sistema?
¿Quien consume esa informacion?
¿El mapa visual y logico coinciden?
¿La estructura simple alcanza?
¿Hace falta pathfinding?
¿Hace falta costo?
¿Hace falta bloqueo?
¿Hace falta ruta alternativa?
¿Hace falta desbloqueo?
¿Que se gana?
¿Que costo tiene?
¿Como se valida?
```

Si no se puede explicar el beneficio, no conviene expandir el sistema.

---

## Validacion visual

La capa de mapa logico debe poder validarse.

Se puede mostrar:

```txt
nodos
conexiones
grillas
celdas
zonas bloqueadas
zonas navegables
costos
rutas alternativas
rutas desbloqueadas
ruta calculada
estado actual del mapa
```

La validacion visual debe ayudar a detectar:

```txt
diferencias entre mapa visual y logico
zonas mal marcadas
costos incoherentes
rutas que no conectan
caminos visualmente abiertos pero logicamente cerrados
caminos logicamente abiertos pero visualmente cerrados
```

---

## Criterio para una IA

Cuando una IA proponga IA aplicada al diseño de mapas, debe justificar:

```txt
que problema del juego se esta resolviendo
que estructura minima alcanza
que sistemas consumen el mapa
que responsabilidad tiene cada parte
que costo de implementacion tiene
que costo de optimizacion tiene
como se valida
que queda fuera
```

No debe proponer:

```txt
usar todo
conectar todo
linkear todo
hacer el sistema mas completo porque si
```

Debe proponer lo necesario.

---

## Checklist

Antes de cerrar una decision de IA aplicada al diseño de mapas, revisar:

```txt
¿El mapa necesita ser leido por sistemas?
¿La estructura elegida responde al juego?
¿Se evito sobrearquitectura?
¿El mapa expone informacion sin decidir comportamiento?
¿Los sistemas consumidores estan claros?
¿Los costos, bloqueos o rutas tienen razon?
¿El mapa visual y logico coinciden?
¿Hay validacion visual?
¿Hay frecuencia de consultas controlada?
¿La solucion puede mantenerse?
```

---

## Regla final

IA aplicada al diseño de mapas no significa hacer mapas inteligentes por complejidad.

Significa darle al juego una forma clara de entender el espacio cuando eso aporta valor.

```txt
Mapa visual
→ experiencia visible

Mapa logico
→ informacion usable

Criterio de diseño
→ decide si hace falta
```
# Diseno y aplicacion de mapas

## Proposito

Esta subcarpeta reune criterios para aplicar representaciones de mapa, reglas espaciales y navegacion dentro de proyectos reales.

No existe para explicar todos los algoritmos en detalle.
No existe para duplicar notas tecnicas.
No existe para decidir comportamiento completo de NPC.
No existe para convertir todo mapa en un sistema complejo.

Existe para responder:

```txt
¿Que estructura de mapa conviene para este juego concreto?
```

---

## Idea central

La IA para desarrollo de mapas debe estar al servicio del diseño del juego.

No alcanza con que una estructura funcione tecnicamente.

Debe ayudar a:

```txt
guiar entidades
calcular rutas utiles
sostener decisiones de gameplay
controlar progresion
crear rutas alternativas
validar comportamiento
hacer el espacio mas legible
evitar comportamientos incoherentes
```

Un mapa logico vale si mejora el juego, la IA o el control del diseño.

---

## Responsabilidad de esta subcarpeta

Esta subcarpeta debe conectar tecnica con criterio de diseño.

Su responsabilidad incluye:

```txt
decidir cuando usar nodos
decidir cuando usar grillas
decidir cuando usar waypoints
decidir cuando usar pathfinding
evaluar sobrearquitectura
conectar mapas con gameplay
conectar mapas con NPCs sin mezclar responsabilidades
documentar decisiones de mapa
validar si una solucion espacial aporta valor
```

No es responsabilidad principal de esta subcarpeta explicar:

```txt
implementacion completa de A Star
implementacion completa de Theta Star
codigo detallado de NPC
todas las reglas de combate
todos los estados de IA
todos los patrones de arquitectura
```

Los conceptos tecnicos viven en sus notas correspondientes.

Esta subcarpeta decide como aplicarlos con criterio.

---

## Como usar esta subcarpeta

Usar esta subcarpeta cuando el problema sea de criterio aplicado.

Ejemplos:

```txt
No se si usar waypoints, nodos o grilla.
No se si necesito pathfinding.
No se si mi mapa esta sobrearquitecturado.
Quiero integrar rutas alternativas a gameplay.
Quiero documentar por que elegi una estructura de mapa.
Quiero saber si una solucion espacial ayuda al juego.
Quiero preparar una explicacion para una IA o equipo.
```

---

## Flujo recomendado

El flujo sano es:

```txt
1. Entender el tipo de juego.
2. Entender como se usa el espacio.
3. Identificar que entidades o sistemas necesitan leer el mapa.
4. Evaluar la solucion mas simple viable.
5. Revisar si hacen falta reglas, costos o pathfinding.
6. Elegir estructura.
7. Documentar motivo.
8. Validar en gameplay.
9. Ajustar complejidad solo si el problema lo justifica.
```

Esta subcarpeta no debe arrancar desde la tecnica.

Debe arrancar desde la necesidad del juego.

---

## [[IA aplicada al diseno de mapas]]

Nota integradora para pensar el mapa como sistema usable por IA, gameplay y diseño de niveles.

Sirve para conectar decisiones de estructura, navegacion y reglas espaciales sin convertir cada nota tecnica en un hub.

Pregunta principal:

```txt
¿Como se traduce esta estructura de mapa en una mejor experiencia o mejor sistema?
```

---

## Criterios de eleccion

### Cuando usar waypoints

Usar waypoints cuando:

```txt
el recorrido es simple
el camino esta predefinido
no hay muchas rutas alternativas
el agente solo necesita seguir puntos
el diseño necesita control manual
no hace falta calcular caminos
```

Ejemplo:

```txt
Patrulla simple entre puntos.
```

---

### Cuando usar nodos

Usar nodos cuando:

```txt
hay puntos importantes del mapa
hay conexiones entre posiciones
se necesita elegir entre rutas
el mapa no necesariamente es una grilla
el escenario tiene zonas conectadas
se necesita una red navegable mas flexible
```

Ejemplo:

```txt
NPC que puede moverse entre sectores del escenario.
```

---

### Cuando usar grillas

Usar grillas cuando:

```txt
el mapa funciona por celdas
el juego es tactico o tile-based
las reglas dependen de casilleros
el pathfinding necesita vecinos regulares
la posicion logica importa mas que la posicion libre
```

Ejemplo:

```txt
Juego tactico por turnos.
```

---

### Cuando usar pathfinding

Usar pathfinding cuando:

```txt
el destino es variable
hay obstaculos
hay multiples rutas posibles
el agente debe encontrar camino
el mapa cambia o tiene costos
una ruta fija no alcanza
```

Ejemplo:

```txt
Enemigo que debe perseguir al jugador en un escenario con obstaculos.
```

---

### Cuando NO usar pathfinding

No usar pathfinding cuando:

```txt
el recorrido es fijo
el agente no necesita elegir camino
el mapa no tiene obstaculos relevantes
una ruta manual alcanza
una spline alcanza
una secuencia de waypoints alcanza
el costo tecnico no se justifica
```

Ejemplo:

```txt
Objeto que se mueve siempre por la misma ruta.
```

---

## Costos de diseño

Cada decision de mapa tiene costo de diseño.

Ejemplos:

```txt
Waypoints
→ simples, controlables, pero poco flexibles.

Nodos
→ flexibles, buenos para caminos conectados, pero requieren conexiones claras.

Grillas
→ ordenadas y faciles de consultar, pero pueden forzar lectura por celdas.

Pathfinding
→ potente para destinos variables, pero agrega complejidad y costo tecnico.

Costos
→ permiten decisiones mas finas, pero requieren tuning.

Rutas alternativas
→ enriquecen el mapa, pero aumentan validacion y balance.
```

La mejor solucion no es la mas avanzada.

Es la que resuelve mejor el problema con menor complejidad razonable.

---

## Costos de implementacion

Antes de elegir una estructura, considerar:

```txt
tiempo de implementacion
tiempo de debug
cantidad de datos a cargar
facilidad para modificar el mapa
facilidad para validar visualmente
impacto en otros sistemas
cantidad de agentes que lo usaran
frecuencia de recalculo
mantenibilidad
```

Un sistema espacial puede funcionar tecnicamente y aun asi ser malo para el proyecto si es dificil de mantener.

---

## Costos de optimizacion

La decision de mapa tambien afecta rendimiento.

Posibles costos:

```txt
cantidad de nodos
cantidad de conexiones
cantidad de celdas
frecuencia de recalculo de rutas
cantidad de agentes consultando el mapa
validaciones de line of sight
actualizacion de costos dinamicos
debug visual excesivo
allocations por consultas frecuentes
```

Preguntas clave:

```txt
¿Cuantos agentes usan esta estructura?
¿Cada cuanto consultan?
¿Cada cuanto recalculan?
¿El mapa cambia?
¿Se puede cachear informacion?
¿Se puede actualizar por eventos?
¿Hay debug desactivable?
```

Una solucion buena para un prototipo puede no escalar si se usa sin control.

---

## Mala practica en diseño de mapas logicos

Malas practicas comunes:

```txt
usar grillas porque parecen ordenadas aunque el juego no las necesite
usar grafos porque parecen mas profesionales
usar pathfinding para recorridos fijos
duplicar logica entre mapa y NPC
guardar decisiones de comportamiento dentro del mapa
guardar estructura de mapa dentro del NPC
crear costos sin significado
crear rutas alternativas que no cambian gameplay
no validar visualmente
hacer que el mapa dependa de todos sus consumidores
```

Ejemplo de mala practica:

```txt
El mapa sabe que el NPC persigue, huye, ataca y patrulla.

Problema:
el mapa dejo de representar espacio
y empezo a conocer comportamientos.
```

La direccion correcta es:

```txt
Mapa
→ expone estructura y reglas.

Sistema consumidor
→ interpreta y decide.
```

---

## Preguntas antes de diseñar la estructura

Antes de definir la estructura del mapa, una IA debe responder:

```txt
¿Que necesita hacer el juego con el espacio?
¿Quien consume la informacion del mapa?
¿El recorrido es fijo o variable?
¿El destino cambia?
¿Hay obstaculos?
¿Hay rutas alternativas?
¿Hay costos?
¿El mapa cambia durante la partida?
¿La solucion simple alcanza?
¿Como se valida visualmente?
¿Que costo tecnico tiene?
¿Que parte queda fuera de esta estructura?
```

Si estas preguntas no tienen respuesta, todavia no conviene definir una arquitectura cerrada.

---

## Relacion con proyectos reales

En un proyecto real, la decision de mapa debe considerar:

```txt
tipo de juego
tamaño del escenario
cantidad de agentes
frecuencia de recalculo
necesidad de rutas alternativas
claridad visual
facilidad de debug
costo de implementacion
mantenibilidad
herramientas disponibles
tiempo del equipo
```

El mapa logico debe servir al proyecto.

No al ego tecnico.

---

## Relacion con IA para NPC

Esta subcarpeta puede conectar con IA para NPC, pero sin mezclar responsabilidades.

```txt
Diseno de mapa
→ define como se estructura el espacio.

IA para NPC
→ define como una entidad percibe, decide y actua.

Integracion con Pathfinding
→ conecta decision del NPC con ruta calculada.
```

Ejemplo:

```txt
El NPC decide huir.
El sistema de mapa ofrece rutas.
Pathfinding calcula camino.
Movimiento ejecuta.
```

El mapa no decide huir.

El NPC no deberia reconstruir todo el mapa.

---

## Criterio para una IA

Cuando una IA trabaje con esta subcarpeta, debe evitar proponer estructuras avanzadas sin justificar.

Antes debe responder:

```txt
¿Que experiencia busca el juego?
¿Que necesita hacer el agente o sistema?
¿El mapa necesita ser leido por sistemas?
¿La solucion simple alcanza?
¿Que trade-off tiene la tecnica propuesta?
¿Como se valida en gameplay?
¿Como se documenta la decision?
```

No alcanza con decir:

```txt
Usar nodos.
Usar grilla.
Usar A Star.
```

Debe explicar por que esa decision mejora el proyecto.

---

## Resultado esperado

Despues de usar esta subcarpeta, una persona o una IA deberia poder explicar:

```txt
que estructura de mapa conviene
por que conviene
que problema resuelve
que problema no resuelve
que costo tiene
como se integra con gameplay
como se valida
que queda fuera
```

---

## Checklist

Antes de cerrar una decision de mapa, revisar:

```txt
¿La estructura responde a una necesidad real?
¿La solucion simple fue considerada?
¿Se evito sobrearquitectura?
¿Esta claro quien consume el mapa?
¿Esta claro que datos expone el mapa?
¿Esta claro que NO debe hacer el mapa?
¿Hay criterio de validacion?
¿Hay costo de implementacion aceptable?
¿Hay costo de optimizacion controlado?
¿La decision puede explicarse a una IA o equipo?
```

---

## Regla final

El diseño de mapas no empieza preguntando que algoritmo usar.

Empieza preguntando que necesita el juego.

```txt
Necesidad del juego
→ estructura minima suficiente
→ tecnica adecuada
→ validacion en gameplay
```
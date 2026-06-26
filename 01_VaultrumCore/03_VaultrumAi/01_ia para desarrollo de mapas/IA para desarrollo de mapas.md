## Propósito

Esta sección organiza el conocimiento relacionado con la representación, análisis y uso lógico del espacio dentro de un videojuego.

Su función es ayudar a convertir un mapa visual en información útil para sistemas de navegación, pathfinding, reglas de gameplay o toma de decisiones.

No existe para juntar algoritmos sueltos.

Existe para ordenar responsabilidades espaciales.

La pregunta central de esta sección es:

¿Cómo entiende el sistema el espacio del juego?

---

## Idea central

Un mapa no es solamente escenario visual.

También puede ser información estructurada.

El mapa puede definir puntos navegables, conexiones, costos, zonas bloqueadas, rutas, obstáculos, caminos desbloqueables o posiciones relevantes.

La relación base es:

Mapa visual  
→ Representación lógica  
→ Navegación  
→ Decisión  
→ Movimiento

El mapa no decide por el NPC.

El mapa ofrece información para que otros sistemas puedan decidir, navegar o moverse mejor.

---

## Responsabilidad de esta sección

Esta sección se encarga de organizar conocimiento sobre cómo representar y usar el espacio del juego.

Su responsabilidad es ayudar a definir:

- cómo se representa el mapa;
    
- cómo se conectan posiciones;
    
- cómo se calculan rutas;
    
- cómo se aplican reglas espaciales;
    
- cómo se validan caminos;
    
- cómo se prepara información para NPCs u otros sistemas.
    

No es responsabilidad principal de esta sección explicar percepción, estados, comportamiento, ataque, huida o toma de decisiones de NPC.

Esos temas pertenecen a:

[[IA para NPC]]

---

## [[Representacion de mapa]]

Agrupa las formas de convertir el espacio del juego en información útil para sistemas.

Esta rama responde principalmente:

¿Cómo represento el mapa para que el sistema pueda leerlo?

Usar esta rama cuando el problema esté relacionado con nodos, grillas, waypoints, grafos, conexiones, vecinos o estructuras navegables.

---

## [[Navegacion y pathfinding]]

Agrupa los conceptos relacionados con calcular, validar o recorrer caminos dentro del espacio del juego.

Esta rama responde principalmente:

¿Cómo calculo o valido una ruta entre dos puntos?

Usar esta rama cuando el problema esté relacionado con pathfinding, búsqueda de caminos, rutas, nodo más cercano, target real, line of sight o validación visual de recorridos.

---

## [[Reglas de mapa]]

Agrupa criterios que modifican cómo se interpreta o se recorre el mapa.

Esta rama responde principalmente:

¿Qué reglas afectan por dónde se puede o conviene pasar?

Usar esta rama cuando el problema esté relacionado con costos, zonas navegables, zonas bloqueadas, rutas alternativas, caminos desbloqueables o cambios dinámicos del mapa.

---

## [[Diseno y aplicacion de mapas]]

Agrupa criterios para aplicar mapas lógicos en proyectos reales sin sobrecomplicar.

Esta rama responde principalmente:

¿Qué representación conviene para este juego concreto?

Usar esta rama cuando el problema no sea solo técnico, sino de decisión: cuándo usar nodos, grillas, waypoints, grafos, pathfinding, reglas de mapa o una solución más simple.

---

## Relación con IA para NPC

IA para desarrollo de mapas e IA para NPC están conectadas, pero no cumplen la misma responsabilidad.

IA para desarrollo de mapas responde:

¿Cómo entiende el sistema el espacio?

IA para NPC responde:

¿Qué quiere hacer una entidad dentro de ese espacio?

La separación sana es:

NPC  
→ define intención.

Mapa lógico  
→ define estructura navegable.

Pathfinding  
→ calcula camino.

Movimiento  
→ ejecuta ruta.

Un NPC no debería absorber toda la representación lógica del mapa.

Un mapa no debería decidir el comportamiento del NPC.

---

## Regla final

La IA para desarrollo de mapas no existe para hacer mapas más complejos.

Existe para hacer que el espacio del juego sea entendible y útil para los sistemas.

Primero responsabilidad.

Después técnica.
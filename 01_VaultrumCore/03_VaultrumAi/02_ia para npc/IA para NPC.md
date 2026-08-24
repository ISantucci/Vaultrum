## Propósito

Esta sección organiza el conocimiento necesario para diseñar, documentar e implementar inteligencia artificial para NPCs en videojuegos.

La IA para NPC se enfoca en entidades que cumplen un rol dentro del juego, reciben información, toman decisiones y ejecutan comportamientos.

No existe para acumular técnicas de comportamiento.

Existe para ordenar responsabilidades de una entidad dentro del mundo.

La pregunta central de esta sección es:

¿Cómo actúa una entidad dentro del juego?

---

## Idea central

Un NPC no es solamente un objeto que se mueve.

Un NPC puede percibir, decidir, cambiar de estado, ejecutar acciones, desplazarse, reaccionar al jugador o cumplir un rol dentro del diseño del juego.

La relación base es:

NPC  
→ Percepción  
→ Toma de decisiones  
→ Comportamiento  
→ Movimiento  
→ Validación

Cada parte debe tener una responsabilidad clara.

La IA para NPC no empieza por técnica.

Empieza por rol, responsabilidad y utilidad dentro del juego.

---

## Responsabilidad de esta sección

Esta sección se encarga de organizar conocimiento sobre cómo diseñar y construir NPCs.

Su responsabilidad es ayudar a definir:

- qué es el NPC;
    
- qué rol cumple;
    
- qué información recibe;
    
- cómo decide;
    
- qué comportamientos puede ejecutar;
    
- cómo se mueve;
    
- cómo se combinan sus sistemas;
    
- cómo crear moldes reutilizables.
    

No es responsabilidad principal de esta sección explicar representación lógica de mapas, costos, zonas bloqueadas o cálculo completo de rutas.

Esos temas pertenecen a:

`IA para desarrollo de mapas`

---

## [[NPC]]

Define qué es un NPC, qué rol cumple dentro del juego y qué límites debe respetar como entidad.

Esta nota funciona como base conceptual.

No debe absorber percepción, decisión, comportamiento, movimiento ni pathfinding.

---

## [[Percepcion]]

Agrupa los conceptos relacionados con cómo un NPC recibe información del mundo.

Esta rama responde principalmente:

¿Qué información puede detectar o recibir el NPC?

Usar esta rama cuando el problema esté relacionado con detección, visión, escucha, rango, estímulos o formas de percibir al jugador y al entorno.

---

## [[Comportamientos]]

Agrupa las acciones o modos que un NPC puede ejecutar.

Esta rama responde principalmente:

¿Qué puede hacer el NPC?

Usar esta rama cuando el problema esté relacionado con patrullar, perseguir, atacar, huir, esperar, interactuar o ejecutar acciones concretas.

---

## [[Toma de decisiones]]

Agrupa los sistemas que permiten decidir qué comportamiento ejecutar.

Esta rama responde principalmente:

¿Cómo elige el NPC qué hacer?

Usar esta rama cuando el problema esté relacionado con estados, árboles de decisión, selección ponderada, prioridades, condiciones o transición entre comportamientos.

---

## [[Movimiento]]

Agrupa los conceptos relacionados con el desplazamiento físico del NPC.

Esta rama responde principalmente:

¿Cómo se mueve el NPC dentro del mundo?

Usar esta rama cuando el problema esté relacionado con steering, avoidance, seguimiento de rutas, integración con pathfinding o ejecución espacial del movimiento.

---

## [[Diseno y aplicacion de NPCs]]

Agrupa el criterio para combinar percepción, decisión, comportamiento y movimiento según el rol del NPC y las necesidades del juego.

Esta rama responde principalmente:

¿Cómo diseño un NPC concreto sin mezclar responsabilidades?

No es una carpeta de recetas finales.

Funciona como guía para crear, evaluar y ajustar NPCs según contexto real.

---

## [[NPC Presets]]

Agrupa moldes reutilizables de NPCs.

Cada preset documenta una combinación concreta de sistemas para resolver un tipo de NPC frecuente.

Esta rama responde principalmente:

¿Qué combinaciones reutilizables existen para crear NPCs concretos?

Los presets pueden autonutrirse a medida que se desarrollan NPCs reales en proyectos.

---

## Relación con IA para desarrollo de mapas

IA para NPC e IA para desarrollo de mapas están conectadas, pero no cumplen la misma responsabilidad.

IA para NPC responde:

¿Qué quiere hacer la entidad?

IA para desarrollo de mapas responde:

¿Cómo entiende el sistema el espacio donde esa entidad se mueve?

La separación sana es:

NPC  
→ define rol, intención y comportamiento.

Mapa lógico  
→ define estructura navegable.

Pathfinding  
→ calcula camino.

Movimiento  
→ ejecuta ruta.

Un NPC puede usar información del mapa.

Pero no debería absorber toda la lógica de representación del mapa.

---

## Regla final

La IA para NPC no empieza por técnica.

Empieza por rol, responsabilidad y utilidad dentro del juego.

Primero se define qué debe ser el NPC.

Después se elige cómo percibe, decide, actúa y se mueve.
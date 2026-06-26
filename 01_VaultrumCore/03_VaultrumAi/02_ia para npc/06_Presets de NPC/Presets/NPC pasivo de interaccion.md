## Definicion

NPC pasivo de interaccion es un preset para personajes cuya funcion principal es responder al jugador mediante dialogo, comercio, informacion, entrega de misiones o interaccion contextual.

```txt
NPC pasivo
→ espera interaccion
→ responde
→ entrega informacion, servicio o evento
```

No esta pensado para combate, persecucion, huida ni navegacion compleja.

---

## Rol de gameplay

Este preset sirve para NPCs que existen para cumplir una funcion clara dentro del mundo o del flujo del jugador.

Ejemplos:

```txt
comerciante
personaje de quest
guia
NPC narrativo
personaje que entrega informacion
NPC que abre una tienda
NPC que inicia una conversacion
```

Su valor no esta en moverse o decidir de forma compleja.

Su valor esta en ser claro, confiable y facil de interactuar.

---

## Cuando usarlo

Usar este preset cuando:

```txt
el NPC debe responder a interaccion directa
el NPC debe mostrar dialogo
el NPC debe abrir tienda
el NPC debe entregar informacion
el NPC no necesita tomar decisiones complejas
el NPC no necesita reaccionar dinamicamente al jugador
```

Pregunta clave:

```txt
¿El jugador necesita hablar, comprar, recibir informacion o activar algo?
```

---

## Cuando no usarlo

No usar este preset si:

```txt
el NPC debe patrullar
el NPC debe perseguir
el NPC debe atacar
el NPC debe huir
el NPC debe reaccionar a amenazas
el NPC debe tomar decisiones complejas
```

En esos casos conviene partir de otro preset.

---

## Sistemas necesarios

```txt
sistema de interaccion
trigger o distancia de interaccion
dialogo o respuesta
feedback visual
estado simple de disponibilidad
```

Ejemplos de feedback:

```txt
icono de interactuar
outline
texto flotante
prompt de tecla
burbuja de dialogo
```

---

## Sistemas opcionales

```txt
inventario o tienda
sistema de misiones
estado de conversacion
condiciones de desbloqueo
animacion idle
rutina simple
voz o sonido
```

---

## Sistemas que NO necesita

Normalmente no necesita:

```txt
Field of View
deteccion del jugador compleja
pathfinding
steering
obstacle avoidance
seleccion ponderada
arbol de decision complejo
persecucion
ataque
huida
```

Regla:

```txt
No agregar IA de percepcion o combate si el NPC solo cumple una funcion de interaccion.
```

---

## Flujo de comportamiento

```txt
1. NPC permanece disponible.
2. Jugador entra en rango o apunta al NPC.
3. Sistema muestra feedback de interaccion.
4. Jugador interactua.
5. NPC ejecuta respuesta.
6. Se abre dialogo, tienda, informacion o evento.
7. NPC vuelve a estado disponible si corresponde.
```

---

## Estructura recomendada

```txt
NPCInteractionController
→ recibe interaccion.

InteractionPrompt
→ muestra feedback.

DialogueProvider / ShopProvider / QuestProvider
→ entrega contenido especifico.

NPCState
→ define si esta disponible, bloqueado o ya usado.
```

Separacion esperada:

```txt
interaccion
→ detecta input o proximidad.

contenido
→ define que responde.

estado
→ define si puede responder.
```

---

## Datos necesarios

```txt
nombre del NPC
tipo de interaccion
rango de interaccion
texto o dialogo
estado de disponibilidad
condiciones de desbloqueo
feedback visual
```

Opcional:

```txt
items de tienda
mision asociada
dialogos alternativos
sonido de interaccion
animacion idle
```

---

## Variantes posibles

```txt
comerciante
NPC de quest
guia de tutorial
NPC narrativo
NPC que desbloquea puerta
NPC que entrega objeto
NPC con dialogo segun progreso
```

---

## Costos de implementacion

Costo bajo a medio.

Puede requerir:

```txt
sistema de interaccion
UI de dialogo
datos de conversacion
validacion de rango
feedback visual
integracion con misiones o tienda
```

El costo aumenta si:

```txt
hay multiples ramas de dialogo
hay tienda
hay condiciones por progreso
hay persistencia de estado
```

---

## Costos de optimizacion

Normalmente bajo.

Riesgos:

```txt
buscar jugador constantemente
activar UI innecesariamente
tener muchos NPCs con triggers mal configurados
actualizar dialogos cada frame
```

Alternativas:

```txt
usar triggers
cachear referencia al jugador
activar prompt solo en rango
evaluar condiciones al interactuar
```

---

## Validacion

Validar:

```txt
si el jugador entiende que puede interactuar
si la interaccion ocurre solo en rango
si el dialogo o tienda se abre correctamente
si el NPC no responde cuando esta bloqueado
si el feedback aparece y desaparece bien
```

Debug util:

```txt
rango de interaccion visible
estado actual del NPC
logs de interaccion
estado de desbloqueo
```

---

## Errores comunes

```txt
agregar sistemas de IA innecesarios
no dar feedback de interaccion
mezclar dialogo, tienda e input en una sola clase
no controlar estado de disponibilidad
hacer que el NPC dependa de logica global sin necesidad
```

---

## Criterio para una IA

Cuando una IA use este preset debe:

```txt
mantenerlo simple
priorizar claridad de interaccion
no agregar percepcion compleja
no agregar movimiento si no aporta
separar input, contenido y estado
validar feedback para el jugador
```

---

## Checklist

```txt
¿El NPC solo necesita responder a interaccion?
¿El rango esta definido?
¿Hay feedback visual?
¿El contenido esta separado de la interaccion?
¿Hay estado de disponibilidad?
¿Necesita tienda, dialogo o quest?
¿Se evitaron sistemas innecesarios?
```

---

## Regla final

```txt
Un NPC pasivo no necesita parecer inteligente.

Necesita responder de forma clara y confiable.
```
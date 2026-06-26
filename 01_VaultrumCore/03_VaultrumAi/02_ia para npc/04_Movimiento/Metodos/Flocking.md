## Definición

Flocking es una técnica de movimiento grupal que permite que varios agentes se desplacen de forma coordinada usando reglas locales simples.

Se usa para simular grupos, bandadas, enjambres, multitudes o unidades que se mueven juntas sin depender de un controlador central absoluto.

```txt
Agente
→ observa vecinos cercanos
→ calcula tendencias locales
→ ajusta su movimiento
→ genera comportamiento grupal
```

Flocking no decide el objetivo general del grupo.

Solo ayuda a que los agentes se muevan de forma colectiva y orgánica.

---

## Responsabilidad

La responsabilidad de Flocking es coordinar movimiento grupal a partir de reglas locales entre agentes.

Debe responder:

```txt
¿Cómo se mueve un agente en relación con sus vecinos?
¿Cómo evita amontonarse?
¿Cómo mantiene dirección similar al grupo?
¿Cómo permanece cerca del grupo?
¿Cómo se genera movimiento colectivo sin controlar cada agente manualmente?
```

Flocking pertenece a movimiento.

No pertenece a toma de decisiones.

No pertenece a percepción general.

No pertenece a pathfinding.

---

## Reglas principales

Flocking suele apoyarse en tres reglas base:

```txt
Separation
→ evitar amontonamiento.

Alignment
→ alinearse con la dirección promedio de los vecinos.

Cohesion
→ acercarse al centro del grupo.
```

La combinación de estas reglas puede generar movimiento grupal creíble a partir de decisiones locales simples.

---

## Separation

Separation busca que un agente se aleje de vecinos demasiado cercanos.

Responde:

```txt
¿Estoy demasiado cerca de otros agentes?
```

Sirve para evitar:

```txt
superposición
amontonamiento
choques entre agentes
movimiento grupal ilegible
```

Ejemplo conceptual:

```txt
Si un vecino está demasiado cerca
→ generar dirección opuesta
→ aumentar separación
```

---

## Alignment

Alignment busca que un agente tienda a moverse en una dirección similar a la de sus vecinos.

Responde:

```txt
¿Hacia dónde se está moviendo el grupo cercano?
```

Sirve para generar:

```txt
bandadas
enjambres
grupos que avanzan juntos
unidades con dirección común
```

Ejemplo conceptual:

```txt
Calcular dirección promedio de vecinos
→ ajustar dirección propia hacia ese promedio
```

---

## Cohesion

Cohesion busca que un agente permanezca cerca del grupo.

Responde:

```txt
¿Dónde está el centro de mis vecinos cercanos?
```

Sirve para evitar que los agentes se dispersen demasiado.

Ejemplo conceptual:

```txt
Calcular centro promedio de vecinos
→ moverse levemente hacia ese centro
```

---

## Qué problema resuelve

Flocking ayuda cuando varios agentes deben moverse como grupo sin que cada uno tenga una ruta manual o una decisión individual compleja.

Puede aportar en:

```txt
bandadas de aves
enjambres de insectos
peces
multitudes
grupos de enemigos
unidades aliadas
criaturas que se mueven en manada
```

Sin flocking, los agentes pueden:

```txt
superponerse
moverse todos igual
chocar entre sí
separarse sin control
parecer demasiado rígidos
```

---

## Datos que necesita

Flocking puede necesitar:

```txt
posición actual del agente
velocidad actual
vecinos cercanos
radio de percepción local
distancia mínima de separación
peso de separation
peso de alignment
peso de cohesion
velocidad máxima
aceleración máxima
delta time
```

No todos los proyectos necesitan todos estos datos.

La cantidad de vecinos y la frecuencia de cálculo afectan mucho el costo del sistema.

---

## Qué produce

Flocking puede producir:

```txt
dirección deseada
fuerza resultante
velocidad ajustada
tendencia de separación
tendencia de alineación
tendencia de cohesión
```

Ejemplo:

```txt
Fuerza final
= Separation * peso
+ Alignment * peso
+ Cohesion * peso
```

Esa salida no decide el objetivo del agente.

Solo ajusta cómo se mueve dentro del grupo.

---

## Relación con Steering Behaviours

Flocking puede entenderse como una composición de Steering Behaviours.

```txt
Steering Behaviours
→ técnicas generales de movimiento.

Flocking
→ combinación de steering para movimiento grupal.
```

Separation, Alignment y Cohesion funcionan como tendencias de steering combinadas.

Por eso Flocking vive dentro de Movimiento, pero merece nota propia cuando el movimiento grupal necesita explicarse con más profundidad.

---

## Qué NO debe hacer

Flocking no debe:

```txt
decidir comportamiento general
elegir objetivos estratégicos
calcular pathfinding completo
reemplazar estados del NPC
reemplazar toma de decisiones
controlar combate
resolver animaciones completas
mover todos los agentes desde una clase monolítica sin separación
```

Ejemplo incorrecto:

```txt
FlockingSystem
→ decide atacar
→ calcula ruta global
→ mueve agentes
→ aplica daño
→ cambia estados
```

Ejemplo correcto:

```txt
Toma de decisiones
→ define intención general.

Movimiento
→ solicita desplazamiento.

Flocking
→ ajusta movimiento grupal según vecinos.
```

Regla:

```txt
Flocking coordina movimiento local de grupo.

No decide la IA completa.
```

---

## Cuándo conviene usarlo

Conviene usar Flocking cuando:

```txt
hay varios agentes moviéndose juntos
se busca movimiento grupal orgánico
los agentes no deben superponerse
se quiere evitar controlar cada agente manualmente
el grupo debe reaccionar localmente
la formación no necesita ser rígida
```

Pregunta clave:

```txt
¿El problema es movimiento grupal local?
```

Si la respuesta es sí, Flocking puede aportar valor.

---

## Cuándo NO conviene usarlo

No conviene usar Flocking si:

```txt
hay pocos agentes
el grupo necesita una formación exacta
los agentes se mueven por grilla estricta
cada agente necesita decisiones muy diferentes
el movimiento simple alcanza
el costo de calcular vecinos no se justifica
```

Ejemplos:

```txt
un solo enemigo
NPC de diálogo
grupo que sigue waypoints fijos sin interacción local
unidades tácticas por casillas
formación militar rígida
```

Regla:

```txt
No usar Flocking si no hay problema real de movimiento grupal.
```

---

## Riesgos comunes

Riesgos comunes al implementar Flocking:

```txt
calcular todos contra todos sin optimización
usar radios mal ajustados
dar demasiado peso a una sola regla
generar vibración
hacer que el grupo se disperse demasiado
hacer que todos se amontonen
no limitar velocidad o fuerza
mezclar decisión con movimiento grupal
no debuggear vecinos ni fuerzas
```

El costo puede crecer rápido si muchos agentes buscan vecinos cada frame.

---

## Validación

Flocking se valida revisando:

```txt
si los agentes mantienen distancia
si el grupo se mueve de forma coherente
si no hay amontonamiento
si no hay dispersión excesiva
si las reglas se combinan con sentido
si el movimiento aporta al gameplay
```

Debug útil:

```txt
radio de vecinos
vecinos detectados
vector de separation
vector de alignment
vector de cohesion
fuerza final
velocidad resultante
```

---

## Regla final

Flocking no es una IA completa.

Es movimiento grupal basado en reglas locales.

Separation evita amontonamiento.

Alignment alinea dirección.

Cohesion mantiene grupo.

Primero movimiento grupal.

Después técnica.
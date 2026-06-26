## Definicion

Ataque es un comportamiento en el que un NPC ejecuta una accion ofensiva contra un objetivo.

Puede implicar daño, empuje, proyectiles, animaciones, cooldowns, area de efecto o condiciones de rango.

```txt
Ataque
→ accion ofensiva
→ objetivo valido
→ condicion cumplida
→ efecto aplicado
```

Atacar no es lo mismo que detectar o perseguir.

Un NPC puede detectar y perseguir sin atacar todavia.

---

## Responsabilidad

La responsabilidad del ataque es ejecutar una accion ofensiva cuando las condiciones necesarias se cumplen.

Debe responder:

```txt
¿Tengo un objetivo valido?
¿Estoy en rango?
¿Puedo atacar ahora?
¿El ataque esta en cooldown?
¿Que efecto produce?
¿Cuando termina el ataque?
¿Que feedback muestra?
```

Ataque puede aplicar daño o activar un efecto.

No debe decidir toda la IA del NPC.

---

## Que NO debe hacer

Ataque no debe absorber:

```txt
deteccion del jugador
decision completa
persecucion
pathfinding
movimiento general
control total de animaciones
sistema completo de vida
UI
drops
spawning
```

Ejemplo incorrecto:

```txt
AttackBehaviour
→ busca jugador
→ decide perseguir
→ mueve al NPC
→ calcula ruta
→ aplica daño
→ cambia estado global
```

Ejemplo correcto:

```txt
AttackBehaviour
→ verifica condiciones de ataque
→ ejecuta ataque
→ informa finalizacion o cooldown.

Sistema de vida
→ recibe daño.

Sistema de decision
→ decide si seguir atacando, perseguir o huir.
```

Regla:

```txt
Ataque ejecuta ofensiva.
No reemplaza decision, deteccion ni movimiento.
```

---

## Que problema resuelve

Ataque define como un NPC amenaza, daña o afecta al jugador u otros objetivos.

Puede resolver:

```txt
enemigos cuerpo a cuerpo
enemigos a distancia
bosses
animales agresivos
aliados que ayudan al jugador
torretas o entidades hostiles
guardianes
```

Un ataque bien definido permite equilibrar:

```txt
daño
rango
frecuencia
anticipacion
riesgo
feedback
ventana de respuesta del jugador
```

---

## Datos que necesita

Ataque puede necesitar:

```txt
objetivo
rango
daño
cooldown
tiempo de anticipacion
duracion
area de efecto
punto de origen
layer de objetivos
estado de disponibilidad
referencia al sistema de vida o daño
feedback visual
feedback sonoro
```

No todos los ataques necesitan todos esos datos.

Ejemplo simple:

```txt
enemigo melee
→ rango
→ daño
→ cooldown
```

Ejemplo avanzado:

```txt
boss
→ fases
→ patrones
→ areas
→ anticipacion
→ proyectiles
→ telegraphs
→ ventanas de vulnerabilidad
```

---

## Que produce

Ataque puede producir:

```txt
daño aplicado
efecto ofensivo
evento de ataque iniciado
evento de impacto
evento de ataque terminado
cooldown activado
feedback visual o sonoro
```

Ejemplo:

```txt
AttackStarted = true
DamageApplied = 10
CooldownStarted = true
```

Eso no significa que el NPC decida perseguir o huir.

Solo significa que el comportamiento ofensivo se ejecuto.

---

## Como funciona

Un ataque simple puede seguir este flujo:

```txt
1. Recibir objetivo.
2. Verificar rango.
3. Verificar cooldown.
4. Ejecutar anticipacion si existe.
5. Aplicar efecto.
6. Activar feedback.
7. Entrar en cooldown.
```

Ejemplo conceptual:

```csharp
using UnityEngine;

public interface IDamageable
{
    void TakeDamage(int amount);
}

public class MeleeAttack
{
    private readonly Transform owner;
    private readonly float range;
    private readonly int damage;
    private readonly float cooldown;

    private float lastAttackTime = -999f;

    public MeleeAttack(
        Transform owner,
        float range,
        int damage,
        float cooldown)
    {
        this.owner = owner;
        this.range = range;
        this.damage = damage;
        this.cooldown = cooldown;
    }

    public bool CanAttack(Transform target, float currentTime)
    {
        if (currentTime < lastAttackTime + cooldown)
        {
            return false;
        }

        float distance = Vector3.Distance(owner.position, target.position);
        return distance <= range;
    }

    public void Execute(IDamageable target, float currentTime)
    {
        target.TakeDamage(damage);
        lastAttackTime = currentTime;
    }
}
```

Este ejemplo se limita a ataque.

No detecta, no persigue y no decide todo el comportamiento.

---

## Tipos de ataque

Ataques comunes:

```txt
cuerpo a cuerpo
a distancia
area de efecto
carga
proyectil
explosion
empuje
debilitacion
ataque por fases
ataque con anticipacion visual
```

Cada tipo tiene costos y validaciones distintas.

Ejemplo:

```txt
Ataque cuerpo a cuerpo
→ depende de rango y timing.

Ataque a distancia
→ depende de linea de disparo, proyectil o hitscan.

Ataque de area
→ depende de zona, anticipacion y feedback.
```

---

## Como aplicarlo en videojuegos

Conviene implementar ataque cuando el NPC debe representar amenaza, oposicion o asistencia ofensiva.

Ejemplos:

```txt
enemigos
bosses
aliados combatientes
animales agresivos
torretas
guardianes
entidades hostiles
```

Preguntas utiles:

```txt
¿El NPC debe dañar o afectar a otro objetivo?
¿El jugador debe poder anticipar el ataque?
¿Hay rango claro?
¿Hay cooldown?
¿Hay feedback?
¿Hay forma de evitarlo o responder?
```

---

## Relacion con vida y daño

Ataque puede aplicar daño, pero no debe manejar toda la vida del objetivo.

Separacion sana:

```txt
Ataque
→ dispara o calcula efecto ofensivo.

Sistema de daño
→ aplica daño.

Sistema de vida
→ reduce vida y evalua muerte.
```

Esto evita que el ataque conozca demasiados detalles del objetivo.

---

## Cuando conviene implementarlo

Conviene implementar ataque cuando:

```txt
el NPC debe generar amenaza
el NPC debe dañar al jugador
el NPC debe afectar a otro objetivo
el combate es parte del rol
el jugador necesita responder a una ofensiva
```

Pregunta clave:

```txt
¿El NPC necesita una accion ofensiva para cumplir su rol?
```

Si la respuesta es si, ataque puede ser necesario.

---

## Cuando NO conviene implementarlo

No conviene implementar ataque si el NPC no necesita ofensiva.

Ejemplos:

```txt
comerciante
civil pasivo
NPC narrativo
guia
objeto interactivo
enemigo que solo bloquea camino sin dañar
```

Tampoco conviene crear un sistema de ataque complejo si alcanza con una interaccion simple.

Regla:

```txt
No todo conflicto necesita un sistema de combate completo.
```

---

## Mala practica al implementarlo

Malas practicas comunes:

```txt
atacar sin rango
atacar sin cooldown
aplicar daño varias veces por frame
mezclar ataque con persecucion
mezclar ataque con deteccion
no dar feedback
no dar anticipacion
hacer daño antes de la animacion
spawnear proyectiles sin pooling
no separar ataque de vida
```

Ejemplo de mala practica:

```txt
AttackBehaviour detecta jugador, se mueve, cambia estado y aplica daño.
```

Problema:

```txt
El ataque deja de ser accion ofensiva.
Pasa a contener media IA del NPC.
```

---

## Costos de implementacion

Ataque puede requerir:

```txt
sistema de daño
rango
cooldown
animacion
feedback visual
feedback sonoro
deteccion de impacto
hitboxes
proyectiles
sincronizacion con movimiento
balance de valores
validacion de timing
```

El costo crece con:

```txt
muchos tipos de ataque
combos
fases
proyectiles
areas
cancelaciones
ventanas de invulnerabilidad
multiplayer
```

---

## Costos de optimizacion

Riesgos comunes:

```txt
chequear rango contra muchos objetivos cada frame
spawnear proyectiles sin pooling
usar OverlapSphere sin filtros
crear hitboxes constantemente
activar efectos sin control
mantener colliders temporales activos de mas
```

Alternativas:

```txt
cooldowns claros
eventos de animacion
pooling de proyectiles
layers y masks
activar hitboxes solo durante ventana de ataque
cachear objetivos
limitar chequeos por intervalo
```

---

## Criterio de optimizacion

Antes de optimizar ataque, revisar:

```txt
cantidad de NPCs atacando
tipo de ataque
cantidad de proyectiles
cantidad de chequeos de rango
frecuencia de hitboxes
cantidad de efectos visuales
si hay pooling
si hay eventos de animacion
```

Criterio:

```txt
ataque melee simple con cooldown
→ costo bajo.

muchos proyectiles instanciados constantemente
→ riesgo alto.

proyectiles con pooling y cooldowns claros
→ mas controlable.
```

---

## Validacion

Ataque se valida revisando:

```txt
si solo ocurre cuando corresponde
si respeta rango
si respeta cooldown
si aplica daño correcto
si tiene feedback claro
si el jugador puede entenderlo
si no golpea a traves de paredes salvo que sea intencional
si no se ejecuta multiples veces por error
```

Debug util:

```txt
gizmo de rango
logs de ataque
visualizacion de hitbox
cooldown visible en inspector
eventos de animacion marcados
```

---

## Preguntas antes de implementarlo

Antes de implementar ataque, preguntar:

```txt
¿El NPC necesita hacer daño o aplicar efecto ofensivo?
¿Cual es el objetivo valido?
¿Cual es el rango?
¿Tiene cooldown?
¿Hay anticipacion?
¿Hay feedback visual o sonoro?
¿Como se aplica el daño?
¿Puede golpear varias veces por error?
¿Esta separado de deteccion y persecucion?
¿Se puede validar con gizmos, logs o hitboxes?
```

---

## Errores comunes

Errores comunes:

```txt
atacar sin rango
atacar sin cooldown
aplicar daño varias veces por frame
mezclar ataque con persecucion
mezclar ataque con deteccion
no dar feedback
no dar anticipacion
hacer daño antes de la animacion
spawnear proyectiles sin pooling
no separar ataque de vida
```

---

## Criterio para una IA

Cuando una IA trabaje con ataque debe:

```txt
mantenerlo como comportamiento ofensivo
no duplicar deteccion
no duplicar persecucion
no absorber vida ni muerte completa
definir rango, cooldown y objetivo
explicar feedback necesario
indicar cuando conviene y cuando no
considerar costos de proyectiles, hitboxes o chequeos frecuentes
proponer validacion clara
respetar navegacion waterfall
```

Regla operativa:

```txt
Ataque debe ser entendible para el jugador y limitado para el sistema.
```

---

## Checklist

Antes de implementar ataque, revisar:

```txt
¿El NPC necesita hacer daño o aplicar efecto ofensivo?
¿Cual es el objetivo valido?
¿Cual es el rango?
¿Tiene cooldown?
¿Hay anticipacion?
¿Hay feedback visual o sonoro?
¿Como se aplica el daño?
¿Puede golpear varias veces por error?
¿Esta separado de deteccion y persecucion?
¿Se puede validar con gizmos, logs o hitboxes?
```

---

## Regla final

```txt
Atacar no es decidir toda la IA.

Atacar es ejecutar una accion ofensiva bajo condiciones claras.
```
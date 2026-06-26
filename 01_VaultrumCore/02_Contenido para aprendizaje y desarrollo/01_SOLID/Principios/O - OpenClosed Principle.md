## Definicion

El principio Open/Closed establece que un sistema debe estar abierto a extension, pero cerrado a modificacion.

Tambien puede entenderse como:

```txt
Poder agregar nuevos comportamientos sin tener que romper o reescribir lo que ya funciona.
```

Esto no significa que nunca se pueda modificar codigo existente.

Significa que, cuando un sistema crece con variantes previsibles, conviene diseñarlo para extenderse sin tocar constantemente su nucleo.

---

## Idea central

Cuando cada nueva variante obliga a modificar muchas partes del sistema, el codigo se vuelve fragil.

```txt
Nueva variante
→ muchos cambios internos
→ mas riesgo
→ mas bugs
→ menor mantenibilidad
```

El objetivo de este principio es permitir crecimiento controlado.

---

## Que problema resuelve

Este principio ayuda a evitar sistemas donde cada nueva feature rompe la estructura existente.

Problemas comunes:

- agregar un nuevo enemigo obliga a modificar varias clases,
- agregar una nueva torre obliga a tocar logica central,
- agregar un nuevo tipo de proyectil rompe el flujo actual,
- agregar una nueva accion llena el codigo de `if` y `switch`,
- cada variante nueva requiere modificar codigo que ya estaba funcionando,
- el sistema no permite crecer sin riesgo.

---

## Como aplicarlo con criterio

Antes de aplicar este principio, hay que entender si realmente existen variantes o crecimiento esperado.

Preguntas utiles:

```txt
¿Este sistema va a tener variantes?
¿Cada variante nueva obliga a modificar codigo existente?
¿Hay reglas comunes y comportamientos variables?
¿Se puede extender sin tocar el nucleo?
¿Crear una abstraccion ahora reduce riesgo o agrega complejidad?
¿El problema ya esta apareciendo o es solo una posibilidad futura?
```

No se diseña para infinitas posibilidades.

Se diseña para los cambios razonables del proyecto.

---

## Ejemplo general en videojuegos

Ejemplo problematico:

```txt
EnemySpawner
→ si enemyType == "Goblin", crear goblin
→ si enemyType == "Orc", crear orc
→ si enemyType == "Dragon", crear dragon
→ si enemyType == "Slime", crear slime
```

Cada nuevo enemigo obliga a modificar el mismo bloque.

Una version mas extensible podria separar la creacion o configuracion de enemigos para que el sistema no tenga que conocer cada caso manualmente.

```txt
EnemySpawner
→ recibe una definicion de enemigo
→ pide crear enemigo
→ no necesita saber todos los tipos concretos
```

La solucion exacta depende del proyecto.

El principio no impone un patron.

Impone criterio de extension.

---

## Ejemplo aplicado a Unity

En Unity, este principio suele aparecer cuando hay objetos configurables o variantes de gameplay.

Ejemplo problematico:

```txt
Tower
→ si towerType == Fire
→ si towerType == Ice
→ si towerType == Poison
→ si towerType == Electric
```

Cada nueva torre obliga a modificar la clase `Tower`.

Una alternativa mas sana podria ser:

```txt
Tower
→ comportamiento base

TowerData
→ datos configurables

AttackBehaviour
→ comportamiento variable

ProjectileData
→ configuracion del proyectil
```

Asi se pueden agregar variantes desde datos, componentes o sistemas existentes sin reescribir constantemente la clase principal.

---

## Como debe usarlo una IA

Cuando una IA proponga una solucion tecnica, debe revisar si el cambio esta cerrando o abriendo correctamente el sistema.

Debe preguntarse:

```txt
¿Estoy modificando codigo estable para agregar una variante?
¿Este cambio podria repetirse muchas veces?
¿Existe ya una forma de extension en el proyecto?
¿Conviene usar la estructura existente?
¿Estoy agregando una abstraccion justificada?
¿Estoy preparando extension real o imaginaria?
```

La IA no debe crear sistemas extensibles por anticipacion vacia.

Primero debe explicar:

```txt
Variacion detectada
Codigo que hoy deberia modificarse
Riesgo de seguir asi
Forma de extension propuesta
Motivo
Impacto
Validacion necesaria
```

---

## Senales de que se esta rompiendo OCP

Un sistema probablemente rompe este principio si:

- cada variante nueva requiere modificar la misma clase,
- hay muchos `if` o `switch` para tipos de comportamiento,
- el codigo central conoce demasiados casos concretos,
- agregar contenido nuevo rompe contenido existente,
- no hay una forma clara de extender,
- se duplican flujos parecidos,
- una feature nueva obliga a tocar archivos que no deberian cambiar.

---

## Cuando NO aplicarlo de forma agresiva

No conviene aplicar este principio de forma agresiva si:

- solo existe una variante,
- no hay crecimiento previsto,
- el sistema todavia esta explorandose,
- una solucion simple alcanza,
- crear abstracciones haria el codigo menos claro,
- todavia no se entiende bien el comportamiento real.

Open/Closed no significa diseñar para todos los futuros posibles.

Significa evitar que cambios esperables rompan el sistema.

---

## Error comun

Un error comun es pensar:

```txt
Como podria haber mas variantes en el futuro, tengo que abstraer todo ahora.
```

Eso puede generar sobrearquitectura.

Ejemplo:

```txt
Una sola torre
→ interfaz de torre
→ factory
→ strategy
→ manager
→ registry
→ configuracion avanzada
```

Si el proyecto todavia no necesita eso, es exceso.

El criterio correcto es:

```txt
Si el cambio es probable y repetible, preparar extension.
Si el cambio es incierto, mantener simple.
```

---

## Relacion con Vaultrum

Dentro de Vaultrum, este principio debe usarse para decidir cuando conviene preparar un sistema para crecer.

Especialmente cuando se trabaja con:

- variantes de enemigos,
- torres,
- proyectiles,
- habilidades,
- items,
- estados,
- objetivos,
- acciones de jugador,
- comportamientos de IA,
- sistemas configurables desde Unity.

No se usa para imaginar todos los futuros.

Se usa para evitar que cambios reales rompan codigo estable.

---

## Resultado esperado

Aplicar bien este principio deberia permitir:

- agregar variantes con menos riesgo,
- reducir modificaciones en codigo estable,
- evitar duplicacion,
- mantener sistemas extensibles,
- mejorar configuracion desde Unity,
- facilitar iteracion,
- proteger comportamiento existente,
- reducir bugs por cambios repetidos.

---

## Regla final

```txt
Un sistema no debe romperse cada vez que crece.
Debe permitir extender lo que cambia sin destruir lo que ya funciona.
```
## Definicion

El principio de sustitucion de Liskov establece que una clase derivada debe poder reemplazar a su clase base sin romper el comportamiento esperado del sistema.

Tambien puede entenderse como:

```txt
Si una clase hereda de otra, debe poder usarse como esa clase sin generar comportamientos incorrectos.
```

La herencia no debe usarse solo porque dos cosas se parecen.

Debe representar una relacion real de comportamiento.

---

## Idea central

Una herencia mal diseñada genera sistemas fragiles.

```txt
Herencia forzada
→ excepciones raras
→ metodos vacios
→ comportamiento inesperado
→ bugs dificiles de detectar
```

El objetivo de este principio es asegurar que las jerarquias tengan sentido.

---

## Que problema resuelve

Este principio ayuda a evitar herencias incorrectas.

Problemas comunes:

- una subclase hereda metodos que no puede cumplir,
- una clase hija deja metodos vacios,
- una clase hija lanza errores porque no soporta algo de la base,
- el sistema espera un comportamiento general y recibe una excepcion rara,
- se usa herencia para compartir codigo aunque conceptualmente no corresponda,
- una jerarquia obliga a forzar comportamientos.

---

## Como aplicarlo con criterio

Antes de usar herencia, hay que validar si la relacion es real.

Preguntas utiles:

```txt
¿La clase hija realmente es una version de la clase base?
¿Puede reemplazarla sin romper expectativas?
¿Todos los metodos heredados tienen sentido?
¿Hay comportamientos que la hija no puede cumplir?
¿Estoy usando herencia solo para reutilizar codigo?
¿Composicion seria mas clara que herencia?
```

No toda similitud justifica herencia.

A veces dos objetos comparten datos o comportamiento, pero no pertenecen a la misma jerarquia.

---

## Ejemplo general en videojuegos

Ejemplo problematico:

```txt
Enemy
→ Move()
→ Attack()

TurretEnemy hereda de Enemy
→ no se mueve
→ Move() queda vacio o lanza error
```

El problema es que `TurretEnemy` no puede cumplir correctamente el contrato de `Enemy` si el sistema espera que todo enemigo pueda moverse.

Una alternativa podria ser separar responsabilidades:

```txt
Enemy
→ vida, daño recibido, estado general

IMovable
→ movimiento

IAttacker
→ ataque
```

O usar componentes segun el caso.

La solucion exacta depende del proyecto.

El principio ayuda a detectar que la herencia estaba forzada.

---

## Ejemplo aplicado a Unity

En Unity puede aparecer cuando se crea una clase base demasiado grande.

Ejemplo problematico:

```txt
BaseTower
→ Shoot()
→ RotateToTarget()
→ ConsumeAmmo()
→ ApplyAreaDamage()

LaserTower hereda BaseTower
→ no usa ammo
→ no dispara proyectiles
→ no aplica area damage
```

Si muchas torres heredan metodos que no usan, la jerarquia probablemente esta mal diseñada.

Una alternativa mas sana puede ser:

```txt
Tower
→ comportamiento base comun

Componentes o comportamientos separados
→ ataque
→ rotacion
→ consumo de recurso
→ efecto aplicado
```

La torre no deberia heredar obligaciones que no puede cumplir.

---

## Como debe usarlo una IA

Cuando una IA proponga herencia o modifique una jerarquia, debe validar si respeta este principio.

Debe preguntarse:

```txt
¿La clase hija puede reemplazar a la base sin romper nada?
¿La clase base promete comportamientos que no todas las hijas cumplen?
¿Hay metodos vacios, anulados sin sentido o excepciones?
¿Estoy usando herencia para compartir codigo en vez de representar una relacion real?
¿Conviene composicion?
¿El proyecto ya usa una estructura compatible?
```

La IA no debe proponer herencia solo porque parece ordenada.

Primero debe explicar:

```txt
Relacion propuesta
Comportamiento comun
Comportamientos que no encajan
Riesgo de herencia
Alternativa considerada
Motivo de la decision
Validacion necesaria
```

---

## Senales de que se esta rompiendo LSP

Una jerarquia probablemente rompe este principio si:

- una subclase no puede cumplir metodos heredados,
- hay metodos vacios solo para satisfacer la base,
- una subclase lanza errores en comportamientos heredados,
- se necesitan muchos `if` para tratar casos especiales,
- el codigo pregunta constantemente que tipo concreto es,
- la clase base tiene demasiadas responsabilidades,
- una hija cambia el significado esperado de un metodo,
- usar una hija en lugar de la base produce bugs.

---

## Cuando NO aplicarlo de forma agresiva

No conviene rediseñar toda una jerarquia si:

- la herencia es simple y funciona,
- no hay comportamientos incompatibles,
- el sistema es chico,
- no hay variantes conflictivas,
- separar todo agregaria complejidad innecesaria.

LSP no significa evitar toda herencia.

Significa usar herencia solo cuando la sustitucion tiene sentido.

---

## Error comun

Un error comun es pensar:

```txt
Estas dos clases comparten codigo, entonces una debe heredar de la otra.
```

Compartir codigo no siempre justifica herencia.

Ejemplo:

```txt
Enemy
FlyingEnemy
Door
```

Tal vez todos tengan vida y reciban daño, pero eso no significa que una puerta sea un enemigo.

Puede ser mejor compartir una responsabilidad mediante un componente o contrato especifico.

El criterio correcto es:

```txt
Herencia para relaciones reales.
Composicion para responsabilidades combinables.
```

---

## Relacion con Vaultrum

Dentro de Vaultrum, este principio debe usarse para revisar jerarquias y evitar herencias forzadas.

Especialmente cuando se trabaja con:

- enemigos,
- torres,
- proyectiles,
- items,
- habilidades,
- NPCs,
- entidades dañables,
- estados,
- objetos interactuables,
- sistemas de gameplay.

No se usa para eliminar herencia.

Se usa para asegurar que la herencia represente comportamiento real.

---

## Resultado esperado

Aplicar bien este principio deberia permitir:

- jerarquias mas sanas,
- menos excepciones raras,
- menos metodos vacios,
- menos casos especiales,
- codigo mas predecible,
- mejor reutilizacion,
- menos bugs por sustitucion,
- mejor separacion entre herencia y composicion.

---

## Regla final

```txt
Una clase hija no debe fingir que es algo que no puede ser.
```
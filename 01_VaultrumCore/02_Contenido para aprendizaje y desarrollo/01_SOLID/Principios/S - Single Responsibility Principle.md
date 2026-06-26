## Definicion

El principio de responsabilidad unica establece que una clase, componente o sistema debe tener una responsabilidad principal clara.

Tambien puede entenderse como:

```txt
Una clase debe tener una sola razon principal para cambiar.
```

Esto no significa que una clase solo pueda tener un metodo.

Significa que todo lo que hace debe pertenecer al mismo motivo de cambio.

---

## Idea central

Una clase con demasiadas responsabilidades se vuelve dificil de entender, modificar, probar y reutilizar.

```txt
Responsabilidades mezcladas
→ cambios mas riesgosos
→ mas acoplamiento
→ mas bugs
→ menor mantenibilidad
```

El objetivo de este principio es que cada parte del sistema tenga un motivo claro para existir.

---

## Que problema resuelve

Este principio ayuda a evitar que una clase concentre demasiadas decisiones.

Problemas comunes:

- una clase controla logica de gameplay y UI,
- un manager absorbe responsabilidades de muchos sistemas,
- un componente maneja datos, validaciones, efectos y eventos,
- una clase cambia por muchos motivos distintos,
- un cambio pequeño obliga a tocar codigo no relacionado,
- el sistema se vuelve dificil de extender sin romper algo.

---

## Como aplicarlo con criterio

Antes de separar una clase, primero hay que entender que responsabilidades tiene.

Preguntas utiles:

```txt
¿Que hace esta clase?
¿Por que motivos podria cambiar?
¿Tiene una responsabilidad principal clara?
¿Esta mezclando logica, UI, datos, audio, efectos o coordinacion?
¿Hay una parte que podria vivir en otro componente o sistema?
¿Separarla mejora claridad o solo agrega archivos innecesarios?
```

No se separa por separar.

Se separa cuando la mezcla de responsabilidades genera confusion, fragilidad o dificultad para cambiar.

---

## Ejemplo general en videojuegos

Ejemplo de clase con responsabilidades mezcladas:

```txt
Player
→ lee input
→ mueve al personaje
→ calcula vida
→ actualiza UI
→ reproduce sonidos
→ guarda progreso
→ maneja inventario
```

El problema no es que `Player` tenga varias funciones.

El problema es que cambia por demasiados motivos distintos.

Una version mas ordenada podria separar responsabilidades:

```txt
PlayerMovement
→ movimiento

PlayerHealth
→ vida y daño

PlayerInventory
→ inventario

PlayerUI
→ visualizacion

PlayerAudio
→ sonidos

SaveSystem
→ guardado
```

La division exacta depende del proyecto.

El principio no impone nombres.

Impone criterio.

---

## Ejemplo aplicado a Unity

En Unity es comun que un `MonoBehaviour` empiece simple y crezca demasiado.

Ejemplo problematico:

```txt
Tower
→ detecta enemigos
→ dispara
→ calcula upgrades
→ compra mejoras
→ actualiza UI
→ reproduce feedback visual
→ maneja venta
→ comunica eventos
```

Una separacion mas sana podria ser:

```txt
Tower
→ comportamiento base de la torre

TowerTargeting
→ busqueda de objetivo

TowerAttack
→ disparo o ataque

TowerUpgradeComponent
→ mejoras

TowerData
→ datos configurables

UpgradePanel
→ visualizacion de UI

TowerSelectionHandler
→ seleccion
```

Esto permite modificar upgrades sin tocar seleccion, UI o ataque.

Tambien permite modificar valores desde Unity sin tener logica hardcodeada mezclada en una clase gigante.

---

## Como debe usarlo una IA

Cuando una IA trabaje sobre codigo, debe usar este principio para detectar responsabilidades mezcladas antes de proponer cambios.

Debe preguntarse:

```txt
¿La clase actual esta haciendo demasiado?
¿La nueva feature pertenece realmente a esta clase?
¿Estoy agregando otra responsabilidad a una clase que ya esta cargada?
¿Existe ya un sistema encargado de esto?
¿Conviene reutilizar una responsabilidad existente?
¿Separar esto reduce riesgo o solo agrega complejidad?
```

La IA no debe crear clases nuevas automaticamente.

Primero debe explicar:

```txt
Responsabilidad detectada
Problema actual
Riesgo de mantenerlo asi
Separacion propuesta
Motivo
Impacto
Validacion necesaria
```

---

## Senales de que se esta rompiendo SRP

Una clase probablemente rompe este principio si:

- tiene muchos motivos distintos para cambiar,
- mezcla UI con reglas de negocio o gameplay,
- mezcla datos configurables con logica,
- mezcla audio, efectos y validaciones,
- tiene demasiadas referencias a sistemas distintos,
- sus metodos no parecen pertenecer al mismo objetivo,
- cada nueva feature termina agregandose ahi,
- nadie sabe claramente que responsabilidad tiene.

---

## Cuando NO aplicarlo de forma agresiva

No conviene separar una clase si:

- el sistema es muy pequeño,
- la responsabilidad sigue siendo clara,
- separar generaria mas confusion,
- no hay cambios previstos,
- no hay reutilizacion real,
- no hay riesgo actual,
- se estaria creando arquitectura por anticipado.

SRP no significa convertir cada accion en una clase.

Significa evitar que una clase concentre responsabilidades que deberian poder cambiar de forma independiente.

---

## Error comun

Un error comun es pensar:

```txt
Esta clase tiene varios metodos, entonces rompe SRP.
```

Eso no siempre es cierto.

Una clase puede tener varios metodos y seguir teniendo una sola responsabilidad.

El problema aparece cuando esos metodos responden a motivos de cambio distintos.

Ejemplo:

```txt
Move()
Jump()
ApplyGravity()
CheckGround()
```

Estos metodos pueden pertenecer a una misma responsabilidad: movimiento.

Pero:

```txt
Move()
UpdateHealthBar()
SaveGame()
BuyUpgrade()
PlayExplosionSound()
```

Ahi aparecen responsabilidades distintas.

---

## Relacion con Vaultrum

Dentro de Vaultrum, este principio debe usarse como criterio para mantener sistemas entendibles y modificables.

Especialmente cuando se revisan:

- componentes de Unity,
- managers,
- sistemas de gameplay,
- UI,
- herramientas,
- codigo generado por IA,
- refactors,
- integraciones entre sistemas.

No se usa para dividir todo.

Se usa para decidir si una responsabilidad esta en el lugar correcto.

---

## Resultado esperado

Aplicar bien este principio deberia permitir:

- entender mejor cada clase,
- reducir bugs por cambios laterales,
- modificar sistemas con menos riesgo,
- reutilizar componentes,
- evitar managers gigantes,
- separar UI de logica,
- facilitar pruebas,
- mejorar mantenimiento,
- preparar mejor el proyecto para crecer.

---

## Regla final

```txt
Una clase no debe hacer todo lo que puede hacer.
Debe hacer lo que le corresponde.
```
## Definicion

El principio de segregacion de interfaces establece que una clase no deberia estar obligada a implementar metodos que no necesita.

Tambien puede entenderse como:

```txt
Es mejor tener interfaces especificas que interfaces gigantes y genericas.
```

Una interfaz debe representar una capacidad o contrato claro.

No debe ser una bolsa de metodos.

---

## Idea central

Cuando una interfaz obliga a implementar cosas innecesarias, el sistema se vuelve confuso y fragil.

```txt
Interfaz demasiado grande
→ metodos vacios
→ implementaciones falsas
→ contratos poco claros
→ mayor acoplamiento
```

El objetivo de este principio es que cada clase dependa solo de las capacidades que realmente usa.

---

## Que problema resuelve

Este principio ayuda a evitar contratos demasiado amplios.

Problemas comunes:

- una clase implementa metodos vacios,
- una interfaz mezcla responsabilidades distintas,
- un objeto debe fingir capacidades que no tiene,
- cambiar una interfaz afecta clases que no usan ese cambio,
- el codigo depende de mas informacion de la necesaria,
- los contratos dejan de ser claros.

---

## Como aplicarlo con criterio

Antes de crear o modificar una interfaz, hay que entender que capacidad representa.

Preguntas utiles:

```txt
¿Que capacidad expresa esta interfaz?
¿Todos los metodos pertenecen a la misma responsabilidad?
¿Todas las clases que la implementan usan todos sus metodos?
¿Hay metodos vacios o forzados?
¿Conviene dividir esta interfaz?
¿La division mejora claridad o solo agrega archivos innecesarios?
```

No se crean interfaces por costumbre.

Se crean cuando hay un contrato real que ayuda al sistema.

---

## Ejemplo general en videojuegos

Ejemplo problematico:

```txt
ICharacter
→ Move()
→ Attack()
→ Talk()
→ Trade()
→ TakeDamage()
```

Un enemigo puede moverse, atacar y recibir daño, pero no comerciar.

Un mercader puede hablar y comerciar, pero no atacar.

Un objeto destruible puede recibir daño, pero no moverse ni hablar.

Una version mas clara podria separar capacidades:

```txt
IMovable
→ Move()

IAttacker
→ Attack()

ITalkable
→ Talk()

ITradeable
→ Trade()

IDamageable
→ TakeDamage()
```

Cada objeto implementa solo lo que necesita.

---

## Ejemplo aplicado a Unity

En Unity, este principio es util cuando varios objetos comparten interacciones parciales.

Ejemplo problematico:

```txt
IInteractable
→ Interact()
→ Highlight()
→ PickUp()
→ Open()
→ Talk()
```

No todo interactuable se puede recoger, abrir o hablar.

Una division mas sana podria ser:

```txt
IInteractable
→ Interact()

IHighlightable
→ Highlight()

IPickable
→ PickUp()

IOpenable
→ Open()

ITalkable
→ Talk()
```

Asi la UI, el sistema de interaccion o el gameplay pueden consultar capacidades concretas sin forzar implementaciones falsas.

---

## Como debe usarlo una IA

Cuando una IA proponga interfaces, debe revisar si el contrato es claro y especifico.

Debe preguntarse:

```txt
¿Esta interfaz representa una capacidad real?
¿Estoy mezclando responsabilidades?
¿Todas las clases necesitan todos los metodos?
¿Estoy creando una interfaz gigante?
¿Estoy creando interfaces innecesarias?
¿El proyecto ya tiene un contrato similar?
¿Separar esta interfaz mejora el codigo?
```

La IA no debe crear interfaces solo para que el codigo parezca mas profesional.

Primero debe explicar:

```txt
Capacidad detectada
Clases que la necesitan
Metodos necesarios
Metodos que sobran
Separacion propuesta
Motivo
Validacion necesaria
```

---

## Senales de que se esta rompiendo ISP

Una interfaz probablemente rompe este principio si:

- muchas clases dejan metodos vacios,
- hay metodos con nombres genericos y responsabilidades distintas,
- una modificacion afecta implementaciones no relacionadas,
- los objetos implementan capacidades que no tienen,
- una interfaz parece describir un objeto completo en vez de una capacidad,
- se necesitan comentarios para explicar que metodos ignorar,
- aparecen excepciones como "no soportado".

---

## Cuando NO aplicarlo de forma agresiva

No conviene dividir interfaces si:

- la interfaz es pequeña y clara,
- todos los implementadores usan todos los metodos,
- no hay implementaciones falsas,
- dividirla agregaria complejidad,
- el sistema todavia es muy simple,
- no hay beneficio real.

ISP no significa crear una interfaz por metodo.

Significa evitar contratos que obligan a mentir.

---

## Error comun

Un error comun es pensar:

```txt
Para aplicar SOLID, todo necesita interfaz.
```

Eso es falso.

Una interfaz tiene sentido cuando representa un contrato util.

Ejemplo de exceso:

```txt
IMove
IJump
IRun
IWalk
ILook
ITurn
```

Si esas capacidades siempre viven juntas dentro del mismo sistema y no hay necesidad de separarlas, dividirlas puede empeorar la claridad.

El criterio correcto es:

```txt
Interfaces especificas cuando hay capacidades realmente separadas.
Clases simples cuando no hace falta abstraer.
```

---

## Relacion con Vaultrum

Dentro de Vaultrum, este principio debe usarse para revisar contratos entre sistemas.

Especialmente cuando se trabaja con:

- objetos interactuables,
- entidades dañables,
- sistemas de input,
- UI,
- inventario,
- NPCs,
- habilidades,
- objetos del mundo,
- servicios o managers,
- codigo generado por IA.

No se usa para llenar el proyecto de interfaces.

Se usa para evitar contratos falsos o demasiado grandes.

---

## Resultado esperado

Aplicar bien este principio deberia permitir:

- contratos mas claros,
- menos metodos vacios,
- menos implementaciones falsas,
- menor acoplamiento,
- sistemas mas faciles de extender,
- clases mas honestas,
- mejor comunicacion entre componentes,
- menor riesgo al modificar interfaces.

---

## Regla final

```txt
Una clase no debe prometer capacidades que no tiene.
```
## Definicion

Factory es un patron de diseno que centraliza la creacion de objetos.

En lugar de crear objetos directamente en cualquier parte del codigo, se delega esa responsabilidad a una fabrica.

```txt
Solicitud de creacion
→ Factory
→ objeto creado
```

La fabrica decide como construir el objeto segun datos, reglas o contexto.

---

## Idea central

Factory separa la creacion de objetos del sistema que los usa.

```txt
Sistema que necesita un objeto
→ pide creacion
→ Factory resuelve detalles
```

El objetivo es evitar que la logica de creacion quede dispersa.

---

## Que problema resuelve

Factory ayuda cuando crear un objeto requiere mas que una instancia directa.

Problemas comunes:

- la creacion se repite en muchos lugares,
- hay muchos prefabs o variantes,
- la creacion depende de datos,
- se inicializan objetos con reglas especificas,
- el codigo cliente conoce demasiados detalles de construccion,
- agregar variantes obliga a tocar muchas clases.

---

## Cuando conviene usarlo

Conviene considerar Factory cuando:

- hay variantes de objetos,
- la creacion tiene reglas,
- se usan prefabs configurables,
- se necesita centralizar inicializacion,
- varios sistemas crean el mismo tipo de objeto,
- se quiere evitar duplicar logica de creacion.

Ejemplos posibles:

```txt
enemigos
proyectiles
torres
items
habilidades
efectos visuales
misiones
objetos interactuables
```

---

## Cuando NO conviene usarlo

No conviene usar Factory si:

- solo se crea un objeto simple,
- no hay variantes,
- no hay reglas de creacion,
- la instancia directa es clara,
- la fabrica solo envuelve una llamada sin aportar valor,
- agrega una capa innecesaria.

No todo `Instantiate` necesita una Factory.

---

## Como decidir si aplica

Antes de proponer Factory, la IA debe responder:

```txt
¿Que objetos se estan creando?
¿La creacion esta repetida?
¿Hay variantes?
¿La creacion depende de datos o reglas?
¿El cliente conoce demasiados detalles?
¿Existe una fabrica ya usada en el proyecto?
¿Una creacion directa alcanza?
```

Si no hay variacion ni repeticion, probablemente no hace falta.

---

## Estructura conceptual

Una estructura simple puede ser:

```txt
Cliente
→ solicita objeto

Factory
→ recibe tipo, datos o configuracion
→ crea e inicializa objeto

Objeto creado
→ se entrega listo para usar
```

La Factory debe encargarse de la creacion.

No debe absorber todo el comportamiento del objeto.

---

## Ejemplo conceptual breve

Sin Factory:

```txt
Spawner
→ elige prefab
→ instancia
→ configura vida
→ configura velocidad
→ asigna ruta
→ registra enemigo
```

Problema:

```txt
La creacion esta mezclada con el spawner.
Si otro sistema crea enemigos, puede duplicar la logica.
```

Con Factory:

```txt
Spawner
→ pide enemigo a EnemyFactory

EnemyFactory
→ crea, configura y devuelve enemigo
```

El spawner no necesita conocer todos los detalles de construccion.

---

## Como debe usarlo una IA

Una IA debe considerar Factory cuando detecta creacion repetida, variantes o reglas de inicializacion.

Debe razonar asi:

```txt
Hay creacion de objetos
→ reviso si es simple o compleja
→ reviso variantes
→ reviso si ya existe una Factory
→ decido si centralizar aporta valor
```

Antes de implementar, debe presentar:

```txt
Objeto a crear
Creacion actual
Problema detectado
Factory existente o propuesta
Datos necesarios
Alternativa simple
Riesgos
Validacion esperada
```

---

## Como NO debe usarlo una IA

Una IA no debe crear una Factory solo porque se esta creando un objeto.

No debe:

- envolver cada `new` o `Instantiate`,
- crear fabricas para objetos sin variantes,
- ocultar creacion simple sin beneficio,
- duplicar una fabrica existente,
- mezclar creacion con logica de gameplay,
- crear una Factory gigante para todo el juego,
- agregar una capa que dificulte configurar desde Unity.

Ejemplo de mal uso:

```txt
Problema:
Crear una unica moneda en escena.

Mala decision:
Crear CoinFactory.

Motivo:
No hay variantes, reglas ni repeticion que lo justifiquen.
```

---

## Reutilizacion antes que invencion

Si el proyecto ya tiene una Factory para ese tipo de objeto, la IA debe analizar si puede extenderla.

```txt
Nueva variante
→ revisar Factory existente
→ extender configuracion si corresponde
→ evitar flujo paralelo
```

---

## Senales de que Factory puede servir

Puede valer la pena analizar Factory si:

- hay creacion duplicada,
- hay muchos prefabs similares,
- agregar variantes requiere tocar muchas clases,
- la inicializacion tiene varios pasos,
- un sistema externo conoce demasiado de la construccion,
- hay datos configurables que definen objetos.

---

## Senales de Factory mal aplicada

Factory probablemente esta mal aplicada si:

- solo reenvia `Instantiate`,
- no reduce duplicacion,
- conoce demasiados sistemas externos,
- crea objetos no relacionados,
- se convierte en fabrica universal,
- hace mas dificil seguir el flujo,
- no permite configurar datos de forma clara.

---

## Preguntas antes de implementar

```txt
¿Que objeto se quiere crear?
¿Donde se crea hoy?
¿Hay creacion repetida?
¿Hay variantes?
¿Que datos necesita?
¿Que reglas de inicializacion existen?
¿Hay una Factory existente?
¿Como se valida que la creacion sigue funcionando?
```

---

## Formato de propuesta esperado

```txt
Patron:
Factory

Objeto o familia de objetos:
...

Problema actual:
...

Por que aplica:
...

Sistema existente relacionado:
...

Alternativa simple:
...

Riesgos:
...

Validacion:
...
```

---

## Resultado esperado

Aplicar bien Factory deberia permitir:

- centralizar creacion,
- reducir duplicacion,
- manejar variantes con mas claridad,
- separar uso de construccion,
- mejorar configuracion,
- facilitar extension,
- mantener inicializacion consistente.

---

## Regla final

```txt
Factory no existe para crear objetos por crear.
Existe para centralizar creaciones que tienen variantes, reglas o repeticion real.
```
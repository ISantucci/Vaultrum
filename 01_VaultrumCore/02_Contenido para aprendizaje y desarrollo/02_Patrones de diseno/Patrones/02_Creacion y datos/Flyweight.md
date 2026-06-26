## Definicion

Flyweight es un patron que permite compartir datos comunes entre muchas instancias para evitar duplicacion innecesaria.

```txt
Datos compartidos
→ se guardan una vez

Instancias
→ referencian esos datos
```

---

## Idea central

Cuando muchos objetos repiten la misma informacion, conviene separar lo compartido de lo individual.

```txt
Datos repetidos
→ memoria desperdiciada
→ mantenimiento mas dificil
```

Flyweight busca reducir duplicacion.

---

## Que problema resuelve

Flyweight ayuda cuando muchas instancias tienen datos iguales o muy similares.

Problemas comunes:

- muchas copias de la misma informacion,
- uso innecesario de memoria,
- cambios duplicados,
- instancias pesadas,
- datos compartidos mezclados con estado individual.

---

## Cuando conviene usarlo

Conviene considerar Flyweight cuando:

- hay muchas instancias,
- comparten gran parte de sus datos,
- los datos compartidos son estables,
- se quiere reducir memoria,
- se repite configuracion,
- muchas entidades usan una misma definicion base.

Ejemplos posibles:

```txt
balas
enemigos repetidos
items del mismo tipo
tiles
particulas logicas
recursos
decoraciones
datos visuales compartidos
```

---

## Cuando NO conviene usarlo

No conviene usar Flyweight si:

- hay pocas instancias,
- los datos no se repiten,
- cada objeto tiene informacion muy distinta,
- compartir datos complica el sistema,
- no hay problema real de memoria o duplicacion,
- Type Object ya resuelve el caso de forma suficiente.

---

## Como decidir si aplica

Antes de proponer Flyweight, la IA debe responder:

```txt
¿Hay muchas instancias?
¿Que datos se repiten?
¿Que datos son individuales?
¿La duplicacion genera costo real?
¿Compartir datos mejora memoria o mantenimiento?
¿Ya existe una estructura de datos compartidos?
¿La solucion simple alcanza?
```

---

## Estructura conceptual

```txt
Flyweight
→ datos compartidos

Instancia
→ estado individual
→ referencia al Flyweight
```

La clave es separar lo compartido de lo propio.

---

## Ejemplo conceptual breve

Sin Flyweight:

```txt
1000 enemigos
→ cada uno guarda nombre, icono, descripcion, stats base, prefab, sonidos
```

Problema:

```txt
Muchos datos se repiten sin necesidad.
```

Con Flyweight:

```txt
EnemySharedData
→ nombre, icono, stats base, sonidos

EnemyInstance
→ vida actual, posicion, estado actual
→ referencia a EnemySharedData
```

---

## Como debe usarlo una IA

Una IA debe considerar Flyweight cuando detecta duplicacion masiva de datos compartidos.

Debe razonar asi:

```txt
Hay muchas instancias
→ reviso datos repetidos
→ separo compartido de individual
→ verifico si el ahorro justifica el cambio
```

Antes de implementar, debe presentar:

```txt
Instancias afectadas
Datos repetidos
Datos individuales
Costo actual
Beneficio esperado
Alternativa simple
Riesgos
Validacion esperada
```

---

## Como NO debe usarlo una IA

Una IA no debe usar Flyweight solo porque hay datos compartidos.

No debe:

- aplicarlo si hay pocas instancias,
- complicar un sistema sin problema real,
- compartir datos que deberian ser individuales,
- romper configuraciones existentes,
- confundirlo con cualquier uso de ScriptableObjects,
- usarlo sin identificar costo de duplicacion.

Ejemplo de mal uso:

```txt
Problema:
Hay tres enemigos distintos.

Mala decision:
Crear sistema Flyweight complejo.

Motivo:
No hay volumen ni costo que lo justifique.
```

---

## Reutilizacion antes que invencion

Si el proyecto ya separa datos compartidos mediante assets, configs o tipos, la IA debe revisar si eso ya resuelve el problema antes de crear una estructura nueva.

---

## Senales de que Flyweight puede servir

Puede valer la pena analizar Flyweight si:

- hay muchas instancias similares,
- se repiten datos pesados,
- la memoria empieza a importar,
- los datos compartidos cambian juntos,
- las instancias solo deberian guardar estado individual.

---

## Senales de Flyweight mal aplicado

Flyweight probablemente esta mal aplicado si:

- no hay muchas instancias,
- se comparte estado que deberia ser individual,
- el sistema se vuelve dificil de entender,
- no hay ahorro real,
- duplica un sistema de datos ya existente,
- se aplica por teoria y no por necesidad.

---

## Preguntas antes de implementar

```txt
¿Cuantas instancias existen?
¿Que datos se repiten?
¿Que datos son individuales?
¿Hay costo real?
¿Que estructura compartida existe?
¿Como se evita compartir estado mutable incorrecto?
¿Como se valida?
```

---

## Formato de propuesta esperado

```txt
Patron:
Flyweight

Datos repetidos:
...

Instancias afectadas:
...

Beneficio esperado:
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

Aplicar bien Flyweight deberia permitir:

- reducir duplicacion,
- ahorrar memoria,
- separar estado individual de datos compartidos,
- mantener datos comunes en un solo lugar,
- mejorar mantenimiento en sistemas con muchas instancias.

---

## Regla final

```txt
Flyweight no existe para abstraer datos.
Existe para compartir datos repetidos cuando la cantidad de instancias lo justifica.
```
## Definicion

Type Object es un patron que separa los datos de un tipo de objeto de sus instancias concretas.

En lugar de hardcodear valores en cada objeto, se define un objeto de tipo que contiene datos compartidos.

```txt
Tipo
→ datos comunes

Instancia
→ estado individual
```

---

## Idea central

Type Object permite que muchas instancias compartan una definicion de tipo.

```txt
SwordType
→ daño, rareza, icono, costo

Sword instance
→ durabilidad, dueño, estado actual
```

El objetivo es separar configuracion de instancia.

---

## Que problema resuelve

Type Object ayuda cuando hay muchas variantes similares que comparten estructura pero cambian datos.

Problemas comunes:

- valores hardcodeados,
- muchas clases para variantes simples,
- datos repetidos en instancias,
- dificil balance desde Unity,
- cambios de diseño obligan a tocar codigo,
- objetos similares tienen configuraciones dispersas.

---

## Cuando conviene usarlo

Conviene considerar Type Object cuando:

- hay variantes configurables,
- los datos deben editarse sin cambiar codigo,
- muchas instancias comparten el mismo tipo,
- se necesita balancear valores,
- se quieren crear objetos desde datos,
- la diferencia entre variantes esta en datos mas que en logica.

Ejemplos posibles:

```txt
torres
enemigos
items
armas
habilidades
proyectiles
misiones
recursos
upgrades
```

---

## Cuando NO conviene usarlo

No conviene usar Type Object si:

- no hay variantes,
- los datos no cambian,
- cada objeto tiene logica completamente distinta,
- crear datos externos complica mas de lo que ayuda,
- la configuracion no necesita editarse,
- el sistema todavia es demasiado incierto.

---

## Como decidir si aplica

Antes de proponer Type Object, la IA debe responder:

```txt
¿Hay variantes del mismo concepto?
¿Comparten estructura?
¿Cambian principalmente datos?
¿Los valores necesitan balance?
¿Deben ser editables desde Unity?
¿Hoy hay hardcodeo o duplicacion?
¿El proyecto ya usa datos configurables?
```

Si la diferencia es de comportamiento profundo, puede hacer falta otro enfoque.

---

## Estructura conceptual

```txt
Type Object
→ datos compartidos del tipo

Instancia
→ referencia al tipo
→ estado propio
```

La instancia usa datos del tipo, pero mantiene su propio estado.

---

## Ejemplo conceptual breve

Sin Type Object:

```txt
FireTower
→ daño = 10
→ rango = 5

IceTower
→ daño = 6
→ rango = 4
```

Problema:

```txt
Cada variante puede terminar como clase nueva.
Los datos quedan pegados al codigo.
Balancear requiere tocar scripts.
```

Con Type Object:

```txt
TowerData
→ daño
→ rango
→ costo
→ icono

Tower
→ referencia a TowerData
```

Ahora se pueden crear variantes cambiando datos.

---

## Como debe usarlo una IA

Una IA debe considerar Type Object cuando detecta datos hardcodeados o variantes configurables.

Debe razonar asi:

```txt
Hay variantes
→ reviso si cambian datos o comportamiento
→ reviso si ya existe estructura de datos
→ propongo Type Object si mejora configuracion
```

Antes de implementar, debe presentar:

```txt
Tipo de objeto
Datos compartidos
Estado individual
Problema actual
Sistema de datos existente
Alternativa simple
Riesgos
Validacion esperada
```

---

## Como NO debe usarlo una IA

Una IA no debe usar Type Object para convertir todo en datos.

No debe:

- crear assets de datos para valores que no cambian,
- separar datos si no hay variantes,
- esconder logica dentro de datos confusos,
- reemplazar comportamiento real con configuracion forzada,
- duplicar un sistema de datos existente,
- crear estructuras enormes antes de saber que se necesita.

Ejemplo de mal uso:

```txt
Problema:
Un objeto unico con un valor fijo.

Mala decision:
Crear un Type Object configurable.

Motivo:
No hay variantes ni necesidad de balanceo.
```

---

## Reutilizacion antes que invencion

Si el proyecto ya usa ScriptableObjects, configs o datos editables para variantes, la IA debe extender ese sistema antes de crear otro.

---

## Senales de que Type Object puede servir

Puede valer la pena analizar Type Object si:

- hay muchos valores hardcodeados,
- hay variantes que solo cambian datos,
- se necesitan balanceos frecuentes,
- varias instancias comparten configuracion,
- crear una clase por variante parece excesivo,
- Unity deberia permitir editar parametros.

---

## Senales de Type Object mal aplicado

Type Object probablemente esta mal aplicado si:

- hay datos externos sin variantes reales,
- la configuracion se vuelve dificil de entender,
- se duplican estructuras de datos,
- los datos empiezan a contener demasiada logica,
- el sistema necesita comportamiento distinto pero solo se cambian valores,
- se agrego complejidad sin mejorar balance ni mantenimiento.

---

## Preguntas antes de implementar

```txt
¿Que concepto tiene variantes?
¿Que datos cambian?
¿Que estado pertenece a cada instancia?
¿Que datos deben compartirse?
¿Como se editaria desde Unity?
¿Existe una estructura similar?
¿Como se valida que las variantes funcionan?
```

---

## Formato de propuesta esperado

```txt
Patron:
Type Object

Concepto con variantes:
...

Datos compartidos:
...

Estado individual:
...

Problema actual:
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

Aplicar bien Type Object deberia permitir:

- reducir hardcodeo,
- facilitar balance,
- crear variantes desde datos,
- compartir configuracion,
- separar tipo de instancia,
- mejorar mantenimiento,
- evitar clases innecesarias.

---

## Regla final

```txt
Type Object no existe para convertir todo en configuracion.
Existe para separar datos compartidos de instancias cuando las variantes lo justifican.
```
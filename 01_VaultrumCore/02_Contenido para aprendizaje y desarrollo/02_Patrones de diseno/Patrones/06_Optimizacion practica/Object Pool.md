## Definicion

Object Pool es un patron que reutiliza objetos en lugar de crearlos y destruirlos constantemente.

```txt
Pool
→ entrega objeto disponible
→ objeto se usa
→ vuelve al pool
```

---

## Idea central

Crear y destruir objetos muchas veces puede generar costo y problemas de rendimiento.

Object Pool evita ese ciclo repetido.

```txt
crear/destruir repetidamente
→ costo
→ posibles picos
→ reutilizar objetos
```

---

## Que problema resuelve

Object Pool ayuda cuando hay objetos temporales que aparecen muchas veces.

Problemas comunes:

- muchos `Instantiate` y `Destroy`,
- picos de rendimiento,
- basura para el garbage collector,
- objetos temporales repetidos,
- efectos o proyectiles creados constantemente,
- necesidad de controlar cantidad activa.

---

## Cuando conviene usarlo

Conviene considerar Object Pool cuando:

- hay muchas creaciones repetidas,
- los objetos tienen vida corta,
- aparecen en gameplay frecuente,
- se nota costo de instanciacion,
- se quiere controlar reutilizacion,
- los objetos pueden resetearse bien.

Ejemplos posibles:

```txt
proyectiles
enemigos repetidos
particulas logicas
efectos visuales
popups de daño
sonidos temporales
objetos de UI repetidos
```

---

## Cuando NO conviene usarlo

No conviene usar Object Pool si:

- el objeto aparece una sola vez,
- hay pocas instancias,
- el costo de creacion no importa,
- el objeto es dificil de resetear,
- la pool agrega mas bugs que beneficio,
- no hay evidencia ni necesidad razonable.

---

## Como decidir si aplica

Antes de proponer Object Pool, la IA debe responder:

```txt
¿El objeto se crea y destruye muchas veces?
¿Es temporal?
¿Puede resetearse correctamente?
¿Hay costo real o probable?
¿Ya existe una pool en el proyecto?
¿La cantidad activa puede controlarse?
¿Instantiate/Destroy simple alcanza?
```

---

## Estructura conceptual

```txt
Pool
→ mantiene objetos disponibles

Get()
→ entrega objeto

Release()
→ devuelve objeto

Objeto reutilizado
→ se resetea antes de volver a usarse
```

El reseteo correcto es clave.

---

## Ejemplo conceptual breve

Sin Object Pool:

```txt
Cada disparo
→ Instantiate proyectil
→ proyectil impacta
→ Destroy proyectil
```

Problema:

```txt
En muchos disparos, esto puede generar costo repetido.
```

Con Object Pool:

```txt
Disparo
→ pedir proyectil al pool
→ activar proyectil
→ al impactar vuelve al pool
```

---

## Como debe usarlo una IA

Una IA debe considerar Object Pool cuando detecta creacion repetida de objetos temporales.

Debe razonar asi:

```txt
Hay objetos temporales repetidos
→ reviso frecuencia
→ reviso si ya existe pool
→ reviso reseteo
→ propongo pool solo si aporta rendimiento o control
```

Antes de implementar, debe presentar:

```txt
Objeto a reutilizar
Frecuencia de uso
Pool existente o propuesta
Datos a resetear
Riesgos
Alternativa simple
Validacion esperada
```

---

## Como NO debe usarlo una IA

Una IA no debe usar Object Pool por defecto.

No debe:

- poolizar objetos que casi no se crean,
- crear pools para todo,
- ignorar el reseteo de estado,
- duplicar una pool existente,
- ocultar bugs por objetos mal reiniciados,
- aplicar pooling sin necesidad de rendimiento,
- hacer mas dificil configurar prefabs.

Ejemplo de mal uso:

```txt
Problema:
Crear un objeto unico al iniciar nivel.

Mala decision:
Crear Object Pool.

Motivo:
No hay repeticion ni costo que lo justifique.
```

---

## Reutilizacion antes que invencion

Si el proyecto ya tiene un sistema de pools, la IA debe intentar extenderlo.

No se crean pools paralelas para el mismo tipo de problema sin justificacion.

---

## Senales de que Object Pool puede servir

Puede valer la pena analizar Object Pool si:

- hay muchos `Instantiate/Destroy`,
- aparecen proyectiles o efectos repetidos,
- hay picos de rendimiento,
- hay objetos temporales de vida corta,
- la misma prefab se usa muchas veces,
- el profiler o el diseño sugieren costo repetido.

---

## Senales de Object Pool mal aplicado

Object Pool probablemente esta mal aplicado si:

- no hay repeticion real,
- los objetos vuelven con estado viejo,
- se crean varias pools para lo mismo,
- la pool crece sin control,
- es mas dificil usarla que instanciar,
- no hay validacion de rendimiento o necesidad razonable.

---

## Preguntas antes de implementar

```txt
¿Que objeto se reutiliza?
¿Cada cuanto aparece?
¿Cuando vuelve al pool?
¿Que estado debe resetearse?
¿Que tamaño inicial necesita?
¿Que pasa si no hay objetos disponibles?
¿Existe pool actual?
¿Como se valida?
```

---

## Formato de propuesta esperado

```txt
Patron:
Object Pool

Objeto:
...

Frecuencia:
...

Problema actual:
...

Pool existente:
...

Datos a resetear:
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

Aplicar bien Object Pool deberia permitir:

- reducir creaciones repetidas,
- bajar costo de instanciacion,
- controlar objetos activos,
- mejorar rendimiento en objetos temporales,
- reducir basura generada,
- mantener flujo mas estable.

---

## Regla final

```txt
Object Pool no existe para optimizar por intuicion.
Existe para reutilizar objetos temporales cuando la repeticion lo justifica.
```
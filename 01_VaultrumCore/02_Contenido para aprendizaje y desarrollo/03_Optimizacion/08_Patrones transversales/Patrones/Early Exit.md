## Definicion

Early Exit consiste en dejar de procesar apenas se conoce el resultado.

Si una condicion ya determina la respuesta, seguir ejecutando es trabajo pagado sin beneficio.

```txt
Se conoce el resultado
→ se corta
→ no se ejecuta lo que viene despues
```

El bloque canonico es este:

```csharp
if (!active)
    return;

if (distance > range)
    return;

if (!insideFOV)
    return;

// operacion cara
```

Cada guarda responde una pregunta barata.

La operacion cara queda al final y solo se alcanza cuando ninguna guarda la descarto antes.

El patron no vive en un recurso ni en un subsistema.

Aparece igual en CPU, en GPU, en fisica, en IA, en rendering y en interfaz.

---

## Que problema ayuda a prevenir

Ayuda con:

```txt
Trabajo ejecutado sobre entidades irrelevantes.
Queries fisicas disparadas sin necesidad.
Calculos completos para descartar al final.
Costo que escala con la cantidad de objetos.
Codigo anidado dificil de leer y de perfilar.
```

Tambien previene un patron de escritura muy comun:

```txt
Calcular todo
→ decidir al final si servia
```

Early Exit invierte ese orden.

```txt
Decidir primero
→ calcular solo si hace falta
```

---

## Como funciona

Las condiciones se ordenan por costo, de la mas barata a la mas cara.

```txt
Comparacion de bool
↓
comparacion numerica
↓
producto escalar o angulo
↓
query fisica
↓
algoritmo completo
```

La regla de orden es simple.

```txt
Lo que descarta mas y cuesta menos
va primero.
```

Ejemplo con estructura anidada:

```csharp
if (active)
{
    if (distance <= range)
    {
        if (insideFOV)
        {
            DoExpensiveWork();
        }
    }
}
```

La misma logica con salida temprana:

```csharp
if (!active) return;
if (distance > range) return;
if (!insideFOV) return;

DoExpensiveWork();
```

El resultado es identico.

Cambia el costo promedio y cambia la legibilidad: la operacion importante queda al mismo nivel de indentacion que el resto.

---

## Como aplicarlo en videojuegos

El patron aterriza en ramas muy distintas.

En IA:

```txt
Percepcion
→ ¿el agente esta activo?
→ ¿el objetivo esta en rango?
→ ¿esta dentro del campo de vision?
→ recien ahi, raycast.
```

En fisica y colisiones:

```txt
Contacto
→ ¿las capas pueden interactuar?
→ ¿los volumenes se tocan?
→ recien ahi, resolucion precisa.
```

En input:

```txt
Accion
→ ¿hay input este frame?
→ ¿el estado permite la accion?
→ ¿el cooldown termino?
→ recien ahi, ejecutar.
```

En interfaz:

```txt
Actualizacion
→ ¿el valor cambio?
→ recien ahi, escribir el texto.
```

En rendering:

```txt
Objeto
→ ¿esta dentro del volumen visible?
→ ¿esta ocluido por otra geometria?
→ recien ahi, preparar el dibujo.
```

Es la misma forma en cinco ramas distintas: una pregunta barata protege un trabajo caro.

Ejemplo en un Tower Defense:

```csharp
private void TryShoot(Enemy enemy)
{
    if (!enemy.IsAlive) return;
    if (cooldown > 0f) return;

    float sqr = (enemy.Position - Position).sqrMagnitude;
    if (sqr > rangeSqr) return;

    if (!HasLineOfSight(enemy)) return;

    Fire(enemy);
}
```

La torre paga una comparacion por enemigo descartado.

Solo el enemigo que supera todas las guardas paga la linea de vision y el disparo.

---

## Relacion con arquitectura

Se relaciona con:

```txt
Filtrar barato antes de validar caro.
Reducir trabajo antes que acelerarlo.
Responsabilidad unica por metodo.
Codigo plano en vez de anidado.
```

Las guardas explicitan las precondiciones de una operacion.

```txt
Leer las guardas
→ leer bajo que condiciones esto tiene sentido
```

Eso mejora la lectura y tambien el perfilado, porque el costo queda concentrado en un punto identificable.

Conviene mantener las guardas en la entrada del metodo.

```txt
Guardas al principio.
Trabajo en el medio.
Un solo camino caro al final.
```

Cuando las guardas empiezan a repetirse en varios metodos, suelen estar pidiendo subir un nivel.

```txt
Guarda repetida en muchos lugares
→ probablemente sea un filtro del sistema
→ y no una condicion de cada entidad
```

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
CPU
Frame Budget
```

Puede afectar tambien:

```txt
GPU
Memoria
```

cuando la operacion evitada genera geometria, allocations o comandos de dibujo.

El ahorro no se mide por guarda.

Se mide por la ecuacion de siempre:

```txt
Costo evitado
×
cantidad de entidades
×
frecuencia
```

Una guarda que descarta el noventa por ciento de los casos vale mucho mas que una microoptimizacion dentro del diez por ciento restante.

---

## Cuando conviene usarlo

Conviene cuando:

```txt
La operacion posterior es cara.
Muchas entidades ejecutan el mismo camino.
Buena parte de los casos se descarta.
Existen condiciones baratas que descartan temprano.
El codigo tiene varios niveles de anidado.
```

Casos claros:

```txt
Percepcion de IA.
Seleccion de objetivo.
Queries fisicas.
Validacion de acciones.
Actualizacion de interfaz.
```

---

## Cuando NO conviene usarlo

No aporta cuando:

```txt
La operacion posterior ya es trivial.
Casi ningun caso se descarta.
La guarda cuesta parecido a lo que evita.
El metodo se ejecuta pocas veces por partida.
```

Y hay un caso donde directamente estorba:

```txt
Guarda que consulta un componente,
recorre una lista
o hace su propia query,
para evitar una multiplicacion.
```

Ahi la guarda es el costo.

---

## Trade-offs

Ventajas:

```txt
Menos trabajo promedio.
Codigo mas plano y mas legible.
Precondiciones explicitas.
Costo concentrado y facil de perfilar.
```

Costos:

```txt
Mas puntos de salida en un metodo.
Orden de guardas que hay que mantener.
Riesgo de duplicar condiciones entre metodos.
Riesgo de saltear efectos necesarios al cortar antes.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Cortar antes de actualizar estado que debia actualizarse igual.
Ordenar las guardas de cara a barata.
Poner una guarda costosa primero.
Repetir la misma guarda en varios niveles.
Usar el return temprano para tapar un flujo mal definido.
Acumular guardas hasta que nadie entiende cuando entra.
```

Ejemplo de riesgo real:

```txt
Se corta antes de decrementar el cooldown.

Resultado:
la torre queda con el cooldown congelado
y deja de disparar.
```

Lo que se saltea tiene que ser trabajo opcional, no estado que el sistema necesita mantener.

---

## Checklist de implementacion

```txt
¿Cual es la operacion cara que se quiere evitar?
¿Que condiciones la descartan?
¿Cuanto cuesta evaluar cada condicion?
¿Estan ordenadas de barata a cara?
¿Cual descarta la mayor cantidad de casos?
¿Alguna guarda cuesta mas de lo que evita?
¿Se saltea estado que debia actualizarse igual?
¿Hay guardas repetidas en varios niveles?
¿El metodo sigue siendo legible?
¿Se midio el porcentaje de casos descartados?
¿Se midio antes y despues?
```

---

## Regla final

Si el resultado ya se conoce, seguir calculando es gasto puro.

```txt
Preguntar barato antes de trabajar caro.
Cortar apenas se sabe.
Lo que se saltea debe ser trabajo, nunca estado.
```

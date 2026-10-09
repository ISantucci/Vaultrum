## Definicion

Evitar allocations por frame significa reducir o eliminar la creacion de memoria temporal durante gameplay critico.

La idea principal es:

```txt
Allocation por frame
→ basura temporal
→ presion sobre Garbage Collector
→ posible stuttering
```

No significa eliminar toda allocation del juego.

Significa evitar allocations frecuentes en partes que se ejecutan constantemente.

---

## Que problema ayuda a prevenir

Ayuda con:

```txt
GC Alloc por frame
Strings por frame
UI actualizada innecesariamente
Instantiate y destroy constantes
Stuttering
Spikes
Frame time irregular
```

Tambien ayuda a mantener mas estable el Frame Budget.

---

## Como funciona

Se revisan caminos criticos y se evita crear objetos temporales innecesarios.

Ejemplos problematicos:

```csharp
private void Update()
{
    List<Enemy> enemies = new List<Enemy>();
}
```

```csharp
private void Update()
{
    scoreText.text = "Score: " + score;
}
```

```csharp
private void Update()
{
    var enemies = allEnemies.Where(e => e.IsAlive).ToList();
}
```

Soluciones:

```txt
Reutilizar listas.
Actualizar UI por evento.
Evitar LINQ en runtime critico.
Evitar strings por frame.
Usar Object Pool.
Prealocar estructuras.
```

---

## Como aplicarlo en videojuegos

Revisar especialmente:

```txt
Update.
FixedUpdate.
Loops de enemigos.
Targeting.
Pathfinding.
UI.
Proyectiles.
Eventos frecuentes.
Logs.
Sistemas de particulas.
```

Ejemplo:

```txt
Targeting crea una lista nueva cada frame.
```

Mejor:

```txt
Targeting reutiliza una lista temporal controlada.
```

Ejemplo:

```txt
UI concatena texto cada frame.
```

Mejor:

```txt
UI actualiza texto solo cuando cambia el valor.
```

---

## Relacion con arquitectura

Se relaciona con:

```txt
GC Alloc por frame
GC Alloc
Strings por frame
Object pool como optimizacion
UI orientada a eventos
Cacheo de referencias
```

Tambien se relaciona con Estructuras de datos, porque elegir como organizar y reutilizar colecciones afecta allocations.

---

## Relacion con hardware/runtime

Afecta:

```txt
Memoria administrada
Garbage Collector
CPU
Frame Budget
```

Menos allocations frecuentes suelen significar:

```txt
menos presion sobre GC
menos spikes
mas estabilidad
```

---

## Cuando conviene aplicarlo

Conviene cuando:

```txt
Profiler muestra GC Alloc.
Hay stuttering.
Hay allocations por frame.
Hay muchos objetos temporales.
Hay UI con textos frecuentes.
Hay Instantiate/Destroy.
Hay LINQ o listas temporales en Update.
```

---

## Cuando NO conviene obsesionarse

No conviene complicar codigo por allocations que ocurren:

```txt
al cargar escena,
en inicializacion,
al abrir un menu raro,
en herramientas de editor,
en momentos no criticos.
```

La prioridad es runtime critico.

---

## Trade-offs

Ventajas:

```txt
Menos GC.
Menos stuttering.
Mas estabilidad.
Menos memoria temporal.
```

Costos:

```txt
Codigo menos expresivo.
Mas reutilizacion manual.
Mas cuidado con limpieza.
Mas riesgo de estado viejo en colecciones.
```

Ejemplo:

```txt
Reutilizar lista
→ menos allocations
→ hay que limpiarla correctamente.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Reutilizar colecciones sin limpiarlas.
Optimizar codigo que no importa.
Hacer codigo dificil de leer.
Eliminar LINQ en partes no criticas sin necesidad.
Crear pools innecesarios.
```

Ejemplo:

```txt
Lista reutilizada
→ no se limpia
→ contiene enemigos viejos
→ targeting falla
```

---

## Checklist de implementacion

```txt
¿Hay GC Alloc por frame?
¿Ocurre en gameplay critico?
¿Viene de strings?
¿Viene de UI?
¿Viene de listas/arrays?
¿Viene de LINQ?
¿Viene de Instantiate/Destroy?
¿Se puede reutilizar memoria?
¿Se limpian estructuras reutilizadas?
¿Se valido con Profiler?
```

---

## Regla final

No se trata de nunca crear objetos.

Se trata de no crear basura temporal constantemente en el momento mas sensible del juego.

```txt
Runtime critico
→ evitar allocations frecuentes
```
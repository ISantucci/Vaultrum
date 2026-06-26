## Definición

Evitar allocations por frame significa reducir o eliminar la creación de memoria temporal durante gameplay crítico.

La idea principal es:

```txt
Allocation por frame
→ basura temporal
→ presión sobre Garbage Collector
→ posible stuttering
```

No significa eliminar toda allocation del juego.

Significa evitar allocations frecuentes en partes que se ejecutan constantemente.

---

## Qué problema ayuda a prevenir

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

También ayuda a mantener más estable el Frame Budget.

---

## Cómo funciona

Se revisan caminos críticos y se evita crear objetos temporales innecesarios.

Ejemplos problemáticos:

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
Evitar LINQ en runtime crítico.
Evitar strings por frame.
Usar Object Pool.
Prealocar estructuras.
```

---

## Cómo aplicarlo en videojuegos

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
Sistemas de partículas.
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

## Relación con arquitectura

Se relaciona con:

```txt
GC Alloc por frame
GC Alloc
Strings por frame
Object pool como optimizacion
UI orientada a eventos
Cacheo de referencias
```

También se relaciona con Estructuras de datos, porque elegir cómo organizar y reutilizar colecciones afecta allocations.

---

## Relación con hardware/runtime

Afecta:

```txt
Memoria administrada
Garbage Collector
CPU
Frame Budget
```

Menos allocations frecuentes suelen significar:

```txt
menos presión sobre GC
menos spikes
más estabilidad
```

---

## Cuándo conviene aplicarlo

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

## Cuándo NO conviene obsesionarse

No conviene complicar código por allocations que ocurren:

```txt
al cargar escena,
en inicialización,
al abrir un menú raro,
en herramientas de editor,
en momentos no críticos.
```

La prioridad es runtime crítico.

---

## Trade-offs

Ventajas:

```txt
Menos GC.
Menos stuttering.
Más estabilidad.
Menos memoria temporal.
```

Costos:

```txt
Código menos expresivo.
Más reutilización manual.
Más cuidado con limpieza.
Más riesgo de estado viejo en colecciones.
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
Optimizar código que no importa.
Hacer código difícil de leer.
Eliminar LINQ en partes no críticas sin necesidad.
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

## Checklist de implementación

```txt
¿Hay GC Alloc por frame?
¿Ocurre en gameplay crítico?
¿Viene de strings?
¿Viene de UI?
¿Viene de listas/arrays?
¿Viene de LINQ?
¿Viene de Instantiate/Destroy?
¿Se puede reutilizar memoria?
¿Se limpian estructuras reutilizadas?
¿Se validó con Profiler?
```

---

## Regla final

No se trata de nunca crear objetos.

Se trata de no crear basura temporal constantemente en el momento más sensible del juego.

```txt
Runtime crítico
→ evitar allocations frecuentes
```
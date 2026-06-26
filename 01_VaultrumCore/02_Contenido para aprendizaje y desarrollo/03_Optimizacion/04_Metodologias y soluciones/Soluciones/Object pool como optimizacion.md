## Definición

Object Pool como optimización consiste en reutilizar objetos en lugar de crearlos y destruirlos constantemente durante gameplay.

La idea principal es:

```txt
Sin pool:
Instantiate
→ usar
→ Destroy

Con pool:
Get
→ usar
→ Reset
→ Release
→ reutilizar
```

Esta técnica es especialmente útil para objetos temporales que aparecen y desaparecen muchas veces.

---

## Qué problema ayuda a prevenir

Ayuda principalmente con:

```txt
Instantiate y destroy constantes
GC Alloc por frame
Spikes
Stuttering
CPU Bound por creación/destrucción
Presión sobre Garbage Collector
```

Ejemplos de objetos candidatos:

```txt
Proyectiles.
Partículas.
Efectos de impacto.
Enemigos comunes.
Números flotantes de daño.
Objetos temporales.
Loot.
```

---

## Cómo funciona

Un pool mantiene objetos disponibles para reutilizar.

Flujo típico:

```txt
Pool crea objetos iniciales.
Sistema pide objeto.
Pool entrega objeto inactivo.
Objeto se activa y usa.
Objeto termina su ciclo.
Objeto se resetea.
Objeto vuelve al pool.
```

Ejemplo conceptual:

```csharp
public interface IPoolable
{
    void OnGetFromPool();
    void OnReturnToPool();
}
```

El objeto debe saber limpiar su estado.

```txt
Resetear posición.
Resetear velocidad.
Resetear target.
Resetear vida útil.
Detener partículas si corresponde.
Limpiar eventos.
Desactivar colisiones si hace falta.
```

---

## Cómo aplicarlo en videojuegos

En un Tower Defense:

```txt
Tower
→ quiere disparar

ProjectilePool
→ entrega proyectil

Projectile
→ se mueve hacia objetivo

Al impactar:
→ aplica daño
→ vuelve al pool
```

La torre no debería hacer `Instantiate` directamente en cada disparo.

Mejor:

```txt
Tower
→ solicita proyectil

Factory / Pool
→ resuelve creación o reutilización
```

También se puede usar en:

```txt
Impact effects.
Floating damage numbers.
Enemy spawn.
Particles.
Audio sources temporales.
```

---

## Relación con arquitectura

Se relaciona con:

```txt
Object Pool
Factory
Flyweight
Type Object
Instantiate y destroy constantes
GC Alloc por frame
```

Como patrón, Object Pool organiza reutilización.

Como optimización, reduce creación/destrucción durante runtime crítico.

Puede trabajar junto con Factory:

```txt
Factory
→ sabe crear objetos

Pool
→ sabe reutilizarlos
```

No son lo mismo.

---

## Relación con hardware/runtime

Afecta principalmente:

```txt
CPU
Memoria
Garbage Collector
Frame Budget
```

Reduce:

```txt
Instantiate.
Destroy.
Allocations.
Spikes de inicialización.
```

Pero aumenta:

```txt
Memoria reservada.
Complejidad de ciclo de vida.
```

---

## Cuándo conviene usarlo

Conviene usar pool cuando:

```txt
El objeto se crea y destruye muchas veces.
El objeto tiene vida corta.
Hay spikes por creación/destrucción.
Hay GC Alloc asociado.
Se usa durante gameplay crítico.
Hay muchos objetos iguales o similares.
```

Ejemplos claros:

```txt
Balas.
Proyectiles.
Efectos.
Partículas.
Enemigos comunes en oleadas.
```

---

## Cuándo NO conviene usarlo

No conviene usar pool cuando:

```txt
El objeto se crea pocas veces.
El objeto vive toda la escena.
El objeto es muy pesado y raro.
El reset sería más complejo que recrearlo.
No hay problema medido.
La memoria disponible es muy limitada.
```

Ejemplo:

```txt
Un boss único que aparece una vez
→ probablemente no necesita pool.
```

---

## Trade-offs

Ventajas:

```txt
Menos Instantiate/Destroy.
Menos spikes.
Menos presión sobre GC.
Mayor estabilidad en gameplay.
```

Costos:

```txt
Más memoria reservada.
Reset obligatorio.
Más manejo de estado.
Mayor complejidad.
Riesgo de bugs por reutilización.
```

---

## Riesgos de aplicarlo mal

Riesgos comunes:

```txt
No resetear estado.
No limpiar target.
No detener partículas.
No limpiar eventos.
No controlar tamaño del pool.
Pool demasiado grande.
Pool demasiado chico.
Objetos activos duplicados.
Referencias viejas.
```

Ejemplo:

```txt
Proyectil vuelve al pool con target anterior.
Se reutiliza.
Persigue target viejo.
```

Otro ejemplo:

```txt
Objeto se desactiva pero sigue suscripto a evento.
Evento lo llama aunque está en pool.
```

---

## Checklist de implementación

```txt
¿El objeto se crea/destruye frecuentemente?
¿El problema fue medido?
¿Hay spikes o GC Alloc?
¿El objeto puede resetearse bien?
¿Se definió tamaño inicial?
¿Se definió tamaño máximo?
¿Se limpian referencias?
¿Se limpian eventos?
¿Se valida antes/después?
¿El pool no aumenta memoria de forma peligrosa?
```

---

## Regla final

Object Pool no es solo una lista de objetos inactivos.

Es control de ciclo de vida.

```txt
Reutilizar sin resetear
→ bug seguro tarde o temprano.
```
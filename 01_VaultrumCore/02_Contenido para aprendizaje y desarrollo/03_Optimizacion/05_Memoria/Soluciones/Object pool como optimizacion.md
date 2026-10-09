## Definicion

Object Pool como optimizacion consiste en reutilizar objetos en lugar de crearlos y destruirlos constantemente durante gameplay.

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

Esta tecnica es especialmente util para objetos temporales que aparecen y desaparecen muchas veces.

---

## Que problema ayuda a prevenir

Ayuda principalmente con:

```txt
Instantiate y destroy constantes
GC Alloc por frame
Spikes
Stuttering
CPU Bound por creacion/destruccion
Presion sobre Garbage Collector
```

Ejemplos de objetos candidatos:

```txt
Proyectiles.
Particulas.
Efectos de impacto.
Enemigos comunes.
Numeros flotantes de daño.
Objetos temporales.
Loot.
```

---

## Como funciona

Un pool mantiene objetos disponibles para reutilizar.

Flujo tipico:

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
Resetear posicion.
Resetear velocidad.
Resetear target.
Resetear vida util.
Detener particulas si corresponde.
Limpiar eventos.
Desactivar colisiones si hace falta.
```

---

## Como aplicarlo en videojuegos

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

La torre no deberia hacer `Instantiate` directamente en cada disparo.

Mejor:

```txt
Tower
→ solicita proyectil

Factory / Pool
→ resuelve creacion o reutilizacion
```

Tambien se puede usar en:

```txt
Impact effects.
Floating damage numbers.
Enemy spawn.
Particles.
Audio sources temporales.
```

---

## Relacion con arquitectura

Se relaciona con:

```txt
Object Pool
Factory
Flyweight
Type Object
Instantiate y destroy constantes
GC Alloc por frame
```

Como patron, Object Pool organiza reutilizacion.

Como optimizacion, reduce creacion/destruccion durante runtime critico.

Puede trabajar junto con Factory:

```txt
Factory
→ sabe crear objetos

Pool
→ sabe reutilizarlos
```

No son lo mismo.

---

## Relacion con hardware/runtime

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
Spikes de inicializacion.
```

Pero aumenta:

```txt
Memoria reservada.
Complejidad de ciclo de vida.
```

---

## Cuando conviene usarlo

Conviene usar pool cuando:

```txt
El objeto se crea y destruye muchas veces.
El objeto tiene vida corta.
Hay spikes por creacion/destruccion.
Hay GC Alloc asociado.
Se usa durante gameplay critico.
Hay muchos objetos iguales o similares.
```

Ejemplos claros:

```txt
Balas.
Proyectiles.
Efectos.
Particulas.
Enemigos comunes en oleadas.
```

---

## Cuando NO conviene usarlo

No conviene usar pool cuando:

```txt
El objeto se crea pocas veces.
El objeto vive toda la escena.
El objeto es muy pesado y raro.
El reset seria mas complejo que recrearlo.
No hay problema medido.
La memoria disponible es muy limitada.
```

Ejemplo:

```txt
Un boss unico que aparece una vez
→ probablemente no necesita pool.
```

---

## Trade-offs

Ventajas:

```txt
Menos Instantiate/Destroy.
Menos spikes.
Menos presion sobre GC.
Mayor estabilidad en gameplay.
```

Costos:

```txt
Mas memoria reservada.
Reset obligatorio.
Mas manejo de estado.
Mayor complejidad.
Riesgo de bugs por reutilizacion.
```

---

## Riesgos de aplicarlo mal

Riesgos comunes:

```txt
No resetear estado.
No limpiar target.
No detener particulas.
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
Evento lo llama aunque esta en pool.
```

---

## Checklist de implementacion

```txt
¿El objeto se crea/destruye frecuentemente?
¿El problema fue medido?
¿Hay spikes o GC Alloc?
¿El objeto puede resetearse bien?
¿Se definio tamaño inicial?
¿Se definio tamaño maximo?
¿Se limpian referencias?
¿Se limpian eventos?
¿Se valida antes/despues?
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
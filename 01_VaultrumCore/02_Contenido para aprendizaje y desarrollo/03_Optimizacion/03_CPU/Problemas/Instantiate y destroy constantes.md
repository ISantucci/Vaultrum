## Definicion

El problema de `Instantiate` y `Destroy` constantes aparece cuando el juego crea y destruye objetos repetidamente durante gameplay.

En Unity, instanciar y destruir objetos en runtime tiene costo.

Ese costo puede afectar CPU, memoria y Garbage Collector, especialmente si ocurre muchas veces o en momentos criticos.

La idea principal es:

```txt
Crear objetos constantemente
+ destruir objetos constantemente
=
costo de runtime
+ presion de memoria
+ posibles spikes
```

No significa que `Instantiate` o `Destroy` sean malos.

Significa que usarlos constantemente en sistemas repetitivos puede volverse caro.

---

## Responsabilidad de esta nota

Esta nota existe para diagnosticar problemas causados por creacion y destruccion repetida de objetos.

No existe para decir que todo objeto debe usar pool.
No existe para reemplazar la medicion.
No existe para aplicar Object Pool por costumbre.

Su responsabilidad es ayudar a responder:

```txt
¿El juego esta creando y destruyendo objetos demasiadas veces durante gameplay?
```

El foco esta en detectar si el costo viene de:

```txt
instanciacion
destruccion
allocations
picos de CPU
picos de GC
objetos temporales repetidos
```

---

## Sintomas

Sintomas comunes:

```txt
Spikes al disparar.
Tirones al aparecer enemigos.
Caidas cuando se generan efectos.
Stuttering en combate.
GC Alloc frecuente.
CPU Usage alto en momentos de spawn.
Frame time irregular.
Congelamientos breves al crear objetos.
```

Tambien puede verse asi:

```txt
Sin combate
→ el juego anda bien.

Combate con muchos disparos
→ aparecen tirones.
```

O:

```txt
Pocas particulas
→ estable.

Muchas particulas instanciadas
→ spikes.
```

---

## Que parte del software suele causarlo

Suele aparecer en sistemas como:

```txt
Proyectiles.
Enemigos.
Particulas.
Efectos visuales.
Popups de daño.
Objetos temporales.
Loot.
UI dinamica.
Spawners.
Explosiones.
Sonidos instanciados como GameObjects.
```

Ejemplo tipico:

```csharp
void Shoot()
{
    Instantiate(projectilePrefab, firePoint.position, firePoint.rotation);
}
```

Y luego:

```csharp
void OnHit()
{
    Destroy(gameObject);
}
```

Si esto ocurre cientos de veces, puede generar costo acumulado.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
CPU
Memoria
Garbage Collector
Frame Budget
```

Puede afectar CPU porque crear objetos implica trabajo de inicializacion.

Puede afectar memoria porque se crean objetos nuevos.

Puede afectar GC porque se genera basura administrada o referencias temporales.

Tambien puede afectar estabilidad del frame si muchas creaciones o destrucciones ocurren juntas.

---

## Como detectarlo

Se detecta revisando momentos donde aparecen objetos temporales.

Buscar especialmente:

```txt
Spikes coincidiendo con disparos.
Spikes coincidiendo con spawns.
Picos al destruir oleadas.
GC Alloc durante combate.
Muchos objetos creados y destruidos por segundo.
Uso repetido de Instantiate.
Uso repetido de Destroy.
```

Preguntas practicas:

```txt
¿Cuantos objetos se crean por segundo?
¿Cuantos se destruyen por segundo?
¿Son objetos temporales repetidos?
¿Aparecen en momentos criticos?
¿Se pueden reutilizar?
¿El problema aparece al aumentar la cantidad?
```

---

## Herramientas de deteccion

Herramientas utiles:

```txt
Unity Profiler
CPU Usage
Timeline
GC Alloc
Memory Profiler
Logs de diagnostico
```

Que mirar:

```txt
Instantiate.
Destroy.
GC Alloc.
Spikes de CPU.
Cantidad de objetos activos.
Cantidad de objetos creados por segundo.
Cantidad de objetos destruidos por segundo.
```

Logs utiles:

```txt
Cantidad de proyectiles creados.
Cantidad de enemigos instanciados.
Cantidad de efectos creados.
Cantidad de objetos devueltos o destruidos.
```

---

## Soluciones posibles

Soluciones candidatas:

```txt
Object Pool como optimizacion.
Precarga de objetos.
Reutilizacion de instancias.
Desactivar en vez de destruir.
Limitar cantidad maxima de objetos temporales.
Agrupar spawns.
Reducir frecuencia de creacion.
Usar efectos compartidos cuando corresponda.
```

Ejemplo:

```txt
Antes:
Cada disparo instancia una bala nueva.
Cada impacto destruye la bala.

Despues:
Las balas se toman de una pool.
Al impactar vuelven a la pool.
```

Otro ejemplo:

```txt
Antes:
Cada enemigo instancia un popup de daño.

Despues:
Los popups se reutilizan desde una pool de UI.
```

---

## Trade-offs

Usar pooling puede mejorar rendimiento, pero trae responsabilidades.

```txt
Object Pool
→ reduce Instantiate/Destroy
→ requiere resetear estado correctamente.

Precarga
→ evita spikes en gameplay
→ aumenta costo inicial o memoria reservada.

Objetos desactivados
→ se reutilizan rapido
→ pueden ocupar memoria aunque no esten visibles.

Limites maximos
→ controlan costo
→ pueden afectar gameplay o feedback visual.
```

El riesgo principal es olvidar limpiar estado.

Ejemplo:

```txt
Una bala reutilizada conserva daño viejo.
Un efecto conserva escala anterior.
Un enemigo conserva estado de IA previo.
```

Pooling mal aplicado puede generar bugs dificiles.

---

## Ejemplo en videojuegos

En un Tower Defense:

```txt
Torres disparan proyectiles.
Proyectiles impactan enemigos.
Impactos generan particulas.
Enemigos mueren.
Spawner crea nuevas oleadas.
UI muestra popups de daño.
```

Si cada parte instancia y destruye objetos constantemente, el juego puede generar spikes.

Una solucion mas sana puede ser:

```txt
ProjectilePool
→ reutiliza proyectiles.

EffectPool
→ reutiliza efectos.

DamagePopupPool
→ reutiliza UI temporal.

EnemyPool
→ reutiliza enemigos si el diseño lo justifica.
```

No todo necesita pool.

Pero los objetos temporales repetidos son buenos candidatos.

---

## Como guia el diagnostico

Esta nota guia el diagnostico cuando los tirones aparecen junto a creacion o destruccion de objetos.

Flujo recomendado:

```txt
Sintoma:
spikes durante combate o spawn.

Sospecha:
Instantiate/Destroy constante.

Medicion:
Profiler / Timeline / GC Alloc.

Dato esperado:
picos asociados a instanciacion, destruccion o allocations.

Problema confirmado:
objetos temporales generando costo.

Solucion candidata:
Object Pool, precarga o reutilizacion.
```

La pregunta clave es:

```txt
¿Este objeto aparece muchas veces y vive poco tiempo?
```

---

## Errores comunes al intentar solucionarlo

Errores comunes:

```txt
Aplicar Object Pool a todo.
No resetear objetos reutilizados.
Dejar objetos activos al devolverlos.
No limpiar eventos o referencias.
Crear pools enormes sin necesidad.
No medir si Instantiate/Destroy era el problema real.
Usar pool para objetos que casi nunca se crean.
Hacer una pool distinta para cada caso sin criterio.
```

Ejemplo de mala solucion:

```txt
Problema:
Spikes en combate.

Decision:
Crear pools para todos los prefabs del juego.

Resultado:
mas memoria usada, mas complejidad y bugs de estado.
```

La pool debe responder a un problema real.

---

## Hacia donde seguir

Si hace falta medir:

```txt
→ Unity Profiler
→ Timeline
→ GC Alloc
→ Memory Profiler
```

Si se confirma el problema:

```txt
→ Object Pool como optimizacion
→ Evitar allocations por frame
```

Si el problema aparece dentro de muchos Updates:

```txt
→ Muchos Update activos
```

Si hay referencias buscadas al crear objetos:

```txt
→ Busquedas globales por frame
→ Cacheo de referencias
```

Si hace falta entender memoria o GC:

```txt
→ Recursos de hardware
→ GC Alloc por frame
```

---

## Checklist de diagnostico

```txt
¿Hay Instantiate durante gameplay?
¿Hay Destroy durante gameplay?
¿Ocurre muchas veces por segundo?
¿Los objetos son temporales?
¿Los objetos se repiten?
¿El problema aparece en combate, spawn o efectos?
¿Se midio Timeline?
¿Se reviso GC Alloc?
¿Se midio antes/despues?
¿Una pool reduce realmente el costo?
¿La pool tiene reset correcto?
¿Hay riesgo de dejar referencias viejas?
¿El costo de memoria de la pool esta justificado?
```

---

## Regla final

`Instantiate` y `Destroy` no son enemigos.

El problema es usarlos constantemente para objetos repetitivos durante gameplay.

```txt
Si un objeto aparece muchas veces,
vive poco tiempo
y se repite constantemente,
probablemente convenga evaluar reutilizacion.
```
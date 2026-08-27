## Definicion

Los logs de diagnostico son mensajes o registros usados para observar informacion interna del juego durante runtime.

Sirven para verificar hipotesis que no siempre se ven directamente en el Profiler.

La idea principal es:

```txt
Logs de diagnostico
→ datos internos controlados para entender comportamiento
```

No son una herramienta de profiling en sentido estricto, pero pueden ayudar mucho a investigar sistemas.

---

## Para que sirven

Los logs de diagnostico sirven para responder preguntas como:

- ¿Cuantos enemigos estan activos?
- ¿Cuantos proyectiles se crearon?
- ¿Cuantos objetos hay en el pool?
- ¿Cuantas veces se llama un metodo?
- ¿Cuantos eventos se disparan?
- ¿Cuantos listeners hay suscriptos?
- ¿Cuantas rutas se recalculan por segundo?
- ¿Cuantas veces se actualiza la UI?
- ¿Se esta ejecutando una logica mas de lo esperado?

Son utiles para validar hipotesis.

Ejemplo:

```txt
Creo que la UI se actualiza cada frame.
Agrego contador controlado.
Confirmo cantidad de llamadas.
```

---

## Que problemas ayudan a detectar

Logs de diagnostico pueden ayudar con:

```txt
Muchos update activos
Instantiate y destroy constantes
Busquedas globales por frame
UI actualizada innecesariamente
Pathfinding recalculado demasiado seguido
Memory Leak
Pools mal dimensionados
Eventos duplicados
Listeners no desuscriptos
Errores de ciclo de vida
```

Son especialmente utiles cuando el problema es logico o de arquitectura.

---

## Que metricas mirar

Ejemplos de metricas internas:

```txt
Cantidad de objetos activos.
Cantidad de objetos creados.
Cantidad de objetos destruidos.
Cantidad de objetos en pool.
Cantidad de llamadas por segundo.
Cantidad de eventos disparados.
Cantidad de listeners.
Cantidad de rutas solicitadas.
Cantidad de enemigos registrados.
Cantidad de referencias nulas.
Cantidad de rebinding de UI.
```

Tambien pueden usarse contadores acumulados:

```txt
TotalProjectilesCreated
TotalProjectilesReused
TotalPathRequests
TotalUIRefreshes
TotalEnemiesRegistered
```

---

## Como interpretar señales

Ejemplo 1:

```txt
UI Refresh called 3600 times en 60 segundos.

Interpretacion:
La UI se actualiza cada frame.
```

Ejemplo 2:

```txt
Projectiles created: 1000
Projectiles reused: 0

Interpretacion:
El pool no se esta usando o esta mal integrado.
```

Ejemplo 3:

```txt
Path requests per second: 500

Interpretacion:
Pathfinding probablemente se recalcula demasiado seguido.
```

Ejemplo 4:

```txt
Listeners MoneyChanged: 35
Despues de recargar escena: 70

Interpretacion:
Puede haber listeners duplicados o no desuscriptos.
```

---

## Que NO demuestran por si solos

Los logs no reemplazan al Profiler.

Pueden decir:

```txt
se llamo muchas veces
```

pero no siempre dicen:

```txt
cuanto costo
```

Tambien pueden alterar rendimiento si se usan mal.

Ejemplo:

```txt
Debug.Log en Update
→ puede generar costo y allocations
```

Por eso deben usarse con control.

---

## Ejemplo de uso

Ejemplo para proyectiles:

```txt
Objetivo:
Ver si se estan instanciando proyectiles durante gameplay.

Logs:
TotalCreated
TotalReused
ActiveCount
PoolCount
```

Resultado esperado con pool sano:

```txt
Created sube al inicio o bajo demanda.
Reused sube durante gameplay.
ActiveCount varia.
PoolCount recupera objetos.
```

Ejemplo para UI:

```txt
Objetivo:
Ver si HUD actualiza demasiado.

Log controlado:
MoneyTextUpdated count per 10 seconds.
```

Si el dinero cambio 3 veces y el texto se actualizo 600 veces, hay problema.

---

## Errores comunes al usarlos

Errores comunes:

```txt
Dejar Debug.Log dentro de Update.
Loguear cada frame.
No usar flags de debug.
No agrupar resultados.
No quitar logs de builds finales.
Confundir cantidad de llamadas con costo real.
No complementar con Profiler.
Generar strings con logs y causar GC Alloc.
```

Una mala practica:

```csharp
private void Update()
{
    Debug.Log("Enemy position: " + transform.position);
}
```

Esto puede causar mas ruido y costo que informacion util.

---

## Buenas practicas

Buenas practicas:

```txt
Usar flags de debug.
Agrupar logs cada cierto intervalo.
Usar contadores.
Evitar logs por frame.
Loguear solo cambios importantes.
Separar logs de desarrollo y build final.
Usar nombres claros.
Documentar que mide cada contador.
```

Ejemplo conceptual:

```txt
Cada 5 segundos:
- enemigos activos
- proyectiles activos
- proyectiles en pool
- path requests
```

Esto da informacion sin saturar consola.

---

## Relacion con otros sistemas

Logs de diagnostico se relacionan con:

```txt
Unity Profiler
Comparacion antes y despues
Memory Profiler
Update Manager como optimizacion
Object pool como optimizacion
UI orientada a eventos
Pathfinding recalculado demasiado seguido
```

Tambien se relacionan con analisis por IA/agentes.

Una IA puede usar logs bien diseñados para entender:

```txt
frecuencia,
cantidad,
ciclo de vida,
eventos,
estado interno.
```

---

## Checklist de uso

```txt
¿El log responde una pregunta concreta?
¿Esta controlado por flag?
¿Evita ejecutarse cada frame?
¿Agrupa informacion util?
¿No genera demasiado ruido?
¿No altera la medicion?
¿Se combina con Profiler?
¿Se removio o desactivo para build final?
¿La metrica sirve para comparar antes/despues?
```

---

## Regla final

Un buen log de diagnostico no es ruido.

Es una medicion interna con proposito.

```txt
Log util
→ responde una hipotesis

Log excesivo
→ crea ruido y puede afectar rendimiento
```
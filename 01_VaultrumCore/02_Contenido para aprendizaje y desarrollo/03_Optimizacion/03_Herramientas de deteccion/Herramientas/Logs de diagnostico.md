## Definición

Los logs de diagnóstico son mensajes o registros usados para observar información interna del juego durante runtime.

Sirven para verificar hipótesis que no siempre se ven directamente en el Profiler.

La idea principal es:

```txt
Logs de diagnóstico
→ datos internos controlados para entender comportamiento
```

No son una herramienta de profiling en sentido estricto, pero pueden ayudar mucho a investigar sistemas.

---

## Para qué sirven

Los logs de diagnóstico sirven para responder preguntas como:

- ¿Cuántos enemigos están activos?
- ¿Cuántos proyectiles se crearon?
- ¿Cuántos objetos hay en el pool?
- ¿Cuántas veces se llama un método?
- ¿Cuántos eventos se disparan?
- ¿Cuántos listeners hay suscriptos?
- ¿Cuántas rutas se recalculan por segundo?
- ¿Cuántas veces se actualiza la UI?
- ¿Se está ejecutando una lógica más de lo esperado?

Son útiles para validar hipótesis.

Ejemplo:

```txt
Creo que la UI se actualiza cada frame.
Agrego contador controlado.
Confirmo cantidad de llamadas.
```

---

## Qué problemas ayudan a detectar

Logs de diagnóstico pueden ayudar con:

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

Son especialmente útiles cuando el problema es lógico o de arquitectura.

---

## Qué métricas mirar

Ejemplos de métricas internas:

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

También pueden usarse contadores acumulados:

```txt
TotalProjectilesCreated
TotalProjectilesReused
TotalPathRequests
TotalUIRefreshes
TotalEnemiesRegistered
```

---

## Cómo interpretar señales

Ejemplo 1:

```txt
UI Refresh called 3600 times en 60 segundos.

Interpretación:
La UI se actualiza cada frame.
```

Ejemplo 2:

```txt
Projectiles created: 1000
Projectiles reused: 0

Interpretación:
El pool no se está usando o está mal integrado.
```

Ejemplo 3:

```txt
Path requests per second: 500

Interpretación:
Pathfinding probablemente se recalcula demasiado seguido.
```

Ejemplo 4:

```txt
Listeners MoneyChanged: 35
Después de recargar escena: 70

Interpretación:
Puede haber listeners duplicados o no desuscriptos.
```

---

## Qué NO demuestran por sí solos

Los logs no reemplazan al Profiler.

Pueden decir:

```txt
se llamó muchas veces
```

pero no siempre dicen:

```txt
cuánto costó
```

También pueden alterar rendimiento si se usan mal.

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
Ver si se están instanciando proyectiles durante gameplay.

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
ActiveCount varía.
PoolCount recupera objetos.
```

Ejemplo para UI:

```txt
Objetivo:
Ver si HUD actualiza demasiado.

Log controlado:
MoneyTextUpdated count per 10 seconds.
```

Si el dinero cambió 3 veces y el texto se actualizó 600 veces, hay problema.

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

Una mala práctica:

```csharp
private void Update()
{
    Debug.Log("Enemy position: " + transform.position);
}
```

Esto puede causar más ruido y costo que información útil.

---

## Buenas prácticas

Buenas prácticas:

```txt
Usar flags de debug.
Agrupar logs cada cierto intervalo.
Usar contadores.
Evitar logs por frame.
Loguear solo cambios importantes.
Separar logs de desarrollo y build final.
Usar nombres claros.
Documentar qué mide cada contador.
```

Ejemplo conceptual:

```txt
Cada 5 segundos:
- enemigos activos
- proyectiles activos
- proyectiles en pool
- path requests
```

Esto da información sin saturar consola.

---

## Relación con otros sistemas

Logs de diagnóstico se relacionan con:

```txt
Unity Profiler
Comparacion antes y despues
Memory Profiler
UpdateManager
Object pool como optimizacion
UI orientada a eventos
Pathfinding recalculado demasiado seguido
```

También se relacionan con análisis por IA/agentes.

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
¿Está controlado por flag?
¿Evita ejecutarse cada frame?
¿Agrupa información útil?
¿No genera demasiado ruido?
¿No altera la medición?
¿Se combina con Profiler?
¿Se removió o desactivó para build final?
¿La métrica sirve para comparar antes/después?
```

---

## Regla final

Un buen log de diagnóstico no es ruido.

Es una medición interna con propósito.

```txt
Log útil
→ responde una hipótesis

Log excesivo
→ crea ruido y puede afectar rendimiento
```
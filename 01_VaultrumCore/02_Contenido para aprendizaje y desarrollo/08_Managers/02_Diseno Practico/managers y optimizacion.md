## Propósito dentro de Vaultrum

Este documento define cómo un manager puede ayudar o perjudicar la optimización de un videojuego.

El objetivo es evitar una idea incorrecta:

```txt
Crear un manager no optimiza automáticamente.
```

Un manager solo ayuda al rendimiento si administra mejor una responsabilidad que tenía costo innecesario, duplicación, mala frecuencia, mala carga o mal ciclo de vida.

La idea principal es:

```txt
Un manager optimiza cuando reduce trabajo innecesario,
controla recursos,
ordena actualizaciones,
o evita operaciones costosas repetidas.
```

---

## Cuándo un manager puede optimizar

Un manager puede aportar optimización cuando controla:

```txt
frecuencia de actualización,
creación y destrucción de objetos,
carga y descarga de assets,
actualización de UI,
búsquedas globales,
eventos diferidos,
limpieza de memoria,
reutilización de objetos,
acceso a recursos compartidos.
```

Ejemplos:

```txt
UpdateManager
→ reduce Updates dispersos y controla frecuencia.

PoolManager
→ evita Instantiate/Destroy constantes.

AssetManager
→ evita cargas duplicadas y libera recursos.

UIManager
→ evita actualizar UI si el dato no cambió.

EventQueueManager
→ ordena procesamiento de eventos.
```

---

## Cuándo un manager NO optimiza

Un manager no optimiza si solo centraliza código sin reducir costo real.

Ejemplo:

```txt
Antes:
100 objetos hacen trabajo innecesario.

Después:
GameManager hace el mismo trabajo innecesario para 100 objetos.
```

No se optimizó.

Solo se movió el problema.

Tampoco optimiza si:

```txt
agrega un Update gigante,
hace búsquedas globales,
retiene memoria innecesaria,
centraliza demasiados datos,
expone APIs que generan acoplamiento,
o procesa todo cada frame sin criterio.
```

Regla:

```txt
Optimizar no es mover código a un manager.
Optimizar es reducir costo real con evidencia.
```

---

## UpdateManager

Un UpdateManager puede ayudar si muchos objetos ejecutan Update innecesariamente.

Puede administrar:

```txt
registro,
desregistro,
ticks,
frecuencia,
grupos,
pausa,
prioridades si están justificadas.
```

Ejemplo:

```txt
Enemigos lejanos
→ actualizar cada 0.2 segundos.

Torres activas
→ actualizar según necesidad.

Sistemas críticos
→ actualizar cada frame.
```

Riesgo:

```txt
UpdateManager con una lista enorme que procesa todo cada frame sin criterio.
```

Regla:

```txt
UpdateManager sirve si controla frecuencia y reduce callbacks innecesarios.
```

---

## PoolManager

Un PoolManager puede ayudar si hay objetos que aparecen y desaparecen constantemente.

Ejemplos:

```txt
proyectiles,
partículas,
efectos,
enemigos frecuentes,
indicadores visuales,
objetos temporales.
```

Optimiza porque evita:

```txt
Instantiate constante,
Destroy constante,
picos de GC,
costos de inicialización repetidos.
```

Pero debe resetear objetos correctamente.

Riesgo:

```txt
objeto reutilizado conserva estado viejo.
```

Regla:

```txt
PoolManager optimiza si reutiliza objetos sin introducir bugs de estado.
```

---

## AssetManager

Un AssetManager puede ayudar si el proyecto tiene carga dinámica o muchos assets.

Puede optimizar:

```txt
memoria,
tiempos de carga,
duplicación de recursos,
assets innecesarios en escena,
carga bajo demanda,
liberación controlada.
```

Pero puede perjudicar si:

```txt
carga assets pesados durante gameplay crítico,
no libera recursos,
duplica cargas,
mantiene cache infinita,
o acopla gameplay a keys internas.
```

Regla:

```txt
AssetManager optimiza si carga menos, carga mejor y libera correctamente.
```

---

## UIManager

Un UIManager puede ayudar a evitar UI actualizada innecesariamente.

Ejemplo sano:

```txt
MoneyChanged
→ HUD actualiza texto de dinero.
```

Ejemplo malo:

```txt
HUD actualiza todos sus textos cada frame aunque nada haya cambiado.
```

Optimización posible:

```txt
UI orientada a eventos,
cache de referencias,
actualización solo ante cambios,
separar paneles activos e inactivos,
evitar reconstrucciones innecesarias.
```

Riesgo:

```txt
UIManager se vuelve dueño de toda la lógica de UI y gameplay.
```

Regla:

```txt
UIManager optimiza si coordina UI sin absorber reglas de juego.
```

---

## Cacheo de referencias

Un manager puede evitar búsquedas repetidas si cachea referencias correctamente.

Ejemplo:

```txt
Buscar una vez.
Usar muchas veces.
Limpiar cuando deja de ser válido.
```

Pero cachear no significa retener para siempre.

Riesgo:

```txt
manager persistente conserva referencias a objetos destruidos.
```

Regla:

```txt
Cache útil
→ referencia válida y ciclo de vida claro.

Cache peligrosa
→ referencia vieja sin limpieza.
```

---

## Reducir frecuencia

Una optimización muy importante es hacer menos trabajo.

Un manager puede ayudar a reducir frecuencia.

Ejemplos:

```txt
revisar objetivos cada 0.2 segundos,
actualizar UI solo ante eventos,
procesar diagnóstico cada 1 segundo,
recalcular pathfinding solo si cambia el mapa,
limpiar pools al salir de nivel.
```

Regla:

```txt
No todo necesita ocurrir cada frame.
```

---

## Medición antes y después

Un manager de optimización debe validarse con medición.

Antes:

```txt
¿Cuál era el costo?
¿Cuál era el síntoma?
¿Dónde aparecía?
¿Qué herramienta lo mostró?
```

Después:

```txt
¿Bajó el costo?
¿Se redujo GC?
¿Mejoró frame time?
¿Se eliminaron spikes?
¿Se mantuvo comportamiento?
¿Aparecieron nuevos bugs?
```

Herramientas posibles:

```txt
Unity Profiler,
CPU Usage,
Timeline,
GC Alloc,
Memory Profiler,
Frame Debugger,
logs de diagnóstico.
```

Regla:

```txt
Sin comparación antes/después,
la optimización es una suposición.
```

---

## Relación con SOLID

Un manager puede mejorar rendimiento y aun así romper arquitectura.

Ejemplo peligroso:

```txt
Crear un GameManager gigante para evitar Update en muchos objetos.
```

Quizás reduce callbacks, pero rompe SRP.

Mejor:

```txt
UpdateManager
→ administra ticks.

IUpdatable
→ abstracción chica.

Sistemas concretos
→ registran/desregistran.
```

Regla:

```txt
Optimización no debe ser excusa para destruir separación de responsabilidades.
```

---

## Criterio para IA/agente

Cuando una IA proponga un manager por optimización, debe responder:

```txt
¿Qué problema de rendimiento detectó?
¿Qué evidencia existe?
¿Qué costo reduce?
¿Qué herramienta debería medirlo?
Qué responsabilidad administra?
Qué alternativa evaluó?
Qué trade-off introduce?
Cómo se valida antes/después?
```

No debe decir simplemente:

```txt
“Creo un manager para optimizar.”
```

Eso no alcanza.

---

## Ejemplo aplicado a videojuegos

Caso:

```txt
Tower Defense con muchos proyectiles.
Cada disparo instancia y destruye un proyectil.
Aparecen spikes y GC.
```

Solución posible:

```txt
PoolManager de proyectiles.
```

Responsabilidad:

```txt
crear pool inicial,
entregar proyectil,
resetear proyectil,
recibir proyectil,
expandir si corresponde.
```

No debería:

```txt
calcular daño,
elegir objetivo,
decidir disparo,
sumar dinero,
actualizar UI.
```

Validación:

```txt
medir Instantiate/Destroy antes,
medir GC Alloc antes,
implementar pool,
medir después,
verificar que proyectiles resetean estado.
```

---

## Checklist de optimización

Antes de usar un manager como optimización:

```txt
¿Hay síntoma medido?
¿Se identificó el costo real?
¿El manager reduce trabajo, frecuencia, memoria o duplicación?
¿La solución no solo mueve el problema?
¿Tiene responsabilidad clara?
¿Mantiene SOLID?
¿Tiene ciclo de vida definido?
¿Evita Update gigante?
¿Evita búsquedas globales?
¿Limpia referencias?
¿Se puede medir antes/después?
¿Hay trade-off aceptable?
```

---

## Regla final

Un manager no optimiza por existir.

```txt
Manager útil para optimización
→ reduce trabajo real,
→ controla frecuencia,
→ administra recursos,
→ mejora ciclo de vida,
→ se valida con medición.

Manager inútil para optimización
→ centraliza código,
→ agrega acoplamiento,
→ procesa todo igual,
→ y no demuestra mejora.
```
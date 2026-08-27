## Definicion

CPU Bound significa que el rendimiento del juego esta limitado principalmente por la CPU.

En este caso, el problema no esta principalmente en la GPU, sino en el tiempo que tarda el procesador en ejecutar logica, scripts, fisica, IA, animaciones, UI u otros sistemas.

La idea principal es:

```txt
CPU Bound
→ la CPU limita el rendimiento
```

Ejemplo:

```txt
La GPU podria renderizar mas rapido.
Pero la CPU tarda demasiado en preparar el frame.

Resultado:
el juego no llega al objetivo de FPS.
```

---

## Responsabilidad de esta nota

Esta nota existe para explicar cuando el limite de rendimiento esta en CPU.

No existe para resolver todos los problemas de scripts.
No existe para asumir que toda caida de FPS es CPU.
No existe para elegir automaticamente una solucion.

Su responsabilidad es ayudar a responder:

```txt
¿El problema viene del trabajo que esta haciendo la CPU?
```

CPU Bound ayuda a orientar el diagnostico hacia:

```txt
scripts
Update
fisica
IA
pathfinding
busquedas
UI
eventos
instanciacion
logica de gameplay
```

---

## Que problema ayuda a entender

Entender CPU Bound ayuda a evitar confundir problemas de logica con problemas graficos.

Un juego puede bajar FPS aunque visualmente no sea pesado.

Ejemplo:

```txt
Escena simple.
Pocos modelos.
Pocas luces.

Pero:
1000 objetos con Update.
IA costosa.
Busquedas globales.
Pathfinding frecuente.

Resultado:
CPU Bound.
```

CPU Bound ayuda a responder:

- El problema esta en scripts?
- Hay demasiada logica por frame?
- La fisica esta costando mucho?
- La IA consume demasiado?
- Hay muchos callbacks activos?
- Hay busquedas globales?
- El juego escala mal con mas entidades?
- Conviene reducir frecuencia?
- Conviene usar Update Manager?
- Conviene separar logica en clases puras?

---

## Como funciona

La CPU se encarga de ejecutar logica y preparar muchas partes del frame.

En Unity, la CPU puede verse afectada por:

```txt
MonoBehaviour.Update
FixedUpdate
LateUpdate
Scripts
IA
Pathfinding
Fisica
Animaciones
UI
Eventos
Spawners
Instantiate/Destroy
Busquedas
Managers
```

Si esas tareas tardan demasiado, el frame se retrasa.

Ejemplo:

```txt
Objetivo:
60 FPS → 16,66 ms

CPU tarda:
22 ms

GPU tarda:
8 ms

Resultado:
el frame queda limitado por CPU.
```

Aunque la GPU este disponible, el juego no puede ir mas rapido porque la CPU no entrega el frame a tiempo.

---

## Como aplicarlo en videojuegos

CPU Bound suele aparecer en juegos con mucha logica activa.

Ejemplos:

```txt
Muchos enemigos.
Muchos proyectiles.
Muchas colisiones.
IA compleja.
Pathfinding frecuente.
Sistemas de percepcion.
UI dinamica.
Eventos masivos.
Managers mal diseñados.
```

Ejemplo inspirado en Tower Defense:

```txt
Cada torre busca enemigos cada frame.
Cada enemigo calcula progreso.
Cada proyectil ejecuta Update.
El spawner evalua oleadas.
La UI actualiza textos.
El sistema de eventos procesa mensajes.
```

Cada sistema puede parecer razonable, pero la suma puede saturar CPU.

Soluciones posibles dependen de la causa:

```txt
Muchos Update
→ Update Manager
→ reducir frecuencia de actualizacion

Busquedas globales
→ cacheo de referencias

Instantiate/Destroy
→ Object Pool

IA frecuente
→ actualizar por intervalos

Pathfinding frecuente
→ recalcular solo cuando haga falta

UI por frame
→ UI orientada a eventos
```

---

## Como guia el diagnostico

CPU Bound no significa automaticamente “usar una tecnica de optimizacion”.

Primero hay que identificar que parte de la CPU esta costando demasiado.

Flujo recomendado:

```txt
Frame time alto
→ sospecha de CPU
→ medir CPU Usage / Timeline
→ identificar sistema costoso
→ revisar problema asociado
→ evaluar solucion candidata
```

Ejemplo:

```txt
Sintoma:
El juego baja FPS cuando hay muchos enemigos.

Medicion:
CPU Usage muestra alto costo en scripts.

Posibles problemas:
Muchos Update activos.
IA ejecutandose cada frame.
Pathfinding recalculado demasiado seguido.
Busquedas globales por frame.

Siguiente paso:
Ir a la rama CPU para identificar la causa concreta.
```

---

## Cuando conviene consultarlo

Conviene analizar CPU Bound cuando:

```txt
El juego baja FPS aunque visualmente no parece pesado.
Los scripts aparecen costosos.
Hay muchos objetos activos.
El rendimiento cae al aumentar enemigos.
Hay stuttering al ejecutar logica.
La fisica tarda demasiado.
La IA o pathfinding se vuelven pesados.
La UI consume CPU.
```

Tambien conviene consultarlo si una optimizacion grafica no mejora el rendimiento.

Ejemplo:

```txt
Se bajaron sombras y modelos.
El rendimiento no mejoro.

Posible conclusion:
el problema no estaba en GPU.
Revisar CPU.
```

---

## Cuando NO conviene asumirlo

No conviene asumir CPU Bound solo porque el juego baja FPS.

Tambien puede ser:

```txt
GPU Bound
GC Alloc
Memory leak
Carga de assets
VRAM saturada
Render pipeline costoso
```

Ejemplo:

```txt
Hay muchos modelos y luces dinamicas.
El juego baja FPS.
Pero no se midio CPU ni GPU.
```

No se puede afirmar CPU Bound sin datos.

Tampoco conviene asumir que toda logica debe optimizarse.

Ejemplo:

```txt
Un sistema consume 0.05 ms.
No es bottleneck.
```

No vale la pena complicarlo si no limita el frame.

---

## Errores que ayuda a evitar

Entender CPU Bound ayuda a evitar:

- Bajar calidad visual cuando el problema esta en scripts.
- Aplicar Object Pool cuando el costo real esta en pathfinding.
- Optimizar GPU sin revisar CPU.
- Ignorar frecuencia de ejecucion.
- Meter todo en Update.
- Usar busquedas globales por frame.
- Actualizar UI sin cambios.
- Ejecutar IA pesada cada frame.
- Diagnosticar por intuicion.
- Pensar que una escena visualmente simple siempre es barata.

La idea clave es:

```txt
Un juego puede verse simple y aun asi ser caro para CPU.
```

---

## Riesgos de interpretarlo mal

El primer riesgo es confundir CPU Bound con “todo script esta mal”.

No todo script caro es problema.

Hay que analizar:

```txt
cuanto cuesta
cuantas veces se ejecuta
en que contexto ocurre
si escala
si rompe el frame budget
```

Otro riesgo es aplicar soluciones demasiado grandes.

Ejemplo:

```txt
Hay pocos Updates.
Pero se crea un Update Manager complejo.
```

Eso puede agregar sobrearquitectura.

Otro riesgo es mover trabajo sin reducirlo.

Ejemplo:

```txt
Se saca logica de Update.
Pero se ejecuta igual cada frame desde otro manager.
```

El problema sigue.

---

## Hacia donde seguir

Esta nota pertenece a Fundamentos.

Si se quiere entender el presupuesto temporal:

```txt
→ Frame Budget
```

Si se quiere entender que limita el rendimiento:

```txt
→ Bottleneck
```

Si se quiere entender el ciclo de ejecucion:

```txt
→ Game loop
```

Si hay un sintoma concreto de CPU:

→ [[CPU]]

Especialmente:

```txt
Muchos Update activos
Busquedas globales por frame
Pathfinding recalculado demasiado seguido
UI actualizada innecesariamente
Instantiate y Destroy constantes
```

Si hace falta medir:

```txt
→ Flujo de diagnostico
```

Herramientas utiles:

```txt
Unity Profiler
CPU Usage
Timeline
```

Si ya se confirmo el problema:

→ [[Patrones transversales]]

---

## Checklist de diagnostico

Antes de concluir que el juego esta CPU Bound, revisar:

```txt
¿Se midio CPU Usage?
¿La GPU esta esperando a la CPU?
¿El frame time supera el presupuesto?
¿El costo viene de scripts?
¿Hay muchos Update activos?
¿Hay fisica costosa?
¿Hay IA o pathfinding frecuente?
¿Hay busquedas globales?
¿Hay UI actualizada sin cambios?
¿El problema escala con cantidad de objetos?
¿La solucion propuesta reduce costo, cantidad o frecuencia?
```

---

## Regla final

CPU Bound no significa que haya que optimizar todo el codigo.

Significa que la CPU es el limite actual.

```txt
Primero identificar que trabajo de CPU cuesta.
Despues decidir si conviene reducir costo, cantidad o frecuencia.
```
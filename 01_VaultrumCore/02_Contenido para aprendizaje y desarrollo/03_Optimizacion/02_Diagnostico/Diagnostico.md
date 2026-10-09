## Proposito

Esta rama reune el metodo y las herramientas que permiten pasar de un sintoma a un recurso identificado.

No existe para listar herramientas.
No existe para mirar numeros al azar.
No existe para confirmar una sospecha que ya se tenia.

Existe porque ninguna de las otras ramas se puede elegir sin haber medido antes.

---

## Idea central

Esta es la unica rama que no se saltea.

```txt
Fundamentos     se puede consultar despues
CPU             se entra si el diagnostico lo dice
GPU             se entra si el diagnostico lo dice
Memoria         se entra si el diagnostico lo dice
Carga e IO      se entra si el diagnostico lo dice
UI              se entra si el diagnostico lo dice

Diagnostico     se pasa siempre
```

Una herramienta no da un diagnostico: da un dato. El diagnostico lo arma quien interpreta ese dato contra una hipotesis.

```txt
Sintoma
→ hipotesis
→ medicion
→ diagnostico
→ solucion
→ trade-off
→ nueva medicion
→ validacion
```

---

## El primer branch

Despues de detectar un frame caro, lo primero que hay que responder es:

```txt
¿CPU o GPU?
```

Pero con una advertencia que esta rama repite en varias notas: no todo entra en una clasificacion binaria.

```txt
puede haber sincronizacion
puede haber espera de un procesador por el otro
puede ser memoria
puede ser carga
puede ser mixto
```

Por eso la rama trae `CPU Bound` y `GPU Bound` como par simetrico, y no una sola nota que descarte la mitad del problema.

---

## Cuando usar esta rama

Usar Diagnostico cuando:

```txt
hay un sintoma y no se sabe de quien es
hay una hipotesis y hace falta confirmarla
hay que elegir que herramienta responde la pregunta
hay que interpretar una lectura del profiler
hay que demostrar que una optimizacion funciono
la optimizacion funciono y ahora limita otra cosa
```

---

## Como debe usar esta rama una IA

Una IA no debe abrir el profiler y describir lo que ve.

Debe entrar con una hipotesis y salir con un diagnostico:

```txt
Sintoma:      al aparecer una wave hay stutter
Hipotesis:    Instantiate masivo
Medicion:     capturar la aparicion de la wave
Confirmacion: pico en Instantiate y GC Alloc en ese frame
Diagnostico:  CPU, spawning
Candidata:    pooling
Validacion:   volver a capturar la misma wave
```

Si no puede medir, debe declararlo con esas palabras: medicion no disponible, estimacion. No debe presentar una impresion como si fuera un dato.

---

## Herramienta correcta para pregunta correcta

El conocimiento operativo no esta en conocer las herramientas. Esta en saber que pregunta responde cada una.

```txt
¿Donde se consume CPU?              → CPU Profiler / CPU Usage
¿Cuando ocurre y en que thread?     → Timeline
¿Que esta generando basura?         → GC Alloc
¿Que ocupa memoria y que sigue vivo? → Memory Profiler
¿Que se esta dibujando y como?      → Frame Debugger
¿Cuantos batches y triangulos hay?  → Stats
¿Cuantas veces paso esto?           → logs de diagnostico
¿Mejoro de verdad?                  → comparacion antes y despues
```

---

## Metodo

### [[Flujo de diagnostico]]

Explica el recorrido completo desde el sintoma hasta la validacion, y que se hace y que no se hace en cada paso.

Consultar al abrir cualquier trabajo de optimizacion. Es el procedimiento que gobierna toda la seccion.

### [[CPU Bound]]

Explica que significa estar limitado por CPU, que sistemas suelen saturarla y como se confirma.

Consultar cuando el frame sea caro y la escena sea visualmente simple.

### [[GPU Bound]]

Explica que significa estar limitado por GPU, que etapas suelen saturarla y como se confirma.

Consultar cuando el frame sea caro y la escena sea visualmente rica, o cuando bajar la resolucion cambie el frame.

### [[Traslado del cuello de botella]]

Explica por que una optimizacion exitosa puede mover el limite a otro recurso, y por que eso no es un fracaso.

Consultar despues de cada optimizacion, antes de declararla terminada.

### [[Comparacion antes y despues]]

Explica como armar una comparacion valida y que condiciones tienen que ser equivalentes para que el numero signifique algo.

Consultar al cerrar una optimizacion y cada vez que alguien afirme una mejora sin dos mediciones.

---

## Herramientas incluidas

### [[Unity Profiler]]

Herramienta central de medicion. Permite ver el reparto del frame entre subsistemas.

Consultar como primer paso de casi cualquier medicion.

### [[CPU Usage]]

Vista del reparto de CPU dentro del frame: scripts, fisica, animacion, rendering, UI y recoleccion.

Consultar cuando la hipotesis sea de CPU y haga falta saber que subsistema paga.

### [[Timeline]]

Muestra cuando ocurre cada cosa dentro del frame y en que thread, y donde esta el spike.

Consultar cuando el problema sea de distribucion o de picos y el promedio no alcance.

### [[GC Alloc]]

Señal de memoria administrada nueva. La frecuencia importa mas que la cantidad.

Consultar cuando haya spikes periodicos o sospecha de basura por frame.

### [[Memory Profiler]]

Permite ver que ocupa memoria, que sigue vivo y por que, comparando estados.

Consultar cuando la memoria crezca o cuando algo no se libere al cambiar de escena.

### [[Frame debugger|Frame Debugger]]

Muestra como se construye el frame: draw calls, orden, objetos, materiales, passes y batching.

Consultar cuando la hipotesis sea de rendering, para entender que se dibuja y como.

### [[Stats window|Stats]]

Lectura rapida de batches, SetPass calls, triangulos y vertices.

Consultar como señal inicial, nunca como diagnostico final.

### [[Logs de diagnostico]]

Instrumentacion propia: contadores, flags y agrupacion temporal cuando el profiler no responde la pregunta.

Consultar cuando haga falta saber cuantas veces ocurrio algo, no cuanto tardo.

---

## Como se conecta con otras ramas

```txt
Fundamentos
→ da el marco con el que se interpreta la medicion

Diagnostico
→ decide de que recurso es el problema

CPU / GPU / Memoria / Carga e IO / UI
→ la rama del recurso confirmado

Patrones transversales
→ la solucion cuando la misma idea sirve en varias ramas
```

---

## Criterio de uso

Una medicion sirve si se puede repetir.

```txt
misma escena
misma cantidad de objetos
misma duracion
mismo hardware
mismo modo (build o editor)
un solo cambio por vez
```

Cambiar dos cosas y medir una vez no produce evidencia: produce una coincidencia.

---

## Regla final

La herramienta no dice que hacer.

Dice donde mirar.

```txt
Hipotesis
→ medicion
→ diagnostico
```

Sin hipotesis previa, el profiler devuelve numeros. Con hipotesis previa, devuelve una respuesta.

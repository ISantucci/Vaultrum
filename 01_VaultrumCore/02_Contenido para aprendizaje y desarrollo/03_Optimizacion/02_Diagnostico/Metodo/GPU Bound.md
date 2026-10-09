## Definicion

GPU Bound significa que el rendimiento del juego esta limitado principalmente por la GPU.

En este caso, el problema no esta principalmente en la logica, sino en el tiempo que tarda la placa grafica en procesar vertices, fragmentos, transparencias, sombras o efectos de pantalla.

La idea principal es:

```txt
GPU Bound
→ la GPU limita el rendimiento
```

Ejemplo:

```txt
La CPU ya termino de preparar el frame.
Pero la GPU sigue dibujando.

Resultado:
el juego no llega al objetivo de FPS.
```

---

## Responsabilidad de esta nota

Esta nota existe para explicar cuando el limite de rendimiento esta en GPU.

No existe para resolver todos los problemas graficos.
No existe para asumir que toda caida de FPS es GPU.
No existe para culpar automaticamente a la cantidad de poligonos.
No existe para elegir automaticamente una solucion.

Su responsabilidad es ayudar a responder:

```txt
¿El problema viene del trabajo que esta haciendo la GPU?
```

GPU Bound ayuda a orientar el diagnostico hacia:

```txt
resolucion
fragment cost
shaders
transparencias
overdraw
iluminacion
sombras
post-processing
geometria
```

---

## Que problema ayuda a entender

Entender GPU Bound ayuda a evitar confundir problemas graficos con problemas de logica.

Esa es la señal clave: un juego puede bajar FPS aunque los scripts sean triviales.

Ejemplo:

```txt
Pocos scripts.
Poca IA.

Pero:
muchas luces dinamicas.
sombras en todos los objetos.
particulas transparentes grandes.
post-processing completo.

Resultado:
GPU Bound.
```

GPU Bound ayuda a responder:

```txt
¿El costo esta en la cantidad de pixeles procesados?
¿La resolucion es demasiado alta para el hardware objetivo?
¿Hay overdraw acumulado por capas superpuestas?
¿Las transparencias cubren demasiada pantalla?
¿El shader caro se ejecuta donde mas se repite?
¿Las sombras estan configuradas de mas?
¿El post-processing trabaja sobre la pantalla completa?
¿La geometria es demasiado densa para lo que aporta?
```

---

## Como funciona

La GPU esta diseñada para procesar grandes cantidades de trabajo grafico en paralelo.

De forma simplificada, el recorrido es:

```txt
Geometria
→ procesamiento de vertices
→ rasterizacion
→ procesamiento de fragmentos
→ imagen
```

Para optimizar GPU hay que entender que etapa esta generando el costo.

No alcanza con decir que hay demasiados poligonos.

Inventario de lo que puede saturarla:

```txt
Resolucion
Fragment cost
Shaders
Transparencias
Overdraw
Iluminacion
Sombras
Post-processing
Geometria
```

Ejemplo:

```txt
Objetivo:
60 FPS → 16,66 ms

CPU tarda:
8 ms

GPU tarda:
18 ms

Resultado:
el frame queda limitado por GPU.
```

Bajar el costo de CPU no mueve el frame final:

```txt
CPU: 8 ms → 5 ms
GPU: 18 ms → 18 ms

Frame final:
practicamente igual.
```

La CPU termina antes y espera. El limite no se movio.

---

## Como aplicarlo en videojuegos

GPU Bound suele aparecer en juegos con mucha carga visual activa.

Ejemplos:

```txt
Resolucion alta.
Muchas luces dinamicas.
Particulas grandes y transparentes.
Efectos de pantalla completa.
Mucha UI con alpha.
```

Ejemplo inspirado en Tower Defense:

```txt
El mapa usa iluminacion dinamica completa.
Cada torre proyecta sombra.
Cada proyectil deja una estela transparente.
Las explosiones de oleada cubren media pantalla.
El HUD de dinero, vida y wave usa paneles translucidos.
La camara abarca todo el recorrido a la vez.
```

Cada elemento puede parecer razonable, pero la suma puede saturar GPU.

Mapa de causa a solucion candidata:

```txt
Resolucion alta
→ bajar resolucion de render
→ escalar la imagen final

Fragment cost alto
→ simplificar el fragment shader

Transparencias grandes
→ reducir tamaño y cantidad
→ acortar lifetime de particulas

Overdraw
→ reducir capas superpuestas
→ revisar particulas y UI

Iluminacion costosa
→ menos luces dinamicas
→ informacion precalculada

Sombras costosas
→ menor resolucion de sombra
→ menos objetos que proyectan

Post-processing costoso
→ desactivar efectos de bajo valor perceptual

Geometria densa
→ LOD
→ frustum y occlusion culling
```

---

## Como guia el diagnostico

GPU Bound no significa automaticamente bajar la calidad grafica.

Primero hay que identificar que etapa de la GPU esta costando demasiado.

Flujo recomendado:

```txt
Frame time alto
→ sospecha de GPU
→ medir tiempo de GPU
→ identificar etapa costosa
→ revisar problema asociado
→ evaluar solucion candidata
```

Una prueba barata y muy informativa:

```txt
Bajar la resolucion a la mitad.

Mejora mucho → el costo depende de pixeles.
Casi no cambia → el costo esta en otra parte.
```

Ejemplo:

```txt
Sintoma:
El juego baja FPS cuando explota una oleada entera.

Medicion:
El tiempo de GPU sube y el de CPU se mantiene.

Posibles problemas:
Particulas transparentes muy grandes.
Overdraw acumulado.

Siguiente paso:
Ir al problema concreto de la rama grafica.
```

---

## Cuando conviene consultarlo

Conviene analizar GPU Bound cuando:

```txt
El juego baja FPS aunque los scripts sean simples.
El rendimiento cae al subir la resolucion.
El rendimiento cae al mirar hacia una zona cargada.
Aparecen caidas al disparar efectos o particulas.
Bajar calidad grafica mejora el rendimiento.
El mismo juego corre bien en una placa mejor.
```

Tambien conviene consultarlo si una optimizacion de logica no mejora el rendimiento.

Ejemplo:

```txt
Se centralizaron los Update.
Se cachearon referencias.
El rendimiento no mejoro.

Posible conclusion:
el problema no estaba en CPU.
Revisar GPU.
```

---

## Cuando NO conviene asumirlo

No conviene asumir GPU Bound solo porque la escena se ve cargada.

Tambien puede ser:

```txt
CPU Bound
Draw calls preparados por CPU
GC Alloc
VRAM saturada
Carga de assets
Problema mixto
```

Ejemplo:

```txt
Hay miles de objetos distintos en pantalla.
El juego baja FPS.
Pero el costo esta en preparar y enviar los draw calls.
```

Ese caso se ve grafico y es principalmente CPU.

Tampoco conviene asumir que el triangle count explica el costo.

Ejemplo:

```txt
Una particula tiene pocos vertices.
Pero cubre media pantalla.
```

Menos poligonos no significa menos GPU.

---

## Errores que ayuda a evitar

Entender GPU Bound ayuda a evitar:

- Reescribir scripts cuando el problema esta en pixeles.
- Culpar al triangle count sin medir.
- Tratar los draw calls como costo seguro de GPU.
- Ignorar el overdraw de particulas y UI.
- Dejar sombras al maximo en objetos irrelevantes.
- Aplicar post-processing completo sin evaluar que aporta.
- Subir resolucion sin revisar el hardware objetivo.
- Usar transparencias enormes por comodidad.
- Diagnosticar por impresion visual.
- Pensar que una escena vistosa siempre es problema de GPU.

La idea clave es:

```txt
Un juego puede tener scripts triviales y aun asi ser caro para GPU.
```

---

## Riesgos de interpretarlo mal

El primer riesgo es tratar la clasificacion CPU/GPU como binaria pura.

Entre los dos procesadores tambien existe:

```txt
sincronizacion
espera
memoria
carga
```

Un frame puede estar limitado por una espera y no por trabajo grafico.

Otro riesgo es bajar calidad como primera respuesta.

Ejemplo:

```txt
Se apagan todos los efectos.
El juego corre mas rapido.
Pero se perdio lectura y feedback.
```

Eso arregla un numero y rompe la experiencia.

Otro riesgo es mover trabajo sin reducirlo.

Ejemplo:

```txt
Se pasa un calculo del shader a la CPU.
La GPU baja.
La CPU sube y vuelve a limitar.
```

El frame completo no mejoro.

---

## Hacia donde seguir

Esta nota es la gemela simetrica de CPU Bound.

Base conceptual del presupuesto y del limite:

→ [[Fundamentos]]

Conceptos de apoyo:

```txt
→ Frame Budget
→ Bottleneck
→ CPU Bound
```

Si hay un sintoma concreto de GPU:

→ [[GPU]]

Especialmente:

```txt
Overdraw
Transparencias grandes
Sombras costosas
Geometria densa sin LOD
```

Si el costo aparece al preparar y enviar el frame:

→ [[CPU]]

Si el problema apunta a recursos graficos residentes:

→ [[Memoria]]

Herramientas utiles:

```txt
→ Frame debugger
→ Stats window
→ Unity Profiler
```

Si ya se confirmo el problema:

→ [[Patrones transversales]]

---

## Checklist de diagnostico

Antes de concluir que el juego esta GPU Bound, revisar:

```txt
¿Se midio el tiempo de GPU?
¿La CPU esta esperando a la GPU?
¿El frame time supera el presupuesto?
¿Bajar la resolucion mejora el frame?
¿Hay overdraw visible en particulas o UI?
¿Cuantas luces dinamicas hay activas?
¿Cuantos objetos proyectan sombra?
¿El shader caro se ejecuta en muchos pixeles?
¿Hay LOD y culling aplicados?
¿La solucion propuesta reduce pixeles, capas o calidad innecesaria?
```

---

## Regla final

GPU Bound no significa que haya que bajar toda la calidad grafica.

Significa que la GPU es el limite actual.

```txt
Primero identificar que trabajo grafico cuesta.
Despues decidir si conviene reducir pixeles, capas o calidad.
```

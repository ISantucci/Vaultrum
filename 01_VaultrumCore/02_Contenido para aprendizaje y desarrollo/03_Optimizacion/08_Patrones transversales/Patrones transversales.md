## Proposito

Esta rama reune lo que no pertenece a un solo recurso: los patrones que reaparecen en CPU, en GPU, en fisica, en IA y en rendering, y la arquitectura que permite optimizar sin romper comportamiento.

No existe para coleccionar patrones.
No existe para aplicarlos porque estan escritos.
No existe para justificar arquitectura compleja con optimizaciones hipoteticas.

Existe porque hay ideas que se aprenden una vez y sirven en cinco lugares distintos, y separarlas evita escribirlas cinco veces.

---

## Idea central

Cuando la misma solucion aparece en dos ramas distintas, deja de ser una tecnica de esa rama y pasa a ser un patron.

```txt
filtrar barato antes de calcular caro
  → percepcion de IA:      distancia, angulo, raycast
  → fisica:                broad phase, narrow phase
  → rendering:             frustum, occlusion
  → targeting:             candidatos, validos, elegido

no procesar lo que no contribuye
  → IA:          agentes lejanos
  → rendering:   objetos fuera de camara
  → animacion:   personajes no visibles
  → audio:       fuentes lejanas

gastar segun contribucion perceptual
  → geometria, shaders, sombras, animaciones, particulas,
    IA, frecuencia de actualizacion
```

Reconocer el patron es lo que permite resolver un problema nuevo con algo que ya se entendio en otro contexto.

---

## Cuando usar esta rama

Usar Patrones transversales cuando:

```txt
la misma idea sirve en dos ramas distintas
hay que elegir entre varias soluciones que se parecen
hay que explicar por que una solucion funciona, no solo que funciona
hay que dejar el sistema preparado para poder optimizarlo despues
```

---

## Como debe usar esta rama una IA

Una IA debe usar estos patrones para nombrar lo que esta haciendo, no para decidir que hacer.

```txt
correcto    el diagnostico dice X, la solucion es Y, y Y es un caso de broad/narrow
incorrecto  conozco broad/narrow, busco donde aplicarlo
```

El orden importa. Un patron aplicado sin diagnostico es sobrearquitectura con buen nombre.

Y sobre la mitad de arquitectura de esta rama, la regla es dura:

```txt
No hacer arquitectura compleja
porque quizas en el futuro sea mas rapida.
```

Primero tiene que existir un problema real. La performance es una restriccion de ingenieria mas, no una excusa para destruir legibilidad, mantenibilidad, separacion ni testabilidad.

---

## Patrones incluidos

### [[Early Exit]]

Dejar de procesar apenas se conoce el resultado, con los chequeos ordenados de mas barato a mas caro.

Consultar cuando una operacion cara se ejecute para casos que se podian descartar antes.

### [[Broad phase y narrow phase]]

Seleccion amplia y barata, conjunto reducido, validacion precisa y cara.

Consultar cuando haya que validar muchos candidatos con una operacion costosa.

### [[Active Set]]

Distinguir entre los objetos que existen y los que estan siendo actualizados.

Consultar cuando el costo escale con la cantidad de entidades existentes y no con las relevantes.

### [[Escalado de precision]]

Bajar precision donde el jugador no la percibe, como dimension del LOD y no como sistema aparte.

Consultar cuando algo se evalue con mas exactitud de la que hace falta para su situacion.

### [[Batch processing]]

Procesar en grupo entidades que hacen operaciones semejantes, en vez de repartir la logica por objetos.

Consultar cuando muchas entidades hagan lo mismo y el costo este disperso en cientos de lugares.

---

## Arquitectura incluida

### [[Clases puras]]

Logica en C# que no depende del lifecycle del motor.

Consultar cuando haga falta poder medir, testear y reemplazar un sistema sin arrastrar la escena.

### [[Monobehaviour como puente|MonoBehaviour como puente]]

El componente adapta el motor; la clase pura tiene las reglas.

Consultar cuando la logica de gameplay este mezclada con los callbacks del motor.

### [[Separar logica de unity|Separar logica de Unity]]

Tratar al motor como capa de ejecucion y visualizacion, no como el lugar donde viven las reglas.

Consultar cuando no se pueda cambiar un algoritmo sin tocar objetos de escena.

### [[Separacion model view|Separacion model / view]]

El modelo tiene estado y reglas; la view tiene la representacion. Y el gameplay emite hechos que otros sistemas escuchan.

Consultar cuando una optimizacion en un sistema obligue a reescribir UI, camara, input o audio.

---

## Por que la arquitectura esta en una rama de optimizacion

Porque una optimizacion se hace en el lugar donde esta el costo, y eso solo es posible si ese lugar tiene bordes.

```txt
Input
≠
Gameplay
≠
Model
≠
View
≠
UI
```

Si el sistema de enemigos es caro, deberia poder cambiarse sin reescribir la UI, la camara, el input ni el audio. Cuando eso no se puede, el problema no es de performance: es que no hay donde intervenir.

Las clases gigantes hacen exactamente lo contrario:

```txt
dificultan el profiling
aumentan el acoplamiento
dificultan reemplazar algoritmos
esconden que parte del sistema consume recursos
```

Pero la aclaracion tambien es parte del criterio: esto es principalmente arquitectura, no performance. Vaultrum sostiene esa distincion en vez de vender arquitectura como si fuera velocidad.

---

## Como se conecta con otras ramas

```txt
Diagnostico   dice donde esta el costo; el patron dice con que forma atacarlo
Fundamentos   la jerarquia de reduccion de trabajo es de donde salen casi todos estos patrones
CPU           Early Exit, broad/narrow, Active Set y batch processing viven sobre todo ahi
GPU           culling y LOD son estos mismos patrones aplicados al frame grafico
UI            Active Set y Early Exit aplican a listas, paneles y raycasts
```

---

## Criterio de uso

Un patron entra a esta rama si cumple las tres:

```txt
aparece en al menos dos ramas distintas
se puede explicar sin nombrar una API concreta
sigue siendo valido si cambia el motor
```

Si solo sirve para un recurso, pertenece a la rama de ese recurso.

---

## Regla final

Un patron no es una razon para optimizar.

Es la forma que toma una optimizacion que ya fue justificada.

```txt
Diagnostico
→ decision
→ patron
```

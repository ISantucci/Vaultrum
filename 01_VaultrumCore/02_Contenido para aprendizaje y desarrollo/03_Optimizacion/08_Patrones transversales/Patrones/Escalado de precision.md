## Definicion

Escalado de precision consiste en ajustar cuanta exactitud recibe cada sistema segun cuanto aporta esa exactitud a la percepcion del jugador.

No todos los sistemas necesitan maxima precision.

```txt
NPC distante
Sombra lejana
Fisica secundaria
Animacion fuera de camara
Percepcion remota
```

En todos esos casos, buena parte del calculo se pierde antes de llegar a los ojos del jugador.

La precision se escala en varias dimensiones a la vez.

```txt
Frecuencia de evaluacion
Resolucion del resultado
Cantidad de muestras
Complejidad del algoritmo
Cantidad de pasos de simulacion
```

Esto no es un sistema aparte.

```txt
LOD
→ gastar recursos en proporcion
  a la contribucion perceptual

Precision
→ una dimension mas de ese mismo LOD
```

El LOD de geometria es el caso mas conocido, no el unico.

El patron aparece igual en CPU, en GPU, en fisica, en IA y en rendering.

---

## Que problema ayuda a prevenir

Ayuda con:

```txt
Calculo exacto sobre cosas que el jugador no distingue.
IA que evalua a maxima frecuencia estando lejos.
Fisica secundaria simulada con el mismo detalle que la principal.
Sombras y reflejos caros a distancias irrelevantes.
Costo constante sin importar la relevancia.
```

La pregunta que ordena todo es:

```txt
¿Que parte de esta precision llega a percibirse?
```

Si la respuesta es ninguna, ese calculo es candidato claro.

```txt
Costo computacional alto
+
valor perceptual bajo
= candidato a escalar precision
```

---

## Como funciona

La contribucion perceptual se estima con factores baratos.

```txt
Distancia a la camara.
Tamaño en pantalla.
Visibilidad.
Relevancia de gameplay.
Velocidad relativa.
```

A partir de ahi se define una escala de niveles.

```txt
Cerca
→ maxima precision

Distancia media
→ precision reducida

Lejos
→ precision minima

Fuera de percepcion
→ candidato a no ejecutarse
```

La reduccion mas simple y mas rentable suele ser la frecuencia.

```txt
60 evaluaciones/s
→
10 evaluaciones/s
```

Es la misma logica que ya se aplica por sistema.

```txt
Movimiento del jugador
→ cada frame

IA tactica
→ frecuencia menor

Percepcion
→ frecuencia menor

Sistemas ambientales
→ ocasionalmente
```

Si el jugador no puede percibir la diferencia, esas cinco sextas partes del trabajo se ahorran sin costo de experiencia.

Los cambios de nivel conviene distribuirlos.

```txt
Todos bajan de nivel el mismo frame
→ spike

Bajan escalonados
→ costo repartido
```

---

## Como aplicarlo en videojuegos

En IA:

```txt
Agente cercano
→ percepcion frecuente, decisiones finas

Agente lejano
→ percepcion espaciada, decisiones gruesas
```

En fisica:

```txt
Cuerpo principal
→ timestep completo

Fisica secundaria y decorativa
→ menos pasos, menos precision
```

En animacion:

```txt
Personaje en pantalla
→ evaluacion completa

Personaje lejano
→ evaluacion espaciada y menos huesos
```

En rendering:

```txt
Cerca
→ mesh detallado, sombra nitida

Lejos
→ mesh simple, sombra de menor resolucion
```

Ejemplo en un Tower Defense:

```txt
Enemigo en zona de combate
→ busqueda de camino y evasion frecuentes

Enemigo recien spawneado, lejos del jugador
→ avance por ruta simplificada
```

Y del lado de las torres:

```txt
Torre con enemigos en rango
→ reevalua objetivo seguido

Torre sin enemigos cerca
→ revisa cada varios frames
```

La diferencia no se ve en pantalla, y el costo del sistema baja de forma notoria.

Esa torre sin enemigos cerca es tambien el ejemplo de Active Set, que es donde esta desarrollado, y conviene no mezclar las dos respuestas. La pregunta que las separa es:

```txt
¿Puede dejar de hacerlo sin que se note?   → sale del conjunto activo
¿Tiene que seguir haciendolo, mas lento?   → baja de frecuencia o de precision
```

Escalado de precision se ocupa del segundo caso: la torre sigue vigilando, pero mas espaciado. Si directamente puede dejar de vigilar hasta que algo entre a su rango, eso es Active Set.

---

## Relacion con arquitectura

Se relaciona con:

```txt
LOD entendido como principio perceptual.
Valor perceptual por costo.
Distribucion temporal del trabajo.
Frecuencia de actualizacion como parametro.
```

Conviene que el nivel de precision sea un dato del sistema, no una constante escondida en el codigo.

```txt
Nivel de precision
→ parametro visible
→ ajustable por perfil de calidad
→ ajustable por plataforma
```

Y conviene que el sistema conozca su propio nivel.

```txt
Quien decide el nivel
→ el sistema que ve la escena completa

Quien lo usa
→ cada entidad
```

Si cada entidad calcula su propio nivel todos los frames, ese calculo se vuelve parte del costo.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
CPU
GPU
Frame Budget
```

Puede afectar tambien:

```txt
Memoria
```

cuando los niveles se implementan con recursos distintos y hay que tener varios cargados.

El intercambio es directo:

```txt
Precision
↔
tiempo de CPU o de GPU
```

Ese intercambio ya es conocido en fisica.

```txt
menor timestep
→ mas simulaciones por segundo
→ mas costo

mayor timestep
→ menos costo
→ menos precision
```

Escalar precision es aplicar esa misma perilla por entidad y por contexto en vez de aplicarla globalmente.

---

## Cuando conviene usarlo

Conviene cuando:

```txt
Hay muchas entidades a distancias muy distintas.
El costo del sistema es alto y su aporte perceptual es desigual.
Existe una medida barata de relevancia.
La degradacion se puede hacer gradual.
Hay que sostener el juego en hardware de distinta capacidad.
```

Casos claros:

```txt
Multitudes y poblacion de mundo abierto.
Sombras y reflejos.
Fisica decorativa.
Percepcion de IA a distancia.
Sistemas ambientales.
```

---

## Cuando NO conviene usarlo

Hay sistemas donde bajar precision no ahorra: rompe el feeling.

```txt
Input.
Movimiento principal del personaje.
Camara.
Colisiones criticas de gameplay.
Acciones frame-perfect.
```

Esos sistemas definen como se siente el juego.

```txt
Input muestreado a menor frecuencia
→ el juego responde tarde

Camara evaluada de a saltos
→ la imagen se siente rota

Colision critica con menos precision
→ el disparo que acerto no cuenta
```

Ahi la precision no es un costo: es la funcion.

Tampoco conviene cuando la relevancia no se puede estimar barato, o cuando la cantidad de entidades es tan baja que el sistema ya entra en presupuesto.

---

## Trade-offs

Ventajas:

```txt
Costo proporcional a lo que se percibe.
Margen grande sin tocar el algoritmo.
Escalabilidad entre plataformas.
Perilla de calidad con impacto medible.
```

Costos:

```txt
Transiciones visibles entre niveles.
Comportamiento que puede variar segun la distancia.
Mas parametros que ajustar y mantener.
Posible desincronizacion entre entidades de niveles distintos.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Escalar precision en sistemas que definen el feeling.
Umbrales sin histeresis que hacen oscilar el nivel.
Cambiar de nivel de golpe y de forma visible.
Bajar precision hasta cambiar el resultado de gameplay.
Estimar relevancia con un calculo caro.
Ajustar los umbrales sin medir el impacto real.
```

Ejemplo de riesgo real:

```txt
La percepcion lejana baja a 2 evaluaciones por segundo.

Resultado:
el enemigo tarda medio segundo en reaccionar
y el jugador lo lee como un bug.
```

Una optimizacion que cambia como se juega dejo de ser una optimizacion.

---

## Checklist de implementacion

```txt
¿Que parte de esta precision se percibe?
¿Con que medida barata se estima la relevancia?
¿Cuantos niveles hacen falta?
¿Que dimension se reduce en cada nivel?
¿La frecuencia baja lo suficiente para importar?
¿Hay histeresis entre niveles?
¿Los cambios de nivel estan distribuidos en el tiempo?
¿El sistema afecta input, camara, movimiento o colision critica?
¿Cambia algun resultado de gameplay?
¿Los umbrales son parametros visibles?
¿Se valido jugando y no solo con el Profiler?
¿Se midio antes y despues?
```

---

## Regla final

La precision se gasta donde se percibe.

```txt
Lejos, tarde o invisible admite menos exactitud.
Input, camara, movimiento y colision critica no.
Ahi la precision no es costo: es el juego.
```

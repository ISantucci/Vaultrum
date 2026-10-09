## Definicion

Level of Detail consiste en bajar el costo de algo a medida que baja su importancia perceptual.

El caso mas conocido es el geometrico:

```txt
cerca → mesh detallado
media distancia → mesh medio
lejos → mesh simple
```

Pero la idea academica de LOD es mucho mas amplia que un sistema de mallas.

Es un criterio de reparto:

```txt
Principio:
gastar recursos proporcionalmente
a la contribucion perceptual.
```

Se puede aplicar a:

```txt
Geometria.
Shaders.
Sombras.
Animaciones.
Particulas.
IA.
Frecuencia de actualizacion.
```

Lo que el jugador percibe menos puede costar menos.

---

## Que problema ayuda a prevenir

Ayuda principalmente con:

```txt
Costo de vertices y geometria
Costo de fragmentos y shaders
Sombras costosas
Iluminacion en runtime
Trabajo de CPU sobre entidades lejanas
```

El desperdicio que ataca es siempre el mismo:

```txt
Un objeto paga su costo maximo
sin importar cuanto aporta
a la imagen final.
```

Casos tipicos de ese desperdicio:

```txt
Un enemigo denso ocupando diez pixeles.
Un shader completo sobre algo apenas visible.
Una sombra nitida a mucha distancia.
Una animacion evaluada fuera de camara.
Particulas con la misma densidad cerca y lejos.
IA razonando igual a cualquier distancia.
```

---

## Como funciona

LOD necesita dos cosas: una medida de importancia y un conjunto de versiones.

```txt
Medir importancia
→ elegir version
→ ejecutar esa version
```

La medida de importancia suele salir de:

```txt
Distancia a la camara.
Tamaño en pantalla.
Visibilidad.
Relevancia de gameplay.
Presupuesto disponible.
```

Las versiones no son necesariamente mallas:

```txt
Geometria → mas o menos triangulos.
Shader → variante completa o reducida.
Sombra → nitida, difusa o ninguna.
Animacion → cada frame o cada varios frames.
Particulas → mas o menos emision.
IA → decision completa o simplificada.
```

El cambio de nivel puede ser duro o progresivo:

```txt
Corte seco
→ implementacion barata
→ se nota el salto.

Transicion gradual
→ mas suave
→ cuesta mas durante el cambio.
```

---

## Como aplicarlo en videojuegos

En un Tower Defense la camara suele estar alejada y el mapa entero visible. Eso hace que el LOD por distancia rinda menos y el LOD por tamaño en pantalla rinda mas.

Reparto razonable en torres:

```txt
Torre seleccionada
→ maximo detalle.

Torres del resto del mapa
→ detalle medio.

Decoracion del borde del mapa
→ silueta simple.
```

Aplicado a enemigos:

```txt
Enemigo dentro del rango de una torre
→ animacion completa.

Enemigo caminando por el fondo del recorrido
→ animacion a menor frecuencia.

Enemigo recien aparecido y lejos de todo
→ solo posicion y avance.
```

Aplicado a efectos de oleada:

```txt
Explosion cerca del punto de defensa
→ efecto completo.

Explosion en el extremo del mapa
→ menos particulas y menor duracion.
```

El HUD de dinero, vida y wave nunca deberia degradarse: es informacion, no decoracion.

---

## Relacion con arquitectura

LOD funciona bien cuando existe separacion entre que hace un sistema y con cuanto detalle lo hace.

```txt
Comportamiento
≠
nivel de detalle del comportamiento
```

Eso pide:

```txt
Un criterio central que asigna niveles.
Sistemas que aceptan un nivel como entrada.
Configuracion por nivel, no logica dispersa.
Nada de umbrales escondidos en cada objeto.
```

Si cada entidad decide su propio LOD con su propia regla, el resultado se vuelve imposible de balancear y de perfilar.

Se relaciona directamente con:

```txt
Active Set
Frecuencia de actualizacion
Precision escalada
Culling
```

Culling es el caso extremo de LOD: el nivel en que el costo pasa a cero.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
GPU
CPU
Memoria
Ancho de banda
```

Segun donde se aplique, el ahorro cae en lugares distintos:

```txt
LOD de geometria → procesamiento de vertices.
LOD de shader → procesamiento de fragmentos.
LOD de sombras → passes adicionales de escena.
LOD de animacion → CPU.
LOD de IA → CPU.
```

Pero hay un costo que va en direccion contraria:

```txt
Varias versiones del mismo asset
→ mas memoria residente
→ mas datos a cargar.
```

LOD baja tiempo por frame y sube ocupacion de memoria. Es un intercambio, no una ganancia limpia.

---

## Cuando conviene usarlo

Conviene cuando:

```txt
Hay mucha variacion de tamaño en pantalla.
El frame esta limitado por GPU y se midio.
Hay muchas instancias del mismo objeto.
El detalle maximo no se percibe siempre.
La escena tiene profundidad real.
Hay presupuesto de memoria disponible.
```

Rinde especialmente bien con:

```txt
Vegetacion.
Multitudes.
Props repetidos.
Terreno.
Enemigos numerosos.
```

---

## Cuando NO conviene usarlo

No conviene cuando:

```txt
Todo se ve siempre al mismo tamaño.
La camara es fija y cercana.
Hay pocos objetos en escena.
La memoria es el recurso critico.
El objeto es unico y siempre protagonista.
No hay problema medido.
```

Tampoco corresponde degradar informacion que el jugador necesita leer:

```txt
HUD.
Indicadores de estado.
Feedback de daño.
Señales de peligro.
```

Eso no es optimizar. Es romper la comunicacion del juego.

---

## Trade-offs

```txt
Menos detalle a distancia
→ menos costo por frame
→ posible perdida visual.

Varias versiones del asset
→ transicion controlada
→ mas memoria y mas carga.

Cambio de nivel abrupto
→ implementacion simple
→ popping visible.

Transicion gradual
→ sin popping
→ mas costo durante el cambio.

Autoria manual de niveles
→ control fino
→ mucho tiempo de produccion.

Generacion automatica
→ rapida
→ resultados irregulares.
```

---

## Riesgos de aplicarlo mal

Riesgos comunes:

```txt
Popping evidente al cruzar el umbral.
Umbrales elegidos sin mirar el juego.
Niveles que ahorran poco y cuestan mucha autoria.
Aplicar LOD cuando el limite era CPU.
Bajar detalle a objetos protagonistas.
Degradar feedback de gameplay.
Multiplicar memoria sin ganar frame.
Siluetas que cambian de forma al bajar de nivel.
```

Ejemplo:

```txt
Antes:
El enemigo lejano usa la version simple.

Problema:
La version simple pierde el color del casco.

Resultado:
El jugador deja de distinguir el tipo de enemigo.
```

El nivel bajo tiene que conservar la lectura, no solamente la forma general.

---

## Checklist de implementacion

```txt
¿El problema fue medido?
¿El limite estaba realmente en GPU?
¿Se conoce el tamaño en pantalla del objeto?
¿Los umbrales se probaron jugando?
¿Se nota el popping en movimiento?
¿La silueta se mantiene entre niveles?
¿La lectura del objeto se mantiene?
¿Cuanta memoria agregan las versiones extra?
¿Se aplico tambien a shaders, sombras o animaciones?
¿El HUD quedo fuera de la degradacion?
¿Se midio despues del cambio?
¿El ahorro justifica el costo de autoria?
```

---

## Regla final

LOD no es una tecnica de mallas. Es una politica de gasto.

```txt
El costo de algo
deberia parecerse
a lo que ese algo aporta
a lo que el jugador percibe.
```

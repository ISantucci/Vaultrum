## Problema

El CPU se va en animar personajes que el jugador no ve.

## Área

CPU.

## Síntoma observable

```txt
el costo de animacion es el mismo mirando a la pared que mirando a la oleada
muchos personajes detras de la camara o lejos siguen actualizando su esqueleto
```

## Causa técnica

Por defecto, muchos componentes de animación **evalúan la pose en cada cuadro**, se vea o no el personaje. Un esqueleto que nadie ve se paga entero (`Huesos e influencias`).

## Detección

```txt
el profiler: tiempo de animacion con la camara mirando a la nada
cuantos componentes de animacion estan activos contra cuantos estan en pantalla
la configuracion de visibilidad de cada uno
```

## Diagnóstico

Si el tiempo de animación no baja cuando los personajes salen de cámara, es esto.

## Solución

Los motores tienen opciones para animar según la visibilidad y para bajar la frecuencia de actualización con la distancia:

```txt
Unity    el modo de culling del Animator: animar siempre, dejar de actualizar las
         transforms fuera de camara, o detenerse por completo
Unreal   la opcion de tick segun visibilidad del componente de malla esqueletica, y la
         optimizacion de frecuencia de actualizacion por distancia
```

**La trampa.** Detener por completo la animación fuera de cámara también detiene lo que la animación mueve: si el personaje se desplaza por **root motion**, deja de avanzar cuando nadie lo mira, y aparece en otro lugar del que el gameplay esperaba. Lo que mueve al personaje se decide antes (`RA-011`, regla 4: in-place o root motion), y la opción de visibilidad se elige con eso.

## Trade-off

```txt
detener fuera de camara      un salto de pose al volver a entrar en cuadro
menos frecuencia de lejos    movimiento entrecortado si la camara se acerca rapido
```

## Validación

Tiempo de animación con la cámara mirando a la nada, antes y después, y una prueba de gameplay con personajes que se mueven fuera de cámara: tienen que llegar adonde tenían que llegar.

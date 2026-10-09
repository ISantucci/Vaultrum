## Problema

La memoria de animación crece más de lo esperado, o los clips pesan mucho más que lo que el animador creyó haber hecho.

## Área

Memoria y, al descomprimir, CPU.

## Síntoma observable

```txt
un clip de dos segundos pesa como uno largo
la memoria de animacion crece con cada clip nuevo
clips "simples" de pocas claves pesan lo mismo que los complejos
```

## Causa técnica

**Las claves que puso el animador no son las claves que guarda el juego.** Al importar, muchos motores re-muestrean la animación a una frecuencia fija: una muestra por canal y por intervalo, haya o no clave ahí.

```txt
canales por hueso   posicion (3) + rotacion (4) + escala (3) = 10 valores
muestras            una por intervalo de muestreo

sin comprimir  ~  huesos x 10 x muestras por segundo x segundos x 4 bytes

60 huesos, 30 muestras por segundo  ->  ~70 KB por segundo de animacion
```

Después actúa la **compresión**: se descartan las muestras que se pueden reconstruir dentro de un error tolerado, y los canales que no cambian quedan casi gratis. Por eso lo que pesa no es la cantidad de claves del animador sino **cuánto cambia** cada canal.

## Qué pesa cada tipo de clip

```txt
ciclo corto (caminata, carrera)   corto y en bucle: barato. Se paga una vez y se repite
idle                              largo y de poco movimiento: comprime muy bien
accion de combate                 corta y rapida: comprime menos, pero dura poco
transicion                        muchas y cortas: el costo esta en cuantas hay
cinematica                        larga, no ciclica, con todo moviendose: la mas cara
canal de escala animado           un canal que casi nunca hace falta y, si se anima sin
                                  querer, se paga entero
UI                                pocas claves por propiedad (dos a cuatro por
                                  transicion): el costo es despreciable; lo caro es
                                  animar el layout (Canvas rebuild)
2D por cuadros                    no son claves: son imagenes. Ver Sprites en memoria
```

## Detección

```txt
memoria de animacion por clip en el motor, antes y despues de comprimir
canales presentes por hueso: escala animada sin necesidad, huesos sin movimiento
frecuencia de muestreo de importacion
```

## Diagnóstico

Si un clip pesa mucho aunque se mueva poco, hay canales que no hacen falta o la compresión está apagada. Si pesa mucho porque es largo y todo se mueve, el costo es legítimo y se decide por diseño.

## Solución

```txt
compresion encendida y ajustada   con el error tolerado mas alto que no se vea
sin canales de mas                quitar escala animada y huesos quietos del clip
muestreo segun la accion          una accion lenta no necesita la frecuencia de una rapida
clips en bucle donde se pueda     un ciclo de dos segundos en vez de una toma de diez
capas y aditivas                  la respiracion como capa, no repetida en cada clip
```

## Trade-off

```txt
mas compresion     temblor en los extremos, pies que se despegan del piso
menos muestreo     pierde lo rapido: un golpe de dos cuadros desaparece
```

## Validación

Memoria de animación antes y después, y la plancha de contactos del clip comprimido: los pies tienen que seguir apoyando donde apoyaban (`RA-011`).

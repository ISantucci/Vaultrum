## Definición

**El orden de las capas**: el feel se afina en orden —respuesta, simulación, pulido—. Lo que falta en una capa no se compra con la siguiente. Y las tres tienen que decir lo mismo.

---

## Idea central

La capa 3 es la más barata de agregar y la que mejor se ve en un video. Por eso se agrega primero, y por eso es el error más caro: un movimiento que no se puede anticipar con partículas hermosas se siente **resbaloso y caro**; uno que se anticipa bien, sin un solo efecto, se siente **sólido**.

```txt
capa 1  respuesta     sin ella las otras dos no se perciben: un efecto que llega tarde
                      se lee como error, no como impacto
capa 2  simulacion    la que produce prediccion. Un juego se puede sentir bien sin
                      efectos; no se puede sentir bien sin esta
capa 3  pulido        la unica que se agrega al final sin rehacer nada
```

**Armonía.** Las capas, y la metáfora y las reglas encima, tienen que contar la misma historia. Un golpe con sacudida y pausa de impacto sobre un personaje que pesa como una pluma, o un auto realista que gira como un cursor, se perciben como algo que está mal sin que el jugador pueda decir qué. El pulido no promete lo que la simulación no hace.

---

## Especificación en Unity

```txt
1 respuesta    el input se lee en Update, no solo en FixedUpdate: un pulsado leido
               solo en el paso fijo se puede perder. El primer cambio visible (pose,
               sonido) se dispara en el mismo cuadro
2 simulacion   el movimiento se integra con paso fijo; con Rigidbody, la interpolacion
               activada para que el render no tiemble entre pasos (01_Bucle_de_simulacion).
               La interpolacion muestra el paso anterior: suma hasta un paso de retraso
               (20 ms con el paso por defecto de 50 Hz), y entra en la cuenta de la cadena.
               En un juego de precision, paso fijo de 60 Hz o mas
3 pulido       los efectos en un sistema aparte, suscripto a eventos, con un solo
               interruptor que lo apaga entero. El acuse de la accion es capa 1: no se
               apaga con ese interruptor
```

El interruptor no es un lujo: es como se prueba el orden. Con la capa 3 apagada, el juego tiene que seguir siendo controlable.

---

## Quién lo aplica

```txt
Game Design    escribe la seccion de feel en ese orden, y no cierra la capa 3 sin la 2
Produccion     planifica el pulido despues de la simulacion validada, no en paralelo
Programacion   entrega la capa 2 jugable antes de abrir la 3
Arte           el peso de la animacion es el de la simulacion: no lo agranda ni lo achica
Calidad        prueba con la capa 3 apagada
```

---

## Cómo se juzga

```txt
se mide     con el interruptor de capa 3 apagado se completa el recorrido de prueba
            (si o no, y el tiempo contra el de la capa 3 encendida)
se juzga    si se puede anticipar donde termina cada movimiento, y si pulido,
            simulacion y metafora dicen lo mismo
```

---

## Errores comunes

```txt
Arrancar por las particulas.
Agregar juice para tapar un control flojo.
Una animacion de golpe pesado sobre un avatar que la fisica hace liviano.
Un sistema de efectos mezclado con el gameplay, que no se puede apagar.
Afinar la capa 3 mirando un video en vez de jugando.
```

---

## Fuentes

- `02_Game_feel` (Fundamentos) — las tres capas y la regla de orden; la armonía, entre los ocho principios.
- `05_Game_Feel` (Fuentes) — los tres bloques de Swink y el principio de armonía (lectura Vaultrum, sin confrontar con el capítulo 17).
- `01_Bucle_de_simulacion` (Construcción) — el paso fijo y la interpolación.

## Propósito

Los principios que todo juego de Vaultrum cumple para **sentirse bien de manejar**. Son ocho, salen del libro de Swink destilado en la Biblioteca —tres de sus lecturas son de Vaultrum, y están declaradas— y de lo que pasó en proyectos reales, y se aplican en todo desarrollo con interacción en tiempo real sin que el owner tenga que pedirlos.

No existe para enseñar game feel: eso es `02_Game_feel`, en la Biblioteca, con el vocabulario, los números y los casos.
No existe para dictar el estilo de un juego: cuán pesado, cuán rápido o cuán exagerado lo trae el `GDS`.
Existe para que ningún juego llegue a una entrega con el feel como retoque final de Programación.

---

## Por qué es regla y no referencia

Hasta el 2026-10-20 el game feel vivía sólo en la Biblioteca. Funcionó cuando un libro de género lo empujaba y desapareció cuando no:

```txt
un plataformero real   el libro de genero empujaba el feel: el GDS de game feel declaro cada
                       efecto con lo que afirma, su ventana y su techo, y el screenshake
                       quedo reservado a la muerte
un tower defense real  el requerimiento de "game feel y audio" fue de Produccion directo a
                       Programacion, SIN GDS: veinte sonidos, numeros de dano, flash y
                       sacudida, sin ventanas ni techos, en un juego donde mueren diez
                       enemigos a la vez. La validacion de la entrega registro que nadie
                       habia escuchado ni visto un solo efecto
```

El conocimiento estaba. Faltaba que fuera obligatorio, y que cada área supiera qué parte le toca.

---

## Idea central

El game feel es **control en tiempo real** de algo en un **espacio simulado**, con **pulido** que confirma lo que pasó. Se construye en tres capas que se afinan en orden:

```txt
capa 1  respuesta     el sistema acusa en 2 cuadros, y a tiempo     -> agencia
capa 2  simulacion    lo que se mueve se puede anticipar           -> control
capa 3  pulido        cada efecto confirma que paso algo           -> contundencia
```

Y se declara en seis componentes: **input, respuesta, contexto, pulido, metáfora y reglas**. Las cinco partes de la sección de feel del `GDS` los cubren —input → perdón · respuesta → sobre · pulido → efectos · metáfora · reglas—, y el contexto lo pone Level Design. Un `GDS` sin esa sección no especificó el feel: lo dejó para que lo invente quien lo programe.

**De dónde sale cada principio.** Los ocho de Swink (capítulo 17) no son estos ocho: se reescribieron como reglas de Vaultrum y se reparten así.

```txt
Swink, cap. 17             hoja del Core
resultados predecibles     04 - El movimiento tiene sobre
respuesta instantanea      03 - Respuesta instantanea
facil pero profundo        05 - El input se interpreta a favor del jugador
novedad                    07 - Todo efecto tiene frecuencia y techo
respuesta atractiva        08 - El feel se prueba en gris y se cierra jugando
movimiento organico        04 - El movimiento tiene sobre          (lectura Vaultrum)
armonia                    02 - El orden de las capas              (lectura Vaultrum)
pertenencia                05 - El input se interpreta...          (lectura Vaultrum)
sin equivalente en Swink   01 y 06: salen de 02_Game_feel y de los proyectos
```

**Los números de estas notas son del libro que se nombra al lado.** Si difieren, manda el libro: el principio remite, no legisla el número.

---

## Quién aplica qué, en la cadena

```txt
Produccion      ningun requerimiento de feel salta a Programacion sin GDS: el feel es diseno
Game Design     DUENO. Escribe la seccion de feel del GDS —metafora, reglas bajas, sobre,
                perdon, efectos con ventana y techo— y corre el checklist al cerrar
Level Design    el contexto: el espacio que le da sentido al movimiento, contando con el
                perdon declarado y no con el ideal
UI/UX           cuanta senal entra por cada canal: el feel no se come el presupuesto
Arte            cada animacion y cada efecto afirman lo que el GDS declara
Programacion    la capa 2 tal como el GDS la escribe, y los efectos con techo y costo medido
Calidad         el feel se verifica jugando: sin audio, sin capa 3, en serie
```

---

## Cómo debe usar esta sección una IA

Antes de diseñar, implementar o aprobar algo que el jugador maneja:

```txt
¿Que se mueve, y que cree el jugador que es?           (metafora)
¿En que capa estoy decidiendo: respuesta, simulacion o pulido?
¿Lo dicta el GDS, o lo estoy eligiendo yo?
¿Que parte se puede medir antes de jugarlo?
¿Cuantas veces por minuto va a pasar esto?
```

La última es la que más rinde y la que menos se hace.

---

## [[01 - El feel se especifica]]

El feel es diseño y se escribe en el `GDS`: metáfora, reglas, sobre, perdón y cada efecto con lo que afirma, su ventana y su techo. *"Que se sienta bien"* no es una especificación.

Usar al abrir cualquier `RQ` o `GDS` con interacción en tiempo real.

---

## [[02 - El orden de las capas]]

Primero que conteste, después que se pueda anticipar, al final que confirme. Lo que falta en la simulación no se compra con efectos, y los efectos no prometen lo que la simulación no hace.

Usar al ordenar el trabajo de feel y cuando un juego "tiene de todo y se siente mal".

---

## [[03 - Respuesta instantanea]]

Todo input tiene acuse en dos cuadros y la cadena entera entra en el tope de su género (`10_Input_y_respuesta`). 100 ms es el borde donde el control deja de sentirse instantáneo, nunca el objetivo.

Usar en todo `SOL` que lea input y en toda animación de una acción del jugador.

---

## [[04 - El movimiento tiene sobre]]

Lo que el jugador maneja acelera, sostiene y frena con números declarados —el sobre ADSR—, y la metáfora decide cuáles se esperan. Curvas, no saltos de valor, y el mismo movimiento en cualquier máquina.

Usar antes de escribir el movimiento de un avatar, un vehículo o cualquier cosa que el jugador conduzca.

---

## [[05 - El input se interpreta a favor del jugador]]

El juego perdona lo que una persona hace mal siempre —el borde que vio tarde, el botón que apretó antes— y lo declara. Pero no juega por ella: el resultado tiene que seguir siendo suyo.

Usar en todo `GDS` con timing, saltos, apuntado o bordes.

---

## [[06 - Cada efecto afirma algo]]

Un efecto es una oración sobre el estado del juego. Si no cambia lo que el jugador sabe es ruido, y si además tapa algo es un defecto. Se dispara cuando pasa lo que afirma.

Usar al escribir la capa 3 de un `GDS` y al aprobar cualquier efecto visual, sonoro o de cámara.

---

## [[07 - Todo efecto tiene frecuencia y techo]]

Cada efecto se diseña multiplicado por las veces que pasa, con un techo que no se puede pasar, una variación que no se vuelve azar y un costo medido.

Usar en todo efecto que se pueda repetir o acumular.

---

## [[08 - El feel se prueba en gris y se cierra jugando]]

Moverse tiene que gustar en un cuarto vacío, con cubos, antes del arte. Y el feel no se cierra compilado: se cierra cuando alguien lo jugó y lo miró, o se declara no verificado.

Usar al planificar el orden de una entrega, y en todo `QA` y `VE` de un juego.

---

## Lo que no es de esta sección

```txt
el vocabulario, los numeros      Biblioteca: 02_Game_feel
y los casos
la latencia y el perdon,         Biblioteca: 10_Input_y_respuesta
en detalle
el screenshake y la camara       Biblioteca: 11_Camara_y_encuadre
el audio como informacion        Biblioteca: 16_Audio_como_gameplay
la anticipacion de una           Core: Principios de animacion (Anticipacion)
animacion
el costo de un efecto            Core: Optimizacion (Frame Budget, Object Pool)
```

Se nombran, no se enlazan.

---

## Uso correcto dentro de Vaultrum

```txt
RQ jugable
-> GDS con su seccion de feel (Game Design)
-> SOL que implementa la capa 2 tal como esta escrita (Programacion)
-> efectos con techo y costo medido
-> QA jugando: sin audio, sin capa 3, en serie
-> VE que dice quien lo jugo, o que declara que nadie lo hizo
```

No es:

```txt
Funciona
-> le agregamos juice al final
-> se ve bien en el video
-> se cierra
```

---

## Fuentes de la sección

`02_Game_feel` (Fundamentos), actualizado en `EST-023` con la destilación de `05_Game_Feel` (Swink), `69_Designing_Game_Feel_Survey` y `70_Measuring_Game_Feel_Acceleration`; los documentos `59_The_Art_of_Screenshake`, `60_Juice_It_or_Lose_It` y `61_Juicing_Your_Cameras_With_Math`; y los vecinos `10_Input_y_respuesta`, `11_Camara_y_encuadre`, `16_Audio_como_gameplay` y `13_Playtesting_y_validacion`.

Y la evidencia que la volvió regla: dos proyectos reales del owner, uno donde el libro de género empujó el feel y otro donde el feel saltó de requerimiento a código sin pasar por diseño.

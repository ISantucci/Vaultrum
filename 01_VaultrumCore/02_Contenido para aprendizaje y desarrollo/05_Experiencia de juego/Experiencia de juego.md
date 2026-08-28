## Que es esta seccion

Es un **indice**, no un contenido. Es el puntero del Core hacia la **Biblioteca de la Escuela** (`05_Escuela/Biblioteca/`): dice que hay y donde, para que se cargue el libro puntual sin cargar la Biblioteca entera.

```txt
el Core indexa   → liviano, siempre disponible
la Biblioteca    → el peso, se carga on-demand
```

Esa division es deliberada. Un Core que absorbiera los libros seria un Core que hay que leer entero para empezar cualquier cosa.

### Alcance de esta seccion, y su nombre

Esta nota se llama `Experiencia de juego` porque cuando nacio la Biblioteca guardaba solo eso. Hoy indexa **dos mitades**, y conviene decirlo aca antes que descubrirlo abajo:

```txt
EXPERIENCIA    que hace que algo se SIENTA bien       → Fundamentos · Juegos
               lo consultan Produccion, Game Design, Level Design, UI/UX
               ANTES de cerrar el GDS

CONSTRUCCION   COMO se construye tecnicamente         → Construccion
               lo consulta Programacion
               DESPUES, al escribir el SOL
```

El nombre quedo mas angosto que el contenido y **no se renombra**: la Ley 5 pide *un puente por par de capas, y declarado*, y lo que hace de esta nota el puente es su declaracion, no su titulo. Renombrarla dejaria a doce registros `ARQ` nombrando una nota que ya no existe — se rompen doce historias para arreglar una etiqueta. Lo que corresponde es que el alcance este escrito, y esta escrito aca.

---

## Por que esta en el Core

El Core sabia construir bien y no sabia que se siente bien. SOLID, patrones, optimizacion, estructuras, algoritmos y managers producen codigo mantenible; ninguno responde por que un juego correcto puede no ser divertido.

Esa asimetria produjo entregas tecnicamente impecables sin menu, sin condicion de fin y sin forma de volver a jugar. La correccion no fue meter game design en el Core: fue **indexar** el conocimiento que la Escuela destila, para que las areas lo encuentren.

Hay una segunda asimetria, medida en `ARQ-022` y del mismo tipo: **el Core tiene el precio de todo y el mecanismo de nada.** `Fisica costosa` dice cuanto sale la fisica por frame; ninguna nota dice que es un integrador. `Costo de fragmentos y shaders` dice que pagas por un shader; ninguna dice como corre el pipeline. `Game loop` lo declara en su propio cuerpo: *"no existe para documentar el orden interno del motor"*. El mecanismo tampoco entra al Core: se indexa, igual que la experiencia.

Esta nota es el **puente** del Core hacia la Biblioteca: la unica seccion del Core que enlaza hacia otra capa, y la unica que puede hacerlo. Lo hace por diseno: el Core es la fuente de criterio, y parte del criterio es saber donde esta el resto. Lo que el Core **no** hace es depender de la Biblioteca para existir — si un libro falta, el Core lo dice y eso dispara una mision de Escuela.

---

## [[00_Indice_fundamentos|Estante de Fundamentos (transversal a todo genero)]]

Los cinco primeros son el marco; los doce siguientes profundizan un pilar de `05` cada uno. Se carga **el que hace falta**, no el estante.

| Libro | Que responde | Cuando cargarlo |
|-------|--------------|-----------------|
| 04_Playbook_de_diseno | principios accionables ordenados **por funcion** (mostrar, guiar, feel, decisiones, retener, sistemas, emocion, marco, produccion, restricciones) | cuando se sabe *que se quiere lograr* y falta como |
| 05_Fundamentos_de_experiencia_ludica | los 9 pilares de por que algo **se siente bien**, con checklist verificable por especificacion | al disenar o revisar un sistema jugable |
| 01_Loop_de_experiencia | input → feedback → objetivo → victoria/derrota; loops anidados | cuando hay dudas de si lo que hay es un juego o un juguete |
| 02_Game_feel | las tres capas del feel, vocabulario de efectos con sus ventanas, juice que informa vs juice que decora | cuando el sistema funciona y no se siente |
| 03_Definicion_de_terminado | la checklist que separa *compila* de *esta hecho* | antes de dar cualquier entregable por terminado |
| 06_Dificultad_y_curva | cuatro ejes de dificultad, curva escalonada, DDA, asistencias | al fijar dificultad, o cuando el playtest dice "facil" y "dificil" a la vez |
| 07_Economia_y_balance | fuentes, sumideros y stocks; bola de nieve y catch-up; balance sin datos | cuando hay recursos que entran y salen |
| 08_Progresion_y_recompensa | las tres progresiones (personaje / jugador / contenido), vertical vs horizontal | cuando el jugador tiene que sentir que avanza |
| 09_Onboarding_y_tutorial | ensenar es diseno de niveles; presupuesto de atencion 60s / 5min / 30min | antes de escribir el primer tutorial |
| 10_Input_y_respuesta | la cadena de latencia en siete tramos con tope ≤65 ms, perdon de input, curvas analogicas | en todo GDS con movimiento — es seccion propia y obligatoria |
| 11_Camara_y_encuadre | taxonomia de camara, contrato de informacion, smoothing, presupuesto de screenshake | cuando la camara marea, tapa o llega tarde |
| 12_Pacing_y_estructura | la curva de intensidad como objeto disenable, unidades de pacing, densidad de novedad | al ordenar el contenido en el tiempo |
| 13_Playtesting_y_validacion | **dueno del territorio de playtest**: protocolo, preguntas prohibidas, telemetria (tope duro de 10 eventos) | antes de sentar al primer tester |
| 14_UI_HUD_y_menus | jerarquia de informacion, cuatro superficies, los estados de UI que se olvidan, gamepad | al disenar cualquier pantalla |
| 15_Muerte_reintento_y_checkpoints | el costo de la muerte como perilla, checkpoints, muerte instructiva | cuando el jugador puede perder |
| 16_Audio_como_gameplay | confirmar / advertir / ubicar; jerarquia de mezcla; redundancia visual | cuando el audio tiene que **informar**, no acompanar |
| 17_Scope_prototipado_y_cierre | el verbo unico, que pregunta responde cada prototipo, feature freeze | al abrir un proyecto y al no poder cerrarlo |

**Diferencia entre los dos grandes:** el Playbook ordena el canon por *para que sirve*; `05_Fundamentos_de_experiencia_ludica` lo ordena por *por que se siente bien* y aterriza en un gate. Se usan juntos, no se reemplazan.

**Regla de carga, medida:** los doce libros `06`–`17` juntos pesan **53.2k tokens = 133% de un presupuesto de 40k**. Un `GDS` real —`05` mas los dos o tres pilares que toca— pesa 19.5k, el 49%. Jalar el estante entero **no entra**. No es una recomendacion de estilo.

---

## [[00_Indice_juegos|Estante de Juegos (por genero)]]

| Genero | Tipo | Libro |
|--------|------|-------|
| Arcade | Paleta-y-pelota | 01_Pong |
| Plataformas | Plataformero 2D de precision | 02_Plataformero_2D |

El estante crece de a un libro por genero, por mision de la Escuela.

**Que trae un libro de genero que no trae un Fundamento:** las *table-stakes* concretas de ese tipo de juego, su juice caracteristico, su baseline de parametros con rangos, y su definicion de terminado especifica. Es lo que permite que un pedido de "hace un X" arranque con el minimo de X ya cubierto.

---

## [[00_Indice_construccion|Estante de Construccion (el mecanismo)]]

La otra mitad. Estante abierto en `ARQ-022` porque la Biblioteca era una escuela de juegos y tenia que ser una escuela de **desarrollo** de videojuegos. Los libros de aca no dicen que se siente bien: dicen como funciona la cosa que el Core ya sabe cuanto cuesta.

| Libro | Que responde | Cuando cargarlo | Que del Core supone sabido |
|-------|--------------|-----------------|-----------------------------|
| 01_Bucle_de_simulacion | el paso fijo con acumulador; que relacion amarra `h` con las ventanas que el GDS escribe en frames; de donde sale el techo de pasos; determinismo | al escribir cualquier `SOL` que simule movimiento, y **obligatoriamente** si el GDS declara una tolerancia en frames | `Game loop`, `Frame Budget`, `Frame time y estabilidad` — el presupuesto de frame |
| 02_Colision_y_consulta_espacial | las tres preguntas geometricas (solape, barrido, consulta); resolucion por eje; el raycast y sus seis modos de fallar | antes de elegir motor de fisica contra cinematica propia, y antes del primer raycast de un `SOL` | `Broad phase y narrow phase`, `Fisica costosa`, `Particionado espacial`, `Early Exit` — el costo |
| 03_Matematica_del_movimiento | vectores como intencion; por que el suavizado por frame da una camara distinta en cada maquina; easing; curvas; aleatoriedad con semilla | antes de escribir cualquier suavizado o camara, y cuando el GDS escribe un porcentaje | `Costo cantidad y frecuencia` — cuando el costo importa |

**La direccion del remite es una sola:** el libro nombra al Core con backticks; el Core no aprende del libro. Un libro de Construccion que empiece a legislar sobre costo esta fuera de su territorio.

**Territorio que el estante todavia no cubre**, ordenado por lo que desbloquea en `EST-011_Mision_Mapa_Territorio_Tecnico`: datos y guardado, herramientas de editor, fichas de manuales oficiales, audio tecnico, build y release, animacion, arte tecnico, netcode. Si Programacion necesita uno de esos y no esta, **no se suple con criterio propio**: se declara el faltante y se deriva a la Escuela.

---

## Como se usa

**Regla de carga:** se jala el libro puntual, nunca la Biblioteca entera. Medido arriba: el estante de Fundamentos entero excede el presupuesto en un tercio.

```txt
DISENO (antes de cerrar el GDS)
1. Identificar el genero / tipo del entregable.
2. Cargar el libro de ese genero desde el estante de Juegos.
3. Cargar los Fundamentos que ese trabajo requiera (no todos).

CONSTRUCCION (al escribir el SOL)
4. Cargar de Construccion solo el libro del mecanismo que el SOL decide.

EN LOS DOS CASOS
5. Si el libro NO existe o esta vacio:
     no se suple con criterio propio
     se declara el faltante y se deriva a la Escuela
```

El paso 5 no es opcional. Es la regla de borde de `Gates verificables`: el insumo se verifica antes de consumirlo. Un libro vacio consumido como si tuviera contenido fue exactamente lo que hundio una entrega.

**Un libro solo es insumo valido cuando esta *En la Biblioteca*.** Un libro *En estudio* o *En validacion* es material en curso: Produccion lo rechaza en su gate de insumo y deriva a Escuela.

---

## Quien lo consulta

```txt
Produccion      → antes de escribir requerimientos (que table-stakes entran como RQ propio)
Game Design     → al disenar el sistema y al correr el checklist por especificacion
Level Design    → pacing y curva, cuando aplica
UI/UX           → claridad, legibilidad, feedback
Programacion    → al escribir el SOL: el estante de Construccion
Conocimiento    → para decidir que de la Biblioteca se promueve a criterio indexado
```

---

## Relacion con Criterios de entrega

Las dos secciones se necesitan y no se superponen:

```txt
Baseline de entregable     → dice que TIENE QUE HABER un minimo por tipo
esta seccion                   → dice DONDE ESTA ese minimo, por tipo
```

La primera es la regla. Esta es el indice. Si la regla existe y el indice esta vacio para un tipo dado, la regla no se puede cumplir — y eso es un faltante declarable, no una licencia para improvisar.

---

## Regla de esta seccion

```txt
Esta seccion indexa. No copia.
```

Si un contenido de la Biblioteca aparece transcrito aca, es duplicacion: se borra y se deja el puntero al estante. Lo unico que puede crecer en esta seccion es la tabla — y **crecer es parte del trabajo**: esta nota indexo cinco Fundamentos de diecisiete durante tres misiones, mientras el estante crecia sin ella. Un indice que no sigue a su estante es un indice que manda a las areas a un mapa viejo.

Que un libro se promueva a criterio propio del Core —dejando de ser referencia y pasando a ser regla— lo decide el Area de Conocimiento con aprobacion del owner. Hasta entonces, se indexa.

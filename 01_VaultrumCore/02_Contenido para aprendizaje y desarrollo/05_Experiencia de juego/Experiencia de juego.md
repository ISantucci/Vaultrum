## Que es esta seccion

Es un **indice**, no un contenido.

El conocimiento sobre experiencia jugable —que hace que algo se sienta bien de jugar, y cual es el minimo de cada genero— no vive en el Core: vive en la Biblioteca de la Escuela (`05_Escuela/Biblioteca/`). Esta seccion es el puntero liviano que dice **que hay y donde**, para que se pueda cargar el libro puntual sin cargar la Biblioteca entera.

```txt
el Core indexa   → liviano, siempre disponible
la Biblioteca    → el peso, se carga on-demand
```

Esa division es deliberada. Un Core que absorbiera los libros seria un Core que hay que leer entero para empezar cualquier cosa.

---

## Por que esta en el Core

El Core sabia construir bien y no sabia que se siente bien. SOLID, patrones, optimizacion, estructuras, algoritmos y managers producen codigo mantenible; ninguno responde por que un juego correcto puede no ser divertido.

Esa asimetria produjo entregas tecnicamente impecables sin menu, sin condicion de fin y sin forma de volver a jugar. La correccion no fue meter game design en el Core: fue **indexar** el conocimiento que la Escuela destila, para que las areas lo encuentren.

Es la unica seccion del Core que enlaza hacia la Biblioteca. Lo hace por diseno: el Core es la fuente de criterio, y parte del criterio es saber donde esta el resto.

---

## [[00_Indice_fundamentos|Estante de Fundamentos (transversal a todo genero)]]

| Libro | Que responde | Cuando cargarlo |
|-------|--------------|-----------------|
| 04_Playbook_de_diseno | principios accionables ordenados **por funcion** (mostrar, guiar, feel, decisiones, retener, sistemas, emocion, marco, produccion, restricciones) | cuando se sabe *que se quiere lograr* y falta como |
| 05_Fundamentos_de_experiencia_ludica | los 9 pilares de por que algo **se siente bien**, con checklist verificable por especificacion | al disenar o revisar un sistema jugable |
| 01_Loop_de_experiencia | input → feedback → objetivo → victoria/derrota; loops anidados | cuando hay dudas de si lo que hay es un juego o un juguete |
| 02_Game_feel | juice, peso, respuesta al control | cuando el sistema funciona y no se siente |
| 03_Definicion_de_terminado | la checklist que separa *compila* de *esta hecho* | antes de dar cualquier entregable por terminado |

Los dos primeros estan destilados y completos. Los otros tres son mas chicos y crecen por mision de la Escuela.

**Diferencia entre los dos grandes:** el Playbook ordena el canon por *para que sirve*; Fundamentos de experiencia ludica lo ordena por *por que se siente bien* y aterriza en un gate. Se usan juntos, no se reemplazan.

---

## [[00_Indice_juegos|Estante de Juegos (por genero)]]

| Genero | Tipo | Libro |
|--------|------|-------|
| Arcade | Paleta-y-pelota | 01_Pong |

El estante crece de a un libro por genero, por mision de la Escuela.

**Que trae un libro de genero que no trae un Fundamento:** las *table-stakes* concretas de ese tipo de juego, su juice caracteristico, su baseline de parametros con rangos, y su definicion de terminado especifica. Es lo que permite que un pedido de "hace un X" arranque con el minimo de X ya cubierto.

---

## Como se usa

**Regla de carga:** se jala el libro puntual, nunca la Biblioteca entera.

```txt
1. Identificar el genero / tipo del entregable.
2. Cargar el libro de ese genero desde el estante de Juegos.
3. Cargar los Fundamentos que ese trabajo requiera (no todos).
4. Si el libro de genero NO existe o esta vacio:
     no se suple con criterio propio
     se declara el faltante y se deriva a la Escuela
```

El paso 4 no es opcional. Es la regla de borde de `Gates verificables`: el insumo se verifica antes de consumirlo. Un libro vacio consumido como si tuviera contenido fue exactamente lo que hundio una entrega.

---

## Quien lo consulta

```txt
Produccion      → antes de escribir requerimientos (que table-stakes entran como RQ propio)
Game Design     → al disenar el sistema y al correr el checklist por especificacion
Level Design    → pacing y curva, cuando aplica
UI/UX           → claridad, legibilidad, feedback
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

Si un contenido de la Biblioteca aparece transcrito aca, es duplicacion: se borra y se deja el puntero al estante. Lo unico que puede crecer en esta seccion es la tabla.

Que un libro se promueva a criterio propio del Core —dejando de ser referencia y pasando a ser regla— lo decide el Area de Conocimiento con aprobacion del owner. Hasta entonces, se indexa.

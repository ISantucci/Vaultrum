## Propósito

Esta subsección reúne el criterio para **construir** una malla: en qué orden, con qué topología, dónde poner la densidad y qué cambia según lo que se modela.

No existe para enseñar los comandos de un programa: eso lo opera la IA desde `08_Operar el arte`.
No existe para fijar un presupuesto de caras: eso es `Caras en pantalla`, en la rama Arte de Optimización.

Existe porque el Modelador del Área de Arte tiene nueve reglas de construcción salidas de defectos, y ninguna que diga cómo se decide una topología antes de que falle.

---

## Idea central

```txt
la silueta primero, el detalle despues
la densidad donde se ve y donde se dobla, en ningun otro lado
la topologia se elige por lo que la malla va a HACER, no por como se ve quieta
```

Un modelo quieto perdona casi todo. Uno que se deforma, que se ve de cerca o que aparece doscientas veces, no.

---

## [[Del bloqueo al detalle]]

El orden de construcción: bloquear con primitivas para fijar escala, proporción y silueta, y recién después refinar. Es el orden que evita detallar algo que después cambia de tamaño.

---

## [[Topologia y flujo de aristas]]

Quads, bucles de aristas que siguen la forma, polos y dónde ponerlos. Es lo que hace que una malla se pueda leer, editar y subdividir.

---

## [[Topologia para deformar]]

Lo que necesita una malla que se va a doblar: bucles en las articulaciones, densidad donde la piel se estira, y la prueba con poses extremas antes de animar.

---

## [[Low poly]]

Los dos significados de *low poly* —un estilo y un presupuesto— y por qué las caras se gastan en la silueta.

---

## [[Hard surface y organico]]

Superficie dura y orgánica piden topologías, sombreados y flujos distintos. Elegir mal el enfoque es la causa más común de una malla en ley que se ve mal.

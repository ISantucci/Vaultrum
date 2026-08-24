## Que es

El criterio que define **que trae una entrega sin que haya que pedirlo, y que no trae aunque se pueda**.

Se enuncia en una linea:

```txt
Completo en experiencia, minimo en maquinaria.
```

Son dos reglas que parecen opuestas y son la misma vista desde los dos lados. Una dice que hay que traer sin pedirlo lo que el entregable necesita para ser satisfactorio. La otra dice que no hay que traer sin pedirlo lo que nadie necesita.

---

## Por que existe

El costo de quien usa un sistema asistido se mide en **cuantas veces tiene que pedir**.

Cada vez que hay que pedir algo que cualquier version competente del entregable ya deberia traer, ese pedido se gasta en trabajo remedial en vez de gastarse en la idea propia. Y cada vez que la entrega trae maquinaria que nadie pidio, consume el mismo presupuesto que una funcionalidad que nadie pidio.

Los dos errores producen el mismo sintoma —una entrega que no responde a lo que se queria— desde direcciones opuestas.

**Origen:** el desarrollo del Pong 3D (`TL-002` / `TL-003`). El juego salio 7/10; el *desarrollo* saco 4/10. El problema no fue el codigo: fue la cantidad de pedidos que hicieron falta para llegar a algo tan basico. En paralelo, una corrida tecnica del mismo juego hecha fuera del sistema produjo ingenieria excelente —loop con accumulator a 120 Hz, deteccion de colision continua propia, cero asignaciones por frame, batching ajustado— para un problema donde nadie habia pedido rendimiento ni determinismo. Ocho decisiones, todas tecnicas, ninguna sobre la experiencia. Ese build no tenia menu, ni condicion de fin declarada, ni forma de volver a jugar.

Las dos mitades de la ley salieron del mismo proyecto.

---

## Mitad 1 — Completo en experiencia

> Las *table-stakes* de un tipo de entregable no se piden: se incluyen.

Una *table-stake* es lo que hace que el entregable **sea** de su tipo. No es una funcionalidad extra: es la condicion para que la cosa exista como esa cosa.

En un videojuego, el minimo es:

```txt
input → feedback perceptible
objetivo claro sin explicacion externa
condicion de victoria y de derrota
estados: inicio / pausa / fin / reinicio
poder volver a jugar sin cerrar la aplicacion
ninguna pantalla sin salida
```

Un juego sin condicion de fin no es un juego incompleto: es un juguete. Un menu sin forma de salir no es un menu austero: es un menu roto.

Fuera de videojuegos la lista cambia y la regla no. Un script de linea de comandos sin mensaje de error util, sin codigo de salida y sin `--help` esta igual de incompleto. Un documento sin la pregunta que responde declarada arriba, tambien.

**Donde vive la lista concreta.** El Core no la guarda: la guarda la Biblioteca de la Escuela, por genero y por tipo, y se consulta on-demand. Ver `Experiencia de juego` para el indice. Si el entregable es de un tipo que la Biblioteca no cubre, eso **no** se resuelve por intuicion: se declara como faltante y se manda a estudiar.

---

## Mitad 2 — Minimo en maquinaria

> No enciendas maquinaria que ningun requerimiento pidio — y eso incluye la maquinaria propia.

La regla **no** es "no optimices" ni "no uses patrones". Es que la justificacion tiene que apuntar a un requerimiento, no a un principio.

El mismo codigo puede ser correcto o ser alcance no pedido segun contra que se justifique:

```txt
apagar la fisica en un Pong
  porque el rebote de Pong no es fisico          → correcto (regla de diseno)
  porque la broadphase cuesta                     → alcance no pedido (nadie pidio rendimiento)

un solo Update
  porque el efecto lee la velocidad de la paleta
  en el instante del golpe y el orden no puede
  depender del execution order                    → correcto (lo pide el diseno)
  porque ahorra saltos managed/native             → alcance no pedido
```

Misma decision tecnica. Distinta justificacion. Solo una de las dos se puede defender frente a quien pidio el trabajo.

Ver `Cuando NO optimizar` para el desarrollo de esta mitad aplicado a rendimiento.

---

## Como se prueba cada mitad

Las dos tienen una prueba mecanica. Ninguna depende de opinion.

**Mitad 1 — prueba de cobertura.** Por cada *table-stake* del tipo de entregable, existe un requerimiento explicito que la cubre. Si una table-stake aparecio en la implementacion sin requerimiento detras, entro por intuicion — y la proxima vez puede no entrar.

```txt
table-stake 1 → cubierta por RQ-XXX.n   [si/no]
table-stake 2 → cubierta por RQ-XXX.n   [si/no]
...
```

**Mitad 2 — prueba de justificacion.** Por cada decision tecnica, se escribe la linea:

```txt
esto existe porque el requerimiento X pide Y
```

La que no la tenga: o se declara como deuda con su motivo, o no se hace. La forma practica es una tabla de dos columnas — **lo que se hizo** (con su requerimiento) y **lo que deliberadamente no se hizo** (con el motivo). La segunda columna es la que suele faltar, y es la que demuestra que hubo criterio y no olvido.

---

## Senales de que se esta rompiendo

**Se rompe la mitad 1** cuando:

- hay que pedir el menu, la pausa o la condicion de victoria;
- la entrega "funciona" y no se puede jugar / usar de punta a punta;
- una table-stake aparece dentro de la implementacion sin requerimiento;
- se entrega lo minimo funcional y se llama minimo viable.

**Se rompe la mitad 2** cuando:

- hay decisiones tecnicas que no se pueden atar a ningun requerimiento;
- la justificacion de una decision es un principio ("es mas performante", "es mas SOLID") y no un pedido;
- la entrega es tecnicamente impecable y no responde lo que se queria;
- no existe la columna de *lo que deliberadamente no se hizo*.

---

## Limites

- **No define la lista de table-stakes.** Define que tiene que haber una, que tiene que estar escrita afuera y que se consulta antes de planificar. La lista por tipo es contenido de la Biblioteca, no del Core.
- **No prohibe optimizar.** Prohibe optimizar sin encargo. Si hay un requerimiento de rendimiento, optimizar es exactamente el trabajo.
- **No resuelve el conflicto entre las dos mitades.** Hay casos donde una table-stake exige maquinaria (una pelota que nunca atraviese una pared en un Pong exige continuidad de colision). Ahi la maquinaria **si** tiene requerimiento detras: la table-stake es el requerimiento. El conflicto es aparente.

---

## Regla final

```txt
Lo que el entregable necesita para ser lo que es: entra sin que lo pidan.
Lo que nadie pidio: no entra, o entra declarado como deuda con su motivo.
```

Todo lo demas es negociable. Estas dos no.

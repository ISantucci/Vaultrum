## Propósito

Esta sección reúne los principios de arte como **criterio** para construir, juzgar y pedir assets y animaciones.

No existe para enseñar a usar una herramienta: eso es operación, y vive en IA Operativa (`08_Operar el arte`).
No existe para dictar un estilo: la dirección de arte la trae el owner.
No existe para reemplazar los instrumentos del Área de Arte: las leyes se siguen midiendo con `arte.py` y `animacion.py`.

Existe para que ninguna decisión de oficio salga de la memoria de quien la toma. Cuántas poses lleva una caminata, qué curva va en un rebote, cuánto se estiliza un personaje sin que deje de ser él, de dónde sale una paleta: hasta esta sección, en Vaultrum eso lo contestaba el modelo de cabeza.

---

## Idea central

Cuatro preguntas distintas, cuatro lugares distintos:

```txt
¿esta EN LEY?            el Area de Arte, con instrumento     arte.py · animacion.py
¿esta BIEN HECHO?        esta seccion                          el criterio de oficio
¿cuanto CUESTA?          Optimizacion, rama Arte               el precio
¿como lo OPERA la IA?    IA Operativa, 08_Operar el arte       la herramienta y el pedido
```

Las dos primeras se confunden y no son la misma. Un goblin puede cerrar las seis leyes **EN LEY** y tener una silueta que no se distingue de la del orco que está al lado. Una caminata puede pasar `animacion.py` —lienzo, alfa, línea de apoyo, loop— y patinar, o leerse como carrera. La ley dice que el asset no está roto; el principio dice si sirve.

---

## Qué se mide y qué se juzga

El Área de Arte tiene una doctrina: **verificar por instrumento, nunca por ojo**. Esta sección no la afloja. Cada nota declara, para su principio, qué parte se puede medir y con qué, y qué parte queda como juicio:

```txt
se mide     lo que tiene un numero: volumen, escala de silueta, contraste de valor,
            cuadros entre input y respuesta, normales, islas, caras
se juzga    lo que no lo tiene: si la pose comunica, si es el mismo personaje,
            si el material se lee. Se escribe como juicio, nunca como medicion
```

Un juicio presentado como medición es el defecto que el área existe para evitar.

---

## Cómo debe usar esta sección una IA

Antes de construir, pedir o aprobar algo de arte:

```txt
¿Que estoy decidiendo: forma, movimiento, color, conjunto?
¿Que principio lo gobierna?
¿Lo dicto un insumo del proyecto (GDS, LDS, guia de estilo) o lo estoy eligiendo yo?
¿Que parte se puede medir antes de mirarla?
¿Que restriccion de juego le gana al principio? (el input, el collider, la camara)
```

La última pregunta es la que separa esta sección de un libro de animación de cine: en un juego hay un jugador con el control, un collider que no se deforma y una cámara que no elige el animador. Cada principio trae su **especificación para videojuegos**, y esa especificación le gana al principio cuando chocan.

---

## Cómo recorrer esta sección

```txt
1. Identificar que se esta decidiendo.
2. Entrar por la subseccion: objeto, modelado, animacion, color, personaje, conjunto.
3. Leer la nota puntual, no la seccion entera.
4. Medir lo medible antes de juzgar lo demas.
5. Declarar que se midio y que se juzgo.
```

---

## [[Objetos 3D]]

La anatomía del objeto: malla, normales, cierre, transform, origen y unidades.

Es lo que el contrato del asset del Área de Arte da por sabido. Usar cuando haga falta entender **por qué** una cara invertida, una malla abierta o una escala sin aplicar rompen algo que se ve bien.

---

## [[Modelado]]

La técnica de construir la malla: del bloqueo al detalle, la topología, la topología que tiene que deformarse, el low poly y la diferencia entre superficie dura y orgánica.

Usar antes de modelar un asset nuevo, o cuando una malla en ley se deforma mal o se sombrea raro.

---

## [[Principios de animacion]]

Los doce principios de Thomas y Johnston, cada uno con su **especificación para videojuegos**, y las curvas de interpolación con las que se ajustan.

Usar antes de animar, antes de escribir un encargo de animación y antes de aprobar lo que vuelve. Es la subsección que más le faltaba al área: el control de juego de cada principio vivía en una regla de uso (`RA-010`) sin fuente.

---

## [[Color]]

Valor antes que tono, la paleta cerrada, el color que distingue y el color en su contexto.

Usar al fijar la paleta de un proyecto, al sumar un material nuevo, y siempre que dos cosas que el jugador tiene que distinguir se parezcan.

---

## [[Diseno de personaje y forma]]

Silueta, lenguaje de formas, proporción y estilización, y la personalidad que está en el movimiento.

Usar al diseñar o corregir un personaje, una criatura o cualquier asset que el jugador tenga que reconocer de un vistazo.

---

## [[Direccion de arte]]

Los pilares visuales, la guía de estilo y la coherencia del conjunto.

Usar al abrir el arte de un proyecto —la mitad A del `ART`— y cada vez que un asset nuevo entra a un set que ya existe.

---

## Lo que no es de esta sección

```txt
el costo de un asset          Optimizacion, rama Arte
operar Blender, Unreal y      IA Operativa, 08_Operar el arte
los generadores
las leyes medidas y las       Area de Arte: Area_arte y sus reglas RA
reglas de uso
cuantas senales entran        UI/UX: el arte ejecuta ese presupuesto, no lo dicta
y por que canal
como se siente el juego       Biblioteca: 02_Game_feel
```

Se nombran, no se enlazan.

---

## Uso correcto dentro de Vaultrum

```txt
Decision de arte
→ principio relacionado
→ especificacion de juego
→ lo medible, medido
→ lo demas, juzgado y declarado como juicio
```

No es:

```txt
Me gusta como queda
→ lo apruebo
→ justifico el criterio despues
```

---

## Fuentes de la sección

Las fichas de la Biblioteca que sostienen estas notas: `59_The_Illusion_of_Life`, `60_The_Animators_Survival_Kit`, `61_Game_Anim`, `62_Color_and_Light`, `63_Interaction_of_Color`, `64_Creating_Characters_with_Personality`, `65_Digital_Modeling`, `67_Pixel_Logic`, `51_Understanding_Comics`, y la fuente propia `68_Apuntes_de_catedra_Animacion_2D_3D`.

Y el uso real que la hizo necesaria: las doce reglas `RA` del Área de Arte, que salieron todas de defectos medidos. Esta sección no las reemplaza: les da de dónde partir.

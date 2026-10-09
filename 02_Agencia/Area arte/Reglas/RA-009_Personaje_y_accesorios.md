# RA-009 — Personaje segmentado y accesorios apoyados

Sale del Goblin, primer cuerpo de enemigo. Lo anterior eran objetos: se apoyan
en el piso y no se mueven. Un personaje se anima, tiene ropa y lleva cosas en
la mano. Eso rompe tres supuestos de RA-002 a la vez.

## 1. El blueprint da formas; la pose la da la función

Un blueprint de personaje casi siempre viene en pose de presentación —
agachado, corriendo, apoyado en el arma. Horneada en la malla, esa pose es
inservible: el animador no saca un ciclo de caminata de ahí.

**Se modela en bind pose** (pose A, mirando +Y, origen entre los pies) y del
blueprint se toman las formas: proporción, silueta, orejas, nariz, ropa, arma.
Si el blueprint no tiene cotas, el tamaño lo dicta el rol en el juego medido
contra un asset ya construido, no el dibujo.

## 2. La ropa no es una capa: es un tramo

Una prenda modelada *encima* del cuerpo es interpenetración garantizada, y no
hay holgura que la salve sin que se vea flotando.

**La región vestida se modela una sola vez.** El pantalón *es* el muslo, con el
material del pantalón; la piel arranca en el dobladillo. El cambio de color cae
en un borde de objeto, que es justo donde el ojo espera una costura.

La excepción es lo que tiene que leerse *por encima* — un tirante que cruza en
X, un cinturón, una correa. Eso sí va como pieza aparte, y va apoyado (§4).

## 3. Junta con holgura de diseño, y la pieza ancha afuera

Un personaje segmentado no puede tener piezas que se toquen exactamente: al
riggear, cada segmento gira sobre su junta. Se deja **4 a 8 mm de holgura** en
cada junta, y **la pieza más ancha va del lado de afuera** (el dobladillo del
pantalón sobre la pantorrilla, la caña del zapato sobre el tobillo, la cabeza
sobre el cuello) para que la ranura quede tapada y nunca se lea como agujero.

Sobre 1.15 m, 6 mm es el 0.5 %: invisible desde la cámara del juego, y es lo
que permite animar sin abrir la malla.

## 4. Un accesorio se apoya MIDIENDO, no calculando

Tres intentos fallaron antes de esto, cada uno por una razón distinta:

- normal radial (z = 0): sobre un hombro que se cierra, empujar en horizontal
  no despega nada, desliza;
- normal real de la superficie: correcta en el centro de la cinta, pero el
  problema no es el centro sino **cada borde**;
- más holgura: una cinta rígida **no puede apoyarse sobre un quiebre**, lo
  puentea y clava el borde, y subir la holgura sólo la hace flotar.

Lo que funciona es medir. `apoyar()` tira, por cada vértice del accesorio, un
rayo desde el eje del cuerpo hacia afuera contra la **malla real**; si el
vértice quedó más adentro que el impacto, lo lleva al impacto más la holgura.
El cuerpo es estrellado respecto de su eje, así que el rayo da la respuesta
exacta. Es la misma idea que los 192 rayos de Roca_Aguja: no preguntarle a la
fórmula dónde está la superficie, preguntarle a la superficie.

Corolario de sección: con `n=4` un barrido da un **rombo**, y su arista interior
a −b es lo primero que toca. Una cinta tiene cara plana: sección
**rectangular**.

## 5. Dos slots de material antes que una pieza más

Una pupila, un pomo dorado, una suela: si lo único que cambia es el color y la
pieza ya está cerrada, se resuelve con **dos slots de material en la misma
malla**, asignando por posición o por hacia dónde mira la cara.

Cuesta cero caras, cero orígenes, cero juntas que verificar. Sólo se hace pieza
aparte cuando además cambia la forma o el objeto se tiene que mover solo.

## 6. Cuando la simetría rompe el instrumento

`relajar()` (RA-002) empuja sobre la recta que une los dos orígenes. Para un par
simétrico — dos orejas en una misma malla, una ceja sobre la línea media — ese
vector es degenerado y el empuje sale para cualquier lado.

Dos consecuencias: **las piezas simétricas van separadas en `_Der` / `_Izq`**
(que además es lo que pide RA-001), y cuando la dirección de separación la
dicta la función — una oreja sale del cráneo hacia afuera — se pasa explícita
(`separar_dirigido`) en vez de deducirla.

## 7. Lo que atraviesa una mano, se perfora

Un mango de daga no puede pasar por dentro de un puño macizo, y partirlo en dos
muñones a los costados se ve. Se perfora el puño con un boolean del diámetro del
mango más holgura y el mango pasa de verdad. El agujero no se ve porque está el
mango adentro, y RA-002 queda contenta.

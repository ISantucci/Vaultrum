## Propósito

Esta parte reúne los **principios de juego**: lo que todo desarrollo de Vaultrum cumple para que el juego *se juegue bien*, no sólo para que esté bien construido.

Es regla, no referencia. Cada principio se aplica en todo proyecto sin que el owner tenga que pedirlo, y dice qué área lo aplica, en qué paso de la cadena y cómo se juzga.

Vaultrum hace juegos en Unity, y estos principios están escritos para eso.

---

## Idea central

El Core sabía construir bien y no sabía qué se siente bien. Lo dice `Experiencia de juego`, y la respuesta fue indexar la Biblioteca: el conocimiento de experiencia quedó como referencia que se carga si alguien la busca. Funcionó cuando un libro de género lo empujaba y se perdió cuando no.

Esta parte es el paso siguiente: lo que la Escuela estudió y Conocimiento promovió, convertido en **criterio propio del Core**.

```txt
02_Contenido     ¿esta BIEN CONSTRUIDO?    codigo, arte, optimizacion, calidad
04_Principios    ¿se JUEGA BIEN?           lo que el jugador siente, dominio por dominio
Biblioteca       ¿COMO se hace, y por que? los numeros, los casos, el porque largo
```

Las dos primeras son regla. La tercera es el cómo, y se carga cuando hace falta.

---

## Cómo se ordena

Una sección por **dominio del juego**, en el orden de la cadena en que se decide: arriba lo que fijan Producción y Game Design, abajo lo que cierran Programación y Calidad. Una IA que recorre la cadena encuentra los principios en el orden en que los va a necesitar.

Todas las secciones tienen la misma forma: un índice con el porqué y quién aplica qué, y una nota por principio con su especificación en Unity y cómo se juzga.

Una sección nace cuando hay con qué escribirla: un estudio de la Biblioteca que la sostenga y la promoción de Conocimiento con aprobación del owner. No se abren secciones vacías.

---

## [[Principios de game feel]]

La sensación de manejar algo: que el juego conteste a tiempo, que lo que se mueve se pueda anticipar, que cada efecto diga algo y que nada sature.

Usar en todo `GDS` con interacción en tiempo real, antes de escribir el movimiento de cualquier cosa que el jugador maneje, y antes de dar por terminada una entrega que se juega. Es la primera sección porque atraviesa a todas las que vienen: entrada, cámara, audio, física y render son las piezas con las que se construye el feel.

---

## El mapa de la parte

Las secciones que esta parte va a tener, en el orden de la cadena, y de qué estudio de la Biblioteca saldría cada una. Hoy existe una.

```txt
dominio                    lo decide             sale de (Biblioteca)
alcance y planificacion    Produccion            17_Scope_prototipado_y_cierre
game feel                  Game Design           02_Game_feel                         escrita
entrada                    GD / Programacion     10_Input_y_respuesta
camara                     GD / Level Design     11_Camara_y_encuadre
audio                      GD / UI-UX            16_Audio_como_gameplay
fisica y colisiones        Programacion          01_Bucle_de_simulacion · 02_Colision_y_consulta_espacial
render y efectos           Arte / Programacion   sin estudio todavia
herramientas de editor     Programacion          04_Proyecto_editable_en_Unity
publicacion                Programacion / QA     sin estudio todavia (build y release)
```

**Cuando nazca una sección vecina**, puede que un principio de game feel le pertenezca —el perdón de input a Entrada, por ejemplo—. Si pasa, se muda con su `ARQ` y se nombra desde acá. No se escribe dos veces.

---

## Lo que ya vive en otra parte del Core

Varios dominios de un juego ya tienen su criterio en el Core y **no se mudan acá**. Moverlos rompería las historias que los nombran, y esta parte existe para completar el Core, no para reordenarlo.

```txt
arquitectura y sistemas     01_SOLID · 02_Patrones de diseno · 08_Managers
estructuras y algoritmos    06_Estructuras de datos · 07_Algoritmos
IA del juego                03_VaultrumAi
optimizacion                03_Optimizacion
pruebas                     09_Calidad y testing
arte                        11_Principios de arte
lo que hay que entregar     04_Criterios de entrega
```

Se nombran, no se enlazan.

---

## Relación con la Biblioteca

Esta parte **no es un puente**. El único puente del Core hacia la Biblioteca sigue siendo `Experiencia de juego` (Ley 5). Las notas de acá nombran los libros con backticks: el principio dice qué se exige; el libro, cómo se cumple y por qué.

Si un libro afina un número, el principio no se reescribe: remite al libro, que es el dueño del número.

---

## Regla de esta parte

```txt
un principio es regla       se aplica sin que nadie lo pida
un principio tiene dueno    dice que area lo aplica y en que paso de la cadena
un principio se juzga       dice que se mide y que se juzga, y no los confunde
```

Una nota de esta parte que no cumple las tres no es un principio: es una opinión con formato.

---
tipo: construccion
estado: En la Biblioteca
mision: EST-014_Mision_Matematica_del_movimiento
remite: 11_Camara_y_encuadre, 02_Game_feel, 10_Input_y_respuesta, 07_Economia_y_balance, 06_Dificultad_y_curva, Reglas de mapa
cruza: 01_Bucle_de_simulacion, 02_Colision_y_consulta_espacial
---

# Construcción 03 — Matemática del movimiento

> Tercer libro del estante. **El sustrato que los otros dos dan por sabido**: qué es un vector cuando se lo usa como intención, por qué el suavizado por frame produce una cámara distinta en cada máquina, qué elige uno cuando elige una curva de easing, y qué quiere decir realmente "aleatorio" cuando lo escribe un `GDS`.
> **No cubre:** cuánto tiempo dura un efecto (`02_Game_feel`), cuánto se suaviza una cámara (`11_Camara_y_encuadre`), cuánta latencia se tolera (`10_Input_y_respuesta`), ni qué probabilidad tiene que tener un drop (`07_Economia_y_balance`). Esos libros son dueños de los **valores**; este es dueño de las **funciones** sobre las que esos valores se aplican, y los remite.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Índice del libro

- Qué es y por qué se rompe si falta
- Vectores — la intención antes que el número
- Interpolación — el defecto más caro del estante
- Easing — la forma es una decisión de diseño
- Curvas — cuando la relación no es una fórmula
- Aleatoriedad — lo que se pide y lo que se quiere
- Baseline numérico
- Aplicación · Límites · Fuentes

---

## Qué es y por qué se rompe si falta

Tres libros del estante de Fundamentos legislan sobre esta matemática sin nombrarla:

```txt
11_Camara_y_encuadre   fija cuanto se suaviza una camara
02_Game_feel           fija las ventanas de tiempo de cada efecto
10_Input_y_respuesta   fija las curvas analogicas del stick
```

Los tres se apoyan en una interpolación que ningún libro define. Y no es que nadie lo haya visto: `11_Camara_y_encuadre` **ya nombra el defecto**, en una celda de tabla —

> *"Lerp por frame · `t` fijo · aceptable a 60 fps · depende del framerate: a 30 fps es otro juego"*

— y no tenía adónde mandar al lector. Nombrar un defecto sin poder remitir su mecanismo es el estado que este libro cierra. La medición del resto: `quaternion` una mención en todo el vault, `easing` siete veces sin dueño, `spline` ninguna. La Biblioteca legislaba sobre operaciones que no explicaba.

No es un problema estético. La sección de interpolación de este libro documenta un defecto que hace que **la misma línea de código produzca una cámara doscientas veces más lenta en una máquina que en otra**, sin error, sin warning y sin que nadie lo note hasta que lo prueba alguien con otro monitor.

---

## Vectores — la intención antes que el número

Un vector son dos cosas juntas: **una dirección y una magnitud**. Casi todos los bugs de transformación salen de olvidar que los mismos tres números pueden ser dos cosas distintas:

```txt
POSICION       un punto. "donde estoy". Sumar dos posiciones no significa nada.
DESPLAZAMIENTO una flecha. "cuanto me muevo". Sumarlo a una posicion si significa.
```

El compilador no distingue entre los dos y por eso el error no se detecta: se manifiesta como un objeto que aparece en el lugar equivocado.

### La diagonal — la relación que todo el mundo rompe una vez

Input de teclado: derecha `(1,0)`, arriba `(0,1)`, las dos `(1,1)`. La magnitud de `(1,1)` es √2 ≈ 1.41.

```txt
mover en diagonal es 41% mas rapido que mover en recto
```

Esto pasa en todo juego que suma teclas y no normaliza, y se presenta como *"conviene ir en zigzag"* — un exploit que nadie diseñó. La corrección es escribir la relación en vez del resultado:

```txt
velocidad = direccion_normalizada × rapidez
              ↑ QUE lado           ↑ CUANTO
```

Son dos decisiones distintas multiplicadas, no una sola escalada. Separarlas es lo que permite que la rapidez venga del `GDS` y la dirección del input sin que se contaminen.

### La trampa del vector cero

Normalizar `(0,0)` es dividir por cero. En punto flotante eso no revienta: da `NaN`. Y `NaN` es contagioso — se propaga a la posición, a la cámara, a todo lo que la toque — y **nunca vuelve a ser un número**:

```txt
NaN == NaN   →  false        ← ni siquiera es igual a si mismo
NaN < 0      →  false
NaN > 0      →  false        ← todo chequeo de rango lo deja pasar
```

Síntoma: el objeto desaparece y no vuelve, sin un solo error en consola. Causa: alguien soltó las teclas y el código normalizó la nada. Guardia: si la magnitud al cuadrado es cero, la dirección es la anterior o el vector cero, **nunca el resultado de la división**.

### El producto punto — para qué sirve, en tres usos

```txt
dot(A,B) = cuanto de A apunta en la direccion de B

1. ORIENTACION   dot(mi_frente, hacia_el_objetivo) > 0   → esta adelante
                 con ambos normalizados, el valor ES el coseno del angulo:
                 1 = de frente, 0 = a 90 grados, −1 = a la espalda.
                 Es el chequeo de cono de vision sin una sola llamada trigonometrica.

2. PROYECCION    descomponer un movimiento en "a lo largo de la pared" y "contra la
                 pared". Restarle la parte contra la pared es lo que produce el
                 deslizamiento en vez del frenazo. Es el complemento geometrico de
                 la resolucion por eje de `02_Colision_y_consulta_espacial`.

3. DISTANCIA     comparar distancias NUNCA necesita raiz cuadrada:
                    d² < r²   ⟺   d < r      (para valores no negativos)
                 Es una equivalencia exacta, no una aproximacion. La raiz solo hace
                 falta cuando el numero se muestra o se suma a otra distancia.
```

El tercero es una relación, no un truco de optimización: la raíz aparece cuando hace falta el **número**, no cuando hace falta la **comparación**. Escribirlo así evita la discusión de si "vale la pena optimizar" — no se está optimizando nada, se está evitando calcular algo que no se usa.

`Broad phase y narrow phase`, en el Core, ya lista *"distancia al cuadrado"* entre las aproximaciones baratas de la fase ancha, y `Costo cantidad y frecuencia` es dueño de cuándo eso importa como costo. Lo que aportan estas tres líneas y no está ahí es **por qué la equivalencia es exacta**: no es una aproximación que se acepta por barata, es el mismo resultado. Esa diferencia decide si se puede apoyar una regla de gameplay en ella.

---

## Interpolación — el defecto más caro del estante

`lerp(a, b, t)` devuelve el punto que está a la fracción `t` del camino de `a` a `b`. Con `t=0` da `a`, con `t=1` da `b`. Eso es todo, y no es donde está el problema.

El problema es este patrón, que es el más escrito de todo el código de cámara:

```txt
cada frame:   posicion = lerp(posicion, objetivo, 0.10)
```

Se lee como *"acercarse un 10% al objetivo"*. Lo que hace es **acercarse un 10% por frame**, y la cantidad de frames la decide la máquina.

### El diagrama, con sus invariantes

**Invariantes que este diagrama declara.** Se regeneró por script (`05_Escuela/Herramientas/diagrama_lerp.py`) verificándolas antes de escribirlo.

```txt
I1  ingenuo:  restante = (1−t)^n   con n = fps × segundos     → DEPENDE de fps
I2  correcto: restante = base^segundos                        → NO depende de fps
I3  las dos formas coinciden exactamente en el fps de calibracion
I4  restante ∈ (0,1] siempre: un suavizado se acerca, nunca sobrepasa
```

```txt
suavizado 'lerp(pos, objetivo, 0.10) por frame' — que queda despues de 0.5 s

  fps  frames    INGENUO restante   CORRECTO restante
   30      15              20.6%               4.2%
   60      30               4.2%               4.2%
  144      72               0.1%               4.2%
```

La misma línea de código: a 30 fps la cámara todavía está a un quinto del camino; a 144 fps ya llegó. **Doscientas veces de diferencia**, sin error y sin aviso. `11_Camara_y_encuadre` fija cuánto tiene que suavizar una cámara; con este patrón, ese número solo vale en la máquina donde se afinó.

### La forma correcta

```txt
t_dt = 1 − base^dt          base = la fraccion que queda despues de UN SEGUNDO
posicion = lerp(posicion, objetivo, t_dt)
```

La perilla deja de ser "cuánto por frame" —que no significa nada— y pasa a ser **"cuánto por segundo"**, que es una unidad que el `GDS` puede escribir y que se mantiene igual en toda máquina. La fila de 60 fps de la tabla es idéntica en las dos columnas porque es el fps en el que se calibró: la corrección no cambia el juego que se afinó, cambia todos los demás.

Y esa unidad es exactamente la que los libros de Fundamentos ya venían usando sin poder implementarla. `02_Game_feel` especifica la aceleración del avatar como *"llegar al 90% en 0.1–0.2 s"*: eso **es** un `base^dt` con `base = 0.10` y el tiempo declarado. La forma correcta no le agrega una perilla al diseño — es la que le permite escribir la que ya quería.

### La relación con el paso fijo — y por qué no lo arregla todo

Adentro de `simular(h)`, `dt` **es** `h` por definición (`01_Bucle_de_simulacion`), así que el lerp ingenuo pasa a ser correcto: los frames de simulación son siempre los mismos.

```txt
adentro de simular(h)     el lerp ingenuo es CORRECTO   ← h es constante
en render / presentacion  el lerp ingenuo es INCORRECTO ← corre al ritmo del display
```

Y la cámara es casi siempre código de presentación. Por eso el paso fijo, que resuelve tantas cosas, **no resuelve esta**: el suavizado de cámara vive del otro lado de la línea. Es la clase de defecto que sobrevive a hacer todo lo demás bien.

---

## Easing — la forma es una decisión de diseño

Una curva de easing reparte el mismo recorrido y la misma duración de otra manera. Elegirla no es estética: cambia qué se percibe.

```txt
LINEAL      velocidad constante. Se lee como mecanico. Sirve para barras de progreso
            y para nada que quiera parecer fisico.

EASE-OUT    arranca rapido, frena al final. Es el default de todo lo que el JUGADOR
            causo: la respuesta empieza de inmediato y despues se acomoda.

EASE-IN     arranca lento, acelera. Sirve para lo que se ANUNCIA: un ataque que se
            carga, una plataforma que empieza a moverse. Telegrafia.

EASE-IN-OUT arranca y termina suave. Camaras, transiciones de pantalla, todo lo que
            no quiere llamar la atencion sobre si mismo.
```

La relación que hay que escribir, porque es la que decide la sensación:

```txt
lo que se percibe como "responde" es el PRIMER 20% del recorrido, no la duracion total
```

De ahí sale la regla: **ease-in sobre una acción del jugador se siente roto aunque la duración sea corta**, porque los primeros milisegundos no pasa nada. Y al revés: un ease-out largo puede sentirse rápido, porque arranca de inmediato. Duración y curva son perillas separadas y la segunda pesa más en la percepción de respuesta.

Los **valores** —cuántos milisegundos dura cada efecto— son de `02_Game_feel` y `10_Input_y_respuesta`, que ya los legislan. Este libro no los toca: es dueño de la forma, y la remisión va en esa dirección.

**La frontera con las curvas de respuesta de `10_Input_y_respuesta`, porque son dos cosas con el mismo nombre:**

```txt
CURVA DE RESPUESTA   mapea una ENTRADA a una salida: cuanto vale el stick al 40%.
                     Es de `10_Input_y_respuesta`, que ya fija el exponente en 1.5-2.5.
EASING               mapea TIEMPO a progreso: donde esta el objeto a mitad de la animacion.
                     Es de este libro.
```

La confusión entre las dos produce el error que `10_Input_y_respuesta` ya prohíbe con todas las letras —*"nunca apliques lerp al input crudo para suavizar: eso se siente como patinar"*— y que es aplicar easing donde iba una curva de respuesta.

---

## Curvas — cuando la relación no es una fórmula

Una curva editable (`AnimationCurve` en Unity, o una tabla de puntos con interpolación) es la forma honesta de decir *"este número cambia con este otro"* cuando la relación no tiene fórmula.

```txt
tres constantes magicas en el codigo   =  una curva que nadie puede ver
una curva declarada                    =  la misma relacion, editable y graficable
```

Es la aplicación directa de la ley de este estante: **donde haya una relación, escribí la relación y no el resultado.** Tres valores elegidos a mano —daño a corta, media y larga distancia— son tres números que pueden dejar de cerrar entre sí sin que nadie se entere. La misma información como curva es una sola cosa que se mira de un vistazo.

Cuándo conviene cada una:

```txt
FORMULA   cuando la relacion se puede escribir y defender: velocidad × tiempo,
          costo que crece al cuadrado. Una formula se testea.
CURVA     cuando la relacion es "lo que se siente bien" y se afina probando.
          Una curva se juega.
TABLA     cuando los puntos son discretos y no interpolan: los niveles de un arma.
          Una tabla se lee.
```

El error frecuente es la tabla usada como curva: doce valores escritos a mano que deberían interpolar, y que en la práctica producen escalones que nadie diseñó.

---

## Aleatoriedad — lo que se pide y lo que se quiere

Cuando un `GDS` escribe *"10% de probabilidad de drop"*, casi nunca quiere decir lo que dice.

```txt
ALEATORIO UNIFORME  cada tirada es independiente. 10% real.
                    Consecuencia medible: en 10 intentos, un 35% de los jugadores
                    no ve NINGUN drop. Y algunos ven tres seguidos.
                    Se percibe como roto, no como aleatorio.

BOLSA (shuffle bag) se arma un mazo con la proporcion declarada y se reparte sin
                    reposicion. La frecuencia se cumple en la ventana; se pierde
                    la sorpresa de la racha.

CONTADOR DE PIEDAD  uniforme, pero la probabilidad sube con cada fallo hasta
                    garantizar. Es lo que la mayoria de la gente quiere decir
                    cuando escribe "10%".
```

La relación que hace falta declarar, y que casi nunca está:

```txt
probabilidad declarada  ↔  frecuencia observada  ↔  EN QUE VENTANA
```

Un 10% sin ventana no es una especificación: es un número suelto. "10% por tirada" y "uno cada diez" son diseños distintos y producen juegos distintos.

Los **valores** de probabilidad son de `07_Economia_y_balance`; el ajuste de dificultad según el resultado es de `06_Dificultad_y_curva`. Este libro es dueño del mecanismo y de la pregunta que hay que hacerle al `GDS`.

### Semilla

Un generador con semilla produce la misma secuencia siempre. Dos usos, y conviene no mezclarlos:

```txt
REPRODUCIBILIDAD  la corrida se puede repetir  → condicion 4 de `01_Bucle_de_simulacion`,
                  y la razon por la que el generador de la simulacion NO puede ser el
                  mismo que consumen las particulas
GENERACION        el mismo mundo desde el mismo numero → semilla como contenido
```

Dos generadores separados, uno para la simulación y otro para la presentación. Compartirlos produce el defecto de *"solo falla cuando están las partículas"*, que es indistinguible de un bug de física hasta que alguien mira el generador.

### Ruido

Ruido coherente (Perlin, value noise) no es aleatorio: es aleatorio **suavizado**, de modo que dos muestras cercanas dan valores cercanos.

```txt
random(x)   muestras vecinas: sin relacion   → estatica
ruido(x)    muestras vecinas: parecidas      → terreno, viento, variacion organica
```

Esa correlación entre vecinos es toda la diferencia y es la razón de que sirva para terreno y no sirva para un drop. La **aplicación** a generación de mapas tiene dueño y no es este libro: `Reglas de mapa` y `Diseño y aplicación de mapas` en `VaultrumAi`, con `52_Procedural_Content_Generation` como fuente.

---

## Baseline numérico

| Perilla | Arranque | La relación que la sostiene |
|---|---|---|
| dirección de input | siempre normalizada | `velocidad = dirección × rapidez` — dos decisiones, no una |
| normalizar `(0,0)` | guardia obligatoria | `NaN` pasa todo chequeo de rango; el objeto desaparece sin error |
| comparar distancias | `d² < r²` | equivalencia exacta; la raíz es para mostrar, no para comparar |
| suavizado | `1 − base^dt` | `base` = fracción restante tras **un segundo**. Nunca "un t por frame" |
| easing de una acción del jugador | ease-out | lo que se percibe como respuesta es el primer 20% del recorrido |
| tres constantes relacionadas | una curva | una relación se escribe como relación, no como sus resultados |
| "N% de probabilidad" | preguntar la ventana | un porcentaje sin ventana no es una especificación |
| generadores aleatorios | dos, separados | simulación y presentación no comparten secuencia |

---

## Aplicación

```txt
antes de escribir cualquier suavizado, seguimiento o camara    ← ahi vive el defecto caro
cuando el movimiento diagonal se siente mas rapido
cuando un objeto desaparece y no vuelve, sin error en consola  ← NaN
cuando el juego se siente distinto en otra maquina y el bucle ya es de paso fijo
cuando el GDS escribe un porcentaje                            ← preguntar la ventana
cuando hay tres constantes que solo tienen sentido juntas       ← es una curva
antes de apoyar cualquier regla en una comparacion de distancias
```

## Límites

```txt
NO fija duraciones de efectos ni ventanas de tiempo   → `02_Game_feel`, `10_Input_y_respuesta`
NO fija cuanto suaviza una camara ni su punto de mareo → `11_Camara_y_encuadre`
NO es dueño de las curvas de RESPUESTA (entrada→salida)  → `10_Input_y_respuesta`.
     Este libro es dueño del easing (tiempo→progreso). Mismo nombre, distinta funcion.
NO fija probabilidades ni economia de drops           → `07_Economia_y_balance`
NO fija ajuste de dificultad                          → `06_Dificultad_y_curva`
NO cubre generacion procedural de mapas               → `VaultrumAi`: `Reglas de mapa`
NO cubre matrices, espacios de coordenadas ni quaternions. Es 3D y hay dos proyectos
     que lo van a necesitar (`Pong3D`, `VaultrumWorld` isometrico), pero ninguno lo
     necesita HOY. Declarado como la proxima mision de este estante, no como omision.
NO cubre punto flotante en profundidad — solo la parte que muerde: NaN y el borde exacto.
```

## Fuentes

- Dunn, F. & Parberry, I. (2011). *3D Math Primer for Graphics and Game Development* (2ª ed.). A K Peters / CRC Press. Texto completo libre: https://gamemath.com/book/ — `48_3D_Math_Primer`. Vectores con interpretación geométrica antes que algebraica, y el producto punto como herramienta. Catalogada por `EST-009` sin destilar; esta misión es su destilación parcial: se tomó la parte 2D y de vectores, no matrices ni quaternions.
- Gregory, J. (2018). *Game Engine Architecture* (3ª ed.). CRC Press / A K Peters. — `46_Game_Engine_Architecture`. Interpolación en el ciclo del frame.
- Fiedler, G. *Fix Your Timestep!*. — `65_Fix_Your_Timestep`. Para la frontera entre lo que corre a paso fijo y lo que corre al ritmo del display.
- Togelius, J. et al. *Procedural Content Generation in Games*. — `52_Procedural_Content_Generation`. Ruido coherente y semilla como contenido; se remite, no se destila acá.

**Evidencia interna:** `11_Camara_y_encuadre` legisla smoothing y **ya nombraba este defecto en una celda de tabla** sin poder remitir su mecanismo; `02_Game_feel` especifica la aceleración del avatar en una forma que es un `base^dt` sin nombrarlo; `10_Input_y_respuesta` prohíbe el lerp sobre input crudo. Los tres eran correctos y ninguno tenía dónde apoyarse.

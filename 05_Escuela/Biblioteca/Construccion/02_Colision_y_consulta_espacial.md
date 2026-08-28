---
tipo: construccion
estado: En la Biblioteca
mision: EST-013_Mision_Colision_y_consulta_espacial
remite: Broad phase y narrow phase, Fisica costosa, Particionado espacial, Early Exit, IA que piensa de mas, Field of View
cruza: 01_Bucle_de_simulacion, 03_Matematica_del_movimiento, 01_Pong, 02_Plataformero_2D
---

# Construcción 02 — Colisión y consulta espacial

> Segundo libro del estante. **Tres preguntas geométricas distintas que el código suele confundir en una**: ¿se solapan ahora?, ¿se cruzaron entre dos instantes?, ¿qué hay en esta dirección? Cubre la resolución por eje, el barrido contra el tunneling, y el raycast como consulta — que veinticinco notas del vault usan y ninguna define.
> **No cubre:** el costo de la colisión ni cómo se diagnostica, que es del Core (`Física costosa`, `Broad phase y narrow phase`, `Particionado espacial`, `Early Exit`) y este libro lo **remite**. Tampoco el uso del raycast para percepción de NPC, que es de `Field of View` y `Detección del jugador` en `VaultrumAi`.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Índice del libro

- Qué es y por qué se rompe si falta
- Las tres preguntas
- El diagrama, con sus invariantes
- Las dos relaciones, y la que se remite
- Raycast — la consulta sin dueño
- Los modos de fallar
- Baseline numérico
- Aplicación · Límites · Fuentes

---

## Qué es y por qué se rompe si falta

`01_Pong` declara en su tabla de table-stakes que el fallo número uno de todo Pong apurado es el tunneling: *una pelota que atraviesa la paleta rompe el Pilar 5 — el jugador hizo bien y perdió igual*. La Biblioteca nombraba el fallo desde su primer libro y no tenía una sola pieza que dijera cómo se resuelve. `EST-009` catalogó la fuente que lo resuelve y la dejó sin destilar. Esta es esa destilación.

El defecto de fondo no es "falta detección de colisiones": los motores la traen. Es que hay **tres preguntas geométricas distintas**, con tres costos y tres modos de fallar distintos, y el código las trata como si fueran una.

---

## Las tres preguntas

```txt
1. SOLAPE      ¿estos dos cuerpos ocupan el mismo lugar AHORA?
               barato · falla cuando algo se mueve mas que su propio tamaño
               (esto es lo que hace un motor por default)

2. BARRIDO     ¿se cruzaron ENTRE la posicion anterior y esta?
               caro · es la pregunta correcta cuando hay velocidad
               devuelve un TIEMPO de impacto, no un booleano

3. CONSULTA    ¿que hay en esta direccion / en esta zona?
               raycast, shapecast, overlap. NO es colision: es una PREGUNTA
               que el codigo hace, no un evento que el mundo produce
```

La diferencia entre 1 y 2 es lo que decide el tunneling. La diferencia entre 3 y las otras dos es la que produce los bugs más difíciles de leer, porque una consulta que devuelve `false` es indistinguible de una consulta que nunca debió hacerse.

**El barrido devuelve un tiempo, y eso es lo que lo hace útil.** Un solape contesta *sí o no*; un barrido contesta *en qué fracción del paso*. Con esa fracción se puede poner el cuerpo exactamente en el punto de contacto en vez de un poco adentro, que es la diferencia entre un rebote correcto y uno que empieza con el objeto medio metido en la pared.

---

## El diagrama, con sus invariantes

**Invariantes que este diagrama declara.** Se regeneró por script (`05_Escuela/Herramientas/diagrama_barrido.py`) verificándolas antes de escribirlo.

```txt
I1  el objeto avanza exactamente v×h por paso en LOS DOS casos
    (el barrido no lo hace ir mas lento: mira mejor, no distinto)
I2  el discreto mira las POSICIONES de los pasos; el barrido mira el SEGMENTO entre ellas
I3  hay tunneling si y solo si  v×h > espesor  Y ninguna posicion de paso cae adentro
I4  el tiempo de impacto t ∈ [0,1) es una fraccion del PASO, no del frame
```

```txt
h = 16.7 ms    v = 720 px/s    →   v×h = 12.0 px por paso
pared en x=100, espesor 4 px   →   [100 .. 104]

posiciones de paso:  94.0 ──→ 106.0 ──→ 118.0
                              ninguna cae en [100..104]

SOLAPE     [O]          |‖|          [O]
           94          100 104        106
           ¿se solapan ahora? no.  ¿y ahora? no.        → TUNNELING

BARRIDO    [O]===================>[O]
           94        ^            106
                   t=0.50                               → impacto en x=100.0
```

La condición `I3` se lee entera: **no alcanza con que `v×h` supere el espesor**. Si una posición de paso cae adentro de la pared, el solape la encuentra igual. Por eso el tunneling es intermitente — depende de dónde caiga la grilla de pasos respecto de la pared — y por eso es de los defectos que "solo pasan a veces" y no se reproducen. El paso fijo de `01_Bucle_de_simulacion` es lo que los vuelve reproducibles.

---

## Las dos relaciones, y la que se remite

### R1 · cuándo hace falta barrer — remitida, no re-legislada

La relación `v_max × h` contra el espesor mínimo **es del libro `01_Bucle_de_simulacion` (R2)**, porque es una restricción sobre el bucle. Este libro no la reescribe: es dueño de **qué se hace cuando no se cumple**, que es lo que aquel deja abierto.

```txt
v_max × h < espesor_minimo     → alcanza el solape. No agregues barrido: es costo sin beneficio.
v_max × h ≥ espesor_minimo     → tres remedios, en orden de menor a mayor costo:

  a. bajar h                     ← barato, y cambia las ventanas del GDS. Rara vez es la opcion.
  b. engrosar el collider fino   ← barato, invisible, y miente sobre la geometria.
                                    Sirve para paredes de escenario, no para lo que el jugador mira.
  c. barrer                      ← correcto y caro. Es el unico que no depende de que nadie
                                    suba la velocidad despues.
```

El error a no cometer: subir el **techo de pasos** creyendo que ayuda. El techo cambia cuántos pasos entran en un frame; el tunneling ocurre *dentro* de un paso. No se tocan.

El Core ya nombra la otra mitad de esto desde el lado del costo, y conviene leerlo junto: `Física costosa` da como ejemplo de mala solución *"physics caro → timestep al doble → menos costo, pero proyectiles que atraviesan enemigos"*, y cierra con **"un juego más rápido que se rompe no está optimizado"**. Este libro dice por qué pasa; esa nota dice por qué no se hace.

### R2 · el eje que se resuelve primero decide el comportamiento en las esquinas

Resolver las dos direcciones a la vez —empujar el cuerpo por el vector de penetración mínima— produce un defecto característico: un personaje que corre sobre un piso hecho de tiles **se engancha en las juntas**. En el borde entre dos tiles la penetración vertical y la horizontal empatan, el desempate cae para el lado equivocado, y el cuerpo se frena contra una pared que no existe.

El remedio es resolver **por eje, en dos pasadas**:

```txt
mover en X  →  resolver X  →  mover en Y  →  resolver Y
```

Y la relación que hay que escribir, porque es una decisión de diseño disfrazada de detalle de implementación:

```txt
el eje que se resuelve ULTIMO es el que GANA el empate
  Y ultimo  →  aterrizar gana:   el personaje se para sobre la esquina
  X ultimo  →  la pared gana:    el personaje resbala hacia abajo por la esquina
```

Las dos son legítimas y producen juegos distintos. Un plataformero de precisión quiere que aterrizar gane, porque el jugador apunta a plataformas. Elegirlo sin saber que se está eligiendo es lo que produce el clásico *"a veces me subo al borde y a veces no"*.

El *corner correction* que `02_Plataformero_2D` declara como table-stake es una capa **encima** de esto: primero la resolución tiene que ser predecible, después se le perdona al jugador el píxel que le faltó.

### La fase ancha — territorio del Core, remitido

Acá había una tercera relación en el borrador y **no le corresponde a este libro**. `Broad phase y narrow phase`, en el Core, ya es dueño de la asimetría completa y la escribe mejor de lo que este libro la escribiría:

> *"La broad phase no necesita tener razón. Necesita no perder candidatos válidos."*
> *"→ puede dejar pasar falsos positivos · → nunca debería descartar un verdadero positivo"*

Esa nota además declara que el patrón no pertenece a la colisión: aparece igual en física, IA, targeting, consultas espaciales y rendering. Escribir acá una versión propia habría producido dos notas que dicen lo mismo con distintas palabras y que se pueden desincronizar — que es exactamente el defecto que el lote `EST-006` pagó cuando cuatro libros legislaron encima del territorio de `13`.

**Lo que este libro sí aporta al tema**, y es una línea: el modo de fallar geométrico. Un volumen envolvente **envuelve** — una caja que contiene al objeto puede sobrar, nunca faltar. Ajustarla hasta que quede pegada al modelo, "para optimizar", invierte la asimetría del Core y produce colisiones que faltan de vez en cuando: falsos negativos raros, que se archivan como *no se pudo reproducir*.

## Raycast — la consulta sin dueño

`raycast` aparece en veinticinco notas del vault: en optimización como costo, en `VaultrumAi` como percepción, en los presets de NPC como herramienta. Ninguna responde por él. Lo que sigue es lo mínimo que hace falta para usarlo sin sorpresas.

**Un rayo es una muestra unidimensional de un mundo que no lo es.** Su punto ciego es todo lo que no está sobre la línea. Ese es el modelo mental correcto y de él salen casi todos los modos de fallar.

```txt
1. ORIGEN ADENTRO      un rayo que empieza dentro de un collider puede no reportarlo.
                       Depende del motor y de la configuración, y cambia entre versiones.
                       Sintoma: "funciona salvo cuando estoy pegado a la pared".

2. EL PERSONAJE NO ES UN RAYO   un rayo tiene largo y no tiene ancho. Chequear el piso
                       con un rayo desde el centro deja los dos bordes del personaje sin
                       muestrear: se cae por un agujero de un pixel, o queda flotando en
                       un borde. Lo que hace falta es un shapecast, o varios rayos con su
                       separacion DECLARADA contra el ancho del personaje.

3. LA MASCARA OLVIDADA un rayo sin capa declarada choca con todo, incluido el propio
                       cuerpo que lo dispara. Es el bug de percepcion mas comun y se
                       presenta como "el NPC se ve a si mismo".

4. PRIMERO CONTRA TODOS  pedir el primer impacto y pedir todos cuestan distinto, y en
                       varios motores la lista de "todos" NO viene ordenada por distancia.
                       Ordenarla es del que llama.

5. LARGO INFINITO      un rayo sin tope paga la escena entera. `Early Exit` en el Core es
                       dueño del criterio de por que eso importa; acá basta con que el
                       largo del rayo sea SIEMPRE una decision escrita, no un default.

6. EL BORDE EXACTO     un rayo que roza una arista es el caso donde el punto flotante
                       decide. No se resuelve con mas precision: se resuelve no apoyando
                       ninguna regla de juego en un rozamiento exacto.
```

La relación que conviene escribir, porque es la que se olvida:

```txt
cantidad de rayos × separacion  ≥  ancho del cuerpo que se esta muestreando
```

Tres rayos para chequear el piso de un personaje de 32 px no son "tres rayos": son un muestreo cada 16 px, y todo lo más fino que eso es invisible. Si el nivel tiene plataformas de 8 px, el número de rayos no alcanza y no hay forma de enterarse mirando el código.

El uso de rayos para **percepción de NPC** —conos de visión, líneas de vista, detección— tiene dueño y no es este libro: `Field of View` y `Detección del jugador` en `VaultrumAi`. Su costo tiene otro: `IA que piensa de más`.

---

## Los modos de fallar

| # | Falla | Síntoma | Qué se confundió |
|---|---|---|---|
| 1 | **Solape donde hacía falta barrido** | el objeto atraviesa; intermitente, no se reproduce | pregunta 1 por pregunta 2 |
| 2 | **Barrido donde alcanzaba el solape** | costo sin beneficio; `v×h` nunca llegó al espesor | R1 sin medir |
| 3 | **Resolución simultánea de ejes** | el personaje se engancha en las juntas del piso | R2 sin elegir |
| 4 | **Empate de esquina sin declarar** | "a veces me subo al borde y a veces no" | R2 elegido por accidente |
| 5 | **Rayo por cuerpo** | se cae por agujeros de un píxel, o flota en los bordes | pregunta 3 por pregunta 1 |
| 6 | **Envolvente ajustada de más** | colisiones que faltan, muy de vez en cuando | la asimetría del Core (`Broad phase y narrow phase`) invertida |

El modo 6 es el peor de la tabla y el que menos se investiga: produce **falsos negativos raros**, y un falso negativo raro se archiva como "no se pudo reproducir". Su criterio vive en el Core; acá está solo su forma geométrica.

---

## Baseline numérico

| Perilla | Arranque | La relación que la sostiene |
|---|---|---|
| solape / barrido | según | **R1**: `v_max × h` contra el espesor mínimo. La relación es de `01_Bucle_de_simulacion`; el remedio es de acá |
| orden de ejes | Y último | **R2**: el último gana el empate. "Aterrizar gana" es el default sano para plataformas — pero es una decisión de diseño y se declara |
| rayos de piso | ≥ 2, en los bordes | **la relación del raycast**: `cantidad × separación ≥ ancho del cuerpo`, contra el elemento más fino del nivel |
| largo del rayo | siempre finito y escrito | nunca un default; el largo es parte de la pregunta |
| máscara de capas | siempre explícita | un rayo sin máscara se ve a sí mismo |
| envolvente | conservadora, nunca ajustada | la asimetría es del Core: falsos positivos sí, falsos negativos jamás |

---

## Aplicación

```txt
antes de elegir motor de fisica contra cinematica propia
cuando un objeto rapido tiene que golpear algo fino          ← Pong, disparos, caidas largas
cuando el personaje se engancha, flota o se cae por juntas
antes de escribir el primer raycast de un SOL
cuando un defecto de colision "no se reproduce"              ← casi siempre es I3
```

## Límites

```txt
NO es dueño del costo ni del diagnostico          → Core: `Broad phase y narrow phase`,
     `Particionado espacial`, `Early Exit`, `Fisica costosa`
NO es dueño del raycast como percepcion de NPC    → `Field of View`, `Deteccion del jugador`
NO es dueño de la relacion v×h                     → `01_Bucle_de_simulacion` (R2)
NO cubre vectores, normalizacion ni proyeccion     → `03_Matematica_del_movimiento`
NO cubre fisica con restricciones: joints, pilas de cuerpos, friccion resuelta por impulsos.
     Es otro territorio y no tiene consumidor en Vaultrum hoy.
NO cubre colision en 3D contra malla arbitraria    → el motor la resuelve; lo que no
     resuelve es que se le pregunte lo que no corresponde, que es de lo que trata este libro.
```

## Fuentes

- Ericson, C. (2004). *Real-Time Collision Detection*. Morgan Kaufmann / Elsevier. — `54_Real_Time_Collision_Detection`. La distinción discreta/continua, el tunneling, y la asimetría de la fase ancha. Catalogada por `EST-009` sin destilar; esta misión es su destilación.
- Gregory, J. (2018). *Game Engine Architecture* (3ª ed.). CRC Press / A K Peters. — `46_Game_Engine_Architecture`. El subsistema de colisión y su lugar en el frame.
- Fiedler, G. *Fix Your Timestep!*. — `65_Fix_Your_Timestep`. Para el lado del bucle de la relación R1.

**Evidencia interna:** `01_Pong` nombra el tunneling como su fallo número uno desde el primer libro del estante de Juegos. `SOL-001_Arquitectura_Salto` eligió "colisión por eje, con barrido" y midió el desplazamiento por paso en 3.2 px. Este libro escribe por qué esas dos decisiones son la misma decisión.

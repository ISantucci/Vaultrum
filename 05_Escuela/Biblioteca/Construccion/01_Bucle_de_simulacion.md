---
tipo: construccion
estado: En la Biblioteca
mision: EST-012_Mision_Bucle_de_simulacion
remite: Game loop, Frame Budget, Frame time y estabilidad, 10_Input_y_respuesta, Calidad y testing
cruza: 02_Colision_y_consulta_espacial, 03_Matematica_del_movimiento
---

# Construcción 01 — Bucle de simulación

> Primer libro del estante. **El bucle como contrato de simulación**: por qué el paso es fijo, qué relación amarra el tamaño del paso con las ventanas del `GDS`, de dónde sale el techo de pasos y qué es exactamente lo que se interpola al renderizar.
> **No cubre:** el presupuesto de frame ni el diagnóstico de costo — eso es del Core (`Game loop`, `Frame Budget`, `Frame time y estabilidad`) y este libro lo **remite**, no lo re-legisla. Tampoco cubre la cadena de latencia completa, que es de `10_Input_y_respuesta`: acá solo se aporta un eslabón.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

---

## Índice del libro

- Qué es y por qué se rompe si falta
- El modelo — los tres relojes
- Las cuatro relaciones
- El diagrama, con sus invariantes
- Los cuatro modos de fallar
- Determinismo — hasta dónde llega
- Baseline numérico
- Aplicación · Límites · Fuentes

---

## Qué es y por qué se rompe si falta

El bucle es el lugar donde el juego decide **cuánto tiempo avanzó el mundo**. Parece una decisión de rendimiento y no lo es: es la decisión de la que dependen todos los números que el diseño escribió.

El bucle ingenuo mide cuánto tardó el frame anterior y avanza el mundo esa cantidad:

```txt
mientras corre:
    dt = ahora - antes
    simular(dt)          ← el mundo avanza lo que tardó la máquina
    renderizar()
```

Funciona hasta que alguien escribe una especificación. `GDS-001.2` de Salto declara el coyote time en **frames**. En un bucle de paso variable, "6 frames" mide 100 ms en una máquina a 60 fps y 200 ms en una a 30 fps: la misma especificación, dos juegos distintos, y ninguno de los dos es el que se diseñó. El bug no está en el salto — está en que el mundo avanza a la velocidad de la máquina.

**Lo que fuerza el paso fijo no es el rendimiento: es que el diseño escribe ventanas.** Ese es el orden causal y conviene tenerlo derecho, porque el error habitual es adoptar paso fijo "porque es lo correcto" y no poder explicar qué se rompería sin él.

---

## El modelo — los tres relojes

Hay tres relojes y no marchan juntos. Casi todo defecto de bucle es confundir dos de ellos.

```txt
RELOJ REAL           el que corre afuera. Irregular: el sistema operativo, la
                     pestaña que se congela, el disco. No se controla.
RELOJ DE SIMULACION  avanza en pasos discretos de tamaño FIJO h, y solo cuando
                     el bucle decide. Es el reloj del que habla el GDS.
RELOJ DE PRESENTACION cuando el display puede mostrar algo. Ni coincide con h
                     ni hace falta que coincida.
```

El bucle de paso fijo es el traductor entre los tres: absorbe la irregularidad del reloj real en un **acumulador**, gasta ese acumulador en pasos exactos de `h`, y le entrega al render lo que sobró como una fracción.

```txt
acumulador += dt_real
pasos = 0
mientras acumulador >= h  y  pasos < TECHO:
    simular(h)                   ← siempre h. Nunca dt.
    acumulador -= h
    pasos += 1

alpha = acumulador / h           ← lo que sobró, en fracciones de paso
render(interpolar(estado_previo, estado_actual, alpha))
```

Tres propiedades que salen de esas seis líneas y conviene nombrar:

- `simular(h)` no recibe nunca el tiempo real. La simulación no sabe qué máquina la corre, y esa ignorancia es la feature.
- El acumulador **no se descarta**: lo que sobra de un frame se paga en el siguiente. Sin eso el reloj de simulación se atrasaría un poco cada frame.
- El render no dibuja el estado de la simulación: dibuja un estado **intermedio** que nunca existió. Es correcto, y es lo que la sección de latencia matiza.

---

## Las cuatro relaciones

Este es el cuerpo del libro. Cada perilla del bucle está amarrada a otra por una relación, y **el número suelto es el defecto**: dos valores elegidos por separado, cada uno defendible, que no cierran entre sí.

### R1 · el paso amarra las ventanas del diseño

```txt
ventana_en_segundos = frames_declarados × h
```

Si el `GDS` declara una tolerancia en frames, `h` deja de ser una preferencia de implementación: es lo que le da significado a esa tolerancia. Y la flecha va al revés de lo que parece — **el `GDS` elige `h`, no la Programación**:

```txt
h ≤ ventana_mas_chica_del_GDS / frames_declarados
```

Una ventana de 6 frames que el diseño quiere de 100 ms fija `h ≤ 16.7 ms`. Si más adelante alguien sube `h` a 1/30 para ganar presupuesto, no está optimizando: está cambiando el coyote time a 200 ms sin decírselo a Game Design.

### R2 · el paso amarra la velocidad máxima con el objeto más chico

```txt
desplazamiento_por_paso = v_max × h
```

La colisión discreta pregunta si dos cosas se solapan **ahora**. Si en un paso el objeto avanza más que el espesor de lo que tiene que golpear, pasa de un lado al otro sin haberse solapado nunca. Eso es *tunneling*.

```txt
v_max × h  <  espesor_minimo        ← se puede muestrear discreto
v_max × h  >= espesor_minimo        ← hace falta barrido
```

Tres números que solo cierran juntos: elegí dos y el tercero queda determinado. Salto avanza 3.2 px por paso a velocidad terminal, y eso no es un dato del bucle: es `v_max × h` evaluado, y su comparación contra el tile más fino es la que decidió que hubiera barrido. El mecanismo del barrido es del libro `02_Colision_y_consulta_espacial`; acá vive la relación que obliga a usarlo.

**Y la relación no se arregla subiendo el techo de pasos.** El techo cambia cuántos pasos entran en un frame; no cambia cuánto avanza el objeto *dentro de un paso*, que es lo único que causa el tunneling.

### R3 · el techo sale del presupuesto de frame, no de la intuición

Si un paso de simulación cuesta más de `h` de tiempo real, el acumulador crece cada frame, lo que pide más pasos, lo que cuesta más. Es realimentación positiva y tiene nombre: **espiral de la muerte**. El juego no baja de fps: se cuelga.

El techo la corta dejando que el reloj de simulación **se atrase** en vez de intentar alcanzarlo. El juego entra en cámara lenta, que es un mal resultado y es infinitamente mejor que un cuelgue.

```txt
TECHO ≤ presupuesto_de_frame / costo_medido_de_un_paso
```

El techo no es un número mágico: es una división, y el numerador es del Core. `Frame Budget` es dueño del presupuesto y `Frame time y estabilidad` de cómo se mide; este libro los **remite** y no los reescribe. Lo único que agrega es el denominador — hay que medir cuánto sale **un paso**, no un frame entero, y son cosas distintas en cuanto el techo es mayor que 1.

Leído al derecho: un techo de 5 a 60 Hz dice *"puedo recuperar hasta 83 ms de atraso en un frame"*, que es lo que hace falta para sobrevivir a una pestaña congelada corta sin entrar en cámara lenta.

### R4 · la interpolación amarra suavidad con latencia

Renderizar entre el estado previo y el actual elimina el judder y **cuesta latencia**: lo que se ve está entre 0 y `h` atrás de la simulación, `h/2` en promedio.

```txt
latencia_de_presentacion ∈ [0, h]     por interpolar
```

La alternativa es extrapolar —predecir hacia adelante— que va sin atraso y se equivoca justo donde más se nota: predice a través de una pared y después corrige de un salto.

**Este libro aporta un eslabón, no el presupuesto.** La cadena de latencia completa es territorio de `10_Input_y_respuesta`, que la desglosa en siete tramos y fija el tope en **≤65 ms, ideal ≤50**. Si el eslabón de `h/2` no entra en ese tope, la decisión es de ese libro, no de este.

**Y el eslabón hoy no está en esa cadena.** El tramo *RENDER + PRESENTACIÓN* de `10_Input_y_respuesta` cuenta cola de GPU, VSync y triple buffer — todo lo que pasa **después** de que el frame se arma. La interpolación cuesta antes: entre elegir qué estado dibujar y armarlo.

```txt
LOGICA DE JUEGO
   │  0–h       ← este eslabon. Con h=16.7 ms: 0–16.7, promedio 8.3
   ▼              lo paga QUIEN INTERPOLA, y es un tramo que el dev controla
RENDER + PRESENTACION      ← acá empieza lo que la cadena ya contaba
```

No es un error de aquel libro: es un tramo que aparece recién cuando el bucle es de paso fijo con interpolación, que es lo que este libro trae. Lo que corresponde es **declararlo y devolverlo**: si el proyecto interpola, la cadena de `10_Input_y_respuesta` tiene ocho tramos y no siete, y **si los 8.3 ms de promedio entran en su tope de 65 lo decide ese libro**. Extrapolar es la palanca que lo saca, al precio de corregir de un salto en las colisiones.

---

## El diagrama, con sus invariantes

**Invariantes que este diagrama declara.** Un diagrama sin invariantes escritas solo se puede mirar; con ellas se puede verificar, y este se regeneró por script (`05_Escuela/Herramientas/diagrama_bucle.py`) comprobándolas antes de escribirlo.

```txt
I1  todo paso de simulacion mide exactamente h — nunca dt
I2  pasos_en_el_frame <= TECHO
I3  al salir del while el resto es < h ... salvo que el techo haya cortado
I4  alpha ∈ [0,1) ... con la misma salvedad
```

```txt
h = 16.7 ms   techo = 5 pasos

 dt real  pasos   resto  alpha   estado
    27ms      1    10.3   0.62   al dia
    12ms      1     5.7   0.34   al dia
    41ms      2    13.3   0.80   al dia
     9ms      1     5.7   0.34   al dia
   210ms      5   132.3   7.94   TECHO — la simulacion se atrasa
```

La última fila es la que enseña algo, y salió de verificar los invariantes en vez de mirarlos: **cuando el techo corta, `I3` e `I4` dejan de valer**. El resto queda en 132 ms y `alpha` da 7.94. Un render que interpola con ese alpha proyecta el objeto ocho pasos hacia adelante y produce un salto visible en el peor momento posible — justo cuando el juego ya está en apuros.

```txt
alpha = min(acumulador / h, 1.0)     ← el clamp no es defensivo: es I4 sostenido a mano
                                        cuando el techo se lo lleva por delante
```

---

## Los cuatro modos de fallar

| # | Falla | Síntoma | Qué relación se violó |
|---|---|---|---|
| 1 | **Paso variable** | el juego se siente distinto en cada máquina; las ventanas del `GDS` no significan nada | R1 — no hay `h` que le dé significado a un frame |
| 2 | **Sin techo** | el juego se cuelga en vez de bajar de fps, y se cuelga **más** cuanto más tarda | R3 — realimentación positiva sin corte |
| 3 | **Techo mudo** | el juego entra en cámara lenta y nadie sabe por qué; el defecto es irreproducible | R3 — el corte existe y no es observable |
| 4 | **Paso fijo sin interpolar** | judder: simulación a 60 Hz sobre un display de 144 Hz repite frames de forma despareja | R4 — se resolvió el reloj de simulación y se ignoró el de presentación |

El modo 3 es el caro y el que menos se ve venir. Un techo que se activa en silencio convierte un problema de rendimiento en un problema de *comportamiento*: el jugador reporta "el salto se sintió raro", QA no lo reproduce, y nadie relaciona las dos cosas. **El techo tiene que contarse**: un contador de veces que cortó y de cuánto atraso acumulado es la diferencia entre un defecto diagnosticable y uno que se discute. El criterio de por qué eso importa es de `Calidad y testing` en el Core, que pide defectos reproducibles; acá está el mecanismo que los hace reproducibles.

---

## Determinismo — hasta dónde llega

El paso fijo es **necesario y no suficiente** para que una corrida se reproduzca. La lista completa, y ninguna de las cinco es opcional:

```txt
1. h fijo                    ← el paso fijo, que es lo que este libro trae
2. input indexado al PASO    la entrada se registra contra el numero de paso,
                             nunca contra el reloj real
3. cero lecturas del reloj real adentro de la simulacion
4. PRNG con semilla, avanzado SOLO adentro de la simulacion
                             (si el render consume numeros del mismo generador,
                              la corrida deja de reproducirse y el sintoma es
                              que "solo falla cuando estan las particulas")
5. cero dependencia del orden de iteracion no determinista
                             (recorrer un diccionario, punteros como clave)
```

**El límite, declarado:** con esas cinco condiciones una corrida se reproduce **en la misma máquina y el mismo binario**. El determinismo bit a bit *entre plataformas distintas* es otro problema —punto flotante, orden de operaciones del compilador, funciones trascendentes— y es una disciplina aparte que este libro no cubre. Se nombra el límite porque la confusión entre las dos cosas es lo que hace que alguien prometa replays portables y entregue replays que se desincronizan.

Lo que sí se desbloquea con el determinismo de una máquina, que es mucho: **el defecto reproducible**. Un log de entradas más una semilla es un caso de prueba completo, y convierte "no me pasa a mí" en un archivo.

---

## Baseline numérico

Ningún número de esta tabla se sostiene solo. La columna de la derecha es el libro.

| Perilla | Arranque | De dónde sale — la relación |
|---|---|---|
| `h` (paso) | 1/60 s (16.7 ms) | **R1**: `h ≤ ventana_más_chica_del_GDS / frames_declarados`. Lo elige el diseño, no la implementación |
| `TECHO` | 5 pasos | **R3**: `presupuesto_de_frame / costo_medido_de_un_paso`. Medir el paso, no el frame. Numerador del Core |
| barrido sí/no | según | **R2**: `v_max × h` contra el espesor mínimo. No se arregla con el techo |
| `alpha` | `min(acum/h, 1)` | **R4**: es una consecuencia, no una perilla. El clamp sostiene `I4` cuando el techo corta |
| contador de cortes | obligatorio | modo de falla 3: un techo que no se cuenta convierte rendimiento en comportamiento |

Cambiar `h` **nunca es un cambio de implementación**: es un cambio de las ventanas del `GDS`, y vuelve a Game Design.

---

## Aplicación

Cuándo la IA trae este libro por default:

```txt
al escribir cualquier SOL que simule algo que se mueva
cuando el GDS declara una tolerancia en frames  ← ahí el paso fijo deja de ser opcional
cuando un defecto solo aparece en una maquina, o solo a veces
antes de elegir motor de fisica contra cinematica propia  (la eleccion es del libro 02
   y del libro de genero; la consecuencia sobre el bucle es de acá)
al preparar un caso de prueba que QA tenga que reproducir
```

## Límites

```txt
NO es dueño del presupuesto de frame ni del diagnostico de costo   → Core: `Game loop`,
     `Frame Budget`, `Frame time y estabilidad`, `Fisica costosa`
NO es dueño de la cadena de latencia ni de su tope (≤65 ms)        → `10_Input_y_respuesta`.
     Este libro le APORTA un tramo que hoy no cuenta —la interpolación, 0–h antes del
     render— y le devuelve la decisión de si entra en el presupuesto.
NO cubre el barrido ni la resolucion de colision                   → `02_Colision_y_consulta_espacial`
NO cubre la interpolacion como funcion (lerp, easing)              → `03_Matematica_del_movimiento`
NO cubre determinismo bit a bit entre plataformas
NO aplica a lo que no simula estado: menus, herramientas de editor, juegos por turnos
     sin tiempo real. Un juego por turnos no necesita paso fijo — necesita que sus
     animaciones no decidan reglas.
```

## Fuentes

Las tres primeras ya estaban en la Biblioteca, catalogadas y sin destilar. Esta misión es su destilación.

- Gregory, J. (2018). *Game Engine Architecture* (3ª ed.). CRC Press / A K Peters. — `46_Game_Engine_Architecture`. Ciclo de vida del frame y la capa de gameplay; el marco de los tres relojes.
- Nystrom, R. *Game Programming Patterns*, capítulo «Game Loop». — `42_Game_Programming_Patterns_Robert_Nystrom` en Documentación real. Texto completo libre publicado por el autor. El acumulador y la separación simulación/render.
- Ericson, C. (2004). *Real-Time Collision Detection*. Morgan Kaufmann. — `54_Real_Time_Collision_Detection`. La distinción discreta/continua que sostiene **R2**.
- Fiedler, G. «Fix Your Timestep!». gafferongames.com. — `65_Fix_Your_Timestep` en Documentación real. El artículo canónico del acumulador con interpolación.

**Evidencia interna** (no es fuente externa, es el caso que disparó la misión): `SOL-001_Arquitectura_Salto` decidió paso fijo a 60 Hz con acumulador, render interpolado y techo de 5 pasos, y declaró correctamente el porqué de cada uno. Este libro escribe las relaciones que ahí quedaron implícitas, para que la próxima vez no haya que redescubrirlas.

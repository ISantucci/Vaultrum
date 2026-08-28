## Propósito

El Área de UI/UX cuida **la legibilidad del sistema**, no lo que el sistema hace.

Ninguna otra área se ocupa de esto: Producción decide qué se hace, Game Design cómo funciona, Level Design dónde ocurre, Programación cómo se construye. Todas producen sistemas. Nadie, hasta ahora, se ocupaba de que esos sistemas **se puedan leer**.

El área existe para una sola pregunta:

```txt
¿Puede alguien mirar la pantalla y responder qué pasa, qué puede hacer
y cómo va, sin que nadie se lo explique?
```

Pero no la responde acomodando lo que otro cerró. La responde **antes**.

---

## Sistema y operador, no juego y jugador

Durante tres timelines el área estuvo escrita para un juego y un jugador. `TL-004` la sacó de ahí: el visor de Vaultrum es un instrumento de diagnóstico, quien lo opera es el owner, y su definición de terminado es literalmente de esta área — *las seis fallas se leen sin abrir un archivo*.

Por eso el charter dice **sistema** y **quien lo opera**. Un jugador es un operador con reglas de juego encima; un dashboard, un visor y una herramienta de línea de comandos tienen la misma capa de comunicación y las mismas leyes. Lo que cambia es el vocabulario, no el criterio.

---

## El área no acomoda: dicta el presupuesto

Un ingeniero de sonido no arregla la mezcla cuando la banda ya grabó mal. Dice cuánto lugar hay en el espectro y quién ocupa qué, y por eso después la mezcla existe.

Este área funciona igual. Cuando otra área va a cerrar un sistema que alguien va a tener que leer, **no cierra por su cuenta: le pide el presupuesto de comunicación**, y el área se lo entrega antes de que las reglas queden fijas.

La razón es económica, no estética:

```txt
En TL-002 el área quedó fuera de la cadena. La interfaz se improvisó
dentro del EJ como desvío declarado, y la entrega quedó en PAUSADO.
Rehacerla costó un timeline entero.
Dictar el presupuesto antes cuesta media página.
```

Ese es el fin del área. **La legibilidad no se consigue rediseñando pantallas al final: se consigue no cerrando sistemas ilegibles.**

---

## Los tres modos

El área presta tres servicios. Cada uno se declara en su salida.

### Modo Presupuesto

Un área va a cerrar un sistema que alguien va a tener que leer. El área **no diseña todavía**: entrega el presupuesto de comunicación — cuántos estados distinguibles admite la pantalla, qué canales de señal hay y cuáles ya están ocupados, qué información tiene que estar visible en todo momento, y cuál es el techo de densidad del proyecto. Game Design cierra contra ese presupuesto.

Ejemplo: *"el visor va a marcar seis fallas distintas sobre el mundo"*. El presupuesto dice que el color ya está ocupado por la identidad de área, que seis marcas simultáneas no se distinguen en periferia, y que si las seis tienen que convivir hace falta un segundo canal o una vista dedicada. Eso cambia el diseño del sistema, no su interfaz — y por eso llega antes.

### Modo Interfaz

El `GDS` cerró. El área diseña: pantallas, HUD, menús, jerarquía de información, estados, feedback y accesibilidad, y cierra el `UXS` contra las seis leyes medidas. Es el modo de producción.

### Modo Pasada

El modo residual: medir una interfaz que ya existe —especificada o construida— y decir qué está fuera de ley. **Deja de ser el propósito del área**: si el presupuesto y la interfaz funcionan, una pasada solo hace falta cuando entra material viejo o cuando el owner pide una revisión completa.

---

## El UXS tiene dos mitades y dos cierres

De ahí sale la inversión. El `UXS` deja de ser un documento que empieza cuando el `GDS` termina:

```txt
Mitad A — Presupuesto   se escribe con el RQ en la mano, antes de que el GDS cierre
                        cierra cuando Game Design la acepta
Mitad B — Interfaz      se escribe con el GDS cerrado
                        cierra con legibilidad.py --verificar
```

Un solo archivo, dos cierres declarados. El `UXS` declara sus dos insumos —el `RQ` en la mitad A, el `GDS` en la mitad B— en dos líneas rotuladas, que es la única arista lateral legal del vault.

Un `UXS` que arranca directamente en la mitad B es válido y se declara: significa que el sistema se cerró sin presupuesto. Es deuda, no error, y queda escrita.

---

## Las seis leyes de la comunicación

Las seis leyes no se inventaron acá: se **leyeron de las dos `UXS` que el área ya había escrito bien**, que las cumplían sin tenerlas formalizadas. Son descripción de lo que funcionó, escrito para que se pueda medir.

### Ley 1 — Las tres preguntas tienen respuesta

En todo momento, quien opera puede responder: ¿qué pasa? ¿qué puedo hacer? ¿cómo voy?

Una respuesta ausente no es un descuido: es una decisión, y se declara con su razón. En el menú de un juego la tercera pregunta no aplica *porque todavía no empezó*, y eso se escribe.

Se mide: una fila por estado y tres celdas. Celda vacía sin justificación, falla.

### Ley 2 — Ninguna señal viaja sola en el color

Todo lo que el color comunica lo comunica **además** otra cosa: posición, símbolo, forma o texto. El cian y el naranja de `TL-003` funcionan porque cada jugador está anclado además a un lado fijo de la pantalla.

Se mide: razón de contraste WCAG sobre cada par declarado, y sobre cada par que tiene que distinguirse, la simulación de las tres dicromacias más la escala de grises. Dos señales que colapsan en cualquiera de las cuatro no son dos señales.

### Ley 3 — El mapping es una promesa

Una tecla, un gesto o un control hacen **lo mismo en todas las pantallas**. `ESC` es siempre atrás; `ENTER` nunca cancela. Un mapping inconsistente es la forma más rápida de romper el modelo mental de alguien que recién llega.

Se mide: una tecla con dos verbos falla; una tecla usada sin declarar, también.

### Ley 4 — Ninguna acción sin respuesta en el mismo frame

Toda entrada produce una respuesta visible inmediata. Si una tecla no hace nada, quien opera no concluye *"esto no se puede"*: concluye *"esto se colgó"*.

Se mide: toda tecla del mapping declara su respuesta inmediata.

### Ley 5 — Nada se descubre por prueba y error

Toda acción disponible en un estado está **escrita en pantalla**, con su tecla. Un sistema que esconde la mitad de lo que se puede hacer no es minimalista: es incompleto.

Se mide: las acciones de cada estado tienen que estar contenidas en lo que ese estado muestra.

### Ley 6 — Sin estados muertos y sin pantallas sin retorno

Todo estado tiene al menos una salida, y se llega a él caminando desde la raíz. Salir de la aplicación es una salida legítima; quedar encerrado no lo es.

Se mide: el grafo de navegación, alcanzabilidad y grado de salida.

---

## Dos corolarios operativos

### El presupuesto de pantalla es finito

Cada proyecto declara su techo de bloques de texto por pantalla y sus franjas reservadas, y **ningún elemento se dibuja fuera de ellas**. La cámara o el layout se encuadran descontando las franjas, no al revés.

No es una preferencia de estilo: es lo que permite que la jerarquía funcione en visión periférica. Una diferencia de tamaños de 2:1 se lee como *dos cosas parecidas* y obliga a decidir dónde mirar.

### Una excepción se acota o no es excepción

El recordatorio de teclas de `UXS-003.7` se dibuja sobre la zona jugable y sin embargo está en ley, porque declara las tres cosas: **cuándo aparece** —solo el primer saque—, **cuánto dura** —dos segundos con desvanecido— y **con qué peso** —gris al 60%—. Sin las tres, no es una excepción acotada: es una grieta en la regla.

Las excepciones se declaran una por una en `Herramientas/excepciones.txt`, con su razón escrita.

---

## El piso de interfaz

Las seis leyes miden **el techo**: que lo declarado se lea bien, que no colisione, que no sobre. Ninguna de las seis mide **el piso**: que lo declarado **alcance**.

La Ley 1 es la que más se le acerca y se satisface con una **declaración**. El `UXS` escribe *"cómo voy → el largo del cuerpo"* y la ley da la pregunta por contestada. Nadie preguntó si eso le alcanza a quien juega.

```txt
Que SOBRE senal   se mide     densidad, contraste, colision de canales
Que FALTE senal   no se mide  se descubre jugando
```

### Por qué el presupuesto no lo cubre

Un presupuesto de **cero** en un canal es legítimo. `UXS-001.2` de Salto declara cero HUD permanente y cero texto en juego, y tiene razón: el género vive de que la postura del personaje lo diga todo.

Pero el presupuesto reparte **lo que compite por la pantalla**. Hay una capa que no compite con nada porque no está siempre visible: la pantalla de inventario vacío, el estado de carga, el error de guardado, la primera vez que alguien ve esa pantalla. Esa capa **no se presupuesta: existe o no existe**.

Confundir las dos es lo que produce la interfaz que mide en verde y se siente vacía.

### Los seis ítems del piso

Ninguno depende del género y ninguno consume presupuesto. Un `UXS` que no los declara está incompleto aunque las seis leyes den verde.

| # | Ítem | Qué exige |
|---|------|-----------|
| 1 | **Los cinco estados de pantalla** | toda pantalla declara su estado **vacío**, **cargando**, **error**, **primera vez** y **cambio de dispositivo**, o por qué no aplica |
| 2 | **Pausa que pausa** | existe, abre en ≤200 ms y **congela la simulación**. Nadie muere mirando el menú de opciones |
| 3 | **El cajón de cada dato** | cada dato del sistema está en uno de tres: HUD permanente · a demanda · no va (lo dice el mundo) |
| 4 | **La cadena de respuesta tiene números** | ≤16 ms cambio visual · ≤50 ms sonido · ≤200 ms transición. Arriba de 300 ms sin respuesta, se aprieta de nuevo |
| 5 | **Opciones mínimas** | tres sliders de audio, remapeo, salir — alcanzables en ≤3 pasos desde la pausa |
| 6 | **El encuadre tiene margen** | safe area del 5%, tipografía de cuerpo dimensionada para la distancia de lectura declarada |

**La regla de admisión del cajón 1**, que es la que evita las dos fallas opuestas:

```txt
va al HUD permanente  si se consulta >=1 vez cada 10 s
                      Y cambia una decision inmediata
```

Un dato que no cumple las dos cosas no es "poco importante": está en el cajón equivocado. Con esa regla, el HUD vacío y el HUD de simulador de vuelo son la misma falla — nadie asignó los cajones.

### De dónde sale

El piso no se inventó acá. Está destilado en `14_UI_HUD_y_menus` (`05_Escuela/Biblioteca/Fundamentos/`), con su baseline numérico completo, sus diez antipatrones y sus seis pruebas. El área **lo consulta on-demand** y no lo copia: el libro es la fuente, esto es el contrato.

### El corolario del cero

El piso arregla la mitad de la falla: lo que tiene que existir aunque el HUD esté vacío. La otra mitad es el cero mismo.

> **Un canal presupuestado en cero es una hipótesis, no un hecho, hasta que alguien juega.**

`UXS-001.2` de Merma declaró *HUD numérico permanente = 0 elementos* con un argumento bueno —*"el cuerpo ES el marcador, un número al lado sería decir dos veces lo mismo"*—, `legibilidad.py` dio las seis leyes en verde, y el owner jugó y dijo *"faltan bastantes indicadores"*. El instrumento no lo podía ver: mide que lo declarado se lea, no que alcance.

Un cero es la única cifra del presupuesto que **no se puede refutar leyendo**. Cualquier otra se discute contra la densidad y el techo; el cero no compite con nada, así que ningún cruce lo toca.

Por eso se trata distinto:

```txt
todo canal presupuestado en CERO se lista aparte en el UXS, con
  con que se reemplaza      el canal concreto que lleva esa senal en su lugar
  como se verifica          la observacion que lo confirmaria o lo tumbaria

y entra al VE como item a verificar con el owner jugando.
```

No es un veto al cero. `UXS-001.2` de Salto declara `HUD permanente: 0` y `texto en juego: 0`, y ese cero está bien puesto: el género vive de que la postura lo diga todo. Lo que la regla arregla es que **el instrumento no distingue un cero pensado de un cero equivocado** — a los dos les da verde. Listarlo aparte es lo que lo pone bajo la mirada del único que puede decidirlo.

### Lo que el piso todavía no tiene

`legibilidad.py` **no mide el piso**. Los seis ítems se declaran en el `UXS` y los verifica el Validador leyendo, no corriendo. Es deuda declarada, con su motivo: el instrumento se extiende cuando el piso demuestre que la forma sirve en dos proyectos reales. Hasta entonces, el checklist de cierre lo marca como juicio y no como medición.

---

## El costo de lo que se dibuja

El `UXS` decide qué se dibuja y con qué frecuencia cambia. Esas dos cosas fijan el costo recurrente de la interfaz **antes** de que Programación escriba una línea — y la interfaz suele ser el gasto por frame más grande de un juego chico.

No es optimización. **Optimizar sin requerimiento es alcance no pedido; esto es arquitectura, y la arquitectura no tiene ventana de "después".** Separar un canvas cuando ya hay treinta elementos adentro es un rediseño; declararlo el día cero es una fila en una tabla.

Por eso el `UXS` declara, para cada elemento que pone en pantalla, **cada cuánto cambia**:

```txt
nunca            estatico          marco, etiquetas, fondo
por evento       cambia al pasar   vidas, puntaje, estado
por frame        cambia siempre    barra de tiempo, medidor continuo
```

Tres reglas salen de esa tabla, y las tres son del Core (`03_Optimizacion/07_UI/`):

1. **Agrupar por frecuencia de cambio, no por ubicación** — lo que nunca cambia no comparte lote con lo que cambia por frame (`Separar canvas por frecuencia de cambio`).
2. **La interfaz se actualiza por evento, no por sondeo** — el dato cambia, avisa, la UI se entera. No al revés (`UI orientada a eventos`).
3. **Un elemento que se reescribe sin cambiar es trabajo puro** (`UI actualizada innecesariamente`, `Canvas rebuild`).

El área **no** elige la implementación: eso es del `SOL`. Declara la frecuencia, que es información de diseño, y sin ella Programación tiene que adivinarla o descubrirla con el profiler cuando ya es cara.

```txt
En la corrida de Merma, OnGUI dibujaba todo dos veces por frame.
No lo encontro ninguna lectura del documento: lo encontro contar rectangulos.
La frecuencia de cambio no estaba declarada en ningun lado.
```

---

## Sub-agentes del área

### [[01_Consultor_Legibilidad]]

Entrega el presupuesto de comunicación antes de que el sistema cierre. Traduce lo que otra área va a diseñar en cuántas señales entran, por qué canal y con qué techo. No diseña la interfaz.

### [[02_Analista_UX]]

Encuadra. Interpreta qué necesita ver, entender y decidir quien opera en cada momento, y mapea sus flujos. No define el layout.

### [[03_Disenador_Interfaz]]

Diseña. Pantallas, HUD, menús, jerarquía, estados, feedback y accesibilidad, y deja el `UXS` instrumentado para que se pueda medir. No cambia reglas.

### [[04_Auditor_Legibilidad]]

Mide. Corre la herramienta sobre el `UXS` y entrega el estado real de las seis leyes con números, sin proponer nada todavía.

### [[05_Validador_UX]]

Valida y cierra **los tres modos**. El veredicto sale de la herramienta, no de una lectura: falla la entrega si una ley quedó en rojo sin excepción declarada.

---

## Flujos del área

### [[01_Flujo_Presupuesto]]

Convertir lo que otra área va a cerrar en un presupuesto de comunicación que condicione el diseño antes de que sea caro cambiarlo.

### [[02_Flujo_Analisis_UX]]

Transformar el `GDS` cerrado en un encuadre: qué necesita ver, entender y decidir quien opera.

### [[03_Flujo_Diseno_Interfaz]]

Convertir el encuadre en un `UXS` instrumentado.

### [[04_Flujo_Auditoria_Legibilidad]]

Medir el estado real de las seis leyes y entregar el informe.

### [[05_Flujo_Validacion_UX]]

Verificar que la entrega dejó las seis leyes en verde, y cerrar el `UXS`.

---

## Los cuatro gates del área

Un gate que no se puede verificar mecánicamente no es un gate, es una intención. Tres de los cuatro corren; el cuarto se comprueba a posteriori y lo declara.

| Gate | Cuándo | Qué exige | Cómo se verifica |
|------|--------|-----------|------------------|
| Comunicación | antes de que cierre un `GDS` con interfaz | presupuesto entregado y citado en el `GDS` | la mitad A del `UXS` existe y el `GDS` la nombra |
| Interfaz | todo `RQ` con interfaz | `UXS` abierto antes de que Programación abra el `SOL` | el `SOL` declara su `UXS` |
| Cierre | todo `UXS` que se cierra | las seis leyes en verde, **los seis ítems del piso declarados y todo canal en cero listado aparte** | `legibilidad.py --verificar` devuelve 0 · el piso y los ceros los lee el Validador (todavía no se miden) |
| No aplica | un `GDS` declara que no hay interfaz | qué dimensión de comunicación queda ausente | el test del *no aplica* al cerrar el `VE` |

Corregir el texto de una etiqueta o el valor de un parámetro visual en un `UXS` ya cerrado **no** dispara ningún gate. El área se activa cuando cambia lo que se comunica, no cuando cambia cómo está escrito.

---

## Salidas del área

### [[00_Indice_uxs]]

El registro de las specs de interfaz. Cada `UXS-XXX.n` declara su **modo** y el estado de sus dos mitades, y queda con lo que se midió, lo que se diseñó y cómo cerró.

---

## Herramienta del área

El área no valida a ojo. La medición la hace `Herramientas/legibilidad.py`, que lee los bloques declarativos del `UXS` y prueba las seis leyes:

```txt
python3 "02_Agencia/Area ui-ux/Herramientas/legibilidad.py" "02_Agencia/Area ui-ux/Salidas"
python3 "02_Agencia/Area ui-ux/Herramientas/legibilidad.py" "02_Agencia/Area ui-ux/Salidas" --verificar
```

`--verificar` devuelve código 1 si una respuesta falta sin justificación, si un par de colores no llega al contraste mínimo, si dos señales colapsan en daltonismo o en grises, si una tecla tiene dos significados, si una acción no tiene respuesta declarada, si algo se descubre por prueba y error, o si un estado quedó muerto o inalcanzable.

Los bloques que la herramienta lee viven dentro de bloques de código cercados. Eso es deliberado: `grafo.py` ignora los bloques de código, así que **instrumentar un `UXS` no agrega ni una arista al grafo del vault**.

---

## Regla operativa

Primero el presupuesto, después el encuadre, después la interfaz, y recién entonces la validación.

**El piso antes que el techo.** Primero existe lo que tiene que existir; recién después se discute cuánto entra en pantalla. Un `UXS` que discute densidad sin haber asignado los cajones está optimizando un presupuesto que todavía no sabe qué reparte.

**Usabilidad primero, engagement después.** La interfaz no cierra hasta que quien opera *puede* operar el sistema sin fricción. Nunca decorar a costa de la legibilidad: nada de lo que se agregue puede tapar una falla ni volver ambiguo un estado.

Y el área **no afirma un número sin medirlo**. Si la herramienta no se puede correr, se dice con esas palabras: *medición no disponible*.

---

## Límites del área

**No define reglas ni balance.** Eso es de Game Design. El área dice cuántos estados se pueden distinguir; cuáles existen lo decide el `GDS`.

**No diseña el espacio jugable.** Eso es de Level Design.

**No programa.** El `UXS` cerrado es insumo de Programación, no una implementación.

**No define alcance.** Eso es de Producción.

**No hace arte final ni ilustración.** Define el sistema de señales, no la pieza gráfica.

Si al `GDS` le falta un estado o un feedback, el área **no lo inventa**: lo marca y deriva a Game Design. Un estado que la interfaz inventa es una regla escrita en el lugar equivocado.

---

## Encadenado con otras áreas

El área entra **dos veces**: antes de que Game Design cierre, y después.

```txt
        RQ con interfaz
              ↓
        UI/UX  →  UXS mitad A: presupuesto de comunicación
              ↓
        Game Design cierra el GDS contra el presupuesto
              ↓
        UI/UX  →  UXS mitad B: la interfaz
              ↓
        gate de cierre: legibilidad.py --verificar
              ↓
        Programación abre el SOL con el UXS en la mano
```

Recibe de **Producción** el `RQ` y de **Game Design** el `GDS`; opcionalmente de **Level Design** el `LDS` cuando la interfaz depende del espacio. Entrega a **Programación**.

Consulta on-demand la Biblioteca de la Escuela: `05_Fundamentos_de_experiencia_ludica` (pilares 3, 4, 5 y 7) y `14_UI_HUD_y_menus`, que es de donde sale el piso. Según el caso, además: `09_Onboarding_y_tutorial` cuando la interfaz enseña, `10_Input_y_respuesta` cuando hay que fijar la cadena de respuesta, `11_Camara_y_encuadre` cuando la cámara transporta señal, y `16_Audio_como_gameplay` cuando el sonido es el canal redundante del color. Los cuatro están *En la Biblioteca* desde la corrección del lote `EST-006`. **On-demand quiere decir uno por vez, por lo que se necesita** — la Biblioteca entera no se carga. Cuando el entregable no es un juego, el pilar 4 sigue aplicando entero y los otros tres se leen como feedback, control y progreso visible del sistema.

Y consulta al Área de Arquitectura antes de crear, mover o purgar notas: el `UXS` es una nota del vault y su forma la dicta el arquitecto.

Lo que el área aprende sobre la legibilidad puede volver al Core como criterio, por la vía de siempre: `Area conocimiento/Staging/` y aprobación del owner. Las seis leyes viven acá hasta que el owner decida promoverlas.

---

## Skill del área

La skill ejecutable del área es `vaultrum-uiux`, en `Skills/vaultrum-uiux/`.

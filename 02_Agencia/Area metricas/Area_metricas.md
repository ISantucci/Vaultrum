## Propósito

El **Área de Métricas** responde la pregunta que ninguna otra área de la cadena tenía asignada:

```txt
¿El jugador real se comporta como esperaba el diseño?
Y si no: ¿dónde se separa, y qué evidencia hace falta para decidir qué cambiar?
```

Game Design escribe lo que **espera** que pase. Control de Calidad verifica que lo construido **no se caiga**. Producción valida que lo entregado sea **lo prometido**. Ninguna de las tres mide lo que hace la gente con un sistema que funciona — y esa es la única prueba de que el diseño acertó.

La función se lee en una cadena, y el área es dueña de toda ella menos de la decisión final:

```txt
objetivo -> comportamiento esperado -> KPI -> instrumentación -> datos
         -> diagnóstico -> decisión o experimento -> nueva medición
```

> **El área existe para mejorar decisiones, no para producir números.**

El criterio de fondo vive en el Core, en `Metricas y analytics`. Esta área lo aplica; no lo repite.

---

## Por qué es un área y no una silla de otra

La pregunta se hizo antes de crearla, y la respuesta es de estructura, no de gusto. Las tres candidatas naturales —Producción, Control de Calidad y Game Design— consumen métricas, y ninguna puede ser su dueña sin romper un límite que ya tiene escrito.

| Candidata | Por qué parecía | Por qué no |
|---|---|---|
| **Producción** | define el objetivo y la fase, y lee el resultado en el `VE` | decide. Si la misma silla fija el objetivo, elige el KPI, lee el dato y valida la entrega, se juzga a sí misma: es el **metric shopping** con un solo autor |
| **Control de Calidad** | ya entra antes con el *presupuesto de verificación* y ya admite el perfil de entrada `datos` | su límite escrito: **no valida la experiencia**, eso es del `VE` y del playtest. Una métrica de producto mide experiencia |
| **Game Design** | el balance y la economía necesitan datos | diseña. Quien escribió la regla es el peor lector de si la regla funcionó |

Lo que sí es de cada una, y se queda donde está:

```txt
Producción          declara la FASE del producto y el OBJETIVO, y DECIDE con el resultado
Game Design         escribe el comportamiento esperado, y reinterpreta el diseño con la lectura
Programación        implementa los eventos del tracking plan
Control de Calidad  verifica que cada evento dispare bien, contra los criterios que escribe esta área
```

Métricas mide y lee. **No decide ni diseña.**

---

## Dónde está parada

**Entra dos veces**, como UI/UX, Arte y Control de Calidad, y por la misma razón: una medición que aparece recién al final descubre que no hay eventos para medir.

```txt
GDS cerrado
  ├─► Level Design · UI/UX mitad B · Arte mitad A
  └─► MÉTRICAS mitad A   → MET-XXX.n   plan de medición: KPI, guardrails, tracking plan
        ↓                              ANTES del SOL: Programación implementa los eventos
Programación (SOL + EJ)
  ↓
Control de Calidad (QA)   ⟵ incluye la QA de eventos que escribió la mitad A
  ↓
MÉTRICAS mitad B          → MET-XXX    lectura de la entrega, con los datos del playtest
  ↓
Producción (VE)           ⟵ decide con la lectura en la mano
```

Y un tercer servicio para un producto con jugadores de verdad: **Salud**, la revisión periódica sin problema específico.

**Es opcional, y la omisión se declara.** Producción escribe en el `RQ` si Métricas aplica, igual que con `UXS` y `ART`:

```txt
MET aplica    — hay una pregunta sobre el comportamiento del jugador que decide algo: <cuál>
MET no aplica — <qué dimensión falta> : <por qué>
                (no hay nadie más que el owner jugando, es una herramienta sin usuarios,
                 el hilo es de infraestructura…)
```

---

## La fase la declara Producción, y el área la respeta

Cada fase hace una pregunta distinta, y la métrica correcta es la que responde la pregunta de la fase. El detalle está en el Core, en `Fases del producto y que medir`.

```txt
Planning         ¿vale la pena construirlo?
Pre-Production   ¿funciona el núcleo?
Production       ¿los sistemas funcionan como deberían?
Testing          ¿el jugador real se comporta como esperaba el diseño?
Pre-Launch       ¿funciona como producto completo antes de escalar?
Launch           ¿qué pasa con el mercado real, a escala?
Post-Launch      ¿cómo evoluciona?
Live Ops         ¿cómo se mantiene y mejora un producto vivo?
```

**La fase no la decide esta área.** Es un dato del proyecto: Producción la escribe en el cuaderno y en el `TL`. Si no está, el área no la adivina — devuelve a Producción. Es lo que evita el anti-patrón más barato de cometer: **ignorar la fase**, medir ARPPU en un prototipo que todavía no sabe si su loop funciona.

Todo lo que corrió la cadena hasta hoy —`Pong3D`, `Salto`, `TowerDefense`— vive entre Pre-Production y Testing. Ahí las preguntas son de comprensión, de loop y de drop-off, y la telemetría tiene tope.

---

## Las seis leyes de la medición

Paralelas a las del grafo, la comunicación, la verificación, la documentación y el arte. Las cinco primeras las mide `Herramientas/metricas.py` sobre el plan; la sexta, sobre la lectura y sobre el dato.

### Ley 1 — Objetivo antes que métrica

Ningún KPI se elige sin un **objetivo** y un **comportamiento esperado** escritos antes. "Qué KPI ponemos" es la pregunta equivocada; la correcta es qué evidencia haría falta para saber si esto produce el comportamiento que se buscaba. Dueño: `01`.

### Ley 2 — Un KPI se define entero, y no cambia después de ver el dato

Nombre, fórmula, población, ventana, fuente y baseline —o su ausencia declarada—. El nombre no alcanza: `ARPU` divide por usuarios totales en una herramienta y por activos en otra. Y el KPI primario **se congela en el plan**: si la lectura decide con otro, eso es metric shopping y el instrumento lo detecta comparando los dos documentos. Dueño: `01`, y lo vigila `04`.

### Ley 3 — Todo KPI viaja con sus guardrails

Una mejora local puede romper el producto: anuncios vistos +300%, D7 −20%. Ningún plan cierra sin al menos un guardrail. Dueño: `01`.

### Ley 4 — Cada evento justifica su existencia

Un evento por pregunta, que alimenta una métrica declarada. Nombre en `snake_case` sin valores dinámicos adentro, sin datos personales en los parámetros, y **dentro del presupuesto de la fase**: donde rige el playtest, el tope es el de `13_Playtesting_y_validacion` —diez eventos—, y pasarlo se declara con su razón. Dueño: `02`.

### Ley 5 — La fase decide qué se mide

Fase y modelo de negocio declarados; ningún KPI que la fase no puede sostener. El instrumento marca las siglas de escala —ARPU, ARPPU, LTV, DAU, D30…— en un plan de Pre-Production o de Production. Dueño: `01`.

### Ley 6 — El dato dice qué, no por qué

Dos mitades, en este orden. **Se valida antes de leerse**: duplicados, entornos mezclados, eventos fuera del plan, eventos del plan que nunca dispararon, signo de los recursos. **Y se lee rotulado**: hechos, interpretaciones, hipótesis y recomendación en secciones separadas, con la próxima medición escrita. Correlación no es causalidad. Dueños: `03` lee, `04` verifica.

---

## Los tres modos

Se entra por el modo que corresponde al estado del trabajo, no por todos.

### Modo Plan — mitad A

Con el `GDS` cerrado y antes del `SOL`. `01` convierte el objetivo del `RQ` y el comportamiento esperado del `GDS` en un KPI primario con sus diagnósticas y guardrails; `02` escribe el tracking plan y los criterios de QA de eventos; `04` corre `metricas.py plan` y cierra el **`MET-XXX.n`**.

### Modo Lectura — mitad B

Con datos en la mano: un playtest, una build de prueba, un soft launch. `04` corre `metricas.py datos` y decide si el dato es legible; `03` lee contra el plan congelado; `04` corre `metricas.py lectura` y cierra el **`MET-XXX`**, que es insumo del `VE`.

### Modo Salud — un producto con jugadores

Sin problema específico, sobre un producto lanzado. Las cinco preguntas del Core en orden —¿entra gente? ¿vuelve? ¿qué hace? ¿paga? ¿la economía sostiene valor?— más la salud técnica. Produce un `MET-XXX` de salud, que cuelga del `TL` de operación que Producción abra para eso. **Hasta hoy no hay ningún proyecto del vault en esa fase**, y el modo queda escrito para cuando lo haya.

---

## Sub-agentes del área

### [[01_Analista_Objetivo]]

Del objetivo al KPI. Lee el objetivo en el `RQ`, el comportamiento esperado en el `GDS` y la fase en el cuaderno; elige **un** KPI primario, lo define entero, y le pone guardrails. No diseña eventos.

### [[02_Disenador_Medicion]]

Del KPI al evento. Escribe el tracking plan con la mínima instrumentación suficiente, los criterios de QA de eventos para Control de Calidad y la línea de privacidad. No elige el KPI ni lo cambia.

### [[03_Lector_Datos]]

Del dato a la lectura. Lee **contra el plan congelado**, separa hecho de interpretación, de hipótesis y de recomendación, y escribe la próxima medición. No puede cambiar el KPI después de mirar.

### [[04_Validador_Medicion]]

Corre el instrumento y cierra los tres modos. Valida el dato antes de que nadie lo lea, y verifica que ninguna hipótesis haya llegado a la recomendación disfrazada de hecho.

---

## Por qué cuatro sillas, y lo que todavía no se sabe de ellas

Cada separación ataca un anti-patrón documentado de la disciplina:

| Separación | El anti-patrón que evita |
|---|---|
| Objetivo ≠ Diseño de medición | **telemetry spam**: quien diseña eventos tiende a instrumentar todo. Fijar la pregunta primero es lo que acota los eventos |
| Diseño ≠ Lectura | **metric shopping**: el KPI se congela antes del dato, y quien lee no lo puede tocar. Es la *versión congelada* de Calidad, aplicada a la pregunta |
| Lectura ≠ Validación | **causalidad por correlación**: quien construyó una explicación es el peor juez de si el dato la sostiene. Es *el que construye es el peor juez de lo que construyó*, de Arte |

**Honestidad que el área le debe al resto:** a diferencia de las siete sillas de Arte, **ninguna de estas separaciones tiene todavía un defecto medido en Vaultrum** que la justifique. Salen de los errores que la industria repite, no de un caso propio. El primer caso las confirma o las funde, y si dos sillas resultan ser una sola, se funden sin ceremonia.

---

## Flujos del área

### [[01_Flujo_Objetivo]]

Del pedido vago al KPI definido entero, con diagnósticas y guardrails.

### [[02_Flujo_Plan_De_Medicion]]

El tracking plan, la QA de eventos y la privacidad, medidos por `metricas.py plan`.

### [[03_Flujo_Lectura]]

La lectura del dato contra el plan congelado, rotulada.

### [[04_Flujo_Validacion_Medicion]]

El dato validado antes de leerse, y el cierre de los tres modos con el instrumento.

---

## Salidas del área

### [[00_Indice_met]]

El contrato de salida del `MET`. Dos cortes —el plan del hilo `MET-XXX.n` y la lectura de la entrega `MET-XXX`—, sus secciones y cuándo cierran.

---

## Herramienta del área

```txt
Herramientas/metricas.py          EL INSTRUMENTO
  plan    <MET-XXX.n.md>          leyes 1-5 sobre el plan de medición
  lectura <MET-XXX.md>            ley 6 sobre la lectura, y ley 2: el KPI no cambió
  datos   <eventos.csv>           ley 6 sobre el dato: calidad primero, después
                                  retención clásica y rolling por cohorte, funnel,
                                  progresión, sesiones y economía
Herramientas/probar_metricas.py   LA PRUEBA: 36 casos, 0 fallas
```

**Sin dependencias.** Corre con el Python del owner, sin `pip install`: el gate que no se puede correr en la máquina donde se trabaja no es un gate.

**El instrumento ya tuvo su primer defecto, y lo encontró su primera corrida.** Sobre un CSV de muestra, `datos` reportaba *"wave: 0% de completion"*: contaba `wave_started` como el inicio de un intento que nunca podía terminar. Un número correcto sobre el objeto equivocado —el mismo defecto que ya tuvieron `sim.py`, `requerimientos.py` e `instalar_skills.py`—. Ahora una base es progresión sólo si alguna vez termina, y el caso quedó escrito en la prueba.

Lo que el instrumento **no** mide, declarado: si el KPI elegido es el correcto para el objetivo, si la interpretación es buena, y si la recomendación es la mejor. Eso es juicio y se rotula como juicio.

---

## Los gates del área

| Gate | Cuándo | Qué exige |
|------|--------|-----------|
| Fase | antes de abrir un `MET` | fase y modelo declarados por Producción en el cuaderno o el `TL` |
| Plan | antes del `SOL` del hilo | `metricas.py plan` en ley: el `SOL` implementa eventos que existen en un plan cerrado |
| Dato | antes de leer | `metricas.py datos --verificar`: sin duplicados, sin entornos mezclados, sin signos ambiguos |
| Lectura | antes del `VE` | `metricas.py lectura` en ley, con el mismo KPI que el plan congeló |

Un paso condicional que no corre **declara su omisión**.

---

## Límites del área

No decide qué se construye ni la prioridad (Producción). No diseña reglas, balance ni economía: los mide y devuelve la lectura (Game Design). No implementa eventos (Programación). No verifica que el evento dispare: escribe los criterios, y los ejecuta Control de Calidad. No diseña la interfaz de un tablero (UI/UX). No decide dónde vive una nota (Arquitectura). No mergea al Core (Conocimiento).

**No declara causalidad sin experimento o sin estrategia de identificación.** No optimiza un número ignorando la experiencia, el bienestar del jugador o la confianza: FOMO, aversión a la pérdida y recompensas variables se miden, no se explotan. No recolecta datos "por si acaso". No reemplaza una revisión legal de privacidad.

---

## Encadenado con otras áreas

```txt
RQ (objetivo, MET aplica)  +  GDS cerrado (comportamiento esperado)  +  cuaderno (fase)
  ↓
MÉTRICAS mitad A   → MET-XXX.n   ─► Programación: el tracking plan
                                 ─► Control de Calidad: los criterios de QA de eventos
  ↓ (build con eventos verificados, y datos de juego)
MÉTRICAS mitad B   → MET-XXX     ─► Producción: insumo del VE
                                 ─► Game Design: la lectura, si el diseño tiene que moverse
```

**Recibe de:** Producción (objetivo, fase, modelo, y si aplica) · Game Design (`GDS`, sección *Experiencia esperada*) · Control de Calidad (la build verificada) · el juego (el CSV de eventos).

**Deriva a:** Producción si falta objetivo o fase · Game Design si el comportamiento esperado no está escrito · Programación si un evento no se puede implementar como se pidió · Arquitectura antes de crear cualquier nota.

---

## El área nace sin caso, y lo dice

Es la condición que `00_START_HERE` le pone a toda área nueva: **un área necesita un caso, no una spec**. `LDS` y `QA` nacieron escritas y corrieron por primera vez con `Salto`; Arte entró con el caso ya hecho. Esta entra como entraron las dos primeras: con el contrato, las leyes y el instrumento probado, y **ningún `MET` escrito**.

El primer caso natural es el playtest del próximo tower defense: Pre-Production, pocos testers, diez eventos como techo, y una pregunta de comprensión —¿construye su primera torre sin ayuda?—. Ese `MET` es el que va a decir si las cuatro sillas son cuatro.

---

## Skill del área

La skill ejecutable del área es `vaultrum-metricas`, en `Skills/vaultrum-metricas/`.

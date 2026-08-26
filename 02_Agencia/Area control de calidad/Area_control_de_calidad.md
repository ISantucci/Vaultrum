## Propósito

El Área de Control de Calidad es **el último paso**: la que dice si lo construido se sostiene.

Ninguna otra área lo hace. Programación valida **cómo está construido** cada hilo contra criterios técnicos. Producción valida **si lo entregado es lo prometido** contra la intención. Entre las dos quedaba una pregunta sin dueño, y es la que se paga cuando falta:

```txt
¿Esto funciona de verdad, resiste que alguien lo use mal,
y sigue funcionando después del último cambio?
```

La salida del área no es "probamos y parece andar". Es una decisión respaldada por evidencia, con tres valores posibles y ninguno ambiguo:

```txt
GO               se cumplen los criterios de salida
CONDITIONAL GO   hay desviaciones conocidas, enumeradas, con dueño y riesgo aceptado por escrito
NO-GO            hay una condición obligatoria incumplida, o no hay evidencia suficiente
```

---

## Dónde está parada

Al final de una épica, y **antes del `VE`**. Una épica puede ser una implementación específica —un hilo `.n`— o la entrega completa de un timeline; en los dos casos el área es el paso final de trabajo antes de que Producción cierre.

```txt
EJ (revisión técnica OK)
  ↓
Área de Control de Calidad  → QA     ⟵ ¿se sostiene lo construido?
  ↓
Área de Producción          → VE     ⟵ ¿es lo que se prometió?
  ↓
commit de la entrega
```

El orden no es cosmético. El `VE` valida la entrega frente a la intención y a la experiencia: para hacerlo necesita saber que lo que está mirando no se cae, que los defectos conocidos están enumerados y que el riesgo que queda vivo tiene nombre. **El veredicto del `QA` es insumo obligatorio del `VE`**, y un `VE` no puede cerrar en **Cerrado** con un `QA` en NO-GO.

Esto no lo inventó esta área: estaba escrito como deuda en `Area_produccion` desde que existe el `VE` — *"la verificación técnica previa al commit va a ser del área de QA cuando exista"*. Existe.

---

## La decisión de fondo: calidad transversal, gate final independiente

El área es el último paso, pero **el control de calidad no empieza al final**.

```txt
durante   testabilidad, criterios de aceptación verificables, instrumentación, datos de prueba
al final  el gate: independiente, sobre una versión congelada, con evidencia
```

Las dos mitades son necesarias y evitan los dos extremos que rompen:

- un gate tardío descubre problemas estructurales cuando ya son caros de corregir;
- un control absorbido por quien construyó pierde independencia y deja de ser un gate.

Por eso el área **entra dos veces**. Antes, con el **presupuesto de verificación**: qué hace falta para poder probar esto —instrumentación, semilla fija, atajos de estado, logs— dicho mientras todavía se puede construir. Después, con el **gate**: sobre una build identificable, con evidencia y decisión escrita.

Quien recibe una feature terminada sin entender qué cambió, qué riesgos tiene y qué sistemas toca está verificando con información incompleta. Por eso el Intake y el Análisis de Riesgo son obligatorios y no se saltean ni en el perfil más liviano.

---

## Las seis leyes de la verificación

Ninguna es nueva en el mundo; todas son la forma que toman acá. Las seis se miden con `Herramientas/calidad.py`, y ninguna depende de la lectura de quien cierra.

### Ley 1 — Nada se verifica sin versión congelada

Un resultado sobre una build que puede cambiar no es un resultado. La entrada declara build, commit o rama, plataforma y entorno — y esa versión no se toca durante el pase.

Si el arreglo de un defecto exige una build nueva, el pase no continúa sobre la anterior: se declara qué se verificó sobre cuál.

### Ley 2 — Antes del pase, la build se acepta o se rechaza

La verificación de build responde una sola pregunta: **¿vale la pena gastar horas probando esto?** No intenta probar el producto: comprueba que arranca, que el bucle principal se puede iniciar, que el camino crítico no está bloqueado y que no hay una falla evidente.

Si un criterio bloqueante falla, **la build se rechaza y el pase profundo no empieza**. Un pase completo sobre una build rota consume el día y no produce información.

### Ley 3 — Un hallazgo se reproduce, o se declara intermitente

Un defecto sin pasos, sin versión y sin evidencia no es un defecto: es un aviso. Y un defecto que no se reproduce siempre no se descarta — se registra como intermitente, con las condiciones y la frecuencia observada.

Lo intermitente es justamente lo que llega al jugador.

### Ley 4 — Nada se cierra sin reverificar

Quien programa no cierra un defecto: lo deja **listo para reverificar**. Cierra quien verificó el arreglo, sobre una versión identificable.

La ley es la separación de quién cierra, y existe porque cambiar código no es lo mismo que resolver el problema. El detalle del ciclo de vida y la diferencia entre confirmación y regresión están en el Core.

### Ley 5 — Un pase declara lo que no ejecutó

La cobertura se escribe con tres valores y ninguno se deja vacío: **sí**, **no**, **no aplica con su razón**. Es la forma que toma acá la regla general del vault —una omisión declarada es criterio, una silenciosa es un hueco— y acá es mecánica: la herramienta falla la celda vacía y el "no aplica" pelado.

Un "no" no baja la nota del área. Baja el veredicto a CONDITIONAL GO, que es otra cosa: significa que alguien se hace cargo de un hueco conocido.

### Ley 6 — Un riesgo aceptado tiene dueño con nombre

**CONDITIONAL GO** no es un GO con asterisco. Es válido solo si las excepciones están enumeradas, el impacto está comprendido, existe un dueño que las acepta por escrito y ninguna contradice una regla innegociable de plataforma o de release.

Aceptar un riesgo es una decisión legítima. Aceptarlo sin registrarlo es la forma más cara de olvidarlo.

---

## Los dos cortes y los tres perfiles

El mismo mecanismo corre en dos escalas, con la misma lógica y distinta profundidad.

```txt
QA-XXX.n   gate de hilo      cuelga del EJ-XXX.n    una implementación específica
QA-XXX     gate de entrega   cuelga del TL-XXX      la épica completa, con sus hilos ya verificados
```

Y la profundidad la elige el riesgo, no la costumbre:

| Perfil | Cuándo | Qué corre |
|---|---|---|
| **Ligero** | hilo de riesgo bajo, sin datos persistentes ni camino crítico | intake, riesgo, humo del camino afectado, casos dirigidos, cobertura declarada |
| **Estándar** | por defecto | lo anterior + exploratorio con charter + regresión del sistema afectado |
| **Completo** | entrega, build candidata, cualquier cosa que toque guardado, economía o plataforma | lo anterior + compatibilidad + rendimiento + regresión completa + conocidos |

El perfil se declara en el `QA` y se justifica con el riesgo. **Bajar de perfil es una decisión declarable; saltear el gate no lo es.**

---

## Qué puede entrar al área

No solo "bugs de gameplay". El gate admite perfiles de entrada distintos, y cada uno mira otra cosa:

```txt
jugable        reglas, estados, límites, interrupciones, progresión, persistencia, feedback
técnico        excepciones, memoria, rendimiento, determinismo, ciclo de vida, build real
interfaz       navegación, foco, escalado, estados vacíos y de error, texto, accesibilidad
contenido      colisiones, atascos, disparadores, secuencia de objetivos, recorrido extremo
build          instalación, arranque, integridad, guardado compatible, permisos, plataforma
datos          tablas y configuraciones: completitud, unidades, referencias rotas, contradicciones
```

El último importa más de lo que parece: una tabla de balance con una referencia rota produce una falla igual de real que una línea de código mal escrita, y no la ve ninguna prueba de gameplay.

---

## Sub-agentes del área

### [[01_Receptor_De_Entrada]]

Recibe y **rechaza**. Comprueba que la entrada sea verificable —versión congelada, alcance, dueño, criterios de aceptación, entorno— y si falta lo imprescindible declara **NO LISTO PARA QA** en vez de empezar igual. No prueba nada.

### [[02_Analista_De_Riesgo]]

Decide **dónde se gasta el esfuerzo**. Estima qué puede fallar, con qué probabilidad, con qué impacto y con qué dificultad de detección; elige el perfil y las técnicas. No ejecuta el pase.

### [[03_Ejecutor_De_Pruebas]]

Diseña y ejecuta: verificación de build, casos dirigidos, exploratorio con charter. Reporta defectos reproducibles con evidencia. No decide si el defecto se arregla ni si la entrega sale.

### [[04_Triador_De_Defectos]]

Clasifica lo encontrado: validez, severidad, urgencia, dueño, si bloquea, si necesita regresión, si necesita análisis de causa raíz. Rebota cada hallazgo al área que corresponde. No arregla.

### [[05_Validador_De_Gate]]

Cierra. Corre la confirmación y la regresión, mide con la herramienta y emite **GO / CONDITIONAL GO / NO-GO** con su fundamento. Es el único que firma el veredicto.

---

## Flujos del área

Cada flujo es un paso del recorrido. Se entra por el que corresponde al estado del trabajo, no por todos.

### [[01_Flujo_Intake]]

### [[02_Flujo_Analisis_De_Riesgo]]

### [[03_Flujo_Verificacion_De_Build]]

### [[04_Flujo_Pase_De_Prueba]]

### [[05_Flujo_Gate_De_Calidad]]

---

## El instrumento

El área no declara un veredicto a ojo. La medición la hace `Herramientas/calidad.py`, que lee el `QA` instrumentado y, si existe, la planilla de operación del proyecto:

```txt
python3 "02_Agencia/Area control de calidad/Herramientas/calidad.py" <ruta del QA>
python3 "02_Agencia/Area control de calidad/Herramientas/calidad.py" <ruta del QA> --verificar
python3 "02_Agencia/Area control de calidad/Herramientas/calidad.py" <ruta> --planilla <archivo.xlsx>
```

`--verificar` devuelve código 1 si falta el análisis de riesgo que justifica el perfil, si la versión no está congelada, si la verificación de build no declaró su resultado, si un defecto cerrado no tiene reverificación, si la cobertura tiene celdas vacías o un "no aplica" sin razón, si **cualquier** defecto queda abierto o diferido sin dueño que lo acepte, o si el veredicto declarado no coincide con el medido. Cuando se le pasa la planilla —o la encuentra al lado del `QA`— cruza además cada defecto contra el registro: sin pasos, evidencia y reproducibilidad, no está reportado.

**Lo que la herramienta no prueba se declara como juicio**, nunca como medición: si el sistema se siente bien, si el diseño es correcto, si la experiencia se sostiene. Eso no es de esta área — es del `VE` y del playtest.

La planilla del área es `Herramientas/Vaultrum_QA_Operations.xlsx`: registro de defectos, casos, regresión, verificación de build, riesgos, cobertura, gate y sesiones exploratorias. **Es una plantilla vacía y no se llena acá.** Al abrir el `QA` de un proyecto se copia a la carpeta de calidad de ese proyecto y ahí se opera.

Las excepciones se declaran una por una en `Herramientas/excepciones.txt`, con su razón escrita. Una excepción sin razón es una falla con mejor redacción.

---

## Salidas del área

### [[00_Indice_qa]]

El contrato de salida: qué produce el área, qué forma tiene un `QA`, cómo se numera y cuándo está cerrado.

---

## Plantillas del área

### [[00_Plantillas_qa]]

Los formularios operativos: estrategia, plan de prueba, verificación de build, charter, reporte de defecto, resumen de pase, problemas conocidos, gate, causa raíz y modelo de prueba reusable.

---

## Los cinco gates del área

Un gate que no se puede verificar mecánicamente no es un gate, es una intención. Los cinco corren, no se piden.

| Gate | Cuándo | Qué exige | Cómo se verifica |
|------|--------|-----------|------------------|
| Entrada | toda épica que entra | versión congelada, alcance, dueño y criterios de aceptación | el bloque de build del `QA` está completo |
| Build | antes del pase profundo | verificación de build en Aceptada, o Condicional con lo que queda sin poder probarse declarado | el bloque de humo declara su resultado |
| Reverificación | todo defecto que se cierra | confirmación sobre la build del arreglo | ningún defecto cerrado sin reverificación |
| Cierre | todo `QA` que se cierra | `calidad.py --verificar` devuelve 0 | lo corre la herramienta |
| Entrega | todo `VE` que va a cerrar | `QA` en GO o CONDITIONAL GO con riesgo aceptado | el `VE` cita el `QA` y su veredicto |

---

## Los modelos de prueba reusables

Lo que el área aprende de un sistema no muere en un ticket. Cada sistema relevante puede tener su **modelo de prueba reusable**: propósito, valor para el jugador, componentes, estados, integraciones, modos de falla, defectos históricos, límites, combinaciones de alto valor, charters estándar y candidatos a regresión y a automatización.

Viven en `Modelos/`, se crean cuando existe el primero —nada se pre-crea— y usan la plantilla del área. Es lo que convierte al control de calidad en **una biblioteca acumulativa de vulnerabilidades**, en vez de una colección de tickets muertos.

Cuando un modelo deja de ser de este proyecto y pasa a ser criterio reutilizable, no se promueve solo: se deriva al Área de Conocimiento, que decide qué vuelve al Core.

---

## Límites del área

**No arregla.** Reporta, clasifica y rebota con evidencia al área dueña. Un área que encuentra y arregla deja de ser independiente.

**No decide si se entrega.** Informa la calidad y recomienda el gate. La aceptación de un riesgo puede ser del negocio, y esa aceptación queda registrada con nombre.

**No valida la experiencia.** Que el sistema se sienta bien, que la entrega valga la pena, que el jugador entienda: eso es del `VE` y del playtest. El área puede detectar **fricción observable** y la reporta como observación, no como defecto.

**No revisa arquitectura ni estilo de código.** Eso es del Revisor Técnico del Área de Programación, contra criterios del Core.

**No define alcance ni prioridad de producto.** La urgencia la decide Producción; el área declara la severidad.

**No escribe automatización.** Decide qué merece automatizarse y con qué prioridad; el código de las pruebas lo escribe el Área de Programación.

Antes de crear, mover o purgar notas del vault, pide el plano o el emplazamiento al Área de Arquitectura y lo cita en su salida.

---

## Encadenado con otras áreas

Recibe de: **Programación** (el `EJ` con su revisión técnica en OK y la build), **Producción** (el `TL`, los `RQ` y los criterios de aceptación), **Game Design**, **Level Design** y **UI/UX** (las specs que son el criterio contra el cual se compara).

Entrega a: **Producción** (el veredicto, insumo del `VE`), **Programación** (los defectos con su evidencia), **Conocimiento** (lo aprendido que merece volver al Core).

Consulta on-demand: la sección `Calidad y testing` del Core para el criterio, y la Biblioteca de la Escuela cuando el baseline del género define qué es un comportamiento esperado.

La numeración `.n` se hereda del hilo: `RQ-004.2 → GDS-004.2 → SOL-004.2 → EJ-004.2 → QA-004.2`. El `QA` de entrega cuelga del `TL` sin `.n`, igual que el `VE`.

---

## Regla operativa

Primero verificar que la entrada se puede probar.
Después decidir dónde gastar el esfuerzo.
Después comprobar que la build merece el pase.
Después ejecutar, reportar con evidencia y clasificar.
Después reverificar y proteger lo que se arregló.
Recién ahí, decidir — y escribir por qué.

---

## Regla final

**Nada sale de Control de Calidad por intuición. Sale por evidencia, riesgo conocido y una decisión explícita.**

Y nada debería volver a fallar de la misma manera sin que el área se pregunte qué prueba, qué señal o qué herramienta faltó la vez anterior.

---

## Skill del área

El área corre como la skill `vaultrum-calidad` (fuente versionada en `02_Agencia/Area control de calidad/Skills/vaultrum-calidad/SKILL.md`).

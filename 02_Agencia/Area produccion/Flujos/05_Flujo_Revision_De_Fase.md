## Propósito

El Flujo de Revisión de Fase contesta la pregunta que ningún `VE` contesta: **¿esta entrega alcanza para cambiar de fase?**

El `VE` dice si se entregó lo prometido. No dice si el proyecto ya sabe lo que la fase tenía que averiguar. Un proyecto puede cerrar diez entregas seguidas en Cerrado y seguir en Pre-Production sin saber si su núcleo funciona, porque nadie hizo la pregunta.

Y cuida lo que viene antes de la pregunta: que no se abra trabajo nuevo encima de deuda que nadie mira. Eso son las **señales de parada**.

```txt
el caso que lo motivo, medido sobre un proyecto real del vault

  4 entregas cerradas            4 QA de entrega en CONDITIONAL GO
  0 veces arranco el juego       en el gate de ninguna de las cuatro
  3 defectos mayores             listados en un QA y ausentes del siguiente, sin cerrarse
  1 timeline entero              dedicado a completar secciones de documentos
                                 mientras el juego seguia sin abrirse
  0 fase declarada               en el cuaderno
```

Ninguna de esas cosas era invisible: estaban escritas en los `QA`. Lo que faltaba era alguien que las cruzara y dijera *"acá se frena"*. En un estudio ese alguien es el productor; en Vaultrum es este flujo, con `fase.py` como instrumento.

---

## Cuándo corre

```txt
al retomar un proyecto         Paso 0 de vaultrum-produccion   las senales, antes de hablar
antes de abrir un timeline     Paso 2                          fase.py --verificar
despues de cada VE             Paso 4                          la revision de fase completa
revision periodica             a pedido o programada           fase.py 06_Proyectos --todos
```

La revisión la conduce el `01_Consultor_Estrategico`: es la misma pregunta que le hace a una idea nueva —¿conviene avanzar, ajustar o frenar?— hecha sobre un proyecto que ya tiene evidencia. **Decide el owner.** El flujo arma el caso; no firma la salida.

---

## Entrada del flujo

- el cuaderno del proyecto, con la fase y el modelo de negocio declarados,
- el último `VE` y el `QA` de entrega que cita,
- la lectura `MET-XXX` si hubo playtest,
- la salida de `fase.py <proyecto> --salida`.

Si la fase no está declarada, el flujo no arranca: no hay contra qué revisar. Producción la declara primero.

---

## Las señales de parada

Una señal de parada **no prohíbe trabajar**: prohíbe abrir un timeline de trabajo nuevo como si no pasara nada. Con una parada activa hay dos salidas, y las dos se escriben:

```txt
a) el proximo timeline ataca la parada, y solo eso
b) el owner la acepta por escrito para esta entrega, en el registro del cuaderno:
   | PRJ-0NN | AAAA-MM-DD | parada S6 tras VE-XXX | Confirmado | <por que se sigue igual> | -- |
```

La aceptación vale hasta la entrega siguiente. Con un `VE` nuevo, se vuelve a decidir.

```txt
S1  fase sin declarar                    el cuaderno no dice en que fase esta el proyecto
                                         -> cualquier area que mida contesta la pregunta de otra fase
S2  cuaderno atrasado                    el cuaderno no nombra el ultimo TL o el ultimo VE
                                         -> se compara el TEXTO, no la fecha del archivo
S3  entrega abierta debajo de otra       un TL sin VE y un timeline posterior ya abierto
S4  deuda arrastrada                     un defecto mayor o peor, abierto en las dos ultimas entregas
S5  defecto desaparecido                 un defecto abierto en un QA que no aparece en ningun QA posterior
                                         -> parada si es mayor o peor; aviso si es menor
S6  el juego no arranco                  las dos ultimas entregas cerraron sin "arranque ok" en qa-humo
S7  fase con jugadores sin playtest      Testing o posterior, y ninguna lectura MET-XXX
S8  codigo sin diseno                    un RQ de un timeline abierto tiene SOL o EJ, no tiene GDS
                                         y no declara que no es jugable
S9  fase sin revisar                     el ultimo VE no tiene su fila "fase: revision tras VE-XXX"
```

Las nueve son mecánicas: `fase.py` las lee de los archivos del proyecto y ninguna depende de interpretar prosa. Es a propósito. Una señal que se puede discutir no frena nada.

---

## Cuándo la documentación ya no alcanza

Es la pregunta de fondo detrás de las señales S2 y S8, y tiene tres respuestas distintas según qué falla:

```txt
la memoria no alcanza    el cuaderno no nombra lo ultimo que paso (S2)
                         -> Produccion lo pone al dia antes de responder nada
el diseno no alcanza     hay codigo sobre un requerimiento jugable sin GDS (S8)
                         -> se frena el hilo y Game Design cierra su GDS
documentar no alcanza    la pregunta abierta se contesta jugando, no escribiendo
                         -> el Documentador para y se prototipa (flujo 07 de Conocimiento)
```

Y la cantidad de documento que pide cada fase no es la misma. Documentar de más en Pre-Production es tan caro como documentar de menos en Production:

```txt
Planning         el cuaderno, el verbo en una oracion, el presupuesto de contenido, la lista NO
Pre-Production   por prototipo: la pregunta, la fecha de corte y el criterio de exito, en el RQ.
                 El GDS de un prototipo tiene las secciones del contrato y cabe en una pagina:
                 se tira con el codigo
Production       el GDS de produccion de cada sistema ANTES de su SOL (S8 lo mide), y LDS, UXS,
                 ART y MET segun apliquen. Un prototipo no se promueve a produccion sin su GDS
Testing          el plan de playtest (MET-XXX.n) antes de jugar y la lectura (MET-XXX) despues.
                 Un GDS nuevo en Testing necesita una lectura que lo pida
```

---

## Los criterios de salida

`fase.py --salida` lee este bloque. Cada línea es `medido <clave>` —la mide el instrumento sobre los archivos— o `juicio` —la firma el owner, y el instrumento la lista sin opinar—. Una clave que el instrumento no conoce es un error, no un silencio.

Los criterios salen del libro `17_Scope_prototipado_y_cierre`, de `13_Playtesting_y_validacion` y de la nota del Core `Fases del producto y que medir`. Las fases de Launch en adelante no se cierran con una lista: son ciclos, y su criterio queda escrito para cuando haya un caso.

```txt
PLANNING          vale la pena construirlo?
  medido modelo       el modelo de negocio esta declarado
  medido senales      ninguna parada activa sin aceptar
  juicio              el juego entra en una oracion de 15 palabras o menos, con un verbo principal
  juicio              el presupuesto de contenido esta hecho y el calendario sale derivado de el
  juicio              la lista NO existe
  juicio              cada prototipo de Pre-Production tiene escrita su pregunta y su fecha de corte

PRE-PRODUCTION    funciona el nucleo?
  medido senales      ninguna parada activa sin aceptar
  medido build        la build de la ultima entrega arranco en el gate de Calidad
  medido deuda        la ultima entrega no deja defectos mayores o peores abiertos
  medido met          hay una lectura de Metricas sobre un playtest
  juicio              el prototipo de feel paso: el verbo se siente bien en una sala vacia
  juicio              la prueba de comprension paso: 4 de 5 testers juegan 2 minutos sin ayuda
  juicio              existe una vertical slice honesta de 3 a 10 minutos a calidad final
  juicio              el costo por minuto de juego esta medido sobre la slice y el calendario se rehizo
  juicio              los sistemas que pasan a produccion tienen su GDS de produccion, no el del prototipo

PRODUCTION        los sistemas funcionan como deberian?
  medido senales      ninguna parada activa sin aceptar
  medido build        la build de la ultima entrega arranco en el gate de Calidad
  medido entregas     todos los timelines tienen su VE
  medido bloqueantes  ningun bloqueante ni critico abierto
  juicio              feature freeze escrito en el registro del cuaderno: nada nuevo desde ahi
  juicio              content lock: el contenido esta completo y congelado
  juicio              alguien externo jugo una build de este mes
  juicio              tareas cerradas sobre tareas creadas, 1 o mas en las ultimas 4 semanas

TESTING           el jugador real se comporta como esperaba el diseno?
  medido senales      ninguna parada activa sin aceptar
  medido build        la build de la ultima entrega arranco en el gate de Calidad
  medido met          hay una lectura de Metricas sobre el playtest
  medido deuda        la ultima entrega no deja defectos mayores o peores abiertos
  medido bloqueantes  ningun bloqueante ni critico abierto
  juicio              la lectura contesta la pregunta de la fase: expectativa contra realidad, con hechos
  juicio              bug bar: 0 crashes, 0 softlocks, 5 cosmeticos conocidos o menos
  juicio              lo que la lectura pidio cambiar esta hecho, o esta en la lista NO

PRE-LAUNCH        funciona como producto completo antes de escalar?
  medido senales      ninguna parada activa sin aceptar
  medido build        la build de la ultima entrega arranco en el gate de Calidad
  medido met          hay una lectura de Metricas del soft launch o la beta
  medido bloqueantes  ningun bloqueante ni critico abierto
  juicio              la lectura mide retencion y funnel contra su objetivo, con los KPIs del modelo de negocio
  juicio              existe una fecha de release escrita, aunque sea un rango de un mes

LAUNCH            que pasa con el mercado real, a escala?
  medido senales      ninguna parada activa sin aceptar
  medido met          hay una lectura de Metricas en modo Salud sobre la primera cohorte
  juicio              la primera cohorte llego a su D30 y la lectura la compara contra el soft launch

POST-LAUNCH       como evoluciona?
  medido senales      ninguna parada activa sin aceptar
  medido met          hay una lectura de Metricas en modo Salud
  juicio              existe una cadencia de actualizaciones y cada una se mide contra la anterior

LIVE OPS          como se mantiene y mejora un producto vivo?
  medido senales      ninguna parada activa sin aceptar
  medido met          hay una lectura de Metricas en modo Salud
  juicio              cada evento declara su objetivo y su medicion antes de salir
```

---

## Qué aporta cada área

```txt
Control de Calidad   la evidencia de que el juego corre y de cuanta deuda queda: qa-humo
                     ("arranque ok") y qa-defectos del QA de entrega. La entrega que propone
                     cerrar una fase corre en perfil Completo, y ningun defecto abierto
                     desaparece de un QA al siguiente
Metricas             la lectura MET-XXX que contesta la pregunta de la fase, con los hechos
                     separados de las hipotesis. De Testing en adelante, sin ella no hay caso
Produccion           el caso armado, la recomendacion del Consultor Estrategico y el registro
                     de la decision en el cuaderno
el owner             los juicios, y la decision
```

---

## Las cuatro salidas

```txt
AVANZAR   la fase respondio su pregunta: el cuaderno cambia de fase, y el proximo timeline
          declara la nueva en su Objetivo
SEGUIR    todavia no: el proximo timeline ataca lo que falta del criterio, y solo eso
VOLVER    la evidencia contradice la fase declarada: se baja una. Production que descubre
          que el nucleo no se entiende vuelve a Pre-Production, y no es un fracaso: es la
          fase haciendo su trabajo
CORTAR    la respuesta es no: se recorta alcance en el orden del libro 17 (cantidad, variedad,
          sistemas secundarios, modos, narrativa, fidelidad; el core loop nunca), o se cierra
          el proyecto
```

La decisión se registra en la sección 5 del cuaderno, con la fila que `fase.py` busca:

```txt
| PRJ-0NN | AAAA-MM-DD | fase: revision tras VE-XXX | Confirmado | SEGUIR en Pre-Production -- <por que> | -- |
```

Si la salida es AVANZAR, la sección 3 cambia de fase **en la misma pasada**. Una fase decidida en el registro y no escrita en el estado es la señal S1 o la S2 esperando la próxima sesión.

---

## Criterios de aceptación

El flujo puede darse por cerrado cuando:

- `fase.py --salida` corrió y su salida está citada en el `VE` o en la respuesta al owner,
- cada criterio medido tiene su evidencia, y cada juicio tiene una respuesta del owner o dice que no la tiene,
- la recomendación del Consultor nombra una de las cuatro salidas y dice por qué,
- la decisión del owner está en el registro del cuaderno,
- si la salida fue AVANZAR, la sección 3 del cuaderno ya dice la fase nueva.

---

## Qué debe evitar

No avanza de fase con un criterio medido en falta. Si el owner decide avanzar igual, eso es una aceptación escrita con su razón, no un avance limpio.

No convierte los juicios en medidos. Que el instrumento no pueda leer "la prueba de comprensión pasó" no autoriza a darla por pasada.

No decide por el owner, ni en nombre de la velocidad. Un SEGUIR bien argumentado vale más que un AVANZAR por cansancio.

No revisa la fase leyendo documentos. La evidencia de Pre-Production en adelante sale del juego corriendo y de gente jugándolo.

---

## Lo que todavía no se sabe

El flujo nace sin una sola revisión de fase hecha. Las nueve señales se probaron contra dos proyectos reales del vault, leyendo sus archivos sin tocarlos; los criterios de salida, contra ninguno. Los umbrales del libro 17 —4 de 5 testers, 3 a 10 minutos de slice, 5 cosméticos— son un baseline para un dev solo, y el propio libro pide reemplazarlos por los medidos en la primera vertical slice. La primera revisión real corrige esta nota.

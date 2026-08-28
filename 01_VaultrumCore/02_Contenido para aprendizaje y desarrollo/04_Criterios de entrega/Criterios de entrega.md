## Proposito

Esta seccion reune los criterios que responden una sola pregunta:

```txt
Cuando algo esta terminado?
```

No es una seccion de tecnica. Es la seccion que define **que se le puede exigir a una entrega** antes de darla por hecha, y que vocabulario usar cuando la respuesta no es un si o un no limpio.

Existe porque el resto del Core sabe construir bien y no sabia declarar terminado. SOLID, patrones, optimizacion, estructuras, algoritmos y managers responden *como se construye*. Ninguno responde *cuanto alcanza*.

---

## Por que existe esta seccion

Los criterios de abajo no se inventaron: salieron de entregas reales.

El ciclo `TL-002 → TL-003` del Pong 3D produjo tres aprendizajes que no entraban en ninguna seccion existente:

```txt
la entrega estaba completa en maquinaria y vacia en experiencia
la verificacion era binaria: o gate cerrado o nada
la cadena fallaba en los bordes, no en el medio
```

Los tres son criterios de entrega. Ninguno es de optimizacion, de arquitectura ni de diseno. Por eso la seccion.

El cuarto —`Alcance del instrumento`— llego despues y por otra via: no de una entrega de proyecto, sino de dos pasadas sobre las herramientas del propio vault. Confirma la regla de esta seccion en vez de romperla: tambien salio de algo que paso, no de algo que sonaba razonable.

Los tres siguientes entraron el 2026-08-28, de una pasada de cierre sobre el sistema. Los tres traen la evidencia que esta seccion exige —tres apariciones en dominios distintos cada uno— y ninguno sale de una intuicion:

```txt
Direccion de falla de un guardrail   tres instrumentos rotos hacia el mismo lado
La superficie del ejecutor           cuatro superficies, la spec correcta en las cuatro
Conocimiento cargado o archivado     un libro y una seccion entera del Core sin consumidor
```

Es tambien la unica parte del Core que nacio del uso del propio sistema y no de bibliografia externa. Eso la hace la mas fragil y la que mas evidencia necesita antes de crecer: una nota entra aca cuando una entrega real la produjo, no cuando suena razonable.

---

## Alcance

Estos criterios aplican a **cualquier entregable**, no solo a videojuegos.

Un juego, una herramienta, un script, un documento o un sistema comparten la misma estructura de problema: alguien pidio algo, alguien lo construyo, y hay que decidir si esta hecho. Lo que cambia por dominio es *que* cuenta como baseline de experiencia — no la regla de que tiene que haber uno.

Donde un criterio sea especifico de videojuegos, lo dice.

---

## [[Baseline de entregable]]

> **Completo en experiencia, minimo en maquinaria.**

El criterio central. Define que trae una entrega sin que haya que pedirlo, y que no trae aunque se pueda.

Responde:

- que son las *table-stakes* de un tipo de entregable;
- por que entregar lo minimo funcional no es entregar lo minimo satisfactorio;
- por que una decision tecnica sin requerimiento detras es alcance no pedido;
- como se prueba cada una de las dos mitades.

Usar esta nota cuando haya que decidir **que entra** en una entrega, antes de construir.

---

## [[Verificacion parcial declarada]]

Entre *"no se verifico nada"* y *"se probo en el entorno real"* hay terreno util, y hasta ahora no tenia nombre.

Responde:

- como se declara una verificacion que cubre algo y no todo;
- por que una verificacion sin alcance declarado se lee como cierre;
- por que un juicio global tampoco reemplaza al instrumento.

Usar esta nota cuando **no se pueda verificar en el entorno de destino** y haya que declarar lo que si se sabe.

---

## [[Gates verificables]]

> **Un gate que no se puede verificar mecanicamente no es un gate: es una intencion.**

Responde:

- por que las cadenas de trabajo fallan en los bordes y no en el medio;
- que diferencia un criterio escrito de un paso ejecutable;
- como convertir el segundo en el primero.

Usar esta nota al **disenar o revisar un flujo de trabajo**, propio o de la Agencia.

---

## [[Alcance del instrumento]]

> **Una ley que el instrumento no mide no esta vigente: esta escrita.**

El criterio hermano de `Gates verificables`, por el lado de la herramienta. Aquel dice que un gate sin comprobacion mecanica es una intencion; este dice que un gate mecanico que corre y devuelve cero tampoco alcanza si mide de menos, reconoce las excepciones por su rotulo, o mide un artefacto que no es el que se entrega.

Responde:

- por que un gate en verde puede estar declarando cumplida una regla que nadie prueba;
- por que una excepcion implementada por su nombre es la puerta de lo que la ley prohibe;
- por que un veredicto cierto sobre el artefacto equivocado no sirve;
- que diferencia hay entre declarar una decision y declarar un defecto.

Usar esta nota cuando haya que **escribir o revisar un gate**, no cuando haya que decidir el alcance de una entrega.

---

## [[Direccion de falla de un guardrail]]

> **Todo guardrail tiene una direccion de falla, y hay que elegirla al escribirlo.**

`Alcance del instrumento` pregunta si la medicion cubre la regla. Esta pregunta de que lado cae el instrumento **cuando se equivoca**, que es una asimetria y no una cobertura.

Responde:

- por que un instrumento que falla hacia *segui* es peor que no tenerlo;
- como se calcula cual de los dos errores es el caro;
- por que *"no encontre nada"* y *"no se"* no son la misma respuesta.

Usar esta nota al **escribir un chequeo que le da permiso a alguien** para hacer o no hacer trabajo.

---

## [[La superficie del ejecutor]]

> **Una spec cerrada dice que hacer. Falta la linea que dice donde tiene que poder correr.**

Responde:

- por que una spec completa igual falla cuando la ejecuta otro;
- que se comprueba antes de delegar, y con que prueba barata;
- por que un fallo mencionado al final se lee como color y no frena nada.

Usar esta nota antes de **delegar algo que produce un artefacto** a un ejecutor que no es uno mismo.

---

## [[Conocimiento cargado o archivado]]

> **Un cuerpo de conocimiento que ningun consumidor nombra no esta cargado: esta archivado.**

Responde:

- por que el inventario no mide cobertura y la lista de consulta si;
- como se detecta un area trabajando sin su propio material;
- por que buscar antes de encargar estudio es el ahorro mas grande y el mas olvidado.

Usar esta nota al **escribir conocimiento nuevo, armar la lista de consulta de un rol, o encargar una mision de estudio**.

---

## Como se relacionan

Los tres cubren momentos distintos de la misma entrega:

```txt
antes de construir    → Baseline de entregable            (que tiene que traer)
durante               → Verificacion parcial              (que sabemos hasta ahora)
al disenar el flujo   → Gates verificables                (como se comprueba sin criterio subjetivo)
al escribir el gate   → Alcance del instrumento           (si la comprobacion prueba lo que dice)
                      → Direccion de falla de un guardrail (de que lado cae cuando se equivoca)
antes de delegar      → La superficie del ejecutor        (si el otro puede, no si sabe)
antes de escribir     → Conocimiento cargado o archivado  (si lo escrito le va a llegar a alguien)
```

El primero define la vara. El segundo define como se habla de una medicion incompleta. El tercero define como se comprueba sin depender del juicio de quien mira. El cuarto cierra el circulo: comprueba la comprobacion.

`Gates verificables` y `Alcance del instrumento` son el mismo criterio en dos tiempos: aquel se pregunta si la regla **puede** medirse; este, si la medicion que existe **la mide de verdad**, y sobre que cosa. `Direccion de falla de un guardrail` agrega el tercer tiempo, que es el unico que sigue valiendo cuando la medicion es correcta: **de que lado se rompe.**

Los dos ultimos cubren los bordes de la entrega en vez de su medio. `La superficie del ejecutor` mira hacia adelante —quien va a hacer esto, ¿puede?— y `Conocimiento cargado o archivado` hacia atras —lo que hace falta para hacerlo bien, ¿le llega a alguien?

---

## Relacion con la Agencia

La Agencia **aplica** estos criterios; no los define.

```txt
Baseline de entregable    → Produccion (RQ) y Game Design (GDS)
Verificacion parcial      → Programacion (EJ), Control de Calidad (QA) y Produccion (VE)
Gates verificables        → toda skill que declare un paso obligatorio
Alcance del instrumento   → Arquitectura, Conocimiento, UI/UX y Control de Calidad
                            (las cuatro areas que miden con herramienta propia)
Direccion de falla        → las mismas cuatro, mas la Escuela (su dedup autoriza misiones)
La superficie del ejecutor → Programacion (el SOL y su Contrato de ejecucion) y la capa
                            de Despacho, que es la que reparte entre ejecutores
Conocimiento cargado      → Escuela y Conocimiento, y toda skill que declare de que lee
```

Si una skill y esta seccion divergen, la seccion es la fuente de criterio y la skill es el procedimiento. Se corrige la skill.

---

## Regla de esta seccion

Un criterio entra aca cuando cumple las tres:

```txt
salio de una entrega real, no de una intuicion
se puede aplicar fuera del proyecto que lo produjo
se puede comprobar sin depender de quien lo mira
```

Si falla la tercera, todavia no es un criterio. Es una buena idea.

## Proposito

Esta seccion reune los criterios que responden una sola pregunta:

```txt
Cuando algo esta terminado?
```

No es una seccion de tecnica. Es la seccion que define **que se le puede exigir a una entrega** antes de darla por hecha, y que vocabulario usar cuando la respuesta no es un si o un no limpio.

Existe porque el resto del Core sabe construir bien y no sabia declarar terminado. SOLID, patrones, optimizacion, estructuras, algoritmos y managers responden *como se construye*. Ninguno responde *cuanto alcanza*.

---

## Por que existe esta seccion

Los tres criterios de abajo no se inventaron: salieron de una entrega real.

El ciclo `TL-002 → TL-003` del Pong 3D produjo tres aprendizajes que no entraban en ninguna seccion existente:

```txt
la entrega estaba completa en maquinaria y vacia en experiencia
la verificacion era binaria: o gate cerrado o nada
la cadena fallaba en los bordes, no en el medio
```

Los tres son criterios de entrega. Ninguno es de optimizacion, de arquitectura ni de diseno. Por eso la seccion.

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

## Como se relacionan

Los tres cubren momentos distintos de la misma entrega:

```txt
antes de construir   → Baseline de entregable      (que tiene que traer)
durante              → Verificacion parcial        (que sabemos hasta ahora)
al disenar el flujo  → Gates verificables          (como se comprueba sin criterio subjetivo)
```

El primero define la vara. El segundo define como se habla de una medicion incompleta. El tercero define como se comprueba sin depender del juicio de quien mira.

---

## Relacion con la Agencia

La Agencia **aplica** estos criterios; no los define.

```txt
Baseline de entregable    → Produccion (RQ) y Game Design (GDS)
Verificacion parcial      → Programacion (EJ), Control de Calidad (QA) y Produccion (VE)
Gates verificables        → toda skill que declare un paso obligatorio
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

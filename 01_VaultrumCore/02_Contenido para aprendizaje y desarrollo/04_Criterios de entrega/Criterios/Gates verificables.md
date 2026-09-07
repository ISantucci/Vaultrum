## Que es

> **Un gate que no se puede verificar mecanicamente no es un gate: es una intencion.**

Un *gate* es un punto de una cadena de trabajo donde algo no avanza hasta cumplir una condicion. Para que funcione, la condicion tiene que poder comprobarse **sin depender del criterio de quien mira**.

Si para saber si el gate se cumplio hay que hacer un juicio, el gate no frena nada: frena a quien es cuidadoso y deja pasar a quien tiene apuro. Que es exactamente al reves de lo que se queria.

---

## Por que existe

Cuando una entrega sale mal, el instinto es sospechar del medio de la cadena. La evidencia dice lo contrario: **el medio funciona y los bordes no.**

**Origen:** comparacion entre `TL-002` y `TL-003` del Pong 3D. `TL-002` tenia requerimientos, especificacion de diseno, solucion tecnica y ejecucion de buena calidad — tanto que varias de sus piezas se releyeron y reutilizaron para escribir `TL-003`. Y sin embargo la entrega quedo en PAUSADO y su implementacion **nunca llego a estar en disco**.

Los tres fallos fueron de borde:

| Borde | Que fallo | Por que es de borde |
|---|---|---|
| **Entrada** | El libro de referencia del genero estaba vacio. Las table-stakes las puso el criterio de quien escribio el requerimiento | Nadie verifico que el insumo existiera antes de consumirlo |
| **Ramas opcionales** | Un paso opcional se declaro *no aplica*. El trabajo se hizo igual, mas abajo, como desvio | "No aplica" se acepto como afirmacion sin prueba |
| **Salida** | La entrega no aterrizo en la carpeta destino y nadie lo detecto hasta releerla | Nadie verifico la existencia del artefacto |

Ninguno de los tres es un problema de calidad del trabajo. Los tres son gates que existian escritos y no existian ejecutables.

---

## Las tres reglas de borde

Salen del caso de arriba y son generalizables a cualquier cadena.

### 1. El insumo se verifica antes de consumirlo

Un paso que declara depender de un insumo **comprueba que el insumo existe y no esta vacio** antes de arrancar. Si falta, eso dispara la produccion del insumo — no se sigue de largo con criterio propio.

```txt
mal:  el paso asume el insumo y lo suple con intuicion si falta
bien: el paso comprueba el insumo; si falta, se marca y se deriva
```

Es la diferencia entre una intencion y un mecanismo: la intencion dice "hay que partir del conocimiento disponible", el mecanismo comprueba que ese conocimiento este ahi.

### 2. Un "no aplica" es una afirmacion verificable, no un atajo

Cuando un paso es opcional, declarar que no aplica exige decir **que dimension del entregable esta ausente**. No alcanza con marcar la casilla.

Y tiene una prueba a posteriori, que es lo que la hace un gate y no una recomendacion:

```txt
TEST DEL "NO APLICA"
  la siguiente etapa tuvo que hacer ese trabajo igual?
    si  → el "no aplica" era falso
    no  → el "no aplica" era correcto
```

Si el trabajo de un paso "no aplicable" reaparece mas abajo como desvio declarado, la declaracion original era un atajo. El test se corre al cerrar, sobre lo que efectivamente paso.

### 3. Existir es parte del cierre

Un paso no esta reportado si el artefacto no esta donde el plan dice que va. No "esta escrito", no "esta disenado": **esta en la ruta destino**.

```txt
mal:  el reporte describe lo que se hizo
bien: el reporte describe lo que se hizo y verifica que este donde va
```

Es la mas tonta de las tres y es la que hundio una entrega entera.

---

## Como convertir un criterio en gate

El patron es siempre el mismo:

```txt
1. Escribir la condicion como pregunta de si/no.
2. Si la respuesta requiere juicio, la condicion todavia no sirve. Reescribirla.
3. Definir que se hace cuando la respuesta es "no" — y que ese camino exista.
4. Ponerlo en el procedimiento ejecutable, no solo en la documentacion.
```

El paso 4 es el que se saltea. Un criterio que vive solo en el documento del area es una intencion; el mismo criterio como paso numerado del procedimiento que efectivamente corre es un gate.

**Prueba de si un gate es real:** si alguien apurado puede pasarlo sin darse cuenta de que lo paso, no es un gate.

---

## La otra mitad: el gate que existe, corre, y alguien lo saltea igual

Todo lo de arriba resuelve el gate que **no se puede** verificar. Falta el caso que el Area de Arte midio cuatro veces, y que es peor porque no se parece a un hueco:

> **El gate existe, corre, y una inspeccion humana confiada lo saltea igual, porque la pieza se ve bien.**

Cuatro defectos reales pasaron una inspeccion visual perfecta: una pieza corrida en tres ejes, dos piezas hundidas mas de cien milimetros, un objeto medido en dos marcos de coordenadas distintos, y un personaje con partes adentro del torso. Los cuatro los encontro el instrumento. Ninguno se veia.

La leccion no es que la vista sea mala: es que **la vista contesta otra pregunta**. Mirar responde *"¿esto parece estar bien?"*, y el instrumento responde *"¿esto cumple la regla?"*. Las dos preguntas coinciden casi siempre, y el "casi" es exactamente donde vive el defecto que va a llegar a la entrega.

```txt
lo que la vista hace bien    encontrar lo que no se penso: una silueta que no
                             comunica, un ritmo raro, algo que molesta
lo que la vista NO hace      confirmar una regla. Para eso esta el numero.
```

Por eso un gate mecanico **no se aprueba mirando**, ni siquiera cuando quien mira construyo la cosa y esta seguro. Sobre todo entonces: el que construye es el peor juez de lo que construyo, porque revisa contra lo que quiso hacer y no contra lo que hizo.

## Cuando NO aplica

- **No todo tiene que ser un gate.** Un gate por cada criterio produce una cadena que nadie corre. Los gates van en los bordes —entrada, ramas opcionales, salida— porque ahi es donde falla.
- **No convierte juicio en mecanica.** "Esto es divertido" no se puede volver verificable, y forzarlo produce checklists que se tildan sin mirar. Lo verificable es *que se haya corrido la checklist*, no que el resultado sea bueno.
- **No agrega pasos al medio.** Si la parte central de la cadena funciona, meterle gates la vuelve mas lenta sin volverla mas segura.

---

## Regla final

```txt
Un criterio escrito le recuerda algo a quien ya lo iba a hacer.
Un gate ejecutable frena a quien no.
```

La diferencia se paga en los bordes.

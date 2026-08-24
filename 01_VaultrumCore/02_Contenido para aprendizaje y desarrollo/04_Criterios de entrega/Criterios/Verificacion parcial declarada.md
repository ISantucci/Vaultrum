## Que es

Una entrega puede verificarse **parcialmente** sin el entorno de destino, siempre que la verificacion declare su alcance: **que cubre y que no**, en el mismo parrafo.

```txt
"no se verifico nada"  ←  terreno util  →  "se probo en el entorno real"
                             ↑
                    verificacion parcial declarada
```

Ese terreno del medio existe siempre y casi nunca tiene nombre. Sin nombre, se lo trata como uno de los dos extremos — y las dos lecturas son falsas.

---

## Por que existe

El problema es que una verificacion sin alcance declarado **se lee como cierre**.

Si alguien dice "verifique la entrega" y en realidad reviso el codigo sin ejecutarlo, quien lo lee entiende que la entrega esta verificada. No mintio: omitio el alcance. El resultado es el falso *Cerrado* que los gates existen para evitar.

La regla no agrega un gate nuevo ni debilita ninguno. Agrega **vocabulario para lo que pasa antes del gate**.

**Origen:** `EJ-003` / `VE-002` / `VE-003` del Pong 3D. `VE-002` habia quedado en PAUSADO con un diagnostico correcto —*"verificar el codigo no es verificar la entrega"*— que sin embargo dejaba un binario. En `EJ-003` se compilaron 17 scripts fuera del motor, contra un stub de la API, en dos configuraciones de defines. Eso cerro una clase entera de errores (sintaxis, tipos, firmas) sin poder abrir el editor, y encontro un bug real que solo habria aparecido en runtime.

No convirtio un PAUSADO en Cerrado. Convirtio *"no sabemos nada"* en *"sabemos esto y no aquello"*, que es una posicion de trabajo distinta.

---

## La regla

> Toda verificacion que no sea la del gate declara **que cubre y que no**, en el mismo parrafo.

Dos partes, ninguna opcional:

1. **Que se verifico** — el metodo concreto, no la intencion. No "se reviso"; si "se compilo fuera del entorno contra un stub".
2. **Que clase de error queda viva** — no una lista de bugs posibles, sino la *clase*. "Todo lo que dependa de que el entorno resuelva sus recursos en runtime."

---

## Formato

```txt
VERIFICACION PARCIAL

Metodo:      que se hizo, concretamente
Cubre:       que clase de error queda descartada
No cubre:    que clase de error sigue viva
Consecuencia: que estado habilita (y cual no)
```

Ejemplo real:

```txt
VERIFICACION PARCIAL

Metodo:      compilacion de los 17 scripts fuera del motor, contra un stub
             de la API, en las dos configuraciones de defines de entrada.
Cubre:       sintaxis, tipos, firmas, referencias a API inexistente.
No cubre:    nada que dependa del runtime del motor — resolucion de recursos,
             generacion de escena, comportamiento en Play, encuadre de camara.
Consecuencia: habilita reportar la ejecucion. NO habilita cerrar la entrega.
```

Lo que hace util al formato es la tercera linea. Sin ella, las dos primeras se leen como tramite.

---

## Corolario — el juicio global tampoco reemplaza al instrumento

El movimiento inverso vale igual y se olvida mas seguido.

En `VE-003` el owner jugo el juego y dijo 8/10, *"es divertido"*. Es informacion real, de primera mano, y suficiente para cerrar una entrega. Pero los 18 items de la definicion de terminado no se recorrieron uno por uno.

```txt
un 8/10 dice que el conjunto funciona
no dice cual de los dieciocho falla
```

Los dos son verificaciones parciales. El juicio global cubre la impresion de conjunto y no cubre el detalle; la checklist cubre el detalle y no cubre si el conjunto se sostiene. **Ambos declaran su alcance o los dos mienten por omision.**

---

## Cuando NO aplica

- **No sustituye al gate.** Una verificacion parcial, por bien declarada que este, no cierra lo que el gate exige. Si el gate pide el entregable corriendo, el gate pide el entregable corriendo.
- **No es excusa para no verificar.** Declarar el alcance no es gratis: obliga a nombrar lo que quedo sin cubrir, y eso suele mostrar que se podia cubrir mas.
- **No aplica a hallazgos.** Un bug encontrado es un bug encontrado, con o sin alcance declarado.

---

## Regla final

```txt
Una verificacion sin alcance declarado se lee como cierre.
Con alcance declarado, es una posicion de trabajo.
```

Nombrar lo que no se sabe es parte de saber.

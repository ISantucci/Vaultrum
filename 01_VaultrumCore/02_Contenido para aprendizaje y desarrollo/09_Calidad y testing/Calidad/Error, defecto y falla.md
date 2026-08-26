## Que es

Tres palabras para tres cosas distintas que la conversacion diaria llama "bug".

```txt
error     una persona se equivoca            un malentendido, un descuido, una suposicion
defecto   el error queda escrito             en el codigo, en el dato, en la spec, en la config
falla     el defecto se manifiesta           el sistema se comporta distinto de lo esperado
```

La cadena tiene una direccion y no siempre se completa:

```txt
error de una persona → defecto en el artefacto → (si se ejecuta esa linea, con esos datos,
en ese estado) → falla observable → impacto en quien lo usa
```

Un defecto puede vivir anos sin producir una sola falla, porque nadie llego a ese estado. Eso no lo vuelve inofensivo: lo vuelve **invisible hasta que alguien llega**. Y quien llega primero suele ser un jugador, no un tester.

Al reves tambien pasa: hay fallas sin defecto en el producto. Un driver, un sistema operativo, un disco lleno, una red caida o un dato corrupto de afuera producen comportamiento erroneo sin que el codigo tenga nada mal. Distinguirlo temprano evita perseguir un defecto que no existe.

---

## Por que importa la distincion

Porque cada eslabon se ataca distinto.

| Eslabon | Como se ataca |
|---|---|
| error | requisitos claros, criterios de aceptacion, revision, pares, menos ambiguedad |
| defecto | revision de codigo, analisis estatico, pruebas unitarias, tipos |
| falla | pruebas de sistema, exploratorio, telemetria, reportes de jugadores |
| impacto | mitigacion, workaround, comunicacion, decision de riesgo |

Un equipo que solo trabaja sobre fallas esta atacando el ultimo eslabon de la cadena: el mas visible, el mas tardio y el mas caro.

---

## Los principios del testing

No son teoria de manual: cada uno explica un error operativo que se comete todo el tiempo.

### 1. El testing muestra presencia de defectos, no ausencia

Encontrar defectos prueba que hay defectos. No encontrarlos no prueba nada sobre lo que no se probo.

Por eso una entrega **nunca** se declara "sin bugs". Se declara: *se ejecuto esto, con este resultado, y esto quedo sin ejecutar*.

### 2. Probarlo todo es imposible

Salvo en casos triviales, el espacio de entradas, estados y combinaciones es demasiado grande. Un sistema con diez opciones binarias tiene 1.024 combinaciones; sumale el orden en que se activan y el numero deja de importar porque ya no se puede recorrer.

La consecuencia no es "probemos menos": es **elegir con criterio**, que es de lo que trata `Tecnicas de diseno de pruebas` y `Testing basado en riesgo`.

### 3. Cuanto antes, mas barato

Un defecto de requisitos detectado al escribir el requisito cuesta una conversacion. El mismo defecto detectado despues de construir cuesta rehacer el diseno, el codigo, las pruebas y la documentacion — y si salio publicado, ademas cuesta la confianza.

Por eso una revision de una spec ambigua es testing, aunque no se ejecute nada.

### 4. Los defectos se agrupan

No se reparten parejo. Una minoria de modulos concentra la mayoria de los defectos: los mas complejos, los mas tocados, los mas nuevos, los que integran varios sistemas y los que nadie entiende del todo.

Uso practico: **el historial de defectos es un mapa de donde buscar**. Un sistema que ya fallo tres veces es el mejor candidato para el proximo pase, no el que nunca dio problemas.

### 5. La paradoja del pesticida

Un set de pruebas que se repite igual deja de encontrar defectos nuevos: ya mato todo lo que sabia matar. Que la suite pase entera no significa que el sistema este sano; significa que no aprendio nada nuevo.

Uso practico: la regresion protege lo conocido, y **hace falta ademas exploracion** que busque donde nadie miro.

### 6. El testing depende del contexto

Un prototipo interno, un juego que se muestra manana en una feria y un sistema que maneja dinero no se prueban igual. No hay una cantidad correcta de testing: hay una cantidad correcta **para este riesgo**.

### 7. La ausencia de defectos es una falacia

Un sistema puede tener cero defectos conocidos y aun asi ser inutil: resuelve el problema equivocado, o resuelve el correcto de una forma que nadie quiere usar.

Cumplir la especificacion no es lo mismo que servir. Por eso el gate de calidad informa, y la decision de entregar es de quien es dueno del producto.

---

## Ejemplo completo de la cadena

```txt
error      quien escribio el requisito asumio que "descartar" siempre pide confirmacion
defecto    el codigo del inventario borra el item sin pasar por el popup si se suelta afuera
falla      el jugador pierde un item unico sin ver ninguna confirmacion
impacto    progresion bloqueada, save inservible, un ticket de soporte por cada jugador que lo hizo
```

Cada eslabon tenia su momento de deteccion barato: una pregunta al escribir el requisito, una revision del codigo, una prueba de limite. El que se pago fue el ultimo.

---

## Regla final

```txt
Que no haya aparecido no significa que no este.

Un informe honesto dice que se ejecuto, que no,
y donde queda el riesgo que nadie miro.
```

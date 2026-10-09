## Que es

Un criterio sobre **hacia donde se rompe** un instrumento cuando se rompe.

> **Todo guardrail tiene una direccion de falla, y hay que elegirla al escribirlo.**

`Alcance del instrumento` pregunta si la medicion cubre la regla. Esta nota pregunta otra cosa, y es independiente: **cuando el instrumento se equivoca, ¿de que lado cae?** Un gate puede medir exactamente lo que dice medir y aun asi ser peligroso, porque su modo de fallar autoriza en vez de frenar.

Las cuatro formas de fallar de `Alcance del instrumento` son de cobertura. Esta es de **asimetria**: dos errores del mismo instrumento no cuestan lo mismo.

---

## Por que existe

Salio de tres instrumentos del propio vault, en tres dominios distintos, todos rotos hacia el mismo lado.

```txt
biblioteca.py --dedup   buscaba la frase entera como substring. Una consulta de dos
                        palabras -- que es como se enuncia un gap real -- no encontraba
                        nada y contestaba "nada cubre esto todavia, la mision es alta".
                        El libro estaba en el estante.
                        -> autorizo una mision de estudio entera para reescribirlo.

instalar_skills.py      ya_esta() matcheaba por el nombre del script y no por el comando.
                        Si el hook estaba, se daba por bueno cualquiera -- incluido uno
                        escrito en otra maquina con un interprete que aca no resuelve.
                        Imprimia "los hooks ya estaban configurados".
                        -> autorizo no arreglar un hook mudo.

gate del Contrato       daba la seccion por cumplida con encontrar su encabezado, aunque
de ejecucion            estuviera vacia.
                        -> autorizo cerrar una SOL sin la seccion que permite delegar.
```

Ninguno de los tres estaba caido. Los tres corrian, devolvian un resultado, y el resultado era *segui*.

**Un instrumento que falla hacia adelante es peor que no tenerlo**, porque presta su autoridad a la decision equivocada. Sin el guardrail, alguien habria mirado. Con el, nadie miro.

---

## La regla

> Un guardrail que **autoriza** trabajo falla hacia *frena y fijate*.
> Un guardrail que **frena** trabajo falla hacia *segui*.

Las dos mitades salen de la misma pregunta: ¿cual de los dos errores es recuperable?

```txt
guardrail que autoriza     falso negativo = trabajo duplicado, una mision entera
   (dedup, "ya existe?")   falso positivo = alguien mira dos segundos de mas
                           -> fallar hacia el falso positivo

guardrail que frena        falso positivo = la entrega se traba por nada
   (gate, "esto pasa?")    falso negativo = entra algo que no deberia, y se ve despues
                           -> depende de si lo que entra es reversible
```

La asimetria no es una opinion: se calcula. Un falso negativo del dedup cuesta una mision de estudio; un falso positivo cuesta una lectura. Trescientos a uno.

---

## Como se aplica

Al escribir o revisar cualquier gate, chequeo, validador o guardrail, una pregunta antes de las de `Alcance del instrumento`:

```txt
1. Cuando este instrumento se equivoque, ¿que pasa?
2. ¿Cual de los dos errores es mas caro, y por cuanto?
3. ¿El comportamiento por defecto -- lo que hace cuando no sabe -- cae del lado barato?
```

La tercera es la operativa. Un instrumento que **no sabe** tiene que decirlo con el veredicto del lado barato, no con el veredicto comodo. *"No encontre nada"* y *"no se"* no son la misma respuesta, y el dedup las estaba dando por iguales.

Y una consecuencia de forma: **el veredicto tiene que decir sobre que se pronuncia.** El dedup arreglado no contesta *"no hay nada"*: contesta cuantos terminos toco cada pieza. Un numero se lee distinto que una absolucion.

---

## Cuando NO aplica

- **No es un pedido de conservadurismo.** Un guardrail que frena todo por las dudas no eligio su direccion: se rindio. La regla pide elegir, no pide temer.
- **No aplica al juicio.** Si el criterio es correcto, si el aprendizaje vale, si el texto se entiende: eso no tiene direccion de falla porque no tiene instrumento.
- **No reemplaza la cobertura.** Un guardrail que falla en la direccion correcta y no mide la regla sigue sin medir la regla. Las dos notas se aplican juntas.

---

## Regla final

Un instrumento no se juzga solo por lo que mide.

Se juzga por lo que dice cuando no sabe.

## Que es

> **Un instrumento probado en el medio de su rango no esta probado.**

Todo instrumento tiene un rango implicito: escalas, tamanos, formas de escribir, cantidades, formatos. Se estrena sobre los casos que hay, y **los casos que hay se parecen entre si**. El error que tiene adentro no se manifiesta hasta que llega el caso raro, y para entonces el instrumento ya emitio veredictos.

## Por que existe

Porque el modo de falla no es que el instrumento se rompa: es que **siga contestando**.

Un instrumento que revienta avisa. Uno que mide mal en un extremo devuelve un numero, y ese numero se lee igual que los que estaban bien. La consecuencia no es un error visible; es una serie de decisiones tomadas sobre una medicion que nadie sabia que valia hasta cierto punto.

```txt
CINCO CASOS, DOS DOMINIOS. Ninguno se busco: los cinco aparecieron solos.

un verificador de malla     redondeaba el volumen antes de mirarle el signo.
                            Seis piezas pasaron porque median entre 0.9 y 6.5 m;
                            la primera a escala de milimetros lo rompio.

un inventario de trabajo    leia "estuvo Pausado; reabierto" como un estado
                            vigente. Se probo contra los documentos que
                            DECLARAN, nunca contra el que NARRA.

un instalador de copias     hasheaba el sello que el mismo escribia. Reportaba
                            26 copias fuera de sincronia SIEMPRE, incluso recien
                            sincronizadas: nunca se lo corrio contra una limpia.

un gate de documentacion    su patron de "numero con unidad" no reconocia una
                            regla numerada. Midio 8 de 9 donde habia 9 de 9.

un medidor de grafo         leia un artefacto como si fuera un indice porque su
                            titulo contenia la palabra "Catalogo".
```

Los cinco funcionaban. Los cinco daban un numero. Los cinco estaban probados **contra lo que ya existia**.

## La regla

> El rango se **declara**, y se prueba en **sus dos puntas**.
> Y si el instrumento no acepta datos escritos a mano, no se puede probar en ninguna.

Las dos mitades hacen cosas distintas y las dos hacen falta.

### 1. El caso extremo se fabrica, no se espera

Probar con los casos que hay es probar con los casos que se parecen. El caso que rompe el instrumento es, por definicion, el que todavia no llego.

La prueba es barata y consiste en escribirlo a mano: un valor mil veces mas chico que los medidos, un texto que cuenta en vez de declarar, una entrada recien procesada, un nombre que contiene la palabra que el patron busca. **Cuesta minutos y es lo unico que separa "anda" de "anda hasta aca".**

### 2. Un instrumento que solo corre en su entorno no se puede probar

El caso extremo casi nunca se puede fabricar dentro del entorno real: no hay a mano la pieza rara, ni el estado imposible, ni la copia sucia. **Se fabrica con datos escritos a mano, y eso exige que el instrumento acepte datos y no solo un entorno.**

> **Separar la lectura del entorno de la regla que se aplica no es prolijidad de diseno: es la condicion para poder probar la regla.**

Un instrumento que empieza importando su entorno solo corre adentro de el, y solo sobre lo que ahi haya. Partirlo en dos —el lector por un lado, la regla por el otro— convierte una regla imposible de probar en una funcion con veinte casos de prueba.

Es la inversion de dependencias con una consecuencia de verificacion, no de estilo: **la abstraccion no se elige para que quede lindo, se elige para que la regla se pueda ejercitar sin el mundo.**

## Como se aplica

Al escribir o revisar cualquier instrumento:

```txt
1. ¿Cual es el rango de lo que va a medir?
   Escalas, tamanos, formatos, formas de escribir. Escribilo.

2. ¿Que caso esta en la punta de ese rango, y existe un caso de prueba con el?
   Si no existe, todavia no sabes donde deja de valer.

3. ¿La regla se puede correr con datos escritos a mano?
   Si no, el punto 2 es imposible y el instrumento no es verificable.

4. ¿El veredicto declara hasta donde vale?
   Lo que se probo define el alcance de lo que se afirma.
```

Y al leer un veredicto: **preguntar contra que se probo el instrumento** antes de creerle un numero raro. Un resultado sorprendente es tan probable que sea un hallazgo como que sea el extremo del rango.

## Cuando NO aplica

No aplica a un instrumento de una sola vez: se escribe, se corre, se tira, y nada lo va a leer despues.

No aplica cuando el rango real **es** el que se probo, y eso esta declarado. Un medidor que solo va a ver un tipo de dato no tiene extremo que buscar; tiene un alcance escrito.

No dice que haya que probar todo. Dice que lo que se probo **es** el alcance del veredicto, y que ese alcance se escribe en vez de suponerse.

## Regla final

> Si nadie puede decir con que caso el instrumento deja de funcionar, el instrumento no esta probado: esta estrenado.

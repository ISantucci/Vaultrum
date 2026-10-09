## Que es

Un criterio sobre la relacion entre una regla y la herramienta que la comprueba.

> **Una ley que el instrumento no mide no esta vigente: esta escrita.**

`Gates verificables` dice que un gate que no se puede comprobar mecanicamente es una intencion. Esta nota es el paso siguiente y es mas incomodo: el gate **si** es mecanico, **si** corre, **si** devuelve cero — y aun asi no prueba lo que dice probar.

Un gate que pasa afirma que se verifico. Una regla no medida adentro de un gate que pasa se declara cumplida cada vez que se la infringe.

---

## Por que existe

Salio de dos casos reales del propio vault, con un ano de distancia de horas entre uno y otro.

**El primero.** La prohibicion de enlazar de vuelta al indice padre estaba escrita en tres lugares. La herramienta que verificaba el grafo en cada commit medía cinco de las seis leyes, y esa era la sexta. Entraron 52 links de retorno, uno por ficha, y el gate devolvio `EN LEY` las 52 veces.

**El segundo.** La misma herramienta corria sobre la carpeta del owner y devolvia cero. Reconstruido el paquete que git efectivamente entrega, la misma herramienta sobre el mismo vault devolvio 44 links rotos. Nadie los habia medido nunca, porque nadie habia comparado las dos cosas.

```txt
lo que el gate media     la carpeta de quien trabaja
lo que alguien recibe    el paquete que se entrega
nunca se compararon
```

---

## Las cuatro formas de fallar

Un instrumento puede pasar y no servir de cuatro maneras distintas. Las cuatro son de forma, no de criterio: ninguna se arregla escribiendo mejor la ley.

### 1. Mide de menos

La regla existe y la medicion no la cubre. Es la mas comun y la mas facil de tapar: la salida del gate dice `EN LEY` sin decir **que leyes probo**.

El arreglo no es medirlo todo: es que el veredicto declare su alcance. Un gate que dice *"probe estas cinco, la sexta no la mido"* no miente aunque este incompleto. Es `Verificacion parcial declarada` aplicada al instrumento en vez de a la entrega.

### 2. Reconoce el rotulo y no el efecto

Una excepcion legitima se implementa por como se llama en vez de por lo que hace, y a partir de ahi basta escribir el rotulo correcto arriba de la operacion inversa para que la regla se de vuelta sin que nada proteste.

> **Una excepcion que se identifica por su rotulo y no por su efecto es la puerta por donde entra exactamente lo que la ley prohibe.**

Un instrumento no hereda la intencion de quien lo escribio. Reconoce la forma que sabe reconocer.

### 3. Mide otro artefacto

El gate mide algo real y devuelve un numero cierto, sobre una cosa que no es la que se entrega. La copia de trabajo en vez del paquete. El branch en vez de la release. El caso feliz en vez del que corre en produccion.

> **Un gate mide un artefacto concreto. Si el artefacto que mide no es el que se entrega, su veredicto es cierto y no sirve.**

Es la mas dificil de ver porque no hay sintoma: todo esta verde.

### 4. Compara dos espejos

El gate mide los artefactos correctos y los compara entre si, y los dos se derivan del mismo trabajo. Entonces que coincidan no dice nada del trabajo: dice que la copia se hizo bien.

> **Un verificador que compara dos derivados del mismo hecho no verifica ese hecho. Para verificarlo tiene que llegar al original.**

El caso testigo tiene dos apariciones con meses de distancia y la misma forma. Un libro de la Biblioteca quedo marcado *En validacion* en su ficha mientras el estante y el catalogo escrito a mano lo daban por cerrado: dos espejos coincidian y nadie miraba el original. Reparado eso, la herramienta paso a cruzar la ficha contra el estante — **y son los dos derivados del mismo trabajo**. Un lote entero de 64 piezas quedo declarando cerrado mientras la mision que las produjo se declaraba abierta, y el gate contesto `EN NORMA` las dos veces que corrio.

La pregunta que lo detecta es una sola:

```txt
¿estas dos cosas que comparo pueden estar mal LAS DOS, por la misma causa?
   si  → son espejos. ¿Cual es el original, y lo puedo abrir?
   no  → una de las dos es el original. El cruce sirve.
```

Y el corolario, que es donde esta nota se corrige a si misma: la forma 1 se arregla **declarando** el alcance, y esta no.

```txt
declarar el alcance   correcto  cuando el original esta fuera del instrumento
                      EXCUSA    cuando esta a un open() de distancia
```

Un gate que compara espejos y declara *"no mido esa mitad"* eligio la respuesta barata teniendo la cara. El arreglo no es un descargo ni un cruce mas contra otro derivado — dos espejos no se arreglan con un tercero. Es abrir el original.

---

## El agujero que se declara en vez de arreglarse

El caso testigo de la tercera forma tiene un detalle que vale mas que el caso: el agujero **ya estaba declarado** como excepcion, con su razon escrita. *"La herramienta no distingue el paquete del workspace local"*, decia — y por estar declarado, dejo de doler.

Una excepcion declarada silencia el sintoma sin arreglar el instrumento. Y el instrumento se lleva el agujero a la siguiente cosa que mida.

```txt
declarar una excepcion   honesto, y suficiente cuando el desvio es deliberado
declarar un defecto      honesto, y NUNCA suficiente: sigue siendo un defecto
```

La diferencia esta en si lo declarado es una decision o una limitacion. Una decision se declara y se cierra. Una limitacion se declara y se agenda.

---

## Como se aplica

Al escribir o revisar cualquier gate, criterio de entrega o checklist verificable, cuatro preguntas:

```txt
1. Cada regla escrita, tiene una medicion que le corresponda?
2. Las excepciones, se reconocen por lo que hacen o por como se llaman?
3. El gate mide el artefacto que se entrega, o el que quedo a mano?
4. Si compara dos cosas: ¿cual de las dos es el original?
5. Cuando el gate pasa, la salida dice que probo y que no probo?
```

La quinta es la barata y la que mas rinde: no arregla el instrumento, pero impide que su silencio se lea como aprobacion.

La cuarta es la que mas duele, porque su respuesta correcta suele ser trabajo y no una linea de texto. Si ninguno de los dos lados es el original, el gate tiene que decir cual es y por que no lo alcanza — y si lo alcanza, abrirlo.

---

## Cuando NO aplica

No es un pedido de cobertura total. Un instrumento que mide tres de diez leyes y lo dice es util; uno que mide diez de diez y no dice nada es fragil el dia que una deja de medirse.

Tampoco aplica al juicio. Si el texto se entiende, si el criterio es correcto, si el aprendizaje vale: eso no tiene instrumento y no debe fingir tenerlo. Lo que esta nota exige es que la frontera entre lo medido y lo juzgado este escrita.

---

## Regla final

Una regla vale lo que vale su medicion.

Sin medicion es una intencion. Con una medicion que no la cubre, es peor: es una intencion que se declara cumplida.

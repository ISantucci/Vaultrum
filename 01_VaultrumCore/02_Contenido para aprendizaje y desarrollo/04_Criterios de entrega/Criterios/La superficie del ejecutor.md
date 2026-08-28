## Que es

Un criterio sobre lo que le falta a una spec para que otro pueda ejecutarla.

> **Una spec cerrada dice que hacer. Falta la linea que dice donde tiene que poder correr.**

Una especificacion completa —archivos, interfaces, invariantes, lo prohibido— describe **el trabajo**. No describe **el lugar**. Y el lugar decide si el trabajo puede pasar: un ejecutor sin la herramienta, sin la red o sin permiso de escritura no devuelve un error de spec. Devuelve *hecho*, o devuelve nada, y en los dos casos la spec parece bien.

---

## Por que existe

Cuatro casos, cuatro superficies distintas, todos con la spec correcta.

```txt
1. node fuera del PATH        La corrida entera de un revisor externo se trabo. El modelo,
                              el contrato y el ruteo estaban bien: fallaba el entorno.

2. el hook del trace          "Confirmar que el hook corre en la superficie donde el owner
                              opera de verdad" quedo declarado y sin cerrar durante dias,
                              bloqueando un hilo entero. La spec no tenia defecto.

3. el ejecutor en solo-lectura  Se le pidio producir un archivo, no pudo escribir, y lo
                              menciono al final como nota. En un review se noto porque los
                              hallazgos volvieron igual. En una ejecucion, el pedido habria
                              vuelto CUMPLIDO con el artefacto inexistente.

4. el puente que no commitea   Un ejecutor con el vault montado no puede liberar el lock
                              que su propio git deja. Cada escritura traba el repo.
                              La tarea estaba bien descripta y no se podia terminar.
```

El caso 3 es el que define la regla, porque es el unico donde **el fallo se disfraza de exito**. Los otros tres se ven; ese no.

---

## La regla

> Antes de delegar algo que produce un artefacto, se verifica que el ejecutor **pueda producirlo** — no que sepa como.

Cuatro preguntas, en orden de cuanto duele que fallen:

```txt
Escritura   ¿puede escribir en la ruta destino? Probarlo, no suponerlo.
Herramienta ¿existe el interprete, el motor, la libreria? Con `which` o un import.
Red         ¿alcanza lo que necesita bajar?
Permiso     ¿puede hacer la operacion destructiva que la tarea implica -- borrar, pisar?
```

Es el **gate de existencia en disco aplicado por adelantado**: aquel verifica al volver que el archivo esta; este verifica antes que el archivo pueda estar. Los dos existen porque la misma clase de fallo entro dos veces por puertas distintas.

Y su corolario, que es lo que hace la regla ejecutable:

> **Un ejecutor que no pudo hacer algo lo reporta como fallo, no como nota al pie.**
> Una limitacion mencionada al final se lee como color. Un fallo declarado frena.

---

## Como se aplica

En una spec que se va a delegar, una seccion o una linea:

```txt
Superficie   donde tiene que poder correr esto, y como se comprueba antes de empezar.
```

No es una lista de requisitos del sistema. Es **la prueba mas barata que distingue "puede" de "no puede"**: escribir un archivo vacio en la ruta destino y borrarlo, correr `which` sobre la herramienta, pedir la URL. Segundos, antes de gastar la ejecucion.

Cuando la superficie no da, hay tres respuestas y ninguna es seguir:

```txt
cambiar de ejecutor       el trabajo va donde si se puede hacer
cambiar la superficie     instalar, pedir el permiso, abrir la ruta
declarar y frenar         se anota que superficie falta, y el hilo no avanza
```

---

## Cuando NO aplica

- **No aplica a lo que uno mismo ejecuta en el lugar donde ya trabaja.** La regla existe por la distancia entre quien escribe la spec y quien la corre. Sin distancia, no hay superficie que verificar.
- **No reemplaza la verificacion de salida.** Comprobar que se puede escribir no comprueba que se escribio. El gate de existencia en disco sigue corriendo despues.
- **No convierte un entorno en un requerimiento.** Si la superficie es contingente —una maquina, una sesion, un montaje— se declara como supuesto de esa corrida, no como parte de la arquitectura.

---

## Regla final

Una spec sin superficie declarada no esta cerrada: esta cerrada para el que la escribio.

Y el peor resultado no es que falle. Es que vuelva diciendo que se hizo.

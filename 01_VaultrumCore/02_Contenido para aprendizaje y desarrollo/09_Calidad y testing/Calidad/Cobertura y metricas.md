## Que es

La cobertura responde una sola pregunta: **que superficie se examino, y con que enfoque**.

No responde ninguna de estas:

```txt
quedan defectos?          no lo puede saber
esta listo para entregar? esa es una decision, no una medicion
esta bien hecho?          eso es otra capa de calidad
```

Una cobertura del 100% sobre una dimension significa que se recorrio esa dimension entera. Nada mas. Si la dimension estaba mal elegida, se recorrio entera la superficie equivocada.

---

## Los tres tipos de cobertura

```txt
de requisitos   que porcentaje de lo pedido tiene al menos una prueba asociada
de codigo       que porcentaje de las lineas o decisiones se ejecuto
de dimensiones  que aspectos del sistema se examinaron, y cuales no
```

El primero es el mas util para decidir si algo se puede entregar: dice si hay algo que se prometio y nadie verifico. El segundo es util para quien programa y peligroso como objetivo. El tercero es el que mejor comunica el estado real, porque hace visible **lo que falta**.

---

## La matriz de dimensiones

Es la forma mas honesta de mostrar cobertura, porque en la misma tabla estan lo cubierto, lo no cubierto y lo que no corresponde.

| Sistema | Feliz | Negativo | Limites | Estados | Guardado | Rendimiento | Accesibilidad | Idioma | Plataforma |
|---|---|---|---|---|---|---|---|---|---|
| Descarte de item | si | si | si | si | no aplica | no aplica | si | si | Windows |
| Guardado | si | si | si | si | si | no | no aplica | no aplica | Windows |

Tres valores posibles y ninguno es opcional:

```txt
si          se probo
no          NO se probo, y es un hueco conocido
no aplica   no corresponde, y hay que poder decir por que
```

Un "no aplica" sin razon escrita es un "no" con mejor letra. Esto es la misma regla que el vault aplica a toda omision: declarada es criterio, silenciosa es hueco.

---

## Lo que la cobertura no puede afirmar

```txt
que se ejecute una linea no dice que su resultado sea correcto
que un requisito tenga un caso no dice que el caso sea bueno
que la matriz este llena no dice que las dimensiones elegidas fueran las que importaban
```

El caso limite: un set de pruebas sin una sola comparacion de resultado puede dar 100% de cobertura de codigo. Ejecuta todo y no verifica nada.

---

## Metricas que sirven

Siempre con contexto —version, alcance, periodo— y siempre como tendencia, no como foto.

```txt
defectos abiertos por severidad          donde esta parado el producto hoy
antiguedad de bloqueantes y criticos     un critico de 20 dias es un problema de proceso
tasa de reapertura                       si sube, los arreglos no se estan verificando
tasa de escape                           defectos que llegaron al jugador sobre el total
pases de verificacion de build           cuantas builds se rechazaron y por que
regresiones falladas por version         si sube, algo estructural se esta rompiendo
tasa de pruebas inestables               una suite en la que nadie confia no bloquea nada
tiempo de deteccion a arreglo verificado el ciclo real, no el tiempo de programar
cobertura por sistema, cruzada con riesgo donde hay superficie sin mirar que ademas importa
```

La mas valiosa de todas es la **tasa de escape**: mide lo unico que importa de un proceso de calidad, que es cuanto de lo que fallo llego a quien lo usa.

---

## Metricas que danan como objetivo

```txt
defectos encontrados por persona     premia reportar duplicados y ruido
cantidad de casos ejecutados         premia casos triviales y rapidos
cantidad de tickets cerrados         premia cerrar sin verificar
porcentaje de cobertura de codigo    premia pruebas sin comparacion de resultado
```

Ninguna es inutil como observacion. Todas son daninas como meta, y por la misma razon: **cuando una medida se vuelve objetivo, deja de ser una buena medida.** La gente optimiza el numero, no lo que el numero representaba.

Sintoma concreto: el dia que se premia "bugs encontrados", el registro de defectos se llena de cosmeticos triviales y los sistemas dificiles dejan de tocarse, porque explorar un sistema complejo durante tres horas puede terminar en cero tickets y mucho aprendizaje.

---

## Que informa un cierre honesto

```txt
que se ejecuto
que no se ejecuto, y por que
que fallo, con que severidad
que evidencia existe
que riesgo queda vivo
quien acepta ese riesgo
```

Seis lineas. Un informe que las tiene sirve para decidir; uno que ocupa diez paginas y no las tiene, sirve para demostrar que alguien trabajo.

---

## Regla final

```txt
La cobertura no mide calidad: mide donde se miro.

El valor de un informe esta en lo que declara que NO cubrio.
Todo lo demas ya se sabia.
```

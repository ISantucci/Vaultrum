## Que es

El conjunto de metodos para **elegir que casos probar** cuando probar todo es imposible.

El problema, con numeros: un inventario con 4 formas de entrada, 4 estados de inventario, 5 tipos de item y 4 estados de mundo da 320 combinaciones. Agregale que el jugador puede cancelar a mitad de camino y cambiar de escena durante la confirmacion, y el numero se va a los miles.

Nadie ejecuta miles de casos. La pregunta real no es *como pruebo todo*, es:

```txt
Cuales de estos casos, si estan bien, me dan derecho a suponer
que los demas tambien lo estan?
```

Cada tecnica de abajo es una respuesta distinta a esa pregunta.

---

## Caja negra: se prueba el comportamiento

No mira el codigo. Trabaja con la especificacion, los requisitos y el comportamiento observable. Es la familia principal del control de calidad.

### Particiones de equivalencia

Agrupar entradas que el sistema deberia tratar igual, y probar **una de cada grupo**.

```txt
vida del jugador   [minimo]  negativa | cero | entre 1 y max-1 | max | mayor que max
```

Si el sistema trata igual a 34 y a 57 de vida, probar los dos no agrega informacion. Probar uno de cada clase, si.

Regla: hay que particionar tambien las **entradas invalidas**, no solo las validas. La mitad de los defectos vive del lado que "no deberia pasar nunca".

### Valores limite

Los defectos se juntan en los bordes de cada particion, porque ahi viven los `<` que debian ser `<=`.

```txt
para un limite en n, probar   n-1   n   n+1
inventario de 20 espacios     19    20   21
temporizador de 60 segundos   59    60   61 (y 0, y negativo si puede)
```

Es la tecnica con mejor relacion entre casos y defectos encontrados de toda la lista.

### Tablas de decision

Cuando el comportamiento depende de una combinacion de condiciones, se tabula en vez de narrar.

| Item equipado | Inventario lleno | Confirmacion | Resultado esperado |
|---|---|---|---|
| si | no | acepta | se desequipa y se descarta |
| si | no | cancela | queda equipado |
| si | si | acepta | se desequipa y se descarta |
| no | si | cancela | no pasa nada |

La tabla hace visible la fila que nadie penso. Ese es su verdadero valor: **no encuentra el defecto, encuentra el caso que faltaba**.

### Transicion de estados

Cuando el sistema tiene estados y el orden importa. Se dibuja el diagrama y se prueban:

```txt
cada estado         se llega y se sale
cada transicion     valida, al menos una vez
transiciones invalidas   guardar mientras se muere, pausar durante la pantalla de victoria
secuencias           A→B→A vuelve al mismo A, o quedo algo colgado
```

En juegos es la tecnica mas rentable despues de los limites: menu, pausa, muerte, carga, cinematica y victoria son estados, y casi todos los atascos viven en una transicion que nadie diseno.

### Combinatoria por pares

Cuando hay muchas variables independientes, probar todas las combinaciones es imposible, pero la mayoria de los defectos surge de la interaccion de **dos** factores. Se arma un set donde cada par de valores aparezca al menos una vez.

```txt
4 resoluciones x 3 dispositivos de entrada x 3 calidades x 2 modos = 72 combinaciones
por pares: alcanzan aproximadamente 12
```

Es la tecnica de las matrices de compatibilidad.

---

## Caja blanca: se prueba la estructura

Mira el codigo y pregunta que caminos se ejecutaron.

```txt
cobertura de sentencias   se ejecuto cada linea
cobertura de decisiones   cada if dio verdadero y falso al menos una vez
```

Sirve para lo que la caja negra no ve: la rama de error que nunca se ejecuto, el `else` vacio, el camino muerto. Vive junto a las pruebas de componente y es trabajo del area que programa.

Su limite es duro y conviene tenerlo claro: **100% de cobertura de codigo no dice nada sobre si el codigo hace lo correcto.** Solo dice que se ejecuto.

---

## Basadas en experiencia: se prueba con criterio humano

### Adivinacion de errores

Usar el historial y el olfato: donde suele romperse esto. Vacio, cero, negativo, muy grande, dos veces seguidas, muy rapido, al mismo tiempo, mientras carga, sin conexion, con el disco lleno.

No es rigurosa y encuentra cosas que ninguna tecnica formal buscaba.

### Exploratorio con charter

Explorar **no es jugar sin metodo**. Una sesion exploratoria tiene mision, tiempo acotado y notas:

```txt
charter    que se explora, con que recursos, buscando que tipo de falla
timebox    45 a 90 minutos, no una tarde
notas      que se hizo, que se vio, que quedo pendiente
```

Ejemplo de charter: *explorar el descarte de items combinando arrastre, atajos de teclado, inventario lleno, cambio de escena y cancelacion del popup, buscando perdida, duplicacion o estados invalidos.*

Es la unica familia que encuentra lo que nadie penso, porque las otras solo pueden buscar lo que alguien escribio.

### Listas de comprobacion

Utiles para lo repetitivo (verificacion de build, requisitos de plataforma), peligrosas cuando el item no tiene criterio de falla. Un item que no se puede fallar no es un check: es una decoracion.

---

## Cual usar

| Situacion | Tecnica |
|---|---|
| una entrada con rangos | particiones + valores limite |
| varias condiciones combinadas | tabla de decision |
| el sistema tiene modos o estados | transicion de estados |
| muchas configuraciones independientes | combinatoria por pares |
| logica interna, ramas de error | caja blanca |
| sistema nuevo, riesgo desconocido | exploratorio con charter |
| lo que ya se rompio una vez | caso dirigido, y despues a regresion |

Lo normal es combinar tres capas en un mismo pase: **casos dirigidos** para lo que se pidio, **exploratorio** para lo que nadie penso, **automatizado** para lo que hay que repetir.

---

## Anti-patrones

```txt
casos gigantes de 40 pasos: cuando fallan, no se sabe donde
casos que solo recorren el camino feliz
probar 34 y 57 de vida y ninguno de los bordes
llamar exploratorio a jugar sin notas ni mision
una lista de comprobacion cuyos items no se pueden fallar
```

---

## Regla final

```txt
No se prueba todo. Se elige.

Una prueba vale por los casos que representa,
no por la cantidad de pasos que tiene.
```

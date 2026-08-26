## Que es

Dos preguntas distintas que se suelen mezclar en una sola.

```txt
NIVEL   sobre que pieza se prueba      una funcion, dos sistemas juntos, el producto entero
TIPO    que caracteristica se prueba   que haga lo que dice, que rinda, que se banque el cambio
```

Un mismo tipo se prueba en varios niveles. El rendimiento se puede medir en una funcion, en un sistema o en la build final, y las tres mediciones dicen cosas distintas.

---

## Estatico y dinamico

Antes de la primera division: no todo testing ejecuta el producto.

| | Que hace | Que encuentra bien | Que no puede encontrar |
|---|---|---|---|
| **Estatico** | leer, revisar, analizar sin ejecutar | ambiguedades, contradicciones, requisitos imposibles, codigo sospechoso, valores mal escritos | comportamiento real, rendimiento, integracion |
| **Dinamico** | ejecutar el sistema | fallas observables | lo que nunca se ejecuto |

Revisar una spec, leer una tabla de balance buscando contradicciones o correr un analizador estatico **es testing**, y es el mas barato de todos porque encuentra defectos antes de que existan en codigo.

---

## Los niveles

### Componente (unidad)

Una pieza aislada: una funcion, una clase, una regla. La escribe normalmente quien programa.

```txt
prueba bien   logica pura, calculos, reglas, limites, transformaciones de datos
no prueba     que las piezas se entiendan entre si, ni nada que dependa del motor
```

### Integracion

Dos o mas piezas hablando. Es donde aparecen los defectos de contrato: uno manda metros, el otro espera centimetros; uno avisa una vez, el otro escucha dos veces.

```txt
prueba bien   interfaces, eventos, orden de inicializacion, dependencias, datos que cruzan
no prueba     la experiencia completa
```

### Sistema

El producto entero corriendo, como lo va a usar una persona. Es el nivel principal del gate de calidad.

```txt
prueba bien   flujos completos, estados, progresion, guardado, rendimiento real, interrupciones
no prueba     por que fallo por dentro: dice que fallo, no donde
```

### Aceptacion

La pregunta final: **esto sirve para lo que se pidio**. No busca defectos; busca confianza para decidir.

En Vaultrum este nivel tiene dos duenos declarados: el gate de calidad verifica que lo construido se sostiene, y la validacion de entrega verifica que lo entregado es lo prometido.

---

## Los tipos

### Funcional

Que haga lo que dice. Es el tipo por defecto y el que mas casos genera.

```txt
camino feliz     lo que se espera que pase
caminos negativos entradas invalidas, acciones fuera de orden, cancelaciones
limites          minimo, maximo, vacio, lleno, cero, uno, uno mas
estados          que pasa en cada estado y en cada transicion
```

### No funcional

Como lo hace. Se mide, no se opina.

```txt
rendimiento      cuadros por segundo, tiempos de carga, memoria, picos, estabilidad
compatibilidad   configuraciones, resoluciones, dispositivos de entrada, sistemas
usabilidad       si se entiende y se puede operar
seguridad        que no se pueda hacer lo que no corresponde
portabilidad     instalar, actualizar, migrar, desinstalar
```

Un requisito no funcional sin numero no es verificable. "Que vaya fluido" no se puede aprobar ni rechazar; "60 cuadros por segundo sostenidos en la escena de combate en el equipo de referencia" si.

### Estructural

Prueba por dentro: que caminos del codigo se ejecutaron. Es la base de la cobertura de codigo y vive junto a las pruebas de componente.

### De cambio

Los dos que existen **despues de tocar algo**, y que se confunden todo el tiempo:

```txt
confirmacion   el defecto reportado, exactamente ese, esta arreglado en esta version
regresion      lo que ya funcionaba, sigue funcionando despues de este cambio
```

Son distintos y los dos son obligatorios. Confirmar sin regresion cierra un ticket y abre dos. Regresion sin confirmar deja el defecto original sin verificar.

**Un ticket no se cierra porque alguien cambio codigo.** Se cierra cuando la confirmacion paso sobre una version identificable.

---

## Que nivel para que cosa, en un juego

| Lo que se construyo | Nivel principal | Por que |
|---|---|---|
| formula de dano, curva de experiencia | componente | logica pura, se prueba sin motor |
| guardado y carga | integracion + sistema | cruza datos, version y ciclo de vida |
| flujo de menus | sistema | el defecto vive en la navegacion, no en una funcion |
| nivel nuevo | sistema | colisiones, disparadores, secuencia, atascos |
| rendimiento | sistema, en la build de destino | el editor no mide lo que mide la build |
| entrega completa | aceptacion | responde si sirve, no si funciona |

---

## Regla final

```txt
El nivel dice donde mirar. El tipo dice que mirar.

Confundirlos produce el error mas comun de todos:
probar la experiencia completa buscando un defecto de una funcion.
```

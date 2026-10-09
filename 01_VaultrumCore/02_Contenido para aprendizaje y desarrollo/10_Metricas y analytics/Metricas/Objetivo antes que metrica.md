## Que es

El principio del que salen todos los demas de esta seccion: **nunca se empieza por la metrica.**

```txt
1. cual es el objetivo?
2. que comportamiento deberia cambiar?
3. que senal demostraria ese cambio?
4. que KPI la representa?
5. que metricas diagnosticas ayudan a explicarlo?
6. que efectos negativos hay que vigilar?
```

"Que KPI ponemos" es la pregunta equivocada. La correcta es la que la precede: **que evidencia necesitamos para saber si el producto, el sistema o la feature esta produciendo el comportamiento esperado.**

---

## Metrica y KPI no son lo mismo

```txt
metrica   cualquier dato cuantificable
          partidas jugadas, cofres abiertos, muertes, upgrades, tiempo de sesion
KPI       una metrica ELEGIDA porque evalua el rendimiento contra un objetivo que importa
```

Todo KPI es una metrica. No toda metrica es un KPI. Una metrica se vuelve KPI por la decision que habilita, no por lo grande que es.

Las **vanity metrics** son numeros grandes sin conexion con ninguna decision: descargas totales sin retencion, horas jugadas sin saber si se juega o se espera. Suben siempre, y por eso no dicen nada.

---

## El arbol de metricas

Un objetivo no se mide con un numero: se mide con una jerarquia, y cada nivel tiene una funcion distinta.

```txt
nivel 1  objetivo              aumentar ingresos sostenibles
nivel 2  outcome KPI           ARPU
nivel 3  drivers               conversion · ARPPU · frecuencia de compra
nivel 4  diagnosticas          visitas a la tienda · ofertas vistas · checkouts fallidos
nivel 5  guardrails            retencion · reembolsos · economia · sentimiento
```

El outcome dice si se logro. Los drivers dicen por que se movio. Las diagnosticas dicen donde mirar. Los guardrails dicen **que se rompio en el camino**.

---

## Los guardrails no son opcionales

Una mejora local puede danar el producto.

```txt
ads vistos      +300%
D7 retention    -20%
```

El primer numero, solo, es un exito. Los dos juntos, un problema. Todo plan de medicion define tres cosas y ninguna se omite: **KPI primario, metricas secundarias y guardrails**.

---

## Los datos dicen que pasa, no por que

Una espada tiene 5% de uso. Eso es una **senal**, no una causa. Puede ser:

```txt
bajo descubrimiento      acceso tardio      precio alto
UX confusa               mal balance        otra opcion dominante
poco valor percibido
```

Cada causa pide una correccion distinta, y elegir una sin investigar es adivinar con un numero en la mano.

---

## Correlacion no es causalidad

Dos KPIs pueden moverse juntos sin que uno cause al otro. Antes de afirmar una causa hacen falta tres cosas, en orden de fuerza creciente:

```txt
una hipotesis escrita
evidencia de contexto
idealmente, un experimento controlado u otra forma de identificar el efecto
```

---

## Ninguna metrica es buena o mala sin contexto

La duracion de sesion puede bajar porque empeoro el engagement, **o porque la experiencia se volvio mas eficiente**. Mas alto no es mejor por defecto.

La comparacion que vale es siempre la misma:

```txt
resultado observado  vs  comportamiento esperado
```

Y la tendencia le gana a la foto:

```txt
feature A   25% de uso, creciendo
feature B   30% de uso, cayendo
```

La foto dice que B es mejor. La tendencia dice lo contrario.

---

## Una definicion canonica por metrica

Una sigla puede significar cosas distintas en dos herramientas. `ARPU` en un tablero puede dividir por usuarios totales y en otro por activos. Por eso cada proyecto mantiene un **registro de metricas** con nombre, definicion, formula, poblacion, periodo, zona horaria, fuente, filtros, dueno y version. El formato esta en `Del dato a la decision`.

**Nunca se asume que el nombre alcanza.**

---

## Cuando piden "subir una metrica"

La pregunta que se devuelve siempre:

```txt
Por que queremos subir esa metrica, y que resultado del producto representa?
```

"Subir la duracion de sesion" puede no ser el objetivo. Tal vez el objetivo es mas progreso, mas participacion o mas retencion, y una sesion artificialmente larga empeora la experiencia sin generar valor.

---

## Cuando no se sabe que metrica usar

```txt
objetivo -> poblacion -> comportamiento -> momento del journey
         -> indicador de exito -> KPI -> diagnosticas -> guardrails
```

Nunca se elige por popularidad.

---

## Las preguntas que se reconstruyen antes de elegir nada

```txt
 1. cual es el objetivo?
 2. que comportamiento queremos generar o cambiar?
 3. en que fase esta el proyecto?
 4. que modelo de negocio tiene?
 5. que etapa del journey del jugador afecta?
 6. cual es el KPI primario?
 7. que metricas lo explican?
 8. que poblacion es elegible?
 9. que segmentos o cohortes hacen falta?
10. cual es el baseline?
11. que efectos negativos hay que vigilar?
12. la instrumentacion es confiable?
13. que evidencia permitiria decidir?
```

Version corta:

```txt
objetivo -> comportamiento -> KPI -> segmento -> instrumentacion -> baseline -> cambio -> medicion
```

---

## Regla final

```txt
Si no se puede decir que se quiere lograr, que comportamiento lo representa,
que senal lo mide, que datos hacen falta, que significa el resultado
y que decision habilita, todavia no hay estrategia de medicion.

Hay un tablero.
```

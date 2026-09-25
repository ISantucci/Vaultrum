## Que es

La ultima milla: como se pasa de un numero a una decision sin inventar causas, y que queda escrito para que la proxima medicion mida lo mismo.

---

## Cuatro cosas distintas, cuatro rotulos

Toda conclusion se separa y se rotula:

```txt
hecho            directamente respaldado por el dato
interpretacion   una lectura razonable del hecho
hipotesis        una explicacion todavia no demostrada
recomendacion    una accion propuesta
```

Ejemplo:

```txt
hecho            el uso del arma B cayo 40% en cuatro semanas
interpretacion   perdio relevancia relativa
hipotesis        el arma A domina la misma funcion
recomendacion    analizar rendimiento por encuentro y probar un ajuste controlado
```

Un informe que mezcla los cuatro presenta una hipotesis con la autoridad de un hecho. Es la misma falta que cualquier medicion del vault castiga: **presentar juicio como medicion**.

---

## Los anti-patrones que mas cuestan

```txt
dashboard-first          "metamos todos los KPIs y despues vemos"
maximizar el KPI         "subio la duracion de sesion, entonces mejoro"
vanity metrics           numeros grandes sin decision detras
metric shopping          buscar despues la metrica que "dio positiva"
causa por correlacion    declarar causa sin evidencia
solo agregado            leer el promedio global y nada mas
sin baseline             evaluar una feature sin referencia previa
denominator drift        cambiar la poblacion de una metrica sin escribirlo
definition drift         cambiar formula o nombre entre equipos
telemetry spam           instrumentar todo sin proposito
ignorar la fase          KPIs de monetizacion en un prototipo que valida el loop
```

---

## Salud del producto: el modelo mental por defecto

Cuando no hay un problema especifico, se revisan cinco preguntas en este orden:

```txt
adquisicion     entra gente?
retencion       vuelve?
engagement      que hace y cuanto interactua?
monetizacion    paga, y cuanto?
economia        el sistema interno sostiene valor y progreso?
```

Mas la salud tecnica, segun el producto: crashes, ANR, FPS, tiempo de carga, latencia.

---

## Tableros minimos

No se construye un unico tablero infinito. Uno por pregunta:

```txt
salud del producto   DAU/WAU/MAU · retencion · sesiones · tiempo jugado · revenue · salud tecnica
retencion            tablas de cohortes · D1/D7/D30 · rolling · reactivacion
monetizacion         revenue · conversion · pagadores · ARPU · ARPPU · distribucion de transacciones
economia             sources · sinks · saldos · gasto por categoria · moneda por progresion
progresion           starts · fails · completes · intentos · drop-offs
feature              descubrimiento · adopcion · frecuencia · retencion de uso · resultado
live ops             exposicion · participacion · completion · retencion · revenue · guardrails
```

---

## El registro de metricas

Cada proyecto mantiene un registro canonico. Una entrada por metrica:

```txt
nombre · definicion · formula · poblacion · ventana temporal · zona horaria
· eventos fuente · filtros · segmentos · dueno · objetivo al que responde
· como se interpreta · limitaciones conocidas · version
```

Es lo que impide el denominator drift y el definition drift. Cambiar una entrada sube su version y queda escrito por que.

---

## Que documenta un analisis al cerrar

```txt
la pregunta · el contexto · el periodo · la poblacion · las definiciones usadas
· los hallazgos · los segmentos o cohortes · los hechos · las interpretaciones
· las hipotesis · los riesgos y limitaciones · la recomendacion · la proxima medicion
```

La proxima medicion no es cortesia: es lo que convierte un informe en un ciclo.

---

## Regla final

```txt
El dato dice que paso. La decision la toma quien es dueno del producto.
Entre las dos cosas hay una lectura, y la lectura se firma con sus rotulos.

Una conclusion que no habilita una decision concreta todavia no esta terminada.
```

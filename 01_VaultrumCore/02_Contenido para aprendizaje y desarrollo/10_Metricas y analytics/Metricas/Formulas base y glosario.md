## Que es

Las formulas canonicas de la seccion y sus siglas, en un solo lugar. Es una nota de consulta: la formula no dice cuando usarla, eso lo dicen las demas notas.

La advertencia va primero porque es la que se olvida:

```txt
una sigla no define una metrica.
la definen su denominador, su ventana, su zona horaria y su fuente,
y el registro de metricas del proyecto es quien las fija.
```

---

## Formulas

```txt
conversion              pagadores / usuarios elegibles (o totales, DECLARADO) x 100
ARPU                    revenue / usuarios totales
ARPAU                   revenue / usuarios activos
ARPPU                   revenue / pagadores
ARPDAU                  revenue diario / DAU
relacion                ARPU ~= conversion x ARPPU   (poblaciones y periodos compatibles)
Dn clasica              usuarios de la cohorte que vuelven el dia n / cohorte inicial x 100
stickiness              DAU / MAU   (orientativa, depende del genero)
Current MRR             New MRR + Retained MRR + Reactivated MRR
flujo neto de moneda    sources - sinks
completion rate         completes / starts x 100
failure rate            fails / intentos terminados x 100
                        o  fails / starts x 100      ELEGIR UNA Y DECLARARLA
puntos porcentuales     p2 - p1
cambio relativo         (p2 - p1) / p1 x 100
```

---

## KPIs adicionales que conviene reconocer

```txt
adquisicion   CPI · CAC · CPA · ROAS
anuncios      eCPM · Ad ARPDAU · opt-in de rewarded
tecnicos      crash rate · ANR · FPS · tiempo de carga · latencia
sociales      tasa de referidos · conversion de invitaciones · participacion en clanes
comercio      tasa de reembolso · frecuencia de compra · revenue por transaccion (AOV)
```

Se priorizan solo los relevantes para el objetivo y la fase.

---

## Glosario

```txt
metrica          dato cuantificable
KPI              metrica elegida porque mide un objetivo relevante
guardrail        metrica que protege contra efectos secundarios de una mejora
baseline         estado de referencia previo al cambio
DAU/WAU/MAU      usuarios activos diarios / semanales / mensuales
retencion        capacidad de lograr que el jugador vuelva
engagement       intensidad, frecuencia y profundidad de interaccion
FTUE             First Time User Experience: los primeros minutos
drop-off         perdida de gente dentro de una secuencia
funnel           secuencia de etapas con su conversion
cohorte          grupo comparable de usuarios, clasicamente por fecha de inicio
segmento         subconjunto por atributo o comportamiento
churn            perdida o abandono, SEGUN SU DEFINICION
reactivacion     retorno de un usuario inactivo
conversion       proporcion que realiza la accion objetivo
ARPU             Average Revenue Per User
ARPAU            Average Revenue Per Active User
ARPPU            Average Revenue Per Paying User
ARPDAU           Average Revenue Per Daily Active User
LTV              Lifetime Value: valor de un usuario en su relacion con el producto
MRR / MnRR       Monthly Recurring / Non-Recurring Revenue
source / sink    entrada / salida de un recurso
A/B test         experimento control / tratamiento
live ops         operacion continua de contenido y eventos despues del lanzamiento
cardinalidad     cantidad de valores distintos de un nombre o parametro de evento
```

---

## Regla final

```txt
La formula es la parte facil.
Lo dificil —y lo que se escribe— es sobre quien divide.
```

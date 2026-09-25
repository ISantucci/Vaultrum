## Que es

Tres familias de metricas que se usan como sinonimos y no lo son:

```txt
actividad    cuanta gente esta activa en un periodo      DAU · WAU · MAU
retencion    si vuelve con el paso del tiempo            D1 · D7 · D30 · churn
engagement   que hace y cuanto interactua cuando esta    sesiones · profundidad · uso
```

Atajo que no falla: **retencion = vuelve; engagement = que hace y cuanto.**

---

## Actividad

```txt
DAU   usuarios unicos activos en un dia
WAU   usuarios unicos activos en una semana
MAU   usuarios unicos activos en un mes
```

**Stickiness** se aproxima frecuentemente con `DAU / MAU`: que fraccion de los activos del mes aparece un dia cualquiera. No existe un valor universal "bueno": depende del genero y de la frecuencia de juego que el diseno espera. Un juego de sesiones semanales largas tiene stickiness baja por diseno.

```txt
duracion de sesion      cuanto dura UNA sesion
sesiones por usuario    cuantas sesiones hace un usuario en el periodo
tiempo jugado           el total del usuario en el periodo
```

Duracion de sesion y tiempo jugado no son equivalentes. Y ninguna se maximiza por defecto.

---

## Retencion

La capacidad del producto de lograr que la gente vuelva.

Para una cohorte que empezo el mismo dia:

```txt
Dn = usuarios de la cohorte que vuelven en el dia n / usuarios iniciales de la cohorte
```

Lectura orientativa, no ley:

```txt
D1        la primera experiencia: FTUE, onboarding
D7        el interes de corto y mediano plazo
D30       habito, progresion, valor sostenido
D90/D180  productos longevos
```

### Clasica contra rolling

```txt
clasica   cuenta a quien vuelve EXACTAMENTE el dia n
rolling   cuenta a quien vuelve el dia n O DESPUES (segun la herramienta)
```

Las dos dan numeros distintos sobre los mismos datos, y los dos son correctos. Por eso **cada reporte declara cual usa**. Comparar un D7 clasico contra un D7 rolling es comparar dos metricas con el mismo nombre.

### Churn y reactivacion

**Churn** es la perdida de usuarios o suscriptores, y no significa nada hasta que se define: no jugar durante N dias, cancelar una suscripcion, abandonar una fase. **Reactivacion** es un usuario inactivo que vuelve. Las dos dependen de la misma definicion de inactividad, y se escribe en el registro de metricas.

---

## Engagement

Nivel, frecuencia y profundidad de interaccion. **No se reduce a tiempo de sesion.**

Metricas posibles, segun el core loop:

```txt
sesiones por usuario · duracion · tiempo jugado · quests completadas · partidas
· adopcion y frecuencia de features · interacciones sociales · builds creadas
· progresion · amplitud de contenido · participacion en eventos
```

La metrica correcta de engagement es la que describe **el loop de este juego**. En un juego de construccion son builds; en uno competitivo, partidas; en uno narrativo, capitulos. Copiar la de otro genero mide un loop que no existe.

---

## Por que no son lo mismo

```txt
jugador A   entra todos los dias, juega 2 minutos
jugador B   entra una vez por semana, juega 4 horas
```

A tiene retencion alta y engagement bajo; B, lo contrario. Una feature puede mejorar la frecuencia de retorno sin mejorar la profundidad:

```txt
login -> reclamar recompensa -> logout
```

Eso sube el DAU y no agrega nada. Por eso un sistema de retorno se mide con la **actividad despues del reclamo**, no con el reclamo.

---

## Sistemas de retorno y que se mide

```txt
login diario        objetivo: frecuencia de retorno
                    mide: reclamo · frecuencia de retorno · D1/D7 · actividad post-reclamo
                    riesgo: reclamar y salir
quests diarias      objetivo: retorno + actividad
                    mide: participacion · completion · sesiones · conducta post-completion
                    · diversidad de contenido
achievements        objetivo: segun intencion (exploracion, maestria, rejugabilidad)
                    el KPI depende de cual de las tres
milestones          alcance · completion · tiempo · drop-off
prestige            tasa de prestige · tiempo hasta prestige · prestige repetido
                    · retencion post-prestige · aceleracion de progresion
battle pass         puede mover retencion, engagement, conversion y revenue a la vez
                    mide: inscripcion · completion · avance por tier · conversion a premium
                    · churn al fin de temporada
```

---

## FOMO, aversion a la perdida y recompensas variables

```txt
FOMO                    miedo a perderse algo. Sube actividad, y tambien estres,
                        burnout, frustracion y churn
aversion a la perdida   la perdida percibida pesa mas que una ganancia equivalente
recompensa variable     la recompensa incierta refuerza la repeticion
```

Se pueden identificar y medir. **No se optimizan ignorando** el bienestar del jugador, la retencion de largo plazo, la confianza, la reputacion y la regulacion. Un sistema que sube el D7 quemando el D30 no mejoro la retencion: la adelanto.

---

## Regla final

```txt
Que vuelva no dice que juegue.
Que juegue mucho no dice que vuelva.

Se miden las dos, y se declara con que definicion.
```

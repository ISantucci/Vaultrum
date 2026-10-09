## Que es

Un metodo para decidir **donde gastar el esfuerzo de verificacion** cuando el tiempo disponible es menor que la superficie a probar, que es siempre.

La idea es una sola: no todas las partes merecen el mismo esfuerzo. Se prueba mas hondo donde una falla cuesta mas y donde es mas probable que ocurra.

```txt
riesgo = probabilidad de que falle  x  impacto si falla
```

Y dos correcciones que en la practica pesan tanto como los dos factores originales:

```txt
dificultad de deteccion   cuanto cuesta darse cuenta de que fallo
exposicion                cuanta gente lo va a tocar, y cuan temprano
```

Un defecto grave pero evidente se descubre solo. Un defecto silencioso que corrompe partidas guardadas se descubre tres semanas despues, cuando ya no hay a que volver.

---

## Como se estima

Sin ceremonia: dos escalas de 1 a 5, una conversacion corta entre quien construyo y quien verifica, y el numero anotado.

| Factor | 1 | 5 |
|---|---|---|
| probabilidad | codigo estable, simple, sin tocar hace meses | sistema nuevo, complejo, recien integrado |
| impacto | molesto, hay como seguir | perdida de progreso, no se puede jugar, dano irreversible |
| deteccion | se ve al instante | silencioso, aparece dias despues |
| exposicion | camino opcional que pocos toman | camino obligatorio del primer minuto |

Que la estimacion sea subjetiva no la vuelve inutil: **ordena**. No hace falta que el numero sea exacto, hace falta que separe lo que se prueba primero de lo que se prueba si sobra tiempo.

Senales que suben el riesgo sin discusion:

```txt
toca datos persistentes (guardado, progresion, economia)
integra dos sistemas que no se conocian
se reescribio, no se retoco
ya fallo antes en esta zona
lo entiende una sola persona
se toca en el camino critico del primer minuto de juego
```

---

## Que produce

Una lista ordenada que responde tres cosas antes de empezar a probar:

```txt
que se prueba primero
que profundidad merece cada cosa
que NO se va a probar, dicho en voz alta
```

El tercero es el que le da valor a los otros dos. Un plan que no declara lo que deja afuera se lee como si cubriera todo, y despues nadie sabe si algo no fallo o si nadie lo miro.

**Riesgo aceptado no es riesgo ignorado.** Aceptar tiene tres requisitos: esta escrito, alguien lo acepta con nombre, y se sabe que pasa si ocurre.

---

## Severity y priority

La distincion que mas se mezcla, y la que mas discusiones evita cuando esta clara.

```txt
severity   cuanto DANA el defecto           lo determina el comportamiento
priority   cuanto URGE arreglarlo           lo determina el negocio o la produccion
```

### Severity

| Nivel | Que significa |
|---|---|
| **Bloqueante** | impide seguir probando o usando una parte critica: no hay camino alrededor |
| **Critico** | caida, perdida o corrupcion de datos, progresion rota, atasco severo, explotacion grave |
| **Mayor** | una funcionalidad importante hace algo incorrecto, pero el producto sigue usable |
| **Menor** | impacto acotado o con solucion alternativa simple |
| **Trivial** | cosmetico, sin impacto funcional |

### Priority

`Urgente` · `Alta` · `Media` · `Baja`

**Las dos escalas son independientes, y ahi esta el punto.** Un error de ortografia en la pantalla de titulo es severity trivial y priority urgente si la build se muestra manana en una feria. Una caida en un modo que nadie usa es severity critica y priority baja.

Mezclarlas produce los dos errores clasicos: arreglar primero lo mas grave aunque no importe ahora, o postergar lo grave porque hoy no molesta.

Quien las decide tampoco es el mismo: **la severidad la determina quien verifica**, sobre el comportamiento observado; **la urgencia la decide produccion**, sobre el contexto del proyecto.

---

## Como se aplica al esfuerzo

```txt
riesgo alto    casos dirigidos + limites + estados + exploratorio + regresion + automatizacion si se repite
riesgo medio   casos dirigidos del camino principal + limites + una sesion exploratoria
riesgo bajo    verificacion de que existe y funciona el camino feliz
```

Y el corolario que evita la trampa de la sensacion de cobertura: **el esfuerzo se corre cuando el riesgo se mueve.** Un sistema que fallo dos veces sube de categoria aunque el plan original dijera otra cosa.

---

## Anti-patrones

```txt
repartir el esfuerzo parejo por sistema
probar primero lo que es facil de probar
estimar riesgo sin quien construyo el sistema
aceptar un riesgo sin escribirlo ni ponerle dueno
tratar severity y priority como la misma columna
```

---

## Regla final

```txt
No alcanza para probar todo. Nunca alcanzo.

Lo que distingue a un control serio de uno improvisado
no es cuanto probo: es si puede decir que no probo, y por que.
```

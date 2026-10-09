## Que es

Cada fase del ciclo de vida de un juego hace **una pregunta distinta**, y la metrica correcta es la que responde la pregunta de la fase. Medir con los KPIs de otra fase no es exceso de rigor: es contestar una pregunta que nadie hizo.

El error mas comun tiene nombre propio:

```txt
ignorar la fase   usar KPIs de monetizacion avanzada en un prototipo
                  que todavia esta validando si el core loop funciona
```

---

## Las ocho fases

```txt
Planning         vale la pena construir esto?
Pre-Production   funciona el nucleo del juego?
Production       los sistemas construidos funcionan como deberian?
Testing          el jugador real se comporta como esperaba el diseno?
Pre-Launch       funciona como producto completo antes de escalar?
Launch           que pasa con el mercado real, a escala?
Post-Launch      como evoluciona el producto?
Live Ops         como se mantiene y se mejora un producto vivo?
```

### Planning

Se mira mercado, publico, competencia, propuesta de valor, modelo de negocio, alcance, viabilidad, canales, costos y potencial de ingresos. **Todavia no** hay ARPPU real, D30 real, DAU real ni economia real: cualquier numero de esos es una proyeccion y se declara como tal.

### Pre-Production

La pregunta es si el nucleo funciona, sobre prototipos y primeras pruebas.

```txt
task completion          se completa lo que se pide?
core-loop completion     se cierra el ciclo principal?
time to understand       cuanto tarda en entender que hacer?
feature discovery        llega a ver lo que existe?
feature adoption         lo usa?
failure points           donde falla?
abandono                 donde deja?
feedback cualitativo     que dice?
```

### Production

Los sistemas, uno por uno. Por feature: adopcion, frecuencia, completitud y distribucion de uso. Por nivel: start, complete, fail, intentos, tiempo y drop-off. Por economia: sources, sinks, balance y gasto. Por combate: pick rate, tasa de exito, dano y uso contextual.

### Testing

La idea es una: **expectativa contra realidad**. Tutorial, progresion, drop-off, fallas, uso de features, economia, balance, comportamiento de sesion, crashes y rendimiento.

Testing no es solo bugs. Buscar bugs es de Calidad; esta fase pregunta si la gente juega como el diseno supuso.

### Pre-Launch / Soft Launch

El producto completo, antes de escalar. Aparecen por primera vez los KPIs de producto con sentido:

```txt
retencion      D1 · D7 · D30
engagement     sesiones por usuario · duracion · tiempo jugado · uso de features
monetizacion   conversion · pagadores · ARPU · ARPAU · ARPPU
economia       sources · sinks · saldos
funnel         drop-offs
```

### Launch

El mercado real. Cinco areas: adquisicion, retencion, engagement, monetizacion y salud tecnica. Usuarios nuevos, DAU/WAU/MAU, D1/D7/D30, conversion, revenue, ARPU, ARPPU, crashes y reviews.

### Post-Launch

Tendencias, cohortes, churn, revenue, economia, consumo de contenido, comparacion por version y por segmento, y regresiones.

### Live Ops

Un ciclo, no una lista:

```txt
medir -> detectar -> hipotesis -> implementar -> medir -> comparar -> iterar
```

Las metricas dependen del objetivo de cada evento.

---

## Quien declara la fase

La fase es un dato del proyecto, no una opinion de quien mide. En Vaultrum la declara Produccion en el cuaderno del proyecto y en el `TL`; quien mide la lee y la respeta. Si no esta declarada, no se adivina: se pregunta.

Casi todo lo que hoy corre por la cadena de Vaultrum vive entre **Pre-Production y Testing**: prototipos y entregas jugables sin jugadores fuera del owner. Ahi la pregunta es si el nucleo funciona y si alguien lo entiende, no cuanto rinde por usuario.

---

## Modelos de negocio

La fase dice **que** preguntar; el modelo de negocio dice **que importa** de la respuesta.

```txt
Premium        compra inicial, DLC, expansiones
               adquisicion · conversion de tienda · unidades · revenue · reembolsos
               · completion · reviews · recomendacion
Free-to-play   microtransacciones, moneda premium, boosters, battle pass, ads
               adquisicion · retencion · engagement · conversion · ARPU · ARPPU
               · LTV · economia
Hibrido        pago inicial + monetizacion posterior
               ventas · retencion · engagement · monetizacion posterior · valor percibido
Suscripcion    MRR y sus componentes · suscriptores · renovacion · churn
Con anuncios   impresiones · impresiones por usuario · opt-in de rewarded · completion
               · revenue de ads · eCPM · Ad ARPDAU, siempre con retencion como guardrail
```

En premium la retencion **tambien** importa, por otra razon: satisfaccion, reputacion, DLC, secuelas y boca a boca.

En free-to-play la cadena conceptual es una sola:

```txt
entra -> vuelve -> interactua -> tiene oportunidad de convertir -> paga
```

---

## Modelo de negocio no es estrategia de monetizacion

El modelo dice como vive el producto. La estrategia dice por que canales entra el dinero:

```txt
directa     compra inicial · suscripcion · MTX · IAP · DLC · expansion · battle pass
            · cosmeticos · moneda premium · boosters · bundles · ofertas limitadas
indirecta   publicidad · rewarded · interstitial · product placement · sponsors
            · licencias · merchandising · cross-promotion
```

Dos juegos premium pueden tener estrategias opuestas. Confundir las dos cosas lleva a medir la estrategia de otro.

---

## Regla final

```txt
Antes de proponer una metrica, la pregunta es:
en que fase estamos, y que pregunta hace esa fase?

Una metrica correcta en la fase equivocada es ruido con buena formula.
```

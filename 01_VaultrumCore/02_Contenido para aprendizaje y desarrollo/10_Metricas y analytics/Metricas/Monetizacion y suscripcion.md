## Que es

Las metricas de dinero, y los errores de lectura que las acompanan. Ninguna de estas se interpreta sola: todas dependen de un denominador, y el denominador es lo primero que se pregunta.

---

## Los KPIs de monetizacion

```txt
revenue              ingresos del periodo. Nunca se interpreta aislado
pagadores            usuarios que pagaron en el periodo
conversion           pagadores / poblacion objetivo x 100
ARPU                 revenue / usuarios totales
ARPAU                revenue / usuarios activos
ARPPU                revenue / pagadores
ARPDAU               revenue diario / DAU. Util en F2P mobile, sobre todo con IAP + ads
LTV                  valor que genera un usuario durante su relacion con el producto
frecuencia de compra compras por pagador en el periodo
AOV                  revenue promedio por transaccion
```

**La poblacion de la conversion se declara:** todos los usuarios, los activos o los elegibles. Mezclar denominadores entre reportes produce dos conversiones que no se pueden comparar.

**ARPU cambia de definicion entre herramientas.** Algunas dividen por activos. El registro de metricas del proyecto dice cual se usa; el nombre no alcanza.

**LTV exige cinco cosas escritas:** definicion, horizonte, modelo de estimacion, que revenue incluye y por que segmento. Un LTV sin horizonte es un deseo.

Subir ARPPU es, sobre todo, que gasten mas quienes ya pagan: frecuencia, bundles, upselling, cross-selling, contenido premium, valor percibido. **Nunca se asume que subir precios mejora el ARPPU de forma sostenible.**

---

## La relacion entre conversion, ARPPU y ARPU

Con poblaciones y periodos compatibles:

```txt
ARPU ~= conversion x ARPPU
```

```txt
antes     conversion 4%   ARPPU $20   ARPU ~= 0.04 x 20 = $0.80
despues   conversion 7%   ARPPU $12   ARPU ~= 0.07 x 12 = $0.84
```

La conversion casi se duplico, el ARPPU cayo 40%, y el ARPU apenas se movio. **No se restan porcentajes y dolares directamente**: se recalcula el producto.

---

## Puntos porcentuales contra porcentaje relativo

```txt
conversion 4% -> 7%    +3 puntos porcentuales
                       +75% relativo
```

Las dos afirmaciones son ciertas y dicen cosas distintas. Un informe que dice "+3%" sin aclarar cual de las dos es ambiguo, y la ambiguedad siempre se lee a favor de quien escribio.

---

## Descuentos y elasticidad

Mas ventas no garantizan mas revenue:

```txt
antes     1000 x $10 = $10.000
despues   1600 x  $5 =  $8.000
          unidades +60%, revenue -20%
```

La **elasticidad** describe cuanto responde la demanda a un cambio de precio. No se asume que la respuesta de un juego se replique en otro.

---

## Suscripcion

```txt
MRR               revenue recurrente mensual, normalizado
New MRR           de suscriptores nuevos
Retained MRR      de suscriptores que ya estaban y siguen
Reactivated MRR   de ex-suscriptores que vuelven
Churned MRR       el del periodo anterior que se perdio
```

La relacion base:

```txt
Current MRR = New MRR + Retained MRR + Reactivated MRR
```

El Churned MRR **no forma parte** del MRR activo: se reporta aparte, para explicar la perdida respecto del periodo anterior.

Extensiones que existen y solo entran si el producto las necesita: Expansion MRR, Contraction MRR, Gross MRR Churn, Net Revenue Retention.

**MnRR** es el revenue mensual no recurrente: una montura, una mascota, un cambio de raza, un booster.

### MRR no es dinero cobrado

```txt
suscripcion anual de $156
cobrado en el mes    $156
MRR normalizado      $13 por mes
```

Confundir caja con revenue recurrente normalizado hace que un mes de renovaciones anuales parezca un pico de crecimiento.

---

## Regla final

```txt
Un numero de dinero sin denominador, sin periodo y sin la definicion
de la herramienta que lo calculo no es un KPI: es una cifra.

Y la etica no es un guardrail opcional: la monetizacion que sube el revenue
danando la confianza del jugador se paga despues, con intereses.
```

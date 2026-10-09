## Que es

Un **funnel** es una secuencia de etapas con su conversion entre cada una. Sirve para una pregunta sola: **donde se pierde la gente**.

El modelo base del recorrido completo del jugador:

```txt
Aware User -> Player -> Active Player -> Paying User -> High Paying User -> Advocate
```

Cada flecha es una transicion con un comportamiento detras, y cada comportamiento pide metricas distintas.

---

## Las etapas y que se mide en cada una

```txt
Aware User         conoce el producto          impresiones · alcance · clicks
                                               · trafico de tienda · canales
Player             empieza a jugar de verdad   jugadores nuevos · game start · tutorial start
                                               · FTUE · tutorial completion · drop-off temprano · D1
Active Player      permanece                   DAU/WAU/MAU · retencion · duracion y cantidad
                                               de sesiones · uso de features · contenido completado
Paying User        compra                      pagadores · conversion · ARPU · funnel de compra
                                               · visitas a la tienda
High Paying User   segmento de alto gasto      ARPPU · frecuencia de compra · distribucion
                                               del gasto · LTV · revenue por segmento
Advocate           recomienda                  referidos · invitaciones · reviews
                                               · contenido generado · aporte a la comunidad
```

El Advocate cierra el circulo: alimenta el Awareness de otros.

Una advertencia que se olvida siempre: **un ARPPU alto no demuestra por si solo que existan whales.** Puede ser un gasto parejo y alto. Para saberlo hay que mirar la distribucion.

---

## La regla de diagnostico del funnel

```txt
1. calcular la conversion entre etapas consecutivas
2. buscar el drop-off RELATIVO, no el numero absoluto mas chico
3. interpretar que comportamiento representa esa transicion
4. elegir los KPIs de esa transicion
5. investigar las causas
6. recien entonces, proponer cambios
```

**Nunca se ataca la ultima etapa porque su numero absoluto sea el menor.** Siempre va a ser el menor: es un funnel. El problema esta donde la conversion entre dos etapas cae mas de lo que el diseno esperaba.

---

## Adquisicion

```txt
impresiones · alcance · CTR · visitas a la pagina de tienda · conversion de tienda
· instalaciones · usuarios nuevos · organico vs pago · CPI · CAC · CPA
· atribucion por canal · ROAS
```

Adquirir mucha gente no sirve si abandona enseguida, si no es el publico objetivo, o si su valor no compensa lo que costo traerla. La adquisicion se juzga con la retencion y el LTV de lo que trajo, no con el volumen.

---

## FTUE y onboarding

**FTUE** es First Time User Experience: los primeros minutos, donde se decide el D1.

Se instrumenta como un funnel interno:

```txt
start -> paso 1 -> paso 2 -> paso 3 -> complete
```

Y por paso: tiempo, skip, fallo. Ademas, los primeros hitos reales: primera accion del core, primera recompensa, primer upgrade, drop-off temprano.

Como se disena un buen onboarding no vive aca: es del libro `09_Onboarding_y_tutorial` de la Biblioteca, que ademas propone sus eventos candidatos. Esta nota dice como leerlos.

---

## Drop-off

Punto de un proceso donde se pierde una proporcion relevante de jugadores. Aparece en tutoriales, progresion de niveles, compras, onboarding, quests, crafting y en el journey completo.

Se analiza siempre contra tres cosas:

```txt
la intencion del diseno   se esperaba perder gente aca? (un jefe filtro puede ser deliberado)
la poblacion elegible     todos podian llegar, o solo algunos?
el contexto               version, plataforma, evento, cambio reciente
```

Un drop-off esperado no es un problema. Uno inesperado es la primera pregunta de la proxima lectura.

---

## Regla final

```txt
El funnel no dice que cambiar. Dice donde mirar.

La etapa con menos gente no es la que peor anda:
es la que esta al final.
```

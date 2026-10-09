## Que es

Como se sabe si algo que se construyo **esta funcionando**: un nivel, un jefe, un tutorial, un arma, un sistema entero. Es la nota que mas se usa mientras el proyecto todavia no tiene jugadores a escala, porque no necesita DAU: alcanza con quien juega.

---

## Progresion

Toda progresion se instrumenta con tres estados:

```txt
start    empezo el nivel, el intento, el jefe
fail     fallo
complete completo
```

De esos tres salen casi todas las metricas:

```txt
starts · fails · completes
completion rate          completes / starts
failure rate             SE DEFINE (ver abajo)
intentos por completion  cuantas veces hay que intentarlo
tiempo hasta completar   y tiempo hasta fallar
drop-off                 empezaron y no volvieron a intentar
reintentos               cuantos vuelven despues de fallar
velocidad de progresion  cuanto avanza por unidad de tiempo
```

Usos: dificultad, balance, contenido confuso, muros de progreso, tutorial, jefes, niveles.

**La tasa de fallo tiene dos formulas posibles y no son intercambiables:**

```txt
fails / intentos terminados    ignora a quien abandono a mitad
fails / starts                 cuenta el abandono como no-exito
```

Se elige una, se escribe en el registro y no se cambia en silencio.

Como se disena una curva de dificultad vive en `06_Dificultad_y_curva` de la Biblioteca, con sus eventos candidatos —muertes por punto, intentos por examen—. Esta nota dice como leerlos.

---

## Las siete preguntas de una feature

```txt
descubrimiento   llega a verla?
adopcion         la usa por primera vez?
frecuencia       cuanto la usa?
profundidad      hasta donde usa sus funciones?
retencion de uso la sigue usando despues?
resultado        produce el comportamiento esperado?
impacto          mueve KPIs mayores?
```

El orden importa. Una feature con baja adopcion puede no tener un problema de diseno sino de descubrimiento: nadie la encontro. Arreglar el balance de algo que nadie vio no cambia nada.

**Adopcion sobre elegibles, no sobre todos.** Un arma que se desbloquea en el nivel 10 no puede tener adopcion medida sobre jugadores del nivel 2.

---

## De feature a KPI: ejemplos

```txt
starter pack        objetivo: primera compra
                    primario: conversion
                    secundarias: pagadores · ARPU · revenue · tasa de segunda compra
                    guardrails: ARPPU · retencion · reembolsos · economia

recompensa cada 6h  objetivo: frecuencia de retorno
                    primario: sesiones por usuario · frecuencia de retorno
                    secundarias: tasa de reclamo · actividad post-reclamo · retencion
                    riesgo: reclamar y salir

quests diarias      objetivo: retorno + actividad
                    KPIs: participacion · completion · sesiones por usuario · D7
                    · actividad objetivo

arma nueva          objetivo: sumar una opcion viable
                    KPIs: adopcion elegible · pick rate · frecuencia · rendimiento
                    · retencion de uso
                    5% de uso no se interpreta sin: elegibilidad, desbloqueo,
                    accesibilidad, rol y balance

nivel nuevo         start · complete · fail · intentos · tiempo · drop-off

sink de oro nuevo   cantidad hundida · adopcion · ratio source/sink · distribucion
                    de saldos · tiempo hasta poder pagar · progresion
                    guardrail: retencion

battle pass         participacion · conversion a premium · completion por tier
                    · engagement · revenue
                    guardrails: burnout · D30 · churn post-temporada
```

---

## Regla final

```txt
Una feature no funciona porque existe.
Funciona si la encuentran, la usan, la vuelven a usar
y produce lo que se diseno que produzca.

Cada una de esas cuatro cosas se mide por separado.
```

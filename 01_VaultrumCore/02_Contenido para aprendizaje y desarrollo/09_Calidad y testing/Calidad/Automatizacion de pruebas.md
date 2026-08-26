## Que es

Delegar a la maquina la ejecucion y la comparacion de una prueba: corre sola, compara contra un resultado esperado y avisa.

Lo que gana es concreto y medible:

```txt
velocidad        el resultado vuelve en minutos, no en horas
repetibilidad    la corrida de hoy es identica a la de ayer
precision        mide lo que un humano estima
combinatoria     recorre cientos de casos que nadie ejecutaria a mano
frecuencia       puede correr en cada cambio, no una vez por semana
```

Lo que no gana, y no va a ganar:

```txt
juicio           si lo que ve esta bien, cuando no hay un resultado esperado exacto
percepcion       si se siente bien, si se entiende, si molesta
descubrimiento   solo puede fallar lo que alguien penso que podia fallar
```

**Una prueba automatica no encuentra defectos: los detecta.** La diferencia importa: encuentra el que exploro, detecta el que ya se sabia buscar.

---

## Cuando automatizar

Al menos una de estas, o no vale el costo:

```txt
se va a ejecutar muchas veces
protege algo que ya se rompio antes
tiene demasiadas combinaciones para ejecucion humana regular
necesita medicion precisa (tiempos, memoria, cuadros por segundo)
necesita reproducibilidad exacta
si falla, la build no sale
```

## Cuando no

```txt
el sistema todavia cambia todas las semanas: el test cuesta mas que el riesgo
el valor esta en la percepcion humana
no hay un resultado esperado confiable contra el cual comparar
mantenerlo cuesta mas de lo que ahorra
es un caso que se va a correr dos veces en la vida del proyecto
```

Y una razon que no es razon: **automatizar por prestigio tecnico.** Una suite grande que nadie mira no es cobertura, es mantenimiento.

---

## El test tambien es software

Es la regla que mas se olvida, y la que mas dano hace cuando falta.

Un test automatico se escribe, tiene defectos, envejece y se rompe. Puede fallar cuando el producto esta bien —falso positivo— y puede pasar cuando el producto esta mal —falso negativo, el peor de los dos, porque tranquiliza.

Consecuencia operativa: **un test nuevo no deberia bloquear el pipeline el primer dia.** Primero demuestra estabilidad, despues bloquea. Estados utiles:

```txt
borrador     se esta escribiendo
revision     alguien mas lo mira
prueba       corre, pero su resultado no bloquea nada
confiable    corre y bloquea
cuarentena   fallo sin motivo suficientes veces: sigue corriendo, deja de bloquear
retirado     lo que probaba ya no existe
```

Un test inestable que bloquea builds es peor que no tener el test: entrena al equipo a ignorar el rojo. Y cuando el rojo se ignora por costumbre, el dia que es real tambien se ignora.

---

## Como se organizan las suites

No por carpeta, por **proposito operativo**: lo que define a una suite es que se hace cuando falla.

```txt
bloqueante   si falla, la build no se acepta                      minutos
esencial     regresion funcional del comportamiento ya validado   decenas de minutos
extendida    cobertura lenta, combinatoria, especifica            se corre por hito
```

Esa separacion es lo que permite que la respuesta a un rojo sea automatica y no una discusion.

---

## La forma de la piramide, y por que en juegos se deforma

El modelo general dice: muchas pruebas de unidad rapidas, menos de integracion, pocas de sistema.

En videojuegos la base se achica, y no por descuido: gran parte del comportamiento vive en la integracion entre motor, fisica, entrada, animacion y contenido, y no en funciones puras. Lo que si se puede automatizar bien:

```txt
logica pura        formulas, curvas, economia, reglas, transformaciones de datos
serializacion      guardar y cargar, migracion entre versiones
datos y contenido  validar que ninguna tabla apunte a algo que no existe
humo               arranca, entra al juego, hace lo minimo, no se cae
rendimiento        tiempos y memoria contra un presupuesto declarado
determinismo       misma semilla, mismo resultado
recorrido          bots que caminan el nivel buscando atascos y caidas
```

La regla que queda: automatizar lo que tiene un resultado esperado exacto, y dejar el juicio para las personas.

---

## Anti-patrones

```txt
automatizar todo
medir el exito por cantidad de pruebas automaticas
dejar en verde una suite ignorando fallas conocidas
tests que dependen del orden en que corren
tests sin comparacion de resultado: ejecutan y no verifican nada
una suite de humo tan grande que deja de ser humo
```

---

## Regla final

```txt
La automatizacion no reemplaza a quien verifica: le devuelve el tiempo.

Lo repetible a la maquina.
Lo que requiere criterio, a la persona.
```

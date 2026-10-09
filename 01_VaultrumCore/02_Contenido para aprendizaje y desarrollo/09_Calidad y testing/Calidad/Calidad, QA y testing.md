## Que es

Tres palabras que se usan como sinonimos y nombran cosas distintas.

```txt
Calidad   una propiedad del producto: cuanto satisface lo declarado y lo implicito
QA        el proceso que cuida esa propiedad, antes de que el producto exista
Testing   la actividad que produce informacion sobre esa propiedad
```

La confusion no es academica. Un equipo que dice "hay que mejorar la calidad" y contrata testers esta comprando informacion, no calidad. La informacion sola no arregla nada: la calidad la mejora quien corrige, con lo que el testing le mostro.

---

## Las tres, separadas

| | Pregunta que responde | Cuando actua | Sobre que trabaja |
|---|---|---|---|
| **QA** — aseguramiento | como evitamos producir defectos | antes y durante | el proceso |
| **QC** — control | que defectos tiene esto que ya existe | despues de construir | el producto |
| **Testing** | que pasa si hago esto | sobre una version concreta | el comportamiento |

QA es preventivo y es de todos: criterios de aceptacion claros, requisitos sin ambiguedad, revisiones, convenciones, testabilidad, definicion de terminado. QC es detectivo y necesita algo construido. El testing es la tecnica principal del QC, pero no la unica: una revision de codigo tambien es control de calidad y no ejecuta nada.

**La consecuencia practica:** si el unico esfuerzo de calidad del proyecto es testear al final, no hay QA. Hay QC tardio, que es la forma mas cara de descubrir que el requisito estaba mal escrito.

---

## Que informa un test

Un test no dice "esto esta bien". Dice:

```txt
en esta version, en este entorno, con estos datos,
al hacer esto, paso esto — y esperabamos aquello.
```

Todo lo que falte de esa oracion vuelve al resultado inutil. Un "no anda" sin version es una anecdota; con version, entorno, pasos y resultado esperado, es un dato que otra persona puede reproducir.

De ahi sale una regla que parece obvia y se rompe todo el tiempo: **un test necesita un resultado esperado antes de ejecutarlo.** Sin criterio previo, quien ejecuta decide al final si lo que vio estaba bien, y eso no es una prueba: es una opinion con pasos.

Al criterio de comparacion se lo llama **oraculo**. Puede ser un requisito, una especificacion, una version anterior, una formula, otra implementacion o una regla fisica. Cuando no hay oraculo confiable —"que tan divertido es"— no hay test posible, y hace falta otro metodo.

---

## Calidad interna, externa y en uso

Tres capas que se miden distinto y se confunden seguido.

```txt
interna   como esta construido      acoplamiento, duplicacion, claridad, deuda
externa   como se comporta          hace lo que dice, no se rompe, rinde
en uso    que consigue la persona   logra su objetivo, lo entiende, vuelve
```

Las tres son reales y ninguna implica a las otras. Un sistema impecable por dentro puede fallar a los treinta segundos; uno que funciona puede ser imposible de modificar; uno que funciona y es mantenible puede ser inutilizable.

En Vaultrum cada capa tiene dueno distinto: la interna la cuida el Area de Programacion contra `Principios SOLID` y `Patrones de diseno`; la externa la verifica el Area de Control de Calidad; la de uso la miran UI/UX y Produccion contra la experiencia prometida.

---

## Testabilidad: la calidad que decide todas las demas

Un sistema es testeable cuando se puede **controlar** su estado y **observar** su resultado sin adivinar.

```txt
controlabilidad   puedo poner el sistema en el estado que quiero probar, rapido y a voluntad
observabilidad    puedo ver que hizo por dentro, no solo lo que muestra la pantalla
```

Lo que la vuelve alta o baja:

- se puede llegar al caso en segundos, o hay que jugar veinte minutos para reproducirlo;
- se puede fijar la aleatoriedad con una semilla, o cada corrida es otra;
- hay logs que dicen que paso, o hay que deducirlo del comportamiento;
- el estado se puede guardar y restaurar, o se arma a mano cada vez;
- se pueden inyectar datos y condiciones, o hay que esperar a que ocurran;
- la logica esta separada de la presentacion, o solo se puede probar mirando.

**La testabilidad es una decision de diseno, no una virtud que aparece sola.** Un sistema poco testeable no se verifica menos: se verifica peor y mas caro, porque cada caso cuesta minutos en vez de segundos y varios directamente no se intentan.

Por eso es legitimo que quien verifica pida instrumentacion —una consola de comandos, un salto de nivel, un modo de datos, una semilla fija, un log— y eso es trabajo de desarrollo, no un capricho: baja el costo de todas las verificaciones que vienen despues.

---

## Trazabilidad

Es poder responder, para cualquier prueba, de que requisito viene, y para cualquier requisito, que prueba lo cubre.

```txt
sin trazabilidad   se prueba lo que se recuerda
con trazabilidad   se sabe que quedo sin probar, y eso es una decision, no un olvido
```

No sirve para el papeleo: sirve para dos preguntas concretas que aparecen siempre. *Cambio este requisito, que hay que volver a probar.* *Fallo esto, que requisito quedo incumplido.*

---

## Anti-patrones

```txt
usar "calidad" sin decir cual de las tres capas
testear sin resultado esperado escrito antes
llamar QA a lo que empieza cuando el codigo ya esta terminado
pedir mas testing en vez de mas testabilidad
tratar la instrumentacion de pruebas como trabajo que no produce
```

---

## Regla final

```txt
El testing no mejora la calidad. La mide.

Lo unico que la mejora es corregir lo que el testing mostro,
y disenar de manera que la proxima vez se vea antes.
```

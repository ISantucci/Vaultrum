## Definicion

Los errores conceptuales frecuentes son creencias sobre optimizacion que circulan como si fueran reglas, pero que en realidad son formulaciones incorrectas de una idea correcta.

Casi todas comparten la misma estructura.

```txt
Formulacion incorrecta
→ una operacion es mala

Formulacion correcta
→ una operacion es cara en un contexto determinado
```

El error no esta en el tema, sino en convertir un caso en una ley.

```txt
Observacion valida
→ "aca esto salio caro"

Generalizacion invalida
→ "esto siempre es malo"
```

Una creencia de este tipo produce decisiones sin medicion y discusiones que no se pueden cerrar con datos.

---

## Responsabilidad de esta nota

Esta nota no existe para invertir las reglas y prohibir lo contrario.

Esta nota no existe para defender malas practicas.

Esta nota no existe para dar una lista de tecnicas recomendadas.

Esta nota no existe para reemplazar la medicion.

Existe para desarmar creencias heredadas y devolver cada una a su forma condicional, la unica que se puede verificar.

Su responsabilidad es ayudar a responder:

```txt
¿Esto es un dato o es algo que se repite?
```

---

## Que problema ayuda a entender

Ayuda a entender por que un equipo puede optimizar mucho y mejorar poco.

```txt
Se elimina Update de todos lados.
Se poolea todo.
El frame sigue igual.
```

Ninguna de esas acciones ataco el cuello de botella, porque ninguna nacio de una medicion.

Tambien ayuda a entender por que estas creencias son tan resistentes.

```txt
Cada mito tiene un caso real detras.
El caso real es cierto.
La generalizacion no.
```

Por eso no alcanza con negarlas. Hay que reformularlas.

---

## Como funciona

Los doce mitos, con su correccion.

```txt
1. "Optimizacion prematura es la raiz de todo mal"
Incorrecto: nunca optimizar antes de tener un problema grave.
Correcto: no introducir complejidad basandose solo en problemas hipoteticos.
Si tiene sentido evitar O(n²) obvio, controlar lifecycles
y separar responsabilidades desde el principio.

2. "Update es malo"
Incorrecto.
Correcto: muchisimos callbacks o trabajo redundante por frame pueden ser costosos.

3. "MonoBehaviour es malo"
Incorrecto.
Correcto: no todo dominio de gameplay necesita estar acoplado
al lifecycle de MonoBehaviour.

4. "Instantiate es malo"
Incorrecto.
Correcto: instanciar repetidamente entidades complejas en hot paths
puede provocar costo y spikes.
```

```txt
5. "Siempre pooling"
Incorrecto.
Correcto: pooling intercambia CPU y allocations por memoria y complejidad.

6. "Nunca LINQ"
Incorrecto.
Correcto: ¿donde se usa? ¿cuantas veces? ¿que allocations produce?

7. "GetComponent es malo"
Incorrecto.
Correcto: ninguna operacion se discute sin costo × cantidad × frecuencia.

8. "Hay demasiados poligonos"
Puede ser cierto, pero sin medir es solo una hipotesis.
El bottleneck podria ser overdraw, shader, sombras o resolucion.
```

```txt
9. "Menos draw calls = mejor juego"
No necesariamente. Son una metrica, no un objetivo absoluto.
Agrupar de mas puede perjudicar culling, memoria y flexibilidad.

10. "60 FPS significa que esta optimizado"
No. Hay que conocer hardware objetivo, resolucion, calidad,
estabilidad, memoria y target.

11. "Mas threads = mas rapido"
No necesariamente. Paralelizar agrega sincronizacion y scheduling.
Tiene sentido sobre trabajo suficientemente grande y divisible.

12. "Optimizar = escribir codigo menos legible"
No. Una optimizacion que ahorra una cantidad despreciable
y destruye mantenibilidad normalmente es mala ingenieria.
```

El patron que atraviesa los doce es siempre el mismo.

```txt
El mito habla de una herramienta.
La realidad habla de un contexto de uso.
```

---

## Como aplicarlo en videojuegos

El caso del mito 2 en codigo.

Formulacion incorrecta llevada a la practica:

```csharp
void Update()
{
    moneyText.text = money.ToString();
    livesText.text = lives.ToString();
    waveText.text = wave.ToString();
}
```

El problema no es Update.

Es actualizar tres textos sesenta veces por segundo cuando los datos cambian unas pocas veces por oleada.

Formulacion correcta llevada a la practica:

```csharp
void OnEnable()  => model.MoneyChanged += OnMoneyChanged;
void OnDisable() => model.MoneyChanged -= OnMoneyChanged;

void OnMoneyChanged(int value) => moneyText.text = value.ToString();
```

Ejemplo inspirado en Tower Defense, aplicando la correccion a varios mitos a la vez:

```txt
Creencia:
"Los proyectiles usan Instantiate, hay que poolear todo."

Reformulacion:
¿Cuantos proyectiles por segundo se crean?
¿Aparece en la medicion como spike?
¿Que memoria residente cuesta el pool?
```

```txt
Creencia:
"El juego va a 60 FPS, esta optimizado."

Reformulacion:
¿En que hardware?
¿A que resolucion?
¿Con cuantos enemigos en pantalla?
¿Con que maximos de frame time?
```

---

## Como guia el diagnostico

Estas creencias suelen aparecer justo donde deberia haber una medicion, acortando el flujo a sintoma, creencia y solucion.

El flujo correcto reemplaza la creencia por evidencia.

```txt
Sintoma
→ hipotesis
→ medicion
→ diagnostico
→ solucion
```

Frente a cualquier afirmacion sobre performance, conviene aplicar el mismo filtro.

```txt
¿Quien lo midio?
¿En que escena?
¿En que hardware?
¿Cuanto costaba antes?
¿Cuanto cuesta ahora?
```

Si ninguna de esas preguntas tiene respuesta, lo que hay es una creencia.

Una creencia puede orientar una hipotesis. No puede cerrar un diagnostico.

---

## Cuando conviene consultarlo

Conviene revisar esta nota cuando:

```txt
Aparece una regla absoluta sobre performance.
Alguien propone una solucion antes de medir.
Se discute una API en lugar de un caso.
Se hereda codigo lleno de optimizaciones sin motivo documentado.
Se define un estandar de proyecto.
```

Tambien conviene consultarlo cuando una IA responde con una regla general.

```txt
"Evita GetComponent"
"Usa siempre pooling"
"Reduce los draw calls"
```

Ninguna incluye el contexto que la haria verificable.

---

## Cuando NO conviene forzarlo

No conviene usar esta nota para el efecto contrario.

```txt
"Como Update no es malo, uso Update en todo."
"Como pooling es un trade-off, nunca pooleo."
```

Desarmar un mito no habilita su opuesto.

Tampoco conviene abrir una discusion conceptual cuando ya hay una medicion clara.

```txt
El profiler muestra el costo en Instantiate.
No hace falta debatir si Instantiate es malo.
```

Con dato disponible, la creencia sobra.

Tampoco conviene reformular buenas practicas de arquitectura como si fueran mitos de performance: separar responsabilidades, controlar lifecycles, evitar dependencias ocultas.

Eso es ingenieria, y se sostiene aunque no mejore ningun milisegundo.

---

## Errores que ayuda a evitar

Revisar estas creencias ayuda a evitar:

- Aplicar reglas absolutas sin contexto de uso.
- Refactorizar sistemas enteros sin una medicion previa.
- Poolear entidades que se crean dos veces por partida.
- Perseguir el contador de draw calls como objetivo.
- Reducir poligonos cuando el costo estaba en fill rate.
- Declarar el juego optimizado por un numero de FPS.
- Paralelizar trabajo pequeño y agregar sincronizacion inutil.

La idea clave es:

```txt
Ninguna herramienta es mala.
Un uso puede ser caro en un contexto concreto.
```

---

## Riesgos de interpretarlo mal

Un riesgo comun es leer esta nota como permiso.

```txt
"Nada es malo, entonces da igual como lo escribo."
```

Que no haya reglas absolutas no significa que no haya criterios.

Otro riesgo es descartar la experiencia acumulada del equipo. La intuicion sirve para generar hipotesis y no para cerrar diagnosticos.

Los mitos suelen nacer de casos reales: sirven como sospecha inicial, no como conclusion.

Otro riesgo es quedarse en la correccion teorica sin medir nunca: se desarma el mito, no se mide igual, y queda la misma paralisis con distinto vocabulario.

Otro riesgo es aplicar el mito corregido y no validar.

```txt
Se acepta que Update no es malo.
Se dejan 900 Update activos.
Nunca se midio cuanto suman.
```

La reformulacion habilita medir. No reemplaza el resultado.

Criterio consolidado en Capsule Survivor.

---

## Hacia donde seguir

Esta nota pertenece a Fundamentos.

Lo que reemplaza a una creencia no es otra creencia.

Es un dato medido.

Si hace falta reformular la creencia como una estimacion verificable:

```txt
→ Costo cantidad y frecuencia
→ Medir antes de optimizar
```

Si hace falta declarar el precio de la tecnica discutida:

```txt
→ Trade-offs de optimizacion
```

Si hace falta convertir la creencia en una medicion concreta:

→ [[Diagnostico]]

---

## Checklist de diagnostico

Antes de aceptar una afirmacion sobre performance, revisar:

```txt
¿Es una regla absoluta o una condicion?
¿Menciona donde, cuantas veces y sobre cuantas entidades?
¿Hay una medicion detras?
¿En que escena y en que hardware se midio?
¿Distingue costo de carga de costo de hot path?
¿Declara que recurso se gasta a cambio?
¿La solucion propuesta ataca el bottleneck medido?
¿Se puede comparar antes y despues?
¿Se justifica la complejidad que agrega?
¿Sigue siendo mantenible el codigo resultante?
```

---

## Regla final

Un mito de optimizacion siempre habla de una herramienta.

Un diagnostico siempre habla de un contexto medido.

```txt
Ninguna operacion es mala.
Un uso puede ser caro.
La diferencia se resuelve midiendo, no discutiendo.
```

## Definicion

Fisica costosa es el problema que aparece cuando la simulacion fisica consume una porcion significativa del tiempo de CPU disponible por frame.

La fisica no es un sistema gratuito. Corre en CPU y compite con gameplay, IA, animacion y preparacion del rendering.

El costo depende de varios factores a la vez:

```txt
Cantidad de cuerpos.
Cantidad y tipo de colliders.
Cantidad de contactos activos.
Cantidad de queries.
Frecuencia de simulacion.
Complejidad geometrica.
```

Ninguno es caro por si solo. El problema aparece cuando se multiplican:

```txt
Costo unitario
× cantidad
× frecuencia
=
costo real de fisica
```

---

## Responsabilidad de esta nota

Esta nota existe para diagnosticar cuando la fisica es la que esta consumiendo el frame.

No existe para sugerir que la fisica deberia evitarse.
No existe para prohibir geometrias de colision complejas.
No existe para fijar un timestep universal.
No existe para imponer un limite de queries por agente.

Su responsabilidad es ayudar a responder:

```txt
¿El costo de fisica esta justificado por el comportamiento que el juego necesita?
```

El foco no esta en usar menos fisica.

El foco esta en entender:

```txt
cuantos cuerpos se simulan
cuantas veces por segundo se simulan
cuantas interacciones son posibles
cuantas queries se lanzan y desde cuantos agentes
que precision necesita realmente el gameplay
```

---

## Sintomas

Sintomas comunes:

```txt
Frame time que sube al aumentar la cantidad de cuerpos.
Physics visible como bloque grande en el Profiler.
Spikes al aparecer una oleada o al detonar explosiones.
Costo alto aunque los scripts propios sean baratos.
```

Un sintoma particular de la fisica es que el costo puede no depender del codigo propio:

```txt
Ningun Update propio es caro
+
el frame igual sube
→
sospechar fisica.
```

---

## Que parte del software suele causarlo

Suele originarse en:

```txt
Muchos rigidbodies activos.
Colliders con geometria mas compleja de la necesaria.
Contactos permanentes entre objetos apilados.
Matrices de colision sin filtrar.
Queries lanzadas desde cada agente cada frame.
Timestep mas chico de lo que el gameplay pide.
```

Ejemplo tipico:

```csharp
private void FixedUpdate()
{
    for (int i = 0; i < 5; i++)
    {
        Physics.Raycast(origin, directions[i], out hit, range);
    }
}
```

Cinco queries por agente parecen baratas. El costo real no se lee en el metodo, se lee en la multiplicacion.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
CPU
Frame Budget
Bucle de fisica
```

La fisica trabaja asociada a un timestep fijo, no al frame de render.

Eso significa que un frame puede contener mas de un paso de simulacion:

```txt
frame largo
→ varios pasos de fisica acumulados
→ frame todavia mas largo
```

---

## Como detectarlo

Se detecta separando el costo de fisica del costo de los scripts propios.

Buscar especialmente:

```txt
Tiempo consumido por Physics dentro del frame.
Cantidad de pasos de simulacion por frame.
Cantidad de cuerpos activos y de contactos resueltos.
Cantidad de queries por segundo.
Costo que crece con la cantidad de entidades.
```

Preguntas practicas:

```txt
¿Cuantos de los cuerpos simulados necesitan ser fisicos?
¿Que timestep esta configurado y con que criterio se eligio?
¿Cuantas queries se lanzan por frame y desde cuantos agentes?
¿Hay categorias que nunca deberian interactuar y aun asi se evaluan?
```

---

## Herramientas de deteccion

Herramientas utiles:

```txt
Unity Profiler
CPU Usage
Physics Profiler
Physics Debugger
```

Que mirar:

```txt
Peso del bloque Physics dentro del frame.
Pasos de simulacion, cuerpos activos y contactos.
Costo del FixedUpdate propio.
Spikes coincidentes con spawns o explosiones.
```

Logs utiles:

```txt
Cantidad de rigidbodies activos.
Cantidad de raycasts por segundo.
Cantidad de agentes con sensores activos.
```

---

## Soluciones posibles

Soluciones candidatas:

```txt
Ajustar el timestep al minimo que sostiene el comportamiento.
Simplificar la geometria de colision.
Filtrar interacciones con Physics Layers.
Reducir frecuencia y cantidad de queries por agente.
Reemplazar fisica por logica cuando el gameplay no la necesita.
```

Sobre el timestep:

```txt
menor timestep
→ mas simulaciones por segundo
→ mas costo

mayor timestep
→ menos costo
→ menos precision
```

Sobre colliders, el criterio es funcional y no una regla:

```txt
Utilizar la representacion mas simple
que preserve correctamente el comportamiento requerido.
```

Cuando el gameplay lo permite:

```txt
Box
Sphere
Capsule
```

suelen ser mas economicos que una malla de colision detallada.

Pero si el comportamiento pedido depende de la forma real, simplificar no es optimizar: es romper el juego.

Sobre Physics Layers:

```txt
Si dos categorias nunca deben interactuar,
el sistema no deberia considerar esa combinacion.
```

Sobre queries fisicas:

```txt
Costo de query
× cantidad de agentes
× frecuencia
```

Ejemplo:

```txt
1 raycast
→ irrelevante.

5 raycasts × 500 NPC × 60 FPS
→ un problema completamente distinto.
```

Version con filtro de capa e intervalo:

```csharp
private void FixedUpdate()
{
    if (Time.time < nextScan)
    {
        return;
    }

    nextScan = Time.time + scanInterval;
    Physics.Raycast(origin, forward, out hit, range, obstacleMask);
}
```

---

## Trade-offs

Cada solucion intercambia algo.

```txt
Timestep mas grande
→ menos costo
→ menos precision y mas riesgo de atravesamiento.

Colliders simples
→ menos costo
→ menos fidelidad de forma.

Physics Layers
→ menos trabajo
→ una matriz mas que mantener y documentar.

Menos queries por agente o por segundo
→ menos CPU
→ mas latencia y percepcion mas gruesa.
```

La fisica es un caso claro del intercambio general:

```txt
performance ↔ precision
```

---

## Ejemplo en videojuegos

En un Tower Defense:

```txt
300 enemigos avanzando por el camino.
600 proyectiles en vuelo.
30 torres detectando objetivos por rango.
```

Version cara:

```txt
Cada enemigo con rigidbody y collider de malla.
Cada torre lanzando overlaps cada frame.
Todas las capas pudiendo colisionar entre si.
```

Version medida:

```txt
Enemigos con capsule collider.
Torres evaluando rango por intervalo, no por frame.
Matriz de colision donde proyectil no interactua con proyectil.
```

El juego se ve igual.

El costo de fisica no.

---

## Como guia el diagnostico

Esta nota guia el diagnostico cuando el costo crece con la cantidad de entidades simuladas.

Flujo recomendado:

```txt
Sintoma:
frame que crece con la cantidad de entidades.

Sospecha:
la fisica esta dominando el frame.

Medicion:
Profiler, bloque Physics, pasos de simulacion.

Dato esperado:
Physics con peso alto y creciente.

Problema confirmado:
costo de simulacion, contactos o queries.

Solucion candidata:
filtrar, simplificar, espaciar o distribuir.
```

La pregunta clave es:

```txt
¿Cuanta simulacion necesita realmente este comportamiento?
```

---

## Errores comunes al intentar solucionarlo

Errores comunes:

```txt
Subir el timestep hasta que aparecen atravesamientos.
Reemplazar todas las mallas de colision sin revisar comportamiento.
Copiar una cantidad de raycasts de otro proyecto.
Optimizar fisica sin haber medido que la fisica fuera el cuello.
```

Ejemplo de mala solucion:

```txt
Problema:
Physics caro.

Solucion:
timestep al doble.

Resultado:
menos costo, pero proyectiles que atraviesan enemigos.
```

Un juego mas rapido que se rompe no esta optimizado.

---

## Hacia donde seguir

Si todavia no se confirmo que la fisica sea el cuello:

→ [[Diagnostico]]

Si hace falta entender el presupuesto que la fisica esta gastando:

→ [[Fundamentos]]

Si el patron util es filtrar barato antes de calcular caro:

→ [[Patrones transversales]]

Notas relacionadas dentro de esta rama:

```txt
Distribucion temporal del trabajo
Particionado espacial
IA que piensa de mas
Reducir frecuencia de actualizacion
```

---

## Checklist de diagnostico

```txt
¿Se midio que Physics domina el frame?
¿Cuantos de los cuerpos activos necesitan ser fisicos?
¿Que timestep esta configurado y con que criterio?
¿Hay cuerpos apilados generando contactos permanentes?
¿La geometria de colision es la mas simple que sostiene el comportamiento?
¿Hay capas que nunca deberian interactuar y no estan filtradas?
¿Cuantas queries por frame se lanzan y necesitan esa cantidad?
¿Se puede distribuir el trabajo entre frames?
¿Se valido el gameplay despues del cambio?
```

---

## Regla final

La fisica se paga por paso de simulacion, por contacto y por query.

```txt
Simular lo que el juego necesita,
con la precision que el juego necesita,
tantas veces como el juego necesita.
Nada mas.
```

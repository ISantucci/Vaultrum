## Definicion

Medir antes de optimizar significa no aplicar cambios de rendimiento sin evidencia previa.

La optimizacion debe partir de datos.

No de intuicion.

La idea principal es:

```txt
Primero medir.
Despues diagnosticar.
Despues optimizar.
Despues validar.
```

Optimizar sin medir puede llevar a resolver problemas que no existen, empeorar la arquitectura o tocar partes del sistema que no eran el cuello de botella.

---

## Responsabilidad de esta nota

Esta nota existe para explicar el criterio de evidencia antes de tocar codigo.

No existe para reemplazar herramientas de deteccion.
No existe para listar todas las soluciones posibles.
No existe para frenar todo cambio pequeño y seguro.

Su responsabilidad es ayudar a responder:

```txt
¿Tengo evidencia suficiente para proponer esta optimizacion?
```

Esta nota es transversal, pero pertenece a Fundamentos porque define una regla base de toda optimizacion.

---

## Que problema ayuda a entender

Este principio ayuda a evitar optimizacion prematura y soluciones mal dirigidas.

Ejemplo incorrecto:

```txt
El juego baja FPS.
Supongo que son los graficos.
Bajo poligonos y calidad.
El problema sigue.
```

Ejemplo correcto:

```txt
El juego baja FPS.
Mido con Profiler.
Veo CPU alto en scripts.
Investigo logica por frame.
Aplico solucion sobre la causa real.
```

Medir antes de optimizar ayuda a responder:

- El problema existe realmente?
- Cuando ocurre?
- Que recurso afecta?
- Que sistema lo causa?
- Que tan grave es?
- Que solucion tiene sentido?
- Como se si mejoro?
- El cambio vale el trade-off?

---

## Como funciona

El proceso recomendado es:

```txt
1. Reproducir el problema.
2. Medir con herramientas.
3. Identificar sintoma y contexto.
4. Formular hipotesis.
5. Confirmar causa probable.
6. Aplicar solucion puntual.
7. Medir despues.
8. Comparar resultados.
```

Ejemplo:

```txt
Sintoma:
Stuttering al disparar muchas balas.

Medicion:
Profiler muestra Instantiate/Destroy y GC Alloc.

Diagnostico:
Creacion/destruccion constante genera spikes.

Solucion:
Object Pool.

Validacion:
Menos Instantiate/Destroy.
Menos GC Alloc.
Menos spikes.
```

Sin medicion final, no se sabe si la solucion funciono.

---

## Como aplicarlo en videojuegos

En un proyecto real, se puede aplicar como rutina.

Antes de optimizar:

```txt
Definir escena de prueba.
Definir cantidad de objetos.
Definir duracion de prueba.
Definir herramienta de medicion.
Guardar medicion inicial.
```

Despues de optimizar:

```txt
Repetir la misma prueba.
Comparar datos.
Verificar que no se rompio gameplay.
Documentar resultado.
```

Ejemplo inspirado en Tower Defense:

```txt
Prueba:
Nivel con 100 enemigos y 20 torres.
Duracion: 60 segundos.

Antes:
Medir frame time, spikes, GC Alloc, scripts.

Cambio:
Aplicar Object Pool a proyectiles.

Despues:
Repetir misma escena y comparar.
```

La comparacion debe ser equivalente.

Si cambian las condiciones, la conclusion pierde valor.

---

## Como guia el diagnostico

Medir antes de optimizar guia todo el flujo de trabajo.

No pregunta primero:

```txt
¿Que tecnica uso?
```

Pregunta primero:

```txt
¿Que evidencia tengo?
```

Flujo recomendado:

```txt
Sintoma
→ reproduccion
→ medicion
→ hipotesis
→ confirmacion
→ cambio puntual
→ validacion
```

Ejemplo:

```txt
Sintoma:
La UI parece lenta.

Mala respuesta:
Reescribir toda la UI.

Mejor respuesta:
Medir si la UI se actualiza por frame.
Revisar si hay reconstrucciones innecesarias.
Confirmar costo.
Aplicar solucion puntual.
```

---

## Cuando conviene consultarlo

Conviene aplicar este principio siempre que se vaya a hacer una optimizacion relevante.

Casos:

```txt
Cambiar arquitectura.
Agregar Update Manager.
Implementar Object Pool.
Reducir calidad visual.
Cambiar sistema de carga.
Modificar frecuencia de IA.
Reescribir targeting.
Cambiar UI.
Optimizar memoria.
```

Tambien conviene usarlo antes de pedirle a una IA o agente que modifique un proyecto.

```txt
Primero analizar.
Despues proponer.
Despues cambiar.
Despues validar.
```

---

## Cuando NO hace falta una medicion pesada

No siempre hace falta una medicion profunda para cambios triviales.

Ejemplo:

```txt
Eliminar un Debug.Log accidental en Update.
Cachear una referencia obvia que se busca cada frame.
Evitar una concatenacion de string claramente innecesaria.
```

Pero incluso en esos casos, si el cambio es grande o afecta arquitectura, conviene medir.

Regla practica:

```txt
Cambio pequeño y seguro
→ medicion liviana puede alcanzar.

Cambio grande o estructural
→ medir antes y despues.
```

La medicion debe ser proporcional al riesgo del cambio.

---

## Errores que ayuda a evitar

Medir antes de optimizar ayuda a evitar:

- Optimizar por intuicion.
- Resolver problemas que no existen.
- Tocar sistemas que no eran bottleneck.
- Agregar sobrearquitectura.
- Reducir calidad sin justificar.
- No saber si una mejora funciono.
- Comparar escenarios distintos.
- Hacer varios cambios a la vez sin poder atribuir resultados.
- Confundir sintomas con causas.
- Romper gameplay en nombre del rendimiento.

La idea clave es:

```txt
Una optimizacion no validada es solo una suposicion.
```

---

## Riesgos de interpretarlo mal

Un riesgo es usar “hay que medir” como excusa para no hacer cambios obvios.

Ejemplo:

```txt
Hay un FindObjectOfType dentro de Update.
Se puede cachear la referencia sin reescribir arquitectura.
```

Ese cambio puede ser seguro y razonable.

Otro riesgo es exigir mediciones perfectas cuando una hipotesis tecnica clara ya permite avanzar de forma controlada.

Ejemplo:

```txt
No tengo una medicion completa.
Pero detecte Instantiate/Destroy constante en gameplay.
Puedo proponer medirlo o aplicar una prueba controlada.
```

Medir antes de optimizar no significa paralizar el trabajo.

Significa no hacer cambios grandes sin criterio.

---

## Hacia donde seguir

Esta nota pertenece a Fundamentos.

Si se quiere entender cuanto tiempo hay disponible:

```txt
→ [[Frame Budget]]
```

Si se quiere identificar el cuello de botella:

```txt
→ [[Bottleneck]]
```

Si hace falta elegir herramienta:

```txt
→ [[Herramientas de deteccion]]
```

Herramientas utiles:

```txt
Unity Profiler
CPU Usage
Timeline
GC Alloc
Memory Profiler
Comparacion antes y despues
```

Si ya existe un sintoma:

```txt
→ [[Problemas de rendimiento]]
```

Si ya se confirmo un problema:

```txt
→ [[Metodologias y soluciones]]
```

---

## Checklist antes de optimizar

Antes de proponer una optimizacion, revisar:

```txt
¿Cual es el sintoma?
¿Se puede reproducir?
¿En que escena ocurre?
¿Con que cantidad de objetos ocurre?
¿Que herramienta permite medirlo?
¿Que recurso parece afectado?
¿Que dato confirmaria la hipotesis?
¿La solucion ataca la causa real?
¿Existe una alternativa mas simple?
¿Que trade-off trae?
¿Como se validara despues?
```

---

## Regla final

Medir antes de optimizar no es burocracia.

Es criterio tecnico.

```txt
Sin medicion o hipotesis clara
→ no hay diagnostico confiable.

Sin diagnostico confiable
→ no hay optimizacion justificada.
```
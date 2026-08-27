## Definicion

Strings por frame ocurre cuando el juego crea cadenas de texto nuevas de forma repetida durante gameplay, especialmente dentro de `Update`, loops, UI o logs.

En C#, los strings son inmutables.

Eso significa que cuando se concatena o genera un string nuevo, normalmente se crea una nueva instancia en memoria.

La idea principal es:

```txt
Strings nuevos por frame
→ allocations
→ presion sobre Garbage Collector
→ posibles spikes
```

No todo string es un problema.

El problema aparece cuando se generan strings constantemente en caminos criticos.

---

## Responsabilidad de esta nota

Esta nota existe para diagnosticar problemas causados por creacion repetida de strings durante gameplay.

No existe para prohibir todos los strings.
No existe para microoptimizar textos que no importan.
No existe para reemplazar la medicion de GC Alloc.

Su responsabilidad es ayudar a responder:

```txt
¿El juego esta creando strings nuevos de forma repetida?
```

El foco esta en detectar strings creados en:

```txt
Update
UI
logs
debug
loops
sistemas de puntaje
sistemas de vida
objetivos
cooldowns
```

---

## Sintomas

Sintomas comunes:

```txt
GC Alloc por frame.
Spikes periodicos.
Stuttering.
Frame time irregular.
Allocations al actualizar UI.
Allocations al mostrar puntaje, vida, dinero o cooldowns.
Tirones cuando hay muchos textos actualizandose.
```

Tambien puede verse asi:

```txt
La UI parece simple.
Pero el Profiler muestra GC Alloc constante.
```

O:

```txt
El juego anda bien.
Pero aparecen tirones cada pocos segundos por GC.
```

---

## Que parte del software suele causarlo

Suele aparecer en:

```txt
UI de puntaje.
UI de vida.
UI de monedas.
Contadores.
Cooldowns.
Objetivos.
Logs en gameplay.
Debug por frame.
Mensajes de daño.
Popups.
Indicadores flotantes.
```

Ejemplo problematico:

```csharp
private void Update()
{
    scoreText.text = "Score: " + score;
}
```

Otro ejemplo:

```csharp
private void Update()
{
    Debug.Log("Enemy position: " + transform.position);
}
```

Otro ejemplo:

```csharp
timerText.text = "Time: " + currentTime.ToString();
```

Si ocurre cada frame sin que el dato cambie, genera trabajo innecesario.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
Garbage Collector
Memoria administrada
CPU
Frame Budget
```

Los strings nuevos generan allocations.

Muchas allocations pueden generar presion sobre el GC.

El GC puede provocar spikes cuando limpia memoria.

---

## Como detectarlo

Se detecta buscando allocations asociadas a UI, texto o logs.

Buscar especialmente:

```txt
Concatenaciones en Update.
ToString repetido.
Debug.Log por frame.
Interpolacion de strings por frame.
Textos actualizados aunque el valor no cambie.
Popups creados constantemente.
UI que se refresca completa todo el tiempo.
```

Preguntas practicas:

```txt
¿El texto cambia realmente cada frame?
¿Se esta asignando text aunque el valor sea igual?
¿Hay logs activos durante gameplay?
¿Hay concatenaciones en loops?
¿Hay ToString en caminos criticos?
¿Se puede actualizar solo cuando cambia el dato?
```

---

## Herramientas de deteccion

Herramientas utiles:

```txt
Unity Profiler
GC Alloc
Timeline
Logs de diagnostico
Revision de codigo
```

Que mirar:

```txt
GC Alloc.
Managed allocations.
Allocations asociadas a UI.
Allocations asociadas a strings.
Metodos de actualizacion de texto.
Debug.Log repetido.
```

Tambien conviene revisar si ocurre:

```txt
cada frame
por evento
por cantidad de objetos
solo en editor
solo con debug activo
```

---

## Soluciones posibles

Soluciones candidatas:

```txt
Actualizar texto solo cuando cambia el dato.
Evitar Debug.Log en gameplay repetido.
Cachear valores visibles.
Evitar concatenaciones por frame.
Usar StringBuilder en casos justificados.
Reducir frecuencia de actualizacion.
UI orientada a eventos.
Evitar ToString repetido si no hace falta.
Desactivar logs de diagnostico en build.
```

Ejemplo:

```txt
Antes:
Actualizar scoreText en Update.

Despues:
Actualizar scoreText solo cuando cambia score.
```

Ejemplo conceptual:

```csharp
public void SetScore(int newScore)
{
    if (newScore == currentScore)
        return;

    currentScore = newScore;
    scoreText.text = $"Score: {currentScore}";
}
```

Aunque se cree un string, ocurre solo cuando cambia el valor.

Eso suele ser mucho mejor que hacerlo cada frame.

---

## Trade-offs

Reducir strings por frame suele ser positivo, pero no debe volverse obsesivo.

```txt
Actualizar por evento
→ menos allocations
→ requiere flujo de eventos claro.

Cachear valores
→ evita actualizaciones repetidas
→ agrega estado a mantener.

StringBuilder
→ util en construcciones complejas
→ innecesario para textos simples ocasionales.

Reducir logs
→ mejora rendimiento
→ puede dificultar debug si se elimina todo.
```

No conviene hacer microoptimizaciones si el string se crea una vez o fuera de gameplay.

El foco debe estar en strings frecuentes.

---

## Ejemplo en videojuegos

En un HUD:

```txt
Vida
Dinero
Puntaje
Oleada
Cooldown
Municion
Objetivos
```

Mala estrategia:

```txt
Cada texto se actualiza en Update aunque no cambie.
```

Estrategia mas sana:

```txt
Vida
→ se actualiza cuando cambia la vida.

Dinero
→ se actualiza cuando cambia el dinero.

Oleada
→ se actualiza cuando cambia la oleada.

Cooldown
→ puede actualizarse por intervalo o solo si esta visible.
```

En un Tower Defense:

```txt
moneyText.text = "Money: " + money;
waveText.text = "Wave: " + wave;
healthText.text = "Health: " + baseHealth;
```

Si esto corre cada frame sin cambios, genera trabajo innecesario.

---

## Como guia el diagnostico

Esta nota guia el diagnostico cuando hay GC Alloc o spikes asociados a texto.

Flujo recomendado:

```txt
Sintoma:
GC Alloc por frame o stuttering.

Sospecha:
strings creados por frame.

Medicion:
Profiler / GC Alloc / revision de codigo.

Dato esperado:
allocations asociadas a UI, logs o texto.

Problema confirmado:
creacion repetida de strings.

Solucion candidata:
actualizar solo cuando cambia el dato o reducir logs.
```

La pregunta clave es:

```txt
¿Este texto necesita reconstruirse ahora?
```

---

## Errores comunes al intentar solucionarlo

Errores comunes:

```txt
Intentar eliminar todos los strings del juego.
Optimizar texto que se crea una vez.
Usar StringBuilder para casos simples sin necesidad.
Dejar Debug.Log en Update.
Actualizar texto aunque el valor no cambie.
Cambiar toda la UI sin medir.
Confundir un string ocasional con GC Alloc por frame.
```

Ejemplo de mala solucion:

```txt
Problema:
Un texto se actualiza una vez al iniciar.

Decision:
Crear sistema complejo de cacheo de strings.

Resultado:
sobrearquitectura.
```

La frecuencia define la importancia.

---

## Hacia donde seguir

Si hace falta entender GC:

```txt
→ GC Alloc por frame
→ Recursos de hardware
```

Si hace falta medir:

```txt
→ Unity Profiler
→ GC Alloc
→ Timeline
```

Si el problema viene de UI:

```txt
→ UI actualizada innecesariamente
→ UI orientada a eventos
```

Si se confirma allocation frecuente:

```txt
→ Evitar allocations por frame
```

Si el problema viene de logs:

```txt
→ Logs de diagnostico
```

---

## Checklist de diagnostico

```txt
¿Hay strings creados en Update?
¿Hay concatenaciones por frame?
¿Hay ToString repetido?
¿Hay interpolacion de strings en loops?
¿Hay Debug.Log en gameplay?
¿La UI actualiza texto aunque no cambie?
¿El Profiler muestra GC Alloc?
¿La allocation ocurre cada frame?
¿Se puede actualizar solo por evento?
¿Se puede cachear el ultimo valor mostrado?
¿La solucion mantiene legibilidad?
```

---

## Regla final

Los strings no son el problema.

El problema es reconstruirlos constantemente sin necesidad.

```txt
Si el dato no cambio,
el texto no deberia reconstruirse.
```
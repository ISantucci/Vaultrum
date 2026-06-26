## Definicion

Las busquedas globales por frame ocurren cuando un sistema busca objetos, componentes o referencias dentro de la escena de forma repetida durante gameplay.

En Unity, operaciones como buscar objetos en la escena pueden tener costo si se ejecutan con demasiada frecuencia.

La idea principal es:

```txt
Buscar en la escena
× cada frame
× muchos objetos
=
costo acumulado de CPU
```

No toda busqueda es un problema.

El problema aparece cuando se buscan referencias de forma repetida en caminos criticos, especialmente dentro de `Update`, `FixedUpdate`, loops, IA, targeting o UI.

---

## Responsabilidad de esta nota

Esta nota existe para diagnosticar problemas causados por busquedas repetidas durante gameplay.

No existe para prohibir toda busqueda.
No existe para decir que todo debe estar cacheado siempre.
No existe para reemplazar una medicion real.

Su responsabilidad es ayudar a responder:

```txt
¿El juego esta buscando referencias demasiadas veces?
```

El foco esta en detectar si el costo viene de:

```txt
busquedas en escena
busquedas de componentes
busquedas por tag
busquedas globales
GetComponent repetido
FindObjectOfType repetido
GameObject.Find repetido
```

---

## Sintomas

Sintomas comunes:

```txt
CPU Usage alto.
Scripts costosos.
Caidas de FPS al aumentar objetos.
Frame time mayor con mas enemigos o torres.
Costo creciente sin que aumente mucho el render.
Spikes o microtirones al ejecutar logica.
```

Tambien puede verse asi:

```txt
Pocos objetos
→ no se nota.

Muchos objetos
→ el costo de busqueda se acumula.
```

O:

```txt
Un sistema funciona bien al inicio.
Pero escala mal cuando hay mas entidades activas.
```

---

## Que parte del software suele causarlo

Suele aparecer en sistemas como:

```txt
Enemigos buscando al jugador.
Torres buscando enemigos.
Proyectiles buscando objetivos.
UI buscando managers.
Managers buscando objetos cada frame.
Sistemas de spawn buscando referencias.
Sistemas de audio buscando fuentes.
Sistemas de objetivos buscando elementos en escena.
```

Ejemplo problematico:

```csharp
private void Update()
{
    Player player = FindObjectOfType<Player>();
}
```

Otro ejemplo:

```csharp
private void Update()
{
    var health = GetComponent<Health>();
}
```

Otro ejemplo:

```csharp
private void Update()
{
    GameObject target = GameObject.FindWithTag("Player");
}
```

El problema no es usar estas funciones una vez.

El problema es usarlas repetidamente en runtime sin necesidad.

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
CPU
Game Loop
Frame Budget
```

Puede afectar indirectamente:

```txt
Garbage Collector
```

si la busqueda genera allocations o estructuras temporales.

Tambien puede empeorar con la escala:

```txt
Mas objetos en escena
→ mas trabajo potencial de busqueda
→ mayor costo acumulado
```

---

## Como detectarlo

Se detecta revisando codigo y midiendo costo de scripts.

Buscar especialmente:

```txt
FindObjectOfType en Update.
GameObject.Find en Update.
FindWithTag repetido.
GetComponent repetido en loops.
Busquedas dentro de IA.
Busquedas dentro de targeting.
Busquedas dentro de UI.
Busquedas en listas grandes cada frame.
```

Preguntas practicas:

```txt
¿La referencia podria guardarse una vez?
¿La busqueda ocurre cada frame?
¿La busqueda ocurre por cada objeto?
¿La busqueda ocurre dentro de un loop?
¿La referencia cambia realmente?
¿Existe un sistema que ya podria proveerla?
```

---

## Herramientas de deteccion

Herramientas utiles:

```txt
Unity Profiler
CPU Usage
Timeline
Logs de diagnostico
Revision de codigo
```

Que mirar:

```txt
Tiempo en Scripts.
Metodos llamados muchas veces.
Costo de sistemas de targeting.
Costo de sistemas de IA.
Cantidad de llamadas por segundo.
Costo que escala con cantidad de objetos.
```

Logs utiles:

```txt
Cantidad de busquedas por segundo.
Cantidad de objetos iterados.
Cantidad de enemigos evaluados.
Cantidad de torres buscando objetivo.
```

---

## Soluciones posibles

Soluciones candidatas:

```txt
Cacheo de referencias.
Inyeccion de referencias.
Asignacion por inspector.
Registro en managers.
Eventos.
Listas mantenidas por sistemas responsables.
Reducir frecuencia de busqueda.
Buscar una vez al inicializar.
Buscar solo cuando cambia el contexto.
```

Ejemplo:

```txt
Antes:
Cada enemigo busca al jugador en Update.

Despues:
El spawner o manager entrega la referencia al jugador al crear el enemigo.
```

Otro ejemplo:

```txt
Antes:
Cada UI busca el GameManager cada frame.

Despues:
La UI recibe la referencia al inicializarse o escucha eventos.
```

Otro ejemplo:

```txt
Antes:
Cada torre busca todos los enemigos cada frame.

Despues:
Un sistema mantiene una lista de enemigos activos y la torre consulta con frecuencia controlada.
```

---

## Trade-offs

Reducir busquedas mejora rendimiento, pero trae responsabilidades.

```txt
Cacheo de referencias
→ menos busquedas
→ riesgo de referencias invalidas si el objeto se destruye.

Managers o registros
→ acceso mas ordenado
→ riesgo de acoplamiento si crecen demasiado.

Eventos
→ menos polling
→ cuidado con suscripciones y desuscripciones.

Asignacion por inspector
→ simple y clara
→ puede fallar si falta configurar.

Inyeccion de referencias
→ dependencias mas claras
→ requiere flujo de creacion ordenado.
```

La solucion debe ser proporcional al problema.

No todo necesita un sistema global.

---

## Ejemplo en videojuegos

En un Tower Defense:

```txt
Torres
→ necesitan enemigos para apuntar.

Enemigos
→ pueden necesitar la base o waypoint.

Proyectiles
→ pueden necesitar su target.

UI
→ necesita vida, dinero y oleada.
```

Mala estrategia:

```txt
Cada objeto busca sus dependencias cada frame.
```

Estrategia mas sana:

```txt
Spawner
→ entrega referencias al crear.

EnemyRegistry
→ mantiene enemigos activos.

TowerTargeting
→ consulta enemigos activos con frecuencia controlada.

UI
→ escucha eventos de cambios.
```

El objetivo no es evitar toda busqueda.

Es evitar busquedas repetidas innecesarias.

---

## Como guia el diagnostico

Esta nota guia el diagnostico cuando el costo parece venir de busquedas frecuentes.

Flujo recomendado:

```txt
Sintoma:
CPU alto o caidas con muchos objetos.

Sospecha:
busquedas globales por frame.

Medicion:
CPU Usage / Timeline / revision de codigo.

Dato esperado:
metodos de busqueda repetidos o logica escalando con objetos.

Problema confirmado:
referencias buscadas demasiadas veces.

Solucion candidata:
cacheo, registro, eventos o reduccion de frecuencia.
```

La pregunta clave es:

```txt
¿Esta referencia necesita buscarse ahora, o podria conocerse antes?
```

---

## Errores comunes al intentar solucionarlo

Errores comunes:

```txt
Cachear referencias sin validar ciclo de vida.
Crear un Service Locator global para todo.
Convertir todos los accesos en managers.
No limpiar referencias a objetos destruidos.
Reemplazar una busqueda simple por una arquitectura compleja.
Cachear algo que cambia constantemente sin actualizarlo.
No medir si la busqueda era realmente costosa.
```

Ejemplo de mala solucion:

```txt
Problema:
Un objeto busca al player una vez.

Decision:
Crear un sistema global de referencias.

Resultado:
complejidad innecesaria.
```

La busqueda ocasional puede estar bien.

El problema es la repeticion en caminos criticos.

---

## Hacia donde seguir

Si hace falta entender frecuencia:

```txt
→ Game loop
```

Si hace falta medir CPU:

```txt
→ Unity Profiler
→ CPU Usage
→ Timeline
```

Si se confirma el problema:

```txt
→ Cacheo de referencias
→ Reducir frecuencia de actualizacion
→ UI orientada a eventos
```

Si las busquedas ocurren dentro de muchos Updates:

```txt
→ Muchos Update activos
```

Si las busquedas generan allocations:

```txt
→ GC Alloc por frame
→ Evitar allocations por frame
```

Si se necesita organizar acceso a dependencias:

```txt
→ MonoBehaviour como puente
→ Separar logica de Unity
```

---

## Checklist de diagnostico

```txt
¿Hay FindObjectOfType en runtime?
¿Hay GameObject.Find en runtime?
¿Hay FindWithTag repetido?
¿Hay GetComponent dentro de Update o loops?
¿La busqueda ocurre por cada objeto?
¿La busqueda ocurre cada frame?
¿La referencia podria asignarse una vez?
¿La referencia podria cachearse?
¿Hay riesgo de referencia destruida?
¿Se midio CPU Usage?
¿La solucion reduce busquedas reales?
¿La solucion no crea una dependencia global innecesaria?
```

---

## Regla final

Buscar una referencia una vez puede estar bien.

Buscarla todo el tiempo sin necesidad es el problema.

```txt
Si una dependencia no cambia,
no deberia buscarse cada frame.
```
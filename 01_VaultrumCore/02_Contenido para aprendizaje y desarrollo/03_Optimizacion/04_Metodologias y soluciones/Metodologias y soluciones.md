## Proposito

Esta subcarpeta reune tecnicas, practicas y arquitecturas que pueden ayudar a prevenir o resolver problemas de rendimiento.

No existe para aplicar soluciones por costumbre.
No existe para demostrar tecnica.
No existe para reemplazar el diagnostico.

Existe para elegir una respuesta posible despues de entender el problema y medirlo.

La idea principal es:

```txt
problema medido
→ solucion candidata
→ trade-off
→ aplicacion controlada
→ validacion
```

---

## Idea central

Una solucion de optimizacion solo tiene sentido si responde a un problema real o a un riesgo claro.

No deberia ser:

```txt
Tecnica conocida
→ buscar donde aplicarla
```

Debe ser:

```txt
Problema diagnosticado
→ alternativa adecuada
→ costo de implementacion
→ riesgo
→ validacion
```

Optimizar tambien implica decidir que no tocar.

---

## Cuando usar esta subcarpeta

Usar esta subcarpeta cuando ya exista un diagnostico o una hipotesis tecnica suficientemente clara.

Conviene consultarla cuando:

- ya se midio un problema,
- se conoce el recurso afectado,
- se busca una solucion candidata,
- hay que evaluar trade-offs,
- se quiere prevenir un problema recurrente,
- una IA necesita proponer una implementacion sin sobrearquitecturar,
- se necesita validar si una tecnica corresponde al caso.

---

## Como debe usar esta subcarpeta una IA

Una IA debe usar esta subcarpeta para evaluar soluciones, no para imponerlas.

No debe razonar asi:

```txt
Hay muchos objetos.
→ Object Pool.
```

Debe razonar asi:

```txt
Hay muchos objetos temporales.
→ medir Instantiate/Destroy y GC Alloc.
→ confirmar costo.
→ evaluar Object Pool.
→ revisar trade-off.
→ validar mejora.
```

Antes de proponer una solucion, la IA debe poder explicar:

```txt
que problema resuelve
por que aplica
que alternativa simple existe
que riesgo introduce
como se valida
```

---

## Metodologias incluidas

### [[Addressables como metodologia de optimizacion]]

Metodologia para gestionar carga, descarga y organizacion de assets.

Consultar cuando el problema este relacionado con assets pesados, carga de escenas, memoria o contenido que no deberia estar siempre cargado.

### [[Clases puras]]

Practica para separar logica de Unity y reducir dependencia innecesaria de MonoBehaviour.

Consultar cuando haya logica que no necesita vivir directamente en un componente de Unity.

### [[Evitar allocations por frame]]

Practica para reducir objetos temporales y presion sobre el Garbage Collector.

Consultar cuando haya GC Alloc por frame, strings temporales, listas nuevas o allocations repetidas.

### [[Monobehaviour como puente|MonoBehaviour como puente]]

Metodologia para usar MonoBehaviour como entrada hacia logica separada.

Consultar cuando un sistema esta demasiado acoplado a Unity o mezcla ciclo de vida con reglas de negocio.

### [[Reducir frecuencia de actualizacion]]

Practica para evitar ejecutar logica costosa todos los frames.

Consultar cuando IA, percepcion, targeting, pathfinding o UI se actualicen con mas frecuencia de la necesaria.

### [[Separar logica de unity|Separar logica de Unity]]

Criterio para separar reglas del juego de dependencias directas de Unity.

Consultar cuando un sistema sea dificil de testear, medir, reutilizar o aislar.

### [[UI orientada a eventos]]

Practica para actualizar UI solo cuando cambian los datos relevantes.

Consultar cuando la UI se actualiza por frame o recalcula informacion sin necesidad.

---

## Soluciones incluidas

### [[Assetmanager como optimizacion|AssetManager]]

Sistema para coordinar acceso, carga o descarga de assets segun necesidad del proyecto.

Consultar cuando haga falta organizar el uso de assets sin cargar todo de forma directa o descontrolada.

### [[Cacheo de referencias]]

Solucion para evitar busquedas repetidas de objetos, componentes o dependencias.

Consultar cuando existan busquedas globales, GetComponent repetido o accesos frecuentes innecesarios.

### [[Object pool como optimizacion|Object Pool como optimizacion]]

Solucion para reutilizar objetos en lugar de crearlos y destruirlos constantemente.

Consultar cuando haya proyectiles, enemigos, efectos, particulas u objetos temporales repetidos.

### [[Update Manager como optimizacion|Update Manager]]

Solucion para centralizar y controlar actualizaciones.

Consultar cuando haya muchos Update activos, frecuencia excesiva o necesidad de priorizar actualizaciones.

---

## Temas relacionados pero no propios de esta subcarpeta

Estos temas pueden aparecer en el razonamiento, pero pertenecen a otras partes del vault o a otra subcarpeta.

```txt
Medir antes de optimizar
→ Fundamentos

Patrones de diseno
→ 02_Patrones de diseno

Managers
→ seccion correspondiente de managers

SOLID
→ Principios SOLID
```

No se deben linkear desde aca salvo que haya una necesidad operativa concreta.

---

## Como se conecta con otras subcarpetas

Esta subcarpeta es el ultimo paso antes de aplicar cambios.

El flujo correcto es:

```txt
Fundamentos
→ entender el criterio base

Problemas de rendimiento
→ identificar el problema

Herramientas de deteccion
→ medir y confirmar

Metodologias y soluciones
→ elegir respuesta candidata
```

Ejemplo:

```txt
Problema:
Instantiate y Destroy constantes.

Herramienta:
Unity Profiler / Timeline / GC Alloc.

Solucion candidata:
Object Pool.

Validacion:
Comparacion antes y despues.
```

---

## Criterio de uso

Una solucion no debe aplicarse solo porque existe.

Antes de aplicarla, preguntar:

```txt
Que problema resuelve?
El problema fue medido?
Que evidencia existe?
Que alternativa simple existe?
Que trade-off trae?
Que riesgo introduce?
Como se valida?
```

Si no hay respuesta clara, no se implementa todavia.

---

## Regla final

```txt
Metodologias y soluciones no existe para aplicar tecnicas.
Existe para elegir respuestas justificadas despues de diagnosticar.
```
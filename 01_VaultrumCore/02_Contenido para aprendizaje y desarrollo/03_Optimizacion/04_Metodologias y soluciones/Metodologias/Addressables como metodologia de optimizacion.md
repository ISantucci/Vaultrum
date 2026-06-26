## Definición

Addressables como metodología de optimización es una forma de gestionar assets para controlar mejor cuándo se cargan, cuándo se descargan y qué contenido permanece en memoria.

Addressables no debe pensarse solamente como una herramienta técnica de Unity.

Dentro de optimización, conviene entenderlo como una metodología para organizar contenido de forma más escalable.

La idea principal es:

```txt
Assets directos en escena
→ carga rígida y menos controlada

Assets direccionables
→ carga bajo demanda y mejor control de memoria
```

Addressables permite que el proyecto trabaje con referencias direccionables en lugar de depender siempre de referencias directas en escena o prefabs.

Esto ayuda a separar:

```txt
Contenido del juego
→ prefabs, texturas, audio, efectos, escenas

Momento de uso
→ cuándo realmente se necesitan

Gestión de memoria
→ cuándo cargarlos y cuándo liberarlos
```

---

## Qué problema ayuda a prevenir

Ayuda a prevenir problemas como:

```txt
Escenas demasiado pesadas.
Assets cargados desde el inicio sin necesidad.
Memoria RAM alta.
VRAM alta.
Cargas iniciales largas.
Referencias directas excesivas.
Dificultad para descargar contenido.
Contenido modular mal organizado.
Assets cargados aunque no correspondan al nivel actual.
```

Ejemplo:

```txt
Un juego tiene 20 tipos de enemigos.

Pero el Nivel 1 usa solo 3.

Sin gestión:
la escena puede terminar referenciando demasiados assets.

Con Addressables:
se pueden cargar solo los enemigos necesarios para ese nivel.
```

La metodología apunta a una pregunta:

```txt
¿Qué assets necesita realmente este contexto del juego?
```

---

## Cómo funciona

Addressables permite marcar assets como direccionables y cargarlos mediante una referencia o dirección.

Flujo conceptual:

```txt
Asset marcado como Addressable
→ sistema pide asset
→ Unity lo carga cuando hace falta
→ sistema lo usa
→ cuando deja de usarse, se libera
```

La idea es evitar que todos los assets estén acoplados directamente a una escena o prefab.

Esto permite trabajar con:

```txt
Carga bajo demanda.
Contenido por nivel.
Contenido desbloqueable.
Bundles o grupos de assets.
Referencias indirectas.
Carga asincrónica.
Descarga controlada.
```

Addressables por sí solo no garantiza optimización.

Debe usarse con criterio.

```txt
Cargar bajo demanda
→ útil

Cargar en medio de gameplay crítico sin planificación
→ posible stuttering
```

---

## Cómo aplicarlo en videojuegos

Se puede aplicar a:

```txt
Prefabs de enemigos.
Prefabs de torres.
Modelos.
Texturas.
Audio.
Efectos visuales.
Íconos.
UI pesada.
Escenas.
Skins.
Contenido por nivel.
Contenido desbloqueable.
```

Ejemplo:

```txt
Nivel 1
→ carga enemigos básicos, torres básicas y efectos simples.

Nivel 5
→ carga enemigos especiales, torres avanzadas y efectos nuevos.

Menú
→ carga solo UI, música de menú e íconos necesarios.
```

En un Tower Defense:

```txt
Cada nivel puede tener su propio set de enemigos, torres, proyectiles y efectos.

Addressables permite que esos recursos no tengan que estar todos cargados desde el inicio.
```

---

## Relación con arquitectura

Addressables se relaciona con:

```txt
Recursos de hardware
Memory Profiler
Memory Leak
AssetManager como optimizacion
Factory
Object pool como optimizacion
```

También se relaciona con separación de responsabilidades.

```txt
Gameplay
→ no debería conocer detalles internos de carga.

Sistema de assets
→ debería resolver cómo se obtiene el recurso.
```

Addressables es la metodología de carga direccionable.

Pero en proyectos más ordenados, normalmente conviene que el gameplay no hable directamente con Addressables.

Ahí aparece el AssetManager.

```txt
Gameplay
→ pide recurso a AssetManager

AssetManager
→ usa Addressables internamente
```

---

## Relación con hardware/runtime

Afecta principalmente:

```txt
RAM
VRAM
Disco
CPU
Tiempo de carga
Frame Budget
```

Puede ayudar a mejorar:

```txt
Memoria inicial.
Carga de escenas.
Descarga de contenido no usado.
Organización de assets.
Escalabilidad de contenido.
```

Pero puede perjudicar si se usa mal:

```txt
Carga en momentos críticos.
No liberar recursos.
Cargas duplicadas.
Dependencias mal organizadas.
Stuttering por carga asincrónica mal planificada.
```

---

## Cuándo conviene usarlo

Conviene cuando:

```txt
El proyecto tiene muchos assets.
Hay niveles con contenido distinto.
Hay contenido desbloqueable.
Hay skins o variantes.
Hay escenas pesadas.
La memoria empieza a importar.
Se apunta a escalabilidad.
Se quiere reducir referencias directas.
Se quiere cargar contenido bajo demanda.
```

Ejemplos:

```txt
Juegos por niveles.
Juegos con muchos enemigos.
Juegos con muchas torres.
Juegos con skins.
Juegos con mapas grandes.
Juegos con audio o texturas pesadas.
```

---

## Cuándo NO conviene usarlo

No conviene forzarlo cuando:

```txt
El proyecto es muy chico.
Hay pocos assets.
No hay problemas de carga.
No hay problemas de memoria.
El equipo todavía está prototipando gameplay básico.
La complejidad no se justifica.
```

Ejemplo:

```txt
Prototipo con 5 prefabs simples
→ Addressables puede ser exceso.
```

---

## Trade-offs

Ventajas:

```txt
Carga bajo demanda.
Mejor control de memoria.
Menor peso inicial de escenas.
Mejor organización de contenido.
Más escalabilidad.
Contenido modular.
```

Costos:

```txt
Más configuración.
Cargas asincrónicas.
Manejo de dependencias.
Necesidad de liberar correctamente.
Más testing.
Posibles errores por referencias mal configuradas.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Usar Addressables sin liberar recursos.
Cargar assets pesados durante gameplay crítico.
Acoplar gameplay a keys de Addressables.
Duplicar cargas.
No manejar errores de carga.
No entender dependencias.
Pensar que por usar Addressables ya se optimizó.
```

Ejemplo malo:

```txt
El jugador dispara.
En ese momento se carga por primera vez el prefab del proyectil.

Resultado:
posible tirón en gameplay.
```

Mejor:

```txt
Antes de empezar el nivel:
precargar proyectiles necesarios.
```

---

## Checklist de implementación

```txt
¿Hay suficientes assets como para justificar Addressables?
¿Hay contenido que no siempre se necesita?
¿Se definieron grupos de assets?
¿Se sabe cuándo cargar cada recurso?
¿Se sabe cuándo liberarlo?
¿Se evita cargar en gameplay crítico?
¿Se mide memoria antes/después?
¿Se valida con Memory Profiler?
¿El gameplay está desacoplado de las keys?
¿Hay una capa como AssetManager?
```

---

## Regla final

Addressables como metodología de optimización sirve para organizar la carga de contenido de forma más controlada.

```txt
No optimiza por existir.
Optimiza cuando permite cargar menos, cargar mejor y liberar correctamente.
```
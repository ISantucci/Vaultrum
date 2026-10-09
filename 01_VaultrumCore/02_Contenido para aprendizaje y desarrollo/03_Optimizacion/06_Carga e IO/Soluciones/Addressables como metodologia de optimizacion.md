## Definicion

Addressables como metodologia de optimizacion es una forma de gestionar assets para controlar mejor cuando se cargan, cuando se descargan y que contenido permanece en memoria.

Addressables no debe pensarse solamente como una herramienta tecnica de Unity.

Dentro de optimizacion, conviene entenderlo como una metodologia para organizar contenido de forma mas escalable.

La idea principal es:

```txt
Assets directos en escena
→ carga rigida y menos controlada

Assets direccionables
→ carga bajo demanda y mejor control de memoria
```

Addressables permite que el proyecto trabaje con referencias direccionables en lugar de depender siempre de referencias directas en escena o prefabs.

Esto ayuda a separar:

```txt
Contenido del juego
→ prefabs, texturas, audio, efectos, escenas

Momento de uso
→ cuando realmente se necesitan

Gestion de memoria
→ cuando cargarlos y cuando liberarlos
```

---

## Que problema ayuda a prevenir

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

Sin gestion:
la escena puede terminar referenciando demasiados assets.

Con Addressables:
se pueden cargar solo los enemigos necesarios para ese nivel.
```

La metodologia apunta a una pregunta:

```txt
¿Que assets necesita realmente este contexto del juego?
```

---

## Como funciona

Addressables permite marcar assets como direccionables y cargarlos mediante una referencia o direccion.

Flujo conceptual:

```txt
Asset marcado como Addressable
→ sistema pide asset
→ Unity lo carga cuando hace falta
→ sistema lo usa
→ cuando deja de usarse, se libera
```

La idea es evitar que todos los assets esten acoplados directamente a una escena o prefab.

Esto permite trabajar con:

```txt
Carga bajo demanda.
Contenido por nivel.
Contenido desbloqueable.
Bundles o grupos de assets.
Referencias indirectas.
Carga asincronica.
Descarga controlada.
```

Addressables por si solo no garantiza optimizacion.

Debe usarse con criterio.

```txt
Cargar bajo demanda
→ util

Cargar en medio de gameplay critico sin planificacion
→ posible stuttering
```

---

## Como aplicarlo en videojuegos

Se puede aplicar a:

```txt
Prefabs de enemigos.
Prefabs de torres.
Modelos.
Texturas.
Audio.
Efectos visuales.
Iconos.
UI pesada.
Escenas.
Skins.
Contenido por nivel.
Contenido desbloqueable.
```

Ejemplo:

```txt
Nivel 1
→ carga enemigos basicos, torres basicas y efectos simples.

Nivel 5
→ carga enemigos especiales, torres avanzadas y efectos nuevos.

Menu
→ carga solo UI, musica de menu e iconos necesarios.
```

En un Tower Defense:

```txt
Cada nivel puede tener su propio set de enemigos, torres, proyectiles y efectos.

Addressables permite que esos recursos no tengan que estar todos cargados desde el inicio.
```

---

## Relacion con arquitectura

Addressables se relaciona con:

```txt
Recursos de hardware
Memory Profiler
Memory Leak
AssetManager como optimizacion
Factory
Object pool como optimizacion
```

Tambien se relaciona con separacion de responsabilidades.

```txt
Gameplay
→ no deberia conocer detalles internos de carga.

Sistema de assets
→ deberia resolver como se obtiene el recurso.
```

Addressables es la metodologia de carga direccionable.

Pero en proyectos mas ordenados, normalmente conviene que el gameplay no hable directamente con Addressables.

Ahi aparece el AssetManager.

```txt
Gameplay
→ pide recurso a AssetManager

AssetManager
→ usa Addressables internamente
```

---

## Relacion con hardware/runtime

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
Organizacion de assets.
Escalabilidad de contenido.
```

Pero puede perjudicar si se usa mal:

```txt
Carga en momentos criticos.
No liberar recursos.
Cargas duplicadas.
Dependencias mal organizadas.
Stuttering por carga asincronica mal planificada.
```

---

## Cuando conviene usarlo

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

## Cuando NO conviene usarlo

No conviene forzarlo cuando:

```txt
El proyecto es muy chico.
Hay pocos assets.
No hay problemas de carga.
No hay problemas de memoria.
El equipo todavia esta prototipando gameplay basico.
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
Mejor organizacion de contenido.
Mas escalabilidad.
Contenido modular.
```

Costos:

```txt
Mas configuracion.
Cargas asincronicas.
Manejo de dependencias.
Necesidad de liberar correctamente.
Mas testing.
Posibles errores por referencias mal configuradas.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Usar Addressables sin liberar recursos.
Cargar assets pesados durante gameplay critico.
Acoplar gameplay a keys de Addressables.
Duplicar cargas.
No manejar errores de carga.
No entender dependencias.
Pensar que por usar Addressables ya se optimizo.
```

Ejemplo malo:

```txt
El jugador dispara.
En ese momento se carga por primera vez el prefab del proyectil.

Resultado:
posible tiron en gameplay.
```

Mejor:

```txt
Antes de empezar el nivel:
precargar proyectiles necesarios.
```

---

## Checklist de implementacion

```txt
¿Hay suficientes assets como para justificar Addressables?
¿Hay contenido que no siempre se necesita?
¿Se definieron grupos de assets?
¿Se sabe cuando cargar cada recurso?
¿Se sabe cuando liberarlo?
¿Se evita cargar en gameplay critico?
¿Se mide memoria antes/despues?
¿Se valida con Memory Profiler?
¿El gameplay esta desacoplado de las keys?
¿Hay una capa como AssetManager?
```

---

## Regla final

Addressables como metodologia de optimizacion sirve para organizar la carga de contenido de forma mas controlada.

```txt
No optimiza por existir.
Optimiza cuando permite cargar menos, cargar mejor y liberar correctamente.
```
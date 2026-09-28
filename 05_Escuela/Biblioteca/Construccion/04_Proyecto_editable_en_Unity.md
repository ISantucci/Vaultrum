---
tipo: construccion
estado: En la Biblioteca
mision: EST-017_Mision_Proyecto_editable_en_Unity
remite: Type Object, Separar logica de unity, Monobehaviour como puente, Clases puras, Managers y Unity, Memory Leak, Instantiate y destroy constantes, Object pool como optimizacion, Draw calls y batching, Separar canvas por frecuencia de cambio, Cuando NO optimizar, Baseline de entregable
cruza: 01_Bucle_de_simulacion
---

# Construcción 04 — Proyecto editable en Unity

> Libro de **autoría**: dónde vive el contenido de un juego dentro de un proyecto de Unity para que quien lo diseña lo vea y lo cambie sin tocar código. Cubre escenas, prefabs, ScriptableObjects, serialización, herramientas de editor, el horneado hacia herramientas externas y los generadores de una sola vez.
> **No cubre:** cuánto cuesta cada cosa (materiales, batching, reservas, basura por cuadro, canvas). Eso es del Core y se **remite**, no se re-legisla. Tampoco la arquitectura de gameplay (`Separar logica de unity`, `Monobehaviour como puente`, `Clases puras`) ni el ciclo de vida de un manager (`Managers y Unity`): este libro aporta el mecanismo que esas notas dan por sabido.
> **IP:** conceptos destilados y citados. Ningún texto verbatim con copyright.

---

## Índice del libro

- Qué es y por qué se rompe si falta
- El modelo — tres lugares donde vive el contenido
- Las cinco relaciones
- El diagrama, con sus invariantes
- Herramientas de editor — lo mínimo que hace editable una escena
- Generadores y migraciones — herramientas de una sola vez
- Los seis modos de fallar
- Proyecto que ya existe — dos lecturas
- Baseline
- Aplicación · Límites · Fuentes

---

## Qué es y por qué se rompe si falta

Un proyecto de Unity no es código con assets al costado. Es un **editor de contenido**. Lo que el diseñador toca —un nivel, una torre, el HUD— vive en archivos que el editor guarda y muestra. El código los lee.

Si el contenido se arma por código al dar Play, con objetos creados en tiempo de ejecución, valores en literales o datos en archivos que el editor no muestra, el juego puede andar perfecto y el proyecto queda **cerrado**. Para mover un punto del camino hay que pedírselo a quien programó. Así lo dijo el owner de ClashDefense al abrir su propio proyecto: *"Yo no veo mis niveles, no veo cómo están hechas las cosas"*. Deshacerlo costó una entrega entera (`TL-003`, 534 archivos).

**Poner la autoría en assets no es una cuestión de prolijidad. Decide quién puede cambiar el juego y cuánto le cuesta cada cambio.** Cada valor que solo se puede tocar desde el código es un pedido futuro. En Vaultrum, los pedidos del owner son el presupuesto que más se cuida (`Baseline de entregable`).

---

## El modelo — tres lugares donde vive el contenido

```txt
ESCENA            lo que tiene posición: el nivel, sus caminos, áreas, spawns, cámara, luz
PREFAB            lo que se repite: una torre, un enemigo, un efecto, una pieza de interfaz
SCRIPTABLEOBJECT  lo que es dato y no tiene lugar: balance, oleadas, catálogos, temas
                  ─ los tres son archivos del proyecto, cada uno con su .meta ─
CÓDIGO            los lee. Nunca es el lugar donde vive un valor de diseño.
```

Cuatro mecanismos sostienen el modelo, y cada uno trae su trampa:

**Identidad.** Cada asset tiene un identificador guardado en su archivo `.meta`. Las referencias entre escenas, prefabs y ScriptableObjects apuntan a ese identificador, no a la ruta. Por eso Unity puede mover o renombrar un asset sin romper nada. **La trampa:** si el asset se mueve por fuera del editor y pierde su `.meta`, todas las referencias a él quedan vacías (manual, *Asset metadata*). Mover archivos es una operación de dos archivos, nunca de uno.

**Serialización.** Lo que el Inspector muestra, lo que se guarda y lo que un prefab puede sobrescribir es exactamente lo que se serializa. Se serializa un campo público o marcado `[SerializeField]`, que no sea `static`, `const` ni `readonly`, y cuyo tipo sea primitivo, enum, tipo de Unity, clase o struct `[Serializable]`, referencia a un objeto de Unity, o array o `List` de esos tipos. **No** se serializan las propiedades, los diccionarios, los arrays multidimensionales ni los contenedores anidados. Por defecto se serializa por valor; `[SerializeReference]` agrega referencias compartidas, nulos y polimorfismo (manual, *Serialization rules*). **La trampa:** un valor que no se serializa no es editable y tampoco se guarda. Si el diseño necesita un diccionario, el asset guarda una lista y el código arma el diccionario al leerla.

**Prefab.** Es una plantilla: un objeto con sus componentes, sus valores y sus hijos, guardado como asset. Admite prefabs anidados, variantes (versiones predefinidas sobre una base común) y *overrides* por instancia. Si se edita el prefab, cambian todas sus instancias (manual, *Prefabs*). **La trampa:** un override hecho por código que no se registra como tal se pierde o se aplica al asset equivocado (ver *Herramientas de editor*).

**ScriptableObject.** Es un contenedor de datos que vive como asset y no como componente. Todas las instancias que lo referencian comparten una sola copia en memoria. En el editor, lo que un script le escribe queda en memoria y solo persiste entre sesiones si se lo marca sucio; en una build solo se puede leer (manual, *ScriptableObject*). **La trampa:** ese mismo comportamiento del editor hace que, al jugar, el juego pueda cambiar el asset que diseñó otro (relación R3).

Y un quinto elemento, que ordena los otros cuatro: **varias escenas abiertas a la vez**. El editor y el juego pueden tener cargadas varias escenas juntas (manual, *Multi-scene editing*). Una escena de arranque aporta la cámara, la interfaz y los servicios; la escena del nivel aporta solo su contenido y se carga de forma aditiva. Así hay una sola cámara y un solo HUD, y los niveles no los copian.

---

## Las cinco relaciones

### R1 · Un valor, un lugar

Un valor de diseño tiene **exactamente un** lugar donde se edita. Si vive en dos lugares (un ScriptableObject y un JSON, un prefab y una constante), tarde o temprano difieren, y el síntoma es que dos herramientas dicen cosas distintas sobre el mismo juego.

Si una herramienta externa necesita el dato (un simulador, un bot, la integración continua), **el editor sigue siendo la fuente** y la herramienta lee una **exportación** que el editor genera. Una prueba falla si esa exportación quedó vieja. El razonamiento opuesto —*"la herramienta no lee `.asset`, entonces el dato va en JSON"*— resuelve la necesidad de la herramienta a costa de la del diseñador. Es el caso de ClashDefense, `SOL-001` D3; `SOL-003` D5 lo corrigió convirtiendo el JSON en exportación.

### R2 · Lo que se edita se ve donde se edita

Cada tipo de contenido se edita en el lugar que muestra su forma:

```txt
espacial (caminos, áreas, radios, spawns)   → objetos en la escena, con gizmos y manijas
dato sin lugar (balance, oleadas)            → ScriptableObject con inspector que valida
visual repetido                              → prefab, con referencias a sus partes animadas
```

Un camino guardado como una lista de coordenadas en un texto no está disponible para diseñar: para moverlo hay que calcular. La prueba es simple. Si para cambiar algo hay que imaginarlo en vez de verlo, está en el lugar equivocado.

### R3 · Lo que el juego escribe no es lo que el diseñador escribió

Los ScriptableObjects son compartidos, y en el editor lo que el juego les escribe queda en memoria después de salir de Play. Puede incluso guardarse si algo marca el asset como sucio. Por eso **la partida trabaja sobre copias**: una copia de los datos al empezar, o instancias de los prefabs, nunca el asset mismo. El síntoma de violar R3 es característico: *"el balance cambió después de jugar"*. En una build el defecto no aparece, porque ahí el asset es de solo lectura. Por eso se escapa de las pruebas hechas sobre la build.

### R4 · Dependencias entre objetos: en `Start`, no en `Awake`

Unity no garantiza en qué orden llama al mismo evento (`Awake`, por ejemplo) en objetos distintos, salvo donde está documentado o configurado; para instancias del mismo script no se puede fijar ese orden (manual, *Event function execution order*). La regla que sale de ahí, y que el Core ya tiene como criterio (`Managers y Unity`):

```txt
Awake      estado propio. Nada que dependa de otro objeto.
OnEnable   suscripciones.
Start      referencias a otros objetos, composición, primer uso de servicios.
```

*Script Execution Order* es la excepción explícita, y funciona como parche: ordena scripts, no instancias.

**Por qué este defecto es caro:** el orden depende del archivo de la escena. El mismo código anda en una escena y falla en otra, y puede empezar a fallar cuando una herramienta **regenera** una escena que andaba. Evidencia: ClashDefense `BUG-042`. El Prototipo 0 pasaba y la campaña arrancaba con una excepción que deshabilitaba el componente raíz.

### R5 · El canal de ejecución decide cómo se genera el contenido, no dónde vive

Cuando el contenido lo produce un ejecutor automático o remoto (una IA, una bandeja de órdenes, un MCP), aparece la tentación de construirlo por código en tiempo de ejecución, porque crear assets a distancia es trabajoso. La división correcta es otra. Un **script de editor genera los assets una vez** (escenas, prefabs, ScriptableObjects) y los guarda. A partir de ahí son del diseñador.

```txt
el canal decide    CÓMO se crea la primera versión (a mano, por MCP, por un generador)
el diseño decide   DÓNDE vive (escena, prefab, ScriptableObject)
```

Evidencia: ClashDefense `SOL-001` D5 generó la escena por código por el riesgo de *"ejecución a distancia"*, y D6 armó la interfaz en código porque sus prefabs *"no se pueden generar por la bandeja sin decenas de órdenes"*. Las dos decisiones eran razonables desde el canal y equivocadas desde el proyecto. Dos entregas después hubo que migrarlo todo.

---

## El diagrama, con sus invariantes

```txt
EDITOR — autoría                                        PLAY / BUILD — lectura

escena del nivel ──guardar / entrar a Play──▶ dato horneado ──copia──▶ partida
 (puntos, áreas, rocas, con gizmos)              (SO del nivel)               │
ScriptableObjects de balance y oleadas ──────────────────────copia──▶ partida
prefabs ──────────────────────────────────────instancia (o reserva)──▶ mundo
todos los datos ──exportar al guardar──▶ JSON ──▶ herramienta externa (simulador, CI)

dibujo generado desde las piezas (terreno, trazo del camino) ── se rehace, no se guarda
```

```txt
I1  cada valor de diseño tiene un solo lugar editable                          (R1)
I2  la partida nunca escribe un asset                                          (R3)
I3  lo generado desde las piezas no se guarda ni se selecciona: se rehace;
    se tocan las piezas, nunca su dibujo
I4  la exportación se regenera al guardar, y una prueba falla si quedó vieja    (R1)
I5  lo que define la escena (la forma del nivel) pasa al dato al guardar y al
    entrar a Play: el núcleo, las pruebas y el simulador leen datos, no escenas
```

I5 es lo que permite que las dos mitades convivan. El diseñador trabaja en la escena, y la simulación determinista (`01_Bucle_de_simulacion`) sigue leyendo datos sin depender del motor. El horneado es el puente entre las dos y corre en un solo sentido: de la escena al dato.

---

## Herramientas de editor — lo mínimo que hace editable una escena

Cinco piezas, y cada una responde por algo distinto:

```txt
Gizmos        dibujan lo que no se renderiza: caminos con su sentido, carriles, radios,
              entradas. Sin gizmos, un nivel hecho de objetos vacíos no se ve.
Manijas       mover con el mouse, en la vista de escena, un punto, un radio o el tamaño
              de un área.
Inspector     muestra el error donde se edita y antes de dar Play: un camino que no
que valida    llega a la base, una oleada que manda enemigos a un carril que no existe.
OnValidate    reacciona a un cambio del Inspector; no crea ni destruye objetos.
Validación    antes de construir la build, los datos se validan y un nivel roto frena
previa        la build con su motivo.
```

**Deshacer no es opcional.** Toda herramienta que escribe sobre un objeto llama a `Undo.RecordObject` antes de escribir. Si el objeto es una instancia de prefab, además registra el cambio como override de la instancia (Scripting API, *Undo.RecordObject*). Una herramienta que escribe sin Undo convierte Ctrl+Z en una mentira. El diseñador que la usa una vez y pierde un cambio deja de confiar en editar.

---

## Generadores y migraciones — herramientas de una sola vez

Un script que crea assets desde código es un **generador**. Sirve para producir la primera versión de un contenido o para migrar un proyecto de una forma a otra. Tiene dos mecanismos que muerden:

**1. Abrir una escena en modo Single descarga los assets que solo referencia el código.** Un generador que guarda referencias a assets en variables y crea escenas nuevas en modo Single se queda con referencias muertas. Hay que volver a cargarlos por ruta después de cada escena nueva. El manual de `EditorSceneManager.NewScene` no documenta esa descarga. Esto sale de evidencia interna medida: ClashDefense `BUG-041`, la migración falló al armar su primera escena de nivel.

**2. Una segunda corrida pisa lo editado a mano.** Un generador regenera lo que genera. Una vez que la migración se verificó, **se retira del proyecto**, o queda marcado como destructivo y fuera del menú de uso diario. Un generador vivo en el menú es una trampa con fecha: alguien lo va a correr para *"arreglar"* algo y va a borrar una semana de trabajo del diseñador. Evidencia: ClashDefense cerró `TL-003` con 1.579 líneas de migración de una sola vez todavía en el proyecto y una advertencia en la guía del owner, en vez de retirarlas.

**Y la verificación que corresponde.** Una migración promete no cambiar el juego, así que se prueba por **equivalencia**: se exporta desde lo nuevo y se compara por contenido contra lo viejo. En `TL-003` fueron 10 de 10 archivos iguales. Así, *"no cambió nada"* pasa de afirmación a medición. El criterio de por qué un número así vale más que una confianza está en `Gates verificables`.

---

## Los seis modos de fallar

| # | Falla | Síntoma | Qué se violó |
|---|---|---|---|
| 1 | **Contenido por código en runtime** | el owner no ve su nivel; cada cambio vuelve a ser un pedido | R2, R5 |
| 2 | **Dos fuentes para un valor** | el simulador y el juego dicen cosas distintas del mismo nivel | R1 |
| 3 | **La partida escribe el asset** | el balance cambia después de jugar en el editor, y en la build no pasa | R3 |
| 4 | **Dependencia en `Awake`** | anda en una escena y falla en otra con el mismo código; se rompe al regenerar la escena | R4 |
| 5 | **Archivos movidos sin su `.meta`** | referencias vacías, scripts que aparecen como faltantes | identidad |
| 6 | **Generador vivo** | la segunda corrida borra lo que el diseñador editó | generadores |

El modo 1 es el caro y el que se ve menos, porque **el juego funciona**. Ninguna prueba de gameplay lo detecta, porque lo que falla es la forma de trabajo y no el comportamiento. Se detecta con una sola pregunta hecha antes del `SOL`: *¿dónde va a tocar el owner para cambiar esto?*

---

## Proyecto que ya existe — dos lecturas

Al entrar a un proyecto que ya tiene código se leen **dos cosas**, y rechazar la primera no implica rechazar la segunda:

```txt
QUÉ HACE        reglas y comportamiento   → se contrastan contra el diseño; lo que choca se reemplaza
CÓMO SE TRABAJA dónde viven los valores, cómo se crea una entidad, cómo se arma un nivel y
                una pantalla              → se reutiliza o se extiende, salvo razón declarada
```

El Core ya lo dice para los datos (`Type Object`): si el proyecto usa ScriptableObjects o datos editables para sus variantes, se extiende ese sistema antes de crear otro. Este libro agrega la otra mitad. La forma de trabajo del proyecto también es un sistema existente.

Evidencia: el proyecto previo del owner de ClashDefense tenía datos de torre y enemigo como ScriptableObjects que apuntaban a su prefab, fábricas con catálogo en el Inspector, reserva de proyectiles, el camino como puntos hijos en la escena y las oleadas en el Inspector. `TL-001` rechazó sus reglas por nueve choques documentados con el diseño, y con razón. Pero junto con las reglas rechazó sus convenciones: pasó a JSON y a contenido armado por código. `TL-003` volvió a las mismas convenciones, reconstruidas desde cero y con otros nombres. El error no fue reemplazar: fue no escribir, convención por convención, si se reutilizaba, se extendía o se reemplazaba, y por qué.

---

## Baseline

| Pieza | Arranque | De dónde sale |
|---|---|---|
| Nivel | una escena por nivel con sus piezas (puntos, áreas, spawns) y gizmos, cargada de forma aditiva sobre una escena de arranque | R2; ClashDefense `SOL-003` D1 y D12 |
| Datos de diseño | ScriptableObjects con un inspector que valida; la partida usa copias | R1, R3 |
| Visual repetido | prefab con referencias a sus partes animadas | R2. El costo (materiales compartidos, reserva) es del Core: `Memory Leak`, `Draw calls y batching`, `Object pool como optimizacion` |
| Herramienta externa | lee una exportación que genera el editor, con prueba de frescura | R1, I4 |
| Arranque | composición en `Start`; el primer chequeo de cualquier piloto es que el juego arrancó | R4 |
| Generadores | se retiran al verificar la equivalencia | *Generadores y migraciones* |
| Build | validación previa de datos | *Herramientas de editor* |

Ninguna fila es obligatoria por sí misma. Cada una sale de una relación, y la relación es lo que se defiende en el `SOL`. Si un proyecto decide no seguir una fila (un prototipo de una sesión que nadie más va a editar, por ejemplo), lo declara como desviación con su motivo.

---

## Aplicación

Cuándo la IA trae este libro por defecto:

```txt
al escribir el SOL de cualquier proyecto Unity con contenido: niveles, entidades, interfaz
al entrar a un proyecto que ya tiene código (las dos lecturas)
cuando el canal de ejecución es remoto o automatizado (R5)
antes de escribir un generador, una migración o una herramienta de editor
cuando un defecto aparece en una escena y no en otra con el mismo código (R4)
cuando el simulador o una herramienta externa necesita los datos del juego (R1)
```

## Límites

```txt
NO es dueño del costo: materiales, batching, reservas, basura por cuadro, canvas
     → Core: `Memory Leak`, `Draw calls y batching`, `Instantiate y destroy constantes`,
       `Object pool como optimizacion`, `Separar canvas por frecuencia de cambio`
NO es dueño de la arquitectura de gameplay
     → `Separar logica de unity`, `Monobehaviour como puente`, `Clases puras`
NO cubre el guardado de partida (persistencia del jugador): territorio pendiente del estante
NO cubre Addressables ni la carga de contenido pesado → decidir con `Cuando NO optimizar`
NO cubre los ScriptableObjects como arquitectura (eventos, variables compartidas): es una
     elección de arquitectura y se decide contra un requerimiento, no es parte de la autoría.
     Documentado en `38_Create_modular_game_architecture_with_ScriptableObje`
NO fija el motor: las relaciones R1–R5 valen en otros motores y cambia el mecanismo
     (escenas y recursos en Godot, assets y Blueprints en Unreal). Versión consultada: Unity 6.
```

## Fuentes

- Unity Technologies. *Manual* de Unity 6 (6000.3), páginas consultadas el 2026-09-28:
  - *ScriptableObject* — https://docs.unity3d.com/6000.3/Documentation/Manual/class-ScriptableObject.html. Copia única compartida, persistencia en el editor y solo lectura en la build (R3).
  - *Event function execution order* — https://docs.unity3d.com/6000.3/Documentation/Manual/execution-order.html. Orden no garantizado entre objetos (R4).
  - *Asset metadata* — https://docs.unity3d.com/6000.3/Documentation/Manual/AssetMetadata.html. Identidad en el `.meta` (identidad, modo 5).
  - *Prefabs* — https://docs.unity3d.com/6000.3/Documentation/Manual/Prefabs.html. Anidados, variantes, overrides.
  - *Multi-scene editing* — https://docs.unity3d.com/6000.3/Documentation/Manual/MultiSceneEditing.html. Varias escenas a la vez, en el editor y en el juego.
  - *Serialization rules* — https://docs.unity3d.com/6000.3/Documentation/Manual/script-serialization-rules.html. Qué se serializa y qué no.
- Unity Technologies. *Scripting API*: `Undo.RecordObject` — https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Undo.RecordObject.html. Deshacer en herramientas, y overrides de instancias de prefab.
- `39_Unity_Best_practice_guides_manual_oficial` y `38_Create_modular_game_architecture_with_ScriptableObje`, en Documentación real. El índice oficial de buenas prácticas y los ScriptableObjects como arquitectura. Ya estaban catalogados; esta misión destila la parte de autoría.

**Evidencia interna** (no es fuente externa: es el caso que disparó la misión). Proyecto ClashDefense: `SOL-001` (D3, D5 y D6), `SOL-003` (D1–D17), `BUG-041`, `BUG-042`, `QA-003` y el proyecto previo del owner en el mismo repositorio. Las relaciones de este libro son las que esas decisiones dejaron implícitas, o dejaron escritas del lado equivocado.

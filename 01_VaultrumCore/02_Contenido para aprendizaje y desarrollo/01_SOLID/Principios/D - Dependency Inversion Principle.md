## Definicion

El principio de inversion de dependencias establece que los sistemas de alto nivel no deberian depender directamente de detalles de bajo nivel cuando eso vuelve fragil la arquitectura.

Tambien puede entenderse como:

```txt
La logica importante debe depender de contratos estables, no de implementaciones concretas cambiantes.
```

Este principio no significa que todo deba usar interfaces.

Significa que las dependencias importantes deben pensarse con criterio.

---

## Idea central

Cuando una clase importante depende directamente de demasiados detalles concretos, cualquier cambio externo puede romperla.

```txt
Dependencia rigida
→ cambios mas costosos
→ menor flexibilidad
→ mas acoplamiento
→ mas riesgo
```

El objetivo de este principio es proteger la logica central de detalles que pueden cambiar.

---

## Que problema resuelve

Este principio ayuda a evitar sistemas demasiado acoplados.

Problemas comunes:

- la logica principal depende directamente de clases concretas,
- cambiar una implementacion rompe sistemas importantes,
- no se pueden reemplazar servicios, datos o comportamientos,
- es dificil testear porque todo esta atado,
- una clase crea internamente sus propias dependencias,
- los sistemas centrales conocen demasiados detalles.

---

## Como aplicarlo con criterio

Antes de invertir una dependencia, hay que entender si esa dependencia realmente necesita flexibilidad.

Preguntas utiles:

```txt
¿Esta clase depende de un detalle que puede cambiar?
¿La dependencia concreta vuelve fragil el sistema?
¿Necesito poder reemplazar esta implementacion?
¿Hay varias implementaciones posibles?
¿Esto afecta testeo, extension o mantenimiento?
¿Una abstraccion mejora claridad o agrega complejidad?
```

No se invierten dependencias por costumbre.

Se hace cuando reduce acoplamiento real.

---

## Ejemplo general en videojuegos

Ejemplo problematico:

```txt
QuestSystem
→ depende directamente de EmailNotification
```

Si despues se quiere mostrar notificacion en UI, sonido, popup o log interno, el sistema de quests queda atado a una implementacion concreta.

Una alternativa mas flexible:

```txt
QuestSystem
→ depende de un contrato de notificacion

NotificationUI
NotificationSound
NotificationLog
→ implementan distintas formas de notificar
```

El sistema importante no necesita saber como se muestra la notificacion.

Solo necesita emitir o solicitar una notificacion.

---

## Ejemplo aplicado a Unity

Ejemplo problematico:

```txt
TowerUpgradeComponent
→ busca directamente UpgradePanel
→ modifica textos
→ activa botones
→ decide feedback visual
```

El sistema de upgrades queda atado a una UI concreta.

Una version mas sana podria ser:

```txt
TowerUpgradeComponent
→ aplica reglas de upgrade
→ expone resultado

UpgradePanel
→ muestra datos
→ solicita upgrade
→ representa resultado visual
```

O se puede usar el mecanismo existente del proyecto para comunicar cambios.

Lo importante es que la logica del upgrade no dependa directamente de detalles visuales de la UI.

---

## Como debe usarlo una IA

Cuando una IA proponga una solucion, debe revisar dependencias importantes.

Debe preguntarse:

```txt
¿La logica central esta dependiendo de detalles concretos?
¿Esta clase deberia conocer esta implementacion?
¿Existe un contrato o mecanismo ya usado en el proyecto?
¿Conviene desacoplar o una referencia directa alcanza?
¿Estoy creando una abstraccion necesaria o decorativa?
¿El cambio mejora mantenimiento o solo agrega capas?
```

La IA no debe introducir interfaces, servicios o localizadores sin justificar.

Primero debe explicar:

```txt
Dependencia detectada
Riesgo actual
Motivo para desacoplar
Alternativa simple
Solucion propuesta
Impacto
Validacion necesaria
```

---

## Senales de que se esta rompiendo DIP

Un sistema probablemente rompe este principio si:

- una clase central instancia directamente muchas dependencias,
- cambiar UI rompe logica de gameplay,
- cambiar una fuente de datos rompe sistemas no relacionados,
- no se puede reemplazar una implementacion concreta,
- el codigo es dificil de probar por dependencias rigidas,
- una clase importante conoce detalles que no deberia,
- hay referencias cruzadas fuertes entre sistemas,
- el flujo funciona solo si todo esta conectado de una forma especifica.

---

## Cuando NO aplicarlo de forma agresiva

No conviene invertir una dependencia si:

- la dependencia es estable,
- no hay variantes,
- no se necesita reemplazo,
- no mejora testeo ni mantenimiento,
- el sistema es muy pequeño,
- una referencia directa es mas clara,
- la abstraccion agregaria complejidad sin beneficio.

DIP no significa esconder todo detras de interfaces.

Significa proteger la logica importante cuando las dependencias concretas generan fragilidad.

---

## Error comun

Un error comun es pensar:

```txt
Para aplicar Dependency Inversion, todo debe depender de interfaces.
```

Eso puede producir arquitectura innecesaria.

Ejemplo de exceso:

```txt
IPlayer
IPlayerMovement
IPlayerHealth
IPlayerAudio
IPlayerUI
IPlayerData
```

Si no hay necesidad real de reemplazar esas implementaciones, puede ser ruido.

El criterio correcto es:

```txt
Abstraer dependencias cuando el acoplamiento genera riesgo real.
Mantener simple cuando la dependencia directa es suficiente.
```

---

## Relacion con Vaultrum

Dentro de Vaultrum, este principio debe usarse para revisar dependencias entre sistemas importantes.

Especialmente cuando se trabaja con:

- UI y logica,
- managers,
- sistemas de gameplay,
- datos configurables,
- servicios,
- eventos,
- input,
- guardado,
- notificaciones,
- codigo generado por IA,
- integraciones entre sistemas.

No se usa para ocultar todo detras de contratos.

Se usa para evitar que detalles cambiantes rompan la logica central.

---

## Resultado esperado

Aplicar bien este principio deberia permitir:

- menor acoplamiento,
- sistemas mas flexibles,
- logica central mas protegida,
- mejor testeo,
- reemplazo mas simple de implementaciones,
- menor impacto ante cambios,
- integraciones mas limpias,
- codigo mas mantenible.

---

## Regla final

```txt
La logica importante no deberia depender de detalles que cambian todo el tiempo.
```
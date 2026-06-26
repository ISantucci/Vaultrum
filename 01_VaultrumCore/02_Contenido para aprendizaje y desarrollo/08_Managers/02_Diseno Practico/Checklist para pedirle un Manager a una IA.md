## Propósito dentro de Vaultrum

Este documento sirve como plantilla para pedirle a una IA que analice, diseñe o implemente un manager.

El objetivo es evitar pedidos vagos como:

```txt
Creame un manager para esto.
```

Ese tipo de pedido suele producir:

```txt
clases dios,
singletons innecesarios,
APIs enormes,
responsabilidades mezcladas,
dependencias ocultas,
y cambios demasiado grandes.
```

La idea principal es:

```txt
Antes de pedir código,
pedir criterio.
```

---

## Regla base para trabajar con IA

Una IA no debería crear un manager automáticamente.

Primero debe analizar.

Debe justificar:

```txt
qué problema detecta,
por qué corresponde un manager,
qué alternativas descarta,
qué responsabilidad tendrá,
qué responsabilidades no tendrá,
qué API mínima propone,
qué ciclo de vida necesita,
qué riesgos introduce,
y cómo se validará.
```

Si no puede justificar eso, no debería implementar todavía.

---

## Prompt base

```txt
Quiero que analices si hace falta crear o modificar un Manager para este sistema.

No escribas código todavía.

Primero analizá:

1. Qué problema arquitectónico detectás.
2. Qué responsabilidad está dispersa, duplicada o mal ubicada.
3. Si realmente corresponde un Manager.
4. Qué alternativas evaluás:
   - clase común,
   - Factory,
   - Facade,
   - Object Pool,
   - Event Queue,
   - Observer,
   - State Machine,
   - Service Locator,
   - clase pura,
   - sistema específico.
5. Qué responsabilidad central tendría el Manager.
6. Qué responsabilidades tendría prohibidas.
7. Qué API mínima proponés.
8. Qué ciclo de vida tendría.
9. Si debería ser MonoBehaviour o clase pura.
10. Si debería persistir entre escenas.
11. Cómo se comunicaría con otros sistemas.
12. Qué riesgos SOLID aparecen.
13. Qué riesgos de Unity aparecen.
14. Qué archivos tocarías.
15. Qué archivos no tocarías.
16. Qué validaciones harías después.

No crees un Manager por costumbre.
No uses singleton salvo que lo justifiques.
No metas lógica de UI, audio, assets, gameplay o guardado en el mismo manager.
Priorizá cambios incrementales.
```

---

## Prompt para auditar managers existentes

```txt
Analizá los managers existentes del proyecto.

No modifiques código.

Quiero un informe con:

1. Lista de managers detectados.
2. Responsabilidad aparente de cada uno.
3. Responsabilidad real según sus métodos y dependencias.
4. Señales de Manager Dios.
5. Señales de singleton innecesario.
6. Señales de referencias viejas o problemas entre escenas.
7. Señales de APIs demasiado grandes.
8. Señales de violación de SOLID.
9. Managers que parecen Facade, Factory, Pool, State Machine o Service.
10. Managers que conviene mantener.
11. Managers que conviene dividir.
12. Managers que conviene renombrar.
13. Managers que conviene eliminar.
14. Refactors incrementales sugeridos.
15. Riesgos de cada cambio.
16. Orden recomendado de trabajo.

No propongas reescritura total.
No agregues managers nuevos sin justificar.
```

---

## Prompt para diseñar un manager nuevo

```txt
Necesito diseñar un Manager para resolver este problema:

[describir problema]

Antes de escribir código, proponé el diseño.

Usá esta estructura:

# Manager propuesto

## Problema que resuelve
## Por qué corresponde un Manager
## Alternativas descartadas
## Responsabilidad central
## Responsabilidades permitidas
## Responsabilidades prohibidas
## API mínima propuesta
## Ciclo de vida
## Relación con Unity
## Relación con eventos
## Persistencia entre escenas
## Riesgos SOLID
## Riesgos de sobrearquitectura
## Plan incremental
## Archivos que tocarías
## Archivos que NO tocarías
## Validación posterior

Después de eso, esperá mi aprobación antes de escribir código.
```

---

## Prompt para implementar después del diseño

```txt
Ahora implementá el Manager aprobado respetando el diseño anterior.

Condiciones:

1. No agregues responsabilidades nuevas.
2. No conviertas el manager en clase dios.
3. No uses singleton salvo que ya haya sido aprobado.
4. No llames manualmente Awake, Start ni Update.
5. Usá métodos explícitos como Initialize, ResetState, EnterLevel, ExitLevel, Register o Unregister si corresponde.
6. Mantené la API mínima.
7. No modifiques UI, audio, assets, guardado o gameplay si no estaba aprobado.
8. Indicá exactamente qué archivos modificaste.
9. Indicá qué métodos agregaste.
10. Indicá cómo validar en Unity.
11. Indicá riesgos o supuestos.

Si necesitás tocar archivos no aprobados, frená y pedí confirmación.
```

---

## Prompt para evitar sobrearquitectura

```txt
Antes de crear este Manager, quiero que intentes demostrar que NO hace falta.

Analizá si el problema podría resolverse mejor con:

- una clase pura,
- una Factory,
- una Facade,
- un Object Pool,
- un Event Queue,
- Observer,
- una State Machine,
- una referencia explícita,
- un ScriptableObject,
- o una pequeña refactorización.

Solo proponé el Manager si esas alternativas no son suficientes.

Respondé con:

1. Alternativas posibles.
2. Por qué cada una alcanza o no alcanza.
3. Costo de crear el Manager.
4. Riesgo de no crearlo.
5. Riesgo de crearlo.
6. Decisión final.
```

---

## Prompt para revisar un manager antes de agregar una feature

```txt
Antes de agregar esta feature al Manager existente, analizá si corresponde.

Feature:
[describir feature]

Manager actual:
[pegar clase o describir manager]

Quiero que respondas:

1. Si la feature pertenece a la responsabilidad central del manager.
2. Si agregarla violaría responsabilidad única.
3. Si corresponde crear otro sistema.
4. Si corresponde usar eventos.
5. Si corresponde usar Factory, Pool, State Machine o Facade.
6. Qué método mínimo haría falta.
7. Qué responsabilidades quedarían prohibidas.
8. Qué riesgo hay de clase dios.
9. Recomendación final.

No escribas código hasta que apruebe la decisión.
```

---

## Prompt para revisar ciclo de vida

```txt
Analizá el ciclo de vida de este Manager.

Quiero saber:

1. Cuándo se crea.
2. Cuándo se inicializa.
3. Quién lo inicializa.
4. Si usa Awake, Start o Update correctamente.
5. Si alguien llama manualmente callbacks de Unity.
6. Si persiste entre escenas.
7. Si conserva referencias de escena.
8. Si limpia referencias al cambiar de escena.
9. Si se desuscribe de eventos.
10. Si tiene ResetState, Initialize, Shutdown, Bind o Unbind cuando corresponde.
11. Qué bugs pueden aparecer al recargar escena.
12. Qué cambios mínimos recomendás.

No modifiques código todavía.
```

---

## Prompt para revisar SOLID en un manager

```txt
Auditá este Manager usando SOLID.

Quiero un análisis concreto, no genérico.

Respondé:

1. Responsabilidad central declarada.
2. Responsabilidad real según el código.
3. Razones para cambiar.
4. Posibles violaciones de SRP.
5. Posibles violaciones de OCP.
6. Posibles problemas de LSP si usa abstracciones.
7. Posibles violaciones de ISP.
8. Posibles violaciones de DIP.
9. Métodos que parecen no pertenecer.
10. Dependencias riesgosas.
11. Refactor incremental recomendado.
12. Qué NO tocarías todavía.

No propongas una reescritura total.
```

---

## Checklist antes de enviar un prompt a IA

Antes de pedirle algo a una IA:

```txt
¿Le expliqué el problema real?
¿Le dije que no escriba código todavía?
¿Le pedí alternativas al manager?
¿Le pedí responsabilidades permitidas?
¿Le pedí responsabilidades prohibidas?
¿Le pedí API mínima?
¿Le pedí ciclo de vida?
¿Le pedí riesgos SOLID?
¿Le pedí riesgos de Unity?
¿Le pedí archivos a tocar?
¿Le pedí archivos que no debe tocar?
¿Le pedí validación posterior?
¿Le aclaré si puede o no usar singleton?
¿Le aclaré si puede o no modificar escenas/prefabs?
```

---

## Checklist para evaluar la respuesta de la IA

Una buena respuesta debería incluir:

```txt
problema claro,
responsabilidad clara,
alternativas evaluadas,
manager justificado o rechazado,
API mínima,
límites,
ciclo de vida,
riesgos,
plan incremental,
validación,
archivos afectados.
```

Una respuesta débil suele decir:

```txt
creé un manager para centralizar,
hice singleton para acceso fácil,
agregué métodos útiles,
modifiqué varios sistemas,
actualicé UI desde el manager,
dejé todo listo.
```

Eso requiere revisión antes de aceptar.

---

## Regla final

Para pedir managers a una IA, no hay que pedir primero implementación.

Hay que pedir decisión arquitectónica.

```txt
Primero:
analizar.

Después:
diseñar.

Después:
aprobar.

Recién después:
implementar.
```

Un buen prompt no solo dice qué crear.

También dice qué no crear, qué no tocar y cómo validar.
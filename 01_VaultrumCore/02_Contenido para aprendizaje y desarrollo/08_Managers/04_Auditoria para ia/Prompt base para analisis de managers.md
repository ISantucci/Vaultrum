## Objetivo

Este documento contiene prompts reutilizables para pedirle a una IA que analice, audite, proponga o refactorice managers en un proyecto de videojuegos.

La intención es evitar pedidos vagos y forzar una respuesta arquitectónica antes de tocar código.

Regla base:

```txt
Primero análisis.
Después diseño.
Después aprobación.
Recién después implementación.
```

---

## Prompt base de auditoría general

```txt
Quiero que audites los managers de este proyecto.

No modifiques código todavía.

Analizá el proyecto y devolveme un informe con esta estructura:

# Auditoría de Managers

## Managers detectados

Listá todas las clases que funcionen como managers, aunque no se llamen Manager.

Incluí:
- clases con nombre Manager,
- singletons,
- clases persistentes entre escenas,
- clases con muchas referencias,
- coordinadores globales,
- clases que todos los sistemas llaman.

## Resumen general

Explicá el estado general de la arquitectura de managers.

## Análisis por manager

Para cada manager, indicá:

### Nombre
### Responsabilidad aparente
### Responsabilidad real
### Estado
Usá una de estas categorías:
- Sano
- Aceptable con deuda
- Riesgoso
- Clase dios
- Innecesario
- Mal nombrado

### Señales positivas
### Señales de riesgo
### Responsabilidades mezcladas
### API pública
### Ciclo de vida
### Persistencia entre escenas
### Uso de eventos
### Riesgos SOLID
### Riesgos propios de Unity
### Recomendación
### Refactor incremental sugerido
### Archivos que revisarías
### Archivos que NO tocarías todavía

No propongas reescritura total.
No crees managers nuevos sin justificar.
No escribas código todavía.
```

---

## Prompt para detectar managers innecesarios

```txt
Quiero que detectes managers innecesarios o sobredimensionados.

No modifiques código.

Buscá managers que:
- no tengan responsabilidad clara,
- solo envuelvan una lista,
- solo llamen a otra clase,
- solo existan para ser singleton,
- solo eviten pasar referencias,
- deberían ser Factory,
- deberían ser Facade,
- deberían ser Object Pool,
- deberían ser Observer o Event Queue,
- deberían ser State Machine,
- deberían ser clase pura,
- fueron creados por anticipación sin problema real.

Para cada caso, devolvé:

## Manager analizado
## Responsabilidad declarada
## Responsabilidad real
## Por qué podría ser innecesario
## Alternativa recomendada
## Riesgo de eliminarlo
## Riesgo de mantenerlo
## Decisión recomendada
Mantener / reducir / renombrar / reemplazar / eliminar

No elimines nada.
No escribas código.
```

---

## Prompt para detectar clase dios

```txt
Quiero que analices si esta clase funciona como clase dios.

No modifiques código.

Revisá:
- cantidad de responsabilidades,
- razones para cambiar,
- dependencias,
- métodos públicos,
- referencias serializadas,
- uso de singleton,
- uso de Update,
- lógica de UI,
- lógica de audio,
- lógica de guardado,
- lógica de assets,
- lógica de spawn,
- lógica de gameplay,
- lógica de escenas,
- eventos emitidos y escuchados.

Devolveme:

# Análisis de clase dios

## Clase analizada
## Responsabilidad declarada
## Responsabilidad real
## Métodos agrupados por responsabilidad
## Campos agrupados por responsabilidad
## Dependencias detectadas
## Señales de clase dios
## Riesgos principales
## Responsabilidades candidatas a extraer
## Qué piezas deberían recibir esas responsabilidades
## Orden recomendado de refactor
## Primer refactor sugerido
## Qué NO tocaría todavía
## Validación posterior

No propongas reescritura total.
No escribas código todavía.
```

---

## Prompt para refactor incremental de clase dios

```txt
Quiero refactorizar esta clase dios de forma incremental.

No hagas una reescritura total.

Primero elegí UNA responsabilidad para extraer.

Criterios:
- bajo riesgo,
- alto beneficio,
- API mínima,
- comportamiento preservado,
- cambios fáciles de validar.

Devolvé:

# Refactor incremental propuesto

## Responsabilidad elegida
## Por qué conviene empezar por esta
## Métodos que se moverían
## Campos que se moverían
## Nuevo sistema o manager destino
## API mínima del nuevo sistema
## Cambios necesarios en la clase original
## Wrappers temporales si hacen falta
## Archivos a tocar
## Archivos que NO tocarías
## Riesgos
## Validación en Unity

Esperá mi aprobación antes de escribir código.
```

---

## Prompt para proponer un manager nuevo

```txt
Necesito analizar si conviene crear un nuevo Manager para este problema:

[describir problema]

No escribas código todavía.

Primero intentá demostrar que NO hace falta un manager.

Evaluá estas alternativas:
- clase pura,
- Factory,
- Facade,
- Object Pool,
- Observer,
- Event Queue,
- State Machine,
- ScriptableObject,
- referencia explícita,
- Registry,
- Repository,
- sistema específico.

Luego devolvé:

# Propuesta de Manager

## Problema detectado
## Alternativas evaluadas
## Por qué alcanzan o no alcanzan
## Decisión
Crear manager / no crear manager / usar otra pieza

Si proponés manager, agregá:

## Responsabilidad central
## Responsabilidades permitidas
## Responsabilidades prohibidas
## API mínima inicial
## Ciclo de vida
## Integración con Unity
MonoBehaviour / clase pura / ScriptableObject / servicio / escena / persistente

## Comunicación con otros sistemas
eventos / llamadas directas / facade / event queue / registro

## Persistencia entre escenas
## Riesgos SOLID
## Riesgos de sobrearquitectura
## Plan incremental
## Validación posterior

No uses singleton salvo que lo justifiques.
No crees una clase dios.
No escribas código hasta que apruebe.
```

---

## Prompt para revisar si una feature pertenece a un manager

```txt
Antes de agregar esta feature al manager existente, quiero que analices si corresponde.

Feature:
[describir feature]

Manager actual:
[pegar clase o describir manager]

No escribas código.

Respondé:

## Responsabilidad central del manager
## Responsabilidad de la feature
## ¿La feature pertenece al manager?
Sí / No / Parcialmente

## Riesgo de agregarla
## Principios SOLID afectados
## Alternativas
- otro manager,
- sistema específico,
- clase pura,
- evento,
- facade,
- factory,
- pool,
- state machine.

## Recomendación final
## API mínima si corresponde
## Qué NO debería agregarse
## Validación posterior

Si no pertenece, explicá dónde debería ir.
```

---

## Prompt para revisar ciclo de vida de un manager

```txt
Quiero que revises el ciclo de vida de este manager.

No modifiques código.

Analizá:

1. Cuándo se crea.
2. Cuándo se inicializa.
3. Quién lo inicializa.
4. Si puede usarse antes de estar listo.
5. Si usa Awake correctamente.
6. Si usa Start correctamente.
7. Si usa Update y por qué.
8. Si alguien llama manualmente Awake, Start o Update.
9. Si tiene Initialize, ResetState, Shutdown, Bind o Unbind.
10. Si persiste entre escenas.
11. Si conserva referencias de escena.
12. Si limpia referencias al cambiar escena.
13. Si evita duplicados.
14. Si se suscribe a eventos.
15. Si se desuscribe correctamente.
16. Qué bugs pueden aparecer al recargar escena.
17. Qué cambios mínimos recomendás.

Devolvé:
- diagnóstico,
- riesgos,
- cambios incrementales,
- validación.
```

---

## Prompt para revisar SOLID en un manager

```txt
Auditá este manager usando SOLID.

No quiero una explicación genérica de SOLID.
Quiero un análisis aplicado a este código.

Respondé:

## Responsabilidad central declarada
## Responsabilidad real según código
## Razones para cambiar

## SRP
¿Tiene una sola responsabilidad?
¿Qué responsabilidades mezcla?

## OCP
¿Cada feature nueva obliga a modificar este manager?
¿Hay switches o ifs crecientes por tipo?

## LSP
Si usa abstracciones, ¿se pueden reemplazar sin casos especiales?

## ISP
¿Expone una API demasiado grande?
¿Los consumidores dependen de métodos que no usan?

## DIP
¿Depende de demasiadas clases concretas?
¿Hay dependencias ocultas o búsquedas globales?

## Riesgos principales
## Refactor incremental recomendado
## Qué NO tocaría todavía
## Validación posterior

No escribas código todavía.
```

---

## Prompt para revisar persistencia entre escenas

```txt
Quiero que revises si este manager debe ser persistente entre escenas.

No modifiques código.

Analizá:

1. Qué responsabilidad tiene.
2. Si esa responsabilidad atraviesa escenas.
3. Si usa DontDestroyOnLoad.
4. Si puede duplicarse.
5. Qué estado conserva.
6. Qué referencias de escena conserva.
7. Si limpia referencias de escena.
8. Si tiene BindSceneReferences.
9. Si tiene UnbindSceneReferences.
10. Si se desuscribe de eventos.
11. Qué pasa al volver al menú.
12. Qué pasa al reiniciar nivel.
13. Qué bugs pueden aparecer.
14. Si debería ser global, de escena, de nivel o de partida.

Devolvé:
- decisión recomendada,
- riesgos,
- cambios mínimos,
- validación en Unity.
```

---

## Prompt para revisar managers antes de pasar código a producción

```txt
Quiero una revisión final de managers antes de cerrar esta feature.

No modifiques código.

Revisá:

1. Si se crearon managers nuevos innecesarios.
2. Si algún manager creció demasiado.
3. Si alguna feature quedó en el manager incorrecto.
4. Si hay singletons nuevos sin justificar.
5. Si hay APIs públicas demasiado grandes.
6. Si hay referencias de escena en managers persistentes.
7. Si hay eventos sin desuscripción.
8. Si hay Update innecesario.
9. Si se rompió responsabilidad única.
10. Si hay oportunidades de mover lógica a clases puras.
11. Si hay managers que deberían ser Facade, Factory, Pool, Event Queue o State Machine.

Devolvé:
- hallazgos críticos,
- hallazgos menores,
- recomendaciones,
- qué dejaría como deuda aceptable,
- qué corregiría antes de seguir.
```

---

## Prompt corto para uso rápido

```txt
Analizá este manager antes de modificarlo.

No escribas código.

Decime:
1. Qué responsabilidad tiene.
2. Qué responsabilidades está mezclando.
3. Si realmente debería ser manager.
4. Si debería ser otra pieza arquitectónica.
5. Si tiene riesgo de clase dios.
6. Si su API pública es demasiado grande.
7. Si su ciclo de vida está claro.
8. Si persiste entre escenas correctamente.
9. Qué cambio mínimo recomendás.
10. Qué NO tocarías todavía.
```

---

## Checklist para evaluar respuestas de IA

Una buena respuesta de IA debería:

```txt
analizar antes de implementar,
detectar responsabilidad real,
evaluar alternativas,
evitar singletons por comodidad,
evitar clase dios,
proponer API mínima,
definir ciclo de vida,
indicar riesgos,
sugerir cambios incrementales,
explicar archivos afectados,
y pedir aprobación antes de tocar código.
```

Una respuesta débil suele decir:

```txt
creé un manager para centralizar,
lo hice singleton,
agregué métodos útiles,
modifiqué varios sistemas,
actualicé UI desde el manager,
dejé todo listo.
```

Eso debe revisarse antes de aceptar.

---

## Regla final

Un prompt bueno no pide solamente código.

Pide criterio, límites y validación.

```txt
Prompt sano
→ problema claro,
→ análisis previo,
→ alternativas,
→ límites,
→ aprobación,
→ implementación incremental.

Prompt peligroso
→ “creame un manager para esto”
→ resultado probable: clase dios.
```
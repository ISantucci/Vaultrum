## Definicion

Singleton es un patron que garantiza que exista una unica instancia accesible de una clase o sistema.

```txt
Sistema
→ una sola instancia
→ acceso compartido
```

---

## Idea central

Singleton controla existencia y acceso global a un sistema que realmente debe ser unico.

El problema es que puede ocultar dependencias si se usa sin cuidado.

---

## Que problema resuelve

Singleton ayuda cuando un sistema debe tener una unica instancia clara.

Problemas posibles:

- hay multiples instancias de un sistema que deberia ser unico,
- distintos objetos necesitan acceder a un servicio central,
- se requiere persistencia entre escenas,
- se necesita un punto unico de coordinacion.

---

## Cuando conviene usarlo

Conviene considerar Singleton cuando:

- el sistema debe ser unico,
- duplicarlo generaria errores,
- el acceso compartido esta justificado,
- la responsabilidad es clara,
- no oculta dependencias importantes.

Ejemplos posibles:

```txt
GameManager
AudioManager
SaveManager
SceneLoader
InputManager
```

Estos ejemplos no significan que siempre deban ser Singleton.

---

## Cuando NO conviene usarlo

No conviene usar Singleton si:

- se usa solo por comodidad,
- oculta dependencias,
- vuelve dificil testear,
- se convierte en acceso global para todo,
- absorbe muchas responsabilidades,
- reemplaza una referencia clara,
- genera problemas entre escenas.

---

## Como decidir si aplica

Antes de proponer Singleton, la IA debe responder:

```txt
¿Este sistema realmente debe ser unico?
¿Que pasa si existen dos instancias?
¿El acceso global esta justificado?
¿La responsabilidad es clara?
¿Hay otra forma mas explicita de pasar la referencia?
¿Ya existe un manager o servicio equivalente?
¿Puede generar dependencias ocultas?
```

---

## Estructura conceptual

```txt
Singleton
→ instancia unica
→ acceso controlado
→ evita duplicados
```

La implementacion debe cuidar inicializacion, ciclo de vida y duplicados.

---

## Ejemplo conceptual breve

Uso posible:

```txt
AudioManager
→ una instancia central
→ reproduce musica y sonidos globales
```

Problema si se abusa:

```txt
Cualquier clase llama AudioManager.Instance
→ se ocultan dependencias
→ se dificulta cambiar o testear
```

Singleton puede servir, pero debe usarse con criterio.

---

## Como debe usarlo una IA

Una IA debe tratar Singleton como una herramienta delicada.

Debe razonar asi:

```txt
Hay sistema central
→ valido si debe ser unico
→ reviso responsabilidades
→ reviso dependencias ocultas
→ reviso alternativas
```

Antes de implementar, debe presentar:

```txt
Sistema candidato
Motivo por el que debe ser unico
Riesgo de duplicados
Responsabilidad
Alternativa simple
Riesgos
Validacion esperada
```

---

## Como NO debe usarlo una IA

Una IA no debe usar Singleton para acceder facil a cualquier cosa.

No debe:

- convertir todo manager en Singleton,
- usarlo para evitar pasar referencias,
- esconder dependencias importantes,
- crear sistemas globales por comodidad,
- meter varias responsabilidades en una instancia global,
- ignorar ciclo de vida entre escenas,
- crear Singleton si el sistema no debe ser unico.

Ejemplo de mal uso:

```txt
Problema:
Necesito que una torre conozca su panel de UI.

Mala decision:
Crear UpgradePanelSingleton.

Motivo:
Esconde una dependencia que probablemente deberia manejarse por seleccion, eventos o referencia clara.
```

---

## Reutilizacion antes que invencion

Si ya existe un sistema global o manager, la IA debe revisar si corresponde usarlo, extenderlo o evitarlo.

No debe crear un nuevo Singleton sin revisar los existentes.

---

## Senales de que Singleton puede servir

Puede valer la pena analizar Singleton si:

- duplicar el sistema rompe el juego,
- el sistema representa un servicio central,
- debe persistir entre escenas,
- existe una responsabilidad global clara,
- el acceso compartido esta justificado.

---

## Senales de Singleton mal aplicado

Singleton probablemente esta mal aplicado si:

- hay muchos `.Instance` por todos lados,
- nadie sabe que depende de que,
- el sistema global hace demasiadas cosas,
- se usa para evitar arquitectura,
- rompe reinicios de escena,
- dificulta pruebas,
- guarda estado que deberia pertenecer a otro sistema.

---

## Preguntas antes de implementar

```txt
¿Debe existir una sola instancia?
¿Por que?
¿Que responsabilidad tiene?
¿Quien necesita acceder?
¿Hay alternativa mas explicita?
¿Como se maneja ciclo de vida?
¿Como se evitan duplicados?
¿Como se valida?
```

---

## Formato de propuesta esperado

```txt
Patron:
Singleton

Sistema candidato:
...

Motivo de instancia unica:
...

Responsabilidad:
...

Alternativa simple:
...

Riesgos:
...

Validacion:
...
```

---

## Resultado esperado

Aplicar bien Singleton deberia permitir:

- evitar duplicados criticos,
- centralizar servicios realmente globales,
- coordinar sistemas unicos,
- mantener responsabilidad clara,
- controlar ciclo de vida.

---

## Regla final

```txt
Singleton no existe para acceder facil a todo.
Existe solo cuando una unica instancia esta realmente justificada.
```
## MVP1 en Cowork - Comportamiento del Productor

**Fecha**: 22 de Mayo, 2026  
**Status**: ✓ OPERACIONAL  
**Scope**: Proyecto Nuevo solamente

---

## Cómo Funciona

### Usuario abre Cowork

```
1. Usuario abre Cowork
2. Carga contexto: VAULTRUM
3. Sin hacer nada más...
```

### Productor se presenta automáticamente

```
El Productor: "Hola, soy el Productor de Vaultrum. 
Sé que tienes una idea para un juego. 
¿Quieres crear un proyecto nuevo?"
```

### Usuario responde

Si dice sí, comienza MVP1.  
Si dice otra cosa, el Productor se adapta.

---

## Flujo MVP1 - Proyecto Nuevo

### Paso 1: Presentación

```
Productor: "Perfecto. Te haré 14 preguntas simples 
sobre tu idea. Esto nos toma ~15 minutos.

Después, tendré tu proyecto listo:
- Carpeta estructurada
- Proyecto de Unity
- Obsidian Vault con documentación
- Listo para comenzar a desarrollar"
```

### Paso 2: Las 14 Preguntas

El Productor pregunta en orden:

1. **Idea principal** → "¿Cuál es tu idea de juego?"
2. **Género** → "¿Qué género es?"
3. **Público** → "¿Quién es tu público objetivo?"
4. **Perspectiva** → "¿Qué perspectiva de cámara?"
5. **Arte** → "¿Concepto artístico?"
6. **UVP** → "¿Qué lo hace único?"
7. **Unity** → "¿Qué versión de Unity?"
8. **Plataforma** → "¿Qué plataforma(s)?" (multiselect)
9. **Equipo** → "¿Cuántas personas?"
10. **Roles** → "¿Qué roles?"
11. **Plazo** → "¿Cuánto tiempo?"
12. **Fase** → "¿PoC, MVP o 1.0?"
13. **Restricciones** → "¿Restricciones técnicas?"
14. **Notas** → "¿Algo más?"

### Paso 3: Validación

Si una respuesta es vaga, el Productor ofrece 3 opciones:

```
Usuario: "No sé el género"

Productor: "Ok, ¿cuál de estos se acerca más?
1. Puzzle - Desafío lógico
2. Acción - Rápido y reflejos
3. Aventura - Exploración e historia"
```

### Paso 4: Confirmación

```
Productor: "Perfecto, tu proyecto es:
- Idea: [respuesta]
- Género: [respuesta]
... (resume todo)

¿Creo la estructura?"
```

Usuario confirma.

### Paso 5: Creación Automática

El Productor crea:

```
📁 [nombre_proyecto]/
  ├── Assets/
  ├── ProjectSettings/
  │   └── ProjectVersion.txt
  ├── Packages/
  └── [nombre_proyecto]Vault/
      ├── README.md
      ├── 00_START_HERE.md
      ├── GDD/
      ├── Decisiones/
      └── .obsidian/
```

### Paso 6: Listo

```
Productor: "¡Listo! Tu proyecto está en:
/path/to/[nombre_proyecto]/

Tu documentación está en:
/path/to/[nombre_proyecto]/[nombre_proyecto]Vault/

Abre 00_START_HERE.md en Obsidian para comenzar."
```

---

## Qué NO hace MVP1

(Y qué sí hace MVP2):

- ❌ Detecta versiones de Unity automáticamente (hardcodeadas)
- ❌ Analiza proyectos existentes (MVP2)
- ❌ Auto-vincula con Vaultrum Central (futuro)
- ❌ Crea archivos complejos (solo lo básico)

---

## Comportamiento en Diferentes Escenarios

### Escenario 1: Usuario quiere proyecto nuevo

```
Usuario: "Quiero empezar un juego de puzzle"
Productor: Ejecuta MVP1
Resultado: Proyecto creado
```

### Escenario 2: Usuario quiere proyecto existente

```
Usuario: "Tengo un proyecto que ya empecé"
Productor: "Eso es MVP2, que viene después.
Por ahora solo puedo ayudarte con proyectos nuevos."
```

### Escenario 3: Usuario quiere otra cosa

```
Usuario: "Necesito ayuda con la arquitectura"
Productor: Se adapta, pero puede sugerir cambiar de rol
"Esto suena para un Programador. ¿Quieres que te presente?"
```

---

## Limitaciones de MVP1 - Explícitamente Claras

```
SOLO PROYECTO NUEVO
SOLO 14 PREGUNTAS
SOLO CREAR ESTRUCTURA BÁSICA
SIN ANÁLISIS AUTOMÁTICO
SIN DETECCIÓN DE VERSIONES
```

No hay promesas de futuro. Solo lo que funciona hoy.

---

## Cómo se ve en la práctica

```
Usuario: "Abro Cowork con contexto de Vaultrum"

Productor: "Hola, soy el Productor de Vaultrum.
Veo que quieres crear un juego.
¿Es un proyecto nuevo?"

Usuario: "Sí, es mi primer juego"

Productor: "Genial. Te haré 14 preguntas rápidas.
Comenzamos?

1. ¿Cuál es la idea principal?"

Usuario: "Un puzzle game donde resuelves 
acertijos con mecánica de tiempo rewind"

Productor: "Bueno. Siguiente:
2. ¿Qué género es?"

[... continúa hasta pregunta 14 ...]

Productor: "Perfecto. Ahora creo la estructura.
Confirmas?"

Usuario: "Dale"

Productor: "[crear proyecto]
¡Listo! Tu proyecto está en /path/...
Abre el Obsidian Vault para comenzar."

[Proyecto creado y listo para desarrollar]
```

---

## Conclusión

MVP1 en Cowork:
- ✓ Automático cuando Vaultrum está cargado
- ✓ El Productor es la cara visible
- ✓ Flujo simple: 14 preguntas → estructura
- ✓ Sin scope creep
- ✓ Práctico y viable

Usuario no necesita entender Python, comandos, nada.  
Solo abre Cowork y el Productor lo guía.

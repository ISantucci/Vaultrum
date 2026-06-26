## Propósito

Este documento define el flujo inicial que ejecuta el agente **Productor** cuando un usuario quiere conectar un proyecto de videojuego **ya existente** a Vaultrum.

El Productor NO rediseña el proyecto.
El Productor NO reescribe la documentación.

El Productor ANALIZA el proyecto automáticamente, intenta completar las 14 preguntas base, y pide ayuda solo donde necesita aclaración.

Con esto, el usuario y Vaultrum quedan alineados y el desarrollo puede continuar apoyado por el sistema.

---

## Idea central

Un proyecto que ya comenzó tiene información dispersa:
- Carpeta del proyecto (Unity settings)
- GDD o documentación inicial
- Scripts y arquitectura
- Decisiones tomadas
- Restricciones conocidas

El Productor RECOPILA esa información, la ordena, y la conecta a Vaultrum.

No inventa nada. Solo recopila lo que existe.

---

## Lo que el Productor HACE

```txt
1. Pide que pongan la carpeta del proyecto en la ruta de Vaultrum
2. Analiza automáticamente el contenido
3. Intenta responder las 14 preguntas por sí solo
4. Para cada pregunta: ¿Puede responderla? → SÍ / NO
5. Si NO → Pide ayuda del usuario
6. Completa todas las preguntas
7. Crea Obsidian Vault dentro del proyecto
8. Documenta en el Vault
```

---

## Lo que el Productor NO HACE

```txt
✗ No modifica el proyecto Unity existente
✗ No borra archivos o carpetas
✗ No reescribe código
✗ No corrige decisiones previas
✗ No asume información que no puede verificar
✗ No inventa documentación
```

---

## Flujo operativo

### Paso 1: Preparar la carpeta

El Productor instruye al usuario:

```
Para conectar tu proyecto existente a Vaultrum:

1. Coloca la carpeta de tu proyecto en esta ubicación:
   [ruta de Vaultrum]/../[NombreDelProyecto]

2. La estructura debe ser:
   [Ruta Vaultrum]/../[NombreDelProyecto]/
   ├── Assets/
   ├── ProjectSettings/
   ├── Packages/
   └── ... (otros archivos de Unity)

3. Espera mientras analizo el proyecto...
```

Una vez ubicada, el Productor escanea automáticamente.

---

### Paso 2: Análisis Automático

El Productor analiza el proyecto e intenta responder cada pregunta:

#### **P1: ¿Cuál es la idea principal?**

**Búsqueda automática:**
- Lee `ProjectSettings/ProjectVersion.txt` para nombre
- Busca archivo `README.md` o `GDD.md`
- Busca comentarios en scripts principales
- Busca en metadata del proyecto

**Si encuentra:** Extrae la idea
**Si NO encuentra:** Pide al usuario

---

#### **P2: ¿Qué género es?**

**Búsqueda automática:**
- Analiza carpetas de Assets (si hay `RPG/`, `Puzzle/`, etc.)
- Lee GDD si existe
- Analiza estructura de scripts (si hay `EnemyAI`, `TurnManager`, etc.)
- Detecta patterns conocidos (Tower Defense, Puzzle, RPG, etc.)

**Si encuentra:** Propone el género
**Si NO encuentra:** Pide al usuario

---

#### **P3: ¿Quién es el público objetivo?**

**Búsqueda automática:**
- Lee ProjectSettings (target API level indica mobile/PC)
- Busca documentación
- Analiza complejidad de Assets (gráficos simples = casual, complejos = hardcore)
- Revisa edad rating si existe

**Si encuentra indicios:** Propone público
**Si NO encuentra:** Pide al usuario

---

#### **P4: ¿Perspectiva de cámara?**

**Búsqueda automática:**
- Busca scripts de cámara (Camera.cs, CameraController.cs)
- Analiza prefabs de cámara (posición relativa al player)
- Si hay Canvas o UI: probablemente es UI-based
- Si hay cinemachine: puede inferir perspectiva

**Si encuentra:** Detecta automáticamente
**Si NO encuentra:** Pide al usuario

---

#### **P5: ¿Concepto artístico?**

**Búsqueda automática:**
- Analiza Assets/Textures: resolución, estilo (pixel vs. 3D)
- Revisa shaders usados
- Analiza modelos 3D si existen
- Clasifica: pixel art, realista, cartoon, minimalista

**Si encuentra:** Detecta automáticamente
**Si NO encuentra:** Pide al usuario

---

#### **P6: ¿UVP (Qué lo hace único)?**

**Búsqueda automática:**
- Lee README.md
- Busca "unique", "diferente", "feature" en documentación
- Analiza si hay features no estándar (custom mechanics)
- Revisa commits iniciales (puede indicar innovación)

**Si encuentra:** Extrae el UVP
**Si NO encuentra:** Pide al usuario (CRÍTICO - es información clave)

---

#### **P7: ¿Versión de Unity?**

**Búsqueda automática:**
- Lee `ProjectSettings/ProjectVersion.txt`
- Detecta automáticamente

**Resultado:** SIEMPRE se encuentra

---

#### **P8: ¿Plataforma(s) de lanzamiento?**

**Búsqueda automática:**
- Lee `ProjectSettings/ProjectSettings.asset`
- Revisa build settings: qué plataformas están habilitadas
- Detecta automáticamente

**Resultado:** SIEMPRE se encuentra

---

#### **P9: ¿Cuántas personas en el equipo?**

**Búsqueda automática:**
- Revisa commit history (si es repo Git)
- Analiza si hay carpetas compartidas o scripts de múltiples personas
- Puede inferir si es solo desarrollador o equipo

**Si encuentra indicios:** Propone número
**Si NO encuentra:** Pide al usuario

---

#### **P10: ¿Roles de cada miembro?**

**Búsqueda automática:**
- Analiza carpetas (si hay `Art/`, `Code/`, `Design/`)
- Revisa tipos de assets (si hay solo 3D models → artista; si solo scripts → programador)
- Busca documentación sobre roles

**Si encuentra indicios:** Propone roles
**Si NO encuentra:** Pide al usuario (completar manualmente)

---

#### **P11: ¿Plazo para terminarlo?**

**Búsqueda automática:**
- Busca en README o documentación
- Analiza commit history para estimar velocidad
- Busca referencias a fechas límite

**Si encuentra:** Extrae plazo
**Si NO encuentra:** Pide al usuario

---

#### **P12: ¿Fase del proyecto?**

**Búsqueda automática:**
- Analiza número de features implementadas
- Revisa si hay build player
- Analiza versioning (0.1, 1.0, etc.)
- Determina: PoC, MVP o versión completa

**Si encuentra indicios:** Propone fase
**Si NO encuentra:** Pide al usuario

---

#### **P13: ¿Restricciones/limitaciones?**

**Búsqueda automática:**
- Lee README o documentación de problemas conocidos
- Busca comentarios "TODO", "FIXME", "HACK"
- Analiza si falta algo crítico (audio system sin sonidista, etc.)

**Si encuentra:** Extrae restricciones
**Si NO encuentra:** Pide al usuario si hay limitaciones

---

#### **P14: ¿Algo más que deba saber?**

**Búsqueda automática:**
- Busca en documentación datos especiales
- Lee archivos de configuración
- Analiza si hay agentes especializados necesarios (multiplayer, IA, etc.)

**Si encuentra:** Lo documenta
**Si NO encuentra:** Pregunta abierta al usuario

---

### Paso 3: Presentar Hallazgos

El Productor presenta lo que encontró:

```
ANÁLISIS AUTOMÁTICO COMPLETADO

P1 - Idea principal: 
   ✓ ENCONTRADO: "Puzzle game cooperativo"

P2 - Género:
   ✓ ENCONTRADO: Puzzle

P3 - Público objetivo:
   ✗ NO ENCONTRADO - Necesito tu ayuda:
   ¿Quién es tu público? (casual, hardcore, edad)

P4 - Perspectiva:
   ✓ ENCONTRADO: Top-down

P5 - Concepto artístico:
   ✓ ENCONTRADO: Pixel Art

P6 - UVP:
   ✗ NO ENCONTRADO - CRÍTICO:
   ¿Qué hace ÚNICO a tu juego?

... (y así con las 14)

PENDIENTES: P3, P6, P9, P11
Necesito que completes estas 5 preguntas.
```

---

### Paso 4: Completar Preguntas Pendientes

El Productor:
1. Lista las preguntas donde NO encontró respuesta
2. Las hace una por una
3. El usuario responde
4. Valida que la respuesta es clara (si no, repite)
5. Continúa hasta completar TODAS

**Regla:** Si una pregunta quedó sin respuesta clara, el Productor propone 3 opciones (igual que en flujo de nuevo proyecto).

---

### Paso 5: Crear Obsidian Vault del Proyecto

Una vez completadas las 14 preguntas:

```
Se va a crear Obsidian Vault en:
[Carpeta del Proyecto]/[NombreProyecto]Vault

Esto contendrá:
- Análisis completo del proyecto
- Las 14 preguntas respondidas
- Decisiones documentadas
- Siguiente paso para desarrollo

¿Continuar?
```

Crea automáticamente.

---

### Paso 6: Documentar en el Vault

El Productor crea un documento inicial en el **Obsidian Vault del Proyecto** con:

```txt
PROYECTO: [Nombre]
IDEA CENTRAL: [De P1]
GÉNERO: [De P2]
PÚBLICO: [De P3]
PERSPECTIVA: [De P4]
CONCEPTO ARTÍSTICO: [De P5]
UVP: [De P6]
VERSION UNITY: [De P7]
PLATAFORMA(S): [De P8]
EQUIPO: [De P9 y P10]
PLAZO: [De P11]
FASE: [De P12]
RESTRICCIONES: [De P13]
NOTAS: [De P14]

ESTADO: ✓ Proyecto conectado a Vaultrum
SIGUIENTE PASO: Usuario puede continuar desarrollo con apoyo de Vaultrum
```

---

## Reglas críticas

### 1. No asumir sin evidencia

Si no puede verificar automáticamente, pide al usuario.

Mejor preguntar que adivinar.

### 2. Las 14 preguntas DEBEN estar completas

No avanza hasta que todas estén respondidas.

### 3. Mantener proyecto intacto

NO modifica nada del proyecto Unity.

Solo ANALIZA y DOCUMENTA.

### 4. Vaultrum Central + Project Vault

Crea el Vault DENTRO del proyecto (no referencias externas).

Pero mantiene conexión con Vaultrum Central.

---

## Errores que este flujo PREVIENE

```txt
✗ Proyecto desalineado con Vaultrum
   → Porque lo analiza automáticamente

✗ Documentación duplicada
   → Porque extrae lo que ya existe

✗ Información perdida
   → Porque recopila del proyecto existente

✗ Decisiones no documentadas
   → Porque crea Vault del proyecto

✗ Proyecto sin guía clara
   → Porque completa las 14 preguntas
```

---

## Regla de finalización

El flujo inicial para proyecto comenzado está **COMPLETO** cuando:

```txt
✓ Las 14 preguntas TODAS están respondidas
✓ Obsidian Vault del proyecto fue creado
✓ Documentación inicial está en el Vault
✓ Usuario puede continuar con desarrollo apoyado por Vaultrum
```

---

## Diferencia con Flujo de Proyecto Nuevo

| Aspecto | Proyecto Nuevo | Proyecto Comenzado |
|---------|----------------|-------------------|
| **Entrada** | Idea del usuario | Proyecto existente |
| **Análisis** | Usuario responde 14 preguntas | Vaultrum analiza automáticamente |
| **Preguntas pendientes** | Pocas (usuario es claro) | Varias (info dispersa) |
| **Creación** | Crea carpeta + Unity + Vault | Solo crea Vault (carpeta existe) |
| **Documentación inicial** | Nueva, en blanco | Basada en análisis |
| **Siguiente paso** | Usuario comienza desarrollo | Usuario continúa desarrollo |

---

## Ejemplos de análisis automático

### Ejemplo 1: Proyecto con buena documentación

```
Usuario coloca carpeta.
Productor analiza:
- ProjectVersion.txt → Unity 2022.3
- README.md → Idea, género, público
- GDD.pdf → Detalles de mecánicas
- Scripts → Detecta perspectiva top-down

Resultado: 13/14 preguntas encontradas automáticamente
Pendiente: Solo P14 (datos adicionales)
Tiempo: 2 minutos de análisis
```

### Ejemplo 2: Proyecto sin documentación

```
Usuario coloca carpeta.
Productor analiza:
- ProjectVersion.txt → Unity 2023.2
- Assets → Detecta pixel art
- Scripts → Detecta estructura de puzzle
- Build Settings → Detecta Web

Resultado: 7/14 preguntas encontradas
Pendientes: P1, P3, P6, P9, P10, P11, P14
Usuario debe responder esas 7
Tiempo: 5 minutos de análisis + respuestas del usuario
```

---

## Integración con Vaultrum Central

El Obsidian Vault del Proyecto está vinculado a Vaultrum Central:

```txt
Vaultrum Central
  ↓ (referencia)
Project Vault
  ↓ (hereda conocimiento)
Usuario desarrolla con ambos abiertos
```

El Arquitecto de Vaultrum es responsable de mantener esa relación.


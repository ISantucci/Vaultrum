## Propósito

Esta carpeta contiene los requerimientos generados por el Área de Producción.

Cada requerimiento debe concretar una parte del timeline asociado.

---

## Formato obligatorio

Cada requerimiento respeta esta estructura:

```txt
Título
Área afectada
Criticidad
Descripción
Subtasks
```

---

## Regla de numeración y nombre de archivo

Un requerimiento hereda el número base del timeline que concreta, y lo subnumera:

```txt
TL-001
  RQ-001.1
  RQ-001.2
  RQ-001.3
```

El archivo se nombra con el código, el separador y el nombre descriptivo:

```txt
RQ-XXX.Y_Nombre_Descriptivo.md
RQ-001.1_Paletas_Controlables.md
```

---

## Requerimientos registrados

Los requerimientos de un proyecto viven en `06_Proyectos/<Proyecto>/01_Produccion/`. Acá quedan **solo los de Modo Owner**.

### TL-007 — La apertura de Vaultrum (Modo Owner)

- [[RQ-007.1_Contrato_De_Instalacion|RQ-007.1 Contrato de instalación]] — dónde vive Vaultrum, la estructura resultante y la ley de no-autoescritura
- [[RQ-007.2_La_Puerta|RQ-007.2 La puerta]] — `CLAUDE.md` de raíz: Modo Vaultrum arranca solo en el primer mensaje
- [[RQ-007.3_Relevamiento_De_Apertura|RQ-007.3 Relevamiento de apertura]] — bifurcación, las quince preguntas por bloques, variante de proyecto existente y palabra de salteo
- [[RQ-007.4_El_Cuaderno_Del_Proyecto|RQ-007.4 El cuaderno del proyecto]] — el markdown afuera de Vaultrum. Decisión tomada: el cuaderno es **un archivo**; los artefactos van a carpetas por área (`TL-008`)
- [[RQ-007.6_Rama_UIUX_Independiente|RQ-007.6 Rama UI/UX independiente]] — `UXS` cuelga del `RQ`, no del `GDS`. `LDS` no cambia, y está escrito por qué
- [[RQ-007.7_Portabilidad_ClaudeCode_Codex|RQ-007.7 Portabilidad Claude Code + Codex]] — las diez skills instaladas en `.claude/skills` y `.agents/skills`, con el presupuesto ya medido

Hilo `.5` (**mudanza de salidas**) **absorbido por `RQ-008.4_Mudanza_De_Lo_Historico`**, que se ejecutó el 2026-08-25.

### TL-008 — La Agencia es la empresa, no el archivo (Modo Owner)

- [[RQ-008.1_Contrato_De_Salida_Por_Area|RQ-008.1 Contrato de salida por área]] — `Salidas/` deja de guardar y pasa a declarar: forma, numeración, criterios de cierre
- [[RQ-008.2_Estructura_De_Carpeta_De_Proyecto|RQ-008.2 Estructura de carpeta de proyecto]] — el árbol, la creación perezosa y los wikilinks. **Emplazamiento del Arquitecto, vinculante**
- [[RQ-008.3_Reapuntado_De_Las_Skills|RQ-008.3 Reapuntado de las skills]] — cinco áreas escriben en el proyecto; Conocimiento y Arquitectura no cambian
- [[RQ-008.4_Mudanza_De_Lo_Historico|RQ-008.4 Mudanza de lo histórico]] — los 69 archivos de Pong y de Vaultrum World salen del sistema con plano del Arquitecto
- [[RQ-008.5_Conocimiento_Copiloto_De_Documentacion|RQ-008.5 Conocimiento copiloto de documentación]] — asiste en la escritura del proyecto. **Asiste, no firma**

> Proyectos: `00_Proyectos`. Los requerimientos del Pong 3D y de Vaultrum World se mudaron ahí el 2026-08-25.

---


---
tipo: documento
familia: Documentación oficial de motor
autor: Epic Games, documentación viva
anio: vivo (versión 5.8 consultada, 2026-10-04)
formato: Doc técnica oficial
acceso: Libre
licencia: nivel B — publicada libremente por Epic Games; sin licencia de reuso del texto declarada
prioridad: alta
estado: Catalogado
mision: EST-020_Mision_Mapa_Territorio_Arte
url: https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python
---

# Documento 77 — Unreal: scripting del editor con Python

> Artefacto real de la industria, catalogado para que la IA Operativa pueda automatizar el editor de Unreal. Es referencia de la herramienta, no un tutorial.
> **IP:** ficha + referencia. La Biblioteca no aloja ni reproduce el documento original.

---

- **Autor / estudio y año:** Epic Games, documentación viva (versión 5.8 consultada)
- **Tipo:** doc técnica oficial
- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python
- **Estado de acceso:** **Libre.** Nivel B.
- **Qué se aprende:**
  - Que el scripting con Python en Unreal es **solo de editor**: corre en el editor, no en el juego ni en una build empaquetada.
  - Qué hay que habilitar (el *Python Editor Script Plugin*) y qué Python embebe el motor (3.11.8 en la 5.8, alineado con la VFX Reference Platform).
  - Las formas de ejecutar: la consola del Output Log, el comando `py`, un parámetro de línea de comandos, scripts de arranque configurados en el proyecto e `init_unreal.py`.
  - El módulo `unreal` y las prácticas que evitan romper un proyecto: usar las librerías de assets del editor en vez de mover archivos por el sistema operativo, cambiar propiedades con `set_editor_property` para que el editor se entere, y agrupar varias operaciones en una transacción para que se deshagan juntas.
- **Gap de Vaultrum que cubre:** es la capa sobre la que se apoya casi cualquier automatización del editor, con o sin MCP. Referencia de `Unreal para motion graphics` y de toda operación por lotes sobre assets.
- **Prioridad:** **Alta**

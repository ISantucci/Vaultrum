---
tipo: documento
familia: Documentación oficial de motor
autor: Epic Games, documentación viva
anio: 2026 (plugin introducido en UE 5.8)
formato: Doc técnica oficial de plugin experimental
acceso: Libre
licencia: nivel B — publicada libremente por Epic Games; sin licencia de reuso del texto declarada
prioridad: alta
estado: Catalogado
mision: EST-020_Mision_Mapa_Territorio_Arte
url: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-mcp-in-unreal-editor
---

# Documento 76 — Unreal: plugin MCP del editor

> Artefacto real de la industria, catalogado para que la IA Operativa pueda operar el editor de Unreal. Es referencia de la herramienta, no un tutorial.
> **IP:** ficha + referencia. La Biblioteca no aloja ni reproduce el documento original.

---

- **Autor / estudio y año:** Epic Games, documentación viva (versión 5.8 consultada)
- **Tipo:** doc técnica oficial de un plugin experimental
- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-mcp-in-unreal-editor
- **Estado de acceso:** **Libre.** Nivel B.
- **Qué se aprende:**
  - Que Unreal trae un plugin MCP **oficial y experimental** (`ModelContextProtocol`, visible como *Unreal MCP*), introducido en la 5.8: un servidor MCP embebido en el propio editor.
  - Transporte: HTTP local, con Server-Sent Events; no admite stdio ni WebSocket. Dirección por defecto: `http://127.0.0.1:8000/mcp`, con puerto y ruta configurables en las preferencias del editor.
  - Cómo se pone en marcha: se habilita el plugin junto con el de conjuntos de herramientas, se configura el arranque automático en las preferencias del editor y un comando de consola genera la configuración del cliente.
  - Qué expone: herramientas sobre actores, escena, instancias de material y objetos, inspección de widgets y ejecución de tests de automatización.
  - Su límite de seguridad: por defecto solo acepta conexiones locales y **no tiene autenticación**; no es seguro exponerlo fuera de la máquina.
  - Hay alternativas comunitarias de terceros, anteriores al plugin oficial: github.com/chongdashu/unreal-mcp y github.com/flopperam/unreal-engine-mcp. No son de Epic y no se tratan como tales.
- **Gap de Vaultrum que cubre:** es la vía oficial para que Vaultrum opere el editor de Unreal como ya opera Blender. Referencia de base para `Unreal para motion graphics` y `Motion graphics y UI` cuando el trabajo se hace a través del editor. Al ser experimental, toda instrucción que dependa de él declara la versión del motor.
- **Prioridad:** **Alta**

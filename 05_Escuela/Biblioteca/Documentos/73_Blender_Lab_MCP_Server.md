---
tipo: documento
familia: Documentación oficial de motor
autor: Blender Foundation (Blender Lab)
anio: 2026
formato: Página de proyecto experimental, con repositorio de código
acceso: Libre
licencia: nivel B — página pública del proyecto; la licencia del código no se confirmó en lo consultado (verificar en el repositorio)
prioridad: alta
estado: Catalogado
mision: EST-020_Mision_Mapa_Territorio_Arte
url: https://www.blender.org/lab/mcp-server/
---

# Documento 73 — Blender Lab: MCP Server

> Artefacto real de la industria, catalogado para que la IA Operativa pueda operar Blender. Es referencia de la herramienta, no un tutorial.
> **IP:** ficha + referencia. La Biblioteca no aloja ni reproduce el documento original.

---

- **Autor / estudio y año:** Blender Foundation, dentro de Blender Lab, 2026
- **Tipo:** página de proyecto oficial y experimental
- **URL:** https://www.blender.org/lab/mcp-server/ · código, según la propia página: https://projects.blender.org/lab/blender_mcp
- **Estado de acceso:** **Libre.** Nivel B para la página; la licencia del código queda a confirmar en el repositorio.
- **Qué se aprende:**
  - Que existe un servidor MCP **oficial** de Blender: una interfaz liviana para que un modelo de lenguaje use la API de Python, consulte la documentación y explore escenas complejas.
  - Requisito de versión: **Blender 5.1 o posterior.**
  - Su estado: **experimental**, parte de Blender Lab y no del producto estable.
  - La advertencia que manda sobre todo lo demás: el servidor **ejecuta código generado por el modelo sin resguardos** que eviten que los datos se borren o se envíen afuera. La propia página recomienda usarlo en un entorno aislado o en una máquina sin información sensible.
  - Existe una alternativa comunitaria de terceros, anterior y distinta (github.com/ahujasid/blender-mcp). No es la oficial y no se trata como tal.
- **Gap de Vaultrum que cubre:** es la referencia de origen de `Blender por MCP`. Fija qué versión hace falta, qué expone el servidor y, sobre todo, el riesgo que se asume al usarlo: toda operación que toque archivos del owner pasa por esa advertencia.
- **Prioridad:** **Alta**

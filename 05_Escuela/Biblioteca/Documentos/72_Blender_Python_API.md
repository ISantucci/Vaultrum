---
tipo: documento
familia: Documentación oficial de motor
autor: Blender Foundation, referencia viva generada desde el código
anio: vivo (consultada 2026-10-04)
formato: Referencia de API de Python (web; también empaquetada en el servidor MCP de Blender)
acceso: Libre
licencia: nivel B — pública y oficial; lo consultado no declara licencia de reuso del texto (Blender es GPL; la licencia de la referencia queda a confirmar)
prioridad: alta
estado: Catalogado
mision: EST-020_Mision_Mapa_Territorio_Arte
url: https://docs.blender.org/api/current/
---

# Documento 72 — Blender Python API

> Artefacto real de la industria, catalogado para que la IA Operativa pueda operar Blender por código. Es referencia de la herramienta, no un tutorial.
> **IP:** ficha + referencia. La Biblioteca no aloja ni reproduce el documento original.

---

- **Autor / estudio y año:** Blender Foundation, referencia viva generada desde el propio código de Blender
- **Tipo:** referencia oficial de la API de Python
- **URL:** https://docs.blender.org/api/current/
- **Estado de acceso:** **Libre.** Nivel B: la licencia del texto no está declarada en lo consultado. El servidor MCP de Blender que usa Vaultrum trae esta referencia empaquetada junto con el manual y la busca sin conexión.
- **Qué se aprende:**
  - El módulo `bpy` entero: `bpy.data` (los datos del archivo), `bpy.context` (lo seleccionado y activo), `bpy.ops` (los operadores, lo mismo que hace un botón) y `bpy.types` (todas las clases). Saber cuál de los cuatro usar es la mitad del trabajo.
  - La sección *Gotchas*: los errores típicos de quien escribe código para Blender — operadores que dependen del contexto, referencias a datos que quedan inválidas, acceso a mallas en modo edición contra modo objeto, hilos, rutas de archivo. Es la página que evita la mayoría de los fallos de un script generado.
  - Los módulos de bajo nivel (`bmesh`, `mathutils`) para editar geometría sin pasar por operadores.
- **Gap de Vaultrum que cubre:** cuando Vaultrum opera Blender por MCP, lo que se ejecuta es código Python contra esta API. Es la referencia directa de `Blender por MCP`: antes de ejecutar, se verifica acá que la llamada existe en la versión instalada. Secundaria para `Rigging y skinning` y `Texturizado UV y materiales` cuando se automatizan.
- **Prioridad:** **Alta**

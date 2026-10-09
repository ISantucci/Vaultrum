---
tipo: documento
familia: Documentación oficial de motor
autor: Epic Games, documentación viva
anio: vivo (versión 5.8 consultada; la función está marcada Beta)
formato: Doc técnica oficial con referencia de API HTTP
acceso: Libre
licencia: nivel B — publicada libremente por Epic Games; sin licencia de reuso del texto declarada
prioridad: media
estado: Catalogado
mision: EST-020_Mision_Mapa_Territorio_Arte
url: https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-for-unreal-engine
---

# Documento 78 — Unreal: Remote Control API

> Artefacto real de la industria, catalogado para que la IA Operativa pueda operar Unreal desde afuera del editor. Es referencia de la herramienta, no un tutorial.
> **IP:** ficha + referencia. La Biblioteca no aloja ni reproduce el documento original.

---

- **Autor / estudio y año:** Epic Games, documentación viva (versión 5.8 consultada)
- **Tipo:** doc técnica oficial, con referencia de la API HTTP
- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-for-unreal-engine · referencia HTTP: https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-api-http-reference-for-unreal-engine
- **Estado de acceso:** **Libre.** Nivel B.
- **Qué se aprende:**
  - Que Remote Control expone el motor a un cliente externo por un servidor web: pedidos HTTP con una API de estilo REST y mensajes por WebSocket.
  - Qué se puede hacer: llamar cualquier función expuesta a Blueprint y Python, y leer o escribir cualquier propiedad expuesta o publicada en un *Remote Control Preset*. Los presets permiten exponer controles sin programar.
  - La referencia HTTP lista las rutas: información de rutas (`/remote/info`), llamada a funciones (`/remote/object/call`), propiedades (`/remote/object/property`), descripción de objetos, búsqueda de assets, miniaturas, lotes (`/remote/batch`) y eventos (experimental).
  - Su estado: **Beta**, y deshabilitado por defecto en proyectos empaquetados o en modo `-game`, salvo que se lo habilite por línea de comandos.
  - Puerto: las dos páginas consultadas no lo declaran. El que circula como predeterminado es 30010 para HTTP (30020 para WebSocket); se verifica en la configuración del proyecto antes de apuntar un cliente.
- **Gap de Vaultrum que cubre:** la vía alternativa al MCP para operar Unreal desde afuera: más madura (Beta, contra experimental) y sin un modelo de lenguaje en el medio. Referencia para `Unreal para motion graphics` (controlar una pieza en vivo) y para `Motion graphics y UI`.
- **Prioridad:** **Media**

---
tipo: documento
familia: Documentación oficial de motor
autor: Epic Games, documentación viva
anio: vivo (versión 5.8 consultada, 2026-10-04)
formato: Doc técnica oficial (guía práctica)
acceso: Libre
licencia: nivel B — publicada libremente por Epic Games; sin licencia de reuso del texto declarada
prioridad: media
estado: Catalogado
mision: EST-020_Mision_Mapa_Territorio_Arte
url: https://dev.epicgames.com/documentation/en-us/unreal-engine/animating-umg-widgets-in-unreal-engine
---

# Documento 74 — Unreal: Animating UMG Widgets

> Artefacto real de la industria, catalogado para que la IA Operativa pueda operar la animación de interfaces en Unreal. Es referencia de la herramienta, no un tutorial.
> **IP:** ficha + referencia. La Biblioteca no aloja ni reproduce el documento original.

---

- **Autor / estudio y año:** Epic Games, documentación viva (versión 5.8 consultada)
- **Tipo:** doc técnica oficial, guía práctica
- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/animating-umg-widgets-in-unreal-engine
- **Estado de acceso:** **Libre.** Nivel B.
- **Qué se aprende:**
  - Dónde vive la animación de una interfaz UMG: el panel de animaciones crea las pistas y la línea de tiempo aplica los cambios de propiedad (posición, color, escala) a un widget a lo largo del tiempo, con claves.
  - Las dos formas de poner claves: automática (*Auto Key*) o una por propiedad, para control fino.
  - Que cada animación queda como variable en el Blueprint del widget y se dispara con nodos de reproducir y detener, desde eventos como la construcción del widget o un botón.
- **Gap de Vaultrum que cubre:** `Motion graphics y UI` necesita saber dónde se anima una interfaz en Unreal y cómo se dispara esa animación; `Unreal para motion graphics` la toma como el caso más simple, antes de Motion Design. Es la referencia de *dónde se toca*, no un curso de UI.
- **Prioridad:** **Media**

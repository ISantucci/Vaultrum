---
tipo: documento
familia: Documentación oficial de motor
autor: Epic Games, documentación viva
anio: —
formato: Doc técnica oficial
acceso: **Libre, sin cuenta ni paywall
licencia: a confirmar
prioridad: alta
estado: Catalogado
mision: EST-006_Mision_Lote_Biblioteca_Agosto26
url: https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine
---

# Documento 40 — Unreal Engine — Gameplay Framework

> Artefacto real de la industria, catalogado para consulta del Productor y de Game Design.
> **IP:** ficha + referencia. La Biblioteca no aloja ni reproduce el documento original.

---

- **Autor / estudio y año:** Epic Games, documentación viva (UE 5.8 consultada)
- **Tipo:** Doc técnica oficial
- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine (**fetcheada OK**) · Referencia rápida: https://dev.epicgames.com/documentation/unreal-engine/gameplay-framework-quick-reference-in-unreal-engine · Guía C++ de terceros muy usada: https://tomlooman.com/unreal-engine-gameplay-framework/
- **Estado de acceso:** **Libre, sin cuenta ni paywall.**
- **Qué se aprende:**
  - Las clases base y su reparto de responsabilidades: Actor, Actor Component, Pawn, Character, Controller.
  - Sistemas de gestión: Game Instance, Game Mode, Game State, Player State — **una taxonomía de estado por alcance y ciclo de vida** que es transferible a cualquier motor, Unity incluido.
  - La separación Controller/Pawn: el controlador es un actor no físico que posee un pawn, y hay implementaciones distintas para humano y para IA. Patrón de desacople muy limpio.
  - Que la misma arquitectura se exprese en C++ o Blueprint muestra cómo diseñar una API que sirva a dos audiencias técnicas.
- **Gap de Vaultrum que cubre:** modelo de referencia de gameplay framework y gestión de estado, aplicable como marco conceptual aun trabajando en Unity.
- **Prioridad:** **Alta**

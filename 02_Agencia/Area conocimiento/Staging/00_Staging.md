## Propósito

Staging es la pizarra de **commits pendientes** del Área de Conocimiento: aprendizajes escritos que esperan aprobación para mergearse al Core.

Es una zona **transitoria**, no un registro histórico.

---

## Cómo funciona

```
Encargado de Commits detecta aprendizaje
   ↓
Documentador escribe la nota .md acá (Staging)
   ↓
Arquitecto de Conocimiento define destino y diff
   ↓
Se presenta el diff al maintainer
   ↓
   ├── Aprobado → merge al Core → la nota se limpia de Staging
   └── Rechazado → se descarta → la nota se limpia de Staging
```

---

## Reglas

- Cada `.md` en Staging es un aprendizaje candidato, no conocimiento definitivo.
- Nada en Staging es fuente de verdad: la fuente es el Core (`main`).
- Al mergear o descartar, la nota se elimina de Staging (principio 11: no acumular historial).
- Si se quiere historial, vive en git (`git log`), no acá.

---

## Estado actual

**Vacío.** No hay commits pendientes.

Los tres que había se mergearon al Core en el primer ciclo completo `Core → Agencia → Conocimiento → Core`:

| Commit | Aprendizaje | Dónde quedó |
|--------|-------------|-------------|
| `COMMIT-001` | Optimizar sin requerimiento de performance es scope no pedido | Cuando NO optimizar (Fundamentos de Optimización) + mitad 2 de Baseline de entregable |
| `COMMIT-002` | Una verificación parcial vale si declara su alcance | Verificacion parcial declarada |
| `COMMIT-003` | El medio de la cadena funciona; fallan la entrada, las ramas opcionales y la salida | Gates verificables + tres pasos ejecutables en `vaultrum-produccion`, `vaultrum-gamedesign` y `vaultrum-programador` |

Los tres viven en la sección nueva del Core `01_VaultrumCore/.../04_Criterios de entrega/`, junto a la Ley del baseline formalizada desde la bitácora.

Se sumó además el handoff de la Escuela: `EST-001`, `EST-004` y `EST-005` se resolvieron **por indexación** en `Experiencia de juego` — el Core guarda el puntero, la Biblioteca guarda el peso. El libro `01_Pong` pasó a *En la Biblioteca* y quedó escrita la regla que faltaba: un libro solo es insumo válido de producción si está en ese estado.

---

## Nota de la primera vuelta

Vale dejarlo escrito porque es el hallazgo, no el trámite: **hasta este ciclo, Staging nunca se había vaciado.** Tres commits esperaban aprobación y dos `EST` esperaban handoff, mientras la arquitectura entera se justificaba en un ciclo que todavía no había cerrado una vez.

Un ciclo que no cierra convierte al Core en biblioteca estática y a esta área en decorativa. La señal de que el sistema funciona no es que Staging tenga contenido: es que **se vacíe**.

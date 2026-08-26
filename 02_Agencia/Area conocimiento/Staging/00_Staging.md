## Propósito

Staging es la pizarra de **commits pendientes** del Área de Conocimiento: aprendizajes escritos que esperan aprobación para mergearse al Core.

Es una zona **transitoria**, no un registro histórico.

---

## Cómo funciona

```
Cosechador detecta el aprendizaje sobre la evidencia juntada
   ↓
Documentador escribe la nota .md acá (Staging)
   ↓
Bibliotecario de Pertenencia define pertenencia, pide el emplazamiento y arma el diff
   ↓
Validador corre el instrumento sobre la nota
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

**Tres commits pendientes.**

### [[00_Leyes_en_antesala|Leyes en antesala]]

Lo que el uso del propio sistema fue dejando como criterio y todavía no se formalizó en el Core. Es literalmente la antesala de una ley, así que su lugar es el Staging y no la raíz del vault: acá es donde se decide qué vuelve a `main`. Se trajo el 2026-08-25 desde `00_START_HERE`.

A diferencia de un `COMMIT-XXX`, no es una propuesta cerrada: es la libreta de la que salen.

### [[COMMIT-005_La_ley_que_la_herramienta_no_mide|COMMIT-005 — La ley que la herramienta no mide]]

Origen: `ARQ-013`, la Pasada sobre el estante de Documentación real de la Escuela. Una ley escrita en tres lugares que el verificador no medía dejó entrar 52 links de retorno con el gate en verde, por una excepción que se reconocía por su rótulo y no por su efecto. Tres movimientos: la regla sin medición, la excepción que se reconoce por su rótulo, y el gate que mide la copia de trabajo en vez del paquete que se entrega. Completa `Gates verificables` y `Verificacion parcial declarada` por el lado del instrumento. Espera aprobación del owner.

### [[COMMIT-006_La_contencion_se_enlaza_la_cadena_se_nombra|COMMIT-006 — La contención se enlaza, la cadena se nombra]]

Origen: `ARQ-014`, el emplazamiento del cuaderno de proyecto de Pong3D. En una carpeta de proyecto conviven dos relaciones —contención y cadena— y se estaban dibujando con el mismo tipo de arista. La cadena converge y cruza carpetas, así que no entra en un árbol en ninguna de las dos direcciones: se nombra con backticks. **Contradice el corolario vigente de la cadena**, así que su aprobación implica reescribirlo. Espera al owner.

### [[COMMIT-004_La_posicion_de_un_area_en_el_tiempo|COMMIT-004 — La posición de un área en el tiempo]]

Origen: `ARQ-005` sobre el Área de Arquitectura y `ARQ-009` sobre el Área de UI/UX. Las dos áreas tenían el mismo defecto —entrar cuando otra ya había cerrado— y el mismo arreglo. La mitad nueva es la segunda: adelantar un área no alcanza si no trae un instrumento con qué probar lo que afirma. Espera aprobación del owner.

---

## Lo que ya se mergeó

**Vacío de la primera vuelta.** No quedaban commits pendientes antes de éste.

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

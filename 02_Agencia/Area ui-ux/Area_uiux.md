## Propósito

El Área de UI/UX de Vaultrum diseña la **capa de comunicación entre el juego y el jugador**: qué información ve, cómo navega y cómo el sistema le responde. No define reglas (Game Design) ni el espacio jugable (Level Design): diseña las pantallas, el HUD, los menús y los flujos que hacen que el sistema sea **legible y usable**.

Es el puente entre "el sistema tiene estos estados, inputs y feedback" y "el jugador los entiende y los opera sin fricción". Toma el `GDS` de Game Design (y el `LDS` si existe) y produce un `UXS` (UI/UX spec) que el Área de Programación construye.

---

## Entrada del área

- un `GDS-XXX.n` cerrado (estados, inputs, salidas/feedback, información que el jugador necesita).
- opcionalmente el `LDS-XXX.n` si la interfaz depende del nivel (HUD contextual, minimapa, etc.).

Si el `GDS` no requiere interfaz ni comunicación con el jugador, esta área no interviene. Si el `GDS` está ambiguo sobre estados o feedback, deriva a Game Design.

---

## Sub-agentes del área

### [[01_Analista_UX]]

Interpreta qué necesita **ver, entender y decidir** el jugador en cada momento. Encuadra con el pilar de **claridad/legibilidad (4)**: en todo momento el jugador debe responder ¿qué pasa? ¿qué puedo hacer? ¿cómo me va? Mapea los flujos del jugador. No define el layout visual final.

### [[02_Disenador_UI]]

Convierte el encuadre en la interfaz: pantallas, HUD, menús, jerarquía de información, affordances/signifiers, mapping control→efecto, estados de la interfaz y feedback visual. Abre el **UXS-XXX.n**. No cambia reglas ni programa.

### [[03_Validador_UX]]

Verifica que la interfaz sea usable primero y atractiva después: legible, sin fricción, con feedback claro, accesible. Si algo no cierra, **rebota** al sub-agente correcto. Cierra el `UXS` y lo deja como insumo para Programación.

---

## Cómo trabaja el área — el loop

```
GDS cerrado (+ LDS si aplica)
  ↓
Analista de UX   → encuadre de UX (qué ve/decide el jugador, flujos)
  ↓
Diseñador de UI  → UXS-XXX.n (pantallas, HUD, menús, jerarquía, feedback)  ⟵ gate de interfaz
  ↓
Validador de UX  → ¿usable, legible, sin fricción, accesible?
        ├── Sí  → cierra el UXS
        └── No  → rebota:
                  · falta entender qué necesita el jugador → Analista de UX
                  · pantallas/jerarquía/feedback sin cerrar → Diseñador de UI
                  · estado o feedback mal definido en reglas → deriva a Game Design
```

Usabilidad primero, engagement después: la interfaz no cierra hasta que el jugador *puede* operar el sistema sin fricción.

---

## Salida del área

Por cada `GDS` con interfaz, un **UXS-XXX.n** registrado en `00_Indice_uxs`, con su índice. La numeración se hereda del `GDS` (`GDS-001.2 → UXS-001.2`).

El `UXS` es insumo del Área de Programación (junto al `GDS` y, si existe, el `LDS`).

Queda registrada en `Salidas/`:

- [[00_Indice_uxs|Índice de UXS]]

---

## Regla operativa

Primero entender qué necesita ver, entender y decidir el jugador.
Después diseñar la interfaz (pantallas, HUD, menús, jerarquía, feedback).
Después validar que sea usable, legible y accesible.
Usabilidad primero, engagement después. Nunca decorar a costa de la legibilidad.

---

## Límites del área

No define reglas ni balance (Game Design). No diseña niveles/espacio jugable (Level Design). No programa (Programación). No define alcance (Producción). No hace arte final ni ilustración. Si falta estado/feedback en las reglas → Game Design; si falta implementación → entrega el `UXS` a Programación.

---

## Encadenado con otras áreas

Recibe de: **Game Design** (`GDS`) y opcionalmente **Level Design** (`LDS`).
Entrega a: **Programación** (`UXS` como insumo de la solución técnica).
Consulta on-demand: la Escuela (`05_Fundamentos_de_experiencia_ludica`), pilares 3, 4, 5, 7.

La numeración `.n` se mantiene entre `GDS / UXS / SOL / EJ` para trazabilidad de punta a punta.

## Flujos del área

Cada flujo es un paso del loop del área. Se entra por el flujo que corresponde al estado del trabajo, no por todos.

### [[01_Flujo_Analisis_UX|Flujo Analisis UX]]

### [[02_Flujo_Diseno_UI|Flujo Diseno UI]]

### [[03_Flujo_Validacion_UX|Flujo Validacion UX]]

---

## Skill del área

El área corre como la skill `vaultrum-uiux` (fuente versionada en `02_Agencia/Area ui-ux/Skills/vaultrum-uiux/SKILL.md`).

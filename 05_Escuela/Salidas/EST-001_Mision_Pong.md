## Misión (gap estudiado)

**EST-001 — Pong: primer "libro" de la librería de Fundamentos de Experiencia.**

Origen: Ley candidata #1 (fricción mínima / baseline competente). La ley nació del Pong3D (vaultrumtest1): el juego salió 7/10 pero el *desarrollo* 4/10, porque hicieron falta demasiados prompts para algo tan básico como un Pong. Empezar la Escuela por Pong cierra ese loop exacto: destilar sus fundamentos para que "hacé un Pong" traiga el baseline sin pedirlo.

Es la **primera misión de la Escuela** y llena el **primer libro** de la [[00_Biblioteca]] → estante [[00_Indice_juegos]] → [[01_Pong]]. Salida del [[01_Flujo_Mision_Estudio]] (rol: [[01_Bibliotecario]]).

---

## Pregunta de estudio (y cuándo se considera respondida)

¿Cuáles son las *table-stakes* y el *juice* de un Pong — lo que lo hace *ser* Pong y sentirse bien — de modo que la IA los traiga como baseline al pedir "hacé un Pong" (o una variante)?

Se considera **respondida** cuando el `EST` de Pong cubre, como mínimo:

- **Loop de experiencia:** input (paleta) → feedback (rebote) → objetivo (puntuar) → victoria/derrota.
- **Table-stakes:** lo que un Pong no puede NO tener para estar terminado (2 paletas, pelota con física de rebote, colisiones, puntaje, condición de fin, saque).
- **Juice / game feel:** lo que lo hace satisfactorio (feedback del golpe, ángulo según dónde pega, aceleración de la pelota, sonido/hit-stop, sensación de control de la paleta).
- **Definición de Terminado:** checklist para decir "este Pong está hecho", no "compila".

Cada punto reutilizable, citado y con aplicación + límites.

---

## Dedup contra el Core

**Alta nueva** (no existe entrada de experiencia para Pong ni módulo de Fundamentos de Experiencia). Si aparece solapamiento con notas de ingeniería del Core, se marca como *actualización* en vez de duplicar.

---

## Presupuesto de tokens (propuesta — a confirmar owner)

Misión acotada. Al ser Pong un caso chico y conocido, una sola corrida debería alcanzar para el `EST` completo. Propuesta: un puñado de fuentes (2–4) entre referencia del Pong original, material de game feel y un par de implementaciones de referencia, y a destilar.

> Nota: AiCare hoy *estima*, no *cuenta* tokens (pendiente en la bitácora). El presupuesto va como barra blanda + criterio del owner, no como corte duro automático.

---

## Barra de calidad (criterios de aceptación)

```txt
[x] Reutilizable: sirve de baseline para cualquier "hacé un Pong" o variante, no para uno solo
[x] Claro: se entiende como criterio por humanos e IAs (principio 8)
[x] Citado: cada fundamento con su fuente
[x] No verbatim: concepto destilado, nunca texto con copyright
[x] Con aplicación (qué trae la IA por default) y límites (cuándo NO)
[x] Incluye una Definición de Terminado accionable para un Pong
[x] No duplica el Core
```

---

## Estado AiCare

```txt
[x] ANTES — misión acotada a un caso (Pong); presupuesto blando fijado; contexto base = Core actual (sin módulo de experiencia).
[x] DURANTE — corrida única, sin búsqueda externa: se destiló sobre las fuentes ya catalogadas del estante (05, 13, 17, 18, 21, 06, 23, 08, 03, 09, 12) y sobre el Fundamento 05, ya en la Biblioteca.
[x] ANTES DE DESTILAR — sin material bruto que podar: el insumo ya estaba destilado en el estante de Fuentes.
[x] ANTES DEL HANDOFF — el libro no duplica el Fundamento 05: éste aporta los 9 pilares transversales, el libro de Pong aporta solo lo específico del género (table-stakes, baseline de parámetros, feel del impacto).
```

---

## Pipeline de la misión

```
[[01_Bibliotecario]]  → misión (este doc) ✔ gate superado
[[02_Investigador]]   → material citado del estante de Fuentes ✔ (sin salida externa: dedup contra lo ya catalogado)
[[03_Destilador]]     → [[01_Pong]] llenado ✔ (loop, 9 table-stakes, juice, baseline de parámetros, Definición de Terminado)
[[04_Validador_Estudio]] → barra + dedup + AiCare ✔ → pendiente handoff a Conocimiento
Área de Conocimiento  → commit → Owner → merge a main   ⟵ PENDIENTE (aprobación del owner)
```

---

## Cómo escala (por qué Pong primero)

Pong es la entrada 1. La misma plantilla se repite por cada tipo de experiencia (breakout, plataformero, shmup, etc.): cada uno un `EST`, cada uno una entrada de la librería. Se empieza por el más básico y mejor entendido para calibrar el formato del "libro" antes de casos más grandes.

---

## Resultado de la corrida

Libro [[01_Pong]] llenado en una sola corrida, sin búsqueda externa: el estante de Fuentes ya tenía catalogado todo lo necesario, así que la misión se resolvió destilando material propio de la Biblioteca. Estado del libro: **En validación** (a la espera del handoff a Conocimiento y la aprobación del owner).

Consumido primero por el [[TL-003_Pong3D_Unity6_Cadena_Completa]] — el primer timeline que carga este libro como insumo obligatorio del `RQ`. Ese es el cierre del loop que originó la Ley #1.

## Decisiones pendientes del owner

1. **Aprobación del libro:** OK para pasar [[01_Pong]] de *En validación* a *En la Biblioteca* vía handoff al Área de Conocimiento.
2. **Fundamento 01:** el libro de Pong aportó material para [[01_Loop_de_experiencia]] (loops anidados de segundos/punto/partida), que sigue *En estudio*. Definir si se actualiza ahora o en misión propia.

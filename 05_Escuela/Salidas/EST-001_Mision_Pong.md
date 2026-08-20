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
[ ] Reutilizable: sirve de baseline para cualquier "hacé un Pong" o variante, no para uno solo
[ ] Claro: se entiende como criterio por humanos e IAs (principio 8)
[ ] Citado: cada fundamento con su fuente
[ ] No verbatim: concepto destilado, nunca texto con copyright
[ ] Con aplicación (qué trae la IA por default) y límites (cuándo NO)
[ ] Incluye una Definición de Terminado accionable para un Pong
[ ] No duplica el Core
```

---

## Estado AiCare

```txt
[x] ANTES — misión acotada a un caso (Pong); presupuesto blando fijado; contexto base = Core actual (sin módulo de experiencia).
[ ] DURANTE — mide consumo en la investigación; corta si excede.
[ ] ANTES DE DESTILAR — poda material bruto (duplicados/ruido).
[ ] ANTES DEL HANDOFF — confirma que el EST no infla ni duplica el Core.
```

---

## Pipeline de la misión

```
[[01_Bibliotecario]]  → misión (este doc) ✔ gate superado
[[02_Investigador]]   → material bruto citado sobre Pong (mecánica + game feel)
[[03_Destilador]]     → EST: fundamentos de Pong (table-stakes + juice + def. de terminado)
[[04_Validador_Estudio]] → barra + dedup + AiCare → handoff a Conocimiento
Área de Conocimiento  → commit → Owner → merge a main
```

---

## Cómo escala (por qué Pong primero)

Pong es la entrada 1. La misma plantilla se repite por cada tipo de experiencia (breakout, plataformero, shmup, etc.): cada uno un `EST`, cada uno una entrada de la librería. Se empieza por el más básico y mejor entendido para calibrar el formato del "libro" antes de casos más grandes.

---

## Decisiones pendientes del owner

1. **Presupuesto:** confirmar el tamaño de la corrida (cuántas fuentes antes de destilar).
2. **Aprobación de arranque:** OK para que el Investigador salga a buscar material de Pong.

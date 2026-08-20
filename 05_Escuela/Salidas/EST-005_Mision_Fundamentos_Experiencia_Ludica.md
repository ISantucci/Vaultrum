## Misión (gap estudiado) + presupuesto usado

**EST-005 — Fundamentos de la buena experiencia lúdica (breadth-first) para el Área de Game Design.**

Tipo de misión: **destilación de marco (cross-source), orientada a experiencia**. Por pedido del owner: que Game Design tenga un **marco + checklist** para diseñar sistemas que se *sientan bien de jugar*, no solo funcionales. Mapear a lo ancho los nueve pilares (core loop/objetivos, victoria/derrota/fin, feedback/game feel, claridad/legibilidad, justicia/control, dificultad/tensión/flow, recompensa/motivación, ritmo/pacing, agencia/decisiones).

**Presupuesto:** 1 hora / una corrida. **Barra:** cubrir los nueve pilares a nivel fundamento + checklist accionable; **no** profundizar en balance fino ni géneros específicos.

**Presupuesto usado:** una pasada; sin búsqueda web (canon ya catalogado en EST-002/003 y destilado en EST-004). Materia prima = [[04_Playbook_de_diseno]] + 29 fuentes. Salida: 1 libro nuevo de Fundamentos.

---

## Fundamento / concepto destilado (reutilizable, claro)

Libro [[05_Fundamentos_de_experiencia_ludica]]: nueve pilares transversales, cada uno con *qué es / por qué importa / baseline / señales de que falla*, más un **CHECKLIST por-GDS** (36 ítems verificables) que Game Design corre en cada spec, y una lista de **misiones de profundización** (una por pilar).

Aporte propio frente al Playbook: reordena el canon por **lente de experiencia** (por qué se siente bien) en vez de por **función** (para qué sirve), y aterriza en un gate accionable por-GDS.

---

## Aplicación (cuándo y cómo lo usa la IA como baseline)

- **Game Design (primario):** corre la lente de los 9 pilares + el CHECKLIST por-GDS como gate antes de declarar un sistema "diseñado". Antídoto contra el "funciona pero no divierte".
- **Producción (RQ, secundario):** vara para que la primera entrega sea sólida (Ley #1), no una demo técnica.
- Cruza-referencia a [[01_Loop_de_experiencia]], [[02_Game_feel]], [[03_Definicion_de_terminado]] y [[04_Playbook_de_diseno]]: los usa, no los repite.

## Límites (cuándo NO aplica)

- Breadth-first a nivel fundamento: **no** cubre balance fino ni convenciones por género (eso son las misiones de profundización listadas en el libro).
- Los pilares entran en tensión entre sí; el checklist detecta huecos, no resuelve trade-offs.
- Ítems N/A son válidos **solo con justificación explícita** en el GDS (ej. sandbox sin victoria formal).

## Fuentes (citas)

Destilado sin verbatim de [[04_Playbook_de_diseno]] y de las fuentes del estante [[00_Indice_fuentes]]:
01 Rules of Play · 02 Art of Game Design · 03 Game Design Workshop · 04 Theory of Fun · 05 Game Feel · 06 Half-Real · 07 Characteristics of Games · 08 Designing Games · 09 Gamer's Brain · 10 Game Usability · 11 How Games Move Us · 12 Design of Everyday Things · 13 Elements of Game Design · 16 Advanced Game Design · 17 Uncertainty in Games · 18 Art of Failure · 19 Playful Production Process · 26 Cybertext.

## Dedup: ¿actualiza algo del Core o es nuevo?

**Alta nueva** en Fundamentos: [[05_Fundamentos_de_experiencia_ludica]]. No duplica al [[04_Playbook_de_diseno]] (lente de función) — lo cruza desde la lente de experiencia y agrega el gate por-GDS. No duplica a los stubs 01/02/03: los referencia como profundizaciones. No toca el Core.

## Estado AiCare (presupuesto, poda aplicada)

```txt
[x] ANTES — gap + presupuesto + barra claros; base medida = Playbook (04) + 29 fuentes ya catalogadas; sin recarga.
[x] DURANTE — sin búsqueda web nueva; una sola pasada; se reusa material ya destilado (no material bruto redundante).
[x] ANTES DE ESCRIBIR — poda: un principio por pilar; cruza-ref en lugar de repetir Fundamentos 01–04.
[x] ANTES DEL HANDOFF — 1 libro nuevo + 1 EST; no infla el contexto (el Core solo indexa; el peso vive en Biblioteca, on-demand).
```

## Handoff a Conocimiento

Candidato listo. La Escuela **no mergea**: el owner aprueba el handoff a Conocimiento, que versiona y propone el commit a `main`.

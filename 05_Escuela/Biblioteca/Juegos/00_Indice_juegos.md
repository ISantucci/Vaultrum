## Estante de Juegos

Un libro por juego/tipo, guardado por **género**. Cada libro son los fundamentos destilados de ese juego (table-stakes + juice + definición de terminado específicos), citados y reutilizables como baseline al pedir un juego de ese género.

Se apoya siempre en los `Fundamentos` transversales: el libro de Juego agrega lo *específico*, los Fundamentos aportan lo *común*.

---

## Registro (por género)

### [[01_Pong|Pong]]

Arcade · Paleta-y-pelota · EST-001 Mision Pong · En la Biblioteca

### [[02_Plataformero_2D|Plataformero 2D]]

Plataformas · Plataformero 2D de precision · EST-010 Mision Plataformero 2D · En la Biblioteca

### [[04_Tower_Defense|Tower Defense]]

Estrategia · Tower defense de colocación libre y cámara fija; economía de la partida y balance con bots (EST-018) · EST-018 Mision Balance Tower Defense · En la Biblioteca

### [[05_Endless_runner|Endless runner]]

Arcade · Endless runner lateral (auto-run, un carril, un golpe); la curva de velocidad como curva de dificultad, huecos derivados del salto y alturas por verbo; calibrado contra el Dino corriendo, con la síncopa legible (EST-021) · EST-021 Mision Chrome Dino jugado · En validación

### [[06_Contrarreloj|Contrarreloj]]

Arcade · Contrarreloj — el reloj como rival: cuenta regresiva, time trial y duración fija; medallas, splits y ghosts · EST-019 Mision Endless runner y contrarreloj · En validación


### [[07_Stealth|Stealth]]

Sigilo · Sigilo top-down 2D con conos de visión, estados de alerta y evasión; detección gradual y legibilidad del sistema (Metal Gear) · EST-022 Mision Lote Juegos Web y Sigilo · En validación

### [[08_Rhythm_tap|Rhythm tap]]

Ritmo · Rhythm tap de carriles (Piano Tiles): ventanas de acierto, relación entre velocidad de caída y cadencia, latencia de audio en la web · EST-022 Mision Lote Juegos Web y Sigilo · En validación

### [[09_Snake|Snake]]

Arcade · Snake de grilla por ticks: input buffering y giro de 180°, comida, muros o wrap, desgaste; densidad y largo como dificultad · EST-022 Mision Lote Juegos Web y Sigilo · En validación

### [[10_2048|2048]]

Puzzle · Puzzle de fusión por deslizamiento en grilla (2048, Threes): reglas de movimiento y fusión, spawn, victoria y game over · EST-022 Mision Lote Juegos Web y Sigilo · En validación

### [[11_Wordle|Wordle]]

Puzzle · Puzzle de palabras diario con feedback por letra: regla de colores con letras repetidas, un intento por día, compartir sin spoilers · EST-022 Mision Lote Juegos Web y Sigilo · En validación

### [[12_Tetris|Tetris]]

Puzzle · Puzzle de piezas que caen: aleatorizador por bolsa, gravedad por nivel, lock delay, rotación, DAS · EST-022 Mision Lote Juegos Web y Sigilo · En validación

---

## Regla

- Se numera correlativo por estante (01, 02, ...).
- **Género y tipo son obligatorios**: es la clave por la que Producción/Game Design encuentran el libro.
- Estados: En estudio / En destilación / En validación / En la Biblioteca / A actualizar.
- Un libro se **actualiza**, no se duplica. Si un nuevo estudio toca uno existente, edita el libro.
- Un libro pasa a "En la Biblioteca" tras handoff a Conocimiento + aprobación del owner.

---

## Nota de gobernanza (cerrada)

`01_Pong` estuvo *En validación* mientras ya se usaba como insumo de producción en `TL-003` — un libro sin aprobar alimentando una entrega real. El hueco se cerró: handoff a Conocimiento hecho, aprobación del owner registrada, y el libro pasó a **En la Biblioteca**.

Regla que queda: **si un libro se usa como insumo de un `RQ`, tiene que estar en estado *En la Biblioteca*.** Un libro *En estudio* o *En validación* no es insumo válido — es material en curso. Producción lo verifica en su gate de insumo.

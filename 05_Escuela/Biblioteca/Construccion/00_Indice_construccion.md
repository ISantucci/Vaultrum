## Estante de Construcción

**Cómo se construye técnicamente un juego.** Los otros estantes responden por la experiencia: qué la hace *ser* una experiencia (`Fundamentos`), qué pide cada género (`Juegos`), qué dijo el mundo (`Fuentes`), cómo lo resolvió alguien de verdad (`Documentos`). Este responde por el **mecanismo**: qué es un paso fijo, qué hace un quaternion, por qué una colisión se resuelve por eje.

---

## La frontera con el Core, en una línea

> El Core ya tiene el **precio** de todo y el **mecanismo** de nada.

`Física costosa` dice cuánto sale la física por frame y qué hacer cuando sale de más. Ninguna nota del Core dice qué es un integrador. `Costo de fragmentos y shaders` dice qué pagás por un shader; ninguna dice cómo corre el pipeline. `Game loop` lo declara literalmente en su propio cuerpo: *"no existe para documentar el orden interno del motor"*.

```txt
CORE           qué decido      cuánto del frame, cuándo A y no B, qué rechazo
CONSTRUCCIÓN   cómo funciona   el mecanismo que esa decisión da por sabido
DOCUMENTOS     qué dice el fabricante   ficha + URL + licencia, nunca alojado
```

Los libros de este estante **remiten** al Core con backticks y no lo re-legislan. La dirección es una sola: el libro nombra al Core; el Core no aprende del libro. Que algo de acá se promueva a criterio propio del Core lo decide Conocimiento con aprobación del owner.

Emplazamiento y razón completos: `ARQ-022_La_frontera_del_material_tecnico`.

---

## Quién lo consulta

**Programación**, al escribir el `SOL` — después de que el `GDS` cerró, contra otro insumo y en otro momento que los Fundamentos.

```txt
Fundamentos    lo consulta Game Design    ANTES de cerrar el GDS
Construcción   lo consulta Programación   DESPUES, al escribir el SOL
```

Regla de carga: se jala el libro puntual, nunca el estante entero. Medido, no supuesto:

```txt
el puente del Core + UN libro          9.6k  =  24% de un presupuesto de 40k   COMODO
el puente + el estante entero         20.3k  =  51%                            COMODO
(para comparar: los 12 Fundamentos del lote EST-006, juntos, dan 53.2k = 133%  EXCEDIDO)
conteo: aproximado (heuristica es-markdown, +-12%)
```

Este estante entra entero y el de Fundamentos no, y la razón es aritmética: tres libros contra diecisiete. **Eso deja de ser cierto alrededor del séptimo libro** — cuando el estante crezca, la regla del libro puntual pasa a ser obligatoria acá también. Se vuelve a medir antes de agregar el cuarto.

---

## Registro

### [[01_Bucle_de_simulacion|Bucle de simulacion]]

paso fijo con acumulador, la relación Hz–ventana–techo, interpolación de render, espiral de la muerte, determinismo · EST-012 Mision Bucle de simulacion · En la Biblioteca

### [[02_Colision_y_consulta_espacial|Colision y consulta espacial]]

por qué se resuelve por eje, barrido contra tunneling, la relación velocidad–tamaño–paso, raycast como consulta y sus modos de fallar · EST-013 Mision Colision y consulta espacial · En la Biblioteca

### [[03_Matematica_del_movimiento|Matematica del movimiento]]

vectores como intención, normalización y sus trampas, lerp y su dependencia del framerate, easing, curvas, ruido con semilla · EST-014 Mision Matematica del movimiento · En la Biblioteca

---

## Regla

- Numeración correlativa por estante (01, 02, ...).
- Estados: Reservado / En estudio / En destilación / En validación / En la Biblioteca / A actualizar.
- Los libros de Construcción **no** llevan `genero` (son transversales al género y específicos del oficio).
- Cada libro declara en frontmatter `remite:` — qué notas del Core toca y no re-legisla.
- Se **actualizan**, no se duplican.
- Un libro que solo se puede leer con el manual del fabricante al lado no es un libro de este estante: es una ficha de `Documentación real`.

---

## Territorio pendiente

El mapa completo del territorio faltante, con su prioridad y lo que desbloquea cada pieza, vive en `EST-011_Mision_Mapa_Territorio_Tecnico`. Lo que sigue, en orden medido: animación (cero notas en todo el vault), datos y saves, herramientas de editor, netcode, arte técnico del lado del mecanismo, audio técnico, build y release, y las fichas de manuales oficiales.

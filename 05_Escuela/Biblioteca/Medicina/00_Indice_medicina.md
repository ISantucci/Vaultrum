## Estante de Medicina

**El cuerpo humano que el juego anima, modela y riggea.** La primera rama es la **morfología del movimiento**: cómo está armado el cuerpo para moverse, qué proporciones tiene, dónde está su peso y cómo camina, corre, salta y lanza.

No es un estante de diseño: no dice qué se siente bien. Es el mecanismo real que una herramienta necesita para no inventar. Cuando un encargo de animación pide una caminata, la regla de oficio sale de Arte (`RA-011_Locomocion_por_apoyos`); los números y el porqué salen de acá.

---

## Quién lo consulta

**Arte, solo cuando anima, riggea o modela una persona o un humanoide**, y solo el libro de lo que está haciendo. Un objeto, un efecto o una interfaz no abren este estante. Cargarlo entero por las dudas es exactamente el costo que la regla del libro puntual existe para evitar.

```txt
encargo de animación de una caminata   → Marcha humana
de una carrera                         → Carrera
de un salto                            → Salto y aterrizaje
de un golpe, un lanzamiento, una patada → Cadena cinética
hoja de referencia, escala, modelado   → Proporciones del cuerpo
rig, límites de articulación, skinning → Anatomía del movimiento
pose con peso: idle, cargar, empujar   → Masa, centro de masa y equilibrio
```

---

## Registro

### [[01_Anatomia_del_movimiento|Anatomía del movimiento]]

Cuánto gira cada articulación y sobre qué eje; límites de rig desde la pose de reposo y prueba de poses · `EST-024` · En la Biblioteca

### [[02_Proporciones_del_cuerpo|Proporciones del cuerpo]]

Alturas y largos como fracción de la estatura, por sexo; dónde va cada articulación del rig; qué se conserva al estilizar · `EST-024` · En la Biblioteca

### [[03_Masa_centro_de_masa_y_equilibrio|Masa, centro de masa y equilibrio]]

Dónde está el peso, cuándo una pose se sostiene, cuánto se inclina el cuerpo para empujar o cargar y cuánto tarda en caer · `EST-024` · En la Biblioteca

### [[04_Marcha_humana|Marcha humana]]

El ciclo de la caminata en porcentajes y cuadros: doble apoyo, rebote, pies en el sprite y en el mundo, cambio con la velocidad y el tamaño · `EST-024` · En la Biblioteca

### [[05_Carrera|Carrera]]

Qué hace que se lea carrera: vuelo, apoyo corto, rodilla flexionada; zancada contra cadencia, cuadros por velocidad, arranque según el juego · `EST-024` · En la Biblioteca

### [[06_Salto_y_aterrizaje|Salto y aterrizaje]]

Fases y tiempos del salto real, la física que el juego invierte, clips separados y aterrizaje blando o rígido · `EST-024` · En la Biblioteca

### [[07_Cadena_cinetica|Cadena cinética]]

El orden pelvis → tronco → brazo → mano en lanzar, golpear y patear, en porcentajes y cuadros; el daño como evento de Game Design · `EST-024` · En la Biblioteca

---

## Regla

- Numeración correlativa (01, 02, ...). Estados: Reservado / En estudio / En destilación / En validación / En la Biblioteca / A actualizar.
- Cada libro sigue el contrato `MED` del Documentador (`contratos.txt`): qué decisión sostiene, modelo, parámetros con fuente en cada fila, relaciones, estilización, medible y juicio, al encargo, límites y fuentes.
- Cada libro declara en frontmatter `consume:` (quién lo carga y cuándo), `remite:` (las notas del Core o de un área que sostiene y no re-legisla) y `cruza:` (los otros libros del estante que da por sabidos).
- **Un número sin fuente no entra.** Un número real que rompe a un personaje estilizado tampoco: por eso la sección de estilización es obligatoria.
- Las fuentes externas van a `Fuentes`; las bases de datos y documentos primarios, a `Documentación real`. El libro las nombra con backticks.
- Se actualizan, no se duplican.

---

## Territorio pendiente

Lo que la primera rama deja afuera a propósito, para que nadie lo supla de memoria: manos y agarre, rostro y expresión, cargar y arrastrar objetos, cuerpos que no son el adulto de referencia (niños, ancianos, patologías de la marcha) y cuadrúpedos.

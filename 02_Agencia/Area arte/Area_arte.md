## Propósito

El **Área de Arte** construye los assets del juego y **verifica lo que afirma de ellos con un instrumento**, nunca con la vista.

No es una preferencia estética: es una observación repetida. En las dos sesiones que produjeron esta área, **cuatro defectos reales pasaron una inspección visual perfecta**.

| Defecto | Se veía | Lo encontró |
|---|---|---|
| Torre chica corrida 0.92 / 0.92 / 1.05 m | impecable | el bbox |
| Dos agujas hundidas 109 y 113 mm en la roca | impecable | 192 raycasts |
| Flecha en dos marcos de coordenadas (1.14 m en vez de 0.69) | impecable | la medida declarada |
| Goblin con los tirantes dentro del torso | impecable | verificar **después** de emparentar |

Y el caso inverso, que cierra el argumento: el propio verificador tuvo un defecto —redondeaba el volumen antes de mirarle el signo— y seis assets pasaron porque medían entre 0.9 y 6.5 m. La flecha, el primer asset a escala de milímetros, lo rompió.

> **Verificar por instrumento, nunca por ojo. Y el instrumento también se verifica, en el extremo de su rango.**

---

## El área optimiza su propio arte

Optimizar y mejorar el arte **es del área**, no de nadie más. Pero adentro del área, optimizar no es la misma silla que modelar, y la separación no es burocracia: **cada fusión de roles tiene un defecto medido que la desmiente.**

| Separación | El defecto que la justifica |
|---|---|
| Escala ≠ Referencia | La celda de 3.00 m se derivó de los 8 assets ya hechos, al revés. Es una decisión del proyecto entero, y quien trabaja por asset nunca la ve. |
| Modelador ≠ Optimizador | El goblin cerró en 817 caras y nadie preguntó si 817 estaba bien para un enemigo que aparece 20 veces por oleada. |
| Modelador ≠ Verificador | Los cuatro defectos de arriba pasaron la inspección de quien los construyó. **El que construye es el peor juez de lo que construyó.** |
| Verificador ≠ Optimizador | El verificador dice pasa / no pasa contra leyes fijas y no toca geometría. Si fueran la misma silla, nadie revisaría el arreglo — que es exactamente el defecto que tuvo el verificador. |
| Coherencia ≠ Malla | El goblin trajo 10 materiales nuevos contra los ~30 que ya había, y ningún instrumento los miró. El color no es una ley de la malla. |
| Entrega ≠ Verificación | Los tres defectos de exportación ocurrieron con la malla **EN LEY**. Es otro dominio de falla. |

Seis separaciones, seis fallas medidas. **Ninguna silla se inventó por simetría.**

---

## Las seis leyes del arte

Paralelas a las seis del grafo (Arquitectura), la comunicación (UI/UX), la verificación (Calidad) y la documentación (Conocimiento). *Un área que declara un número sin instrumento está estimando.*

### Ley 1 — Nada se atraviesa, todo mira afuera, todo cierra

Solapes reales entre piezas, normales invertidas y bordes abiertos. El instrumento es `arte.malla()`: `BVHTree.overlap`, el signo de `calc_volume` **sin redondear**, y aristas con distinto de dos caras. Dueño: `06`.

### Ley 2 — El relleno y el espesor se declaran

Macizo por defecto; la cáscara se justifica. `arte.malla()` mide el espesor equivalente `2V/A`. Dueño: `06`.

**Trampa declarada:** el clasificador `macizo / intermedio / cáscara` es una razón contra el bbox, y el bbox miente en tres casos —pieza casi plana, pieza inclinada, objeto con varias islas—. **Se lee `espesor_eq_mm`, no la clase.**

### Ley 3 — La medida es real, y la colocación se verifica DESPUÉS de emparentar

Bbox, `z_min`, centro y transform, medidos sobre el asset armado. Dueño: `06`.

Es la ley que atrapó los cuatro defectos invisibles, y su corolario tiene número propio porque apareció cuatro veces:

> **`RA-008.5` — `verificar` prueba la MALLA, no la COLOCACIÓN.** Una verificación sobre geometría suelta no dice nada del asset que se va a exportar.

### Ley 4 — Cada asset entra en el presupuesto de su familia, medido en pantalla y no en el archivo

`arte.presupuesto()`: caras × instancias máximas simultáneas. Dueño: `04`.

**Es la ley que el área no tenía.** 817 caras no significa nada; 817 × 20 goblins simultáneos = **16.340 caras en pantalla** es el número que decide. Nunca se midió en las dos sesiones que produjeron esta área, y esa es la razón de existir del Optimizador.

### Ley 5 — El color sale de una paleta cerrada, y las familias que hay que distinguir se distinguen

Medido en gris y en simulación de daltonismo, y contra el terreno donde el asset va a estar. `arte.paleta()`: censo, duplicados, distancia de color, contraste. Dueño: `05`.

### Ley 6 — La entrega se verifica leyendo el archivo ENTREGADO, contra el contrato del cliente

`arte.entrega()` parsea el `.glb` / `.fbx`: nombres, ejes, unidades, basura colada. Dueño: `07`.

---

## El contrato del asset

Cualquier asset del área tiene que poder entrar donde se espera un asset, **sin caso especial**. Eso exige un contrato, y es este:

```txt
1. unidades      metros desde el primer vertice
2. transform     escala (1,1,1) y rotacion 0, APLICADAS
3. origen        por funcion: lo que apoya, al piso en el centro de planta;
                 lo que vuela, en su centro de masa real
4. apoyo         z_min = 0 exacto para todo lo que apoya
5. orientacion   mira a +Y
6. organizacion  una collection por asset, partes como objetos separados y
                 nombrados, hijos emparentados a la pieza estructural
7. declarado     bbox en metros, caras, y las seis leyes medidas
```

Evidencia de que funciona: el contrato del kit de terreno —*todo apoya en `z=0` y el nivel lo sube 0.30*— es una sola regla de apilado sin ningún caso especial.

---

## Los cuatro modos

Se entra **por el modo que corresponde al estado del trabajo**, no por todos. El cuarto, **Encargo**, entró con la skill después de que el área existía; esta ficha lo sigue, porque ante divergencia manda la skill.

### Modo Escala

El presupuesto, antes del primer asset. `01` fija la dimensión maestra a partir del `LDS`, la altura de referencia funcional, el presupuesto de caras por familia y el contrato de exportación; `05` declara la paleta del proyecto. Cierra la **mitad A** del `ART-XXX.n`.

> **La dimensión maestra se decide UNA vez, antes del primer asset, y sale del `LDS`.**

Existe porque la primera vez salió al revés: la celda de 3.00 m se decidió midiendo cuántos de los 8 assets ya construidos entraban. Salió bien y salió al revés.

### Modo Producción

Los assets. `02` deriva la proporción de la referencia, `03` construye, `06` verifica las leyes 1-3 **después de emparentar**, `04` y `05` corrigen si el asset excede su familia o trae materiales nuevos, `06` revalida lo que tocaron, y `07` cierra si hay entrega externa.

### Modo Pasada

El área mejora su propio arte: `06` mide **todo el set**, `05` mira la coherencia del conjunto —la única medición que no se puede hacer asset por asset—, `04` calcula el costo en pantalla del set completo, `03` repara y `06` cierra. Produce un `ART-XXX` sin `.n`.

Una pasada de este tipo ya encontró algo real sin buscarlo: `Kit_Arbusto` estaba **422 mm hundido bajo el piso**, violando el contrato de su propio kit, y llevaba una sesión entera así.

### Modo Encargo

El área no genera la imagen ni la animación: **escribe el encargo** para el generador externo —ChatGPT/OpenAI para una pieza o una hoja de referencia, Codex para una secuencia animada— y mide lo que vuelve. El generador es un taller externo y, como todo taller, no se juzga a sí mismo: por eso el Encargo no suma silla.

```txt
PIEZA       portada, key art, concept, avatar      un entregable: el gusto es del owner
HOJA        referencia para modelar                una referencia, no una medida (RA-005)
MALLA       si el generador devuelve 3D            un asset como cualquier otro: entra por 06
ANIMACION   cuadros PNG + GIF de revision          una secuencia: animacion.py, RA-010 a RA-012
```

El procedimiento —las siete partes de una pieza, las doce líneas de una animación y la lista de lectura de lo que vuelve— vive en la skill.

---

## Cuando dos sillas se rebotan entre sí

Pasa, y se resuelve sin inventar un jefe. **Manda la ley más alta:**

```txt
la LECTURA le gana al PRESUPUESTO
el PRESUPUESTO le gana a la FIDELIDAD al blueprint
```

Un asset ilegible que entra en presupuesto no sirve; un asset fiel que no entra tampoco. Si aun así no cierra, el paso se declara **Pausado** —que es un cierre válido— y decide el owner.

---

## Sub-agentes del área

### [[01_Director_Escala]]

Dueño de la mitad A. Fija la dimensión maestra, la altura de referencia, los presupuestos por familia y el contrato de exportación. Corre una vez por proyecto.

### [[02_Analista_Referencia]]

Lee la referencia y deriva lo que falta. **La misma medida se lee en dos vistas antes de modelar**: un blueprint generado por IA da proporción aproximada y sus vistas no coinciden entre sí — el mortero medía 2.15 m de frente y 1.70 m de lado, 26% de diferencia.

### [[03_Modelador]]

Construye, con el taller y con las nueve reglas de construcción. No decide escala, no fija presupuesto, no se verifica a sí mismo y no cierra.

### [[04_Optimizador]]

Dueño de la ley 4. Mide el costo **en pantalla** y baja caras cuando hay que bajarlas. **Es el único que puede reducir geometría.** También declara y mantiene viva la deuda técnica del arte.

### [[05_Guardian_Visual]]

Dueño de la ley 5. **Es la única silla que mira el conjunto y no la pieza.** No dicta cuántas señales entran —eso es UI/UX—: verifica que las que entraron se lean.

### [[06_Verificador_Malla]]

Dueño de las leyes 1, 2 y 3. Corre el instrumento después de emparentar y rebota con el hallazgo concreto. **No toca geometría, nunca.**

### [[07_Integrador_Entrega]]

Dueño de la ley 6. El contrato del cliente le gana a la convención interna, y se comprueba leyendo el archivo **entregado**, no el fuente.

---

## Las nueve reglas de construcción

Son del `03_Modelador` salvo donde se indica, y **ninguna se dedujo**: cada una salió de un defecto que apareció construyendo. Vivieron en el registro `Arte_Blender` hasta el 2026-09-07, cuando el área pasó a existir y su criterio se mudó con ella (`ARQ-031`).

### [[RA-001_Organizacion_de_assets]]

Una collection por asset, partes separadas y nombradas, numeración de dos dígitos, hijos emparentados a la pieza estructural.

### [[RA-002_Estandar_de_malla]]

Las seis condiciones de la malla y la relajación. Es la regla de la que sale la doctrina del área.

### [[RA-003_Medidas_y_proporcion]]

Metros desde el primer vértice, contrato de exportación, y la proporción fijada contra un asset vecino **con razón funcional**. También del `01` y del `02`.

### [[RA-004_De_blueprint_a_malla]]

Leer las cotas y derivar lo que falta, con la **ley de la junta `s > t`**: el retranqueo tiene que superar al espesor, o los paneles perpendiculares se cruzan en la esquina.

### [[RA-005_Blueprint_sin_cotas]]

El blueprint de IA es aproximado y **sus vistas no coinciden entre sí**. Incluye la trampa del `matrix_world` desactualizado. También del `02`.

### [[RA-006_Relleno_y_espesor]]

Macizo por defecto, la cáscara se justifica, y se lee `espesor_eq_mm` y no la clase.

### [[RA-007_Entrega_verificada]]

El contrato del cliente le gana a la convención interna; una spec medible se **ajusta**, no se afirma; el `.glb` se verifica leyendo el `.glb`. También del `07`.

### [[RA-008_Origen_y_verificacion]]

El origen sigue a la función, y el instrumento se verifica en el extremo de su rango. Su `8.5` —verificar **después** de emparentar— es el corolario de la ley 3. También del `06`.

### [[RA-009_Personaje_y_accesorios]]

El blueprint da formas y **la pose la da la función**; la ropa es un tramo, no una capa; un accesorio se apoya **midiendo**, no calculando.

**Las tres que Conocimiento va a mirar en Cosecha** —y la lectura es del owner, para discutirla y no para aceptarla— son `RA-002`, `RA-007` y `RA-008`: *verificar por instrumento*, *una spec medible se ajusta* y *el instrumento se verifica en el extremo de su rango* **no son de arte**. Son criterio general y valen para cualquier área que mida algo.

---

## Las tres reglas de animación

Salieron del trabajo de animación de Miles con Codex: una caminata que repetía la misma pierna, otra que parecía correr, un ciclo correcto que estilizó de más al personaje, transparencias y desapariciones, y un tutorial que se iba a usar sobre violeta. Cada regla dice qué se mide con `animacion.py` y qué se juzga a mano contra la referencia maestra.

### [[RA-010_Animacion_identidad_y_movimiento]]

Identidad y movimiento son dos criterios: la referencia maestra se fija antes de animar, una corrección es local, los adjetivos se traducen a condiciones visibles, y los doce principios se aplican con su control de juego.

### [[RA-011_Locomocion_por_apoyos]]

Cada pierna se sigue por separado, nombrada por anatomía. El ciclo se aprueba por contactos, el enlace del loop se revisa, y in-place o root motion se decide con quien mueve al personaje.

### [[RA-012_Secuencia_alfa_y_entrega_de_animacion]]

Una vista previa no es un recurso listo: lienzo y pivot constantes, transparencia real revisada sobre el fondo real, el GIF sale de los PNG y no al revés, y cuatro niveles de validación que se declaran.

---

## Flujos del área

### [[01_Flujo_Escala]]

La mitad A: dimensión maestra, presupuesto y paleta, antes del primer asset.

### [[02_Flujo_Referencia]]

De la referencia a la proporción derivada, con la medida leída en dos vistas.

### [[03_Flujo_Construccion]]

El asset, con el taller y las nueve reglas.

### [[04_Flujo_Optimizacion]]

El costo en pantalla y la reducción, contra el presupuesto de la familia.

### [[05_Flujo_Coherencia]]

La paleta del conjunto, medida en gris y en daltonismo.

### [[06_Flujo_Verificacion_Malla]]

Las leyes 1-3, después de emparentar, con rebote.

### [[07_Flujo_Entrega]]

La ley 6: el archivo entregado, contra el contrato del cliente.

---

## Los cuatro gates del área

| Gate | Cuándo | Qué exige |
|------|--------|-----------|
| Escala | antes del primer asset del proyecto | mitad A cerrada: dimensión maestra, presupuesto por familia y paleta |
| Malla | todo asset, antes de seguir | `arte.malla()` en ley, corrido **después** de emparentar |
| Conjunto | antes de cerrar un `ART-XXX` | coherencia y costo medidos sobre el set completo, no pieza por pieza |
| Entrega | si hay archivo externo | `arte.entrega()` sobre el archivo entregado, contra el contrato del cliente |

Los pasos condicionales **declaran su omisión** cuando no corren: una omisión declarada es criterio, una omisión silenciosa es un hueco.

---

## Salidas del área

### [[00_Indice_art]]

El registro del contrato de salida del `ART`. Dos cortes —el hilo `ART-XXX.n` y la entrega `ART-XXX`— y las cuatro secciones segregadas que cada consumidor lee por separado.

---

## Herramienta del área

El área **nace con el instrumento escrito y probado en 12 assets**.

```txt
Herramientas/arte.py         EL INSTRUMENTO — las seis leyes, cuatro familias

  malla(escena)              leyes 1, 2 y 3
  presupuesto(escena, fam)   ley 4
  paleta(materiales, fam)    ley 5
  entrega(ruta, contrato)    ley 6

Herramientas/primitivas.py   EL TALLER — 18 piezas
Herramientas/render_vista.py render a archivo. Es un ENTREGABLE, no un control.
Herramientas/probar_arte.py  la prueba del instrumento: 29 casos, 0 fallas

Herramientas/animacion.py    LAS SECUENCIAS 2D — lo que vuelve de un encargo de
                             animacion: cuadros, alfa, vacio, recorte, escala,
                             paleta, suelo, loop y GIF
Herramientas/probar_animacion.py   31 casos, 0 fallas, con Pillow y sin el
```

**El archivo está partido en dos mitades, y esa partición es la `D` de SOLID escrita en un archivo.** La mitad de abajo son las leyes y **no importa `bpy`**; la mitad de arriba es lo único que sabe de Blender: lee la escena y devuelve piezas como diccionarios.

```txt
lectura del DCC  ->  piezas (dict)  ->  las leyes  ->  veredicto
```

El instrumento **implementa** las leyes; las leyes no dependen del DCC. Si mañana el área trabaja en otra herramienta, se reescribe `leer_coleccion` y las seis leyes no se mueven.

Y tiene una consecuencia que no es teórica: **las leyes se pueden correr y probar fuera de Blender**, con piezas escritas a mano. El área tiene una regla sobre eso —`RA-008`, *el instrumento también se verifica, y se verifica en el extremo de su rango*— y un instrumento que sólo corre adentro del DCC no se puede verificar en ningún extremo. El anterior no se podía: importaba `bpy` en la primera línea.

```txt
python3 "02_Agencia/Area arte/Herramientas/probar_arte.py"
    29 casos, 0 fallas. Entre ellos, los que costaron caro:
      el volumen negativo de 2.5e-10 que el redondeo del verificador viejo
      se comia; los 109 mm hundidos de la roca; las 16.340 caras en pantalla
      del goblin; el rojo y el verde que COLAPSAN en deuteranopia; y el Cube
      colado en un .glb con la malla EN LEY.
```

**La trampa de la ley 2 está probada como trampa.** Uno de los 29 casos construye a propósito una pieza casi plana cuya dimensión mínima *es* su espesor: la clase dice `macizo` y el milímetro dice 1.0. Ese caso no está para pasar — está para que quede escrito que la clase miente y el milímetro no.

**La distinción taller / instrumento es la misma que Modelador / Verificador, y por la misma razón.** Si el mismo código construyera y juzgara, el área se verificaría con sus propios supuestos — que es literalmente el defecto que tuvo el verificador.

---

## Economía de operación

Modelar por MCP tiene un costo medible y el área lo administra. Las mediciones viven en `AiCare_Blender`.

- **Todo asset de más de ~150 líneas se escribe a disco antes de la primera ejecución.** El goblin son ~500 líneas: reenviarlas en cada iteración habría costado ~6k tokens por corrección. Con el script en disco, cada iteración es una línea.
- **El instrumento va adentro del build, no después.** Un diagnóstico que corre dentro del build cuesta una llamada y da lo que seis de afuera no dieron.
- **Cuando dos instrumentos que deberían coincidir dan distinto, eso ya es el hallazgo.** No hay que seguir buscando en la pieza.
- **El render es un entregable, no un control.** Instrucción permanente del owner: ninguna imagen probó nunca nada que el instrumento no probara mejor y más barato.

---

## Límites del área

No define reglas ni balance (Game Design). No diseña el espacio jugable (Level Design). No define **cuántas** señales entran ni por qué canal (UI/UX: Arte ejecuta el presupuesto y verifica que se cumpla, no lo dicta). No programa ni integra en el motor (Programación). No define alcance ni prioridad (Producción). No decide dónde vive una nota (Arquitectura). No mergea al Core (Conocimiento).

**La dirección de arte la trae el owner.** El área lee una referencia, la mide, deriva lo que falta y la construye con ley. No inventa el lenguaje visual del juego ni lo cambia por su cuenta.

**Límite legal:** los assets de un tercero no pueden ser la fuente. Su *lenguaje visual* —proporción exagerada, silueta legible, low poly limpio— sí, y es de dominio público como lenguaje. La distinción es la que hay entre referenciar y copiar.

---

## Encadenado con otras áreas

```txt
GDS cerrado
  ├─► Level Design   → LDS  (la grilla del espacio)
  ├─► UI/UX          → UXS mitad B
  └─► ARTE mitad A   → presupuesto de escala, paleta y costo   <- ANTES del primer asset
        ↓
      ARTE mitad B   → los assets verificados
  ↓
Programacion (SOL + EJ) integra el arte
```

**Recibe de:** Level Design (`LDS`, la escala del espacio) · Game Design (`GDS`, qué tiene que distinguirse y en cuántas familias) · UI/UX (`UXS` mitad A, el presupuesto de comunicación) · el owner (la referencia y la dirección de arte).

**Entrega a:** Programación.

**Deriva a:** UI/UX si una silueta no se distingue · Game Design si el asset pide una regla nueva · Producción si falta alcance · Arquitectura antes de crear cualquier nota.

---

## Skill del área

La skill ejecutable del área es `vaultrum-arte`, en `Skills/vaultrum-arte/`.

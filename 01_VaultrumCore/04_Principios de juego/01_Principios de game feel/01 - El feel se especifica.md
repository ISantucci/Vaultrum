## Definición

**El feel se especifica**: el feel de un sistema se declara en su `GDS` antes de implementarse. Qué se maneja y qué cree el jugador que es, qué está en juego cuando se mueve, cómo acelera y frena, qué perdona el input, y qué efecto confirma cada evento, con su ventana y su techo.

---

## Idea central

El feel no es una fase de pulido: es diseño, y tiene dueño. Cuando nadie lo escribe, lo inventa el que programa, y lo inventa como lista de efectos.

```txt
especificado     cada efecto tiene evento, oracion, ventana y techo. Se puede afinar,
                 probar y discutir, porque hay un numero de cada cosa
no especificado  una lista de efectos sin relacion entre si. No se puede afinar, porque
                 no hay contra que comparar, y nadie sabe si esta bien
```

Un `GDS` que dice *"que se sienta bien"*, *"que tenga juice"* o *"que sea satisfactorio"* sin nombrar capa, efecto y ventana no declaró nada. Dejó la decisión para el último eslabón de la cadena, que es el que menos contexto tiene.

---

## Especificación en Unity

La sección de feel de un `GDS` tiene cinco partes, y ninguna se omite sin decir por qué no aplica:

```txt
metafora      que es lo que se mueve, y en que grado: real, iconico o abstracto
reglas bajas  lo que cambia el movimiento de un momento a otro: dano, estados,
              invulnerabilidad, tiempos
sobre         ataque, sostenido y liberacion en segundos; velocidad maxima en unidades/s
perdon        coyote, buffer, asistencias, en cuadros o ms
efectos       evento | efecto | que afirma | ventana | techo | eventos por minuto
```

En el proyecto, esas cinco partes se vuelven datos y no código:

```txt
un lugar      cada parametro de feel vive en un ScriptableObject o en campos serializados,
              editable sin tocar codigo (04_Proyecto_editable_en_Unity)
un evento     cada fila de la tabla de efectos es un evento de gameplay (evento C# o
              UnityEvent). El feel se suscribe; el gameplay nunca llama a un efecto.
              El acuse de la accion no es de esta tabla: es capa 1, vive en el
              controlador y la animacion, y sale del evento "accion iniciada"
un apagado    sacar el modulo de feel no rompe el juego: los eventos se emiten igual
```

---

## Quién lo aplica

```txt
Produccion     un requerimiento de feel es jugable: pasa por Game Design, nunca directo
               a Programacion
Game Design    escribe la seccion. El Validador de Diseno rebota un GDS sin ella
Programacion   si recibe un efecto sin ventana o sin techo, no lo inventa: lo devuelve
```

---

## Cómo se juzga

```txt
se mide     cada evento del GDS tiene su fila con los seis campos, y cada efecto del codigo
            tiene su fila en el GDS (en los dos sentidos). Ningun parametro de feel escrito
            como literal en un script
se juzga    si la metafora elegida es la que el juego necesita
```

---

## Errores comunes

```txt
El feel como requerimiento de Programacion.
El feel como la ultima epica, "cuando ande todo".
Parametros de movimiento escritos como numeros sueltos en el codigo.
Un efecto que existe en el juego y no en el GDS.
"Que se sienta como X" sin decir que de X: el sobre, los efectos o la camara.
```

---

## Ejemplo en videojuegos

Un salto, especificado:

```txt
metafora      iconica: un personaje, no una pelota
reglas bajas  caer en un pozo o tocar un pincho cuesta el intento
sobre         horizontal: ataque al 90% en 0.15 s, liberacion 0.1 s, 8 u/s; vertical:
              despega en el cuadro del input, altura segun cuanto se sostiene el boton
perdon        coyote 100 ms, buffer 133 ms, una sola accion en cola
efectos       despegue | estiramiento + 3 particulas | despegue, con impulso | 80 ms |
                no se acumula | ~20/min
              aterrizaje de alto | compresion fuerte + 5 particulas | cai de alto, y el
                juego lo sabe | 100 ms | uno a la vez | ~8/min
```

Sin especificar: *"que el salto se sienta bien"*.

---

## Fuentes

- `02_Game_feel` (Fundamentos) — las tres capas, los seis componentes y la tabla de efectos.
- `05_Game_Feel` (Fuentes) — metáfora y reglas como componentes del feel.
- `04_Proyecto_editable_en_Unity` (Construcción) — un valor en un solo lugar, editable sin código.
- `Baseline de entregable` (Core) — el juice como table-stake de un juego terminado.

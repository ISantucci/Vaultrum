## Definición

Una malla poligonal es un conjunto de **vértices** (puntos en el espacio), **aristas** (segmentos entre dos vértices) y **caras** (polígonos cerrados por aristas).

```txt
vertice   un punto, con posicion y atributos
arista    dos vertices unidos
cara      un poligono: triangulo (3), quad (4) o ngon (5 o mas)
isla      un conjunto de caras conectadas entre si y no con el resto
```

Todo lo demás —el modelado, el sombreado, la deformación, el costo— se apoya en estas cuatro palabras.

---

## Idea central

**La GPU solo dibuja triángulos.** Quads y ngons son una comodidad de quien modela; al exportar, o al llegar al motor, todo se triangula.

```txt
modelar en quads    porque el flujo de aristas se lee, se subdivide limpio y se deforma bien
entregar en tris    porque es lo que el motor va a dibujar de todos modos
ngons               solo en superficies planas que no se deforman ni se subdividen
```

Y un vértice no es solo una posición. Viaja con **atributos**:

```txt
normal          hacia donde mira, para el sombreado
UV              donde cae en la textura
color           color por vertice, si lo hay
pesos           a que huesos sigue, si se deforma (skinning)
```

Cuando dos caras vecinas necesitan valores distintos de un atributo en el mismo punto —una arista dura, una costura de UV—, el motor **parte el vértice en dos**. Por eso el número de vértices que cuesta en el motor casi nunca coincide con el que muestra el programa de modelado. El precio está en `Vertices partidos`, en la rama Arte de Optimización.

---

## Las islas

Un objeto puede tener varias islas: un personaje con ojos separados, un árbol con hojas sueltas, una torre con piezas apoyadas.

Importa por dos razones:

```txt
el bbox miente     la caja que envuelve varias islas no dice nada del espesor de ninguna.
                   Es la trampa declarada de la ley 2 del Area de Arte: se lee espesor_eq_mm,
                   no la clase macizo / cascara
las islas sueltas  una pieza que flota separada del cuerpo es un apoyo sin verificar:
                   el accesorio se apoya MIDIENDO (RA-009)
```

---

## Cómo se juzga

```txt
se mide     caras, vertices, triangulos, islas, ngons: todo es conteo, por script
se juzga    si cada isla tiene que ser una isla, o es una pieza que tendria que estar unida
```

El conteo de caras de un asset no es su costo: el costo depende de cuántas veces aparece en pantalla (`Caras en pantalla`).

---

## Errores comunes

```txt
Entregar ngons en zonas que se deforman: se triangulan distinto en cada motor.
Leer el conteo de vertices del DCC como si fuera el del motor.
Tratar un objeto de muchas islas como una pieza al medir espesor.
Unir islas que tienen que moverse por separado (o separar lo que es una pieza).
```

---

## Fuentes

- `65_Digital_Modeling` — vocabulario y flujo de la malla poligonal.
- `71_Blender_Manual` — la referencia de la herramienta.
- `RA-002_Estandar_de_malla`, `RA-006_Relleno_y_espesor` y `RA-009_Personaje_y_accesorios`, del Área de Arte: de dónde salieron las trampas de esta nota.

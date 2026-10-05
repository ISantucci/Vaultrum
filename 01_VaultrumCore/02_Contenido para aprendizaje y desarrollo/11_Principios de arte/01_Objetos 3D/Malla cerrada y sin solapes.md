## Definición

Una malla está **cerrada** (manifold, estanca) cuando cada arista pertenece exactamente a dos caras: no hay bordes abiertos, ni aristas compartidas por tres caras, ni vértices que unen dos volúmenes por un punto.

Dos piezas **se solapan** cuando una atraviesa a la otra: comparten volumen.

---

## Idea central

```txt
abierta        hay un borde con una sola cara: un agujero, aunque no se vea
no-manifold    una arista con tres caras, o dos volumenes tocandose por un vertice
solape         dos piezas ocupan el mismo espacio
```

Importa por lo que deja medir:

```txt
volumen y espesor     solo existen sobre una malla cerrada. Sin cierre no hay
                      "adentro", y la ley 2 del Area de Arte no se puede medir
normales              "hacia afuera" no esta definido en una malla abierta
booleanas, horneado,  fallan o producen basura sobre mallas abiertas
impresion 3D
```

Y el solape importa aunque no se vea: dos agujas hundidas 109 y 113 mm en una roca **se veían perfectas**. Lo encontraron 192 raycasts. Un solape esconde geometría que se paga y no se ve, produce parpadeo de profundidad donde las superficies coinciden, y dice que la colocación no se verificó.

---

## Macizo y cáscara

```txt
macizo     cerrado, con volumen: el default del area
cascara    una superficie sin espesor: un plano de hoja, una tarjeta de pelo, una bandera
```

La cáscara **se justifica**, no se presume (`RA-006`). Una hoja de árbol es un plano y está bien; un muro hecho de un plano no.

---

## Cómo se juzga

```txt
se mide     aristas con distinto de dos caras (borde abierto o no-manifold), solapes
            reales con BVHTree.overlap, espesor equivalente 2V/A: todo en arte.malla(),
            leyes 1 y 2. Y se mide DESPUES de emparentar (RA-008.5)
se juzga    si una cascara esta justificada
```

---

## Errores comunes

```txt
Verificar las piezas sueltas y no el asset armado: la colocacion no se probo.
Leer la clase macizo / cascara en vez del espesor en milimetros.
Cerrar un agujero con una cara que no se ve "porque total no se ve".
Dejar que un accesorio atraviese el cuerpo porque en la pose de presentacion no se nota:
en la animacion se va a notar.
```

---

## Fuentes

- `65_Digital_Modeling` — mallas estancas y topología limpia.
- Área de Arte: leyes 1 y 2, `RA-002_Estandar_de_malla`, `RA-006_Relleno_y_espesor`, `RA-008_Origen_y_verificacion`. Los casos de esta nota son suyos.

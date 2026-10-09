## Propósito

Esta subsección reúne lo que un objeto 3D **es** antes de ser un asset: de qué está hecha una malla, hacia dónde mira cada cara, qué significa que esté cerrada, y qué transform, origen y unidades trae.

No existe para enseñar a modelar: eso es `Modelado`.
No existe para repetir el contrato del asset del Área de Arte: lo explica.

Existe porque el contrato dice **qué** exigirle a un asset —metros, transform aplicada, origen por función, mira a +Y— y nadie decía **por qué**. Sin el porqué, una excepción parece razonable y se cuela.

---

## Idea central

```txt
la malla se VE con el sombreado
el motor la LEE con los datos

una malla puede verse perfecta y tener los datos rotos:
normales al reves, bordes abiertos, escala sin aplicar, origen en otro lado
```

Los cuatro defectos invisibles que fundaron el Área de Arte —la torre corrida, las agujas hundidas, la flecha en dos marcos de coordenadas, los tirantes dentro del torso— eran todos de esta subsección. Ninguno se veía.

---

## [[Anatomia de una malla]]

Vértices, aristas, caras, triángulos, quads y ngons, islas, y los atributos que viajan con cada vértice. Es el vocabulario que el resto de la sección da por sabido.

---

## [[Normales y orientacion de caras]]

Hacia dónde mira cada cara y por qué una cara invertida no es un detalle: el motor la descarta o la sombrea al revés. Incluye la diferencia entre la normal de cara y la normal de vértice, que es la que decide el sombreado.

---

## [[Malla cerrada y sin solapes]]

Qué es una malla cerrada, por qué el volumen y el espesor solo se pueden medir sobre una, y por qué dos piezas que se atraviesan son un defecto aunque nadie las vea.

---

## [[Transform origen y unidades]]

Escala y rotación aplicadas, el origen según la función, las unidades y los ejes de cada motor. Es la mitad del contrato del asset que se rompe al exportar.

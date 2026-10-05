# Legibilidad

## Qué hace Vaultrum acá

Mide si algo se **lee**: si se reconoce por su silueta, si se separa del fondo por valor, si dos familias se siguen distinguiendo con daltonismo, al tamaño real en pantalla.

El principio vive en el Core —`Silueta legible`, `Valor antes que tono`, `Color que distingue`— y la decisión de cuántas señales entran es de UI/UX. Esta nota es el **procedimiento**: cómo lo mide la IA con las herramientas que tiene.

## Con qué opera la IA

```txt
silueta          render del asset en un solo color plano sobre fondo blanco, desde la
                 camara de juego, a la resolucion que ocupa en pantalla. En Blender,
                 Workbench con color unico; en 2D, el canal alfa del sprite es la mascara
superposicion    dos siluetas como mascaras, alineadas: que fraccion comparten. Cuanto
                 mas comparten, mas se confunden. Es un script corto sobre dos imagenes
valor            la imagen pasada a luminancia; el contraste entre figura y fondo REAL
daltonismo       simulacion de protanopia, deuteranopia y tritanopia: arte.paleta() lo
                 hace sobre la paleta
tamano real      todo lo anterior a la escala de pantalla: un asset que ocupa 60 px se
                 prueba a 60 px, no a pantalla completa
```

**Hueco declarado.** `arte.paleta()` mide valor y daltonismo sobre la paleta. La superposición de siluetas todavía no es parte de ningún instrumento: la IA la corre como script suelto. Si se repite en dos proyectos, pasa al instrumento del área.

## Cómo pedírselo

```txt
"Medi la legibilidad de <familias> sobre <nivel o fondo>, a <tamano en pantalla>,
 desde la camara de juego."
```

## Qué devuelve

```txt
la silueta de cada familia, y la superposicion entre cada par
el contraste de valor de cada familia contra el fondo real
las familias que colapsan en alguna forma de daltonismo
y lo que queda como juicio: si la silueta dice lo que tiene que decir
```

No hay un umbral universal de superposición: se compara contra las otras familias del mismo juego.

## Lo que no hace

No decide cuántas familias hay ni por qué canal se distinguen: eso es UI/UX. No corrige el asset: reporta, y corrige el área.

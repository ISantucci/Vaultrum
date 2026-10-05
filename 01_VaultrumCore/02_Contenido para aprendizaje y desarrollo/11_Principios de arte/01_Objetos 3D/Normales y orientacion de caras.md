## Definición

La **normal** de una cara es el vector perpendicular que dice hacia dónde mira. Una cara tiene frente y dorso, y el frente lo define el orden de sus vértices.

```txt
normal de cara      hacia donde mira el poligono: decide que lado es el frente
normal de vertice   promedio (o no) de las caras vecinas: decide como se sombrea
```

Son dos cosas, y se rompen por separado.

---

## Idea central

**Una cara invertida no es un detalle de prolijidad: es un error de datos que el motor ejecuta.**

```txt
backface culling    el motor no dibuja el dorso de las caras, para ahorrar.
                    Una cara invertida desaparece: se ve un agujero
iluminacion         la luz se calcula con la normal. Invertida, la cara se sombrea
                    como si mirara para adentro: oscura donde tendria que haber luz
volumen             el volumen con signo de una malla cerrada sale NEGATIVO si toda la
                    malla mira adentro. Unas pocas caras invertidas no lo dan vuelta:
                    solo lo achican. Mirar el total no alcanza para encontrarlas
```

Por eso es **corrección y no optimización**: un asset con normales invertidas está mal, no caro. Se arregla recalculando las normales hacia afuera, no prendiendo el dibujado de dos caras.

---

## Normales de vértice: suave y duro

La normal de vértice decide el sombreado:

```txt
suave (smooth)    las caras vecinas comparten la normal del vertice: la superficie se
                  ve curva aunque sea facetada
duro (flat /      cada cara tiene su normal en ese vertice: el borde se ve como arista
arista marcada)   viva. Es lo que hace leer un bisel o una esquina de maquina
```

Una arista dura obliga al motor a **partir el vértice**: dos normales distintas en el mismo punto son dos vértices. Un low poly facetado entero multiplica los vértices que la GPU procesa: cerca de cuatro veces en una malla de quads y de seis en una de triángulos, antes de sumar las costuras de UV. No es un error, es un precio: está en `Vertices partidos`.

---

## Cómo se juzga

```txt
se mide     la orientacion es un dato de la malla: se mide, no se mira. En conjunto
            (toda la malla adentro) y cara por cara (una cara al reves contra sus
            vecinas): hacen falta las dos. Como lo hace la IA con la herramienta, y que
            no ve el instrumento del area, esta en IA Operativa: Blender por MCP
            el overlay de orientacion de caras del DCC (frente azul, dorso rojo en
            Blender) es un control visual, no una medicion
se juzga    donde va una arista dura y donde una suave: es lectura de la forma
```

---

## Errores comunes

```txt
Arreglar un agujero con material de dos caras: oculta el error y duplica el costo
de fragmentos de esa malla.
Aplicar u hornear una escala negativa sin recalcular: invierte el sentido de las caras. Muchos visores y motores compensan la escala negativa al dibujar, y el defecto aparece recién en el archivo exportado.
Recalcular normales "hacia afuera" en una malla abierta: no hay afuera definido.
Marcar todas las aristas duras para "que se vea low poly" sin mirar el costo.
Confiar en la vista del DCC: el visor puede tener backface culling apagado.
```

---

## Ejemplo

Una roca del kit de terreno se ve bien en Blender y aparece con un hueco negro en el motor. No es la textura ni la luz: tres caras quedaron invertidas al unir dos piezas. Mirar el total no la encuentra: tres caras de cientos apenas cambian el volumen. La encuentra una prueba cara por cara; recalcular normales lo corrige sin tocar geometría.

---

## Fuentes

- `71_Blender_Manual` — el overlay de orientación de caras y el recálculo de normales.
- `65_Digital_Modeling` — normales y sombreado.
- Área de Arte: ley 1, *todo mira afuera*.

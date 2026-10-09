## Definición

El **valor** es cuán claro u oscuro es un color, independiente de su tono. Un rojo y un verde pueden tener el mismo valor; pasados a gris, son el mismo gris.

```txt
tono        rojo, verde, azul: el nombre del color
saturacion  cuan puro o cuan apagado
valor       cuan claro o cuan oscuro: lo unico que sobrevive en gris
```

---

## Idea central

**La lectura la lleva el valor.** Lo que separa una figura del fondo, un enemigo del piso o un peligro del paisaje es el contraste de valor. El tono le da sentido a lo que ya se separó.

```txt
si se lee en gris, se lee
si no se lee en gris, el tono no lo salva: lo salva menos gente
```

Es por qué el Área de Arte mide la paleta **en gris**: no por accesibilidad solamente, sino porque el gris es la prueba de lectura que no depende de nadie.

---

## Especificación para videojuegos

```txt
lo jugable contrasta     lo que el jugador tiene que ver —el, los enemigos, lo que se
                         agarra, lo que mata— tiene contraste de valor con su fondo.
                         Lo decorativo, menos
el fondo cede            en una escena cargada, el fondo baja su rango de valores para
                         que la figura tenga donde destacar
un valor, una funcion    si el peligro es oscuro en un nivel y claro en otro, el jugador
                         tiene que reaprender
```

---

## Cómo se juzga

```txt
se mide     convertir a gris (luminancia) y medir la diferencia entre figura y fondo,
            y entre familias: arte.paleta() hace el censo y la distancia; para texto, el
            contraste WCAG de UI/UX
se juzga    si la jerarquia de valores es la que pide el juego
```

---

## Errores comunes

```txt
Distinguir dos cosas solo por tono con el mismo valor.
Aprobar una paleta en color sin pasarla a gris.
Un fondo con todo el rango de valores: la figura no tiene donde destacar.
```

---

## Fuentes

- `62_Color_and_Light` — valor, y la separación de luz y color.
- `63_Interaction_of_Color` — por qué el valor engaña según el vecino.
- Área de Arte: ley 5, `arte.paleta()` y `05_Flujo_Coherencia`.

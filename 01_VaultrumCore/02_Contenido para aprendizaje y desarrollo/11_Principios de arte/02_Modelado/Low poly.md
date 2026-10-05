## Definición

*Low poly* nombra dos cosas que se confunden:

```txt
un ESTILO        facetado visible, formas simples, color plano o por cara,
                 sin textura de detalle
un PRESUPUESTO   pocas caras para lo que el asset tiene que mostrar,
                 por limite de plataforma o de cantidad en pantalla
```

Un asset puede ser una sin la otra. Un personaje de 3.000 caras con textura realista puede ser de presupuesto bajo —según la plataforma y cuántos haya en pantalla— y no tener estilo low poly. Un árbol facetado de 800 caras con flat shading es estilo low poly y puede ser caro si hay cuatrocientos.

---

## Idea central

**Las caras se gastan en la silueta.**

```txt
la silueta     es lo que el jugador lee, y lo unico que una cara mas siempre mejora
el interior    de una superficie casi plana, una cara mas no se ve: se ve el sombreado
```

Por eso el low poly bien hecho no es "menos caras en todos lados": es **todas las caras donde cambia el contorno**, y casi ninguna adentro.

---

## Lo que el estilo cuesta y no se ve

El facetado se hace con aristas duras: cada cara tiene su propia normal. Eso **parte los vértices**: en el motor, un low poly facetado puede tener varias veces los vértices que muestra el DCC. El precio está en `Vertices partidos`. No es un motivo para no usar el estilo; es un número que hay que conocer.

Y el estilo tiene un riesgo de lectura: con poca forma y color plano, dos familias se parecen más fácil. La paleta y la silueta tienen que hacer el trabajo que el detalle no hace.

---

## Cómo se juzga

```txt
se mide     caras del asset, y caras EN PANTALLA: caras por instancias maximas
            simultaneas (arte.presupuesto(), ley 4). 817 caras no dicen nada;
            817 x 20 goblins = 16.340 caras en pantalla, si
se juzga    si la silueta lee con esas caras, a la distancia de juego
```

---

## Errores comunes

```txt
Reducir caras parejo en todo el asset en vez de en el interior.
Llamar "low poly" a un asset que es solo barato, o "barato" a uno que es solo low poly.
Olvidar los vertices partidos del facetado al calcular el costo.
Dar por bueno el conteo del asset sin multiplicar por las instancias.
```

---

## Fuentes

- `65_Digital_Modeling` — densidad y silueta.
- Área de Arte: ley 4 (`arte.presupuesto()`), `RA-002_Estandar_de_malla`, y el goblin de TowerDefense.

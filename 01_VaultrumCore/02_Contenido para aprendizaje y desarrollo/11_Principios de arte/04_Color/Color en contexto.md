## Definición

Un color no se ve igual en todos lados: **se ve según lo que tiene al lado y bajo qué luz**. Es la idea central de Albers: el mismo color parece dos colores distintos sobre dos fondos distintos.

---

## Idea central

```txt
la muestra suelta miente     un color aprobado sobre blanco puede desaparecer sobre el
                             fondo donde va a vivir
la luz cambia el color       una escena calida tine todo de calido; el color local del
                             objeto y el color que se ve no son el mismo
```

---

## Especificación para videojuegos

```txt
se aprueba sobre el fondo real   el asset, sobre el terreno del nivel; la UI, sobre la
                                 pantalla donde aparece. El tutorial WASD se iba a usar
                                 sobre violeta: la tecla activa se eligio turquesa oscuro
                                 CONTRA ese violeta, no contra una muestra (RA-012)
se aprueba con la luz real       la luz del nivel, el ciclo dia y noche si lo hay, el
                                 post-proceso
un fondo, varios contextos       si el asset aparece en tres niveles, se prueba en los tres
```

---

## Cómo se juzga

```txt
se mide     contraste de valor y distancia de color del asset CONTRA el fondo real, no
            contra blanco (arte.paleta() mira el conjunto y el terreno)
se juzga    si el color dice lo que tiene que decir en ese lugar
```

---

## Errores comunes

```txt
Aprobar en el visor del DCC, con fondo gris neutro.
Aprobar la UI sobre blanco y usarla sobre un fondo de color.
Olvidar el post-proceso, que corre todos los colores al final.
```

---

## Fuentes

- `63_Interaction_of_Color` — el color relativo.
- `62_Color_and_Light` — color local y color de la luz.
- `RA-012_Secuencia_alfa_y_entrega_de_animacion` — el tutorial sobre violeta.
